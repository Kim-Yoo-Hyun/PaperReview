# 이동과 전신 제어

- Updated: 2026-10-23 KST

## Scope

ZMP/model-based walking, learned motion priors, perpetual motion tracking, versatile neural whole-body control, rapid adaptation, perceptive locomotion, humanoid imitation, mobile manipulation과 loco-manipulation을 통합해서 비교한다.

### Taxonomy boundary and curation schema

- **Primary axis:** locomotion/body state → contact and balance control → motion prior or policy learning → whole-body/mobile deployment.
- **Taxonomy note:** humanoid는 별도 category가 아니라 locomotion, whole-body control, imitation 또는 mobile/loco-manipulation의 embodiment facet으로 기록한다.
- **In scope:** legged or humanoid locomotion, whole-body control, mobile manipulation, motion imitation, adaptation, balance/contact와 hardware deployment이 robot behavior를 직접 평가하는 경우.
- **Out of scope:** character animation without physical robot implications, arm-only manipulation, 또는 locomotion과 whole-body interface가 없는 generic motion generation.
- **Inclusion test:** embodiment, body/contact state, action/control level, adaptation or training setting, stability/task evaluation 중 최소 네 가지를 비교할 수 있어야 한다.
- **Role vocabulary:** `foundation`, `controller`, `motion prior`, `policy`, `adaptation`, `dataset`, `benchmark`, `simulator`, `system`을 사용한다.

