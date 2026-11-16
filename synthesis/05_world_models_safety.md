# World Models, Safety, and Recovery

- Updated: 2026-11-09 KST

## Scope

Latent dynamics, robot/human-video world models, synthetic experience generation, MPC, policy evaluation, uncertainty calibration, runtime failure detection, safety filtering과 recovery를 비교한다.

### Taxonomy boundary and curation schema

- **Primary axis:** state/world prediction → uncertainty or safety signal → policy/planning use → failure detection and recovery.
- **In scope:** robot world model, model-based policy improvement, safety constraint/filter, failure monitor, recovery policy와 correction benchmark가 closed-loop execution을 평가하는 경우.
- **Out of scope:** visual prediction만 있고 robot action conditioning·planning·safety interface가 없는 video model, 또는 일반적인 safety 논문으로 robot deployment contract를 확인할 수 없는 경우.
- **Inclusion test:** prediction target or safety signal, action conditioning, runtime use, failure/recovery behavior, evaluation consequence 중 최소 세 가지를 확인할 수 있어야 한다.
- **Role vocabulary:** `foundation`, `world model`, `policy optimizer`, `safety filter`, `detector`, `recovery policy`, `benchmark`, `evaluation protocol`, `system`을 사용한다.

공통 matrix/evidence 규약은 [synthesis 안내](./README.md#공통-비교-규약과-질문-분류)를 따른다.

## Reading Path

현재 읽기 우선순위는 [READING_PLAN.md](../research/READING_PLAN.md)를 따른다. 아래 계보는 비교 탐색용이며 전체 선행 완독 의무가 아니다.

2026-10-19 초점: VLA/RL manipulation·navigation의 policy improvement, runtime failure detection 및 recovery 비용을 중심으로 비교한다. TD-MPC2와 Recovery RL을 기준으로 model fidelity·reward error·intervention·reset 조건을 명시한다.

World Models/PlaNet/Dreamer → DayDreamer/TD-MPC2 → DreamGen/DreamDojo and physical/video-action world models → CBF/Recovery RL → SAFE/FLARE/FaultEval → calibrated world-model use.

### 2026-10-19 추가 논문 비교

아래는 등록된 abstract/project 근거에서 만든 **정독 전 비교 질문**이다. 직접 citation이나 실험 결론으로 취급하지 않으며, 읽기 순서와 tier는 READING_PLAN의 최신 값을 따른다.

| 비교할 논문 | 비교 축 | 본문에서 확인할 조건 |
|---|---|---|
| [VLAW](../2026/ICML/2026_ICML_VLAW-Iterative-Co-Improvement-of-Vision-Language-Action-Po/01_overview.md) ↔ [VLA-MBPO](../2026/ICML/2026_ICML_Towards-Practical-World-Model-based-Reinforcement-Learning/01_overview.md) ↔ [RISE](../2026/RSS/2026_RSS_Self-Improving-Robot-Policy-with-Compositional-World-Model/01_overview.md) | World-model rollout과 policy improvement | 고정 model과 반복 갱신 model을 같은 real-data budget에서 비교하고 reward error·failure coverage를 확인한다. |
| [PointWorld](../2026/CVPR/2026_CVPR_PointWorld-Scaling-3D-World-Models-for-In-The-Wild-Robotic/01_overview.md) ↔ [PersistWorld](../2026/ECCV/2026_ECCV_Persistent-Robot-World-Models-Stabilizing-Multi-Step-Rollo/01_overview.md) / Ctrl-World·WMPO | 3D dynamics/MPC와 rollout fidelity의 역할 구분 | Prediction 품질, planning utility와 실제 policy 성공을 별도로 기록한다. PersistWorld는 REFERENCE이며 intensive queue를 늘리지 않는다. |
| [OopsieVerse](../2026/RSS/2026_RSS_OopsieVerse-A-Safety-Benchmark-with-Damage-Aware-Simulatio/01_overview.md) / Recovery RL | Task success와 물리적 damage의 분리 | Damage 정의, simulator 적용 범위와 success–safety trade-off를 확인한다. Simulation 결과로 실제 안전성을 보장하지 않는다. |

<!-- READING_QUEUE:START -->

## Assigned Reading Queue

### Safety and robot world models — 2

| Tier | Paper | Year / Venue | Status | Evidence |
|---|---|---|---|---|
| CORE | [TD-MPC2: Scalable, Robust World Models for Continuous Control](../2024/ICLR/2024_ICLR_TD-MPC2-Scalable-Robust-World-Models-for-Continuous-Contro/01_overview.md) | 2024 / ICLR | `UNREAD` | `FULL_TEXT_CHECKED` |
| CORE | [Recovery RL: Safe Reinforcement Learning with Learned Recovery Zones](../2020/RA-L/2020_RA-L_Recovery-RL-Safe-Reinforcement-Learning-with-Learned-Recov/01_overview.md) | 2020 / RA-L | `UNREAD` | `FULL_TEXT_CHECKED` |

### World models, uncertainty, failure detection, and recovery — 47

| Tier | Paper | Year / Venue | Status | Evidence |
|---|---|---|---|---|
| NEXT | [VLAW: Iterative Co-Improvement of Vision-Language-Action Policy and World Model](../2026/ICML/2026_ICML_VLAW-Iterative-Co-Improvement-of-Vision-Language-Action-Po/01_overview.md) | 2026 / ICML | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [Towards Practical World Model-based Reinforcement Learning for Vision-Language-Action Models](../2026/ICML/2026_ICML_Towards-Practical-World-Model-based-Reinforcement-Learning/01_overview.md) | 2026 / ICML | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [Self-Improving Robot Policy with Compositional World Model](../2026/RSS/2026_RSS_Self-Improving-Robot-Policy-with-Compositional-World-Model/01_overview.md) | 2026 / RSS | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [PointWorld: Scaling 3D World Models for In-The-Wild Robotic Manipulation](../2026/CVPR/2026_CVPR_PointWorld-Scaling-3D-World-Models-for-In-The-Wild-Robotic/01_overview.md) | 2026 / CVPR | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [OopsieVerse: A Safety Benchmark with Damage-Aware Simulation for Robot Manipulation](../2026/RSS/2026_RSS_OopsieVerse-A-Safety-Benchmark-with-Damage-Aware-Simulatio/01_overview.md) | 2026 / RSS | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [World Models](../2018/NeurIPS-Workshop/2018_NeurIPS-Workshop_World-Models/01_overview.md) | 2018 / NeurIPS Workshop | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [DayDreamer: World Models for Physical Robot Learning](../2022/CoRL/2022_CoRL_DayDreamer-World-Models-for-Physical-Robot-Learning/01_overview.md) | 2022 / CoRL | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [Control Barrier Function Based Quadratic Programs for Safety Critical Systems](../2017/TAC/2017_TAC_Control-Barrier-Function-Based-Quadratic-Programs-for-Safe/01_overview.md) | 2017 / TAC | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [DreamGen: Unlocking Generalization in Robot Learning through Video World Models](../2025/CoRL/2025_CoRL_DreamGen-Unlocking-Generalization-in-Robot-Learning-throug/01_overview.md) | 2025 / CoRL | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [DreamDojo: A Generalist Robot World Model from Large-Scale Human Videos](../2026/ICML/2026_ICML_DreamDojo-A-Generalist-Robot-World-Model-from-Large-Scale/01_overview.md) | 2026 / ICML | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [Learning Latent Dynamics for Planning from Pixels](../2019/ICML/2019_ICML_Learning-Latent-Dynamics-for-Planning-from-Pixels/01_overview.md) | 2019 / ICML | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [Dream to Control: Learning Behaviors by Latent Imagination](../2020/ICLR/2020_ICLR_Dream-to-Control-Learning-Behaviors-by-Latent-Imagination/01_overview.md) | 2020 / ICLR | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [Mastering Diverse Domains through World Models](../2025/Nature/2025_Nature_Mastering-Diverse-Domains-through-World-Models/01_overview.md) | 2025 / Nature | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [PIN-WM: Learning Physics-INformed World Models for Non-Prehensile Manipulation](../2025/RSS/2025_RSS_PIN-WM-Learning-Physics-INformed-World-Models-for-Non-Preh/01_overview.md) | 2025 / RSS | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets](../2025/RSS/2025_RSS_Unified-World-Models-Coupling-Video-and-Action-Diffusion-f/01_overview.md) | 2025 / RSS | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [FlowDreamer: A RGB-D World Model With Flow-Based Motion Representations for Robot Manipulation](../2026/RA-L/2026_RA-L_FlowDreamer-A-RGB-D-World-Model-With-Flow-Based-Motion-Rep/01_overview.md) | 2026 / RA-L | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [Can We Detect Failures Without Failure Data? Uncertainty-Aware Runtime Failure Detection for Imitation Learning Policies](../2025/RSS/2025_RSS_Can-We-Detect-Failures-Without-Failure-Data-Uncertainty-Aw/01_overview.md) | 2025 / RSS | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [SAFE: Multitask Failure Detection for Vision-Language-Action Models](../2025/NeurIPS/2025_NeurIPS_SAFE-Multitask-Failure-Detection-for-Vision-Language-Actio/01_overview.md) | 2025 / NeurIPS | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [WorldGym: World Model as An Environment for Policy Evaluation](../2026/ICLR/2026_ICLR_WorldGym-World-Model-as-An-Environment-for-Policy-Evaluati/01_overview.md) | 2026 / ICLR | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [WMPO: World Model-based Policy Optimization for Vision-Language-Action Models](../2026/ICLR/2026_ICLR_WMPO-World-Model-based-Policy-Optimization-for-Vision-Lang/01_overview.md) | 2026 / ICLR | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [FLARE: A Failure-Aware Framework for Autonomous Correction and Recovery in Visual-Language Robotic Manipulation](../2026/CVPR/2026_CVPR_FLARE-A-Failure-Aware-Framework-for-Autonomous-Correction/01_overview.md) | 2026 / CVPR | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [Can VLMs Diagnose and Recover from VLA Manipulation Faults?](../2026/ICML/2026_ICML_Can-VLMs-Diagnose-and-Recover-from-VLA-Manipulation-Faults/01_overview.md) | 2026 / ICML | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [Temporal Difference Calibration in Sequential Tasks: Application to Vision-Language-Action Models](../2026/ICML/2026_ICML_Temporal-Difference-Calibration-in-Sequential-Tasks-Applic/01_overview.md) | 2026 / ICML | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [Memory Retrieval in Visuomotor Policies for Long-Horizon Robot Control](../2026/RSS/2026_RSS_Memory-Retrieval-in-Visuomotor-Policies-for-Long-Horizon-R/01_overview.md) | 2026 / RSS | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [Demonstrating ViSafe: Vision-enabled Safety for High-speed Detect and Avoid](../2025/RSS/2025_RSS_Demonstrating-ViSafe-Vision-enabled-Safety-for-High-speed/01_overview.md) | 2025 / RSS | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [Learned Perceptive Forward Dynamics Model for Safe and Platform-aware Robotic Navigation](../2025/RSS/2025_RSS_Learned-Perceptive-Forward-Dynamics-Model-for-Safe-and-Pla/01_overview.md) | 2025 / RSS | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [Certifiably-Correct Mapping for Safe Navigation Despite Odometry Drift](../2025/RSS/2025_RSS_Certifiably-Correct-Mapping-for-Safe-Navigation-Despite-Od/01_overview.md) | 2025 / RSS | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [Particle-Grid Neural Dynamics for Learning Deformable Object Models from RGB-D Videos](../2025/RSS/2025_RSS_Particle-Grid-Neural-Dynamics-for-Learning-Deformable-Obje/01_overview.md) | 2025 / RSS | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [Map Space Belief Prediction for Manipulation-Enhanced Mapping](../2025/RSS/2025_RSS_Map-Space-Belief-Prediction-for-Manipulation-Enhanced-Mapp/01_overview.md) | 2025 / RSS | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [Unified Video Action Model](../2025/RSS/2025_RSS_Unified-Video-Action-Model/01_overview.md) | 2025 / RSS | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [From Foresight to Forethought: VLM-In-the-Loop Policy Steering via Latent Alignment](../2025/RSS/2025_RSS_From-Foresight-to-Forethought-VLM-In-the-Loop-Policy-Steer/01_overview.md) | 2025 / RSS | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [Prompting with the Future: Open-World Model Predictive Control with Interactive Digital Twins](../2025/RSS/2025_RSS_Prompting-with-the-Future-Open-World-Model-Predictive-Cont/01_overview.md) | 2025 / RSS | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [Self-Correcting Robot Manipulation via Gaussian-Splatted Foresight](../2025/AAAI/2025_AAAI_Self-Correcting-Robot-Manipulation-via-Gaussian-Splatted-F/01_overview.md) | 2025 / AAAI | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [WMNav: Integrating Vision-Language Models into World Models for Object Goal Navigation](../2025/IROS/2025_IROS_WMNav-Integrating-Vision-Language-Models-into-World-Models/01_overview.md) | 2025 / IROS | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [RoboDreamer: Learning Compositional World Models for Robot Imagination](../2024/ICML/2024_ICML_RoboDreamer-Learning-Compositional-World-Models-for-Robot/01_overview.md) | 2024 / ICML | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [Learning Interactive Real-World Simulators](../2024/ICLR/2024_ICLR_Learning-Interactive-Real-World-Simulators/01_overview.md) | 2024 / ICLR | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [SafeMimic: Towards Safe and Autonomous Human-to-Robot Imitation for Mobile Manipulation](../2025/RSS/2025_RSS_SafeMimic-Towards-Safe-and-Autonomous-Human-to-Robot-Imita/01_overview.md) | 2025 / RSS | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [Ctrl-World: A Controllable Generative World Model for Robot Manipulation](../2026/ICLR/2026_ICLR_Ctrl-World-A-Controllable-Generative-World-Model-for-Robot/01_overview.md) | 2026 / ICLR | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [LIBERO-RIG: A Hardware-Setup Robustness Benchmark for Vision-Language-Action Models](../2026/arXiv/2026_arXiv_LIBERO-RIG-A-Hardware-Setup-Robustness-Benchmark-for-Visio/01_overview.md) | 2026 / arXiv | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons](../2026/RSS/2026_RSS_Robometer-Scaling-General-Purpose-Robotic-Reward-Models-vi/01_overview.md) | 2026 / RSS | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [RoboReward: General-Purpose Vision-Language Reward Models for Robotics](../2026/arXiv/2026_arXiv_RoboReward-General-Purpose-Vision-Language-Reward-Models-f/01_overview.md) | 2026 / arXiv | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [Simple Masked Training Strategies Yield Control Policies That Are Robust to Sensor Failure](../2025/CoRL/2025_CoRL_Simple-Masked-Training-Strategies-Yield-Control-Policies-T/01_overview.md) | 2025 / CoRL | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [Scaling Robot Policy Evaluation via Discrete Diffusion World Model](../2026/ICML/2026_ICML_Scaling-Robot-Policy-Evaluation-via-Discrete-Diffusion-Wor/01_overview.md) | 2026 / ICML | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [Towards Generalizable Safety in Crowd Navigation via Conformal Uncertainty Handling](../2025/CoRL/2025_CoRL_Towards-Generalizable-Safety-in-Crowd-Navigation-via-Confo/01_overview.md) | 2025 / CoRL | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [DRILL: Training World Models to Improve Policies, Not Predict Pixels](../2026/NeurIPS/2026_NeurIPS_DRILL-Training-World-Models-to-Improve-Policies-Not-Predic/01_overview.md) | 2026 / NeurIPS | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [Causal World Modeling for Robot Control](../2026/RSS/2026_RSS_Causal-World-Modeling-for-Robot-Control/01_overview.md) | 2026 / RSS | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [Offline Policy Evaluation for Manipulation Policies via Discounted Liveness Formulation](../2026/RSS/2026_RSS_Offline-Policy-Evaluation-for-Manipulation-Policies-via-Di/01_overview.md) | 2026 / RSS | `UNREAD` | `ABSTRACT_CHECKED` |

