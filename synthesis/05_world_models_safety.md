# World Models, Safety, and Recovery

- Updated: 2026-09-02 KST

## Scope

Latent dynamics, robot/human-video world models, synthetic experience generation, MPC, policy evaluation, uncertainty calibration, runtime failure detection, safety filtering과 recovery를 비교한다.

## Reading Path

World Models/PlaNet/Dreamer → DayDreamer/TD-MPC2 → DreamGen/DreamDojo and physical/video-action world models → CBF/Recovery RL → SAFE/FLARE → Agentic RL/ActFovea/ProbeAct → same-onset branch evaluation and calibrated world-model use.

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
| NEXT | [DreamGen: Unlocking Generalization in Robot Learning through Video World Models](../2025/CoRL/2025_CoRL_DreamGen-Unlocking-Generalization-in-Robot-Learning-throug/01_overview.md) | 2025 / CoRL | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [DreamDojo: A Generalist Robot World Model from Large-Scale Human Videos](../2026/ICML/2026_ICML_DreamDojo-A-Generalist-Robot-World-Model-from-Large-Scale/01_overview.md) | 2026 / ICML | `UNREAD` | `ABSTRACT_CHECKED` |
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
| NEXT | [Demonstrating ViSafe: Vision-enabled Safety for High-speed Detect and Avoid](../2025/RSS/2025_RSS_Demonstrating-ViSafe-Vision-enabled-Safety-for-High-speed/01_overview.md) | 2025 / RSS | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [Learned Perceptive Forward Dynamics Model for Safe and Platform-aware Robotic Navigation](../2025/RSS/2025_RSS_Learned-Perceptive-Forward-Dynamics-Model-for-Safe-and-Pla/01_overview.md) | 2025 / RSS | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [Certifiably-Correct Mapping for Safe Navigation Despite Odometry Drift](../2025/RSS/2025_RSS_Certifiably-Correct-Mapping-for-Safe-Navigation-Despite-Od/01_overview.md) | 2025 / RSS | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [Particle-Grid Neural Dynamics for Learning Deformable Object Models from RGB-D Videos](../2025/RSS/2025_RSS_Particle-Grid-Neural-Dynamics-for-Learning-Deformable-Obje/01_overview.md) | 2025 / RSS | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [Map Space Belief Prediction for Manipulation-Enhanced Mapping](../2025/RSS/2025_RSS_Map-Space-Belief-Prediction-for-Manipulation-Enhanced-Mapp/01_overview.md) | 2025 / RSS | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [Unified Video Action Model](../2025/RSS/2025_RSS_Unified-Video-Action-Model/01_overview.md) | 2025 / RSS | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [From Foresight to Forethought: VLM-In-the-Loop Policy Steering via Latent Alignment](../2025/RSS/2025_RSS_From-Foresight-to-Forethought-VLM-In-the-Loop-Policy-Steer/01_overview.md) | 2025 / RSS | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [Prompting with the Future: Open-World Model Predictive Control with Interactive Digital Twins](../2025/RSS/2025_RSS_Prompting-with-the-Future-Open-World-Model-Predictive-Cont/01_overview.md) | 2025 / RSS | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [Self-Correcting Robot Manipulation via Gaussian-Splatted Foresight](../2025/AAAI/2025_AAAI_Self-Correcting-Robot-Manipulation-via-Gaussian-Splatted-F/01_overview.md) | 2025 / AAAI | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [WMNav: Integrating Vision-Language Models into World Models for Object Goal Navigation](../2025/IROS/2025_IROS_WMNav-Integrating-Vision-Language-Models-into-World-Models/01_overview.md) | 2025 / IROS | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [RoboDreamer: Learning Compositional World Models for Robot Imagination](../2024/ICML/2024_ICML_RoboDreamer-Learning-Compositional-World-Models-for-Robot/01_overview.md) | 2024 / ICML | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [Learning Interactive Real-World Simulators](../2024/ICLR/2024_ICLR_Learning-Interactive-Real-World-Simulators/01_overview.md) | 2024 / ICLR | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [SafeMimic: Towards Safe and Autonomous Human-to-Robot Imitation for Mobile Manipulation](../2025/RSS/2025_RSS_SafeMimic-Towards-Safe-and-Autonomous-Human-to-Robot-Imita/01_overview.md) | 2025 / RSS | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [Ctrl-World: A Controllable Generative World Model for Robot Manipulation](../2026/ICLR/2026_ICLR_Ctrl-World-A-Controllable-Generative-World-Model-for-Robot/01_overview.md) | 2026 / ICLR | `UNREAD` | `FULL_TEXT_CHECKED` |

