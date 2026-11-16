# VLA Reading Plan for Manipulation and Navigation

- Updated: 2026-11-16 KST
- Source registry: [PAPER.md](../PAPER.md)
- Full tier index: [READING_TIERS.csv](./READING_TIERS.csv)
- Reading tracker: [READING_STATUS.csv](./READING_STATUS.csv)
- Inactive reading history: [READING_STATUS_HISTORY.csv](./READING_STATUS_HISTORY.csv)
- Intensive-reading set: **455 papers** (CORE 50 + NEXT 405)
- Base tier review: 2026-10-19; 최근 등록·게재 갱신은 [유지보수 이력](../work/update/README.md)을 따른다. 개별 membership은 이 생성기의 CORE/NEXT group으로 관리하고 사용자 읽기 이력은 보존한다. Registry는 VLA 기반 manipulation·navigation과 action-relevant 3D를 다루며, 현재 새 주제 탐색은 사용자 요청에 따라 VLA + RL을 우선한다.

## Research Scope and Reading Policy

주 연구축은 VLA를 기반으로 다양한 로봇의 manipulation과 navigation을 다루는 것이다. 현재 새 탐색은 VLA + RL 결합이며, 기존 비-RL 후보의 문헌과 판단도 보존한다. 관측·언어 지시·보상이 실제 행동과 일반화에 주는 효과, 로봇별 적응 비용과 기존 능력 보존을 함께 검토한다. 3D vision은 policy state, spatial memory, affordance, localization, collision/contact reasoning이 실제 행동을 바꾸는 경우 우선한다.

읽기 결과는 [7개 synthesis와 교차 질문 분류](../synthesis/README.md)에 연결한다. 행동 표현·시간/feedback·상태/기억·접촉/실행 가능성·적응/평가 신뢰도를 구분해 비교한다. 현재 후보는 [주제 index](../work/research_topics/README.md), 과거 판정은 [16개 주제 요약](../work/research_candidates/summaries/README.md), 활성 작업은 [TODO](../TODO.md)에서 관리한다. 후보 HOLD/NO-GO와 GPU 확보는 아래 tier membership이나 실제 읽기 상태를 자동으로 바꾸지 않는다.

`observation/history → state/belief/3D memory → language/task/skill decision → VLA/policy/control → contact/failure feedback → adaptation/recovery (RL optional)`

1. **CORE 50편:** 목표 연구의 재사용 가능한 foundation, 대표 policy/RL interface, 데이터·평가 기준이다. 각 논문의 선정 이유를 아래에 기록한다.
2. **NEXT 405편:** 해당 branch의 선행 개념을 확인한 뒤 읽는 전문화·frontier다. CORE 전체 완독을 기다릴 필요는 없다.
3. **REFERENCE 509편:** controller, sensor, embodiment, reconstruction 방법을 실제로 사용할 때 조회한다.
4. **ARCHIVE 242편:** 현재 범위 밖의 검색·역사 자료로 보존한다.

### 운영 원칙

- 연도만으로 승격·강등하지 않는다. TD, policy gradient, PPO, SAC, POMDP, impedance는 최신 방법의 objective와 interface를 이해하는 데 필요한 범위로 유지한다.
- CORE의 번호는 탐색과 기본 진행 순서다. 아래 dependency batch에서 필요한 선행을 확인하면 해당 NEXT를 병행한다.
- Manipulation의 direct VLA RL, RL-generated data distillation, navigation의 hierarchical VLA/RL control을 서로 다른 개선 경로로 비교한다.
- 동일 플랫폼의 fleet, pretraining-seen/RL-held-out robot, target adaptation, unseen-embodiment zero-shot을 구분한다. RL 전이는 동일 데이터 SFT·후학습 전 base policy와 비교한다.
- Locomotion은 navigation controller·mobile manipulation과 직접 연결될 때 우선하며, humanoid motion tracking이나 순수 보행 전문화는 필요시 참조한다.
- 7개 primary track과 연도/venue 폴더 구조를 유지한다. Navigation은 관련 track의 task/interface로 연결하고 중복 등록하지 않는다.
- 선정 이유는 연구자의 curation 판단이다. abstract/project 재확인은 본문 정독이나 reading status 승격을 뜻하지 않는다.

## Priority Criteria

1. VLA/generalist policy의 reward-driven 개선 또는 manipulation/navigation 실행에 직접 필요한가
2. action representation, policy gradient/value objective, offline-to-online data, controller interface를 이해할 기준인가
3. 여러 후속 연구에서 재사용할 foundation, 공개 system, 데이터 또는 benchmark인가
4. 3D representation의 효과가 perception 점수와 함께 downstream behavior로 평가되는가
5. demonstration·interaction·compute·inference budget을 맞춘 비교가 가능한가
6. partial observability, long horizon, reward error, contact, recovery를 구체적으로 평가하는가
7. 최신 논문은 기존 기준의 어떤 한계를 검증하거나 바꾸는가

## Tier Definitions

| Tier | Papers | Use |
|---|---:|---|
| CORE | 50 | VLA 기반 manipulation/navigation의 기반·대표 interface·평가 좌표계 |
| NEXT | 405 | 해당 CORE prerequisite 이후 읽는 직접 관련 전문화·frontier |
| REFERENCE | 509 | 특정 구현·sensor·embodiment가 요구할 때 읽는 기반과 대안 |
| ARCHIVE | 242 | 현재 범위 밖의 검색·역사 자료 |

CORE는 최신 논문 모음이나 고정 quota가 아니다. 중요성과 dependency가 바뀌면 규모도 바뀐다.

## Completion Rule

논문 하나를 정독한 뒤 문제·가정, observation/state/action/control interface, embodiment/task/data/metric/failure, 재사용·반박할 지점을 tracker와 해당 synthesis에 기록한다. 노트의 존재와 source evidence는 사용자의 읽기 상태와 별개다.

## Dependency-Based Reading Batches

단일 canonical plan 안의 비교 경로다. 화살표는 개념적 prerequisite이며 직접 citation을 뜻하지 않는다. 각 경로의 선행을 확인한 뒤 frontier와 baseline을 함께 읽는다.

| Branch | Foundation and comparison spine | NEXT extension | Exit artifact |
|---|---|---|---|
| VLA + RL manipulation | TD/GAE → PPO + Diffusion Policy → DPPO; IQL/CQL → AWAC/Cal-QL ↔ FQL; RLPD/SERL → HIL-SERL; OFT → ConRFT ↔ RLDG | SimpleVLA-RL, RL4VLA, WCM, RoboAlign, STARE-VLA; Real-Time EXPO-FT는 별도 editor 구조의 대안 | advantage/critic·actor 갱신 대상·배포 구조, demonstration·interaction·compute를 맞춘 비교표 |
| Reward, goals and temporal abstraction | Potential-based reward shaping; UVFA → HER ↔ Successor Features; options/semi-MDP | HIQL, Is Value Learning Really the Main Bottleneck in Offline RL?, Horizon Reduction, Act2Goal | 목표·전이 동역학·종료/할인 가정, value 오차와 policy extraction·horizon 병목을 분리한 표 |
| Action representation and generalization | DAgger/RoboMimic → ACT/Diffusion Policy; DDPM/Flow Matching → Octo/OpenVLA/π0 → FAST/π0.5; DPPO/FQL | Q-chunking → DQC, SpatialVLA, reactive/force VLA | actor chunk·critic horizon·feedback rate·latency·action likelihood와 RL objective 표 |
| Navigation and mobile manipulation | POMDP/Habitat/VLN-CE → ViNT/NoMaD; CLIP/ConceptFusion/VLFM → SayCan/NaVILA; Mobile ALOHA | NaVid → Uni-NaVid/StreamVLN, NavDP/LoGoPlanner, SocialNav, FeedTTA, GOAT, WMNav | goal type·memory·action granularity·collision·social compliance·SPL/success와 reward 접근 조건 표 |
| Action-relevant 3D | RVT ↔ DP3; ConceptFusion ↔ VLFM | LoGoPlanner의 metric memory, PointWorld의 3D dynamics/MPC, VLMaps, PointVLA, Any3D-VLA | policy·data·compute를 고정한 RGB/3D 비교, pose/calibration 접근과 downstream failure |
| Evaluation, contact and recovery | LIBERO/CALVIN/DROID/Habitat; DAgger → DART; MuJoCo/impedance → Recovery RL/TD-MPC2 | D4RL ↔ OGBench, Tune to Learn, Discounted Liveness OPE, OopsieVerse, Tac2Real, RLBench, ManiSkill3, FurnitureBench, SAFE | task/split·reward·gain·damage·reset·intervention 비용, recovery·truncation·OOD protocol |
| World-model policy improvement | TD-MPC2 → Ctrl-World/WMPO/WorldGym | VLAW ↔ VLA-MBPO ↔ RISE; PointWorld의 MPC와 비교; PersistWorld는 prediction-fidelity 참조 | fixed real-data budget, imagined vs real success, failure coverage와 model bias의 분리 |

Batch 산출물과 source location을 확인한 뒤에만 synthesis evidence로 사용한다. Benchmark 간 성공률을 같은 난이도의 점수로 합치지 않는다.

## Research Lenses Across Tracks

- VLA RL과 from-scratch RL, supervised fine-tuning, RL-generated-data distillation을 분리한다.
- Offline demonstration과 online interaction 양, human intervention, reset, reward annotation 비용을 함께 기록한다.
- Navigation의 instruction/goal grounding과 low-level execution을 분리하고 privileged state·map·oracle success 접근을 명시한다.
- 3D 입력의 이득은 action success·collision·sample efficiency·latency와 연결한다.
- 최신 2024–2026 연구도 장기 foundation으로 단정하지 않는다. 공개 interface와 평가 근거가 부족하면 NEXT 또는 REFERENCE로 유지한다.
- Task success 외에 disturbance, long horizon, contact failure, forgetting, recovery를 비교한다.

## CORE — 50 papers

### RL, IL, and policy learning foundations — 23

1. [Learning to Predict by the Methods of Temporal Differences](../1988/Machine-Learning/1988_Machine-Learning_Learning-to-Predict-by-the-Methods-of-Temporal-Differences/01_overview.md) — 1988 Machine Learning.
   - 선정 이유: TD bootstrapping은 SAC·IQL·RLPD의 value target과 offline/online 오차를 이해하는 공통 기반이다.
2. [Policy invariance under reward transformations: Theory and application to reward shaping](../1999/ICML/1999_ICML_Policy-invariance-under-reward-transformations-Theory-and/01_overview.md) — 1999 ICML.
   - 선정 이유: VLM progress·단계 보상·접촉 보상으로 목표를 변경하는지 판단할 공통 이론 원전이므로 CORE다.
3. [Universal Value Function Approximators](../2015/ICML/2015_ICML_Universal-Value-Function-Approximators/01_overview.md) — 2015 ICML.
   - 선정 이유: HER·HIQL·목표 조건부 critic과 단일 VLA의 지시별 가치 표현을 이해하는 원전이므로 CORE다.
4. [Policy Gradient Methods for Reinforcement Learning with Function Approximation](../1999/NeurIPS/1999_NeurIPS_Policy-Gradient-Methods-for-Reinforcement-Learning-with-Fu/01_overview.md) — 1999 NeurIPS.
   - 선정 이유: Policy-gradient objective와 gradient estimator는 PPO 및 VLA의 reward-driven 정책 갱신을 비교하는 기반이다.
5. [High-Dimensional Continuous Control Using Generalized Advantage Estimation](../2016/ICLR/2016_ICLR_High-Dimensional-Continuous-Control-Using-Generalized-Adva/01_overview.md) — 2016 ICLR.
   - 선정 이유: PPO 기반 VLA RL에서 advantage·bootstrap·시간 단위가 학습에 미치는 영향을 해석하기 위한 공통 원전이므로 CORE다.
6. [Proximal Policy Optimization Algorithms](../2017/arxiv/2017_arxiv_Proximal-Policy-Optimization-Algorithms/01_overview.md) — 2017 arXiv.
   - 선정 이유: PPO의 clipped policy update는 on-policy VLA RL과 navigation policy optimization의 대표 비교 기준이다.
7. [Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor](../2018/ICML/2018_ICML_Soft-Actor-Critic-Off-Policy-Maximum-Entropy-Deep-Reinforc/01_overview.md) — 2018 ICML.
   - 선정 이유: Entropy-regularized off-policy actor-critic은 SERL·HIL-SERL 계열의 sample-efficient manipulation RL을 이해하는 기반이다.
8. [Offline Reinforcement Learning with Implicit Q-Learning](../2022/ICLR/2022_ICLR_Offline-Reinforcement-Learning-with-Implicit-Q-Learning/01_overview.md) — 2022 ICLR.
   - 선정 이유: Dataset action support 안에서 value와 policy를 학습하는 IQL은 VLA의 offline initialization과 online 개선을 구분하는 기준이다.
9. [Conservative Q-Learning for Offline Reinforcement Learning](../2020/NeurIPS/2020_NeurIPS_Conservative-Q-Learning-for-Offline-Reinforcement-Learning/01_overview.md) — 2020 NeurIPS.
   - 선정 이유: Offline 데이터 밖 action의 value 과대평가를 다루는 CQL은 IQL·VLA RL의 보수성과 탐색 trade-off를 비교하는 기반이다.
10. [A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning](../2011/AISTATS/2011_AISTATS_A-Reduction-of-Imitation-Learning-and-Structured-Predictio/01_overview.md) — 2011 AISTATS.
   - 선정 이유: DAgger의 distribution shift와 data aggregation은 VLA closed-loop 실패 및 intervention 기반 RL 개선을 해석하는 기반이다.
11. [What Matters in Learning from Offline Human Demonstrations for Robot Manipulation](../2021/CoRL/2021_CoRL_What-Matters-in-Learning-from-Offline-Human-Demonstrations/01_overview.md) — 2021 CoRL.
   - 선정 이유: RoboMimic의 demonstration·observation·평가 설계는 VLA/RL 방법 비교에서 데이터 품질과 정책 효과를 분리하는 기준이다.
12. [Denoising Diffusion Probabilistic Models](../2020/NeurIPS/2020_NeurIPS_Denoising-Diffusion-Probabilistic-Models/01_overview.md) — 2020 NeurIPS.
   - 선정 이유: DDPM의 denoising objective는 Diffusion Policy와 이후 diffusion-action RL의 정책 분포를 이해하는 기반이다.
13. [Flow Matching for Generative Modeling](../2023/ICLR/2023_ICLR_Flow-Matching-for-Generative-Modeling/01_overview.md) — 2023 ICLR.
   - 선정 이유: Flow Matching의 vector-field 학습은 π0 계열 continuous action 생성과 RL 적응의 policy parameterization을 이해하는 기반이다.
14. [Diffusion Policy: Visuomotor Policy Learning via Action Diffusion](../2023/RSS/2023_RSS_Diffusion-Policy-Visuomotor-Policy-Learning-via-Action-Dif/01_overview.md) — 2023 RSS.
   - 선정 이유: Diffusion Policy는 VLA의 개선이 language pretraining·action generation·RL 중 어디서 생기는지 비교할 대표 visuomotor IL baseline이다.
15. [Diffusion Policy Policy Optimization](../2025/ICLR/2025_ICLR_Diffusion-Policy-Policy-Optimization/01_overview.md) — 2025 ICLR.
   - 선정 이유: Foundation bridge. PPO를 denoising policy의 RL fine-tuning으로 연결한다. Diffusion Policy → DPPO → RL-100 등 직접 policy 개선을 비교하는 prerequisite이므로 CORE를 검토할 이유가 있다. VLA 자체를 제안한 논문은 아니다.
16. [Flow Q-Learning](../2025/ICML/2025_ICML_Flow-Q-Learning/01_overview.md) — 2025 ICML.
   - 선정 이유: Foundation bridge. Expressive flow policy와 Q-learning/one-step actor를 연결한다. IQL/CQL 이후 flow-action RL과 Q-chunking 계열의 구현·비교 기준으로 중요하다. 평가가 곧 실제 robot VLA 학습을 입증하는 것은 아니다.
17. [Efficient Online Reinforcement Learning with Offline Data](../2023/ICML/2023_ICML_Efficient-Online-Reinforcement-Learning-with-Offline-Data/01_overview.md) — 2023 ICML.
   - 선정 이유: RLPD의 offline/online replay 결합은 SERL·HIL-SERL에서 demonstration을 활용하는 실제 robot RL 학습 경로의 선행 기반이다.
18. [SERL: A Software Suite for Sample-Efficient Robotic Reinforcement Learning](../2024/ICRA/2024_ICRA_SERL-A-Software-Suite-for-Sample-Efficient-Robotic-Reinfor/01_overview.md) — 2024 ICRA.
   - 선정 이유: SERL은 actor/learner·reward·robot interface를 연결해 HIL-SERL과 VLA RL의 실제 학습 비용을 평가할 공개 시스템 기준이다.
19. [Precise and dexterous robotic manipulation via human-in-the-loop reinforcement learning](../2025/Science-Robotics/2025_Science-Robotics_Precise-and-dexterous-robotic-manipulation-via-human-in-th/01_overview.md) — 2025 Science Robotics.
   - 선정 이유: HIL-SERL은 demonstration·human intervention·reward classifier를 결합한 real-robot RL의 대표 실행 기준이며 ConRFT·RLDG 비교에 필요하다.
20. [RLDG: Robotic Generalist Policy Distillation via Reinforcement Learning](../2025/RSS/2025_RSS_RLDG-Robotic-Generalist-Policy-Distillation-via-Reinforcem/01_overview.md) — 2025 RSS.
   - 선정 이유: RLDG는 specialist RL로 얻은 데이터를 generalist에 증류하는 경로를 제시해 ConRFT의 직접 VLA RL 미세조정과 구분할 핵심 비교 기준이다.
21. [DROID: A Large-Scale In-The-Wild Robot Manipulation Dataset](../2024/RSS/2024_RSS_DROID-A-Large-Scale-In-The-Wild-Robot-Manipulation-Dataset/01_overview.md) — 2024 RSS.
   - 선정 이유: DROID는 실제 환경의 조작 데이터 다양성과 수집 조건을 제공하여 VLA 사전학습·fine-tuning의 데이터 가정을 판단하는 기준이다.
22. [Benchmarking Knowledge Transfer for Lifelong Robot Learning](../2023/NeurIPS/2023_NeurIPS_Benchmarking-Knowledge-Transfer-for-Lifelong-Robot-Learnin/01_overview.md) — 2023 NeurIPS.
   - 선정 이유: LIBERO는 OpenVLA-OFT와 VLA RL의 task suite·transfer 평가를 이해하고 baseline을 공정하게 비교하기 위한 benchmark 기반이다.
23. [Habitat: A Platform for Embodied AI Research](../2019/ICCV/2019_ICCV_Habitat-A-Platform-for-Embodied-AI-Research/01_overview.md) — 2019 ICCV.
   - 선정 이유: Habitat는 navigation의 task·sensor·simulator·generalization protocol을 제공하여 VLN-CE와 navigation RL 평가를 해석하는 기반이다.

### VLA and generalist robot policies — 13

24. [Learning Transferable Visual Models From Natural Language Supervision](../2021/ICML/2021_ICML_Learning-Transferable-Visual-Models-From-Natural-Language/01_overview.md) — 2021 ICML.
   - 선정 이유: CLIP의 image-language alignment는 VLA backbone과 VLFM·ConceptFusion의 semantic grounding을 이해하는 공통 기반이다.
25. [RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control](../2023/CoRL/2023_CoRL_RT-2-Vision-Language-Action-Models-Transfer-Web-Knowledge/01_overview.md) — 2023 CoRL.
   - 선정 이유: RT-2는 pretrained VLM에서 robot action으로의 전이를 정식화해 OpenVLA 및 이후 VLA의 action-token 설계를 이해하는 기반이다.
26. [Open X-Embodiment: Robotic Learning Datasets and RT-X Models](../2024/ICRA/2024_ICRA_Open-X-Embodiment-Robotic-Learning-Datasets-and-RT-X-Model/01_overview.md) — 2024 ICRA.
   - 선정 이유: Open X-Embodiment는 Octo·OpenVLA의 heterogeneous robot-data와 embodiment transfer 가정을 이해하는 데이터 기반이다.
27. [Octo: An Open-Source Generalist Robot Policy](../2024/RSS/2024_RSS_Octo-An-Open-Source-Generalist-Robot-Policy/01_overview.md) — 2024 RSS.
   - 선정 이유: Octo는 공개 generalist policy의 diffusion action·cross-embodiment adaptation을 제공해 VLA 및 RL 개선의 baseline이 된다.
28. [OpenVLA: An Open-Source Vision-Language-Action Model](../2024/CoRL/2024_CoRL_OpenVLA-An-Open-Source-Vision-Language-Action-Model/01_overview.md) — 2024 CoRL.
   - 선정 이유: OpenVLA는 공개 VLA 학습·fine-tuning 경로를 제공하며 OFT와 후속 VLA RL의 backbone 기준이다.
