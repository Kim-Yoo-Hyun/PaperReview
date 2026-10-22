# World Models, Safety, and Recovery

- Updated: 2026-10-23 KST

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

### World models, uncertainty, failure detection, and recovery — 41

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
| NEXT | [FlowDreamer: A RGB-D World Model with Flow-based Motion Representations for Robot Manipulation](../2025/arXiv/2025_arXiv_FlowDreamer-A-RGB-D-World-Model-with-Flow-based-Motion-Rep/01_overview.md) | 2025 / arXiv | `UNREAD` | `FULL_TEXT_CHECKED` |
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

## Open Questions

현재 후보 판정은 [주제별 요약](../work/research_candidates/summaries/README.md)을 따른다. 아래 질문은 `CURATION-HYPOTHESIS`이며 재개 승인이 아니다.

| 질문 | 구별할 예측 | 최소 대조·중단 조건 | 근거/판정 |
|---|---|---|---|
| C4 reward의 downstream 효과 | 독립 outcome으로 측정한 policy ranking이 reward model/audit 선택 이후에도 유지되는가? | Versioned rollout·chronology·독립 evaluator·검수 비용이 없으면 정책 개선 주장 불가. 넓은 방법 NO-GO/진단 HOLD. | [검토 근거](../work/research_candidates/2026-10-21_c4_reward_audit/README.md) |
| C5 reset의 분모 | 성공·실패·retry·rescue 전체를 포함하면 coverage와 자율 학습 비용에 대한 결론이 달라지는가? | 성공 episode만 남은 자료로 reset 이득을 추정하지 않는다. Complete ledger 확보 전 HOLD. | [검토 근거](../work/research_candidates/2026-10-21_c5_reset_audit/README.md) |
| C6 선택 편향 | 동일 평가 예산에서 기존 sequential comparison보다 나은 독립 holdout 선택이 가능한가? | Trial-level data·정책 이력·독립 outcome 없이 best checkpoint 점수로 평가하지 않는다. 현재 독립 신규 방법 NO-GO. | [검토 근거](../work/research_candidates/2026-10-21_c6_checkpoint_audit/README.md) |
| World model·recovery | 동일 real rollout budget에서 fidelity/monitor score 개선이 실제 success·damage·intervention cost 개선을 예측하는가? | 모델 bias와 uncertainty calibration, human-video latent action의 contact/actuator 제약을 held-out 실제 실행에서 확인한다. Synthetic 성공은 대체 증거가 아니다. | 기존 track 비교의 연구자 질문; native 효과 미검증 |
