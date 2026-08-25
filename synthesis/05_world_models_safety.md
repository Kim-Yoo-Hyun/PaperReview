# World Models, Safety, and Recovery

## Scope

Latent dynamics, video/action world models, MPC, policy evaluation, uncertainty calibration, runtime failure detection, safety filtering과 recovery를 비교한다.

## Reading Path

World Models/PlaNet/Dreamer → DayDreamer/TD-MPC2 → physical and video-action world models → CBF/Recovery RL → SAFE/WorldGym/WMPO/counterfactual recovery.

<!-- READING_QUEUE:START -->

## Assigned Reading Queue

### Safety and robot world models — 5

| Tier | Paper | Year / Venue | Status | Evidence |
|---|---|---|---|---|
| CORE | [World Models](../2018/NeurIPS-Workshop/2018_NeurIPS-Workshop_World-Models/01_overview.md) | 2018 / NeurIPS Workshop | `UNREAD` | `CURATION_ONLY` |
| CORE | [DayDreamer: World Models for Physical Robot Learning](../2022/CoRL/2022_CoRL_DayDreamer-World-Models-for-Physical-Robot-Learning/01_overview.md) | 2022 / CoRL | `UNREAD` | `CURATION_ONLY` |
| CORE | [TD-MPC2: Scalable, Robust World Models for Continuous Control](../2024/ICLR/2024_ICLR_TD-MPC2-Scalable-Robust-World-Models-for-Continuous-Contro/01_overview.md) | 2024 / ICLR | `UNREAD` | `CURATION_ONLY` |
| CORE | [Control Barrier Function Based Quadratic Programs for Safety Critical Systems](../2017/TAC/2017_TAC_Control-Barrier-Function-Based-Quadratic-Programs-for-Safe/01_overview.md) | 2017 / TAC | `UNREAD` | `CURATION_ONLY` |
| CORE | [Recovery RL: Safe Reinforcement Learning with Learned Recovery Zones](../2020/RA-L/2020_RA-L_Recovery-RL-Safe-Reinforcement-Learning-with-Learned-Recov/01_overview.md) | 2020 / RA-L | `UNREAD` | `CURATION_ONLY` |

### World models, uncertainty, failure detection, and recovery — 14

