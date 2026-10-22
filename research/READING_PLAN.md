# VLA Reading Plan for Manipulation and Navigation

- Updated: 2026-10-23 KST
- Source registry: [PAPER.md](../PAPER.md)
- Full tier index: [READING_TIERS.csv](./READING_TIERS.csv)
- Reading tracker: [READING_STATUS.csv](./READING_STATUS.csv)
- Inactive reading history: [READING_STATUS_HISTORY.csv](./READING_STATUS_HISTORY.csv)
- Intensive-reading set: **322 papers** (CORE 47 + NEXT 275)
- Base tier review: 2026-10-19; incremental review: 2026-10-22. 후보별 비교 문헌 47편을 등록하고 NEXT 18 / REFERENCE 29편으로 배정했다. 기존 membership과 사용자 읽기 이력은 유지한다. 연구 초점은 VLA 기반 manipulation·navigation과 action-relevant 3D이며 RL은 선택 사항이다.

## Research Scope and Reading Policy

주 연구축은 VLA를 기반으로 다양한 로봇의 manipulation과 navigation을 다루는 것이다. RL은 연구 질문에 필요할 때 비교할 방법이다. 관측·언어 지시·보상이 실제 행동과 일반화에 주는 효과, 로봇별 적응 비용과 기존 능력 보존을 함께 검토한다. 3D vision은 policy state, spatial memory, affordance, localization, collision/contact reasoning이 실제 행동을 바꾸는 경우 우선한다.

읽기 결과는 [7개 synthesis와 교차 질문 분류](../synthesis/README.md)에 연결한다. 행동 표현·시간/feedback·상태/기억·접촉/실행 가능성·적응/평가 신뢰도를 구분해 비교한다. 후보별 현재 판정과 재개 조건은 [16개 주제 요약](../work/research_candidates/summaries/README.md), 활성 작업은 [TODO](../TODO.md)에서 관리한다. 후보 HOLD/NO-GO와 GPU 확보는 아래 tier membership이나 실제 읽기 상태를 자동으로 바꾸지 않는다.

`observation/history → state/belief/3D memory → language/task/skill decision → VLA/policy/control → contact/failure feedback → adaptation/recovery (RL optional)`

1. **CORE 47편:** 목표 연구의 재사용 가능한 foundation, 대표 policy/RL interface, 데이터·평가 기준이다. 각 논문의 선정 이유를 아래에 기록한다.
2. **NEXT 275편:** 해당 branch의 선행 개념을 확인한 뒤 읽는 전문화·frontier다. CORE 전체 완독을 기다릴 필요는 없다.
3. **REFERENCE 473편:** controller, sensor, embodiment, reconstruction 방법을 실제로 사용할 때 조회한다.
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
| CORE | 47 | VLA 기반 manipulation/navigation의 기반·대표 interface·평가 좌표계 |
| NEXT | 275 | 해당 CORE prerequisite 이후 읽는 직접 관련 전문화·frontier |
| REFERENCE | 473 | 특정 구현·sensor·embodiment가 요구할 때 읽는 기반과 대안 |
| ARCHIVE | 242 | 현재 범위 밖의 검색·역사 자료 |

CORE는 최신 논문 모음이나 고정 quota가 아니다. 중요성과 dependency가 바뀌면 규모도 바뀐다.

## Completion Rule

논문 하나를 정독한 뒤 문제·가정, observation/state/action/control interface, embodiment/task/data/metric/failure, 재사용·반박할 지점을 tracker와 해당 synthesis에 기록한다. 노트의 존재와 source evidence는 사용자의 읽기 상태와 별개다.

## Dependency-Based Reading Batches

단일 canonical plan 안의 비교 경로다. 화살표는 개념적 prerequisite이며 직접 citation을 뜻하지 않는다. 각 경로의 선행을 확인한 뒤 frontier와 baseline을 함께 읽는다.

| Branch | Foundation and comparison spine | NEXT extension | Exit artifact |
|---|---|---|---|
| VLA + RL manipulation | PPO + Diffusion Policy → DPPO; IQL/CQL + Flow Matching → FQL; RLPD/SERL → HIL-SERL; OFT → ConRFT ↔ RLDG | DSRL, RL-100, SimpleVLA-RL, RLux-VLA, USER, RL4VLA, DyGRO-VLA | direct RL vs latent steering vs RL-data distillation; demonstration·interaction·compute를 맞춘 비교표 |
| Action representation and generalization | DAgger/RoboMimic → ACT/Diffusion Policy; DDPM/Flow Matching → Octo/OpenVLA/π0 → FAST/π0.5; DPPO/FQL | Q-chunking → DQC, SpatialVLA, reactive/force VLA | actor chunk·critic horizon·feedback rate·latency·action likelihood와 RL objective 표 |
| Navigation and mobile manipulation | POMDP/Habitat/VLN-CE → ViNT/NoMaD; CLIP/ConceptFusion/VLFM → SayCan/NaVILA; Mobile ALOHA | NaVid → Uni-NaVid/StreamVLN, NavDP/LoGoPlanner, SocialNav, FeedTTA, GOAT, WMNav | goal type·memory·action granularity·collision·social compliance·SPL/success와 reward 접근 조건 표 |
| Action-relevant 3D | RVT ↔ DP3; ConceptFusion ↔ VLFM | LoGoPlanner의 metric memory, PointWorld의 3D dynamics/MPC, VLMaps, PointVLA, Any3D-VLA | policy·data·compute를 고정한 RGB/3D 비교, pose/calibration 접근과 downstream failure |
| Evaluation, contact and recovery | LIBERO/CALVIN/DROID/Habitat; MuJoCo/impedance → Recovery RL/TD-MPC2 | OGBench, RL4VLA, OopsieVerse, Tac2Real, RLBench, ManiSkill3, FurnitureBench, SAFE | task/split·reward·damage·reset·intervention 비용, recovery·OOD protocol |
| World-model policy improvement | TD-MPC2 → Ctrl-World/WMPO/WorldGym | VLAW ↔ VLA-MBPO ↔ RISE; PointWorld의 MPC와 비교; PersistWorld는 prediction-fidelity 참조 | fixed real-data budget, imagined vs real success, failure coverage와 model bias의 분리 |

Batch 산출물과 source location을 확인한 뒤에만 synthesis evidence로 사용한다. Benchmark 간 성공률을 같은 난이도의 점수로 합치지 않는다.

## Research Lenses Across Tracks

- VLA RL과 from-scratch RL, supervised fine-tuning, RL-generated-data distillation을 분리한다.
- Offline demonstration과 online interaction 양, human intervention, reset, reward annotation 비용을 함께 기록한다.
- Navigation의 instruction/goal grounding과 low-level execution을 분리하고 privileged state·map·oracle success 접근을 명시한다.
- 3D 입력의 이득은 action success·collision·sample efficiency·latency와 연결한다.
- 최신 2024–2026 연구도 장기 foundation으로 단정하지 않는다. 공개 interface와 평가 근거가 부족하면 NEXT 또는 REFERENCE로 유지한다.
- Task success 외에 disturbance, long horizon, contact failure, forgetting, recovery를 비교한다.

## CORE — 47 papers

### RL, IL, and policy learning foundations — 20

1. [Learning to Predict by the Methods of Temporal Differences](../1988/Machine-Learning/1988_Machine-Learning_Learning-to-Predict-by-the-Methods-of-Temporal-Differences/01_overview.md) — 1988 Machine Learning.
   - 선정 이유: TD bootstrapping은 SAC·IQL·RLPD의 value target과 offline/online 오차를 이해하는 공통 기반이다.
2. [Policy Gradient Methods for Reinforcement Learning with Function Approximation](../1999/NeurIPS/1999_NeurIPS_Policy-Gradient-Methods-for-Reinforcement-Learning-with-Fu/01_overview.md) — 1999 NeurIPS.
   - 선정 이유: Policy-gradient objective와 gradient estimator는 PPO 및 VLA의 reward-driven 정책 갱신을 비교하는 기반이다.
3. [Proximal Policy Optimization Algorithms](../2017/arxiv/2017_arxiv_Proximal-Policy-Optimization-Algorithms/01_overview.md) — 2017 arXiv.
   - 선정 이유: PPO의 clipped policy update는 on-policy VLA RL과 navigation policy optimization의 대표 비교 기준이다.
4. [Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor](../2018/ICML/2018_ICML_Soft-Actor-Critic-Off-Policy-Maximum-Entropy-Deep-Reinforc/01_overview.md) — 2018 ICML.
   - 선정 이유: Entropy-regularized off-policy actor-critic은 SERL·HIL-SERL 계열의 sample-efficient manipulation RL을 이해하는 기반이다.
5. [Offline Reinforcement Learning with Implicit Q-Learning](../2022/ICLR/2022_ICLR_Offline-Reinforcement-Learning-with-Implicit-Q-Learning/01_overview.md) — 2022 ICLR.
   - 선정 이유: Dataset action support 안에서 value와 policy를 학습하는 IQL은 VLA의 offline initialization과 online 개선을 구분하는 기준이다.
6. [Conservative Q-Learning for Offline Reinforcement Learning](../2020/NeurIPS/2020_NeurIPS_Conservative-Q-Learning-for-Offline-Reinforcement-Learning/01_overview.md) — 2020 NeurIPS.
   - 선정 이유: Offline 데이터 밖 action의 value 과대평가를 다루는 CQL은 IQL·VLA RL의 보수성과 탐색 trade-off를 비교하는 기반이다.
7. [A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning](../2011/AISTATS/2011_AISTATS_A-Reduction-of-Imitation-Learning-and-Structured-Predictio/01_overview.md) — 2011 AISTATS.
   - 선정 이유: DAgger의 distribution shift와 data aggregation은 VLA closed-loop 실패 및 intervention 기반 RL 개선을 해석하는 기반이다.
8. [What Matters in Learning from Offline Human Demonstrations for Robot Manipulation](../2021/CoRL/2021_CoRL_What-Matters-in-Learning-from-Offline-Human-Demonstrations/01_overview.md) — 2021 CoRL.
   - 선정 이유: RoboMimic의 demonstration·observation·평가 설계는 VLA/RL 방법 비교에서 데이터 품질과 정책 효과를 분리하는 기준이다.
9. [Denoising Diffusion Probabilistic Models](../2020/NeurIPS/2020_NeurIPS_Denoising-Diffusion-Probabilistic-Models/01_overview.md) — 2020 NeurIPS.
   - 선정 이유: DDPM의 denoising objective는 Diffusion Policy와 이후 diffusion-action RL의 정책 분포를 이해하는 기반이다.
10. [Flow Matching for Generative Modeling](../2023/ICLR/2023_ICLR_Flow-Matching-for-Generative-Modeling/01_overview.md) — 2023 ICLR.
   - 선정 이유: Flow Matching의 vector-field 학습은 π0 계열 continuous action 생성과 RL 적응의 policy parameterization을 이해하는 기반이다.
11. [Diffusion Policy: Visuomotor Policy Learning via Action Diffusion](../2023/RSS/2023_RSS_Diffusion-Policy-Visuomotor-Policy-Learning-via-Action-Dif/01_overview.md) — 2023 RSS.
   - 선정 이유: Diffusion Policy는 VLA의 개선이 language pretraining·action generation·RL 중 어디서 생기는지 비교할 대표 visuomotor IL baseline이다.
12. [Diffusion Policy Policy Optimization](../2025/ICLR/2025_ICLR_Diffusion-Policy-Policy-Optimization/01_overview.md) — 2025 ICLR.
   - 선정 이유: Foundation bridge. PPO를 denoising policy의 RL fine-tuning으로 연결한다. Diffusion Policy → DPPO → RL-100 등 직접 policy 개선을 비교하는 prerequisite이므로 CORE를 검토할 이유가 있다. VLA 자체를 제안한 논문은 아니다.
13. [Flow Q-Learning](../2025/ICML/2025_ICML_Flow-Q-Learning/01_overview.md) — 2025 ICML.
   - 선정 이유: Foundation bridge. Expressive flow policy와 Q-learning/one-step actor를 연결한다. IQL/CQL 이후 flow-action RL과 Q-chunking 계열의 구현·비교 기준으로 중요하다. 평가가 곧 실제 robot VLA 학습을 입증하는 것은 아니다.
