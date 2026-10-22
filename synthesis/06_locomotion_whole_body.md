# Locomotion, Whole-Body, Mobile Manipulation, and Humanoids

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

### Locomotion, whole-body control, mobile manipulation, and humanoids — 12

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
| [ZMP Preview Control](../2003/ICRA/2003_ICRA_Biped-Walking-Pattern-Generation-by-using-Preview-Control/01_overview.md) | 2003 / ICRA | foundation; controller | biped; proprioception+ZMP; model-based; locomotion control | preview-based biped walking pattern generation | CoM/cart-table and future ZMP; walking trajectory; ZMP stability objective; preview horizon | learned policy와 비교할 explicit stability/reference baseline | walking simulation/robot; data/split=UNVERIFIED; metric=tracking/stability; real=UNVERIFIED/trials=UNVERIFIED | `CURATION-SEED`; overview + queue | simplified dynamics, flat terrain, fixed contact schedule | learned command에 classical stability signal을 남김 |
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
| [ZMP Preview Control](../2003/ICRA/2003_ICRA_Biped-Walking-Pattern-Generation-by-using-Preview-Control/01_overview.md) → [Dynamic Whole-Body Motion Generation](../2013/T-RO/2013_T-RO_Dynamic-Whole-Body-Motion-Generation-under-Rigid-Contacts/01_overview.md) / [HQP](../2014/IJRR/2014_IJRR_Hierarchical-Quadratic-Programming-Fast-Online-Humanoid-Ro/01_overview.md) → [Whole-Body NMPC](../2018/RA-L/2018_RA-L_Whole-Body-Nonlinear-Model-Predictive-Control-Through-Cont/01_overview.md) | simplified balance reference tracking에서 explicit multi-contact dynamics, task hierarchy와 predictive constraint handling으로 확장된다. | learned motion command와 contact schedule가 바뀔 때 classical stability quantity를 어떤 runtime signal로 유지할 것인가 |
| [Dynamic Whole-Body Motion Generation](../2013/T-RO/2013_T-RO_Dynamic-Whole-Body-Motion-Generation-under-Rigid-Contacts/01_overview.md) / [HQP](../2014/IJRR/2014_IJRR_Hierarchical-Quadratic-Programming-Fast-Online-Humanoid-Ro/01_overview.md) / [Whole-Body NMPC](../2018/RA-L/2018_RA-L_Whole-Body-Nonlinear-Model-Predictive-Control-Through-Cont/01_overview.md) → learned whole-body policies → [HWC-Loco](../2026/ICLR/2026_ICLR_HWC-Loco-A-Hierarchical-Whole-Body-Control-Approach-to-Rob/01_overview.md) | explicit dynamics/contact hierarchy에서 대규모 policy learning으로 이동한 뒤, task policy와 safety-recovery policy를 계층화하는 방향이 나타난다. | learned high-level switch가 model-based feasibility와 stability guarantee를 얼마나 보존하는가 |
| [Domain Randomization](../2017/IROS/2017_IROS_Domain-Randomization-for-Transferring-Deep-Neural-Networks/01_overview.md) / quadruped sim-to-real → [RMA](../2021/RSS/2021_RSS_RMA-Rapid-Motor-Adaptation-for-Legged-Robots/01_overview.md) / [Perceptive Locomotion](../2022/Science-Robotics/2022_Science-Robotics_Learning-Robust-Perceptive-Locomotion-for-Quadrupedal-Robo/01_overview.md) → [ANYmal Parkour](../2024/Science-Robotics/2024_Science-Robotics_ANYmal-Parkour-Learning-Agile-Navigation-for-Quadrupedal-R/01_overview.md) / [ASAP](../2025/RSS/2025_RSS_ASAP-Aligning-Simulation-and-Real-World-Physics-for-Learni/01_overview.md) / [VIRAL](../2026/CVPR/2026_CVPR_VIRAL-Visual-Sim-to-Real-at-Scale-for-Humanoid-Loco-Manipu/01_overview.md) | robustness randomization에서 latent adaptation, terrain perception, agile skill과 real-physics/visual alignment로 확장된다. | adaptation, perception과 privileged teacher가 각각 실제 deployment robustness에 기여하는 비율은 무엇인가 |
| [DeepMimic](../2018/TOG-SIGGRAPH/2018_TOG-SIGGRAPH_DeepMimic-Example-Guided-Deep-Reinforcement-Learning-of-Ph/01_overview.md) → [AMP](../2021/ACM-Transactions-on-Grap/2021_ACM-Transactions-on-Grap_AMP-Adversarial-Motion-Priors-for-Stylized-Physics-Based-C/01_overview.md) → [PHC](../2023/ICCV/2023_ICCV_Perpetual-Humanoid-Control-for-Real-time-Simulated-Avatars/01_overview.md) / [MaskedMimic](../2024/ACM-Transactions-on-Grap/2024_ACM-Transactions-on-Grap_MaskedMimic-Unified-Physics-Based-Character-Control-Throug/01_overview.md) → [HOVER](../2025/ICRA/2025_ICRA_HOVER-Versatile-Neural-Whole-Body-Controller-for-Humanoid/01_overview.md) / [SONIC](../2026/Science-Robotics/2026_Science-Robotics_SONIC-Supersizing-Motion-Tracking-for-Natural-Humanoid-Who/01_overview.md) | reference tracking에서 adversarial style prior, perpetual/fallback tracking, masked multi-command unification과 scaled real-humanoid controller로 확장된다. | 자연스러운 tracking score, physical feasibility, fall/recovery와 object-level task success를 어떻게 공동 평가할 것인가 |
| AMP/PHC/MaskedMimic motion-controller backbone → [HumanPlus](../2024/CoRL/2024_CoRL_HumanPlus-Humanoid-Shadowing-and-Imitation-from-Humans/01_overview.md) / [OmniH2O](../2024/CoRL/2024_CoRL_OmniH2O-Universal-and-Dexterous-Human-to-Humanoid-Whole-Bo/01_overview.md) → [LangWBC](../2025/RSS/2025_RSS_LangWBC-Language-Directed-Humanoid-Whole-Body-Control-via/01_overview.md) | motion prior/controller가 human shadowing·teleoperation, retargeting과 language-conditioned compositional whole-body behavior의 저수준 substrate가 된다. | semantic command가 balance margin, contact feasibility와 recovery budget을 전달하는가 |
| [Mobile ALOHA](../2024/CoRL/2024_CoRL_Mobile-ALOHA-Learning-Bimanual-Mobile-Manipulation-using-L/01_overview.md) → [RoboPanoptes](../2025/RSS/2025_RSS_RoboPanoptes-The-All-Seeing-Robot-with-Whole-body-Dexterit/01_overview.md) → humanoid loco-manipulation | whole-body teleoperation과 mobile bimanual data에서 distributed whole-body perception 및 body-contact manipulation으로 확장된다. | base motion, arm action, distributed vision의 서로 다른 bandwidth를 하나의 policy가 안정적으로 다루는가 |
| locomotion/manipulation benchmark → [HumanoidBench](../2024/RSS/2024_RSS_HumanoidBench-Simulated-Humanoid-Benchmark-for-Whole-Body/01_overview.md) → real-world whole-body systems | 개별 motor skill을 넘어 locomotion과 manipulation을 한 embodiment에서 비교할 공통 평가로 이동한다. | simulator 순위가 hardware durability, fall severity, recovery와 일치하는가 |

