#!/usr/bin/env python3
"""Expand the non-CORE/NEXT paper notes without fabricating full-text evidence.

The registry contains 190 CORE/NEXT papers with curated formulation profiles
and 682 remaining papers whose notes previously stopped at a common scaffold.
This script gives the remaining notes the same analysis surface as the
intensive notes: domain-specific scope, formulation bridge, module pipeline,
interface variables, evaluation matrix, fairness checks, and reproduction
questions.

The source boundary is deliberate.  It reads the current overview, the
current notes, and (when available) the tracked pre-migration note from HEAD.
The latter preserves useful legacy extraction cues after the scaffold
migration.  It does not download PDFs, promote reading status, or turn a cue
into a verified claim.  Run without ``--apply`` for a dry run.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import subprocess
from collections import Counter
from pathlib import Path
from typing import Any

try:
    from migrate_method_notes import DOMAIN_VARIABLES, runtime_contract
    from migrate_problem_notes import DOMAIN_SCOPE
except ModuleNotFoundError:  # pragma: no cover - package/importlib fallback
    from .migrate_method_notes import DOMAIN_VARIABLES, runtime_contract
    from .migrate_problem_notes import DOMAIN_SCOPE


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "work" / "sources" / "papers.json"
TIERS = ROOT / "research" / "READING_TIERS.csv"

VALID_EVIDENCE = {
    "CURATION_ONLY",
    "ABSTRACT_CHECKED",
    "FULL_TEXT_CHECKED",
    "EXPERIMENT_CHECKED",
}

COMMON_PROBLEM_HEADINGS = (
    "## Problem in One Sentence",
    "## System and Scope",
    "## Formal Problem Formulation",
    "## Bottleneck in Prior Work",
    "## What the Paper Changes",
    "## Assumptions and Failure Boundary",
    "## Position in the Robotics Loop",
    "## Verification Questions",
)

COMMON_METHOD_HEADINGS = (
    "## Method in One Sentence",
    "## Design Rationale",
    "## Source Evidence Cues",
    "## Pipeline",
    "## Objective / Update Rule",
    "## Variables and Parameters",
    "## Observation–State–Action Interface",
    "## Temporal and Runtime Contract",
    "## Training vs Inference",
    "## Method-Specific Formal Details",
    "## Evaluation Link",
    "## Failure and Ablation Link",
    "## Reproduction Checklist",
    "## Verification Questions",
)

COMMON_EVAL_HEADINGS = (
    "## Evaluation in One Sentence",
    "## Evaluation Type and Scope",
    "## Experimental Matrix",
    "## Dataset / Benchmark Role",
    "## Embodiment / Environment",
    "## Metrics and Success Definition",
    "## Baselines and Fairness",
    "## Ablations and Sensitivity",
    "## Main Results / Claim–Evidence Map",
    "## Generalization and Failure Cases",
    "## Statistics, Efficiency, and Reproducibility",
    "## Limitations and Verification Questions",
)


# The registry's canonical seven tracks are intentionally translated into a
# smaller note-domain vocabulary.  The domain is a note-writing aid, not a
# second taxonomy or a tier decision.
TRACK_TO_DOMAIN = {
    "Planning and control": "planning",
    "RL, IL, offline learning, and robot data": "rl",
    "Manipulation, contact, tactile, and dexterity": "manipulation",
    "VLA and generalist robot policies": "vla",
    "World models, safety, uncertainty, and recovery": "world_model",
    "Locomotion, whole-body, mobile manipulation, and humanoids": "locomotion",
    "Robotics-enabling 3D perception": "3d_perception",
}


UPSTREAM_SCOPE = (
    "paper-specific non-robotics upstream data/task domain",
    "source-defined image, text, sequence, or multimodal input",
    "learned representation, latent variable, or prediction state",
    "prediction, embedding, generated sample, or task cue",
    "source-defined quality metric; direct closed-loop robot utility is not established in this note",
)


DOMAIN_MODULES: dict[str, list[tuple[str, str, str, str, str, str]]] = {
    "planning": [
        ("Problem / state representation", "decision state와 feasible set을 만든다", "state, map, goal, constraints", "source-specific graph, symbolic state, belief 또는 configuration representation을 구성", "search/optimization state", "task and motion decision이 소비할 수 있는 상태를 노출"),
        ("Search / trajectory decision", "goal을 향한 candidate를 생성·개선한다", "state와 cost/heuristic", "search, sampling, dynamic programming 또는 trajectory optimization을 적용", "plan, path, option 또는 trajectory", "cost와 feasibility를 함께 비교"),
        ("Execution interface", "계획을 실행 가능한 command로 변환한다", "plan과 current feedback", "collision/contact/dynamics check, smoothing, replanning 또는 controller handoff를 수행", "waypoint, option, action 또는 reference", "planner–controller 경계를 확인"),
    ],
    "control": [
        ("Task / error representation", "motion·force 목표를 제어 error로 바꾼다", "joint/task state, reference, wrench", "task frame, Jacobian, impedance, selection 또는 error coordinates를 구성", "desired task command", "contact-relevant target을 명시"),
        ("Dynamics / constraint solve", "목표를 feasible actuator command로 바꾼다", "error, model, constraints", "inverse dynamics, QP, MPC, operational mapping 또는 feedback law를 계산", "torque, force, velocity 또는 position command", "actuator/contact constraint를 반영"),
        ("Feedback / actuation", "실제 state와 disturbance에 따라 command를 닫힌 loop로 보정한다", "sensor feedback과 nominal command", "tracking correction, saturation, null-space, fallback 또는 replan을 수행", "next actuation과 response", "model error와 contact failure 경계를 드러냄"),
    ],
    "estimation": [
        ("State / observation model", "latent robot/world state와 measurement 관계를 표현한다", "prior state와 sensor observation", "transition, observation, uncertainty 또는 learned encoder를 구성", "state/uncertainty representation", "planner/controller가 사용할 state interface를 만든다"),
        ("Prediction / fusion", "새 시점의 prior 또는 fused state를 계산한다", "history, model, multi-sensor input", "recursive prediction, registration, fusion 또는 temporal aggregation을 수행", "prior/fused state", "partial observation을 압축"),
        ("Correction / downstream handoff", "measurement feedback으로 state를 보정하고 전달한다", "prior와 current observation", "innovation, refinement, confidence update 또는 query를 수행", "posterior/map/task cue", "feedback이 decision loop에 들어감"),
    ],
    "rl": [
        ("Policy / value representation", "state에서 action과 return estimate를 표현한다", "state/observation과 task context", "actor, critic, value, Q 또는 sequence policy를 계산", "policy/value estimate", "decision interface와 learning signal을 연결"),
        ("Rollout / target construction", "interaction에서 update target을 만든다", "state, action, reward, next state", "return, advantage, TD target 또는 trajectory statistics를 구성", "training target", "credit assignment와 data use를 고정"),
        ("Policy / value update", "목표를 최적화해 다음 policy를 만든다", "target, replay/data와 parameters", "gradient, trust region, entropy, replay 또는 constraint update를 수행", "updated policy/controller", "stability·exploration·sample efficiency를 비교"),
    ],
    "offline_rl": [
        ("Fixed-data support", "온라인 탐색 없이 transition/action 분포를 정의한다", "offline trajectories와 metadata", "dataset support, behavior distribution과 task return을 정리", "training batch/support", "OOD action boundary를 명시"),
        ("Value / uncertainty update", "dataset 밖 action의 과대추정을 억제한다", "batch transition과 value parameters", "conservative, implicit, uncertainty 또는 behavior-regularized update를 수행", "Q/V/uncertainty estimate", "extrapolation error를 통제"),
        ("Policy extraction / deployment", "학습된 value를 실행 action으로 변환한다", "value와 behavior support", "argmax, advantage weighting, sequence decoding 또는 constraint filtering을 적용", "dataset-supported action", "closed-loop deployment gap을 평가"),
    ],
    "il": [
        ("Demonstration representation", "expert trajectory를 training pair/context로 정렬한다", "observation history, goal, expert action", "temporal alignment, relabeling 또는 latent context construction을 수행", "training sample/context", "demonstration coverage를 명시"),
        ("Policy fitting", "expert action distribution을 학습한다", "context와 action target", "behavior cloning, adversarial, sequence, diffusion 또는 flow objective를 최적화", "policy/action distribution", "multimodality와 compounding error를 결정"),
        ("Closed-loop rollout", "distribution shift와 recovery를 확인한다", "current observation/history", "action/chunk을 실행하고 feedback으로 다음 prediction을 갱신", "trajectory/failure signal", "offline imitation을 실제 control과 연결"),
    ],
    "robot_data": [
        ("Data schema / normalization", "heterogeneous robot trajectory를 공통 sample로 만든다", "observation, action, task와 embodiment metadata", "sensor/action schema alignment, filtering, normalization을 수행", "shared dataset representation", "cross-robot 비교 가능성을 만든다"),
        ("Coverage / augmentation", "task·embodiment·failure variation을 확장한다", "dataset과 metadata", "retargeting, relabeling, synthetic/teleoperation augmentation 또는 sampling을 적용", "expanded data support", "generalization claim의 실제 범위를 결정"),
        ("Downstream learning interface", "정규화된 data를 policy/representation이 사용한다", "shared observations/actions", "pretraining, BC, action-token 또는 representation learning을 수행", "checkpoint/policy action", "data effect와 model effect를 분리"),
    ],
    "vla": [
        ("Multimodal task encoding", "vision·language·proprioception·3D context를 결합한다", "image/video, instruction, state/history", "pretrained encoder, adapter, attention, grounding 또는 fusion을 적용", "task-conditioned context", "semantic prior와 robot state를 같은 interface로 연결"),
        ("Action / skill decoding", "context에서 continuous action 또는 skill을 생성한다", "context와 history", "autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용", "action, pose, option 또는 action chunk", "action representation의 temporal/multimodal choice를 드러냄"),
        ("Receding execution / feedback", "예측을 부분 실행하고 다시 관측한다", "action chunk와 current observation", "execute, replan, terminate, recover 또는 memory update를 수행", "next action/feedback state", "long-horizon과 contact robustness를 평가"),
    ],
    "world_model": [
        ("Observation / latent state", "raw observation을 decision-relevant latent로 압축한다", "image, proprioception, tactile와 history", "encoder, belief inference, scene representation 또는 memory update를 수행", "latent state", "partial observability를 관리"),
        ("Action-conditioned prediction", "행동 후 미래를 예측한다", "latent state와 candidate action", "learned dynamics, video/state prediction, reward 또는 uncertainty rollout을 수행", "future latent/observation/reward", "counterfactual planning을 지원"),
        ("Planner / policy interface", "예측을 행동 선택으로 연결한다", "imagined future와 task objective", "candidate evaluation, model-predictive selection, policy update 또는 uncertainty filter를 수행", "action/option sequence", "model error가 closed-loop failure로 전파되는 경로를 확인"),
    ],
    "safety": [
        ("Risk / failure representation", "unsafe state와 uncertainty를 계산한다", "observation, nominal command, history", "barrier, risk model, failure classifier, uncertainty 또는 safe set을 추정", "risk/margin/failure state", "runtime intervention interface를 만든다"),
        ("Filtering / recovery", "nominal command를 안전 command로 바꾼다", "nominal action과 safety constraint", "QP shield, backup policy, correction, stop 또는 recovery plan을 선택", "safe/recovery action", "task utility와 violation을 동시에 비교"),
        ("Monitoring / re-entry", "실행 결과를 다시 risk decision에 반영한다", "executed action과 next observation", "threshold, update, replan, abort 또는 return-to-task를 수행", "continue/correct/abort state", "false positive·negative와 recovery latency를 드러냄"),
    ],
    "simulation": [
        ("Physics state / interface", "robot·environment state를 simulator contract로 표현한다", "geometry, dynamics, contact, control input", "rigid-body/contact/differentiable state를 구성", "simulator state", "rollout과 controller의 공통 interface를 만든다"),
        ("Rollout / model query", "candidate action의 consequence를 계산한다", "state와 action", "physics step, learned dynamics, parallel 또는 differentiable rollout을 수행", "trajectory/reward/prediction", "planning·learning data를 만든다"),
        ("Learning / transfer handoff", "simulation result를 policy 또는 real deployment로 전달한다", "rollout과 task objective", "gradient, replay, randomization, calibration 또는 transfer adaptation을 적용", "policy/controller/data", "simulator bias와 transfer gap을 평가"),
    ],
    "3d_perception": [
        ("Geometry / pose extraction", "image·depth·point input에서 spatial state를 만든다", "RGB/RGB-D, point cloud, camera pose 또는 multi-view input", "depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정", "geometry/map/pose", "metric relation과 occlusion을 downstream에 노출"),
        ("Semantic / temporal fusion", "geometry에 semantics와 history를 정렬한다", "geometry, visual/language feature와 temporal context", "feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행", "queryable 3D state", "open-vocabulary/task context와 spatial state를 연결"),
        ("Robot query / planning handoff", "3D state를 task decision에 전달한다", "map/feature와 task query", "target grounding, affordance, collision/free-space 또는 action cue를 생성", "goal, pose, path 또는 policy input", "perception metric과 robot behavior의 연결을 검증"),
    ],
    "navigation": [
        ("Map / localization state", "sensor stream을 pose와 world map으로 누적한다", "camera/depth/LiDAR, odometry, history", "mapping, localization, scene graph 또는 map update를 수행", "pose/map/free-space state", "navigation memory를 구성"),
        ("Global / local decision", "goal과 risk를 고려해 route를 정한다", "map, goal, obstacle/risk estimate", "graph search, local planning, language grounding 또는 replanning을 수행", "path/waypoint/local goal", "geometry·semantics·safety를 함께 비교"),
        ("Motion execution / recovery", "route를 velocity/action으로 실행하고 실패에 대응한다", "path와 current pose/feedback", "tracking, collision check, recovery 또는 replan을 수행", "velocity/base command", "drift, latency, dynamic obstacle 경계를 확인"),
    ],
    "mobile_manipulation": [
        ("Scene / interaction state", "base·arm·object 관계를 표현한다", "egocentric RGB-D, language goal, proprioception", "map, object, reachability, contact 또는 affordance state를 구성", "base-arm interaction state", "navigation과 manipulation의 shared state를 만든다"),
        ("Base-arm task decision", "접근·도킹·grasp·manipulation sequence를 결정한다", "interaction state와 task instruction", "keypoint, option, trajectory, grasp 또는 joint planning을 수행", "base path plus arm/gripper plan", "reachability·collision·contact constraints를 노출"),
        ("Execution / correction", "부분 실행 후 observation으로 계획을 수정한다", "current pose, visual/force feedback", "tracking, regrasp, docking correction, recovery 또는 replan을 수행", "next mobile-manipulation action", "long-horizon failure recovery를 평가"),
    ],
    "manipulation": [
        ("Geometry / affordance state", "object와 contact-relevant scene을 표현한다", "RGB-D, point cloud, object/task observation", "pose, affordance, grasp/contact graph 또는 SE(3) descriptor를 구성", "object/contact state", "visual state가 action space를 제한"),
        ("Grasp / trajectory generation", "goal을 feasible manipulation candidate로 바꾼다", "geometry/contact state와 task goal", "grasp sampling, pose planning, trajectory optimization 또는 policy decoding을 적용", "grasp, pose, force 또는 trajectory", "kinematic/contact feasibility를 비교"),
        ("Contact execution / correction", "interaction outcome으로 action을 닫힌 loop로 수정한다", "candidate와 visual/force/tactile feedback", "tracking, regrasp, correction, termination 또는 recovery를 수행", "next action/task state", "open-loop contact failure를 드러냄"),
    ],
    "tactile": [
        ("Multi-modal contact encoding", "vision과 touch를 contact feature로 결합한다", "tactile image/force, vision, proprioception", "tactile encoder, calibration, fusion 또는 temporal feature extraction을 수행", "contact feature/state", "hidden geometry와 interaction cue를 보완"),
        ("Contact / dynamics inference", "contact mode와 object response를 추정한다", "contact feature와 action history", "mode classifier, force/dynamics model 또는 state estimator를 update", "contact/force prediction", "다음 action uncertainty를 줄임"),
        ("Force-aware action correction", "interaction feedback으로 command를 보정한다", "predicted contact와 current wrench/touch", "policy/control law가 action, force 또는 grasp를 재계산", "contact-safe action/torque", "slip·damage·failure recovery를 평가"),
    ],
    "locomotion": [
        ("Command / terrain state", "body state와 terrain/task context를 표현한다", "proprioception, terrain/perception, velocity command", "history encoder, reference, terrain latent 또는 behavior mode를 구성", "locomotion context", "gait와 adaptation을 조건화"),
        ("Whole-body policy / controller", "context에서 joint target 또는 torque를 만든다", "context, body state, contact", "RL policy, reference tracking, inverse dynamics 또는 whole-body control을 적용", "joint action/torque", "balance·contact·actuator constraint를 반영"),
        ("Adaptation / recovery", "disturbance와 contact mismatch에 대응한다", "new observation/history와 failure signal", "latent adaptation, foothold change, recovery 또는 replan을 수행", "updated command", "sim-to-real과 fall boundary를 평가"),
    ],
    "humanoid": [
        ("Reference / embodiment interface", "human/task reference를 robot-compatible state로 바꾼다", "reference motion, visual/language input, body state", "retargeting, pose/skill conditioning 또는 multimodal encoding을 수행", "whole-body context", "high-DoF intent를 action interface로 축소"),
        ("Balance-aware whole-body execution", "reference를 contact·balance-aware command로 변환한다", "context, body state, contact", "policy, WBC, inverse dynamics 또는 hierarchical control을 적용", "joint target/torque", "contact/actuator constraints를 반영"),
        ("Recovery / adaptation", "mismatch·disturbance·fall 뒤 behavior를 복구한다", "feedback/history와 failure state", "adaptation, motion completion, reinitialization 또는 safe stop을 수행", "recovery command", "deployment boundary를 드러냄"),
    ],
    "benchmark": [
        ("Task / interface definition", "method 비교에 필요한 task·state·action contract를 고정한다", "environment, embodiment, task variation, split", "episode, instruction, observation/action schema와 reset rule을 정의", "benchmark episodes", "비교 가능성을 확보"),
        ("Baseline harness", "같은 protocol로 method와 baseline을 실행한다", "episode와 method interface", "baseline, ablation, seed, checkpoint와 rollout budget을 통제", "comparable trajectories/scores", "gain의 귀속을 가능하게 함"),
        ("Metric / failure reporting", "success 외에 generalization과 failure를 측정한다", "trajectory, log, task outcome", "score aggregation, failure taxonomy, efficiency와 reproducibility audit을 적용", "comparison matrix", "benchmark overfitting을 드러냄"),
    ],
    "generative": [
        ("Data / condition representation", "data와 condition을 generation state로 바꾼다", "data, text/image/task condition", "encoder, noise/path parameterization 또는 latent representation을 구성", "conditioned generation state", "분포와 condition interface를 고정"),
        ("Denoiser / vector field", "data distribution을 복원하는 방향을 학습한다", "noisy/interpolated state와 time", "score, noise, velocity, flow 또는 autoregressive objective를 optimize", "denoising/velocity prediction", "multimodality와 training stability를 결정"),
        ("Sampling / downstream interface", "learned field를 sample·action으로 변환한다", "base noise와 condition", "iterative denoising, ODE integration, decoding 또는 filtering을 수행", "sample/action/trajectory", "sampling steps와 deployment latency를 평가"),
    ],
    "vision": [
        ("Visual representation", "raw image/video를 task-relevant feature로 바꾼다", "image, video, text/task condition", "backbone, attention, equivariant 또는 self-supervised encoder를 적용", "visual feature/state", "downstream robot state의 visual part를 제공"),
        ("Pretraining / objective", "representation을 학습하고 prior를 정렬한다", "image-label/text/augmentation pair", "supervised, contrastive, masked, generative 또는 multimodal objective를 optimize", "trained representation", "invariance와 data prior를 결정"),
        ("Task / robot interface", "feature를 prediction·grounding·control cue로 전달한다", "feature와 query/task context", "head, projection, fusion, grounding 또는 policy adapter를 적용", "prediction/pose/action cue", "robot utility는 downstream evaluation에서 별도 확인"),
    ],
    "upstream": [
        ("Input representation", "source-defined input을 learnable representation으로 바꾼다", "paper-specific image/text/sequence input", "encoder, tokenization, normalization 또는 feature extraction을 수행", "latent feature/state", "upstream task interface를 고정"),
        ("Core objective / transformation", "source task의 prediction·generation 목표를 최적화한다", "representation, target/condition", "paper-specific model, loss, decoder 또는 generative process를 적용", "prediction/embedding/sample", "정확한 contribution 위치를 확인"),
        ("Downstream transfer boundary", "결과를 후속 task 또는 embodied system에 전달한다", "output와 query/task context", "task head, retrieval, grounding 또는 adapter를 적용", "task cue/representation", "직접 robot closed-loop claim은 별도 근거가 필요"),
    ],
    "general": [
        ("Input / state representation", "paper input을 decision-ready representation으로 바꾼다", "source-defined observation/input", "paper-specific encoder, transform 또는 feature extraction을 수행", "state/feature", "후속 모듈의 interface를 고정"),
        ("Core method", "representation에서 paper target을 최적화한다", "state/feature와 objective", "paper-specific algorithm/model/control law를 적용", "prediction/plan/action", "contribution이 위치하는 모듈"),
        ("Output / feedback", "결과를 downstream task 또는 environment에 연결한다", "output과 feedback/query", "execution, evaluation, refinement 또는 replan을 수행", "next output/metric", "closed-loop relevance를 확인"),
    ],
}


DOMAIN_FORMULATION: dict[str, tuple[str, str, str, str]] = {
    "planning": ("s/q", "a/ξ ∈ feasible decisions", "path/task cost or expected utility", "success/reachability and constraint satisfaction"),
    "control": ("q, q̇, x, wrench", "u/τ subject to dynamics and actuator/contact constraints", "tracking or interaction error", "stability, tracking and constraint satisfaction"),
    "estimation": ("latent state x_t and observation o_t", "estimate x̂_t and uncertainty Σ_t", "estimation error or posterior uncertainty", "calibrated state estimate for downstream control"),
    "rl": ("s_t/o_t", "a_t sampled or selected by πθ", "expected return / constrained return", "task return, success and safe execution"),
    "offline_rl": ("dataset transition (s,a,r,s′)", "dataset-supported policy action", "offline value with OOD control", "offline return and deployment safety"),
    "il": ("observation history o_{t−H:t}", "expert-like action/chunk a_{t:t+H}", "imitation or action-distribution loss", "closed-loop task success and robustness"),
    "robot_data": ("trajectory D with task/embodiment metadata", "normalized sample or downstream action", "coverage/data efficiency/transfer objective", "cross-domain transfer and task performance"),
    "vla": ("multimodal context o,l,p/history", "action, pose, option or chunk a", "policy/action modeling objective", "instruction-conditioned task success"),
    "world_model": ("latent z_t, observation o_t and action a_t", "predicted future z/o/r", "prediction or model-based decision loss", "horizon-aware prediction and closed-loop return"),
    "safety": ("state/history and risk h(s)", "filtered/recovery action u_safe", "task utility subject to safety constraint", "low violation/failure probability with useful intervention"),
    "simulation": ("sim state s_t and parameters δ", "sim action/rollout", "physics/model/planning objective", "fidelity, throughput and downstream task utility"),
    "3d_perception": ("image/point input I/P and pose", "geometry/map/query r", "geometric/semantic reconstruction or matching loss", "spatial accuracy and downstream robot utility"),
    "navigation": ("sensor/map state and goal", "path/waypoint/velocity", "path cost, risk or goal utility", "goal reach with collision-free execution"),
    "mobile_manipulation": ("base-arm-object state and language/task goal", "base plus arm/gripper action", "long-horizon task utility under reachability/contact constraints", "task completion and recovery"),
    "manipulation": ("object geometry/contact state", "grasp/pose/force/trajectory", "task/contact/pose objective", "completion, contact success and robustness"),
    "tactile": ("visual/tactile/proprioceptive contact history", "contact-aware action/force", "contact prediction/control error", "slip/contact success and safe interaction"),
    "locomotion": ("body/proprioceptive/terrain state", "joint action/torque/footstep", "return, tracking or stability objective", "progress, balance and terrain robustness"),
    "humanoid": ("whole-body pose/contact/reference state", "joint/whole-body action", "tracking/balance/task objective", "motion/task success and recovery"),
    "benchmark": ("standardized episode e and interface", "method trajectory/action", "benchmark score and failure cost", "comparable score and protocol validity"),
    "generative": ("data x₀, noisy state x_t, condition c", "sample/action x̂ or trajectory", "distribution/denoising/flow objective", "sample quality, diversity and latency"),
    "vision": ("image/video I and label/query y", "feature/prediction z/ŷ", "representation or prediction loss", "task accuracy and downstream utility"),
    "upstream": ("source-defined input o", "prediction/embedding/sample ŷ", "paper-specific objective", "source task metric; robot link not established"),
    "general": ("source-defined observation/input o", "paper-specific output/action y/a", "paper-specific objective", "source task target and closed-loop utility"),
}


DOMAIN_ASSUMPTIONS: dict[str, list[tuple[str, str, str]]] = {
    "planning": [
        ("state/goal and successor interface is available", "search or optimization needs a well-defined decision state", "state aliasing, missing geometry or invalid successors"),
        ("cost/heuristic reflects task preference", "candidate ranking depends on it", "suboptimal or unsafe path under misspecified cost"),
        ("feasibility check is sufficiently faithful", "a plan must be executable", "collision/contact/dynamics mismatch at execution"),
    ],
    "control": [
        ("state, reference and relevant feedback are observable", "feedback law needs a timely error signal", "delay, occlusion or unmeasured contact destabilizes control"),
        ("model/frame/actuator contract is usable", "mapping and constraint solve depend on it", "model error, singularity, saturation or flexible hardware"),
        ("command rate is compatible with dynamics", "closed-loop correction must arrive in time", "latency and unmodeled high-frequency contact"),
    ],
    "rl": [
        ("training distribution and reward represent the target task", "policy update optimizes the specified objective", "reward hacking or out-of-distribution state"),
        ("environment interaction/transition signal is valid", "rollout target and credit assignment depend on it", "partial observability or simulator bias"),
        ("action is feasible under deployment constraints", "policy output must be executable", "unsafe action, saturation or contact failure"),
    ],
    "offline_rl": [
        ("dataset covers decision-relevant states/actions", "value and policy cannot invent unsupported behavior reliably", "extrapolation error and brittle deployment"),
        ("behavior support can be identified or regularized", "OOD action risk must be controlled", "high-value but unsupported actions are selected"),
        ("offline metric predicts closed-loop execution", "static value can differ from real rollout", "distribution shift and compounding failure"),
    ],
    "il": [
        ("demonstrations cover relevant recovery states", "behavior cloning only observes supplied action modes", "compounding error without recovery behavior"),
        ("observation/action alignment is consistent", "supervision must refer to the same time and frame", "temporal or embodiment mismatch"),
        ("expert behavior is a suitable target", "policy inherits demonstration bias", "unsafe or task-incomplete demonstrations"),
    ],
    "robot_data": [
        ("data schema and calibration are comparable", "shared learning assumes aligned semantics", "cross-embodiment/action mismatch"),
        ("metadata describes task and embodiment coverage", "transfer claims depend on support", "hidden confounding by robot, task or source"),
        ("additional data are comparable in quality", "scale/augmentation effects need attribution", "data leakage or noisy demonstrations"),
    ],
    "vla": [
        ("language/visual grounding refers to executable task state", "semantic context must reach action selection", "plausible text but infeasible action"),
        ("action representation and control rate are compatible", "decoder output must be executed before it becomes stale", "chunk latency and contact failure"),
        ("training data cover embodiment and recovery variation", "foundation prior alone does not guarantee transfer", "unseen embodiment/object/skill"),
    ],
    "world_model": [
        ("latent state preserves decision-relevant information", "planner/policy relies on compressed state", "aliasing and incorrect future action"),
        ("prediction remains calibrated over the decision horizon", "model error compounds during rollout", "long-horizon hallucination or model exploitation"),
        ("planner can detect uncertainty/model disagreement", "imagined success must be checked by feedback", "unsafe real execution"),
    ],
    "safety": [
        ("risk/safe-set estimate covers relevant failures", "filter/recovery only protects represented hazards", "unknown failure passes the shield"),
        ("intervention latency is below hazard timescale", "late correction cannot restore safety", "fast contact or fall event"),
        ("backup/recovery action remains feasible", "safety action must execute on hardware", "recovery dead-end or repeated intervention"),
    ],
    "simulation": [
        ("simulator captures decision-relevant dynamics/contact", "rollout is used as a proxy for reality", "sim-to-real behavior gap"),
        ("randomization/parameterization spans deployment variation", "robustness depends on support", "unseen dynamics or sensor regime"),
        ("simulation step and policy/control interface are aligned", "timing affects learned behavior", "latency and discretization artifacts"),
    ],
    "3d_perception": [
        ("camera/point geometry and calibration are usable", "metric reconstruction/query depends on them", "drift, scale error and misregistration"),
        ("visible geometry/semantics are sufficient for the query", "occlusion and ambiguity limit state recovery", "wrong target or collision estimate"),
        ("perception output is consumed by a downstream task", "image metric alone may not imply robot benefit", "no behavior improvement despite better score"),
    ],
    "navigation": [
        ("map/localization remains consistent over route", "planning needs a stable frame", "drift and loop-closure error"),
        ("free-space/risk estimate is conservative enough", "route must be executable", "collision under dynamic/unknown obstacle"),
        ("replanning can react within environment dynamics", "stale route causes failure", "latency or blocked-goal dead end"),
    ],
    "mobile_manipulation": [
        ("base-arm reachability and collision model are usable", "docking and manipulation need shared geometry", "arm/base interference or unreachable contact"),
        ("object/task state remains grounded during navigation", "long-horizon decisions depend on persistence", "stale target or lost object"),
        ("local correction can recover from interaction mismatch", "open-loop plans fail at contact", "repeated docking/grasp failure"),
    ],
    "manipulation": [
        ("object geometry/affordance is sufficiently observed", "candidate grasp/trajectory depends on it", "occlusion, articulation or pose error"),
        ("contact model and gripper/actuator are compatible", "planned interaction must be feasible", "slip, collision or force overshoot"),
        ("feedback is available for correction", "contact outcome is not fully predictable", "open-loop failure and no recovery"),
    ],
    "tactile": [
        ("tactile signal is calibrated and synchronized", "fusion and force inference need consistent timing", "sensor drift or asynchronous contact"),
        ("contact observation identifies the relevant mode", "action correction depends on mode", "ambiguous surface/slip state"),
        ("force command respects hardware/object limits", "contact success cannot trade away safety", "damage or unstable grasp"),
    ],
    "locomotion": [
        ("proprioception/contact and terrain state are timely", "balance feedback is time-sensitive", "unobserved foothold or delay"),
        ("sim/model and real dynamics are sufficiently matched", "policy/controller transfers through that model", "slip, actuator saturation or fall"),
        ("recovery state/action is reachable", "disturbance need not terminate the task", "irrecoverable fall or oscillation"),
    ],
    "humanoid": [
        ("reference is retargetable to the robot embodiment", "high-DoF action must satisfy morphology", "joint limit/contact mismatch"),
        ("balance/contact constraints are represented", "whole-body execution must remain stable", "foot slip, fall or self-collision"),
        ("actuation and sensing support the required rate", "large-body dynamics leave little latency margin", "delayed correction or hardware limit"),
    ],
    "benchmark": [
        ("task, reset and interface are standardized", "scores are only comparable under the same contract", "protocol confounding"),
        ("split isolates the claimed generalization", "held-out task/scene/embodiment defines the claim", "train-test leakage"),
        ("metric captures the intended behavior", "success proxy can hide failure", "benchmark optimization without useful deployment"),
    ],
    "generative": [
        ("data/condition distribution is representative", "generation quality is distribution-dependent", "mode collapse or OOD condition"),
        ("sampling budget fits the downstream use", "iterative generation may be too slow", "stale action/sample"),
        ("quality metric correlates with task utility", "visual/sample score is not necessarily behavior quality", "high score with poor control"),
    ],
    "vision": [
        ("training labels/augmentations define the intended invariance", "representation inherits supervision bias", "domain shift and shortcut"),
        ("visual feature retains task-relevant geometry/semantics", "downstream query depends on it", "ambiguous or non-metric feature"),
        ("downstream interface is compatible", "benchmark gain must transfer through the adapter", "no robot utility despite visual gain"),
    ],
    "upstream": [
        ("source data/task definition is stable", "the objective depends on that contract", "distribution or task shift"),
        ("learned representation retains downstream-relevant information", "generic quality need not imply robotics utility", "transfer failure"),
        ("source metric is a valid proxy", "benchmark score may not capture deployment need", "unverified downstream claim"),
    ],
    "general": [
        ("source-defined input/output contract is available", "the method cannot be reproduced without it", "interface ambiguity"),
        ("paper objective matches the recorded metric", "otherwise the comparison is misaligned", "metric shortcut"),
        ("deployment/evaluation setting matches the formulation", "transfer depends on the boundary", "unseen regime failure"),
    ],
}


def parse_sections(markdown: str) -> dict[str, str]:
    sections: dict[str, list[str]] = {}
    current: str | None = None
    for line in markdown.splitlines():
        if line.startswith("## "):
            current = line[3:].strip()
            sections.setdefault(current, [])
        elif line.startswith("# ") and current is not None:
            current = None
        elif current is not None:
            sections[current].append(line)
    return {key: "\n".join(value).strip() for key, value in sections.items()}


def strip_marker(value: str) -> str:
    value = re.sub(r"^\s*(?:[-*+]\s+|\d+[.)]\s+)", "", value.strip())
    if value.startswith("|") and value.endswith("|"):
        cells = [cell.strip() for cell in value.strip("|").split("|")]
        value = " — ".join(cell for cell in cells if cell)
    return value.strip()


def clean_line(value: str, limit: int = 520) -> str:
    value = strip_marker(value)
    value = re.sub(r"\s+", " ", value).strip()
    value = value.replace("paper.pdf", "원문")
    value = re.sub(r"\s*\.\.\.\s*", " … ", value).strip()
    if len(value) > limit:
        value = value[: limit - 1].rstrip() + "…"
    return value


NOISE_PREFIXES = (
    "year/venue:",
    "category:",
    "tags:",
    "paper link:",
    "official paper:",
    "code/project:",
    "source audit:",
    "canonical metadata:",
    "evidence maturity:",
    "analysis basis:",
    "자동 추출",
    "본문 확인 필요",
    "본문 수동 확인 필요",
    "unverified",
    "정독 시",
    "source cue와 사전 구조화",
    "legacy dataset/metric keyword",
    "current note is a scaffold",
    "현재 note",
    "현재 source 범위에서 확정하지 않음",
    "object / environment:",
    "observation / input:",
    "latent state / decision variable:",
    "output / action:",
    "horizon / evaluation target:",
    "paper-specific method module",
    "paper-specific evaluation claim",
    "formulation field",
    "resource — role",
    "metric / success signal",
    "baseline / comparison cue",
    "ablation / sensitivity factor",
    "reproducibility field",
    "dimension — recorded cue",
    "evaluation type —",
    "source anchor:",
)


def useful_lines(block: str, limit: int = 8) -> list[str]:
    result: list[str] = []
    for raw in block.splitlines():
        value = clean_line(raw)
        if not value or value.startswith((">", "|---", "| ---")):
            continue
        low = value.casefold()
        if low.startswith(NOISE_PREFIXES):
            continue
        if "본문 확인 필요" in low or "확인 필요" in low and "source" not in low:
            continue
        if any(
            phrase in low
            for phrase in (
                "자동 추출에서는",
                "schema를 확정하지 않는다",
                "함께 확인해야 한다",
                "method section을 함께",
                "입력/출력 schema",
            )
        ):
            continue
        if low in {"not reported", "not found", "not applicable", "자동 추출 실패."}:
            continue
        if re.fullmatch(r"[-—: ]+", value) or low.startswith("--- —"):
            continue
        if "source status" in low or "evidence boundary" in low or "reported status / source" in low:
            continue
        if re.search(r"(?:^|\s)(?:module|purpose|input|operation|output|source)\s*\|", low):
            continue
        # Dense extracted tables are useful only after the exact table is
        # located; retaining them as prose creates false method/eval claims.
        numeric = re.findall(r"\b\d+(?:\.\d+)?\b", value)
        if len(numeric) >= 6 and ("|" in raw or len(value) < 220):
            continue
        if re.search(r"\b(?:table|figure|fig\.)\s*\d", low) and len(numeric) >= 4:
            continue
        if value not in result:
            result.append(value)
        if len(result) >= limit:
            break
    return result


def first_nonempty(sections: dict[str, str], names: tuple[str, ...]) -> str:
    for name in names:
        if sections.get(name, "").strip():
            return sections[name]
    return ""


def collect(docs: list[str], names: tuple[str, ...], limit: int = 8) -> list[str]:
    result: list[str] = []
    for document in docs:
        sections = parse_sections(document)
        for name in names:
            for value in useful_lines(sections.get(name, ""), limit):
                if value not in result:
                    result.append(value)
                if len(result) >= limit:
                    return result
    return result


def compact(values: list[str], fallback: str, limit: int = 2) -> str:
    if not values:
        return fallback
    text = " ".join(values[:limit]).strip()
    if not text.endswith((".", "다.", "?", "!", "…")):
        text += "."
    return text


def md_cell(value: Any) -> str:
    return re.sub(r"\s+", " ", str(value).replace("|", "\\|").replace("\n", " ")).strip()


def table(headers: list[str], rows: list[list[Any]]) -> str:
    lines = [
        "| " + " | ".join(md_cell(value) for value in headers) + " |",
        "|" + "|".join("---" for _ in headers) + "|",
    ]
    for row in rows:
        lines.append("| " + " | ".join(md_cell(value) for value in row) + " |")
    return "\n".join(lines)


def git_source(relative: str) -> str:
    try:
        result = subprocess.run(
            ["git", "show", f"HEAD:{relative}"],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
            encoding="utf-8",
        )
    except OSError:
        return ""
    return result.stdout if result.returncode == 0 else ""


def resolve_folder(folder_name: str) -> Path:
    direct = ROOT / folder_name
    if direct.is_dir():
        return direct
    current = ROOT
    for part in Path(folder_name).parts:
        matches = [child for child in current.iterdir() if child.name.casefold() == part.casefold()]
        if len(matches) != 1:
            raise FileNotFoundError(folder_name)
        current = matches[0]
    return current


def read_tiers() -> dict[str, dict[str, str]]:
    with TIERS.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    result: dict[str, dict[str, str]] = {}
    for row in rows:
        result[row["paper_id"]] = row
        result[row["title"]] = row
    return result


def evidence_for(item: dict[str, Any], *documents: str) -> str:
    value = str(item.get("provenance", {}).get("content_evidence", "")).strip()
    if value in VALID_EVIDENCE:
        return value
    for document in documents:
        match = re.search(r"(?im)^\s*[-*> ]*Evidence maturity:\s*`?([A-Z_]+)", document)
        if match and match.group(1) in VALID_EVIDENCE:
            return match.group(1)
    return "CURATION_ONLY"


def basis_text(evidence: str) -> str:
    if evidence == "CURATION_ONLY":
        return (
            "registry metadata/official source pointer와 기존 note의 legacy extraction cue 기반; "
            "method/formulation/evaluation exact detail은 본문 수동 확인 필요. tracker의 reading status/evidence는 변경하지 않았다."
        )
    if evidence == "ABSTRACT_CHECKED":
        return (
            "공식 abstract/proceedings/project 수준의 source cue와 기존 note의 legacy extraction cue 기반; "
            "본문의 exact formulation, experiment condition과 result table은 확인 필요. tracker의 reading status/evidence는 변경하지 않았다."
        )
    if evidence == "FULL_TEXT_CHECKED":
        return (
            "manifest에 기록된 full-text evidence와 기존 note cue를 구조화했지만, 이 일괄 확장에서 새 수식·수치·status를 승격하지 않았다. "
            "tracker의 reading status/evidence는 변경하지 않았다."
        )
    return (
        "기존 experiment cue와 manifest evidence boundary를 구조화했지만, 새 결과를 추가로 검증하지 않았다. "
        "tracker의 reading status/evidence는 변경하지 않았다."
    )


def infer_domain(item: dict[str, Any], tier_row: dict[str, str]) -> str:
    track = tier_row.get("primary_track", "")
    category = str(item.get("category", ""))
    tags = " ".join(str(tag) for tag in item.get("tags", []))
    title = str(item.get("title", ""))
    focus = " ".join((category, tags, title)).casefold()
    identity = " ".join((tags, title)).casefold()
    text = " ".join((track, focus)).casefold()

    if any(token in identity for token in ("mujoco", "physics engine", "simulator")) and any(token in identity for token in ("simulation", "physics")):
        return "simulation"
    if "benchmark" in category.casefold() or "dataset" in category.casefold() or "benchmark" in focus:
        return "benchmark"
    if "mobile manipulation" in identity or ("navigation" in identity and "manipulation" in identity):
        return "mobile_manipulation"
    if "humanoid" in identity or "whole-body" in identity or "whole body" in identity:
        return "humanoid"
    if any(token in identity for token in ("biped", "quadruped", "legged", "locomotion", "walking")):
        return "locomotion"
    if any(token in identity for token in ("tactile", "haptic", "force sensing", "force-aware", "touch")):
        return "tactile"
    if any(token in identity for token in ("navigation", "slam", "mapping", "scene graph")):
        return "navigation"
    category_low = category.casefold()
    if "vla" in category_low or "vision-language-action" in category_low:
        return "vla"
    if "embodied navigation" in category_low or "navigation and mapping" in category_low:
        return "navigation"
    if "robot learning and data" in category_low:
        if any(token in focus for token in ("offline", "batch rl", "implicit q", "conservative q")):
            return "offline_rl"
        if any(token in focus for token in ("imitation", "demonstration", "behavior cloning", "inverse reinforcement", "visual pretraining")):
            return "il"
        return "robot_data"
    if any(token in category_low for token in ("3d geometry", "3d representation", "neural scene", "3d vision", "language-grounded 3d", "autonomous 3d", "robotics-enabling 3d", "sensor fusion")):
        return "3d_perception"
    if "world model" in category_low or "safety" in category_low or "recovery" in category_low:
        if any(token in focus for token in ("safety", "safe", "barrier", "uncertainty", "recovery")):
            return "safety"
        if any(token in focus for token in ("simulation", "sim-to-real", "sim2real", "physics")):
            return "simulation"
        return "world_model"
    if "contact" in category_low and not any(token in identity for token in ("humanoid", "whole-body", "whole body")):
        return "manipulation"
    if "locomotion" in category_low or "whole-body" in category_low or "humanoid" in category_low:
        return "humanoid" if "humanoid" in category_low or "whole-body" in category_low else "locomotion"
    if "manipulation" in category_low or "contact" in category_low or "dexterity" in category_low:
        return "manipulation"
    if "robotics foundations: planning and control" in category_low:
        # The category label itself contains the word ``control``.  Using the
        # full category in this test therefore misclassified every planning
        # classic as a control note.  Resolve the writing domain from the
        # paper title/tags and keep the canonical track unchanged.
        if any(token in identity for token in ("trajectory following", "online adaptation")):
            return "control"
        if any(token in identity for token in ("kalman", "filtering", "state estimation", "state estimator", "belief update")):
            return "estimation"
        if any(token in identity for token in ("path planning", "motion planning", "minimum cost", "roadmap", "rapidly-exploring", "rrt", "chomp", "trajopt", "pddl", "task and motion", "kinodynamic", "planner", "pomdp", "partially observable")):
            return "planning"
        return "control" if any(token in identity for token in ("control", "controller", "impedance", "force control", "operational space", "dynamics", "mpc", "trajectory following")) else "planning"
    if "foundations: vision and language" in category_low:
        return "upstream"
    if "foundations: generative" in category_low or "3d generative" in category_low:
        return "generative"
    if any(token in focus for token in ("tactile", "haptic", "force sensing", "force-aware", "touch")):
        return "tactile"
    if any(token in focus for token in ("humanoid", "whole-body", "whole body")):
        return "humanoid"
    if any(token in focus for token in ("biped", "quadruped", "legged", "locomotion", "walking")):
        return "locomotion"
    if any(token in focus for token in ("navigation", "slam", "mapping", "scene graph")):
        return "navigation"
    if "vla" in focus or "vision-language-action" in focus or track == "VLA and generalist robot policies":
        return "vla"
    if track == "RL, IL, offline learning, and robot data":
        if any(token in focus for token in ("offline", "batch rl", "implicit q", "conservative q")):
            return "offline_rl"
        if any(token in focus for token in ("imitation", "demonstration", "behavior cloning", "inverse reinforcement")):
            return "il"
        if any(token in focus for token in ("data", "dataset", "lifelong", "cross-embodiment")):
            return "robot_data"
        return "rl"
    if track == "Planning and control":
        return "control" if any(token in focus for token in ("control", "controller", "impedance", "force control", "dynamics")) else "planning"
    if track == "World models, safety, uncertainty, and recovery":
        if any(token in focus for token in ("safety", "safe", "barrier", "uncertainty", "recovery")):
            return "safety"
        if any(token in focus for token in ("simulation", "sim-to-real", "sim2real", "physics")):
            return "simulation"
        return "world_model"
    if track == "Manipulation, contact, tactile, and dexterity":
        return "manipulation"
    if track == "Locomotion, whole-body, mobile manipulation, and humanoids":
        return "locomotion"
    if track == "Robotics-enabling 3D perception":
        if any(token in focus for token in ("neural scene", "radiance", "gaussian", "view synthesis", "generative 3d")):
            return "3d_perception"
        return "3d_perception"

    if not track and any(token in category.casefold() for token in ("foundations: vision and language", "foundations: generative")):
        return "upstream"
    if any(token in focus for token in ("diffusion", "generative", "score-based", "flow matching")):
        return "generative"
    if any(token in focus for token in ("vision", "image", "visual", "clip", "bert", "language model", "transformer")):
        return "vision" if any(token in focus for token in ("image", "vision", "visual", "clip")) else "upstream"
    return "upstream"


def scope_for(domain: str, item: dict[str, Any]) -> tuple[str, str, str, str, str]:
    if domain == "upstream":
        return UPSTREAM_SCOPE
    if domain in DOMAIN_SCOPE:
        return tuple(DOMAIN_SCOPE[domain])  # type: ignore[return-value]
    return tuple(DOMAIN_SCOPE["general"])  # type: ignore[return-value]


def source_bundle(item: dict[str, Any], folder: Path) -> dict[str, list[str]]:
    overview = (folder / "01_overview.md").read_text(encoding="utf-8")
    current_problem = (folder / "02_problem.md").read_text(encoding="utf-8")
    current_method = (folder / "03_method.md").read_text(encoding="utf-8")
    current_eval = (folder / "04_evaluation.md").read_text(encoding="utf-8")
    relative = str(item["folder"])
    old_problem = git_source(f"{relative}/02_problem.md")
    old_method = git_source(f"{relative}/03_method.md")
    old_eval = git_source(f"{relative}/04_evaluation.md")

    def raw_note(document: str) -> str:
        # A normalized note is an output artifact, not a source document.
        # This matters for new/untracked papers whose pre-migration note is
        # unavailable: falling back to the current generated note would make
        # every rerun duplicate its own audit text.
        if not document.strip() or "Canonical metadata:" in document:
            return ""
        return document

    old_problem = raw_note(old_problem)
    old_method = raw_note(old_method)
    old_eval = raw_note(old_eval)
    current_problem = raw_note(current_problem)
    current_method = raw_note(current_method)
    current_eval = raw_note(current_eval)

    # The current 02–04 notes contain generated audit tables.  Prefer the
    # tracked pre-migration note for source cues so those tables are not mined
    # as if they were paper prose.  The current note is a fallback only for a
    # path that was not present in HEAD.
    problem_docs = ([old_problem] if old_problem.strip() else [current_problem]) + [overview]
    method_docs = ([old_method] if old_method.strip() else [current_method]) + [overview]
    eval_docs = ([old_eval] if old_eval.strip() else [current_eval]) + [overview]
    return {
        "problem": collect(problem_docs, ("Problem in One Sentence", "Problem", "왜 문제인가", "Target Problem and Assumptions", "해결하려는 문제"), 8),
        "bottleneck": collect(problem_docs, ("Bottleneck in Prior Work", "왜 문제인가", "선행 연구 / 배경 단서", "선행 연구 분석", "Problem"), 8),
        "changes": collect(problem_docs, ("What the Paper Changes", "해결하려는 문제", "Core Idea", "Contribution", "Problem in One Sentence"), 8),
        "problem_interface": collect(problem_docs, ("System and Scope", "Input / Output", "Interface", "Observation–State–Action Interface"), 6),
        "method": collect(method_docs, ("Method in One Sentence", "Brief Method", "Abstract Method Cue", "핵심 방법론", "Core Idea", "Contribution"), 8),
        "rationale": collect(method_docs, ("Design Rationale", "원리적 동기", "왜 문제인가", "Problem", "Limitation"), 8),
        "interface": collect(method_docs, ("Observation–State–Action Interface", "Interface", "Input / Output", "핵심 방법론"), 6),
        "dataset": collect(eval_docs, ("Dataset / Benchmark Role", "Dataset / Benchmark", "Dataset", "Benchmark"), 8),
        "metrics": collect(eval_docs, ("Metrics and Success Definition", "Metrics", "Metric"), 8),
        "protocol": collect(eval_docs, ("Evaluation in One Sentence", "Experimental Matrix", "Evaluation Protocol and Results", "Main Results / Claim–Evidence Map", "Protocol", "Evaluation Scope", "Main Claims"), 8),
        "baseline": collect(eval_docs, ("Baselines and Fairness", "Baselines", "Baseline"), 8),
        "ablation": collect(eval_docs, ("Ablations and Sensitivity", "Ablations", "Ablation", "Failure and Reproducibility"), 8),
        "failure": collect(eval_docs, ("Generalization and Failure Cases", "Limitations and Verification Questions", "Limitations and Reproducibility", "Failure and Reproducibility", "Limitation"), 8),
        "repro": collect(eval_docs, ("Statistics, Efficiency, and Reproducibility", "Reproducibility Notes", "Reproducible Minimum"), 8),
        "overview_claim": collect([overview], ("Main Claims", "Contribution", "Evaluation Scope"), 6),
    }


def cue(values: list[str], fallback: str, limit: int = 2) -> str:
    return compact(values, fallback, limit)


def method_only(values: list[str], limit: int = 8) -> list[str]:
    """Remove obvious dataset/evaluation prose from a method cue list.

    Legacy extraction often placed a paper's dataset paragraph under its
    ``Brief Method`` heading.  Those lines remain useful in 04, but mapping
    them to a pipeline module would make the method record misleading.
    """

    result: list[str] = []
    for value in values:
        low = value.casefold()
        if re.search(
            r"^(?:this|our|the|a|an)?\s*(?:dataset|benchmark|evaluation|experiment|results? in|"
            r"table|appendix|the real dataset|the synthetic dataset)\b",
            low,
        ) or re.search(r"\b(?:dataset|benchmark|evaluation|experimental results|success rate|training (?:set|data|steps)|test set|validation set)\b", low):
            continue
        if value not in result:
            result.append(value)
        if len(result) >= limit:
            break
    return result


def source_label(kind: str) -> str:
    return f"source cue ({kind}); exact section/page/equation은 본문 확인 필요"


def domain_runtime(domain: str) -> dict[str, str]:
    if domain in DOMAIN_SCOPE:
        try:
            return runtime_contract(domain, "")
        except (KeyError, TypeError):
            pass
    return {
        "horizon": "paper-specific horizon; 본문 확인 필요.",
        "rate": "paper-specific inference/control rate; 본문 확인 필요.",
        "memory": "paper-specific history/state memory; 본문 확인 필요.",
        "compute": "representation, optimization/inference steps와 hardware가 latency를 결정한다; exact profile 확인 필요.",
        "training": "paper-specific training/offline setup; 본문 확인 필요.",
        "inference": "paper-specific inference/deployment loop; 본문 확인 필요.",
    }


def note_header(kind: str, title: str, evidence: str, basis: str) -> str:
    return (
        f"# {kind} — {title}\n\n"
        "> Canonical metadata: [01_overview.md](./01_overview.md).\n"
        f"> Evidence maturity: `{evidence}`.\n"
        f"> Analysis basis: {basis}\n\n"
    )


def render_problem(item: dict[str, Any], domain: str, evidence: str, cues: dict[str, list[str]]) -> str:
    title = str(item["title"])
    scope = scope_for(domain, item)
    formulation = DOMAIN_FORMULATION.get(domain, DOMAIN_FORMULATION["general"])
    assumptions = DOMAIN_ASSUMPTIONS.get(domain, DOMAIN_ASSUMPTIONS["general"])
    loop = {
        "upstream": "upstream representation/model stage; current evidence does not establish a direct robot closed loop.",
        "benchmark": "task/interface → policy/control → outcome log; benchmark defines the comparison contract across the loop.",
    }.get(domain, f"{domain} domain의 observation → state/world model → task & motion decision → policy/control → feedback 위치; paper-specific handoff는 본문 확인 필요.")
    problem = cue(cues["problem"], f"현재 source 범위에서 {domain} domain의 target problem은 본문 확인 필요.")
    bottleneck = cue(cues["bottleneck"], f"{domain} domain에서 일반적으로 발생하는 bottleneck 후보는 source-specific prior work와 대조해야 한다; paper-specific bottleneck은 본문 확인 필요.")
    changes = cue(cues["changes"] or cues["method"], "논문이 바꾼 problem formulation은 현재 source 범위에서 확정하지 않으며 본문 확인 필요.")
    interface_cue = cue(cues["problem_interface"] + cues["interface"], "paper-specific observation/input과 output/action schema는 본문 확인 필요.")
    formal_rows = [
        ["State / observation variable", formulation[0], "domain-normalized analysis schema; paper notation과 동일하다고 가정하지 않음"],
        ["Decision / output variable", formulation[1], "paper-specific output/action과 exact constraint는 본문 확인 필요"],
        ["Objective / loss / cost", formulation[2], "problem target bridge; exact objective/loss 식은 source에서 확인 필요"],
        ["Success / guarantee", formulation[3], "reported guarantee나 metric이 아니라 verification target"],
    ]
    assumption_rows = [
        [assumption, reason, f"{failure}; paper-specific failure report는 본문 확인 필요"]
        for assumption, reason, failure in assumptions
    ]
    return (
        note_header("Problem", title, evidence, basis_text(evidence))
        + "## Problem in One Sentence\n\n"
        + f"현재 확보된 source cue 기준: {problem}\n\n"
        + "## System and Scope\n\n"
        + "\n".join(
            [
                f"- **Object / environment:** {scope[0]}.",
                f"- **Observation / input:** {scope[1]}. Interface cue: {interface_cue}",
                f"- **Latent state / decision variable:** {scope[2]}; exact representation은 본문 확인 필요.",
                f"- **Output / action:** {scope[3]}; exact output frame/unit은 본문 확인 필요.",
                f"- **Horizon / evaluation target:** {scope[4]}; source-specific horizon과 denominator은 본문 확인 필요.",
            ]
        )
        + "\n\n## Formal Problem Formulation\n\n"
        + table(["Formulation field", "Recorded bridge", "Evidence boundary"], formal_rows)
        + "\n\n- **Source-specific formulation status:** abstract/legacy cue를 domain-level bridge로 정리한 것이며, exact state transition, objective, constraint, initial/terminal condition은 본문에서 대조해야 한다.\n\n"
        + "## Bottleneck in Prior Work\n\n"
        + bottleneck
        + "\n\n- **Interpretation rule:** 위 문장은 source cue가 있으면 해당 cue를 보존하고, 없으면 domain-level review question으로만 취급한다.\n\n"
        + "## What the Paper Changes\n\n"
        + changes
        + "\n\n- **Contribution boundary:** source cue가 지지하는 formulation/method change와, 아직 검증되지 않은 downstream benefit을 분리한다.\n\n"
        + "## Assumptions and Failure Boundary\n\n"
        + table(["Candidate assumption / boundary", "Why it matters", "Failure or stress test"], assumption_rows)
        + "\n\n- 위 표의 assumption은 domain analysis hypothesis이며, 논문이 명시한 assumption으로 승격하지 않는다.\n\n"
        + "## Position in the Robotics Loop\n\n"
        + loop
        + "\n\n- **Closed-loop handoff to verify:** observation/state representation이 실제 planner·policy·controller·contact feedback 중 어디로 전달되는지 본문에서 확인한다.\n\n"
        + "## Verification Questions\n\n"
        + f"- **Evidence anchor:** {source_label('02/03/04 legacy note와 01_overview')}\n"
        + "- **Formulation:** paper의 exact state, transition/observation model, objective/loss/cost, constraints는 어느 equation/section에 정의되는가?\n"
        + "- **Interface:** observation, state/latent, output/action의 frame·unit·horizon·control rate는 무엇인가?\n"
        + "- **Boundary:** 위 assumption 중 실제 limitation/failure로 보고된 것과 단지 재현 시 stress test인 것은 무엇인가?\n"
        + "- **Robotics relevance:** upstream paper라면 어떤 downstream state estimation/planning/control 행동을 실제로 바꾸는지 근거가 있는가?\n"
    )


def pipeline_rows(domain: str, method_cues: list[str]) -> list[list[str]]:
    modules = DOMAIN_MODULES.get(domain, DOMAIN_MODULES["general"])
    rows: list[list[str]] = []
    for index, (name, purpose, input_value, operation, output, benefit) in enumerate(modules):
        paper_cue = method_cues[index] if index < len(method_cues) else "paper-specific module operation은 본문 확인 필요"
        rows.append(
            [
                name,
                purpose,
                input_value,
                f"{operation}. Source method cue: {paper_cue}",
                output,
                benefit,
                "legacy/overview cue; exact method subsection·equation·page 확인 필요",
            ]
        )
    return rows


def render_variables(domain: str) -> str:
    values = DOMAIN_VARIABLES.get(domain, DOMAIN_VARIABLES.get("general", []))
    rows = []
    for symbol, type_value, meaning, used_in in values:
        rows.append([symbol, type_value, meaning, used_in, "domain-normalized notation; paper-specific symbol/unit 확인 필요"])
    if not rows:
        rows = [["oₜ / zₜ / yₜ", "input/state/output", "paper-specific variables", "method interface", "본문 확인 필요"]]
    return table(["Symbol / parameter", "Type / unit", "Meaning", "Used in", "Source status"], rows)


def objective_cue(cues: dict[str, list[str]]) -> str:
    values = cues["method"] + cues["rationale"] + cues["problem"]
    for value in values:
        if re.search(r"loss|objective|optimi[sz]|maximize|minimi[sz]|gradient|equation|control law|predict|generate|mapping|tracking", value, re.I):
            return value
    return "objective/loss/control law cue가 현재 source note에 없음"


def render_method(item: dict[str, Any], domain: str, evidence: str, cues: dict[str, list[str]], eval_note: str) -> str:
    title = str(item["title"])
    scope = scope_for(domain, item)
    runtime = domain_runtime(domain)
    modules = DOMAIN_MODULES.get(domain, DOMAIN_MODULES["general"])
    method_sentence = cue(cues["method"], f"현재 source 범위에서 {domain} method의 exact operation은 본문 확인 필요.")
    rationale = cue(cues["rationale"] or cues["bottleneck"], "method design rationale은 본문 확인 필요.")
    method_cues = method_only(list(dict.fromkeys(cues["method"] + cues["interface"] + cues["changes"])))
    interface_cues = method_only(cues["interface"])
    eval_cue = cue(cues["protocol"], "04_evaluation.md에 usable protocol/result cue가 없음 — 본문 확인 필요.")
    baseline_cue = cue(cues["baseline"], "baseline cue가 없음 — exact comparison table 확인 필요.")
    ablation_cue = cue(cues["ablation"], "reported ablation cue가 없음 — component removal은 재현 시 별도 실행 필요.")
    evaluation_rows = []
    for index, (name, _purpose, _input, _operation, _output, benefit) in enumerate(modules):
        comparison = baseline_cue if index == 0 else ablation_cue if index == 1 else eval_cue
        evaluation_rows.append([name, benefit, comparison, "04 cue; exact baseline/ablation/result condition 확인 필요"])
    failure_rows = [
        [name, f"{benefit}의 핵심 가정을 제거하거나 입력/데이터/compute를 고정한 variant", "candidate audit; paper-reported ablation으로 간주하지 않음"]
        for name, _purpose, _input, _operation, _output, benefit in modules
    ]
    return (
        note_header("Method", title, evidence, basis_text(evidence))
        + "## Method in One Sentence\n\n"
        + f"현재 확보된 source cue 기준: {method_sentence}\n\n"
        + "## Design Rationale\n\n"
        + rationale
        + "\n\n- **Design-level interpretation:** source cue가 직접 지지하는 rationale과 domain-level reproduction question을 구분한다.\n\n"
        + "## Source Evidence Cues\n\n"
        + "\n".join(f"- {value}" for value in (method_cues or ["method cue 없음 — 본문 확인 필요"]))
        + f"\n- **Source anchor:** {source_label('legacy 03_method와 01_overview')}\n\n"
        + "## Pipeline\n\n"
        + table(["Module", "Purpose", "Input", "Operation", "Output", "Interface / expected benefit", "Evidence"], pipeline_rows(domain, method_cues))
        + "\n\n## Objective / Update Rule\n\n"
        + f"- **Source objective/update cue:** {objective_cue(cues)}.\n"
        + "- **Analysis contract:** module은 source-defined target을 optimize/update하거나 control law를 실행하는 것으로 정리했으며, exact loss sign, optimizer, solver, target network, gain과 stopping rule은 본문 확인 필요.\n"
        + "- **Constraint/regularization:** input/action feasibility, model validity, data support와 runtime budget 중 실제 paper constraint를 구분해야 한다.\n"
        + "- **Source:** legacy method cue; exact equation/algorithm box/page 확인 필요.\n\n"
        + "## Variables and Parameters\n\n"
        + render_variables(domain)
        + "\n\n## Observation–State–Action Interface\n\n"
        + f"- **Observation / input:** {scope[1]}. Source interface cue: {cue(interface_cues, 'paper-specific observation schema는 본문 확인 필요.')}\n"
        + f"- **State / latent representation:** {scope[2]}; exact tensor/frame/uncertainty representation은 본문 확인 필요.\n"
        + f"- **Action / output:** {scope[3]}; exact action space, unit, decoder/control handoff는 본문 확인 필요.\n"
        + "- **Planner–controller / policy–environment interface:** action이 environment에 직접 적용되는지, planner/reference/controller를 거치는지와 feedback timing을 확인한다.\n\n"
        + "## Temporal and Runtime Contract\n\n"
        + f"- **Horizon:** {runtime['horizon']}\n"
        + f"- **Inference/control rate:** {runtime['rate']}\n"
        + f"- **History / memory:** {runtime['memory']}\n"
        + f"- **Compute / latency dependency:** {runtime['compute']}\n\n"
        + "## Training vs Inference\n\n"
        + f"- **Training / offline setup:** {runtime['training']} exact data split·pretraining·privileged input은 본문 확인 필요.\n"
        + f"- **Inference / online execution:** {runtime['inference']} exact runtime path와 fallback은 본문 확인 필요.\n"
        + "- **Boundary to keep separate:** training throughput, inference rate, low-level actuator rate, action horizon, memory window와 feedback latency를 하나로 기록하지 않는다.\n\n"
        + "## Method-Specific Formal Details\n\n"
        + "- Exact equation/loss/control law와 paper notation은 현재 source 범위에서 확정하지 않는다. domain-normalized formulation은 02_problem.md에 있고, source-specific equation 번호·algorithm step·hyperparameter는 본문 확인 필요.\n"
        + f"- **Formal bridge:** {DOMAIN_FORMULATION.get(domain, DOMAIN_FORMULATION['general'])[0]} → {DOMAIN_FORMULATION.get(domain, DOMAIN_FORMULATION['general'])[1]} → {DOMAIN_FORMULATION.get(domain, DOMAIN_FORMULATION['general'])[2]}.\n\n"
        + "## Evaluation Link\n\n"
        + "> 아래는 method module과 evaluation cue의 연결표다. 새로운 result를 주장하지 않으며, 원문 table/figure와 조건을 찾아야 한다.\n\n"
        + table(["Method module", "What evaluation should isolate", "Baseline / ablation / result cue", "Evidence"], evaluation_rows)
        + "\n\n## Failure and Ablation Link\n\n"
        + table(["Module / assumption", "Minimum stress test", "Status"], failure_rows)
        + "\n\n- **Causal attribution rule:** input, data, compute, horizon, action interface와 controller를 고정하지 않은 비교는 module contribution으로 해석하지 않는다.\n\n"
        + "## Reproduction Checklist\n\n"
        + "1. [ ] source method section에서 module input/output, exact variable/unit, equation 또는 algorithm step을 옮긴다.\n"
        + "2. [ ] objective/loss/control law와 constraint, initialization, update schedule을 분리해 기록한다.\n"
        + "3. [ ] observation/action frame, horizon, memory, inference/control rate와 latency budget을 고정한다.\n"
        + "4. [ ] 04의 baseline, ablation, dataset split, seed/trial과 success denominator를 같은 조건으로 대조한다.\n"
        + "5. [ ] primary metric뿐 아니라 failure mode, generalization, compute와 closed-loop recovery를 기록한다.\n\n"
        + "## Verification Questions\n\n"
        + f"- **Source anchor:** {source_label('legacy 03_method와 04_evaluation')}\n"
        + "- **Module attribution:** 제안 method를 제거·대체했을 때 어떤 evaluation row가 실제로 변하는가?\n"
        + "- **Runtime:** training/inference와 policy/control rate, action chunk/horizon, memory를 각각 얼마로 재현해야 하는가?\n"
        + "- **Evidence boundary:** 현재 evidence level에서 확인하지 않은 optimizer, hyperparameter, negative result와 latency를 추가하지 않았는가?\n"
    )


def infer_eval_type(item: dict[str, Any], domain: str, cues: dict[str, list[str]]) -> str:
    paper_type = str(item.get("paper_type", ""))
    all_text = " ".join(sum(cues.values(), [])).casefold()
    if domain == "benchmark" or paper_type == "benchmark_or_dataset":
        return "BENCHMARK / DATASET PROTOCOL"
    if paper_type == "system" and any(token in all_text for token in ("real robot", "real-world", "hardware", "physical")):
        return "SYSTEM / REAL-ROBOT OR MIXED CUE"
    if paper_type == "theory_or_foundation" and not (cues["dataset"] or cues["protocol"] or cues["metrics"]):
        return "THEORY / FORMULATION OR ANALYTIC"
    if cues["dataset"] or cues["protocol"] or cues["metrics"]:
        return "EMPIRICAL / SOURCE-CUE EVALUATION"
    if paper_type == "system":
        return "SYSTEM / PROTOCOL NOT RESOLVED"
    return "PROVISIONAL / EVALUATION SCOPE NOT RESOLVED"


def resource_records(values: list[str]) -> list[tuple[str, str, str]]:
    if not values:
        return [("not found", "resource name not found in the current source cue", "본문 확인 필요")]
    records = []
    for value in values[:8]:
        records.append((value, "source cue; train/eval/pretraining/auxiliary role unresolved", "legacy 04 dataset cue; exact table/section 확인 필요"))
    return records


def metric_records(values: list[str], domain: str) -> list[tuple[str, str, str]]:
    if not values:
        target = {
            "3d_perception": "geometric/semantic accuracy and downstream robot utility",
            "vla": "task success and instruction-conditioned generalization",
            "planning": "path cost/feasibility and goal reach",
            "control": "tracking/contact error and stability",
            "benchmark": "benchmark score and failure breakdown",
        }.get(domain, "paper-specific primary metric")
        return [(target, "analysis target, not paper-reported metric", "02 scope; exact metric 확인 필요")]
    records = [(value, "source metric cue; definition, direction, unit and aggregation unresolved", "legacy 04 metric cue; exact table/section 확인 필요") for value in values[:8]]
    return records


def baseline_records(values: list[str], eval_type: str) -> list[str]:
    if values:
        return values[:6]
    if eval_type.startswith("THEORY"):
        return ["not applicable / conceptual comparison or analytic reference not resolved"]
    return ["not found in current source cue"]


def ablation_records(values: list[str], domain: str, modules: list[tuple[str, str, str, str, str, str]], eval_type: str) -> list[tuple[str, str, str, str]]:
    records: list[tuple[str, str, str, str]] = []
    for value in values[:5]:
        records.append((value, modules[1][0], "source cue; reported status and result require body verification", "legacy 04 ablation/protocol cue"))
    candidate = {
        "vla": "vision/language/3D input or action horizon variant",
        "3d_perception": "geometry/semantic/temporal fusion variant",
        "tactile": "vision-only versus tactile/force input",
        "locomotion": "history/adaptation or privileged-input variant",
        "world_model": "rollout horizon/model uncertainty variant",
        "benchmark": "task split/reset/metric protocol variant",
    }.get(domain, "core module removal with input, data, compute and runtime fixed")
    if not records:
        status = "not applicable as a component ablation" if eval_type.startswith("THEORY") else "minimum audit; not paper-reported"
        records.append((f"not reported — {candidate}", modules[1][0], "sensitivity of the central interface/assumption", status))
    return records[:5]


def trial_seed(values: list[str]) -> tuple[str, str, str]:
    trial = "not reported"
    seed = "not reported"
    stats = "not reported"
    for value in values:
        if trial == "not reported":
            match = re.search(r"(?:\d+\s+)?(?:trials?|episodes?|runs?)\s*(?:=|:)?\s*\d+|\bN\s*=\s*\d+", value, re.I)
            if match:
                trial = match.group(0)
        if seed == "not reported":
            match = re.search(r"(?:\d+\s+)?(?:random\s+)?seeds?\s*(?:=|:)?\s*\d+", value, re.I)
            if match:
                seed = match.group(0)
        if stats == "not reported" and ("±" in value or re.search(r"standard deviation|confidence interval|mean", value, re.I)):
            stats = value
    return trial, seed, stats


def render_evaluation(item: dict[str, Any], domain: str, evidence: str, cues: dict[str, list[str]]) -> str:
    title = str(item["title"])
    scope = scope_for(domain, item)
    eval_type = infer_eval_type(item, domain, cues)
    datasets = resource_records(cues["dataset"])
    metrics = metric_records(cues["metrics"], domain)
    baselines = baseline_records(cues["baseline"], eval_type)
    modules = DOMAIN_MODULES.get(domain, DOMAIN_MODULES["general"])
    ablations = ablation_records(cues["ablation"], domain, modules, eval_type)
    protocol = cues["protocol"] or cues["overview_claim"]
    result_cue = cue(protocol, "result/evidence cue가 현재 source note에 없음 — 본문 확인 필요.", 2)
    trial, seed, stats = trial_seed(protocol + cues["repro"])
    setting_text = " ".join(protocol[:3]).casefold()
    if re.search(r"\breal(?:[- ]world)?\b|\breal robot\b|\bphysical robot\b|\bhardware\b", setting_text):
        setting = "real/system cue"
    elif "simulat" in setting_text or "simulator" in setting_text or "simulation" in setting_text:
        setting = "simulation cue"
    elif eval_type.startswith("THEORY"):
        setting = "analytic/formulation cue"
    else:
        setting = "setting not resolved in current source cue"
    baseline = baselines[0]
    metric = metrics[0][0]
    dataset = datasets[0][0]
    matrix_rows = []
    protocol_rows = protocol[:3] or ["protocol cue not found"]
    for line in protocol_rows:
        matrix_rows.append([
            "paper-specific claim/experiment",
            setting,
            f"{dataset}; role/split unresolved",
            scope[0],
            baseline,
            f"{metric}; {line}",
            f"trials: {trial}; seeds: {seed}",
            "legacy/overview evaluation cue; exact table/figure/page 확인 필요",
        ])
    environment_rows = [
        ["Evaluation type", eval_type, "provisional source-cue classification", "source cue"],
        ["Robot / simulator / hardware", setting, "real/sim status and hardware configuration unresolved", "legacy 04 protocol cue"],
        ["Observation / sensor", scope[1], "sensor, calibration and preprocessing require body verification", "02 scope bridge"],
        ["Output / decision", scope[3], "action/metric output and evaluation unit require body verification", "02 scope bridge"],
        ["Task / episode unit", cue([line for line in protocol if re.search(r"task|episode|sequence|environment|benchmark", line, re.I)], "task count/reset/timeout not found"), "denominator and termination rule unresolved", "legacy 04 protocol cue"],
        ["Generalization / variation", cue([line for line in protocol + cues["failure"] if re.search(r"novel|unseen|general|transfer|robust|varied|challenge", line, re.I)], "unseen split or variation not found"), "split and held-out dimensions require body verification", "legacy evaluation cue"],
    ]
    metric_rows = [[name, "direction/unit/aggregation unresolved", role, source] for name, role, source in metrics]
    baseline_rows = [[name, "comparison identity or claimed comparison", "same data/observation/compute not verified", "legacy 04 baseline cue"] for name in baselines]
    fairness_rows = [
        ["Observation/action interface", "not reported", "hold sensor modality, frame, action space and preprocessing fixed"],
        ["Data/pretraining", "not reported", "match demonstrations, pretraining, labels and leakage boundary"],
        ["Compute/runtime", "not reported", "match parameter budget, inference steps, latency and control rate"],
        ["Evaluation protocol", "not reported", "match split, reset/timeout, seeds and success denominator"],
    ]
    ablation_rows = [[factor, module, interpretation, source] for factor, module, interpretation, source in ablations]
    failure_rows = []
    for assumption, _reason, failure in DOMAIN_ASSUMPTIONS.get(domain, DOMAIN_ASSUMPTIONS["general"]):
        failure_rows.append([assumption, failure, "domain stress-test hypothesis; not necessarily paper-reported", "02 problem analysis; exact failure evidence verify"])
    for value in cues["failure"][:4]:
        failure_rows.append(["source limitation/failure cue", value, "legacy cue; source strength unresolved", "legacy 04 limitation cue"])
    if not failure_rows:
        failure_rows.append(["paper-specific assumption", "failure case not found in current source cue", "verification required", "본문 확인 필요"])
    statistic_rows = [
        ["Trials / episodes", trial, "not reported means no count was found; not zero", "legacy protocol cue"],
        ["Random seeds / repeats", seed, "not reported", "legacy protocol/repro cue"],
        ["Mean ± std / CI", stats, "not reported", "legacy result/repro cue"],
        ["Latency / throughput", "not reported", "numeric value only after exact source location", "본문 확인 필요"],
        ["Compute / hardware dependency", cue(cues["repro"], "not reported", 1), "configuration not fully resolved", "legacy reproducibility cue"],
        ["Train/eval split and leakage", cue([line for line in cues["dataset"] + cues["protocol"] if re.search(r"split|train|test|validation|held[- ]out|unseen", line, re.I)], "not reported"), "role and leakage boundary require body verification", "legacy dataset/protocol cue"],
        ["Code/checkpoint/environment", "see 01_overview.md; not duplicated here", "availability is not reprinted as metadata", "01_overview.md"],
        ["Evaluation mode", eval_type, "governs which fields are applicable", "evaluation type audit"],
    ]
    missing = []
    if dataset in {"not found", "not applicable"}:
        missing.append("dataset/benchmark role")
    if baselines and baselines[0] == "not found in current source cue":
        missing.append("baseline identity/fairness")
    if trial == "not reported" or seed == "not reported":
        missing.append("trial/seed statistics")
    return (
        note_header("Evaluation", title, evidence, basis_text(evidence))
        + "## Evaluation in One Sentence\n\n"
        + f"현재 확보된 source cue 기준: {result_cue}\n\n"
        + "## Evaluation Type and Scope\n\n"
        + f"- **Evaluation type:** `{eval_type}` (provisional; source body에서 확인 필요)\n"
        + f"- **Target system/task:** {scope[0]}\n"
        + f"- **Input/observation boundary:** {scope[1]}\n"
        + f"- **Output/decision under evaluation:** {scope[3]}\n"
        + f"- **Primary target:** {scope[4]}\n"
        + "- **Scope rule:** theory/formulation은 theorem·analytic example·controller behavior를, empirical paper는 matched task/data/baseline/trial을, benchmark는 task/protocol/score definition을 분리해 기록한다.\n\n"
        + "## Experimental Matrix\n\n"
        + table(["Experiment / claim", "Type & setting", "Dataset / split", "Robot / system", "Baseline", "Metric / result cue", "Trials / seeds", "Source"], matrix_rows)
        + "\n\n## Dataset / Benchmark Role\n\n"
        + table(["Resource", "Role", "Split / size", "Source"], [[name, role, "not reported", source] for name, role, source in datasets])
        + "\n\n- Dataset/resource names are retained as cues only; experiment section에서 train/eval/pretraining/auxiliary role을 찾기 전까지 verified dataset으로 사용하지 않는다.\n\n"
        + "## Embodiment / Environment\n\n"
        + table(["Dimension", "Recorded cue", "Interpretation / missing detail", "Source"], environment_rows)
        + "\n\n## Metrics and Success Definition\n\n"
        + table(["Metric / success signal", "Direction / unit", "Status", "Source"], metric_rows)
        + "\n\n- **Success/failure/timeout definition:** current source cue에 없는 exact denominator, collision/contact rule와 termination condition은 본문 확인 필요.\n\n"
        + "## Baselines and Fairness\n\n"
        + table(["Baseline / comparison cue", "What it should isolate", "Same data/observation/compute?", "Source"], baseline_rows)
        + "\n\n**Baseline fairness audit**\n\n"
        + table(["Fairness dimension", "Current record", "Required check"], fairness_rows)
        + "\n\n## Ablations and Sensitivity\n\n"
        + table(["Ablation / sensitivity factor", "Method component", "Expected interpretation", "Reported status / source"], ablation_rows)
        + "\n\n## Main Results / Claim–Evidence Map\n\n"
        + table(["Claim / target", "Evidence or result cue", "Evaluation type", "Strength", "Source"], [[scope[4], result_cue, eval_type, "source cue only; exact result table/conditions verify", "legacy/overview evaluation cue"]])
        + "\n\n## Generalization and Failure Cases\n\n"
        + table(["Assumption / regime", "Failure or stress test", "Status", "Source"], failure_rows)
        + "\n\n- **Untested regime audit:** embodiment, sensor noise/calibration, contact mode, long horizon, unseen object/task/scene, dynamic environment and recovery behavior are not assumed covered unless explicitly reported.\n\n"
        + "## Statistics, Efficiency, and Reproducibility\n\n"
        + table(["Reproducibility field", "Recorded value/cue", "Status", "Source"], statistic_rows)
        + "\n\n## Limitations and Verification Questions\n\n"
        + "- **Evidence boundary:** evaluation cue를 reported result로 승격하지 않았으며 exact table/figure/page는 원문 확인이 필요하다.\n"
        + f"- **Missing comparison fields:** {', '.join(missing) if missing else '현재 source cue에서 명시적 누락을 모두 해소했다는 뜻은 아니며 body verification remains required'}.\n"
        + "- **Interpretation rule:** `not applicable`은 평가 유형상 해당하지 않음을, `not found`는 현재 source cue에 이름이 없음을, `not reported`는 보고 여부를 확인하지 못했음을 뜻한다.\n"
        + "- **Do not overclaim:** single success/accuracy cue만으로 generalization, robustness, causality, real-robot reproducibility를 주장하지 않는다.\n"
        + f"- **Source anchor:** {source_label('legacy 04_evaluation와 01_overview')}\n"
        + "- **Claim–condition check:** 모든 result는 task, embodiment/simulator, input/action interface, metric, baseline, trial/seed와 source location을 함께 가져야 한다.\n"
        + "- **Reproduction check:** reset/timeout/success denominator, preprocessing, checkpoint, compute, inference/control rate와 failure handling을 본문에서 확인한다.\n"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true", help="write the 682 non-CORE/NEXT notes; default is dry-run")
    parser.add_argument("--show", type=int, default=0, help="show the first N generated paper bundles")
    args = parser.parse_args()

    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    tier_rows = read_tiers()
    counts: Counter[str] = Counter()
    changed = Counter()
    previews: list[str] = []
    selected = 0
    skipped_intensive = 0
    missing: list[str] = []

    for item in manifest:
        tier_row = tier_rows.get(str(item.get("paper_id"))) or tier_rows.get(str(item["title"]))
        if not tier_row:
            missing.append(f"tier row: {item['title']}")
            continue
        if tier_row.get("tier") in {"CORE", "NEXT"}:
            skipped_intensive += 1
            continue
        selected += 1
        folder = resolve_folder(str(item["folder"]))
        paths = {name: folder / f"0{name}_{suffix}.md" for name, suffix in ((1, "overview"), (2, "problem"), (3, "method"), (4, "evaluation"))}
        if not all(path.exists() for path in paths.values()):
            missing.append(str(item["title"]))
            continue
        overview = paths[1].read_text(encoding="utf-8")
        old_notes = [paths[index].read_text(encoding="utf-8") for index in (2, 3, 4)]
        evidence = evidence_for(item, overview, *old_notes)
        domain = infer_domain(item, tier_row)
        cues = source_bundle(item, folder)
        new_notes = {
            2: render_problem(item, domain, evidence, cues),
            3: render_method(item, domain, evidence, cues, old_notes[2]),
            4: render_evaluation(item, domain, evidence, cues),
        }
        counts[domain] += 1
        for index, content in new_notes.items():
            path = paths[index]
            old = path.read_text(encoding="utf-8")
            if content != old:
                changed[index] += 1
                if args.apply:
                    path.write_text(content, encoding="utf-8")
        if args.show and len(previews) < args.show:
            previews.append(
                f"--- {item['title']} [{tier_row.get('tier')}, {domain}]\n"
                + "\n\n".join(f"### 0{index}_{name}\n{new_notes[index]}" for index, name in ((2, "problem"), (3, "method"), (4, "evaluation")))
            )

    print(
        {
            "mode": "apply" if args.apply else "dry-run",
            "selected_remaining": selected,
            "skipped_core_next": skipped_intensive,
            "notes_to_update": dict(changed),
            "total_file_updates": sum(changed.values()),
            "domain_counts": dict(counts),
            "missing": len(missing),
        }
    )
    for value in missing:
        print(f"MISSING: {value}")
    for preview in previews:
        print(preview)


if __name__ == "__main__":
    main()