14. [Efficient Online Reinforcement Learning with Offline Data](../2023/ICML/2023_ICML_Efficient-Online-Reinforcement-Learning-with-Offline-Data/01_overview.md) — 2023 ICML.
   - 선정 이유: RLPD의 offline/online replay 결합은 SERL·HIL-SERL에서 demonstration을 활용하는 실제 robot RL 학습 경로의 선행 기반이다.
15. [SERL: A Software Suite for Sample-Efficient Robotic Reinforcement Learning](../2024/ICRA/2024_ICRA_SERL-A-Software-Suite-for-Sample-Efficient-Robotic-Reinfor/01_overview.md) — 2024 ICRA.
   - 선정 이유: SERL은 actor/learner·reward·robot interface를 연결해 HIL-SERL과 VLA RL의 실제 학습 비용을 평가할 공개 시스템 기준이다.
16. [Precise and Dexterous Robotic Manipulation via Human-in-the-Loop Reinforcement Learning](../2024/arXiv/2024_arXiv_Precise-and-Dexterous-Robotic-Manipulation-via-Human-in-th/01_overview.md) — 2024 arXiv.
   - 선정 이유: HIL-SERL은 demonstration·human intervention·reward classifier를 결합한 real-robot RL의 대표 실행 기준이며 ConRFT·RLDG 비교에 필요하다.
17. [RLDG: Robotic Generalist Policy Distillation via Reinforcement Learning](../2025/RSS/2025_RSS_RLDG-Robotic-Generalist-Policy-Distillation-via-Reinforcem/01_overview.md) — 2025 RSS.
   - 선정 이유: RLDG는 specialist RL로 얻은 데이터를 generalist에 증류하는 경로를 제시해 ConRFT의 직접 VLA RL 미세조정과 구분할 핵심 비교 기준이다.
18. [DROID: A Large-Scale In-The-Wild Robot Manipulation Dataset](../2024/RSS/2024_RSS_DROID-A-Large-Scale-In-The-Wild-Robot-Manipulation-Dataset/01_overview.md) — 2024 RSS.
   - 선정 이유: DROID는 실제 환경의 조작 데이터 다양성과 수집 조건을 제공하여 VLA 사전학습·fine-tuning의 데이터 가정을 판단하는 기준이다.
19. [Benchmarking Knowledge Transfer for Lifelong Robot Learning](../2023/NeurIPS/2023_NeurIPS_Benchmarking-Knowledge-Transfer-for-Lifelong-Robot-Learnin/01_overview.md) — 2023 NeurIPS.
   - 선정 이유: LIBERO는 OpenVLA-OFT와 VLA RL의 task suite·transfer 평가를 이해하고 baseline을 공정하게 비교하기 위한 benchmark 기반이다.
20. [Habitat: A Platform for Embodied AI Research](../2019/ICCV/2019_ICCV_Habitat-A-Platform-for-Embodied-AI-Research/01_overview.md) — 2019 ICCV.
   - 선정 이유: Habitat는 navigation의 task·sensor·simulator·generalization protocol을 제공하여 VLN-CE와 navigation RL 평가를 해석하는 기반이다.

### VLA and generalist robot policies — 13

21. [Learning Transferable Visual Models From Natural Language Supervision](../2021/ICML/2021_ICML_Learning-Transferable-Visual-Models-From-Natural-Language/01_overview.md) — 2021 ICML.
   - 선정 이유: CLIP의 image-language alignment는 VLA backbone과 VLFM·ConceptFusion의 semantic grounding을 이해하는 공통 기반이다.
22. [RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control](../2023/CoRL/2023_CoRL_RT-2-Vision-Language-Action-Models-Transfer-Web-Knowledge/01_overview.md) — 2023 CoRL.
   - 선정 이유: RT-2는 pretrained VLM에서 robot action으로의 전이를 정식화해 OpenVLA 및 이후 VLA의 action-token 설계를 이해하는 기반이다.
23. [Open X-Embodiment: Robotic Learning Datasets and RT-X Models](../2024/ICRA/2024_ICRA_Open-X-Embodiment-Robotic-Learning-Datasets-and-RT-X-Model/01_overview.md) — 2024 ICRA.
   - 선정 이유: Open X-Embodiment는 Octo·OpenVLA의 heterogeneous robot-data와 embodiment transfer 가정을 이해하는 데이터 기반이다.
24. [Octo: An Open-Source Generalist Robot Policy](../2024/RSS/2024_RSS_Octo-An-Open-Source-Generalist-Robot-Policy/01_overview.md) — 2024 RSS.
   - 선정 이유: Octo는 공개 generalist policy의 diffusion action·cross-embodiment adaptation을 제공해 VLA 및 RL 개선의 baseline이 된다.
25. [OpenVLA: An Open-Source Vision-Language-Action Model](../2024/CoRL/2024_CoRL_OpenVLA-An-Open-Source-Vision-Language-Action-Model/01_overview.md) — 2024 CoRL.
   - 선정 이유: OpenVLA는 공개 VLA 학습·fine-tuning 경로를 제공하며 OFT와 후속 VLA RL의 backbone 기준이다.
26. [Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success](../2025/RSS/2025_RSS_Fine-Tuning-Vision-Language-Action-Models-Optimizing-Speed/01_overview.md) — 2025 RSS.
   - 선정 이유: OpenVLA-OFT는 action chunking·parallel decoding·continuous action의 강한 supervised baseline으로 RL의 추가 이득을 분리하는 데 필요하다.
27. [π0: A Vision-Language-Action Flow Model for General Robot Control](../2025/RSS/2025_RSS_pi0-A-Vision-Language-Action-Flow-Model-for-General-Robot/01_overview.md) — 2025 RSS.
   - 선정 이유: π0는 VLM과 flow-based action expert를 결합해 이후 flow VLA와 RL 정책 갱신의 action interface를 이해하는 기반이다.
28. [FAST: Efficient Action Tokenization for Vision-Language-Action Models](../2025/RSS/2025_RSS_FAST-Efficient-Action-Tokenization-for-Vision-Language-Act/01_overview.md) — 2025 RSS.
   - 선정 이유: FAST는 action tokenization과 고주파 action chunk 압축을 분리해 continuous-flow와 autoregressive VLA의 비용을 비교하는 기준이다.
29. [π0.5: a Vision-Language-Action Model with Open-World Generalization](../2025/CoRL/2025_CoRL_pi0.5-a-Vision-Language-Action-Model-with-Open-World-Gener/01_overview.md) — 2025 CoRL.
   - 선정 이유: π0.5는 open-world generalization과 이질적 데이터 결합의 대표 시스템으로 RL 개선을 새로운 환경·task transfer와 함께 평가할 기준이다.
30. [ConRFT: A Reinforced Fine-tuning Method for VLA Models via Consistency Policy](../2025/RSS/2025_RSS_ConRFT-A-Reinforced-Fine-tuning-Method-for-VLA-Models-via/01_overview.md) — 2025 RSS.
   - 선정 이유: ConRFT는 offline BC/Q 학습에서 online human-intervention VLA RL로 이어지는 직접 fine-tuning 경로를 제공하는 연구축의 핵심 비교 기준이다.
31. [Do As I Can, Not As I Say: Grounding Language in Robotic Affordances](../2022/CoRL/2022_CoRL_Do-As-I-Can-Not-As-I-Say-Grounding-Language-in-Robotic-Aff/01_overview.md) — 2022 CoRL.
   - 선정 이유: SayCan은 language task proposal과 learned affordance/value를 결합해 VLA+RL의 hierarchical manipulation·navigation 의사결정을 이해하는 기반이다.
32. [NaVILA: Legged Robot Vision-Language-Action Model for Navigation](../2025/RSS/2025_RSS_NaVILA-Legged-Robot-Vision-Language-Action-Model-for-Navig/01_overview.md) — 2025 RSS.
   - 선정 이유: NaVILA는 VLA의 중간 수준 spatial command와 visual locomotion RL을 연결해 navigation에서 reasoning/control interface를 비교하는 대표 시스템이다.
33. [CALVIN: A Benchmark for Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks](../2022/RA-L/2022_RA-L_CALVIN-A-Benchmark-for-Language-Conditioned-Policy-Learnin/01_overview.md) — 2022 RA-L.
   - 선정 이유: CALVIN은 language-conditioned long-horizon manipulation의 연속 skill 성공과 일반화를 평가해 LIBERO와 다른 실패 누적을 비교하는 기준이다.

### Manipulation, contact, tactile, and dexterity — 2

34. [Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware](../2023/RSS/2023_RSS_Learning-Fine-Grained-Bimanual-Manipulation-with-Low-Cost/01_overview.md) — 2023 RSS.
   - 선정 이유: ACT는 action chunk와 temporal aggregation을 사용하는 조작 IL 기준으로 OFT·flow VLA·RL 개선의 action-interface 효과를 분리한다.
35. [3D Diffusion Policy: Generalizable Visuomotor Policy Learning via Simple 3D Representations](../2024/RSS/2024_RSS_3D-Diffusion-Policy-Generalizable-Visuomotor-Policy-Learni/01_overview.md) — 2024 RSS.
   - 선정 이유: DP3는 sparse point-cloud representation을 action diffusion에 연결해 3D 입력이 조작 일반화에 주는 효과를 직접 비교하는 기준이다.

### Planning, control, and whole-body foundations — 4

36. [Planning and Acting in Partially Observable Stochastic Domains](../1998/Artificial-Intelligence/1998_Artificial-Intelligence_Planning-and-Acting-in-Partially-Observable-Stochastic-Dom/01_overview.md) — 1998 Artificial Intelligence.
   - 선정 이유: POMDP의 belief와 partial observability는 navigation memory·VLA history·recovery의 상태 가정을 명시하는 기반이다.
37. [Impedance Control: An Approach to Manipulation: Part I—Theory](../1985/Journal-of-Dynamic-Syste/1985_Journal-of-Dynamic-Syste_Impedance-Control-An-Approach-to-Manipulation-Part-ITheory/01_overview.md) — 1985 Journal of Dynamic Systems, Measurement, and Control.
   - 선정 이유: Impedance control은 contact-rich policy의 action이 low-level compliance와 어떻게 연결되는지 판단하고 RL 성능과 controller 효과를 구분하는 기반이다.
38. [MuJoCo: A Physics Engine for Model-Based Control](../2012/IROS/2012_IROS_MuJoCo-A-Physics-Engine-for-Model-Based-Control/01_overview.md) — 2012 IROS.
   - 선정 이유: MuJoCo는 조작 RL benchmark의 접촉 dynamics와 simulator 가정을 이해해 reward·success·sim-to-real 비교를 해석하는 기반이다.
39. [NoMaD: Goal Masked Diffusion Policies for Navigation and Exploration](../2024/ICRA/2024_ICRA_NoMaD-Goal-Masked-Diffusion-Policies-for-Navigation-and-Ex/01_overview.md) — 2024 ICRA.
   - 선정 이유: NoMaD는 goal-conditioned diffusion과 exploration을 결합해 ViNT 이후 navigation action generation의 비교 기준을 제공한다.

### Robotics-enabling 3D perception — 4

40. [ConceptFusion: Open-set Multimodal 3D Mapping](../2023/RSS/2023_RSS_ConceptFusion-Open-set-Multimodal-3D-Mapping/01_overview.md) — 2023 RSS.
   - 선정 이유: ConceptFusion은 open-set semantic 3D memory가 object navigation과 language-grounded robot action으로 이어지는 representation 기준이다.
41. [RVT: Robotic View Transformer for 3D Object Manipulation](../2023/CoRL/2023_CoRL_RVT-Robotic-View-Transformer-for-3D-Object-Manipulation/01_overview.md) — 2023 CoRL.
   - 선정 이유: RVT는 3D scene을 multi-view action representation으로 연결해 DP3·spatial VLA와 비교할 manipulation 기준이다.
42. [VLFM: Vision-Language Frontier Maps for Zero-Shot Semantic Navigation](../2024/ICRA/2024_ICRA_VLFM-Vision-Language-Frontier-Maps-for-Zero-Shot-Semantic/01_overview.md) — 2024 ICRA.
   - 선정 이유: VLFM은 semantic value map과 frontier exploration을 연결해 learned navigation VLA/RL과 비교할 modular object-navigation 기준이다.