<!-- READING_QUEUE:END -->

## Historical curation — 2026-09-02

아래는 해당 날짜의 변경 이력이다. 현재 membership과 수량은 위 generated queue를 따른다.

`WMNav`, `RoboDreamer`, `Learning Interactive Real-World Simulators`, `SafeMimic`, `Ctrl-World`를 `NEXT`에 반영했다. 이 queue는 world model을 reconstruction 결과가 아니라 action-conditioned prediction, policy evaluation/improvement, safety/recovery와 연결되는 폐루프 component로 다룬다. `Flow Equivariant World Models`는 action-conditioned foundation이지만 현재 검증된 real-robot evidence가 없어 `REFERENCE`에 유지했다.

## Comparison Matrix

> Matrix maturity: `CURATION-SEED`. 아래는 읽기 전 비교 가설이며 `READ`를 의미하지 않는다. `Paper` 링크는 local overview를 가리키고, official paper/project/code URL은 해당 note header에서 확인한다.
>
> Row convention: 한 행은 한 registry paper이다. `State / action / objective / timing`은 고정 순서로 기록하고, `Evaluation`은 `setup; data/split; metric; real/trials` 순서를 따른다. `Evidence / source`가 `CURATION-SEED`이면 수치나 세부 조건을 아직 주장하지 않는다.