29. [Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success](../2025/RSS/2025_RSS_Fine-Tuning-Vision-Language-Action-Models-Optimizing-Speed/01_overview.md) — 2025 RSS.
   - 선정 이유: OpenVLA-OFT는 action chunking·parallel decoding·continuous action의 강한 supervised baseline으로 RL의 추가 이득을 분리하는 데 필요하다.
30. [π0: A Vision-Language-Action Flow Model for General Robot Control](../2025/RSS/2025_RSS_pi0-A-Vision-Language-Action-Flow-Model-for-General-Robot/01_overview.md) — 2025 RSS.
   - 선정 이유: π0는 VLM과 flow-based action expert를 결합해 이후 flow VLA와 RL 정책 갱신의 action interface를 이해하는 기반이다.
31. [FAST: Efficient Action Tokenization for Vision-Language-Action Models](../2025/RSS/2025_RSS_FAST-Efficient-Action-Tokenization-for-Vision-Language-Act/01_overview.md) — 2025 RSS.
   - 선정 이유: FAST는 action tokenization과 고주파 action chunk 압축을 분리해 continuous-flow와 autoregressive VLA의 비용을 비교하는 기준이다.
32. [π0.5: a Vision-Language-Action Model with Open-World Generalization](../2025/CoRL/2025_CoRL_pi0.5-a-Vision-Language-Action-Model-with-Open-World-Gener/01_overview.md) — 2025 CoRL.
   - 선정 이유: π0.5는 open-world generalization과 이질적 데이터 결합의 대표 시스템으로 RL 개선을 새로운 환경·task transfer와 함께 평가할 기준이다.
33. [ConRFT: A Reinforced Fine-tuning Method for VLA Models via Consistency Policy](../2025/RSS/2025_RSS_ConRFT-A-Reinforced-Fine-tuning-Method-for-VLA-Models-via/01_overview.md) — 2025 RSS.
   - 선정 이유: ConRFT는 offline BC/Q 학습에서 online human-intervention VLA RL로 이어지는 직접 fine-tuning 경로를 제공하는 연구축의 핵심 비교 기준이다.
34. [Do As I Can, Not As I Say: Grounding Language in Robotic Affordances](../2022/CoRL/2022_CoRL_Do-As-I-Can-Not-As-I-Say-Grounding-Language-in-Robotic-Aff/01_overview.md) — 2022 CoRL.
   - 선정 이유: SayCan은 language task proposal과 learned affordance/value를 결합해 VLA+RL의 hierarchical manipulation·navigation 의사결정을 이해하는 기반이다.
35. [NaVILA: Legged Robot Vision-Language-Action Model for Navigation](../2025/RSS/2025_RSS_NaVILA-Legged-Robot-Vision-Language-Action-Model-for-Navig/01_overview.md) — 2025 RSS.
   - 선정 이유: NaVILA는 VLA의 중간 수준 spatial command와 visual locomotion RL을 연결해 navigation에서 reasoning/control interface를 비교하는 대표 시스템이다.
36. [CALVIN: A Benchmark for Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks](../2022/RA-L/2022_RA-L_CALVIN-A-Benchmark-for-Language-Conditioned-Policy-Learnin/01_overview.md) — 2022 RA-L.
   - 선정 이유: CALVIN은 language-conditioned long-horizon manipulation의 연속 skill 성공과 일반화를 평가해 LIBERO와 다른 실패 누적을 비교하는 기준이다.

### Manipulation, contact, tactile, and dexterity — 2

37. [Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware](../2023/RSS/2023_RSS_Learning-Fine-Grained-Bimanual-Manipulation-with-Low-Cost/01_overview.md) — 2023 RSS.
   - 선정 이유: ACT는 action chunk와 temporal aggregation을 사용하는 조작 IL 기준으로 OFT·flow VLA·RL 개선의 action-interface 효과를 분리한다.
38. [3D Diffusion Policy: Generalizable Visuomotor Policy Learning via Simple 3D Representations](../2024/RSS/2024_RSS_3D-Diffusion-Policy-Generalizable-Visuomotor-Policy-Learni/01_overview.md) — 2024 RSS.
   - 선정 이유: DP3는 sparse point-cloud representation을 action diffusion에 연결해 3D 입력이 조작 일반화에 주는 효과를 직접 비교하는 기준이다.

### Planning, control, and whole-body foundations — 4

39. [Planning and Acting in Partially Observable Stochastic Domains](../1998/Artificial-Intelligence/1998_Artificial-Intelligence_Planning-and-Acting-in-Partially-Observable-Stochastic-Dom/01_overview.md) — 1998 Artificial Intelligence.
   - 선정 이유: POMDP의 belief와 partial observability는 navigation memory·VLA history·recovery의 상태 가정을 명시하는 기반이다.
40. [Impedance Control: An Approach to Manipulation: Part I—Theory](../1985/Journal-of-Dynamic-Syste/1985_Journal-of-Dynamic-Syste_Impedance-Control-An-Approach-to-Manipulation-Part-ITheory/01_overview.md) — 1985 Journal of Dynamic Systems, Measurement, and Control.
   - 선정 이유: Impedance control은 contact-rich policy의 action이 low-level compliance와 어떻게 연결되는지 판단하고 RL 성능과 controller 효과를 구분하는 기반이다.
41. [MuJoCo: A Physics Engine for Model-Based Control](../2012/IROS/2012_IROS_MuJoCo-A-Physics-Engine-for-Model-Based-Control/01_overview.md) — 2012 IROS.
   - 선정 이유: MuJoCo는 조작 RL benchmark의 접촉 dynamics와 simulator 가정을 이해해 reward·success·sim-to-real 비교를 해석하는 기반이다.
42. [NoMaD: Goal Masked Diffusion Policies for Navigation and Exploration](../2024/ICRA/2024_ICRA_NoMaD-Goal-Masked-Diffusion-Policies-for-Navigation-and-Ex/01_overview.md) — 2024 ICRA.
   - 선정 이유: NoMaD는 goal-conditioned diffusion과 exploration을 결합해 ViNT 이후 navigation action generation의 비교 기준을 제공한다.

### Robotics-enabling 3D perception — 4

43. [ConceptFusion: Open-set Multimodal 3D Mapping](../2023/RSS/2023_RSS_ConceptFusion-Open-set-Multimodal-3D-Mapping/01_overview.md) — 2023 RSS.
   - 선정 이유: ConceptFusion은 open-set semantic 3D memory가 object navigation과 language-grounded robot action으로 이어지는 representation 기준이다.
44. [RVT: Robotic View Transformer for 3D Object Manipulation](../2023/CoRL/2023_CoRL_RVT-Robotic-View-Transformer-for-3D-Object-Manipulation/01_overview.md) — 2023 CoRL.
   - 선정 이유: RVT는 3D scene을 multi-view action representation으로 연결해 DP3·spatial VLA와 비교할 manipulation 기준이다.
45. [VLFM: Vision-Language Frontier Maps for Zero-Shot Semantic Navigation](../2024/ICRA/2024_ICRA_VLFM-Vision-Language-Frontier-Maps-for-Zero-Shot-Semantic/01_overview.md) — 2024 ICRA.
   - 선정 이유: VLFM은 semantic value map과 frontier exploration을 연결해 learned navigation VLA/RL과 비교할 modular object-navigation 기준이다.
46. [Beyond the Nav-Graph: Vision-and-Language Navigation in Continuous Environments](../2020/ECCV/2020_ECCV_Beyond-the-Nav-Graph-Vision-and-Language-Navigation-in-Con/01_overview.md) — 2020 ECCV.
   - 선정 이유: VLN-CE는 graph waypoint를 넘어 low-level action을 실행하는 continuous navigation formulation으로 NaVILA와 VLN RL의 평가 가정을 구분한다.

### Locomotion, mobile manipulation, and humanoid systems — 2

47. [ViNT: A Foundation Model for Visual Navigation](../2023/CoRL/2023_CoRL_ViNT-A-Foundation-Model-for-Visual-Navigation/01_overview.md) — 2023 CoRL.
   - 선정 이유: ViNT는 다양한 robot navigation 데이터의 goal-conditioned pretraining을 제공해 NoMaD와 navigation VLA의 transfer를 이해하는 기반이다.
48. [Mobile ALOHA: Learning Bimanual Mobile Manipulation using Low-Cost Whole-Body Teleoperation](../2024/CoRL/2024_CoRL_Mobile-ALOHA-Learning-Bimanual-Mobile-Manipulation-using-L/01_overview.md) — 2024 CoRL.
   - 선정 이유: Mobile ALOHA는 base와 bimanual arm을 함께 다루는 데이터·policy interface를 제공해 navigation과 manipulation의 결합 범위를 판단하는 기준이다.

### Safety and robot world models — 2

49. [TD-MPC2: Scalable, Robust World Models for Continuous Control](../2024/ICLR/2024_ICLR_TD-MPC2-Scalable-Robust-World-Models-for-Continuous-Contro/01_overview.md) — 2024 ICLR.
   - 선정 이유: TD-MPC2는 latent dynamics·value·planning을 함께 사용하는 model-based RL 기준으로 VLA+world-model 개선의 비용과 효과를 비교한다.
50. [Recovery RL: Safe Reinforcement Learning with Learned Recovery Zones](../2020/RA-L/2020_RA-L_Recovery-RL-Safe-Reinforcement-Learning-with-Learned-Recov/01_overview.md) — 2020 RA-L.
   - 선정 이유: Recovery RL은 task policy와 recovery policy의 역할을 분리해 VLA/RL의 실패 후 복구 및 안전한 online 학습을 비교하는 기반이다.

해당 branch의 CORE prerequisite를 확인한 뒤 아래 NEXT를 병행한다. 모든 CORE를 먼저 완독할 필요는 없다.

## NEXT — 405 papers

### RL, IL, offline learning, and robot data — 96

1. [Reinforcement Learning with Action Chunking](../2025/NeurIPS/2025_NeurIPS_Reinforcement-Learning-with-Action-Chunking/01_overview.md) — 2025 NeurIPS.
   - 선정 이유: Current trend. Chunk 단위의 exploration과 TD backup을 결합한다. ACT/FAST의 표현 관점에 RLPD/FQL의 학습 관점을 더하므로 장기 manipulation의 비교 baseline으로 필요하다.
2. [Decoupled Q-Chunking](../2026/ICLR/2026_ICLR_Decoupled-Q-Chunking/01_overview.md) — 2026 ICLR.
   - 선정 이유: Current trend. Critic과 actor의 chunk 길이를 분리한다. Q-chunking의 value propagation 이점과 짧은 action horizon의 반응성 사이의 설계 문제를 직접 다룬다. 실제 contact feedback 성능으로의 확장은 본문/실험 확인이 필요하다.
3. [Steering Your Diffusion Policy with Latent Space Reinforcement Learning](../2025/CoRL/2025_CoRL_Steering-Your-Diffusion-Policy-with-Latent-Space-Reinforce/01_overview.md) — 2025 CoRL.
   - 선정 이유: Current trend. Base policy weight를 고정하고 latent noise를 RL로 조정한다. ConRFT의 fine-tuning, RLDG의 distillation과 구분되는 adaptation baseline이며 generalist policy와 실제 robot 평가가 있다.
4. [Performant robotic manipulation with real-world reinforcement learning](../2026/Science-Robotics/2026_Science-Robotics_Performant-robotic-manipulation-with-real-world-reinforcem/01_overview.md) — 2026 Science Robotics.
   - 선정 이유: Current trend / real-robot system. Diffusion policy에서 imitation→offline/online RL과 빠른 실행을 연결한다. HIL-SERL/DPPO와 비교해 실제 interaction 비용·latency·복구를 읽을 가치가 크다. 제목/이름의 “100”을 모든 환경에서의 무실패 보장으로 해석하지 않는다.
5. [OGBench: Benchmarking Offline Goal-Conditioned RL](../2025/ICLR/2025_ICLR_OGBench-Benchmarking-Offline-Goal-Conditioned-RL/01_overview.md) — 2025 ICLR.
   - 선정 이유: Benchmark. Stitching·장기 horizon·pixel input 등의 능력을 구분하는 기준이다. FQL/Q-chunking/DQC 결과를 이해하는 prerequisite이며 LIBERO/CALVIN과 평가 목적을 구분한다. Language-conditioned real-robot benchmark는 아니다.
6. [USER: A Unified and Extensible System for Online Real-World Policy Learning in Embodied AI](../2026/RSS/2026_RSS_USER-A-Unified-and-Extensible-System-for-Online-Real-World/01_overview.md) — 2026 RSS.
   - 선정 이유: Current system. 실제 robot online RL에서 edge/cloud·buffer·weight synchronization을 구현할 때 SERL/HIL-SERL의 시스템 확장으로 읽는다. Simulator 중심 RLinf-VLA와 역할이 다르다.
7. [Trust Region Policy Optimization](../2015/ICML/2015_ICML_Trust-Region-Policy-Optimization/01_overview.md) — 2015 ICML.
   - 선정 이유: TRPO는 PPO의 trust-region 계보를 더 깊게 이해할 때 읽는 선택적 기반으로 둔다.
8. [Domain Randomization for Transferring Deep Neural Networks from Simulation to the Real World](../2017/IROS/2017_IROS_Domain-Randomization-for-Transferring-Deep-Neural-Networks/01_overview.md) — 2017 IROS.
   - 선정 이유: Domain Randomization은 VLA/RL sim-to-real 실험을 설계할 때 읽는 직접 관련 전문화로 둔다.
9. [Implicit Behavioral Cloning](../2022/CoRL/2022_CoRL_Implicit-Behavioral-Cloning/01_overview.md) — 2022 CoRL.
   - 선정 이유: IBC는 action energy optimization과 diffusion/flow policy를 비교하는 선택적 baseline으로 둔다.
10. [Decision Transformer: Reinforcement Learning via Sequence Modeling](../2021/NeurIPS/2021_NeurIPS_Decision-Transformer-Reinforcement-Learning-via-Sequence-M/01_overview.md) — 2021 NeurIPS.
   - 선정 이유: Decision Transformer는 sequence-modeling과 value/policy optimization의 차이를 비교할 때 읽는다.
11. [Q-Transformer: Scalable Offline Reinforcement Learning via Autoregressive Q-Functions](../2024/CoRL/2024_CoRL_Q-Transformer-Scalable-Offline-Reinforcement-Learning-via/01_overview.md) — 2024 CoRL.
   - 선정 이유: Q-Transformer는 autoregressive action과 offline Q-learning을 연결하는 VLA+RL 전문화로 유지한다.
12. [Behavior Transformers: Cloning k modes with one stone](../2022/NeurIPS/2022_NeurIPS_Behavior-Transformers-Cloning-k-modes-with-one-stone/01_overview.md) — 2022 NeurIPS.
13. [R3M: A Universal Visual Representation for Robot Manipulation](../2022/CoRL/2022_CoRL_R3M-A-Universal-Visual-Representation-for-Robot-Manipulati/01_overview.md) — 2022 CoRL.
14. [Where are we in the search for an Artificial Visual Cortex for Embodied Intelligence?](../2023/arXiv/2023_arXiv_Where-are-we-in-the-search-for-an-Artificial-Visual-Cortex/01_overview.md) — 2023 arXiv.
15. [Maximum a Posteriori Policy Optimisation](../2018/ICLR/2018_ICLR_Maximum-a-Posteriori-Policy-Optimisation/01_overview.md) — 2018 ICLR.
16. [MT-Opt: Continuous Multi-Task Robotic Reinforcement Learning at Scale](../2021/arXiv/2021_arXiv_MT-Opt-Continuous-Multi-Task-Robotic-Reinforcement-Learnin/01_overview.md) — 2021 arXiv.
17. [Isaac Gym: High Performance GPU Based Physics Simulation For Robot Learning](../2021/NeurIPS-Datasets-and-Ben/2021_NeurIPS-Datasets-and-Ben_Isaac-Gym-High-Performance-GPU-Based-Physics-Simulation-Fo/01_overview.md) — 2021 NeurIPS Datasets and Benchmarks.
18. [Eureka: Human-Level Reward Design via Coding Large Language Models](../2024/ICLR/2024_ICLR_Eureka-Human-Level-Reward-Design-via-Coding-Large-Language/01_overview.md) — 2024 ICLR.
19. [DrEureka: Language Model Guided Sim-To-Real Transfer](../2024/Robotics-Science-and-Sys/2024_Robotics-Science-and-Sys_DrEureka-Language-Model-Guided-Sim-To-Real-Transfer/01_overview.md) — 2024 Robotics: Science and Systems.
20. [Continuous Control with Deep Reinforcement Learning](../2016/ICLR/2016_ICLR_Continuous-Control-with-Deep-Reinforcement-Learning/01_overview.md) — 2016 ICLR.
21. [Addressing Function Approximation Error in Actor-Critic Methods](../2018/ICML/2018_ICML_Addressing-Function-Approximation-Error-in-Actor-Critic-Me/01_overview.md) — 2018 ICML.
22. [Hindsight Experience Replay](../2017/NeurIPS/2017_NeurIPS_Hindsight-Experience-Replay/01_overview.md) — 2017 NeurIPS.
23. [Constrained Policy Optimization](../2017/ICML/2017_ICML_Constrained-Policy-Optimization/01_overview.md) — 2017 ICML.
24. [MOPO: Model-based Offline Policy Optimization](../2020/NeurIPS/2020_NeurIPS_MOPO-Model-based-Offline-Policy-Optimization/01_overview.md) — 2020 NeurIPS.
25. [A Minimalist Approach to Offline Reinforcement Learning](../2021/NeurIPS/2021_NeurIPS_A-Minimalist-Approach-to-Offline-Reinforcement-Learning/01_overview.md) — 2021 NeurIPS.
26. [Learning Complex Dexterous Manipulation with Deep Reinforcement Learning and Demonstrations](../2018/RSS/2018_RSS_Learning-Complex-Dexterous-Manipulation-with-Deep-Reinforc/01_overview.md) — 2018 RSS.
27. [Learning Latent Plans from Play](../2020/CoRL/2020_CoRL_Learning-Latent-Plans-from-Play/01_overview.md) — 2020 CoRL.
28. [Relay Policy Learning: Solving Long-Horizon Tasks via Imitation and Reinforcement Learning](../2020/CoRL/2020_CoRL_Relay-Policy-Learning-Solving-Long-Horizon-Tasks-via-Imita/01_overview.md) — 2020 CoRL.
29. [RLBench: The Robot Learning Benchmark & Learning Environment](../2020/RA-L/2020_RA-L_RLBench-The-Robot-Learning-Benchmark-and-Learning-Environm/01_overview.md) — 2020 RA-L.
30. [MimicGen: A Data Generation System for Scalable Robot Learning using Human Demonstrations](../2023/CoRL/2023_CoRL_MimicGen-A-Data-Generation-System-for-Scalable-Robot-Learn/01_overview.md) — 2023 CoRL.
31. [Universal Manipulation Interface: In-The-Wild Robot Teaching Without In-The-Wild Robots](../2024/RSS/2024_RSS_Universal-Manipulation-Interface-In-The-Wild-Robot-Teachin/01_overview.md) — 2024 RSS.
32. [Robot Fine-Tuning Made Easy: Pre-Training Rewards and Policies for Autonomous Real-World Reinforcement Learning](../2024/ICRA/2024_ICRA_Robot-Fine-Tuning-Made-Easy-Pre-Training-Rewards-and-Polic/01_overview.md) — 2024 ICRA.
33. [Demonstrating GPU Parallelized Robot Simulation and Rendering for Generalizable Embodied AI with ManiSkill3](../2025/RSS/2025_RSS_Demonstrating-GPU-Parallelized-Robot-Simulation-and-Render/01_overview.md) — 2025 RSS.
34. [RoboVerse: A Unified Platform, Benchmark and Dataset for Scalable and Generalizable Robot Learning](../2025/RSS/2025_RSS_RoboVerse-A-Unified-Platform-Benchmark-and-Dataset-for-Sca/01_overview.md) — 2025 RSS.
35. [DexWild: Dexterous Human Interactions for In-the-Wild Robot Policies](../2025/RSS/2025_RSS_DexWild-Dexterous-Human-Interactions-for-In-the-Wild-Robot/01_overview.md) — 2025 RSS.
36. [Dex1B: Learning with 1B Demonstrations for Dexterous Manipulation](../2025/RSS/2025_RSS_Dex1B-Learning-with-1B-Demonstrations-for-Dexterous-Manipu/01_overview.md) — 2025 RSS.
37. [Sim-and-Real Co-Training: A Simple Recipe for Vision-Based Robotic Manipulation](../2025/RSS/2025_RSS_Sim-and-Real-Co-Training-A-Simple-Recipe-for-Vision-Based/01_overview.md) — 2025 RSS.
38. [Novel Demonstration Generation with Gaussian Splatting Enables Robust One-Shot Manipulation](../2025/RSS/2025_RSS_Novel-Demonstration-Generation-with-Gaussian-Splatting-Ena/01_overview.md) — 2025 RSS.
39. [You Only Teach Once: Learn One-Shot Bimanual Robotic Manipulation from Video Demonstrations](../2025/RSS/2025_RSS_You-Only-Teach-Once-Learn-One-Shot-Bimanual-Robotic-Manipu/01_overview.md) — 2025 RSS.
40. [RoboMIND: Benchmark on Multi-embodiment Intelligence Normative Data for Robot Manipulation](../2025/RSS/2025_RSS_RoboMIND-Benchmark-on-Multi-embodiment-Intelligence-Normat/01_overview.md) — 2025 RSS.
41. [Bridging Perception and Action: Spatially-Grounded Mid-Level Representations for Robot Generalization](../2025/RSS/2025_RSS_Bridging-Perception-and-Action-Spatially-Grounded-Mid-Leve/01_overview.md) — 2025 RSS.
42. [DemoGen: Synthetic Demonstration Generation for Data-Efficient Visuomotor Policy Learning](../2025/RSS/2025_RSS_DemoGen-Synthetic-Demonstration-Generation-for-Data-Effici/01_overview.md) — 2025 RSS.
43. [AgiBot World Colosseo: A Large-scale Manipulation Platform for Scalable and Intelligent Embodied Systems](../2025/IROS/2025_IROS_AgiBot-World-Colosseo-A-Large-scale-Manipulation-Platform/01_overview.md) — 2025 IROS.
44. [MP1: MeanFlow Tames Policy Learning in 1-step for Robotic Manipulation](../2026/AAAI/2026_AAAI_MP1-MeanFlow-Tames-Policy-Learning-in-1-step-for-Robotic-M/01_overview.md) — 2026 AAAI.
45. [Diffusion Meets DAgger: Supercharging Eye-in-hand Imitation Learning](../2024/RSS/2024_RSS_Diffusion-Meets-DAgger-Supercharging-Eye-in-hand-Imitation/01_overview.md) — 2024 RSS.
46. [Consistency Policy: Accelerated Visuomotor Policies via Consistency Distillation](../2024/RSS/2024_RSS_Consistency-Policy-Accelerated-Visuomotor-Policies-via-Con/01_overview.md) — 2024 RSS.
47. [Any-point Trajectory Modeling for Policy Learning](../2024/RSS/2024_RSS_Any-point-Trajectory-Modeling-for-Policy-Learning/01_overview.md) — 2024 RSS.
48. [Evaluating Real-World Robot Manipulation Policies in Simulation](../2024/CoRL/2024_CoRL_Evaluating-Real-World-Robot-Manipulation-Policies-in-Simul/01_overview.md) — 2024 CoRL.
49. [MimicPlay: Long-Horizon Imitation Learning by Watching Human Play](../2023/CoRL/2023_CoRL_MimicPlay-Long-Horizon-Imitation-Learning-by-Watching-Huma/01_overview.md) — 2023 CoRL.
50. [Test-Time Adaptation for Online Vision-Language Navigation with Feedback-based Reinforcement Learning](../2025/ICML/2025_ICML_Test-Time-Adaptation-for-Online-Vision-Language-Navigation/01_overview.md) — 2025 ICML.
   - 선정 이유: FeedTTA는 episodic success/failure feedback을 이용한 online VLN adaptation으로 manipulation VLA RL과 navigation RL의 reward·stability 차이를 비교한다.