43. [Beyond the Nav-Graph: Vision-and-Language Navigation in Continuous Environments](../2020/ECCV/2020_ECCV_Beyond-the-Nav-Graph-Vision-and-Language-Navigation-in-Con/01_overview.md) — 2020 ECCV.
   - 선정 이유: VLN-CE는 graph waypoint를 넘어 low-level action을 실행하는 continuous navigation formulation으로 NaVILA와 VLN RL의 평가 가정을 구분한다.

### Locomotion, mobile manipulation, and humanoid systems — 2

44. [ViNT: A Foundation Model for Visual Navigation](../2023/CoRL/2023_CoRL_ViNT-A-Foundation-Model-for-Visual-Navigation/01_overview.md) — 2023 CoRL.
   - 선정 이유: ViNT는 다양한 robot navigation 데이터의 goal-conditioned pretraining을 제공해 NoMaD와 navigation VLA의 transfer를 이해하는 기반이다.
45. [Mobile ALOHA: Learning Bimanual Mobile Manipulation using Low-Cost Whole-Body Teleoperation](../2024/CoRL/2024_CoRL_Mobile-ALOHA-Learning-Bimanual-Mobile-Manipulation-using-L/01_overview.md) — 2024 CoRL.
   - 선정 이유: Mobile ALOHA는 base와 bimanual arm을 함께 다루는 데이터·policy interface를 제공해 navigation과 manipulation의 결합 범위를 판단하는 기준이다.

### Safety and robot world models — 2

46. [TD-MPC2: Scalable, Robust World Models for Continuous Control](../2024/ICLR/2024_ICLR_TD-MPC2-Scalable-Robust-World-Models-for-Continuous-Contro/01_overview.md) — 2024 ICLR.
   - 선정 이유: TD-MPC2는 latent dynamics·value·planning을 함께 사용하는 model-based RL 기준으로 VLA+world-model 개선의 비용과 효과를 비교한다.
47. [Recovery RL: Safe Reinforcement Learning with Learned Recovery Zones](../2020/RA-L/2020_RA-L_Recovery-RL-Safe-Reinforcement-Learning-with-Learned-Recov/01_overview.md) — 2020 RA-L.
   - 선정 이유: Recovery RL은 task policy와 recovery policy의 역할을 분리해 VLA/RL의 실패 후 복구 및 안전한 online 학습을 비교하는 기반이다.

해당 branch의 CORE prerequisite를 확인한 뒤 아래 NEXT를 병행한다. 모든 CORE를 먼저 완독할 필요는 없다.

## NEXT — 275 papers

### RL, IL, offline learning, and robot data — 55

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
   - 선정 이유: Current system. 실제 robot online RL에서 edge/cloud·buffer·weight synchronization을 구현할 때 SERL/HIL-SERL의 시스템 확장으로 읽는다. Simulator 중심 RLux-VLA와 역할이 다르다.
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
51. [SAIL: Faster-than-Demonstration Execution of Imitation Learning Policies](../2025/CoRL/2025_CoRL_SAIL-Faster-than-Demonstration-Execution-of-Imitation-Lear/01_overview.md) — 2025 CoRL.
   - 선정 이유: E2에서 retiming·tracking·feedback 이득을 분해할 핵심 IL baseline이다. NEXT: 현재 VLA 정독 흐름의 직접 비교·평가 기준으로 편입한다.
52. [AutoEval: Autonomous Evaluation of Generalist Robot Manipulation Policies in the Real World](../2025/CoRL/2025_CoRL_AutoEval-Autonomous-Evaluation-of-Generalist-Robot-Manipul/01_overview.md) — 2025 CoRL.
   - 선정 이유: C5/C6의 reset ledger와 반복 평가를 설계할 핵심 system 기준이다. NEXT: 현재 VLA 정독 흐름의 직접 비교·평가 기준으로 편입한다.
53. [Is Your Imitation Learning Policy Better than Mine? Policy Comparison with Near-Optimal Stopping](../2025/RSS/2025_RSS_Is-Your-Imitation-Learning-Policy-Better-than-Mine-Policy/01_overview.md) — 2025 RSS.
   - 선정 이유: C6의 trial budget·통계적 중단에 대한 표준 직접 기준이다. NEXT: 현재 VLA 정독 흐름의 직접 비교·평가 기준으로 편입한다.
54. [Beyond Binary Success: Sample-Efficient and Statistically Rigorous Robot Policy Comparison](../2026/RSS/2026_RSS_Beyond-Binary-Success-Sample-Efficient-and-Statistically-R/01_overview.md) — 2026 RSS.
   - 선정 이유: C6의 progress-aware 선택을 신규 통계 방법으로 재주장하지 않도록 하는 최신 기준이다. NEXT: 현재 VLA 정독 흐름의 직접 비교·평가 기준으로 편입한다.
55. [RoboFollow: Unveiling the Instruction Following Mirage in Embodied Agents](../2026/CoRL/2026_CoRL_RoboFollow-Unveiling-the-Instruction-Following-Mirage-in-E/01_overview.md) — 2026 CoRL.
   - 선정 이유: C2/D3의 instruction switch와 성공 지표를 검증할 핵심 benchmark다. NEXT: 현재 VLA 정독 흐름의 직접 비교·평가 기준으로 편입한다.

### VLA, cross-embodiment, and long-horizon planning — 80

56. [What Can RL Bring to VLA Generalization? An Empirical Study](../2025/NeurIPS/2025_NeurIPS_What-Can-RL-Bring-to-VLA-Generalization-An-Empirical-Study/01_overview.md) — 2025 NeurIPS.
   - 선정 이유: Benchmark / empirical study. Visual·semantic·execution generalization을 나누어 SFT와 RL을 비교한다. OpenVLA/OFT 이후 RL의 효과를 주장할 때 필요한 평가 기준이다. 해당 실험에서의 PPO 결과를 모든 VLA에 대한 우열로 일반화하지 않는다.
57. [SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning](../2026/ICLR/2026_ICLR_SimpleVLA-RL-Scaling-VLA-Training-via-Reinforcement-Learni/01_overview.md) — 2026 ICLR.
   - 선정 이유: Current trend / system. OpenVLA-OFT에서 outcome reward와 scalable rollout/training을 다룬다. 현재 OFT → ConRFT 경로에 대규모 simulator RL의 비교 지점을 추가한다. Real-world 결과와 real-world online training의 범위는 구분해서 정독해야 한다.
58. [RLux-VLA: A Unified and Efficient Framework for Reinforcement Learning of Vision-Language-Action Models](../2026/RSS/2026_RSS_RLux-VLA-A-Unified-and-Efficient-Framework-for-Reinforceme/01_overview.md) — 2026 RSS.
   - 선정 이유: Current trend / system. 여러 VLA·RL 알고리즘·시뮬레이터를 비교할 공통 interface와 resource allocation을 제공한다. SimpleVLA-RL 및 ConRFT 실험을 설계할 때 algorithm 효과와 시스템 throughput을 분리하는 데 유용하다. 공식 software에서는 RLinf-VLA라는 이름도 사용한다.
59. [NaVid: Video-based VLM Plans the Next Step for Vision-and-Language Navigation](../2024/RSS/2024_RSS_NaVid-Video-based-VLM-Plans-the-Next-Step-for-Vision-and-L/01_overview.md) — 2024 RSS.
   - 선정 이유: Foundation lineage. RGB video history에서 next action을 출력하는 navigation VLM이다. Uni-NaVid/StreamVLN을 비교할 때 선행 interface를 보충한다. **NaVILA 및 Uni-NaVid와 다른 논문**이다.
60. [StreamVLN: Streaming Vision-and-Language Navigation via SlowFast Context Modeling](../2026/ICRA/2026_ICRA_StreamVLN-Streaming-Vision-and-Language-Navigation-via-Slo/01_overview.md) — 2026 ICRA.
   - 선정 이유: Current trend. Fast action context와 slow history memory를 결합한다. NaVid/Uni-NaVid 이후 긴 video history를 제한된 inference budget으로 처리하는 비교 대상이다. RL 자체의 논문으로 분류하지 않는다.
61. [SocialNav: Training Human-Inspired Foundation Model for Socially-Aware Embodied Navigation](../2026/CVPR/2026_CVPR_SocialNav-Training-Human-Inspired-Foundation-Model-for-Soc/01_overview.md) — 2026 CVPR.
   - 선정 이유: Current trend / dataset. Semantic reasoning과 trajectory generation에 socially compliant reward를 연결한다. NaVILA/VLFM의 task success 중심 비교에 행동 제약을 더한다. 기존 **SocialNav-SUB는 별도 benchmark**다.
62. [DyGRO-VLA: Cross-Task Scaling of Vision–Language–Action Models via Dynamic Grouped Residual Optimization](../2026/ICML/2026_ICML_DyGRO-VLA-Cross-Task-Scaling-of-VisionLanguageAction-Model/01_overview.md) — 2026 ICML.
   - 선정 이유: Current trend. RL fine-tuning 중 task-specific overfitting을 줄이는 것이 연구 질문일 때 RL4VLA/ConRFT와 비교한다. 새 architecture라는 이유만으로 CORE로 올리지는 않는다.
63. [CLIPort: What and Where Pathways for Robotic Manipulation](../2021/CoRL/2021_CoRL_CLIPort-What-and-Where-Pathways-for-Robotic-Manipulation/01_overview.md) — 2021 CoRL.
   - 선정 이유: CLIPort는 semantic grounding과 spatial action을 분리하는 VLA/3D manipulation의 선택적 비교 기준이다.
64. [PaLM-E: An Embodied Multimodal Language Model](../2023/ICML/2023_ICML_PaLM-E-An-Embodied-Multimodal-Language-Model/01_overview.md) — 2023 ICML.
   - 선정 이유: PaLM-E는 embodied multimodal reasoning 계보로 보존하고 직접 action/RL interface 논문 이후에 읽는다.
65. [RT-1: Robotics Transformer for Real-World Control at Scale](../2022/arxiv/2022_arxiv_RT-1-Robotics-Transformer-for-Real-World-Control-at-Scale/01_overview.md) — 2022 arXiv.
   - 선정 이유: RT-1은 RT-2·OpenVLA의 robot-data/action-token 계보를 확인할 때 읽는 기반으로 둔다.
66. [VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models](../2023/CoRL/2023_CoRL_VoxPoser-Composable-3D-Value-Maps-for-Robotic-Manipulation/01_overview.md) — 2023 CoRL.
   - 선정 이유: VoxPoser는 VLA 직접 정책과 language-conditioned 3D planning을 비교하는 전문화로 유지한다.
