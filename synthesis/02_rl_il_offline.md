# RL, IL, Offline Learning, and Robot Data

## Scope

Online RL, offline RL, imitation learning, inverse/reward learning, sequence modeling, diffusion policy, demonstration generation과 data curation을 비교한다.

## Reading Path

DAgger/GAIL → RoboMimic/RLBench → TRPO/PPO/SAC → IQL/CQL/Q-Transformer → DDPM/Flow Matching → Diffusion Policy/π0 → MimicGen/DROID/cross-embodiment data.

<!-- READING_QUEUE:START -->

## Assigned Reading Queue

### RL, IL, and policy learning foundations — 15

| Tier | Paper | Year / Venue | Status | Evidence |
|---|---|---|---|---|
| CORE | [A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning](../2011/AISTATS/2011_AISTATS_A-Reduction-of-Imitation-Learning-and-Structured-Predictio/01_overview.md) | 2011 / AISTATS | `UNREAD` | `CURATION_ONLY` |
| CORE | [Learning Neural Network Policies with Guided Policy Search under Unknown Dynamics](../2016/JMLR/2016_JMLR_Learning-Neural-Network-Policies-with-Guided-Policy-Search/01_overview.md) | 2016 / JMLR | `UNREAD` | `CURATION_ONLY` |
| CORE | [Generative Adversarial Imitation Learning](../2016/NeurIPS/2016_NeurIPS_Generative-Adversarial-Imitation-Learning/01_overview.md) | 2016 / NeurIPS | `UNREAD` | `CURATION_ONLY` |
| CORE | [Trust Region Policy Optimization](../2015/ICML/2015_ICML_Trust-Region-Policy-Optimization/01_overview.md) | 2015 / ICML | `UNREAD` | `CURATION_ONLY` |
| CORE | [Proximal Policy Optimization Algorithms](../2017/arxiv/2017_arxiv_Proximal-Policy-Optimization-Algorithms/01_overview.md) | 2017 / arxiv | `UNREAD` | `CURATION_ONLY` |
| CORE | [Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor](../2018/ICML/2018_ICML_Soft-Actor-Critic-Off-Policy-Maximum-Entropy-Deep-Reinforc/01_overview.md) | 2018 / ICML | `UNREAD` | `CURATION_ONLY` |
| CORE | [Domain Randomization for Transferring Deep Neural Networks from Simulation to the Real World](../2017/IROS/2017_IROS_Domain-Randomization-for-Transferring-Deep-Neural-Networks/01_overview.md) | 2017 / IROS | `UNREAD` | `CURATION_ONLY` |
| CORE | [What Matters in Learning from Offline Human Demonstrations for Robot Manipulation](../2021/CoRL/2021_CoRL_What-Matters-in-Learning-from-Offline-Human-Demonstrations/01_overview.md) | 2021 / CoRL | `UNREAD` | `CURATION_ONLY` |
| CORE | [Implicit Behavioral Cloning](../2022/CoRL/2022_CoRL_Implicit-Behavioral-Cloning/01_overview.md) | 2022 / CoRL | `UNREAD` | `CURATION_ONLY` |
| CORE | [Offline Reinforcement Learning with Implicit Q-Learning](../2022/ICLR/2022_ICLR_Offline-Reinforcement-Learning-with-Implicit-Q-Learning/01_overview.md) | 2022 / ICLR | `UNREAD` | `CURATION_ONLY` |
| CORE | [Decision Transformer: Reinforcement Learning via Sequence Modeling](../2021/NeurIPS/2021_NeurIPS_Decision-Transformer-Reinforcement-Learning-via-Sequence-M/01_overview.md) | 2021 / NeurIPS | `UNREAD` | `CURATION_ONLY` |
| CORE | [Denoising Diffusion Probabilistic Models](../2020/NeurIPS/2020_NeurIPS_Denoising-Diffusion-Probabilistic-Models/01_overview.md) | 2020 / NeurIPS | `UNREAD` | `CURATION_ONLY` |
| CORE | [Flow Matching for Generative Modeling](../2023/ICLR/2023_ICLR_Flow-Matching-for-Generative-Modeling/01_overview.md) | 2023 / ICLR | `UNREAD` | `CURATION_ONLY` |
| CORE | [Diffusion Policy: Visuomotor Policy Learning via Action Diffusion](../2023/RSS/2023_RSS_Diffusion-Policy-Visuomotor-Policy-Learning-via-Action-Dif/01_overview.md) | 2023 / RSS | `UNREAD` | `CURATION_ONLY` |
| CORE | [Q-Transformer: Scalable Offline Reinforcement Learning via Autoregressive Q-Functions](../2024/CoRL/2024_CoRL_Q-Transformer-Scalable-Offline-Reinforcement-Learning-via/01_overview.md) | 2024 / CoRL | `UNREAD` | `CURATION_ONLY` |