## 2026-10-23 근거 통합

아래는 2026-10-22까지의 registry/source 감사와 후보 검토를 연결한 연구자 해석이다. 새 정독·효과 검증·직접 citation 관계의 확인을 뜻하지 않는다. Paper별 본문 확인 범위는 overview 및 연결된 dossier를 따른다.

| 비교 축 | 등록된 선행 | 현재 남길 구분 |
|---|---|---|
| Attachment와 이동 중 제어 | [Geometric Fabrics](../2025/RA-L/2025_RA-L_Globally-Guided-Geometric-Fabrics-for-Reactive-Mobile-Mani/01_overview.md) (2025 RA-L); [WBAG](../2026/arXiv/2026_arXiv_WBAG-A-Whole-Body-and-Attached-Geometry-Safety-Framework-f/01_overview.md) (2026 arXiv) | 이동체·팔·부착 물체의 제약을 VLA의 고수준 명령과 연결한다. Attached geometry 안전성을 명령 생성 능력과 분리한다. |

## Open Questions

현재 후보 판정은 [주제별 요약](../work/research_candidates/summaries/README.md)을 따른다. 아래 질문은 `CURATION-HYPOTHESIS`이며 재개 승인이 아니다.

| 질문 | 구별할 예측 | 최소 대조·중단 조건 | 근거/판정 |
|---|---|---|---|
| VLA→저수준 command | 고정 low-level controller에서 command rate·delay·unsafe-command rejection이 base 안정성과 arm success를 어떻게 바꾸는가? | HOVER/SONIC류 controller의 입력 단위·termination·queue를 기록한다. Controller 교체 효과를 VLA 개선으로 귀속하지 않는다. | 기존 track 비교의 연구자 질문; native 효과 미검증 |
| Whole-body contact | Human motion prior와 큰 tracking corpus가 task 성공·contact feasibility를 유지하면서 rare failure를 줄이는가? | Fall·actuator saturation·recovery onset의 event 분모를 남긴다. Tracking score와 manipulation 성공을 따로 평가한다. | 기존 track 비교의 연구자 질문; native 효과 미검증 |