| Tier | Paper | Year / Venue | Status | Evidence |
|---|---|---|---|---|
| NEXT | [Learning Latent Dynamics for Planning from Pixels](../2019/ICML/2019_ICML_Learning-Latent-Dynamics-for-Planning-from-Pixels/01_overview.md) | 2019 / ICML | `UNREAD` | `CURATION_ONLY` |
| NEXT | [Dream to Control: Learning Behaviors by Latent Imagination](../2020/ICLR/2020_ICLR_Dream-to-Control-Learning-Behaviors-by-Latent-Imagination/01_overview.md) | 2020 / ICLR | `UNREAD` | `CURATION_ONLY` |
| NEXT | [Mastering Diverse Domains through World Models](../2025/Nature/2025_Nature_Mastering-Diverse-Domains-through-World-Models/01_overview.md) | 2025 / Nature | `UNREAD` | `CURATION_ONLY` |
| NEXT | [PIN-WM: Learning Physics-INformed World Models for Non-Prehensile Manipulation](../2025/RSS/2025_RSS_PIN-WM-Learning-Physics-INformed-World-Models-for-Non-Preh/01_overview.md) | 2025 / RSS | `UNREAD` | `CURATION_ONLY` |
| NEXT | [Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets](../2025/RSS/2025_RSS_Unified-World-Models-Coupling-Video-and-Action-Diffusion-f/01_overview.md) | 2025 / RSS | `UNREAD` | `CURATION_ONLY` |
| NEXT | [FlowDreamer: A RGB-D World Model with Flow-based Motion Representations for Robot Manipulation](../2025/arXiv/2025_arXiv_FlowDreamer-A-RGB-D-World-Model-with-Flow-based-Motion-Rep/01_overview.md) | 2025 / arXiv | `UNREAD` | `CURATION_ONLY` |
| NEXT | [Can We Detect Failures Without Failure Data? Uncertainty-Aware Runtime Failure Detection for Imitation Learning Policies](../2025/RSS/2025_RSS_Can-We-Detect-Failures-Without-Failure-Data-Uncertainty-Aw/01_overview.md) | 2025 / RSS | `UNREAD` | `CURATION_ONLY` |
| NEXT | [SAFE: Multitask Failure Detection for Vision-Language-Action Models](../2025/NeurIPS/2025_NeurIPS_SAFE-Multitask-Failure-Detection-for-Vision-Language-Actio/01_overview.md) | 2025 / NeurIPS | `UNREAD` | `CURATION_ONLY` |
| NEXT | [WorldGym: World Model as An Environment for Policy Evaluation](../2026/ICLR/2026_ICLR_WorldGym-World-Model-as-An-Environment-for-Policy-Evaluati/01_overview.md) | 2026 / ICLR | `UNREAD` | `CURATION_ONLY` |
| NEXT | [WMPO: World Model-based Policy Optimization for Vision-Language-Action Models](../2026/ICLR/2026_ICLR_WMPO-World-Model-based-Policy-Optimization-for-Vision-Lang/01_overview.md) | 2026 / ICLR Poster | `UNREAD` | `CURATION_ONLY` |
| NEXT | [FLARE: A Failure-Aware Framework for Autonomous Correction and Recovery in Visual-Language Robotic Manipulation](../2026/CVPR/2026_CVPR_FLARE-A-Failure-Aware-Framework-for-Autonomous-Correction/01_overview.md) | 2026 / CVPR | `UNREAD` | `CURATION_ONLY` |
| NEXT | [Can VLMs Diagnose and Recover from VLA Manipulation Faults?](../2026/ICML/2026_ICML_Can-VLMs-Diagnose-and-Recover-from-VLA-Manipulation-Faults/01_overview.md) | 2026 / ICML | `UNREAD` | `CURATION_ONLY` |
| NEXT | [Temporal Difference Calibration in Sequential Tasks: Application to Vision-Language-Action Models](../2026/ICML/2026_ICML_Temporal-Difference-Calibration-in-Sequential-Tasks-Applic/01_overview.md) | 2026 / ICML | `UNREAD` | `CURATION_ONLY` |
| NEXT | [Memory Retrieval in Visuomotor Policies for Long-Horizon Robot Control](../2026/RSS/2026_RSS_Memory-Retrieval-in-Visuomotor-Policies-for-Long-Horizon-R/01_overview.md) | 2026 / RSS | `UNREAD` | `CURATION_ONLY` |

<!-- READING_QUEUE:END -->

## Comparison Matrix

> Matrix maturity: `CURATION-SEED`. 아래 행은 읽기 전 비교 가설이며 `READ`를 의미하지 않는다. 각 논문을 정독할 때 source location과 수치를 확인하고, 틀린 항목은 수정한 뒤 tracker를 갱신한다.

