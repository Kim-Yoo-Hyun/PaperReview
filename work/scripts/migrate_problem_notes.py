#!/usr/bin/env python3
"""Normalize every 02_problem.md and add formulation-first analysis.

The migration has two deliberately separate paths:

* all registry notes receive the same problem-note structure and lose copied
  paper metadata; and
* CORE/NEXT notes use a curated formulation profile containing the object,
  variables, objective, constraints, bottleneck, and closed-loop role.

The script never changes reading status.  A note can therefore contain an
agent-written formulation review without pretending that the user has read
the method and evaluation sections.  Run without --apply for a dry run.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "work" / "sources" / "papers.json"
STATUS = ROOT / "research" / "READING_STATUS.csv"
IMPORT_DIR = ROOT / "work" / "sources" / "imports"

VALID_EVIDENCE = {
    "CURATION_ONLY",
    "ABSTRACT_CHECKED",
    "FULL_TEXT_CHECKED",
    "EXPERIMENT_CHECKED",
}

COMMON_HEADINGS = (
    "## Problem in One Sentence",
    "## System and Scope",
    "## Formal Problem Formulation",
    "## Bottleneck in Prior Work",
    "## What the Paper Changes",
    "## Assumptions and Failure Boundary",
    "## Position in the Robotics Loop",
    "## Verification Questions",
)


def profile(
    title: str,
    *,
    problem: str,
    model: str,
    objective: str,
    constraints: str,
    success: str,
    bottleneck: str,
    changes: str,
    assumptions: list[tuple[str, str, str]],
    loop: str,
    anchor: str,
    domain: str = "general",
    body_basis: str = "BODY_FORMULATION_REVIEWED",
) -> dict[str, Any]:
    return {
        "title": title,
        "problem": problem,
        "model": model,
        "objective": objective,
        "constraints": constraints,
        "success": success,
        "bottleneck": bottleneck,
        "changes": changes,
        "assumptions": assumptions,
        "loop": loop,
        "anchor": anchor,
        "domain": domain,
        "body_basis": body_basis,
    }


# The compact profiles below are the source for the intensive-reading notes.
# They intentionally describe the problem, rather than repeating the method
# section.  Exact result values remain in 04_evaluation.md and are not copied
# here.
PROFILES: dict[str, dict[str, Any]] = {}


def add(paper: dict[str, Any]) -> None:
    PROFILES[paper["title"]] = paper


def add_many(items: list[dict[str, Any]]) -> None:
    for item in items:
        add(item)


# Planning, estimation, control, and TAMP foundations.
add_many(
    [
        profile(
            "A New Approach to Linear Filtering and Prediction Problems",
            problem="선형 동역학과 noisy observation에서 과거 관측으로 현재·미래·과거의 latent state를 추정하고 지정한 평균제곱 오차를 최소화한다.",
            model="상태 xₖ는 선형 transition과 process disturbance를 따르고, 관측 yₖ는 선형 observation과 measurement noise를 따른다. 필터는 관측 history의 sufficient statistic을 estimate mean과 error covariance로 유지한다.",
            objective="조건부 기대값에 대한 quadratic loss E[(xₖ−x̂ₖ)ᵀW(xₖ−x̂ₖ)]를 최소화하는 causal estimate를 구한다.",
            constraints="선형 transition/observation과 noise의 2차 통계가 주어져야 하며, filtering은 현재까지의 관측만 사용하고 prediction/smoothing은 시간 인덱스에 따라 허용된 관측 범위를 바꾼다.",
            success="새 관측이 들어올 때 estimate와 covariance를 재귀적으로 갱신하고, 그 covariance가 달성 가능한 estimation error를 나타내는 것이다.",
            bottleneck="일반 batch least-squares나 전체 history 재계산은 online control에 비싸고, noisy partial observation을 그대로 제어기에 넣으면 uncertainty를 숨긴다.",
            changes="state reconstruction을 별도 문제로 두지 않고 conditional estimation, prediction, smoothing을 같은 선형-확률 formulation과 recursion으로 묶는다.",
            assumptions=[
                ("선형 transition/observation", "prediction과 update를 닫힌 재귀로 만들기 위해 필요", "강한 비선형·접촉 전환에서는 covariance recursion이 실제 오차를 대표하지 않을 수 있음"),
                ("noise의 평균·공분산을 모델링할 수 있음", "gain과 posterior uncertainty를 계산하기 위해 필요", "bias, heavy-tail, 미모델 센서 고장은 confidence를 과소평가함"),
            ],
            loop="observation → state/world model의 state-estimation 단계이며, covariance는 planner·controller·recovery가 사용할 uncertainty interface다.",
            anchor="본문의 filtering/prediction/smoothing formulation과 orthogonal-projection 및 covariance recursion 부분.",
            domain="estimation",
        ),
        profile(
            "A Formal Basis for the Heuristic Determination of Minimum Cost Paths",
            problem="양의 arc cost를 갖는 graph에서 start node와 goal set 사이의 minimum-cost path를 찾으면서 heuristic이 탐색량을 줄이고 최적성 보장을 유지하게 한다.",
            model="노드 n의 누적 비용 g(n), 목표까지의 실제 최적 잔여 비용 h*(n), heuristic h(n)을 두고, open list에서 f(n)=g(n)+h(n)가 가장 작은 후보를 확장한다.",
            objective="목표에 도달하는 경로의 누적 arc cost를 최소화한다.",
            constraints="arc cost는 양수이고 successor/goal test가 주어져야 한다. h(n)≤h*(n)이면 admissible하며, graph search의 경우 duplicate-state 처리와 reopen 규칙이 최적성에 영향을 준다.",
            success="goal에 도달했을 때 반환한 path가 minimum cost이고, 같은 정보 조건에서 불필요한 node expansion을 줄이는 것이다.",
            bottleneck="uninformed search는 branching factor 때문에 많은 노드를 확장하고, 임의의 heuristic은 빠를 수 있어도 최적 경로를 버릴 수 있다.",
            changes="domain knowledge를 lower-bound heuristic으로 명시해 path cost와 goal-distance estimate를 하나의 우선순위로 결합하고 admissibility 조건을 정리한다.",
            assumptions=[
                ("양의 arc cost와 명시적 successor", "finite path cost와 termination 논증에 필요", "연속 dynamics·time-varying cost·negative cycle에서는 그대로 적용되지 않음"),
                ("heuristic이 true remaining cost의 lower bound", "optimality를 보존하기 위해 필요", "과대추정 heuristic은 빠른 suboptimal path를 반환할 수 있음"),
            ],
            loop="task & motion decision 중 discrete task-planning 단계에서 graph state를 executable subgoal sequence로 바꾸는 문제다.",
            anchor="본문의 problem definition, evaluation function f=g+h, admissibility와 optimality theorem 부분.",
            domain="planning",
        ),
        profile(
            "Planning and Acting in Partially Observable Stochastic Domains",
            problem="state를 직접 볼 수 없고 action·observation이 stochastic한 domain에서 history를 이용해 expected discounted reward를 최대화하는 policy를 찾는다.",
            model="POMDP tuple (S,A,T,R,Ω,O)와 initial belief b₀를 두고, belief update b'(s')∝O(o|s')ΣₛT(s'|s,a)b(s)로 history를 belief state로 압축한다.",
            objective="belief에서 action을 선택하는 policy π가 expected discounted return E[ΣγᵗR(sₜ,aₜ)]을 최대화한다.",
            constraints="transition·observation·reward model과 finite state/action/observation set이 주어져야 하며, action 후 observation을 받은 뒤 belief를 갱신한다.",
            success="observation history가 달라도 동일한 belief가 같은 decision state가 되고, policy/value가 hidden-state uncertainty를 반영해 장기 return을 높이는 것이다.",
            bottleneck="fully observable planning은 state aliasing을 만들고, history를 그대로 tree search하면 horizon에 따라 branch가 폭발한다.",
            changes="불완전 관측의 history를 belief-MDP로 바꾸고, policy-tree value의 piecewise-linear structure를 이용해 witness-based backup과 finite-state controller를 탐색한다.",
            assumptions=[
                ("transition·observation model을 알고 있음", "belief update와 predictive value 계산에 필요", "unknown dynamics/visual perception error에서는 belief가 잘못 보정됨"),
                ("belief가 relevant history를 충분히 요약", "Markov decision interface를 만들기 위해 필요", "고차원 continuous robot state와 unmodeled contact에서는 finite representation이 부족할 수 있음"),
            ],
            loop="observation → belief/state estimate → information-gathering 또는 task action → 다음 observation의 feedback loop를 formalize한다.",
            anchor="본문의 POMDP definition, belief-state transformation, policy-tree value와 Witness algorithm 부분.",
            domain="planning",
        ),
        profile(
            "A Unified Approach for Motion and Force Control of Robot Manipulators: The Operational Space Formulation",
            problem="joint-space dynamics만으로는 end-effector motion, contact wrench, configuration-dependent inertia와 task-direction coupling을 직접 지정하기 어려워 operational coordinates에서 이를 제어한다.",
            model="q, q̇, joint inertia A(q), Jacobian J(q), task coordinate x와 operational inertia Λ=(J A⁻¹Jᵀ)⁻¹를 사용해 task-space dynamics와 wrench-to-joint mapping τ=JᵀF를 구성한다.",
            objective="지정된 task-space acceleration/motion과 force 방향을 추종하면서 redundant DOF의 null-space objective도 만족한다.",
            constraints="task/force selection matrix, rigid-body dynamics, Jacobian rank와 contact wrench 관계가 주어져야 하며 singularity에서는 유효 task subspace를 분리해야 한다.",
            success="task-space command가 desired end-effector behavior와 contact force를 만들고, redundancy가 secondary posture/stability objective를 해치지 않는 것이다.",
            bottleneck="joint coordinates의 독립 servo는 task-level inertia와 contact direction을 노출하지 않아 coupled motion/force 작업에서 조정이 어렵다.",
            changes="motion·force specification matrix를 사용해 operational dynamics, dynamically consistent inverse와 null-space를 하나의 formulation으로 통합한다.",
            assumptions=[
                ("usable rigid-body model과 Jacobian", "task wrench를 joint torque로 일관되게 변환하기 위해 필요", "model error·friction·flexibility가 크면 force tracking과 decoupling이 깨짐"),
                ("task/constraint frame과 force sensing", "어느 방향을 움직이고 밀어야 하는지 정의하기 위해 필요", "contact geometry가 바뀌거나 wrench가 관측되지 않으면 specification이 stale해짐"),
            ],
            loop="task & motion decision → operational-space motion/force controller → joint torque → contact feedback의 low-level interface다.",
            anchor="본문의 operational-space equations, generalized task specification, redundancy·impact·singularity discussion.",
            domain="control",
        ),
        profile(
            "Hybrid Position/Force Control of Manipulators",
            problem="환경과 접촉하는 manipulator에서 position/orientation과 force/torque를 동시에 만족하려면 task geometry가 정한 방향별 제어 분리가 필요하다.",
            model="Cartesian task frame C에서 position/force error를 계산하고 binary compliance selection S로 force-controlled subspace와 position-controlled subspace를 분리한다.",
            objective="S가 선택한 방향에서는 desired contact force를, 나머지 방향에서는 desired position/velocity를 추종한다.",
            constraints="natural constraint가 정한 contact frame과 selection matrix가 주어지고, 한 task DOF를 position과 force loop가 동시에 지배하지 않아야 한다.",
            success="공통 manipulator joints가 두 subspace loop의 명령을 실행해 접촉 방향의 force와 비접촉 방향의 motion을 각각 안정적으로 유지하는 것이다.",
            bottleneck="모든 Cartesian DOF를 stiff position servo로 제어하면 작은 geometry error가 큰 contact force로 증폭되고, force만 제어하면 자유 방향의 motion 목표를 잃는다.",
            changes="contact-induced natural constraint를 기준으로 task frame을 만들고, position/force feedback loop를 selection matrix로 합성하는 controller architecture를 제시한다.",
            assumptions=[
                ("contact geometry와 natural constraint를 식별", "force/position subspace를 정하기 위해 필요", "contact mode가 바뀌거나 frame calibration이 틀리면 잘못된 DOF를 제어함"),
                ("wrist force와 joint position을 충분한 bandwidth로 측정", "두 feedback loop를 닫기 위해 필요", "sensor delay/noise와 actuator saturation이 force oscillation을 만들 수 있음"),
            ],
            loop="contact → wrench/pose feedback → hybrid task controller → joint actuation에 해당하는 interaction-control 단계다.",
            anchor="본문의 natural/artificial constraint 구분, task frame C와 selection matrix S, hybrid loop architecture 부분.",
            domain="control",
        ),
        profile(
            "Impedance Control: An Approach to Manipulation: Part I—Theory",
            problem="불확실한 환경과 접촉하는 동안 motion 또는 force 하나를 hard-tracking하기보다 robot이 원하는 mechanical interaction을 갖도록 해야 한다.",
            model="end-effector displacement x와 external wrench F 사이에 desired inertia M_d, damping D_d, stiffness K_d를 갖는 impedance 관계 M_d ẍ+D_d ẋ+K_d(x−x_d)=F_ext를 둔다.",
            objective="환경과의 closed-loop interaction이 지정된 dynamic compliance/impedance를 보이게 한다.",
            constraints="mechanical impedance가 positive/passive한 범위와 actuator, sensor bandwidth를 만족해야 하며 환경 stiffness와 robot dynamics가 coupled된다.",
            success="접촉 force가 환경 위치 오차에 민감하게 폭증하지 않고, desired compliance에 따라 접촉·충돌·조립 동작이 안정적으로 진행되는 것이다.",
            bottleneck="position control은 environment stiffness를 미리 정확히 알아야 하고 direct force control은 contact geometry와 force reference에 민감하다.",
            changes="position-to-force 또는 force-to-position의 단일 목표 대신 motion-force 관계 자체를 desired second-order dynamics로 설계한다.",
            assumptions=[
                ("external wrench를 측정하거나 추정", "interaction dynamics의 feedback 항을 만들기 위해 필요", "unmeasured friction/impact에서는 desired impedance와 실제 응답이 다름"),
                ("model과 controller bandwidth가 충분", "stable impedance를 구현하기 위해 필요", "sampling delay와 high environment stiffness가 passivity를 깨뜨릴 수 있음"),
            ],
            loop="contact feedback → compliant interaction controller → actuation의 low-level behavior specification이다.",
            anchor="본문의 manipulation impedance definition, desired dynamic relationship와 stability/passivity discussion.",
            domain="control",
        ),
        profile(
            "Probabilistic Roadmaps for Path Planning in High-Dimensional Configuration Spaces",
            problem="고차원 configuration space에서 collision-free start-to-goal path를 반복 query에 사용할 수 있도록 확률적으로 연결된 roadmap을 만든다.",
            model="configuration q∈C_free를 random sample하고 local planner로 이웃 sample을 연결해 graph G=(V,E)를 구성한다.",
            objective="query start/goal을 roadmap에 연결한 뒤 edge cost 합이 짧은 feasible path를 찾는다.",
            constraints="sample이 C_free에 있어야 하고 local connector가 전체 edge에서 collision-free여야 한다. probabilistic completeness는 sampling/connectivity 조건에 의존한다.",
            success="sample 수가 증가하면 path가 존재할 때 graph가 free-space connectivity를 포착하고, query time이 roadmap reuse로 줄어드는 것이다.",
            bottleneck="grid/complete cell decomposition은 DOF가 늘면 지수적으로 비싸고, single-query search는 반복적인 collision checking을 다시 한다.",
            changes="planning과 query를 pre-processing/roadmap construction으로 분리해 고차원 free-space의 connectivity를 random samples와 local connections로 근사한다.",
            assumptions=[
                ("collision checker와 local planner 제공", "sample 간 edge feasibility를 결정하기 위해 필요", "좁은 passage·긴 geodesic path에서 연결 확률이 낮음"),
                ("정적 또는 천천히 변하는 geometry", "roadmap을 재사용하기 위해 필요", "dynamic obstacle·contact mode 변화에서는 stale edge가 됨"),
            ],
            loop="task & motion decision에서 geometric configuration path를 생성해 low-level trajectory tracking으로 넘기는 planning 단계다.",
            anchor="본문의 C-free/roadmap construction, visibility graph와 probabilistic completeness discussion.",
            domain="planning",
        ),
        profile(
            "Rapidly-Exploring Random Trees: A New Tool for Path Planning",
            problem="고차원·비convex configuration space에서 single-query feasible path를 빠르게 찾고 아직 탐색되지 않은 영역을 확장한다.",
            model="tree vertex q_near에 random sample q_rand 방향으로 steer하여 q_new를 만들고, local collision check를 통과하면 edge를 추가한다.",
            objective="start에서 goal region까지의 feasible path를 찾으며, 기본 RRT는 path length 최적화보다 reachability/coverage를 우선한다.",
            constraints="sample/steer domain, bounded step size와 collision-free local edge가 필요하고, kinodynamic variant는 dynamics와 input bounds를 만족해야 한다.",
            success="반복 sampling으로 reachable free-space를 빠르게 커버하고 goal에 도달하는 path를 반환하는 것이다.",
            bottleneck="고차원 nonconvex space에서는 deterministic search가 narrow passage와 많은 homotopy를 다루기 어렵고, full optimal planning은 expensive하다.",
            changes="tree expansion bias를 사용해 unexplored region을 빠르게 탐색하는 randomized single-query planner를 제시한다.",
            assumptions=[
                ("uniform/random sampler가 relevant free space를 덮음", "probabilistic completeness에 필요", "좁은 passage 또는 measure-zero goal에서는 실용적 도달성이 낮음"),
                ("steering/local collision check 가능", "새 vertex를 실제 feasible path로 연결하기 위해 필요", "nonholonomic/contact dynamics가 복잡하면 단순 interpolation이 무효"),
            ],
            loop="task & motion planning에서 current configuration을 executable collision-free path로 바꾸는 single-query 단계다.",
            anchor="본문의 RRT algorithm, Voronoi bias/rapid exploration와 probabilistic completeness discussion.",
            domain="planning",
        ),
        profile(
            "CHOMP: Gradient Optimization Techniques for Efficient Motion Planning",
            problem="고차원 robot trajectory의 collision-free feasibility뿐 아니라 smoothness와 higher-order motion quality를 짧은 시간에 함께 개선한다.",
            model="trajectory ξ=(q₀,…,q_T)를 finite-dimensional vector로 두고 smoothness functional과 obstacle cost를 covariant metric으로 미분한다.",
            objective="F(ξ)=F_smooth(ξ)+F_obs(ξ)를 최소화해 jerk/velocity quality와 collision cost를 동시에 낮춘다.",
            constraints="start/goal boundary와 joint limits를 유지하고 obstacle signed-distance cost가 collision-free basin을 유도한다. local optimization이라 초기 trajectory와 local minima에 의존한다.",
            success="충돌하는 naive initialization도 feasible하고 실행 가능한 smooth trajectory로 수렴하는 것이다.",
            bottleneck="sampling planner path는 jagged하고 post-processing이 필요하며, 좁은 passage용 탐색 heuristic을 sparse obstacle 환경에서도 계속 지불한다.",
            changes="sampled path를 후처리하는 대신 covariant gradient trajectory refinement를 standalone motion planner처럼 사용하고 higher-order smoothness를 objective에 넣는다.",
            assumptions=[
                ("continuous collision cost/gradient 또는 signed distance 제공", "gradient update로 obstacle을 피하기 위해 필요", "discontinuous contact·unknown obstacle에서는 gradient가 없거나 misleading"),
                ("초기 trajectory가 목적 basin과 연결", "local optimizer가 feasible solution으로 갈 수 있게 하기 위해 필요", "다른 homotopy/narrow passage는 local minimum에 갇힘"),
            ],
            loop="task & motion decision → trajectory optimization → position/torque tracking → collision/contact feedback의 planning-control 경계다.",
            anchor="본문의 Introduction, covariant gradient functional, obstacle/smoothness cost와 manipulation·quadruped examples.",
            domain="planning",
        ),
        profile(
            "TrajOpt: A Sequential Convex Optimization Algorithm for Robot Motion Planning",
            problem="nonconvex collision·kinematic constraints를 가진 robot trajectory를 naive initialization에서 빠르게 locally collision-free path로 개선한다.",
            model="waypoint trajectory ξ를 두고 nonlinear cost/constraint를 현재 iterate 주변에서 convex/quadratic subproblem으로 근사하며 trust region 안에서 반복한다.",
            objective="smoothness/path cost와 collision hinge penalty를 최소화하고, outer loop에서 penalty를 높여 continuous-time collision violation을 줄인다.",
            constraints="start/goal, joint limits와 equality/inequality kinematic constraints를 만족해야 하며 swept trajectory의 collision을 discrete waypoint만으로 놓치지 않아야 한다.",
            success="짧은 시간에 local optimum에 도달하면서 continuous-time collision check를 통과하는 실행 가능한 trajectory를 반환하는 것이다.",
            bottleneck="기존 trajectory optimization은 collision constraint가 비convex라 초기 feasible path에 민감하고, sampling planner는 high-dimensional query에서 느리다.",
            changes="collision을 hinge penalty로 다루고 sequential convexification과 trust region, continuous-time collision checking을 결합한다.",
            assumptions=[
                ("collision distance/gradient와 convex local model 제공", "subproblem을 만들기 위해 필요", "contact geometry가 discontinuous하거나 gradient가 부정확하면 infeasible step"),
                ("local optimum이면 충분한 query", "global completeness 대신 실용적 runtime을 선택하기 위해 필요", "나쁜 initialization은 다른 collision-free homotopy를 놓침"),
            ],
            loop="task & motion decision → local trajectory optimization → robot controller의 motion command로 이어지는 planning stage다.",
            anchor="정정된 저자/출판사 PDF의 Introduction, sequential convex optimization, hinge collision penalty와 continuous collision checking 부분.",
            domain="planning",
            body_basis="BODY_FORMULATION_REVIEWED_CORRECTED_SOURCE",
        ),
        profile(
            "MuJoCo: A Physics Engine for Model-Based Control",
            problem="model-based control과 optimization이 사용할 articulated rigid-body 및 contact dynamics를 빠르고 수치적으로 안정적으로 시뮬레이션한다.",
            model="generalized coordinates q와 velocity q̇에 대해 rigid-body equations, constraint/contact forces와 actuator dynamics를 timestep integrator로 전파한다.",
            objective="시뮬레이션 step당 계산량과 constraint/contact solver cost를 낮추면서 control-relevant physical state를 재현한다.",
            constraints="robot XML/model, inertial/geom/contact parameters와 solver tolerances가 주어져야 하고 non-penetration, friction, joint/actuator limits를 근사한다.",
            success="같은 model과 action에서 안정적인 state transition·contact response를 제공해 optimizer/RL이 충분한 rollouts를 수집하는 것이다.",
            bottleneck="고정밀 multi-body/contact simulation은 model-based control의 inner loop를 느리게 하고, oversimplified dynamics는 control policy를 잘못 학습시킨다.",
            changes="constraint-based rigid-body dynamics와 efficient contact solver를 control/optimization-oriented simulator interface로 묶는다.",
            assumptions=[
                ("model parameters가 physical system을 대표", "simulation trajectory가 training signal이 되기 위해 필요", "friction/compliance/actuator mismatch는 sim-to-real gap을 만듦"),
                ("contact model이 task-relevant interaction을 보존", "contact-rich policy 학습에 필요", "deformation·sensor latency·unmodeled impact는 누락될 수 있음"),
            ],
            loop="state/world model의 simulated transition을 제공해 planning·RL·controller training의 inner environment가 된다.",
            anchor="본문의 articulated-body dynamics, constraint/contact formulation과 model-based control application 부분.",
            domain="simulation",
        ),
        profile(
            "Information Theoretic MPC for Model-Based Reinforcement Learning",
            problem="learned 또는 approximate dynamics 아래에서 nonconvex continuous control sequence를 짧은 horizon 안에 online 최적화한다.",
            model="현재 state x_t에서 candidate action sequence를 sampling하고 model rollout cost와 control prior의 KL/path-integral weighting으로 distribution을 갱신한다.",
            objective="receding horizon expected cost와 control-distribution divergence를 최소화하고 첫 action만 실행한 뒤 다시 계획한다.",
            constraints="action bounds, horizon, dynamics model과 finite sample budget이 주어져야 하며 model error가 rollout cost를 오염시킨다.",
            success="매 control cycle마다 낮은-cost sequence를 찾고 disturbance나 model update 뒤에도 재계획이 가능한 것이다.",
            bottleneck="gradient-based nonlinear MPC는 local derivatives와 initialization에 민감하고, model-free RL은 real interaction sample이 많다.",
            changes="information-theoretic/path-integral objective로 sampled trajectory를 cost-weighted update해 derivative 부담을 줄이는 MPC interface를 제시한다.",
            assumptions=[
                ("단기 dynamics model이 usable", "sample rollout의 cost ranking을 위해 필요", "long-horizon model bias는 잘못된 action sequence를 선호함"),
                ("sample budget과 control latency가 충분", "online distribution update를 수행하기 위해 필요", "high-dimensional action 또는 contact mode에서 sampling coverage가 부족함"),
            ],
            loop="estimated state/world model → short-horizon decision → first action → feedback/replan의 online control loop다.",
            anchor="본문의 information-theoretic MPC objective, sampling-based update와 model-based RL/control experiments.",
            domain="control",
        ),
        profile(
            "PDDLStream: Integrating Symbolic Planners and Blackbox Samplers via Optimistic Adaptive Planning",
            problem="symbolic action sequence와 continuous pose·grasp·motion·collision feasibility를 하나의 task-and-motion planning problem에서 결합한다.",
            model="PDDL facts/actions에 stream이라는 black-box conditional sampler를 추가하고, sampled continuous values가 predicate를 satisfy하는지 검사한다.",
            objective="goal을 만족하는 symbolic skeleton과 continuous parameter binding을 찾으면서 stream/sample와 planner call을 줄인다.",
            constraints="symbolic predicate가 실제 geometric state를 충분히 표현하고 sampler가 feasible 값을 생성해야 하며, optimistic planning과 finite sampled problem의 관계가 필요하다.",
            success="task plan의 각 action이 collision-free/kinematically executable하고, 새로운 sample이 추가될 때 solution quality가 개선되는 것이다.",
            bottleneck="순수 symbolic planner는 continuous feasibility를 모르고, 순수 motion planner는 discrete task combinatorics를 모른다.",
            changes="declarative black-box streams와 optimistic adaptive planning으로 symbolic search와 continuous sampling을 interleave한다.",
            assumptions=[
                ("stream sampler와 predicate evaluator가 제공", "continuous parameter를 symbolic planner에 연결하기 위해 필요", "perception uncertainty·stale object pose는 false predicate를 만듦"),
                ("symbolic abstraction이 task-relevant", "finite planning problem으로 환원하기 위해 필요", "contact mode·force state가 빠지면 plan이 execution에서 실패"),
            ],
            loop="task goal → symbolic/TAMP search → motion/interaction execution → updated facts의 planning-feedback interface다.",
            anchor="본문의 PDDLStream problem, stream semantics, optimistic adaptive planning과 robotics domains.",
            domain="planning",
        ),
        profile(
            "Dynamic Whole-Body Motion Generation under Rigid Contacts and Other Unilateral Constraints",
            problem="30+ DOF humanoid가 multiple rigid contacts, balance, actuator·joint·obstacle constraints를 만족하는 dynamic whole-body motion을 생성한다.",
            model="full-body state x=(q,q̇), torque/contact wrench u를 rigid-body dynamics와 contact constraints에 넣고 task functions를 strict hierarchy로 정렬한다.",
            objective="우선순위 task를 만족하는 feasible acceleration/torque/motion을 계산하면서 lower-priority posture·visibility objective를 가능한 만큼 수행한다.",
            constraints="rigid-contact velocity equality, unilateral contact force/friction, joint position/velocity/torque bounds와 obstacle inequality를 동시에 만족한다.",
            success="contact sequence 안에서 dynamic balance와 hard constraints를 유지하며 reference task를 실시간에 가깝게 수행하는 것이다.",
            bottleneck="inverse kinematics는 full dynamics와 unilateral contact/torque feasibility를 직접 보장하지 못하고, sampling은 constraint manifold에서 비싸다.",
            changes="task-function hierarchy를 full dynamics와 equality/inequality constraint solver로 확장하고 multiple planar contact를 reduced form으로 계산한다.",
            assumptions=[
                ("rigid contact와 contact mode를 model", "constraint equation과 reaction force를 계산하기 위해 필요", "compliance/impact·contact switch error가 feasibility를 깨뜨림"),
                ("full-body model과 priority hierarchy가 적절", "여러 task의 충돌을 해결하기 위해 필요", "bad priority는 balance보다 secondary task를 우선시할 수 있음"),
            ],
            loop="whole-body state/contact observation → prioritized motion/force decision → torque/contact execution → feedback의 control layer다.",
            anchor="본문의 Introduction, rigid/unilateral constraints, strict task hierarchy와 HRP-2 multi-contact formulation.",
            domain="control",
        ),
        profile(
            "Hierarchical Quadratic Programming: Fast Online Humanoid-Robot Motion Generation",
            problem="서로 충돌할 수 있는 equality와 inequality task를 strict priority로 정렬하면서 whole-body control frequency로 푼다.",
            model="decision x(velocity/acceleration/torque)에 대해 각 level의 least-square residual과 linearized constraints를 QP로 표현한다.",
            objective="level 1의 task residual을 먼저 최소화하고, 그 optimum을 보존하는 범위에서 lower-level residual을 순차적으로 최소화한다.",
            constraints="joint limits, collision, balance/support polygon와 task equalities/inequalities가 hierarchy level별로 활성화된다.",
            success="incompatible tasks가 있을 때 hard priority와 feasibility를 유지하면서 iterative projection보다 낮은 latency로 solution을 얻는 것이다.",
            bottleneck="pseudo-inverse/iterative projection은 inequality와 changing active set에서 반복 횟수와 numerical cost가 커진다.",
            changes="hierarchical least-square problem을 active-set 기반 QP solver로 직접 풀어 equality와 inequality를 같은 strict hierarchy에 둔다.",
            assumptions=[
                ("task를 현재 state 주변에서 linearize 가능", "online QP를 만들기 위해 필요", "큰 step·contact transition에서는 local constraint가 실제 geometry를 벗어남"),
                ("priority가 안전/feasibility를 올바르게 반영", "lower level을 희생할 기준을 정하기 위해 필요", "잘못된 hierarchy는 충돌 또는 task starvation을 만듦"),
            ],
            loop="whole-body state → hierarchical QP → velocity/acceleration/torque command → constraint feedback의 online controller다.",
            anchor="본문의 hierarchy of quadratic problems, active inequality handling과 humanoid motion-generation experiments.",
            domain="control",
        ),
        profile(
            "Whole-Body Nonlinear Model Predictive Control Through Contacts for Quadrupeds",
            problem="quadruped의 full-body dynamics와 contact timing/location을 미리 고정하지 않고 short-horizon dynamic motion을 최적화한다.",
            model="rigid-body state x=(q,q̇), torque u, contact forces와 contact geometry를 nonlinear dynamics에 넣고 horizon trajectory를 rollout한다.",
            objective="tracking, posture, torque와 regularization cost를 finite horizon에서 최소화하며 contact sequence/timing/location도 solution에 포함한다.",
            constraints="rigid-body dynamics, contact kinematics, unilateral/friction constraints, actuator limits와 state bounds를 만족한다.",
            success="receding-horizon torque가 periodic gait와 dynamic motion을 hardware에서 안정적으로 실행하고 disturbance 뒤 replanning하는 것이다.",
            bottleneck="centroidal/planner-controller 분리는 dynamically infeasible reference를 만들고 tracking controller가 foothold/contact timing을 바꾸지 못한다.",
            changes="explicit differentiable contact dynamics를 whole-body NMPC 안에 넣어 contact를 fixed schedule이 아닌 optimization variable로 둔다.",
            assumptions=[
                ("contact model과 derivatives가 online 계산 가능", "nonlinear solver와 190 Hz급 loop를 위해 필요", "unmodeled compliance·slippage가 model-based action을 틀리게 함"),
                ("짧은 horizon이 future contact를 대표", "계산량과 feedback responsiveness를 절충하기 위해 필요", "장애물·long-horizon task는 local optimum 또는 myopic gait가 됨"),
            ],
            loop="state/contact feedback → whole-body receding-horizon decision → torque/contact → next state의 closed-loop controller다.",
            anchor="본문의 Introduction/B contributions, rigid-body/contact dynamics와 hardware NMPC formulation.",
            domain="control",
        ),
        profile(
            "Logic-Geometric Programming: An Optimization-Based Approach to Combined Task and Motion Planning",
            problem="symbolic action/mode sequence와 continuous trajectory·kinematic·contact feasibility를 함께 선택하는 manipulation TAMP를 푼다.",
            model="logic variables가 mode sequence를 정하고 각 mode에 대응하는 continuous state/trajectory ξ와 nonlinear constraints를 묶은 optimization을 구성한다.",
            objective="논리적으로 유효한 skeleton 중 trajectory cost와 constraint violation을 최소화하는 feasible task-motion solution을 찾는다.",
            constraints="collision, grasp, inverse kinematics, contact/mode transition와 initial/goal conditions가 각 logic branch에서 만족되어야 한다.",
            success="discrete plan이 continuous optimizer에서 실제 feasible trajectory로 연결되고, branch의 cost가 비교되는 것이다.",
            bottleneck="symbolic planner와 geometric optimizer를 순차로 돌리면 서로 infeasibility를 되돌려야 하고, mode combination이 폭발한다.",
            changes="logic-defined mode sequence를 nonlinear program/trajectory optimizer와 결합해 task와 motion을 공동 탐색한다.",
            assumptions=[
                ("모든 relevant mode와 constraint를 사람이 표현", "logic branch를 생성하기 위해 필요", "open-world perception과 novel contact mode는 누락될 수 있음"),
                ("각 branch의 nonlinear optimization이 초기화에서 수렴", "feasible plan을 증명하기 위해 필요", "nonconvex contact problem은 false failure/local minimum을 만들 수 있음"),
            ],
            loop="task goal → logic skeleton → geometric trajectory → execution feedback의 hybrid planning layer다.",
            anchor="공식 IJCAI paper의 logic-geometric problem definition, mode sequence와 trajectory optimization 부분.",
            domain="planning",
            body_basis="ABSTRACT_AND_PROCEEDINGS_FORMULATION",
        ),
        profile(
            "FFRob: Leveraging Symbolic Planning for Efficient Task and Motion Planning",
            problem="large hybrid task-motion search에서 symbolic planning heuristic을 이용해 geometric sample과 motion-feasible action을 효율적으로 조합한다.",
            model="factored symbolic representation, conditional samplers와 motion planner를 사용해 object pose/grasp 같은 continuous value를 lazy하게 생성한다.",
            objective="goal을 달성하는 action skeleton과 feasible parameter binding을 찾으면서 sampler와 expensive motion-planner 호출을 줄인다.",
            constraints="symbolic precondition/effect와 sampled geometric predicate가 일치하고, 각 motion segment가 collision-free여야 한다.",
            success="symbolic search가 promising action sequence를 먼저 제시하고 continuous checks가 실제 executable plan을 확정하는 것이다.",
            bottleneck="uniform sampling은 irrelevant parameter를 많이 만들고, geometric failure를 symbolic search에 늦게 전달한다.",
            changes="forward-chaining symbolic planner를 search guide로 사용해 sample generation과 motion feasibility evaluation을 factor하고 지연시킨다.",
            assumptions=[
                ("conditional sampler와 symbolic model이 충분", "continuous parameter와 action applicability를 연결하기 위해 필요", "잘못된 predicate/sampler는 completeness와 success를 동시에 해침"),
                ("정적 scene과 신뢰할 수 있는 geometry", "계획 결과를 재사용하기 위해 필요", "execution 중 object motion/uncertainty는 plan invalidation을 유발"),
            ],
            loop="task facts → symbolic-guided TAMP → motion execution → fact update의 planning stage다.",
            anchor="본문의 FFRob representation, symbolic search heuristic과 task-and-motion planning experiments.",
            domain="planning",
            body_basis="ABSTRACT_AND_PROCEEDINGS_FORMULATION",
        ),
    ]
)


# Robotics-facing 3D perception, articulated-object interaction, and 3D VLA.
add_many(
    [
        profile(
            "Where2Act: From Pixels to Actions for Articulated 3D Objects",
            problem="articulated object의 관측에서 어느 pixel/part에 어떤 elementary action을 가해야 하는지와 그 action의 성공 가능성을 예측한다.",
            model="RGB-D/point observation의 각 point 또는 pixel에 actionability score를 부여하고, action type·direction·trajectory proposal과 success likelihood를 함께 출력한다.",
            objective="interaction data에서 feasible하고 성공하는 push/pull action의 localized score와 trajectory proposal을 높인다.",
            constraints="object part가 보이고 action primitive의 contact/direction이 실행 가능해야 하며, predicted trajectory는 collision·kinematic constraints를 만족해야 한다.",
            success="훈련에 없던 articulated object instance/category에서도 actionable region을 찾아 실제 articulation을 유발하는 것이다.",
            bottleneck="분류/segmentation만으로는 어디를 어떻게 누르거나 당겨야 하는지 알 수 없고, object category별 hand-coded action model은 novel articulation에 일반화되지 않는다.",
            changes="perception output을 object label이 아닌 dense actionability와 interaction proposal로 바꾸고, learning-from-interaction data loop로 action feasibility를 학습한다.",
            assumptions=[
                ("elementary push/pull action과 local contact로 articulation을 표현", "action proposal space를 정의하기 위해 필요", "복합 grasp·force-controlled interaction은 표현력 밖"),
                ("point/pixel observation이 movable part와 local geometry를 충분히 관측", "actionable region을 위해 필요", "occlusion·transparent/deformable object는 ambiguity"),
            ],
            loop="RGB-D/point observation → actionable pixel·action proposal → contact execution → articulation success feedback/data sampling다.",
            anchor="본문의 Where2Act task, per-point actionability/trajectory/success prediction과 online interaction sampling formulation.",
            domain="manipulation",
            body_basis="FULL_TEXT_FORMULATION_REVIEWED",
        ),
        profile(
            "FlowBot3D: Learning 3D Articulation Flow to Manipulate Articulated Objects",
            problem="unseen articulated object의 point cloud만 보고 각 point가 articulation에 따라 움직일 방향을 추정해 manipulation motion을 계획한다.",
            model="point cloud P의 각 point p에 articulation flow v(p)를 예측하고, 선택한 flow vector를 axis/trajectory estimate와 analytical motion planner에 전달한다.",
            objective="실제 articulation이 큰 방향과 contact point를 선택해 object joint displacement 또는 opening progress를 최대화한다.",
            constraints="rigid-part kinematics, contact/approach geometry, collision-free end-effector trajectory와 robot workspace를 만족해야 한다.",
            success="novel object instance와 category에서 dense flow가 articulation motion을 올바르게 나타내고 real robot이 object를 움직이는 것이다.",
            bottleneck="category-specific pose/action model은 unseen object의 joint axis와 movable part를 알 수 없고, 단순 affordance score는 motion direction을 제공하지 않는다.",
            changes="articulation을 discrete object class가 아니라 point-wise 3D motion field로 예측하고, learned perception과 analytical planner를 연결한다.",
            assumptions=[
                ("한 번의 point cloud에서 articulation flow가 식별 가능", "motion direction prediction을 위해 필요", "대칭·가려진 joint와 multiple plausible axes는 ambiguity"),
                ("flow vector를 robot contact/trajectory로 변환 가능", "downstream planner를 위해 필요", "gripper geometry·obstacle·force limit는 별도 failure"),
            ],
            loop="point cloud → 3D articulation flow → contact/action planning → object motion feedback다.",
            anchor="본문의 dense point-wise 3D articulation flow, flow-vector selection과 analytical motion planning pipeline.",
            domain="manipulation",
            body_basis="FULL_TEXT_FORMULATION_REVIEWED",
        ),
        profile(
            "Ditto: Building Digital Twins of Articulated Objects from Interaction",
            problem="상호작용 전후의 제한된 visual observation으로 articulated object의 part geometry와 kinematic articulation model을 복원한다.",
            model="before/after partial point clouds를 입력으로 implicit neural representation이 part-level geometry를 reconstruct하고 joint type/axis/limits를 추정한다.",
            objective="관측된 geometry와 interaction-induced motion을 설명하는 digital twin의 reconstruction error와 articulation estimation error를 최소화한다.",
            constraints="두 observation이 동일 object의 알려진 interaction 전후를 나타내고, part motion이 underlying kinematic joint로 설명 가능해야 한다.",
            success="reconstructed twin을 simulation/collision computation에 넣어 unseen articulated object의 geometry와 motion을 재현하는 것이다.",
            bottleneck="한 장의 static scan은 hidden part와 articulation axis를 식별하지 못하며, marker/action trajectory에 의존하는 방식은 deployment interaction에 제한된다.",
            changes="active interaction을 sensing action으로 사용하고, pair observation에서 geometry와 articulation을 joint latent implicit representation으로 추정한다.",
            assumptions=[
                ("interaction 전후 변화가 articulation을 충분히 excite", "joint model 식별을 위해 필요", "작은 motion·occlusion은 multiple model ambiguity"),
                ("object가 part-level rigid geometry와 제한된 joint family를 따름", "digital twin parameterization을 위해 필요", "deformable/multi-contact mechanism은 mismatch"),
            ],
            loop="partial scan → exploratory interaction → before/after observation → geometry+joint model → simulation/planning feedback다.",
            anchor="본문의 interactive perception, before/after point-cloud input, implicit geometry와 articulation model estimation formulation.",
            domain="manipulation",
            body_basis="FULL_TEXT_FORMULATION_REVIEWED",
        ),
        profile(
            "VLMaps: Visual-Language Maps for Robot Navigation",
            problem="language instruction을 spatially precise한 3D map location과 navigation goal로 grounding한다.",
            model="video/depth와 camera pose로 3D reconstruction을 만들고, pretrained visual-language feature를 map voxel/point에 투영해 language-indexable spatial map을 유지한다.",
            objective="language query와 map의 visual feature similarity를 높이면서 target location을 geometric navigation graph/obstacle map에 연결한다.",
            constraints="camera pose/depth가 일관되고 2D feature와 3D map 좌표가 정렬되어야 하며, query object/region이 관측 또는 feature vocabulary에 있어야 한다.",
            success="단순 image matching보다 복잡한 relational/spatial language를 map에서 찾고, 여러 robot embodiment가 공유 가능한 navigation target으로 변환하는 것이다.",
            bottleneck="off-the-shelf VLM은 image-language match는 가능하지만 map geometry와 분리되어 spatial precision·obstacle-aware planning을 제공하지 못한다.",
            changes="visual-language feature를 3D reconstruction에 spatial anchor로 fuse해 semantic query와 geometric planning을 같은 state representation에서 수행한다.",
            assumptions=[
                ("SLAM/depth pose와 feature projection이 map 좌표에서 안정적", "spatial anchoring을 위해 필요", "drift·dynamic scene·sparse view는 semantic map을 오정렬"),
                ("언어 query가 visual feature와 map geometry로 grounding 가능", "goal retrieval을 위해 필요", "관계·수량·hidden object는 단순 similarity로 부족"),
            ],
            loop="video/depth exploration → 3D visual-language map → language goal retrieval → geometric navigation → map/pose feedback다.",
            anchor="본문의 3D reconstruction과 pretrained visual-language feature fusion, language-indexed navigation formulation.",
            domain="3d_perception",
            body_basis="FULL_TEXT_FORMULATION_REVIEWED",
        ),
        profile(
            "Open3DSG: Open-Vocabulary 3D Scene Graphs from Point Clouds with Queryable Objects and Open-Set Relationships",
            problem="point cloud에서 고정 label set에 없는 object와 관계까지 query 가능한 open-vocabulary 3D scene graph를 예측한다.",
            model="3D scene을 object node와 directed relation edge로 표현하고, point-cloud geometry와 open-vocabulary semantic embedding을 사용해 node class와 spatial/supportive/semantic relation을 생성한다.",
            objective="object·relation prediction이 known class에 overfit되지 않으면서 graph query에 필요한 node identity와 edge consistency를 높인다.",
            constraints="point cloud segmentation/instance grouping이 안정적이고, open-vocabulary embedding과 relation predicate가 동일 scene coordinate에서 해석되어야 한다.",
            success="scene-graph annotation 없이도 arbitrary object class와 open-set inter-object relationship을 복원해 planning·place recognition query를 지원하는 것이다.",
            bottleneck="기존 3D scene graph predictor는 labeled dataset과 fixed object/relation categories에 의존해 novel household object와 관계를 표현하지 못한다.",
            changes="closed-set supervised graph prediction을 open-vocabulary point-cloud graph construction으로 바꾸고, queryable node/edge를 출력 대상으로 둔다.",
            assumptions=[
                ("foundation semantic feature가 novel object/relation 의미를 보존", "open-set prediction을 위해 필요", "domain-specific geometry/contact relation은 semantic prior만으로 혼동"),
                ("point cloud가 object boundary와 relative geometry를 보존", "graph edge를 위해 필요", "occlusion·sparse scan은 missing node/edge"),
            ],
            loop="3D scan → object/relationship scene graph → language/spatial query → planning or perception decision다.",
            anchor="본문의 fixed-category 3D scene graph bottleneck, open-vocabulary node/edge prediction과 queryable graph formulation.",
            domain="3d_perception",
            body_basis="FULL_TEXT_FORMULATION_REVIEWED",
        ),
        profile(
            "VGGT: Visual Geometry Grounded Transformer",
            problem="여러 장의 scene images에서 별도 iterative geometric optimization 없이 camera, depth, point map과 point track 등 3D attributes를 feed-forward로 추정한다.",
            model="image set를 sequence/tokens로 입력한 Transformer가 모든 view에 대한 camera parameters, dense point maps/depth와 cross-view tracks를 공동 출력한다.",
            objective="multi-view geometric supervision에서 camera/point/depth/track prediction error를 공동으로 최소화한다.",
            constraints="입력 images가 충분한 overlap과 공통 scene geometry를 갖고 camera/projective ambiguity를 학습된 convention으로 해소해야 한다.",
            success="수백 image까지 한 번에 처리하며 camera estimation, depth, dense reconstruction과 tracking에서 usable한 metric geometry를 제공하는 것이다.",
            bottleneck="pairwise reconstruction은 image 수가 늘면 post-processing/fusion과 optimization이 필요하고, classical bundle adjustment는 latency가 크다.",
            changes="3D-inductive optimization pipeline을 large feed-forward Transformer의 joint multi-view prediction으로 reformulate한다.",
            assumptions=[
                ("training 3D data가 deployment camera/scene distribution을 충분히 cover", "metric geometry generalization을 위해 필요", "domain shift·dynamic object는 inconsistent map"),
                ("single forward pass의 correspondence가 geometry ambiguity를 해소", "post-processing 제거를 위해 필요", "textureless/repetitive scene은 scale/pose ambiguity"),
            ],
            loop="multi-view images → camera/point/depth/track state → mapping, localization or collision-aware planning다.",
            anchor="본문의 feed-forward multi-image input, camera·point map·depth·track joint output과 optimization-free 3D task formulation.",
            domain="3d_perception",
            body_basis="FULL_TEXT_FORMULATION_REVIEWED",
        ),
        profile(
            "SUGAR: Pre-training 3D Visual Representations for Robotics",
            problem="복잡한 cluttered multi-object scene에서 semantic identity, 3D geometry와 manipulation affordance를 함께 보존하는 robot-oriented 3D representation을 학습한다.",
            model="RGB-D/point-cloud object와 scene representation을 입력으로 semantic, geometric, affordance prediction heads를 공동 학습하고 downstream recognition/grounding/manipulation에 transfer한다.",
            objective="3D semantic label, geometric structure와 affordance supervision의 multi-task loss를 최소화해 task-relevant representation을 얻는다.",
            constraints="point cloud와 RGB-D frame이 정렬되고, simulation에서 생성한 multi-object labels/affordance가 real clutter와 충분히 대응해야 한다.",
            success="zero-shot 3D recognition, referring-expression grounding과 language-driven manipulation에서 2D/기존 3D representation보다 transfer가 좋아지는 것이다.",
            bottleneck="internet-pretrained 2D feature는 occlusion과 precise 3D localization/affordance를 약하게 표현하고, 기존 3D pretraining은 single-object에 치우친다.",
            changes="3D pretraining target을 semantic recognition만이 아니라 geometry와 affordance까지 포함하는 robot downstream formulation으로 확장한다.",
            assumptions=[
                ("semantic·geometry·affordance supervision이 공통 point representation에 align", "multi-task transfer를 위해 필요", "label noise/shortcut은 downstream manipulation을 오도"),
                ("simulation clutter가 real scene occlusion/contact distribution을 대표", "data scaling을 위해 필요", "재질·센서 noise·동적 clutter는 domain gap"),
            ],
            loop="RGB-D/point cloud → semantic-geometric-affordance state → referring/manipulation decision → robot action feedback다.",
            anchor="본문의 single/multi-object 3D pretraining, semantic·geometry·affordance targets와 robotics downstream formulation.",
            domain="3d_perception",
            body_basis="FULL_TEXT_FORMULATION_REVIEWED",
        ),
        profile(
            "Splat-Nav: Safe Real-Time Robot Navigation in Gaussian Splatting Maps",
            problem="Gaussian Splatting scene representation에서 language-specified goal을 찾고, collision safety와 real-time localization을 유지하는 robot trajectory를 계획한다.",
            model="language-embedded 3DGS를 semantic goal/map state로 사용하고, Splat-Plan이 density 기반 safe polytope corridor와 trajectory를 생성하며 Splat-Loc이 image/depth로 pose를 추정한다.",
            objective="goal-reaching path cost와 replanning latency를 줄이면서 trajectory가 safe corridor/collision constraints를 만족하게 한다.",
            constraints="Gaussian density가 geometry/occupied space를 충분히 나타내고, planned corridor가 실제 robot body와 obstacle 사이의 collision-free margin을 보장해야 한다.",
            success="point-cloud/NeRF 기반 pipeline보다 빠르게 language goal navigation을 수행하면서 simulation과 hardware에서 safety와 localization을 유지하는 것이다.",
            bottleneck="radiance/3DGS map은 rich scene detail을 주지만 직접 collision geometry·pose reference로 쓰기 어렵고, dense optimization localization은 real-time budget을 초과한다.",
            changes="3DGS 위에서 safe planning과 robust localization을 분리한 두 모듈로 구성해 rich visual map을 navigation state/action interface로 만든다.",
            assumptions=[
                ("GSplat density가 obstacle boundary와 free space를 충분히 encode", "safe corridor를 만들기 위해 필요", "view-dependent artifact·sparse capture는 false free space"),
                ("map과 onboard image/depth가 common frame에 연결", "localization/planning feedback을 위해 필요", "frame drift·dynamic scene은 safety margin을 훼손"),
            ],
            loop="streaming image/goal → semantic 3DGS → safe corridor planning+pose localization → motion control → visual/map feedback다.",
            anchor="본문의 Splat-Plan safe polytope corridor, Splat-Loc pose estimation과 Gaussian-map navigation formulation.",
            domain="navigation",
            body_basis="FULL_TEXT_FORMULATION_REVIEWED",
        ),
        profile(
            "EmbodiedSplat: Online Feed-Forward Semantic 3DGS for Open-Vocabulary 3D Scene Understanding",
            problem="agent가 탐색하는 동안 streaming image로 whole scene을 online reconstruct하면서 open-vocabulary semantic query를 거의 real-time으로 지원한다.",
            model="300개 이상 streaming image와 pose를 입력으로 online sparse coefficient field가 3D Gaussians와 CLIP global codebook을 연결해 geometry, color와 semantic field를 갱신한다.",
            objective="novel-view/color/depth reconstruction과 2D·3D semantic segmentation/query consistency를 공동으로 높이며 frame-wise processing latency를 제한한다.",
            constraints="camera pose/stream alignment, incremental memory budget과 sparse semantic coefficients를 유지하면서 scene 전체를 누적해야 한다.",
            success="scene exploration과 동시에 open-vocabulary 3DGS를 만들고 semantic segmentation·rendering·depth query를 downstream embodied task에 제공하는 것이다.",
            bottleneck="offline open-vocabulary 3DGS는 complete image set와 expensive optimization에 의존해 exploration 중 즉시 쓸 수 없고, pure 2D features는 spatial consistency가 약하다.",
            changes="semantic 3D reconstruction을 offline post-processing이 아닌 online feed-forward embodied perception state로 reformulate한다.",
            assumptions=[
                ("streaming view와 pose가 scene coverage를 빠르게 제공", "online reconstruction을 위해 필요", "long-tail unseen area와 pose drift는 holes/semantic misalignment"),
                ("CLIP codebook이 robot query vocabulary를 cover", "open-vocabulary indexing을 위해 필요", "fine-grained affordance·part relation은 부족"),
            ],
            loop="streaming images/poses → online semantic 3DGS → open-vocabulary query/scene state → navigation or manipulation feedback다.",
            anchor="본문의 online whole-scene 3DGS, Online Sparse Coefficients Field+CLIP Global Codebook과 embodied perception objective.",
            domain="3d_perception",
            body_basis="FULL_TEXT_FORMULATION_REVIEWED",
        ),
        profile(
            "RoboSpatial: Teaching Spatial Understanding to 2D and 3D Vision-Language Models for Robotics",
            problem="2D/3D vision-language model이 robot reference frame에서 object 간 spatial relation과 affordance를 이해하도록 학습한다.",
            model="real indoor/tabletop 3D scans와 egocentric images, spatial relation/affordance annotations와 language instruction을 입력·target pair로 사용해 spatial reasoning model을 fine-tune한다.",
            objective="spatial relationship, affordance와 manipulation-relevant instruction prediction error를 줄여 language를 2D/3D location과 action cue로 grounding한다.",
            constraints="annotation의 coordinate/reference frame이 명확하고 image·3D scan·language가 동일 scene/object에 정렬되어야 한다.",
            success="기존 VLM의 verbal spatial description을 넘어 correct reference frame의 relation/affordance prediction과 downstream manipulation grounding을 얻는 것이다.",
            bottleneck="web-scale image-text pretraining은 sophisticated 3D spatial relation과 egocentric robot frame을 거의 supervision하지 않는다.",
            changes="robot spatial reasoning을 위한 real 2D/3D paired dataset과 task-specific supervision을 formulation의 중심으로 두어 VLM의 representation gap을 보완한다.",
            assumptions=[
                ("scene annotation이 robot task에 필요한 relation/affordance를 대표", "dataset supervision을 위해 필요", "annotation ambiguity·frame convention mismatch는 model shortcut"),
                ("learned spatial representation이 novel object/task에 transfer", "generalization을 위해 필요", "unseen geometry/contact는 language prior만으로 불충분"),
            ],
            loop="egocentric image/3D scan+language → spatial/affordance state → grounding/planning/manipulation decision다.",
            anchor="본문의 real indoor/tabletop 3D scan·egocentric data, spatial annotations와 affordance/manipulation downstream formulation.",
            domain="3d_perception",
            body_basis="FULL_TEXT_FORMULATION_REVIEWED",
        ),
        profile(
            "PointVLA: Injecting the 3D World into Vision-Language-Action Models",
            problem="기존 2D-pretrained VLA의 knowledge/data를 유지하면서 point cloud를 추가해 3D geometry가 필요한 robot action을 개선한다.",
            model="RGB image·language와 point cloud를 pretrained VLA에 입력하고, lightweight modular point feature injection block이 3D feature를 vision/action expert context에 삽입해 action chunk를 출력한다.",
            objective="3D-aware robot demonstrations의 supervised action prediction loss를 최소화해 task success를 높이고, frozen/mostly preserved 2D VLA knowledge를 유지한다.",
            constraints="point cloud가 camera/action frame과 정렬되고, 작은 3D data와 modular block의 capacity가 target geometry를 표현해야 하며 inference latency가 control rate를 맞춰야 한다.",
            success="simulation과 real manipulation에서 2D VLA, Diffusion Policy와 3D diffusion baseline보다 3D-sensitive action generalization이 좋아지는 것이다.",
            bottleneck="VLA를 처음부터 3D data로 재학습하는 비용은 크고, 2D input만으로는 occlusion·depth·precise spatial relation이 action에 전달되지 않는다.",
            changes="3D point input을 full VLA retraining의 전제조건이 아니라 pretrained policy에 주입하는 modular interface로 reformulate한다.",
            assumptions=[
                ("point cloud와 RGB/action frame의 calibration이 정확", "3D feature injection을 위해 필요", "extrinsic drift·sparse/occluded point cloud는 wrong action"),
                ("소량 3D demonstrations가 pretrained VLA representation을 보완", "efficient adaptation을 위해 필요", "new embodiment/contact regime는 negative transfer"),
            ],
            loop="RGB+language+point cloud → 3D-injected VLA → action chunk → contact/task feedback다.",
            anchor="본문의 pretrained VLA/3D-data bottleneck, lightweight 3D feature injection block과 simulation·real action-prediction setup.",
            domain="vla",
            body_basis="FULL_TEXT_FORMULATION_REVIEWED",
        ),
    ]
)


# Humanoid whole-body control, loco-manipulation, and active 3D perception.
add_many(
    [
        profile(
            "Perpetual Humanoid Control for Real-time Simulated Avatars",
            problem="noisy human-pose or generated-motion reference를 따라가면서 humanoid가 넘어져도 reset 없이 복구하고 멀리 있는 다음 reference로 계속 이동한다.",
            model="reference motion window와 simulated humanoid state를 입력으로 progressive multiplicative control policy가 joint-level control target을 출력하며, motion progress와 recovery state를 함께 관리한다.",
            objective="reference pose/velocity tracking을 높이면서 physical stability, heading/progress와 fall-recovery 가능성을 유지한다.",
            constraints="high-DOF humanoid dynamics, joint/contact limits와 noisy 또는 discontinuous reference를 만족하고, episode reset 없이 recovery transition을 처리해야 한다.",
            success="대규모 motion set과 disjoint clip sequence를 real-time으로 추종하고, fall 후 self-recovery와 reference 재접속을 지속하는 것이다.",
            bottleneck="기존 physics controller는 perfect motion input과 reset에 의존해 video/language의 noisy·불연속 reference와 fall을 견디지 못한다.",
            changes="PMCP와 recovery-aware motion tracking을 결합해 tracking, long-horizon progress와 failure recovery를 하나의 perpetual controller 문제로 둔다.",
            assumptions=[
                ("reference pose가 humanoid가 추종할 수 있는 범위에 있음", "tracking target을 정의하기 위해 필요", "kinematic infeasibility와 큰 discontinuity는 fall/recovery로 이어짐"),
                ("현재 state와 reference progress로 recovery mode를 판단할 수 있음", "reset 없는 control을 위해 필요", "심한 관측 지연·발 밑 contact loss에서는 잘못된 progress"),
            ],
            loop="reference/pose observation → motion tracking or recovery policy → joint control → simulated body/contact feedback의 perpetual whole-body loop다.",
            anchor="본문의 PMCP, noisy input, fall recovery, far-away reference 재접속과 no-reset perpetual control formulation.",
            domain="humanoid",
            body_basis="FULL_TEXT_FORMULATION_REVIEWED",
        ),
        profile(
            "MaskedMimic: Unified Physics-Based Character Control Through Masked Motion Inpainting",
            problem="full-body target, sparse joint keyframe, joystick, object/path goal, text 등 부분적으로 주어진 constraint를 하나의 physics-based character controller가 만족한다.",
            model="character state와 시간별 partial motion constraint를 mask로 표현하고, conditioned policy가 관측된 target을 유지하면서 missing body motion과 joint control을 생성한다.",
            objective="관측된 constraint tracking과 task goal을 달성하면서 reference-like motion quality, balance와 physical plausibility를 높인다.",
            constraints="mask가 어떤 joint/time constraint를 고정하는지 명확해야 하고, generated completion은 body kinematics, contacts와 actuator/dynamics limits를 만족해야 한다.",
            success="서로 다른 control modality와 그 조합을 specialist policy 교체 없이 같은 controller로 수행하는 것이다.",
            bottleneck="기존 physics controller는 full motion 또는 하나의 narrow command modality에 특화되어 sparse target·text·object interaction을 조합하지 못한다.",
            changes="control을 complete reference tracking이 아니라 masked motion inpainting으로 reformulate해 관측된 부분을 조건으로 물리적으로 feasible한 나머지 motion을 생성한다.",
            assumptions=[
                ("mask와 constraint가 task intent를 충분히 지정", "completion의 자유도를 제어하기 위해 필요", "모호한 sparse target은 여러 incompatible motion을 허용"),
                ("motion corpus와 physics simulator가 desired behaviors를 포함", "unified policy를 학습하기 위해 필요", "unseen contact/tool interaction은 hallucinated completion이 될 수 있음"),
            ],
            loop="partial motion/text/path constraint → masked completion policy → physics action → body/contact feedback의 unified whole-body loop다.",
            anchor="본문의 full-body/VR/any-joint control, path/object/text conditioning과 masked motion inpainting formulation.",
            domain="humanoid",
            body_basis="FULL_TEXT_FORMULATION_REVIEWED",
        ),
        profile(
            "HOVER: Versatile Neural Whole-Body Controller for Humanoid Robots",
            problem="velocity command, pose/keypoint tracking 등 서로 다른 whole-body command를 하나의 real humanoid neural controller가 안정적으로 수행한다.",
            model="humanoid proprioception과 command modality를 conditioned policy에 넣어 joint target/action을 출력하며, command-specific behavior를 shared whole-body dynamics 안에서 표현한다.",
            objective="command tracking과 task completion을 높이면서 balance, contact consistency, joint limits와 actuator effort를 유지한다.",
            constraints="모든 command가 공통 observation/action interface로 retarget 가능해야 하고, high-DOF body dynamics와 real-time inference를 만족해야 한다.",
            success="다양한 command와 motion mode를 별도 controller 없이 simulation·hardware에서 전환하며 추종하는 것이다.",
            bottleneck="task별 controller/retargeting은 behavior coverage와 deployment maintenance를 제한하고, 단일 tracking policy는 command distribution 변화에 brittle하다.",
            changes="command-conditioned neural whole-body policy를 large-scale physics training과 결합해 versatile humanoid controller를 문제의 공통 interface로 만든다.",
            assumptions=[
                ("command representation이 task-relevant whole-body intent를 보존", "shared policy conditioning을 위해 필요", "force/contact intent가 pose·velocity만으로는 빠질 수 있음"),
                ("simulated morphology/dynamics randomization이 real robot variation을 포함", "sim-to-real을 위해 필요", "actuator delay·contact compliance가 tracking을 붕괴"),
            ],
            loop="proprioception+command → neural whole-body action → humanoid contact/dynamics → tracking and balance feedback다.",
            anchor="논문의 command modality, versatile neural whole-body controller와 physical humanoid tracking setting.",
            domain="humanoid",
            body_basis="ABSTRACT_AND_PROCEEDINGS_FORMULATION",
        ),
        profile(
            "SONIC: Supersizing Motion Tracking for Natural Humanoid Whole-Body Control",
            problem="더 크고 다양한 human motion distribution을 실제 humanoid가 자연스럽고 안정적으로 추종하도록 motion-tracking policy의 data·model·training scale을 확장한다.",
            model="reference whole-body motion과 현재 humanoid state를 motion-conditioned policy에 입력해 high-rate joint action을 생성하고, long-horizon tracking을 closed loop로 수행한다.",
            objective="pose/velocity/phase tracking fidelity와 naturalness를 높이면서 balance, contact와 hardware feasibility를 유지한다.",
            constraints="motion retargeting, body morphology, real-time control rate와 diverse motion corpus가 함께 맞아야 한다.",
            success="훈련 분포보다 넓은 motion과 transition을 physical humanoid에서 끊김 없이 수행하고, scale 증가가 실제 tracking robustness로 이어지는 것이다.",
            bottleneck="소규모 motion set·task-specific policy는 motion diversity와 naturalness를 제한하고, 단순 data scaling만으로는 humanoid contact/dynamics failure를 해결하지 못한다.",
            changes="motion tracking을 단일 skill optimization이 아닌 scalable corpus·policy·physics training 문제로 정식화하고 자연스러운 whole-body deployment를 목표로 둔다.",
            assumptions=[
                ("retargeted motion label이 humanoid feasible motion과 충분히 일치", "supervision을 만들기 위해 필요", "human-robot morphology/contact 차이는 infeasible target을 생성"),
                ("scale된 training distribution이 deployment motion을 cover", "zero-shot tracking을 위해 필요", "새로운 contact·object interaction은 OOD"),
            ],
            loop="reference motion → scaled motion-tracking policy → joint/whole-body action → balance/contact feedback다.",
            anchor="논문의 motion-tracking scale, natural humanoid whole-body control 목표와 real-robot deployment claim.",
            domain="humanoid",
            body_basis="ABSTRACT_OR_PROJECT_PAGE_FORMULATION",
        ),
        profile(
            "DeepMimic: Example-Guided Deep Reinforcement Learning of Physics-Based Character Skills",
            problem="kinematic motion example을 guide로 삼아 simulated character가 물리적으로 실행 가능한 locomotion·acrobatic·task skill을 학습한다.",
            model="character state와 reference motion phase를 policy에 입력하고 joint action을 출력하며, pose·velocity·end-effector·root tracking feature로 motion similarity를 계산한다.",
            objective="motion imitation reward와 task/regularization reward의 discounted return을 최대화한다.",
            constraints="physics dynamics, joint/torque/contact limits를 매 time step 만족하고, reference의 phase progression과 task success를 함께 유지해야 한다.",
            success="reference 밖의 perturbation·goal 상황에서도 자연스러운 physics-based skill을 실행하고, hand-authored keyframe에도 적용하는 것이다.",
            bottleneck="kinematic playback은 contact와 passive physics를 제대로 처리하지 못하고, pure task reward RL은 자연스러운 motion과 안정적인 skill acquisition을 보장하지 않는다.",
            changes="example motion을 dense imitation reward로 바꾸어 model-free RL이 task-directed이면서 reference-like한 physical policy를 학습하게 한다.",
            assumptions=[
                ("reference motion이 desired skill의 temporal structure를 담음", "imitation reward를 위해 필요", "잘못 retarget된 contact는 unnatural policy를 유도"),
                ("simulator가 character contact/dynamics를 충분히 대표", "training을 위해 필요", "real robot transfer에는 morphology·actuator gap이 남음"),
            ],
            loop="reference phase+character state → RL policy → physics action → pose/contact/task feedback의 skill-learning loop다.",
            anchor="본문의 motion imitation reward components, task reward와 physics-based skill learning formulation.",
            domain="locomotion",
            body_basis="FULL_TEXT_FORMULATION_REVIEWED",
        ),
        profile(
            "Sim-to-Real: Learning Agile Locomotion For Quadruped Robots",
            problem="randomized simulation에서 학습한 quadruped locomotion policy를 dynamic·unseen terrain의 real robot으로 transfer한다.",
            model="proprioceptive state와 velocity command를 policy에 넣어 leg joint target을 출력하며, teacher는 privileged simulator state를 활용하고 student는 onboard observation으로 distill된다.",
            objective="commanded velocity tracking, stability와 forward progress를 높이면서 energy, slip와 unsafe contact를 줄인다.",
            constraints="quadruped rigid-body/contact dynamics, joint/torque limits, sensor availability와 actuator latency를 만족해야 한다.",
            success="시뮬레이션의 domain randomization과 student observation만으로 real robot이 agile locomotion을 안정적으로 수행하는 것이다.",
            bottleneck="real-world trial-and-error는 위험하고 비싸며, nominal simulation policy는 dynamics·friction·sensor/actuator mismatch에 취약하다.",
            changes="privileged teacher, randomized physics와 real-observable student policy를 분리해 sim-to-real robustness를 locomotion formulation의 핵심으로 둔다.",
            assumptions=[
                ("randomization distribution이 실제 dynamics variation을 cover", "zero-shot transfer를 위해 필요", "unmodeled compliance·terrain은 failure"),
                ("proprioceptive observation으로 local dynamics를 충분히 infer", "student interface를 위해 필요", "시각적 foothold·장애물 정보는 표현되지 않음"),
            ],
            loop="proprioception+velocity command → locomotion policy → leg action/contact → body velocity feedback다.",
            anchor="본문의 privileged teacher/student distillation, dynamics randomization과 real quadruped transfer formulation.",
            domain="locomotion",
            body_basis="FULL_TEXT_FORMULATION_REVIEWED",
        ),
        profile(
            "Learning Quadrupedal Locomotion over Challenging Terrain",
            problem="rough terrain의 height/foothold 구조를 인식하면서 quadruped가 commanded motion을 유지하고 넘어짐을 피한다.",
            model="proprioception과 exteroceptive terrain representation을 recurrent/command-conditioned policy에 넣어 leg-level action을 출력한다.",
            objective="velocity/progress와 terrain traversal success를 최대화하고 body orientation error, collision, slip와 effort를 억제한다.",
            constraints="terrain collision, contact schedule, leg kinematics, torque/velocity limits와 body stability를 만족해야 한다.",
            success="훈련에 없던 heightmap/obstacle 조합에서 perception-aware policy가 안정적으로 foothold를 선택하고 traversal한다.",
            bottleneck="flat-ground locomotion policy는 terrain geometry와 foothold feasibility를 보지 못하며, hand-designed gait는 복잡한 contact transition에 brittle하다.",
            changes="terrain-aware observation과 end-to-end policy learning을 결합해 locomotion을 velocity tracking뿐 아니라 terrain traversal 문제로 확장한다.",
            assumptions=[
                ("sensor terrain map이 relevant obstacle geometry를 관측", "foothold decision을 위해 필요", "occlusion/noisy depth는 wrong contact를 유도"),
                ("training terrains가 deployment의 contact regime을 대표", "generalization을 위해 필요", "slippery·deformable ground는 미모델"),
            ],
            loop="terrain/proprioception → foothold-aware locomotion policy → leg contact → body/terrain feedback다.",
            anchor="본문의 challenging-terrain observation, locomotion policy와 terrain generalization experiment formulation.",
            domain="locomotion",
            body_basis="FULL_TEXT_FORMULATION_REVIEWED",
        ),
        profile(
            "Extreme Parkour with Legged Robots",
            problem="높은 gap/jump, wall, rail, handstand 같은 extreme obstacle을 legged robot이 연속적으로 판단하고 dynamic maneuver로 통과한다.",
            model="perception/terrain state와 desired maneuver를 high-level skill policy에 입력하고, low-level whole-body controller가 contact-aware joint/torque action을 실행한다.",
            objective="obstacle traversal/progress와 landing stability를 높이면서 collision, fall와 excessive impact를 줄인다.",
            constraints="flight/contact phase, foothold/landing geometry, actuator torque·velocity limits와 body orientation constraints를 만족해야 한다.",
            success="훈련된 maneuver를 조합해 unseen obstacle sequence에서 dynamic traversal과 recovery를 유지하는 것이다.",
            bottleneck="일반 보행 policy는 ballistic flight와 high-impact landing을 다루지 못하고, obstacle별 hand-coded controller는 skill composition과 generalization이 약하다.",
            changes="parkour를 locomotion command tracking이 아닌 skill-conditioned whole-body trajectory/control 문제로 두고 diverse dynamic behaviors를 학습한다.",
            assumptions=[
                ("obstacle geometry와 maneuver feasibility를 충분히 추정", "skill selection을 위해 필요", "partial observation은 late takeoff/landing을 초래"),
                ("simulated impact/dynamics가 real robot을 대표", "risk 있는 training을 simulation으로 옮기기 위해 필요", "actuator lag·compliance가 landing을 바꿈"),
            ],
            loop="terrain perception → maneuver/skill selection → dynamic whole-body action → contact/landing feedback다.",
            anchor="본문의 extreme obstacle taxonomy, dynamic maneuver policy/controller와 real legged-robot parkour formulation.",
            domain="locomotion",
            body_basis="FULL_TEXT_FORMULATION_REVIEWED",
        ),
        profile(
            "Walk These Ways: Tuning Robot Control for Generalization with Multiplicity of Behavior",
            problem="같은 locomotion command를 여러 feasible behavior/gait로 수행하도록 policy에 multiplicity를 주어 morphology·terrain·task 변화에 일반화한다.",
            model="proprioceptive state, command와 behavior latent/style variable을 policy에 입력해 joint action을 생성하고, auxiliary reward가 behavior family를 구조화한다.",
            objective="command tracking과 stability를 만족하는 diverse behavior distribution을 학습하며, task-specific reward와 style/regularization reward를 함께 최적화한다.",
            constraints="모든 behavior가 dynamic balance, contact, joint/torque limits를 만족하고 latent variation이 controllable해야 한다.",
            success="한 mode에 과적합하지 않고 새로운 terrain/command/morphology에서 여러 안정적인 gait를 선택·유지하는 것이다.",
            bottleneck="single optimum locomotion policy는 실제 feasible solution의 다양성을 버려 distribution shift와 failure recovery에 취약하다.",
            changes="policy optimization target을 하나의 gait가 아닌 structured multiplicity로 바꾸고, latent-conditioned policy가 behavior manifold를 탐색하게 한다.",
            assumptions=[
                ("task reward만으로는 behavior diversity를 식별할 수 없음", "auxiliary objective 설계를 위해 필요", "잘못된 shaping은 diversity와 task performance를 tradeoff"),
                ("latent variable가 실제 controllable behavior 차이를 유발", "mode selection을 위해 필요", "latent collapse는 multiplicity를 제거"),
            ],
            loop="command+state+behavior latent → locomotion policy → contact/action → task/stability feedback다.",
            anchor="본문의 multiplicity of behavior, auxiliary rewards와 generalization-oriented locomotion policy formulation.",
            domain="locomotion",
            body_basis="FULL_TEXT_FORMULATION_REVIEWED",
        ),
        profile(
            "HumanPlus: Humanoid Shadowing and Imitation from Humans",
            problem="human motion data와 적은 real demonstrations로 humanoid의 whole-body shadowing과 autonomous manipulation skill을 학습한다.",
            model="retargeted human body/hand pose와 humanoid proprioception을 low-level shadowing policy에 넣어 desired body/hand pose를 출력하고, egocentric RGB와 history를 skill BC policy에 넣어 action pose를 예측한다.",
            objective="human pose tracking, whole-body stability와 autonomous task imitation success를 높이며 visual feature가 proprioception에만 의존하지 않도록 regularize한다.",
            constraints="human-to-humanoid retargeting, morphology/actuation mismatch, camera visibility와 joint/contact limits를 처리해야 한다.",
            success="single RGB camera shadowing으로 data를 모으고 최대 수십 demonstration으로 shoe wearing·folding·rearrangement 같은 task를 수행하는 것이다.",
            bottleneck="humanoid data와 teleoperation interface가 부족하고, task-specific low-level controller와 expensive mocap은 skill scale을 제한한다.",
            changes="40-hour human motion으로 task-agnostic low-level controller를 pretrain한 뒤, shadowing data와 vision BC를 연결하는 full-stack formulation을 제시한다.",
            assumptions=[
                ("retargeted human pose가 task intent와 feasible humanoid target을 보존", "low-level conditioning을 위해 필요", "force/contact intent와 morphology 차이는 pose만으로 해결되지 않음"),
                ("egocentric RGB가 manipulation-relevant state를 관측", "vision skill policy를 위해 필요", "occlusion·lighting·hand-object ambiguity는 failure"),
            ],
            loop="human RGB/pose or egocentric observation → pose/action prediction → humanoid whole-body action → task feedback/data collection다.",
            anchor="본문의 40-hour human motion retargeting, Humanoid Shadowing Transformer, Humanoid Imitation Transformer와 real task interface.",
            domain="humanoid",
            body_basis="FULL_TEXT_FORMULATION_REVIEWED",
        ),
        profile(
            "ASAP: Aligning Simulation and Real-World Physics for Learning Agile Humanoid Whole-Body Skills",
            problem="human motion 기반 agile whole-body skill을 simulation에서 학습하면서 실제 humanoid의 dynamics/contact/actuation 차이로 인한 transfer failure를 줄인다.",
            model="reference motion과 simulated body state를 policy/controller에 넣고, real-world physics mismatch를 residual 또는 alignment model로 보정해 joint-level action을 생성한다.",
            objective="motion/skill tracking과 task success를 높이면서 simulation trajectory와 real trajectory의 dynamics discrepancy를 줄인다.",
            constraints="humanoid contact transition, joint/torque limits, residual correction의 안정성과 real-time control budget을 만족해야 한다.",
            success="simulation에서 습득한 agile whole-body skill이 추가적인 task-specific real-world tuning을 최소화하고 hardware에서 재현되는 것이다.",
            bottleneck="simulator에서의 high-DoF contact skill은 효율적으로 학습할 수 있지만, small physics mismatch가 jump·impact·whole-body balance에서 큰 failure를 만든다.",
            changes="sim-to-real을 단순 domain randomization이 아니라 simulation/real physics alignment와 residual dynamics correction을 명시적으로 포함하는 문제로 바꾼다.",
            assumptions=[
                ("sim-real discrepancy가 관측 trajectory에서 학습 가능한 residual로 표현", "alignment를 위해 필요", "unseen contact regime·model bias는 residual extrapolation을 깨뜨림"),
                ("reference skill이 real robot의 kinematic/dynamic feasibility 안에 있음", "transfer target을 위해 필요", "large morphology/actuator mismatch는 controller 한계"),
            ],
            loop="motion/state observation → simulated policy+physics alignment → whole-body action/contact → real dynamics residual feedback다.",
            anchor="논문의 simulation–real physics alignment, residual dynamics와 agile humanoid whole-body skill transfer formulation.",
            domain="humanoid",
            body_basis="ABSTRACT_OR_PROJECT_PAGE_FORMULATION",
        ),
        profile(
            "LangWBC: Language-Directed Humanoid Whole-Body Control via End-to-End Learning",
            problem="자연어 instruction을 humanoid의 locomotion·whole-body control action으로 직접 grounding해 language-directed behavior를 수행한다.",
            model="language command와 humanoid sensory/proprioceptive state를 policy에 입력해 whole-body joint action 또는 motion target을 출력한다.",
            objective="instruction-conditioned task completion과 motion feasibility를 높이며 balance/contact constraint를 유지한다.",
            constraints="언어가 feasible motion intent로 해석되어야 하고, high-level semantic ambiguity를 low-level real-time control interface로 압축해야 한다.",
            success="별도 hand-coded planner나 command-specific decomposition을 최소화하면서 language variation에 대응하는 humanoid control을 얻는 것이다.",
            bottleneck="language model output과 whole-body controller 사이의 interface가 분리되어 semantic intent가 contact·timing·balance로 전달되지 않는다.",
            changes="language conditioning을 whole-body policy의 observable input으로 두고 end-to-end learning을 통해 instruction-to-action formulation을 직접 최적화한다.",
            assumptions=[
                ("instruction이 demonstration/task label과 일관되게 align", "language-conditioned learning을 위해 필요", "underspecified instruction은 unstable/ambiguous behavior"),
                ("training instruction/action coverage가 deployment command를 포함", "generalization을 위해 필요", "새 동사·contact intent는 미학습"),
            ],
            loop="language+humanoid observation → language-directed WBC policy → whole-body action → task/contact feedback다.",
            anchor="논문의 language-directed whole-body control interface와 end-to-end humanoid policy formulation.",
            domain="humanoid",
            body_basis="ABSTRACT_OR_PROJECT_PAGE_FORMULATION",
        ),
        profile(
            "RoboPanoptes: The All-Seeing Robot with Whole-body Dexterity",
            problem="wide-field whole-body sensing과 mobile manipulation을 사용해 humanoid/robot이 주변을 보면서 locomotion, reach와 dexterous manipulation을 협응한다.",
            model="body-mounted camera와 proprioceptive/contact observations를 fused whole-body state로 만들고, locomotion·arm·hand action을 shared planner/controller로 생성한다.",
            objective="관측 가능한 workspace를 넓히고 whole-body dexterous task success와 reachability를 높이면서 collision, balance와 contact feasibility를 유지한다.",
            constraints="카메라 시야·calibration, self/scene occlusion, full-body kinematics, contact/actuator limits와 mobile base stability를 만족해야 한다.",
            success="몸 전체의 sensing/actuation을 활용해 arm-only 또는 head-camera-only system보다 다양한 dexterous manipulation을 수행하는 것이다.",
            bottleneck="고정 시점 perception과 arm-only control은 humanoid의 넓은 workspace·self-occlusion·whole-body balance를 활용하지 못한다.",
            changes="whole-body perception과 dexterity를 분리된 센서/skill이 아닌 하나의 closed-loop mobile manipulation formulation으로 묶는다.",
            assumptions=[
                ("body-mounted sensors가 manipulation target과 contact를 충분히 관측", "all-seeing state를 위해 필요", "occlusion·motion blur·calibration drift는 state를 훼손"),
                ("planner/controller가 perception update latency를 견딤", "whole-body execution을 위해 필요", "fast contact와 hand dexterity는 stale plan을 만듦"),
            ],
            loop="whole-body visual/proprioceptive observation → reach/locomotion/hand decision → action/contact → active sensing feedback다.",
            anchor="논문의 whole-body perception, all-seeing sensor arrangement와 dexterous mobile manipulation system interface.",
            domain="mobile_manipulation",
            body_basis="ABSTRACT_OR_PROJECT_PAGE_FORMULATION",
        ),
        profile(
            "Demonstrating OK-Robot: What Really Matters in Integrating Open-Knowledge Models for Robotics",
            problem="open-vocabulary instruction으로 novel home environment에서 object를 찾고 이동·grasp·drop하는 mobile manipulation pipeline을 구성한다.",
            model="RGB-D mapping/semantic detection, navigation primitives와 grasping primitive를 결합해 language object query를 base pose와 pick/place action으로 변환한다.",
            objective="open-ended object navigation and pick-and-drop success를 높이면서 mapping, navigation과 grasping error의 누적을 줄인다.",
            constraints="object query가 map/detector vocabulary에 grounding되고, base navigation, collision-free motion, grasp reachability와 placement constraints를 만족해야 한다.",
            success="새로운 real home에서 open-vocabulary pick-and-drop를 end-to-end로 수행하고, subsystem 조합에서 어떤 component가 성능을 결정하는지 식별하는 것이다.",
            bottleneck="각 perception·planning·manipulation component가 개별적으로 좋아도 open home의 map, object identity, navigation과 grasp interface가 어긋나면 전체 task가 실패한다.",
            changes="VLM/오픈 지식 model을 완전한 end-to-end policy로 주장하기보다 map·navigation·grasping primitives의 조합과 component interaction을 문제 formulation의 대상으로 둔다.",
            assumptions=[
                ("open-vocabulary detector/LLM이 query object를 scene instance에 grounding", "semantic navigation을 위해 필요", "동일 object·작은/가려진 물체에서 false match"),
                ("정적 map과 primitive가 task horizon 동안 유효", "pipeline composition을 위해 필요", "사람·물체 이동과 grasp 실패 후 replanning은 누적 오류"),
            ],
            loop="language query → map/detection → navigation → grasp/place primitive → scene feedback and replanning다.",
            anchor="본문의 open-home/open-vocabulary formulation, VLM detection·navigation·grasp primitive composition과 real-home protocol.",
            domain="mobile_manipulation",
            body_basis="FULL_TEXT_FORMULATION_REVIEWED",
        ),
        profile(
            "HWC-Loco: A Hierarchical Whole-Body Control Approach to Robust Humanoid Locomotion",
            problem="training과 deployment 환경·robot structure가 달라도 humanoid가 commanded velocity를 유지하고 disturbance에서 안전하게 회복한다.",
            model="low-level whole-body locomotion policies와 high-level planner/selector를 계층화하고, 현재 state·terrain·risk에 따라 goal-tracking policy와 recovery policy를 선택한다.",
            objective="robust optimization 관점에서 uncertain dynamics의 worst-case locomotion return을 높이면서 goal tracking과 safety recovery의 trade-off를 조절한다.",
            constraints="humanoid dynamics, contact/balance, joint/torque limits와 high-level switching/dynamic safety constraints를 만족해야 한다.",
            success="diverse terrain, robot structure와 disturbance에서 안정적으로 걷고, hard failure 전에 recovery behavior로 전환하는 것이다.",
            bottleneck="single policy는 sim-to-real/model mismatch에서 brittle하고 goal tracking과 recovery를 동시에 최적화하면 어느 쪽도 충분히 강하지 않다.",
            changes="policy learning을 robust optimization으로 reformulate하고 high-level selector가 behavior policy를 상황별로 활성화하는 계층 구조를 둔다.",
            assumptions=[
                ("현재 state/observation으로 failure risk와 policy suitability를 판단", "selector timing을 위해 필요", "partial observability는 late switch를 발생"),
                ("recovery policy가 fall boundary 이전에 controllable", "safety를 위해 필요", "irreversible contact·actuator saturation은 복구 불가"),
            ],
            loop="state/terrain/risk → high-level policy selection → low-level WBC action → contact/stability feedback다.",
            anchor="본문의 robust optimization, hierarchical policy selector, goal-tracking/recovery trade-off와 disturbance formulation.",
            domain="humanoid",
            body_basis="FULL_TEXT_FORMULATION_REVIEWED",
        ),
        profile(
            "VIRAL: Visual Sim-to-Real at Scale for Humanoid Loco-Manipulation",
            problem="RGB observation만으로 humanoid가 걸어서 물체를 조작하는 long-horizon loco-manipulation을 simulation에서 학습해 real hardware로 zero-shot transfer한다.",
            model="RGB/proprioception과 task/phase context를 privileged teacher policy와 vision student policy에 입력하고, WBC/PD interface를 통해 base·arms·hands action을 실행한다.",
            objective="navigation·grasp·place loop success와 continuous cycle을 높이면서 tracking, collision/fall와 visual sim-real error를 줄인다.",
            constraints="camera/hand alignment, morphology/contact dynamics, action latency, WBC feasibility와 student가 실제 사용 가능한 observation만 쓰는 조건을 만족해야 한다.",
            success="diverse simulated scenes에서 학습한 RGB student가 Unitree G1에서 최대 수십 cycle의 continuous loco-manipulation을 수행하는 것이다.",
            bottleneck="humanoid loco-manipulation은 vision, navigation, dexterous hand contact와 whole-body balance의 sim-real gap이 동시에 누적되어 single-task demonstrations만으로 scale하기 어렵다.",
            changes="privileged teacher→vision student distillation, delta action/reference initialization, online DAgger+BC와 large simulation compute를 하나의 visual sim-to-real formulation으로 결합한다.",
            assumptions=[
                ("RGB와 proprioception이 object/terrain/contact-relevant cue를 충분히 제공", "vision student를 위해 필요", "occlusion·lighting·hand alignment drift는 failure"),
                ("simulation scale/randomization이 real loco-manipulation variation을 cover", "zero-shot transfer를 위해 필요", "unseen object mass·friction과 actuator lag는 residual"),
            ],
            loop="RGB/proprioception → teacher/student policy → WBC/PD whole-body action → navigation/contact/visual feedback다.",
            anchor="본문의 RGB-based teacher/student pipeline, delta action/reference initialization, DAgger+BC와 continuous real G1 loop.",
            domain="mobile_manipulation",
            body_basis="FULL_TEXT_FORMULATION_REVIEWED",
        ),
    ]
)


# Video/world models, runtime failure detection, recovery, and memory.
add_many(
    [
        profile(
            "DreamGen: Unlocking Generalization in Robot Learning through Video World Models",
            problem="large-scale video world model이 robot policy가 관측하지 못한 visual/dynamics variation을 imagination data로 보완하게 한다.",
            model="video/robot observation history와 action condition을 world model에 넣어 future frames/latent trajectories를 generate하고 policy training data로 사용한다.",
            objective="video prediction/consistency와 imagined policy task return을 높인다.",
            constraints="video model이 action-conditioned, temporally coherent하며 generated frame/state가 robot task distribution과 연결되어야 한다.",
            success="real robot data보다 넓은 visual/task variation을 imagined rollout으로 제공해 policy generalization을 개선하는 것이다.",
            bottleneck="robot demonstrations는 expensive하고 scene variation이 좁아 policy가 deployment shift에 취약하다.",
            changes="video world model을 robot learning data/augmentation source로 사용해 policy generalization을 확장한다.",
            assumptions=[
                ("video-generated future가 action consequence를 보존", "policy training을 위해 필요", "hallucinated contact/physics"),
                ("imagined data가 real distribution을 보완", "generalization을 위해 필요", "model bias가 policy에 증폭"),
            ],
            loop="observation/action history → video world-model imagination → policy training/planning → real feedback의 data loop다.",
            anchor="공식 NVIDIA project page의 video-world-model robot-learning scope; dynamics/action-conditioning details는 본문 확인 필요.",
            domain="world_model",
            body_basis="ABSTRACT_OR_PROJECT_PAGE_FORMULATION",
        ),
        profile(
            "DreamDojo: A Generalist Robot World Model from Large-Scale Human Videos",
            problem="human video로 pretrain한 generalist world model이 diverse robot task의 visual future와 action consequences를 예측한다.",
            model="video history, action/robot condition을 latent/video dynamics model에 넣어 future observation/state representation을 generate한다.",
            objective="large-scale video prediction/pretraining과 robot-conditioned rollout consistency를 높인다.",
            constraints="human motion/video가 robot affordance/dynamics prior를 제공하고 robot action conditioning이 physical scene 변화와 align되어야 한다.",
            success="limited robot data로 novel embodiment/task의 policy planning/learning에 useful world-model prior를 transfer하는 것이다.",
            bottleneck="robot video/action data는 작고, human video는 broad semantics를 갖지만 robot action/control labels가 부족하다.",
            changes="human-video pretraining과 robot action conditioning을 generalist world-model interface로 결합한다.",
            assumptions=[
                ("human video visual dynamics가 robot task prior로 전이", "pretraining benefit을 위해 필요", "embodiment/contact mismatch"),
                ("latent model이 action-relevant state를 유지", "planning을 위해 필요", "visual plausibility와 physical validity divergence"),
            ],
            loop="video/robot observation → latent world model → imagined policy/action evaluation → robot feedback의 world-model loop다.",
            anchor="공식 arXiv abstract/page의 large-scale human-video generalist world-model scope; robot action conditioning details는 본문 확인 필요.",
            domain="world_model",
            body_basis="ABSTRACT_OR_PROJECT_PAGE_FORMULATION",
        ),
        profile(
            "Learning Latent Dynamics for Planning from Pixels",
            problem="pixels만 관측되는 environment에서 planning에 충분한 compact latent dynamics와 reward model을 학습한다.",
            model="image encoder maps o_t→z_t; latent transition f(z_t,a_t) predicts z_{t+1}, reward and terminal/reconstruction signals.",
            objective="latent representation/dynamics prediction과 planning policy return을 optimize한다.",
            constraints="latent state가 Markov/control-sufficient하고 short imagined rollout error가 제한되어야 한다.",
            success="raw pixels에서 model-based planning을 수행해 model-free pixel RL보다 sample-efficient policy를 얻는 것이다.",
            bottleneck="pixel-space prediction과 model-free exploration은 high-dimensional observation과 long-horizon dynamics에서 비싸다.",
            changes="planning을 pixel reconstruction 대신 learned latent dynamics space에서 수행한다.",
            assumptions=[
                ("latent가 reward/dynamics-relevant information을 보존", "planning validity를 위해 필요", "representation aliasing"),
                ("imagined latent rollout이 policy horizon에서 안정", "sample efficiency를 위해 필요", "compounding error"),
            ],
            loop="pixel observation → latent state/dynamics → model-based plan → action → new pixels의 world-model loop다.",
            anchor="본문의 pixel-to-latent dynamics, latent planning objective와 model-based RL experiments.",
            domain="world_model",
        ),
        profile(
            "Dream to Control: Learning Behaviors by Latent Imagination",
            problem="pixel observation에서 learned latent dynamics의 imagination으로 policy를 학습해 real interaction을 줄인다.",
            model="recurrent state-space model가 observation/action history를 deterministic/stochastic latent state로 encode하고 actor-critic이 imagined latent trajectory를 사용한다.",
            objective="latent reconstruction/reward/transition consistency와 imagined return을 jointly optimize한다.",
            constraints="latent RSSM state가 partial observation을 기억하고 model rollout이 control-relevant uncertainty를 유지해야 한다.",
            success="짧은 real data로 latent dream에서 behavior를 학습하고 actual environment로 transfer하는 것이다.",
            bottleneck="raw pixel model-free RL은 sample-expensive하고 one-step observation만으로 partial observability를 처리하기 어렵다.",
            changes="recurrent latent world model과 imagination actor-critic을 end-to-end control pipeline으로 만든다.",
            assumptions=[
                ("recurrent latent state가 hidden state를 충분히 기억", "partial observation control을 위해 필요", "long-memory aliasing"),
                ("model reward/dynamics가 policy-relevant", "imagined learning을 위해 필요", "model exploitation"),
            ],
            loop="pixel/history → latent recurrent world model → imagined actor-critic → real action/feedback의 dream-to-control loop다.",
            anchor="본문의 latent recurrent state-space model, imagination actor-critic과 pixel control setup.",
            domain="world_model",
        ),
        profile(
            "Mastering Diverse Domains through World Models",
            problem="여러 visual/control domain에서 하나의 world model과 imagination-based agent가 diverse task behavior를 학습한다.",
            model="observation/action/reward history를 latent dynamics model로 encode하고 task-conditioned actor/critic이 imagined trajectory를 optimize한다.",
            objective="multi-domain task return과 world-model prediction quality를 jointly maximize한다.",
            constraints="domain/task conditioning, latent state capacity와 diverse observation/dynamics distribution이 shared model에서 분리되어야 한다.",
            success="단일 domain method보다 many tasks/embodiments에서 world model planning and control을 scale하는 것이다.",
            bottleneck="world model은 task별 model/representation을 요구하고 domain diversity가 커질수록 prediction interference가 발생한다.",
            changes="large-scale multi-domain data와 generalized world-model/imagination training으로 domain coverage를 확장한다.",
            assumptions=[
                ("shared latent가 domain-relevant dynamics를 표현", "multi-domain scaling을 위해 필요", "negative transfer/task aliasing"),
                ("simulated imagination과 target domain dynamics가 align", "control benefit을 위해 필요", "unseen contact/physics"),
            ],
            loop="multidomain observation → shared world model → imagined planning/policy → environment feedback의 generalist model loop다.",
            anchor="본문의 multi-domain world-model architecture, latent imagination과 diverse-control formulation.",
            domain="world_model",
        ),
        profile(
            "PIN-WM: Learning Physics-INformed World Models for Non-Prehensile Manipulation",
            problem="non-prehensile object dynamics를 physics prior와 learned world model로 결합해 pushing/rolling action consequence를 예측한다.",
            model="RGB-D/point/object state와 pusher action을 neural dynamics에 넣고 rigid/quasi-static physics residual 또는 constraints를 함께 학습한다.",
            objective="future object pose/contact mode prediction error와 model-based manipulation task cost를 줄인다.",
            constraints="friction/contact geometry, nonpenetration, pusher kinematics와 physics-informed residual assumptions를 만족해야 한다.",
            success="pure data-driven model보다 limited data에서 accurate prediction/planning과 non-prehensile goal success를 얻는 것이다.",
            bottleneck="pushing contact mode가 sparse data에서 underdetermined이고 black-box video prediction은 physically inconsistent할 수 있다.",
            changes="physics-informed inductive bias/constraint를 learned world model에 넣어 non-prehensile manipulation planning을 개선한다.",
            assumptions=[
                ("quasi-static/contact physics가 object motion을 설명", "physics prior를 위해 필요", "dynamic impact/deformation은 residual로 남음"),
                ("vision state estimation과 friction parameter가 usable", "model prediction을 위해 필요", "occlusion/unknown surface"),
            ],
            loop="RGB-D/contact observation → physics-informed world model → push planning/action → object feedback의 model-based loop다.",
            anchor="본문의 physics-informed dynamics, non-prehensile contact variables와 world-model planning setup.",
            domain="world_model",
            body_basis="ABSTRACT_AND_PROCEEDINGS_FORMULATION",
        ),
        profile(
            "Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets",
            problem="large robot video와 action data를 unified world model에서 학습해 visual future와 action-conditioned outcome을 함께 예측한다.",
            model="observation/video latent와 action chunk를 diffusion/denoising model에 condition해 future video/state 및 action trajectory를 생성한다.",
            objective="video reconstruction/prediction과 action-conditioned future consistency를 jointly 학습한다.",
            constraints="video-action temporal alignment, heterogeneous robot embodiment와 diffusion sampling budget이 필요하다.",
            success="video-only world model보다 robot policy learning/planning에 직접 useful한 action-aware representation을 제공하는 것이다.",
            bottleneck="video pretraining은 broad visual dynamics를 갖지만 action causality가 없고 robot action data는 scale/diversity가 작다.",
            changes="video diffusion과 action diffusion을 coupling해 visual prediction과 action consequence model을 unified pretraining task로 둔다.",
            assumptions=[
                ("video/action pairing이 causal signal을 포함", "action-conditioned model을 위해 필요", "offline alignment/noisy action"),
                ("shared latent가 embodiments를 정렬", "large dataset scaling을 위해 필요", "action convention mismatch"),
            ],
            loop="video+action history → unified world model → imagined future/action evaluation → robot feedback의 pretraining loop다.",
            anchor="본문의 coupled video/action diffusion, large robot dataset pretraining과 action-conditioned world-model formulation.",
            domain="world_model",
        ),
        profile(
            "FlowDreamer: A RGB-D World Model with Flow-based Motion Representations for Robot Manipulation",
            problem="RGB-D geometry와 motion/action distribution을 flow-based world model로 예측해 manipulation planning/learning을 돕는다.",
            model="RGB-D observation/history와 action condition을 encode해 future geometric/motion representation을 flow model로 generate한다.",
            objective="future depth/scene motion prediction과 action-conditioned manipulation outcome consistency를 높인다.",
            constraints="RGB-D calibration/visibility, object motion representation과 flow integration budget이 필요하다.",
            success="visual RGB-only world model보다 3D geometry/contact-relevant future prediction을 제공하는 것이다.",
            bottleneck="2D video prediction은 depth/occlusion/metric motion을 잃고 diffusion/flow sampling이 control latency와 충돌한다.",
            changes="RGB-D input과 flow-based motion representation을 robot manipulation world model에 결합한다.",
            assumptions=[
                ("RGB-D observation이 object geometry/motion을 관측", "3D prediction을 위해 필요", "depth noise/occlusion"),
                ("flow future가 action consequence를 보존", "planning을 위해 필요", "contact model error"),
            ],
            loop="RGB-D history+action → flow world model → imagined 3D future → manipulation action feedback의 loop다.",
            anchor="본문의 RGB-D/flow motion representation, action-conditioned future prediction과 manipulation setup.",
            domain="world_model",
        ),
        profile(
            "Can We Detect Failures Without Failure Data? Uncertainty-Aware Runtime Failure Detection for Imitation Learning Policies",
            problem="실패 trajectory label 없이 정상 demonstration/policy signal에서 deployment failure onset을 runtime에 탐지한다.",
            model="policy input/output/history를 scalar anomaly/uncertainty score로 distill하고 sequential OOD/conformal detector가 alarm을 낸다.",
            objective="failure detection delay와 false alarm을 낮추면서 normal execution을 통과시킨다.",
            constraints="normal data signal이 failure와 correlate하고 calibration distribution이 deployment sequence와 sufficiently exchangeable해야 한다.",
            success="failure data collection 없이 impending imitation-policy failure를 early warning하는 것이다.",
            bottleneck="failure cases는 다양하고 수집 비용이 높으며, success-only detector는 confidence calibration과 distribution shift를 놓친다.",
            changes="post-hoc policy signal, sequential OOD와 conformal uncertainty를 modular runtime monitor로 비교한다.",
            assumptions=[
                ("normal training data가 failure boundary와 구분되는 signal을 포함", "failure-free learning을 위해 필요", "novel failure has no detectable precursor"),
                ("calibration distribution이 deployment에서 유지", "conformal threshold를 위해 필요", "closed-loop intervention/shift에서 guarantee 약화"),
            ],
            loop="policy observation/output → uncertainty monitor → alarm/stop/recovery selector → execution feedback의 runtime safety loop다.",
            anchor="본문의 failure-free detection formulation, score distillation/sequential OOD/conformal calibration과 robot tasks.",
            domain="safety",
            body_basis="ABSTRACT_AND_PROCEEDINGS_FORMULATION",
        ),
        profile(
            "SAFE: Multitask Failure Detection for Vision-Language-Action Models",
            problem="여러 VLA manipulation task에서 action/visual state가 실패로 향하는지 공통 failure detector가 판단한다.",
            model="VLA hidden state, visual observation/action history와 task context를 multitask failure classifier/score로 map한다.",
            objective="failure classification/early detection accuracy와 task-generalization을 높이고 false alarm/delay를 낮춘다.",
            constraints="task-conditioned labels/negative examples, temporal failure onset과 detector-to-recovery interface가 필요하다.",
            success="VLA model/ task가 달라도 runtime failure signal이 consistent하게 recovery/termination을 trigger하는 것이다.",
            bottleneck="VLA success score는 task-specific이고 failure modes가 heterogeneous해 single-task binary detector가 확장되지 않는다.",
            changes="multitask failure representation/detection을 VLA runtime layer로 학습하고 task-conditioned signal을 제공한다.",
            assumptions=[
                ("cross-task failure cues가 공유", "multitask detector를 위해 필요", "task-specific contact failures"),
                ("detector score가 recovery timing과 align", "safe intervention을 위해 필요", "late/false alarm"),
            ],
            loop="VLA observation/action → multitask failure score → stop/retry/recovery → feedback의 safety loop다.",
            anchor="본문의 multitask VLA failure detector, temporal score/labels와 recovery-facing evaluation.",
            domain="safety",
        ),
        profile(
            "WorldGym: World Model as An Environment for Policy Evaluation",
            problem="real environment interaction 없이 learned world model을 environment proxy로 사용해 robot/VLA policy를 평가한다.",
            model="initial observation/history와 candidate action을 world model에 넣어 future observation/reward/done을 generate하는 simulator-like API를 만든다.",
            objective="policy ranking/evaluation consistency와 rollout efficiency를 높인다.",
            constraints="world model prediction uncertainty, action conditioning과 evaluation horizon이 실제 environment outcome을 충분히 proxy해야 한다.",
            success="많은 policy candidate를 cheap imagined environment에서 screen하고 real evaluation cost를 줄이는 것이다.",
            bottleneck="real robot policy evaluation은 slow/dangerous하며 static offline metrics는 closed-loop compounding failure를 측정하지 못한다.",
            changes="world model을 policy evaluation environment/API로 operationalize하고 real-vs-imagined performance gap을 분석한다.",
            assumptions=[
                ("world model ranking이 real ranking과 상관", "evaluation surrogate를 위해 필요", "model exploitation/misranking"),
                ("initial state/action distribution이 known", "rollout validity를 위해 필요", "OOD policy action"),
            ],
            loop="logged initial state → imagined world rollout → policy score/ranking → selected real rollout의 evaluation loop다.",
            anchor="본문의 world-model-as-environment API, policy evaluation protocol과 real/imagined comparison.",
            domain="benchmark",
        ),
        profile(
            "WMPO: World Model-based Policy Optimization for Vision-Language-Action Models",
            problem="VLA policy가 expensive real robot rollout 대신 learned world model에서 action sequence를 optimize한다.",
            model="visual-language observation/history를 world model에 condition하고 candidate action chunks/future observations를 rollout해 policy update signal을 만든다.",
            objective="imagined task return/success를 maximize하고 model uncertainty/OOD rollout을 제한한다.",
            constraints="world model이 VLA action space를 condition으로 이해하고 real-data calibration/uncertainty constraint가 필요하다.",
            success="real interaction을 줄이면서 VLA control policy의 performance/generalization을 개선하는 것이다.",
            bottleneck="VLA fine-tuning은 real data가 비싸고 offline behavior cloning은 action consequence를 충분히 평가하지 못한다.",
            changes="world-model rollout을 VLA policy optimization/data augmentation loop에 삽입한다.",
            assumptions=[
                ("world model이 action consequence와 language task reward를 예측", "policy optimization을 위해 필요", "hallucinated success"),
                ("uncertainty-aware rollout selection이 model exploitation을 억제", "safe improvement를 위해 필요", "unknown contact failure"),
            ],
            loop="VLA observation/language → world-model imagined rollouts → policy update → real feedback/calibration의 loop다.",
            anchor="본문의 VLA world-model policy optimization, imagined action rollout과 uncertainty/evaluation setup.",
            domain="world_model",
        ),
        profile(
            "FLARE: A Failure-Aware Framework for Autonomous Correction and Recovery in Visual-Language Robotic Manipulation",
            problem="VLA/visual policy가 manipulation failure를 감지하면 retry/correction/recovery action을 autonomous하게 선택한다.",
            model="current visual/action history에서 failure type/progress를 predict하고 correction/retry/reset policy 또는 action branch를 dispatch한다.",
            objective="task success와 recovery success를 높이고 unnecessary reset/time/unsafe actions를 줄인다.",
            constraints="failure detection/diagnosis가 timely하고 recovery action이 safe/feasible하며 retry budget이 제한된다.",
            success="첫 policy action이 실패해도 autonomous correction으로 long-horizon task를 완료하는 것이다.",
            bottleneck="standard VLA는 failed action 뒤에도 같은 policy를 계속 실행하거나 human intervention을 요구한다.",
            changes="failure-aware monitor와 correction/recovery dispatcher를 visual-language manipulation loop에 명시적으로 추가한다.",
            assumptions=[
                ("failure onset/type이 visual history에서 관측", "branch selection을 위해 필요", "hidden contact/occlusion"),
                ("recovery primitive이 해당 failure를 되돌림", "autonomy를 위해 필요", "irreversible damage/late detection"),
            ],
            loop="visual-language-action → failure monitor → correction/retry/recovery → feedback/replan의 recovery loop다.",
            anchor="본문의 failure-aware framework, failure decision/recovery branches와 visual-language manipulation evaluation.",
            domain="safety",
        ),
        profile(
            "Can VLMs Diagnose and Recover from VLA Manipulation Faults?",
            problem="VLM이 VLA manipulation fault의 원인과 상태를 진단하고 적절한 recovery/rollback action을 선택할 수 있는지 평가한다.",
            model="visual/action trajectory와 task context를 VLM에 넣어 fault type, severity/progress와 recovery instruction을 출력한다.",
            objective="fault diagnosis accuracy와 post-fault task recovery success를 높인다.",
            constraints="fault observation/counterfactual context가 충분하고 VLM diagnosis가 executable recovery primitive로 grounding되어야 한다.",
            success="단순 failure detection을 넘어 원인별 corrective action과 task continuation을 선택하는 것이다.",
            bottleneck="VLA failure는 grasp, occlusion, contact, wrong object 등 원인이 다르지만 binary success signal은 recovery action을 정하지 못한다.",
            changes="VLA-FixBench식 fault taxonomy/benchmark로 VLM diagnosis와 recovery capability를 분리 평가한다.",
            assumptions=[
                ("fault cause가 available visual/action evidence로 구분", "diagnosis를 위해 필요", "ambiguous hidden contact"),
                ("diagnosis가 safe primitive으로 변환", "recovery를 위해 필요", "language plan infeasibility"),
            ],
            loop="fault trajectory → VLM diagnosis → recovery/rollback action → renewed observation의 fault-recovery loop다.",
            anchor="공식 VLA-FixBench page의 fault diagnosis/recovery task scope; exact benchmark protocol은 본문 확인 필요.",
            domain="safety",
            body_basis="ABSTRACT_OR_PROJECT_PAGE_FORMULATION",
        ),
        profile(
            "Temporal Difference Calibration in Sequential Tasks: Application to Vision-Language-Action Models",
            problem="각 timestep confidence가 아니라 sequential task success probability를 calibrated하게 예측해 VLA intervention timing을 결정한다.",
            model="VLA value/success prediction V_t를 temporal-difference target/reward sequence와 calibration mapping으로 보정한다.",
            objective="predicted probability와 empirical future task success의 calibration error를 줄인다.",
            constraints="sequence dependence, nonstationary policy/environment와 calibration set distribution을 고려해야 한다.",
            success="현재 partial progress에서 episode-level success confidence와 failure risk를 reliable하게 표시하는 것이다.",
            bottleneck="per-step classifier confidence는 long-horizon compounding error와 future task completion을 반영하지 못한다.",
            changes="TD-style sequential target과 calibration을 결합해 VLA success prediction을 trajectory-aware signal로 만든다.",
            assumptions=[
                ("TD target/reward가 future success와 연결", "sequential calibration을 위해 필요", "sparse/ambiguous success"),
                ("deployment sequence가 calibration regime과 유사", "probability guarantee를 위해 필요", "distribution shift/intervention"),
            ],
            loop="VLA trajectory → temporal success estimate → calibrated intervention/recovery → updated feedback의 runtime loop다.",
            anchor="본문의 sequential TD calibration objective, VLA success-confidence task와 calibration evaluation.",
            domain="safety",
        ),
        profile(
            "Memory Retrieval in Visuomotor Policies for Long-Horizon Robot Control",
            problem="long-horizon visuomotor policy가 과거 successful/relevant episodes를 retrieve해 current ambiguous state의 action을 보완한다.",
            model="current visual/proprioceptive context를 memory keys와 match하고 retrieved trajectory/skill embedding을 policy input으로 condition한다.",
            objective="retrieval relevance와 current task action/long-horizon success를 높인다.",
            constraints="memory association/temporal indexing, storage/retrieval latency와 retrieved behavior의 current state compatibility가 필요하다.",
            success="현재 observation만으로 모호한 subtask/skill을 기억 기반으로 복원해 repeated trial/failure를 줄이는 것이다.",
            bottleneck="finite context/windowed policy는 long task의 이전 object state·subtask·successful correction을 잃는다.",
            changes="external episodic memory retrieval을 visuomotor policy state/action interface로 추가한다.",
            assumptions=[
                ("past trajectory가 current state와 reusable", "retrieval benefit을 위해 필요", "stale/incorrect memory"),
                ("memory key가 task phase/relevance를 구분", "selection을 위해 필요", "visually similar but different affordance"),
            ],
            loop="current observation → memory retrieve → visuomotor action → outcome/memory update의 long-horizon loop다.",
            anchor="공식 RSS program/paper page의 memory-retrieval visuomotor-control scope; retrieval/update details는 본문 확인 필요.",
            domain="vla",
            body_basis="ABSTRACT_OR_PROGRAM_PAGE_FORMULATION",
        ),
    ]
)


# Cross-embodiment VLA, long-horizon planning, active perception, and evaluation.
add_many(
    [
        profile(
            "A Generalist Agent",
            problem="text, images, discrete actions와 continuous robot/embodied observations를 하나의 sequence model이 처리하는 generalist agent를 만든다.",
            model="각 modality를 token으로 serialize하고 Transformer가 mixed context를 autoregressively model해 task-specific action token을 출력한다.",
            objective="heterogeneous sequence next-token likelihood와 embodied task reward/behavior imitation을 jointly optimize한다.",
            constraints="modalities/action spaces의 serialization과 task/embodiment identifiers가 shared model에서 충돌하지 않아야 한다.",
            success="single agent가 language, vision, games와 robot action setting 사이에서 transfer/generalization하는 것이다.",
            bottleneck="specialized models는 modality/task마다 따로 학습되고 knowledge/action interface가 공유되지 않는다.",
            changes="many tasks와 modalities를 token-level autoregressive objective로 묶어 generalist agent formulation을 제시한다.",
            assumptions=[
                ("tokenization이 modality semantics를 보존", "shared Transformer를 위해 필요", "continuous contact/state detail loss"),
                ("task token/context가 behavior mode를 disambiguate", "multi-task policy를 위해 필요", "unseen task/action interface ambiguity"),
            ],
            loop="multimodal observation/instruction → generalized sequence policy → task action → feedback의 generalist agent loop다.",
            anchor="본문의 multi-domain token interface, autoregressive agent objective와 robotics task formulation.",
            domain="vla",
            body_basis="ABSTRACT_AND_PROCEEDINGS_FORMULATION",
        ),
        profile(
            "AutoRT: Embodied Foundation Models for Large Scale Orchestration of Robotic Agents",
            problem="foundation model이 여러 실제 robot을 자연어 task로 orchestrate해 diverse data를 수집하고 safe action sequence를 실행한다.",
            model="VLM/LLM이 robot state, scene observation, instruction을 받아 high-level task/action proposal을 생성하고 low-level policy/controller가 실행한다.",
            objective="task completion과 useful data collection을 높이면서 safety filters, action validity와 human oversight constraints를 만족한다.",
            constraints="robot capability/tool API, scene grounding, safety policy와 human rejection/monitoring interface가 필요하다.",
            success="large-scale autonomous robot data collection과 multi-robot task orchestration을 사람의 step-level teleoperation 없이 수행하는 것이다.",
            bottleneck="robot data scale는 human operator와 fixed task scripts에 묶이고, LLM text plan은 real robot capability/safety를 직접 알지 못한다.",
            changes="embodied foundation model을 high-level proposer/orchestrator로 사용하고 robot fleet feedback으로 data/skill collection을 닫는다.",
            assumptions=[
                ("LLM proposal이 robot API로 grounding 가능", "orchestration을 위해 필요", "capability mismatch/ambiguous language"),
                ("safety filter가 invalid proposal을 차단", "real deployment를 위해 필요", "unmodeled contact·long-horizon failure"),
            ],
            loop="scene+language → high-level robot action proposal → low-level execution → observation/data feedback의 orchestration loop다.",
            anchor="본문의 multi-robot orchestration/data-collection pipeline, capability constraints와 safety intervention.",
            domain="vla",
            body_basis="ABSTRACT_AND_PROCEEDINGS_FORMULATION",
        ),
        profile(
            "RT-H: Action Hierarchies Using Language",
            problem="long-horizon robot task를 language-specified high-level actions와 reusable low-level skills로 계층화한다.",
            model="vision/language context가 subtask/skill token을 선택하고 skill policy가 current state에서 short-horizon motor action을 출력한다.",
            objective="subtask completion과 full task success를 높이며 high-level plan/low-level execution mismatch를 줄인다.",
            constraints="skill library와 termination/precondition이 정의되고 language action이 executable skill로 grounding되어야 한다.",
            success="long-horizon compositional instruction에서 flat action policy보다 generalization과 reusability를 얻는 것이다.",
            bottleneck="flat VLA는 긴 horizon에서 credit assignment·action latency가 크고, language planner는 motor feasibility를 모른다.",
            changes="language를 action hierarchy/skill invocation interface로 사용해 semantic plan과 motor policy를 분리한다.",
            assumptions=[
                ("skill primitives가 task를 충분히 cover", "hierarchical execution을 위해 필요", "novel contact skill은 library 밖"),
                ("skill boundary/termination이 관측 가능", "handoff를 위해 필요", "premature termination이 task state를 망가뜨림"),
            ],
            loop="language/vision → skill selection → low-level action → subtask feedback/next skill의 hierarchical VLA loop다.",
            anchor="본문의 language action hierarchy, high-level skill selection과 low-level controller interface.",
            domain="vla",
            body_basis="ABSTRACT_AND_PROCEEDINGS_FORMULATION",
        ),
        profile(
            "Gemini Robotics: Bringing AI into the Physical World",
            problem="general multimodal foundation model의 visual/spatial reasoning을 embodied robot action과 safety-aware physical interaction으로 확장한다.",
            model="camera, language, proprioception/task context를 embodied model에 넣어 robot-specific action representation 또는 high-level plan을 출력한다.",
            objective="instruction following, spatial grounding과 physical task success를 높이면서 safe behavior를 유지한다.",
            constraints="embodiment/action adapter, real-time control interface, visual state uncertainty와 safety evaluation이 필요하다.",
            success="novel robot embodiment/task에서 language-visual knowledge가 executable action과 robust interaction으로 transfer되는 것이다.",
            bottleneck="web-scale multimodal models는 physical dynamics/contact/action semantics가 없고 conventional robot policies는 semantic coverage가 작다.",
            changes="embodied reasoning/model adaptation을 general multimodal foundation model과 robot controller 사이의 interface로 제시한다.",
            assumptions=[
                ("multimodal reasoning state가 action-relevant geometry를 보존", "embodied transfer를 위해 필요", "force/contact state가 hidden"),
                ("robot adapter가 model output을 safe action으로 변환", "deployment를 위해 필요", "latency/embodiment mismatch"),
            ],
            loop="vision+language+robot state → embodied reasoning → action/controller → physical feedback의 VLA loop다.",
            anchor="공식 arXiv abstract/page의 physical-world/robotics model scope; detailed action head and limits는 본문 확인 필요.",
            domain="vla",
            body_basis="ABSTRACT_OR_PROJECT_PAGE_FORMULATION",
        ),
        profile(
            "NVIDIA Isaac GR00T N1: An Open Foundation Model for Humanoid Robots",
            problem="heterogeneous humanoid demonstrations와 human/vision-language prior를 open foundation model로 통합해 whole-body robot action을 생성한다.",
            model="vision-language input과 robot state를 dual-system VLM/planner 및 diffusion/action module에 넣어 humanoid joint/end-effector action sequence를 출력한다.",
            objective="instruction-conditioned whole-body task success와 motion quality를 높인다.",
            constraints="humanoid morphology/action normalization, contact/balance/actuator limits와 data/teleoperation alignment가 필요하다.",
            success="새 task/scene 및 humanoid embodiment에서 generalist manipulation/locomotion policy를 fine-tune/deploy하는 것이다.",
            bottleneck="humanoid data scarcity와 high-DOF contact dynamics가 generalist action learning을 어렵게 하고 single-skill controllers는 재사용이 낮다.",
            changes="open humanoid foundation model과 VLM-to-action/diffusion control interface를 large-scale robot/human data에 적용한다.",
            assumptions=[
                ("cross-embodiment/humanoid action schema가 정렬", "foundation policy를 위해 필요", "morphology/contact mismatch"),
                ("high-level semantic output이 balance-aware low-level action으로 decode", "whole-body execution을 위해 필요", "unmodeled contact/fall recovery"),
            ],
            loop="visual/language/proprioception → humanoid foundation action → whole-body controller/contact → feedback의 humanoid VLA loop다.",
            anchor="공식 NVIDIA publication page의 GR00T N1 foundation-model scope; exact model/data/ablation은 본문 확인 필요.",
            domain="humanoid",
            body_basis="ABSTRACT_OR_PROJECT_PAGE_FORMULATION",
        ),
        profile(
            "BC-Z: Zero-Shot Task Generalization with Robotic Imitation Learning",
            problem="language/task description과 demonstrations를 조건으로 robot policy가 training task 조합 밖의 zero-shot manipulation을 수행한다.",
            model="visual observation, language instruction/goal과 proprioception을 conditional behavior-cloning policy에 넣어 action을 예측한다.",
            objective="demonstration action likelihood를 높이고 task description에 따른 goal-conditioned success를 maximize한다.",
            constraints="language task representation과 demonstration coverage가 compositional task structure를 담아야 한다.",
            success="새 task instruction 또는 object combination에서 추가 task-specific data 없이 policy가 행동하는 것이다.",
            bottleneck="task-specific BC는 instruction/object variation이 바뀔 때 새 policy/data를 요구한다.",
            changes="language-conditioned behavior cloning과 broad task demonstrations를 결합해 zero-shot task generalization을 목표로 한다.",
            assumptions=[
                ("language/task token이 relevant goal 차이를 표현", "conditional policy를 위해 필요", "ambiguous or unseen instruction"),
                ("training demonstrations가 compositional primitives를 cover", "zero-shot composition을 위해 필요", "novel contact primitive는 미학습"),
            ],
            loop="language+visual observation → conditional BC action → manipulation execution → goal feedback의 VLA loop다.",
            anchor="본문의 language-conditioned BC, zero-shot task generalization과 robot task setup.",
            domain="vla",
        ),
        profile(
            "Perceiver-Actor: A Multi-Task Transformer for Robotic Manipulation",
            problem="고해상도 multi-view visual input을 scalable하게 처리해 multi-task manipulation action을 예측한다.",
            model="latent Perceiver cross-attention이 pixel/voxel observation을 압축하고 actor head가 task-conditioned end-effector action을 출력한다.",
            objective="multi-task demonstration action likelihood/behavior-cloning loss를 최소화한다.",
            constraints="latent bottleneck이 object/geometry 정보를 보존하고 task conditioning과 action normalization이 공유되어야 한다.",
            success="large visual input과 many task setting에서 convolutional/flat Transformer보다 data/compute 효율적인 manipulation policy를 얻는 것이다.",
            bottleneck="full-resolution visual Transformer는 compute가 크고, task별 policy는 data/representation을 재사용하지 못한다.",
            changes="Perceiver-style latent cross-attention과 task-conditioned actor를 multi-task robot manipulation에 적용한다.",
            assumptions=[
                ("latent tokens가 action-relevant geometry를 유지", "scalable perception을 위해 필요", "fine contact detail compression"),
                ("task token이 policy mode를 disambiguate", "multi-task action을 위해 필요", "unseen task composition"),
            ],
            loop="multi-view visual/task observation → latent actor → end-effector action → feedback의 multi-task VLA loop다.",
            anchor="본문의 Perceiver latent bottleneck, actor action head와 multi-task manipulation formulation.",
            domain="vla",
        ),
        profile(
            "VIMA: General Robot Manipulation with Multimodal Prompts",
            problem="text/image/object prompt를 포함하는 multimodal instruction으로 diverse tabletop manipulation task를 하나의 policy가 수행한다.",
            model="prompt tokens와 visual scene tokens를 Transformer에 넣어 sequential action/waypoint token을 autoregressively 예측한다.",
            objective="expert trajectory action likelihood와 prompt-conditioned task success를 높인다.",
            constraints="prompt modality/tokenization이 task goal/object identity를 보존하고 simulation variation/data split이 compositionality를 평가해야 한다.",
            success="novel prompt/task/object combination에서 같은 policy가 zero-shot generalization하는 것이다.",
            bottleneck="language-only instruction은 object-specific visual goal을 표현하지 못하고 task-specific policies는 compositional prompt를 재사용하지 못한다.",
            changes="multimodal prompts를 policy input의 first-class interface로 만들고 large procedurally generated task/data benchmark를 제공한다.",
            assumptions=[
                ("prompt가 goal과 interaction semantics를 충분히 specify", "conditional policy를 위해 필요", "ambiguous prompt는 action mode를 불명확하게 함"),
                ("simulation task diversity가 real manipulation prior를 제공", "generalization을 위해 필요", "real contact/dynamics transfer"),
            ],
            loop="multimodal prompt+scene → autoregressive action → tabletop contact → task success/next observation의 policy loop다.",
            anchor="본문의 multimodal prompt tokenization, 600K+ trajectory benchmark와 zero-shot generalization formulation.",
            domain="vla",
        ),
        profile(
            "Inner Monologue: Embodied Reasoning through Planning with Language Models",
            problem="LLM high-level plan이 one-shot open-loop로 끝나지 않고 robot execution feedback을 language state로 받아 재계획한다.",
            model="visual/semantic observation과 low-level action result를 textual feedback/monologue로 convert해 LLM planner가 next subgoal/action을 선택한다.",
            objective="long-horizon task completion과 plan consistency를 높이고 failed action 뒤 recovery/replanning을 수행한다.",
            constraints="perception/predicate feedback가 accurate하고 action primitives가 executable하며 planner latency가 acceptable해야 한다.",
            success="실행 중 observation·success·failure를 이용해 계획을 수정하고 long-horizon manipulation/navigation을 완료하는 것이다.",
            bottleneck="LLM 계획은 stale scene과 action failure를 모르고, open-loop language plan은 contact/partial observability에 취약하다.",
            changes="embodied feedback를 inner-language state로 loop에 삽입해 LLM planning을 closed-loop로 만든다.",
            assumptions=[
                ("feedback predicates가 execution state를 충분히 요약", "replanning을 위해 필요", "hidden contact/continuous error를 놓침"),
                ("low-level primitives가 planner action을 실행", "language-to-action을 위해 필요", "primitive failure와 handoff"),
            ],
            loop="observation → language plan → primitive action → success/failure feedback → replan의 embodied planning loop다.",
            anchor="본문의 inner-monologue feedback representation, LLM planner/primitive interface와 long-horizon task setup.",
            domain="vla",
        ),
        profile(
            "SayPlan: Grounding Large Language Models using 3D Scene Graphs for Scalable Robot Task Planning",
            problem="LLM이 open-world spatial relationships를 반영한 scalable robot task plan을 3D scene graph에서 생성한다.",
            model="3D scene graph G=(V,E)와 natural-language goal을 LLM context에 넣고 high-level action sequence를 생성한 뒤 motion planner에 ground한다.",
            objective="goal predicate를 만족하는 symbolic task sequence와 scene-grounded action selection을 얻는다.",
            constraints="scene graph object/relation이 정확하고 graph serialization/context window가 relevant spatial state를 보존해야 한다.",
            success="novel object/scene language instruction에서 LLM plan이 executable robot action sequence로 연결되는 것이다.",
            bottleneck="raw image/text만으로는 LLM이 metric/spatial relation을 안정적으로 추론하기 어렵고 long scene context가 커진다.",
            changes="3D scene graph를 LLM planning context로 사용해 language plan과 spatially grounded task actions를 연결한다.",
            assumptions=[
                ("scene graph predicates가 task-relevant spatial state를 cover", "grounded planning을 위해 필요", "perception error/stale graph"),
                ("action schema와 motion planner가 LLM output을 실행", "TAMP interface를 위해 필요", "contact-rich feasibility absent"),
            ],
            loop="3D map/scene graph+language → LLM task plan → motion/action execution → graph feedback의 grounded planning loop다.",
            anchor="본문의 3D scene-graph serialization, LLM planning과 robot execution/motion-grounding interface.",
            domain="planning",
        ),
        profile(
            "XSkill: Cross Embodiment Skill Discovery",
            problem="서로 다른 robot embodiment의 demonstrations에서 embodiment-agnostic skill representation을 발견하고 transfer한다.",
            model="multi-robot observation/action trajectories를 latent skill z와 embodiment-specific decoder/policy로 factorize한다.",
            objective="trajectory reconstruction/action likelihood와 cross-embodiment skill reuse/goal success를 높인다.",
            constraints="skills가 embodiment-independent task semantics를 담고 action decoder가 각 robot dynamics/kinematics를 만족해야 한다.",
            success="한 embodiment에서 발견한 skill이 다른 robot body/action space에서 재사용되는 것이다.",
            bottleneck="raw action trajectories는 morphology/control frequency가 달라 direct sharing이 불가능하고 skill labels가 부족하다.",
            changes="shared latent skill과 embodiment-conditioned execution을 분리해 unsupervised/cross-embodiment skill discovery를 한다.",
            assumptions=[
                ("different robots가 common task-level skill을 공유", "latent factorization을 위해 필요", "embodiment-specific contact dynamics"),
                ("decoder가 skill을 feasible action으로 변환", "transfer를 위해 필요", "morphology/action limit mismatch"),
            ],
            loop="heterogeneous trajectory → shared skill latent → embodiment controller → task feedback의 transfer loop다.",
            anchor="본문의 cross-embodiment skill latent/decoder formulation과 multi-robot transfer tasks.",
            domain="vla",
        ),
        profile(
            "Scaling Proprioceptive-Visual Learning with Heterogeneous Pre-trained Transformers",
            problem="visual observation과 proprioceptive state를 heterogeneous pretrained Transformer로 scale해 robot policy representation을 개선한다.",
            model="image/video encoder와 proprioceptive encoder의 pretrained tokens를 fusion/adapter하고 action head가 control sequence를 출력한다.",
            objective="robot demonstration action prediction과 cross-task/embodiment generalization을 높인다.",
            constraints="proprioception/action schema, temporal alignment와 pretrained modality feature fusion이 task state를 보존해야 한다.",
            success="visual-only 또는 scratch policy보다 broad robot dataset/task에서 sample/compute scaling benefit을 얻는 것이다.",
            bottleneck="vision foundation feature는 robot joint/contact state를 모르고 scratch multimodal model은 data/compute가 크다.",
            changes="heterogeneous pretrained visual/proprioceptive backbones와 scaling/fusion recipe를 robot learning policy에 결합한다.",
            assumptions=[
                ("pretrained features가 robot state와 align 가능", "multimodal transfer를 위해 필요", "domain/camera/embodiment shift"),
                ("proprioceptive signal이 action ambiguity를 줄임", "policy scaling을 위해 필요", "sensor calibration/latency"),
            ],
            loop="visual+proprioceptive history → fused Transformer policy → action → robot feedback의 multimodal learning loop다.",
            anchor="본문의 heterogeneous pretrained encoders, proprioceptive-visual fusion과 scaling experiment setup.",
            domain="vla",
        ),
        profile(
            "FAST: Efficient Action Tokenization for Vision-Language-Action Models",
            problem="temporal correlation이 강한 continuous robot action chunk를 per-dimension/per-timestep token보다 짧고 효율적으로 표현한다.",
            model="action sequence를 discrete cosine transform frequency coefficients로 압축하고 autoregressive VLA가 coefficient tokens를 예측해 trajectory를 복원한다.",
            objective="action reconstruction error와 token sequence likelihood를 낮추면서 inference token count를 줄인다.",
            constraints="frequency truncation/quantization이 contact-critical high-frequency signal을 보존하고 decoder가 valid action bounds를 출력해야 한다.",
            success="같은 action horizon을 훨씬 적은 token과 latency로 표현하면서 task success를 유지하는 것이다.",
            bottleneck="naive action tokenization은 horizon·dimension에 비례해 sequence가 길고 autoregressive VLA runtime을 제한한다.",
            changes="DCT frequency-space compression을 universal robot action tokenizer로 사용한다.",
            assumptions=[
                ("action trajectory가 frequency-space에서 compressible", "token efficiency를 위해 필요", "abrupt contact correction은 truncation에 손상"),
                ("token reconstruction이 control precision을 보존", "execution을 위해 필요", "quantization/bound clipping"),
            ],
            loop="observation → compressed action tokens → continuous trajectory decode → control/contact feedback의 efficient VLA loop다.",
            anchor="본문의 DCT action representation, token reconstruction과 VLA efficiency/control formulation.",
            domain="vla",
            body_basis="ABSTRACT_AND_PROCEEDINGS_FORMULATION",
        ),
        profile(
            "Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success",
            problem="pretrained VLA를 새 embodiment에 fine-tune할 때 action decoder/objective/chunking을 speed와 success 기준으로 선택한다.",
            model="image-language-proprioception을 OpenVLA-style backbone에 넣고 continuous action chunk를 parallel decoder로 예측한다.",
            objective="action imitation loss와 real/sim task success를 높이면서 inference latency/throughput을 개선한다.",
            constraints="action chunk execution과 feedback rate의 tradeoff, embodiment/action normalization과 fine-tuning data coverage가 필요하다.",
            success="같은 backbone에서 training recipe가 success를 유지하며 substantially faster action generation을 제공하는 것이다.",
            bottleneck="autoregressive VLA decoding은 느리고 action representation/chunk/objective choices가 benchmark 간에 혼합되어 있다.",
            changes="parallel decoding, continuous action, action chunking과 L1 objective를 하나의 fine-tuning recipe로 비교/결합한다.",
            assumptions=[
                ("chunked action이 contact feedback을 충분히 유지", "throughput improvement를 위해 필요", "긴 chunk는 disturbance 반응을 늦춤"),
                ("backbone prior가 new embodiment로 전이", "fine-tuning을 위해 필요", "small data/morphology mismatch"),
            ],
            loop="vision/language/state → parallel action chunk → partial execution → feedback의 speed-success loop다.",
            anchor="본문의 fine-tuning/action-decoder comparison, chunking/parallel decoding과 LIBERO/real setup.",
            domain="vla",
            body_basis="ABSTRACT_AND_PROCEEDINGS_FORMULATION",
        ),
        profile(
            "AtomicVLA: Unlocking the Potential of Atomic Skill Learning in Robots",
            problem="long-horizon VLA가 continuous action을 끝없이 예측하지 않고 atomic skill 단위로 종료·재호출하며 조합한다.",
            model="vision/language/history에서 atomic skill policy와 termination/progress state를 예측하고 skill action chunk를 실행한다.",
            objective="각 atomic skill success와 skill sequence composition을 높이고 premature/late termination을 줄인다.",
            constraints="skill boundary/termination semantics, precondition/effect와 action handoff state가 명확해야 한다.",
            success="failure 후 적절한 atomic skill을 재선택해 long-horizon task completion과 controllability를 개선하는 것이다.",
            bottleneck="monolithic VLA는 long horizon credit assignment와 termination ambiguity로 실패 후 계속 잘못된 action을 낸다.",
            changes="policy action을 atomic skill과 explicit termination semantics로 분해해 closed-loop composition을 만든다.",
            assumptions=[
                ("task가 reusable atomic skills로 factorize", "skill library를 위해 필요", "novel cross-skill contact transition"),
                ("termination/progress signal이 observable", "handoff와 recovery를 위해 필요", "false termination이 state를 망침"),
            ],
            loop="observation/history → atomic skill selection → chunk execution → termination/progress feedback의 hierarchical VLA loop다.",
            anchor="본문의 atomic skill/action termination formulation, long-horizon task and continuation semantics.",
            domain="vla",
        ),
        profile(
            "PALM: Progress-Aware Policy Learning via Affordance Reasoning for Long-Horizon Robotic Manipulation",
            problem="long-horizon manipulation에서 현재 subgoal이 얼마나 진행됐는지와 다음 affordance를 추정해 policy action을 선택한다.",
            model="visual/language/history에서 affordance/progress representation을 만들고 progress-conditioned policy가 action/skill을 출력한다.",
            objective="task progress와 final success를 높이고 redundant/failed action과 subgoal drift를 줄인다.",
            constraints="progress/affordance labels 또는 estimator가 reliable하고 subgoal transition이 action policy와 align되어야 한다.",
            success="중간 상태가 부분적으로 가려지거나 여러 subtask가 있는 task에서 progress-aware policy가 long-horizon success를 개선하는 것이다.",
            bottleneck="flat VLA는 성공 여부와 진행 상태를 구분하지 못해 같은 action을 반복하거나 subtask transition을 놓친다.",
            changes="affordance reasoning과 progress signal을 policy conditioning/selection에 넣어 long-horizon control을 구조화한다.",
            assumptions=[
                ("affordance/progress가 visual state에서 추정 가능", "policy condition을 위해 필요", "occlusion/hidden state ambiguity"),
                ("progress estimate가 action transition과 aligned", "subtask selection을 위해 필요", "false progress triggers wrong skill"),
            ],
            loop="visual/language/history → affordance/progress state → policy action → progress feedback의 long-horizon loop다.",
            anchor="본문의 affordance reasoning, progress-aware policy input과 long-horizon manipulation setup.",
            domain="vla",
        ),
        profile(
            "ActiveVLA: Injecting Active Perception into Vision-Language-Action Models for Precise 3D Robotic Manipulation",
            problem="모호한 3D scene을 수동적으로 관측하지 않고 camera/viewpoint를 움직여 필요한 geometry를 확인한 뒤 precision action을 수행한다.",
            model="VLA가 visual-language state에서 view/attention action 또는 manipulation action을 선택하고 active observation 후 policy를 업데이트한다.",
            objective="3D localization/manipulation success를 높이고 view movement/time과 unnecessary exploration을 줄인다.",
            constraints="camera/robot viewpoint action, scene reconstruction/visibility와 active perception budget가 필요하다.",
            success="occlusion/depth ambiguity에서 active view가 task-relevant geometry를 드러내 precise manipulation을 개선하는 것이다.",
            bottleneck="fixed camera VLA는 hidden side/occluded contact geometry를 추정해야 해 3D action pose가 불안정하다.",
            changes="active perception decision을 VLA policy loop에 넣어 observation과 action을 공동 선택한다.",
            assumptions=[
                ("viewpoint action이 uncertainty를 줄임", "active sensing benefit을 위해 필요", "view change가 hidden region을 못 봄"),
                ("추가 sensing time이 task budget에 허용", "exploration을 위해 필요", "fast contact task에서 delay"),
            ],
            loop="observation → view/action selection → new 3D observation → manipulation action → feedback의 active VLA loop다.",
            anchor="본문의 active-view/action interface, 3D manipulation uncertainty와 precision task formulation.",
            domain="3d_perception",
        ),
        profile(
            "Spatial Memory for Out-of-Vision Manipulation in Vision-Language-Action",
            problem="현재 camera view 밖으로 가려진 object/hand state를 persistent spatial memory에서 복원해 manipulation을 계속한다.",
            model="visual history와 action/pose observation을 object-centric spatial memory M_t에 write/update하고 VLA가 M_t와 current view에서 action을 선택한다.",
            objective="out-of-view object localization/pose consistency와 long-horizon task success를 높인다.",
            constraints="camera/robot pose tracking, memory association/expiry와 object motion model이 hidden state를 정확히 예측해야 한다.",
            success="object가 시야 밖이 된 뒤에도 geometry/goal relation을 유지해 search/reach/retrieve action을 수행하는 것이다.",
            bottleneck="finite image context와 partial observability는 occluded object state를 잃어 VLA가 다시 추측하거나 task를 중단하게 한다.",
            changes="spatial memory를 VLA state interface로 분리해 out-of-view manipulation의 hidden state를 지속한다.",
            assumptions=[
                ("memory association이 동일 object를 추적", "persistent state를 위해 필요", "occlusion/re-identification failure"),
                ("object motion이 memory model로 예측 가능", "out-of-view action을 위해 필요", "unobserved human/object disturbance"),
            ],
            loop="visual/action history → spatial memory update → VLA action → out-of-view feedback/re-observation의 partial-observable loop다.",
            anchor="공식 ICML/OpenReview paper page의 out-of-view spatial-memory problem; memory update/evaluation details는 본문 확인 필요.",
            domain="vla",
            body_basis="ABSTRACT_OR_PROGRAM_PAGE_FORMULATION",
        ),
        profile(
            "Counterfactual VLA: Self-Reflective Vision-Language-Action Model with Adaptive Reasoning",
            problem="현재 action을 바로 실행하기 전에 alternative/counterfactual outcome을 비교해 VLA failure와 ambiguity를 줄인다.",
            model="visual-language state와 candidate action/trajectory를 model/reflector가 평가하고 adaptive reasoning budget으로 action을 선택한다.",
            objective="task success와 expected outcome quality를 높이고 unnecessary reasoning/latency를 줄인다.",
            constraints="counterfactual evaluator가 action consequence를 예측할 정보가 있고 candidate set/compute budget가 제한되어야 한다.",
            success="실행 전 self-reflection이 wrong target/action을 걸러내고 closed-loop manipulation success를 개선하는 것이다.",
            bottleneck="standard VLA는 single action prediction 뒤 physical feedback을 기다려야 하며 uncertainty를 action selection에 반영하지 않는다.",
            changes="candidate action의 counterfactual comparison과 adaptive reasoning을 VLA inference loop에 넣는다.",
            assumptions=[
                ("candidate outcome model이 relative ranking을 제공", "counterfactual selection을 위해 필요", "contact dynamics/model bias"),
                ("추가 inference latency가 failure cost보다 작음", "adaptive reasoning을 위해 필요", "high-frequency control에서 too slow"),
            ],
            loop="observation → candidate actions/counterfactual evaluation → selected action → feedback/reasoning update의 reflective VLA loop다.",
            anchor="본문의 self-reflective/counterfactual action comparison, adaptive reasoning과 manipulation task formulation.",
            domain="vla",
        ),
        profile(
            "Any3D-VLA: Enhancing VLA Robustness via Diverse Point Clouds",
            problem="point cloud의 viewpoint/geometry diversity를 VLA input에 넣어 3D scene variation과 visual distribution shift에 robust하게 한다.",
            model="RGB/point cloud와 language를 3D-aware encoder/adapter로 fuse해 action policy가 3D state-conditioned action을 예측한다.",
            objective="multi-view/point-cloud augmentation consistency와 manipulation action/goal success를 높인다.",
            constraints="point cloud calibration/scale, diverse source geometry와 VLA input adapter가 action-relevant 3D structure를 보존해야 한다.",
            success="camera/viewpoint/object geometry가 바뀌어도 2D-only VLA보다 robust한 manipulation을 수행하는 것이다.",
            bottleneck="2D VLA는 depth/occlusion/spatial relation 변화에 overfit하고 3D retraining data가 부족하다.",
            changes="diverse point-cloud representation을 VLA perception interface에 넣어 3D robustness를 높인다.",
            assumptions=[
                ("point cloud가 visual ambiguity를 줄임", "3D robustness를 위해 필요", "sparse/noisy depth와 calibration error"),
                ("3D augmentation이 real distribution을 cover", "generalization을 위해 필요", "unseen contact/appearance"),
            ],
            loop="RGB+point cloud+language → 3D-aware VLA state → action → manipulation feedback의 robust VLA loop다.",
            anchor="공식 ICML/OpenReview paper page의 point-cloud VLA robustness problem; encoder/ablation details는 본문 확인 필요.",
            domain="3d_perception",
            body_basis="ABSTRACT_OR_PROGRAM_PAGE_FORMULATION",
        ),
        profile(
            "MomaGraph: State-Aware Unified Scene Graphs with Vision-Language Models for Embodied Task Planning",
            problem="scene graph가 object identity만 저장하지 않고 task-relevant state/progress를 유지해 VLM/LLM planner의 embodied action을 grounding한다.",
            model="visual observations를 object/relation/state graph G_t로 parse하고 language goal과 graph history를 planner에 넣어 action/subgoal을 출력한다.",
            objective="state-aware goal planning, predicate satisfaction과 long-horizon task success를 높인다.",
            constraints="graph state/relation extraction, temporal update와 action precondition/effect가 실제 scene 변화를 반영해야 한다.",
            success="object state change와 subtask progress를 graph에 반영해 stale plan/repeated action을 줄이는 것이다.",
            bottleneck="static scene graph는 open/closed/held/used 같은 state transition을 잃어 LLM plan이 현재 affordance와 어긋난다.",
            changes="unified state-aware scene graph를 VLM planning memory와 embodied task interface로 사용한다.",
            assumptions=[
                ("VLM이 state/relation을 정확히 parse", "graph update를 위해 필요", "occlusion/ambiguous affordance"),
                ("graph predicate가 action precondition을 충분히 표현", "planning을 위해 필요", "continuous/contact state omission"),
            ],
            loop="visual history → state-aware scene graph → VLM/LLM task plan → action → graph update feedback의 planning loop다.",
            anchor="공식 ICLR/OpenReview paper page의 state-aware scene-graph planning problem; graph update/benchmark details는 본문 확인 필요.",
            domain="planning",
            body_basis="ABSTRACT_OR_PROGRAM_PAGE_FORMULATION",
        ),
        profile(
            "AVA-VLA: Improving Vision-Language-Action Models with Active Visual Attention",
            problem="VLA가 전체 image를 동일하게 처리하지 않고 action-relevant region에 visual attention을 능동적으로 배분한다.",
            model="vision-language state에서 region/token attention 또는 crop/zoom을 선택하고 attended representation으로 action을 예측한다.",
            objective="target localization/action prediction과 manipulation success를 높이고 irrelevant visual processing을 줄인다.",
            constraints="attention region이 object/contact cue를 포함하고 attention latency/selection budget가 control loop에 허용되어야 한다.",
            success="clutter/occlusion에서 active attention이 wrong object/pose action을 줄이는 것이다.",
            bottleneck="uniform visual encoding은 clutter에 distract되고 fine manipulation point에 필요한 resolution을 제한한다.",
            changes="active visual attention을 VLA inference state/action interface로 삽입한다.",
            assumptions=[
                ("action-relevant region을 attention selector가 찾음", "focus policy를 위해 필요", "selector error/occlusion"),
                ("focus cost가 success gain보다 작음", "active attention을 위해 필요", "high-rate control latency"),
            ],
            loop="image+language → active region selection → action prediction → visual feedback의 attention-controlled VLA loop다.",
            anchor="본문의 active attention mechanism, region selection과 VLA manipulation setup.",
            domain="vla",
        ),
        profile(
            "VLA-Arena: An Open-Source Framework for Benchmarking Vision-Language-Action Models",
            problem="VLA model의 language following, task success, robustness와 embodiment/generalization을 공통 executable benchmark에서 비교한다.",
            model="task/instruction, visual/proprioceptive observation과 action API를 standardized evaluation harness로 연결한다.",
            objective="model performance를 success, efficiency, robustness/coverage와 failure outcome으로 비교 가능하게 만든다.",
            constraints="robot/simulator environment, task split, action mode, prompt protocol과 evaluation seed/trial이 고정되어야 한다.",
            success="같은 checkpoint/protocol에서 서로 다른 VLA의 headline result와 failure mode를 재현 가능하게 비교하는 것이다.",
            bottleneck="VLA 논문은 task subset·prompt·action horizon·hardware가 달라 reported success를 직접 비교하기 어렵다.",
            changes="open-source arena/evaluation protocol과 task/metric harness를 제공해 VLA comparison을 표준화한다.",
            assumptions=[
                ("benchmark tasks가 target capabilities를 대표", "evaluation validity를 위해 필요", "narrow tasks가 robustness를 과장"),
                ("action/environment adapters가 공정", "model comparison을 위해 필요", "hardware/controller difference"),
            ],
            loop="instruction+observation → VLA action → environment/task feedback → standardized metrics의 evaluation loop다.",
            anchor="본문의 VLA-Arena task/metric/protocol definition과 open evaluation framework.",
            domain="benchmark",
        ),
    ]
)


# Contact-rich extensions and tactile/3D dexterity frontiers.
add_many(
    [
        profile(
            "Dense Object Nets: Learning Dense Visual Object Descriptors By and For Robotic Manipulation",
            problem="novel object instance의 corresponding points와 task landmarks를 RGB-D observation에서 찾아 manipulation action을 generalize한다.",
            model="image/depth pixel을 dense descriptor field f(o,p)로 map하고 same object points가 viewpoint/object instance 사이에서 가까워지도록 학습한다.",
            objective="correspondence descriptor distance와 downstream grasp/pose/action error를 최소화한다.",
            constraints="object appearance/geometry가 observations 사이에 overlap되고 descriptors가 task-relevant surface correspondence를 보존해야 한다.",
            success="few demonstrations로 novel object instance에 grasp/interaction point를 transfer하는 것이다.",
            bottleneck="global category feature는 exact manipulation point를 구분하지 못하고 pixel coordinate는 object pose/viewpoint 변화에 brittle하다.",
            changes="dense object-centric descriptor를 학습해 image pixels를 cross-instance manipulation correspondence로 사용한다.",
            assumptions=[
                ("corresponding surface points가 관측되고 labeling/interaction supervision 가능", "descriptor training을 위해 필요", "occlusion/textureless object에서 correspondence ambiguity"),
                ("descriptor correspondence가 action affordance와 일치", "manipulation transfer를 위해 필요", "semantic match가 contact feasibility를 보장하지 않음"),
            ],
            loop="RGB-D observation → dense object correspondence/landmark → grasp/action → visual feedback의 3D manipulation loop다.",
            anchor="본문의 dense descriptor field, object correspondence training과 robot manipulation transfer task.",
            domain="manipulation",
            body_basis="ABSTRACT_AND_PROCEEDINGS_FORMULATION",
        ),
        profile(
            "DIGIT: A Novel Design for a Low-Cost Compact High-Resolution Tactile Sensor with Application to In-Hand Manipulation",
            problem="손끝의 contact geometry/force를 저비용·소형 sensor로 측정해 in-hand manipulation feedback에 사용한다.",
            model="camera가 elastomer/marker deformation image를 관측하고 calibration model이 tactile image를 contact location, deformation/force feature로 변환한다.",
            objective="compact sensor의 spatial resolution과 force/shape estimation fidelity를 높이면서 hardware cost/size를 낮춘다.",
            constraints="sensor skin, illumination, camera calibration과 contact area가 stable해야 하며 hand integration에서 occlusion/latency가 제한되어야 한다.",
            success="low-cost tactile signal이 in-hand grasp adjustment/object rotation을 distinguish할 만큼 informative한 것이다.",
            bottleneck="wrist/force-torque sensor는 distributed fingertip contact를 잃고 기존 high-resolution tactile hardware는 robot hand scale/cost에 부적합하다.",
            changes="compact camera-based tactile design과 open hardware/processing pipeline으로 fingertip observation interface를 만든다.",
            assumptions=[
                ("elastomer deformation과 contact force/geometry가 calibration으로 recoverable", "tactile estimate를 위해 필요", "wear/hysteresis/temperature drift"),
                ("sensor image rate가 in-hand feedback에 충분", "closed-loop manipulation을 위해 필요", "high-speed slip/contact는 delay에 민감"),
            ],
            loop="fingertip contact → tactile image → force/geometry state → hand action의 sensing-control loop다.",
            anchor="본문의 DIGIT mechanical/optical design, tactile calibration과 in-hand manipulation application.",
            domain="tactile",
            body_basis="ABSTRACT_AND_PROCEEDINGS_FORMULATION",
        ),
        profile(
            "DeXtreme: Transfer of Agile In-hand Manipulation from Simulation to Reality",
            problem="high-DOF hand가 object를 빠르게 reorient하는 agile in-hand manipulation policy를 simulation에서 학습해 real hardware로 transfer한다.",
            model="hand proprioception와 object/goal state를 policy에 넣어 joint torque/action을 출력하고 simulated contact dynamics에서 RL한다.",
            objective="object pose/orientation goal과 regrasp progress를 maximize하면서 falls, collision과 torque cost를 줄인다.",
            constraints="hand kinematics/contact/friction, actuator limits와 real sensor/action rate를 simulator에 반영해야 한다.",
            success="agile multi-contact reorientation을 sim-to-real에서 안정적으로 수행하는 것이다.",
            bottleneck="in-hand dynamics는 contact mode와 friction에 민감하고 real trial이 비싸 high-DOF exploration을 제한한다.",
            changes="large-scale simulation/domain randomization과 policy transfer pipeline으로 agile hand skill을 학습한다.",
            assumptions=[
                ("randomized simulation이 real contact/dynamics를 cover", "zero-shot transfer를 위해 필요", "unmodeled compliance/friction은 object drop"),
                ("proprioception이 object state를 추정하기 충분", "vision-free/limited sensing policy를 위해 필요", "object pose ambiguity와 slip detection failure"),
            ],
            loop="hand proprioception/object goal → torque policy → multi-contact dynamics → tactile/proprioceptive feedback의 dexterous loop다.",
            anchor="본문의 agile in-hand task, simulation training/domain randomization과 real transfer protocol.",
            domain="manipulation",
            body_basis="ABSTRACT_AND_PROCEEDINGS_FORMULATION",
        ),
        profile(
            "Control-Limited Differential Dynamic Programming",
            problem="nonlinear dynamics와 bounded control에서 trajectory를 locally optimize하면서 control limits를 위반하지 않는다.",
            model="discrete dynamics x_{t+1}=f(x_t,u_t)와 finite-horizon cost를 두고 local quadratic value expansion을 backward/forward pass로 갱신한다.",
            objective="Σ_t l(x_t,u_t)+l_T(x_T)를 최소화한다.",
            constraints="u_min≤u_t≤u_max와 state/terminal constraints를 local linear-quadratic subproblem에서 유지해야 한다.",
            success="bounded actuator를 가진 robot에서 빠른 receding-horizon trajectory optimization과 feasible control을 얻는 것이다.",
            bottleneck="unconstrained DDP가 actuator saturation 뒤에는 실제 trajectory와 다른 local model을 만들고, generic NLP는 online control에 느리다.",
            changes="control-limit active set/box constraints를 DDP backward pass에 직접 포함한다.",
            assumptions=[
                ("dynamics가 differentiable하고 local quadratic approximation 유효", "DDP update를 위해 필요", "contact discontinuity는 model expansion을 깨뜨림"),
                ("local solution이 충분", "global planning 대신 online speed를 위해 필요", "bad initial trajectory는 local minimum"),
            ],
            loop="state estimate → finite-horizon DDP → first bounded action → next state feedback의 model-based control loop다.",
            anchor="본문의 control-limited DDP derivation, active bound handling과 robot trajectory optimization examples.",
            domain="control",
        ),
        profile(
            "In-Hand Manipulation via Motion Cones",
            problem="hand가 object를 grasp한 상태에서 allowable contact motion 방향을 분석해 object reorientation/translation을 계획한다.",
            model="contact geometry, friction cones와 hand/object twist를 motion cone으로 map해 feasible object velocity/twist set을 계산한다.",
            objective="target object pose/twist를 달성할 수 있는 contact motion sequence와 hand action을 선택한다.",
            constraints="Coulomb friction, unilateral contact, grasp kinematics와 non-slipping/rolling constraints를 만족해야 한다.",
            success="contact mode와 feasible motion set을 활용해 in-hand manipulation trajectory를 효율적으로 계획하는 것이다.",
            bottleneck="general-purpose motion planner는 high-dimensional contact mode와 friction feasibility를 직접 탐색하기 어렵다.",
            changes="contact geometry에서 induced object motion의 feasible cone을 analytic representation으로 만들어 planning search를 줄인다.",
            assumptions=[
                ("rigid body와 friction/contact model을 앎", "motion cone derivation을 위해 필요", "deformation/unknown friction은 cone을 왜곡"),
                ("contact mode/hand configuration이 식별", "piecewise feasible motion을 위해 필요", "mode switch transition이 실패"),
            ],
            loop="hand/object state → motion-cone contact plan → finger action → force/slip feedback의 in-hand planning loop다.",
            anchor="본문의 motion cone definition, contact/friction constraints와 in-hand manipulation planning experiments.",
            domain="manipulation",
        ),
        profile(
            "Towards Tight Convex Relaxations for Contact-Rich Manipulation",
            problem="nonconvex contact-rich manipulation dynamics를 tractable convex optimization으로 relax하면서 solution bound의 looseness를 줄인다.",
            model="robot/object trajectory, contact force와 complementarity variables를 polynomial/linearized constraints로 표현하고 convex relaxation을 구성한다.",
            objective="task/trajectory cost와 contact constraint violation을 최소화하고 relaxation gap을 줄인다.",
            constraints="nonpenetration, unilateral/friction contact, dynamics, joint/actuator limits가 relaxation 또는 valid feasible recovery를 통해 반영된다.",
            success="convex solver가 global lower bound와 실제 executable contact trajectory에 가까운 solution을 빠르게 제공하는 것이다.",
            bottleneck="contact mode enumeration과 complementarity는 global optimization을 어렵게 하고 local solver는 초기화에 민감하다.",
            changes="contact dynamics의 tighter convex envelopes/relaxations를 설계해 global planning tractability와 solution quality를 절충한다.",
            assumptions=[
                ("contact geometry/friction model이 알려짐", "relaxation을 구성하기 위해 필요", "model error와 compliance gap"),
                ("relaxed solution을 feasible trajectory로 round/recover 가능", "optimization result를 실행하기 위해 필요", "large relaxation gap에서 false feasibility"),
            ],
            loop="scene/contact state → convex contact trajectory optimization → action/force execution → feedback의 model-based planning loop다.",
            anchor="본문의 contact-rich optimization formulation, convex relaxation/tightness 분석과 manipulation examples.",
            domain="manipulation",
        ),
        profile(
            "Physics-Driven Data Generation for Contact-Rich Manipulation via Trajectory Optimization",
            problem="실제 contact-rich demonstration 수집 없이 physics model과 trajectory optimization으로 policy training data를 생성한다.",
            model="robot/object state x_t, contact dynamics와 action u_t를 physics simulator에 넣어 feasible trajectory를 optimize하고 demonstrations로 저장한다.",
            objective="task goal/progress와 contact stability를 높이는 trajectory를 만들고 collision/force/effort cost를 제한한다.",
            constraints="rigid/contact dynamics, friction, nonpenetration, actuator/kinematic limits와 terminal goal을 만족해야 한다.",
            success="generated trajectory가 learned policy의 data diversity와 contact generalization을 실제 task에서 높이는 것이다.",
            bottleneck="contact-rich data는 human teleoperation과 trial failure 비용이 높고, purely learned generator는 physical infeasibility를 만든다.",
            changes="physics-driven trajectory optimization을 data-generation mechanism으로 사용해 contact-consistent supervision을 만든다.",
            assumptions=[
                ("simulator/contact model이 real manipulation을 대표", "generated data의 validity를 위해 필요", "friction/compliance mismatch가 systematic bias"),
                ("optimized trajectory가 policy distribution을 충분히 cover", "learning transfer를 위해 필요", "solver local minima가 narrow behavior를 만듦"),
            ],
            loop="physics state/model → optimized contact trajectory → policy training → real feedback의 data-generation loop다.",
            anchor="본문의 physics-driven generation, trajectory optimization constraints와 contact-rich manipulation data setup.",
            domain="robot_data",
            body_basis="ABSTRACT_AND_PROCEEDINGS_FORMULATION",
        ),
        profile(
            "Complementarity-Free Multi-Contact Modeling and Optimization for Dexterous Manipulation",
            problem="다중 contact의 mode switching과 complementarity constraint를 numerical optimization이 다루기 쉬운 smooth formulation으로 바꾼다.",
            model="hand/object state와 contact force/penetration variables를 smooth contact potential/constraint로 표현해 trajectory optimization을 구성한다.",
            objective="dexterous task cost와 contact consistency/penetration penalty를 최소화한다.",
            constraints="contact nonpenetration, friction, hand kinematics, dynamics와 actuator limits를 complementarity 없이 근사한다.",
            success="multi-contact dexterous trajectory가 nonsmooth mode enumeration 없이 solver에서 수렴하고 실제 실행 가능해지는 것이다.",
            bottleneck="contact complementarity는 product constraints와 discrete modes를 만들어 gradient-based optimization을 불안정하게 한다.",
            changes="complementarity-free smooth contact model을 사용해 multi-contact trajectory optimization을 differentiable하게 만든다.",
            assumptions=[
                ("smooth penalty가 true contact force/mode를 충분히 근사", "optimization을 위해 필요", "penalty scale과 penetration tradeoff가 큰 경우 false contact"),
                ("local solver가 relevant contact basin에 있음", "feasible motion을 위해 필요", "unseen mode/global rearrangement를 놓침"),
            ],
            loop="hand/object state → differentiable multi-contact optimizer → dexterous action/force → contact feedback의 planning-control loop다.",
            anchor="본문의 complementarity-free contact formulation, smooth optimization과 dexterous manipulation tasks.",
            domain="manipulation",
            body_basis="ABSTRACT_AND_PROCEEDINGS_FORMULATION",
        ),
        profile(
            "SoftGym: Benchmarking Deep Reinforcement Learning for Deformable Object Manipulation",
            problem="cloth, fluid, rope 등 deformable object manipulation에서 RL algorithm을 공통 differentiable/visual simulator와 task variation으로 비교한다.",
            model="deformable state geometry/particles, RGB observation과 robot action을 physics simulator dynamics로 연결한다.",
            objective="deformable object goal shape/pose/coverage와 task reward를 maximize한다.",
            constraints="deformation dynamics, contact, robot kinematics, self-collision와 task-specific goal/termination을 만족해야 한다.",
            success="algorithm/data/observation choice가 deformable manipulation generalization에 미치는 영향을 재현 가능하게 비교하는 것이다.",
            bottleneck="rigid object benchmark는 topology/contact/dynamics가 변하는 deformable task의 exploration difficulty를 반영하지 않는다.",
            changes="deformable physics task suite, visual state/action API, domain randomization과 evaluation protocol을 제공한다.",
            assumptions=[
                ("simulated deformation이 real object behavior에 충분한 proxy", "benchmark를 위해 필요", "material/contact mismatch"),
                ("visual observation이 shape/task state를 표현", "vision-based RL을 위해 필요", "occlusion/cloth self-contact ambiguity"),
            ],
            loop="RGB/state observation → deformable manipulation policy → contact dynamics → shape/reward feedback의 benchmark loop다.",
            anchor="본문의 SoftGym task families, deformable simulator state/action interface와 RL benchmark formulation.",
            domain="benchmark",
        ),
        profile(
            "DiffSkill: Skill Abstraction from Differentiable Physics for Deformable Object Manipulations with Tools",
            problem="tool을 이용한 deformable object manipulation의 long-horizon action을 differentiable physics로 skill/trajectory abstraction한다.",
            model="deformable state x, tool pose/action u와 differentiable dynamics fθ를 사용해 trajectory와 latent skill z를 optimize/learn한다.",
            objective="target shape/state와 trajectory cost를 최소화하고 latent skill policy가 multi-step manipulation을 재현한다.",
            constraints="differentiable simulator, tool-object contact, deformation dynamics와 action/geometry bounds를 만족해야 한다.",
            success="low-level tool trajectories를 latent skill로 압축해 new goal/shape에서 planning과 policy learning을 개선하는 것이다.",
            bottleneck="deformable object의 action space가 크고 contact effects가 long horizon에 누적되어 model-free RL exploration이 어렵다.",
            changes="differentiable physics trajectory optimization을 skill abstraction/latent policy supervision으로 사용한다.",
            assumptions=[
                ("physics gradient가 deformation/contact outcome을 유도", "skill optimization을 위해 필요", "nondifferentiable friction/impact는 gradient를 왜곡"),
                ("latent skill이 goal variation에 reusable", "hierarchical planning을 위해 필요", "skill boundary/shape variation에 brittle"),
            ],
            loop="deformable observation → differentiable skill/trajectory plan → tool action → shape feedback의 hierarchical loop다.",
            anchor="본문의 differentiable physics, skill abstraction과 tool-based deformable manipulation problem.",
            domain="manipulation",
        ),
        profile(
            "Neural Descriptor Fields: SE(3)-Equivariant Object Representations for Manipulation",
            problem="object pose/viewpoint 변화에도 consistent 3D descriptor를 제공해 demonstrations의 manipulation affordance를 novel pose로 transfer한다.",
            model="point/RGB-D observation을 continuous descriptor field f(x)로 encode하고 SE(3) transform에 equivariant하게 descriptor/query point를 변환한다.",
            objective="corresponding object points의 descriptor distance와 downstream pose/action transfer error를 최소화한다.",
            constraints="object coordinate frame과 geometric correspondence, SE(3) transformation/visible surface가 안정적으로 정의되어야 한다.",
            success="new object pose/scene에서 demonstration landmark와 manipulation action을 geometric transform으로 재사용하는 것이다.",
            bottleneck="image feature는 viewpoint/pose 변화에 equivariance가 약하고, explicit keypoint detector는 category/object variation에 brittle하다.",
            changes="SE(3)-equivariant continuous descriptor field를 learned object representation과 manipulation interface로 사용한다.",
            assumptions=[
                ("object geometry와 correspondence를 관측", "equivariant field supervision을 위해 필요", "occlusion/symmetry ambiguity"),
                ("rigid transform이 task geometry를 보존", "action transfer를 위해 필요", "deformation/articulation은 단일 SE(3)로 부족"),
            ],
            loop="RGB-D/point observation → equivariant object descriptor/landmark → transformed action → contact feedback의 3D manipulation loop다.",
            anchor="본문의 SE(3)-equivariant descriptor field, correspondence objective와 manipulation transfer formulation.",
            domain="3d_perception",
        ),
        profile(
            "Diffusion-EDFs: Bi-equivariant Denoising Generative Modeling on SE(3) for Visual Robotic Manipulation",
            problem="visual observation에서 multimodal 6-DoF manipulation pose/action을 생성하면서 object/robot coordinate transformation equivariance를 유지한다.",
            model="scene/object point features를 condition으로 SE(3) action pose distribution에 noise를 넣고 bi-equivariant denoising network가 pose를 복원한다.",
            objective="expert pose/action distribution의 diffusion denoising loss를 최소화한다.",
            constraints="SE(3) group action, collision/kinematic feasibility와 camera-object frame transform을 보존해야 한다.",
            success="pose/motion mode가 여러 개인 visual manipulation에서 data efficiency와 geometric generalization을 얻는 것이다.",
            bottleneck="Euclidean action diffusion은 rotations/transforms의 geometry를 왜곡하고 deterministic pose regression은 multimodality를 평균낸다.",
            changes="SE(3) bi-equivariance와 diffusion generative modeling을 결합해 geometric action distribution을 학습한다.",
            assumptions=[
                ("point/scene geometry가 correct frame으로 정렬", "equivariance를 위해 필요", "pose/calibration error가 action transform을 오염"),
                ("diffusion inference latency가 execution에 허용", "generative pose policy를 위해 필요", "long denoising은 feedback을 늦춤"),
            ],
            loop="visual 3D state → SE(3) diffusion action pose → motion/contact execution → feedback의 manipulation policy loop다.",
            anchor="본문의 SE(3) bi-equivariant denoising, pose action representation과 visual manipulation setup.",
            domain="manipulation",
        ),
        profile(
            "IndustReal: Transferring Contact-Rich Assembly Tasks from Simulation to Reality",
            problem="contact-rich industrial assembly policy를 simulation에서 학습해 real geometry/friction/actuator mismatch를 견디도록 transfer한다.",
            model="object/robot state와 contact observation을 simulated assembly dynamics에 넣어 action/force trajectory를 policy가 출력한다.",
            objective="insertion/assembly progress와 final fit success를 높이고 collision/force/episode time을 줄인다.",
            constraints="tight tolerance geometry, friction/contact transitions, actuator/force limits와 real sensing/control rate를 만족해야 한다.",
            success="sim-trained or sim-augmented policy가 real industrial assembly에서 robustness와 sample efficiency를 보이는 것이다.",
            bottleneck="assembly success는 small pose/friction error와 contact mode에 민감하고 real failed trials는 비용이 크다.",
            changes="contact-aware simulation/data randomization/transfer strategy를 조합해 simulation-to-real assembly gap을 줄인다.",
            assumptions=[
                ("sim contact parameter/randomization이 real variation을 cover", "transfer를 위해 필요", "tolerance/compliance OOD"),
                ("observation/action interface가 contact onset을 표현", "reactive policy를 위해 필요", "force sensor latency·occlusion"),
            ],
            loop="visual/proprioceptive/force state → assembly policy → contact execution → insertion feedback의 contact-rich loop다.",
            anchor="본문의 industrial assembly task, simulation transfer recipe와 real contact evaluation setup.",
            domain="tactile",
        ),
        profile(
            "Binding Touch to Everything: Learning Unified Multimodal Tactile Representations",
            problem="tactile observation을 vision/language/other modalities와 shared representation으로 align해 contact-aware task reasoning을 가능하게 한다.",
            model="tactile image/signal와 visual/language token을 modality encoders/projectors로 map해 contrastive or masked multimodal embedding을 학습한다.",
            objective="paired touch-vision-language semantics와 tactile geometry/force information을 shared embedding에서 보존한다.",
            constraints="time/spatial alignment과 paired multimodal data가 필요하고 tactile sensor/domain variation이 representation에 흡수되어야 한다.",
            success="novel tactile query/recognition/manipulation task에서 touch가 visual-language prior와 함께 사용되는 것이다.",
            bottleneck="vision-language foundation model은 occluded contact/force를 보지 못하고 sensor-specific tactile models는 transfer가 어렵다.",
            changes="tactile을 first-class modality로 binding해 unified representation과 downstream robot interface를 제시한다.",
            assumptions=[
                ("touch와 paired visual/language semantics가 정렬", "cross-modal learning을 위해 필요", "weak/noisy pairing은 shortcut"),
                ("shared representation이 force/geometry를 보존", "robot policy transfer를 위해 필요", "semantic alignment가 high-frequency control을 대체하지 않음"),
            ],
            loop="touch+vision+language observation → unified contact representation → task/action decision의 multimodal perception layer다.",
            anchor="본문의 unified tactile/vision/language representation, multimodal pretraining objectives와 robot applications.",
            domain="tactile",
        ),
        profile(
            "DenseMatcher: Learning 3D Semantic Correspondence for Category-Level Manipulation from a Single Demo",
            problem="single demonstration의 manipulation correspondence를 같은 category의 novel object/pose에 3D semantic matching으로 transfer한다.",
            model="query/demo point cloud와 current scene point cloud의 3D features를 dense correspondence field로 매칭해 action/landmark pose를 추정한다.",
            objective="semantic corresponding point/trajectory alignment와 downstream category-level manipulation success를 높인다.",
            constraints="category geometry와 affordance structure가 공유되고 demo/current view가 enough overlap되어야 한다.",
            success="one demonstration에서 novel category instance의 action point/pose를 찾고 실행하는 것이다.",
            bottleneck="pixel correspondence는 viewpoint/shape variation에 약하고 category-level action transfer는 explicit correspondence supervision이 부족하다.",
            changes="3D semantic dense matching을 single-demo manipulation transfer의 central formulation으로 둔다.",
            assumptions=[
                ("category-level geometry/affordance가 보존", "single-demo transfer를 위해 필요", "large shape/topology variation은 match failure"),
                ("point cloud overlap와 calibration이 충분", "3D matching을 위해 필요", "occlusion/sparse depth가 correspondence를 흔듦"),
            ],
            loop="demo+current 3D observation → semantic correspondence → transformed action → execution feedback의 manipulation loop다.",
            anchor="본문의 single-demo category-level correspondence problem, 3D matching representation과 manipulation evaluation.",
            domain="3d_perception",
            body_basis="ABSTRACT_AND_PROCEEDINGS_FORMULATION",
        ),
        profile(
            "G3Flow: Generative 3D Semantic Flow for Pose-aware and Generalizable Object Manipulation",
            problem="object pose와 category variation을 고려해 3D semantic affordance/action flow를 생성하고 manipulation pose로 변환한다.",
            model="3D object features와 goal/task condition을 flow field/transport representation으로 map해 pose-aware action correspondence를 생성한다.",
            objective="demo-to-target semantic flow alignment와 manipulation success를 높이고 pose mismatch/collision을 줄인다.",
            constraints="SE(3) object pose, category shape correspondence, scene geometry와 action/robot kinematic feasibility가 필요하다.",
            success="novel object pose/category에서도 learned 3D flow가 contact/action target을 generalize하는 것이다.",
            bottleneck="2D correspondence와 pose-agnostic features는 viewpoint/object pose change에서 action point가 drift한다.",
            changes="generative 3D semantic flow를 pose-aware manipulation correspondence/action representation으로 사용한다.",
            assumptions=[
                ("3D semantic features가 affordance correspondence를 보존", "flow generation을 위해 필요", "category gap과 occlusion"),
                ("generated flow를 feasible robot pose로 decode", "execution을 위해 필요", "collision/IK failure"),
            ],
            loop="3D scene/object state → semantic flow/action pose → motion/contact → visual feedback의 pose-aware loop다.",
            anchor="본문의 3D semantic flow, pose-aware generalization과 object manipulation formulation.",
            domain="3d_perception",
        ),
        profile(
            "Reactive Diffusion Policy: Slow-Fast Visual-Tactile Policy Learning for Contact-Rich Manipulation",
            problem="긴 visual action chunk 실행 중 변하는 contact를 high-frequency tactile correction으로 보정한다.",
            model="slow visual latent diffusion policy가 action chunk를 만들고 fast tactile/asymmetric tokenizer가 chunk 내부 action residual을 업데이트한다.",
            objective="contact-rich task success와 reaction quality를 높이며 visual plan과 tactile correction mismatch를 최소화한다.",
            constraints="두 control rate의 synchronization, tactile calibration/feedback와 action residual bound가 필요하다.",
            success="visual-only chunk policy보다 contact onset/disturbance에 빠르게 반응하는 것이다.",
            bottleneck="long action chunk는 multimodal trajectory에는 좋지만 chunk 중 contact mode 변화와 force error에 늦게 반응한다.",
            changes="slow visual plan과 fast tactile correction을 분리한 dual-rate diffusion policy를 제안한다.",
            assumptions=[
                ("tactile feedback가 correction-relevant contact state를 제공", "fast loop를 위해 필요", "sensor delay/transfer mismatch"),
                ("residual correction이 base chunk를 무너뜨리지 않음", "hierarchical composition을 위해 필요", "large disturbance/novel contact는 recovery 필요"),
            ],
            loop="vision → slow action plan → tactile fast residual → contact feedback/replan의 dual-rate control loop다.",
            anchor="본문의 slow-fast policy architecture, tactile action correction과 contact-rich task formulation.",
            domain="tactile",
            body_basis="ABSTRACT_AND_PROCEEDINGS_FORMULATION",
        ),
        profile(
            "AT-VLA: Adaptive Tactile Injection for Enhanced Feedback Reaction in Vision-Language-Action Models",
            problem="VLA가 visual-language prior만으로 놓치는 contact feedback을 adaptive tactile token injection으로 action decision에 반영한다.",
            model="vision-language-action hidden state와 tactile stream을 condition-dependent fusion/gating module로 결합해 action chunk를 예측한다.",
            objective="tactile event에 맞춘 action correction과 manipulation success를 높이고 unnecessary tactile interference를 줄인다.",
            constraints="tactile/visual time alignment, sensor modality availability와 adaptive injection gate가 필요하다.",
            success="contact onset·slip·force change에 대해 VLA action이 더 빠르고 적절하게 반응하는 것이다.",
            bottleneck="기존 VLA는 language/vision context가 풍부해도 high-frequency contact state를 늦게 관측하거나 tactile을 단순 concatenate한다.",
            changes="tactile information을 모든 timestep에 고정 주입하지 않고 필요한 때 adaptive하게 VLA representation에 넣는다.",
            assumptions=[
                ("tactile event와 required action correction이 correlation", "adaptive gate를 학습하기 위해 필요", "sensor noise/spurious contact"),
                ("VLA backbone이 tactile token을 action-relevant로 해석", "fusion을 위해 필요", "semantic prior가 tactile signal을 overshadow"),
            ],
            loop="vision+language+tactile → adaptive VLA state → action → contact feedback의 multimodal control loop다.",
            anchor="본문의 adaptive tactile injection/fusion, feedback reaction objective와 VLA manipulation setup.",
            domain="vla",
        ),
        profile(
            "ForceVLA2: Unleashing Hybrid Force-Position Control with Force Awareness for Contact-Rich Manipulation",
            problem="VLA action이 contact task의 position과 force direction을 함께 제어하도록 force-aware hybrid output을 학습한다.",
            model="visual-language-force/proprioceptive observation을 policy에 넣고 task frame selection, position/pose action과 force command를 출력한다.",
            objective="task pose/progress와 desired contact force를 추종하면서 force spike, slip과 collision을 제한한다.",
            constraints="hybrid position-force subspace, wrench sensing/calibration, robot dynamics와 actuator/safety bounds를 만족해야 한다.",
            success="vision-language policy가 contact-rich manipulation에서 force feedback을 사용해 pure pose action보다 robust한 것이다.",
            bottleneck="일반 VLA는 position/pose action 중심이라 insertion/pressing에서 force error를 직접 조절하지 못한다.",
            changes="hybrid force-position control semantics와 force-aware observation/action head를 VLA loop에 통합한다.",
            assumptions=[
                ("force sensor와 task frame이 calibrated", "force/position decomposition을 위해 필요", "frame error가 wrong force axis"),
                ("force command가 low-level controller에 faithfully execute", "VLA output을 위해 필요", "bandwidth/saturation이 contact stability를 제한"),
            ],
            loop="vision+language+force → hybrid action decision → compliant controller/contact → feedback의 contact-aware VLA loop다.",
            anchor="본문의 force-aware VLA, hybrid position/force action interface와 contact-rich task formulation.",
            domain="vla",
        ),
        profile(
            "Dexterous World Models",
            problem="high-DOF hand-object contact dynamics를 visual/proprioceptive latent world model로 예측해 dexterous policy planning을 가능하게 한다.",
            model="hand/object observation o_t와 action u_t를 latent dynamics model에 넣어 future visual/contact state, reward 또는 task outcome을 predict한다.",
            objective="multi-step latent prediction과 action-conditioned manipulation success를 높인다.",
            constraints="hidden contact mode/force state가 latent에 보존되고 model rollout이 real dynamics를 일정 horizon 동안 예측해야 한다.",
            success="실제 interaction 전에 imagined dexterous rollout으로 action/skill을 평가하고 generalize하는 것이다.",
            bottleneck="hand-object contact는 partial observation과 mode switching이 심해 flat policy가 시행착오를 많이 요구한다.",
            changes="dexterous interaction-specific state/dynamics prediction을 world-model planning interface로 구성한다.",
            assumptions=[
                ("visual/proprioceptive history가 contact state를 충분히 관측", "latent belief를 위해 필요", "occluded fingertip/force ambiguity"),
                ("learned model이 action consequence를 horizon 내 예측", "planning을 위해 필요", "compounding contact error"),
            ],
            loop="vision/tactile/proprioception → latent dexterous world model → imagined action selection → contact feedback의 model-based loop다.",
            anchor="본문의 dexterous world-model state/action prediction, contact dynamics와 planning/control evaluation.",
            domain="world_model",
        ),
        profile(
            "EquAct: An SE(3)-Equivariant Multi-Task Transformer for 3D Robotic Manipulation",
            problem="multiple 3D manipulation tasks와 object pose 변화에서 geometric action representation이 equivariant하게 generalize하도록 한다.",
            model="point cloud/RGB-D scene과 task instruction을 SE(3)-equivariant Transformer에 넣어 3D action pose/trajectory를 예측한다.",
            objective="multi-task expert action likelihood와 transformed-scene consistency를 높인다.",
            constraints="SE(3) scene/action coordinate transformation, camera calibration과 robot kinematic/action bounds를 보존해야 한다.",
            success="translation/rotation of object or scene에 따라 action이 일관되게 transform되고 multi-task success가 개선되는 것이다.",
            bottleneck="image/token policy는 absolute coordinate에 overfit하고 3D pose variation에서 data augmentation만으로 충분한 equivariance를 못 얻는다.",
            changes="SE(3)-equivariant multi-task Transformer를 3D manipulation action prediction에 적용한다.",
            assumptions=[
                ("point cloud와 action frame이 accurately registered", "equivariance를 위해 필요", "calibration/noisy depth가 transformation consistency를 깸"),
                ("task action이 rigid transform으로 충분히 설명", "multi-task transfer를 위해 필요", "contact force/orientation-dependent dynamics는 추가 state 필요"),
            ],
            loop="3D observation+instruction → equivariant action → robot motion/contact → feedback의 geometric VLA loop다.",
            anchor="본문의 SE(3)-equivariant Transformer, 3D action representation과 multi-task manipulation setup.",
            domain="3d_perception",
            body_basis="ABSTRACT_AND_PROCEEDINGS_FORMULATION",
        ),
        profile(
            "Tabero: Learning Gentle Manipulation with Closed-Loop Force Feedback from Vision, Touch, and Language",
            problem="fragile/gentle manipulation에서 vision-language goal과 touch/force feedback을 이용해 contact force를 closed-loop로 조절한다.",
            model="vision, tactile/force, language와 proprioception을 policy state로 결합해 low-force pose/velocity/force action을 출력한다.",
            objective="task success와 object integrity를 높이고 peak/impulse contact force와 slip을 낮춘다.",
            constraints="force safety envelope, tactile calibration, object fragility와 controller bandwidth를 만족해야 한다.",
            success="open-loop visual policy보다 delicate contact에서 force overshoot를 줄이고 successful handling을 얻는 것이다.",
            bottleneck="vision/language는 object fragility와 instantaneous force를 직접 관측하지 못하고 position-only action은 contact error를 증폭한다.",
            changes="touch/force observation을 closed-loop VLA action decision과 gentle manipulation objective에 직접 연결한다.",
            assumptions=[
                ("touch/force signal이 damage/slip state를 timely하게 표시", "gentle controller를 위해 필요", "sensor latency/saturation"),
                ("force threshold가 task-safe envelope를 대표", "safety objective를 위해 필요", "unknown object material/geometry에서 threshold mismatch"),
            ],
            loop="vision+language+touch/force → force-aware action → contact → feedback/recovery의 gentle manipulation loop다.",
            anchor="본문의 vision-touch-language input, closed-loop force feedback과 gentle manipulation task definition.",
            domain="tactile",
        ),
        profile(
            "TactAlign: Human-to-Robot Policy Transfer via Tactile Alignment",
            problem="human demonstration과 robot execution 사이의 embodiment/visual gap을 tactile contact signal alignment로 줄인다.",
            model="human/robot visual-tactile trajectory를 shared tactile representation 또는 alignment objective로 map하고 robot action policy를 학습한다.",
            objective="aligned contact state/action representation과 demonstration-to-robot task success를 높인다.",
            constraints="tactile sensor geometry/calibration, temporal alignment와 human/robot contact event 대응이 필요하다.",
            success="visual appearance/embodiment가 달라도 tactile event sequence가 policy transfer의 common signal이 되는 것이다.",
            bottleneck="human video/teleop trajectory의 image/action distribution은 robot sensor·hand morphology와 달라 direct BC가 실패한다.",
            changes="tactile alignment를 cross-embodiment policy transfer의 invariant interface로 사용한다.",
            assumptions=[
                ("human/robot tactile events가 동일 task phase를 표현", "alignment를 위해 필요", "different contact geometry가 event semantics를 바꿈"),
                ("tactile representation이 action-relevant", "transfer를 위해 필요", "force magnitude/embodiment-specific detail loss"),
            ],
            loop="human/robot tactile+vision → aligned contact state → robot policy action → contact feedback의 transfer loop다.",
            anchor="공식 RSS program/paper page의 tactile-alignment problem과 human-to-robot policy transfer scope; 세부 식은 본문 확인 필요.",
            domain="tactile",
            body_basis="ABSTRACT_OR_PROGRAM_PAGE_FORMULATION",
        ),
        profile(
            "DexterityGen: Foundation Controller for Unprecedented Dexterity",
            problem="large-scale heterogeneous dexterous motion data를 foundation controller가 다양한 hand task/skill의 low-level action으로 생성한다.",
            model="hand proprioception, object/task/goal condition을 shared dexterous policy/controller에 넣어 joint/torque action trajectory를 출력한다.",
            objective="diverse dexterous skill completion과 motion quality를 높이면서 contact/actuator constraints를 만족한다.",
            constraints="hand morphology/action normalization, contact dynamics, data coverage와 real-time controller bandwidth가 필요하다.",
            success="single-task controller보다 broad unseen dexterity와 skill composition/transfer를 제공하는 것이다.",
            bottleneck="dexterous controllers는 task/morphology-specific data와 reward에 묶여 skill diversity와 transfer가 낮다.",
            changes="foundation-scale data/model을 dexterous control prior로 두어 many-task action generation을 목표로 한다.",
            assumptions=[
                ("heterogeneous action/state schema가 align", "foundation controller를 위해 필요", "morphology mismatch와 negative transfer"),
                ("dataset이 rare contact skills를 충분히 포함", "unprecedented dexterity를 위해 필요", "coverage 부족은 interpolation만 가능"),
            ],
            loop="task/observation → dexterous foundation controller → hand contact/action → tactile/proprioceptive feedback의 low-level policy loop다.",
            anchor="공식 RSS program/paper page의 foundation-controller scope; action/state details와 empirical formulation은 본문 확인 필요.",
            domain="manipulation",
            body_basis="ABSTRACT_OR_PROGRAM_PAGE_FORMULATION",
        ),
    ]
)


# Policy scaling, offline data, simulation, and robot-learning benchmarks.
add_many(
    [
        profile(
            "Behavior Transformers: Cloning k modes with one stone",
            problem="같은 observation에서 여러 valid behavior mode가 존재하는 multimodal demonstration을 one-mode averaging 없이 clone한다.",
            model="observation/context encoder와 latent behavior mode z를 사용해 k mixture/cluster-conditioned action trajectory distribution을 예측한다.",
            objective="expert action likelihood 또는 mode assignment를 높여 multiple behavior modes를 보존한다.",
            constraints="dataset이 distinct modes를 충분히 포함하고 inference가 mode selection/conditioning을 안정적으로 해야 한다.",
            success="ambiguous state에서 평균 action 대신 coherent trajectory mode를 선택해 long-horizon rollout success를 높이는 것이다.",
            bottleneck="deterministic BC와 per-step regression은 mutually exclusive expert choices를 평균내어 invalid action을 만든다.",
            changes="behavior mode를 latent/cluster variable로 분리해 Transformer sequence policy가 k modes를 함께 모델링한다.",
            assumptions=[
                ("modes가 observation/context로 구분 가능", "mixture behavior를 선택하기 위해 필요", "unobserved intent는 mode ambiguity로 남음"),
                ("long-horizon trajectory mode consistency", "per-step mode switching을 피하기 위해 필요", "contact recovery mode가 data에 없으면 생성 불가"),
            ],
            loop="observation/history → mode-conditioned action sequence → execution → next state feedback의 multimodal policy loop다.",
            anchor="본문의 multimodal behavior cloning problem, k-mode latent/mixture sequence model과 rollout evaluation.",
            domain="il",
            body_basis="ABSTRACT_AND_PROCEEDINGS_FORMULATION",
        ),
        profile(
            "R3M: A Universal Visual Representation for Robot Manipulation",
            problem="internet video와 robot data에서 학습한 visual representation이 object/task 변화에도 manipulation-relevant state feature를 제공하게 한다.",
            model="video/image encoder fθ(o_{t:t+H})를 temporal/visual pretraining objective로 학습하고 downstream robot policy가 feature를 condition으로 사용한다.",
            objective="video temporal consistency·language/visual correspondence를 학습해 downstream action prediction/goal success를 높인다.",
            constraints="web video의 visual motion이 robot affordance와 충분히 관련되고 camera viewpoint/task semantics가 align되어야 한다.",
            success="robot demonstration이 적어도 pretrained representation을 fine-tune해 novel manipulation task generalization을 얻는 것이다.",
            bottleneck="robot-only visual encoder는 dataset 규모가 작고 task-specific appearance에 overfit한다.",
            changes="large-scale human video pretraining과 robot manipulation transfer를 universal representation problem으로 연결한다.",
            assumptions=[
                ("human video motion이 robot action-relevant concept를 보존", "representation transfer를 위해 필요", "embodiment/contact dynamics mismatch"),
                ("feature가 geometric pose보다 semantic prior를 보완", "few-shot policy learning을 위해 필요", "fine 3D geometry/force state는 별도 sensing 필요"),
            ],
            loop="camera history → pretrained visual state → robot policy/control → manipulation feedback의 representation layer다.",
            anchor="본문의 universal representation motivation, video pretraining objectives와 robot manipulation transfer setup.",
            domain="vision",
        ),
        profile(
            "Where are we in the search for an Artificial Visual Cortex for Embodied Intelligence?",
            problem="embodied agent가 시각 input에서 action-relevant object/geometry/state representation을 얻도록 visual learning pipeline을 비교·정리한다.",
            model="visual observation을 object/scene/motion/affordance representation으로 encode하고 policy/planner가 해당 representation으로 action을 선택한다.",
            objective="perception representation의 semantic/geometry fidelity와 downstream embodied task performance 사이의 tradeoff를 분석한다.",
            constraints="representation이 task-relevant information을 보존하고 sensor viewpoint, embodiment와 task distribution을 연결해야 한다.",
            success="vision backbone 선택이 robot decision/control에 어떤 inductive bias와 failure를 주는지 공통 problem map으로 설명하는 것이다.",
            bottleneck="recognition benchmark accuracy는 closed-loop action usefulness, temporal state와 affordance grounding을 직접 측정하지 않는다.",
            changes="visual cortex analogy를 통해 object-centric, 3D, temporal, action-conditioned representation research를 embodied loop 관점에서 taxonomy화한다.",
            assumptions=[
                ("downstream task가 representation quality를 드러냄", "embodied evaluation을 해석하기 위해 필요", "proxy benchmark와 robot success가 불일치할 수 있음"),
                ("visual state가 action choice의 주요 bottleneck", "perception-first analysis를 위해 필요", "contact/proprioception/feedback이 더 큰 원인일 수 있음"),
            ],
            loop="observation → visual state/world model → task/action decision의 perception research question이다.",
            anchor="본문의 artificial visual cortex survey framing, visual representation axes와 embodied intelligence discussion.",
            domain="vision",
            body_basis="ABSTRACT_AND_REVIEW_FORMULATION",
        ),
        profile(
            "Maximum a Posteriori Policy Optimisation",
            problem="off-policy replay와 prior policy를 사용해 continuous policy를 sample-efficient하게 개선하되 policy collapse와 distribution shift를 제어한다.",
            model="behavior/replay distribution q(a|s)와 current policy πθ를 두고 Q-weighted target policy를 KL-regularized MAP update로 추정한다.",
            objective="Q-value를 높이는 policy와 prior behavior 사이의 KL-regularized posterior를 maximize한다.",
            constraints="replay data coverage, Q estimator accuracy와 policy-prior KL constraint/temperature가 필요하다.",
            success="deterministic/off-policy policy optimization보다 robust하게 continuous-control return과 sample efficiency를 개선하는 것이다.",
            bottleneck="naive off-policy actor update는 dataset 밖 action Q를 과대평가하고, policy improvement가 급격한 distribution shift를 만든다.",
            changes="policy improvement를 MAP inference/KL-regularized update로 해석해 behavior prior와 Q improvement를 결합한다.",
            assumptions=[
                ("Q가 sampled action의 relative quality를 신뢰성 있게 평가", "posterior policy를 위해 필요", "critic overestimation이 unsafe exploration"),
                ("behavior prior가 useful support를 가짐", "KL regularization을 위해 필요", "poor replay data가 policy ceiling을 정함"),
            ],
            loop="replay transition → Q/value estimation → MAP policy update → continuous action feedback의 off-policy RL loop다.",
            anchor="본문의 MAP policy-improvement derivation, KL regularization과 off-policy continuous-control setup.",
            domain="offline_rl",
            body_basis="ABSTRACT_AND_PROCEEDINGS_FORMULATION",
        ),
        profile(
            "MT-Opt: Continuous Multi-Task Robotic Reinforcement Learning at Scale",
            problem="real robot fleet에서 diverse task data를 지속 수집하고 multi-task policy가 새로운 task/experience를 활용하도록 한다.",
            model="camera/proprioceptive state와 task goal을 conditional policy/Q-function에 넣어 continuous robot action을 선택하고 distributed replay를 갱신한다.",
            objective="task-conditioned expected return을 large-scale off-policy RL로 maximize한다.",
            constraints="robot fleet/action interface, asynchronous data collection, task labels/rewards와 safe exploration policy가 필요하다.",
            success="많은 real-world interaction과 multi-task replay가 single-task 학습보다 sample reuse/generalization을 높이는 것이다.",
            bottleneck="real robot RL은 data collection이 느리고, task별 policy는 fleet experience와 infrastructure를 공유하지 못한다.",
            changes="continuous multi-task data collection, relabeling/replay와 scalable distributed training을 하나의 robot RL system으로 구성한다.",
            assumptions=[
                ("task-conditioned representation/action space가 공유 가능", "multi-task policy를 위해 필요", "task conflict와 embodiment difference가 negative transfer"),
                ("online exploration이 안전·효율적", "real data scale을 위해 필요", "failures/rare contact cost가 큰 작업은 coverage가 낮음"),
            ],
            loop="fleet observation/task → distributed policy action → real robot transition → replay/training feedback loop다.",
            anchor="본문의 multi-task robot RL problem, fleet data/replay pipeline과 continuous policy interface.",
            domain="rl",
        ),
        profile(
            "Isaac Gym: High Performance GPU Based Physics Simulation For Robot Learning",
            problem="수천 개 environment rollout을 병렬 실행해 model-free/model-based robot learning의 simulation bottleneck을 줄인다.",
            model="GPU tensor state q,q̇/contact를 병렬 physics engine에 넣고 batch action u를 동시에 적용해 next state/reward/done을 출력한다.",
            objective="physics simulation throughput을 높이면서 task reward와 contact dynamics를 학습에 제공한다.",
            constraints="GPU memory/batch size, discretization/contact solver와 simulator model fidelity가 training signal을 결정한다.",
            success="large-scale parallel rollout이 policy optimization wall-time과 sample collection bottleneck을 개선하는 것이다.",
            bottleneck="CPU simulator와 host-device copy는 high-throughput RL에서 environment step을 policy update보다 느리게 만든다.",
            changes="GPU-native simulation/state access와 massive parallel environment interface를 robot learning loop에 제공한다.",
            assumptions=[
                ("GPU contact approximation이 task-relevant", "parallel training을 위해 필요", "sim-to-real dynamics/contact mismatch"),
                ("batch environments의 domain variation이 충분", "generalization을 위해 필요", "massive identical rollouts는 overfit"),
            ],
            loop="simulated state batch → parallel physics step → reward/next state → RL update의 training environment layer다.",
            anchor="본문의 GPU physics architecture, tensor API와 large-scale robot learning benchmark/application.",
            domain="simulation",
        ),
        profile(
            "Eureka: Human-Level Reward Design via Coding Large Language Models",
            problem="robot skill RL에서 사람이 reward function을 수작업 설계하는 병목을 natural-language task description과 code-generating LM으로 줄인다.",
            model="task description/robot environment context를 LLM에 넣어 executable reward code r_φ(s,a)를 생성하고 RL policy rollout score로 후보를 평가한다.",
            objective="generated reward 아래 학습한 policy의 task success/behavior quality를 maximize한다.",
            constraints="environment state/API가 reward code에 노출되고 LLM code가 실행 가능·안전하며 proxy reward가 true task goal과 align되어야 한다.",
            success="human-written reward baseline보다 적은 manual shaping으로 policy가 desired behavior를 학습하는 것이다.",
            bottleneck="sparse/complex robot reward는 contact·progress·stability terms를 사람이 일일이 조정해야 하고 reward hacking이 발생한다.",
            changes="LLM이 reward program을 생성하고 simulation feedback/evolution으로 candidates를 탐색하는 reward-design loop를 제시한다.",
            assumptions=[
                ("state/API가 task semantics를 충분히 expose", "code reward를 만들기 위해 필요", "숨은 contact/force state는 잘못된 proxy"),
                ("proxy reward success와 상관", "RL optimization을 위해 필요", "reward hacking·unsafe shortcut은 실제 목표와 어긋남"),
            ],
            loop="language goal → reward code → policy learning → rollout evaluation/feedback의 meta-learning loop다.",
            anchor="본문의 LLM-generated reward code, evolutionary candidate evaluation과 robot simulation tasks.",
            domain="rl",
            body_basis="ABSTRACT_AND_PROCEEDINGS_FORMULATION",
        ),
        profile(
            "DrEureka: Language Model Guided Sim-To-Real Transfer",
            problem="사람이 만든 reward/randomization 없이 language model을 이용해 simulated robot policy가 real dynamics로 transfer되도록 한다.",
            model="task description과 simulator API를 LLM에 넣어 reward/dynamics randomization code를 생성하고 sim RL policy를 real robot에 배치한다.",
            objective="simulated expected return과 real-world task success를 동시에 높이는 reward/randomization design을 찾는다.",
            constraints="LLM code가 simulator에서 실행 가능하고 randomized dynamics가 real system을 cover하며 safety bounds가 유지되어야 한다.",
            success="language-guided reward와 domain randomization이 hand-designed sim-to-real recipe와 경쟁하는 것이다.",
            bottleneck="sim-to-real은 reward shaping과 parameter randomization을 수작업으로 조정해야 하고 chosen distribution이 real dynamics를 놓친다.",
            changes="LLM을 simulator-aware code designer로 사용해 reward와 randomization을 자동 제안·평가한다.",
            assumptions=[
                ("simulator API가 relevant physical parameter를 expose", "code generation을 위해 필요", "unmodeled actuator/contact bias는 transfer되지 않음"),
                ("generated reward가 real task goal과 align", "policy behavior를 위해 필요", "simulation shortcut/reward hacking"),
            ],
            loop="language/task specification → generated reward/randomization → sim policy → real feedback의 sim-to-real design loop다.",
            anchor="RSS 본문의 language-model-guided reward/randomization, simulation training과 real transfer setup.",
            domain="sim2real",
        ),
        profile(
            "Continuous Control with Deep Reinforcement Learning",
            problem="continuous action space에서 neural actor가 high-dimensional state를 action으로 매핑하도록 off-policy RL을 수행한다.",
            model="deterministic actor μθ(s)와 critic Qφ(s,a)를 replay transitions로 학습하고 target networks로 Bellman backup을 안정화한다.",
            objective="critic TD error를 줄이고 actor가 Qφ(s,μθ(s))를 maximize한다.",
            constraints="continuous bounded action, replay buffer, target network/soft update와 exploration noise가 필요하다.",
            success="discrete action DQN을 continuous robot control로 확장해 simulated physical tasks에서 policy를 학습하는 것이다.",
            bottleneck="Q-learning의 discrete argmax는 continuous action에서 계산 불가능하고 model-free real control은 sample-expensive하다.",
            changes="deterministic policy gradient와 actor-critic/replay/target-network 구조를 continuous control에 적용한다.",
            assumptions=[
                ("critic이 continuous action Q를 충분히 근사", "actor gradient를 위해 필요", "function approximation error가 policy를 망가뜨림"),
                ("exploration noise가 useful actions를 탐색", "off-policy data를 위해 필요", "contact safety와 sparse reward에서 inefficient"),
            ],
            loop="state observation → deterministic actor action → replay transition → critic/actor update의 continuous RL loop다.",
            anchor="본문의 continuous-control motivation, deterministic policy gradient, replay와 target network formulation.",
            domain="rl",
        ),
        profile(
            "Addressing Function Approximation Error in Actor-Critic Methods",
            problem="actor-critic의 approximate Q가 overestimate되어 actor가 잘못된 action으로 update되는 문제를 줄인다.",
            model="두 independent critics Q_{φ1},Q_{φ2}의 clipped/min target과 delayed actor update로 continuous action value를 추정한다.",
            objective="conservative target Bellman error를 줄이고 actor가 underestimated/min critic을 기준으로 policy return을 높인다.",
            constraints="critic ensemble independence, target smoothing noise와 delayed policy update가 필요하다.",
            success="function approximation error에 대한 robustness와 continuous-control benchmark 성능을 DDPG보다 개선하는 것이다.",
            bottleneck="DDPG actor가 noisy overestimated Q를 maximize하면 작은 approximation error도 systematic policy degradation으로 증폭된다.",
            changes="clipped double Q, target policy smoothing과 delayed policy update를 결합해 critic-induced error를 완화한다.",
            assumptions=[
                ("두 critic error가 완전히 같은 방향이 아님", "min operator가 overestimate를 줄이기 위해 필요", "correlated error는 보정이 약함"),
                ("target smoothing이 local action robustness를 반영", "sharp Q peak을 피하기 위해 필요", "fine contact action은 smoothing에 손상"),
            ],
            loop="replay transition → twin critic/actor update → continuous action → environment feedback의 stabilized off-policy loop다.",
            anchor="본문의 overestimation error diagnosis, clipped double Q·target policy smoothing·delayed update.",
            domain="rl",
        ),
        profile(
            "Hindsight Experience Replay",
            problem="sparse reward goal-conditioned task에서 실패한 rollout도 달성한 다른 goal의 성공 경험으로 재사용한다.",
            model="transition (s_t,a_t,s_{t+1},g)를 실제 goal g와 hindsight relabeled goal g'로 재구성해 goal-conditioned Q/policy를 학습한다.",
            objective="goal g' 달성 여부의 sparse reward를 통해 value/policy를 개선하고 desired goal g success를 높인다.",
            constraints="goal relabeling이 state trajectory에서 valid goal을 만들고 goal-conditioned dynamics/reward가 정의되어야 한다.",
            success="원래 goal에는 실패한 episode도 useful learning signal로 바꾸어 sparse-reward exploration을 개선하는 것이다.",
            bottleneck="robot manipulation/reaching의 sparse success reward는 random exploration에서 거의 관측되지 않는다.",
            changes="episode hindsight goal을 사용해 unsuccessful experience를 off-policy goal-conditioned training data로 재해석한다.",
            assumptions=[
                ("achieved state가 valid alternative goal", "relabelled success reward를 위해 필요", "contact/path-dependent goal은 단순 relabeling 불가"),
                ("goal-conditioned policy가 여러 goal을 표현", "reuse된 data를 일반화하기 위해 필요", "high-dimensional visual goals는 representation bottleneck"),
            ],
            loop="state+goal → action → achieved state → hindsight relabel/replay의 goal-conditioned learning loop다.",
            anchor="본문의 sparse-reward goal-conditioned MDP, hindsight goal relabeling과 off-policy algorithm.",
            domain="rl",
        ),
        profile(
            "Constrained Policy Optimization",
            problem="expected return을 높이면서 expected cost/safety constraint를 위반하지 않는 stochastic policy를 trust-region update로 학습한다.",
            model="policy πθ와 cost/value function을 두고 reward/cost surrogate와 average KL trust region을 constrained optimization으로 푼다.",
            objective="J_R(π)를 maximize subject to J_C(π)≤d를 만족한다.",
            constraints="cost limit, KL trust region과 accurate reward/cost advantage estimates가 필요하다.",
            success="각 update가 safety constraint를 유지하거나 violation을 controlled bound 안에 두면서 policy performance를 개선하는 것이다.",
            bottleneck="reward penalty tuning은 safety-performance scale에 민감하고 unsafe policy를 직접 탐색한다.",
            changes="policy improvement bound와 constraint surrogate를 동시에 만족하는 constrained natural-gradient step을 사용한다.",
            assumptions=[
                ("cost critic과 constraint threshold가 신뢰 가능", "safety surrogate를 위해 필요", "rare failure/partial observation에서 cost를 과소평가"),
                ("KL local trust region이 bound를 대표", "feasible update를 위해 필요", "unmodeled dynamics는 formal constraint 밖"),
            ],
            loop="rollout → reward/cost advantage → constrained policy update → safe environment feedback의 safe RL loop다.",
            anchor="본문의 constrained MDP, reward/cost surrogate와 KL-constrained policy update.",
            domain="safety",
        ),
        profile(
            "Conservative Q-Learning for Offline Reinforcement Learning",
            problem="offline dataset 밖 action의 Q overestimation을 억제하면서 dataset에서 얻을 수 있는 high-return policy를 학습한다.",
            model="Q(s,a)를 Bellman target으로 학습하고 log-sum-exp/expectation over actions term으로 dataset action보다 unseen action Q를 보수적으로 낮춘다.",
            objective="data-support action의 value를 보존하면서 out-of-distribution action의 Q를 lower bound 방향으로 regularize한다.",
            constraints="offline dataset support와 action sampling/integration, conservative regularization coefficient가 필요하다.",
            success="online exploration 없이 distribution shift와 extrapolation error를 줄인 offline policy improvement를 얻는 것이다.",
            bottleneck="standard Q-learning의 max over unseen actions는 critic error를 크게 확대해 unsafe policy를 만든다.",
            changes="Q objective에 conservative penalty를 넣어 unseen action의 value overestimation을 명시적으로 억제한다.",
            assumptions=[
                ("dataset에 useful behavior coverage", "conservative learner의 성능 ceiling을 위해 필요", "dataset 밖 recovery는 발견되지 않음"),
                ("penalty scale이 support와 improvement를 절충", "under/over-conservatism을 피하기 위해 필요", "task reward scale에 민감"),
            ],
            loop="offline transition log → conservative Q → policy extraction → deployment feedback의 offline RL loop다.",
            anchor="본문의 offline MDP, extrapolation error와 conservative Q regularization objective.",
            domain="offline_rl",
        ),
        profile(
            "MOPO: Model-based Offline Policy Optimization",
            problem="offline data가 cover하지 않는 state-action에서 model error가 큰 rollout을 피하면서 model-based policy improvement를 한다.",
            model="offline transition으로 ensemble dynamics model을 학습하고 predicted uncertainty u(s,a)를 reward penalty로 사용해 synthetic rollout을 생성한다.",
            objective="model reward minus uncertainty penalty의 expected return을 maximize한다.",
            constraints="ensemble disagreement가 model epistemic uncertainty를 반영하고 rollout horizon/penalty가 distribution shift를 제한해야 한다.",
            success="offline dataset을 model rollout으로 확장하면서 OOD hallucinated transition이 policy를 오도하지 않게 하는 것이다.",
            bottleneck="offline RL은 data 밖 action을 평가할 수 없고 naive model-based augmentation은 compounding model error를 낳는다.",
            changes="uncertainty-aware conservative reward로 model-generated data를 policy optimization에 제한적으로 사용한다.",
            assumptions=[
                ("ensemble uncertainty가 dynamics error와 correlate", "penalty를 설계하기 위해 필요", "systematic shared model bias는 감지되지 않음"),
                ("short synthetic rollout이 useful", "model error accumulation을 줄이기 위해 필요", "long-horizon task에는 myopic policy"),
            ],
            loop="offline data → ensemble world model → uncertainty-penalized rollout → policy update의 offline model-based loop다.",
            anchor="본문의 offline model learning, uncertainty penalty와 model rollout policy optimization.",
            domain="offline_rl",
        ),
        profile(
            "A Minimalist Approach to Offline Reinforcement Learning",
            problem="복잡한 offline RL regularizer 없이 behavior policy constraint와 standard actor-critic만으로 dataset 밖 action 문제를 줄인다.",
            model="dataset critic/value와 behavior-cloning regularization을 결합해 policy π가 data action에서 크게 벗어나지 않도록 한다.",
            objective="Q-value improvement와 behavior cloning penalty 사이의 tradeoff를 최적화한다.",
            constraints="dataset coverage, actor regularization coefficient와 critic stability가 필요하다.",
            success="단순한 policy constraint recipe가 offline continuous-control benchmark에서 specialized methods와 경쟁하는 것이다.",
            bottleneck="offline RL은 여러 conservative component로 복잡해지지만 핵심은 critic extrapolation과 behavior support 유지다.",
            changes="behavior cloning과 Q improvement를 최소 구성으로 결합해 method complexity와 tuning burden을 줄인다.",
            assumptions=[
                ("behavior data가 near-optimal signal을 포함", "regularized policy가 개선될 여지를 위해 필요", "low-quality demonstrations는 policy를 묶음"),
                ("critic estimate가 useful ordering을 제공", "Q-weighted improvement를 위해 필요", "rare contact action은 misranked"),
            ],
            loop="offline dataset → constrained actor-critic → action policy → limited/no online feedback의 offline learning loop다.",
            anchor="본문의 offline distribution-shift diagnosis, behavior regularization과 minimalist actor-critic formulation.",
            domain="offline_rl",
        ),
        profile(
            "Learning Complex Dexterous Manipulation with Deep Reinforcement Learning and Demonstrations",
            problem="고차원 dexterous hand가 demonstration의 coordination prior와 RL exploration을 결합해 complex manipulation을 학습한다.",
            model="hand proprioception/object state와 demonstration/reference를 policy에 condition하고 simulator RL 또는 imitation warm-start로 torque/action을 생성한다.",
            objective="task completion/reward, object pose/goal error와 stable contact를 최적화한다.",
            constraints="hand dynamics, contact/friction, joint/torque limits와 demonstration retargeting feasibility를 만족해야 한다.",
            success="pure RL보다 적은 exploration으로 difficult dexterous manipulation skill을 policy가 습득하는 것이다.",
            bottleneck="high-DOF hand의 sparse contact reward와 narrow successful trajectories는 model-free exploration을 비현실적으로 만든다.",
            changes="human demonstrations를 initialization/behavior prior로 사용한 뒤 deep RL이 task-specific correction과 dynamics를 학습한다.",
            assumptions=[
                ("demonstration이 useful contact coordination을 포함", "exploration bootstrap을 위해 필요", "retargeting error가 wrong contact prior"),
                ("sim dynamics/contact가 real hand를 대표", "policy training/transfer를 위해 필요", "friction/compliance mismatch"),
            ],
            loop="demonstration+proprioception → dexterous policy → contact dynamics → reward/feedback의 imitation-RL loop다.",
            anchor="본문의 dexterous manipulation motivation, demonstration-guided RL setup과 hand/object state-action formulation.",
            domain="manipulation",
        ),
        profile(
            "Learning Latent Plans from Play",
            problem="unstructured play trajectories에서 long-horizon task를 구성하는 reusable latent plan/skill을 발견한다.",
            model="observation/action sequence를 latent plan z와 low-level goal-conditioned policy로 factorize해 z가 subgoal/temporal abstraction을 표현한다.",
            objective="play data sequence reconstruction/action likelihood와 downstream goal-reaching success를 높인다.",
            constraints="play trajectories가 다양한 behavior transition을 포함하고 latent plan이 controllable subgoal로 decode되어야 한다.",
            success="명시적 task labels 없이 play data에서 temporally coherent latent plans를 학습해 novel goal manipulation에 transfer하는 것이다.",
            bottleneck="flat BC는 long-horizon dependency와 skill boundary를 모델링하기 어렵고 task-labeled demo는 수집 비용이 크다.",
            changes="unstructured play를 latent plan discovery와 hierarchical goal-conditioned control의 supervision으로 사용한다.",
            assumptions=[
                ("play data에 task-relevant subgoals가 반복", "latent plan discovery를 위해 필요", "random/uninformative play는 representation을 흐림"),
                ("latent plan이 low-level controller로 실행 가능", "hierarchical transfer를 위해 필요", "contact state/termination은 latent가 놓칠 수 있음"),
            ],
            loop="play observation history → latent plan/subgoal → low-level action → outcome feedback의 hierarchical policy loop다.",
            anchor="본문의 play-data setting, latent plan model과 goal-conditioned downstream manipulation formulation.",
            domain="il",
        ),
        profile(
            "Relay Policy Learning: Solving Long-Horizon Tasks via Imitation and Reinforcement Learning",
            problem="long-horizon manipulation을 여러 temporally localized subtask policy로 분해해 demonstration과 RL을 tractable하게 결합한다.",
            model="subtask/phase selector가 current observation을 보고 relay할 local policy π_i를 선택하고 each policy가 local action을 출력한다.",
            objective="각 subtask success와 transition을 높여 전체 long-horizon task return을 maximize한다.",
            constraints="subtask boundary/relay condition이 식별 가능하고 local policies의 state/action interface가 연결되어야 한다.",
            success="flat policy가 sparse long-horizon reward에서 실패하는 문제를 imitation initialization + local RL로 개선하는 것이다.",
            bottleneck="전체 task horizon의 exploration/credit assignment가 어렵고 한 policy가 모든 phase의 distribution을 모델링한다.",
            changes="long-horizon trajectory를 subtask-specific policy relay로 분해해 local data와 reward를 사용한다.",
            assumptions=[
                ("subtask segmentation/relay state가 안정적", "policy handoff를 위해 필요", "handoff error가 accumulated failure"),
                ("각 local policy가 다음 phase로 필요한 state를 남김", "composition을 위해 필요", "greedy local success가 global dead-end"),
            ],
            loop="observation → subtask selector → local policy action → phase feedback/relay의 hierarchical manipulation loop다.",
            anchor="본문의 long-horizon problem, policy relay/segmentation과 IL+RL training setup.",
            domain="il",
        ),
        profile(
            "RLBench: The Robot Learning Benchmark & Learning Environment",
            problem="multi-task imitation/RL/visual planning algorithms를 다양한 manipulation task·variation·observation에서 비교할 공통 environment를 제공한다.",
            model="task definition, scene/object state, RGB-D/segmentation/proprioception observation과 waypoint/action API를 benchmark interface로 노출한다.",
            objective="task-specific success predicate를 만족하는 policy의 generalization/few-shot performance를 비교한다.",
            constraints="simulator physics, task variation generation, demonstrations와 action mode가 고정·명시되어야 한다.",
            success="100개 task와 variation이 algorithm/data/observation choice의 차이를 재현 가능하게 드러내는 것이다.",
            bottleneck="기존 robot learning 결과는 task/scene/action protocol이 달라 숫자 비교와 generalization 해석이 어렵다.",
            changes="procedural task suite, multimodal observations, demonstrations와 evaluation API를 하나의 benchmark로 통합한다.",
            assumptions=[
                ("CoppeliaSim task/contact가 연구 질문에 충분", "simulation benchmark proxy를 위해 필요", "real contact robustness는 보장되지 않음"),
                ("waypoint demonstrations가 expert signal", "IL baseline을 위해 필요", "planner bias와 task shortcut이 학습 결과를 바꿈"),
            ],
            loop="scene/task observation → robot policy/action → simulator contact → task success feedback의 benchmark loop다.",
            anchor="본문의 100-task benchmark definition, observation/action API, variation과 demonstration protocol.",
            domain="benchmark",
            body_basis="FULL_TEXT_FORMULATION_REVIEWED",
        ),
        profile(
            "MimicGen: A Data Generation System for Scalable Robot Learning using Human Demonstrations",
            problem="소수 human demonstrations를 object/scene initial state variation에 재사용해 scalable robot manipulation dataset을 만든다.",
            model="source demonstration의 end-effector/object-relative segments를 새 scene/object pose에 retarget하고 generated trajectory를 policy training data로 저장한다.",
            objective="generated demonstration이 task success와 physical feasibility를 유지하면서 data diversity를 높인다.",
            constraints="object pose/coordinate correspondence, segmentation/subtask boundaries와 retargeted trajectory collision/contact feasibility가 필요하다.",
            success="manual demonstration collection 수를 크게 늘리지 않고 new initial state/scene에서 valid trajectories를 생성하는 것이다.",
            bottleneck="robot data scale는 teleoperation 비용에 묶이고 단일 demonstration은 initial configuration variation을 cover하지 못한다.",
            changes="demonstration을 annotated segments와 object-relative transforms로 replay해 synthetic-but-structured data generation pipeline을 제공한다.",
            assumptions=[
                ("object-relative action segment가 scene variation에서 invariant", "replay를 위해 필요", "contact geometry/occlusion change는 retargeting 실패"),
                ("generated trajectory quality가 human demo와 유사", "BC data scaling을 위해 필요", "오류가 dataset에 자동 증폭"),
            ],
            loop="human demo → retargeted trajectory generation → offline policy → rollout success feedback의 data loop다.",
            anchor="본문의 segment/transform-based generation, task variation과 generated-data validation experiments.",
            domain="robot_data",
        ),
        profile(
            "DROID: A Large-Scale In-The-Wild Robot Manipulation Dataset",
            problem="다양한 실제 환경·operator·object에서 수집한 manipulation trajectories로 policy generalization과 robustness를 학습·평가한다.",
            model="multi-camera RGB, proprioception/action, language/task metadata를 time-aligned trajectory dataset으로 구성한다.",
            objective="dataset이 diverse observation/state-action distribution을 제공해 in-the-wild manipulation success를 높인다.",
            constraints="sensor calibration/time synchronization, embodiment/action schema와 task metadata가 trajectory에 일관되게 붙어야 한다.",
            success="lab-constrained demonstrations보다 broad real-world variation에서 학습/transfer가 개선되는 것이다.",
            bottleneck="기존 robot datasets는 single lab/embodiment/controlled scene에 편중되어 deployment distribution과 gap이 크다.",
            changes="large-scale in-the-wild data collection system, standardized episode schema와 diverse task/environment distribution을 제공한다.",
            assumptions=[
                ("dataset diversity가 useful variation을 포함", "generalization을 위해 필요", "heterogeneous noise/weak labels가 learning signal을 희석"),
                ("action/camera/proprioception alignment가 정확", "behavior cloning을 위해 필요", "time offset은 policy error로 보임"),
            ],
            loop="real-world observation/action logging → dataset pretraining → policy execution → new environment feedback의 data foundation loop다.",
            anchor="본문의 in-the-wild collection protocol, trajectory schema와 manipulation-data coverage discussion.",
            domain="robot_data",
        ),
    ]
)


# Geometry, mapping, and 3D representations used by the robot loop.
add_many(
    [
        profile(
            "A Method for Registration of 3-D Shapes",
            problem="초기 정렬이 주어진 두 3D shape/point-set 사이의 rigid transform을 correspondence와 least-squares fitting으로 추정한다.",
            model="source points p_i와 target points q_j의 closest-point correspondence를 정하고 q≈Rp+t 형태의 rigid transform (R,t)을 반복 업데이트한다.",
            objective="corresponding point distance Σ_i||Rp_i+t−q_i||²를 최소화한다.",
            constraints="R∈SO(3), translation rigid transform과 충분한 overlap/초기 정렬이 필요하며 correspondence는 현재 transform에 의존한다.",
            success="두 shape가 같은 object/scene일 때 registration error가 줄고 일관된 pose/map frame을 얻는 것이다.",
            bottleneck="3D observations는 서로 다른 frame에 있고 correspondence가 알려지지 않아 downstream mapping/object pose가 직접 비교되지 않는다.",
            changes="closest-point assignment와 rigid transform fitting을 번갈아 수행하는 ICP 계열 iterative registration을 정식화한다.",
            assumptions=[
                ("초기 pose와 충분한 overlap", "correct basin의 correspondence를 만들기 위해 필요", "large displacement/symmetric shape는 local minimum"),
                ("point noise/outlier가 제한", "least-squares fit을 위해 필요", "outlier·partial scan은 wrong alignment"),
            ],
            loop="multi-view/point observation → pose registration → map/object state → planning/control의 3D state-estimation 단계다.",
            anchor="본문의 shape representation, closest-point correspondence와 rigid transform minimization/iteration 부분.",
            domain="3d_perception",
            body_basis="ABSTRACT_AND_CLASSIC_FORMULATION",
        ),
        profile(
            "PointNet: Deep Learning on Point Sets for 3D Classification and Segmentation",
            problem="unordered point cloud를 voxel/image로 변환하지 않고 permutation-invariant representation으로 분류·segmentation한다.",
            model="point set P={p_i}를 shared point MLP h(p_i)에 통과시키고 symmetric max pooling γ=max_i h(p_i)로 global feature를 만든다.",
            objective="global object class 또는 point-wise part/semantic label prediction loss를 최소화한다.",
            constraints="point permutation에 불변이어야 하고 input point sampling/noise에 robust하며, local geometric interactions는 architecture가 충분히 표현해야 한다.",
            success="raw 3D point set에서 compact global/local feature를 얻어 downstream recognition/robot perception에 사용 가능한 것이다.",
            bottleneck="voxelization은 memory/computation을 폭발시키고 multi-view image는 metric 3D geometry와 point correspondence를 잃는다.",
            changes="shared pointwise function과 symmetric aggregation으로 unordered point set을 직접 처리하는 unified network를 제시한다.",
            assumptions=[
                ("max-pooled critical points가 task geometry를 보존", "permutation invariance와 compact feature를 위해 필요", "fine contact/local topology가 누락될 수 있음"),
                ("point density/noise가 train과 유사", "robust recognition을 위해 필요", "occlusion/sparse depth는 segmentation을 흔듦"),
            ],
            loop="depth/LiDAR point cloud → semantic/geometric state → grasp/navigation/planning의 perception encoder다.",
            anchor="본문의 point-set representation, permutation invariance, shared MLP/max pooling과 classification/segmentation objectives.",
            domain="3d_perception",
        ),
        profile(
            "DROID-SLAM: Deep Visual SLAM for Monocular, Stereo, and RGB-D Cameras",
            problem="monocular/stereo/RGB-D video에서 camera trajectory와 dense scene geometry를 robust하게 jointly estimate한다.",
            model="frame images와 recurrent update hidden state로 camera pose, pixelwise depth와 correspondence를 예측하고 dense bundle adjustment를 반복한다.",
            objective="reprojection/photometric correspondence residual과 pose/depth consistency를 최소화한다.",
            constraints="camera calibration or depth/stereo geometry, temporal overlap와 static-scene assumption이 필요하며 scale observability가 sensor에 따라 다르다.",
            success="lost tracks, optimization divergence와 drift를 줄이면서 online pose/map을 제공하는 것이다.",
            bottleneck="classical SLAM은 feature loss, local optimization divergence와 accumulated drift에서 real-world robustness가 부족하다.",
            changes="recurrent learned update와 differentiable dense bundle adjustment를 결합해 multi-camera visual SLAM을 end-to-end robustify한다.",
            assumptions=[
                ("scene이 locally static하고 frame overlap이 존재", "correspondence/BA를 위해 필요", "dynamic object/fast motion은 pose residual을 오염"),
                ("camera/depth model이 calibration됨", "metric geometry를 위해 필요", "calibration drift와 rolling shutter는 systematic error"),
            ],
            loop="camera stream → pose/depth/map state → navigation/manipulation planning → next frame feedback의 state-estimation loop다.",
            anchor="본문의 visual SLAM problem, recurrent update, dense bundle adjustment와 mono/stereo/RGB-D formulation.",
            domain="3d_perception",
        ),
        profile(
            "3D Gaussian Splatting for Real-Time Radiance Field Rendering",
            problem="unbounded scene의 novel-view rendering을 neural radiance field 수준의 quality로 빠르게 학습·렌더링한다.",
            model="scene을 3D Gaussian primitives (mean, covariance, opacity, view-dependent color)로 표현하고 camera pose에서 differentiable splatting으로 image를 합성한다.",
            objective="training-view photometric reconstruction loss와 regularization을 최적화해 radiance field rendering error를 줄인다.",
            constraints="multi-view camera poses/visibility와 Gaussian covariance/opacity가 scene appearance를 설명해야 하며 geometry consistency가 별도 보장되지는 않는다.",
            success="interactive frame rate rendering과 짧은 optimization time에서 high-quality novel views를 제공하는 것이다.",
            bottleneck="NeRF는 per-ray neural query가 비싸고 fast methods는 quality를 희생해 robot navigation/planning에 실시간 사용이 어렵다.",
            changes="explicit adaptive 3D Gaussian scene representation과 visibility-aware differentiable rasterization으로 optimization/rendering을 가속한다.",
            assumptions=[
                ("camera poses와 multi-view coverage가 충분", "Gaussians를 triangulate/optimize하기 위해 필요", "sparse view/pose error는 floaters와 wrong geometry"),
                ("scene appearance가 static/mostly view-consistent", "radiance fitting을 위해 필요", "dynamic object와 changing illumination은 stale map"),
            ],
            loop="multi-view observation → 3D scene/world representation → spatial query/navigation/manipulation의 world-model layer다.",
            anchor="본문의 Gaussian parameterization, differentiable rasterization과 reconstruction/rendering objective.",
            domain="3d_perception",
        ),
        profile(
            "ConceptFusion: Open-set Multimodal 3D Mapping",
            problem="RGB-D reconstruction에 text/image/audio/click foundation feature를 pixel-aligned하게 융합해 open-vocabulary spatial query를 지원한다.",
            model="3D map voxel/point/Gaussian 위치에 RGB pixel feature (CLIP/DINO/AudioCLIP 등)를 project·aggregate해 multimodal concept embedding을 유지한다.",
            objective="multi-view feature consistency와 open-set concept retrieval/spatial relation query accuracy를 높인다.",
            constraints="camera/depth alignment, pose estimate와 foundation embedding의 pixel semantics가 map frame에 맞아야 한다.",
            success="보지 못한 object/concept를 natural language/image/audio로 query하고 robot manipulation/navigation target으로 grounding하는 것이다.",
            bottleneck="closed-set semantic map은 새로운 concept와 language goal을 표현하지 못하고 2D feature는 3D spatial relation을 잃는다.",
            changes="open-set multimodal feature를 online 3D map에 fuse하고 spatial reasoning/query interface를 추가한다.",
            assumptions=[
                ("RGB-D pose와 2D feature alignment가 정확", "3D fusion을 위해 필요", "SLAM drift/occlusion은 concept 위치를 틀리게 함"),
                ("foundation feature가 fine-grained affordance를 포함", "open-set manipulation query를 위해 필요", "semantic match가 graspability/geometry를 보장하지 않음"),
            ],
            loop="RGB-D+multimodal observation → open-set 3D map → language/spatial goal → manipulation/navigation action의 perception-to-task loop다.",
            anchor="본문의 online open-set map construction, pixel-aligned feature fusion, spatial query와 robot task examples.",
            domain="3d_perception",
        ),
        profile(
            "RVT: Robotic View Transformer for 3D Object Manipulation",
            problem="3D manipulation에 필요한 multi-view geometry를 explicit voxel의 계산비용 없이 scalable policy representation으로 사용한다.",
            model="multi-camera RGB-D observation을 virtual robot-centric views로 re-render하고 view attention transformer가 3D action heatmap/pose를 예측한다.",
            objective="task-conditioned pick/place or end-effector action prediction loss와 closed-loop manipulation success를 최적화한다.",
            constraints="camera calibration/virtual view transform, workspace voxel/resolution과 discrete action-to-motion controller가 필요하다.",
            success="여러 RLBench task/variation에서 3D reasoning success와 training/inference efficiency를 동시에 얻는 것이다.",
            bottleneck="single-view image policy는 depth/occlusion/3D pose를 놓치고 explicit voxel representations는 memory와 compute가 크다.",
            changes="multi-view attention과 virtual view rendering을 결합해 3D-aware manipulation policy를 scalable하게 만든다.",
            assumptions=[
                ("calibrated views가 workspace를 충분히 cover", "view aggregation과 action grounding을 위해 필요", "occluded contact/novel camera가 실패"),
                ("voxel/action discretization이 required precision을 유지", "policy output을 controller로 연결하기 위해 필요", "fine insertion/contact에서 quantization error"),
            ],
            loop="multi-view RGB-D → 3D action representation → end-effector motion → task feedback의 3D visuomotor loop다.",
            anchor="본문의 multi-view/virtual-view transformer, action representation과 RLBench/real manipulation setup.",
            domain="3d_perception",
        ),
        profile(
            "DUSt3R: Geometric 3D Vision Made Easy",
            problem="unknown camera intrinsics/poses를 가진 arbitrary image collection에서 dense correspondence, depth와 globally consistent 3D geometry를 한 번에 복원한다.",
            model="image pair/collection을 Transformer에 넣어 pixel-aligned pointmaps를 예측하고 pairwise pointmaps를 global frame으로 align한다.",
            objective="pointmap/3D correspondence reconstruction consistency를 학습해 camera, depth와 point cloud recovery를 지원한다.",
            constraints="images 사이에 enough overlap와 static scene이 있어야 하며 global alignment graph가 pairwise predictions를 연결해야 한다.",
            success="calibration 없이 monocular/multi-view geometry를 빠르게 얻어 robot mapping, pose와 planning에 사용할 수 있는 것이다.",
            bottleneck="classical MVS는 intrinsics/extrinsics를 먼저 알아야 하고 correspondence·triangulation·global consistency pipeline이 복잡하다.",
            changes="pointmap을 central output으로 두어 camera parameter, depth, matches와 3D reconstruction을 unified feed-forward model로 연결한다.",
            assumptions=[
                ("image overlap와 visual texture가 충분", "correspondence와 global alignment를 위해 필요", "textureless/dynamic/low-overlap scene은 ambiguity"),
                ("learned pointmap scale/geometry가 task에 적절", "robot metric planning으로 쓰기 위해 필요", "absolute scale/pose drift는 별도 calibration 필요"),
            ],
            loop="image stream → dense 3D/world state → pose/goal/action planning의 enabling perception stage다.",
            anchor="본문의 unconstrained MVS problem, pointmap prediction, global alignment과 camera/depth recovery formulation.",
            domain="3d_perception",
        ),
    ]
)


add_many(
    [
        profile(
            "World Models",
            problem="visual agent가 environment dynamics를 compact latent state로 예측해 imagination 안에서 long-horizon decision을 학습한다.",
            model="image encoder maps observation to latent z_t, recurrent/memory model predicts z_{t+1}, reward and done, and decoder reconstructs future observation.",
            objective="reconstruction/prediction error와 reward/done prediction을 줄여 learned latent world model을 만든다.",
            constraints="latent model이 action-conditioned dynamics와 relevant reward information을 보존해야 하며 imagined rollout이 stable해야 한다.",
            success="real environment interaction 일부만으로 latent dream rollout에서 policy/controller를 학습하고 actual task behavior로 transfer하는 것이다.",
            bottleneck="pixel-level model-free RL은 enormous interaction을 요구하고 raw observations에서 temporal dynamics를 매번 다시 학습한다.",
            changes="visual encoder·memory·controller를 분리한 latent world-model pipeline으로 policy search를 imagined environment로 옮긴다.",
            assumptions=[
                ("latent state가 control-sufficient", "imagined action selection을 위해 필요", "representation이 reward/contacts를 버리면 model rollout은 그럴듯해도 unsafe"),
                ("short rollout model error가 누적되지 않음", "dream training을 위해 필요", "long-horizon compounding error가 real policy를 오도"),
            ],
            loop="observation → latent world model → imagined decision/policy → real action → next observation의 model-based loop다.",
            anchor="본문의 visual latent model, memory/dynamics/reward prediction과 imagination-based control setup.",
            domain="world_model",
        ),
        profile(
            "DayDreamer: World Models for Physical Robot Learning",
            problem="real robot interaction이 비싸고 위험한 continuous-control 학습을 learned latent dynamics의 imagination으로 가속한다.",
            model="camera/proprioceptive observation을 latent RSSM state로 encode하고 recurrent stochastic dynamics가 action-conditioned future/reward를 예측한다.",
            objective="latent reconstruction/reward/dynamics loss를 학습한 뒤 imagined trajectories에서 actor-critic policy return을 maximize한다.",
            constraints="latent model이 physical dynamics와 contact-relevant observation을 충분히 예측하고, uncertainty/initial state mismatch가 제한되어야 한다.",
            success="few real interactions와 online model updates로 quadruped/robot manipulation behavior를 실제 hardware에 학습하는 것이다.",
            bottleneck="physical robot에서 millions of trial을 수집하기 어렵고 model-free RL의 sample cost가 deployment를 막는다.",
            changes="world model의 latent imagination을 real robot data loop에 직접 연결해 on-hardware model-based RL을 구현한다.",
            assumptions=[
                ("초기 real data가 dynamics를 cover", "world model bootstrap을 위해 필요", "unseen contact/impact에서 imagined policy가 실패"),
                ("latent reward/observation prediction이 control sufficient", "actor learning을 위해 필요", "visual reconstruction이 정확해도 force state는 누락될 수 있음"),
            ],
            loop="real observation → latent model update → imagined actor/critic update → real action feedback의 robot learning loop다.",
            anchor="본문의 RSSM/world-model training, latent imagination과 physical robot experiments.",
            domain="world_model",
        ),
        profile(
            "TD-MPC2: Scalable, Robust World Models for Continuous Control",
            problem="많은 continuous-control task와 task/agent variation을 하나의 latent world model + MPC policy로 scalable하게 학습한다.",
            model="latent encoder z_t, action-conditioned latent dynamics, reward/value heads를 학습하고 short horizon latent trajectory에서 terminal value를 예측한다.",
            objective="TD consistency와 reward/dynamics representation을 학습하면서 sampling-based MPC가 predicted return을 maximize한다.",
            constraints="latent dynamics가 task-relevant state를 유지하고 ensemble/task conditioning, action bounds와 horizon이 안정적이어야 한다.",
            success="single-task world model보다 다양한 domain/scale에서 robust sample-efficient continuous control을 제공하는 것이다.",
            bottleneck="world model methods는 task별 tuning·architecture·instability가 크고 continuous control scale에서 latent prediction이 어렵다.",
            changes="compact latent dynamics와 TD-MPC planning objective를 multi-task/scalable training recipe로 확장한다.",
            assumptions=[
                ("latent representation이 multiple tasks를 분리", "shared model scaling을 위해 필요", "task aliasing은 wrong value and action을 만듦"),
                ("short horizon + terminal value가 long return을 대표", "MPC 계산량을 제한하기 위해 필요", "contact transition/rare failure가 terminal estimate에 가려짐"),
            ],
            loop="state/observation → latent world model + MPC candidate rollout → action → feedback의 receding-horizon loop다.",
            anchor="본문의 latent dynamics, TD learning, MPC planning과 multi-task continuous-control formulation.",
            domain="world_model",
        ),
        profile(
            "Control Barrier Function Based Quadratic Programs for Safety Critical Systems",
            problem="nominal controller가 task performance를 추구하는 동안 control action이 state를 safe set 밖으로 내보내지 않도록 실시간 제약을 건다.",
            model="control-affine dynamics ẋ=f(x)+g(x)u와 safe function h(x)≥0를 두고 CBF condition L_fh+L_gh u+α(h)≥0를 만든다.",
            objective="nominal input u_nom과 가장 가까운 u를 QP로 찾되 barrier inequality와 input bounds를 만족한다.",
            constraints="relative-degree/CBF differentiability, known dynamics, safe-set boundary와 actuator constraints가 필요하다.",
            success="nominal performance를 최대한 유지하면서 forward invariance of safe set을 formal guarantee하는 것이다.",
            bottleneck="learned/planned action은 collision/constraint violation을 직접 보장하지 않고, rule-based clipping은 dynamics-aware safety를 놓친다.",
            changes="safety condition을 differentiable barrier inequality로 바꾸고 nominal control 위에 minimum-intervention QP filter를 둔다.",
            assumptions=[
                ("safe set과 dynamics/relative degree를 앎", "CBF derivative constraint를 계산하기 위해 필요", "model error와 unknown contact는 guarantee를 약화"),
                ("QP feasible action이 존재", "safe filter를 실행하기 위해 필요", "task/safety conflict가 infeasibility를 만듦"),
            ],
            loop="state estimate → nominal policy/control → CBF-QP safety filter → actuation → state feedback의 runtime layer다.",
            anchor="본문의 control-affine system, CBF forward-invariance condition과 quadratic-program controller.",
            domain="safety",
        ),
        profile(
            "Recovery RL: Safe Reinforcement Learning with Learned Recovery Zones",
            problem="task policy가 exploratory action으로 unsafe state에 접근할 때 learned recovery policy가 safe region으로 되돌린다.",
            model="state s와 safe/recovery zone classifier V_φ(s)를 학습하고, task policy π_task와 recovery policy π_rec 중 하나를 gate가 선택한다.",
            objective="task return을 높이면서 state distribution이 unsafe/irreversible failure region에 들어가지 않게 한다.",
            constraints="recovery zone label/critic, safe policy의 controllable set과 switching threshold가 제공되어야 한다.",
            success="task policy learning과 safety recovery를 분리해 unknown disturbance에서 catastrophic failure를 줄이는 것이다.",
            bottleneck="penalty-based safe RL은 unsafe exploration을 직접 겪어야 하고 task reward와 safety constraint를 하나의 critic이 혼합한다.",
            changes="recovery policy와 learned recovery-zone boundary를 별도 학습해 runtime action selector로 task policy를 shield한다.",
            assumptions=[
                ("recovery policy가 unsafe boundary 이전에 controllable", "rollback safety를 위해 필요", "late detection·irreversible contact는 복구 불가"),
                ("state/safety critic이 zone을 분리", "gate timing을 위해 필요", "partial observability와 OOD state에서 false safe alarm"),
            ],
            loop="state/uncertainty → task/recovery selector → action → safety feedback의 failure-prevention loop다.",
            anchor="본문의 learned recovery zone, task/recovery policy separation과 safe RL experiments.",
            domain="safety",
        ),
    ]
)


# Locomotion, humanoid, and mobile manipulation foundations.
add_many(
    [
        profile(
            "Biped Walking Pattern Generation by using Preview Control of Zero-Moment Point",
            problem="주어진 footstep/ZMP reference를 안정적으로 만족하도록 biped center-of-mass trajectory와 walking pattern을 생성한다.",
            model="linear inverted-pendulum/cart-table dynamics와 ZMP output을 두고 future ZMP reference를 preview하는 discrete linear controller를 계산한다.",
            objective="predicted ZMP와 reference ZMP error, control effort/CoM trajectory cost를 최소화한다.",
            constraints="prescribed support/contact sequence, ZMP가 support polygon 안에 있고 CoM/foot kinematics가 feasible해야 한다.",
            success="preview reference를 따라 stable walking pattern을 실시간 생성하는 것이다.",
            bottleneck="reactive footstep correction만으로는 delayed dynamics를 보지 못하고, purely local CoM control은 future support transition을 놓친다.",
            changes="미래 ZMP reference를 finite preview window에 넣는 linear pattern generator를 제시한다.",
            assumptions=[
                ("linear inverted-pendulum model", "preview control을 닫힌 선형 문제로 만들기 위해 필요", "large angular momentum/uneven terrain에서는 model mismatch"),
                ("footstep/contact sequence가 사전 지정", "support polygon constraint를 계산하기 위해 필요", "unexpected contact/fall recovery는 범위 밖"),
            ],
            loop="footstep/ZMP plan → CoM pattern → whole-body tracking → ZMP/force feedback의 locomotion planning-control loop다.",
            anchor="본문의 cart-table/ZMP model, preview control derivation과 biped walking pattern generation experiment.",
            domain="locomotion",
            body_basis="ABSTRACT_AND_CLASSIC_FORMULATION",
        ),
        profile(
            "AMP: Adversarial Motion Priors for Stylized Physics-Based Character Control",
            problem="reference motion의 style와 task goal을 동시에 만족하는 physically simulated character/robot controller를 학습한다.",
            model="motion state/history와 task command를 policy π에 넣어 joint action을 출력하고 discriminator가 reference motion과 generated motion feature를 구분한다.",
            objective="task reward를 높이면서 discriminator가 expert/reference style로 판단할 motion distribution을 생성한다.",
            constraints="physics simulator, retargetable motion clips와 stable discriminator/policy control이 필요하다.",
            success="single motion clip imitation을 넘어서 style-consistent locomotion/skill control과 task variation을 얻는 것이다.",
            bottleneck="task reward만 사용하면 unnatural gait가 나오고, direct motion tracking은 reference 밖의 goal/perturbation에 유연하지 않다.",
            changes="motion prior를 adversarial reward로 학습해 task RL policy가 natural motion manifold 안에서 행동하도록 한다.",
            assumptions=[
                ("reference motion이 desired style을 대표", "adversarial prior target을 위해 필요", "편향된 clip은 robot-safe motion과 다를 수 있음"),
                ("simulator dynamics/retargeting이 valid", "policy training을 위해 필요", "real actuator/contact mismatch는 style와 balance를 깨뜨림"),
            ],
            loop="proprioception+task command → physics policy → simulated/real motion feedback의 locomotion skill loop다.",
            anchor="본문의 motion-prior discriminator, adversarial reward와 physics-based character control formulation.",
            domain="locomotion",
        ),
        profile(
            "RMA: Rapid Motor Adaptation for Legged Robots",
            problem="terrain·dynamics가 deployment에서 바뀌어도 legged locomotion policy가 짧은 history로 hidden environment dynamics에 적응한다.",
            model="proprioceptive history를 adaptation encoder z_t로 요약하고 policy π(s_t,z_t,command)가 joint-level action을 출력한다.",
            objective="velocity tracking, stability와 energy/collision cost를 학습하며 privileged teacher의 latent adaptation target을 distill한다.",
            constraints="student가 limited onboard proprioception/history만 사용하고 terrain/dynamics randomization의 variation을 커버해야 한다.",
            success="명시적 terrain perception 없이 novel terrain/physical parameter에서 robust locomotion을 유지하는 것이다.",
            bottleneck="single policy는 simulator-to-real dynamics/terrain shift에 brittle하고 privileged simulation state는 hardware에서 사용할 수 없다.",
            changes="rapid online adaptation module과 privileged-to-privileged/student training을 분리해 hidden dynamics를 infer한다.",
            assumptions=[
                ("짧은 proprioceptive history가 environment parameter를 식별", "adaptation latent를 위해 필요", "abrupt contact/friction change는 history에 늦게 반영"),
                ("training randomization이 real variation을 cover", "zero-shot transfer를 위해 필요", "unseen terrain geometry/actuator fault는 OOD"),
            ],
            loop="proprioceptive history → adaptation latent → locomotion policy → foot contact feedback의 adaptive control loop다.",
            anchor="본문의 privileged teacher/student, adaptation encoder와 real quadruped deployment formulation.",
            domain="locomotion",
        ),
        profile(
            "Learning Robust Perceptive Locomotion for Quadrupedal Robots in the Wild",
            problem="rough terrain에서 exteroceptive terrain perception과 proprioception을 이용해 quadruped foothold/velocity를 robust하게 제어한다.",
            model="heightmap/depth/terrain observation과 proprioceptive state를 policy에 넣어 foot/joint command를 출력하고 recurrent/history state가 temporal terrain context를 유지한다.",
            objective="commanded velocity/progress를 달성하면서 body stability, foot clearance와 energy/torque cost를 최적화한다.",
            constraints="contact/friction, foot kinematics, actuator limits와 terrain collision을 만족해야 한다.",
            success="unseen natural terrain과 disturbances에서 perception-aware policy가 stable forward locomotion을 수행하는 것이다.",
            bottleneck="blind locomotion은 rough terrain을 예측하지 못하고, privileged terrain representation은 real sensor distribution에 전이되지 않는다.",
            changes="perceptive input을 locomotion policy에 통합하고 large-scale simulation randomization/real-world deployment를 함께 설계한다.",
            assumptions=[
                ("terrain observation이 foothold-relevant geometry를 포함", "perceptive policy를 위해 필요", "occlusion/noisy depth는 wrong foothold"),
                ("contact/dynamics randomization이 field variation을 cover", "robust sim-to-real을 위해 필요", "mud/slip/unknown obstacle은 failure"),
            ],
            loop="terrain/proprioception observation → foothold/motor policy → contacts → perception feedback의 locomotion loop다.",
            anchor="본문의 perceptive locomotion state/action, terrain randomization과 wild quadruped experiments.",
            domain="locomotion",
        ),
        profile(
            "ANYmal Parkour: Learning Agile Navigation for Quadrupedal Robots",
            problem="높은 장애물·gap·경사 등 heterogeneous parkour obstacle을 연속적으로 판단하고 dynamic locomotion skill로 통과한다.",
            model="terrain/perception과 command를 high-level behavior/skill selector 및 low-level motion policy에 넣어 foothold/leg actions를 생성한다.",
            objective="progress/goal reach와 behavior-specific landing/stability를 높이고 collision/fall risk와 energy를 줄인다.",
            constraints="full-body dynamics, contact sequence, takeoff/landing geometry, actuator/torque limits를 만족해야 한다.",
            success="different obstacle types와 transitions를 real ANYmal에서 agile하게 수행하는 것이다.",
            bottleneck="단일 locomotion gait는 extreme obstacle geometry와 dynamic transitions를 표현하지 못하고 behavior switching이 brittle하다.",
            changes="parkour behaviors를 skill/selector 구조와 perceptive navigation objective로 묶어 dynamic obstacle traversal을 학습한다.",
            assumptions=[
                ("obstacle class와 relevant skill을 추정", "behavior selection을 위해 필요", "ambiguous/novel obstacle에서 wrong maneuver"),
                ("simulation contact/dynamics가 landing을 대표", "training을 위해 필요", "real impact/compliance는 fall mode"),
            ],
            loop="terrain image/state → parkour skill selection → dynamic whole-body action → landing feedback의 locomotion loop다.",
            anchor="본문의 parkour obstacle/task formulation, skill selection과 real ANYmal evaluation.",
            domain="locomotion",
        ),
        profile(
            "HumanoidBench: Simulated Humanoid Benchmark for Whole-Body Locomotion and Manipulation",
            problem="복잡한 humanoid whole-body locomotion/manipulation을 공통 simulation tasks와 success criteria로 비교한다.",
            model="humanoid generalized state, contacts, proprioception/visual observation과 action interface를 environment API로 정의한다.",
            objective="task-specific goal completion/reward를 높이면서 balance, contact, joint/actuator constraints를 지킨다.",
            constraints="whole-body dynamics, contact stability, morphology/actuator limits와 task termination/success predicate가 명시된다.",
            success="여러 body parts와 long-horizon tasks에서 algorithm의 robustness/generalization gap을 재현 가능하게 측정하는 것이다.",
            bottleneck="기존 benchmark는 single skill·simplified body라 humanoid balance/manipulation coordination의 어려움을 가린다.",
            changes="dexterous hands, locomotion과 whole-body tasks를 한 simulated benchmark와 hierarchical baseline으로 통합한다.",
            assumptions=[
                ("simulator task/contact가 research question에 충분", "benchmark proxy를 만들기 위해 필요", "sim success가 hardware safety/transfer를 보장하지 않음"),
                ("observation/action API가 method comparison을 공정하게 함", "baseline 비교를 위해 필요", "camera/action mode 차이는 결과를 바꿈"),
            ],
            loop="benchmark observation/state → whole-body policy/controller → contact dynamics → task success feedback의 evaluation loop다.",
            anchor="본문의 HumanoidBench task taxonomy, state/action API, success definitions와 baseline findings.",
            domain="benchmark",
        ),
        profile(
            "OmniH2O: Universal and Dexterous Human-to-Humanoid Whole-Body Teleoperation and Learning",
            problem="사람의 full-body motion과 verbal/visual command를 full-size humanoid의 locomotion·dexterous action으로 retarget하고 학습한다.",
            model="human pose/VR/RGB/instruction를 universal kinematic pose interface로 변환하고 sim RL teacher/student가 sparse robot sensors에서 action을 출력한다.",
            objective="human motion/task goal tracking과 whole-body stability/manipulation success를 높인다.",
            constraints="retargeted pose가 humanoid kinematics/contact/actuator limits를 만족하고 teacher privileged state가 student sensor로 distill되어야 한다.",
            success="teleoperation과 learned autonomous policy가 서로 다른 whole-body tasks에서 같은 pose/action interface로 동작하는 것이다.",
            bottleneck="humanoid teleoperation은 expensive hardware/interface에 묶이고, isolated arm/locomotion data는 whole-body coordination을 제공하지 못한다.",
            changes="universal pose interface, large-scale retargeting/augmentation과 privileged-to-sparse sim-to-real policy pipeline을 결합한다.",
            assumptions=[
                ("human pose가 task/contact intent를 충분히 담음", "retargeting을 위해 필요", "force/hand-object detail은 pose만으로 소실"),
                ("retargeted motion과 RL stabilization이 compatible", "autonomy transfer를 위해 필요", "real contact/latency에서 tracking failure"),
            ],
            loop="human/visual instruction → pose retargeting/policy → humanoid whole-body action → contact feedback의 teleop-learning loop다.",
            anchor="본문의 universal kinematic interface, teleoperation data, privileged teacher/student와 Unitree H1 tasks.",
            domain="humanoid",
        ),
        profile(
            "Mobile ALOHA: Learning Bimanual Mobile Manipulation using Low-Cost Whole-Body Teleoperation",
            problem="tabletop arm-only policy로는 reachability와 bimanual coordination이 부족한 long-horizon mobile manipulation을 학습한다.",
            model="mobile base, two arms, grippers의 whole-body observation/action trajectory를 teleoperation으로 수집해 behavior-cloning policy를 학습한다.",
            objective="multi-stage household task completion을 높이고 base navigation·arm manipulation의 joint trajectory error를 줄인다.",
            constraints="base/arm kinematics, collision, bimanual object coordination과 actuator/workspace limits를 만족해야 한다.",
            success="limited demonstrations와 co-training data로 fridge/cabinet/carrying 같은 mobile bimanual task를 real robot에서 수행하는 것이다.",
            bottleneck="static tabletop dataset은 mobile reachability, whole-body balance와 long-horizon navigation-manipulation transitions를 다루지 않는다.",
            changes="low-cost whole-body teleoperation platform과 supervised BC/co-training recipe로 mobile manipulation data interface를 만든다.",
            assumptions=[
                ("teleoperation action이 task-relevant base-arm coordination을 포함", "BC target을 위해 필요", "operator latency/compensation은 policy bias"),
                ("co-training static/mobile data의 action semantics가 호환", "data efficiency를 위해 필요", "embodiment/action distribution mismatch는 negative transfer"),
            ],
            loop="multimodal observation → base+dual-arm action → object/contact feedback → next observation의 mobile manipulation loop다.",
            anchor="본문의 Mobile ALOHA hardware/action interface, teleoperation dataset과 co-training task formulation.",
            domain="mobile_manipulation",
        ),
    ]
)


# Vision-language representations, generalist robot policies, and world/safety.
add_many(
    [
        profile(
            "Learning Transferable Visual Models From Natural Language Supervision",
            problem="image representation이 고정 label set에 묶이지 않고 자연어 concept와 visual appearance를 함께 generalize하도록 학습한다.",
            model="image encoder f_I(I)와 text encoder f_T(t)의 normalized embedding을 contrastive pair objective로 정렬한다.",
            objective="matched image-text pair의 similarity를 높이고 batch 내 mismatched pair를 구분한다.",
            constraints="internet-scale paired image-text data와 language vocabulary가 target visual concept를 충분히 cover해야 한다.",
            success="unseen text query와 downstream robot observation을 shared embedding으로 연결해 zero-shot recognition/grounding을 제공하는 것이다.",
            bottleneck="closed-set supervised vision은 task-specific label과 dataset bias에 묶여 새 instruction/object concept를 표현하지 못한다.",
            changes="language supervision을 visual pretraining target으로 사용해 open-vocabulary semantic prior를 만든다.",
            assumptions=[
                ("image-text pair가 의미적으로 정렬", "contrastive signal을 만들기 위해 필요", "web noise/bias는 rare robot object semantics를 오염"),
                ("embedding similarity가 action-relevant concept를 보존", "robot grounding으로 전이하기 위해 필요", "visual recognition과 affordance/geometry는 불일치할 수 있음"),
            ],
            loop="camera observation → language-aligned visual state → task/affordance decision의 perception foundation이다.",
            anchor="본문의 image-text contrastive objective, zero-shot transfer와 large-scale web data formulation.",
            domain="vision",
        ),
        profile(
            "CLIPort: What and Where Pathways for Robotic Manipulation",
            problem="language가 지시하는 semantic object와 실제 집어야 할 spatial pixel/pose를 동시에 grounding해 manipulation action으로 변환한다.",
            model="language-conditioned semantic pathway와 spatially equivariant transport pathway가 image observation을 pick/place correspondence map으로 표현한다.",
            objective="언어 instruction에 맞는 pick location과 place location의 transport likelihood를 높인다.",
            constraints="camera frame과 workspace calibration, language-object correspondence와 pick/place action primitive가 주어져야 한다.",
            success="unseen language composition과 object arrangement에서 correct pick-place pose를 예측하는 것이다.",
            bottleneck="language model embedding은 where 정보를 잃고, pure visual transport는 what/goal semantics를 표현하지 못한다.",
            changes="what(semantic)과 where(spatial equivariant) representation을 분리·결합하는 two-pathway manipulation policy를 제시한다.",
            assumptions=[
                ("task가 pick-place primitive으로 표현", "action output을 정의하기 위해 필요", "tool use·contact-rich action은 추가 primitive가 필요"),
                ("camera image에 target geometry가 보임", "spatial transport를 위해 필요", "occlusion·depth ambiguity에서 wrong pixel 선택"),
            ],
            loop="RGB/language observation → pick/place correspondence → end-effector action → task feedback의 visuomotor loop다.",
            anchor="본문의 what/where pathway, transport formulation과 language/task composition evaluation.",
            domain="vla",
        ),
        profile(
            "PaLM-E: An Embodied Multimodal Language Model",
            problem="vision, language와 continuous sensor/state input을 하나의 language-model reasoning context로 결합해 embodied task를 수행한다.",
            model="image/state embeddings를 language token stream에 interleave하고 autoregressive multimodal Transformer가 text answer 또는 action-relevant output을 예측한다.",
            objective="multimodal sequence likelihood와 embodied task/action objective를 공동 학습해 observation-conditioned reasoning을 얻는다.",
            constraints="모달리티 tokenization이 spatial/proprioceptive information을 보존하고 robot action head/embodiment interface가 있어야 한다.",
            success="훈련된 language/vision knowledge가 robot task의 novel object, instruction과 multi-task reasoning으로 transfer되는 것이다.",
            bottleneck="separate VLM과 robot policy를 이어 붙이면 web knowledge가 physical state/action semantics로 grounding되지 않는다.",
            changes="continuous embodied observations를 language-model input space에 직접 삽입해 general-purpose multimodal model을 embodied learner로 확장한다.",
            assumptions=[
                ("sensor embedding이 LM context에 안정적으로 align", "multimodal reasoning을 위해 필요", "token compression이 fine geometry/contact cue를 잃을 수 있음"),
                ("web prior와 robot data의 objective가 충돌하지 않음", "joint transfer를 위해 필요", "language fluency가 physical feasibility를 보장하지 않음"),
            ],
            loop="visual/proprioceptive observation+language → multimodal reasoning → task/action output의 VLA interface다.",
            anchor="본문의 embodied token input, multimodal LM training과 robot transfer tasks.",
            domain="vla",
        ),
        profile(
            "RT-1: Robotics Transformer for Real-World Control at Scale",
            problem="많은 task/instruction과 real-world variation을 하나의 robot policy로 학습하면서 image stream을 low-level action으로 안정적으로 변환한다.",
            model="camera image history와 natural-language task token을 Transformer policy에 넣어 discretized end-effector/base action token과 termination을 예측한다.",
            objective="offline demonstration의 next-action cross-entropy를 minimize해 multi-task behavior cloning policy를 학습한다.",
            constraints="data collection platform/action vocabulary가 shared interface를 가져야 하고 camera/proprioception observation이 task state를 충분히 표현해야 한다.",
            success="single task policy collection보다 많은 real tasks와 unseen scene variation에서 one model이 reliable action을 출력하는 것이다.",
            bottleneck="task-specific BC는 data/model을 재사용하지 못하고, real-world policy scale에서 temporal/action representation과 inference throughput이 병목이다.",
            changes="robot trajectories를 token sequence로 바꾸는 Robotics Transformer와 large-scale multi-task data/augmentation을 제시한다.",
            assumptions=[
                ("shared action tokenization이 task/robot behavior를 표현", "multi-task model을 위해 필요", "contact-specific continuous precision은 quantization에 손상"),
                ("demonstration distribution이 deployment scene을 cover", "BC generalization을 위해 필요", "novel object/failure recovery는 unseen"),
            ],
            loop="image/language history → action-token policy → low-level controller → next frame feedback의 VLA execution loop다.",
            anchor="본문의 RT-1 input/action token interface, large-scale real-robot data와 multi-task policy formulation.",
            domain="vla",
        ),
        profile(
            "RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control",
            problem="web-scale vision-language knowledge를 robot action token으로 transfer해 novel concepts/instructions를 physical manipulation에 grounding한다.",
            model="VLM/vision-language Transformer가 image+language token sequence를 받아 coordinate/discrete action token을 autoregressively 예측한다.",
            objective="web VQA/captioning와 robot trajectory/action token likelihood를 co-fine-tune해 semantic generalization과 control을 함께 학습한다.",
            constraints="action을 language-like token으로 serialize할 수 있고 web semantics와 robot action labels가 shared vocabulary로 연결되어야 한다.",
            success="훈련에 없던 object/property/instruction을 web prior로 추론하고 실행 가능한 robot action으로 변환하는 것이다.",
            bottleneck="robot-only data는 semantic coverage가 작고, VLM output은 physical action/geometry로 직접 이어지지 않는다.",
            changes="robot action을 multimodal token prediction task로 놓아 pretrained VLM의 knowledge와 control fine-tuning을 결합한다.",
            assumptions=[
                ("web concept와 robot affordance가 대응", "zero-shot transfer를 위해 필요", "semantic similarity가 grasp/contact feasibility를 보장하지 않음"),
                ("token action resolution이 task precision을 제공", "physical execution을 위해 필요", "fine contact와 latency는 discrete autoregression에 취약"),
            ],
            loop="image+language → VLA token reasoning/action → robot controller → visual feedback의 semantic-to-action loop다.",
            anchor="본문의 web-to-robot transfer, action tokenization과 emergent generalization setup.",
            domain="vla",
        ),
        profile(
            "VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models",
            problem="open-ended language instruction을 3D workspace에서 조작 가능한 spatial constraints/value로 바꾸고 low-level controller와 연결한다.",
            model="language model이 instruction을 3D value maps와 affordance/collision functions로 분해하고, motion optimizer가 point cloud/robot state 위에서 trajectory를 선택한다.",
            objective="language-specified target/affordance value를 높이고 collision·workspace·smoothness cost를 낮추는 end-effector trajectory를 찾는다.",
            constraints="3D scene geometry, object grounding, kinematic/collision checker와 primitive controller가 제공되어야 한다.",
            success="새 language composition을 재학습 없이 compositional 3D constraint와 executable manipulation trajectory로 grounding하는 것이다.",
            bottleneck="LLM text plan은 metric geometry와 collision feasibility가 없고, end-to-end VLA는 novel instruction에서 action semantics가 opaque하다.",
            changes="LLM을 3D value/affordance map program generator로 사용하고 conventional motion optimizer/control에 연결한다.",
            assumptions=[
                ("scene reconstruction과 object grounding이 정확", "3D map composition을 위해 필요", "occlusion/pose error는 plan collision과 wrong target을 만듦"),
                ("language decomposition이 valid primitive으로 변환", "open-vocabulary control을 위해 필요", "ambiguous instruction과 unmodeled contact는 실패"),
            ],
            loop="vision+language → 3D value/constraint map → motion/action optimization → contact feedback의 task-to-motion loop다.",
            anchor="본문의 value map/affordance program, 3D scene representation과 real manipulation interface.",
            domain="vla",
        ),
        profile(
            "Open X-Embodiment: Robotic Learning Datasets and RT-X Models",
            problem="서로 다른 robot embodiment·action convention·task dataset을 공동 학습해 cross-embodiment policy scaling의 benefit을 측정한다.",
            model="heterogeneous trajectory (observation, language, action, proprioception)를 normalized RT-X action/observation interface로 map해 Transformer policy를 학습한다.",
            objective="각 embodiment의 demonstration action likelihood 또는 task success를 하나의 multi-robot dataset에서 높인다.",
            constraints="action/state normalization과 embodiment metadata가 shared policy가 구분해야 할 차이를 보존해야 한다.",
            success="다양한 robot data joint training이 단일-dataset policy보다 target embodiment/task generalization을 높이는 것이다.",
            bottleneck="robot data가 platform별로 silo되어 scale이 작고, 서로 다른 morphology/control frequency를 그대로 합치기 어렵다.",
            changes="large heterogeneous robot dataset과 cross-embodiment RT-X policy/training interface를 공개한다.",
            assumptions=[
                ("embodiment-conditioned interface가 action semantics를 보존", "joint policy를 위해 필요", "misalignment는 negative transfer와 unsafe action을 만듦"),
                ("dataset quality/coverage가 충분", "scaling benefit을 위해 필요", "많은 weak demonstrations가 rare contact skill을 희석"),
            ],
            loop="multi-robot observation/metadata → shared policy → embodiment adapter/controller → rollout feedback의 data-scaling loop다.",
            anchor="본문의 Open X-Embodiment data schema, RT-X multi-robot training과 transfer formulation.",
            domain="vla",
        ),
        profile(
            "Octo: An Open-Source Generalist Robot Policy",
            problem="heterogeneous robot trajectory와 language/image goal을 lightweight open policy로 통합해 new task/robot에 fine-tune한다.",
            model="observation, language/goal image, proprioception token을 diffusion/Transformer-style policy backbone에 condition해 action chunk를 생성한다.",
            objective="cross-embodiment demonstration action sequence의 conditional likelihood/denoising objective를 최소화한다.",
            constraints="dataset action normalization, observation token schema와 robot-specific fine-tuning interface가 필요하다.",
            success="pretraining checkpoint가 적은 new demonstrations로 unseen task/embodiment에 adapted policy를 제공하는 것이다.",
            bottleneck="각 robot policy는 data와 compute를 중복하고, closed generalist models는 reproducibility/adapter comparison을 막는다.",
            changes="open model/data/training recipe와 flexible goal conditioning/action chunk interface를 제공한다.",
            assumptions=[
                ("shared token interface가 embodiment variation을 흡수", "generalist pretraining을 위해 필요", "morphology/action-rate mismatch는 adapter bottleneck"),
                ("pretraining data가 target task prior를 포함", "few-shot adaptation을 위해 필요", "novel contact mode는 demonstration이 필요"),
            ],
            loop="multimodal goal+observation history → action chunk → robot controller → feedback의 generalist policy loop다.",
            anchor="본문의 observation/goal tokenization, action chunk prediction과 multi-robot pretraining/fine-tuning setup.",
            domain="vla",
        ),
        profile(
            "OpenVLA: An Open-Source Vision-Language-Action Model",
            problem="web vision-language prior와 약 1M real robot demonstrations를 open VLA로 결합해 task/object/language generalization을 높인다.",
            model="image와 language를 pretrained vision-language backbone에 넣고 autoregressive action token head가 normalized robot action chunk를 예측한다.",
            objective="robot demonstration의 action token likelihood를 fine-tune해 instruction-conditioned control을 학습한다.",
            constraints="heterogeneous data의 action convention, camera/proprioception schema와 token quantization이 embodiment별로 정렬되어야 한다.",
            success="closed VLA와 비교 가능한 generalist manipulation 성능을 공개 weights/data/code로 재현하고 new robot/task에 fine-tune하는 것이다.",
            bottleneck="로봇 policy는 data diversity가 작고 closed VLA는 architecture/training/data를 감사하기 어렵다.",
            changes="7B open VLA, diverse robot demonstrations와 reproducible fine-tuning/evaluation stack을 제시한다.",
            assumptions=[
                ("web semantic prior가 action-relevant visual concept로 전이", "VLA generalization을 위해 필요", "semantic knowledge가 force/contact policy는 대체하지 못함"),
                ("action tokens/chunk가 controller precision을 보존", "real execution을 위해 필요", "quantization과 autoregressive latency가 reactive task를 제한"),
            ],
            loop="image+language+proprioception → action token/chunk → low-level controller → next observation의 VLA loop다.",
            anchor="본문의 open-VLA architecture, 970k robot demonstration interface와 generalist manipulation problem.",
            domain="vla",
        ),
        profile(
            "π0: A Vision-Language-Action Flow Model for General Robot Control",
            problem="heterogeneous robot embodiment와 dexterous task를 하나의 generalist policy로 다루면서 high-dimensional continuous action을 빠르게 생성한다.",
            model="pretrained VLM representation과 action expert가 image/language/proprioception을 condition으로 continuous action chunk의 flow-matching velocity를 예측한다.",
            objective="demonstration action distribution을 conditional flow vector-field regression으로 학습해 chunk sample을 생성한다.",
            constraints="cross-embodiment action normalization/adapter, flow ODE integration budget과 action chunk feedback rate가 필요하다.",
            success="semantic VLM prior와 continuous dexterous action generation을 결합해 multi-platform manipulation generalization을 얻는 것이다.",
            bottleneck="discrete autoregressive action token은 long/high-frequency action에 느리고, robot-only policy는 semantic/data coverage가 작다.",
            changes="VLM backbone 위에 flow-matching action expert를 두고 continuous action chunk와 heterogeneous robot data를 공동 학습한다.",
            assumptions=[
                ("embodiment actions가 common adapter로 align", "joint flow policy를 위해 필요", "misaligned coordinates는 unsafe transfer"),
                ("flow sample latency가 feedback loop에 허용", "continuous control을 위해 필요", "긴 integration과 chunk open-loop는 contact recovery를 늦춤"),
            ],
            loop="vision/language/proprioception → flow action chunk → partial execution → feedback/replan의 generalist control loop다.",
            anchor="RSS 본문의 flow-matching action expert, VLM conditioning과 cross-embodiment control formulation.",
            domain="vla",
            body_basis="BODY_FORMULATION_REVIEWED",
        ),
        profile(
            "π0.5: a Vision-Language-Action Model with Open-World Generalization",
            problem="closed-set robot demonstrations를 넘어 novel object, scene와 language composition에 robust한 open-world VLA control을 얻는다.",
            model="vision-language backbone과 continuous/flow action module이 visual observation, instruction, proprioception/history를 condition으로 action chunk를 생성한다.",
            objective="diverse robot/web or synthetic data에서 action prediction과 open-world task success를 공동 개선한다.",
            constraints="open-world visual concept와 robot affordance를 align할 data/representation이 필요하며 embodiment adapter와 control rate가 유지되어야 한다.",
            success="훈련에 없거나 분포가 달라진 object/scene/task에서도 semantic grounding과 physical execution을 함께 유지하는 것이다.",
            bottleneck="prior VLA는 data distribution과 object vocabulary에 과적합하고 novel visual context에서 action failure를 detect/recover하지 못한다.",
            changes="π0 flow/control interface를 open-world data/grounding strategy로 확장해 semantic generalization과 robot action을 함께 다룬다.",
            assumptions=[
                ("open-world data가 target concept/affordance를 간접적으로 cover", "generalization을 위해 필요", "rare geometry/contact regime는 여전히 OOD"),
                ("semantic novelty와 dynamics novelty가 분리 가능", "policy conditioning을 위해 필요", "visual novelty가 unseen force/contact state를 숨길 수 있음"),
            ],
            loop="open-world observation+language → VLA action chunk → contact/execution → visual feedback·replan의 closed loop다.",
            anchor="본문의 open-world generalization setting, π0.5 observation/action formulation과 novel-scene evaluation.",
            domain="vla",
        ),
    ]
)


# Grasping, contact, tactile sensing, and the first generalist robot policies.
add_many(
    [
        profile(
            "Planning Optimal Grasps",
            problem="object geometry와 frictional contact model 아래에서 물체를 안정적으로 잡고 원하는 wrench를 만들 contact placement를 선택한다.",
            model="finger contact 위치와 contact forces를 grasp map G, friction cone과 object wrench space로 표현한다.",
            objective="force-closure/robust grasp quality 또는 desired object wrench를 만족하는 contact configuration을 최적화한다.",
            constraints="finger가 object surface에 놓이고 friction cone·normal force·hand kinematics를 만족해야 한다.",
            success="작은 modeling/force disturbance에도 object wrench를 지지하고 grasp가 안정적으로 유지되는 것이다.",
            bottleneck="단순 geometric proximity는 contact wrench와 frictional stability를 보장하지 않아 grasp 후보의 실제 robustness를 설명하지 못한다.",
            changes="grasp를 discrete finger pose 선택이 아니라 wrench-space quality와 contact constraints를 갖는 optimization problem으로 정식화한다.",
            assumptions=[
                ("object geometry와 friction coefficient를 앎", "contact/wrench feasibility를 계산하기 위해 필요", "perception error·unknown material은 quality estimate를 오도"),
                ("rigid contact와 quasi-static wrench model", "force closure 기준을 만들기 위해 필요", "dynamic grasp, compliance와 slip은 직접 보장되지 않음"),
            ],
            loop="3D object state → grasp/contact decision → hand actuation → force/slip feedback의 manipulation planning 단계다.",
            anchor="본문의 grasp representation, contact/wrench mapping과 grasp quality/optimization formulation.",
            domain="manipulation",
            body_basis="ABSTRACT_AND_CLASSIC_FORMULATION",
        ),
        profile(
            "GelSight: High-Resolution Robot Tactile Sensors for Estimating Geometry and Force",
            problem="contact patch의 fine geometry와 force를 low-resolution proprioception만으로 알기 어려운 manipulation에서 tactile observation을 제공한다.",
            model="deformable elastomer의 camera image I_t를 contact surface deformation, 3D shape와 force-related tactile state로 map한다.",
            objective="image-derived contact geometry/force estimate의 reconstruction or regression error를 줄인다.",
            constraints="sensor skin의 known material/calibration과 sufficient contact visibility가 필요하며 camera/illumination response가 stable해야 한다.",
            success="grasped object shape·contact location·normal/shear force를 high spatial resolution으로 추정해 closed-loop manipulation에 사용할 수 있는 것이다.",
            bottleneck="vision은 occluded contact를 볼 수 없고 conventional force sensor는 contact patch geometry와 distributed pressure를 잃는다.",
            changes="camera와 compliant elastomer를 결합해 contact deformation을 dense visual tactile signal로 바꾸는 hardware/estimation interface를 제시한다.",
            assumptions=[
                ("elastomer deformation이 contact force/geometry와 재현성 있게 연결", "calibration-based estimate를 위해 필요", "hysteresis·wear·temperature는 mapping을 바꿈"),
                ("contact가 sensor surface 안에 있음", "image-to-contact inference를 위해 필요", "edge contact·occlusion·multi-contact는 ambiguity를 만듦"),
            ],
            loop="contact → tactile image → geometry/force state estimate → grasp/manipulation feedback의 sensing layer다.",
            anchor="본문의 tactile sensor construction, gel deformation image와 geometry/force estimation experiments.",
            domain="tactile",
            body_basis="ABSTRACT_AND_CLASSIC_FORMULATION",
        ),
        profile(
            "Contact-Invariant Optimization for Hand Manipulation",
            problem="hand-object contact가 바뀌어도 task behavior를 유지하는 manipulation trajectory와 contact configuration을 찾는다.",
            model="hand configuration q와 object pose x, contact locations/forces를 trajectory optimization variables로 두고 contact mode를 명시적으로 고정하지 않는다.",
            objective="task-space manipulation goal과 smoothness/effort를 최소화하면서 contact-invariant feature/constraint를 만족한다.",
            constraints="hand kinematics, nonpenetration, friction/contact consistency와 grasp/object dynamics를 각 time step에서 만족해야 한다.",
            success="새 contact가 생기거나 일부 contact가 사라져도 동일한 high-level manipulation behavior가 실행되는 것이다.",
            bottleneck="fixed contact mode planning은 hand trajectory를 brittle하게 만들고, contact sequence를 모두 열거하면 combinatorial search가 커진다.",
            changes="contact configuration 변화에 덜 민감한 objective/representation을 trajectory optimization에 넣어 mode enumeration 의존성을 줄인다.",
            assumptions=[
                ("contact geometry와 differentiable distance/constraint가 계산 가능", "optimization gradient를 위해 필요", "discontinuous impact와 friction switching은 local model을 깨뜨림"),
                ("invariance가 task에 충분", "contact variation을 흡수하기 위해 필요", "정밀 force regulation은 invariant position objective만으로 부족"),
            ],
            loop="object/hand observation → contact-aware trajectory decision → dexterous execution → contact feedback의 manipulation loop다.",
            anchor="본문의 contact-invariant objective, hand manipulation trajectory optimization과 contact variation experiments.",
            domain="manipulation",
        ),
        profile(
            "GraspNet-1Billion: A Large-Scale Benchmark for General Object Grasping",
            problem="unseen object와 clutter에서 6-DoF grasp detection을 공통 data/metric으로 학습·비교할 benchmark가 필요하다.",
            model="RGB-D/point cloud scene O를 입력으로 object별 grasp pose g∈SE(3), gripper width와 quality score를 예측한다.",
            objective="predicted grasp가 collision-free이고 physical pickup에 성공할 확률을 높인다.",
            constraints="gripper kinematics, object collision, approach direction·width와 force/contact feasibility를 만족해야 한다.",
            success="large-scale unseen object/clutter split에서 predicted top-k grasp의 physical success와 detection quality를 비교 가능한 방식으로 측정하는 것이다.",
            bottleneck="기존 grasp dataset은 object/scene diversity와 standardized physical evaluation이 부족해 generalization을 분리하기 어렵다.",
            changes="대규모 synthetic/real object grasp corpus, cluttered scene setup과 6-DoF grasp benchmark protocol을 제공한다.",
            assumptions=[
                ("depth/geometry가 grasp candidate를 충분히 관측", "6-DoF pose proposal을 위해 필요", "occlusion·reflective object는 candidate를 누락"),
                ("simulated grasp quality가 real pickup과 상관", "large-scale supervision을 위해 필요", "friction·compliance·gripper mismatch가 ranking을 바꿈"),
            ],
            loop="RGB-D/point cloud → grasp proposal/ranking → grasp execution → binary success feedback의 manipulation perception interface다.",
            anchor="본문의 benchmark definition, grasp representation/dataset construction과 physical evaluation protocol.",
            domain="manipulation",
        ),
        profile(
            "Contact-GraspNet: Efficient 6-DoF Grasp Generation in Cluttered Scenes",
            problem="cluttered point cloud에서 sequential object segmentation·pose estimation 없이 closed-loop에 쓸 6-DoF contact grasp를 빠르게 생성한다.",
            model="scene point cloud P의 각 point/contact를 condition으로 gripper pose, approach direction, width와 grasp score를 dense하게 예측한다.",
            objective="contact가 object를 stable하게 grasp하고 scene collision 없이 pickup하는 candidate distribution을 maximize한다.",
            constraints="predicted gripper geometry·approach가 observed clutter와 collision-free이고 contact/friction feasibility를 만족해야 한다.",
            success="unseen objects in structured clutter에서 적은 sequential failure와 낮은 inference latency로 successful grasp를 제공하는 것이다.",
            bottleneck="multi-stage 6-DoF grasp pipelines는 segmentation/pose errors가 누적되고 clutter에서 runtime이 closed-loop grasping에 맞지 않는다.",
            changes="point-wise contact-conditioned, end-to-end grasp generation으로 scene-to-grasp pipeline을 단순화한다.",
            assumptions=[
                ("point cloud가 contact-relevant surface를 포함", "dense grasp generation을 위해 필요", "occlusion과 sparse depth에서는 wrong contact가 많음"),
                ("training synthetic/real distribution이 clutter를 대표", "unseen grasp generalization을 위해 필요", "new gripper/material/friction은 ranking을 흔듦"),
            ],
            loop="depth/point cloud → contact grasp proposal → gripper motion → pickup/contact feedback의 perception-to-action loop다.",
            anchor="본문의 cluttered-scene motivation, point-wise grasp/contact parameterization과 robot grasp study.",
            domain="manipulation",
        ),
        profile(
            "Factory: Fast Contact for Robotic Assembly",
            problem="assembly에서 contact-rich insertion/fit을 높은 frequency로 수행하면서 learned policy가 위치와 force 변화에 반응하게 한다.",
            model="visual/proprioceptive/force observation o_t와 action history를 policy가 받아 end-effector pose/velocity/force action chunk를 출력한다.",
            objective="assembly goal success와 alignment/progress를 높이고 contact force·time을 제한한다.",
            constraints="peg/hole geometry, collision/nonpenetration, force/torque limits와 safety termination을 지켜야 한다.",
            success="다양한 contact-rich assembly task에서 fast policy inference와 real-world success를 함께 달성하는 것이다.",
            bottleneck="pure visual open-loop imitation은 contact onset·misalignment를 늦게 감지하고, task-specific controller는 data/skill scale이 어렵다.",
            changes="large-scale contact-aware data/system과 fast action interface를 사용해 assembly behavior를 학습 가능한 benchmark/problem으로 묶는다.",
            assumptions=[
                ("force/visual feedback가 contact state를 식별할 만큼 빠름", "reactive assembly를 위해 필요", "sensor delay는 insertion force spike를 놓침"),
                ("task geometry가 training distribution에 포함", "skill transfer를 위해 필요", "새 tolerance/material은 recovery mode가 필요"),
            ],
            loop="visual/force observation → contact-aware policy → assembly motion/force → success/failure feedback의 high-rate loop다.",
            anchor="본문의 fast contact-rich assembly setup, action/observation interface와 physical task formulation.",
            domain="tactile",
        ),
        profile(
            "Global Planning for Contact-Rich Manipulation via Local Smoothing of Quasi-Dynamic Contact Models",
            problem="contact mode가 연속적으로 바뀌는 manipulation에서 global task path와 quasi-dynamic contact motion을 함께 계획한다.",
            model="object/robot configuration x_t, contact mode/force와 control u_t를 quasi-static/quasi-dynamic equations와 trajectory constraints에 넣는다.",
            objective="goal-reaching trajectory의 path/control cost와 contact transition cost를 최소화한다.",
            constraints="unilateral contact, friction cone, nonpenetration, kinematic limits와 object quasi-dynamic force balance를 만족한다.",
            success="local smoothing이 생성한 trajectory가 multiple contact modes를 연결하고 실제 contact-rich task에서 실행 가능한 것이다.",
            bottleneck="sampling-based global planning은 contact manifold를 찾기 어렵고, local optimizer는 initial mode/path에 갇힌다.",
            changes="quasi-dynamic contact model을 local smoothing problem으로 만들어 global planner가 contact transitions를 다룰 수 있게 한다.",
            assumptions=[
                ("quasi-dynamic model이 contact outcome을 대표", "force/motion feasibility를 최적화하기 위해 필요", "impact/inertia-dominant manipulation에서는 오차가 큼"),
                ("relevant contact mode와 initial path가 탐색됨", "global/local planner 연결에 필요", "unknown mode/open-world object는 누락"),
            ],
            loop="scene/object state → global contact plan → local trajectory smoothing → execution/contact feedback의 planning-control loop다.",
            anchor="본문의 quasi-dynamic contact equations, global planning/local smoothing 분해와 manipulation experiments.",
            domain="manipulation",
        ),
        profile(
            "Tactile-Driven Non-Prehensile Object Manipulation via Extrinsic Contact Mode Control",
            problem="손으로 잡지 않는 pushing/sliding manipulation에서 object pose를 tactile feedback으로 추정하고 contact mode를 online 전환한다.",
            model="object pose x_t와 extrinsic contact mode m_t를 tactile/vision observation으로 추정하고 control u_t를 mode-conditioned policy/planner가 선택한다.",
            objective="target object pose/rearrangement goal을 달성하면서 contact force, slip과 action length를 제한한다.",
            constraints="support surface, friction, nonpenetration, pusher/object kinematics와 mode transition feasibility를 만족한다.",
            success="visual model이 불확실한 contact에서 tactile event가 mode를 알려주고 pushing trajectory를 closed-loop로 수정하는 것이다.",
            bottleneck="non-prehensile contact는 grasped object처럼 rigidly controlled되지 않고 small friction/pose error가 motion mode를 바꾼다.",
            changes="tactile-driven mode inference/control을 explicit action interface로 두어 visual-only open-loop planning을 보완한다.",
            assumptions=[
                ("tactile signal이 mode transition을 식별", "feedback controller의 state를 만들기 위해 필요", "ambiguous contact와 sensor saturation은 mode aliasing"),
                ("quasi-static/friction model이 target surface에 근접", "pushing outcome를 예측하기 위해 필요", "dynamic impact·deformable object는 별도 model 필요"),
            ],
            loop="tactile/vision observation → contact mode estimate → push action → tactile feedback의 non-prehensile loop다.",
            anchor="본문의 extrinsic contact mode 정의, tactile-driven control policy와 non-prehensile task setup.",
            domain="tactile",
        ),
        profile(
            "RoboPack: Learning Tactile-Informed Dynamics Models for Dense Packing",
            problem="dense packing에서 occluded object interaction과 contact force를 visual observation만으로 예측하기 어려워 tactile-informed dynamics model이 필요하다.",
            model="packed object state/latent geometry z_t, robot action u_t와 tactile/vision observation o_t를 dynamics pθ(z_{t+1}|z_t,u_t,o_t)로 예측한다.",
            objective="packing progress/density와 next-state prediction accuracy를 높이고 collision/force cost를 낮춘 action을 선택한다.",
            constraints="container/object geometry, nonpenetration, gripper workspace와 force/torque safety bounds를 만족한다.",
            success="부분적으로 가려진 dense contact에서도 tactile feedback이 state transition prediction과 planning을 개선하는 것이다.",
            bottleneck="vision-only model은 hidden contact와 object arrangement change를 관측하지 못하고, sparse tactile alone은 global geometry를 잃는다.",
            changes="tactile observation을 learned dynamics/world model에 결합해 dense packing의 hidden contact state를 예측한다.",
            assumptions=[
                ("tactile signal이 hidden packing state와 상관", "latent dynamics observability를 위해 필요", "sensor placement·occlusion은 unseen contact를 남김"),
                ("training packing distribution이 deployment geometry를 cover", "model-based action selection을 위해 필요", "새 object shape/friction은 rollout bias"),
            ],
            loop="vision+tactile observation → dynamics prediction/planning → packing action → contact feedback의 model-based manipulation loop다.",
            anchor="본문의 dense-packing setup, tactile-informed dynamics model과 planning/control objective.",
            domain="tactile",
        ),
        profile(
            "DexTrack: Towards Generalizable Neural Tracking Control for Dexterous Manipulation from Human References",
            problem="human reference motion을 다른 hand embodiment에서 retarget하면서 object/contact dynamics를 유지하는 dexterous tracking policy를 학습한다.",
            model="reference pose/motion r_t, robot proprioception q_t와 object/vision state를 입력으로 torque/position action u_t를 출력한다.",
            objective="reference tracking error와 object task error를 최소화하면서 smooth/feasible hand motion을 생성한다.",
            constraints="hand joint/velocity/torque limits, object nonpenetration, contact/grasp constraints와 embodiment kinematics를 만족한다.",
            success="novel human reference와 object/task variation에서도 stable dexterous tracking과 manipulation outcome을 유지하는 것이다.",
            bottleneck="kinematic retargeting만으로는 hand dynamics·contact force·embodiment 차이를 설명하지 못하고 trajectory tracking이 brittle하다.",
            changes="reference-conditioned neural tracking control을 contact/task objective와 결합해 motion capture를 direct action skill로 바꾼다.",
            assumptions=[
                ("reference가 task-relevant motion/contact cue를 포함", "policy conditioning을 위해 필요", "reference에 unseen contact/occlusion이 있으면 extrapolation"),
                ("simulator/training dynamics가 hand contact를 대표", "generalization을 위해 필요", "real tendon/compliance mismatch가 tracking을 깨뜨림"),
            ],
            loop="human reference+robot state → neural tracking action → dexterous contact → visual/tactile feedback의 skill-control loop다.",
            anchor="본문의 reference-conditioned tracking problem, hand/object state-action interface와 generalization experiments.",
            domain="manipulation",
        ),
    ]
)


# Reinforcement learning, imitation learning, and generative action foundations.
add_many(
    [
        profile(
            "Learning to Predict by the Methods of Temporal Differences",
            problem="episode가 끝날 때까지 기다리지 않고 sequential state value를 online으로 예측·갱신한다.",
            model="Markov reward process의 value V(s)를 현재 prediction과 다음 state prediction 사이의 TD error δₜ=rₜ₊₁+γV(sₜ₊₁)−V(sₜ)로 학습한다.",
            objective="방문한 state의 장기 discounted return 예측 오차를 줄이면서 bootstrapped target을 사용한다.",
            constraints="transition/reward stream과 discount factor가 있고, 충분한 visitation과 안정적인 step-size 조건이 필요하다.",
            success="one-step reward와 다음 예측만으로 eventual return을 점진적으로 맞추며 episode 종료 전에도 개선하는 것이다.",
            bottleneck="Monte Carlo return은 long episode와 delayed reward에서 늦고 variance가 크며, model-based DP는 transition model을 요구한다.",
            changes="실제 return 대신 다음 value estimate를 bootstrap하는 temporal-difference error를 prediction 학습의 기본 신호로 둔다.",
            assumptions=[
                ("state representation이 Markov에 가깝다", "다음 prediction으로 value를 bootstrap하기 위해 필요", "partial observation/state aliasing은 bias를 만든다"),
                ("방문 state와 step-size가 충분", "online convergence를 위해 필요", "sparse visitation·nonstationary dynamics에서는 미학습 영역이 남음"),
            ],
            loop="observation/state → value prediction → reward/next-state feedback의 policy evaluation foundation이다.",
            anchor="본문의 TD prediction problem, TD error update와 Markov reward-process examples.",
            domain="rl",
            body_basis="ABSTRACT_AND_CLASSIC_FORMULATION",
        ),
        profile(
            "Q-Learning",
            problem="transition model 없이 trial-and-error experience만으로 각 state-action의 long-term value와 optimal policy를 학습한다.",
            model="Q(s,a)를 두고 Q(sₜ,aₜ)←Q(sₜ,aₜ)+α[rₜ₊₁+γ max_a Q(sₜ₊₁,a)−Q(sₜ,aₜ)]로 asynchronous Bellman optimality update를 수행한다.",
            objective="각 state에서 최대 discounted return을 주는 action-value Q*(s,a)를 추정한다.",
            constraints="environment가 Markov이고 discrete table 또는 충분히 안정적인 representation을 가지며, all state-action pairs가 반복 sampling되어야 한다.",
            success="behavior policy와 independent하게 greedy action value가 Q*로 수렴하고 optimal policy를 산출하는 것이다.",
            bottleneck="model-based dynamic programming은 transition model을 필요로 하고, policy evaluation만으로는 탐험 결과를 optimal action으로 직접 전파하지 못한다.",
            changes="observed transition만으로 off-policy Bellman optimality backup을 수행해 model-free control을 가능하게 한다.",
            assumptions=[
                ("반복적인 exploration과 finite/discrete representation", "convergence theorem의 sampling 조건", "continuous high-dimensional robot action에서는 function approximation 불안정"),
                ("reward와 transition이 stationary Markov", "Q value의 고정점을 정의하기 위해 필요", "nonstationary contact/dynamics에서는 오래된 Q가 policy를 오도"),
            ],
            loop="state observation → Q-based action selection → reward/next state feedback의 model-free policy learning loop다.",
            anchor="본문의 controlled Markov domain, Q-learning update와 convergence theorem 부분.",
            domain="rl",
            body_basis="ABSTRACT_AND_CLASSIC_FORMULATION",
        ),
        profile(
            "Simple Statistical Gradient-Following Algorithms for Connectionist Reinforcement Learning",
            problem="differentiable environment model 없이 stochastic policy parameter를 expected return이 증가하는 방향으로 갱신한다.",
            model="policy π_θ(a|s)의 trajectory를 sample하고, log-probability gradient ∇θ log π_θ(aₜ|sₜ)에 return/reinforcement signal을 곱해 estimator를 만든다.",
            objective="J(θ)=E_{τ∼πθ}[R(τ)]를 maximize하는 policy parameter θ를 찾는다.",
            constraints="policy가 sample probability를 제공하고 return signal을 관측해야 하며, estimator variance를 줄일 baseline/normalization이 실용적으로 필요하다.",
            success="환경 dynamics를 미분하지 않고 unbiased-in-expectation policy gradient로 평균 성능을 개선하는 것이다.",
            bottleneck="value-function greedy policy는 stochastic optimal policy와 discontinuous action selection에 취약하고, model differentiation은 robot에 어렵다.",
            changes="reinforcement를 score-function likelihood-ratio gradient와 결합해 direct stochastic policy search를 제시한다.",
            assumptions=[
                ("trajectory return이 policy sample과 연결", "likelihood-ratio estimator를 만들기 위해 필요", "long-horizon sparse reward는 variance가 폭증"),
                ("policy distribution이 differentiable", "parameter gradient를 계산하기 위해 필요", "discrete/quantized action과 saturation에서는 gradient signal이 약함"),
            ],
            loop="trajectory observation/action → return signal → stochastic policy update의 policy-learning 단계다.",
            anchor="본문의 connectionist reinforcement learning formulation, REINFORCE-style statistical gradient estimator.",
            domain="rl",
            body_basis="ABSTRACT_AND_CLASSIC_FORMULATION",
        ),
        profile(
            "Policy Gradient Methods for Reinforcement Learning with Function Approximation",
            problem="대규모 continuous/state-action domain에서 value approximator의 greedy discontinuity를 피하면서 parameterized policy의 expected return을 최적화한다.",
            model="stochastic policy π_θ(a|s)와 value/action-value approximator를 두고 ∇θJ=E[∇θlogπ_θ(a|s) Q^{π}(s,a)] 형태의 policy gradient를 trajectory에서 추정한다.",
            objective="average 또는 discounted performance J(θ)를 local policy-parameter update로 maximize한다.",
            constraints="differentiable policy, compatible critic/advantage approximation과 ergodic/discounted MDP 조건이 필요하다.",
            success="function approximation을 사용해 locally optimal policy로 수렴하는 policy iteration/actor-critic update를 얻는 것이다.",
            bottleneck="value-function approximation 후 greedy action은 작은 value error가 action을 불연속적으로 바꾸며 stochastic policy를 자연스럽게 표현하지 못한다.",
            changes="policy를 명시적 differentiable function approximator로 두고 critic/advantage를 gradient estimator에 사용한다.",
            assumptions=[
                ("critic이 compatible하거나 advantage를 충분히 근사", "gradient bias를 통제하기 위해 필요", "critic misspecification은 잘못된 update 방향을 만든다"),
                ("policy class가 task-optimal behavior를 표현", "local optimum의 의미를 유지하기 위해 필요", "협소한 policy class는 exploration과 contact strategy를 제한"),
            ],
            loop="state/trajectory feedback → actor gradient와 critic → policy action distribution의 learning loop다.",
            anchor="본문의 policy-gradient theorem, function approximation과 actor-critic convergence discussion.",
            domain="rl",
            body_basis="FULL_TEXT_FORMULATION_REVIEWED",
        ),
        profile(
            "PILCO: A Model-Based and Data-Efficient Approach to Policy Search",
            problem="실제 system interaction을 최소화하면서 uncertain learned dynamics를 이용해 continuous-control policy를 학습한다.",
            model="transition f(x,u)를 Gaussian process로 모델링하고, moment matching으로 multi-step state distribution과 predictive uncertainty를 rollout한다.",
            objective="analytic policy gradient로 expected long-horizon cost E[Σc(xₜ)]를 최소화한다.",
            constraints="GP kernel/data가 dynamics를 설명하고 policy가 differentiable해야 하며, uncertainty propagation approximation이 horizon 동안 유효해야 한다.",
            success="적은 real interaction으로 policy를 개선하고 model uncertainty가 exploration과 policy gradient에 반영되는 것이다.",
            bottleneck="model-free policy search는 robot data를 많이 요구하고, deterministic learned model은 long-horizon error를 과신한다.",
            changes="GP predictive distribution을 policy rollout에 전파해 model learning과 policy search를 uncertainty-aware analytic optimization으로 결합한다.",
            assumptions=[
                ("저차원 transition function과 GP scaling", "full predictive distribution을 유지하기 위해 필요", "고차원 image/action과 긴 horizon에서 계산·approximation이 깨짐"),
                ("uncertainty model이 epistemic error를 반영", "risk-aware rollout을 위해 필요", "OOD contact state에서 GP variance가 실제 error와 불일치할 수 있음"),
            ],
            loop="state-transition data → probabilistic world model → policy rollout/gradient → real action feedback의 model-based RL loop다.",
            anchor="본문의 GP dynamics, uncertainty propagation, analytic policy gradient와 data-efficient policy-search setup.",
            domain="rl",
        ),
        profile(
            "A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning",
            problem="learner action이 다음 observation/state distribution을 바꾸는 sequential imitation에서 expert-state i.i.d. 학습의 covariate shift를 줄인다.",
            model="정책 π가 생성한 state distribution에서 expert action을 query해 dataset을 aggregate하고, 매 iteration loss-sensitive online learner를 학습한다.",
            objective="learner가 유발하는 state distribution에서 sequence loss와 expected mistakes를 최소화한다.",
            constraints="expert가 현재 learner state에서 label을 제공하고 no-regret online learner가 있으며 state/action rollout이 finite horizon이다.",
            success="expert-only demonstration에서 벗어나 learner가 실제로 방문하는 오류 상태에서도 누적 loss가 sublinear/no-regret bound를 갖는 것이다.",
            bottleneck="behavior cloning은 expert distribution의 작은 one-step error가 rollout에서 O(T²) 수준의 compounding error로 커질 수 있다.",
            changes="learner-induced state를 다시 수집하는 dataset aggregation과 no-regret reduction으로 stationary deterministic policy를 학습한다.",
            assumptions=[
                ("학습 중 expert correction/query 가능", "learner state의 action label을 수집하기 위해 필요", "offline-only setting에서는 DAgger loop를 수행할 수 없음"),
                ("online supervised loss가 sequence loss와 연결", "regret bound를 policy performance로 변환하기 위해 필요", "long-horizon contact failure가 단순 action loss와 불일치"),
            ],
            loop="observation/state rollout → learner action → expert relabeling → policy update의 imitation feedback loop다.",
            anchor="본문의 i.i.d. violation, learner-induced distribution, no-regret reduction과 dataset aggregation algorithm.",
            domain="il",
        ),
        profile(
            "Learning Neural Network Policies with Guided Policy Search under Unknown Dynamics",
            problem="raw images에서 robot motor torques까지 perception과 control을 함께 학습하되 high-dimensional neural policy의 exploration을 tractable하게 한다.",
            model="trajectory-centric local controllers가 state/action trajectory distribution을 만들고, supervised neural policy π_θ(o)와 KL/consistency constraint로 이를 distill한다.",
            objective="task cost를 낮추는 local trajectory policy와 image-to-torque neural policy의 action/state distribution mismatch를 번갈아 줄인다.",
            constraints="local controller가 trajectory를 안정적으로 탐색하고 policy가 image observation에서 torque를 표현하며, alternating optimization의 local regions가 겹쳐야 한다.",
            success="hand-engineered perception/state-estimation 대신 raw image-to-torque policy가 real manipulation에서 실행되는 것이다.",
            bottleneck="direct policy search는 neural parameter 공간이 크고 real robot exploration이 위험하며, modular pipeline은 perception/control co-design을 제한한다.",
            changes="trajectory-centric RL을 supervised policy learning의 teacher로 사용해 unknown dynamics에서도 deep visuomotor policy를 훈련한다.",
            assumptions=[
                ("local trajectory controller와 state estimate 사용 가능", "teacher rollout을 만들기 위해 필요", "contact mode나 image ambiguity가 크면 local teacher가 일반화하지 않음"),
                ("camera observation이 torque policy에 충분", "end-to-end interface를 위해 필요", "occlusion·latency·unseen object에서 state aliasing"),
            ],
            loop="image observation → neural torque policy → robot transition → trajectory-centric correction의 end-to-end control loop다.",
            anchor="JMLR 본문의 problem statement, trajectory-centric guided policy search와 raw-image-to-torque setup.",
            domain="il",
        ),
        profile(
            "Generative Adversarial Imitation Learning",
            problem="expert demonstration만으로 policy를 학습할 때 behavioral cloning의 compounding error와 IRL의 expensive reward-recovery 단계를 줄인다.",
            model="policy가 생성한 state-action occupancy와 expert occupancy를 discriminator D가 구분하고, policy는 D가 expert로 판단하는 방향으로 RL update를 수행한다.",
            objective="expert와 learner의 occupancy measure divergence를 최소화하며 expert-like trajectory를 생성한다.",
            constraints="expert trajectory만 있고 environment interaction/RL rollout은 가능해야 하며 discriminator-policy game이 안정적으로 학습되어야 한다.",
            success="명시적 reward function을 복원하지 않고도 expert trajectory distribution에 가까운 policy를 얻는 것이다.",
            bottleneck="BC는 one-step state-action mismatch를 누적하고, IRL은 cost inference 후 별도 RL을 돌려 계산량과 ambiguity가 크다.",
            changes="IRL의 occupancy matching 목표를 adversarial discriminator와 direct policy optimization으로 합성한다.",
            assumptions=[
                ("expert occupancy가 task behavior를 대표", "matching target을 정의하기 위해 필요", "좁은 demonstrations는 unseen recovery를 가르치지 않음"),
                ("environment rollout과 on-policy RL 가능", "learner occupancy를 관측하기 위해 필요", "offline-only robot data에서는 직접 적용 불가"),
            ],
            loop="state/action rollout → discriminator reward → policy update → next rollout의 imitation-RL loop다.",
            anchor="본문의 imitation setting, occupancy measure matching과 adversarial formulation.",
            domain="il",
        ),
        profile(
            "Trust Region Policy Optimization",
            problem="large nonlinear policy의 expected return을 개선하면서 한 번의 policy update가 performance를 급락시키지 않게 한다.",
            model="old policy π_old의 samples로 surrogate L(θ)=E[r_θ A_old]를 만들고 average KL(π_old||π_θ)≤δ trust-region constraint 아래 최적화한다.",
            objective="surrogate expected advantage를 최대화해 true policy performance lower bound를 개선한다.",
            constraints="정책 ratio/advantage estimator와 KL approximation이 유효하고, update가 local trust region 안에 있어야 한다.",
            success="continuous-control locomotion 등에서 hyperparameter tuning을 과도하게 늘리지 않고 monotonic improvement 경향을 얻는 것이다.",
            bottleneck="vanilla policy gradient는 step size에 민감하고 큰 neural policy update가 state distribution과 return을 불안정하게 바꾼다.",
            changes="policy improvement bound를 KL-constrained surrogate optimization으로 근사하고 natural-gradient/conjugate-gradient update로 푼다.",
            assumptions=[
                ("advantage와 old-policy distribution이 적절히 추정", "surrogate가 true improvement를 대표하기 위해 필요", "critic bias와 sparse contact reward는 direction을 왜곡"),
                ("KL constraint가 policy change를 대표", "monotonic bound를 유지하기 위해 필요", "partial observation/history policy에서는 chosen KL이 충분하지 않을 수 있음"),
            ],
            loop="rollout observation → advantage estimate → constrained policy update → next rollout의 on-policy RL loop다.",
            anchor="본문의 policy improvement bound, KL-constrained surrogate와 TRPO algorithm.",
            domain="rl",
        ),
        profile(
            "Proximal Policy Optimization Algorithms",
            problem="TRPO 수준의 안정적 policy update를 1차 gradient와 minibatch multiple epochs로 단순하고 data-efficient하게 구현한다.",
            model="importance ratio rₜ(θ)=πθ(aₜ|sₜ)/πold(aₜ|sₜ)를 clipped surrogate min(rA,clip(r,1−ε,1+ε)A)로 제한한다.",
            objective="on-policy samples의 clipped expected advantage와 value/entropy objective를 최적화한다.",
            constraints="data가 old policy에서 수집되고 clipping range가 policy ratio의 유효 trust region 역할을 하며 rollout distribution이 너무 변하지 않아야 한다.",
            success="여러 minibatch epoch를 허용하면서도 locomotion/Atari에서 sample efficiency와 wall-time 성능을 유지하는 것이다.",
            bottleneck="vanilla PG는 sample마다 한 update만 가능하고, TRPO는 second-order/constrained solver와 architecture 제약이 복잡하다.",
            changes="explicit KL-constrained solver 대신 ratio clipping으로 지나친 policy change의 objective incentive를 잘라낸다.",
            assumptions=[
                ("old-policy data와 importance ratio가 계산 가능", "off-policy correction을 위해 필요", "stale data나 large policy drift에서 clipping이 bias를 숨김"),
                ("ε와 minibatch epochs가 적절", "stability/sample efficiency 절충을 위해 필요", "contact-rich sparse reward에서는 under/over-update가 모두 가능"),
            ],
            loop="on-policy rollout → clipped surrogate update → new policy rollout의 iterative policy optimization loop다.",
            anchor="본문의 clipped surrogate objective, multiple epochs와 benchmark control experiments.",
            domain="rl",
        ),
        profile(
            "Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor",
            problem="continuous control에서 on-policy deep RL의 높은 sample cost와 brittle exploration을 줄이면서 안정적인 stochastic policy를 학습한다.",
            model="soft Q(s,a)를 Bellman backup으로 학습하고, actor πφ가 Q와 entropy αH(π) 합을 최대화하도록 off-policy replay에서 update한다.",
            objective="E[Σγᵗ(rₜ+αH(π(·|sₜ)))]를 maximize해 reward와 state-wise action entropy를 함께 최적화한다.",
            constraints="replay transitions, stochastic reparameterizable policy와 temperature/entropy target이 있으며 Markov dynamics와 bounded action이 가정된다.",
            success="과거 replay data를 재사용하면서 diverse exploration과 robust continuous-control performance를 얻는 것이다.",
            bottleneck="on-policy PG는 매 update마다 새 samples가 필요하고 deterministic/low-entropy policy는 exploration과 local failure에 취약하다.",
            changes="off-policy actor-critic과 maximum-entropy objective, twin/soft value backup을 하나의 stochastic control algorithm으로 결합한다.",
            assumptions=[
                ("replay distribution이 current policy에 충분히 관련", "off-policy Q backup을 위해 필요", "severe distribution shift와 extrapolation error가 critic을 망가뜨림"),
                ("entropy coefficient가 task scale에 맞음", "exploration과 exploitation을 조절하기 위해 필요", "contact precision task에서 과도한 stochasticity가 실패를 만듦"),
            ],
            loop="replay state/action/reward → soft critic/actor update → stochastic action → environment feedback loop다.",
            anchor="본문의 maximum-entropy objective, soft policy iteration과 off-policy actor-critic algorithm.",
            domain="rl",
        ),
        profile(
            "Domain Randomization for Transferring Deep Neural Networks from Simulation to the Real World",
            problem="simulator에서 학습한 visual policy가 real camera/lighting/object/dynamics의 reality gap을 넘어가도록 한다.",
            model="simulation domain parameter ξ를 distribution p(ξ)에서 randomize하고 policy πθ(o_ξ) 또는 perception model을 mixture of simulated domains에서 학습한다.",
            objective="randomized training distribution 전반의 expected task loss를 최소화해 target real domain에서도 robust하게 한다.",
            constraints="real domain이 randomization support 안에 있거나 close해야 하며 simulator가 task-relevant visual/physical variation을 생성해야 한다.",
            success="real image/robot에서 별도 real labels·fine-tuning 없이 sim-trained model이 target task를 수행하는 것이다.",
            bottleneck="single simulated appearance/dynamics에 overfit한 network는 real sensor statistics와 friction/actuator mismatch에서 실패한다.",
            changes="simulator parameter를 넓게 randomize해 real domain을 하나의 unknown sample로 취급하는 robustness training을 제안한다.",
            assumptions=[
                ("real variation이 chosen randomization family에 포함", "domain generalization을 위해 필요", "unmodeled camera/dynamics/contact는 여전히 OOD"),
                ("randomization이 task semantics를 파괴하지 않음", "학습 가능한 signal을 유지하기 위해 필요", "너무 넓은 distribution은 sample inefficiency를 낳음"),
            ],
            loop="sim observation variation → policy training → real observation → action execution의 sim-to-real perception/control bridge다.",
            anchor="본문의 reality-gap motivation, randomized rendering parameters와 real-world transfer experiment.",
            domain="sim2real",
        ),
        profile(
            "What Matters in Learning from Offline Human Demonstrations for Robot Manipulation",
            problem="offline human demonstration의 algorithm·history·data quality·checkpoint choice 중 무엇이 manipulation performance를 좌우하는지 공통 조건에서 분리한다.",
            model="demonstration dataset D={(o_t,s_t,a_t)}와 history/context를 사용해 behavior policy 또는 offline RL policy를 학습한다.",
            objective="deployment state distribution에서 action prediction/long-horizon rollout success를 높이는 representation과 data/algorithm configuration을 선택한다.",
            constraints="online corrective labels가 없고 train demonstrations가 deployment states를 충분히 cover해야 하며 비교 실험의 task/data split이 고정되어야 한다.",
            success="algorithm 이름보다 demonstration proficiency, dataset quality, history와 model selection이 성능 차이를 설명하는지 재현 가능하게 밝히는 것이다.",
            bottleneck="offline robot learning 결과는 dataset quality와 evaluation protocol이 섞여 있어 방법 간 headline 비교가 어렵다.",
            changes="공통 benchmark/codebase에서 imitation/offline RL, data quality와 history/selection 변수를 factorial하게 비교한다.",
            assumptions=[
                ("offline data가 test state를 덮음", "behavior cloning/offline policy가 실패하지 않게 하기 위해 필요", "covariate shift와 unseen recovery는 미해결"),
                ("validation metric이 rollout success와 연결", "checkpoint selection을 정당화하기 위해 필요", "offline loss가 contact failure를 반영하지 않을 수 있음"),
            ],
            loop="logged observation/history → offline policy learning → closed-loop rollout evaluation의 data-centric robot learning loop다.",
            anchor="본문의 controlled comparison, demonstration quality/history/model-selection study와 manipulation task setup.",
            domain="il",
        ),
        profile(
            "Implicit Behavioral Cloning",
            problem="동일 observation에서 여러 plausible action이 있는 multimodal demonstration을 평균내지 않고 높은 차원의 continuous action을 표현한다.",
            model="energy/action-likelihood function Eθ(a|o)를 implicit neural representation으로 학습하고, 주어진 observation에서 low-energy action을 optimization 또는 sampling으로 찾는다.",
            objective="expert state-action pairs의 energy를 낮추고 non-expert/negative action보다 expert manifold를 선호하게 한다.",
            constraints="action energy landscape에서 inference optimization이 충분히 빠르고, demonstrations가 relevant multimodality를 포함해야 한다.",
            success="conditional action distribution의 여러 mode를 보존해 ambiguous manipulation state에서 일관된 action을 생성하는 것이다.",
            bottleneck="deterministic BC는 mode averaging으로 invalid intermediate action을 만들고 mixture/categorical output은 high-dimensional continuous trajectory에서 복잡하다.",
            changes="explicit normalized density 대신 unnormalized implicit energy를 학습해 multimodal action selection을 단순화한다.",
            assumptions=[
                ("energy inference가 control frequency에 맞음", "implicit model을 실제 policy로 사용하기 위해 필요", "iterative optimization latency가 closed loop를 제한"),
                ("training negatives/energy shape가 mode를 분리", "mode collapse를 피하기 위해 필요", "sparse demos와 out-of-distribution action에서 arbitrary minima"),
            ],
            loop="observation/history → implicit action energy → action inference → robot feedback의 visuomotor policy layer다.",
            anchor="본문의 multimodal action motivation, implicit energy-based BC objective와 inference procedure.",
            domain="il",
        ),
        profile(
            "Offline Reinforcement Learning with Implicit Q-Learning",
            problem="fixed dataset 밖의 action value를 과대추정하지 않고 behavior policy를 벗어나지 않으면서 offline optimal policy를 학습한다.",
            model="dataset transition으로 state value를 expectile regression으로 추정하고 Q(s,a)=r+γV(s')를 계산한 뒤 advantage-weighted behavior cloning으로 policy를 갱신한다.",
            objective="dataset support 안에서 high-advantage action을 선택하도록 expected return을 높인다.",
            constraints="offline dataset이 유용한 high-return trajectories를 포함하고, expectile τ와 advantage weight가 distribution shift를 통제해야 한다.",
            success="online interaction 없이 conservative Q backup의 max extrapolation을 피하면서 dataset-best policy를 복원하는 것이다.",
            bottleneck="offline Q-learning의 Bellman max는 dataset에 없는 action을 평가해 extrapolation error와 catastrophic policy를 만든다.",
            changes="explicit policy constraint 없이 value를 implicit policy distribution의 expectile로 학습하고 advantage-weighted regression을 사용한다.",
            assumptions=[
                ("dataset coverage가 좋은 action을 포함", "offline improvement의 ceiling을 정하기 위해 필요", "narrow/low-quality data에서는 IQL도 unseen recovery를 만들 수 없음"),
                ("expectile와 weight scale이 적절", "conservatism과 improvement를 조절하기 위해 필요", "task reward scale/contact outlier에 민감"),
            ],
            loop="offline state/action/reward log → value/Q estimation → weighted policy → deployment feedback의 offline RL loop다.",
            anchor="본문의 in-sample policy improvement, expectile value regression과 advantage-weighted behavioral cloning.",
            domain="offline_rl",
        ),
        profile(
            "Decision Transformer: Reinforcement Learning via Sequence Modeling",
            problem="value backup과 bootstrapping 없이 offline trajectories에서 desired return-conditioned behavior를 sequence model로 생성한다.",
            model="trajectory token sequence (return-to-go, state, action)를 causal Transformer에 넣어 context-conditioned next action distribution을 예측한다.",
            objective="offline dataset의 action sequence likelihood를 maximize하고 target return/goal context에 맞는 trajectory를 autoregressively generate한다.",
            constraints="long context가 relevant history와 return signal을 포함하고 train dataset이 target behavior를 support해야 한다.",
            success="offline RL objective를 sequence modeling으로 바꾸어 stochastic/multimodal long-horizon action pattern을 조건부로 재생하는 것이다.",
            bottleneck="offline Q/value learning은 distribution shift와 unstable bootstrapping에 취약하고, long-horizon dependencies를 one-step policy로 잃는다.",
            changes="MDP optimization을 return-conditioned autoregressive sequence prediction으로 reformulate한다.",
            assumptions=[
                ("desired return이 achievable trajectory와 연결", "conditioning variable의 의미를 위해 필요", "out-of-range return은 unsupported behavior를 유발"),
                ("context window가 task-relevant history를 유지", "partial observability와 temporal credit을 위해 필요", "long horizon/occlusion은 finite context 밖으로 밀림"),
            ],
            loop="history·return-to-go → sequence action prediction → environment transition → updated return context의 policy loop다.",
            anchor="본문의 trajectory tokenization, return conditioning과 offline sequence-modeling formulation.",
            domain="offline_rl",
        ),
        profile(
            "Denoising Diffusion Probabilistic Models",
            problem="복잡한 high-dimensional data distribution을 tractable likelihood/denoising objective로 학습해 sample을 생성한다.",
            model="forward process가 x₀에 Gaussian noise를 단계적으로 더해 x_T≈N(0,I)를 만들고, reverse Markov chain pθ(x_{t−1}|x_t)가 noise를 제거한다.",
            objective="noise prediction 또는 variational bound를 최소화해 data distribution p_data(x₀)의 reverse denoising transition을 학습한다.",
            constraints="fixed noise schedule, sufficiently many denoising steps와 reverse network capacity가 필요하다.",
            success="Gaussian prior에서 시작해 data manifold sample을 안정적으로 생성하고 multimodal distribution을 mode averaging 없이 표현하는 것이다.",
            bottleneck="single-step Gaussian regression은 multimodal target을 평균내며, autoregressive/likelihood model은 high-dimensional sampling과 optimization이 어렵다.",
            changes="simple forward noising과 learned reverse denoising을 결합해 complex distribution을 sequence of local conditional denoisers로 학습한다.",
            assumptions=[
                ("noise schedule과 score/denoiser가 data structure를 보존", "reverse recovery를 위해 필요", "few steps·OOD conditioning에서는 sample quality가 저하"),
                ("sampling latency가 허용", "iterative reverse chain을 실제 시스템에 사용하기 위해 필요", "robot control에서는 feedback rate와 충돌"),
            ],
            loop="condition/observation → iterative action/sample denoising → generated output의 generative policy foundation이다.",
            anchor="본문의 forward diffusion, reverse Markov chain, variational/noise-prediction objective.",
            domain="generative",
        ),
        profile(
            "Flow Matching for Generative Modeling",
            problem="continuous normalizing flow를 simulation-free vector-field regression으로 학습해 generative sampling을 단순화한다.",
            model="conditional probability path p_t(x|x₁,x₀)의 target velocity u_t(x|x₁,x₀)를 neural vector field vθ(t,x)에 회귀한다.",
            objective="E_{t,x₀,x₁}[||vθ(t,x_t)−u_t(x_t|x₀,x₁)||²]를 최소화해 base에서 data로 가는 probability flow를 복원한다.",
            constraints="선택한 conditional path와 coupling이 tractable하고 ODE solver가 learned vector field를 적분할 수 있어야 한다.",
            success="diffusion-like 또는 optimal-transport path에서 likelihood simulation 없이 sample을 생성하며 step/quality tradeoff를 조절하는 것이다.",
            bottleneck="diffusion training은 noisy Markov chain과 많은 sampling step을 요구하고, CNF likelihood training은 expensive ODE simulation을 포함한다.",
            changes="path의 conditional velocity를 직접 회귀해 CNF/ diffusion family를 하나의 flow training objective로 통합한다.",
            assumptions=[
                ("conditional probability path가 target distribution을 연결", "vector-field target을 정의하기 위해 필요", "poor path/coupling은 stiff ODE와 sample error를 만듦"),
                ("ODE integration cost가 허용", "sample을 생성하기 위해 필요", "robot action chunk latency가 control frequency를 제한"),
            ],
            loop="conditioning observation → flow vector-field integration → action/sample trajectory의 generative-action foundation이다.",
            anchor="본문의 conditional probability paths, vector-field regression objective와 ODE sampling section.",
            domain="generative",
            body_basis="ABSTRACT_AND_PROCEEDINGS_FORMULATION",
        ),
        profile(
            "Diffusion Policy: Visuomotor Policy Learning via Action Diffusion",
            problem="robot action trajectory의 multimodality·temporal correlation·high-dimensional precision을 유지하는 visuomotor policy를 학습한다.",
            model="observation history o_{t−H:t}를 condition으로 action chunk A_{t:t+H}에 Gaussian noise를 넣고 conditional denoising network가 reverse action distribution을 생성한다.",
            objective="expert action sequence의 diffusion denoising loss를 최소화해 p(A_chunk|O_history)를 모델링한다.",
            constraints="action chunk가 controller가 실행할 수 있는 horizon이어야 하고 denoising inference가 receding-horizon feedback rate에 맞아야 한다.",
            success="single-step regression보다 multimodal trajectory와 sequential correlation을 보존하며 manipulation success를 높이는 것이다.",
            bottleneck="Gaussian mixture/categorical action representation은 multimodal high-dimensional trajectory와 temporal correlation을 비효율적으로 표현한다.",
            changes="policy output을 one-step action이 아닌 conditional diffusion action sequence로 두고 receding-horizon action chunk를 실행한다.",
            assumptions=[
                ("demonstrations가 relevant action modes를 포함", "conditional distribution을 학습하기 위해 필요", "unseen recovery mode는 생성되지 않음"),
                ("observation history와 action chunk length가 충분", "temporal precision을 위해 필요", "latency/occlusion과 long chunk는 stale action을 만듦"),
            ],
            loop="visual/proprioceptive observation history → action diffusion chunk → partial execution → next observation feedback다.",
            anchor="본문의 action-distribution motivation, conditional denoising policy와 receding-horizon execution.",
            domain="il",
        ),
        profile(
            "Q-Transformer: Scalable Offline Reinforcement Learning via Autoregressive Q-Functions",
            problem="large heterogeneous robot datasets에서 high-dimensional continuous actions의 offline Q-learning을 scalable autoregressive model로 수행한다.",
            model="continuous action을 discretized tokens로 factorize하고 Transformer Q-function이 state와 previous action tokens를 조건으로 token-level action value를 예측한다.",
            objective="dataset transition에서 conservative/temporal-difference Q objective를 학습하고 autoregressive greedy action을 선택한다.",
            constraints="action discretization이 control precision을 보존하고 dataset support가 token combinations를 충분히 포함해야 한다.",
            success="multi-dimensional robot action과 long-horizon offline data를 sequence model로 다루면서 Q-guided policy improvement를 얻는 것이다.",
            bottleneck="standard offline RL은 continuous high-dimensional action max와 cross-embodiment data scaling이 어렵다.",
            changes="Q-function을 action token sequence에 대한 autoregressive factorization으로 바꾸어 tractable한 discrete conditional maximization을 사용한다.",
            assumptions=[
                ("token bins가 meaningful action precision을 유지", "continuous control을 discretize하기 위해 필요", "fine contact adjustment가 quantization error에 손상"),
                ("offline data coverage와 conservative Q가 충분", "OOD action overestimation을 막기 위해 필요", "rare but successful recovery는 여전히 미학습"),
            ],
            loop="offline robot transition → autoregressive Q/value update → tokenized action → deployment feedback의 offline policy layer다.",
            anchor="본문의 action-token factorization, autoregressive Q objective와 heterogeneous robot-data setup.",
            domain="offline_rl",
        ),
    ]
)


DOMAIN_SCOPE: dict[str, tuple[str, str, str, str, str]] = {
    "estimation": (
        "부분 관측·noise가 있는 동적 시스템",
        "시간별 sensor observation과 알려진 model/control input",
        "latent state와 uncertainty/belief",
        "causal estimate, prediction 또는 smoothing output",
        "estimation error, covariance 또는 downstream state quality",
    ),
    "planning": (
        "graph, configuration space 또는 task-and-motion planning domain",
        "start/goal, map, dynamics와 successor/operator description",
        "path, trajectory, symbolic state 또는 task-motion decision",
        "feasible action sequence 또는 minimum-cost plan",
        "path cost, goal reachability, feasibility와 computation",
    ),
    "control": (
        "robot mechanism의 state와 task-space dynamics",
        "joint/task state, reference와 sensor feedback",
        "state estimate, task-space error와 control decision",
        "torque, force, velocity 또는 position command",
        "tracking, stability, constraint satisfaction과 contact behavior",
    ),
    "rl": (
        "robot/environment의 sequential decision process",
        "state 또는 observation, action, reward와 transition history",
        "policy/value state와 action-selection variable",
        "action policy와 induced trajectory",
        "expected return, task success, stability와 sample efficiency",
    ),
    "il": (
        "demonstration으로 정의된 robot task distribution",
        "observation history와 expert trajectory/action",
        "behavior policy와 temporal action context",
        "predicted action 또는 action chunk",
        "imitation error, task success, robustness와 compounding error",
    ),
    "offline_rl": (
        "offline robot transition/trajectory dataset과 deployment MDP",
        "dataset state/observation, action, reward와 return-to-go",
        "Q/value 또는 sequence-policy state",
        "dataset-supported action sequence",
        "offline policy value, OOD safety와 closed-loop success",
    ),
    "generative": (
        "high-dimensional data 또는 robot action-trajectory distribution",
        "conditioning observation와 noisy/intermediate sample",
        "latent/noise variable와 conditional distribution",
        "generated sample, action chunk 또는 trajectory",
        "distribution fit, multimodality, sample quality와 latency",
    ),
    "sim2real": (
        "simulated robot dynamics와 mismatched real hardware",
        "sim state/privileged observation 및 real-observable sensor",
        "transfer policy와 hidden dynamics/domain variable",
        "real-robot control action",
        "real task success, stability, transfer gap과 robustness",
    ),
    "simulation": (
        "physics simulation의 robot/environment model",
        "simulated state, geometry, contact와 control input",
        "dynamics/contact state 또는 learned simulator representation",
        "simulation step, trajectory 또는 environment query",
        "physical plausibility, speed, reproducibility와 task utility",
    ),
    "safety": (
        "uncertain robot state와 safe/unsafe operating region",
        "observation, uncertainty/risk estimate와 task command",
        "safe set, recovery state 또는 constraint margin",
        "shielded, recovery 또는 safe action",
        "task return과 violation/failure probability",
    ),
    "world_model": (
        "partially observed robot environment와 its future dynamics",
        "observation/action history와 latent scene state",
        "latent state, dynamics model 또는 imagined rollout",
        "predicted future observation/reward 또는 model-based action",
        "prediction quality, planning return, horizon과 uncertainty",
    ),
    "vla": (
        "language-conditioned robot task와 embodiment",
        "image/video, language instruction, proprioception과 history",
        "language-grounded task state와 action-policy context",
        "continuous action, pose 또는 action chunk",
        "instruction following, task success, generalization과 latency",
    ),
    "vision": (
        "visual scene과 downstream embodied task",
        "image/video와 natural-language or task annotation",
        "visual representation/semantic state",
        "class, embedding, grounding 또는 task cue",
        "recognition/grounding quality와 downstream robot utility",
    ),
    "3d_perception": (
        "3D scene/object와 robot coordinate frame",
        "RGB-D, image set, point cloud, depth와 camera pose",
        "geometry, map, object/relationship state",
        "point map, pose, scene graph, affordance 또는 query result",
        "geometric accuracy, semantic consistency와 planning/manipulation utility",
    ),
    "navigation": (
        "mapped 3D environment과 mobile robot",
        "camera/depth stream, pose, map와 language goal",
        "robot pose, free-space/semantic map와 local goal",
        "collision-free trajectory 또는 velocity command",
        "goal reach, safety, localization error와 replanning latency",
    ),
    "manipulation": (
        "rigid/articulated object와 robot manipulator contact scene",
        "RGB-D/point cloud, object state와 contact/task observation",
        "object geometry, affordance, contact mode 또는 end-effector state",
        "grasp, pose, force 또는 end-effector trajectory",
        "task completion, contact success, pose/force error와 generalization",
    ),
    "tactile": (
        "contact-rich manipulation scene",
        "tactile image/force, vision과 proprioceptive history",
        "contact geometry, force state 또는 latent dynamics",
        "grasp/contact action, force command 또는 object motion",
        "slip/contact success, force/pose error와 robustness",
    ),
    "locomotion": (
        "legged robot, terrain과 contact dynamics",
        "proprioception, terrain/perception observation과 velocity command",
        "body/contact state, foothold 또는 behavior mode",
        "joint target, torque, footstep 또는 locomotion action",
        "velocity/progress, stability, energy와 terrain generalization",
    ),
    "humanoid": (
        "high-DoF humanoid whole-body dynamics와 contacts",
        "proprioception, reference pose/motion, visual or language command",
        "whole-body pose, balance/contact state와 skill/mode",
        "joint/whole-body action, motion target 또는 task trajectory",
        "tracking, balance, skill/task success와 recovery",
    ),
    "mobile_manipulation": (
        "mobile base와 one/two-arm manipulation environment",
        "egocentric RGB-D, language/task goal, base-arm proprioception",
        "map/object/contact state와 base-arm coordination decision",
        "base motion plus arm/gripper action",
        "long-horizon task success, reachability, collision과 recovery",
    ),
    "robot_data": (
        "multi-robot demonstration/dataset ecosystem",
        "multi-view observation, language/task label과 action trajectory",
        "shared representation, embodiment/task identity와 data distribution",
        "dataset sample 또는 learned policy action",
        "coverage, cross-embodiment transfer, data efficiency와 task success",
    ),
    "benchmark": (
        "defined robot simulator/hardware task suite",
        "standardized observation, action, task state와 evaluation split",
        "benchmark state/goal와 method decision",
        "policy/controller trajectory 또는 measured result",
        "success metric, robustness, generalization과 reproducibility",
    ),
    "general": (
        "논문이 정의한 robot/embodied environment",
        "논문이 명시한 observation과 task input",
        "task state 또는 decision variable",
        "paper-specific output/action",
        "primary task objective와 closed-loop behavior",
    ),
}


def parse_sections(markdown: str) -> dict[str, str]:
    """Collect level-two sections from a legacy note without its metadata."""

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


def first_section(sections: dict[str, str], *names: str) -> str:
    for name in names:
        value = sections.get(name, "").strip()
        if value:
            return value
    return ""


def extract_evidence(markdown: str) -> str:
    match = re.search(
        r"(?im)^\s*(?:>\s*)?(?:[-*]\s*)?Evidence maturity\s*:\s*(?:`([^`]+)`|([^\.\n]+))",
        markdown,
    )
    if not match:
        return ""
    value = (match.group(1) or match.group(2) or "").strip()
    return value if value in VALID_EVIDENCE else ""


def read_tracker() -> dict[str, dict[str, str]]:
    if not STATUS.exists():
        return {}
    tracker: dict[str, dict[str, str]] = {}
    with STATUS.open(encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            overview = row.get("overview_path", "").removeprefix("./")
            if not overview:
                continue
            folder = overview.removesuffix("/01_overview.md")
            tracker[folder] = row
            tracker[folder.casefold()] = row
    return tracker


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


def strip_list_marker(value: str) -> str:
    return re.sub(r"^\s*(?:[-*+]\s+|\d+[.)]\s+)", "", value.strip()).strip()


def useful_lines(block: str, limit: int = 4) -> list[str]:
    result: list[str] = []
    ignored = (
        "자동 추출 실패",
        "자동 추출 없음",
        "본문 확인 필요",
        "본문 수동 확인 필요",
        "unverified",
        "위 method/evaluation",
        "본문 기반 자동 추출에서는",
    )
    for raw in block.splitlines():
        value = strip_list_marker(raw)
        if not value or value.casefold().startswith(tuple(x.casefold() for x in ignored)):
            continue
        if value not in result:
            result.append(value)
        if len(result) >= limit:
            break
    return result


def compact_cue(block: str, fallback: str, limit: int = 3) -> str:
    values = useful_lines(block, limit)
    if not values:
        return fallback
    text = " ".join(values).strip()
    return text if text.endswith((".", "다.", "다?", "다!", "?", "!")) else text + "."


def evidence_for(item: dict[str, Any], old: str, overview: str, tracker: dict[str, dict[str, str]]) -> str:
    # The tracker is the canonical source for the 190 intensive-reading rows.
    row = tracker.get(str(item["folder"])) or tracker.get(str(item["folder"]).casefold())
    if row and row.get("evidence_level") in VALID_EVIDENCE:
        return row["evidence_level"]
    overview_evidence = extract_evidence(overview)
    if overview_evidence:
        return overview_evidence
    legacy_evidence = extract_evidence(old)
    if legacy_evidence:
        return legacy_evidence
    return "CURATION_ONLY"


def basis_text(profile_data: dict[str, Any] | None) -> str:
    if profile_data is None:
        return "registry/abstract cue 기반 scaffold; exact formulation은 본문 수동 확인 필요. tracker의 reading status/evidence는 변경하지 않았다."
    basis = profile_data.get("body_basis", "BODY_FORMULATION_REVIEWED")
    messages = {
        "FULL_TEXT_FORMULATION_REVIEWED": "source PDF의 abstract·introduction·problem/formulation 단락을 검토해 이 문제 formulation을 작성했다.",
        "BODY_FORMULATION_REVIEWED": "source PDF 또는 공식 full-text source의 problem/formulation 관련 본문 단서를 검토해 이 문제 formulation을 작성했다.",
        "BODY_FORMULATION_REVIEWED_CORRECTED_SOURCE": "원래 PDF URL의 내용이 논문과 불일치해 검증된 저자/공식 source의 본문을 다시 확인한 뒤 이 문제 formulation을 작성했다.",
        "ABSTRACT_AND_PROCEEDINGS_FORMULATION": "공식 abstract/proceedings와 available paper cue를 바탕으로 formulation을 작성했다; exact equation/page는 본문 확인이 필요하다.",
        "ABSTRACT_AND_CLASSIC_FORMULATION": "공식 abstract와 canonical problem formulation을 바탕으로 구조화했다; source-specific equation/page는 본문 확인이 필요하다.",
        "ABSTRACT_OR_PROJECT_PAGE_FORMULATION": "공식 abstract/project page 수준의 source를 바탕으로 구조화했다; method-specific formulation은 본문 확인이 필요하다.",
        "ABSTRACT_OR_PROGRAM_PAGE_FORMULATION": "공식 abstract/program page 수준의 source를 바탕으로 구조화했다; method-specific formulation은 본문 확인이 필요하다.",
        "ABSTRACT_AND_REVIEW_FORMULATION": "공식 abstract와 review-level source를 바탕으로 구조화했다; method-specific formulation은 본문 확인이 필요하다.",
    }
    message = messages.get(basis, messages["BODY_FORMULATION_REVIEWED"])
    return f"{message} tracker의 reading status/evidence는 이 migration에서 변경하지 않았다."


def scope_lines(profile_data: dict[str, Any]) -> list[str]:
    domain = profile_data.get("domain", "general")
    values = DOMAIN_SCOPE.get(domain, DOMAIN_SCOPE["general"])
    return [
        f"- **Object / environment:** {values[0]}",
        f"- **Observation / input:** {values[1]}",
        f"- **Latent state / decision variable:** {values[2]}",
        f"- **Output / action:** {values[3]}",
        f"- **Horizon / evaluation target:** {values[4]}",
    ]


def render_assumptions(assumptions: list[tuple[str, str, str]]) -> str:
    rows = ["| Assumption | Why it is needed | Failure boundary |", "|---|---|---|"]
    for assumption, reason, failure in assumptions:
        values = [assumption, reason, failure]
        values = [value.replace("|", "\\|").replace("\n", " ").strip() for value in values]
        rows.append("| " + " | ".join(values) + " |")
    return "\n".join(rows)


def legacy_scaffold(old: str, overview: str, item: dict[str, Any]) -> dict[str, str]:
    old_sections = parse_sections(old)
    overview_sections = parse_sections(overview)
    problem = compact_cue(
        first_section(old_sections, "Target Problem and Assumptions", "Problem in One Sentence", "Problem"),
        compact_cue(first_section(overview_sections, "Problem"), "현재 source 범위에서 target problem은 본문 확인 필요."),
    )
    bottleneck = compact_cue(
        first_section(old_sections, "왜 문제인가", "선행 연구 / 배경 단서", "선행 연구 분석"),
        "선행 연구의 bottleneck은 현재 source 범위에서 확정하지 않으며 본문 확인이 필요하다.",
    )
    changes = compact_cue(
        first_section(old_sections, "해결하려는 문제", "What the Paper Changes"),
        compact_cue(first_section(overview_sections, "Core Idea", "Contribution"), "논문이 바꾼 formulation은 본문 확인 필요."),
    )
    position = compact_cue(
        first_section(old_sections, "Closed-Loop Position", "Position in the Robotics Loop"),
        "observation → state/world model → task & motion decision → policy/control → contact → feedback의 어느 위치인지 본문 확인 필요.",
    )
    anchor = compact_cue(
        first_section(overview_sections, "Problem", "Core Idea", "Abstract Cue"),
        "현재 01_overview와 기존 note에는 formulation source location이 기록되어 있지 않다.",
    )
    return {
        "problem": problem,
        "bottleneck": bottleneck,
        "changes": changes,
        "position": position,
        "anchor": anchor,
    }


def render_note(
    item: dict[str, Any],
    old: str,
    overview: str,
    tracker: dict[str, dict[str, str]],
) -> str:
    title = str(item["title"])
    evidence = evidence_for(item, old, overview, tracker)
    profile_data = PROFILES.get(title)
    basis = basis_text(profile_data)

    if profile_data is not None:
        problem = profile_data["problem"]
        bottleneck = profile_data["bottleneck"]
        changes = profile_data["changes"]
        position = profile_data["loop"]
        anchor = profile_data["anchor"]
        scope = scope_lines(profile_data)
        formal = [
            f"- **State / model:** {profile_data['model']}",
            f"- **Objective / loss / cost:** {profile_data['objective']}",
            f"- **Constraints / initial-boundary-terminal conditions:** {profile_data['constraints']}",
            f"- **Success / guarantee:** {profile_data['success']}",
        ]
        assumptions = render_assumptions(profile_data["assumptions"])
        still_verify = (
            "equation 번호와 exact source location, 그리고 04_evaluation의 reported protocol과 연결되는지를 확인한다."
            if profile_data.get("body_basis") in {"FULL_TEXT_FORMULATION_REVIEWED", "BODY_FORMULATION_REVIEWED", "BODY_FORMULATION_REVIEWED_CORRECTED_SOURCE"}
            else "abstract/formulation cue를 원문 method/problem section의 equation, assumption과 대조한다."
        )
    else:
        legacy = legacy_scaffold(old, overview, item)
        problem = legacy["problem"]
        bottleneck = legacy["bottleneck"]
        changes = legacy["changes"]
        position = legacy["position"]
        anchor = legacy["anchor"]
        scope = [
            "- **Object / environment:** 현재 source note에서 확인된 task/environment 범위만 유지하며 상세 조건은 본문 확인 필요.",
            "- **Observation / input:** observation/input interface는 본문 확인 필요.",
            "- **Latent state / decision variable:** state/decision variable은 본문 확인 필요.",
            "- **Output / action:** output/action/control interface는 본문 확인 필요.",
            "- **Horizon / evaluation target:** horizon과 evaluation target은 본문 확인 필요.",
        ]
        formal = [
            "- **State / model:** 현재 source 범위에서 확정하지 않음 — 본문 확인 필요.",
            "- **Objective / loss / cost:** 현재 source 범위에서 확정하지 않음 — 본문 확인 필요.",
            "- **Constraints / initial-boundary-terminal conditions:** 현재 source 범위에서 확정하지 않음 — 본문 확인 필요.",
            "- **Success / guarantee:** 현재 source 범위에서 확정하지 않음 — 본문 확인 필요.",
        ]
        assumptions = render_assumptions(
            [("논문이 두는 핵심 가정", "problem formulation을 재현하기 위해 필요", "원문 확인 전에는 failure boundary를 확정하지 않음")]
        )
        still_verify = "abstract/registry cue를 원문 problem·method section과 대조하고 state, objective, constraint, success condition을 채운다."

    return (
        f"# Problem — {title}\n\n"
        "> Canonical metadata: [01_overview.md](./01_overview.md).\n"
        f"> Evidence maturity: `{evidence}`.\n"
        f"> Analysis basis: {basis}\n\n"
        "## Problem in One Sentence\n\n"
        f"{problem}\n\n"
        "## System and Scope\n\n"
        + "\n".join(scope)
        + "\n\n## Formal Problem Formulation\n\n"
        + "\n".join(formal)
        + "\n\n## Bottleneck in Prior Work\n\n"
        + bottleneck
        + "\n\n## What the Paper Changes\n\n"
        + changes
        + "\n\n## Assumptions and Failure Boundary\n\n"
        + assumptions
        + "\n\n## Position in the Robotics Loop\n\n"
        + position
        + "\n\n## Verification Questions\n\n"
        + f"- **Evidence anchor:** {anchor}\n"
        + f"- **Still to verify:** {still_verify}\n"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true", help="write normalized notes; default is a dry run")
    parser.add_argument("--show", type=int, default=0, help="show the first N generated notes in dry-run mode")
    args = parser.parse_args()

    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    tracker = read_tracker()
    counts: Counter[str] = Counter()
    changed = 0
    missing_profiles: list[str] = []
    previews: list[str] = []

    for item in manifest:
        folder = resolve_folder(str(item["folder"]))
        note_path = folder / "02_problem.md"
        overview_path = folder / "01_overview.md"
        old = note_path.read_text(encoding="utf-8")
        overview = overview_path.read_text(encoding="utf-8")
        profile_data = PROFILES.get(str(item["title"]))
        if str(item["folder"]).casefold() in {key.casefold() for key in tracker} and profile_data is None:
            missing_profiles.append(str(item["title"]))
        new = render_note(item, old, overview, tracker)
        counts["CORE/NEXT profile" if profile_data is not None else "registry scaffold"] += 1
        changed += int(new != old)
        if args.show and len(previews) < args.show:
            previews.append(f"--- {note_path}\n{new}")
        if args.apply and new != old:
            note_path.write_text(new, encoding="utf-8")

    mode = "apply" if args.apply else "dry-run"
    intensive = sum(1 for item in manifest if str(item["title"]) in PROFILES)
    print(
        {
            "mode": mode,
            "registry_papers": len(manifest),
            "notes_to_update": changed,
            "intensive_profiles": intensive,
            "missing_intensive_profiles": len(missing_profiles),
            "profile_or_scaffold": dict(counts),
        }
    )
    for title in missing_profiles:
        print(f"MISSING PROFILE: {title}")
    for preview in previews:
        print(preview)


if __name__ == "__main__":
    main()
