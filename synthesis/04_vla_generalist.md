# VLA and Generalist Robot Policies

- Updated: 2026-11-12 KST

## Scope

Multimodal generalist agents, robot fleet/data orchestration, language-conditioned manipulation, hierarchical action interfaces, cross-embodiment VLA, humanoid foundation policies, long-horizon skill composition과 closed-loop reasoning을 비교한다.

### Taxonomy boundary and curation schema

- **Primary axis:** multimodal foundation → robot action interface → embodiment/data scaling → planning, memory and feedback.
- **In scope:** language-conditioned robot policy, VLA, generalist robot data/model, action representation, planner/policy hierarchy와 deployment interface가 실제 robot behavior를 바꾸는 경우.
- **Out of scope:** language-only model, robot-independent vision-language benchmark, 또는 action/control loop가 없는 general-purpose agent. 해당 논문은 enabling perception·planning track으로 연결한다.
- **Inclusion test:** language/vision/proprioception input, robot-visible state, action format, embodiment/data setting, closed-loop evaluation 중 최소 네 가지를 비교할 수 있어야 한다.
- **Role vocabulary:** `foundation`, `policy`, `action representation`, `data engine`, `planner`, `memory`, `benchmark`, `system`, `safety interface`를 사용한다.

공통 matrix/evidence 규약은 [synthesis 안내](./README.md#공통-비교-규약과-질문-분류)를 따른다.

## Reading Path

현재 읽기 우선순위는 [READING_PLAN.md](../research/READING_PLAN.md)를 따른다. 아래 계보는 비교 탐색용이며 전체 선행 완독 의무가 아니다.

기존 VLA+RL 비교 계보: OpenVLA/OFT·π0·FAST의 action interface를 기반으로 ConRFT의 직접 RL, RLDG의 RL-data distillation, SayCan·NaVILA의 계층적 value/control 결합을 구분한다. Manipulation과 navigation의 reward·memory·action granularity를 동일한 것으로 취급하지 않는다.

2026-10-23 초점: VLA의 행동 표현·시간/feedback·로봇 간 보존·실행 가능성을 비교하며 RL은 추가 설명력이 필요한 경우에 선택한다. 아래 과거 계보는 prerequisites이지 활성 연구 순위가 아니다.

Gato/CLIP/CLIPort → PaLM-E/RT-1/RT-2 → MT-Opt/AutoRT data engine → Open X-Embodiment → Octo/OpenVLA/π0 → RT-H/FAST/OpenVLA-OFT/π0.5 → Gemini Robotics/GR00T N1 → SAFE/FLARE/FaultEval와 3D-, memory-, progress-aware VLA.

### 2026-10-19 추가 논문 비교

아래는 등록된 abstract/project 근거에서 만든 **정독 전 비교 질문**이다. 직접 citation이나 실험 결론으로 취급하지 않으며, 읽기 순서와 tier는 READING_PLAN의 최신 값을 따른다.

| 비교할 논문 | 비교 축 | 본문에서 확인할 조건 |
|---|---|---|
| [RL4VLA](../2025/NeurIPS/2025_NeurIPS_What-Can-RL-Bring-to-VLA-Generalization-An-Empirical-Study/01_overview.md) ↔ [SimpleVLA-RL](../2026/ICLR/2026_ICLR_SimpleVLA-RL-Scaling-VLA-Training-via-Reinforcement-Learni/01_overview.md) ↔ [RLux-VLA](../2026/RSS/2026_RSS_RLux-VLA-A-Unified-and-Efficient-Framework-for-Reinforceme/01_overview.md) ↔ [DyGRO-VLA](../2026/ICML/2026_ICML_DyGRO-VLA-Cross-Task-Scaling-of-VisionLanguageAction-Model/01_overview.md) | VLA generalization·RL update·시스템 효율 | OFT·ConRFT·RLDG를 비교 기준으로 두고 algorithm, data, parallel training과 compute의 효과를 분리한다. |
| [NaVid](../2024/RSS/2024_RSS_NaVid-Video-based-VLM-Plans-the-Next-Step-for-Vision-and-L/01_overview.md) ↔ [StreamVLN](../2026/ICRA/2026_ICRA_StreamVLN-Streaming-Vision-and-Language-Navigation-via-Slo/01_overview.md) ↔ [SocialNav](../2026/CVPR/2026_CVPR_SocialNav-Training-Human-Inspired-Foundation-Model-for-Soc/01_overview.md) / NaVILA | Navigation memory·streaming·social cost | Manipulation과 다른 action granularity, observation history, collision/social metric, robot deployment 범위를 확인한다. |

<!-- READING_QUEUE:START -->

## Assigned Reading Queue

### VLA and generalist robot policies — 13

| Tier | Paper | Year / Venue | Status | Evidence |
|---|---|---|---|---|
| CORE | [Learning Transferable Visual Models From Natural Language Supervision](../2021/ICML/2021_ICML_Learning-Transferable-Visual-Models-From-Natural-Language/01_overview.md) | 2021 / ICML | `UNREAD` | `FULL_TEXT_CHECKED` |
| CORE | [RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control](../2023/CoRL/2023_CoRL_RT-2-Vision-Language-Action-Models-Transfer-Web-Knowledge/01_overview.md) | 2023 / CoRL | `UNREAD` | `FULL_TEXT_CHECKED` |
| CORE | [Open X-Embodiment: Robotic Learning Datasets and RT-X Models](../2024/ICRA/2024_ICRA_Open-X-Embodiment-Robotic-Learning-Datasets-and-RT-X-Model/01_overview.md) | 2024 / ICRA | `UNREAD` | `FULL_TEXT_CHECKED` |
| CORE | [Octo: An Open-Source Generalist Robot Policy](../2024/RSS/2024_RSS_Octo-An-Open-Source-Generalist-Robot-Policy/01_overview.md) | 2024 / RSS | `UNREAD` | `FULL_TEXT_CHECKED` |
| CORE | [OpenVLA: An Open-Source Vision-Language-Action Model](../2024/CoRL/2024_CoRL_OpenVLA-An-Open-Source-Vision-Language-Action-Model/01_overview.md) | 2024 / CoRL | `UNREAD` | `FULL_TEXT_CHECKED` |
| CORE | [Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success](../2025/RSS/2025_RSS_Fine-Tuning-Vision-Language-Action-Models-Optimizing-Speed/01_overview.md) | 2025 / RSS | `UNREAD` | `FULL_TEXT_CHECKED` |
| CORE | [π0: A Vision-Language-Action Flow Model for General Robot Control](../2025/RSS/2025_RSS_pi0-A-Vision-Language-Action-Flow-Model-for-General-Robot/01_overview.md) | 2025 / RSS | `UNREAD` | `FULL_TEXT_CHECKED` |
| CORE | [FAST: Efficient Action Tokenization for Vision-Language-Action Models](../2025/RSS/2025_RSS_FAST-Efficient-Action-Tokenization-for-Vision-Language-Act/01_overview.md) | 2025 / RSS | `UNREAD` | `FULL_TEXT_CHECKED` |
| CORE | [π0.5: a Vision-Language-Action Model with Open-World Generalization](../2025/CoRL/2025_CoRL_pi0.5-a-Vision-Language-Action-Model-with-Open-World-Gener/01_overview.md) | 2025 / CoRL | `UNREAD` | `FULL_TEXT_CHECKED` |
| CORE | [ConRFT: A Reinforced Fine-tuning Method for VLA Models via Consistency Policy](../2025/RSS/2025_RSS_ConRFT-A-Reinforced-Fine-tuning-Method-for-VLA-Models-via/01_overview.md) | 2025 / RSS | `UNREAD` | `FULL_TEXT_CHECKED` |
| CORE | [Do As I Can, Not As I Say: Grounding Language in Robotic Affordances](../2022/CoRL/2022_CoRL_Do-As-I-Can-Not-As-I-Say-Grounding-Language-in-Robotic-Aff/01_overview.md) | 2022 / CoRL | `UNREAD` | `FULL_TEXT_CHECKED` |
| CORE | [NaVILA: Legged Robot Vision-Language-Action Model for Navigation](../2025/RSS/2025_RSS_NaVILA-Legged-Robot-Vision-Language-Action-Model-for-Navig/01_overview.md) | 2025 / RSS | `UNREAD` | `FULL_TEXT_CHECKED` |
| CORE | [CALVIN: A Benchmark for Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks](../2022/RA-L/2022_RA-L_CALVIN-A-Benchmark-for-Language-Conditioned-Policy-Learnin/01_overview.md) | 2022 / RA-L | `UNREAD` | `FULL_TEXT_CHECKED` |

### VLA, cross-embodiment, and long-horizon planning — 156

| Tier | Paper | Year / Venue | Status | Evidence |
|---|---|---|---|---|
| NEXT | [What Can RL Bring to VLA Generalization? An Empirical Study](../2025/NeurIPS/2025_NeurIPS_What-Can-RL-Bring-to-VLA-Generalization-An-Empirical-Study/01_overview.md) | 2025 / NeurIPS | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning](../2026/ICLR/2026_ICLR_SimpleVLA-RL-Scaling-VLA-Training-via-Reinforcement-Learni/01_overview.md) | 2026 / ICLR | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [RLinf-VLA: A Unified and Efficient Framework for Reinforcement Learning of Vision-Language-Action Models](../2026/RSS/2026_RSS_RLux-VLA-A-Unified-and-Efficient-Framework-for-Reinforceme/01_overview.md) | 2026 / RSS | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [A Generalist Pair-wise Progress Critic Model for Vision-Language-Action Robots](../2026/ICML/2026_ICML_A-Generalist-Pair-wise-Progress-Critic-Model-for-Vision-La/01_overview.md) | 2026 / ICML | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [Learning from Hindsight for VLA Reinforcement Learning](../2026/arXiv/2026_arXiv_Learning-from-Hindsight-for-VLA-Reinforcement-Learning/01_overview.md) | 2026 / arXiv | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [CAST: Counterfactual Labels Improve Instruction Following in Vision-Language-Action Models](../2025/arXiv/2025_arXiv_CAST-Counterfactual-Labels-Improve-Instruction-Following-i/01_overview.md) | 2025 / arXiv | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [NaVid: Video-based VLM Plans the Next Step for Vision-and-Language Navigation](../2024/RSS/2024_RSS_NaVid-Video-based-VLM-Plans-the-Next-Step-for-Vision-and-L/01_overview.md) | 2024 / RSS | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [StreamVLN: Streaming Vision-and-Language Navigation via SlowFast Context Modeling](../2026/ICRA/2026_ICRA_StreamVLN-Streaming-Vision-and-Language-Navigation-via-Slo/01_overview.md) | 2026 / ICRA | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [SocialNav: Training Human-Inspired Foundation Model for Socially-Aware Embodied Navigation](../2026/CVPR/2026_CVPR_SocialNav-Training-Human-Inspired-Foundation-Model-for-Soc/01_overview.md) | 2026 / CVPR | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [DyGRO-VLA: Cross-Task Scaling of Vision–Language–Action Models via Dynamic Grouped Residual Optimization](../2026/ICML/2026_ICML_DyGRO-VLA-Cross-Task-Scaling-of-VisionLanguageAction-Model/01_overview.md) | 2026 / ICML | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [CLIPort: What and Where Pathways for Robotic Manipulation](../2021/CoRL/2021_CoRL_CLIPort-What-and-Where-Pathways-for-Robotic-Manipulation/01_overview.md) | 2021 / CoRL | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [PaLM-E: An Embodied Multimodal Language Model](../2023/ICML/2023_ICML_PaLM-E-An-Embodied-Multimodal-Language-Model/01_overview.md) | 2023 / ICML | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [RT-1: Robotics Transformer for Real-World Control at Scale](../2022/arXiv/2022_arxiv_RT-1-Robotics-Transformer-for-Real-World-Control-at-Scale/01_overview.md) | 2022 / arXiv | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models](../2023/CoRL/2023_CoRL_VoxPoser-Composable-3D-Value-Maps-for-Robotic-Manipulation/01_overview.md) | 2023 / CoRL | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [A Generalist Agent](../2022/arXiv/2022_arXiv_A-Generalist-Agent/01_overview.md) | 2022 / arXiv | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [AutoRT: Embodied Foundation Models for Large Scale Orchestration of Robotic Agents](../2024/arXiv/2024_arXiv_AutoRT-Embodied-Foundation-Models-for-Large-Scale-Orchestr/01_overview.md) | 2024 / arXiv | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [RT-H: Action Hierarchies Using Language](../2024/Robotics-Science-and-Sys/2024_Robotics-Science-and-Sys_RT-H-Action-Hierarchies-Using-Language/01_overview.md) | 2024 / Robotics: Science and Systems | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [Gemini Robotics: Bringing AI into the Physical World](../2025/arXiv/2025_arXiv_Gemini-Robotics-Bringing-AI-into-the-Physical-World/01_overview.md) | 2025 / arXiv | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [NVIDIA Isaac GR00T N1: An Open Foundation Model for Humanoid Robots](../2025/arXiv/2025_arXiv_NVIDIA-Isaac-GR00T-N1-An-Open-Foundation-Model-for-Humanoi/01_overview.md) | 2025 / arXiv | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [BC-Z: Zero-Shot Task Generalization with Robotic Imitation Learning](../2022/CoRL/2022_CoRL_BC-Z-Zero-Shot-Task-Generalization-with-Robotic-Imitation/01_overview.md) | 2022 / CoRL | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [Perceiver-Actor: A Multi-Task Transformer for Robotic Manipulation](../2023/CoRL/2023_CoRL_Perceiver-Actor-A-Multi-Task-Transformer-for-Robotic-Manip/01_overview.md) | 2023 / CoRL | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [VIMA: General Robot Manipulation with Multimodal Prompts](../2023/ICML/2023_ICML_VIMA-General-Robot-Manipulation-with-Multimodal-Prompts/01_overview.md) | 2023 / ICML | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [Inner Monologue: Embodied Reasoning through Planning with Language Models](../2022/CoRL/2022_CoRL_Inner-Monologue-Embodied-Reasoning-through-Planning-with-L/01_overview.md) | 2022 / CoRL | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [SayPlan: Grounding Large Language Models using 3D Scene Graphs for Scalable Robot Task Planning](../2023/CoRL/2023_CoRL_SayPlan-Grounding-Large-Language-Models-using-3D-Scene-Gra/01_overview.md) | 2023 / CoRL | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [XSkill: Cross Embodiment Skill Discovery](../2023/CoRL/2023_CoRL_XSkill-Cross-Embodiment-Skill-Discovery/01_overview.md) | 2023 / CoRL | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [Scaling Proprioceptive-Visual Learning with Heterogeneous Pre-trained Transformers](../2024/NeurIPS/2024_NeurIPS_Scaling-Proprioceptive-Visual-Learning-with-Heterogeneous/01_overview.md) | 2024 / NeurIPS | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [AtomicVLA: Unlocking the Potential of Atomic Skill Learning in Robots](../2026/CVPR/2026_CVPR_AtomicVLA-Unlocking-the-Potential-of-Atomic-Skill-Learning/01_overview.md) | 2026 / CVPR | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [PALM: Progress-Aware Policy Learning via Affordance Reasoning for Long-Horizon Robotic Manipulation](../2026/CVPR/2026_CVPR_PALM-Progress-Aware-Policy-Learning-via-Affordance-Reasoni/01_overview.md) | 2026 / CVPR | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [ActiveVLA: Injecting Active Perception into Vision-Language-Action Models for Precise 3D Robotic Manipulation](../2026/CVPR/2026_CVPR_ActiveVLA-Injecting-Active-Perception-into-Vision-Language/01_overview.md) | 2026 / CVPR | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [Spatial Memory for Out-of-Vision Manipulation in Vision-Language-Action](../2026/ICML/2026_ICML_Spatial-Memory-for-Out-of-Vision-Manipulation-in-Vision-La/01_overview.md) | 2026 / ICML | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [Counterfactual VLA: Self-Reflective Vision-Language-Action Model with Adaptive Reasoning](../2026/CVPR/2026_CVPR_Counterfactual-VLA-Self-Reflective-Vision-Language-Action/01_overview.md) | 2026 / CVPR | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [Any3D-VLA: Enhancing VLA Robustness via Diverse Point Clouds](../2026/ICML/2026_ICML_Any3D-VLA-Enhancing-VLA-Robustness-via-Diverse-Point-Cloud/01_overview.md) | 2026 / ICML | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [MomaGraph: State-Aware Unified Scene Graphs with Vision-Language Models for Embodied Task Planning](../2026/ICLR/2026_ICLR_MomaGraph-State-Aware-Unified-Scene-Graphs-with-Vision-Lan/01_overview.md) | 2026 / ICLR | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [AVA-VLA: Improving Vision-Language-Action Models with Active Visual Attention](../2026/CVPR/2026_CVPR_AVA-VLA-Improving-Vision-Language-Action-Models-with-Activ/01_overview.md) | 2026 / CVPR | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [VLA-Arena: An Open-Source Framework for Benchmarking Vision-Language-Action Models](../2026/ICML/2026_ICML_VLA-Arena-An-Open-Source-Framework-for-Benchmarking-Vision/01_overview.md) | 2026 / ICML | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Models](../2025/RSS/2025_RSS_SpatialVLA-Exploring-Spatial-Representations-for-Visual-La/01_overview.md) | 2025 / RSS | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [From Spatial to Actions: Grounding Vision-Language-Action Model in Spatial Foundation Priors](../2026/ICLR/2026_ICLR_From-Spatial-to-Actions-Grounding-Vision-Language-Action-M/01_overview.md) | 2026 / ICLR | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [Uni-NaVid: A Video-based Vision-Language-Action Model for Unifying Embodied Navigation Tasks](../2025/RSS/2025_RSS_Uni-NaVid-A-Video-based-Vision-Language-Action-Model-for-U/01_overview.md) | 2025 / RSS | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [Learning to Act Anywhere with Task-centric Latent Actions](../2025/RSS/2025_RSS_Learning-to-Act-Anywhere-with-Task-centric-Latent-Actions/01_overview.md) | 2025 / RSS | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [CLIP-RT: Learning Language-Conditioned Robotic Policies from Natural Language Supervision](../2025/RSS/2025_RSS_CLIP-RT-Learning-Language-Conditioned-Robotic-Policies-fro/01_overview.md) | 2025 / RSS | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [CodeDiffuser: Attention-Enhanced Diffusion Policy via VLM-Generated Code for Instruction Ambiguity](../2025/RSS/2025_RSS_CodeDiffuser-Attention-Enhanced-Diffusion-Policy-via-VLM-G/01_overview.md) | 2025 / RSS | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [PartInstruct: Part-level Instruction Following for Fine-grained Robot Manipulation](../2025/RSS/2025_RSS_PartInstruct-Part-level-Instruction-Following-for-Fine-gra/01_overview.md) | 2025 / RSS | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [Manual2Skill: Learning to Read Manuals and Acquire Robotic Skills for Furniture Assembly Using Vision-Language Models](../2025/RSS/2025_RSS_Manual2Skill-Learning-to-Read-Manuals-and-Acquire-Robotic/01_overview.md) | 2025 / RSS | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics](../2025/arXiv/2025_arXiv_SmolVLA-A-Vision-Language-Action-Model-for-Affordable-and/01_overview.md) | 2025 / arXiv | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [Gemini Robotics 1.5: Pushing the Frontier of Generalist Robots with Advanced Embodied Reasoning, Thinking, and Motion Transfer](../2025/arXiv/2025_arXiv_Gemini-Robotics-1.5-Pushing-the-Frontier-of-Generalist-Rob/01_overview.md) | 2025 / arXiv | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [GR00T N1.5: An Improved Open Foundation Model for Generalist Humanoid Robots](../2025/Technical-Report/2025_Technical-Report_GR00T-N1.5-An-Improved-Open-Foundation-Model-for-Generalis/01_overview.md) | 2025 / Technical Report | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [GR00T N1.6: An Improved Open Foundation Model for Generalist Humanoid Robots](../2025/Technical-Report/2025_Technical-Report_GR00T-N1.6-An-Improved-Open-Foundation-Model-for-Generalis/01_overview.md) | 2025 / Technical Report | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [Grounding Actions in Camera Space: Observation-Centric Vision-Language-Action Policy](../2026/AAAI/2026_AAAI_Grounding-Actions-in-Camera-Space-Observation-Centric-Visi/01_overview.md) | 2026 / AAAI | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [ReKep: Spatio-Temporal Reasoning of Relational Keypoint Constraints for Robotic Manipulation](../2024/CoRL/2024_CoRL_ReKep-Spatio-Temporal-Reasoning-of-Relational-Keypoint-Con/01_overview.md) | 2024 / CoRL | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [VoxAct-B: Voxel-Based Acting and Stabilizing Policy for Bimanual Manipulation](../2024/CoRL/2024_CoRL_VoxAct-B-Voxel-Based-Acting-and-Stabilizing-Policy-for-Bim/01_overview.md) | 2024 / CoRL | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [3DS-VLA: A 3D Spatial-Aware Vision Language Action Model for Robust Multi-Task Manipulation](../2025/CoRL/2025_CoRL_3DS-VLA-A-3D-Spatial-Aware-Vision-Language-Action-Model-fo/01_overview.md) | 2025 / CoRL | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [GraspVLA: a Grasping Foundation Model Pre-trained on Billion-scale Synthetic Action Data](../2025/CoRL/2025_CoRL_GraspVLA-a-Grasping-Foundation-Model-Pre-trained-on-Billio/01_overview.md) | 2025 / CoRL | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [Long-VLA: Unleashing Long-Horizon Capability of Vision Language Action Model for Robot Manipulation](../2025/CoRL/2025_CoRL_Long-VLA-Unleashing-Long-Horizon-Capability-of-Vision-Lang/01_overview.md) | 2025 / CoRL | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [RDT-1B: a Diffusion Foundation Model for Bimanual Manipulation](../2025/ICLR/2025_ICLR_RDT-1B-a-Diffusion-Foundation-Model-for-Bimanual-Manipulat/01_overview.md) | 2025 / ICLR | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [AHA: A Vision-Language-Model for Detecting and Reasoning Over Failures in Robotic Manipulation](../2025/ICLR/2025_ICLR_AHA-A-Vision-Language-Model-for-Detecting-and-Reasoning-Ov/01_overview.md) | 2025 / ICLR | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [SIMPACT: Simulation-Enabled Action Planning using Vision-Language Models](../2026/CVPR/2026_CVPR_SIMPACT-Simulation-Enabled-Action-Planning-using-Vision-La/01_overview.md) | 2026 / CVPR | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [Vision-Language Foundation Models as Effective Robot Imitators](../2024/ICLR/2024_ICLR_Vision-Language-Foundation-Models-as-Effective-Robot-Imita/01_overview.md) | 2024 / ICLR | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [Unleashing Large-Scale Video Generative Pre-training for Visual Robot Manipulation](../2024/ICLR/2024_ICLR_Unleashing-Large-Scale-Video-Generative-Pre-training-for-V/01_overview.md) | 2024 / ICLR | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [RoboMamba: Efficient Vision-Language-Action Model for Robotic Reasoning and Manipulation](../2024/NeurIPS/2024_NeurIPS_RoboMamba-Efficient-Vision-Language-Action-Model-for-Robot/01_overview.md) | 2024 / NeurIPS | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [Latent Action Pretraining from Videos](../2025/ICLR/2025_ICLR_Latent-Action-Pretraining-from-Videos/01_overview.md) | 2025 / ICLR | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [3D-VLA: A 3D Vision-Language-Action Generative World Model](../2024/ICML/2024_ICML_3D-VLA-A-3D-Vision-Language-Action-Generative-World-Model/01_overview.md) | 2024 / ICML | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [VLMimic: Vision Language Models are Visual Imitation Learner for Fine-grained Actions](../2024/NeurIPS/2024_NeurIPS_VLMimic-Vision-Language-Models-are-Visual-Imitation-Learne/01_overview.md) | 2024 / NeurIPS | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [MIRAGE: Cross-Embodiment Zero-Shot Policy Transfer with Cross-Painting](../2024/RSS/2024_RSS_MIRAGE-Cross-Embodiment-Zero-Shot-Policy-Transfer-with-Cro/01_overview.md) | 2024 / RSS | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [Pushing the Limits of Cross-Embodiment Learning for Manipulation and Navigation](../2024/RSS/2024_RSS_Pushing-the-Limits-of-Cross-Embodiment-Learning-for-Manipu/01_overview.md) | 2024 / RSS | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [LIBERO-Safety: A Comprehensive Benchmark for Physical and Semantic Safety in Vision-Language-Action Models](../2026/ECCV/2026_ECCV_LIBERO-Safety-A-Comprehensive-Benchmark-for-Physical-and-S/01_overview.md) | 2026 / ECCV | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [DISC: Decoupling Instruction from State-Conditioned Control via Policy Generation](../2026/RSS/2026_RSS_DISC-Decoupling-Instruction-from-State-Conditioned-Control/01_overview.md) | 2026 / RSS | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [How Should Vision-Language-Action Models Use Proprioceptive State?](../2026/arXiv/2026_arXiv_How-Should-Vision-Language-Action-Models-Use-Proprioceptiv/01_overview.md) | 2026 / arXiv | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [Self-Adaptive VLA for Robust Robot Deployment](../2026/arXiv/2026_arXiv_Self-Adaptive-VLA-for-Robust-Robot-Deployment/01_overview.md) | 2026 / arXiv | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [ReViP: Mitigating False Completion in Vision-Language-Action Models with Vision-Proprioception Rebalance](../2026/arXiv/2026_arXiv_ReViP-Mitigating-False-Completion-in-Vision-Language-Actio/01_overview.md) | 2026 / arXiv | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [CoRE-VLA: Towards Scalable and Robust Vision-Language-Action Modeling via Conditional Routing of Experts](../2026/arXiv/2026_arXiv_CoRE-VLA-Towards-Scalable-and-Robust-Vision-Language-Actio/01_overview.md) | 2026 / arXiv | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [CoRe-VLA: Preserving Cross-View Coordination in VLAs under Camera Shifts](../2026/arXiv/2026_arXiv_CoRe-VLA-Preserving-Cross-View-Coordination-in-VLAs-under/01_overview.md) | 2026 / arXiv | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [When would Vision-Proprioception Policies Fail in Robotic Manipulation?](../2026/ICLR/2026_ICLR_When-would-Vision-Proprioception-Policies-Fail-in-Robotic/01_overview.md) | 2026 / ICLR | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [Pretrained Vision-Language-Action Models are Surprisingly Resistant to Forgetting in Continual Learning](../2026/ICML/2026_ICML_Pretrained-Vision-Language-Action-Models-are-Surprisingly/01_overview.md) | 2026 / ICML | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [Actions as Language: Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting](../2026/ICLR/2026_ICLR_Actions-as-Language-Fine-Tuning-VLMs-into-VLAs-Without-Cat/01_overview.md) | 2026 / ICLR | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [LAP: Language-Action Pre-training Enables Zero-Shot Cross-Embodiment Transfer](../2026/RSS/2026_RSS_LAP-Language-Action-Pre-training-Enables-Zero-Shot-Cross-E/01_overview.md) | 2026 / RSS | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [Adaptive Action Chunking at Inference-time for Vision-Language-Action Models](../2026/CVPR/2026_CVPR_Adaptive-Action-Chunking-at-Inference-time-for-Vision-Lang/01_overview.md) | 2026 / CVPR | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [Memory Anchors for Continual Robot Learning](../2026/CoRL/2026_CoRL_Memory-Anchors-for-Continual-Robot-Learning/01_overview.md) | 2026 / CoRL | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [Rethinking Visual-Language-Action Model Scaling: Alignment, Mixture, and Regularization](../2026/arXiv/2026_arXiv_Rethinking-Visual-Language-Action-Model-Scaling-Alignment/01_overview.md) | 2026 / arXiv | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [Can Vision-Language-Action Models Learn from Real-World Data Continually without Forgetting?](../2026/arXiv/2026_arXiv_Can-Vision-Language-Action-Models-Learn-from-Real-World-Da/01_overview.md) | 2026 / arXiv | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [SPACE: Enabling Learning from Cross-Robot Data Toward Generalist Policies](../2026/arXiv/2026_arXiv_SPACE-Enabling-Learning-from-Cross-Robot-Data-Toward-Gener/01_overview.md) | 2026 / arXiv | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [Real-Time Execution of Action Chunking Flow Policies](../2025/NeurIPS/2025_NeurIPS_Real-Time-Execution-of-Action-Chunking-Flow-Policies/01_overview.md) | 2025 / NeurIPS | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [Learning High-Frequency Continuous Action Chunks in Latent Space](../2026/ICML/2026_ICML_Learning-High-Frequency-Continuous-Action-Chunks-in-Latent/01_overview.md) | 2026 / ICML | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [CounterAlign: Counterfactual Supervision for Vision-Language-Action Models](../2026/CoRL/2026_CoRL_CounterAlign-Counterfactual-Supervision-for-Vision-Languag/01_overview.md) | 2026 / CoRL | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [Mechanistic Interpretability for Steering Vision-Language-Action Models](../2025/CoRL/2025_CoRL_Mechanistic-Interpretability-for-Steering-Vision-Language/01_overview.md) | 2025 / CoRL | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [LIBERO-Plus: A Progressive Robustness Benchmark for Visual-Language-Action Models](../2026/CVPR/2026_CVPR_LIBERO-Plus-A-Progressive-Robustness-Benchmark-for-Visual/01_overview.md) | 2026 / CVPR | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [THE COLOSSEUM: A Benchmark for Evaluating Generalization for Robotic Manipulation](../2024/RSS/2024_RSS_THE-COLOSSEUM-A-Benchmark-for-Evaluating-Generalization-fo/01_overview.md) | 2024 / RSS | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [RoboMME: Benchmarking and Understanding Memory for Robotic Generalist Policies](../2026/ICML/2026_ICML_RoboMME-Benchmarking-and-Understanding-Memory-for-Robotic/01_overview.md) | 2026 / ICML | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [Beyond Sight: Finetuning Generalist Robot Policies with Heterogeneous Sensors via Language Grounding](../2025/ICRA/2025_ICRA_Beyond-Sight-Finetuning-Generalist-Robot-Policies-with-Het/01_overview.md) | 2025 / ICRA | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [RoboArena: Distributed Real-World Evaluation of Generalist Robot Policies](../2025/CoRL/2025_CoRL_RoboArena-Distributed-Real-World-Evaluation-of-Generalist/01_overview.md) | 2025 / CoRL | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [A Taxonomy for Evaluating Generalist Robot Manipulation Policies](../2026/RA-L/2026_RA-L_A-Taxonomy-for-Evaluating-Generalist-Robot-Manipulation-Po/01_overview.md) | 2026 / RA-L | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [Gen2Act: Human Video Generation in Novel Scenarios enables Generalizable Robot Manipulation](../2025/CoRL/2025_CoRL_Gen2Act-Human-Video-Generation-in-Novel-Scenarios-enables/01_overview.md) | 2025 / CoRL | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [Mobility VLA: Multimodal Instruction Navigation with Long-Context VLMs and Topological Graphs](../2025/CoRL/2025_CoRL_Mobility-VLA-Multimodal-Instruction-Navigation-with-Long-C/01_overview.md) | 2025 / CoRL | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [Behavior-Skill: A Fine-Grained Benchmark for Evaluating Vision-Language-Action Policies in Long-Horizon Tasks](../2026/arXiv/2026_arXiv_Behavior-Skill-A-Fine-Grained-Benchmark-for-Evaluating-Vis/01_overview.md) | 2026 / arXiv | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [ReSteer: Quantifying and Refining the Steerability of Multitask Robot Policies](../2026/RSS/2026_RSS_ReSteer-Quantifying-and-Refining-the-Steerability-of-Multi/01_overview.md) | 2026 / RSS | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [Causeway: Restoring Task Accessibility for Instruction Switching in VLA Policies](../2026/arXiv/2026_arXiv_Causeway-Restoring-Task-Accessibility-for-Instruction-Swit/01_overview.md) | 2026 / arXiv | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [Do VLAs Really Follow Instructions? Diagnosing How-Level Instruction Following in Vision-Language-Action Models](../2026/arXiv/2026_arXiv_Do-VLAs-Really-Follow-Instructions-Diagnosing-How-Level-In/01_overview.md) | 2026 / arXiv | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [ClevrSkills: Compositional Language And Visual Reasoning in Robotics](../2024/NeurIPS/2024_NeurIPS_ClevrSkills-Compositional-Language-And-Visual-Reasoning-in/01_overview.md) | 2024 / NeurIPS | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [Spa-Bench: A Real-Robot Benchmark for Spatial Grounding in Vision-Language-Action Models](../2026/arXiv/2026_arXiv_Spa-Bench-A-Real-Robot-Benchmark-for-Spatial-Grounding-in/01_overview.md) | 2026 / arXiv | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [RICL: Adding In-Context Adaptability to Pre-Trained Vision-Language-Action Models](../2025/CoRL/2025_CoRL_RICL-Adding-In-Context-Adaptability-to-Pre-Trained-Vision/01_overview.md) | 2025 / CoRL | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [Scaling up Memory for Robotic Control via Experience Retrieval](../2026/ICLR/2026_ICLR_Scaling-up-Memory-for-Robotic-Control-via-Experience-Retri/01_overview.md) | 2026 / ICLR | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [LIBERO-X: Robustness Litmus for Vision-Language-Action Models](../2026/RSS/2026_RSS_LIBERO-X-Robustness-Litmus-for-Vision-Language-Action-Mode/01_overview.md) | 2026 / RSS | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [Learning Native Continuation for Action Chunking Flow Policies](../2026/RSS/2026_RSS_Learning-Native-Continuation-for-Action-Chunking-Flow-Poli/01_overview.md) | 2026 / RSS | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [Stable Language Guidance for Vision–Language–Action Models](../2026/ACL/2026_ACL_Stable-Language-Guidance-for-VisionLanguageAction-Models/01_overview.md) | 2026 / ACL | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [Self-Improving Vision-Language-Action Models with Data Generation via Residual RL](../2026/ICLR/2026_ICLR_Self-Improving-Vision-Language-Action-Models-with-Data-Gen/01_overview.md) | 2026 / ICLR | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [Object-Centric Residual RL for Zero-Shot Sim-to-Real VLA Enhancement](../2026/CoRL/2026_CoRL_Object-Centric-Residual-RL-for-Zero-Shot-Sim-to-Real-VLA-E/01_overview.md) | 2026 / CoRL | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [EXPO-FT: Sample-Efficient Reinforcement Learning Finetuning for Vision-Language-Action Models](../2026/CoRL/2026_CoRL_EXPO-FT-Sample-Efficient-Reinforcement-Learning-Finetuning/01_overview.md) | 2026 / CoRL | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [Beyond Appearance Shifts: Task-Semantic Action Calibration for VLA Models](../2026/NeurIPS/2026_NeurIPS_Beyond-Appearance-Shifts-Task-Semantic-Action-Calibration/01_overview.md) | 2026 / NeurIPS | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models](../2026/NeurIPS/2026_NeurIPS_Not-All-Features-Are-Created-Equal-A-Mechanistic-Study-of/01_overview.md) | 2026 / NeurIPS | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [Embodied Interpretability: Linking Causal Understanding to Generalization in Vision-Language-Action Models](../2026/ICML/2026_ICML_Embodied-Interpretability-Linking-Causal-Understanding-to/01_overview.md) | 2026 / ICML | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models](../2025/arXiv/2025_arXiv_RobustVLA-Robustness-Aware-Reinforcement-Post-Training-for/01_overview.md) | 2025 / arXiv | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [CHORUS: Decentralized Multi-Embodiment Collaboration with One VLA Policy](../2026/arXiv/2026_arXiv_CHORUS-Decentralized-Multi-Embodiment-Collaboration-with-O/01_overview.md) | 2026 / arXiv | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [Cooperative Multi-Agent Vision-Language-Action Models via Reinforced Fine Tuning](../2026/arXiv/2026_arXiv_Cooperative-Multi-Agent-Vision-Language-Action-Models-via/01_overview.md) | 2026 / arXiv | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [RA-VLA: Retrieval-Augmented VLA for Test-Time Adaptation](../2026/ICML/2026_ICML_RA-VLA-Retrieval-Augmented-VLA-for-Test-Time-Adaptation/01_overview.md) | 2026 / ICML | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [When Does Retrieval Help? A Study of In-Context Adaptation in Vision-Language-Action Models](../2026/arXiv/2026_arXiv_When-Does-Retrieval-Help-A-Study-of-In-Context-Adaptation/01_overview.md) | 2026 / arXiv | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [Beyond Reconstruction: What Matters in Action Tokenization for Robot Policies?](../2026/arXiv/2026_arXiv_Beyond-Reconstruction-What-Matters-in-Action-Tokenization/01_overview.md) | 2026 / arXiv | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [LongNav-R1: Horizon-Adaptive Multi-Turn RL for Long-Horizon VLA Navigation](../2026/RSS/2026_RSS_LongNav-R1-Horizon-Adaptive-Multi-Turn-RL-for-Long-Horizon/01_overview.md) | 2026 / RSS | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [Visual Verification Enables Inference-time Steering and Autonomous Policy Improvement](../2026/RSS/2026_RSS_Visual-Verification-Enables-Inference-time-Steering-and-Au/01_overview.md) | 2026 / RSS | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [Towards Long-Lived Robots: Continual Learning VLA Models via Reinforcement Fine-Tuning](../2026/RSS/2026_RSS_Towards-Long-Lived-Robots-Continual-Learning-VLA-Models-vi/01_overview.md) | 2026 / RSS | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [LDA-1B: Scaling Latent Dynamics Action Model via Universal Embodied Data Ingestion](../2026/RSS/2026_RSS_LDA-1B-Scaling-Latent-Dynamics-Action-Model-via-Universal/01_overview.md) | 2026 / RSS | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [ControlVLA: Few-shot Object-centric Adaptation for Pre-trained Vision-Language-Action Models](../2025/CoRL/2025_CoRL_ControlVLA-Few-shot-Object-centric-Adaptation-for-Pre-trai/01_overview.md) | 2025 / CoRL | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models](../2026/CVPR/2026_CVPR_SRPO-Self-Referential-Policy-Optimization-for-Vision-Langu/01_overview.md) | 2026 / CVPR | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [Joint-Aligned Latent Action: Towards Scalable VLA Pretraining in the Wild](../2026/CVPR/2026_CVPR_Joint-Aligned-Latent-Action-Towards-Scalable-VLA-Pretraini/01_overview.md) | 2026 / CVPR | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [RehearseVLA: Simulated Post-Training for VLAs with Physically-Consistent World Model](../2026/CVPR/2026_CVPR_RehearseVLA-Simulated-Post-Training-for-VLAs-with-Physical/01_overview.md) | 2026 / CVPR | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [Contrast Sets for Evaluating Language-Guided Robot Policies](../2024/CoRL/2024_CoRL_Contrast-Sets-for-Evaluating-Language-Guided-Robot-Policie/01_overview.md) | 2024 / CoRL | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [Fast-ThinkAct: Efficient Vision-Language-Action Reasoning via Verbalizable Latent Planning](../2026/CVPR/2026_CVPR_Fast-ThinkAct-Efficient-Vision-Language-Action-Reasoning-v/01_overview.md) | 2026 / CVPR | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [MM-ACT: Learn from Multimodal Parallel Generation to Act](../2026/CVPR/2026_CVPR_MM-ACT-Learn-from-Multimodal-Parallel-Generation-to-Act/01_overview.md) | 2026 / CVPR | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [EvoVLA: Self-evolving Vision-Language-Action Model](../2026/ECCV/2026_ECCV_EvoVLA-Self-evolving-Vision-Language-Action-Model/01_overview.md) | 2026 / ECCV | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [Restoring Linguistic Grounding in VLA Models via Train-Free Attention Recalibration](../2026/ECCV/2026_ECCV_Restoring-Linguistic-Grounding-in-VLA-Models-via-Train-Fre/01_overview.md) | 2026 / ECCV | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [VLA-R1: Enhancing Reasoning in Vision-Language-Action Models](../2026/ECCV/2026_ECCV_VLA-R1-Enhancing-Reasoning-in-Vision-Language-Action-Model/01_overview.md) | 2026 / ECCV | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [MobileVLA-R1: Reinforcing Vision-Language-Action for Mobile Robots](../2026/ECCV/2026_ECCV_MobileVLA-R1-Reinforcing-Vision-Language-Action-for-Mobile/01_overview.md) | 2026 / ECCV | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [Scaling Verification Can Be More Effective than Scaling Policy Learning for Vision-Language-Action Alignment](../2026/ECCV/2026_ECCV_Scaling-Verification-Can-Be-More-Effective-than-Scaling-Po/01_overview.md) | 2026 / ECCV | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [GRAD-NAV++: Vision-Language Model Enabled Visual Drone Navigation With Gaussian Radiance Fields and Differentiable Dynamics](../2026/RA-L/2026_RA-L_GRAD-NAV%2B%2B-Vision-Language-Model-Enabled-Visual-Drone-Navi/01_overview.md) | 2026 / RA-L | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [TacCoRL: Integrating Tactile Feedback into VLA via Simulation](../2026/arXiv/2026_arXiv_TacCoRL-Integrating-Tactile-Feedback-into-VLA-via-Simulati/01_overview.md) | 2026 / arXiv | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [CompVLA: A Variable Compliance Vision-Language-Action Model for Contact-rich Manipulation](../2026/arXiv/2026_arXiv_CompVLA-A-Variable-Compliance-Vision-Language-Action-Model/01_overview.md) | 2026 / arXiv | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [TORL-VLA: Tactile Guided Online Reinforcement Learning for Contact-Rich Manipulation](../2026/arXiv/2026_arXiv_TORL-VLA-Tactile-Guided-Online-Reinforcement-Learning-for/01_overview.md) | 2026 / arXiv | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [ForceRFT: Refining VLA Actions through Force-Guided Residual Reinforcement Learning](../2026/arXiv/2026_arXiv_ForceRFT-Refining-VLA-Actions-through-Force-Guided-Residua/01_overview.md) | 2026 / arXiv | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [Facet-0: A Robotic Foundation Model for Contact-Rich Precise Manipulation](../2026/arXiv/2026_arXiv_Facet-0-A-Robotic-Foundation-Model-for-Contact-Rich-Precis/01_overview.md) | 2026 / arXiv | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [πRL: Online RL Fine-tuning for Flow-based Vision-Language-Action Models](../2025/arXiv/2025_arXiv_piRL-Online-RL-Fine-tuning-for-Flow-based-Vision-Language/01_overview.md) | 2025 / arXiv | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [Breaking Lock-In: Preserving Steerability under Low-Data VLA Post-Training](../2026/arXiv/2026_arXiv_Breaking-Lock-In-Preserving-Steerability-under-Low-Data-VL/01_overview.md) | 2026 / arXiv | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [TEMPO: Semantic-Action Decoupled RL Post-Training for Vision-Language-Action Models](../2026/arXiv/2026_arXiv_TEMPO-Semantic-Action-Decoupled-RL-Post-Training-for-Visio/01_overview.md) | 2026 / arXiv | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [When Vision Overrides Language: Evaluating and Mitigating Counterfactual Failures in VLAs](../2026/arXiv/2026_arXiv_When-Vision-Overrides-Language-Evaluating-and-Mitigating-C/01_overview.md) | 2026 / arXiv | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [Trajectory-Level Continuous Action Representation for Robotic Manipulation](../2026/ECCV/2026_ECCV_Trajectory-Level-Continuous-Action-Representation-for-Robo/01_overview.md) | 2026 / ECCV | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [Is Your Robot's Memory Just a Clock? Temporal Shortcuts in Memory-Augmented VLA Policies](../2026/arXiv/2026_arXiv_Is-Your-Robot-s-Memory-Just-a-Clock-Temporal-Shortcuts-in/01_overview.md) | 2026 / arXiv | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [Act2Goal: From World Model To General Goal-conditioned Policy](../2026/RSS/2026_RSS_Act2Goal-From-World-Model-To-General-Goal-conditioned-Poli/01_overview.md) | 2026 / RSS | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [AC2-VLA: Action-Context-Aware Adaptive Computation in Vision-Language-Action Models for Efficient Robotic Manipulation](../2026/IJCAI/2026_IJCAI_AC2-VLA-Action-Context-Aware-Adaptive-Computation-in-Visio/01_overview.md) | 2026 / IJCAI | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [WCM: A World Critic Model for Vision-Language-Action Reinforcement Learning](../2026/arXiv/2026_arXiv_WCM-A-World-Critic-Model-for-Vision-Language-Action-Reinfo/01_overview.md) | 2026 / arXiv | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [Reinforcement Learning for Real-Time Vision-Language-Action Policies](../2026/arXiv/2026_arXiv_Reinforcement-Learning-for-Real-Time-Vision-Language-Actio/01_overview.md) | 2026 / arXiv | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [RoboAlign: Learning Test-Time Reasoning for Language-Action Alignment in Vision-Language-Action Models](../2026/arXiv/2026_arXiv_RoboAlign-Learning-Test-Time-Reasoning-for-Language-Action/01_overview.md) | 2026 / arXiv | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [STARE-VLA: Progressive Stage-Aware Reinforcement for Fine-Tuning Vision-Language-Action Models](../2025/arXiv/2025_arXiv_STARE-VLA-Progressive-Stage-Aware-Reinforcement-for-Fine-T/01_overview.md) | 2025 / arXiv | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [Ψ₀: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation](../2026/RSS/2026_RSS_An-Open-Foundation-Model-Towards-Universal-Humanoid-Loco-M/01_overview.md) | 2026 / RSS | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [Universal Pose Pretraining for Generalizable Vision-Language-Action Policies](../2026/RSS/2026_RSS_Universal-Pose-Pretraining-for-Generalizable-Vision-Langua/01_overview.md) | 2026 / RSS | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [GeoPredict: Leveraging Predictive Kinematics and 3D Gaussian Geometry for Precise VLA Manipulation](../2026/CVPR/2026_CVPR_GeoPredict-Leveraging-Predictive-Kinematics-and-3D-Gaussia/01_overview.md) | 2026 / CVPR | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver](../2026/AAAI/2026_AAAI_ReconVLA-Reconstructive-Vision-Language-Action-Model-as-Ef/01_overview.md) | 2026 / AAAI | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [StructRL: Structured Action-Space Exploration for Flow-Based VLAs](../2026/arXiv/2026_arXiv_StructRL-Structured-Action-Space-Exploration-for-Flow-Base/01_overview.md) | 2026 / arXiv | `UNREAD` | `ABSTRACT_CHECKED` |
| NEXT | [SaPaVe: Towards Active Perception and Manipulation in Vision-Language Action Models for Robotics](../2026/CVPR/2026_CVPR_SaPaVe-Towards-Active-Perception-and-Manipulation-in-Visio/01_overview.md) | 2026 / CVPR | `UNREAD` | `FULL_TEXT_CHECKED` |
| NEXT | [Look Before You Act: Bridging Active Perception and Vision-Language-Action Models via Observation-Aligned Data Adaptation](../2026/arXiv/2026_arXiv_Look-Before-You-Act-Bridging-Active-Perception-and-Vision/01_overview.md) | 2026 / arXiv | `UNREAD` | `ABSTRACT_CHECKED` |

<!-- READING_QUEUE:END -->

## Historical curation — 2026-09-02

아래는 해당 날짜의 변경 이력이다. 현재 membership과 수량은 위 generated queue를 따른다.

`ReKep`, `VoxAct-B`, `3DS-VLA`, `GraspVLA`, `Long-VLA`, `RDT-1B`, `AHA`를 `REFERENCE→NEXT`로, `SIMPACT`를 `ARCHIVE→NEXT`로 반영했다. 새 queue는 spatial/action representation, bimanual and long-horizon execution, grasp pretraining, failure reasoning, simulation-in-loop planning을 VLA의 실제 robot interface 관점에서 비교한다.

## Comparison Matrix

> Matrix maturity: `CURATION-SEED`. 아래는 읽기 전 비교 가설이며 `READ`를 의미하지 않는다. `Paper` 링크는 local overview를 가리키고, official paper/project/code URL은 해당 note header에서 확인한다.
>
> Row convention: 한 행은 한 registry paper이다. `State / action / objective / timing`은 고정 순서로 기록하고, `Evaluation`은 `setup; data/split; metric; real/trials` 순서를 따른다. `Evidence / source`가 `CURATION-SEED`이면 수치나 세부 조건을 아직 주장하지 않는다.

| Paper | Year / Venue | Role | Facets | Problem | State / action / objective / timing | Why included / TL;DR | Evaluation (setup; data/split; metric; real/trials) | Evidence / source | Failure / assumption | Reusable idea |
|---|---|---|---|---|---|---|---|---|---|---|
| [Gato](../2022/arXiv/2022_arXiv_A-Generalist-Agent/01_overview.md) | 2022 / arXiv | foundation; generalist policy | multi-domain; text+vision+control; sim/real; autoregressive tokens | one transformer across heterogeneous modalities and tasks | context-window serialized state; shared discrete/continuous action tokens; next-token objective; domain-dependent loop | observation/action serialization을 generalist policy의 설계 변수로 만든 기준점 | multi-domain and robot arm tasks; data/split=UNVERIFIED; metric=task/control performance; real/sim=UNVERIFIED/trials=UNVERIFIED | `CURATION-SEED`; overview + queue | mixture interference, token precision, specialist gap | tokenization과 action precision을 분리 |
| [AutoRT](../2024/arXiv/2024_arXiv_AutoRT-Embodied-Foundation-Models-for-Large-Scale-Orchestr/01_overview.md) | 2024 / arXiv | data engine; system | multi-robot; language+scene; real; task orchestration | foundation-model task proposal and robot-fleet orchestration | scene/task/safety context; language task selection and policy invocation; data-collection objective; task timescale | policy quality와 data-engine task selection을 분리하는 system 기준 | multi-robot collection; data/split=UNVERIFIED; metric=deployment/data yield; real=yes/trials=UNVERIFIED | `CURATION-SEED`; overview + queue | hallucinated/unsafe tasks, oversight, policy coverage | data collection을 policy evaluation과 분리 |
| [RT-1](../2022/arXiv/2022_arxiv_RT-1-Robotics-Transformer-for-Real-World-Control-at-Scale/01_overview.md) | 2022 / arXiv | foundation; policy | arm; image+language; real; action tokens | scalable image-language-conditioned robot control | implicit visual state; discretized action sequence; behavior cloning; chunked closed loop | transformer policy scaling과 real-robot data의 기준점 | multi-task manipulation; data/split=task/object generalization; metric=success/robustness; real=yes/trials=UNVERIFIED | `CURATION-SEED`; overview + queue | tokenization, data concentration, recovery | action tokenization과 recovery를 별도 측정 |
| [Open X-Embodiment](../2024/ICRA/2024_ICRA_Open-X-Embodiment-Robotic-Learning-Datasets-and-RT-X-Model/01_overview.md) | 2024 / ICRA | dataset; foundation | heterogeneous robots; multimodal; real; data scaling | shared learning substrate across robot datasets | embodiment-dependent observations; normalized action interface; cross-dataset pretraining; chunked policy loop | heterogeneous data와 action normalization을 비교하는 dataset 기준 | multi-dataset robot tasks; data/split=dataset/task splits; metric=transfer/success; real=yes/trials=UNVERIFIED | `CURATION-SEED`; overview + queue | embodiment imbalance, inconsistent action semantics, data attribution | data mixture와 adapter 효과를 분리 |
| [Octo](../2024/RSS/2024_RSS_Octo-An-Open-Source-Generalist-Robot-Policy/01_overview.md) | 2024 / RSS | policy; foundation | heterogeneous robots; multimodal; real/sim; generalist policy | open generalist policy conditioned on diverse robot data | multimodal observations with adapters; shared action interface; behavior cloning/pretraining; policy chunks | open-weight generalist policy의 reproducible 기준점 | downstream manipulation; data/split=task/embodiment splits; metric=success/transfer; real/sim=UNVERIFIED/trials=UNVERIFIED | `CURATION-SEED`; overview + queue | embodiment adapter, data mixture, short horizon | shared interface와 adaptation을 분리 |
| [OpenVLA](../2024/CoRL/2024_CoRL_OpenVLA-An-Open-Source-Vision-Language-Action-Model/01_overview.md) | 2024 / CoRL | policy; foundation | arm; vision+language; real/sim; autoregressive action | open VLA for robot manipulation | pretrained VLM features and robot observation; action tokens; pretrain/fine-tune objective; chunked execution | open baseline에서 success와 reproducibility를 비교 | manipulation; data/split=task/embodiment splits; metric=success; real/sim=UNVERIFIED/trials=UNVERIFIED | `CURATION-SEED`; overview + queue | fine-tuning recipe, action tokenization, contact feedback | open baseline protocol 고정 |
| [OpenVLA-OFT](../2025/RSS/2025_RSS_Fine-Tuning-Vision-Language-Action-Models-Optimizing-Speed/01_overview.md) | 2025 / RSS | method; deployment | arm; vision+language; real; action decoding | deployment-oriented VLA fine-tuning for faster inference | VLM features and robot observations; continuous/parallel action decoding; fine-tuning objective; lower-latency loop | inference speed와 task success의 trade-off를 드러내는 extension | manipulation; data/split=downstream tasks; metric=success/latency; real=UNVERIFIED/trials=UNVERIFIED | `CURATION-SEED`; overview + queue | recipe confound, speed-quality trade-off, hardware dependence | latency를 architecture와 분리 |
| [π0](../2025/RSS/2025_RSS_pi0-A-Vision-Language-Action-Flow-Model-for-General-Robot/01_overview.md) | 2025 / RSS | foundation; policy | heterogeneous robots; image+language+proprioception; real; flow action chunks | flow-based generalist robot action generation | multimodal context; continuous flow action chunk; flow matching objective; chunked closed loop | action representation과 heterogeneous embodiment를 연결하는 current reference | dexterous/manipulation tasks; data/split=task/embodiment splits; metric=success/transfer; real=yes/trials=UNVERIFIED | `CURATION-SEED`; overview + queue | chunk latency, data imbalance, contact feedback | flow action과 feedback rate를 함께 평가 |
| [FAST](../2025/RSS/2025_RSS_FAST-Efficient-Action-Tokenization-for-Vision-Language-Act/01_overview.md) | 2025 / RSS | method; action representation | robot; action sequence; real/sim; tokenization | efficient action tokenization for VLA inference | action sequence; compressed frequency-aware tokens; token prediction objective; high-rate decoding | action compression이 control frequency를 바꾸는 지점 | robot manipulation; data/split=UNVERIFIED; metric=latency/success; real/sim=UNVERIFIED/trials=UNVERIFIED | `CURATION-SEED`; overview + queue | compression discards transients, codec dependence, latency | token budget과 contact feedback을 함께 기록 |
| [RT-H](../2024/Robotics-Science-and-Sys/2024_Robotics-Science-and-Sys_RT-H-Action-Hierarchies-Using-Language/01_overview.md) | 2024 / Robotics: Science and Systems | policy; hierarchy | arm; image+language; real; hierarchical action | language-conditioned policy with intermediate motion layer | visual/instruction state; language motion command to robot action; hierarchical imitation; high-level plus action loop | language-to-motion command contract을 명시한 hierarchy 기준 | real manipulation; data/split=UNVERIFIED; metric=generalization/intervention; real=yes/trials=UNVERIFIED | `CURATION-SEED`; overview + queue | hierarchy granularity, ambiguity, latency | high-level semantic command와 low-level action 분리 |
| [Gemini Robotics](../2025/arXiv/2025_arXiv_Gemini-Robotics-Bringing-AI-into-the-Physical-World/01_overview.md) | 2025 / arXiv | foundation; system | multiple robots; multimodal; real; embodied reasoning | proprietary embodied reasoning and action family | multimodal semantic and robot state; dexterous action; pretraining/adaptation; deployment loop UNVERIFIED | closed foundation policy의 embodiment adaptation reference | cross-task/embodiment tasks; data/split=UNVERIFIED; metric=task success/transfer; real=UNVERIFIED/trials=UNVERIFIED | `CURATION-SEED`; overview + queue | reproducibility, data attribution, contact feedback, controller dependence | closed model과 open baseline의 protocol 분리 |
| [GR00T N1](../2025/arXiv/2025_arXiv_NVIDIA-Isaac-GR00T-N1-An-Open-Foundation-Model-for-Humanoi/01_overview.md) | 2025 / arXiv | foundation; policy | humanoid; multimodal; sim/real; action chunks | open-weight humanoid foundation policy | humanoid state and multimodal context; action chunk; pretraining/adaptation; controller-dependent loop | humanoid를 VLA embodiment와 whole-body interface로 연결 | humanoid tasks; data/split=UNVERIFIED; metric=task/transfer; real/sim=UNVERIFIED/trials=UNVERIFIED | `CURATION-SEED`; overview + queue | hardware/controller dependence, contact feedback, data coverage | embodiment adaptation contract을 고정 |
| [VoxPoser](../2023/CoRL/2023_CoRL_VoxPoser-Composable-3D-Value-Maps-for-Robotic-Manipulation/01_overview.md) | 2023 / CoRL | planner; system | arm; vision+language+3D; real/sim; planner-level | language-guided spatial manipulation through composable value maps | scene and language state; executable motion targets; prompted composition; planner timescale | VLA 위 explicit spatial value/planning layer의 기준 | manipulation tasks; data/split=task prompts; metric=task completion; real/sim=UNVERIFIED/trials=UNVERIFIED | `CURATION-SEED`; overview + queue | perception/value-map error, open-loop execution | semantic plan과 low-level controller를 분리 |
| [SayPlan](../2023/CoRL/2023_CoRL_SayPlan-Grounding-Large-Language-Models-using-3D-Scene-Gra/01_overview.md) | 2023 / CoRL | planner; system | mobile/manipulator; language+3D graph; real/sim; long-horizon | language planning grounded in 3D scene graphs | scene graph and instruction; skill/action plan; prompted planning; long-horizon replanning | language reasoning과 executable spatial plan의 interface | long-horizon manipulation/navigation; data/split=task scenes; metric=completion/plan validity; real/sim=UNVERIFIED/trials=UNVERIFIED | `CURATION-SEED`; overview + queue | predicate error, plan-execution gap, open-loop drift | scene graph와 action execution을 별도 평가 |
| [π0.5](../2025/CoRL/2025_CoRL_pi0.5-a-Vision-Language-Action-Model-with-Open-World-Gener/01_overview.md) | 2025 / CoRL | policy; foundation | heterogeneous robots; multimodal; real; long-horizon VLA | open-world generalist policy and task composition | multimodal context and robot state; continuous/chunked action; heterogeneous co-training; long-horizon loop | π0에서 open-world hierarchy와 generalization으로 확장된 frontier | open-world manipulation; data/split=task/embodiment splits; metric=generalization/success; real=yes/trials=UNVERIFIED | `CURATION-SEED`; overview + queue | recovery/contact robustness, data attribution, hierarchy | high-level behavior context와 action chunk를 분리 |


## Dependency and Evolution

아래 표는 VLA를 하나의 architecture 계보가 아니라 data, representation, planning과 feedback interface의 결합으로 읽기 위한 지도다. 직접 citation 관계는 정독 시 확인한다.

### Relation type index

아래 label은 바로 다음 계보 표의 chain anchor에 적용한다. `formulation`, `method`, `data`, `evaluation`, `deployment`는 개념적 연결의 종류이며 citation 또는 직접 영향 관계를 뜻하지 않는다.

| Chain anchor | Relation type | Interpretation |
|---|---|---|
| multimodal sequence modeling → Gato → PaLM-E/RT-2 → Gemini Robotics | foundation → policy → deployment | shared modality가 embodied reasoning/action으로 확장 |
| MPO → MT-Opt → AutoRT → RT/Open-X ecosystem | optimization → data engine → deployment | policy improvement가 fleet data와 task orchestration으로 확장 |
| DAgger → RoboMimic/BC-Z → RT-1 → Open X/Octo/OpenVLA | data collection → policy/data scaling | imitation data가 multi-task·cross-embodiment policy로 확장 |
| CLIP/CLIPort → PaLM-E/RT-2 → π0 → π0.5 | representation → action interface → deployment | language-vision prior가 flow action과 open-world control로 확장 |
| DDPM/Flow Matching → Diffusion Policy/π0 → FAST | generative formulation → action representation → deployment | action generation이 chunk compression과 inference efficiency로 확장 |
| OpenVLA → OpenVLA-OFT | policy → deployment | autoregressive baseline이 lower-latency execution으로 확장 |
| RT-1/RT-2 → RT-H | flat action → hierarchy/interface | intermediate language-motion concept이 action hierarchy로 연결 |
| Open X-Embodiment/generalist policy → GR00T N1 | data scaling → embodiment adaptation | heterogeneous data가 humanoid action interface로 특화 |
| Inner Monologue/VoxPoser/SayPlan → AtomicVLA/PALM/MomaGraph | planner → skill/memory interface | external planning이 atomic skill, progress, persistent memory로 이동 |
| PointNet → RVT/SUGAR → PointVLA/Any3D/ActiveVLA → AVA-VLA | representation → active policy | 3D input이 action-conditioned perception으로 확장 |
| generalist VLA → SAFE → FLARE/FaultEval | evaluation → safety/recovery interface | alert가 diagnosis·correction protocol로 확장 |
| spatial memory → retrieval/HALO | memory → deployment | persistent state가 task-relevant retrieval로 정리 |
| generalist benchmarks → LIBERO/CALVIN/FurnitureBench → VLA-Arena | benchmark → evaluation | clean success가 stress·safety·long-horizon evaluation으로 확장 |

| Foundation → transition → frontier | 계승·변화 | 아직 확인할 경계 |
|---|---|---|
| multimodal sequence modeling → [Gato](../2022/arXiv/2022_arXiv_A-Generalist-Agent/01_overview.md) → [PaLM-E](../2023/ICML/2023_ICML_PaLM-E-An-Embodied-Multimodal-Language-Model/01_overview.md) / [RT-2](../2023/CoRL/2023_CoRL_RT-2-Vision-Language-Action-Models-Transfer-Web-Knowledge/01_overview.md) → [Gemini Robotics](../2025/arXiv/2025_arXiv_Gemini-Robotics-Bringing-AI-into-the-Physical-World/01_overview.md) | heterogeneous modality/action tokenization에서 embodied multimodal representation, web knowledge transfer와 dedicated embodied reasoning/action model로 확장된다. | broad semantic competence가 contact precision, latency와 recovery competence로 전달되는가 |
| [MPO](../2018/ICLR/2018_ICLR_Maximum-a-Posteriori-Policy-Optimisation/01_overview.md) → [MT-Opt](../2021/arXiv/2021_arXiv_MT-Opt-Continuous-Multi-Task-Robotic-Reinforcement-Learnin/01_overview.md) → [AutoRT](../2024/arXiv/2024_arXiv_AutoRT-Embodied-Foundation-Models-for-Large-Scale-Orchestr/01_overview.md) → RT/Open-X data ecosystem | off-policy multi-task improvement에서 robot-fleet data sharing과 foundation-model-based task orchestration으로 확장된다. | task proposer, safety filter, behavior policy와 data mixture 중 downstream VLA gain을 무엇이 만드는가 |
| [DAgger](../2011/AISTATS/2011_AISTATS_A-Reduction-of-Imitation-Learning-and-Structured-Predictio/01_overview.md) → [RoboMimic](../2021/CoRL/2021_CoRL_What-Matters-in-Learning-from-Offline-Human-Demonstrations/01_overview.md) / [BC-Z](../2022/CoRL/2022_CoRL_BC-Z-Zero-Shot-Task-Generalization-with-Robotic-Imitation/01_overview.md) → [RT-1](../2022/arXiv/2022_arxiv_RT-1-Robotics-Transformer-for-Real-World-Control-at-Scale/01_overview.md) → [Open X-Embodiment](../2024/ICRA/2024_ICRA_Open-X-Embodiment-Robotic-Learning-Datasets-and-RT-X-Model/01_overview.md) / [Octo](../2024/RSS/2024_RSS_Octo-An-Open-Source-Generalist-Robot-Policy/01_overview.md) / [OpenVLA](../2024/CoRL/2024_CoRL_OpenVLA-An-Open-Source-Vision-Language-Action-Model/01_overview.md) | reproducible imitation learning에서 language-conditioned multi-task data, 대규모 transformer policy와 cross-embodiment pretraining으로 확장된다. | data volume, web prior, action interface와 embodiment adaptation의 기여를 분리할 수 있는가 |
| [CLIP](../2021/ICML/2021_ICML_Learning-Transferable-Visual-Models-From-Natural-Language/01_overview.md) / [CLIPort](../2021/CoRL/2021_CoRL_CLIPort-What-and-Where-Pathways-for-Robotic-Manipulation/01_overview.md) → [PaLM-E](../2023/ICML/2023_ICML_PaLM-E-An-Embodied-Multimodal-Language-Model/01_overview.md) / [RT-2](../2023/CoRL/2023_CoRL_RT-2-Vision-Language-Action-Models-Transfer-Web-Knowledge/01_overview.md) → [π0](../2025/RSS/2025_RSS_pi0-A-Vision-Language-Action-Flow-Model-for-General-Robot/01_overview.md) → [π0.5](../2025/CoRL/2025_CoRL_pi0.5-a-Vision-Language-Action-Model-with-Open-World-Gener/01_overview.md) | language–vision representation을 spatial manipulation과 embodied token에 연결하고, flow-matching action expert와 heterogeneous co-training을 long-horizon open-world deployment로 확장한다. | semantic generalization이 precise control, contact와 recovery에 실제로 전달되는가 |
| [DDPM](../2020/NeurIPS/2020_NeurIPS_Denoising-Diffusion-Probabilistic-Models/01_overview.md) / [Flow Matching](../2023/ICLR/2023_ICLR_Flow-Matching-for-Generative-Modeling/01_overview.md) → [Diffusion Policy](../2023/RSS/2023_RSS_Diffusion-Policy-Visuomotor-Policy-Learning-via-Action-Dif/01_overview.md) / π0 → [FAST](../2025/RSS/2025_RSS_FAST-Efficient-Action-Tokenization-for-Vision-Language-Act/01_overview.md) | continuous action generation과 action chunking에서 시작해, 고주파 action sequence의 압축 tokenization으로 inference 및 학습 효율을 개선한다. | token compression이 빠른 feedback와 contact discontinuity를 얼마나 보존하는가 |
| [OpenVLA](../2024/CoRL/2024_CoRL_OpenVLA-An-Open-Source-Vision-Language-Action-Model/01_overview.md) → [OpenVLA-OFT](../2025/RSS/2025_RSS_Fine-Tuning-Vision-Language-Action-Models-Optimizing-Speed/01_overview.md) | 범용 autoregressive action prediction을 parallel decoding, continuous action representation과 fine-tuning recipe로 바꾸어 deployment speed와 success를 높인다. | 효율 개선이 unseen embodiment와 long-horizon recovery에서도 유지되는가 |
| [RT-1](../2022/arXiv/2022_arxiv_RT-1-Robotics-Transformer-for-Real-World-Control-at-Scale/01_overview.md) / [RT-2](../2023/CoRL/2023_CoRL_RT-2-Vision-Language-Action-Models-Transfer-Web-Knowledge/01_overview.md) → [RT-H](../2024/Robotics-Science-and-Sys/2024_Robotics-Science-and-Sys_RT-H-Action-Hierarchies-Using-Language/01_overview.md) | flat token/action prediction에 intermediate language motion concept을 넣어 action hierarchy와 human correction interface를 만든다. | language option이 실제 contact phase, termination과 recoverability를 충분히 구분하는가 |
| Open X-Embodiment/generalist action policy → [GR00T N1](../2025/arXiv/2025_arXiv_NVIDIA-Isaac-GR00T-N1-An-Open-Foundation-Model-for-Humanoi/01_overview.md) | heterogeneous robot-data pretraining을 humanoid bimanual action과 embodiment adaptation에 특화한다. | high-level VLA와 locomotion/whole-body controller 사이의 state, rate와 safety contract가 공개·재현 가능한가 |
| [Inner Monologue](../2022/CoRL/2022_CoRL_Inner-Monologue-Embodied-Reasoning-through-Planning-with-L/01_overview.md) / [VoxPoser](../2023/CoRL/2023_CoRL_VoxPoser-Composable-3D-Value-Maps-for-Robotic-Manipulation/01_overview.md) / [SayPlan](../2023/CoRL/2023_CoRL_SayPlan-Grounding-Large-Language-Models-using-3D-Scene-Gra/01_overview.md) → [AtomicVLA](../2026/CVPR/2026_CVPR_AtomicVLA-Unlocking-the-Potential-of-Atomic-Skill-Learning/01_overview.md) / [PALM](../2026/CVPR/2026_CVPR_PALM-Progress-Aware-Policy-Learning-via-Affordance-Reasoni/01_overview.md) / [MomaGraph](../2026/ICLR/2026_ICLR_MomaGraph-State-Aware-Unified-Scene-Graphs-with-Vision-Lan/01_overview.md) | 외부 language planner와 spatial affordance interface에서 atomic skill, progress state와 persistent scene graph를 내부화하는 방향으로 이동한다. | plan correctness와 execution progress가 contact-level feedback으로 닫히는가 |
| [PointNet](../2017/CVPR/2017_CVPR_PointNet-Deep-Learning-on-Point-Sets-for-3D-Classification/01_overview.md) → [RVT](../2023/CoRL/2023_CoRL_RVT-Robotic-View-Transformer-for-3D-Object-Manipulation/01_overview.md) / [SUGAR](../2024/CVPR/2024_CVPR_SUGAR-Pre-training-3D-Visual-Representations-for-Robotics/01_overview.md) → [PointVLA](../2026/RA-L/2026_RA-L_PointVLA-Injecting-the-3D-World-into-Vision-Language-Actio/01_overview.md) / [Any3D-VLA](../2026/ICML/2026_ICML_Any3D-VLA-Enhancing-VLA-Robustness-via-Diverse-Point-Cloud/01_overview.md) / [ActiveVLA](../2026/CVPR/2026_CVPR_ActiveVLA-Injecting-Active-Perception-into-Vision-Language/01_overview.md) → [AVA-VLA](../2026/CVPR/2026_CVPR_AVA-VLA-Improving-Vision-Language-Action-Models-with-Activ/01_overview.md) | generic point-set encoding에서 manipulation-specific 3D pretraining, VLA input augmentation, action-conditioned view selection과 recurrent active attention으로 확장된다. | 추가 3D input·active attention의 이득이 geometry, sensor coverage, memory 또는 data augmentation 중 어디에서 오는가 |
| generalist VLA → [SAFE](../2025/NeurIPS/2025_NeurIPS_SAFE-Multitask-Failure-Detection-for-Vision-Language-Actio/01_overview.md) → [FLARE](../2026/CVPR/2026_CVPR_FLARE-A-Failure-Aware-Framework-for-Autonomous-Correction/01_overview.md) / [VLA-FixBench/FaultEval](../2026/ICML/2026_ICML_Can-VLMs-Diagnose-and-Recover-from-VLA-Manipulation-Faults/01_overview.md) | runtime alert에서 diagnosis와 correction protocol을 포함하는 failure-aware evaluation으로 확장된다. | detection timing, correction success와 intervention cost를 같은 protocol에서 비교할 수 있는가 |
| persistent spatial memory → [Spatial Memory](../2026/ICML/2026_ICML_Spatial-Memory-for-Out-of-Vision-Manipulation-in-Vision-La/01_overview.md) / [MomaGraph](../2026/ICLR/2026_ICLR_MomaGraph-State-Aware-Unified-Scene-Graphs-with-Vision-Lan/01_overview.md) → [Memory Retrieval/HALO](../2026/RSS/2026_RSS_Memory-Retrieval-in-Visuomotor-Policies-for-Long-Horizon-R/01_overview.md) | out-of-view state graph와 retrieval을 task-relevant sparse history로 정리해 long-horizon drift를 줄이는 방향이다. | retrieval confidence와 memory expiry가 phase transition·safety intervention을 실제로 개선하는가 |
| generalist VLA benchmarks → [LIBERO](../2023/NeurIPS/2023_NeurIPS_Benchmarking-Knowledge-Transfer-for-Lifelong-Robot-Learnin/01_overview.md) / [CALVIN](../2022/RA-L/2022_RA-L_CALVIN-A-Benchmark-for-Language-Conditioned-Policy-Learnin/01_overview.md) / [FurnitureBench](../2023/RSS/2023_RSS_FurnitureBench-Reproducible-Real-World-Benchmark-for-Long/01_overview.md) → [VLA-Arena](../2026/ICML/2026_ICML_VLA-Arena-An-Open-Source-Framework-for-Benchmarking-Vision/01_overview.md) | clean success 중심 benchmark에서 safety·distractor·extrapolation·long-horizon stress dimensions를 함께 비교하는 방향이다. | stress score가 event-level failure·recovery cost와 일치하는가 |

## 2026-10-23 근거 통합

아래는 2026-10-22까지의 registry/source 감사와 후보 검토를 연결한 연구자 해석이다. 새 정독·효과 검증·직접 citation 관계의 확인을 뜻하지 않는다. Paper별 본문 확인 범위는 overview 및 연결된 dossier를 따른다.

| 비교 축 | 등록된 선행 | 현재 남길 구분 |
|---|---|---|
| E2: 시간 표현과 feedback | [AAC](../2026/CVPR/2026_CVPR_Adaptive-Action-Chunking-at-Inference-time-for-Vision-Lang/01_overview.md) (2026 CVPR); [RTC](../2025/NeurIPS/2025_NeurIPS_Real-Time-Execution-of-Action-Chunking-Flow-Policies/01_overview.md) (2025 NeurIPS); [SAIL](../2025/CoRL/2025_CoRL_SAIL-Faster-than-Demonstration-Execution-of-Imitation-Lear/01_overview.md) (2025 CoRL); [Latent continuous chunks](../2026/ICML/2026_ICML_Learning-High-Frequency-Continuous-Action-Chunks-in-Latent/01_overview.md) (2026 ICML); [Real-time correction](../2025/arXiv/2025_arXiv_Leave-No-Observation-Behind-Real-time-Correction-for-VLA-A/01_overview.md) (2025 arXiv) | 표현/retiming/관측 갱신/controller 변경을 분리한다. 서로 다른 주기의 숫자를 같은 control contract로 비교하지 않는다. |
| 새 temporal preprint의 경계 | [Vela](../2026/arXiv/2026_arXiv_Vela-Scaling-Vision-Language-Action-Models-with-Adaptive-A/01_overview.md) (2026 arXiv); [PaceVLA](../2026/arXiv/2026_arXiv_PaceVLA-Adaptive-Temporal-Action-Quantization-in-Vision-La/01_overview.md) (2026 arXiv); [Stability assumption](../2026/arXiv/2026_arXiv_Measuring-the-Stability-Assumption-Behind-Action-Chunking/01_overview.md) (2026 arXiv) | 기존 temporal parameterization·진단을 새 기여에서 제외하고 동일 물리 시간·sensor age 이후 남는 차이를 묻는다. |
| E1: 전이·보존 interface | [Actions as Language](../2026/ICLR/2026_ICLR_Actions-as-Language-Fine-Tuning-VLMs-into-VLAs-Without-Cat/01_overview.md) (2026 ICLR); [LAP](../2026/RSS/2026_RSS_LAP-Language-Action-Pre-training-Enables-Zero-Shot-Cross-E/01_overview.md) (2026 RSS); [Real-world continual VLA](../2026/arXiv/2026_arXiv_Can-Vision-Language-Action-Models-Learn-from-Real-World-Da/01_overview.md) (2026 arXiv); [SPACE](../2026/arXiv/2026_arXiv_SPACE-Enabling-Learning-from-Cross-Robot-Data-Toward-Gener/01_overview.md) (2026 arXiv) | VLM 의미 보존·로봇 skill retention·cross-embodiment transfer는 별도 outcome이다. 공통 표현을 실제 effect 정렬로 자동 해석하지 않는다. |
| Instruction-following의 범위 | [CounterAlign](../2026/CoRL/2026_CoRL_CounterAlign-Counterfactual-Supervision-for-Vision-Languag/01_overview.md) (2026 CoRL); [RoboFollow](../2026/CoRL/2026_CoRL_RoboFollow-Unveiling-the-Instruction-Following-Mirage-in-E/01_overview.md) (2026 CoRL); [ExecVLA](../2026/arXiv/2026_arXiv_ExecVLA-Following-Fine-Grained-Execution-Constraints-in-Vi/01_overview.md) (2026 arXiv) | What/how·반사실 지시 평가 자체는 새 기여가 아니다. 언어 입력 경로·scene equivalence·실행 제약 label이 먼저 필요하다. |

### Registry 연결 갱신 — 2026-10-25

- [Mechanistic Interpretability for Steering Vision-Language-Action Models](../2025/CoRL/2025_CoRL_Mechanistic-Interpretability-for-Steering-Vision-Language/01_overview.md)
- [LIBERO-Plus: A Progressive Robustness Benchmark for Visual-Language-Action Models](../2026/CVPR/2026_CVPR_LIBERO-Plus-A-Progressive-Robustness-Benchmark-for-Visual/01_overview.md)
- [THE COLOSSEUM: A Benchmark for Evaluating Generalization for Robotic Manipulation](../2024/RSS/2024_RSS_THE-COLOSSEUM-A-Benchmark-for-Evaluating-Generalization-fo/01_overview.md)
- [RoboMME: Benchmarking and Understanding Memory for Robotic Generalist Policies](../2026/ICML/2026_ICML_RoboMME-Benchmarking-and-Understanding-Memory-for-Robotic/01_overview.md)
- [Beyond Sight: Finetuning Generalist Robot Policies with Heterogeneous Sensors via Language Grounding](../2025/ICRA/2025_ICRA_Beyond-Sight-Finetuning-Generalist-Robot-Policies-with-Het/01_overview.md)
- [LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization](../2025/arXiv/2025_arXiv_LIBERO-PRO-Towards-Robust-and-Fair-Evaluation-of-Vision-La/01_overview.md)
- [Colosseum V2: Benchmarking Generalization for Vision Language Action Models](../2026/arXiv/2026_arXiv_Colosseum-V2-Benchmarking-Generalization-for-Vision-Langua/01_overview.md)

기억·perturbation·sensor 추가·activation 개입은 같은 일반화 지표로 묶지 않는다. RoboMME를 등록했어도 현재 N3 native 관측 일치는 미검증이며 기존 후보 HOLD는 유지한다.

이번 등록은 `ABSTRACT_CHECKED` 수준의 비교 연결이다. 기존 정독 matrix·reading status·연구 판단을 승격하지 않는다. [등록 범위와 source 경계](../work/update/REGISTRY_REFRESH_2026-10-25.md).

### 2026-10-25 top-tier 보완 — 읽기 전 비교 연결

> Researcher interpretation / CURATION-HYPOTHESIS. 신규 노트는 abstract/project 기반이며 아래 연결은 정독·실험 결과나 직접 citation 관계의 확인이 아니다.

[RoboArena](../2025/CoRL/2025_CoRL_RoboArena-Distributed-Real-World-Evaluation-of-Generalist/01_overview.md)의 분산 pairwise 순위와 [STAR-Gen](../2026/RA-L/2026_RA-L_A-Taxonomy-for-Evaluating-Generalist-Robot-Manipulation-Po/01_overview.md)의 시각·의미·행동 변화 축을 LIBERO-Plus·THE COLOSSEUM과 함께 읽는다. 두 benchmark는 질문이 다르다. 전자는 실환경 정책 순위, 후자는 일반화 조건의 분해다. 실로봇 데이터가 있다는 이유만으로 모든 embodiment를 평가한 것으로 해석하지 않는다.

[Gen2Act](../2025/CoRL/2025_CoRL_Gen2Act-Human-Video-Generation-in-Novel-Scenarios-enables/01_overview.md)는 생성 인간 영상에서 robot action으로 이어지는 interface, [Mobility VLA](../2025/CoRL/2025_CoRL_Mobility-VLA-Multimodal-Instruction-Navigation-with-Long-C/01_overview.md)는 tour video에서 goal frame·graph·navigation으로 이어지는 interface를 제공한다. Video prior의 이득은 정지 semantic cue와, 긴 문맥의 이득은 같은 tour를 받는 retrieval baseline과 비교한다. 이들은 새 방법의 직접 선행이며 기존 memory/latent-action HOLD를 자동 해제하는 근거가 아니다.

## Open Questions

### 물체 자세·3D 추정을 단일 VLA의 행동에 연결하는 조건 — 2026-11-17

**CURATION-HYPOTHESIS.** [Pose-VLA](https://roboticsproceedings.org/rss22/p145.html)의 pose pretraining과 [SaPaVe](https://openaccess.thecvf.com/content/CVPR2026/html/Liu_SaPaVe_Towards_Active_Perception_and_Manipulation_in_Vision-Language_Action_Models_CVPR_2026_paper.html)의 카메라/조작 공동 학습 이후, pose token 추가나 통합 architecture만으로 새 기여를 주장하지 않는다. 여러 pose 가설의 행동 양립성, 입력 geometry 오류의 방향별 조작 영향을 두 초기 질문으로 나눴다. [3D track의 직접 선행과 질문](./07_robotics_3d_perception.md#pose-reconstruction-2026) 및 [후보 index](../work/research_topics/README.md)를 따른다. RL은 해당 학습에 필요할 때 선택하며, pipeline 연결·배포 시 단일 정책·같은 가중치의 공동 갱신을 구별한다. 효과/신규성은 미확립이다.

**2026-11-18 등록 연결 / CURATION-HYPOTHESIS.** [Pose-VLA](../2026/RSS/2026_RSS_Universal-Pose-Pretraining-for-Generalizable-Vision-Langua/01_overview.md)는 pose/trajectory pretraining, [GeoPredict](../2026/CVPR/2026_CVPR_GeoPredict-Leveraging-Predictive-Kinematics-and-3D-Gaussia/01_overview.md)는 훈련 시 3D geometry supervision, [ReconVLA](../2026/AAAI/2026_AAAI_ReconVLA-Reconstructive-Vision-Language-Action-Model-as-Ef/01_overview.md)는 2D target-region 재구성으로 구별한다. ReconVLA를 3D reconstruction 방법으로 분류하지 않는다. [Robo3R](../2026/RSS/2026_RSS_Robo3R-Enhancing-Robotic-Manipulation-with-Accurate-Feed-F/01_overview.md)의 robot-frame geometry와 [GAP](../2026/CVPR/2026_CVPR_Action-Geometry-Prediction-with-3D-Geometric-Prior-for-Bim/01_overview.md)의 미래 action/geometry 공동 예측을 비교하되 geometry supervision 자체를 새 기여로 주장하지 않는다. [REG-R17](../work/update/REGISTRY_MAINTENANCE_2026-11-18.md)의 paper-note는 abstract/project 확인이며 연구 후보의 효과·정독 상태는 승격하지 않았다.

### 같은 목표의 환경별 RL 적응을 단일 정책에 통합할 수 있는가 — 2026-11-17

**CURATION-HYPOTHESIS / R1 이력, R2 현재 선택에서 제외.** [MergeVLA](https://mergevla.github.io/)와 [PolicyWeave](https://arxiv.org/html/2609.33125v1) 이후 일반 VLA 전문가 병합, RL 후학습 이득 통합은 새 기여가 아니다. 남을 수 있는 질문은 같은 embodiment·task·action interface에서 시각/물리 환경별 RL 갱신을 합쳐 미관측 요인 조합에 일반화하는 조건이다. 표준 static merge·context 선택·공동 RL·전문가 증류보다 중요한 차이가 있는지 미확인이다. LANGRET의 지시별 행동 보존이나 폐기 VRL의 residual 재사용과 구별한다. [후보 카드·직접 선행·비용](../work/update/NEW_FIELD_SCOUT_2026-11-17.md#merge). R2 재검색에서는 방법 기여가 더 구체적인 [접촉 관계 기반 탐색 분포](../work/update/NEW_FIELD_SCOUT_2026-11-17.md#relation-exploration)를 다음 검토 대상으로 선택했다.

<a id="foundation-frontier-2026"></a>
### 새 직접 선행의 학습 대상과 배포 구조

**2026-11-12 / 초록 기반 CURATION-HYPOTHESIS.** [REG-R15](../work/update/FOUNDATION_FRONTIER_SUPPLEMENT_2026-11-12.md)에서 추가한 논문을 아래처럼 구분한다. 통합 architecture, 배포 시 한 정책, 같은 가중치의 RL 갱신은 별도 속성이다.

| 논문 | 확인한 범위 | 현재 질문에 필요한 후속 대조 |
|---|---|---|
| [WCM](https://arxiv.org/abs/2607.29613), arXiv 2026 | 미래 latent와 value를 함께 학습하는 시간 정보를 가진 critic으로 VLA RL을 지원 | UNIFIED의 actor/critic 공유 가중치·gradient routing·history 접근이 실제로 같은가? 보조 world-model loss 자체를 새 기여로 제안하지 않음 |
| [RoboAlign](https://arxiv.org/abs/2603.21341), arXiv 2026 | MLLM의 action-aligned reasoning을 RL로 학습하고 diffusion action head를 학습하는 구성 | Token reasoning의 RL과 실제 action expert의 RL 갱신 대상을 구분. 지시별 robot behavior 보존과 동일 평가인지 본문 대조 필요 |
| [STARE-VLA](https://arxiv.org/abs/2512.05107), arXiv 2025 | Stage-aware preference/interaction을 활용한 점진적 후학습 | Stage supervision·privileged 정보·추가 interaction 비용과 reward shaping을 통제한 비교 필요 |
| [Real-Time EXPO-FT](https://arxiv.org/abs/2609.18207), arXiv 2026 | 느린 VLA와 빠른 action editor를 잇는 실시간 RL 구성 | 단일 정책 내부 학습과 다른 배포 구조. Latency·feedback 성능의 강한 대안으로 남김 |
| [AC2-VLA](https://ijcai.org/proceedings/2026/228), IJCAI 2026 | Action context에 따른 adaptive computation과 self-distillation | RL 없이 계산을 줄이는 대안과 동일 control clock·관측 age·wall-clock 비용을 비교 |
| [Act2Goal](https://www.roboticsproceedings.org/rss22/p015.html), RSS 2026 | World model에서 visual-goal policy를 만들고 hindsight 적응을 수행 | Visual goal을 language instruction과 혼동하지 않음. Hindsight 적응을 reward-based RL로 자동 분류하지 않음 |

이 등록 당시에는 연구 계약·순위를 바꾸지 않았다. 현행 유지·폐기는 [주제 index](../work/research_topics/README.md)를 따른다. 신규성 또는 P1 학습 비교를 주장하기 전 해당 주제와 직접 겹치는 본문·공개 구현을 대조한다. 새 초록 등록만으로 기여의 중복/비중복이나 정책 효과를 확정하지 않는다.

### 단일 VLA의 RL 이득과 대안 설명 — 2026-11-08

**CURATION-HYPOTHESIS / abstract 기반 보완.** [SRPO](https://openaccess.thecvf.com/content/CVPR2026/html/Fei_SRPO_Self-Referential_Policy_Optimization_for_Vision-Language-Action_Models_CVPR_2026_paper.html)·[EvoVLA](https://link.springer.com/chapter/10.1007/978-3-032-37023-5_14)의 보상 설계와 [CoVer](https://arxiv.org/abs/2602.12281)의 추론 검증을 함께 대조한다. 같은 rollout·감독·총 계산량에서 정책 가중치 갱신의 이득이 보상 정제나 행동 후보 선택으로 설명되는지가 질문이다. [MM-ACT](https://openaccess.thecvf.com/content/CVPR2026/html/Liang_MM-ACT_Learn_from_Multimodal_Parallel_Generation_to_Act_CVPR_2026_paper.html)와 [LDA-1B](https://roboticsproceedings.org/rss22/p210.html)의 통합 생성/표현을 통합 RL objective의 검증으로 해석하지 않는다.

[Contrast Sets](https://proceedings.mlr.press/v270/anwar25a.html)·[ICBench/IGAR](https://link.springer.com/chapter/10.1007/978-3-032-37152-2_3)를 사용하면 정상 지시 성공과 모순 지시에서의 잘못된 실행을 분리할 수 있다. 무조건 정지와 inference attention 보정도 대안이다. 평균 성공 향상이 언어 grounding 향상이라는 주장을 곧바로 지지하지는 않는다. 새 44편의 노트·분류·버전 경계는 [REG-R12](../work/update/TOP_TIER_SUPPLEMENT_2026-11-08.md)에 연결했다. 기존 후보 판정과 사용자 정독 상태는 유지한다.

<a id="gap-hindsight-transfer"></a>
### 참인 hindsight 목표와 원 과제 전이

**2026-11-17: 현재 HINDSIGHT 설계는 RETIRED.** [폐기 이유](../work/research_topics/retired/README.md#hindsight_transfer). [LfH](../2026/arXiv/2026_arXiv_Learning-from-Hindsight-for-VLA-Reinforcement-Learning/01_overview.md), [SPRINT](https://doi.org/10.1109/ICRA57147.2024.10610606), [SOAR](https://proceedings.mlr.press/v270/zhou25b.html) 이후 언어 재라벨·실패 재사용 자체는 새 기여가 아니다. 유효 목표 중 원 과제 전이를 돕는 선택이라는 좁은 차이에 비해 label 유효성·support·학습 비교 부담이 크다.

재사용할 구분은 보조 목표의 성공과 원래 지시의 성공, 목표 선택과 동일 라벨 모방의 차이다. 실제 전이 효과는 미측정이며 폐기는 투자 판단이다. 과거 N2/P0 계약을 현재 실행 대기로 복제하지 않는다.

### 기존 후보와 함께 심사한 VLA + RL 질문

11/05의 [통합 검토](../work/update/INTEGRATED_GAP_REVIEW_2026-11-05.md)는 당시 이력이다. 11/17에는 VRL을 폐기하고 FEEDBACK을 신뢰성 문헌 탐색의 출발점으로 남겼다. [현행 투자 판단](../work/research_topics/README.md#candidate-priority)과 실행 가능성은 별개다.

<a id="gap-feedback-2026"></a>

**시각 피드백 활용 — 유지.** [BAS-VLA](https://arxiv.org/html/2609.23650v1)는 nuisance 불변성과 의미 변화의 반응을 이미 다룬다. 공개 RL/SFT 비교는 데이터·normalizer 차이 때문에 RL 목적함수만의 인과효과가 아니다. [관측 지연 진단과 최신 실패/복구 선행](../work/research_topics/visual_feedback/내용/README.md#reliability-scout-2026)은 새 관측의 행동상 가치와 실패 원인·유용한 개입을 구별한다. Native 효과는 미확인이다.

<a id="gap-crossplay-2026"></a>

**독립 팀원의 협력 일반화 — 문헌 질문 보존.** [당시 탐색](../work/update/VLA_RL_NEW_GAP_SCAN_2026-11-05.md#cross-play)의 MARL/cross-play와 로봇 능력·정보 접근 대조가 선행되어야 한다. 현재 4개 후보나 실행 queue에 포함하지 않는다.

<a id="gap-vla-rl-2026-11"></a>
### Base 업데이트와 residual·보상 자료의 재사용

**2026-11-17: residual 재사용(VRL) 설계는 RETIRED.** [이유·검증 경계](../work/research_topics/retired/README.md#vla_residual_update). A의 보정 학습부터 B의 적응까지 필요한 비용에 비해 gain·warm-start·동일 데이터 모방 이후 차이가 불명확하다. 계층형 구조라는 이유만으로 폐기하지 않았으며 residual RL 분야 전체를 제외하지 않는다.

보상 reference coverage·label 신뢰도와 policy 학습 데이터 증가 효과는 분리할 비교 원칙이다. [과거 CounterAlign 비교](../work/update/VLA_RL_GAP_REVIEW_2026-11-03.md#counterfactual-coverage)는 문헌 질문으로만 보존한다. 두 질문 모두 현재 자동 실행 대상이 아니다.

<a id="gap-action-codec-2026"></a>
### 행동 토큰화의 복원 점수와 실행 성능

**2026-11-17: CODEC1 독립 주제 RETIRED.** [CPU 결과·폐기 이유](../work/research_topics/retired/README.md#action_tokenization). 20 episode·101 window는 offline 복원 진단이며 실제 robot rollout/성공 개선이 아니다. [ProAct](https://arxiv.org/abs/2610.09170) 이후 복원 점수가 정책 성능과 같지 않다는 일반 관찰을 신규성으로 삼지 않는다. Metric별 codec 선택과 실제 행동 변화의 구별은 평가 원칙으로 남긴다.

### 2026 문헌 보완: 검색·기억·언어·제어의 구분

[RICL](../2025/CoRL/2025_CoRL_RICL-Adding-In-Context-Adaptability-to-Pre-Trained-Vision/01_overview.md)의 외부 시연 적응과 [MemER](../2026/ICLR/2026_ICLR_Scaling-up-Memory-for-Robotic-Control-via-Experience-Retri/01_overview.md)의 episode 기억을 구분한다. [LIBERO-X](../2026/RSS/2026_RSS_LIBERO-X-Robustness-Litmus-for-Vision-Language-Action-Mode/01_overview.md)는 복합 shift 평가, [Residual Semantic Steering](../2026/ACL/2026_ACL_Stable-Language-Guidance-for-VisionLanguageAction-Models/01_overview.md)는 같은 의미의 언어 표현 민감성, [Legato](../2026/RSS/2026_RSS_Learning-Native-Continuation-for-Action-Chunking-Flow-Poli/01_overview.md)는 action chunk의 제어 연속성을 비교할 NEXT 기준이다. [LILAC](../2026/RA-L/2026_RA-L_LILAC-Language-Conditioned-Object-Centric-Optical-Flow-for/01_overview.md)은 개방루프 motion representation을 찾을 때 쓰는 REFERENCE다. 이 연결은 abstract/project 기반 curation이며 새 정독 결과가 아니다.

같은 target support·지시·control budget을 유지한 시연 bank 개입에서도 차이가 남는지 묻되, [Dejavu](../2026/CVPR/2026_CVPR_Dejavu-Towards-Experience-Feedback-Learning-for-Embodied-I/01_overview.md)의 경험 bank + 학습된 residual을 신규 조합으로 재주장하지 않는다. 검색 결과·지시 표현·action queue가 각각 달라지는 효과를 분리해야 한다.


<a id="gap-retrieval-library-2026"></a>
### 시연 저장소 확장과 기존 과제 성능

**2026-11-17: RETRIEVAL 독립 주제 RETIRED.** [자산 감사·이유](../work/research_topics/retired/README.md#context_retrieval). [When Does Retrieval Help?](https://arxiv.org/abs/2610.05492)는 검색 표현과 실제 도움이 되는 retrieval의 차이를 다룬다. 저자의 NeurIPS workshop 표기를 본 학회로 승격하지 않는다. 목표별 검색 이후 차이가 좁고 성공 시연·평가 독립성 근거와 native 입력 확보 부담이 크다. 검색 자료 identity 확인은 성공 인증과 다르며, frozen weights도 context 변화의 영향을 받는다는 사실 자체는 새 기여가 아니다.

<a id="gap-object-set-2026"></a>
### 물체 집합 선택·수량 지시

**2026-11-17: SET 독립 주제 RETIRED.** [폐기 이유·핵심](../work/research_topics/retired/README.md#object_set). [ClevrSkills](../2024/NeurIPS/2024_NeurIPS_ClevrSkills-Compositional-Language-And-Visual-Reasoning-in/01_overview.md)·[Spa-Bench](../2026/arXiv/2026_arXiv_Spa-Bench-A-Real-Robot-Benchmark-for-Spatial-Grounding-in/01_overview.md)·[순차 조합 진단](../2026/CoRL/2026_CoRL_Diagnosing-Compositional-Generalization-in-Sequential-Robo/01_overview.md)의 조합/grounding 문제와 비교한다. 단순 k회 반복·counter 이후 잔여 차이는 미측정이며 새 evaluator 구축의 비중이 커 현재 주력 투자에서 제외했다.

수량 오류를 참조·진행 추적·실행 능력으로 구분하고, terminal-only 목표와 중간 보존 제약을 구별하는 평가 원칙은 남긴다. 기존 논문이 모든 수량 문제를 해결했다고 주장하지 않는다.

<a id="gap-instruction-revision-2026"></a>

### 부분 지시 수정 이후 VLA의 제약 보존과 실행 일관성

**11/01 PRE-GPU-3 보완:** [비실험 완결 검토](../work/update/THREE_CANDIDATES_NONEXPERIMENTAL_2026-11-01.md#revision)에서 인접 코드 생성의 제약 철회·명세 컴파일 선행을 반영해 ledger 자체의 신규성 주장을 제한했다. [비교 계약](../work/research_topics/instruction_revision/재현%20방법/COMPARISON_CONTRACT.json)에 H/S 공통 모델 metadata·입력·sampling, 제한된 규칙 대안·renderer·observer 수식·조건부 교정 절차를 지정했다. 구현·실험 효과·독립 피드백은 미확인이다.
**2026-10-31 registry 연결 / ABSTRACT_CHECKED:** [ReSteer](../2026/RSS/2026_RSS_ReSteer-Quantifying-and-Refining-the-Steerability-of-Multi/01_overview.md)는 상태별 전환 능력, [Causeway](../2026/arXiv/2026_arXiv_Causeway-Restoring-Task-Accessibility-for-Instruction-Swit/01_overview.md)는 접근 가능성 복구, [How-level instruction following](../2026/arXiv/2026_arXiv_Do-VLAs-Really-Follow-Instructions-Diagnosing-How-Level-In/01_overview.md)은 수행 조건 준수를 비교하는 NEXT로 등록했다. 이 세 축과 부분 수정의 의미 갱신을 구별하며, 새 reading 완료 행이나 직접 citation 관계로 승격하지 않는다.

**2026-10-31 GAP-REVISION1 DONE / CURATION-HYPOTHESIS.** [8개 사례](../work/research_topics/instruction_revision/내용/README.md#cases)와 [공개 interface 검토](../work/research_topics/instruction_revision/내용/README.md#source-review)를 완료했다. [10/29 선정](../work/update/VLA_GAP_SELECTION_2026-10-29.md)의 평가 질문을 유지하며 효과·신규성·독립 논문 가치는 미확인이다. 사례는 수작업 명세이고 실제 정책 실패·feasible state 증거는 아니다.

**GPU 전 보완 완료:** [직접 선행·의미/평가 계약](../work/update/PRE_GPU_BUILDUP_REVIEW_2026-10-31.md#instruction-revision). Causeway의 상태 접근 가능성, How-level의 중립 문장 대조를 반영하고 규칙 parser 대안·공통 renderer·prefix 분모/오류 처리를 명세했다. 제약을 무시해도 통과하는 장면의 성공은 제약 이해의 증거가 아니다. 보완은 설계 수준이며 효과·독립 피드백은 미확인이다. 기존 R8 최소 IO 범위는 유지한다.

**비실험 잔여 보완:** [8개 영문 의미 명세](../work/research_topics/instruction_revision/재현%20방법/SEMANTIC_CASES.json)와 [후속 판단](../work/update/PRE_GPU_BUILDUP_REVIEW_2026-10-31.md#remaining-work-review). Oracle에만 있던 취소/허용 문구를 제거해 공통 renderer와 맞췄고, 직전 action의 post-state 채점 후 수정 적용·공통 horizon을 명세했다. ExecVLA·SwitchVLA의 기존 수행 제약/전환과 구별한다. 상위 모델·관측·이력이 같아도 token 압축 효과까지 입증하는 설계는 아니다. 새 정책 효과는 여전히 미측정이다.

- **질문:** 실행 중 목표 일부를 바꿀 때, 수정된 목표를 달성하면서 여전히 유효한 조건은 유지하고 명시적으로 철회된 조건은 제거하는가? 전체 현재 지시를 자동으로 다시 작성하면 충분한가?
- **가까운 선행:** [Hi Robot, ICML 2025](https://proceedings.mlr.press/v267/shi25d.html)은 문맥 피드백과 제약을 다루며, [ReSteer, RSS 2026](https://roboticsproceedings.org/rss22/p143.html)는 상태별 능력과 전환을 평가한다. [How-level 진단, arXiv 2026](https://arxiv.org/html/2610.21251v2)은 온라인 correction과 지시의 실행 조건을 다룬다. 따라서 일반 correction·switching·constraint following을 신규 기여로 주장하지 않는다. 검토 자료만으로 선택적 수정과 전체 재명시의 matched 비교 결과가 확정되지 않아 탐색한다.
- **최소 비교:** 같은 상위 모델이 전체 대화를 다시 해석하는 H와 자신의 목표/조건 목록을 갱신하는 S를 같은 renderer·frozen VLA에 연결한다. 정답 슬롯을 자동 baseline에 주지 않는다. 먼저 정답 전체 지시 O와 짧은 atomic 지시 A의 능력을 확인하며, O를 skill sequence까지 제공하는 oracle과 구별한다. 상위 모델·renderer·observer는 아직 구현하지 않았다.
- **평가:** 수정 목표 달성과 활성 조건의 유효 시간별 준수를 함께 측정하고 goal-only 성공·조건 삭제/잔존·비용을 분리한다. 철회는 허용이지 행동 명령이 아니므로, 이전 금지 행동이 수정 목표에 필요하지 않으면 그 조건의 잔존 여부를 행동만으로 판정하지 않는다. 실제 evaluator·feasibility·정책 능력은 아직 미확인이다.
- **가치와 해석:** 단순 자동 재명시가 충분하면 interface 보완에 투자하고 추가 학습 필요성을 줄인다. 정확한 의미 목록에서도 행동이 실패하면 continuation competence·grounding·prompt distribution·control을 구별한다. 문장 이해 문제만 남으면 일반 dialogue-state 문제로 축소한다. 새 memory/RL 방법은 미선정이다.
- **과거와의 구별:** C2의 static 실행 제약, D3의 irreversible switching, E2의 timing, AUTH의 grounding 판단은 유지한다. 우선 물리적으로 가능한 단일 수정에 한정하며 미검증 과거 실행 packet을 재사용하지 않는다. [HANDOFF](./06_locomotion_whole_body.md#gap-handoff-2026)는 별도 자원 대기로 보존한다.
- **확인된 경로·남은 것:** ReSteer의 prompt/queue 전환·goal key·object pose 경로는 source로 확인했다. 기존 evaluator는 target 첫 성공을 기록하며 시간별 보호 제약과 paired state branch는 추가 검증이 필요하다. SIMPLER-IN도 성공·조건 준수를 이미 분리하므로 그 구별 자체를 기여로 세지 않는다. Hi Robot은 동적 제약의 직접 선행이다.
- **다음 관측:** 핵심은 R1의 목적지 변경 후 제약 유지와 R4의 철회 후 필요한 행동 수행이다. 10/31 [P0 준비](../work/research_topics/instruction_revision/재현%20방법/README.md#execution)에서 R8 단일 IO용 source/asset pins·Docker recipe·probe를 작성했지만 현재 ARM64/GPU allocation 실패로 image 빌드·native 실행은 하지 못했다. 호환 자원에서 R8 두 query와 queue 교체부터 확인한다. 이는 제약 준수·기본 능력의 검증이 아니다. R7 재진술은 대조, R5 허용만의 변경은 의미 검수로 유지하며 활성 행동은 [TODO](../TODO.md)의 GAP-REVISION-P0-R1을 따른다.

같이 검토한 **이미지·텍스트 지시 불일치**는 지시 우선권/정답을 먼저 정의할 예비 질문이다. **가림과 실제 목표 부재의 구별**은 기존 [C1](#gap-selective-observation-2026)·[HRI](./01_planning_control.md#gap-hri-2026)의 인접 질문으로 보존한다. 두 후보의 근거·중복·미확인은 GAP-S4에 남기며 독립 구현 queue로 추가하지 않는다.

<a id="gap-selective-observation-2026"></a>

### C1 재탐색 — 추가 관측을 언제 생략할 수 있는가?

- **2026-10-28 C1-E1 DONE; 평가·실증 질문 유지·구체화.** [지정 3편과 기존 C1 비교](../work/update/C1_OBSERVATION_COST_REVIEW_2026-10-28.md), [source ledger](../work/sources/c1_observation_cost_review_2026-10-28.json). 효과·독립 논문 가치·신규성은 미확인이다. [과거 C1](../work/research_candidates/summaries/C1_SELECTIVE_OBSERVATION.md)의 competence 미확인은 관측 전략의 부정 결과가 아니며 rollout·학습 HOLD는 유지한다.
- **질문과 활용 — 연구자 해석:** 같은 frozen VLA와 전체 물리 시간 예산에서 **look 이전 정보만 사용하는 단순 규칙**으로 성공률을 허용 범위 안에서 유지하면서 관측 동작·시간을 줄일 수 있는가? 초기 시야·시작 자세에 따라 immediate/always-look 중 하나가 충분한 범위도 답이다. RL·새 selector나 사전 양/음 교차는 탐색 요건이 아니다.
- **선행의 경계:** ActiveAlign의 adaptation과 EyeRobot의 co-training을 frozen 정책의 관측 선택 이득으로 옮기지 않는다. EyeRobot의 가상 fixation과 물리 카메라 이동도 구분한다. RESCUE가 제공하는 개입 비용 평가에 look branch만 붙여 새 방법으로 주장하지 않는다. 정확한 비교·시간 단위는 [근거 표](../work/update/C1_OBSERVATION_COST_REVIEW_2026-10-28.md#1-실제-비교된-관측정렬비용)를 따른다.
- **작은 비교:** 같은 checkpoint의 immediate / always physical look / 초기 visibility·confidence gate. Gate tuning과 평가 scene을 분리하고 전체 시간·실패·timeout을 센다. Adapted/unadapted는 각 정책 안에서 비교한다. Wait/pose-matched 대조는 시간·정보·자세의 원인을 구분할 때 추가하며 전체 효과를 보는 탐색의 사전 완료 요건으로 만들지 않는다.
- **후속 주장 기준:** 장면 단위 paired 결과·전체 budget·실패를 포함한 비용과 불확실성이 필요하다. 성공 보존의 허용치는 후속 확인 전에 정하고 비유의성만으로 동등성을 주장하지 않는다. 단순 규칙으로 충분하면 RL 도입을 중단한다. 현재는 비교 초안이며 native packet·효과 결과가 아니다.
- **현재 배치 — 대안 후보 유지:** [GAP-SELECT-E1](../work/update/VLA_EXPLORATION_SELECTION_2026-10-28.md)에서 [HANDOFF](./06_locomotion_whole_body.md#gap-handoff-2026)를 첫 우선 후보로 선정했다. C1의 효과 반증이나 가치 없음 판정이 아니다. 실제 skip 가치·단순 규칙의 충분성은 **실험 필요·미확인**이며 같은 source 감사를 반복하지 않는다. Endpoint-policy 호환성만 보여 주면 HANDOFF에 통합하고 중복 기여로 세지 않는다. 활성 행동은 [TODO](../TODO.md)를 따른다.

<a id="gap-termination-2026"></a>

### GAP-TERM — 자율 종료 조건에 따른 정책 선택

**2026-10-28 GAP-TERM-E1 DONE; 평가·실증 질문 유지·구체화.** [비교 결과](../work/update/VLA_TERMINATION_COMPARISON_2026-10-28.md), [source ledger](../work/sources/vla_termination_comparison_2026-10-28.json). 기존 감사를 재사용하고 3편의 지정 구간을 재확인했다. 실제 정책 선택 변화·안정성·신규성·독립 논문 가치는 미확인이다.

- **질문과 활용 — 연구자 해석:** 최초 목표 달성으로 고른 VLA가 공통의 간단한 종료 규칙에서도 좋은 선택인가? 선택이 안정적인 범위 또는 달라질 때의 배포 손실을 조사한다. 순위 역전·새 종료기·사전 원인 기제·baseline 실패를 탐색 입장 조건으로 두지 않는다.
- **비교 축:** First-hit는 채점 기준, fixed-horizon continuation은 실행 방식이다. 같은 완전한 기록으로 최초 달성·끝 상태를 모두 채점할 수 있다. 신호 정확도와 실제 stop-controller 전환 뒤의 결과는 별도다. [실행/채점 표와 확인된 항목](../work/update/VLA_TERMINATION_COMPARISON_2026-10-28.md#1-먼저-실행-방식과-채점-기준을-분리한다)을 따른다.
- **직접 선행의 경계:** Echo의 신호 평가, SEES Appendix B의 oracle-controlled 감사, SparkVLA의 subtask Stop을 같은 자율 종료 결과로 합치지 않는다. Echo 논문과 고정 code revision의 continuation 차이도 보존한다. P12의 fixed-horizon·achievement/terminal 구별은 기존 선행이며 **본문 범위 미확인**이다. P12 status는 2026-10-27 확인 당시 under review로만 기록하고 이번에는 재접근하지 않았다.
- **최소 비교:** 두 frozen action policy × fixed deadline/공통 detector/서로 다른 관측 query의 연속 확인. **Native stop은 실제 존재할 때 추가하며 필수가 아니다.** 같은 task goal·종료 controller·관측 구간·전체 물리 예산을 사용하고 정책 선택/threshold 조정과 held-out 평가 scene을 분리한다. 현재는 prose 초안이며 실행 packet이 아니다.
- **주장 기준:** 정지 후 물리 trace 없이 continuation을 잘라 자율 완료율을 만들지 않는다. 유지/release 요구 추가는 별도 deployment 계약이다. 같은 입력/action을 유지하지 못하면 종료기만의 효과로 귀속하지 않는다. 안정성은 실용 허용치와 불확실성으로 판단하며 비유의성만으로 동등성을 주장하지 않는다.
- **과거 판정과 재사용:** [GAP-TERM1](../work/update/VLA_TERMINATION_CONTRACT_REVIEW_2026-10-27.md)의 당시 독립 후보 NO-GO·진단 HOLD와 [GAP-TERM-R1](../TODO.md)의 확증/실행 경로는 보존한다. `On`/`Open`·gripper/controller 경계는 이전 계약을 재사용하되 특정 실패가 입증된 task pair로 승격하지 않는다. C4/C5/C6·E2·AUTH·DATA-TRANSFER의 기존 결과도 유지한다.
- **현재 배치 — 질문 보존·공통 평가 원칙 활용:** [GAP-SELECT-E1](../work/update/VLA_EXPLORATION_SELECTION_2026-10-28.md)에서 HANDOFF를 먼저 탐색하기로 했다. TERM의 goal/종료/controller 구별을 사용하되 별도 종료 후 실험까지 HANDOFF의 첫 pilot에 넣지 않는다. 실제 선택 변화·안정성은 자료·실험 필요 미확인으로 남기고 같은 source 감사를 반복하지 않는다. 독립 평가 질문과 기존 실행 gate는 보존한다.


**2026-10-27 AUTH 판정 보존:** [GAP-AUTH](./05_world_models_safety.md#gap-authorization-2026)는 VLA 목표 오선택과 보호 제외의 결합 오류 진단이다. [AUTH4 baseline 심사](../work/update/VLA_CONTACT_AUTHORIZATION_BASELINE_REVIEW_2026-10-27.md)에서 공식 YOLOE-11m/ByteTrack 후보와 초기 지시 grounding+identity 고정의 강한 단순 대안을 특정했다. Target identity는 고정하면서 모든 geometry를 갱신해야 공정하다. 그 이후 고유 이득 미확보로 **현재 두 과제의 방법 채택 NO-GO·진단 HOLD**다. AUTH3의 API/state conditioning 구분과 미검증 attention proxy 경계는 보존한다. 새 자연 사례·단순 대안 이후 예측 전 반복하지 않는다. 다른 공백의 GAP-S2 결과는 종료 평가 질문에 반영했다. Native/효과 미검증·기존 후보 보류 유지.

**2026-10-24 GAP-S1 선택 판단:** [중간 종합](../work/update/VLA_GAP_SELECTION_REVIEW_2026-10-24.md)에서 DATA-TRANSFER·LATENT·WM을 VLA와 직접 연결해 비교했으나 현재 채택 후보는 없다. 정책에 따른 데이터 가치, action supervision, 후보 선택의 모델 오차는 이미 알려진 현상이다. 어느 조건에서 target 재선택·representation 적응·탐색 제한이 필요한지에 대한 경쟁 예측과 작은 비교가 함께 마련되면 재심사한다. 완성된 공개 데이터나 긍정 효과를 pilot 전에 요구하지 않으며, native 실행·외부 피드백은 여전히 미검증이다. 각 질문과 기존 16개 후보의 판정은 유지한다.

| 질문 | 구별할 예측 | 최소 대조·중단 조건 | 근거/판정 |
|---|---|---|---|
| E2 시간/feedback | 같은 reference 물리 시간·sensor age·controller·compute에서 기존 방법과 구별되는 조건부 예측이 있는가? | RTR controller mode·AAC 실행 길이·A2C2 delay/horizon 분리를 반영한다. 일관된 task/model/normalizer/evaluator packet 없는 현재 E2-R1은 WAITING_EVIDENCE다. | [검토 근거](../work/research_candidates/2026-10-22_e2_buildup/CLAIM_CONTRACT.md) |
| D1 관측 보정 | 같은 task에서 보정이 필요한 오류와 보정하면 손해인 실제 변화가 가용 cue로 구별되는가? | Task별 reference·causal 재보정·restoration/residual을 대조한다. 지정 pi05_libero는 state-value 경로가 없어 제외했고 OFT Goal utility는 미검증이다. 방법 NO-GO/진단 HOLD. | [검토 근거](../work/research_candidates/2026-10-21_d1_buildup/NONEXPERIMENTAL_REVIEW.md) |
| D3 목표 변경 | 실제 비가역 사건 전후에 가능한 새 목표와 불가능한 새 목표를 동일 실행 능력에서 구분하는가? | Raw/annotation filename 연결은 RGB/event 정렬·continuation competence가 아니다. R1 gate NOT_MET를 유지하며 predicate baseline 이후의 현상만 남긴다. | [검토 근거](../work/research_candidates/2026-10-22_d3_buildup/R1_REVIEW.md) |
| E1 로봇 간 보존 | 정상 pose/time 정렬 이후 effect 정보의 추가 가치가 있는가? | 공통 task ID 59개는 matched independent episode가 아니다. 두 로봇의 source episode join·scene/command/time·native 평가가 먼저 필요하다. | [검토 근거](../work/research_candidates/2026-10-22_e1_buildup/R1_REVIEW.md) |
| Long-horizon/navigation | Memory·skill library·world model이 같은 history·latency·controller 예산에서 서로 다른 failure를 줄이는가? | Streaming context, collision/social cost와 manipulation contact outcome을 구분한다. Proprietary/open model의 data·sensor·compute 차이를 남긴다. | 기존 track 비교의 연구자 질문; native 효과 미검증 |

<a id="gap-data-2026"></a>
### GAP-DATA — 언어·행동 supervision을 언제 어떻게 보완할 것인가

- 갱신: **2026-10-23**. 상태: **직접 충돌이 강한 보류 질문 / CURATION-HYPOTHESIS**. 현재 새 프로젝트로 채택하지 않는다.
- 남겨 둘 좁은 질문: **새 rollout을 대량 수집하기 전에, 기존 데이터의 재주석·유효한 대안 행동 생성·새 물리 시연 중 어느 보완에 예산을 써야 할지 예측할 수 있는가?**
- 목표 outcome은 단순 grounding 점수가 아니라 비용을 포함한 보완 선택의 이득이다. 언어 다양성·scene-conditioned action support·물리적으로 유효한 대안의 유무를 분리해야 한다.

**이미 답한 부분.** [LangGap §III–V](https://arxiv.org/html/2603.00592v1)는 언어 의존성의 평가와 데이터 보완을, [CAST §III–IV](https://arxiv.org/html/2508.13446v1)는 navigation의 atomic policy를 이용한 반사실 instruction/action label 생성을 다룬다. [CounterAlign §3.1–3.3](https://arxiv.org/html/2608.21740v1)은 joint relabeling의 불확실성과 critic용 instruction relabeling을 구별한다. [CIG의 NeurIPS 2026 공식 abstract](https://neurips.cc/virtual/2026/poster/152584)도 instruction grounding 학습을 직접 다룬다. “언어를 더 잘 사용하게 한다”는 표현만으로 차별화되지 않는다.

특히 [ECT §5.3·Appendix K](https://arxiv.org/html/2609.39971v1)는 기존 CALVIN counterpart 활용, 새로 구성한 유효 행동, 고정 시연 예산의 실제 로봇 비교를 이미 보고한다. **“없는 행동 대안을 수집하고, 있는 대안은 재사용한다”는 초기 구상과 강하게 충돌한다.** 동일 논문의 paired loss도 여러 요인을 함께 바꾸며 일반 contact/mobile/navigation까지 입증하지는 않지만, 그 한계를 다른 환경에 옮기는 것만으로 신규성이 생기지 않는다. ECT는 2026-09-30 preprint이며 채택 논문으로 표시하지 않는다.

[DataMIL](https://proceedings.iclr.cc/paper_files/paper/2026/hash/033d9e8dbbbc0ad90e59222cf1db0fc2-Abstract-Conference.html)은 policy-aware data selection, [RSS 2024 compositional collection](https://roboticsproceedings.org/rss20/p013.html)은 데이터 수집 설계, [RADAR](https://radar-analysis.github.io/)는 training-data-aware 실패 분석의 직접 선행이다. 따라서 남을 수 있는 것은 이들을 넘어 **보완 전에 측정한 정보가 보완 종류의 상대 이득을 예측하는가**라는 조건부 질문이다. 이번 조사만으로 그 공백의 존재를 확정하지 않았다.

**비교가 필요하다면:** 같은 robot·기본 policy·원 데이터에서 factual reannotation, counterfactual instruction supervision, action-valid synthetic alternatives, 새 실제 demonstration을 분리한다. 틀린 action에 기존 next-state를 붙이지 않는다. 동일 episode 수뿐 아니라 사람 annotation 시간·로봇 점유 시간·생성 모델 비용·추가 training compute를 기록한다. 이미 사용한 scene/instruction 조합과 분리한 평가에서, 단순 coverage rule·DataMIL류 선택·ECT류 활용보다 보완 선택이 나아지는지를 봐야 한다. 이 설계와 예산은 아직 실행 계약이 아니다.

**기각 조건:** 기존 논문의 규칙만으로 어떤 보완이 이길지 설명되거나, 새로운 예측 없이 네 데이터 recipe를 비교하는 benchmark만 남으면 독립 연구로 채택하지 않는다. 미확인 직접 선행인 CIG full text, 최신 CAST version, 관련 active data collection·annotation allocation 연구가 해소되기 전에는 신규성 주장을 하지 않는다.

이 질문은 C2의 실행 경로 제약이나 E1의 로봇 간 action/effect 정렬을 자동 재개하지 않는다. 우선 단일 robot의 scene–instruction–action 관계에 한정한다. [GAP-CONTACT](./03_manipulation_contact.md#gap-contact-2026)는 GAP-R2 직접 비교 후 진단 후보 HOLD로 축소했다. 후속 심사와 현재 인계는 [TODO](../TODO.md)를 따른다. [전체 검색·제외 기록](../work/update/VLA_GAP_SCOUT_2026-10-23.md).

### 넓은 주제로 다시 제안하지 않을 범위 — 2026-10-23

| 넓은 구상 | 직접 선행과 이번 판단 |
|---|---|
| VLA가 언어를 무시하는 현상을 처음 진단 | LangGap·CIG·[CofactVLA](https://neurips.cc/virtual/2026/poster/153110)·[Not All Features](https://neurips.cc/virtual/2026/poster/148883)·ECT가 서로 다른 원인과 개입을 다룬다. 모델별 설명의 차이부터 확인한다. |
| Atomic skill을 연결하고 handoff state를 보완 | [RoboCombine 공식 abstract](https://neurips.cc/virtual/2026/poster/139255)가 시작 상태 support를 직접 다룬다. [MoTo](https://proceedings.mlr.press/v305/wu25c.html)의 interaction-aware docking과 기존 D2도 함께 비교해야 한다. |
| 텍스트 reasoning을 action의 완전한 설명으로 사용 | [Say the Same, Act Differently](https://neurips.cc/virtual/2026/poster/154708)가 직접 반례를 다룬다. Abstract 확인이며 세부 mechanism·범위는 본문 대조 전이다. |
| 실패 데이터로 학습·VLM 능력 보존 | [AFIL](https://neurips.cc/virtual/2026/poster/155737)·[representation-centric pretraining](https://neurips.cc/virtual/2026/poster/155956), registry의 VLM2VLA/LAP가 직접 비교 대상이다. |

NeurIPS 2026 링크는 공식 program/poster에 공개된 abstract를 확인한 것이다. 출판 proceedings·코드 재현까지 확인한 것으로 올리지 않는다. 모든 방향이 해결됐다는 뜻이 아니라 위 **넓은 주장 자체를 신규 기여로 쓰지 않는다**는 판단이다.

### VLA 공백 후보의 추가 대조 — 2026-10-23 GAP-V2

[통합 조사](../work/update/INTEGRATED_GAP_REVIEW_2026-10-23.md)는 2024–2026 기반과 최근 직접 선행 30건을 확인/재확인했다. 아래 세 질문과 [접촉 정보의 필요 조건](./03_manipulation_contact.md#gap-contact-2026)을 VLA의 네 축으로 비교한다. 모두 `CURATION-HYPOTHESIS`다. 논문의 존재로 분야를 닫지 않되, 이미 답한 질문을 신규 기여로 반복하지 않는다. 기존 GAP-DATA·C1–C6·D1–D3·E1/E2의 판정은 그대로다.

<a id="gap-latent-2026"></a>
### GAP-LATENT — 영상에서 배운 행동 표현의 이득은 어떤 물리 조건까지 전달되는가?

- **상태:** **GAP-L2 검토 완료 — 일반 supervision/alignment/proxy 주장은 NO-GO, 물리 조건 진단은 REVISE / HOLD.** [직접 비교·비교 계약](../work/update/LATENT_ACTION_REVIEW_2026-10-23.md)과 [source/code ledger](../work/sources/latent_action_review_2026-10-23.json)에 6편 지정 본문/부록, registry 기반 2편, GitHub 4개 revision·HF 4개 목록의 확인 범위를 남겼다. 학습 착수나 신규성 입증이 아니다.
- **기반/알려진 답:** [HRP, RSS 2024](https://www.roboticsproceedings.org/rss20/p068.html)는 human-video affordance를, [LAPA, ICLR 2025](https://proceedings.iclr.cc/paper_files/paper/2025/hash/45d74e190008c7bff2845ffc8e3facd3-Abstract-Conference.html)와 [UniVLA, RSS 2025](https://www.roboticsproceedings.org/rss21/p014.html)는 영상 기반 행동 표현을 로봇 학습에 연결한다. [ViPRA, ICLR 2026](https://proceedings.iclr.cc/paper_files/paper/2026/hash/707e34efcabd2b9375f7a64019600aa8-Abstract-Conference.html)는 미래 영상/latent action과 robot-specific decoder를 함께 다룬다. 따라서 “사람 영상으로 VLA 사전학습”은 공백이 아니다.
- **강한 직접 충돌:** [LAOM, ICML 2025](https://proceedings.mlr.press/v267/nikulin25a.html)는 distractor와 supervision을, [VILA, CVPR 2026](https://openaccess.thecvf.com/content/CVPR2026/html/Jeong_Learning_to_Act_Robustly_with_View-Invariant_Latent_Actions_CVPR_2026_paper.html)는 action label 기반 view alignment를 다룬다. [VLM task-centric latent actions](https://arxiv.org/abs/2601.22714)는 distractor 제거를, [What Matters for Latent Actions](https://arxiv.org/abs/2608.19613)는 design·proxy metric 비교를 이미 제시한다. 뒤 두 편은 이번 확인 범위에서 preprint다. “nuisance 제거”, “좋은 latent metric 만들기” 자체도 신규 주장으로 쓰지 않는다.
- **추가 직접 충돌:** [Action-Similarity Transfer v1, 2026-09 preprint](https://arxiv.org/html/2609.19846v1)는 같은 labels의 regression/similarity, decoder label budget, π₀/작은 정책을 비교한다. 새 UR5에서 기록 latent의 decoded replay와 frozen policy의 closed-loop 실패도 분리했다. 따라서 “label을 초기에 쓴다”, “decoder가 좋아도 policy는 실패한다”는 발견만으로 새 주제가 되지 않는다. 보조 loss만 labels를 줄인 설정과 전체 pipeline 절감을 구분한다.
- **본문·code로 보정한 해석:** LAOM의 decoder는 예측 latent를 사용하고 `obs_emb` 인자를 실제로 읽지 않는다. VILA의 view alignment는 action supervision을 사용한다. ViPRA FM adaptation은 backbone도 학습하며 공개 기본 continuous sampler는 explicit latent token 생성 없이 action을 출력한다. What Matters의 LIBERO-Plus 영상은 Stage I/II에 포함되므로 Stage-III zero-shot을 전체 미노출로 쓰지 않는다. VILA의 세부 비교는 arXiv v1 기준이며 CVF 최종 supplement의 추가 VLA baseline은 검색 색인까지만 확인했다. [근거·버전 경계](../work/update/LATENT_ACTION_REVIEW_2026-10-23.md)
- **남겨 둘 질문 — 연구자 해석:** 관측 가능한 물리 응답 변화에서 같은 target labels를 **decoder에만 사용할지 representation까지 조정할지** 사전에 예측할 수 있는가? Controller/normalizer 보정만 필요한 변화와 제어 정보가 표현에서 사라진 경우를 구별해야 한다. 단순 friction 축 추가나 사후 실패 설명으로는 부족하다. 현재 그 예측이 갈리는 구체적인 사례는 미확보다.
- **최소 대조:** 같은 robot/task/video pool·policy 입력·latent width·head와 label ID 합집합으로 frozen representation+decoder 대 representation supervision+decoder를 비교한다. Direct BC, supervised IDM, pretrained visual encoder, 단순 normalization/controller 보정과 공통 history/proprio baseline을 포함한다. Teacher latent probe·predicted command·closed-loop success를 구분하고 총 compute·target interaction 비용 및 source 성능 보존을 함께 보고한다. [계약 초안](../work/update/LATENT_ACTION_REVIEW_2026-10-23.md#6-남길-수-있는-질문과-반증-계약-초안)
- **기각/축소:** 단순 보정·추가 데이터·head 용량·compute가 차이를 설명하거나, teacher probe에서만 이득이 있거나, 이미 알려진 decoder bottleneck을 반복하면 독립 방법 주장을 중단한다. 픽셀로 식별 불가능한 문제를 다시 보이는 것으로 충분하지 않다. E1의 정상 정렬 이후 effect 정보 질문으로 수렴하면 기존 gate로 합친다.
- **재개 조건/자원:** 실제 task·관측 가능한 물리 개입·split·checkpoint/정규화 연결과 선행과 갈리는 예측이 필요하다. 공개 weight 목록은 확인했지만 payload/호환성/runtime은 미검증이며 GPU만으로 해소되지 않는다. 문헌·정적 감사는 완료했고 같은 확인을 반복하지 않는다. Native inference/학습은 로컬 Docker에서만 수행한다.

<a id="gap-memory-2026"></a>
### GAP-MEMORY — 필요한 기억과 실행 능력 부족을 분리한 평가가 남는가?

- **상태:** 직접 충돌이 강한 보류. 독립 memory module 또는 새 일반 memory benchmark 제안으로 채택하지 않는다.
- **알려진 답:** [MemoryVLA, ICLR 2026](https://openreview.net/pdf?id=54U3XHf7qq)는 memory-conditioned action을, [RoboMME, ICML 2026](https://proceedings.mlr.press/v306/dai26c.html)는 memory 유형과 integration 방식의 체계적 비교를 다룬다. 최신 [MIKASA-Robo-VLA](https://arxiv.org/html/2610.00604v1)의 §5.3–5.4는 긴 task의 결과에 open-loop chunking과 memory-type 구성이 함께 영향을 준다고 명시한다. VLA 확장 preprint를 앞선 ICLR RL benchmark와 혼동하지 않는다.
- **더 강한 충돌:** [Beyond Success Rate §3.2·Appendix K](https://arxiv.org/html/2610.23372v1)는 기억 내용에 대한 개입, reader 도달 확인, decision/execution 분리를 직접 다룬다. 따라서 “기억을 지우거나 바꾸어 진짜 쓰는지 평가”도 현재 신규 기여로 채택하지 않는다. 이 preprint의 실험을 우리가 재현한 것은 아니다.
- **남겨 둘 질문 — 연구자 해석:** 동일 hidden cue와 task에서 retention interval·memory type·실행 chunk를 독립적으로 바꿨을 때, 어떤 memory 설계의 이득이 남는가? Oracle cue를 줘도 실패하는 task를 memory 실패로 세지 않는 검증이 필요하다. 현재는 선행 protocol을 적용하는 평가 연구 후보이며 독립 contribution은 미확보다.
- **최소 대조/반증:** reactive control, oracle-memory control, cue/history leakage 검사와 동일 sensor age·latency·controller를 둔다. Decision correctness와 closed-loop success를 따로 측정하고, chunk 길이를 줄인 단순 baseline으로 차이가 사라지면 memory 방법 주장을 기각한다. Intervention의 OOD artifact와 실제 사실 변경 효과도 분리해야 한다. 기존 protocol의 그대로인 재구현만 남으면 재현 과제로 축소한다.
- **자원/기존 후보 관계:** 시뮬레이터·checkpoint·타임스탬프·GPU가 필요하며, 현재는 source/interface 비교까지 가능하다. Chunk 최적화로 바뀌면 기존 E2, history 선택으로 바뀌면 C1의 판정을 우회하지 않는다. RP-3의 persistent-memory 계획도 자동 재개하지 않는다.

<a id="gap-retention-2026"></a>

**2026-10-25 연결:** [GAP-N1](../work/update/PROXY_OBSERVATION_CONTRACT_REVIEW_2026-10-25.md)은 selector와 target의 입력 정보 차이를 데이터 선택 전이의 통제 변수로 사용한다. [N2 source 심사](../work/update/PROXY_OBSERVATION_QUALIFICATION_REVIEW_2026-10-25.md)에서 FrameSamp의 과거 index·mask 전달과 perceptual subgoal 제거를 조건부 확인했다. [N3 수정 packet](../work/update/PROXY_OBSERVATION_REPAIR_REVIEW_2026-10-25.md)의 source/합성 계약 17/17 PASS는 실제 feature/model 연결이나 관측 equality의 증거가 아니다. N3-A 완료·전체 N3 PARTIAL, native qualification은 현재 로컬 Docker 자원 대기다. Memory 방법을 재개하지 않으며 단순 기억 유무 성능 차이는 subset 전이 가설의 근거가 아니다. [DATA-TRANSFER](./02_rl_il_offline.md#gap-data-transfer-2026)가 질문을 소유하고 연구 채택·수집·학습 HOLD를 유지한다.

### GAP-RETENTION — 올바른 replay로도 남는 지속학습 문제가 있는가?

- **상태:** 방법 주제로는 보류. 알려진 recipe의 적용 경계 확인에 한정한다.
- **본문 대조로 수정한 판단:** [ICML 2026의 forgetting 저항성 연구](https://proceedings.mlr.press/v306/liu26bu.html)는 pretraining과 단순 replay의 효과를 보고한다. [실제 로봇 continual-learning 연구 §5–6](https://arxiv.org/html/2605.26820v1) 역시 replay 빈도와 action normalization을 맞추면 큰 망각을 상당 부분 완화한다. **두 제목을 보고 “시뮬레이션에서는 보존되지만 현실에서는 실패한다”는 대립을 만들면 안 된다.** 후자의 current-task update 수 고정은 replay 추가에 따른 총 연산 증가를 동반한다.
- **이미 연구된 세부 원인:** [PHASER §2·Appendix J](https://arxiv.org/html/2606.03598v1)는 짧은 행동 phase의 replay 부족과 task 간 간섭을 직접 다룬다. Phase-aware sampling을 새 아이디어로 내세우지 않는다. [Actions as Language, ICLR 2026](https://proceedings.iclr.cc/paper_files/paper/2026/hash/7a0f8055c838df8e62329a76c7c6403d-Abstract-Conference.html)의 VLM 의미/VQA 보존은 과거 robot skill 보존과 별도 outcome이다.
- **남겨 둘 질문 — 연구자 해석:** 고정 **전체** memory bytes·학습 시간 아래 task stream과 phase 구성이 달라져도 올바르게 설정한 replay recipe가 유지되는가? 예산을 더 쓰기 전에 기존 recipe로 충분한 stream과 그렇지 않은 stream을 구별할 수 있는가? PHASER의 interference 분석과 같은 질문인지 먼저 확인해야 하며 현재 신규성은 미확보다.
- **최소 대조:** 동일 normalization, uniform/phase-aware replay, 같은 총 compute와 같은 new-task updates라는 두 예산 조건을 구분한다. Buffer 단위도 episode·transition·byte를 구별한다. Task별 획득 성능, retained success, forward/backward transfer를 함께 보고, 애초에 못 배운 task의 낮은 forgetting을 보존 성공으로 세지 않는다. Policy/seed/task-order 전체를 독립 표본처럼 부풀리지 않는다.
- **기각/자원:** 충분한 ER·normalizer 수정으로 현상이 없어지거나 선행의 task/phase scaling 분석과 차이가 없으면 새 방법 연구를 종료한다. 여러 순서의 반복 학습이 필요해 네 VLA 질문 중 검증 비용이 크다. GPU가 있어도 즉시 재개하지 않는다. E1의 cross-robot 보존이나 초기 RL transfer의 RETIRED 판정을 바꾸지 않는다.

<a id="gap-instruction-retention-2026"></a>

### RL 후학습에서 지시별 행동 구분 능력의 보존 조건 — GAP-LANGRET

**11/12 초기 탐색 / CURATION-HYPOTHESIS.** [석사 연구용 공백 비교](../work/update/VLA_MASTERS_GAP_SCOUT_2026-11-12.md#instruction-retention)에서 다음 비실험 질문으로 선택했다. **동일 scene의 유효 목표 A/B를 수행하던 VLA를 A 중심으로 적응시킬 때, B의 보존은 학습 분포 KL·일반 replay로 설명되는가, 아니면 관측–목표 조합의 학습 범위를 별도로 봐야 하는가?** 단일 정책 내부 후학습을 대상으로 하고 물체 선택·놓기 성공을 측정한다.

[RL’s Razor, ICLR 2026](../2026/ICLR/2026_ICLR_RL-s-Razor-Why-Online-Reinforcement-Learning-Forgets-Less/01_overview.md)는 RL의 보존 이점, [RL4VLA, NeurIPS 2025](https://proceedings.nips.cc/paper_files/paper/2025/hash/8c0fabe372177d2aded596be2d3b4544-Abstract-Conference.html)는 semantic generalization을 이미 보고한다. [DeLock](../2026/arXiv/2026_arXiv_Breaking-Lock-In-Preserving-Steerability-under-Low-Data-VL/01_overview.md)·[LIBERO-CF/CAG](../2026/arXiv/2026_arXiv_When-Vision-Overrides-Language-Evaluating-and-Mitigating-C/01_overview.md)도 후학습 lock-in과 다른 지시 수행을 직접 다룬다. 따라서 RL의 망각·언어 무시를 전제하지 않으며, 단순 대비쌍·KL/replay·추론 guidance를 신방법으로 주장하지 않는다.

새 과제 성공과 총비용을 맞춘 보존 비교, 적응 전 두 목표의 실제 능력, 잘못된 목표 선택과 motor failure의 분리가 필요하다. 초기 chunk가 같아도 최종 목표는 다를 수 있어 action distance만으로 실패를 판단하지 않는다. 강한 대안 이후에도 중요한 조건이 남는지는 미확인이다. 기존 GAP-RETENTION의 일반 방법 보류는 유지한다.

**11/12 [LANGRET-N1/N2 완료](../work/research_topics/unified_vla_rl/내용/README.md#langret-n2): 독립 방법 주제 분리를 보류하고 UNIFIED의 후속 보존 분석으로 통합했다.** RL’s Razor·TEMPO 등 직접 선행을 대조한 뒤 SimpleVLA-RL 최종본 G.2와 코드의 **병렬 이산 토큰** 경로를 선택했다. 공식 OFT의 L1·π₀.₅ flow·기존 U1 AR과 구별하며 token KL을 실행 명령/궤적 KL로 부르지 않는다. OBJ-01의 지시별 reward/종료·초기 능력·A 적응/B 보존·학습률/KL/behavior replay·분할·비용을 명세했다. [TEMPO-RL](../2026/arXiv/2026_arXiv_TEMPO-Semantic-Action-Decoupled-RL-Post-Training-for-Visio/01_overview.md)의 모듈별 RL 갱신도 직접 선행으로 등록했다. Native 준비/검증 상태는 [전용 재현 문서](../work/research_topics/unified_vla_rl/재현%20방법/README.md#langret-p0-preparation)를 따른다. Routing과 보존의 추정 대상은 구별하며 기존 U1 계약은 유지한다.

함께 본 [제어 간격 적응](../work/update/VLA_MASTERS_GAP_SCOUT_2026-11-12.md#control-interval)은 [CAT](../2026/ECCV/2026_ECCV_Trajectory-Level-Continuous-Action-Representation-for-Robo/01_overview.md)의 실제 시간 표현, RTC/RTR, [PTS](../2026/arXiv/2026_arXiv_Same-Path-Less-Time-Training-Free-Fast-Execution-of-Vision/01_overview.md)의 학습 없는 실행 대안을 먼저 비교할 예비 질문이다. [실제 결과 기반 기억](../work/update/VLA_MASTERS_GAP_SCOUT_2026-11-12.md#outcome-memory)은 [ActMem-VLA](../2026/arXiv/2026_arXiv_ActMem-VLA-Action-History-Memory-with-Dual-Expert-Denoisin/01_overview.md)의 행동 이력과 [memory-clock](../2026/arXiv/2026_arXiv_Is-Your-Robot-s-Memory-Just-a-Clock-Temporal-Shortcuts-in/01_overview.md)의 temporal-shortcut 진단·event index를 반영해 기존 SET/FEEDBACK 보완으로 남긴다. 이 등록은 새 실험이나 과거 gate 해제가 아니다.

### World-model 후보 선택과의 연결

[GAP-WM1 직접 비교](../work/update/WORLD_MODEL_SELECTION_REVIEW_2026-10-23.md)에서 Cosmos Policy의 계획·VeriVLA의 adaptive verifier를 확인했다. **WM으로 후보를 선택하거나 필요할 때 더 샘플링하는 일반 방법은 신규 주제로 채택하지 않는다.** 후보 수/분포 변경 후 평가 오류를 예측할 수 있는지는 조건부 진단 HOLD다. 고정 VLA와 외부 verifier, joint WAM, 고정 policy ranking은 서로 다른 비교 단위다. Canonical 질문·단순 baseline·동일 상태의 후보별 native outcome 재개 조건은 [GAP-WM](./05_world_models_safety.md#gap-wm-2026)에 모은다. E2의 chunk timing이나 C4/C6의 과거 판단을 우회하지 않는다.

### 협업 도움 신뢰도와의 연결

[GAP-H1 비교](../work/update/HRI_HELP_RELIABILITY_REVIEW_2026-10-23.md)는 질문 선택·noisy help·partner adaptation의 직접 선행을 확인했다. 이 기능의 조합만으로 신규 VLA 방법을 주장하지 않는다. 도움을 이해하는 능력과 실제 skill 실행 능력을 구별하고, 질문 유형/상대 정보에 따른 응답 품질·시간이 고정 VLA의 행동 선택을 바꾸는지는 조건부 진단 HOLD로 남긴다. Canonical 가정·강한 대안·재개 조건은 [GAP-HRI](./01_planning_control.md#gap-hri-2026)에 둔다. 공개 planner/skill interface 또는 diffusion-policy 실험을 native VLA 효과로 확대하지 않는다.

### 변형체의 task-conditioned 탐색 — GAP-DE1/DE2

[GAP-DE1](../work/update/DEFORMABLE_IDENTIFICATION_REVIEW_2026-10-24.md)은 물성 적응·task-oriented exploration의 직접 선행을 확인했다. PGND의 공개 text 경로는 segmentation이며 Make a Donut의 tool/subgoal planner도 native VLA와 구분한다. 지시가 실제 목표/제약과 필요한 probe를 바꾸는 task pair, oracle 정보에서의 정책 기본 능력이 확보되기 전 VLA 효과는 HOLD다. Canonical 질문은 [GAP-DEFORM](./03_manipulation_contact.md#gap-deform-2026)이 소유한다. 일반 방법 NO-GO, material–attachment 조합에 따른 탐색 필요성 진단은 REVISE/HOLD다.

[GAP-DE2](../work/update/DEFORMABLE_ASSET_SUFFICIENCY_REVIEW_2026-10-24.md) 후 **현재 공개 자산 설계는 종료·문헌 진단 HOLD**다. Scene의 물성 knob, object segmentation text, 목표 PCD, 공개 dynamics checkpoint를 모은 것만으로 native VLA 비교가 성립하지 않는다. Task pair·행동 전 정보·단순 feedback·물리 비용·실제 평가를 잇는 새 근거가 생길 때 재심사한다. 이는 native VLA를 실행해 얻은 부정 결과가 아니다.

### 반응형 navigation의 계획 변경 — GAP-P4

반응형 navigation의 질문은 [GAP-PLAN](./01_planning_control.md#gap-plan-2026)이 소유한다. [P3 계약 검사](../work/experiments/reactive_nav_contract/RESULTS.md) 이후 [P4](../work/experiments/reactive_nav_pilot/RESULTS.md)에서 Docker 상태 기반384 branch를 비교했으나 위험·보정 악화 joint gate를 통과하지 못해 현재 진단은 HOLD다. 이는 image/language 정책 실행이나 VLA 성능의 부정 결과가 아니다. ABot의 검토한 pose/occupancy loop에는 reactive pedestrian·physical clock의 연결이 미확인이며 native VLA는 HOLD다. 이미지/언어가 route 선택을 바꾸는 task와 checkpoint/controller/time/evaluator packet을 따로 확보해야 한다.

### 숨은 시연 정보·coverage 연결 — GAP-CF1/CF2

[GAP-CF1 비교](../work/update/CAUSAL_INFORMATION_COVERAGE_REVIEW_2026-10-23.md)는 causal IL·연속 flow RL·CofactVLA와 학습용 cue를 쓰는 CIVIL의 직접 선행을 확인했다. 일반 deconfounding 적용이나 cue 대 시연량 비교 자체는 NO-GO다. CofactVLA 공개 구현은 task와 discretized robot state를 담은 text 전체를 counterfactual branch에서 가리므로, instruction-only 비교에서는 proprio를 보존해야 한다. Model 내부 개입을 환경의 hidden confounder 식별로 해석하지 않는다. 배포 정보를 고정한 조건부 수집 가치 진단은 REVISE/HOLD이며, canonical 질문·기각 조건은 [GAP-CAUSAL](./02_rl_il_offline.md#gap-causal-2026)에 둔다.

[GAP-CF2 자료 심사](../work/update/CAUSAL_DATA_SUFFICIENCY_REVIEW_2026-10-23.md) 후 **현재 공개 자료를 쓰는 설계는 문헌 진단으로 종료**했다. 사후 language annotation·미래 state 차분 action·데이터 통합을 행동 전 시연 정보의 기록으로 바꾸어 해석하지 않는다. CIVIL의 비용 기록 코드는 확인했지만 전체 비교 자료 연결은 미확보다. 새 증거 없이 동일 schema 확인이나 GPU 확보만으로 재개하지 않는다.

<a id="gap-unified-vla-rl"></a>

### 단일 VLA 내부의 RL·가치 표현 공동 학습 — GAP-UNIFIED

2026-11-06 사용자 선호에 따라 [통합 모델 공백 검토](../work/research_topics/unified_vla_rl/내용/README.md)를 추가했다. **CURATION-HYPOTHESIS / 우선 탐색**이며 기존 pipeline 후보의 판정을 바꾸지 않는다. [NeurIPS 2025 RL4VLA](https://papers.nips.cc/paper_files/paper/2025/hash/8c0fabe372177d2aded596be2d3b4544-Abstract-Conference.html)는 shared actor–critic을, [ICML 2026 VLAC](https://proceedings.mlr.press/v306/zhang26if.html)는 action/progress의 통합 구조를 이미 다룬다. [ICLR 2025 representation study](https://proceedings.iclr.cc/paper_files/paper/2025/hash/57da66da25d0ce77e0129b246f358851-Abstract-Conference.html) 이후 일반 공유/분리 비교만으로 새 기여를 주장하지 않는다.

남길 질문은 **같은 관측에서도 언어가 행동을 바꾸어야 하는 조건에서 value loss가 공유 VLA 표현을 갱신하는 이득/손실이 달라지는가**다. Joint/detached-value/단순 loss 조정과 실제 목표 선택·task success를 대조한다. Shared backbone·단일 배포 정책·동일 가중치의 자기 보상은 서로 다르다. Source version, 공개 코드의 정적 경로 확인, 기존 FEEDBACK/VRL과의 차이, 후속 task/환경 계약은 위 주제 문서에 통합한다. Native 실행·효과는 미확인이고 사용자 reading status는 올리지 않았다.

**N1 보완:** [학습·목표 계약 검토](../work/research_topics/unified_vla_rl/내용/README.md#n1-review)에서 merged warm-up + 새 LoRA라는 초기화 범위, joint clipping의 간접 효과, 목표 변경 시 배치가 바뀌는 원 환경을 확인했다. 같은 상태의 goal binding과 group별 clipping을 설계했지만 feasibility·behavior는 미검증이다. VLAC(pr-1111)·actor–critic 표현 연구(pr-1112)를 NEXT에 등록했으며 일반 detach 비교 이상의 기여가 필요한 상태를 유지한다.

P0-PREP에서는 위 비교의 실행 코드를 작성하고 local Docker의 stdlib 제어 검사 15개를 통과했다. 이는 PyTorch gradient나 robot behavior의 검증이 아니며 `CURATION-HYPOTHESIS`를 유지한다. 실제 CUDA build·goal binding·gradient 경로는 [P0 재개](../work/research_topics/unified_vla_rl/재현%20방법/README.md#resume)에서 확인한다.

**N2 내부 비실험 검토 완료:** [비교·종료 기준](../work/research_topics/unified_vla_rl/내용/README.md#nonexperimental-completion)을 통합했다. VLAC **최종본 §4.7**은 reward·value·action logits의 PPO 사용을 명시하므로 이전 preprint의 모델 분리를 최종본에 전사하지 않는다. RL4VLA의 semantic/multi-object 평가도 이미 선행이다. 남는 질문은 목표별 행동에서 routing의 효과와 이를 설명하는 조건이다. 단일/다중 물체 차이를 언어의 순수한 효과로 쓰지 않으며, 단순 scale/optimizer·hidden history·수집 분포를 대조한다. 내부 설계 완료와 외부 응답 미수신·native 미실행·효과 미확인을 구분한다.

<a id="psi0-2026"></a>
## Ψ₀의 학습·제어 경계 — 2026-11-16

**Source-checked comparison; 사용자 정독 상태 승격 없음.** [Ψ₀](../2026/RSS/2026_RSS_An-Open-Foundation-Model-Towards-Universal-Humanoid-Loco-M/01_overview.md)는 RSS2026 논문이다. 지정 본문을 확인한 결과 VLM의 FAST 사전학습→frozen VLM의 flow action expert 후학습→별도 AMO 제어로 구성된다. 사전학습에는 EgoDex와 Humanoid Everyday가 함께 들어가므로 완전한 human-only 단계라고 요약하지 않는다. [원문 §III–IV](https://arxiv.org/html/2603.12263v1).

| 비교할 수준 | Ψ₀ v1에서 확인한 범위 | 연구 해석 경계 |
|---|---|---|
| VLA 표현·행동 학습 | Token prediction과 flow matching의 단계 구분 | 전체 VLA를 reward로 공동 갱신한 결과가 아님 |
| 전신 실행 | 별도 AMO RL 하위 제어기 | 단일 배포 경로와 단일 정책의 RL 학습은 별개 |
| 현재 공개 구현 | 후속 SONIC·새 데이터 recipe 포함 | 논문 당시 checkpoint/data/controller와 버전 구분 |
| 성공 평가 | 실패 subtask 이후 보조 개입 가능 | Subtask와 무개입 full-task 성공을 구분 |

**Open question — 연구자 해석:** 고정 데이터·controller·물리 시간에서 VLA reward update가 지시별 행동 구별과 복구를 함께 개선하는가? 단순 unfreeze·데이터 선택·controller 차이로 설명되는 이득을 제외해야 한다. 기존 UNIFIED/LANGRET 질문의 통제변수를 보강하며 후보 gate·실행 우선순위는 변경하지 않는다. [구체적 평가 경계](../2026/RSS/2026_RSS_An-Open-Foundation-Model-Towards-Universal-Humanoid-Loco-M/04_evaluation.md).