| Paper | Year / Venue | Role | Facets | Problem | State / action / objective / timing | Why included / TL;DR | Evaluation (setup; data/split; metric; real/trials) | Evidence / source | Failure / assumption | Reusable idea |
|---|---|---|---|---|---|---|---|---|---|---|
| [CBF-QP](../2017/TAC/2017_TAC_Control-Barrier-Function-Based-Quadratic-Programs-for-Safe/01_overview.md) | 2017 / TAC | formulation; safety filter | control system; state+dynamics; real/sim; low-level safety | enforce safe-set invariance around a nominal controller | explicit state/dynamics; nominal action filtered by QP; barrier constraint and tracking objective; online filter | learned policy와 hard safety layer를 분리하는 formulation | safety-critical control; data/split=UNVERIFIED; metric=constraint violation/tracking; real/sim=UNVERIFIED/trials=UNVERIFIED | `CURATION-SEED`; overview + queue | dynamics mismatch, infeasible constraints, relative-degree assumptions | policy output과 safety filter를 별도 평가 |
| [Recovery RL](../2020/RA-L/2020_RA-L_Recovery-RL-Safe-Reinforcement-Learning-with-Learned-Recov/01_overview.md) | 2020 / RA-L | method; recovery policy | continuous robot control; state+risk; sim/real; safety/recovery | avoid unsafe transitions with learned recovery behavior | risk/recovery-zone model and state; task or recovery action; return plus safety objective; switching loop | detector가 아니라 executable recovery를 학습하는 기준 | continuous-control safety tasks; data/split=UNVERIFIED; metric=return/violations/recovery; real/sim=UNVERIFIED/trials=UNVERIFIED | `CURATION-SEED`; overview + queue | unsafe-boundary coverage, switching error, model bias | failure monitor와 recovery policy를 분리 |
| [World Models](../2018/NeurIPS-Workshop/2018_NeurIPS-Workshop_World-Models/01_overview.md) | 2018 / NeurIPS Workshop | foundation; world model | simulated agent; visual latent; simulation; model-based RL | learn compact predictive state for control | visual observation to latent state; action-conditioned future; imagination objective; rollout horizon | latent prediction을 policy learning에 연결한 출발점 | simulated control; data/split=UNVERIFIED; metric=return/prediction; real=no/trials=— | `CURATION-SEED`; overview + queue | compounding error, latent aliasing, model exploitation | prediction quality를 control utility와 함께 평가 |
| [DayDreamer](../2022/CoRL/2022_CoRL_DayDreamer-World-Models-for-Physical-Robot-Learning/01_overview.md) | 2022 / CoRL | method; world model | physical robot; vision+proprioception; real; online model-based RL | world-model learning for physical robot interaction | latent predictive state; imagined action policy; return/prediction objective; online update | latent imagination을 physical robot data efficiency와 연결 | physical robot tasks; data/split=UNVERIFIED; metric=return/data efficiency; real=yes/trials=UNVERIFIED | `CURATION-SEED`; overview + queue | nonstationarity, compounding error, real interaction cost | imagination과 real rollout을 분리 |
| [TD-MPC2](../2024/ICLR/2024_ICLR_TD-MPC2-Scalable-Robust-World-Models-for-Continuous-Contro/01_overview.md) | 2024 / ICLR | method; controller | continuous robots; latent state+action; sim/real; MPC | scalable robust latent world model for continuous control | latent dynamics and reward; sampled MPC action; return/value objective; receding horizon | world model과 MPC를 scalable continuous-control 기준으로 연결 | continuous-control tasks; data/split=UNVERIFIED; metric=return/data efficiency; real/sim=UNVERIFIED/trials=UNVERIFIED | `CURATION-SEED`; overview + queue | horizon error, model exploitation, compute/sample budget | model prediction을 receding-horizon utility로 검증 |
| [DreamGen](../2025/CoRL/2025_CoRL_DreamGen-Unlocking-Generalization-in-Robot-Learning-throug/01_overview.md) | 2025 / CoRL | data engine; world model | robot manipulation; video+action; sim/real; synthetic experience | generate robot experience to improve generalization | visual context with task/action conditioning; future video/interaction; generation objective; offline/imagined rollout | generated data를 control-grounded filter와 downstream policy로 연결 | manipulation; data/split=UNVERIFIED; metric=prediction/OOD/downstream success; real/sim=UNVERIFIED/trials=UNVERIFIED | `CURATION-SEED`; overview + queue | video/action inconsistency, embodiment mismatch, latency | generated sample와 control utility를 분리 |
| [DreamDojo](../2026/ICML/2026_ICML_DreamDojo-A-Generalist-Robot-World-Model-from-Large-Scale/01_overview.md) | 2026 / ICML | foundation; world model | robot; human+robot video; real/sim; generalist prediction | generalist robot world model from large-scale video | multimodal/video context and latent action; predicted future/interaction; pretraining objective; inference horizon UNVERIFIED | human-video prior와 robot-centric prediction의 interface | manipulation/contact tasks; data/split=UNVERIFIED; metric=prediction/OOD/downstream utility; real/sim=UNVERIFIED/trials=UNVERIFIED | `CURATION-SEED`; overview + queue | human–robot embodiment mismatch, action grounding, latency | pretraining source와 robot control utility를 분리 |
| [FAIL-Detect](../2025/RSS/2025_RSS_Can-We-Detect-Failures-Without-Failure-Data-Uncertainty-Aw/01_overview.md) | 2025 / RSS | detector; safety method | manipulation policy; observation+action; real/sim; runtime monitor | detect failures without collecting failure labels | policy feature/trajectory context; no action change or intervention trigger; uncertainty score; online monitor | failure-free calibration과 intervention timing의 기준 | manipulation; data/split=UNVERIFIED; metric=lead time/calibration/transfer; real/sim=UNVERIFIED/trials=UNVERIFIED | `CURATION-SEED`; overview + queue | false intervention, detector-action gap, distribution shift | detection과 correction을 분리 평가 |
| [SAFE](../2025/NeurIPS/2025_NeurIPS_SAFE-Multitask-Failure-Detection-for-Vision-Language-Actio/01_overview.md) | 2025 / NeurIPS | detector; benchmark method | VLA manipulation; visual trajectory; real/sim; multitask monitor | multitask failure detection for VLA execution | policy feature/trajectory and action context; intervention score; calibration/detection objective; online monitor | generalist policy의 runtime monitoring interface를 비교 | VLA manipulation; data/split=task splits UNVERIFIED; metric=lead time/calibration/multitask transfer; real/sim=UNVERIFIED/trials=UNVERIFIED | `CURATION-SEED`; overview + queue | false positives, calibration shift, no recovery by itself | monitor와 recovery controller를 분리 |
| [Unified World Models](../2025/RSS/2025_RSS_Unified-World-Models-Coupling-Video-and-Action-Diffusion-f/01_overview.md) | 2025 / RSS | world model; method | robot manipulation; video+action; sim/real; imagined evaluation | couple video and action diffusion for robot prediction | video/action context; future visual/action trajectory; joint generation objective; rollout horizon | visually plausible future와 action-conditioned utility를 함께 보는 기준 | robot manipulation; data/split=UNVERIFIED; metric=prediction/policy improvement; real/sim=UNVERIFIED/trials=UNVERIFIED | `CURATION-SEED`; overview + queue | video-action mismatch, model exploitation, sampling cost | imagined gain과 real gain을 calibration |
| [WMPO](../2026/ICLR/2026_ICLR_WMPO-World-Model-based-Policy-Optimization-for-Vision-Lang/01_overview.md) | 2026 / ICLR | policy optimizer; world model | VLA robot; vision+language+action; sim/real; policy improvement | use world-model rollouts for VLA policy optimization | policy-conditioned predictive state; candidate action/policy; imagined return/penalty; offline or receding update | world-model prediction을 policy improvement로 닫는 frontier | VLA manipulation; data/split=UNVERIFIED; metric=prediction/real policy gain; real/sim=UNVERIFIED/trials=UNVERIFIED | `CURATION-SEED`; overview + queue | visually plausible but action-wrong rollout, distribution shift, compute | model score와 real closed-loop gain을 분리 |