67. [A Generalist Agent](../2022/arXiv/2022_arXiv_A-Generalist-Agent/01_overview.md) — 2022 arXiv.
68. [AutoRT: Embodied Foundation Models for Large Scale Orchestration of Robotic Agents](../2024/arXiv/2024_arXiv_AutoRT-Embodied-Foundation-Models-for-Large-Scale-Orchestr/01_overview.md) — 2024 arXiv.
69. [RT-H: Action Hierarchies Using Language](../2024/Robotics-Science-and-Sys/2024_Robotics-Science-and-Sys_RT-H-Action-Hierarchies-Using-Language/01_overview.md) — 2024 Robotics: Science and Systems.
70. [Gemini Robotics: Bringing AI into the Physical World](../2025/arXiv/2025_arXiv_Gemini-Robotics-Bringing-AI-into-the-Physical-World/01_overview.md) — 2025 arXiv.
71. [NVIDIA Isaac GR00T N1: An Open Foundation Model for Humanoid Robots](../2025/arXiv/2025_arXiv_NVIDIA-Isaac-GR00T-N1-An-Open-Foundation-Model-for-Humanoi/01_overview.md) — 2025 arXiv.
72. [BC-Z: Zero-Shot Task Generalization with Robotic Imitation Learning](../2022/CoRL/2022_CoRL_BC-Z-Zero-Shot-Task-Generalization-with-Robotic-Imitation/01_overview.md) — 2022 CoRL.
73. [Perceiver-Actor: A Multi-Task Transformer for Robotic Manipulation](../2023/CoRL/2023_CoRL_Perceiver-Actor-A-Multi-Task-Transformer-for-Robotic-Manip/01_overview.md) — 2023 CoRL.
74. [VIMA: General Robot Manipulation with Multimodal Prompts](../2023/ICML/2023_ICML_VIMA-General-Robot-Manipulation-with-Multimodal-Prompts/01_overview.md) — 2023 ICML.
75. [Inner Monologue: Embodied Reasoning through Planning with Language Models](../2022/CoRL/2022_CoRL_Inner-Monologue-Embodied-Reasoning-through-Planning-with-L/01_overview.md) — 2022 CoRL.
76. [SayPlan: Grounding Large Language Models using 3D Scene Graphs for Scalable Robot Task Planning](../2023/CoRL/2023_CoRL_SayPlan-Grounding-Large-Language-Models-using-3D-Scene-Gra/01_overview.md) — 2023 CoRL.
77. [XSkill: Cross Embodiment Skill Discovery](../2023/CoRL/2023_CoRL_XSkill-Cross-Embodiment-Skill-Discovery/01_overview.md) — 2023 CoRL.
78. [Scaling Proprioceptive-Visual Learning with Heterogeneous Pre-trained Transformers](../2024/NeurIPS/2024_NeurIPS_Scaling-Proprioceptive-Visual-Learning-with-Heterogeneous/01_overview.md) — 2024 NeurIPS.
79. [AtomicVLA: Unlocking the Potential of Atomic Skill Learning in Robots](../2026/CVPR/2026_CVPR_AtomicVLA-Unlocking-the-Potential-of-Atomic-Skill-Learning/01_overview.md) — 2026 CVPR.
80. [PALM: Progress-Aware Policy Learning via Affordance Reasoning for Long-Horizon Robotic Manipulation](../2026/CVPR/2026_CVPR_PALM-Progress-Aware-Policy-Learning-via-Affordance-Reasoni/01_overview.md) — 2026 CVPR.
81. [ActiveVLA: Injecting Active Perception into Vision-Language-Action Models for Precise 3D Robotic Manipulation](../2026/CVPR/2026_CVPR_ActiveVLA-Injecting-Active-Perception-into-Vision-Language/01_overview.md) — 2026 CVPR.
82. [Spatial Memory for Out-of-Vision Manipulation in Vision-Language-Action](../2026/ICML/2026_ICML_Spatial-Memory-for-Out-of-Vision-Manipulation-in-Vision-La/01_overview.md) — 2026 ICML.
83. [Counterfactual VLA: Self-Reflective Vision-Language-Action Model with Adaptive Reasoning](../2026/CVPR/2026_CVPR_Counterfactual-VLA-Self-Reflective-Vision-Language-Action/01_overview.md) — 2026 CVPR.
84. [Any3D-VLA: Enhancing VLA Robustness via Diverse Point Clouds](../2026/ICML/2026_ICML_Any3D-VLA-Enhancing-VLA-Robustness-via-Diverse-Point-Cloud/01_overview.md) — 2026 ICML.
85. [MomaGraph: State-Aware Unified Scene Graphs with Vision-Language Models for Embodied Task Planning](../2026/ICLR/2026_ICLR_MomaGraph-State-Aware-Unified-Scene-Graphs-with-Vision-Lan/01_overview.md) — 2026 ICLR.
86. [AVA-VLA: Improving Vision-Language-Action Models with Active Visual Attention](../2026/CVPR/2026_CVPR_AVA-VLA-Improving-Vision-Language-Action-Models-with-Activ/01_overview.md) — 2026 CVPR.
87. [VLA-Arena: An Open-Source Framework for Benchmarking Vision-Language-Action Models](../2026/ICML/2026_ICML_VLA-Arena-An-Open-Source-Framework-for-Benchmarking-Vision/01_overview.md) — 2026 ICML.
88. [SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Models](../2025/RSS/2025_RSS_SpatialVLA-Exploring-Spatial-Representations-for-Visual-La/01_overview.md) — 2025 RSS.
89. [From Spatial to Actions: Grounding Vision-Language-Action Model in Spatial Foundation Priors](../2026/ICLR/2026_ICLR_From-Spatial-to-Actions-Grounding-Vision-Language-Action-M/01_overview.md) — 2026 ICLR.
90. [Uni-NaVid: A Video-based Vision-Language-Action Model for Unifying Embodied Navigation Tasks](../2025/RSS/2025_RSS_Uni-NaVid-A-Video-based-Vision-Language-Action-Model-for-U/01_overview.md) — 2025 RSS.
91. [Learning to Act Anywhere with Task-centric Latent Actions](../2025/RSS/2025_RSS_Learning-to-Act-Anywhere-with-Task-centric-Latent-Actions/01_overview.md) — 2025 RSS.
92. [CLIP-RT: Learning Language-Conditioned Robotic Policies from Natural Language Supervision](../2025/RSS/2025_RSS_CLIP-RT-Learning-Language-Conditioned-Robotic-Policies-fro/01_overview.md) — 2025 RSS.
93. [CodeDiffuser: Attention-Enhanced Diffusion Policy via VLM-Generated Code for Instruction Ambiguity](../2025/RSS/2025_RSS_CodeDiffuser-Attention-Enhanced-Diffusion-Policy-via-VLM-G/01_overview.md) — 2025 RSS.
94. [PartInstruct: Part-level Instruction Following for Fine-grained Robot Manipulation](../2025/RSS/2025_RSS_PartInstruct-Part-level-Instruction-Following-for-Fine-gra/01_overview.md) — 2025 RSS.
95. [Manual2Skill: Learning to Read Manuals and Acquire Robotic Skills for Furniture Assembly Using Vision-Language Models](../2025/RSS/2025_RSS_Manual2Skill-Learning-to-Read-Manuals-and-Acquire-Robotic/01_overview.md) — 2025 RSS.
96. [SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics](../2025/arXiv/2025_arXiv_SmolVLA-A-Vision-Language-Action-Model-for-Affordable-and/01_overview.md) — 2025 arXiv.
97. [Gemini Robotics 1.5: Pushing the Frontier of Generalist Robots with Advanced Embodied Reasoning, Thinking, and Motion Transfer](../2025/arXiv/2025_arXiv_Gemini-Robotics-1.5-Pushing-the-Frontier-of-Generalist-Rob/01_overview.md) — 2025 arXiv.
98. [GR00T N1.5: An Improved Open Foundation Model for Generalist Humanoid Robots](../2025/Technical-Report/2025_Technical-Report_GR00T-N1.5-An-Improved-Open-Foundation-Model-for-Generalis/01_overview.md) — 2025 Technical Report.
99. [GR00T N1.6: An Improved Open Foundation Model for Generalist Humanoid Robots](../2025/Technical-Report/2025_Technical-Report_GR00T-N1.6-An-Improved-Open-Foundation-Model-for-Generalis/01_overview.md) — 2025 Technical Report.
100. [Grounding Actions in Camera Space: Observation-Centric Vision-Language-Action Policy](../2026/AAAI/2026_AAAI_Grounding-Actions-in-Camera-Space-Observation-Centric-Visi/01_overview.md) — 2026 AAAI.
101. [ReKep: Spatio-Temporal Reasoning of Relational Keypoint Constraints for Robotic Manipulation](../2024/CoRL/2024_CoRL_ReKep-Spatio-Temporal-Reasoning-of-Relational-Keypoint-Con/01_overview.md) — 2024 CoRL.
102. [VoxAct-B: Voxel-Based Acting and Stabilizing Policy for Bimanual Manipulation](../2024/CoRL/2024_CoRL_VoxAct-B-Voxel-Based-Acting-and-Stabilizing-Policy-for-Bim/01_overview.md) — 2024 CoRL.
103. [3DS-VLA: A 3D Spatial-Aware Vision Language Action Model for Robust Multi-Task Manipulation](../2025/CoRL/2025_CoRL_3DS-VLA-A-3D-Spatial-Aware-Vision-Language-Action-Model-fo/01_overview.md) — 2025 CoRL.
104. [GraspVLA: a Grasping Foundation Model Pre-trained on Billion-scale Synthetic Action Data](../2025/CoRL/2025_CoRL_GraspVLA-a-Grasping-Foundation-Model-Pre-trained-on-Billio/01_overview.md) — 2025 CoRL.
105. [Long-VLA: Unleashing Long-Horizon Capability of Vision Language Action Model for Robot Manipulation](../2025/CoRL/2025_CoRL_Long-VLA-Unleashing-Long-Horizon-Capability-of-Vision-Lang/01_overview.md) — 2025 CoRL.
106. [RDT-1B: a Diffusion Foundation Model for Bimanual Manipulation](../2025/ICLR/2025_ICLR_RDT-1B-a-Diffusion-Foundation-Model-for-Bimanual-Manipulat/01_overview.md) — 2025 ICLR.
107. [AHA: A Vision-Language-Model for Detecting and Reasoning Over Failures in Robotic Manipulation](../2025/ICLR/2025_ICLR_AHA-A-Vision-Language-Model-for-Detecting-and-Reasoning-Ov/01_overview.md) — 2025 ICLR.
108. [SIMPACT: Simulation-Enabled Action Planning using Vision-Language Models](../2026/CVPR/2026_CVPR_SIMPACT-Simulation-Enabled-Action-Planning-using-Vision-La/01_overview.md) — 2026 CVPR.
109. [Vision-Language Foundation Models as Effective Robot Imitators](../2024/ICLR/2024_ICLR_Vision-Language-Foundation-Models-as-Effective-Robot-Imita/01_overview.md) — 2024 ICLR.
110. [Unleashing Large-Scale Video Generative Pre-training for Visual Robot Manipulation](../2024/ICLR/2024_ICLR_Unleashing-Large-Scale-Video-Generative-Pre-training-for-V/01_overview.md) — 2024 ICLR.
111. [RoboMamba: Efficient Vision-Language-Action Model for Robotic Reasoning and Manipulation](../2024/NeurIPS/2024_NeurIPS_RoboMamba-Efficient-Vision-Language-Action-Model-for-Robot/01_overview.md) — 2024 NeurIPS.
112. [Latent Action Pretraining from Videos](../2025/ICLR/2025_ICLR_Latent-Action-Pretraining-from-Videos/01_overview.md) — 2025 ICLR.
113. [3D-VLA: A 3D Vision-Language-Action Generative World Model](../2024/ICML/2024_ICML_3D-VLA-A-3D-Vision-Language-Action-Generative-World-Model/01_overview.md) — 2024 ICML.
114. [VLMimic: Vision Language Models are Visual Imitation Learner for Fine-grained Actions](../2024/NeurIPS/2024_NeurIPS_VLMimic-Vision-Language-Models-are-Visual-Imitation-Learne/01_overview.md) — 2024 NeurIPS.
115. [MIRAGE: Cross-Embodiment Zero-Shot Policy Transfer with Cross-Painting](../2024/RSS/2024_RSS_MIRAGE-Cross-Embodiment-Zero-Shot-Policy-Transfer-with-Cro/01_overview.md) — 2024 RSS.
116. [Pushing the Limits of Cross-Embodiment Learning for Manipulation and Navigation](../2024/RSS/2024_RSS_Pushing-the-Limits-of-Cross-Embodiment-Learning-for-Manipu/01_overview.md) — 2024 RSS.
117. [LIBERO-Safety: A Comprehensive Benchmark for Physical and Semantic Safety in Vision-Language-Action Models](../2026/ECCV/2026_ECCV_LIBERO-Safety-A-Comprehensive-Benchmark-for-Physical-and-S/01_overview.md) — 2026 ECCV.
118. [DISC: Decoupling Instruction from State-Conditioned Control via Policy Generation](../2026/RSS/2026_RSS_DISC-Decoupling-Instruction-from-State-Conditioned-Control/01_overview.md) — 2026 RSS.
   - 선정 이유: OpenVLA 이후 language-conditioned 행동 여부를 확인할 직접 비교군이므로 NEXT다.