| Paper | World/state model | Prediction target | Action conditioning | Planning/policy use | Uncertainty/safety signal | Recovery mechanism | Robot/task | Evaluation | Failure mode | Reusable idea |
|---|---|---|---|---|---|---|---|---|---|---|
| [CBF-QP](../2017/TAC/2017_TAC_Control-Barrier-Function-Based-Quadratic-Programs-for-Safe/01_overview.md) | explicit system state and dynamics | safe-set invariance rather than visual future | nominal control filtered by QP | online safety filter | barrier value/constraint feasibility | corrective safe action from optimization | safety-critical control systems | constraint satisfaction and tracking; exact systems UNVERIFIED | dynamics/model mismatch and infeasible constraints | learned policy와 hard safety layer 분리 |
| [Recovery RL](../2020/RA-L/2020_RA-L_Recovery-RL-Safe-Reinforcement-Learning-with-Learned-Recov/01_overview.md) | learned risk/recovery-zone model | unsafe transition or recovery feasibility | task policy plus recovery policy | switch/filter unsafe actions | learned recovery/value signal | explicit learned recovery policy | continuous-control safety tasks | return, violations and recovery; exact protocol UNVERIFIED | coverage of unsafe boundary and switching errors | detector가 아니라 executable recovery를 학습 |
| [World Models](../2018/NeurIPS-Workshop/2018_NeurIPS-Workshop_World-Models/01_overview.md) → [DayDreamer](../2022/CoRL/2022_CoRL_DayDreamer-World-Models-for-Physical-Robot-Learning/01_overview.md) / [TD-MPC2](../2024/ICLR/2024_ICLR_TD-MPC2-Scalable-Robust-World-Models-for-Continuous-Contro/01_overview.md) | latent predictive state | future latent/reward/value | action-conditioned dynamics | imagination, planning or policy learning | model uncertainty mostly implicit or method-dependent | replanning/policy adaptation | simulated and physical continuous control | return, data efficiency and robot tasks | compounding error and model exploitation | prediction target를 control utility로 평가 |
| [FAIL-Detect](../2025/RSS/2025_RSS_Can-We-Detect-Failures-Without-Failure-Data-Uncertainty-Aw/01_overview.md) / [SAFE](../2025/NeurIPS/2025_NeurIPS_SAFE-Multitask-Failure-Detection-for-Vision-Language-Actio/01_overview.md) | policy feature/trajectory monitor | runtime failure likelihood | conditioned on executed observation/action context | intervention trigger | uncertainty/conformal or learned failure score | detection only; recovery policy is separate | imitation/VLA manipulation | detection lead time, calibration and multitask transfer | false intervention and detector-to-action gap | failure-free calibration과 multitask monitoring 비교 |
| [Unified World Models](../2025/RSS/2025_RSS_Unified-World-Models-Coupling-Video-and-Action-Diffusion-f/01_overview.md) / [WMPO](../2026/ICLR/2026_ICLR_WMPO-World-Model-based-Policy-Optimization-for-Vision-Lang/01_overview.md) | joint video/action or policy-conditioned world model | visual/action future and policy value | candidate/policy action conditioned | pretraining, imagined evaluation or policy optimization | learned confidence/penalty; details UNVERIFIED | policy update rather than online recovery | robot manipulation/VLA | prediction and downstream policy improvement | visually plausible but action-wrong rollouts | imagined gain 대비 real gain calibration |


## Dependency and Evolution

아래 계보는 prediction model, policy optimization과 safety mechanism의 역할 변화를 구분한다. 직접 citation 관계는 정독 시 확인한다.