### RL, IL, offline learning, and robot data — 13

| Tier | Paper | Year / Venue | Status | Evidence |
|---|---|---|---|---|
| NEXT | [Continuous Control with Deep Reinforcement Learning](../2016/ICLR/2016_ICLR_Continuous-Control-with-Deep-Reinforcement-Learning/01_overview.md) | 2016 / ICLR | `UNREAD` | `CURATION_ONLY` |
| NEXT | [Addressing Function Approximation Error in Actor-Critic Methods](../2018/ICML/2018_ICML_Addressing-Function-Approximation-Error-in-Actor-Critic-Me/01_overview.md) | 2018 / ICML | `UNREAD` | `CURATION_ONLY` |
| NEXT | [Hindsight Experience Replay](../2017/NeurIPS/2017_NeurIPS_Hindsight-Experience-Replay/01_overview.md) | 2017 / NeurIPS | `UNREAD` | `CURATION_ONLY` |
| NEXT | [Constrained Policy Optimization](../2017/ICML/2017_ICML_Constrained-Policy-Optimization/01_overview.md) | 2017 / ICML | `UNREAD` | `CURATION_ONLY` |
| NEXT | [Conservative Q-Learning for Offline Reinforcement Learning](../2020/NeurIPS/2020_NeurIPS_Conservative-Q-Learning-for-Offline-Reinforcement-Learning/01_overview.md) | 2020 / NeurIPS | `UNREAD` | `CURATION_ONLY` |
| NEXT | [MOPO: Model-based Offline Policy Optimization](../2020/NeurIPS/2020_NeurIPS_MOPO-Model-based-Offline-Policy-Optimization/01_overview.md) | 2020 / NeurIPS | `UNREAD` | `CURATION_ONLY` |
| NEXT | [A Minimalist Approach to Offline Reinforcement Learning](../2021/NeurIPS/2021_NeurIPS_A-Minimalist-Approach-to-Offline-Reinforcement-Learning/01_overview.md) | 2021 / NeurIPS | `UNREAD` | `CURATION_ONLY` |
| NEXT | [Learning Complex Dexterous Manipulation with Deep Reinforcement Learning and Demonstrations](../2018/RSS/2018_RSS_Learning-Complex-Dexterous-Manipulation-with-Deep-Reinforc/01_overview.md) | 2018 / RSS | `UNREAD` | `CURATION_ONLY` |
| NEXT | [Learning Latent Plans from Play](../2020/CoRL/2020_CoRL_Learning-Latent-Plans-from-Play/01_overview.md) | 2020 / CoRL | `UNREAD` | `CURATION_ONLY` |
| NEXT | [Relay Policy Learning: Solving Long-Horizon Tasks via Imitation and Reinforcement Learning](../2020/CoRL/2020_CoRL_Relay-Policy-Learning-Solving-Long-Horizon-Tasks-via-Imita/01_overview.md) | 2020 / CoRL | `UNREAD` | `CURATION_ONLY` |
| NEXT | [RLBench: The Robot Learning Benchmark & Learning Environment](../2020/RA-L/2020_RA-L_RLBench-The-Robot-Learning-Benchmark-and-Learning-Environm/01_overview.md) | 2020 / RA-L | `UNREAD` | `CURATION_ONLY` |
| NEXT | [MimicGen: A Data Generation System for Scalable Robot Learning using Human Demonstrations](../2023/CoRL/2023_CoRL_MimicGen-A-Data-Generation-System-for-Scalable-Robot-Learn/01_overview.md) | 2023 / CoRL | `UNREAD` | `CURATION_ONLY` |
| NEXT | [DROID: A Large-Scale In-The-Wild Robot Manipulation Dataset](../2024/RSS/2024_RSS_DROID-A-Large-Scale-In-The-Wild-Robot-Manipulation-Dataset/01_overview.md) | 2024 / RSS | `UNREAD` | `CURATION_ONLY` |

<!-- READING_QUEUE:END -->

## Comparison Matrix

> Matrix maturity: `CURATION-SEED`. 아래 행은 읽기 전 비교 가설이며 `READ`를 의미하지 않는다. 각 논문을 정독할 때 source location과 수치를 확인하고, 틀린 항목은 수정한 뒤 tracker를 갱신한다.