119. [How Should Vision-Language-Action Models Use Proprioceptive State?](../2026/arXiv/2026_arXiv_How-Should-Vision-Language-Action-Models-Use-Proprioceptiv/01_overview.md) — 2026 arXiv.
   - 선정 이유: D1에서 state 사용과 history 효과를 먼저 입증할 NEXT prerequisite다.
120. [Self-Adaptive VLA for Robust Robot Deployment](../2026/arXiv/2026_arXiv_Self-Adaptive-VLA-for-Robust-Robot-Deployment/01_overview.md) — 2026 arXiv.
   - 선정 이유: D1의 hardware-cause adaptation과 가장 가까운 NEXT 비교군이다.
121. [ReViP: Mitigating False Completion in Vision-Language-Action Models with Vision-Proprioception Rebalance](../2026/arXiv/2026_arXiv_ReViP-Mitigating-False-Completion-in-Vision-Language-Actio/01_overview.md) — 2026 arXiv.
   - 선정 이유: D1에서 단순 vision 강화나 stage feedback을 새 기여로 재주장하지 않게 하는 NEXT다.
122. [CoRE-VLA: Towards Scalable and Robust Vision-Language-Action Modeling via Conditional Routing of Experts](../2026/arXiv/2026_arXiv_CoRE-VLA-Towards-Scalable-and-Robust-Vision-Language-Actio/01_overview.md) — 2026 arXiv.
   - 선정 이유: D1의 modality robustness와 직접 겹치는 NEXT다. 카메라 복원 CoRe-VLA와 다른 논문이다.
123. [CoRe-VLA: Preserving Cross-View Coordination in VLAs under Camera Shifts](../2026/arXiv/2026_arXiv_CoRe-VLA-Preserving-Cross-View-Coordination-in-VLAs-under/01_overview.md) — 2026 arXiv.
   - 선정 이유: D1 camera-shift 보정의 직접 NEXT baseline이다. Conditional Routing CoRE-VLA와 별도 identity다.
124. [When would Vision-Proprioception Policies Fail in Robotic Manipulation?](../2026/ICLR/2026_ICLR_When-would-Vision-Proprioception-Policies-Fail-in-Robotic/01_overview.md) — 2026 ICLR.
   - 선정 이유: D1에서 modality dominance를 새 발견으로 주장하지 않도록 추가한 직접 NEXT다.
125. [Pretrained Vision-Language-Action Models are Surprisingly Resistant to Forgetting in Continual Learning](../2026/ICML/2026_ICML_Pretrained-Vision-Language-Action-Models-are-Surprisingly/01_overview.md) — 2026 ICML.
   - 선정 이유: E1에서 복잡한 replay selector 전에 확인할 강한 단순 기준이다. NEXT: 현재 VLA 정독 흐름의 직접 비교·평가 기준으로 편입한다.
126. [Actions as Language: Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting](../2026/ICLR/2026_ICLR_Actions-as-Language-Fine-Tuning-VLMs-into-VLAs-Without-Cat/01_overview.md) — 2026 ICLR.
   - 선정 이유: 의미 능력 보존이라는 넓은 방향의 직접 선행이며 action interface 비교에도 필요하다. NEXT: 현재 VLA 정독 흐름의 직접 비교·평가 기준으로 편입한다.
127. [LAP: Language-Action Pre-training Enables Zero-Shot Cross-Embodiment Transfer](../2026/RSS/2026_RSS_LAP-Language-Action-Pre-training-Enables-Zero-Shot-Cross-E/01_overview.md) — 2026 RSS.
   - 선정 이유: Cross-embodiment VLA interface를 비교할 최신 직접 선행이다. NEXT: 현재 VLA 정독 흐름의 직접 비교·평가 기준으로 편입한다.
128. [Adaptive Action Chunking at Inference-time for Vision-Language-Action Models](../2026/CVPR/2026_CVPR_Adaptive-Action-Chunking-at-Inference-time-for-Vision-Lang/01_overview.md) — 2026 CVPR.
   - 선정 이유: E2의 adaptive horizon 주장에 대한 직접 baseline이다. NEXT: 현재 VLA 정독 흐름의 직접 비교·평가 기준으로 편입한다.
129. [Memory Anchors for Continual Robot Learning](../2026/CoRL/2026_CoRL_Memory-Anchors-for-Continual-Robot-Learning/01_overview.md) — 2026 CoRL.
   - 선정 이유: E1의 action-conflict replay와 가장 가까운 직접 비교군이다. NEXT: 현재 VLA 정독 흐름의 직접 비교·평가 기준으로 편입한다.
130. [Rethinking Visual-Language-Action Model Scaling: Alignment, Mixture, and Regularization](../2026/arXiv/2026_arXiv_Rethinking-Visual-Language-Action-Model-Scaling-Alignment/01_overview.md) — 2026 arXiv.
   - 선정 이유: E1에서 정상 action 정렬·mixture 자체의 설명력을 먼저 제거할 기준이다. NEXT: 현재 VLA 정독 흐름의 직접 비교·평가 기준으로 편입한다.
131. [Can Vision-Language-Action Models Learn from Real-World Data Continually without Forgetting?](../2026/arXiv/2026_arXiv_Can-Vision-Language-Action-Models-Learn-from-Real-World-Da/01_overview.md) — 2026 arXiv.
   - 선정 이유: E1의 실환경 단순 baseline과 compute-matched 비교에 필요한 연구다. NEXT: 현재 VLA 정독 흐름의 직접 비교·평가 기준으로 편입한다.
132. [SPACE: Enabling Learning from Cross-Robot Data Toward Generalist Policies](../2026/arXiv/2026_arXiv_SPACE-Enabling-Learning-from-Cross-Robot-Data-Toward-Gener/01_overview.md) — 2026 arXiv.
   - 선정 이유: E1/E2에서 정상적인 state-effect 표현과 dynamics adapter의 강한 대안이다. NEXT: 현재 VLA 정독 흐름의 직접 비교·평가 기준으로 편입한다.
133. [Real-Time Execution of Action Chunking Flow Policies](../2025/NeurIPS/2025_NeurIPS_Real-Time-Execution-of-Action-Chunking-Flow-Policies/01_overview.md) — 2025 NeurIPS.
   - 선정 이유: 초기 지연 후보와 E2가 반드시 비교할 표준 실행 baseline이다. NEXT: 현재 VLA 정독 흐름의 직접 비교·평가 기준으로 편입한다.
134. [Learning High-Frequency Continuous Action Chunks in Latent Space](../2026/ICML/2026_ICML_Learning-High-Frequency-Continuous-Action-Chunks-in-Latent/01_overview.md) — 2026 ICML.
   - 선정 이유: E2에서 고주파 표현과 controller 변경을 분리할 직접 기준이다. NEXT: 현재 VLA 정독 흐름의 직접 비교·평가 기준으로 편입한다.
135. [CounterAlign: Counterfactual Supervision for Vision-Language-Action Models](../2026/CoRL/2026_CoRL_CounterAlign-Counterfactual-Supervision-for-Vision-Languag/01_overview.md) — 2026 CoRL.
   - 선정 이유: C2와 새로운 VLA 탐색에서 지시 준수 개선의 직접 baseline이다. NEXT: 현재 VLA 정독 흐름의 직접 비교·평가 기준으로 편입한다.

### Contact-rich, deformable, force, and dexterous manipulation — 49

136. [Tac2Real: Reliable and GPU Visuotactile Simulation for Online Reinforcement Learning and Zero-Shot Real-World Deployment](../2026/ECCV/2026_ECCV_Tac2Real-Reliable-and-GPU-Visuotactile-Simulation-for-Onli/01_overview.md) — 2026 ECCV.
   - 선정 이유: Current trend / simulator. Tactile feedback을 이용하는 insertion·contact RL을 선택할 때 relevant하다. HIL-SERL 등 실제 interaction 학습과 simulation fidelity/transfer를 비교한다. Peg insertion 결과를 범용 dexterity로 확대하지 않는다.
137. [GraspNet-1Billion: A Large-Scale Benchmark for General Object Grasping](../2020/CVPR/2020_CVPR_GraspNet-1Billion-A-Large-Scale-Benchmark-for-General-Obje/01_overview.md) — 2020 CVPR.
   - 선정 이유: GraspNet은 grasp perception을 task input이나 benchmark로 쓰는 manipulation branch에서 읽는다.
138. [Contact-GraspNet: Efficient 6-DoF Grasp Generation in Cluttered Scenes](../2021/ICRA/2021_ICRA_Contact-GraspNet-Efficient-6-DoF-Grasp-Generation-in-Clutt/01_overview.md) — 2021 ICRA.
   - 선정 이유: Contact-GraspNet은 6-DoF grasp proposal을 사용하는 modular manipulation baseline으로 유지한다.
139. [Factory: Fast Contact for Robotic Assembly](../2022/RSS/2022_RSS_Factory-Fast-Contact-for-Robotic-Assembly/01_overview.md) — 2022 RSS.
   - 선정 이유: Factory는 contact-rich assembly를 sim-to-real RL 실험으로 선택할 때 읽는다.
140. [RoboPack: Learning Tactile-Informed Dynamics Models for Dense Packing](../2024/RSS/2024_RSS_RoboPack-Learning-Tactile-Informed-Dynamics-Models-for-Den/01_overview.md) — 2024 RSS.
   - 선정 이유: RoboPack은 tactile dynamics를 policy feedback에 추가하는 manipulation 전문화로 유지한다.