## Dependency and Evolution

아래 계보는 prediction model, policy optimization과 safety mechanism의 역할 변화를 구분한다. 직접 citation 관계는 정독 시 확인한다.

### Relation type index

아래 label은 바로 다음 계보 표의 chain anchor에 적용한다. `formulation`, `method`, `data`, `evaluation`, `deployment`는 개념적 연결의 종류이며 citation 또는 직접 영향 관계를 뜻하지 않는다.

| Chain anchor | Relation type | Interpretation |
|---|---|---|
| World Models → PlaNet/Dreamer → DayDreamer/TD-MPC2 | formulation → method → deployment | latent prediction이 physical robot control로 확장 |
| DDPM/action diffusion → Unified World Models → WMPO | generative formulation → policy optimization | video/action generation이 imagined policy improvement로 연결 |
| human/robot video → DreamGen → DreamDojo | data → world model | video source가 robot-centric predictive model로 확장 |
| learned world model → PIN-WM/Dexterous World Models | method → formulation | generic latent prediction에 physics/contact structure를 추가 |
| CBF → Recovery RL → FAIL-Detect/SAFE → FLARE/FaultEval | safety formulation → recovery → evaluation | hard constraint가 detection·diagnosis·correction protocol로 확장 |
| MomaGraph/Spatial Memory → Memory Retrieval/HALO | memory → deployment/safety | explicit state가 sparse retrieval과 stale-state handling으로 연결 |

| Foundation → transition → frontier | 계승·변화 | 아직 확인할 경계 |
|---|---|---|
| [World Models](../2018/NeurIPS-Workshop/2018_NeurIPS-Workshop_World-Models/01_overview.md) → [PlaNet](../2019/ICML/2019_ICML_Learning-Latent-Dynamics-for-Planning-from-Pixels/01_overview.md) / [Dreamer](../2020/ICLR/2020_ICLR_Dream-to-Control-Learning-Behaviors-by-Latent-Imagination/01_overview.md) → [DayDreamer](../2022/CoRL/2022_CoRL_DayDreamer-World-Models-for-Physical-Robot-Learning/01_overview.md) / [TD-MPC2](../2024/ICLR/2024_ICLR_TD-MPC2-Scalable-Robust-World-Models-for-Continuous-Contro/01_overview.md) | compressed predictive state에서 latent planning과 imagination-based learning을 거쳐 physical robot online learning과 scalable continuous control로 확장된다. | real-world nonstationarity와 contact에서 horizon별 model error가 policy update를 언제 오도하는가 |
| [DDPM](../2020/NeurIPS/2020_NeurIPS_Denoising-Diffusion-Probabilistic-Models/01_overview.md) / action diffusion → [Unified World Models](../2025/RSS/2025_RSS_Unified-World-Models-Coupling-Video-and-Action-Diffusion-f/01_overview.md) → [WMPO](../2026/ICLR/2026_ICLR_WMPO-World-Model-based-Policy-Optimization-for-Vision-Lang/01_overview.md) | policy, forward/inverse dynamics와 video generation을 공동 모델링하고 imagined rollout을 VLA policy optimization에 사용한다. | video likelihood가 action ranking과 real policy improvement에 충분한가; model exploitation을 어떻게 제한하는가 |
| large-scale human/robot video → [DreamGen](../2025/CoRL/2025_CoRL_DreamGen-Unlocking-Generalization-in-Robot-Learning-throug/01_overview.md) → [DreamDojo](../2026/ICML/2026_ICML_DreamDojo-A-Generalist-Robot-World-Model-from-Large-Scale/01_overview.md) → policy evaluation/model-based planning | robot-domain synthetic experience 생성에서 human-video latent action pretraining과 real-time robot-centric prediction으로 확장된다. | unlabeled human interaction의 latent action이 robot actuation과 contact outcome을 보존하는가 |
| learned world model → [PIN-WM](../2025/RSS/2025_RSS_PIN-WM-Learning-Physics-INformed-World-Models-for-Non-Preh/01_overview.md) / [Dexterous World Models](../2026/CVPR/2026_CVPR_Dexterous-World-Models/01_overview.md) | generic latent/video prediction에 task-relevant physical structure와 dexterous contact dynamics를 넣는 방향이다. | physics prior가 어떤 contact regime에서 generalization을 돕고 언제 model bias를 키우는가 |
| [Control Barrier Function QP](../2017/TAC/2017_TAC_Control-Barrier-Function-Based-Quadratic-Programs-for-Safe/01_overview.md) → [Recovery RL](../2020/RA-L/2020_RA-L_Recovery-RL-Safe-Reinforcement-Learning-with-Learned-Recov/01_overview.md) → [FAIL-Detect](../2025/RSS/2025_RSS_Can-We-Detect-Failures-Without-Failure-Data-Uncertainty-Aw/01_overview.md) / [SAFE](../2025/NeurIPS/2025_NeurIPS_SAFE-Multitask-Failure-Detection-for-Vision-Language-Actio/01_overview.md) → [FLARE](../2026/CVPR/2026_CVPR_FLARE-A-Failure-Aware-Framework-for-Autonomous-Correction/01_overview.md) / [VLA-FixBench/FaultEval](../2026/ICML/2026_ICML_Can-VLMs-Diagnose-and-Recover-from-VLA-Manipulation-Faults/01_overview.md) | constraint·recovery zone에서 alert, diagnosis와 correction protocol로 확장된다. | failure detection, correction success와 intervention cost를 어떤 공통 protocol로 비교할 것인가 |
| [MomaGraph](../2026/ICLR/2026_ICLR_MomaGraph-State-Aware-Unified-Scene-Graphs-with-Vision-Lan/01_overview.md) / [Spatial Memory](../2026/ICML/2026_ICML_Spatial-Memory-for-Out-of-Vision-Manipulation-in-Vision-La/01_overview.md) → [Memory Retrieval/HALO](../2026/RSS/2026_RSS_Memory-Retrieval-in-Visuomotor-Policies-for-Long-Horizon-R/01_overview.md) | explicit state graph와 out-of-view memory에서 task-relevant sparse retrieval과 long-horizon drift mitigation으로 이동한다. | stale memory를 expire/reobserve할 calibrated rule과 safety outcome이 있는가 |

## 2026-10-23 근거 통합

아래는 2026-10-22까지의 registry/source 감사와 후보 검토를 연결한 연구자 해석이다. 새 정독·효과 검증·직접 citation 관계의 확인을 뜻하지 않는다. Paper별 본문 확인 범위는 overview 및 연결된 dossier를 따른다.