| Paper | Learning setting | Observation/state | Action representation | Objective | Data source/scale | Online interaction | Robot/task | Generalization | Failure mode | Reusable idea |
|---|---|---|---|---|---|---|---|---|---|---|
| [DAgger](../2011/AISTATS/2011_AISTATS_A-Reduction-of-Imitation-Learning-and-Structured-Predictio/01_overview.md) | interactive imitation learning | task state/observation | expert-labeled action | no-regret reduction under learner state distribution | iteratively aggregated expert data | required during training | sequential decision tasks | state-distribution shift | expert query cost and unsafe learner rollouts | intervention-triggered robot data collection |
| [RoboMimic](../2021/CoRL/2021_CoRL_What-Matters-in-Learning-from-Offline-Human-Demonstrations/01_overview.md) / [RLBench](../2020/RA-L/2020_RA-L_RLBench-The-Robot-Learning-Benchmark-and-Learning-Environm/01_overview.md) | offline imitation benchmark / multi-task environment | low-dimensional state and/or vision | continuous manipulation action | behavior cloning family and benchmark comparison | human demonstrations / simulated task suite | none for offline training | tabletop manipulation | task, modality and demonstration-quality splits | benchmark-to-real gap and confounded implementation choices | reproducible data/evaluation substrate |
| [PPO](../2017/arxiv/2017_arxiv_Proximal-Policy-Optimization-Algorithms/01_overview.md) / [SAC](../2018/ICML/2018_ICML_Soft-Actor-Critic-Off-Policy-Maximum-Entropy-Deep-Reinforc/01_overview.md) | on-policy / off-policy RL | Markov state or observation | stochastic continuous/discrete policy | clipped policy update / maximum-entropy actor-critic | simulator or environment interaction | substantial | control and locomotion backbones | dynamics randomization and new tasks are downstream uses | reward design, sample cost and sim bias | stable optimization baselines for motor learning |
| [CQL](../2020/NeurIPS/2020_NeurIPS_Conservative-Q-Learning-for-Offline-Reinforcement-Learning/01_overview.md) / [IQL](../2022/ICLR/2022_ICLR_Offline-Reinforcement-Learning-with-Implicit-Q-Learning/01_overview.md) | offline RL | logged state-action transitions | policy induced from learned value/Q | conservative Q regularization / implicit value learning | fixed mixed-quality datasets | none during training | offline control and robot data | OOD action and dataset shift | over-conservatism or extrapolation / support mismatch | failure data를 value-aware하게 재사용 |
| [DDPM](../2020/NeurIPS/2020_NeurIPS_Denoising-Diffusion-Probabilistic-Models/01_overview.md) / [Flow Matching](../2023/ICLR/2023_ICLR_Flow-Matching-for-Generative-Modeling/01_overview.md) | generative modeling foundation | noisy sample plus conditioning | iterative denoising / continuous transport | score/noise objective / vector-field matching | generic pretraining data | none | action generation의 prerequisite | multimodal distribution modeling | sampling/integration cost and schedule dependence | action distribution 설계의 두 생성 backbone 비교 |
| [Diffusion Policy](../2023/RSS/2023_RSS_Diffusion-Policy-Visuomotor-Policy-Learning-via-Action-Dif/01_overview.md) / [π0](../2025/RSS/2025_RSS_pi0-A-Vision-Language-Action-Flow-Model-for-General-Robot/01_overview.md) | imitation-based robot action generation / generalist VLA | images, language and proprioception | continuous action chunks | conditional diffusion / flow-matching action expert | demonstrations / heterogeneous robot data | offline train, closed-loop deployment | manipulation across tasks and embodiments | object/task/embodiment transfer | chunk latency, contact correction and data imbalance | generative action model을 control interface로 평가 |


## Dependency and Evolution

아래 계보에서 화살표는 문제의식과 method interface의 진화를 뜻한다. 직접 citation 관계는 정독 시 확인한다.