<!-- READING_QUEUE:END -->

## 2026-09-02 Curation Update

`WMNav`, `RoboDreamer`, `Learning Interactive Real-World Simulators`, `SafeMimic`, `Ctrl-World`를 `NEXT`에 반영했다. 이 queue는 world model을 reconstruction 결과가 아니라 action-conditioned prediction, policy evaluation/improvement, safety/recovery와 연결되는 폐루프 component로 다룬다. `Flow Equivariant World Models`는 action-conditioned foundation이지만 현재 검증된 real-robot evidence가 없어 `REFERENCE`에 유지했다.

## Comparison Matrix

> Matrix maturity: `CURATION-SEED`. 아래 행은 읽기 전 비교 가설이며 `READ`를 의미하지 않는다. 각 논문을 정독할 때 source location과 수치를 확인하고, 틀린 항목은 수정한 뒤 tracker를 갱신한다.

| Paper | World/state model | Prediction target | Action conditioning | Planning/policy use | Uncertainty/safety signal | Recovery mechanism | Robot/task | Evaluation | Failure mode | Reusable idea |
|---|---|---|---|---|---|---|---|---|---|---|
| [CBF-QP](../2017/TAC/2017_TAC_Control-Barrier-Function-Based-Quadratic-Programs-for-Safe/01_overview.md) | explicit system state and dynamics | safe-set invariance rather than visual future | nominal control filtered by QP | online safety filter | barrier value/constraint feasibility | corrective safe action from optimization | safety-critical control systems | constraint satisfaction and tracking; exact systems UNVERIFIED | dynamics/model mismatch and infeasible constraints | learned policy와 hard safety layer 분리 |
| [Recovery RL](../2020/RA-L/2020_RA-L_Recovery-RL-Safe-Reinforcement-Learning-with-Learned-Recov/01_overview.md) | learned risk/recovery-zone model | unsafe transition or recovery feasibility | task policy plus recovery policy | switch/filter unsafe actions | learned recovery/value signal | explicit learned recovery policy | continuous-control safety tasks | return, violations and recovery; exact protocol UNVERIFIED | coverage of unsafe boundary and switching errors | detector가 아니라 executable recovery를 학습 |
| [World Models](../2018/NeurIPS-Workshop/2018_NeurIPS-Workshop_World-Models/01_overview.md) → [DayDreamer](../2022/CoRL/2022_CoRL_DayDreamer-World-Models-for-Physical-Robot-Learning/01_overview.md) / [TD-MPC2](../2024/ICLR/2024_ICLR_TD-MPC2-Scalable-Robust-World-Models-for-Continuous-Contro/01_overview.md) | latent predictive state | future latent/reward/value | action-conditioned dynamics | imagination, planning or policy learning | model uncertainty mostly implicit or method-dependent | replanning/policy adaptation | simulated and physical continuous control | return, data efficiency and robot tasks | compounding error and model exploitation | prediction target를 control utility로 평가 |
| [DreamGen](../2025/CoRL/2025_CoRL_DreamGen-Unlocking-Generalization-in-Robot-Learning-throug/01_overview.md) / [DreamDojo](../2026/ICML/2026_ICML_DreamDojo-A-Generalist-Robot-World-Model-from-Large-Scale/01_overview.md) | generative video model for robot experience / generalist robot world model from human video | visual context with task/action or latent-action conditioning | generated future video/interaction and latent proxy actions | synthetic policy data, prediction, planning or evaluation | physical plausibility/control calibration not explicit in abstract | no direct recovery; supports policy training/evaluation/planning | manipulation and contact-rich open-world tasks | prediction/OOD and downstream utility; exact protocol UNVERIFIED | video/action inconsistency, human–robot embodiment mismatch and latency | generated data와 counterfactual rollout을 control-grounded filter로 선별 |
| [FAIL-Detect](../2025/RSS/2025_RSS_Can-We-Detect-Failures-Without-Failure-Data-Uncertainty-Aw/01_overview.md) / [SAFE](../2025/NeurIPS/2025_NeurIPS_SAFE-Multitask-Failure-Detection-for-Vision-Language-Actio/01_overview.md) | policy feature/trajectory monitor | runtime failure likelihood | conditioned on executed observation/action context | intervention trigger | uncertainty/conformal or learned failure score | detection only; recovery policy is separate | imitation/VLA manipulation | detection lead time, calibration and multitask transfer | false intervention and detector-to-action gap | failure-free calibration과 multitask monitoring 비교 |
| [Unified World Models](../2025/RSS/2025_RSS_Unified-World-Models-Coupling-Video-and-Action-Diffusion-f/01_overview.md) / [WMPO](../2026/ICLR/2026_ICLR_WMPO-World-Model-based-Policy-Optimization-for-Vision-Lang/01_overview.md) | joint video/action or policy-conditioned world model | visual/action future and policy value | candidate/policy action conditioned | pretraining, imagined evaluation or policy optimization | learned confidence/penalty; details UNVERIFIED | policy update rather than online recovery | robot manipulation/VLA | prediction and downstream policy improvement | visually plausible but action-wrong rollouts | imagined gain 대비 real gain calibration |
| [Agentic RL](https://arxiv.org/html/2607.13818v1) / [ActFovea](https://arxiv.org/abs/2607.29169) / [ProbeAct](https://arxiv.org/abs/2606.09740) | history-conditioned execution context / visual-action consistency / hidden-state probe | selected-mode return, verified observation, kinematic failure state | mode policy or bounded safety intervention | PPO manager / verification rule / training-free state machine+CBF | policy history, consistency score, probe/kinematics | Execute/Retry/Repair/Reset, re-observe/safe fail, safety correction | LIBERO/VLA manipulation | recovery success, safe failure, intervention; exact matched contract는 RP-2에서 재감사 | same-onset all-option supervision·vector-budget·best-fixed regret는 보고 primary protocol에서 확인되지 않음 | broad selector novelty를 닫고 RP-2 residual estimand를 정의 |


## Dependency and Evolution

아래 계보는 prediction model, policy optimization과 safety mechanism의 역할 변화를 구분한다. 직접 citation 관계는 정독 시 확인한다.

| Foundation → transition → frontier | 계승·변화 | 아직 확인할 경계 |
|---|---|---|
| [World Models](../2018/NeurIPS-Workshop/2018_NeurIPS-Workshop_World-Models/01_overview.md) → [PlaNet](../2019/ICML/2019_ICML_Learning-Latent-Dynamics-for-Planning-from-Pixels/01_overview.md) / [Dreamer](../2020/ICLR/2020_ICLR_Dream-to-Control-Learning-Behaviors-by-Latent-Imagination/01_overview.md) → [DayDreamer](../2022/CoRL/2022_CoRL_DayDreamer-World-Models-for-Physical-Robot-Learning/01_overview.md) / [TD-MPC2](../2024/ICLR/2024_ICLR_TD-MPC2-Scalable-Robust-World-Models-for-Continuous-Contro/01_overview.md) | compressed predictive state에서 latent planning과 imagination-based learning을 거쳐 physical robot online learning과 scalable continuous control로 확장된다. | real-world nonstationarity와 contact에서 horizon별 model error가 policy update를 언제 오도하는가 |
| [DDPM](../2020/NeurIPS/2020_NeurIPS_Denoising-Diffusion-Probabilistic-Models/01_overview.md) / action diffusion → [Unified World Models](../2025/RSS/2025_RSS_Unified-World-Models-Coupling-Video-and-Action-Diffusion-f/01_overview.md) → [WMPO](../2026/ICLR/2026_ICLR_WMPO-World-Model-based-Policy-Optimization-for-Vision-Lang/01_overview.md) | policy, forward/inverse dynamics와 video generation을 공동 모델링하고 imagined rollout을 VLA policy optimization에 사용한다. | video likelihood가 action ranking과 real policy improvement에 충분한가; model exploitation을 어떻게 제한하는가 |
| large-scale human/robot video → [DreamGen](../2025/CoRL/2025_CoRL_DreamGen-Unlocking-Generalization-in-Robot-Learning-throug/01_overview.md) → [DreamDojo](../2026/ICML/2026_ICML_DreamDojo-A-Generalist-Robot-World-Model-from-Large-Scale/01_overview.md) → policy evaluation/model-based planning | robot-domain synthetic experience 생성에서 human-video latent action pretraining과 real-time robot-centric prediction으로 확장된다. | unlabeled human interaction의 latent action이 robot actuation, contact outcome와 counterfactual option value를 보존하는가 |
| learned world model → [PIN-WM](../2025/RSS/2025_RSS_PIN-WM-Learning-Physics-INformed-World-Models-for-Non-Preh/01_overview.md) / [Dexterous World Models](../2026/CVPR/2026_CVPR_Dexterous-World-Models/01_overview.md) | generic latent/video prediction에 task-relevant physical structure와 dexterous contact dynamics를 넣는 방향이다. | physics prior가 어떤 contact regime에서 generalization을 돕고 언제 model bias를 키우는가 |
| [Control Barrier Function QP](../2017/TAC/2017_TAC_Control-Barrier-Function-Based-Quadratic-Programs-for-Safe/01_overview.md) → [Recovery RL](../2020/RA-L/2020_RA-L_Recovery-RL-Safe-Reinforcement-Learning-with-Learned-Recov/01_overview.md) → [FAIL-Detect](../2025/RSS/2025_RSS_Can-We-Detect-Failures-Without-Failure-Data-Uncertainty-Aw/01_overview.md) / [SAFE](../2025/NeurIPS/2025_NeurIPS_SAFE-Multitask-Failure-Detection-for-Vision-Language-Actio/01_overview.md) → [FLARE](../2026/CVPR/2026_CVPR_FLARE-A-Failure-Aware-Framework-for-Autonomous-Correction/01_overview.md) / [VLA-FixBench/FaultEval](../2026/ICML/2026_ICML_Can-VLMs-Diagnose-and-Recover-from-VLA-Manipulation-Faults/01_overview.md) → [Agentic RL](https://arxiv.org/html/2607.13818v1) / [ActFovea](https://arxiv.org/abs/2607.29169) / [ProbeAct](https://arxiv.org/abs/2606.09740) | constraint·recovery zone에서 alert, diagnosis, binary correction을 거쳐 learned execution-mode manager, verified observation recovery와 safety net으로 확장된다. | cloned same-onset all-option table이 direct mode policy와 simple mechanism control을 넘어서는가 |
| [MomaGraph](../2026/ICLR/2026_ICLR_MomaGraph-State-Aware-Unified-Scene-Graphs-with-Vision-Lan/01_overview.md) / [Spatial Memory](../2026/ICML/2026_ICML_Spatial-Memory-for-Out-of-Vision-Manipulation-in-Vision-La/01_overview.md) → [Memory Retrieval/HALO](../2026/RSS/2026_RSS_Memory-Retrieval-in-Visuomotor-Policies-for-Long-Horizon-R/01_overview.md) | explicit state graph와 out-of-view memory에서 task-relevant sparse retrieval과 long-horizon drift mitigation으로 이동한다. | stale memory를 expire/reobserve할 calibrated rule과 safety outcome이 있는가 |

## Open Questions

- World model이 실제 환경에서 policy improvement를 잘못 유도하는 조건은 무엇인가?
- Agentic RL식 mode policy와 ActFovea/ProbeAct식 direct mechanism을 넘어 all-option full-information supervision이 필요한 failure/budget regime는 무엇인가?
- Learned safety와 model-based constraints를 어떤 계층에서 결합해야 하는가?
- Human-video world model의 latent action이 robot contact와 actuator constraint를 보존하는지 어떤 same-state intervention으로 검증할 것인가?
- Synthetic experience의 양보다 option ranking·calibration·worst-group control utility를 우선하는 selection rule은 무엇인가?

## Research Gaps

- 통합 gap은 [G-02: detection→recovery](../research/RESEARCH_GAPS.md#g-02-detection에서-recovery까지-닫히지-않은-loop), [G-07: control fidelity](../research/RESEARCH_GAPS.md#g-07-world-model의-visual-fidelity와-control-fidelity-불일치), [G-08: imagined improvement calibration](../research/RESEARCH_GAPS.md#g-08-imagined-policy-improvement의-보수성과-calibration)을 본다.
- 이 문서에는 prediction target, uncertainty와 실제 closed-loop use를 정독 근거로 추가한다.