141. [Dense Object Nets: Learning Dense Visual Object Descriptors By and For Robotic Manipulation](../2018/CoRL/2018_CoRL_Dense-Object-Nets-Learning-Dense-Visual-Object-Descriptors/01_overview.md) — 2018 CoRL.
142. [UMPNet: Universal Manipulation Policy Network for Articulated Objects](../2022/RA-L/2022_RA-L_UMPNet-Universal-Manipulation-Policy-Network-for-Articulat/01_overview.md) — 2022 RA-L.
143. [Distilled Feature Fields Enable Few-Shot Language-Guided Manipulation](../2023/CoRL/2023_CoRL_Distilled-Feature-Fields-Enable-Few-Shot-Language-Guided-M/01_overview.md) — 2023 CoRL.
144. [GaussianGrasper: 3D Language Gaussian Splatting for Open-vocabulary Robotic Grasping](../2024/RA-L/2024_RA-L_GaussianGrasper-3D-Language-Gaussian-Splatting-for-Open-vo/01_overview.md) — 2024 RA-L.
145. [ManiGaussian: Dynamic Gaussian Splatting for Multi-task Robotic Manipulation](../2024/ECCV/2024_ECCV_ManiGaussian-Dynamic-Gaussian-Splatting-for-Multi-task-Rob/01_overview.md) — 2024 ECCV.
146. [Gaussian Splatting Visual MPC for Granular Media Manipulation](../2025/ICRA/2025_ICRA_Gaussian-Splatting-Visual-MPC-for-Granular-Media-Manipulat/01_overview.md) — 2025 ICRA.
147. [Persistent Object Gaussian Splat (POGS) for Tracking Human and Robot Manipulation of Irregularly Shaped Objects](../2025/ICRA/2025_ICRA_Persistent-Object-Gaussian-Splat-POGS-for-Tracking-Human-a/01_overview.md) — 2025 ICRA.
148. [DIGIT: A Novel Design for a Low-Cost Compact High-Resolution Tactile Sensor with Application to In-Hand Manipulation](../2020/IEEE-Robotics-and-Automa/2020_IEEE-Robotics-and-Automa_DIGIT-A-Novel-Design-for-a-Low-Cost-Compact-High-Resolutio/01_overview.md) — 2020 IEEE Robotics and Automation Letters.
149. [DeXtreme: Transfer of Agile In-hand Manipulation from Simulation to Reality](../2023/ICRA/2023_ICRA_DeXtreme-Transfer-of-Agile-In-hand-Manipulation-from-Simul/01_overview.md) — 2023 ICRA.
150. [Control-Limited Differential Dynamic Programming](../2014/ICRA/2014_ICRA_Control-Limited-Differential-Dynamic-Programming/01_overview.md) — 2014 ICRA.
151. [In-Hand Manipulation via Motion Cones](../2019/RSS/2019_RSS_In-Hand-Manipulation-via-Motion-Cones/01_overview.md) — 2019 RSS.
152. [Towards Tight Convex Relaxations for Contact-Rich Manipulation](../2024/RSS/2024_RSS_Towards-Tight-Convex-Relaxations-for-Contact-Rich-Manipula/01_overview.md) — 2024 RSS.
153. [Physics-Driven Data Generation for Contact-Rich Manipulation via Trajectory Optimization](../2025/RSS/2025_RSS_Physics-Driven-Data-Generation-for-Contact-Rich-Manipulati/01_overview.md) — 2025 RSS.
154. [Complementarity-Free Multi-Contact Modeling and Optimization for Dexterous Manipulation](../2025/RSS/2025_RSS_Complementarity-Free-Multi-Contact-Modeling-and-Optimizati/01_overview.md) — 2025 RSS.
155. [SoftGym: Benchmarking Deep Reinforcement Learning for Deformable Object Manipulation](../2020/CoRL/2020_CoRL_SoftGym-Benchmarking-Deep-Reinforcement-Learning-for-Defor/01_overview.md) — 2020 CoRL.
156. [DiffSkill: Skill Abstraction from Differentiable Physics for Deformable Object Manipulations with Tools](../2022/ICLR/2022_ICLR_DiffSkill-Skill-Abstraction-from-Differentiable-Physics-fo/01_overview.md) — 2022 ICLR.
157. [Neural Descriptor Fields: SE(3)-Equivariant Object Representations for Manipulation](../2021/CoRL/2021_CoRL_Neural-Descriptor-Fields-SE3-Equivariant-Object-Representa/01_overview.md) — 2021 CoRL.
158. [Diffusion-EDFs: Bi-equivariant Denoising Generative Modeling on SE(3) for Visual Robotic Manipulation](../2024/CVPR/2024_CVPR_Diffusion-EDFs-Bi-equivariant-Denoising-Generative-Modelin/01_overview.md) — 2024 CVPR.
159. [IndustReal: Transferring Contact-Rich Assembly Tasks from Simulation to Reality](../2023/RSS/2023_RSS_IndustReal-Transferring-Contact-Rich-Assembly-Tasks-from-S/01_overview.md) — 2023 RSS.
160. [Binding Touch to Everything: Learning Unified Multimodal Tactile Representations](../2024/CVPR/2024_CVPR_Binding-Touch-to-Everything-Learning-Unified-Multimodal-Ta/01_overview.md) — 2024 CVPR.
161. [DenseMatcher: Learning 3D Semantic Correspondence for Category-Level Manipulation from a Single Demo](../2025/ICLR/2025_ICLR_DenseMatcher-Learning-3D-Semantic-Correspondence-for-Categ/01_overview.md) — 2025 ICLR.
162. [G3Flow: Generative 3D Semantic Flow for Pose-aware and Generalizable Object Manipulation](../2025/CVPR/2025_CVPR_G3Flow-Generative-3D-Semantic-Flow-for-Pose-aware-and-Gene/01_overview.md) — 2025 CVPR.
163. [Reactive Diffusion Policy: Slow-Fast Visual-Tactile Policy Learning for Contact-Rich Manipulation](../2025/RSS/2025_RSS_Reactive-Diffusion-Policy-Slow-Fast-Visual-Tactile-Policy/01_overview.md) — 2025 RSS.
164. [AT-VLA: Adaptive Tactile Injection for Enhanced Feedback Reaction in Vision-Language-Action Models](../2026/CVPR/2026_CVPR_AT-VLA-Adaptive-Tactile-Injection-for-Enhanced-Feedback-Re/01_overview.md) — 2026 CVPR.
165. [ForceVLA2: Unleashing Hybrid Force-Position Control with Force Awareness for Contact-Rich Manipulation](../2026/CVPR/2026_CVPR_ForceVLA2-Unleashing-Hybrid-Force-Position-Control-with-Fo/01_overview.md) — 2026 CVPR.
166. [Dexterous World Models](../2026/CVPR/2026_CVPR_Dexterous-World-Models/01_overview.md) — 2026 CVPR.
167. [EquAct: An SE(3)-Equivariant Multi-Task Transformer for 3D Robotic Manipulation](../2026/ICLR/2026_ICLR_EquAct-An-SE3-Equivariant-Multi-Task-Transformer-for-3D-Ro/01_overview.md) — 2026 ICLR.
168. [Tabero: Learning Gentle Manipulation with Closed-Loop Force Feedback from Vision, Touch, and Language](../2026/ICML/2026_ICML_Tabero-Learning-Gentle-Manipulation-with-Closed-Loop-Force/01_overview.md) — 2026 ICML.
169. [TactAlign: Human-to-Robot Policy Transfer via Tactile Alignment](../2026/RSS/2026_RSS_TactAlign-Human-to-Robot-Policy-Transfer-via-Tactile-Align/01_overview.md) — 2026 RSS.
170. [DexterityGen: Foundation Controller for Unprecedented Dexterity](../2026/RSS/2026_RSS_DexterityGen-Foundation-Controller-for-Unprecedented-Dexte/01_overview.md) — 2026 RSS.
171. [V-HOP: Visuo-Haptic 6D Object Pose Tracking](../2025/RSS/2025_RSS_V-HOP-Visuo-Haptic-6D-Object-Pose-Tracking/01_overview.md) — 2025 RSS.
172. [PP-Tac: Paper Picking Using Omnidirectional Tactile Feedback in Dexterous Robotic Hands](../2025/RSS/2025_RSS_PP-Tac-Paper-Picking-Using-Omnidirectional-Tactile-Feedbac/01_overview.md) — 2025 RSS.
173. [GeoDEx: A Unified Geometric Framework for Tactile Dexterous and Extrinsic Manipulation under Force Uncertainty](../2025/RSS/2025_RSS_GeoDEx-A-Unified-Geometric-Framework-for-Tactile-Dexterous/01_overview.md) — 2025 RSS.
174. [Demonstrating REASSEMBLE: A Multimodal Dataset for Contact-rich Robotic Assembly and Disassembly](../2025/RSS/2025_RSS_Demonstrating-REASSEMBLE-A-Multimodal-Dataset-for-Contact/01_overview.md) — 2025 RSS.
175. [Robust Peg-in-Hole Assembly under Uncertainties via Compliant and Interactive Contact-Rich Manipulation](../2025/RSS/2025_RSS_Robust-Peg-in-Hole-Assembly-under-Uncertainties-via-Compli/01_overview.md) — 2025 RSS.
176. [FACTR: Force-Attending Curriculum Training for Contact-Rich Policy Learning](../2025/RSS/2025_RSS_FACTR-Force-Attending-Curriculum-Training-for-Contact-Rich/01_overview.md) — 2025 RSS.
177. [CordViP: Correspondence-based Visuomotor Policy for Dexterous Manipulation in Real-World](../2025/RSS/2025_RSS_CordViP-Correspondence-based-Visuomotor-Policy-for-Dextero/01_overview.md) — 2025 RSS.
178. [FlowPolicy: Enabling Fast and Robust 3D Flow-Based Policy via Consistency Flow Matching for Robot Manipulation](../2025/AAAI/2025_AAAI_FlowPolicy-Enabling-Fast-and-Robust-3D-Flow-Based-Policy-v/01_overview.md) — 2025 AAAI.
179. [Sparsh: Self-supervised touch representations for vision-based tactile sensing](../2024/CoRL/2024_CoRL_Sparsh-Self-supervised-touch-representations-for-vision-ba/01_overview.md) — 2024 CoRL.
180. [Octopi: Object Property Reasoning with Large Tactile-Language Models](../2024/RSS/2024_RSS_Octopi-Object-Property-Reasoning-with-Large-Tactile-Langua/01_overview.md) — 2024 RSS.
181. [OPEN TEACH: A Versatile Teleoperation System for Robotic Manipulation](../2024/CoRL/2024_CoRL_OPEN-TEACH-A-Versatile-Teleoperation-System-for-Robotic-Ma/01_overview.md) — 2024 CoRL.
182. [FurnitureBench: Reproducible Real-World Benchmark for Long-Horizon Complex Manipulation](../2023/RSS/2023_RSS_FurnitureBench-Reproducible-Real-World-Benchmark-for-Long/01_overview.md) — 2023 RSS.
183. [Learning Robotic Manipulation Policies from Point Clouds with Conditional Flow Matching](../2024/CoRL/2024_CoRL_Learning-Robotic-Manipulation-Policies-from-Point-Clouds-w/01_overview.md) — 2024 CoRL.
184. [Contact-Anchored Policies: Contact Conditioning Creates Strong Robot Utility Models](../2026/RSS/2026_RSS_Contact-Anchored-Policies-Contact-Conditioning-Creates-Str/01_overview.md) — 2026 RSS.
   - 선정 이유: VLA의 이득이 task specification 차이인지 가릴 강한 non-VLA baseline이므로 NEXT다.

### Planning, control, simulation, and TAMP extensions — 16

185. [NavDP: Learning Sim-to-Real Navigation Diffusion Policy with Privileged Information Guidance](../2026/ICRA/2026_ICRA_NavDP-Learning-Sim-to-Real-Navigation-Diffusion-Policy-wit/01_overview.md) — 2026 ICRA.
   - 선정 이유: Current trend. Simulation training에서 real-world cross-embodiment local navigation으로 이어지는 경로를 보충한다. NoMaD/ViNT의 local policy와 비교할 대상이며, 논문 자체를 language-conditioned VLA RL로 부르지는 않는다.
186. [Rapidly-Exploring Random Trees: A New Tool for Path Planning](../1998/Technical-Report/1998_Technical-Report_Rapidly-Exploring-Random-Trees-A-New-Tool-for-Path-Plannin/01_overview.md) — 1998 Technical Report.
   - 선정 이유: RRT는 learned navigation·manipulation과 motion-planning baseline을 비교하는 선택적 선행으로 유지한다.
187. [Information Theoretic MPC for Model-Based Reinforcement Learning](../2017/ICRA/2017_ICRA_Information-Theoretic-MPC-for-Model-Based-Reinforcement-Le/01_overview.md) — 2017 ICRA.
   - 선정 이유: MPPI는 VLA action과 model-based local control을 결합할 때 필요한 전문화로 둔다.
188. [PDDLStream: Integrating Symbolic Planners and Blackbox Samplers via Optimistic Adaptive Planning](../2020/ICAPS/2020_ICAPS_PDDLStream-Integrating-Symbolic-Planners-and-Blackbox-Samp/01_overview.md) — 2020 ICAPS.
   - 선정 이유: PDDLStream은 SayCan 이후 symbolic/TAMP 대안을 검토하는 계획 branch로 둔다.
189. [Logic-Geometric Programming: An Optimization-Based Approach to Combined Task and Motion Planning](../2015/IJCAI/2015_IJCAI_Logic-Geometric-Programming-An-Optimization-Based-Approach/01_overview.md) — 2015 IJCAI.
190. [FFRob: Leveraging Symbolic Planning for Efficient Task and Motion Planning](../2018/The-International-Journa/2018_The-International-Journa_FFRob-Leveraging-Symbolic-Planning-for-Efficient-Task-and/01_overview.md) — 2018 The International Journal of Robotics Research.
191. [Kinodynamic Trajectory Following with STELA: Simultaneous Trajectory Estimation & Local Adaptation](../2025/RSS/2025_RSS_Kinodynamic-Trajectory-Following-with-STELA-Simultaneous-T/01_overview.md) — 2025 RSS.
192. [Instruction-Augmented Long-Horizon Planning: Embedding Grounding Mechanisms in Embodied Mobile Manipulation](../2025/AAAI/2025_AAAI_Instruction-Augmented-Long-Horizon-Planning-Embedding-Grou/01_overview.md) — 2025 AAAI.
193. [Neural Assembler: Learning to Generate Fine-Grained Robotic Assembly Instructions from Multi-View Images](../2025/AAAI/2025_AAAI_Neural-Assembler-Learning-to-Generate-Fine-Grained-Robotic/01_overview.md) — 2025 AAAI.
194. [Open-Vocabulary Spatio-Temporal Scene Graph for Robot Perception and Teleoperation Planning](../2026/ICRA/2026_ICRA_Open-Vocabulary-Spatio-Temporal-Scene-Graph-for-Robot-Perc/01_overview.md) — 2026 ICRA.
195. [Lookahead Exploration with Neural Radiance Representation for Continuous Vision-Language Navigation](../2024/CVPR/2024_CVPR_Lookahead-Exploration-with-Neural-Radiance-Representation/01_overview.md) — 2024 CVPR.
196. [FOCI: Trajectory Optimization on Gaussian Splats](../2025/IROS/2025_IROS_FOCI-Trajectory-Optimization-on-Gaussian-Splats/01_overview.md) — 2025 IROS.
197. [Partially Observable Task and Motion Planning with Uncertainty and Risk Awareness](../2024/RSS/2024_RSS_Partially-Observable-Task-and-Motion-Planning-with-Uncerta/01_overview.md) — 2024 RSS.
198. [Parallel and Proximal Linear-Quadratic Methods for Real-Time Constrained Model-Predictive Control](../2024/RSS/2024_RSS_Parallel-and-Proximal-Linear-Quadratic-Methods-for-Real-Ti/01_overview.md) — 2024 RSS.
199. [Differentiable Robust Model Predictive Control](../2024/RSS/2024_RSS_Differentiable-Robust-Model-Predictive-Control/01_overview.md) — 2024 RSS.
200. [Linear-time Differential Inverse Kinematics: an Augmented Lagrangian Perspective](../2024/RSS/2024_RSS_Linear-time-Differential-Inverse-Kinematics-an-Augmented-L/01_overview.md) — 2024 RSS.