| Foundation → transition → frontier | 계승·변화 | 아직 확인할 경계 |
|---|---|---|
| [DAgger](../2011/AISTATS/2011_AISTATS_A-Reduction-of-Imitation-Learning-and-Structured-Predictio/01_overview.md) → [RoboMimic](../2021/CoRL/2021_CoRL_What-Matters-in-Learning-from-Offline-Human-Demonstrations/01_overview.md) / [RLBench](../2020/RA-L/2020_RA-L_RLBench-The-Robot-Learning-Benchmark-and-Learning-Environm/01_overview.md) → [BC-Z](../2022/CoRL/2022_CoRL_BC-Z-Zero-Shot-Task-Generalization-with-Robotic-Imitation/01_overview.md) / [MimicGen](../2023/CoRL/2023_CoRL_MimicGen-A-Data-Generation-System-for-Scalable-Robot-Learn/01_overview.md) → [DROID](../2024/RSS/2024_RSS_DROID-A-Large-Scale-In-The-Wild-Robot-Manipulation-Dataset/01_overview.md) / Open X-Embodiment 계열 | distribution-shift-aware imitation에서 reproducible offline-IL benchmark와 multi-task environment를 거쳐 자동 demonstration 확장, in-the-wild와 heterogeneous robot data로 범위가 넓어진다. | 알고리즘, observation modality, demonstration quality와 task/embodiment coverage의 기여를 분리할 수 있는가 |
| [TRPO](../2015/ICML/2015_ICML_Trust-Region-Policy-Optimization/01_overview.md) → [PPO](../2017/arxiv/2017_arxiv_Proximal-Policy-Optimization-Algorithms/01_overview.md) / [SAC](../2018/ICML/2018_ICML_Soft-Actor-Critic-Off-Policy-Maximum-Entropy-Deep-Reinforc/01_overview.md) → RMA·dexterous RL·humanoid control | 안정적인 policy update와 off-policy exploration이 대규모 simulation 및 sim-to-real motor learning의 optimization backbone으로 이어진다. | reward shaping과 simulator coverage가 실제 robustness를 얼마나 대신하는가 |
| [CQL](../2020/NeurIPS/2020_NeurIPS_Conservative-Q-Learning-for-Offline-Reinforcement-Learning/01_overview.md) / [IQL](../2022/ICLR/2022_ICLR_Offline-Reinforcement-Learning-with-Implicit-Q-Learning/01_overview.md) / [Decision Transformer](../2021/NeurIPS/2021_NeurIPS_Decision-Transformer-Reinforcement-Learning-via-Sequence-M/01_overview.md) → [Q-Transformer](../2024/CoRL/2024_CoRL_Q-Transformer-Scalable-Offline-Reinforcement-Learning-via/01_overview.md) → world-model/VLA policy improvement | conservatism, implicit value learning, sequence conditioning이 large robot dataset용 action/value interface로 확장된다. | failure data를 쓰면서 OOD action overestimation과 bad behavior imitation을 동시에 막을 수 있는가 |
| [DDPM](../2020/NeurIPS/2020_NeurIPS_Denoising-Diffusion-Probabilistic-Models/01_overview.md) / [Flow Matching](../2023/ICLR/2023_ICLR_Flow-Matching-for-Generative-Modeling/01_overview.md) → [Diffusion Policy](../2023/RSS/2023_RSS_Diffusion-Policy-Visuomotor-Policy-Learning-via-Action-Dif/01_overview.md) / [π0](../2025/RSS/2025_RSS_pi0-A-Vision-Language-Action-Flow-Model-for-General-Robot/01_overview.md) → [Diffusion-EDFs](../2024/CVPR/2024_CVPR_Diffusion-EDFs-Bi-equivariant-Denoising-Generative-Modelin/01_overview.md) / [Reactive Diffusion Policy](../2025/RSS/2025_RSS_Reactive-Diffusion-Policy-Slow-Fast-Visual-Tactile-Policy/01_overview.md) | 생성 모델의 denoising·continuous transport를 multimodal action trajectory와 generalist VLA에 옮기고, SE(3) structure와 고주파 contact feedback을 추가한다. | iterative inference, integration step과 action chunk가 요구하는 latency가 폐루프 correction을 제한하는가 |
| [Domain Randomization](../2017/IROS/2017_IROS_Domain-Randomization-for-Transferring-Deep-Neural-Networks/01_overview.md) → [RMA](../2021/RSS/2021_RSS_RMA-Rapid-Motor-Adaptation-for-Legged-Robots/01_overview.md) → [ASAP](../2025/RSS/2025_RSS_ASAP-Aligning-Simulation-and-Real-World-Physics-for-Learni/01_overview.md) / [VIRAL](../2026/CVPR/2026_CVPR_VIRAL-Visual-Sim-to-Real-at-Scale-for-Humanoid-Loco-Manipu/01_overview.md) | 고정 randomization에서 latent adaptation, real-physics alignment, visual sim-to-real scaling으로 이동한다. | online adaptation이 distribution shift를 식별하는지 단순히 robust policy로 평균화하는지 |

## Open Questions

- 실패와 비전문 데이터를 안전하게 policy improvement에 쓰는 방법은 무엇인가?
- Action chunking과 closed-loop correction 사이의 적절한 시간 척도는 무엇인가?
- Cross-embodiment data에서 공유해야 하는 것은 representation, skill, value, dynamics 중 무엇인가?

## Research Gaps

- 통합 gap은 [G-06: failure/suboptimal data](../research/RESEARCH_GAPS.md#g-06-failure와-suboptimal-data의-안전한-재사용-부족), [G-08: imagined improvement](../research/RESEARCH_GAPS.md#g-08-imagined-policy-improvement의-보수성과-calibration), [G-12: data scale 대 coverage](../research/RESEARCH_GAPS.md#g-12-data-scale와-data-coverage의-혼동)을 본다.
- 이 문서에는 정독으로 확인한 objective·data assumption·negative result만 누적한다.
