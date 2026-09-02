# World Models, Safety, and Recovery

- Updated: 2026-09-02 KST

## Scope

Latent dynamics, robot/human-video world models, synthetic experience generation, MPC, policy evaluation, uncertainty calibration, runtime failure detection, safety filtering과 recovery를 비교한다.

### Taxonomy boundary and curation schema

- **Primary axis:** state/world prediction → uncertainty or safety signal → policy/planning use → failure detection and recovery.
- **In scope:** robot world model, model-based policy improvement, safety constraint/filter, failure monitor, recovery policy와 correction benchmark가 closed-loop execution을 평가하는 경우.
- **Out of scope:** visual prediction만 있고 robot action conditioning·planning·safety interface가 없는 video model, 또는 일반적인 safety 논문으로 robot deployment contract를 확인할 수 없는 경우.
- **Inclusion test:** prediction target or safety signal, action conditioning, runtime use, failure/recovery behavior, evaluation consequence 중 최소 세 가지를 확인할 수 있어야 한다.
- **Role vocabulary:** `foundation`, `world model`, `policy optimizer`, `safety filter`, `detector`, `recovery policy`, `benchmark`, `evaluation protocol`, `system`을 사용한다.
- **Facet tuple:** `embodiment; modality/data; setting; runtime role; horizon`를 모든 matrix 행에 기록한다. 예: `arm; image+action; real/sim; detector; long-horizon`.
- **Comparison unit:** Comparison Matrix는 registry의 한 논문당 한 행이다. prediction/safety pair는 별도 행으로 나누고, dependency만 개념적 묶음을 허용한다.
- **Metadata/evidence:** Paper 링크의 local overview에 official paper, project/code와 source audit를 둔다. Matrix는 `Year / Venue`, `Role`, `Facets`, `Why included / TL;DR`, `Evidence / source`를 반복 기록하며, Evaluation은 `setup; data/split; metric; real/trials` 순서를 따른다.

## Reading Path

World Models/PlaNet/Dreamer → DayDreamer/TD-MPC2 → DreamGen/DreamDojo and physical/video-action world models → CBF/Recovery RL → SAFE/FLARE/FaultEval → calibrated world-model use.

<!-- READING_QUEUE:START -->

## Assigned Reading Queue

### Safety and robot world models — 5

| Tier | Paper | Year / Venue | Status | Evidence |
|---|---|---|---|---|
| CORE | [World Models](../2018/NeurIPS-Workshop/2018_NeurIPS-Workshop_World-Models/01_overview.md) | 2018 / NeurIPS Workshop | `UNREAD` | `FULL_TEXT_CHECKED` |
| CORE | [DayDreamer: World Models for Physical Robot Learning](../2022/CoRL/2022_CoRL_DayDreamer-World-Models-for-Physical-Robot-Learning/01_overview.md) | 2022 / CoRL | `UNREAD` | `FULL_TEXT_CHECKED` |
| CORE | [TD-MPC2: Scalable, Robust World Models for Continuous Control](../2024/ICLR/2024_ICLR_TD-MPC2-Scalable-Robust-World-Models-for-Continuous-Contro/01_overview.md) | 2024 / ICLR | `UNREAD` | `FULL_TEXT_CHECKED` |
| CORE | [Control Barrier Function Based Quadratic Programs for Safety Critical Systems](../2017/TAC/2017_TAC_Control-Barrier-Function-Based-Quadratic-Programs-for-Safe/01_overview.md) | 2017 / TAC | `UNREAD` | `FULL_TEXT_CHECKED` |
| CORE | [Recovery RL: Safe Reinforcement Learning with Learned Recovery Zones](../2020/RA-L/2020_RA-L_Recovery-RL-Safe-Reinforcement-Learning-with-Learned-Recov/01_overview.md) | 2020 / RA-L | `UNREAD` | `FULL_TEXT_CHECKED` |

### World models, uncertainty, failure detection, and recovery — 30

| Tier | Paper | Year / Venue | Status | Evidence |
|---|---|---|---|---|
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
| NEXT | [Can VLMs Diagnose and Recover from VLA Manipulation Faults?](../2026/ICML/2026_ICML_Can-VLMs-Diagnose-and-Recover-from-VLA-Manipulation-Faults/01_overview.md) | 2026 / ICML | `UNREAD` | `ABSTRACT_CHECKED` |
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

<!-- READING_QUEUE:END -->

## 2026-09-02 Curation Update

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

## Open Questions

- World model이 실제 환경에서 policy improvement를 잘못 유도하는 조건은 무엇인가?
- Runtime failure detection과 recovery를 비교할 때 latency, intervention cost, safety constraint를 어떻게 함께 고정할 것인가?
- Learned safety와 model-based constraints를 어떤 계층에서 결합해야 하는가?
- Human-video world model의 latent action이 robot contact와 actuator constraint를 보존하는지 어떤 matched task protocol로 검증할 것인가?
- Synthetic experience가 실제 policy improvement로 이어지는지 어떤 calibration과 held-out rollout으로 확인할 것인가?

## Research Gaps

- 통합 gap은 [G-02: detection→recovery](../research/RESEARCH_GAPS.md#g-02-detection에서-recovery까지-닫히지-않은-loop), [G-07: control fidelity](../research/RESEARCH_GAPS.md#g-07-world-model의-visual-fidelity와-control-fidelity-불일치), [G-08: imagined improvement calibration](../research/RESEARCH_GAPS.md#g-08-imagined-policy-improvement의-보수성과-calibration)을 본다.
- 이 문서에는 prediction target, uncertainty와 실제 closed-loop use를 정독 근거로 추가한다.