### Active and embodied 3D Vision — 22

201. [LoGoPlanner: Localization Grounded Navigation Policy with Metric-aware Visual Geometry](../2026/ICRA/2026_ICRA_LoGoPlanner-Localization-Grounded-Navigation-Policy-with-M/01_overview.md) — 2026 ICRA.
   - 선정 이유: Current trend / enabling 3D. Metric-aware geometry와 history 기반 state estimation을 trajectory planning에 연결한다. 일반 reconstruction보다 현재 navigation 목표에 직접적이다. Controller가 실제 사용하는 pose·calibration·simulator GT의 범위는 본문/배포 코드 확인이 필요하다.
202. [Vision-and-Language Navigation: Interpreting Visually-Grounded Navigation Instructions in Real Environments](../2018/CVPR/2018_CVPR_Vision-and-Language-Navigation-Interpreting-Visually-Groun/01_overview.md) — 2018 CVPR.
   - 선정 이유: R2R은 VLN instruction grounding과 graph-navigation 평가의 원형으로 VLN-CE·NaVILA의 설정 차이를 비교할 때 읽는다.
203. [PointNet: Deep Learning on Point Sets for 3D Classification and Segmentation](../2017/CVPR/2017_CVPR_PointNet-Deep-Learning-on-Point-Sets-for-3D-Classification/01_overview.md) — 2017 CVPR.
   - 선정 이유: PointNet은 DP3 등 point-cloud policy encoder를 구현·비교할 때 필요한 선택적 representation 기반이다.
204. [DROID-SLAM: Deep Visual SLAM for Monocular, Stereo, and RGB-D Cameras](../2021/NeurIPS/2021_NeurIPS_DROID-SLAM-Deep-Visual-SLAM-for-Monocular-Stereo-and-RGB-D/01_overview.md) — 2021 NeurIPS.
   - 선정 이유: DROID-SLAM은 navigation의 localization 품질이 policy 성능을 제한하는 실험에서 읽는다.
205. [Where2Act: From Pixels to Actions for Articulated 3D Objects](../2021/ICCV/2021_ICCV_Where2Act-From-Pixels-to-Actions-for-Articulated-3D-Object/01_overview.md) — 2021 ICCV.
206. [FlowBot3D: Learning 3D Articulation Flow to Manipulate Articulated Objects](../2022/RSS/2022_RSS_FlowBot3D-Learning-3D-Articulation-Flow-to-Manipulate-Arti/01_overview.md) — 2022 RSS.
207. [Ditto: Building Digital Twins of Articulated Objects from Interaction](../2022/CVPR/2022_CVPR_Ditto-Building-Digital-Twins-of-Articulated-Objects-from-I/01_overview.md) — 2022 CVPR.
208. [VLMaps: Visual-Language Maps for Robot Navigation](../2023/ICRA/2023_ICRA_VLMaps-Visual-Language-Maps-for-Robot-Navigation/01_overview.md) — 2023 ICRA.
209. [SUGAR: Pre-training 3D Visual Representations for Robotics](../2024/CVPR/2024_CVPR_SUGAR-Pre-training-3D-Visual-Representations-for-Robotics/01_overview.md) — 2024 CVPR.
210. [Splat-Nav: Safe Real-Time Robot Navigation in Gaussian Splatting Maps](../2025/IROS/2025_IROS_Splat-Nav-Safe-Real-Time-Robot-Navigation-in-Gaussian-Spla/01_overview.md) — 2025 IROS.
211. [RoboSpatial: Teaching Spatial Understanding to 2D and 3D Vision-Language Models for Robotics](../2025/CVPR/2025_CVPR_RoboSpatial-Teaching-Spatial-Understanding-to-2D-and-3D-Vi/01_overview.md) — 2025 CVPR.
212. [PointVLA: Injecting the 3D World into Vision-Language-Action Models](../2026/RA-L/2026_RA-L_PointVLA-Injecting-the-3D-World-into-Vision-Language-Actio/01_overview.md) — 2026 RA-L.
213. [Vysics: Object Reconstruction Under Occlusion by Fusing Vision and Contact-Rich Physics](../2025/RSS/2025_RSS_Vysics-Object-Reconstruction-Under-Occlusion-by-Fusing-Vis/01_overview.md) — 2025 RSS.
214. [Act the Part: Learning Interaction Strategies for Articulated Object Part Discovery](../2021/ICCV/2021_ICCV_Act-the-Part-Learning-Interaction-Strategies-for-Articulat/01_overview.md) — 2021 ICCV.
215. [Where2Explore: Few-shot Affordance Learning for Unseen Novel Categories of Articulated Objects](../2023/NeurIPS/2023_NeurIPS_Where2Explore-Few-shot-Affordance-Learning-for-Unseen-Nove/01_overview.md) — 2023 NeurIPS.
216. [Clio: Real-time Task-Driven Open-Set 3D Scene Graphs](../2024/RA-L/2024_RA-L_Clio-Real-time-Task-Driven-Open-Set-3D-Scene-Graphs/01_overview.md) — 2024 RA-L.
217. [HAMMER: Heterogeneous, Multi-Robot Semantic Gaussian Splatting](../2025/RA-L/2025_RA-L_HAMMER-Heterogeneous-Multi-Robot-Semantic-Gaussian-Splatti/01_overview.md) — 2025 RA-L.
218. [VISTA: Open-Vocabulary, Task-Relevant Robot Exploration with Online Semantic Gaussian Splatting](../2026/ICRA/2026_ICRA_VISTA-Open-Vocabulary-Task-Relevant-Robot-Exploration-with/01_overview.md) — 2026 ICRA.
219. [RoboRefer: Towards Spatial Referring with Reasoning in Vision-Language Models for Robotics](../2025/NeurIPS/2025_NeurIPS_RoboRefer-Towards-Spatial-Referring-with-Reasoning-in-Visi/01_overview.md) — 2025 NeurIPS.
220. [Volumetric Environment Representation for Vision-Language Navigation](../2024/CVPR/2024_CVPR_Volumetric-Environment-Representation-for-Vision-Language/01_overview.md) — 2024 CVPR.
221. [IGL-Nav: Incremental 3D Gaussian Localization for Image-goal Navigation](../2025/ICCV/2025_ICCV_IGL-Nav-Incremental-3D-Gaussian-Localization-for-Image-goa/01_overview.md) — 2025 ICCV.
222. [Move to Understand a 3D Scene: Bridging Visual Grounding and Exploration for Efficient and Versatile Embodied Navigation](../2025/ICCV/2025_ICCV_Move-to-Understand-a-3D-Scene-Bridging-Visual-Grounding-an/01_overview.md) — 2025 ICCV.

### Locomotion, whole-body control, mobile manipulation, and humanoids — 12

223. [RMA: Rapid Motor Adaptation for Legged Robots](../2021/RSS/2021_RSS_RMA-Rapid-Motor-Adaptation-for-Legged-Robots/01_overview.md) — 2021 RSS.
   - 선정 이유: RMA는 NaVILA 등 legged navigation의 저수준 adaptation을 깊게 다룰 때 읽는다.
224. [RoboPanoptes: The All-Seeing Robot with Whole-body Dexterity](../2025/RSS/2025_RSS_RoboPanoptes-The-All-Seeing-Robot-with-Whole-body-Dexterit/01_overview.md) — 2025 RSS.
225. [Demonstrating OK-Robot: What Really Matters in Integrating Open-Knowledge Models for Robotics](../2024/RSS/2024_RSS_Demonstrating-OK-Robot-What-Really-Matters-in-Integrating/01_overview.md) — 2024 RSS.
226. [Language-Grounded Dynamic Scene Graphs for Interactive Object Search with Mobile Manipulation](../2024/RA-L/2024_RA-L_Language-Grounded-Dynamic-Scene-Graphs-for-Interactive-Obj/01_overview.md) — 2024 RA-L.
227. [Dynamic Open-Vocabulary 3D Scene Graphs for Long-term Language-Guided Mobile Manipulation](../2025/RA-L/2025_RA-L_Dynamic-Open-Vocabulary-3D-Scene-Graphs-for-Long-term-Lang/01_overview.md) — 2025 RA-L.
228. [Demonstrating MOSART: Opening Articulated Structures in the Real World](../2025/RSS/2025_RSS_Demonstrating-MOSART-Opening-Articulated-Structures-in-the/01_overview.md) — 2025 RSS.
229. [HOMIE: Humanoid Loco-Manipulation with Isomorphic Exoskeleton Cockpit](../2025/RSS/2025_RSS_HOMIE-Humanoid-Loco-Manipulation-with-Isomorphic-Exoskelet/01_overview.md) — 2025 RSS.
230. [SPIN: Simultaneous Perception, Interaction and Navigation](../2024/CVPR/2024_CVPR_SPIN-Simultaneous-Perception-Interaction-and-Navigation/01_overview.md) — 2024 CVPR.
231. [GOAT: GO to Any Thing](../2024/RSS/2024_RSS_GOAT-GO-to-Any-Thing/01_overview.md) — 2024 RSS.
232. [Habitat 2.0: Training Home Assistants to Rearrange their Habitat](../2021/NeurIPS/2021_NeurIPS_Habitat-2.0-Training-Home-Assistants-to-Rearrange-their-Ha/01_overview.md) — 2021 NeurIPS.
   - 선정 이유: Habitat 2.0는 navigation에서 object rearrangement/mobile manipulation으로 확장할 때 필요한 task·simulator 기준이다.
233. [MoManipVLA: Transferring Vision-language-action Models for General Mobile Manipulation](../2025/CVPR/2025_CVPR_MoManipVLA-Transferring-Vision-language-action-Models-for/01_overview.md) — 2025 CVPR.
   - 선정 이유: NaVILA·MoTo와 함께 VLA와 기하학적 실행 가능성의 경계를 비교하는 NEXT다.
234. [WholeBodyVLA: Towards Unified Latent VLA for Whole-body Loco-manipulation Control](../2026/ICLR/2026_ICLR_WholeBodyVLA-Towards-Unified-Latent-VLA-for-Whole-body-Loc/01_overview.md) — 2026 ICLR.
   - 선정 이유: NaVILA 이후 VLA와 low-level RL의 역할을 비교할 NEXT다.

### World models, uncertainty, failure detection, and recovery — 41

235. [VLAW: Iterative Co-Improvement of Vision-Language-Action Policy and World Model](../2026/ICML/2026_ICML_VLAW-Iterative-Co-Improvement-of-Vision-Language-Action-Po/01_overview.md) — 2026 ICML.
   - 선정 이유: Current trend. 실제 rollout으로 world model의 failure coverage를 개선하고 synthetic rollout으로 policy를 개선하는 반복 구조다. 이미 등록된 Ctrl-World/WMPO와 연결해 model bias와 real-data budget을 비교한다. Abstract만으로 특정 RL optimizer를 단정하지 않는다.