| 비교 축 | 등록된 선행 | 현재 남길 구분 |
|---|---|---|
| C4: reward audit | [Hypothetical behavior](../2020/ICML/2020_ICML_Learning-Human-Objectives-by-Evaluating-Hypothetical-Behav/01_overview.md) (2020 ICML); [Information-directed reward](../2021/NeurIPS/2021_NeurIPS_Information-Directed-Reward-Learning-for-Reinforcement-Lea/01_overview.md) (2021 NeurIPS); [PROGRESSOR](../2025/ICCV/2025_ICCV_PROGRESSOR-A-Perceptually-Guided-Reward-Estimator-with-Sel/01_overview.md) (2025 ICCV); [Robometer](../2026/RSS/2026_RSS_Robometer-Scaling-General-Purpose-Robotic-Reward-Models-vi/01_overview.md) (2026 RSS); [RoboReward](../2026/arXiv/2026_arXiv_RoboReward-General-Purpose-Vision-Language-Reward-Models-f/01_overview.md) (2026 arXiv) | 보상 정확도와 정책 개선을 별도 축으로 둔다. Adaptive audit 자체보다 policy chronology·독립 outcome·query 비용이 남은 조건이다. |
| C6: policy comparison | [AutoEval](../2025/CoRL/2025_CoRL_AutoEval-Autonomous-Evaluation-of-Generalist-Robot-Manipul/01_overview.md) (2025 CoRL); [Active Offline Selection](../2021/NeurIPS/2021_NeurIPS_Active-Offline-Policy-Selection/01_overview.md) (2021 NeurIPS); [Near-Optimal Stopping](../2025/RSS/2025_RSS_Is-Your-Imitation-Learning-Policy-Better-than-Mine-Policy/01_overview.md) (2025 RSS); [Beyond Binary Success](../2026/RSS/2026_RSS_Beyond-Binary-Success-Sample-Efficient-and-Statistically-R/01_overview.md) (2026 RSS); [Active Experiment Selection](../2025/CoRL/2025_CoRL_Efficient-Evaluation-of-Multi-Task-Robot-Policies-With-Act/01_overview.md) (2025 CoRL) | Checkpoint selection·순차 중단·active 평가의 기존 대안을 포함한다. 평가 protocol 재사용과 독립 신규 방법 채택을 구별한다. |
| Recovery의 행동 가치 | [RESCUE](../2026/arXiv/2026_arXiv_RESCUE-Is-This-Alarm-Worth-Acting-On-Counterfactual-Evalua/01_overview.md) (2026 arXiv); [SafeLoop](../2026/arXiv/2026_arXiv_SafeLoop-Risk-Aware-Rollback-for-Vision-Language-Action-Ma/01_overview.md) (2026 arXiv) | Alarm의 정확도만으로 개입 이득을 주장하지 않는다. Counterfactual continuation·rollback 가능성·추가 시도 비용을 확인한다. |

### Registry 연결 갱신 — 2026-10-25

- [Simple Masked Training Strategies Yield Control Policies That Are Robust to Sensor Failure](../2025/CoRL/2025_CoRL_Simple-Masked-Training-Strategies-Yield-Control-Policies-T/01_overview.md)
- [Scaling Robot Policy Evaluation via Discrete Diffusion World Model](../2026/ICML/2026_ICML_Scaling-Robot-Policy-Evaluation-via-Discrete-Diffusion-Wor/01_overview.md)
- [Towards Generalizable Safety in Crowd Navigation via Conformal Uncertainty Handling](../2025/CoRL/2025_CoRL_Towards-Generalizable-Safety-in-Crowd-Navigation-via-Confo/01_overview.md)

World-model policy ranking, 센서 결손 대비, 군중 예측 보정의 적용 단위를 구분한다. 모델의 시각 품질·coverage만으로 native 성공·안전을 결론내리지 않는다.

이번 등록은 `ABSTRACT_CHECKED` 수준의 비교 연결이다. 기존 정독 matrix·reading status·연구 판단을 승격하지 않는다. [등록 범위와 source 경계](../work/update/REGISTRY_REFRESH_2026-10-25.md).

### 2026-10-25 top-tier 보완 — 읽기 전 비교 연결

> Researcher interpretation / CURATION-HYPOTHESIS. 신규 노트는 abstract/project 기반이며 아래 연결은 정독·실험 결과나 직접 citation 관계의 확인이 아니다.

[General agents need world models](../2025/ICML/2025_ICML_General-agents-need-world-models/01_overview.md)의 정책에서 추출 가능한 예측 모델과 [WorldTest/AutumnBench](../2026/ICML/2026_ICML_Benchmarking-World-Model-Learning-with-Environment-Level-Q/01_overview.md)의 환경 질의는 dWorldEval의 정책 순위 평가와 목적이 다르다. 명시적 video architecture의 필요성, 예측 품질, task return, counterfactual 질의 능력을 한 결론으로 합치지 않는다.

로봇에 옮길 때는 같은 관측 이력으로 구별할 수 없는 환경 쌍과 행동 선택에 필요한 질의를 먼저 정한다. WorldTest의 grid-world 결과를 로봇 안전/제어의 검증으로 승격하지 않는다. GAP-WM·SYSID의 기존 직접 충돌 및 HOLD는 유지한다.

## Open Questions

### Recovery 평가와 action-conditioned 세계 모델의 출처 경계