공통 matrix/evidence 규약은 [synthesis 안내](./README.md#공통-비교-규약과-질문-분류)를 따른다.

## Reading Path

현재 읽기 우선순위는 [READING_PLAN.md](../research/READING_PLAN.md)를 따른다. 아래 계보는 비교 탐색용이며 전체 선행 완독 의무가 아니다.

2026-10-19 초점: ViNT와 Mobile ALOHA를 중심으로 navigation에서 mobile manipulation으로 이어지는 data·policy interface를 다룬다. NaVILA와 연결되는 low-level adaptation은 선택적으로 읽고 순수 gait·human motion tracking은 필요시 참조한다.

ZMP preview control → Dynamic WBC/HQP/NMPC → DeepMimic/AMP → PHC/MaskedMimic → HOVER/SONIC → RMA/perceptive locomotion/parkour → human-to-humanoid imitation → mobile and humanoid loco-manipulation.

### 2026-10-19 추가 논문 비교

아래는 등록된 abstract/project 근거에서 만든 **정독 전 비교 질문**이다. 직접 citation이나 실험 결론으로 취급하지 않으며, 읽기 순서와 tier는 READING_PLAN의 최신 값을 따른다.

| 비교할 논문 | 비교 축 | 본문에서 확인할 조건 |
|---|---|---|
| ViNT·Mobile ALOHA ↔ NaVILA·NavDP·StreamVLN | Navigation에서 mobile manipulation으로 이어지는 interface | 신규 navigation 논문은 각 primary track에 한 번만 배정한다. 이 트랙에서는 base/arm command, low-level controller, 지연과 embodiment transfer 조건을 교차 비교한다. |

<!-- READING_QUEUE:START -->

## Assigned Reading Queue

### Locomotion, mobile manipulation, and humanoid systems — 2

| Tier | Paper | Year / Venue | Status | Evidence |
|---|---|---|---|---|
| CORE | [ViNT: A Foundation Model for Visual Navigation](../2023/CoRL/2023_CoRL_ViNT-A-Foundation-Model-for-Visual-Navigation/01_overview.md) | 2023 / CoRL | `UNREAD` | `FULL_TEXT_CHECKED` |
| CORE | [Mobile ALOHA: Learning Bimanual Mobile Manipulation using Low-Cost Whole-Body Teleoperation](../2024/CoRL/2024_CoRL_Mobile-ALOHA-Learning-Bimanual-Mobile-Manipulation-using-L/01_overview.md) | 2024 / CoRL | `UNREAD` | `FULL_TEXT_CHECKED` |

### Locomotion, whole-body control, mobile manipulation, and humanoids — 20

| Tier | Paper | Year / Venue | Status | Evidence |
|---|---|---|---|---|
| NEXT | [RMA: Rapid Motor Adaptation for Legged Robots](../2021/RSS/2021_RSS_RMA-Rapid-Motor-Adaptation-for-Legged-Robots/01_overview.md) | 2021 / RSS | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [RoboPanoptes: The All-Seeing Robot with Whole-body Dexterity](../2025/RSS/2025_RSS_RoboPanoptes-The-All-Seeing-Robot-with-Whole-body-Dexterit/01_overview.md) | 2025 / RSS | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [Demonstrating OK-Robot: What Really Matters in Integrating Open-Knowledge Models for Robotics](../2024/RSS/2024_RSS_Demonstrating-OK-Robot-What-Really-Matters-in-Integrating/01_overview.md) | 2024 / RSS | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [Language-Grounded Dynamic Scene Graphs for Interactive Object Search with Mobile Manipulation](../2024/RA-L/2024_RA-L_Language-Grounded-Dynamic-Scene-Graphs-for-Interactive-Obj/01_overview.md) | 2024 / RA-L | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [Dynamic Open-Vocabulary 3D Scene Graphs for Long-term Language-Guided Mobile Manipulation](../2025/RA-L/2025_RA-L_Dynamic-Open-Vocabulary-3D-Scene-Graphs-for-Long-term-Lang/01_overview.md) | 2025 / RA-L | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [Demonstrating MOSART: Opening Articulated Structures in the Real World](../2025/RSS/2025_RSS_Demonstrating-MOSART-Opening-Articulated-Structures-in-the/01_overview.md) | 2025 / RSS | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [HOMIE: Humanoid Loco-Manipulation with Isomorphic Exoskeleton Cockpit](../2025/RSS/2025_RSS_HOMIE-Humanoid-Loco-Manipulation-with-Isomorphic-Exoskelet/01_overview.md) | 2025 / RSS | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [SPIN: Simultaneous Perception, Interaction and Navigation](../2024/CVPR/2024_CVPR_SPIN-Simultaneous-Perception-Interaction-and-Navigation/01_overview.md) | 2024 / CVPR | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [GOAT: GO to Any Thing](../2024/RSS/2024_RSS_GOAT-GO-to-Any-Thing/01_overview.md) | 2024 / RSS | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [Habitat 2.0: Training Home Assistants to Rearrange their Habitat](../2021/NeurIPS/2021_NeurIPS_Habitat-2.0-Training-Home-Assistants-to-Rearrange-their-Ha/01_overview.md) | 2021 / NeurIPS | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [MoManipVLA: Transferring Vision-language-action Models for General Mobile Manipulation](../2025/CVPR/2025_CVPR_MoManipVLA-Transferring-Vision-language-action-Models-for/01_overview.md) | 2025 / CVPR | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [WholeBodyVLA: Towards Unified Latent VLA for Whole-body Loco-manipulation Control](../2026/ICLR/2026_ICLR_WholeBodyVLA-Towards-Unified-Latent-VLA-for-Whole-body-Loc/01_overview.md) | 2026 / ICLR | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [TidyBot++: An Open-Source Holonomic Mobile Manipulator for Robot Learning](../2024/CoRL/2024_CoRL_TidyBot%2B%2B-An-Open-Source-Holonomic-Mobile-Manipulator-for/01_overview.md) | 2024 / CoRL | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [Mobi-π: Mobilizing Your Robot Learning Policy](../2025/CoRL/2025_CoRL_Mobi-pi-Mobilizing-Your-Robot-Learning-Policy/01_overview.md) | 2025 / CoRL | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [SAGA: Open-World Mobile Manipulation via Structured Affordance Grounding](../2026/RA-L/2026_RA-L_SAGA-Open-World-Mobile-Manipulation-via-Structured-Afforda/01_overview.md) | 2026 / RA-L | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [MoMa-Kitchen: A 100K+ Benchmark for Affordance-Grounded Last-Mile Navigation in Mobile Manipulation](../2025/ICCV/2025_ICCV_MoMa-Kitchen-A-100K%2B-Benchmark-for-Affordance-Grounded-Las/01_overview.md) | 2025 / ICCV | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [Advancing Humanoid Locomotion: Mastering Challenging Terrains with Denoising World Model Learning](../2024/RSS/2024_RSS_Advancing-Humanoid-Locomotion-Mastering-Challenging-Terrai/01_overview.md) | 2024 / RSS | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [CLONE: Closed-Loop Whole-Body Humanoid Teleoperation for Long-Horizon Tasks](../2025/CoRL/2025_CoRL_CLONE-Closed-Loop-Whole-Body-Humanoid-Teleoperation-for-Lo/01_overview.md) | 2025 / CoRL | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [HumanoidMimicGen: Data Generation for Loco-Manipulation via Whole-Body Planning](../2026/CoRL/2026_CoRL_HumanoidMimicGen-Data-Generation-for-Loco-Manipulation-via/01_overview.md) | 2026 / CoRL | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [HuG: Learning Humanoid Whole-Body Affordance-Aware Grasping with Active Perception](../2026/CoRL/2026_CoRL_HuG-Learning-Humanoid-Whole-Body-Affordance-Aware-Grasping/01_overview.md) | 2026 / CoRL | `UNREAD` | `FULL_TEXT_CHECKED` |

<!-- READING_QUEUE:END -->

## Historical curation — 2026-09-02

아래는 해당 날짜의 변경 이력이다. 현재 membership과 수량은 위 generated queue를 따른다.

`AMO`, `MOSART`, `HOMIE`, `Flying Hand`, `SPIN`, `WoCoCo`를 `NEXT`에 반영했다. 이 논문들은 humanoid를 별도 taxonomy로 만들지 않고 whole-body control, contact switching, mobile/loco-manipulation, aerial manipulation의 실제 execution interface로 비교한다.

## Comparison Matrix

> Matrix maturity: `CURATION-SEED`. 아래는 읽기 전 비교 가설이며 `READ`를 의미하지 않는다. `Paper` 링크는 local overview를 가리키고, official paper/project/code URL은 해당 note header에서 확인한다.
>
> Row convention: 한 행은 한 registry paper이다. `State / action / objective / timing`은 고정 순서로 기록하고, `Evaluation`은 `setup; data/split; metric; real/trials` 순서를 따른다. `Evidence / source`가 `CURATION-SEED`이면 수치나 세부 조건을 아직 주장하지 않는다.

| Paper | Year / Venue | Role | Facets | Problem | State / action / objective / timing | Why included / TL;DR | Evaluation (setup; data/split; metric; real/trials) | Evidence / source | Failure / assumption | Reusable idea |
|---|---|---|---|---|---|---|---|---|---|---|
| [ZMP Preview Control](../1960-2010/2003/ICRA/2003_ICRA_Biped-Walking-Pattern-Generation-by-using-Preview-Control/01_overview.md) | 2003 / ICRA | foundation; controller | biped; proprioception+ZMP; model-based; locomotion control | preview-based biped walking pattern generation | CoM/cart-table and future ZMP; walking trajectory; ZMP stability objective; preview horizon | learned policy와 비교할 explicit stability/reference baseline | walking simulation/robot; data/split=UNVERIFIED; metric=tracking/stability; real=UNVERIFIED/trials=UNVERIFIED | `CURATION-SEED`; overview + queue | simplified dynamics, flat terrain, fixed contact schedule | learned command에 classical stability signal을 남김 |
| [AMP](../2021/ACM-Transactions-on-Grap/2021_ACM-Transactions-on-Grap_AMP-Adversarial-Motion-Priors-for-Stylized-Physics-Based-C/01_overview.md) | 2021 / ACM Transactions on Graphics | motion prior; method | simulated character; proprioception+motion; simulation; joint policy | learn stylized physics-based motion from examples | proprioception and motion reference; joint-level policy; RL plus adversarial prior; simulation loop | motion prior와 task reward를 분리하는 기준 | simulated motion tasks; data/split=mocap/reference set; metric=motion quality/task return; real=no/trials=— | `CURATION-SEED`; overview + queue | motion coverage, fall/recovery, sim-to-real | prior가 behavior diversity에 주는 효과를 분리 |
| [PHC](../2023/ICCV/2023_ICCV_Perpetual-Humanoid-Control-for-Real-time-Simulated-Avatars/01_overview.md) | 2023 / ICCV | controller; motion prior | humanoid avatar; motion reference; simulation; full-body tracking | perpetual large-corpus humanoid motion tracking | reference and body state; joint-level action; tracking/fallback objective; real-time simulation | fallback/recovery structure를 포함한 whole-body tracking reference | simulated humanoid; data/split=motion corpus; metric=tracking/coverage/robustness; real=no/trials=— | `CURATION-SEED`; overview + queue | motion-data coverage, fall/recovery, physical transfer | tracking과 recovery controller를 분리 |
| [MaskedMimic](../2024/ACM-Transactions-on-Grap/2024_ACM-Transactions-on-Grap_MaskedMimic-Unified-Physics-Based-Character-Control-Throug/01_overview.md) | 2024 / ACM Transactions on Graphics | motion prior; controller | humanoid; masked motion commands+proprioception; simulation; whole-body | unified partial-motion-conditioned physics control | masked reference and body state; joint-level action; physics/tracking objective; simulation loop | partial command를 reusable whole-body interface로 만드는 기준 | simulated humanoid; data/split=motion/task conditions; metric=tracking/diversity/robustness; real=no/trials=— | `CURATION-SEED`; overview + queue | actuation/contact limits, command coverage, fall | command-conditioned controller를 상위 policy 아래 둠 |
| [HOVER](../2025/ICRA/2025_ICRA_HOVER-Versatile-Neural-Whole-Body-Controller-for-Humanoid/01_overview.md) | 2025 / ICRA | controller; system | humanoid; motion command+proprioception; sim/real; whole-body | versatile neural whole-body command tracking | command and humanoid state; joint-level action; tracking/contact objective; online control | real-humanoid reusable low-level controller reference | humanoid motion tasks; data/split=UNVERIFIED; metric=tracking/robustness; real=UNVERIFIED/trials=UNVERIFIED | `CURATION-SEED`; overview + queue | actuation limits, unseen hardware, object contact, fall severity | VLA command와 low-level feasibility contract 분리 |
| [SONIC](../2026/Science-Robotics/2026_Science-Robotics_SONIC-Supersizing-Motion-Tracking-for-Natural-Humanoid-Who/01_overview.md) | 2026 / Science Robotics | controller; system | humanoid; motion reference+proprioception; sim/real; whole-body | scaled natural humanoid motion tracking | motion/body state; whole-body action; tracking/naturalness objective; online controller | scale and naturalness frontier for whole-body deployment | humanoid motion tasks; data/split=UNVERIFIED; metric=tracking/naturalness/robustness; real=UNVERIFIED/trials=UNVERIFIED | `CURATION-SEED`; overview + queue | hardware limits, contact/task success, fall severity | tracking score와 physical task success 분리 |
| [RMA](../2021/RSS/2021_RSS_RMA-Rapid-Motor-Adaptation-for-Legged-Robots/01_overview.md) | 2021 / RSS | adaptation; policy | quadruped; proprioception+history; sim-to-real; locomotion policy | rapid adaptation to unknown dynamics | proprioception and history latent; joint-level action; locomotion reward; online latent update | adaptation state를 policy와 분리하는 canonical baseline | quadruped terrain; data/split=sim randomization/real transfer; metric=velocity/stability/traversal; real=yes/trials=UNVERIFIED | `CURATION-SEED`; overview + queue | latent lag/averaging, randomization coverage, hardware shift | explicit adaptation state를 log |
| [Robust Perceptive Locomotion](../2022/Science-Robotics/2022_Science-Robotics_Learning-Robust-Perceptive-Locomotion-for-Quadrupedal-Robo/01_overview.md) | 2022 / Science Robotics | policy; perception-control system | quadruped; proprioception+terrain sensing; sim-to-real; locomotion | robust locomotion over natural terrain under perception uncertainty | body state and exteroceptive terrain; locomotion action; robustness/tracking objective; closed loop | perception uncertainty를 locomotion policy에 주입하는 reference | natural terrain; data/split=sim/real terrain split; metric=traversal/stability; real=yes/trials=UNVERIFIED | `CURATION-SEED`; overview + queue | corrupted/stale perception, rare terrain, terrain shift | perception signal과 controller robustness를 분리 |
| [ANYmal Parkour](../2024/Science-Robotics/2024_Science-Robotics_ANYmal-Parkour-Learning-Agile-Navigation-for-Quadrupedal-R/01_overview.md) | 2024 / Science Robotics | policy; system | quadruped; onboard perception+state; sim-to-real; agile locomotion | agile obstacle traversal with learned skills | perception and robot state; skill/action policy; task reward/curriculum; online execution | perception-conditioned skill library의 real deployment reference | parkour/obstacle tasks; data/split=terrain curriculum; metric=completion/robustness; real=yes/trials=UNVERIFIED | `CURATION-SEED`; overview + queue | curriculum coverage, recovery outside training, contact shift | skill coverage와 recovery를 별도 평가 |
| [Mobile ALOHA](../2024/CoRL/2024_CoRL_Mobile-ALOHA-Learning-Bimanual-Mobile-Manipulation-using-L/01_overview.md) | 2024 / CoRL | system; dataset/policy | mobile manipulator; multi-camera+proprioception; real; whole-body IL | bimanual mobile manipulation from whole-body demonstrations | visual/body state; base+arm action; imitation objective; closed-loop execution | data collection interface가 base-arm coupling을 결정하는 reference | household/mobile tasks; data/split=task demonstrations; metric=task success; real=yes/trials=UNVERIFIED | `CURATION-SEED`; overview + queue | demonstration coverage, base-arm coordination, contact shift | whole-body data와 policy interface를 함께 설계 |
| [OmniH2O](../2024/CoRL/2024_CoRL_OmniH2O-Universal-and-Dexterous-Human-to-Humanoid-Whole-Bo/01_overview.md) | 2024 / CoRL | system; imitation policy | humanoid; human motion+robot state; sim/real; whole-body | universal human-to-humanoid whole-body transfer | reference and robot state; whole-body tracking action; imitation/control objective; online tracking | retargeting과 policy learning의 coupling을 비교 | humanoid motion/task; data/split=human reference/real transfer; metric=tracking/task success; real=yes/trials=UNVERIFIED | `CURATION-SEED`; overview + queue | human-reference feasibility, object contact mismatch | retargeting error와 policy error 분리 |
| [LangWBC](../2025/RSS/2025_RSS_LangWBC-Language-Directed-Humanoid-Whole-Body-Control-via/01_overview.md) | 2025 / RSS | policy; controller interface | humanoid; language+proprioception; real/sim; hierarchical WBC | language-directed humanoid whole-body control | language/task and body state; hierarchical skill/low-level action; task/control objective; multi-rate hierarchy | semantic command와 whole-body controller의 interface reference | humanoid tasks; data/split=UNVERIFIED; metric=completion/stability; real/sim=UNVERIFIED/trials=UNVERIFIED | `CURATION-SEED`; overview + queue | command ambiguity, bandwidth conflict, contact feasibility | semantic command에 body/contact constraints 연결 |
| [HWC-Loco](../2026/ICLR/2026_ICLR_HWC-Loco-A-Hierarchical-Whole-Body-Control-Approach-to-Rob/01_overview.md) | 2026 / ICLR | controller; hierarchy | humanoid; language/task+proprioception; sim/real; loco-manipulation | hierarchical whole-body control for loco-manipulation | task and body state; high-level skill plus low-level control; stability/task objective; multi-rate hierarchy | locomotion과 manipulation objective를 hierarchy로 분리 | loco-manipulation; data/split=UNVERIFIED; metric=completion/stability/disturbance; real/sim=UNVERIFIED/trials=UNVERIFIED | `CURATION-SEED`; overview + queue | objective/bandwidth conflict, contact switching, hardware shift | high-level policy와 balance/contact layer 분리 |


## Dependency and Evolution

Humanoid를 별도 taxonomy로 분리하지 않고, control·adaptation·imitation·mobile manipulation 계보 안에서 읽는다. 직접 citation 관계는 정독 시 확인한다.

### Relation type index

아래 label은 바로 다음 계보 표의 chain anchor에 적용한다. `formulation`, `method`, `data`, `evaluation`, `deployment`는 개념적 연결의 종류이며 citation 또는 직접 영향 관계를 뜻하지 않는다.

| Chain anchor | Relation type | Interpretation |
|---|---|---|
| ZMP Preview → Dynamic WBC/HQP → Whole-Body NMPC | formulation → controller → deployment | simplified balance가 multi-contact predictive control로 확장 |
| Dynamic WBC/HQP/NMPC → learned whole-body policy → HWC-Loco | controller → policy hierarchy | explicit feasibility가 learned high-level hierarchy로 연결 |
| Domain Randomization → RMA/Perceptive Locomotion → ANYmal/ASAP/VIRAL | simulation/data → adaptation → deployment | randomization이 perception·adaptation·real alignment로 확장 |
| DeepMimic → AMP → PHC/MaskedMimic → HOVER/SONIC | motion prior → controller → deployment | reference tracking이 versatile real-humanoid control로 확장 |
| AMP/PHC/MaskedMimic → HumanPlus/OmniH2O → LangWBC | motion prior → embodiment/interface | motion controller가 human-to-humanoid와 language command로 확장 |
| Mobile ALOHA → RoboPanoptes → humanoid loco-manipulation | data/system → whole-body deployment | teleoperation data가 distributed whole-body interaction으로 확장 |
| locomotion/manipulation benchmark → HumanoidBench → real systems | benchmark → evaluation → deployment | single skill 평가가 whole-body hardware evaluation으로 확장 |

| Foundation → transition → frontier | 계승·변화 | 아직 확인할 경계 |
|---|---|---|
| [ZMP Preview Control](../1960-2010/2003/ICRA/2003_ICRA_Biped-Walking-Pattern-Generation-by-using-Preview-Control/01_overview.md) → [Dynamic Whole-Body Motion Generation](../2011-2020/2013/T-RO/2013_T-RO_Dynamic-Whole-Body-Motion-Generation-under-Rigid-Contacts/01_overview.md) / [HQP](../2011-2020/2014/IJRR/2014_IJRR_Hierarchical-Quadratic-Programming-Fast-Online-Humanoid-Ro/01_overview.md) → [Whole-Body NMPC](../2011-2020/2018/RA-L/2018_RA-L_Whole-Body-Nonlinear-Model-Predictive-Control-Through-Cont/01_overview.md) | simplified balance reference tracking에서 explicit multi-contact dynamics, task hierarchy와 predictive constraint handling으로 확장된다. | learned motion command와 contact schedule가 바뀔 때 classical stability quantity를 어떤 runtime signal로 유지할 것인가 |
| [Dynamic Whole-Body Motion Generation](../2011-2020/2013/T-RO/2013_T-RO_Dynamic-Whole-Body-Motion-Generation-under-Rigid-Contacts/01_overview.md) / [HQP](../2011-2020/2014/IJRR/2014_IJRR_Hierarchical-Quadratic-Programming-Fast-Online-Humanoid-Ro/01_overview.md) / [Whole-Body NMPC](../2011-2020/2018/RA-L/2018_RA-L_Whole-Body-Nonlinear-Model-Predictive-Control-Through-Cont/01_overview.md) → learned whole-body policies → [HWC-Loco](../2026/ICLR/2026_ICLR_HWC-Loco-A-Hierarchical-Whole-Body-Control-Approach-to-Rob/01_overview.md) | explicit dynamics/contact hierarchy에서 대규모 policy learning으로 이동한 뒤, task policy와 safety-recovery policy를 계층화하는 방향이 나타난다. | learned high-level switch가 model-based feasibility와 stability guarantee를 얼마나 보존하는가 |
| [Domain Randomization](../2011-2020/2017/IROS/2017_IROS_Domain-Randomization-for-Transferring-Deep-Neural-Networks/01_overview.md) / quadruped sim-to-real → [RMA](../2021/RSS/2021_RSS_RMA-Rapid-Motor-Adaptation-for-Legged-Robots/01_overview.md) / [Perceptive Locomotion](../2022/Science-Robotics/2022_Science-Robotics_Learning-Robust-Perceptive-Locomotion-for-Quadrupedal-Robo/01_overview.md) → [ANYmal Parkour](../2024/Science-Robotics/2024_Science-Robotics_ANYmal-Parkour-Learning-Agile-Navigation-for-Quadrupedal-R/01_overview.md) / [ASAP](../2025/RSS/2025_RSS_ASAP-Aligning-Simulation-and-Real-World-Physics-for-Learni/01_overview.md) / [VIRAL](../2026/CVPR/2026_CVPR_VIRAL-Visual-Sim-to-Real-at-Scale-for-Humanoid-Loco-Manipu/01_overview.md) | robustness randomization에서 latent adaptation, terrain perception, agile skill과 real-physics/visual alignment로 확장된다. | adaptation, perception과 privileged teacher가 각각 실제 deployment robustness에 기여하는 비율은 무엇인가 |
| [DeepMimic](../2011-2020/2018/TOG-SIGGRAPH/2018_TOG-SIGGRAPH_DeepMimic-Example-Guided-Deep-Reinforcement-Learning-of-Ph/01_overview.md) → [AMP](../2021/ACM-Transactions-on-Grap/2021_ACM-Transactions-on-Grap_AMP-Adversarial-Motion-Priors-for-Stylized-Physics-Based-C/01_overview.md) → [PHC](../2023/ICCV/2023_ICCV_Perpetual-Humanoid-Control-for-Real-time-Simulated-Avatars/01_overview.md) / [MaskedMimic](../2024/ACM-Transactions-on-Grap/2024_ACM-Transactions-on-Grap_MaskedMimic-Unified-Physics-Based-Character-Control-Throug/01_overview.md) → [HOVER](../2025/ICRA/2025_ICRA_HOVER-Versatile-Neural-Whole-Body-Controller-for-Humanoid/01_overview.md) / [SONIC](../2026/Science-Robotics/2026_Science-Robotics_SONIC-Supersizing-Motion-Tracking-for-Natural-Humanoid-Who/01_overview.md) | reference tracking에서 adversarial style prior, perpetual/fallback tracking, masked multi-command unification과 scaled real-humanoid controller로 확장된다. | 자연스러운 tracking score, physical feasibility, fall/recovery와 object-level task success를 어떻게 공동 평가할 것인가 |
| AMP/PHC/MaskedMimic motion-controller backbone → [HumanPlus](../2024/CoRL/2024_CoRL_HumanPlus-Humanoid-Shadowing-and-Imitation-from-Humans/01_overview.md) / [OmniH2O](../2024/CoRL/2024_CoRL_OmniH2O-Universal-and-Dexterous-Human-to-Humanoid-Whole-Bo/01_overview.md) → [LangWBC](../2025/RSS/2025_RSS_LangWBC-Language-Directed-Humanoid-Whole-Body-Control-via/01_overview.md) | motion prior/controller가 human shadowing·teleoperation, retargeting과 language-conditioned compositional whole-body behavior의 저수준 substrate가 된다. | semantic command가 balance margin, contact feasibility와 recovery budget을 전달하는가 |
| [Mobile ALOHA](../2024/CoRL/2024_CoRL_Mobile-ALOHA-Learning-Bimanual-Mobile-Manipulation-using-L/01_overview.md) → [RoboPanoptes](../2025/RSS/2025_RSS_RoboPanoptes-The-All-Seeing-Robot-with-Whole-body-Dexterit/01_overview.md) → humanoid loco-manipulation | whole-body teleoperation과 mobile bimanual data에서 distributed whole-body perception 및 body-contact manipulation으로 확장된다. | base motion, arm action, distributed vision의 서로 다른 bandwidth를 하나의 policy가 안정적으로 다루는가 |
| locomotion/manipulation benchmark → [HumanoidBench](../2024/RSS/2024_RSS_HumanoidBench-Simulated-Humanoid-Benchmark-for-Whole-Body/01_overview.md) → real-world whole-body systems | 개별 motor skill을 넘어 locomotion과 manipulation을 한 embodiment에서 비교할 공통 평가로 이동한다. | simulator 순위가 hardware durability, fall severity, recovery와 일치하는가 |

## 2026-10-23 근거 통합

아래는 2026-10-22까지의 registry/source 감사와 후보 검토를 연결한 연구자 해석이다. 새 정독·효과 검증·직접 citation 관계의 확인을 뜻하지 않는다. Paper별 본문 확인 범위는 overview 및 연결된 dossier를 따른다.

| 비교 축 | 등록된 선행 | 현재 남길 구분 |
|---|---|---|
| Attachment와 이동 중 제어 | [Geometric Fabrics](../2025/RA-L/2025_RA-L_Globally-Guided-Geometric-Fabrics-for-Reactive-Mobile-Mani/01_overview.md) (2025 RA-L); [WBAG](../2026/arXiv/2026_arXiv_WBAG-A-Whole-Body-and-Attached-Geometry-Safety-Framework-f/01_overview.md) (2026 arXiv) | 이동체·팔·부착 물체의 제약을 VLA의 고수준 명령과 연결한다. Attached geometry 안전성을 명령 생성 능력과 분리한다. |

### 2026-10-25 top-tier 보완 — 읽기 전 비교 연결

> Researcher interpretation / CURATION-HYPOTHESIS. 신규 노트는 abstract/project 기반이며 아래 연결은 정독·실험 결과나 직접 citation 관계의 확인이 아니다.

[TidyBot++](../2024/CoRL/2024_CoRL_TidyBot%2B%2B-An-Open-Source-Holonomic-Mobile-Manipulator-for/01_overview.md)는 Mobile ALOHA와 비교할 holonomic base·teleoperation 플랫폼이다. 다양한 arm을 지원하는 설계와 모든 arm 조합의 실증은 구분한다. Base의 planar 자유도와 reachability가 달라지면 같은 언어 과제도 action 난도가 달라질 수 있다.

Cross-embodiment 비교에서는 base/arm action 단위·제어 주기·시연 비용·충돌 제약을 먼저 맞춘다. 플랫폼 공개만으로 policy transfer나 clone 후 실행 가능성을 입증하지 않는다.

## Open Questions

<a id="gap-mobile-contact-rl-2026"></a>
### 접촉을 유지하는 이동 조작의 단일 VLA 강화학습

**2026-11-09 / GAP-MOBILE-CONTACT-RL / 3순위 예비 탐색 / CURATION-HYPOTHESIS.** [선정 범위](https://github.com/Kim-Yoo-Hyun/PaperReview/blob/cb650415f47a2a45ad883dabe5bd20c382b5c183/work/update/VLA_RL_ADDITIONAL_GAPS_2026-11-09.md#robotics-reorientation), [근거 R17–R20](../work/sources/vla_rl_additional_gaps_2026-11-09.json). 기존 HANDOFF의 정지 후 정책 교체/도착점 재사용 질문을 재명명한 것이 아니다.

**질문:** 긴 서랍이나 문을 잡은 채 이동할 때, 한 VLA가 base와 arm의 행동을 함께 RL 후학습하여 접촉 상실·관절 한계·충돌을 줄일 수 있는가? Navigation 도착 성공이 아니라 **이동 중 조작 목표의 물리적 실행 가능성**을 측정한다. 처음부터 humanoid 균형까지 포함하지 않고, wheeled mobile manipulator의 한 과제로 좁힐 수 있다.

**강한 선행:** [MoTo, CoRL 2025](https://proceedings.mlr.press/v305/wu25c.html)는 interaction-aware docking과 base/arm의 물리적 trajectory feasibility를, [Mobi-π, CoRL 2025](https://proceedings.mlr.press/v305/yang25b.html)는 기존 조작 정책에 적합한 base pose를 다룬다. [WholeBodyVLA, ICLR 2026](https://proceedings.iclr.cc/paper_files/paper/2026/hash/ff7373914a96956f2a7cacbdf3b0b8d8-Abstract-Conference.html)는 latent VLA와 loco-manipulation용 RL 제어를 제시한다. [MobileVLA-R1](https://aigeeksgroup.github.io/MobileVLA-R1/)도 언어 조건부 mobile action과 RL 후학습을 다룬다. “navigation과 manipulation을 연결한다”, “VLA에 base action을 추가한다”는 공백이 아니다.

**남은 탐색:** 고정된 low-level servo 위에서 하나의 학습 정책이 base·arm reference를 출력할 때, 학습된 공동 적응이 coordinated whole-body MPC/IK·행동 모방·residual RL보다 낫게 만드는 접촉 조건은 무엇인가? WholeBodyVLA 등 본문/부록의 contact-maintenance 비교까지 확인하지 못해, 이 질문의 신규성은 접촉 후보보다 더 불확실하다. 사전 학습된 policy의 action space 확장 자체가 큰 구현 과제다.

비교는 task 성공과 함께 grasp/contact 유지, wrench, collision, joint-limit margin, base 이동 거리·소요 시간을 기록한다. Staged docking은 참고선이며 강한 기준선은 **base와 arm을 동시에 조정하는 고전 whole-body 제어**다. 정지 후 수행해도 충분한 task만 골라 통합 모델을 주장하지 않는다. 두 학습 정책을 한 이름으로 감싼 시스템은 사용자가 원하는 단일 행동 정책과 구별한다. 공개 mobile checkpoint/환경/실물 플랫폼은 아직 고정하지 않았으며, 석사 범위의 검증 부담이 커 우선 실행 후보로 올리지 않는다.

### 3D affordance와 whole-body 제어의 분리

[SAGA](../2026/RA-L/2026_RA-L_SAGA-Open-World-Mobile-Manipulation-via-Structured-Afforda/01_overview.md)는 언어·point·시연을 3D affordance로 바꿔 quadrupedal manipulator를 조건화하는 비교 기준이다. Abstract/project 기반 해석이며, 여러 지시 형식 지원과 여러 embodiment로의 전이 입증을 구분한다. 같은 관측·skill/action budget에서 직접 목표 위치를 전달하는 단순 방식 이후 남는 이득은 무엇인가? HANDOFF의 상태 복원·정책 교체 효과를 이 논문으로 검증했다고 간주하지 않는다.


<a id="gap-handoff-2026"></a>

### 정책 교체와 접근 조건

복원한 조작 시작 상태와 실제 이동 후 도착 상태에서의 능력을 구별한다. [검토 결과](../work/research_topics/RESULTS.md#mobile_policy_transfer)

| 문헌 질문 | 비교에서 구별할 것 |
|---|---|
| VLA→저수준 command | 고정 controller의 command rate·delay·unsafe rejection과 controller 교체 효과 |
| Whole-body contact | Motion tracking과 task 성공, 접촉/actuator margin·회복의 실제 사건 분모 |

<a id="gap-thermal-2026"></a>
### GAP-THERMAL — 순간적으로 가능한 행동을 장시간 반복할 수 있는가?

- 갱신: 2026-10-23. `CURATION-HYPOTHESIS`; locomotion·whole-body control·actuator/thermal engineering 질문. [확장 조사](https://github.com/Kim-Yoo-Hyun/PaperReview/blob/cb650415f47a2a45ad883dabe5bd20c382b5c183/work/update/BROAD_RESEARCH_GAP_SCOUT_2026-10-23.md).
- **문제와 중요성:** 짧은 task 성공과 연속 운용의 능력은 다르다. Payload, ambient temperature, 이동/조작의 반복으로 열이 쌓이면 가능한 torque와 task schedule도 달라질 수 있다. 처리량과 회복 시간을 포함한 장시간 능력을 봐야 한다.
- **이미 답한 범위:** [FALCON, L4DC 2026](https://proceedings.mlr.press/v331/zhang26a.html)은 force-adaptive humanoid loco-manipulation을 다룬다. 온도 기반 reward/input은 [thermal-aware quadruped policy](https://arxiv.org/abs/2603.01631), 성능/열 trade-off와 residual policy는 [후속 thermal residual policy](https://arxiv.org/html/2605.27046v3)에 이미 있다. 두 thermal 논문은 확인한 출처 기준 arXiv이며 acceptance를 확정하지 않는다. [Humanoids 2025 liquid-cooling leg](https://ieeexplore.ieee.org/abstract/document/11203109)처럼 hardware 설계도 직접 대안이다.
- **남은 질문 — 연구자 해석:** 고정된 thermal model에서 배운 제한이 다른 payload·ambient·cooling 상태 및 이동/조작 전환에서도 충분한가? Task 하나의 속도를 낮추는 것보다 task sequence·rest·contact allocation을 바꾸는 것이 같은 열 한도에서 유효 처리량을 높이는 조건은 무엇인가? 일반적인 thermal-aware RL이라는 주장은 새롭지 않다.
- **최소 검증:** 초기 온도·배터리·주변 온도·payload·냉각 대기·motor limits를 통제하고 온도·전류·joint command·contact를 같은 시간축에 남긴다. Torque derating, 고정 rest schedule, thermal-aware MPC/기존 RL, 제안된 scheduling을 같은 최대 온도·안전 한도에서 비교한다. 완료 task/hour, downtime, tracking/contact failure, 온도 추정 오차, 한도 초과를 기록한다. 더 느리게 움직인 효과를 제거하지 않고 endurance 향상으로만 보고하지 않는다.
- **가치·반증·자원:** 운용 가치가 있지만 hardware 의존성이 가장 높다. 기존 derating/rest만으로 같은 처리량을 얻으면 새 학습의 필요성을 줄인다. 실제 thermal parameter와 장시간 telemetry 없이 simulator endurance를 실제 지속 시간으로 주장하지 않는다. 현재는 hardware/데이터 확보 전 문헌 보존 대상으로 둔다. GPU만으로 재개 가능한 주제가 아니다.

<a id="psi0-controller-boundary"></a>
## Ψ₀–AMO–SONIC의 비교 경계 — 2026-11-16

[AMO](../2025/RSS/2025_RSS_AMO-Adaptive-Motion-Optimization-for-Hyper-Dexterous-Human/01_overview.md)의 OCR 기반 노트를 지정 본문으로 교정했다. Ψ₀ v1의 직접 하위 controller이며 adaptation/trajectory optimization과 RL lower policy를 구분한다. [SONIC](../2026/Science-Robotics/2026_Science-Robotics_SONIC-Supersizing-Motion-Tracking-for-Natural-Humanoid-Who/01_overview.md)은 공개 code/DOI를 보완했지만 과거 본문 전체를 이번에 다시 검토한 것은 아니다.

[Ψ₀ 공개 repository](https://github.com/physical-superintelligence-lab/Psi0)의 후속 SONIC 모델은 논문 v1 AMO 결과와 같은 실행 조건이 아니다. Whole-body control token의 통합과 VLA backbone의 RL 공동 갱신을 구분한다. Open question은 controller 변경이 상위 VLA 성능 개선처럼 보이는 조건이며, 동일 feasible command·시간 예산에서 tracking과 task success를 따로 측정해야 한다. 새 효과를 입증하거나 기존 REFERENCE tier를 자동 승격한 것은 아니다.