| Foundation → transition → frontier | 계승·변화 | 아직 확인할 경계 |
|---|---|---|
| [World Models](../2018/NeurIPS-Workshop/2018_NeurIPS-Workshop_World-Models/01_overview.md) → [PlaNet](../2019/ICML/2019_ICML_Learning-Latent-Dynamics-for-Planning-from-Pixels/01_overview.md) / [Dreamer](../2020/ICLR/2020_ICLR_Dream-to-Control-Learning-Behaviors-by-Latent-Imagination/01_overview.md) → [DayDreamer](../2022/CoRL/2022_CoRL_DayDreamer-World-Models-for-Physical-Robot-Learning/01_overview.md) / [TD-MPC2](../2024/ICLR/2024_ICLR_TD-MPC2-Scalable-Robust-World-Models-for-Continuous-Contro/01_overview.md) | compressed predictive state에서 latent planning과 imagination-based learning을 거쳐 physical robot online learning과 scalable continuous control로 확장된다. | real-world nonstationarity와 contact에서 horizon별 model error가 policy update를 언제 오도하는가 |
| [DDPM](../2020/NeurIPS/2020_NeurIPS_Denoising-Diffusion-Probabilistic-Models/01_overview.md) / action diffusion → [Unified World Models](../2025/RSS/2025_RSS_Unified-World-Models-Coupling-Video-and-Action-Diffusion-f/01_overview.md) → [WMPO](../2026/ICLR/2026_ICLR_WMPO-World-Model-based-Policy-Optimization-for-Vision-Lang/01_overview.md) | policy, forward/inverse dynamics와 video generation을 공동 모델링하고 imagined rollout을 VLA policy optimization에 사용한다. | video likelihood가 action ranking과 real policy improvement에 충분한가; model exploitation을 어떻게 제한하는가 |
| learned world model → [PIN-WM](../2025/RSS/2025_RSS_PIN-WM-Learning-Physics-INformed-World-Models-for-Non-Preh/01_overview.md) / [Dexterous World Models](../2026/CVPR/2026_CVPR_Dexterous-World-Models/01_overview.md) | generic latent/video prediction에 task-relevant physical structure와 dexterous contact dynamics를 넣는 방향이다. | physics prior가 어떤 contact regime에서 generalization을 돕고 언제 model bias를 키우는가 |
| [Control Barrier Function QP](../2017/TAC/2017_TAC_Control-Barrier-Function-Based-Quadratic-Programs-for-Safe/01_overview.md) → [Recovery RL](../2020/RA-L/2020_RA-L_Recovery-RL-Safe-Reinforcement-Learning-with-Learned-Recov/01_overview.md) → [FAIL-Detect](../2025/RSS/2025_RSS_Can-We-Detect-Failures-Without-Failure-Data-Uncertainty-Aw/01_overview.md) / [SAFE](../2025/NeurIPS/2025_NeurIPS_SAFE-Multitask-Failure-Detection-for-Vision-Language-Actio/01_overview.md) → [WorldGym](../2026/ICLR/2026_ICLR_WorldGym-World-Model-as-An-Environment-for-Policy-Evaluati/01_overview.md) | model-based constraint enforcement와 learned recovery zone에서 failure-free calibration, generalist-policy monitoring 및 world-model evaluation으로 범위가 넓어진다. | detection·offline evaluation을 intervention과 recovery action 선택까지 어떻게 연결할 것인가 |
| [Control Barrier Function QP](../2017/TAC/2017_TAC_Control-Barrier-Function-Based-Quadratic-Programs-for-Safe/01_overview.md) → [Recovery RL](../2020/RA-L/2020_RA-L_Recovery-RL-Safe-Reinforcement-Learning-with-Learned-Recov/01_overview.md) → [FAIL-Detect](../2025/RSS/2025_RSS_Can-We-Detect-Failures-Without-Failure-Data-Uncertainty-Aw/01_overview.md) / [SAFE](../2025/NeurIPS/2025_NeurIPS_SAFE-Multitask-Failure-Detection-for-Vision-Language-Actio/01_overview.md) → [FLARE](../2026/CVPR/2026_CVPR_FLARE-A-Failure-Aware-Framework-for-Autonomous-Correction/01_overview.md) / [VLA-FixBench/FaultEval](../2026/ICML/2026_ICML_Can-VLMs-Diagnose-and-Recover-from-VLA-Manipulation-Faults/01_overview.md) / [Temporal Difference Calibration](../2026/ICML/2026_ICML_Temporal-Difference-Calibration-in-Sequential-Tasks-Applic/01_overview.md) → [WorldGym](../2026/ICLR/2026_ICLR_WorldGym-World-Model-as-An-Environment-for-Policy-Evaluati/01_overview.md) | model-based constraint enforcement와 learned recovery zone에서 failure calibration, binary recovery, diagnosis/rollback benchmark, sequential confidence 및 world-model evaluation으로 범위가 넓어진다. | detection·offline evaluation을 intervention과 multi-option recovery 선택까지 어떻게 연결할 것인가 |
| [MomaGraph](../2026/ICLR/2026_ICLR_MomaGraph-State-Aware-Unified-Scene-Graphs-with-Vision-Lan/01_overview.md) / [Spatial Memory](../2026/ICML/2026_ICML_Spatial-Memory-for-Out-of-Vision-Manipulation-in-Vision-La/01_overview.md) → [Memory Retrieval/HALO](../2026/RSS/2026_RSS_Memory-Retrieval-in-Visuomotor-Policies-for-Long-Horizon-R/01_overview.md) | explicit state graph와 out-of-view memory에서 task-relevant sparse retrieval과 long-horizon drift mitigation으로 이동한다. | stale memory를 expire/reobserve할 calibrated rule과 safety outcome이 있는가 |

## Open Questions

- World model이 실제 환경에서 policy improvement를 잘못 유도하는 조건은 무엇인가?
- Failure detection의 confidence를 recovery action 선택에 어떻게 연결할 것인가?
- Learned safety와 model-based constraints를 어떤 계층에서 결합해야 하는가?

## Research Gaps

- 통합 gap은 [G-02: detection→recovery](../research/RESEARCH_GAPS.md#g-02-detection에서-recovery까지-닫히지-않은-loop), [G-07: control fidelity](../research/RESEARCH_GAPS.md#g-07-world-model의-visual-fidelity와-control-fidelity-불일치), [G-08: imagined improvement calibration](../research/RESEARCH_GAPS.md#g-08-imagined-policy-improvement의-보수성과-calibration)을 본다.
- 이 문서에는 prediction target, uncertainty와 실제 closed-loop use를 정독 근거로 추가한다.