51. [Studying the Interplay Between the Actor and Critic Representations in Reinforcement Learning](../2025/ICLR/2025_ICLR_Studying-the-Interplay-Between-the-Actor-and-Critic-Repres/01_overview.md) — 2025 ICLR.
52. [SPRINT: Scalable Policy Pre-Training via Language Instruction Relabeling](../2024/ICRA/2024_ICRA_SPRINT-Scalable-Policy-Pre-Training-via-Language-Instructi/01_overview.md) — 2024 ICRA.
   - 선정 이유: 언어 재라벨·skill chaining의 offline policy pretraining 선행. HER/goal-conditioned 학습에서 VLA hindsight 후학습으로 이어지는 차이와 추가 자료 효과를 구별하기 위해 읽는다.
53. [Autonomous Improvement of Instruction Following Skills via Foundation Models](../2024/CoRL/2024_CoRL_Autonomous-Improvement-of-Instruction-Following-Skills-via/01_overview.md) — 2024 CoRL.
   - 선정 이유: 자율 경험 수집·VLM 평가·image-goal 학습을 결합한 실제 로봇 시스템. 단일 VLA RL과 분해된 정책의 정보/감독/상호작용 예산을 비교하는 기준이다.
54. [ReinFlow: Fine-tuning Flow Matching Policy with Online Reinforcement Learning](../2025/NeurIPS/2025_NeurIPS_ReinFlow-Fine-tuning-Flow-Matching-Policy-with-Online-Rein/01_overview.md) — 2025 NeurIPS.
   - 선정 이유: Flow Matching과 policy gradient를 연결하는 online RL 방법. DPPO/FQL 이후 생성 경로 likelihood·학습 noise·적은 생성 step을 비교할 때 필요하다. 후속 VLA repository 기능을 원 논문 결과와 구별한다.
55. [SAIL: Faster-than-Demonstration Execution of Imitation Learning Policies](../2025/CoRL/2025_CoRL_SAIL-Faster-than-Demonstration-Execution-of-Imitation-Lear/01_overview.md) — 2025 CoRL.
   - 선정 이유: E2에서 retiming·tracking·feedback 이득을 분해할 핵심 IL baseline이다. NEXT: 현재 VLA 정독 흐름의 직접 비교·평가 기준으로 편입한다.
56. [AutoEval: Autonomous Evaluation of Generalist Robot Manipulation Policies in the Real World](../2025/CoRL/2025_CoRL_AutoEval-Autonomous-Evaluation-of-Generalist-Robot-Manipul/01_overview.md) — 2025 CoRL.
   - 선정 이유: C5/C6의 reset ledger와 반복 평가를 설계할 핵심 system 기준이다. NEXT: 현재 VLA 정독 흐름의 직접 비교·평가 기준으로 편입한다.
57. [Is Your Imitation Learning Policy Better than Mine? Policy Comparison with Near-Optimal Stopping](../2025/RSS/2025_RSS_Is-Your-Imitation-Learning-Policy-Better-than-Mine-Policy/01_overview.md) — 2025 RSS.
   - 선정 이유: C6의 trial budget·통계적 중단에 대한 표준 직접 기준이다. NEXT: 현재 VLA 정독 흐름의 직접 비교·평가 기준으로 편입한다.
58. [Beyond Binary Success: Sample-Efficient and Statistically Rigorous Robot Policy Comparison](../2026/RSS/2026_RSS_Beyond-Binary-Success-Sample-Efficient-and-Statistically-R/01_overview.md) — 2026 RSS.
   - 선정 이유: C6의 progress-aware 선택을 신규 통계 방법으로 재주장하지 않도록 하는 최신 기준이다. NEXT: 현재 VLA 정독 흐름의 직접 비교·평가 기준으로 편입한다.
59. [RoboFollow: Unveiling the Instruction Following Mirage in Embodied Agents](../2026/CoRL/2026_CoRL_RoboFollow-Unveiling-the-Instruction-Following-Mirage-in-E/01_overview.md) — 2026 CoRL.
   - 선정 이유: C2/D3의 instruction switch와 성공 지표를 검증할 핵심 benchmark다. NEXT: 현재 VLA 정독 흐름의 직접 비교·평가 기준으로 편입한다.
60. [What Matters in Learning from Large-Scale Datasets for Robot Manipulation](../2025/ICLR/2025_ICLR_What-Matters-in-Learning-from-Large-Scale-Datasets-for-Rob/01_overview.md) — 2025 ICLR.
   - 선정 이유: 단순 시각·공간 정렬로 설명되는 이득을 제거하기 위한 DataMIL·GAP-N1의 비교 기준이다.
61. [DataMIL: Selecting Data for Robot Imitation Learning with Datamodels](../2026/ICLR/2026_ICLR_DataMIL-Selecting-Data-for-Robot-Imitation-Learning-with-D/01_overview.md) — 2026 ICLR.
   - 선정 이유: 현재 proxy→target 데이터 전이 질문에서 반드시 대조할 performance-aware 선택 방법이다.
62. [ReMix: Optimizing Data Mixtures for Large Scale Imitation Learning](../2025/CoRL/2025_CoRL_ReMix-Optimizing-Data-Mixtures-for-Large-Scale-Imitation-L/01_overview.md) — 2025 CoRL.
   - 선정 이유: DataMIL의 subset 선택과 domain-level mixture 최적화를 구분하는 필수 비교군이다.
63. [DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning](../2025/ICRA/2025_ICRA_DexMimicGen-Automated-Data-Generation-for-Bimanual-Dextero/01_overview.md) — 2025 ICRA.
   - 선정 이유: 여러 embodiment의 데이터를 늘릴 때 실제 시연과 합성 trajectory의 역할을 비교할 자산이다.
64. [TRANSIC: Sim-to-Real Policy Transfer by Learning from Online Correction](../2025/CoRL/2025_CoRL_TRANSIC-Sim-to-Real-Policy-Transfer-by-Learning-from-Onlin/01_overview.md) — 2025 CoRL.
   - 선정 이유: 새 RL/VLA 적응 기여를 주장하기 전에 인간 개입·residual 학습으로 설명되는 이득을 대조한다.
65. [Equivariant diffusion policy for sample-efficient robotic manipulation](../2026/IJRR/2026_IJRR_Equivariant-diffusion-policy-for-sample-efficient-robotic/01_overview.md) — 2026 IJRR.
   - 선정 이유: 일반화 이득이 더 큰 VLA보다 대칭성 같은 inductive bias로 설명되는지 대조할 기준이다.
66. [Diagnosing Compositional Generalization in Sequential Robot Tasks](../2026/CoRL/2026_CoRL_Diagnosing-Compositional-Generalization-in-Sequential-Robo/01_overview.md) — 2026 CoRL.
   - 선정 이유: DataMIL·ReMix의 데이터 선택 흐름과 SET의 단순 분해를 연결할 instruction-coverage 선행이다. 분해 자체를 신규 기여로 주장하지 않고 학습 support를 따질 NEXT로 등록한다.
67. [A Systematic Study of Data Modalities and Strategies for Co-training Large Behavior Models for Robot Manipulation](../2026/RSS/2026_RSS_A-Systematic-Study-of-Data-Modalities-and-Strategies-for-C/01_overview.md) — 2026 RSS.
   - 선정 이유: Open X-Embodiment·DataMIL·ReMix 이후 데이터 양과 종류의 효과를 분리하는 NEXT 실증 기준이다. 새로운 아키텍처보다 데이터 구성이라는 단순 대안을 먼저 검토하게 한다.
68. [Emergence of Human to Robot Transfer in Vision-Language-Action Models](../2026/RSS/2026_RSS_Emergence-of-Human-to-Robot-Transfer-in-Vision-Language-Ac/01_overview.md) — 2026 RSS.
   - 선정 이유: Open X-Embodiment와 사람 영상 기반 로봇 학습을 잇는 NEXT 데이터 조건 연구다. Cross-embodiment 전이를 보편적 성질로 가정하지 않도록 비교 기준을 추가한다.
69. [Dejavu: Towards Experience Feedback Learning for Embodied Intelligence](../2026/CVPR/2026_CVPR_Dejavu-Towards-Experience-Feedback-Learning-for-Embodied-I/01_overview.md) — 2026 CVPR.
   - 선정 이유: Residual RL과 retrieval의 직접 결합이므로 NEXT에 추가한다. Bank 성장·frozen backbone이라는 조합 자체를 새 연구 공백으로 주장하지 않도록 현재 후보의 선행 경계를 보완한다.
70. [EXPO: Stable Reinforcement Learning with Expressive Policies](../2026/ICLR/2026_ICLR_EXPO-Stable-Reinforcement-Learning-with-Expressive-Policie/01_overview.md) — 2026 ICLR.
   - 선정 이유: Residual/editor와 value 선택을 결합한 강한 직접 baseline이다. Q 선택·base 모방·editor RL이라는 조합 자체의 신규성 주장을 막는 NEXT다.
71. [Policy Decorator: Model-Agnostic Online Refinement for Large Policy Model](../2025/ICLR/2025_ICLR_Policy-Decorator-Model-Agnostic-Online-Refinement-for-Larg/01_overview.md) — 2025 ICLR.
   - 선정 이유: Frozen large policy+bounded residual의 핵심 비교 선행이다. 현재 후보의 scalar gain·탐색 schedule이라는 단순 대안을 놓치지 않도록 NEXT에 추가한다.
72. [Accelerating Residual Reinforcement Learning With Uncertainty Estimation](../2026/RA-L/2026_RA-L_Accelerating-Residual-Reinforcement-Learning-With-Uncertai/01_overview.md) — 2026 RA-L.
   - 선정 이유: 현재 후보의 critic mismatch 대안을 검토할 직접 선행이다. 합성 행동 critic을 새 알고리즘으로 재주장하지 않도록 NEXT에 등록한다.
73. [From Prior to Pro: Efficient Skill Mastery via Distribution Contractive RL Finetuning](../2026/ICML/2026_ICML_From-Prior-to-Pro-Efficient-Skill-Mastery-via-Distribution/01_overview.md) — 2026 ICML.
   - 선정 이유: Frozen prior+residual+선택적 모방의 최신 직접 선행이다. 현재 후보의 규칙 조합만으로 독립 방법 기여를 주장하지 않도록 NEXT에 추가한다.
74. [Latent Theory of Mind: A Decentralized Diffusion Architecture for Cooperative Manipulation](../2025/CoRL/2025_CoRL_Latent-Theory-of-Mind-A-Decentralized-Diffusion-Architectu/01_overview.md) — 2025 CoRL.
   - 선정 이유: CROSSPLAY의 decentralized 협력·상대 행동 모델링은 이미 존재함을 보여 주는 CoRL 직접 선행.
75. [PolaRiS: Scalable Real-to-Sim Evaluations for Generalist Robot Policies](../2026/RSS/2026_RSS_PolaRiS-Scalable-Real-to-Sim-Evaluations-for-Generalist-Ro/01_overview.md) — 2026 RSS.
   - 선정 이유: SIMPLER·RoboCasa의 점수를 실제 개선으로 해석하기 전 필요한 평가 타당성 비교다.
76. [MolmoSpaces: Large-Scale Open Ecosystem for Robot Manipulation and Navigation](../2026/RSS/2026_RSS_MolmoSpaces-Large-Scale-Open-Ecosystem-for-Robot-Manipulat/01_overview.md) — 2026 RSS.
   - 선정 이유: 현재 후보의 한 benchmark 의존을 줄일 추가 환경·데이터 자원이다.
77. [When Life Gives You BC, Make Q-functions: Extracting Q-values from Behavior Cloning for On-Robot Reinforcement Learning](../2026/RSS/2026_RSS_When-Life-Gives-You-BC-Make-Q-functions-Extracting-Q-value/01_overview.md) — 2026 RSS.
   - 선정 이유: BC prior 보존을 새 unified objective 없이 달성하는 강한 대안이다.
78. [Long-Context Robot Imitation Learning by Focusing on Key History Frames](../2026/RSS/2026_RSS_Long-Context-Robot-Imitation-Learning-by-Focusing-on-Key-H/01_overview.md) — 2026 RSS.
   - 선정 이유: VLA memory를 늘리는 것과 필요한 정보만 남기는 것의 차이를 검증할 직접 선행이다.
79. [TMRL: Diffusion Timestep-Modulated Pretraining Enables Exploration for Efficient Policy Finetuning](../2026/RSS/2026_RSS_TMRL-Diffusion-Timestep-Modulated-Pretraining-Enables-Expl/01_overview.md) — 2026 RSS.
   - 선정 이유: VLA 내부 학습을 제안할 때 비교해야 할 사전학습 coverage·탐색 조절 대안이다.
80. [ReWiND: Language-Guided Rewards Teach Robot Policies without New Demonstrations](../2025/CoRL/2025_CoRL_ReWiND-Language-Guided-Rewards-Teach-Robot-Policies-withou/01_overview.md) — 2025 CoRL.
   - 선정 이유: 새 VLA-RL 보상이나 실패 재사용이 기존 언어 보상 일반화와 어떻게 다른지 비교할 선행이다.
81. [CoMo: Learning Continuous Latent Motion from Internet Videos for Scalable Robot Learning](../2026/CVPR/2026_CVPR_CoMo-Learning-Continuous-Latent-Motion-from-Internet-Video/01_overview.md) — 2026 CVPR.
   - 선정 이유: 행동 공간의 통합이 discrete/continuous 선택 자체의 효과인지 분리할 비교다.
82. [General Process Reward Modeling for Robotic Reinforcement Learning](../2026/CVPR/2026_CVPR_General-Process-Reward-Modeling-for-Robotic-Reinforcement/01_overview.md) — 2026 CVPR.
   - 선정 이유: VLA+RL 보상 설계와 HINDSIGHT의 대안 설명을 검토할 직접 선행이다.
83. [Lifelong Autonomous Improvement of Navigation Foundation Models in the Wild](../2024/CoRL/2024_CoRL_Lifelong-Autonomous-Improvement-of-Navigation-Foundation-M/01_overview.md) — 2024 CoRL.
   - 선정 이유: VLA+RL의 지속 학습을 manipulation에 한정하지 않고 실제 항법 운영 조건과 비교할 기준이다.
84. [Steering Your Generalists: Improving Robotic Foundation Models via Value Guidance](../2024/CoRL/2024_CoRL_Steering-Your-Generalists-Improving-Robotic-Foundation-Mod/01_overview.md) — 2024 CoRL.
   - 선정 이유: 단일 정책을 RL로 갱신하는 방법이 추론 후보 선택보다 필요한 이유를 검증할 직접 대조군이다.
85. [DEAS: DEtached value learning with Action Sequence for Scalable Offline RL](../2026/ICLR/2026_ICLR_DEAS-DEtached-value-learning-with-Action-Sequence-for-Scal/01_overview.md) — 2026 ICLR.
   - 선정 이유: Chunk-aware actor-critic과 공유 표현 연구에서 반드시 넘어야 하는 직접 offline RL 선행이다.
86. [PRIMT: Preference-based Reinforcement Learning with Multimodal Feedback and Trajectory Synthesis from Foundation Models](../2025/NeurIPS/2025_NeurIPS_PRIMT-Preference-based-Reinforcement-Learning-with-Multimo/01_overview.md) — 2025 NeurIPS.
   - 선정 이유: Hindsight 재사용과 foundation reward 결합이 이미 연구되었음을 보여 주는 비교 선행이다.