**2026-11-12 / 초록 기반 CURATION-HYPOTHESIS.** [Discounted Liveness OPE, RSS 2026](https://www.roboticsproceedings.org/rss22/p154.html)는 recovery 도중 끝나는 데이터의 truncation bias와 manipulation policy 평가를 다룬다. 관측된 실패가 정책 능력 부족인지 관측 기간·종료 규칙의 효과인지 구분할 직접 선행이다. RSS 초록의 두 simulation task 범위를 사용했으며 preprint의 추가 cloth demo를 같은 최종본의 실물 증거로 합치지 않았다. Offline 평가값의 개선은 native closed-loop 성공률의 검증이 아니다.

[Causal World Modeling for Robot Control, RSS 2026](https://www.roboticsproceedings.org/rss22/p016.html)의 공식 초록은 **CauVA**와 MoT·시간 이력 구조를 기술한다. 같은 제목의 arXiv `2601.21998`은 LingBot-VA 명칭·저자·구성 차이가 있어 동일 version 연결을 보류했다. 그 arXiv ID·code를 RSS entry에 전사하지 않았다. 앞으로 재현이나 직접 충돌 심사에서는 정확한 version·관측 이력·action conditioning을 먼저 고정한다. 이 두 등록과 [VLA의 WCM 비교](./04_vla_generalist.md#foundation-frontier-2026)는 model prediction·critic·offline 평가·정책 실행을 분리하기 위한 보강이며 기존 WM/HOLD 판정을 변경하지 않는다.

<a id="gap-recoverability-rl-2026"></a>
### 복구 행동뿐 아니라 복구 가능성을 보존하는 VLA 강화학습

**2026-11-09 / GAP-RECOVERABILITY-RL / 2순위 예비 탐색 / CURATION-HYPOTHESIS.** [Robotics 중심 비교](../work/update/VLA_RL_ADDITIONAL_GAPS_2026-11-09.md#robotics-reorientation), [근거 R12–R16·R21](../work/sources/vla_rl_additional_gaps_2026-11-09.json). C5의 reset 분포/학습 coverage, HINDSIGHT의 목표 재라벨링과 구별하며 기존 HOLD를 자동 해제하지 않는다.

**질문:** 물체를 작업 공간 밖으로 밀거나 더 깊이 끼우는 행동을 피하도록 단일 VLA를 RL 후학습하면, **원래 지시를 유지하면서** 실패 이후의 회복 여지를 보존하고 전체 자율 성공률을 높일 수 있는가? 실패 뒤 외부 planner를 호출하는 것이 아니라 정상 실행 단계의 행동 선택까지 바꾸는 방향이다. 실패 이후 성공한 다른 목표로 원 목표를 대체하지 않는다.

**이미 해결된 범위:** [ReCoVLA](https://arxiv.org/abs/2606.09630)는 실패 조건부 reward compilation과 residual recovery를, [OGPO](https://arxiv.org/abs/2610.12914)는 offline goal-conditioned post-training과 perturbation 복구를 다룬다. [Kintsugi-VLA](https://arxiv.org/abs/2609.31048)는 고정 expert의 simulator 분기 성공으로 recoverability와 recovery-data 선택을 이미 연구한다. [RESCUE](https://arxiv.org/abs/2610.13516)는 알람 정확도와 실제 개입 가치를 구분한다. 따라서 복구 데이터, reachability reward, 복구 시점/가능성 측정 자체를 최초 기여로 내세우지 않는다. 이 목록은 모두 이번 확인 범위에서 2026 arXiv이며 채택 논문으로 승격하지 않았다.

**좁은 가설:** 학습한 행동의 즉시 진행도와 이후 복구 비용이 충돌하는 자연 상황에서, 단일 VLA의 학습 목적/표현을 바꾸는 것이 성공 데이터 증강·단순 후퇴·표준 위험 민감 RL보다 유용한가? 이는 아직 선행 전체로 확인되지 않은 질문이다. Recovery RL·viability/safe RL와의 직접 차이는 다음 문헌 심사가 필요하다. 높은 로보틱스 관련성이 곧 새 방법의 근거는 아니다.

**비교 초안:** task reward-only RL, recovery data SFT, 단순 힘 제한/후퇴, 위험 또는 비용 penalty를 사용하는 표준 RL, residual recovery를 대조한다. 같은 seed의 원 정책 재실행도 포함한다. [Simple Retreat 분석](https://arxiv.org/abs/2610.06921)이 보여주는 것처럼 우연한 재시도 성공을 learned recovery 효과로 세지 않는다. 정상 episode 성공률·전체 completion time·human rescue 수·최대 힘/작업 공간 이탈을 함께 보고한다.

`Recoverable`은 **지정된 continuation 정책/행동 집합·시간·힘 예산으로 원 목표에 도달할 확률**이다. 고정 expert의 실패를 물리적 불가능으로 단정하지 않는다. Simulator 상태 복원뿐 아니라 물체 속도·접촉 내부 상태·controller/policy history도 맞춰야 한다. 이 확률은 평가 도구이며 정책이 privileged state를 입력받아도 된다는 뜻이 아니다. 회복 데이터/return-weighted imitation·고전 제어로 차이가 설명되면 새 RL 목적의 필요성을 철회한다. 현재는 작은 비실험 탐색만 가능하며 데이터·observer·성공 효과는 미확인이다.

<a id="gap-physics-2026"></a>
### VLA의 시뮬레이션 RL 업데이트와 접촉·동역학 일반화

**11/09 후속:** Robotics 중심 요청에 따라 행동 학습으로 좁힌 [접촉 적응 분기](./03_manipulation_contact.md#gap-contact-rl-2026)를 먼저 검토한다. 아래 broad physics 진단은 예비 질문으로 보존한다.

- **2026-11-09 / GAP-PHYSICS / CURATION-HYPOTHESIS / 조건부 탐색.** [선정·제외 이력](../work/update/VLA_RL_ADDITIONAL_GAPS_2026-11-09.md), [근거 S01·S07–S10](../work/sources/vla_rl_additional_gaps_2026-11-09.json). 단일 VLA의 학습 후 행동을 묻는다. Learned world-model의 candidate scoring(GAP-WM), reward audit(C4), online system identification(SYSID), stale/fresh visual feedback(FEEDBACK)과 같은 질문으로 취급하지 않는다.
- **직접 선행과 반대 증거:** [RL4VLA, NeurIPS 2025](https://proceedings.nips.cc/paper_files/paper/2025/hash/8c0fabe372177d2aded596be2d3b4544-Abstract-Conference.html)는 RL/SFT의 실행·시각·의미 일반화를 비교한다. [Grounding Sim-to-Real §4.3–4.4·B.3](https://arxiv.org/html/2603.22876v2)은 물리 왜곡 실험과 RL의 긍정적 실물 전이를 이미 제시한다. [SIMPLER, CoRL 2024/PMLR 2025](https://proceedings.mlr.press/v270/li25c.html)와 [PolaRiS, RSS 2026](https://roboticsproceedings.org/rss22/p062.html)는 simulation의 real-policy 평가 상관을 연구했다. 따라서 physics gap·sim-to-real 평가 자체는 새 공백이 아니며 RL이 전이를 해친다는 방향도 가정하지 않는다.
- **남은 질문 — 연구자 해석:** 같은 VLA action interface로 RL 업데이트를 진행할 때, 훈련 환경의 성공률 변화와 **실현 가능한 접촉/동역학 변화에 대한 민감도**는 언제 함께 개선되고 언제 분리되는가? Matched-data SFT 및 통상적인 domain randomization 이후에도 업데이트 단계×접촉 regime의 차이가 남는가? 확인한 선행 구간만으로 이 조건부 질문의 답은 결정할 수 없지만, 후속 전체 본문/코드 검토에서 직접 해결된 것으로 드러날 수 있다.
- **최소 비교 초안:** 원 reward/성공 판정·camera·action scaling·controller·control rate를 고정하고, 공통 초기 checkpoint에서 SFT 유지/동일 수집 데이터 추가 SFT/RL/RL+physics randomization을 비교한다. Visual-only, physics-only, 양쪽 변화, 원 환경의 조건을 나눈다. 처음에는 한 simulator에서 타당한 마찰·접촉 조건 범위를 개발 set으로 정하고 별도 범위/조합을 평가에 남긴다. 데이터 수·interaction·학습 계산의 차이를 기록한다. Task 자체가 불가능해진 조건은 별도 분류한다.
- **학습 진행의 비교:** Update budget을 맞춘 learning curve가 주 비교다. 원 환경 성공률을 맞춘 checkpoint 비교는 보조 분석으로 두며 별도 validation에서 선택하고 training cost를 공개한다. Test 성공을 보고 checkpoint를 고르거나 matched-success 선택만으로 RL의 인과 효과를 주장하지 않는다. 성공률 외 접촉 실패·미끄러짐·재시도 등은 simulator가 실제 제공하고 교정 가능한 경우에만 지표로 채택한다.
- **경쟁 설명:** 단순 시각 shift, controller 부정합, 행동 head 변경, 더 많은 online data, 더 어려워진 task가 민감도 차이를 만들 수 있다. 특히 직접 선행의 RL 비교에는 action head 변경 후 SFT 재학습이 포함되므로 이를 그대로 원 SFT와 무통제 비교하지 않는다. Physics 변화는 장래 관측 영상도 바꾸므로 visual/physics 조건 분할만으로 내부 표현의 원인을 식별했다고 주장하지 않는다.
- **기여·축소 조건:** 단순 DR·초기 중단·같은 데이터 SFT로 전부 설명되면 독립 방법 대신 평가 분석으로 축소한다. 반복되는 trade-off가 없으면 “RL의 simulator exploit” 가설을 포기한다. 현상이 있더라도 새로운 solver로 성능이 떨어졌다는 사실만으로 exploit나 실물 실패를 입증하지 못한다. 두 engine 간 비교에는 관측·controller·asset 동등성 교정이 필요하며 실제 sim-to-real 주장에는 실물 평가가 추가로 필요하다.
- **가치와 부담:** 접촉이 중요한 manipulation의 RL 후학습 신뢰성이라는 행동상의 중요성은 크다. 그러나 강한 선행 실증 연구가 있고 물리 타당성·여러 checkpoint 학습·실물 확인 부담이 높아 이번 두 후보 중 두 번째다. 현재 환경/adapter 확인이나 실험은 수행하지 않았다. 작은 진단 자체를 막지는 않되, 대규모 benchmark·새 강건 RL 방법의 개발은 현상 확인 후 결정한다.
- **다음 비실험 관측:** Grounding Sim-to-Real의 physics 및 RL 실험 교차 여부, RL4VLA의 execution shift 정의, 공개 trainer의 action-head/정규화/DR 범위를 본문과 코드로 대조한다. 이미 같은 update×physics 결과가 있으면 반복 연구로 명시하거나 질문을 수정한다. 현재는 외부 피드백·native 현상·방법 효과 모두 미확인이다.

### World-model RL과 VLA policy RL의 평가 대상 — 2026-11-08

**CURATION-HYPOTHESIS.** [RLVR-World](https://proceedings.neurips.cc/paper_files/paper/2025/hash/b63a24a1832bd14fa945c71f535c0095-Abstract-Conference.html)는 decoded transition prediction 지표를 RL 보상으로 최적화한다. [RehearseVLA](https://openaccess.thecvf.com/content/CVPR2026/html/Xiao_RehearseVLA_Simulated_Post-Training_for_VLAs_with_Physically-Consistent_World_Model_CVPR_2026_paper.html)는 world model을 policy 후학습의 simulated environment로 활용한다. 두 논문에서 갱신하는 모델과 보상 대상은 다르다. 같은 planner/actor·상상 rollout·실제 평가 예산에서 예측 품질과 실제 행동 성공을 함께 측정해야 한다. RT-1 영상 예측 성능을 robot policy return으로 승격하지 않는다. [REG-R12](../work/update/TOP_TIER_SUPPLEMENT_2026-11-08.md)의 신규 노트는 ABSTRACT_CHECKED·UNREAD이며 실행 효과는 미검증이다.

현재 후보 판정은 [주제별 요약](../work/research_candidates/summaries/README.md)을 따른다. 아래 질문은 `CURATION-HYPOTHESIS`이며 재개 승인이 아니다.

<a id="gap-authorization-2026"></a>
### GAP-AUTH — 정책의 목표 추정 오류가 보호 대상 설정으로 전파되는가?

- **2026-10-27 GAP-AUTH4:** [로컬 지각·baseline 심사](../work/update/VLA_CONTACT_AUTHORIZATION_BASELINE_REVIEW_2026-10-27.md), [source/비교/재개 gate](../work/sources/vla_contact_authorization_baseline_review_2026-10-27.json). 공식 YOLOE 20파일·AEGIS 2파일 지정 구간과 checkpoint metadata로 공통 지각 후보를 좁혔다. 초기 지시 grounding+identity 고정+최신 geometry 이후 고유 이득 미확보로 **현재 방법 채택 NO-GO·진단 HOLD**. Packet PARTIAL·native/효과 미검증이며 실험적 반증이 아니다. `CURATION-HYPOTHESIS`와 기존 후보 보류 유지.
- **직접 선행:** [KNOWS §3–4](https://arxiv.org/html/2606.09749v1)는 attention 목표를 보호에서 제외하며 낮은 confidence에는 전부 보호한다. [AEGIS](https://arxiv.org/html/2512.11891v2)는 지시 기반 외부 VLM과 CBF를, [RoboGuard](https://arxiv.org/html/2503.07885v2)는 독립 의미 사양 생성을 다룬다. 모두 같은 방법이라고 묶지 않으며 KNOWS/AEGIS의 공식 conference/journal status는 미확인이다. 독립 guard·의미 제약 자체는 새 기여가 아니다.
- **남은 질문 — 연구자 해석:** 같은 geometry·tracking·controller·시점에서 **높은 신뢰도의 잘못된 목표**를 정책이 선택할 때, 내부 의도를 사용한 허용 판단도 같은 오선택을 하는가? 원 지시 기반 고정/독립 판단으로 바꾸면 정상 작업을 유지하면서 그 오류를 줄일 수 있는가? 물체 역할은 task contract에서 고정하며 위반을 물리적 손상과 동일시하지 않는다.
- **반례와 경계:** 보호해야 할 물체를 장애물 집합에서 제외하면, 설정된 제약의 만족이 그 물체의 비접촉을 보장하지 않는다. 이는 이론의 반증이나 실측이 아니다. 첫 pre-grasp gripper 접촉에 범위를 한정하고 모든 link·모든 phase로 확대하지 않는다.
- **최소 대조:** 내부 proxy/원 지시 관계라는 판단 출처 × 초기 identity 고정/query 재판단의 2×2. 특히 **R-init: 처음 지시로 목표를 정해 고정하되 geometry는 계속 갱신**하는 단순 대안을 포함한다. Confidence threshold·전부 보호/정지·oracle reference도 유지한다. 평가 truth는 guard와 분리하고 모든 예정 rollout의 위반·완료·방해·invalid·시간을 함께 센다. 자연 오류와 주입 오류를 분리한다.
- **측정 선행/자산 한계:** [SafeVLA-Bench v3](https://arxiv.org/html/2606.00773v3)는 이미 task별 적용 조건과 비대상 변화 등을 평가한다. Metric 추가만으로 기여를 주장하지 않는다. AUTH2의 두 과제는 목표와 다른 검은 그릇이 있지만 원 goal에 비접촉 조건이 없다. 따라서 새 wrong-instance contact는 native safety가 아닌 수정 진단이다. 평가용 target/geom ID와 guard의 visual track을 분리한다.
- **확인한 연결과 미완료:** 공식 π0.5-LIBERO JAX bundle/quantile norm을 로컬 비교 기준으로 특정했으며 저자 실행 weights와의 동일성은 미확인이다. 선택 config는 state 값을 policy conditioning에 쓰지 않는다. Attention은 camera-only/full-key 정규화를 구분하고 output transform 뒤 별도 export가 필요하다. Contact는 기존 physics forward 직후 기록하도록 명세했으며 step 뒤 정보를 새 state로 잘못 표기하지 않는다. 이들은 정적 확인/계약이지 구현·동일성 검사 결과가 아니다.
- **공정 비교의 잔여:** 단일 bbox/QP를 그대로 쓰면 geometry와 허용 판단 효과가 섞인다. 모든 arm의 공통 visual track·geometry·filter와 독립 evaluator가 필요하다. 평가용 truth ID는 guard에 주지 않으며 평균 attention proxy 실패만으로 validated head 계열을 반박하지 않는다. YOLOE/ByteTrack 자산과 기본 interface는 특정했지만 실제 scene 검출·ID 유지·camera/depth 정합·δ·solver/geometry calibration·native reset/equivalence는 미확정/미검증이다.
- **조건부 충분성/해석:** 초기 relation grounding이 맞고 track identity가 유지되며 task의 허용 instance가 고정이면 R-init의 오허용은 이미 0이다. 이는 조건부 논증이며 scene 검출·tracking 성능·무접촉의 실증이 아니다. 움직인 뒤 현재 on/between 관계를 만족하는 다른 물체로 다시 지칭하면 task를 바꾼 것이다. 지각 오류·초기 선택·갱신·identity 복구를 분리하지 않은 이득을 새로운 독립 guard 효과로 해석하지 않는다.
- **재개 gate:** [TODO](../TODO.md)의 GAP-AUTH-R1은 자연 instance/RGB-D/time/action/contact packet과 validated readout, R-init/I-init/threshold/단순 재평가 이후의 예측이 새로 확보될 때만 심사한다. 현재 비실험 확장은 종료하며 같은 source 감사나 GPU 확보만으로 재개하지 않는다. 별도 [종료 평가 질문](./04_vla_generalist.md#gap-termination-2026)도 [TERM1 심사](../work/update/VLA_TERMINATION_CONTRACT_REVIEW_2026-10-27.md)에서 현재 독립 후보 NO-GO·진단 HOLD로 정했으며 AUTH 재개와 구분한다.

| 질문 | 구별할 예측 | 최소 대조·중단 조건 | 근거/판정 |
|---|---|---|---|
| C4 reward의 downstream 효과 | 독립 outcome으로 측정한 policy ranking이 reward model/audit 선택 이후에도 유지되는가? | Versioned rollout·chronology·독립 evaluator·검수 비용이 없으면 정책 개선 주장 불가. 넓은 방법 NO-GO/진단 HOLD. | [검토 근거](../work/research_candidates/2026-10-21_c4_reward_audit/README.md) |
| C5 reset의 분모 | 성공·실패·retry·rescue 전체를 포함하면 coverage와 자율 학습 비용에 대한 결론이 달라지는가? | 성공 episode만 남은 자료로 reset 이득을 추정하지 않는다. Complete ledger 확보 전 HOLD. | [검토 근거](../work/research_candidates/2026-10-21_c5_reset_audit/README.md) |
| C6 선택 편향 | 동일 평가 예산에서 기존 sequential comparison보다 나은 독립 holdout 선택이 가능한가? | Trial-level data·정책 이력·독립 outcome 없이 best checkpoint 점수로 평가하지 않는다. 현재 독립 신규 방법 NO-GO. | [검토 근거](../work/research_candidates/2026-10-21_c6_checkpoint_audit/README.md) |
| World model·recovery | 동일 real rollout budget에서 fidelity/monitor score 개선이 실제 success·damage·intervention cost 개선을 예측하는가? | 모델 bias와 uncertainty calibration, human-video latent action의 contact/actuator 제약을 held-out 실제 실행에서 확인한다. Synthetic 성공은 대체 증거가 아니다. | 기존 track 비교의 연구자 질문; native 효과 미검증 |

### 2026-10-23 외부 문헌으로 좁힌 범위

[WorldEval](https://worldeval.github.io/)·[dWorldEval](https://dworldeval.github.io/)·[RoboWorld](https://arxiv.org/abs/2607.01060)은 world model 기반 policy 평가를, [DreamTrue](https://arxiv.org/abs/2610.12468)는 action fidelity를 직접 다룬다. [Decision-making-centric position](https://arxiv.org/abs/2606.15032)도 행동 중심 평가를 제안한다. 따라서 **video quality 대신 policy ranking을 보자**는 넓은 주장만으로 새 연구를 채택하지 않는다. Position과 project/abstract의 주장, 독립 실험 증거를 구분한다. 후속 [GAP-WM1](../work/update/WORLD_MODEL_SELECTION_REVIEW_2026-10-23.md)에서 아래 직접 경쟁 5편의 지정 본문과 공개 interface를 대조했다.

dWorldEval은 [ICML 2026 공식 proceedings](https://proceedings.mlr.press/v306/li26hi.html)에서 **Scaling Robot Policy Evaluation via Discrete Diffusion World Model**로 확인했다. 최종 metadata와 preprint 제목/저자 목록을 구별한다. 이번 method 비교는 arXiv v1 지정 구간이며 최종 PDF 본문 전체 대조는 미실시다. 신규 registry 등록은 없고 C4/C6의 판단도 유지한다. [최초 검색 범위](../work/update/VLA_GAP_SCOUT_2026-10-23.md)는 당시 snapshot이다.

<a id="gap-wm-2026"></a>
### GAP-WM — VLA 후보 수·분포가 바뀐 뒤에도 world-model 선택을 믿을 수 있는가?

- 갱신: 2026-10-23, GAP-WM1. `CURATION-HYPOTHESIS`; **일반 방법 NO-GO / 조건부 진단 REVISE·HOLD**. [13편 비교·공개 source·재개 조건](../work/update/WORLD_MODEL_SELECTION_REVIEW_2026-10-23.md). 문헌 작업 완료와 native 효과를 구별한다.
- **직접 충돌:** [Cosmos Policy, ICLR 2026](https://iclr.cc/virtual/2026/poster/10006732)는 action/future/value 계획을, [VeriVLA §3](https://arxiv.org/html/2610.21985v1)는 adaptive sampling·latent verifier를 이미 다룬다. 고정 policy ranking은 dWorldEval/DreamTrue, 모델 오류 악용은 [planner overfitting](https://arxiv.org/abs/1812.01129)과 [Imperfect World Models](https://arxiv.org/html/2605.15960v2) 계보에 있다. 후보 평가·trigger·LCB 자체를 새 기여로 주장하지 않는다.
- **남은 질문 — 연구자 해석:** Frozen VLA·WM·scorer에서 calibration 이후 후보 수/분포를 바꿀 때 선택된 후보의 오류가 언제 커지는가? 평균 예측 오차와 다른 조건 예측이 새로운 task/proposal에도 통하는가? 유한 후보에서 역전이 필연적이거나 단조 증가한다고 전제하지 않는다. 이론의 transition TV를 pixel/latent error로 바꾸지 않는다.
- **최소 비교:** 같은 native state/controller와 실행 길이에서 nested 후보별 실제 outcome을 얻는다. 단일/무작위·작은 K·direct Q·mean/LCB·support 제한·짧은 예측 horizon을 비교한다. Policy 후보 수·WM/value 호출·denoising·wall time/control gap을 함께 센다. Calibration은 test 선택 전에 고정하고 task/proposal holdout을 둔다. Planner 계보와 frozen VLA의 interface 호환성이 확인되기 전 CEM/gradient를 즉시 구현하지 않는다.
- **증거 경계:** DreamTrue App C.2의 recorded-action 240개 조건부 비디오 평가는 모든 대안의 native outcome이 아니다. VeriVLA critical-state proxy도 추가 계산의 인과적 이득 oracle이 아니다. 후보 headroom·reward 오류·dynamics 오류·controller 불일치·latency를 분리한다. 단순 대안으로 설명되면 독립 method를 중단한다.
- **재개 조건:** 동일 상태의 후보–모델 점수–독립 실제 결과 packet과 단순 대안 이후 남는 예측이 필요하다. 공개 code 3개 revision을 정적으로 확인했으나 이 packet과 native 실행은 미확보다. Final dWorldEval 본문, robust MPC·선택 후 calibration 계보의 추가 감사도 방법 채택 전에 필요하다. GPU 확보나 같은 metadata 재검색만으로 재개하지 않는다. C4/C6·E2의 기존 판단은 유지한다.

<a id="gap-sysid-2026"></a>
### GAP-SYSID — 파라미터를 더 맞출 것인가, 모델의 상태·구조를 바꿀 것인가?

- 갱신: 2026-10-23. `CURATION-HYPOTHESIS`; system identification·sim-to-real·adaptive control 질문이다. Planning/control·RL·whole-body에서 교차 참조한다.
- **문제:** 마찰/질량 값이 틀린 경우와 actuator delay·접촉 이력 등 중요한 상태가 모델에서 빠진 경우는 다른 수정이 필요하다. 예측 잔차를 줄였다는 이유로 새 task에서의 control utility까지 확보됐다고 볼 수 없다.
- **직접 선행:** [SPI-Active, CoRL 2025](https://proceedings.mlr.press/v305/sobanbabu25a.html)은 parameter sampling과 Fisher-information 기반 명령 탐색을 이미 결합했다. [§7](https://arxiv.org/html/2505.14266v1)은 offline 동작, multi-behavior policy와 humanoid active exploration의 경계를 명시한다. [IROS 2025 online KF SysID](https://ieeexplore.ieee.org/document/11246753/)는 payload mass/COM을 online 보정한다. [ASTRA](https://pages.cs.wisc.edu/~gearless_joe/astra/)는 abstract state의 비-Markov성을 history로 다룬다(RA-L/IROS 2026은 저자 표기, 공식 status 재확인 필요). [RSS 2026 robust contact control](https://www.roboticsproceedings.org/rss22/p061.html)도 task-sensitive parameter uncertainty를 다룬다.
- **남은 질문 — 연구자 해석:** 제한된 calibration trajectory에서 residual이 비슷한 두 model family 중 어느 것이 새로운 command/contact에 충분한지 판별할 수 있는가? 추가 parameter 탐색을 중단하고 history/actuator 구조를 보강할 근거를 얻을 수 있는가? “task-aware ID”, “active ID”, “online adaptation” 자체는 차별점이 아니다.
- **최소 검증 설계:** parameter-only mismatch와 omitted-state/model-class mismatch를 구별 가능한 조건으로 만든다. 동일 interaction/force·시간 예산에서 passive ID, SPI류 active ID, KF/RLS, residual/history model, DR 및 oracle model을 비교한다. Calibration prediction error와 held-out control regret·constraint violation·probe cost를 별도로 측정한다. 동일 horizon/lag/input 정보의 baseline을 유지한다.
- **반증·기여 가능성:** 단순 delay 추정이나 history 하나로 결과가 설명되면 복잡한 model-selection method를 만들지 않는다. 잔차 기반 진단이 새로운 task에서 구조 오류를 가려내지 못하면 “언제 보정해야 하는가” 주장도 축소한다. 반대로 적은 interaction으로 불필요한 randomization/재학습을 줄이는 조건을 보여주면 식별/제어 사이의 재사용 가능한 지식이 된다.
- **GAP-W2에서 확인한 경계:** [ASTRA §III–IV·VI](https://arxiv.org/html/2604.15289v1)는 history와 task-relevant latent/reward prediction으로 non-Markov abstraction을 이미 보정하며 known state mapping·target trajectory를 요구한다. [SV-DRO §V-A3·VI](https://arxiv.org/html/2605.19029v1)는 parameter 정확도와 control 성공을 구별하면서 uncertainty class를 미리 알아야 하는 한계를 명시한다. 따라서 “잔차보다 task utility”, “누락 상태에 history를 더한다”는 일반 주장만으로 차별화할 수 없다.
- **현재 판단·재검토:** **REVISE / 진단 후보 HOLD**. [GAP-W2 직접 비교와 계약 초안](../work/update/GAP_W2_COMPARATIVE_REVIEW_2026-10-23.md)에 본문 3편과 SPI-Active의 고정 source/config를 기록했다. 공개 경로는 Isaac Gym/CUDA·controller checkpoint를 요구하고 replay/sim2real release가 일부 미완료다. 같은 관측·probe 예산에서 두 model family를 구분할 구체적 물리 사례가 필요하다. 간단한 lag/history 보정으로 설명되면 독립 method를 중단한다. 작은 반례도 새 Docker 실험에 해당하며 이번에는 실행하지 않았다. Native VLA 현상·자산은 미확보이고 일반 model-validation/dual-control 계보의 신규성 감사도 남는다.