236. [Towards Practical World Model-based Reinforcement Learning for Vision-Language-Action Models](../2026/ICML/2026_ICML_Towards-Practical-World-Model-based-Reinforcement-Learning/01_overview.md) — 2026 ICML.
   - 선정 이유: Current trend. Multi-view consistency와 chunk-level branched rollout으로 world-model RL의 오차 누적을 다룬다. WMPO/WorldGym을 읽을 때 직접 비교해야 할 누락 논문이다.
237. [Self-Improving Robot Policy with Compositional World Model](../2026/RSS/2026_RSS_Self-Improving-Robot-Policy-with-Compositional-World-Model/01_overview.md) — 2026 RSS.
   - 선정 이유: Current trend. Multi-view dynamics와 progress value를 분리하여 imagined rollout의 advantage를 만든다. VLA-MBPO/WMPO와 reward/value 신뢰도 및 real-robot transfer를 비교할 가치가 있다.
238. [PointWorld: Scaling 3D World Models for In-The-Wild Robotic Manipulation](../2026/CVPR/2026_CVPR_PointWorld-Scaling-3D-World-Models-for-In-The-Wild-Robotic/01_overview.md) — 2026 CVPR.
   - 선정 이유: Current trend / action-relevant 3D. State와 action을 3D point flow로 표현하고 예측을 manipulation MPC에 연결한다. DP3/3D-VLA 이후 explicit geometry와 world model을 비교할 직접적인 연결이다. 본문 평가의 보장 범위와 calibration 의존성은 추가 확인 대상이다.
239. [OopsieVerse: A Safety Benchmark with Damage-Aware Simulation for Robot Manipulation](../2026/RSS/2026_RSS_OopsieVerse-A-Safety-Benchmark-with-Damage-Aware-Simulatio/01_overview.md) — 2026 RSS.
   - 선정 이유: Benchmark. Task success와 물리적 damage를 분리하고 damage-aware IL/RL 및 VLA 평가를 지원한다. 기존 safety/recovery 흐름에 contact·thermal·fluid damage라는 구체적인 평가 축을 보충한다.
240. [World Models](../2018/NeurIPS-Workshop/2018_NeurIPS-Workshop_World-Models/01_overview.md) — 2018 NeurIPS Workshop.
   - 선정 이유: World Models 원전은 latent world-model 계보를 확인할 때 읽고 실제 robot/control 비교는 TD-MPC2와 후속 연구에 우선한다.
241. [DayDreamer: World Models for Physical Robot Learning](../2022/CoRL/2022_CoRL_DayDreamer-World-Models-for-Physical-Robot-Learning/01_overview.md) — 2022 CoRL.
   - 선정 이유: DayDreamer는 실제 robot model-based RL branch에서 학습 예산과 dynamics 사용을 비교한다.
242. [Control Barrier Function Based Quadratic Programs for Safety Critical Systems](../2017/TAC/2017_TAC_Control-Barrier-Function-Based-Quadratic-Programs-for-Safe/01_overview.md) — 2017 TAC.
   - 선정 이유: CBF는 safety filter의 가정과 보장을 연구하는 branch에서 읽으며 VLA/RL 전체의 선행 의무에서는 분리한다.
243. [DreamGen: Unlocking Generalization in Robot Learning through Video World Models](../2025/CoRL/2025_CoRL_DreamGen-Unlocking-Generalization-in-Robot-Learning-throug/01_overview.md) — 2025 CoRL.
244. [DreamDojo: A Generalist Robot World Model from Large-Scale Human Videos](../2026/ICML/2026_ICML_DreamDojo-A-Generalist-Robot-World-Model-from-Large-Scale/01_overview.md) — 2026 ICML.
245. [Learning Latent Dynamics for Planning from Pixels](../2019/ICML/2019_ICML_Learning-Latent-Dynamics-for-Planning-from-Pixels/01_overview.md) — 2019 ICML.
246. [Dream to Control: Learning Behaviors by Latent Imagination](../2020/ICLR/2020_ICLR_Dream-to-Control-Learning-Behaviors-by-Latent-Imagination/01_overview.md) — 2020 ICLR.
247. [Mastering Diverse Domains through World Models](../2025/Nature/2025_Nature_Mastering-Diverse-Domains-through-World-Models/01_overview.md) — 2025 Nature.
248. [PIN-WM: Learning Physics-INformed World Models for Non-Prehensile Manipulation](../2025/RSS/2025_RSS_PIN-WM-Learning-Physics-INformed-World-Models-for-Non-Preh/01_overview.md) — 2025 RSS.
249. [Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets](../2025/RSS/2025_RSS_Unified-World-Models-Coupling-Video-and-Action-Diffusion-f/01_overview.md) — 2025 RSS.
250. [FlowDreamer: A RGB-D World Model with Flow-based Motion Representations for Robot Manipulation](../2025/arXiv/2025_arXiv_FlowDreamer-A-RGB-D-World-Model-with-Flow-based-Motion-Rep/01_overview.md) — 2025 arXiv.
251. [Can We Detect Failures Without Failure Data? Uncertainty-Aware Runtime Failure Detection for Imitation Learning Policies](../2025/RSS/2025_RSS_Can-We-Detect-Failures-Without-Failure-Data-Uncertainty-Aw/01_overview.md) — 2025 RSS.
252. [SAFE: Multitask Failure Detection for Vision-Language-Action Models](../2025/NeurIPS/2025_NeurIPS_SAFE-Multitask-Failure-Detection-for-Vision-Language-Actio/01_overview.md) — 2025 NeurIPS.
253. [WorldGym: World Model as An Environment for Policy Evaluation](../2026/ICLR/2026_ICLR_WorldGym-World-Model-as-An-Environment-for-Policy-Evaluati/01_overview.md) — 2026 ICLR.
254. [WMPO: World Model-based Policy Optimization for Vision-Language-Action Models](../2026/ICLR/2026_ICLR_WMPO-World-Model-based-Policy-Optimization-for-Vision-Lang/01_overview.md) — 2026 ICLR.
255. [FLARE: A Failure-Aware Framework for Autonomous Correction and Recovery in Visual-Language Robotic Manipulation](../2026/CVPR/2026_CVPR_FLARE-A-Failure-Aware-Framework-for-Autonomous-Correction/01_overview.md) — 2026 CVPR.
256. [Can VLMs Diagnose and Recover from VLA Manipulation Faults?](../2026/ICML/2026_ICML_Can-VLMs-Diagnose-and-Recover-from-VLA-Manipulation-Faults/01_overview.md) — 2026 ICML.
257. [Temporal Difference Calibration in Sequential Tasks: Application to Vision-Language-Action Models](../2026/ICML/2026_ICML_Temporal-Difference-Calibration-in-Sequential-Tasks-Applic/01_overview.md) — 2026 ICML.
258. [Memory Retrieval in Visuomotor Policies for Long-Horizon Robot Control](../2026/RSS/2026_RSS_Memory-Retrieval-in-Visuomotor-Policies-for-Long-Horizon-R/01_overview.md) — 2026 RSS.
259. [Demonstrating ViSafe: Vision-enabled Safety for High-speed Detect and Avoid](../2025/RSS/2025_RSS_Demonstrating-ViSafe-Vision-enabled-Safety-for-High-speed/01_overview.md) — 2025 RSS.
260. [Learned Perceptive Forward Dynamics Model for Safe and Platform-aware Robotic Navigation](../2025/RSS/2025_RSS_Learned-Perceptive-Forward-Dynamics-Model-for-Safe-and-Pla/01_overview.md) — 2025 RSS.
261. [Certifiably-Correct Mapping for Safe Navigation Despite Odometry Drift](../2025/RSS/2025_RSS_Certifiably-Correct-Mapping-for-Safe-Navigation-Despite-Od/01_overview.md) — 2025 RSS.
262. [Particle-Grid Neural Dynamics for Learning Deformable Object Models from RGB-D Videos](../2025/RSS/2025_RSS_Particle-Grid-Neural-Dynamics-for-Learning-Deformable-Obje/01_overview.md) — 2025 RSS.
263. [Map Space Belief Prediction for Manipulation-Enhanced Mapping](../2025/RSS/2025_RSS_Map-Space-Belief-Prediction-for-Manipulation-Enhanced-Mapp/01_overview.md) — 2025 RSS.
264. [Unified Video Action Model](../2025/RSS/2025_RSS_Unified-Video-Action-Model/01_overview.md) — 2025 RSS.
265. [From Foresight to Forethought: VLM-In-the-Loop Policy Steering via Latent Alignment](../2025/RSS/2025_RSS_From-Foresight-to-Forethought-VLM-In-the-Loop-Policy-Steer/01_overview.md) — 2025 RSS.
266. [Prompting with the Future: Open-World Model Predictive Control with Interactive Digital Twins](../2025/RSS/2025_RSS_Prompting-with-the-Future-Open-World-Model-Predictive-Cont/01_overview.md) — 2025 RSS.
267. [Self-Correcting Robot Manipulation via Gaussian-Splatted Foresight](../2025/AAAI/2025_AAAI_Self-Correcting-Robot-Manipulation-via-Gaussian-Splatted-F/01_overview.md) — 2025 AAAI.
268. [WMNav: Integrating Vision-Language Models into World Models for Object Goal Navigation](../2025/IROS/2025_IROS_WMNav-Integrating-Vision-Language-Models-into-World-Models/01_overview.md) — 2025 IROS.
269. [RoboDreamer: Learning Compositional World Models for Robot Imagination](../2024/ICML/2024_ICML_RoboDreamer-Learning-Compositional-World-Models-for-Robot/01_overview.md) — 2024 ICML.
270. [Learning Interactive Real-World Simulators](../2024/ICLR/2024_ICLR_Learning-Interactive-Real-World-Simulators/01_overview.md) — 2024 ICLR.
271. [SafeMimic: Towards Safe and Autonomous Human-to-Robot Imitation for Mobile Manipulation](../2025/RSS/2025_RSS_SafeMimic-Towards-Safe-and-Autonomous-Human-to-Robot-Imita/01_overview.md) — 2025 RSS.
272. [Ctrl-World: A Controllable Generative World Model for Robot Manipulation](../2026/ICLR/2026_ICLR_Ctrl-World-A-Controllable-Generative-World-Model-for-Robot/01_overview.md) — 2026 ICLR.
273. [LIBERO-RIG: A Hardware-Setup Robustness Benchmark for Vision-Language-Action Models](../2026/arXiv/2026_arXiv_LIBERO-RIG-A-Hardware-Setup-Robustness-Benchmark-for-Visio/01_overview.md) — 2026 arXiv.
   - 선정 이유: D1의 fault taxonomy와 policy/controller 경계 진단에 필요한 NEXT benchmark다.
274. [Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons](../2026/RSS/2026_RSS_Robometer-Scaling-General-Purpose-Robotic-Reward-Models-vi/01_overview.md) — 2026 RSS.
   - 선정 이유: C4/C6의 reward·progress·평가 신호를 비교할 핵심 최신 baseline이다. NEXT: 현재 VLA 정독 흐름의 직접 비교·평가 기준으로 편입한다.
275. [RoboReward: General-Purpose Vision-Language Reward Models for Robotics](../2026/arXiv/2026_arXiv_RoboReward-General-Purpose-Vision-Language-Reward-Models-f/01_overview.md) — 2026 arXiv.
   - 선정 이유: C4의 독립 outcome과 reward model 차이를 정할 직접 기준이다. NEXT: 현재 VLA 정독 흐름의 직접 비교·평가 기준으로 편입한다.

## REFERENCE — On-Demand Reading

기존 foundation의 가치를 낮춘 분류가 아니다. 일반 search/control, tactile hardware, whole-body locomotion, generic reconstruction은 선택한 실험의 요구에 따라 다시 읽는다. 현재 tier에서 빠진 기존 읽기 상태와 개인 분석은 history CSV에 보존하며 재승격 시 복원한다.

## ARCHIVE — Search Only

현재 연구 범위 밖의 논문도 registry와 표준 노트에서 검색할 수 있다. 이번 재분류는 논문 수·PDF 보유 여부·venue quota를 기준으로 하지 않는다.