87. [RL's Razor: Why Online Reinforcement Learning Forgets Less](../2026/ICLR/2026_ICLR_RL-s-Razor-Why-Online-Reinforcement-Learning-Forgets-Less/01_overview.md) — 2026 ICLR.
   - 선정 이유: RL이 지시 능력을 잃는다는 가정을 먼저 반박할 직접 선행이며 KL 진단의 기준이다.
88. [Successor Features for Transfer in Reinforcement Learning](../2017/NeurIPS/2017_NeurIPS_Successor-Features-for-Transfer-in-Reinforcement-Learning/01_overview.md) — 2017 NeurIPS.
   - 선정 이유: 보상 전이와 로봇 동역학 전이를 혼동하지 않게 하는 명확한 이론·로봇 비교 기준이다.
89. [AWAC: Accelerating Online Reinforcement Learning with Offline Datasets](../2020/arXiv/2020_arXiv_AWAC-Accelerating-Online-Reinforcement-Learning-with-Offli/01_overview.md) — 2020 arXiv.
   - 선정 이유: RL 이득이 성공 선택이나 weighted imitation으로 설명되는지 비교할 핵심 baseline이다.
90. [DART: Noise Injection for Robust Imitation Learning](../2017/CoRL/2017_CoRL_DART-Noise-Injection-for-Robust-Imitation-Learning/01_overview.md) — 2017 CoRL.
   - 선정 이유: 복구 성공을 RL 고유 이득으로 해석하기 전 넘어야 할 강한 데이터 수집·모방 대안이다.
91. [Cal-QL: Calibrated Offline RL Pre-Training for Efficient Online Fine-Tuning](../2023/NeurIPS/2023_NeurIPS_Cal-QL-Calibrated-Offline-RL-Pre-Training-for-Efficient-On/01_overview.md) — 2023 NeurIPS.
   - 선정 이유: 초기 성능 손실을 semantic forgetting으로만 설명하지 않게 하는 critic calibration baseline이다.
92. [HIQL: Offline Goal-Conditioned RL with Latent States as Actions](../2023/NeurIPS/2023_NeurIPS_HIQL-Offline-Goal-Conditioned-RL-with-Latent-States-as-Act/01_overview.md) — 2023 NeurIPS.
   - 선정 이유: 공유 가치함수와 계층 정책을 단일 actor 공동 학습과 구별하고 장기 credit 문제의 강한 대안으로 비교한다.
93. [Is Value Learning Really the Main Bottleneck in Offline RL?](../2024/NeurIPS/2024_NeurIPS_Is-Value-Learning-Really-the-Main-Bottleneck-in-Offline-RL/01_overview.md) — 2024 NeurIPS.
   - 선정 이유: 단일 VLA critic 개선 후보가 actor 학습·coverage 효과를 놓치지 않도록 하는 핵심 원인 분석이다.
94. [Horizon Reduction Makes RL Scalable](../2025/NeurIPS/2025_NeurIPS_Horizon-Reduction-Makes-RL-Scalable/01_overview.md) — 2025 NeurIPS.
   - 선정 이유: Chunk 길이·목표 분해와 데이터 scaling의 효과를 분리할 최신 기준 연구다.
95. [EgoDex: Learning Dexterous Manipulation from Large-Scale Egocentric Video](../2026/ICLR/2026_ICLR_EgoDex-Learning-Dexterous-Manipulation-from-Large-Scale-Eg/01_overview.md) — 2026 ICLR.
   - 선정 이유: Ψ₀ 사전학습의 인간 데이터 전제이며 hand prediction과 robot closed-loop 성공을 구분할 핵심 데이터 기준이다.
96. [Humanoid Everyday: A Comprehensive Robotic Dataset for Open-World Humanoid Manipulation](../2025/arXiv/2025_arXiv_Humanoid-Everyday-A-Comprehensive-Robotic-Dataset-for-Open/01_overview.md) — 2025 arXiv.
   - 선정 이유: Ψ₀의 로봇 데이터 전제와 G1/H1 action schema를 비교하는 데 필요하며 전체 corpus와 모델 사용 subset을 구분한다.

### VLA, cross-embodiment, and long-horizon planning — 150

97. [What Can RL Bring to VLA Generalization? An Empirical Study](../2025/NeurIPS/2025_NeurIPS_What-Can-RL-Bring-to-VLA-Generalization-An-Empirical-Study/01_overview.md) — 2025 NeurIPS.
   - 선정 이유: Benchmark / empirical study. Visual·semantic·execution generalization을 나누어 SFT와 RL을 비교한다. OpenVLA/OFT 이후 RL의 효과를 주장할 때 필요한 평가 기준이다. 해당 실험에서의 PPO 결과를 모든 VLA에 대한 우열로 일반화하지 않는다.
98. [SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning](../2026/ICLR/2026_ICLR_SimpleVLA-RL-Scaling-VLA-Training-via-Reinforcement-Learni/01_overview.md) — 2026 ICLR.
   - 선정 이유: Current trend / system. OpenVLA-OFT에서 outcome reward와 scalable rollout/training을 다룬다. 현재 OFT → ConRFT 경로에 대규모 simulator RL의 비교 지점을 추가한다. Real-world 결과와 real-world online training의 범위는 구분해서 정독해야 한다.
99. [RLinf-VLA: A Unified and Efficient Framework for Reinforcement Learning of Vision-Language-Action Models](../2026/RSS/2026_RSS_RLux-VLA-A-Unified-and-Efficient-Framework-for-Reinforceme/01_overview.md) — 2026 RSS.
   - 선정 이유: Current trend / system. 여러 VLA·RL 알고리즘·시뮬레이터를 비교할 공통 interface와 resource allocation을 제공한다. SimpleVLA-RL 및 ConRFT 실험을 설계할 때 algorithm 효과와 시스템 throughput을 분리하는 데 유용하다. 공식 RSS title은 RLinf-VLA다.
100. [A Generalist Pair-wise Progress Critic Model for Vision-Language-Action Robots](../2026/ICML/2026_ICML_A-Generalist-Pair-wise-Progress-Critic-Model-for-Vision-La/01_overview.md) — 2026 ICML.
101. [Learning from Hindsight for VLA Reinforcement Learning](../2026/arXiv/2026_arXiv_Learning-from-Hindsight-for-VLA-Reinforcement-Learning/01_overview.md) — 2026 arXiv.
   - 선정 이유: 직접 선행. 실패의 보조 언어 목표와 원 지시를 공동 학습하는 LfH는 hindsight 재사용 자체의 신규성을 제한한다. 원 과제 전이를 위한 복수 valid-label 선택을 연구하기 전에 비교해야 한다. arXiv v2 기준이며 main-conference 채택은 미확인이다.
102. [CAST: Counterfactual Labels Improve Instruction Following in Vision-Language-Action Models](../2025/arXiv/2025_arXiv_CAST-Counterfactual-Labels-Improve-Instruction-Following-i/01_overview.md) — 2025 arXiv.
   - 선정 이유: VLA 언어 추종을 위한 counterfactual instruction/action 증강. 실제 실패의 참인 hindsight 목표와 실행되지 않은 합성 행동 자료의 기여를 구분하는 직접 대조다. 공식 main venue 미확인 preprint다.
103. [NaVid: Video-based VLM Plans the Next Step for Vision-and-Language Navigation](../2024/RSS/2024_RSS_NaVid-Video-based-VLM-Plans-the-Next-Step-for-Vision-and-L/01_overview.md) — 2024 RSS.
   - 선정 이유: Foundation lineage. RGB video history에서 next action을 출력하는 navigation VLM이다. Uni-NaVid/StreamVLN을 비교할 때 선행 interface를 보충한다. **NaVILA 및 Uni-NaVid와 다른 논문**이다.
104. [StreamVLN: Streaming Vision-and-Language Navigation via SlowFast Context Modeling](../2026/ICRA/2026_ICRA_StreamVLN-Streaming-Vision-and-Language-Navigation-via-Slo/01_overview.md) — 2026 ICRA.
   - 선정 이유: Current trend. Fast action context와 slow history memory를 결합한다. NaVid/Uni-NaVid 이후 긴 video history를 제한된 inference budget으로 처리하는 비교 대상이다. RL 자체의 논문으로 분류하지 않는다.
105. [SocialNav: Training Human-Inspired Foundation Model for Socially-Aware Embodied Navigation](../2026/CVPR/2026_CVPR_SocialNav-Training-Human-Inspired-Foundation-Model-for-Soc/01_overview.md) — 2026 CVPR.
   - 선정 이유: Current trend / dataset. Semantic reasoning과 trajectory generation에 socially compliant reward를 연결한다. NaVILA/VLFM의 task success 중심 비교에 행동 제약을 더한다. 기존 **SocialNav-SUB는 별도 benchmark**다.
106. [DyGRO-VLA: Cross-Task Scaling of Vision–Language–Action Models via Dynamic Grouped Residual Optimization](../2026/ICML/2026_ICML_DyGRO-VLA-Cross-Task-Scaling-of-VisionLanguageAction-Model/01_overview.md) — 2026 ICML.
   - 선정 이유: Current trend. RL fine-tuning 중 task-specific overfitting을 줄이는 것이 연구 질문일 때 RL4VLA/ConRFT와 비교한다. 새 architecture라는 이유만으로 CORE로 올리지는 않는다.
107. [CLIPort: What and Where Pathways for Robotic Manipulation](../2021/CoRL/2021_CoRL_CLIPort-What-and-Where-Pathways-for-Robotic-Manipulation/01_overview.md) — 2021 CoRL.
   - 선정 이유: CLIPort는 semantic grounding과 spatial action을 분리하는 VLA/3D manipulation의 선택적 비교 기준이다.
108. [PaLM-E: An Embodied Multimodal Language Model](../2023/ICML/2023_ICML_PaLM-E-An-Embodied-Multimodal-Language-Model/01_overview.md) — 2023 ICML.
   - 선정 이유: PaLM-E는 embodied multimodal reasoning 계보로 보존하고 직접 action/RL interface 논문 이후에 읽는다.
109. [RT-1: Robotics Transformer for Real-World Control at Scale](../2022/arXiv/2022_arxiv_RT-1-Robotics-Transformer-for-Real-World-Control-at-Scale/01_overview.md) — 2022 arXiv.
   - 선정 이유: RT-1은 RT-2·OpenVLA의 robot-data/action-token 계보를 확인할 때 읽는 기반으로 둔다.
110. [VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models](../2023/CoRL/2023_CoRL_VoxPoser-Composable-3D-Value-Maps-for-Robotic-Manipulation/01_overview.md) — 2023 CoRL.
   - 선정 이유: VoxPoser는 VLA 직접 정책과 language-conditioned 3D planning을 비교하는 전문화로 유지한다.
111. [A Generalist Agent](../2022/arXiv/2022_arXiv_A-Generalist-Agent/01_overview.md) — 2022 arXiv.
112. [AutoRT: Embodied Foundation Models for Large Scale Orchestration of Robotic Agents](../2024/arXiv/2024_arXiv_AutoRT-Embodied-Foundation-Models-for-Large-Scale-Orchestr/01_overview.md) — 2024 arXiv.
113. [RT-H: Action Hierarchies Using Language](../2024/Robotics-Science-and-Sys/2024_Robotics-Science-and-Sys_RT-H-Action-Hierarchies-Using-Language/01_overview.md) — 2024 Robotics: Science and Systems.
114. [Gemini Robotics: Bringing AI into the Physical World](../2025/arXiv/2025_arXiv_Gemini-Robotics-Bringing-AI-into-the-Physical-World/01_overview.md) — 2025 arXiv.
115. [NVIDIA Isaac GR00T N1: An Open Foundation Model for Humanoid Robots](../2025/arXiv/2025_arXiv_NVIDIA-Isaac-GR00T-N1-An-Open-Foundation-Model-for-Humanoi/01_overview.md) — 2025 arXiv.
116. [BC-Z: Zero-Shot Task Generalization with Robotic Imitation Learning](../2022/CoRL/2022_CoRL_BC-Z-Zero-Shot-Task-Generalization-with-Robotic-Imitation/01_overview.md) — 2022 CoRL.
117. [Perceiver-Actor: A Multi-Task Transformer for Robotic Manipulation](../2023/CoRL/2023_CoRL_Perceiver-Actor-A-Multi-Task-Transformer-for-Robotic-Manip/01_overview.md) — 2023 CoRL.
118. [VIMA: General Robot Manipulation with Multimodal Prompts](../2023/ICML/2023_ICML_VIMA-General-Robot-Manipulation-with-Multimodal-Prompts/01_overview.md) — 2023 ICML.
119. [Inner Monologue: Embodied Reasoning through Planning with Language Models](../2022/CoRL/2022_CoRL_Inner-Monologue-Embodied-Reasoning-through-Planning-with-L/01_overview.md) — 2022 CoRL.
120. [SayPlan: Grounding Large Language Models using 3D Scene Graphs for Scalable Robot Task Planning](../2023/CoRL/2023_CoRL_SayPlan-Grounding-Large-Language-Models-using-3D-Scene-Gra/01_overview.md) — 2023 CoRL.
121. [XSkill: Cross Embodiment Skill Discovery](../2023/CoRL/2023_CoRL_XSkill-Cross-Embodiment-Skill-Discovery/01_overview.md) — 2023 CoRL.
122. [Scaling Proprioceptive-Visual Learning with Heterogeneous Pre-trained Transformers](../2024/NeurIPS/2024_NeurIPS_Scaling-Proprioceptive-Visual-Learning-with-Heterogeneous/01_overview.md) — 2024 NeurIPS.
123. [AtomicVLA: Unlocking the Potential of Atomic Skill Learning in Robots](../2026/CVPR/2026_CVPR_AtomicVLA-Unlocking-the-Potential-of-Atomic-Skill-Learning/01_overview.md) — 2026 CVPR.
124. [PALM: Progress-Aware Policy Learning via Affordance Reasoning for Long-Horizon Robotic Manipulation](../2026/CVPR/2026_CVPR_PALM-Progress-Aware-Policy-Learning-via-Affordance-Reasoni/01_overview.md) — 2026 CVPR.
125. [ActiveVLA: Injecting Active Perception into Vision-Language-Action Models for Precise 3D Robotic Manipulation](../2026/CVPR/2026_CVPR_ActiveVLA-Injecting-Active-Perception-into-Vision-Language/01_overview.md) — 2026 CVPR.
126. [Spatial Memory for Out-of-Vision Manipulation in Vision-Language-Action](../2026/ICML/2026_ICML_Spatial-Memory-for-Out-of-Vision-Manipulation-in-Vision-La/01_overview.md) — 2026 ICML.
127. [Counterfactual VLA: Self-Reflective Vision-Language-Action Model with Adaptive Reasoning](../2026/CVPR/2026_CVPR_Counterfactual-VLA-Self-Reflective-Vision-Language-Action/01_overview.md) — 2026 CVPR.
128. [Any3D-VLA: Enhancing VLA Robustness via Diverse Point Clouds](../2026/ICML/2026_ICML_Any3D-VLA-Enhancing-VLA-Robustness-via-Diverse-Point-Cloud/01_overview.md) — 2026 ICML.
129. [MomaGraph: State-Aware Unified Scene Graphs with Vision-Language Models for Embodied Task Planning](../2026/ICLR/2026_ICLR_MomaGraph-State-Aware-Unified-Scene-Graphs-with-Vision-Lan/01_overview.md) — 2026 ICLR.
130. [AVA-VLA: Improving Vision-Language-Action Models with Active Visual Attention](../2026/CVPR/2026_CVPR_AVA-VLA-Improving-Vision-Language-Action-Models-with-Activ/01_overview.md) — 2026 CVPR.
131. [VLA-Arena: An Open-Source Framework for Benchmarking Vision-Language-Action Models](../2026/ICML/2026_ICML_VLA-Arena-An-Open-Source-Framework-for-Benchmarking-Vision/01_overview.md) — 2026 ICML.
132. [SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Models](../2025/RSS/2025_RSS_SpatialVLA-Exploring-Spatial-Representations-for-Visual-La/01_overview.md) — 2025 RSS.
133. [From Spatial to Actions: Grounding Vision-Language-Action Model in Spatial Foundation Priors](../2026/ICLR/2026_ICLR_From-Spatial-to-Actions-Grounding-Vision-Language-Action-M/01_overview.md) — 2026 ICLR.
134. [Uni-NaVid: A Video-based Vision-Language-Action Model for Unifying Embodied Navigation Tasks](../2025/RSS/2025_RSS_Uni-NaVid-A-Video-based-Vision-Language-Action-Model-for-U/01_overview.md) — 2025 RSS.
135. [Learning to Act Anywhere with Task-centric Latent Actions](../2025/RSS/2025_RSS_Learning-to-Act-Anywhere-with-Task-centric-Latent-Actions/01_overview.md) — 2025 RSS.
136. [CLIP-RT: Learning Language-Conditioned Robotic Policies from Natural Language Supervision](../2025/RSS/2025_RSS_CLIP-RT-Learning-Language-Conditioned-Robotic-Policies-fro/01_overview.md) — 2025 RSS.
137. [CodeDiffuser: Attention-Enhanced Diffusion Policy via VLM-Generated Code for Instruction Ambiguity](../2025/RSS/2025_RSS_CodeDiffuser-Attention-Enhanced-Diffusion-Policy-via-VLM-G/01_overview.md) — 2025 RSS.
138. [PartInstruct: Part-level Instruction Following for Fine-grained Robot Manipulation](../2025/RSS/2025_RSS_PartInstruct-Part-level-Instruction-Following-for-Fine-gra/01_overview.md) — 2025 RSS.
139. [Manual2Skill: Learning to Read Manuals and Acquire Robotic Skills for Furniture Assembly Using Vision-Language Models](../2025/RSS/2025_RSS_Manual2Skill-Learning-to-Read-Manuals-and-Acquire-Robotic/01_overview.md) — 2025 RSS.
140. [SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics](../2025/arXiv/2025_arXiv_SmolVLA-A-Vision-Language-Action-Model-for-Affordable-and/01_overview.md) — 2025 arXiv.
141. [Gemini Robotics 1.5: Pushing the Frontier of Generalist Robots with Advanced Embodied Reasoning, Thinking, and Motion Transfer](../2025/arXiv/2025_arXiv_Gemini-Robotics-1.5-Pushing-the-Frontier-of-Generalist-Rob/01_overview.md) — 2025 arXiv.
142. [GR00T N1.5: An Improved Open Foundation Model for Generalist Humanoid Robots](../2025/Technical-Report/2025_Technical-Report_GR00T-N1.5-An-Improved-Open-Foundation-Model-for-Generalis/01_overview.md) — 2025 Technical Report.
143. [GR00T N1.6: An Improved Open Foundation Model for Generalist Humanoid Robots](../2025/Technical-Report/2025_Technical-Report_GR00T-N1.6-An-Improved-Open-Foundation-Model-for-Generalis/01_overview.md) — 2025 Technical Report.
144. [Grounding Actions in Camera Space: Observation-Centric Vision-Language-Action Policy](../2026/AAAI/2026_AAAI_Grounding-Actions-in-Camera-Space-Observation-Centric-Visi/01_overview.md) — 2026 AAAI.
145. [ReKep: Spatio-Temporal Reasoning of Relational Keypoint Constraints for Robotic Manipulation](../2024/CoRL/2024_CoRL_ReKep-Spatio-Temporal-Reasoning-of-Relational-Keypoint-Con/01_overview.md) — 2024 CoRL.
146. [VoxAct-B: Voxel-Based Acting and Stabilizing Policy for Bimanual Manipulation](../2024/CoRL/2024_CoRL_VoxAct-B-Voxel-Based-Acting-and-Stabilizing-Policy-for-Bim/01_overview.md) — 2024 CoRL.
147. [3DS-VLA: A 3D Spatial-Aware Vision Language Action Model for Robust Multi-Task Manipulation](../2025/CoRL/2025_CoRL_3DS-VLA-A-3D-Spatial-Aware-Vision-Language-Action-Model-fo/01_overview.md) — 2025 CoRL.
148. [GraspVLA: a Grasping Foundation Model Pre-trained on Billion-scale Synthetic Action Data](../2025/CoRL/2025_CoRL_GraspVLA-a-Grasping-Foundation-Model-Pre-trained-on-Billio/01_overview.md) — 2025 CoRL.
149. [Long-VLA: Unleashing Long-Horizon Capability of Vision Language Action Model for Robot Manipulation](../2025/CoRL/2025_CoRL_Long-VLA-Unleashing-Long-Horizon-Capability-of-Vision-Lang/01_overview.md) — 2025 CoRL.
150. [RDT-1B: a Diffusion Foundation Model for Bimanual Manipulation](../2025/ICLR/2025_ICLR_RDT-1B-a-Diffusion-Foundation-Model-for-Bimanual-Manipulat/01_overview.md) — 2025 ICLR.
151. [AHA: A Vision-Language-Model for Detecting and Reasoning Over Failures in Robotic Manipulation](../2025/ICLR/2025_ICLR_AHA-A-Vision-Language-Model-for-Detecting-and-Reasoning-Ov/01_overview.md) — 2025 ICLR.
152. [SIMPACT: Simulation-Enabled Action Planning using Vision-Language Models](../2026/CVPR/2026_CVPR_SIMPACT-Simulation-Enabled-Action-Planning-using-Vision-La/01_overview.md) — 2026 CVPR.
153. [Vision-Language Foundation Models as Effective Robot Imitators](../2024/ICLR/2024_ICLR_Vision-Language-Foundation-Models-as-Effective-Robot-Imita/01_overview.md) — 2024 ICLR.
154. [Unleashing Large-Scale Video Generative Pre-training for Visual Robot Manipulation](../2024/ICLR/2024_ICLR_Unleashing-Large-Scale-Video-Generative-Pre-training-for-V/01_overview.md) — 2024 ICLR.
155. [RoboMamba: Efficient Vision-Language-Action Model for Robotic Reasoning and Manipulation](../2024/NeurIPS/2024_NeurIPS_RoboMamba-Efficient-Vision-Language-Action-Model-for-Robot/01_overview.md) — 2024 NeurIPS.
156. [Latent Action Pretraining from Videos](../2025/ICLR/2025_ICLR_Latent-Action-Pretraining-from-Videos/01_overview.md) — 2025 ICLR.
157. [3D-VLA: A 3D Vision-Language-Action Generative World Model](../2024/ICML/2024_ICML_3D-VLA-A-3D-Vision-Language-Action-Generative-World-Model/01_overview.md) — 2024 ICML.
158. [VLMimic: Vision Language Models are Visual Imitation Learner for Fine-grained Actions](../2024/NeurIPS/2024_NeurIPS_VLMimic-Vision-Language-Models-are-Visual-Imitation-Learne/01_overview.md) — 2024 NeurIPS.
159. [MIRAGE: Cross-Embodiment Zero-Shot Policy Transfer with Cross-Painting](../2024/RSS/2024_RSS_MIRAGE-Cross-Embodiment-Zero-Shot-Policy-Transfer-with-Cro/01_overview.md) — 2024 RSS.
160. [Pushing the Limits of Cross-Embodiment Learning for Manipulation and Navigation](../2024/RSS/2024_RSS_Pushing-the-Limits-of-Cross-Embodiment-Learning-for-Manipu/01_overview.md) — 2024 RSS.
161. [LIBERO-Safety: A Comprehensive Benchmark for Physical and Semantic Safety in Vision-Language-Action Models](../2026/ECCV/2026_ECCV_LIBERO-Safety-A-Comprehensive-Benchmark-for-Physical-and-S/01_overview.md) — 2026 ECCV.
162. [DISC: Decoupling Instruction from State-Conditioned Control via Policy Generation](../2026/RSS/2026_RSS_DISC-Decoupling-Instruction-from-State-Conditioned-Control/01_overview.md) — 2026 RSS.
   - 선정 이유: OpenVLA 이후 language-conditioned 행동 여부를 확인할 직접 비교군이므로 NEXT다.
163. [How Should Vision-Language-Action Models Use Proprioceptive State?](../2026/arXiv/2026_arXiv_How-Should-Vision-Language-Action-Models-Use-Proprioceptiv/01_overview.md) — 2026 arXiv.
   - 선정 이유: D1에서 state 사용과 history 효과를 먼저 입증할 NEXT prerequisite다.
164. [Self-Adaptive VLA for Robust Robot Deployment](../2026/arXiv/2026_arXiv_Self-Adaptive-VLA-for-Robust-Robot-Deployment/01_overview.md) — 2026 arXiv.
   - 선정 이유: D1의 hardware-cause adaptation과 가장 가까운 NEXT 비교군이다.
165. [ReViP: Mitigating False Completion in Vision-Language-Action Models with Vision-Proprioception Rebalance](../2026/arXiv/2026_arXiv_ReViP-Mitigating-False-Completion-in-Vision-Language-Actio/01_overview.md) — 2026 arXiv.
   - 선정 이유: D1에서 단순 vision 강화나 stage feedback을 새 기여로 재주장하지 않게 하는 NEXT다.
166. [CoRE-VLA: Towards Scalable and Robust Vision-Language-Action Modeling via Conditional Routing of Experts](../2026/arXiv/2026_arXiv_CoRE-VLA-Towards-Scalable-and-Robust-Vision-Language-Actio/01_overview.md) — 2026 arXiv.
   - 선정 이유: D1의 modality robustness와 직접 겹치는 NEXT다. 카메라 복원 CoRe-VLA와 다른 논문이다.
167. [CoRe-VLA: Preserving Cross-View Coordination in VLAs under Camera Shifts](../2026/arXiv/2026_arXiv_CoRe-VLA-Preserving-Cross-View-Coordination-in-VLAs-under/01_overview.md) — 2026 arXiv.
   - 선정 이유: D1 camera-shift 보정의 직접 NEXT baseline이다. Conditional Routing CoRE-VLA와 별도 identity다.
168. [When would Vision-Proprioception Policies Fail in Robotic Manipulation?](../2026/ICLR/2026_ICLR_When-would-Vision-Proprioception-Policies-Fail-in-Robotic/01_overview.md) — 2026 ICLR.
   - 선정 이유: D1에서 modality dominance를 새 발견으로 주장하지 않도록 추가한 직접 NEXT다.
169. [Pretrained Vision-Language-Action Models are Surprisingly Resistant to Forgetting in Continual Learning](../2026/ICML/2026_ICML_Pretrained-Vision-Language-Action-Models-are-Surprisingly/01_overview.md) — 2026 ICML.
   - 선정 이유: E1에서 복잡한 replay selector 전에 확인할 강한 단순 기준이다. NEXT: 현재 VLA 정독 흐름의 직접 비교·평가 기준으로 편입한다.
170. [Actions as Language: Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting](../2026/ICLR/2026_ICLR_Actions-as-Language-Fine-Tuning-VLMs-into-VLAs-Without-Cat/01_overview.md) — 2026 ICLR.
   - 선정 이유: 의미 능력 보존이라는 넓은 방향의 직접 선행이며 action interface 비교에도 필요하다. NEXT: 현재 VLA 정독 흐름의 직접 비교·평가 기준으로 편입한다.
171. [LAP: Language-Action Pre-training Enables Zero-Shot Cross-Embodiment Transfer](../2026/RSS/2026_RSS_LAP-Language-Action-Pre-training-Enables-Zero-Shot-Cross-E/01_overview.md) — 2026 RSS.
   - 선정 이유: Cross-embodiment VLA interface를 비교할 최신 직접 선행이다. NEXT: 현재 VLA 정독 흐름의 직접 비교·평가 기준으로 편입한다.
172. [Adaptive Action Chunking at Inference-time for Vision-Language-Action Models](../2026/CVPR/2026_CVPR_Adaptive-Action-Chunking-at-Inference-time-for-Vision-Lang/01_overview.md) — 2026 CVPR.
   - 선정 이유: E2의 adaptive horizon 주장에 대한 직접 baseline이다. NEXT: 현재 VLA 정독 흐름의 직접 비교·평가 기준으로 편입한다.
173. [Memory Anchors for Continual Robot Learning](../2026/CoRL/2026_CoRL_Memory-Anchors-for-Continual-Robot-Learning/01_overview.md) — 2026 CoRL.
   - 선정 이유: E1의 action-conflict replay와 가장 가까운 직접 비교군이다. NEXT: 현재 VLA 정독 흐름의 직접 비교·평가 기준으로 편입한다.
174. [Rethinking Visual-Language-Action Model Scaling: Alignment, Mixture, and Regularization](../2026/arXiv/2026_arXiv_Rethinking-Visual-Language-Action-Model-Scaling-Alignment/01_overview.md) — 2026 arXiv.
   - 선정 이유: E1에서 정상 action 정렬·mixture 자체의 설명력을 먼저 제거할 기준이다. NEXT: 현재 VLA 정독 흐름의 직접 비교·평가 기준으로 편입한다.
175. [Can Vision-Language-Action Models Learn from Real-World Data Continually without Forgetting?](../2026/arXiv/2026_arXiv_Can-Vision-Language-Action-Models-Learn-from-Real-World-Da/01_overview.md) — 2026 arXiv.
   - 선정 이유: E1의 실환경 단순 baseline과 compute-matched 비교에 필요한 연구다. NEXT: 현재 VLA 정독 흐름의 직접 비교·평가 기준으로 편입한다.
176. [SPACE: Enabling Learning from Cross-Robot Data Toward Generalist Policies](../2026/arXiv/2026_arXiv_SPACE-Enabling-Learning-from-Cross-Robot-Data-Toward-Gener/01_overview.md) — 2026 arXiv.
   - 선정 이유: E1/E2에서 정상적인 state-effect 표현과 dynamics adapter의 강한 대안이다. NEXT: 현재 VLA 정독 흐름의 직접 비교·평가 기준으로 편입한다.
177. [Real-Time Execution of Action Chunking Flow Policies](../2025/NeurIPS/2025_NeurIPS_Real-Time-Execution-of-Action-Chunking-Flow-Policies/01_overview.md) — 2025 NeurIPS.
   - 선정 이유: 초기 지연 후보와 E2가 반드시 비교할 표준 실행 baseline이다. NEXT: 현재 VLA 정독 흐름의 직접 비교·평가 기준으로 편입한다.
178. [Learning High-Frequency Continuous Action Chunks in Latent Space](../2026/ICML/2026_ICML_Learning-High-Frequency-Continuous-Action-Chunks-in-Latent/01_overview.md) — 2026 ICML.
   - 선정 이유: E2에서 고주파 표현과 controller 변경을 분리할 직접 기준이다. NEXT: 현재 VLA 정독 흐름의 직접 비교·평가 기준으로 편입한다.
179. [CounterAlign: Counterfactual Supervision for Vision-Language-Action Models](../2026/CoRL/2026_CoRL_CounterAlign-Counterfactual-Supervision-for-Vision-Languag/01_overview.md) — 2026 CoRL.
   - 선정 이유: C2와 새로운 VLA 탐색에서 지시 준수 개선의 직접 baseline이다. NEXT: 현재 VLA 정독 흐름의 직접 비교·평가 기준으로 편입한다.
180. [Mechanistic Interpretability for Steering Vision-Language-Action Models](../2025/CoRL/2025_CoRL_Mechanistic-Interpretability-for-Steering-Vision-Language/01_overview.md) — 2025 CoRL.
   - 선정 이유: Instruction 대응이나 VLA 행동 교정을 연구할 때 fine-tuning 없는 직접 baseline이다.
181. [LIBERO-Plus: A Progressive Robustness Benchmark for Visual-Language-Action Models](../2026/CVPR/2026_CVPR_LIBERO-Plus-A-Progressive-Robustness-Benchmark-for-Visual/01_overview.md) — 2026 CVPR.
   - 선정 이유: 기본 성공률과 일반화 성능을 구분하는 현재 VLA 평가의 직접 기준이다.
182. [THE COLOSSEUM: A Benchmark for Evaluating Generalization for Robotic Manipulation](../2024/RSS/2024_RSS_THE-COLOSSEUM-A-Benchmark-for-Evaluating-Generalization-fo/01_overview.md) — 2024 RSS.
   - 선정 이유: LIBERO 계열에 한정하지 않고 manipulation 일반화를 점검할 benchmark 계보다.
183. [RoboMME: Benchmarking and Understanding Memory for Robotic Generalist Policies](../2026/ICML/2026_ICML_RoboMME-Benchmarking-and-Understanding-Memory-for-Robotic/01_overview.md) — 2026 ICML.
   - 선정 이유: 현재 GAP-N1–N3의 직접 benchmark이며 memory 필요성과 단순 정보 누설을 구분하는 기준이다.
184. [Beyond Sight: Finetuning Generalist Robot Policies with Heterogeneous Sensors via Language Grounding](../2025/ICRA/2025_ICRA_Beyond-Sight-Finetuning-Generalist-Robot-Policies-with-Het/01_overview.md) — 2025 ICRA.
   - 선정 이유: 새 sensor 결합을 연구할 때 naive finetuning·masked training과 함께 대조할 직접 기준이다.
185. [RoboArena: Distributed Real-World Evaluation of Generalist Robot Policies](../2025/CoRL/2025_CoRL_RoboArena-Distributed-Real-World-Evaluation-of-Generalist/01_overview.md) — 2025 CoRL.
   - 선정 이유: LIBERO-Plus·THE COLOSSEUM의 고정 benchmark와 구별되는 실환경 평가 기준을 보완한다.
186. [A Taxonomy for Evaluating Generalist Robot Manipulation Policies](../2026/RA-L/2026_RA-L_A-Taxonomy-for-Evaluating-Generalist-Robot-Manipulation-Po/01_overview.md) — 2026 RA-L.
   - 선정 이유: VLA 일반화 주장을 시각 변화·언어 이해·행동 변화로 분해할 평가 formulation이다.
187. [Gen2Act: Human Video Generation in Novel Scenarios enables Generalizable Robot Manipulation](../2025/CoRL/2025_CoRL_Gen2Act-Human-Video-Generation-in-Novel-Scenarios-enables/01_overview.md) — 2025 CoRL.
   - 선정 이유: VLA의 video prior가 action supervision을 어떻게 보완하는지 비교할 직접 선행이다.
188. [Mobility VLA: Multimodal Instruction Navigation with Long-Context VLMs and Topological Graphs](../2025/CoRL/2025_CoRL_Mobility-VLA-Multimodal-Instruction-Navigation-with-Long-C/01_overview.md) — 2025 CoRL.
   - 선정 이유: NaVILA·NoMaD와 비교할 계층형 VLA navigation 및 환경 사전정보 기준이다.
189. [Behavior-Skill: A Fine-Grained Benchmark for Evaluating Vision-Language-Action Policies in Long-Horizon Tasks](../2026/arXiv/2026_arXiv_Behavior-Skill-A-Fine-Grained-Benchmark-for-Evaluating-Vis/01_overview.md) — 2026 arXiv.
   - 선정 이유: 현재 HANDOFF P0의 직접적인 benchmark/source prerequisite다. 전체 task 성공률과 독립 skill 능력의 차이를 읽을 NEXT로 추가하되 preprint status를 유지한다.
190. [ReSteer: Quantifying and Refining the Steerability of Multitask Robot Policies](../2026/RSS/2026_RSS_ReSteer-Quantifying-and-Refining-the-Steerability-of-Multi/01_overview.md) — 2026 RSS.
   - 선정 이유: 현재 부분 지시 수정 후보의 기본 switching 선행이자 최소 실행의 직접 prerequisite다. 단순 task switch나 행동 큐 교체를 신규 기여로 삼지 않도록 NEXT에 추가한다.
191. [Causeway: Restoring Task Accessibility for Instruction Switching in VLA Policies](../2026/arXiv/2026_arXiv_Causeway-Restoring-Task-Accessibility-for-Instruction-Swit/01_overview.md) — 2026 arXiv.
   - 선정 이유: 전환 실패를 의미 기억 오류로 오인하지 않기 위한 직접 경쟁 설명이다. 새 목표의 물리적 실행 가능성과 언어 해석을 분리할 NEXT로 추가하며 preprint status를 유지한다.
192. [Do VLAs Really Follow Instructions? Diagnosing How-Level Instruction Following in Vision-Language-Action Models](../2026/arXiv/2026_arXiv_Do-VLAs-Really-Follow-Instructions-Diagnosing-How-Level-In/01_overview.md) — 2026 arXiv.
   - 선정 이유: 현재 제약 유지·철회 후보에서 지시 반응, 목표 성공, 제약 준수를 분리할 직접 진단 선행이다. 평가 정의 자체를 새 기여로 과장하지 않기 위한 NEXT이며 preprint로 둔다.
193. [ClevrSkills: Compositional Language And Visual Reasoning in Robotics](../2024/NeurIPS/2024_NeurIPS_ClevrSkills-Compositional-Language-And-Visual-Reasoning-in/01_overview.md) — 2024 NeurIPS.
   - 선정 이유: VIMA·VLABench와 함께 집합/수량 후보의 기존 조합 task와 평가 predicate를 이해할 NEXT benchmark다. 여러 물체 처리·나열 표현 자체를 새 기여로 삼지 않도록 등록한다.
194. [Spa-Bench: A Real-Robot Benchmark for Spatial Grounding in Vision-Language-Action Models](../2026/arXiv/2026_arXiv_Spa-Bench-A-Real-Robot-Benchmark-for-Spatial-Grounding-in/01_overview.md) — 2026 arXiv.
   - 선정 이유: 집합·수량 후보의 가장 직접적인 counting/직접 지시 비교 선행이다. 알려진 공간 grounding 실패를 새 공백으로 과장하지 않도록 NEXT에 등록하며 preprint 경계를 유지한다.
195. [RICL: Adding In-Context Adaptability to Pre-Trained Vision-Language-Action Models](../2025/CoRL/2025_CoRL_RICL-Adding-In-Context-Adaptability-to-Pre-Trained-Vision/01_overview.md) — 2025 CoRL.
   - 선정 이유: OpenVLA·π0 계열의 후학습과 시연 검색을 잇는 직접 선행이다. 현재 bank 확장 질문에서 이미 알려진 ICL 능력·검색 이득을 신규성으로 재주장하지 않도록 NEXT로 등록한다.
196. [Scaling up Memory for Robotic Control via Experience Retrieval](../2026/ICLR/2026_ICLR_Scaling-up-Memory-for-Robotic-Control-via-Experience-Retri/01_overview.md) — 2026 ICLR.
   - 선정 이유: MemoryVLA와 계층 정책의 관계를 구체화하는 NEXT다. 외부 시연 검색과 실행 중 기억을 구분하고 SET의 counting 선행을 보완한다.
197. [LIBERO-X: Robustness Litmus for Vision-Language-Action Models](../2026/RSS/2026_RSS_LIBERO-X-Robustness-Litmus-for-Vision-Language-Action-Mode/01_overview.md) — 2026 RSS.
   - 선정 이유: LIBERO·LIBERO-Plus·VLABench 이후 복합 shift와 목표 다양성을 비교할 NEXT benchmark다. 같은 scene의 다른 goal을 다루는 연구에서 기존 평가 범위를 확인하는 데 필요하다.
198. [Learning Native Continuation for Action Chunking Flow Policies](../2026/RSS/2026_RSS_Learning-Native-Continuation-for-Action-Chunking-Flow-Poli/01_overview.md) — 2026 RSS.
   - 선정 이유: ACT·Diffusion Policy와 RTC 이후 action interface를 이해할 NEXT다. Chunk queue나 지연으로 생긴 차이를 새로운 지시 이해/검색 효과로 혼동하지 않게 한다.
199. [Stable Language Guidance for Vision–Language–Action Models](../2026/ACL/2026_ACL_Stable-Language-Guidance-for-VisionLanguageAction-Models/01_overview.md) — 2026 ACL.
   - 선정 이유: 지시 수정·집합 지시·시연 검색 후보가 공유하는 언어 민감성의 NEXT 직접 대안이다. 같은 의미의 표현 차이를 새로운 task conflict로 해석하지 않도록 등록한다.
200. [Self-Improving Vision-Language-Action Models with Data Generation via Residual RL](../2026/ICLR/2026_ICLR_Self-Improving-Vision-Language-Action-Models-with-Data-Gen/01_overview.md) — 2026 ICLR.
   - 선정 이유: VLA의 residual 개선→데이터 생성→base 갱신을 잇는 직접 선행이다. 현재 후보에서 이 루프 자체를 새 기여로 주장하지 않도록 NEXT에 추가한다.
201. [Object-Centric Residual RL for Zero-Shot Sim-to-Real VLA Enhancement](../2026/CoRL/2026_CoRL_Object-Centric-Residual-RL-for-Zero-Shot-Sim-to-Real-VLA-E/01_overview.md) — 2026 CoRL.
   - 선정 이유: Object-centric residual의 전이를 이미 다룬 직접 충돌 선행이다. 다양한 로봇·base 갱신 전이와 sim-to-real 전이를 구분할 NEXT다.
202. [EXPO-FT: Sample-Efficient Reinforcement Learning Finetuning for Vision-Language-Action Models](../2026/CoRL/2026_CoRL_EXPO-FT-Sample-Efficient-Reinforcement-Learning-Finetuning/01_overview.md) — 2026 CoRL.
   - 선정 이유: 현재 VLA+RL 후보의 가장 가까운 공동 적응 baseline이다. 독립 base 갱신과 editor 공동 학습을 구별할 NEXT다.
203. [Beyond Appearance Shifts: Task-Semantic Action Calibration for VLA Models](../2026/NeurIPS/2026_NeurIPS_Beyond-Appearance-Shifts-Task-Semantic-Action-Calibration/01_overview.md) — 2026 NeurIPS.
   - 선정 이유: REVISION·FEEDBACK·residual 보정의 직접 충돌 선행. 변화에 반응하고 nuisance에 불변이라는 broad proposal의 재발명을 막는다.
204. [Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models](../2026/NeurIPS/2026_NeurIPS_Not-All-Features-Are-Created-Equal-A-Mechanistic-Study-of/01_overview.md) — 2026 NeurIPS.
   - 선정 이유: FEEDBACK의 출발 근거이자 과장 방지 선행. Activation replay 결과와 자연 정책의 closed-loop 행동을 구별하는 NEXT.
205. [Embodied Interpretability: Linking Causal Understanding to Generalization in Vision-Language-Action Models](../2026/ICML/2026_ICML_Embodied-Interpretability-Linking-Causal-Understanding-to/01_overview.md) — 2026 ICML.
   - 선정 이유: FEEDBACK에서 attribution 자체를 새 기여로 주장하지 않도록 하는 직접 진단 baseline.
206. [RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models](../2025/arXiv/2025_arXiv_RobustVLA-Robustness-Aware-Reinforcement-Post-Training-for/01_overview.md) — 2025 arXiv.
   - 선정 이유: FEEDBACK에서 단순 Jacobian 억제·강건 RL을 새 방법으로 제안하지 않도록 하는 직접 비교.
207. [CHORUS: Decentralized Multi-Embodiment Collaboration with One VLA Policy](../2026/arXiv/2026_arXiv_CHORUS-Decentralized-Multi-Embodiment-Collaboration-with-O/01_overview.md) — 2026 arXiv.
   - 선정 이유: CROSSPLAY에서 여러 embodiment·local-only 협력 자체를 새 기여로 주장하지 않도록 하는 직접 선행.
208. [Cooperative Multi-Agent Vision-Language-Action Models via Reinforced Fine Tuning](../2026/arXiv/2026_arXiv_Cooperative-Multi-Agent-Vision-Language-Action-Models-via/01_overview.md) — 2026 arXiv.
   - 선정 이유: CROSSPLAY에서 VLA+MARL 결합 자체의 신규성을 배제하는 가장 가까운 RL 선행.
209. [RA-VLA: Retrieval-Augmented VLA for Test-Time Adaptation](../2026/ICML/2026_ICML_RA-VLA-Retrieval-Augmented-VLA-for-Test-Time-Adaptation/01_overview.md) — 2026 ICML.
   - 선정 이유: RETRIEVAL 후보의 semantic retrieval·execution 결합이라는 넓은 주장이 이미 존재함을 확인하는 ICML 직접 선행.
210. [When Does Retrieval Help? A Study of In-Context Adaptation in Vision-Language-Action Models](../2026/arXiv/2026_arXiv_When-Does-Retrieval-Help-A-Study-of-In-Context-Adaptation/01_overview.md) — 2026 arXiv.
   - 선정 이유: RETRIEVAL의 가장 직접적인 진단 선행으로, 단순 cross-task interference 발견만으로 기여를 주장하지 않게 한다.
211. [Beyond Reconstruction: What Matters in Action Tokenization for Robot Policies?](../2026/arXiv/2026_arXiv_Beyond-Reconstruction-What-Matters-in-Action-Tokenization/01_overview.md) — 2026 arXiv.
   - 선정 이유: CODEC1의 broad motivation과 prefix/replanning confound를 가장 직접적으로 제한하는 선행.
212. [LongNav-R1: Horizon-Adaptive Multi-Turn RL for Long-Horizon VLA Navigation](../2026/RSS/2026_RSS_LongNav-R1-Horizon-Adaptive-Multi-Turn-RL-for-Long-Horizon/01_overview.md) — 2026 RSS.
   - 선정 이유: 조작에서 설계한 VLA+RL 목적함수가 항법의 긴 시간축에도 유효한지 비교할 직접 선행이다.
213. [Visual Verification Enables Inference-time Steering and Autonomous Policy Improvement](../2026/RSS/2026_RSS_Visual-Verification-Enables-Inference-time-Steering-and-Au/01_overview.md) — 2026 RSS.
   - 선정 이유: RL 자체의 기여를 주장할 때 반드시 비교할 자율 데이터 선택·모방 대안이다.
214. [Towards Long-Lived Robots: Continual Learning VLA Models via Reinforcement Fine-Tuning](../2026/RSS/2026_RSS_Towards-Long-Lived-Robots-Continual-Learning-VLA-Models-vi/01_overview.md) — 2026 RSS.
   - 선정 이유: 환경 return 최적화와 참조 행동 기반 RLVR을 구별하기 위한 직접 비교다.
215. [LDA-1B: Scaling Latent Dynamics Action Model via Universal Embodied Data Ingestion](../2026/RSS/2026_RSS_LDA-1B-Scaling-Latent-Dynamics-Action-Model-via-Universal/01_overview.md) — 2026 RSS.
   - 선정 이유: 단일 모델의 행동·세계 예측 공유를 새 기여로 제안하기 전에 비교할 핵심 구조다.
216. [ControlVLA: Few-shot Object-centric Adaptation for Pre-trained Vision-Language-Action Models](../2025/CoRL/2025_CoRL_ControlVLA-Few-shot-Object-centric-Adaptation-for-Pre-trai/01_overview.md) — 2025 CoRL.
   - 선정 이유: RL이 반드시 필요한지를 판단할 저데이터 SFT·표현 적응 비교다.
217. [SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models](../2026/CVPR/2026_CVPR_SRPO-Self-Referential-Policy-Optimization-for-Vision-Langu/01_overview.md) — 2026 CVPR.
   - 선정 이유: HINDSIGHT의 실패 재사용이 이미 존재하는 self-reference reward shaping과 다른지 검토할 직접 선행이다.
218. [Joint-Aligned Latent Action: Towards Scalable VLA Pretraining in the Wild](../2026/CVPR/2026_CVPR_Joint-Aligned-Latent-Action-Towards-Scalable-VLA-Pretraini/01_overview.md) — 2026 CVPR.
   - 선정 이유: Unified VLA-RL의 action representation 기여를 판단할 사전학습 비교 기준이다.
219. [RehearseVLA: Simulated Post-Training for VLAs with Physically-Consistent World Model](../2026/CVPR/2026_CVPR_RehearseVLA-Simulated-Post-Training-for-VLAs-with-Physical/01_overview.md) — 2026 CVPR.
   - 선정 이유: VLAW 등과 함께 imagined rollout으로 실제 interaction을 대체하는 직접 비교 기준이다.
220. [Contrast Sets for Evaluating Language-Guided Robot Policies](../2024/CoRL/2024_CoRL_Contrast-Sets-for-Evaluating-Language-Guided-Robot-Policie/01_overview.md) — 2024 CoRL.
   - 선정 이유: VLA+RL 개선이 언어 민감도까지 바꾸는지 적은 실행으로 진단할 평가 설계의 선행이다.
221. [Fast-ThinkAct: Efficient Vision-Language-Action Reasoning via Verbalizable Latent Planning](../2026/CVPR/2026_CVPR_Fast-ThinkAct-Efficient-Vision-Language-Action-Reasoning-v/01_overview.md) — 2026 CVPR.
   - 선정 이유: RL reasoning의 이득을 긴 텍스트 출력 없이 행동에 전달하는 대안으로 비교한다.
222. [MM-ACT: Learn from Multimodal Parallel Generation to Act](../2026/CVPR/2026_CVPR_MM-ACT-Learn-from-Multimodal-Parallel-Generation-to-Act/01_overview.md) — 2026 CVPR.
   - 선정 이유: 하나의 VLA 내부 통합을 설계할 architecture 선행이며 RL objective 통합 효과로 해석하지 않는다.
223. [EvoVLA: Self-evolving Vision-Language-Action Model](../2026/ECCV/2026_ECCV_EvoVLA-Self-evolving-Vision-Language-Action-Model/01_overview.md) — 2026 ECCV.
   - 선정 이유: VLA+RL 보상 개선에서 이미 다룬 near-miss 구분과 실제 물리 완료의 선행이다.
224. [Restoring Linguistic Grounding in VLA Models via Train-Free Attention Recalibration](../2026/ECCV/2026_ECCV_Restoring-Linguistic-Grounding-in-VLA-Models-via-Train-Fre/01_overview.md) — 2026 ECCV.
   - 선정 이유: RL 이후 성공률이 언어 grounding을 보장하지 않는다는 직접 평가·간단 대안이다.
225. [VLA-R1: Enhancing Reasoning in Vision-Language-Action Models](../2026/ECCV/2026_ECCV_VLA-R1-Enhancing-Reasoning-in-Vision-Language-Action-Model/01_overview.md) — 2026 ECCV.
   - 선정 이유: VLA의 RL이 환경 return이 아닌 검증 가능한 중간 출력 보상일 때의 직접 비교 기준이다.
226. [MobileVLA-R1: Reinforcing Vision-Language-Action for Mobile Robots](../2026/ECCV/2026_ECCV_MobileVLA-R1-Reinforcing-Vision-Language-Action-for-Mobile/01_overview.md) — 2026 ECCV.
   - 선정 이유: Manipulation 외에 단일 VLA 후학습을 검토할 모바일 로봇 선행이다.
227. [Scaling Verification Can Be More Effective than Scaling Policy Learning for Vision-Language-Action Alignment](../2026/ECCV/2026_ECCV_Scaling-Verification-Can-Be-More-Effective-than-Scaling-Po/01_overview.md) — 2026 ECCV.
   - 선정 이유: 정책 RL 갱신의 필요성을 검증할 강한 추론 계산량·검증 대안이다.
228. [GRAD-NAV++: Vision-Language Model Enabled Visual Drone Navigation With Gaussian Radiance Fields and Differentiable Dynamics](../2026/RA-L/2026_RA-L_GRAD-NAV%2B%2B-Vision-Language-Model-Enabled-Visual-Drone-Navi/01_overview.md) — 2026 RA-L.
   - 선정 이유: 언어·시각·행동과 differentiable RL을 결합한 직접 항법 선행이다. 기존 GRaD-Nav의 언어 조건부 확장이라 별도 등록한다.
229. [TacCoRL: Integrating Tactile Feedback into VLA via Simulation](../2026/arXiv/2026_arXiv_TacCoRL-Integrating-Tactile-Feedback-into-VLA-via-Simulati/01_overview.md) — 2026 arXiv.
   - 선정 이유: 촉각 추가와 단일 VLA RL 자체가 이미 선행임을 확인할 직접 비교다.
230. [CompVLA: A Variable Compliance Vision-Language-Action Model for Contact-rich Manipulation](../2026/arXiv/2026_arXiv_CompVLA-A-Variable-Compliance-Vision-Language-Action-Model/01_overview.md) — 2026 arXiv.
   - 선정 이유: 강성 출력을 VLA에 추가하는 것 자체의 신규성을 배제할 직접 선행이다.
231. [TORL-VLA: Tactile Guided Online Reinforcement Learning for Contact-Rich Manipulation](../2026/arXiv/2026_arXiv_TORL-VLA-Tactile-Guided-Online-Reinforcement-Learning-for/01_overview.md) — 2026 arXiv.
   - 선정 이유: 접촉 VLA의 online RL과 사람 개입 credit 처리가 이미 다뤄졌음을 확인할 비교다.
232. [ForceRFT: Refining VLA Actions through Force-Guided Residual Reinforcement Learning](../2026/arXiv/2026_arXiv_ForceRFT-Refining-VLA-Actions-through-Force-Guided-Residua/01_overview.md) — 2026 arXiv.
   - 선정 이유: RL 이득이 성공 데이터 선택·추가 imitation으로 설명되는지 판단할 직접 선행이다.
233. [Facet-0: A Robotic Foundation Model for Contact-Rich Precise Manipulation](../2026/arXiv/2026_arXiv_Facet-0-A-Robotic-Foundation-Model-for-Contact-Rich-Precis/01_overview.md) — 2026 arXiv.
   - 선정 이유: Action–wrench 예측·가치·RL 결합 자체의 중복을 점검할 직접 경쟁 선행이다.
234. [πRL: Online RL Fine-tuning for Flow-based Vision-Language-Action Models](../2025/arXiv/2025_arXiv_piRL-Online-RL-Fine-tuning-for-Flow-based-Vision-Language/01_overview.md) — 2025 arXiv.
   - 선정 이유: 현재 π₀ Flow-SDE/PPO backend의 likelihood·탐색 정의를 이해할 직접 prerequisite다.
235. [Breaking Lock-In: Preserving Steerability under Low-Data VLA Post-Training](../2026/arXiv/2026_arXiv_Breaking-Lock-In-Preserving-Steerability-under-Low-Data-VL/01_overview.md) — 2026 arXiv.
   - 선정 이유: 단순히 지시 보존·semantic freezing을 도입하는 것을 새 연구 기여로 주장하지 않도록 한다.
236. [TEMPO: Semantic-Action Decoupled RL Post-Training for Vision-Language-Action Models](../2026/arXiv/2026_arXiv_TEMPO-Semantic-Action-Decoupled-RL-Post-Training-for-Visio/01_overview.md) — 2026 arXiv.
   - 선정 이유: 단일 VLA 내부의 의미 보존과 모듈별 RL 갱신에 관한 직접 경쟁 선행이다.
237. [When Vision Overrides Language: Evaluating and Mitigating Counterfactual Failures in VLAs](../2026/arXiv/2026_arXiv_When-Vision-Overrides-Language-Evaluating-and-Mitigating-C/01_overview.md) — 2026 arXiv.
   - 선정 이유: LANGRET의 공개 장면·지시쌍·평가기 source이며 기존 counterfactual benchmark와의 중복을 드러낸다.
238. [Trajectory-Level Continuous Action Representation for Robotic Manipulation](../2026/ECCV/2026_ECCV_Trajectory-Level-Continuous-Action-Representation-for-Robo/01_overview.md) — 2026 ECCV.
   - 선정 이유: 제어 간격·물리 시간 조건부 행동 표현 자체를 새 공백으로 오인하지 않게 하는 기준이다.
239. [Is Your Robot's Memory Just a Clock? Temporal Shortcuts in Memory-Augmented VLA Policies](../2026/arXiv/2026_arXiv_Is-Your-Robot-s-Memory-Just-a-Clock-Temporal-Shortcuts-in/01_overview.md) — 2026 arXiv.
   - 선정 이유: 기억의 시간 편향 진단과 사건 기반 index가 이미 선행임을 반영할 직접 반대 근거다.
240. [Act2Goal: From World Model To General Goal-conditioned Policy](../2026/RSS/2026_RSS_Act2Goal-From-World-Model-To-General-Goal-conditioned-Poli/01_overview.md) — 2026 RSS.
   - 선정 이유: Hindsight 목표 변경·world model·단일 정책 연결의 직접 선행이며 언어 VLA와 시각 목표 정책의 경계를 드러낸다.
241. [AC2-VLA: Action-Context-Aware Adaptive Computation in Vision-Language-Action Models for Efficient Robotic Manipulation](../2026/IJCAI/2026_IJCAI_AC2-VLA-Action-Context-Aware-Adaptive-Computation-in-Visio/01_overview.md) — 2026 IJCAI.
   - 선정 이유: RL 기반 시간 적응과 비교할 학습된 계산 절감 baseline이며 지연·feedback·성능의 비용 분리를 돕는다.
242. [WCM: A World Critic Model for Vision-Language-Action Reinforcement Learning](../2026/arXiv/2026_arXiv_WCM-A-World-Critic-Model-for-Vision-Language-Action-Reinfo/01_overview.md) — 2026 arXiv.
   - 선정 이유: 공유 표현·가치 공동 학습 후보의 직접 경쟁 선행이므로 단순 world-model 보조 loss를 신규 기여로 재제안하지 않게 한다.
243. [Reinforcement Learning for Real-Time Vision-Language-Action Policies](../2026/arXiv/2026_arXiv_Reinforcement-Learning-for-Real-Time-Vision-Language-Actio/01_overview.md) — 2026 arXiv.
   - 선정 이유: 지연·feedback 공백의 직접 선행이자 단일 정책 선호와 별도로 보존할 강한 editor pipeline baseline이다.
244. [RoboAlign: Learning Test-Time Reasoning for Language-Action Alignment in Vision-Language-Action Models](../2026/arXiv/2026_arXiv_RoboAlign-Learning-Test-Time-Reasoning-for-Language-Action/01_overview.md) — 2026 arXiv.
   - 선정 이유: VLM의 RL 정렬과 배포 VLA의 직접 RL 갱신을 구분할 선행으로 단일 정책 연구의 기여 경계를 보완한다.
245. [STARE-VLA: Progressive Stage-Aware Reinforcement for Fine-Tuning Vision-Language-Action Models](../2025/arXiv/2025_arXiv_STARE-VLA-Progressive-Stage-Aware-Reinforcement-for-Fine-T/01_overview.md) — 2025 arXiv.
   - 선정 이유: 단계별 credit·보상 shaping 자체가 기존 방법임을 반영하고 원 보상 보존·추가 supervision을 비교하는 직접 선행이다.
246. [Ψ₀: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation](../2026/RSS/2026_RSS_An-Open-Foundation-Model-Towards-Universal-Humanoid-Loco-M/01_overview.md) — 2026 RSS.
   - 선정 이유: Human-video 표현 학습·humanoid action expert·RL 하위 제어의 역할을 분리할 직접 비교 논문이다. VLA 가중치의 reward 공동 갱신과 혼동하지 않는다.

### Contact-rich, deformable, force, and dexterous manipulation — 56

247. [Tac2Real: Reliable and GPU Visuotactile Simulation for Online Reinforcement Learning and Zero-Shot Real-World Deployment](../2026/ECCV/2026_ECCV_Tac2Real-Reliable-and-GPU-Visuotactile-Simulation-for-Onli/01_overview.md) — 2026 ECCV.
   - 선정 이유: Current trend / simulator. Tactile feedback을 이용하는 insertion·contact RL을 선택할 때 relevant하다. HIL-SERL 등 실제 interaction 학습과 simulation fidelity/transfer를 비교한다. Peg insertion 결과를 범용 dexterity로 확대하지 않는다.
248. [GraspNet-1Billion: A Large-Scale Benchmark for General Object Grasping](../2020/CVPR/2020_CVPR_GraspNet-1Billion-A-Large-Scale-Benchmark-for-General-Obje/01_overview.md) — 2020 CVPR.
   - 선정 이유: GraspNet은 grasp perception을 task input이나 benchmark로 쓰는 manipulation branch에서 읽는다.
249. [Contact-GraspNet: Efficient 6-DoF Grasp Generation in Cluttered Scenes](../2021/ICRA/2021_ICRA_Contact-GraspNet-Efficient-6-DoF-Grasp-Generation-in-Clutt/01_overview.md) — 2021 ICRA.
   - 선정 이유: Contact-GraspNet은 6-DoF grasp proposal을 사용하는 modular manipulation baseline으로 유지한다.
250. [Factory: Fast Contact for Robotic Assembly](../2022/RSS/2022_RSS_Factory-Fast-Contact-for-Robotic-Assembly/01_overview.md) — 2022 RSS.
   - 선정 이유: Factory는 contact-rich assembly를 sim-to-real RL 실험으로 선택할 때 읽는다.
251. [RoboPack: Learning Tactile-Informed Dynamics Models for Dense Packing](../2024/RSS/2024_RSS_RoboPack-Learning-Tactile-Informed-Dynamics-Models-for-Den/01_overview.md) — 2024 RSS.
   - 선정 이유: RoboPack은 tactile dynamics를 policy feedback에 추가하는 manipulation 전문화로 유지한다.
252. [Dense Object Nets: Learning Dense Visual Object Descriptors By and For Robotic Manipulation](../2018/CoRL/2018_CoRL_Dense-Object-Nets-Learning-Dense-Visual-Object-Descriptors/01_overview.md) — 2018 CoRL.
253. [UMPNet: Universal Manipulation Policy Network for Articulated Objects](../2022/RA-L/2022_RA-L_UMPNet-Universal-Manipulation-Policy-Network-for-Articulat/01_overview.md) — 2022 RA-L.
254. [Distilled Feature Fields Enable Few-Shot Language-Guided Manipulation](../2023/CoRL/2023_CoRL_Distilled-Feature-Fields-Enable-Few-Shot-Language-Guided-M/01_overview.md) — 2023 CoRL.
255. [GaussianGrasper: 3D Language Gaussian Splatting for Open-vocabulary Robotic Grasping](../2024/RA-L/2024_RA-L_GaussianGrasper-3D-Language-Gaussian-Splatting-for-Open-vo/01_overview.md) — 2024 RA-L.
256. [ManiGaussian: Dynamic Gaussian Splatting for Multi-task Robotic Manipulation](../2024/ECCV/2024_ECCV_ManiGaussian-Dynamic-Gaussian-Splatting-for-Multi-task-Rob/01_overview.md) — 2024 ECCV.
257. [Gaussian Splatting Visual MPC for Granular Media Manipulation](../2025/ICRA/2025_ICRA_Gaussian-Splatting-Visual-MPC-for-Granular-Media-Manipulat/01_overview.md) — 2025 ICRA.
258. [Persistent Object Gaussian Splat (POGS) for Tracking Human and Robot Manipulation of Irregularly Shaped Objects](../2025/ICRA/2025_ICRA_Persistent-Object-Gaussian-Splat-POGS-for-Tracking-Human-a/01_overview.md) — 2025 ICRA.
259. [DIGIT: A Novel Design for a Low-Cost Compact High-Resolution Tactile Sensor with Application to In-Hand Manipulation](../2020/IEEE-Robotics-and-Automa/2020_IEEE-Robotics-and-Automa_DIGIT-A-Novel-Design-for-a-Low-Cost-Compact-High-Resolutio/01_overview.md) — 2020 IEEE Robotics and Automation Letters.
260. [DeXtreme: Transfer of Agile In-hand Manipulation from Simulation to Reality](../2023/ICRA/2023_ICRA_DeXtreme-Transfer-of-Agile-In-hand-Manipulation-from-Simul/01_overview.md) — 2023 ICRA.
261. [Control-Limited Differential Dynamic Programming](../2014/ICRA/2014_ICRA_Control-Limited-Differential-Dynamic-Programming/01_overview.md) — 2014 ICRA.
262. [In-Hand Manipulation via Motion Cones](../2019/RSS/2019_RSS_In-Hand-Manipulation-via-Motion-Cones/01_overview.md) — 2019 RSS.
263. [Towards Tight Convex Relaxations for Contact-Rich Manipulation](../2024/RSS/2024_RSS_Towards-Tight-Convex-Relaxations-for-Contact-Rich-Manipula/01_overview.md) — 2024 RSS.
264. [Physics-Driven Data Generation for Contact-Rich Manipulation via Trajectory Optimization](../2025/RSS/2025_RSS_Physics-Driven-Data-Generation-for-Contact-Rich-Manipulati/01_overview.md) — 2025 RSS.
265. [Complementarity-Free Multi-Contact Modeling and Optimization for Dexterous Manipulation](../2025/RSS/2025_RSS_Complementarity-Free-Multi-Contact-Modeling-and-Optimizati/01_overview.md) — 2025 RSS.
266. [SoftGym: Benchmarking Deep Reinforcement Learning for Deformable Object Manipulation](../2020/CoRL/2020_CoRL_SoftGym-Benchmarking-Deep-Reinforcement-Learning-for-Defor/01_overview.md) — 2020 CoRL.
267. [DiffSkill: Skill Abstraction from Differentiable Physics for Deformable Object Manipulations with Tools](../2022/ICLR/2022_ICLR_DiffSkill-Skill-Abstraction-from-Differentiable-Physics-fo/01_overview.md) — 2022 ICLR.
268. [Neural Descriptor Fields: SE(3)-Equivariant Object Representations for Manipulation](../2021/CoRL/2021_CoRL_Neural-Descriptor-Fields-SE3-Equivariant-Object-Representa/01_overview.md) — 2021 CoRL.
269. [Diffusion-EDFs: Bi-equivariant Denoising Generative Modeling on SE(3) for Visual Robotic Manipulation](../2024/CVPR/2024_CVPR_Diffusion-EDFs-Bi-equivariant-Denoising-Generative-Modelin/01_overview.md) — 2024 CVPR.
270. [IndustReal: Transferring Contact-Rich Assembly Tasks from Simulation to Reality](../2023/RSS/2023_RSS_IndustReal-Transferring-Contact-Rich-Assembly-Tasks-from-S/01_overview.md) — 2023 RSS.
271. [Binding Touch to Everything: Learning Unified Multimodal Tactile Representations](../2024/CVPR/2024_CVPR_Binding-Touch-to-Everything-Learning-Unified-Multimodal-Ta/01_overview.md) — 2024 CVPR.
272. [DenseMatcher: Learning 3D Semantic Correspondence for Category-Level Manipulation from a Single Demo](../2025/ICLR/2025_ICLR_DenseMatcher-Learning-3D-Semantic-Correspondence-for-Categ/01_overview.md) — 2025 ICLR.
273. [G3Flow: Generative 3D Semantic Flow for Pose-aware and Generalizable Object Manipulation](../2025/CVPR/2025_CVPR_G3Flow-Generative-3D-Semantic-Flow-for-Pose-aware-and-Gene/01_overview.md) — 2025 CVPR.
274. [Reactive Diffusion Policy: Slow-Fast Visual-Tactile Policy Learning for Contact-Rich Manipulation](../2025/RSS/2025_RSS_Reactive-Diffusion-Policy-Slow-Fast-Visual-Tactile-Policy/01_overview.md) — 2025 RSS.
275. [AT-VLA: Adaptive Tactile Injection for Enhanced Feedback Reaction in Vision-Language-Action Models](../2026/CVPR/2026_CVPR_AT-VLA-Adaptive-Tactile-Injection-for-Enhanced-Feedback-Re/01_overview.md) — 2026 CVPR.
276. [ForceVLA2: Unleashing Hybrid Force-Position Control with Force Awareness for Contact-Rich Manipulation](../2026/CVPR/2026_CVPR_ForceVLA2-Unleashing-Hybrid-Force-Position-Control-with-Fo/01_overview.md) — 2026 CVPR.
277. [Dexterous World Models](../2026/CVPR/2026_CVPR_Dexterous-World-Models/01_overview.md) — 2026 CVPR.
278. [EquAct: An SE(3)-Equivariant Multi-Task Transformer for 3D Robotic Manipulation](../2026/ICLR/2026_ICLR_EquAct-An-SE3-Equivariant-Multi-Task-Transformer-for-3D-Ro/01_overview.md) — 2026 ICLR.
279. [Tabero: Learning Gentle Manipulation with Closed-Loop Force Feedback from Vision, Touch, and Language](../2026/ICML/2026_ICML_Tabero-Learning-Gentle-Manipulation-with-Closed-Loop-Force/01_overview.md) — 2026 ICML.
280. [TactAlign: Human-to-Robot Policy Transfer via Tactile Alignment](../2026/RSS/2026_RSS_TactAlign-Human-to-Robot-Policy-Transfer-via-Tactile-Align/01_overview.md) — 2026 RSS.
281. [DexterityGen: Foundation Controller for Unprecedented Dexterity](../2026/RSS/2026_RSS_DexterityGen-Foundation-Controller-for-Unprecedented-Dexte/01_overview.md) — 2026 RSS.
282. [V-HOP: Visuo-Haptic 6D Object Pose Tracking](../2025/RSS/2025_RSS_V-HOP-Visuo-Haptic-6D-Object-Pose-Tracking/01_overview.md) — 2025 RSS.
283. [PP-Tac: Paper Picking Using Omnidirectional Tactile Feedback in Dexterous Robotic Hands](../2025/RSS/2025_RSS_PP-Tac-Paper-Picking-Using-Omnidirectional-Tactile-Feedbac/01_overview.md) — 2025 RSS.
284. [GeoDEx: A Unified Geometric Framework for Tactile Dexterous and Extrinsic Manipulation under Force Uncertainty](../2025/RSS/2025_RSS_GeoDEx-A-Unified-Geometric-Framework-for-Tactile-Dexterous/01_overview.md) — 2025 RSS.
285. [Demonstrating REASSEMBLE: A Multimodal Dataset for Contact-rich Robotic Assembly and Disassembly](../2025/RSS/2025_RSS_Demonstrating-REASSEMBLE-A-Multimodal-Dataset-for-Contact/01_overview.md) — 2025 RSS.
286. [Robust Peg-in-Hole Assembly under Uncertainties via Compliant and Interactive Contact-Rich Manipulation](../2025/RSS/2025_RSS_Robust-Peg-in-Hole-Assembly-under-Uncertainties-via-Compli/01_overview.md) — 2025 RSS.
287. [FACTR: Force-Attending Curriculum Training for Contact-Rich Policy Learning](../2025/RSS/2025_RSS_FACTR-Force-Attending-Curriculum-Training-for-Contact-Rich/01_overview.md) — 2025 RSS.
288. [CordViP: Correspondence-based Visuomotor Policy for Dexterous Manipulation in Real-World](../2025/RSS/2025_RSS_CordViP-Correspondence-based-Visuomotor-Policy-for-Dextero/01_overview.md) — 2025 RSS.
289. [FlowPolicy: Enabling Fast and Robust 3D Flow-Based Policy via Consistency Flow Matching for Robot Manipulation](../2025/AAAI/2025_AAAI_FlowPolicy-Enabling-Fast-and-Robust-3D-Flow-Based-Policy-v/01_overview.md) — 2025 AAAI.
290. [Sparsh: Self-supervised touch representations for vision-based tactile sensing](../2024/CoRL/2024_CoRL_Sparsh-Self-supervised-touch-representations-for-vision-ba/01_overview.md) — 2024 CoRL.
291. [Octopi: Object Property Reasoning with Large Tactile-Language Models](../2024/RSS/2024_RSS_Octopi-Object-Property-Reasoning-with-Large-Tactile-Langua/01_overview.md) — 2024 RSS.
292. [OPEN TEACH: A Versatile Teleoperation System for Robotic Manipulation](../2024/CoRL/2024_CoRL_OPEN-TEACH-A-Versatile-Teleoperation-System-for-Robotic-Ma/01_overview.md) — 2024 CoRL.
293. [FurnitureBench: Reproducible Real-World Benchmark for Long-Horizon Complex Manipulation](../2023/RSS/2023_RSS_FurnitureBench-Reproducible-Real-World-Benchmark-for-Long/01_overview.md) — 2023 RSS.
294. [Learning Robotic Manipulation Policies from Point Clouds with Conditional Flow Matching](../2024/CoRL/2024_CoRL_Learning-Robotic-Manipulation-Policies-from-Point-Clouds-w/01_overview.md) — 2024 CoRL.
295. [Contact-Anchored Policies: Contact Conditioning Creates Strong Robot Utility Models](../2026/RSS/2026_RSS_Contact-Anchored-Policies-Contact-Conditioning-Creates-Str/01_overview.md) — 2026 RSS.
   - 선정 이유: VLA의 이득이 task specification 차이인지 가릴 강한 non-VLA baseline이므로 NEXT다.
296. [FMB: A functional manipulation benchmark for generalizable robotic learning](../2025/IJRR/2025_IJRR_FMB-A-functional-manipulation-benchmark-for-generalizable/01_overview.md) — 2025 IJRR.
   - 선정 이유: 범용 pick-and-place 성능과 접촉 조립 능력을 구분할 benchmark를 보완한다.
297. [Learning Visuotactile Estimation and Control for Non-prehensile Manipulation under Occlusions](../2025/CoRL/2025_CoRL_Learning-Visuotactile-Estimation-and-Control-for-Non-prehe/01_overview.md) — 2025 CoRL.
   - 선정 이유: 접촉 VLA의 센서 이득과 상태 추정·feedback controller 이득을 분리할 직접 대안이다.
298. [Force Policy: Learning Hybrid Force-Position Control Policy under Interaction Frame for Contact-Rich Manipulation](../2026/RSS/2026_RSS_Force-Policy-Learning-Hybrid-Force-Position-Control-Policy/01_overview.md) — 2026 RSS.
   - 선정 이유: Unified VLA의 접촉 기여가 분리된 고주파 힘 제어보다 나은지 판단할 비교 기준이다.
299. [Emergent Dexterity Via Diverse Resets and Large-Scale Reinforcement Learning](../2026/ICLR/2026_ICLR_Emergent-Dexterity-Via-Diverse-Resets-and-Large-Scale-Rein/01_overview.md) — 2026 ICLR.
   - 선정 이유: VLA-RL의 탐색 개선이 정책 방법보다 reset coverage에서 오는지 분리할 중요한 대조군이다.
300. [FORGE: Force-Guided Exploration for Robust Contact-Rich Manipulation Under Uncertainty](../2025/RA-L/2025_RA-L_FORGE-Force-Guided-Exploration-for-Robust-Contact-Rich-Man/01_overview.md) — 2025 RA-L.
   - 선정 이유: VLA의 추가 복잡도 전에 넘어야 할 비-VLA 접촉 RL 기준선이다.
301. [ContactBench 1.0: A Benchmark for Everyday Contact-Rich Robotic Manipulation](../2026/arXiv/2026_arXiv_ContactBench-1.0-A-Benchmark-for-Everyday-Contact-Rich-Rob/01_overview.md) — 2026 arXiv.
   - 선정 이유: 접촉 일반화 질문을 구체적인 물리 변화와 재현 자산으로 정의할 benchmark다.
302. [Tune to Learn: How Controller Gains Shape Robot Policy Learning](../2026/RSS/2026_RSS_Tune-to-Learn-How-Controller-Gains-Shape-Robot-Policy-Lear/01_overview.md) — 2026 RSS.
   - 선정 이유: 접촉 VLA RL의 이득을 baseline gain 튜닝과 분리해야 함을 보이는 직접 선행이다.

### Planning, control, simulation, and TAMP extensions — 17

303. [NavDP: Learning Sim-to-Real Navigation Diffusion Policy with Privileged Information Guidance](../2026/ICRA/2026_ICRA_NavDP-Learning-Sim-to-Real-Navigation-Diffusion-Policy-wit/01_overview.md) — 2026 ICRA.
   - 선정 이유: Current trend. Simulation training에서 real-world cross-embodiment local navigation으로 이어지는 경로를 보충한다. NoMaD/ViNT의 local policy와 비교할 대상이며, 논문 자체를 language-conditioned VLA RL로 부르지는 않는다.
304. [Rapidly-Exploring Random Trees: A New Tool for Path Planning](../1998/Technical-Report/1998_Technical-Report_Rapidly-Exploring-Random-Trees-A-New-Tool-for-Path-Plannin/01_overview.md) — 1998 Technical Report.
   - 선정 이유: RRT는 learned navigation·manipulation과 motion-planning baseline을 비교하는 선택적 선행으로 유지한다.
305. [Information Theoretic MPC for Model-Based Reinforcement Learning](../2017/ICRA/2017_ICRA_Information-Theoretic-MPC-for-Model-Based-Reinforcement-Le/01_overview.md) — 2017 ICRA.
   - 선정 이유: MPPI는 VLA action과 model-based local control을 결합할 때 필요한 전문화로 둔다.
306. [PDDLStream: Integrating Symbolic Planners and Blackbox Samplers via Optimistic Adaptive Planning](../2020/ICAPS/2020_ICAPS_PDDLStream-Integrating-Symbolic-Planners-and-Blackbox-Samp/01_overview.md) — 2020 ICAPS.
   - 선정 이유: PDDLStream은 SayCan 이후 symbolic/TAMP 대안을 검토하는 계획 branch로 둔다.
307. [Logic-Geometric Programming: An Optimization-Based Approach to Combined Task and Motion Planning](../2015/IJCAI/2015_IJCAI_Logic-Geometric-Programming-An-Optimization-Based-Approach/01_overview.md) — 2015 IJCAI.
308. [FFRob: Leveraging Symbolic Planning for Efficient Task and Motion Planning](../2018/The-International-Journa/2018_The-International-Journa_FFRob-Leveraging-Symbolic-Planning-for-Efficient-Task-and/01_overview.md) — 2018 The International Journal of Robotics Research.
309. [Kinodynamic Trajectory Following with STELA: Simultaneous Trajectory Estimation & Local Adaptation](../2025/RSS/2025_RSS_Kinodynamic-Trajectory-Following-with-STELA-Simultaneous-T/01_overview.md) — 2025 RSS.
310. [Instruction-Augmented Long-Horizon Planning: Embedding Grounding Mechanisms in Embodied Mobile Manipulation](../2025/AAAI/2025_AAAI_Instruction-Augmented-Long-Horizon-Planning-Embedding-Grou/01_overview.md) — 2025 AAAI.
311. [Neural Assembler: Learning to Generate Fine-Grained Robotic Assembly Instructions from Multi-View Images](../2025/AAAI/2025_AAAI_Neural-Assembler-Learning-to-Generate-Fine-Grained-Robotic/01_overview.md) — 2025 AAAI.
312. [Open-Vocabulary Spatio-Temporal Scene Graph for Robot Perception and Teleoperation Planning](../2026/ICRA/2026_ICRA_Open-Vocabulary-Spatio-Temporal-Scene-Graph-for-Robot-Perc/01_overview.md) — 2026 ICRA.
313. [Lookahead Exploration with Neural Radiance Representation for Continuous Vision-Language Navigation](../2024/CVPR/2024_CVPR_Lookahead-Exploration-with-Neural-Radiance-Representation/01_overview.md) — 2024 CVPR.
314. [FOCI: Trajectory Optimization on Gaussian Splats](../2025/IROS/2025_IROS_FOCI-Trajectory-Optimization-on-Gaussian-Splats/01_overview.md) — 2025 IROS.
315. [Partially Observable Task and Motion Planning with Uncertainty and Risk Awareness](../2024/RSS/2024_RSS_Partially-Observable-Task-and-Motion-Planning-with-Uncerta/01_overview.md) — 2024 RSS.
316. [Parallel and Proximal Linear-Quadratic Methods for Real-Time Constrained Model-Predictive Control](../2024/RSS/2024_RSS_Parallel-and-Proximal-Linear-Quadratic-Methods-for-Real-Ti/01_overview.md) — 2024 RSS.
317. [Differentiable Robust Model Predictive Control](../2024/RSS/2024_RSS_Differentiable-Robust-Model-Predictive-Control/01_overview.md) — 2024 RSS.
318. [Linear-time Differential Inverse Kinematics: an Augmented Lagrangian Perspective](../2024/RSS/2024_RSS_Linear-time-Differential-Inverse-Kinematics-an-Augmented-L/01_overview.md) — 2024 RSS.
319. [KinDER: A Physical Reasoning Benchmark for Robot Learning and Planning](../2026/RSS/2026_RSS_KinDER-A-Physical-Reasoning-Benchmark-for-Robot-Learning-a/01_overview.md) — 2026 RSS.
   - 선정 이유: VLA의 실패가 언어 표현 문제인지 물리적 의사결정 문제인지 진단할 자원이다.

### Active and embodied 3D Vision — 23

320. [LoGoPlanner: Localization Grounded Navigation Policy with Metric-aware Visual Geometry](../2026/ICRA/2026_ICRA_LoGoPlanner-Localization-Grounded-Navigation-Policy-with-M/01_overview.md) — 2026 ICRA.
   - 선정 이유: Current trend / enabling 3D. Metric-aware geometry와 history 기반 state estimation을 trajectory planning에 연결한다. 일반 reconstruction보다 현재 navigation 목표에 직접적이다. Controller가 실제 사용하는 pose·calibration·simulator GT의 범위는 본문/배포 코드 확인이 필요하다.
321. [Vision-and-Language Navigation: Interpreting Visually-Grounded Navigation Instructions in Real Environments](../2018/CVPR/2018_CVPR_Vision-and-Language-Navigation-Interpreting-Visually-Groun/01_overview.md) — 2018 CVPR.
   - 선정 이유: R2R은 VLN instruction grounding과 graph-navigation 평가의 원형으로 VLN-CE·NaVILA의 설정 차이를 비교할 때 읽는다.
322. [PointNet: Deep Learning on Point Sets for 3D Classification and Segmentation](../2017/CVPR/2017_CVPR_PointNet-Deep-Learning-on-Point-Sets-for-3D-Classification/01_overview.md) — 2017 CVPR.
   - 선정 이유: PointNet은 DP3 등 point-cloud policy encoder를 구현·비교할 때 필요한 선택적 representation 기반이다.
323. [DROID-SLAM: Deep Visual SLAM for Monocular, Stereo, and RGB-D Cameras](../2021/NeurIPS/2021_NeurIPS_DROID-SLAM-Deep-Visual-SLAM-for-Monocular-Stereo-and-RGB-D/01_overview.md) — 2021 NeurIPS.
   - 선정 이유: DROID-SLAM은 navigation의 localization 품질이 policy 성능을 제한하는 실험에서 읽는다.
324. [Where2Act: From Pixels to Actions for Articulated 3D Objects](../2021/ICCV/2021_ICCV_Where2Act-From-Pixels-to-Actions-for-Articulated-3D-Object/01_overview.md) — 2021 ICCV.
325. [FlowBot3D: Learning 3D Articulation Flow to Manipulate Articulated Objects](../2022/RSS/2022_RSS_FlowBot3D-Learning-3D-Articulation-Flow-to-Manipulate-Arti/01_overview.md) — 2022 RSS.
326. [Ditto: Building Digital Twins of Articulated Objects from Interaction](../2022/CVPR/2022_CVPR_Ditto-Building-Digital-Twins-of-Articulated-Objects-from-I/01_overview.md) — 2022 CVPR.
327. [VLMaps: Visual-Language Maps for Robot Navigation](../2023/ICRA/2023_ICRA_VLMaps-Visual-Language-Maps-for-Robot-Navigation/01_overview.md) — 2023 ICRA.
328. [SUGAR: Pre-training 3D Visual Representations for Robotics](../2024/CVPR/2024_CVPR_SUGAR-Pre-training-3D-Visual-Representations-for-Robotics/01_overview.md) — 2024 CVPR.
329. [Splat-Nav: Safe Real-Time Robot Navigation in Gaussian Splatting Maps](../2025/T-RO/2025_T-RO_Splat-Nav-Safe-Real-Time-Robot-Navigation-in-Gaussian-Spla/01_overview.md) — 2025 T-RO.
330. [RoboSpatial: Teaching Spatial Understanding to 2D and 3D Vision-Language Models for Robotics](../2025/CVPR/2025_CVPR_RoboSpatial-Teaching-Spatial-Understanding-to-2D-and-3D-Vi/01_overview.md) — 2025 CVPR.
331. [PointVLA: Injecting the 3D World into Vision-Language-Action Models](../2026/RA-L/2026_RA-L_PointVLA-Injecting-the-3D-World-into-Vision-Language-Actio/01_overview.md) — 2026 RA-L.
332. [Vysics: Object Reconstruction Under Occlusion by Fusing Vision and Contact-Rich Physics](../2025/RSS/2025_RSS_Vysics-Object-Reconstruction-Under-Occlusion-by-Fusing-Vis/01_overview.md) — 2025 RSS.
333. [Act the Part: Learning Interaction Strategies for Articulated Object Part Discovery](../2021/ICCV/2021_ICCV_Act-the-Part-Learning-Interaction-Strategies-for-Articulat/01_overview.md) — 2021 ICCV.
334. [Where2Explore: Few-shot Affordance Learning for Unseen Novel Categories of Articulated Objects](../2023/NeurIPS/2023_NeurIPS_Where2Explore-Few-shot-Affordance-Learning-for-Unseen-Nove/01_overview.md) — 2023 NeurIPS.
335. [Clio: Real-time Task-Driven Open-Set 3D Scene Graphs](../2024/RA-L/2024_RA-L_Clio-Real-time-Task-Driven-Open-Set-3D-Scene-Graphs/01_overview.md) — 2024 RA-L.
336. [HAMMER: Heterogeneous, Multi-Robot Semantic Gaussian Splatting](../2025/RA-L/2025_RA-L_HAMMER-Heterogeneous-Multi-Robot-Semantic-Gaussian-Splatti/01_overview.md) — 2025 RA-L.
337. [VISTA: Open-Vocabulary, Task-Relevant Robot Exploration with Online Semantic Gaussian Splatting](../2026/ICRA/2026_ICRA_VISTA-Open-Vocabulary-Task-Relevant-Robot-Exploration-with/01_overview.md) — 2026 ICRA.
338. [RoboRefer: Towards Spatial Referring with Reasoning in Vision-Language Models for Robotics](../2025/NeurIPS/2025_NeurIPS_RoboRefer-Towards-Spatial-Referring-with-Reasoning-in-Visi/01_overview.md) — 2025 NeurIPS.
339. [Volumetric Environment Representation for Vision-Language Navigation](../2024/CVPR/2024_CVPR_Volumetric-Environment-Representation-for-Vision-Language/01_overview.md) — 2024 CVPR.
340. [IGL-Nav: Incremental 3D Gaussian Localization for Image-goal Navigation](../2025/ICCV/2025_ICCV_IGL-Nav-Incremental-3D-Gaussian-Localization-for-Image-goa/01_overview.md) — 2025 ICCV.
341. [Move to Understand a 3D Scene: Bridging Visual Grounding and Exploration for Efficient and Versatile Embodied Navigation](../2025/ICCV/2025_ICCV_Move-to-Understand-a-3D-Scene-Bridging-Visual-Grounding-an/01_overview.md) — 2025 ICCV.
342. [PhysTwin: Physics-Informed Reconstruction and Simulation of Deformable Objects from Videos](../2025/ICCV/2025_ICCV_PhysTwin-Physics-Informed-Reconstruction-and-Simulation-of/01_overview.md) — 2025 ICCV.
   - 선정 이유: 3D 외관 재구성과 행동에 유용한 물성 모델을 구별할 직접 연결 연구다.

### Locomotion, whole-body control, mobile manipulation, and humanoids — 16

343. [RMA: Rapid Motor Adaptation for Legged Robots](../2021/RSS/2021_RSS_RMA-Rapid-Motor-Adaptation-for-Legged-Robots/01_overview.md) — 2021 RSS.
   - 선정 이유: RMA는 NaVILA 등 legged navigation의 저수준 adaptation을 깊게 다룰 때 읽는다.
344. [RoboPanoptes: The All-Seeing Robot with Whole-body Dexterity](../2025/RSS/2025_RSS_RoboPanoptes-The-All-Seeing-Robot-with-Whole-body-Dexterit/01_overview.md) — 2025 RSS.
345. [Demonstrating OK-Robot: What Really Matters in Integrating Open-Knowledge Models for Robotics](../2024/RSS/2024_RSS_Demonstrating-OK-Robot-What-Really-Matters-in-Integrating/01_overview.md) — 2024 RSS.
346. [Language-Grounded Dynamic Scene Graphs for Interactive Object Search with Mobile Manipulation](../2024/RA-L/2024_RA-L_Language-Grounded-Dynamic-Scene-Graphs-for-Interactive-Obj/01_overview.md) — 2024 RA-L.
347. [Dynamic Open-Vocabulary 3D Scene Graphs for Long-term Language-Guided Mobile Manipulation](../2025/RA-L/2025_RA-L_Dynamic-Open-Vocabulary-3D-Scene-Graphs-for-Long-term-Lang/01_overview.md) — 2025 RA-L.
348. [Demonstrating MOSART: Opening Articulated Structures in the Real World](../2025/RSS/2025_RSS_Demonstrating-MOSART-Opening-Articulated-Structures-in-the/01_overview.md) — 2025 RSS.
349. [HOMIE: Humanoid Loco-Manipulation with Isomorphic Exoskeleton Cockpit](../2025/RSS/2025_RSS_HOMIE-Humanoid-Loco-Manipulation-with-Isomorphic-Exoskelet/01_overview.md) — 2025 RSS.
350. [SPIN: Simultaneous Perception, Interaction and Navigation](../2024/CVPR/2024_CVPR_SPIN-Simultaneous-Perception-Interaction-and-Navigation/01_overview.md) — 2024 CVPR.
351. [GOAT: GO to Any Thing](../2024/RSS/2024_RSS_GOAT-GO-to-Any-Thing/01_overview.md) — 2024 RSS.
352. [Habitat 2.0: Training Home Assistants to Rearrange their Habitat](../2021/NeurIPS/2021_NeurIPS_Habitat-2.0-Training-Home-Assistants-to-Rearrange-their-Ha/01_overview.md) — 2021 NeurIPS.
   - 선정 이유: Habitat 2.0는 navigation에서 object rearrangement/mobile manipulation으로 확장할 때 필요한 task·simulator 기준이다.
353. [MoManipVLA: Transferring Vision-language-action Models for General Mobile Manipulation](../2025/CVPR/2025_CVPR_MoManipVLA-Transferring-Vision-language-action-Models-for/01_overview.md) — 2025 CVPR.
   - 선정 이유: NaVILA·MoTo와 함께 VLA와 기하학적 실행 가능성의 경계를 비교하는 NEXT다.
354. [WholeBodyVLA: Towards Unified Latent VLA for Whole-body Loco-manipulation Control](../2026/ICLR/2026_ICLR_WholeBodyVLA-Towards-Unified-Latent-VLA-for-Whole-body-Loc/01_overview.md) — 2026 ICLR.
   - 선정 이유: NaVILA 이후 VLA와 low-level RL의 역할을 비교할 NEXT다.
355. [TidyBot++: An Open-Source Holonomic Mobile Manipulator for Robot Learning](../2025/CoRL/2025_CoRL_TidyBot%2B%2B-An-Open-Source-Holonomic-Mobile-Manipulator-for/01_overview.md) — 2025 CoRL.
   - 선정 이유: 다양한 로봇 연구에서 policy 성능과 base의 운동학적 자유도 차이를 구분할 플랫폼 기준이다.
356. [Mobi-π: Mobilizing Your Robot Learning Policy](../2025/CoRL/2025_CoRL_Mobi-pi-Mobilizing-Your-Robot-Learning-Policy/01_overview.md) — 2025 CoRL.
   - 선정 이유: Mobile ALOHA의 whole-body 데이터와 MoTo의 이동–조작 연결을 보완하며, HANDOFF의 정책별 도착 조건을 비교할 직접 선행이다.
357. [SAGA: Open-World Mobile Manipulation via Structured Affordance Grounding](../2026/RA-L/2026_RA-L_SAGA-Open-World-Mobile-Manipulation-via-Structured-Afforda/01_overview.md) — 2026 RA-L.
   - 선정 이유: VoxPoser·Mobile ALOHA와 구조적 3D grounding을 잇는 NEXT다. 다양한 로봇을 다룬다는 목표에서 의미 표현과 embodiment별 제어의 경계를 비교한다.
358. [MoMa-Kitchen: A 100K+ Benchmark for Affordance-Grounded Last-Mile Navigation in Mobile Manipulation](../2025/ICCV/2025_ICCV_MoMa-Kitchen-A-100K%2B-Benchmark-for-Affordance-Grounded-Las/01_overview.md) — 2025 ICCV.
   - 선정 이유: VLA+RL을 manipulation과 navigation에 통합할 때 성공 조건을 구체화하는 benchmark다.

### World models, uncertainty, failure detection, and recovery — 47

359. [VLAW: Iterative Co-Improvement of Vision-Language-Action Policy and World Model](../2026/ICML/2026_ICML_VLAW-Iterative-Co-Improvement-of-Vision-Language-Action-Po/01_overview.md) — 2026 ICML.
   - 선정 이유: Current trend. 실제 rollout으로 world model의 failure coverage를 개선하고 synthetic rollout으로 policy를 개선하는 반복 구조다. 이미 등록된 Ctrl-World/WMPO와 연결해 model bias와 real-data budget을 비교한다. Abstract만으로 특정 RL optimizer를 단정하지 않는다.
360. [Towards Practical World Model-based Reinforcement Learning for Vision-Language-Action Models](../2026/ICML/2026_ICML_Towards-Practical-World-Model-based-Reinforcement-Learning/01_overview.md) — 2026 ICML.
   - 선정 이유: Current trend. Multi-view consistency와 chunk-level branched rollout으로 world-model RL의 오차 누적을 다룬다. WMPO/WorldGym을 읽을 때 직접 비교해야 할 누락 논문이다.
361. [Self-Improving Robot Policy with Compositional World Model](../2026/RSS/2026_RSS_Self-Improving-Robot-Policy-with-Compositional-World-Model/01_overview.md) — 2026 RSS.
   - 선정 이유: Current trend. Multi-view dynamics와 progress value를 분리하여 imagined rollout의 advantage를 만든다. VLA-MBPO/WMPO와 reward/value 신뢰도 및 real-robot transfer를 비교할 가치가 있다.
362. [PointWorld: Scaling 3D World Models for In-The-Wild Robotic Manipulation](../2026/CVPR/2026_CVPR_PointWorld-Scaling-3D-World-Models-for-In-The-Wild-Robotic/01_overview.md) — 2026 CVPR.
   - 선정 이유: Current trend / action-relevant 3D. State와 action을 3D point flow로 표현하고 예측을 manipulation MPC에 연결한다. DP3/3D-VLA 이후 explicit geometry와 world model을 비교할 직접적인 연결이다. 본문 평가의 보장 범위와 calibration 의존성은 추가 확인 대상이다.
363. [OopsieVerse: A Safety Benchmark with Damage-Aware Simulation for Robot Manipulation](../2026/RSS/2026_RSS_OopsieVerse-A-Safety-Benchmark-with-Damage-Aware-Simulatio/01_overview.md) — 2026 RSS.
   - 선정 이유: Benchmark. Task success와 물리적 damage를 분리하고 damage-aware IL/RL 및 VLA 평가를 지원한다. 기존 safety/recovery 흐름에 contact·thermal·fluid damage라는 구체적인 평가 축을 보충한다.
364. [World Models](../2018/NeurIPS-Workshop/2018_NeurIPS-Workshop_World-Models/01_overview.md) — 2018 NeurIPS Workshop.
   - 선정 이유: World Models 원전은 latent world-model 계보를 확인할 때 읽고 실제 robot/control 비교는 TD-MPC2와 후속 연구에 우선한다.
365. [DayDreamer: World Models for Physical Robot Learning](../2022/CoRL/2022_CoRL_DayDreamer-World-Models-for-Physical-Robot-Learning/01_overview.md) — 2022 CoRL.
   - 선정 이유: DayDreamer는 실제 robot model-based RL branch에서 학습 예산과 dynamics 사용을 비교한다.
366. [Control Barrier Function Based Quadratic Programs for Safety Critical Systems](../2017/TAC/2017_TAC_Control-Barrier-Function-Based-Quadratic-Programs-for-Safe/01_overview.md) — 2017 TAC.
   - 선정 이유: CBF는 safety filter의 가정과 보장을 연구하는 branch에서 읽으며 VLA/RL 전체의 선행 의무에서는 분리한다.
367. [DreamGen: Unlocking Generalization in Robot Learning through Video World Models](../2025/CoRL/2025_CoRL_DreamGen-Unlocking-Generalization-in-Robot-Learning-throug/01_overview.md) — 2025 CoRL.
368. [DreamDojo: A Generalist Robot World Model from Large-Scale Human Videos](../2026/ICML/2026_ICML_DreamDojo-A-Generalist-Robot-World-Model-from-Large-Scale/01_overview.md) — 2026 ICML.
369. [Learning Latent Dynamics for Planning from Pixels](../2019/ICML/2019_ICML_Learning-Latent-Dynamics-for-Planning-from-Pixels/01_overview.md) — 2019 ICML.
370. [Dream to Control: Learning Behaviors by Latent Imagination](../2020/ICLR/2020_ICLR_Dream-to-Control-Learning-Behaviors-by-Latent-Imagination/01_overview.md) — 2020 ICLR.
371. [Mastering Diverse Domains through World Models](../2025/Nature/2025_Nature_Mastering-Diverse-Domains-through-World-Models/01_overview.md) — 2025 Nature.
372. [PIN-WM: Learning Physics-INformed World Models for Non-Prehensile Manipulation](../2025/RSS/2025_RSS_PIN-WM-Learning-Physics-INformed-World-Models-for-Non-Preh/01_overview.md) — 2025 RSS.
373. [Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets](../2025/RSS/2025_RSS_Unified-World-Models-Coupling-Video-and-Action-Diffusion-f/01_overview.md) — 2025 RSS.
374. [FlowDreamer: A RGB-D World Model With Flow-Based Motion Representations for Robot Manipulation](../2026/RA-L/2026_RA-L_FlowDreamer-A-RGB-D-World-Model-With-Flow-Based-Motion-Rep/01_overview.md) — 2026 RA-L.
375. [Can We Detect Failures Without Failure Data? Uncertainty-Aware Runtime Failure Detection for Imitation Learning Policies](../2025/RSS/2025_RSS_Can-We-Detect-Failures-Without-Failure-Data-Uncertainty-Aw/01_overview.md) — 2025 RSS.
376. [SAFE: Multitask Failure Detection for Vision-Language-Action Models](../2025/NeurIPS/2025_NeurIPS_SAFE-Multitask-Failure-Detection-for-Vision-Language-Actio/01_overview.md) — 2025 NeurIPS.
377. [WorldGym: World Model as An Environment for Policy Evaluation](../2026/ICLR/2026_ICLR_WorldGym-World-Model-as-An-Environment-for-Policy-Evaluati/01_overview.md) — 2026 ICLR.
378. [WMPO: World Model-based Policy Optimization for Vision-Language-Action Models](../2026/ICLR/2026_ICLR_WMPO-World-Model-based-Policy-Optimization-for-Vision-Lang/01_overview.md) — 2026 ICLR.
379. [FLARE: A Failure-Aware Framework for Autonomous Correction and Recovery in Visual-Language Robotic Manipulation](../2026/CVPR/2026_CVPR_FLARE-A-Failure-Aware-Framework-for-Autonomous-Correction/01_overview.md) — 2026 CVPR.
380. [Can VLMs Diagnose and Recover from VLA Manipulation Faults?](../2026/ICML/2026_ICML_Can-VLMs-Diagnose-and-Recover-from-VLA-Manipulation-Faults/01_overview.md) — 2026 ICML.
381. [Temporal Difference Calibration in Sequential Tasks: Application to Vision-Language-Action Models](../2026/ICML/2026_ICML_Temporal-Difference-Calibration-in-Sequential-Tasks-Applic/01_overview.md) — 2026 ICML.
382. [Memory Retrieval in Visuomotor Policies for Long-Horizon Robot Control](../2026/RSS/2026_RSS_Memory-Retrieval-in-Visuomotor-Policies-for-Long-Horizon-R/01_overview.md) — 2026 RSS.
383. [Demonstrating ViSafe: Vision-enabled Safety for High-speed Detect and Avoid](../2025/RSS/2025_RSS_Demonstrating-ViSafe-Vision-enabled-Safety-for-High-speed/01_overview.md) — 2025 RSS.
384. [Learned Perceptive Forward Dynamics Model for Safe and Platform-aware Robotic Navigation](../2025/RSS/2025_RSS_Learned-Perceptive-Forward-Dynamics-Model-for-Safe-and-Pla/01_overview.md) — 2025 RSS.
385. [Certifiably-Correct Mapping for Safe Navigation Despite Odometry Drift](../2025/RSS/2025_RSS_Certifiably-Correct-Mapping-for-Safe-Navigation-Despite-Od/01_overview.md) — 2025 RSS.
386. [Particle-Grid Neural Dynamics for Learning Deformable Object Models from RGB-D Videos](../2025/RSS/2025_RSS_Particle-Grid-Neural-Dynamics-for-Learning-Deformable-Obje/01_overview.md) — 2025 RSS.
387. [Map Space Belief Prediction for Manipulation-Enhanced Mapping](../2025/RSS/2025_RSS_Map-Space-Belief-Prediction-for-Manipulation-Enhanced-Mapp/01_overview.md) — 2025 RSS.
388. [Unified Video Action Model](../2025/RSS/2025_RSS_Unified-Video-Action-Model/01_overview.md) — 2025 RSS.
389. [From Foresight to Forethought: VLM-In-the-Loop Policy Steering via Latent Alignment](../2025/RSS/2025_RSS_From-Foresight-to-Forethought-VLM-In-the-Loop-Policy-Steer/01_overview.md) — 2025 RSS.
390. [Prompting with the Future: Open-World Model Predictive Control with Interactive Digital Twins](../2025/RSS/2025_RSS_Prompting-with-the-Future-Open-World-Model-Predictive-Cont/01_overview.md) — 2025 RSS.
391. [Self-Correcting Robot Manipulation via Gaussian-Splatted Foresight](../2025/AAAI/2025_AAAI_Self-Correcting-Robot-Manipulation-via-Gaussian-Splatted-F/01_overview.md) — 2025 AAAI.
392. [WMNav: Integrating Vision-Language Models into World Models for Object Goal Navigation](../2025/IROS/2025_IROS_WMNav-Integrating-Vision-Language-Models-into-World-Models/01_overview.md) — 2025 IROS.
393. [RoboDreamer: Learning Compositional World Models for Robot Imagination](../2024/ICML/2024_ICML_RoboDreamer-Learning-Compositional-World-Models-for-Robot/01_overview.md) — 2024 ICML.
394. [Learning Interactive Real-World Simulators](../2024/ICLR/2024_ICLR_Learning-Interactive-Real-World-Simulators/01_overview.md) — 2024 ICLR.
395. [SafeMimic: Towards Safe and Autonomous Human-to-Robot Imitation for Mobile Manipulation](../2025/RSS/2025_RSS_SafeMimic-Towards-Safe-and-Autonomous-Human-to-Robot-Imita/01_overview.md) — 2025 RSS.
396. [Ctrl-World: A Controllable Generative World Model for Robot Manipulation](../2026/ICLR/2026_ICLR_Ctrl-World-A-Controllable-Generative-World-Model-for-Robot/01_overview.md) — 2026 ICLR.
397. [LIBERO-RIG: A Hardware-Setup Robustness Benchmark for Vision-Language-Action Models](../2026/arXiv/2026_arXiv_LIBERO-RIG-A-Hardware-Setup-Robustness-Benchmark-for-Visio/01_overview.md) — 2026 arXiv.
   - 선정 이유: D1의 fault taxonomy와 policy/controller 경계 진단에 필요한 NEXT benchmark다.
398. [Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons](../2026/RSS/2026_RSS_Robometer-Scaling-General-Purpose-Robotic-Reward-Models-vi/01_overview.md) — 2026 RSS.
   - 선정 이유: C4/C6의 reward·progress·평가 신호를 비교할 핵심 최신 baseline이다. NEXT: 현재 VLA 정독 흐름의 직접 비교·평가 기준으로 편입한다.
399. [RoboReward: General-Purpose Vision-Language Reward Models for Robotics](../2026/arXiv/2026_arXiv_RoboReward-General-Purpose-Vision-Language-Reward-Models-f/01_overview.md) — 2026 arXiv.
   - 선정 이유: C4의 독립 outcome과 reward model 차이를 정할 직접 기준이다. NEXT: 현재 VLA 정독 흐름의 직접 비교·평가 기준으로 편입한다.
400. [Simple Masked Training Strategies Yield Control Policies That Are Robust to Sensor Failure](../2025/CoRL/2025_CoRL_Simple-Masked-Training-Strategies-Yield-Control-Policies-T/01_overview.md) — 2025 CoRL.
   - 선정 이유: 새 multimodal VLA adaptation 전에 대조할 단순 sensor-dropout 기준이다.
401. [Scaling Robot Policy Evaluation via Discrete Diffusion World Model](../2026/ICML/2026_ICML_Scaling-Robot-Policy-Evaluation-via-Discrete-Diffusion-Wor/01_overview.md) — 2026 ICML.
   - 선정 이유: World-model 평가를 연구할 때 시각 품질과 행동별 순위 신뢰도를 구분할 직접 비교군이다.
402. [Towards Generalizable Safety in Crowd Navigation via Conformal Uncertainty Handling](../2025/CoRL/2025_CoRL_Towards-Generalizable-Safety-in-Crowd-Navigation-via-Confo/01_overview.md) — 2025 CoRL.
   - 선정 이유: GAP-P 계열에서 uncertainty 추가 자체를 새로운 navigation 기여로 삼지 않게 하는 직접 선행이다.
403. [DRILL: Training World Models to Improve Policies, Not Predict Pixels](../2026/NeurIPS/2026_NeurIPS_DRILL-Training-World-Models-to-Improve-Policies-Not-Predic/01_overview.md) — 2026 NeurIPS.
   - 선정 이유: World-model utility라는 broad gap의 직접 충돌을 registry에 남겨 같은 제안을 반복하지 않도록 한다.
404. [Causal World Modeling for Robot Control](../2026/RSS/2026_RSS_Causal-World-Modeling-for-Robot-Control/01_overview.md) — 2026 RSS.
   - 선정 이유: Architecture 통합과 RL 공동 갱신을 구별할 world-action 비교 대상으로 보완한다.
405. [Offline Policy Evaluation for Manipulation Policies via Discounted Liveness Formulation](../2026/RSS/2026_RSS_Offline-Policy-Evaluation-for-Manipulation-Policies-via-Di/01_overview.md) — 2026 RSS.
   - 선정 이유: 실험 rollout 종료와 실제 실패를 구별하고 가치 진단의 target을 정할 최신 기준이다.

## REFERENCE — On-Demand Reading

기존 foundation의 가치를 낮춘 분류가 아니다. 일반 search/control, tactile hardware, whole-body locomotion, generic reconstruction은 선택한 실험의 요구에 따라 다시 읽는다. 현재 tier에서 빠진 기존 읽기 상태와 개인 분석은 history CSV에 보존하며 재승격 시 복원한다.

## ARCHIVE — Search Only

현재 연구 범위 밖의 논문도 registry와 표준 노트에서 검색할 수 있다. 이번 재분류는 논문 수·PDF 보유 여부·venue quota를 기준으로 하지 않는다.
