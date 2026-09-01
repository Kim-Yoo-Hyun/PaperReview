# Problem - RealVLG-R1: A Large-Scale Real-World Visual-Language Grounding Benchmark for Robotic Perception and Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Li_RealVLG-R1_A_Large-Scale_Real-World_Visual-Language_Grounding_Benchmark_for_Robotic_Perception_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Li_RealVLG-R1_A_Large-Scale_Real-World_Visual-Language_Grounding_Benchmark_for_Robotic_Perception_CVPR_2026_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (1. Introduction), p. 2 (1. Introduction)): In summary, current VLG and grasping research highlight a clear gap between semantic understanding and manipulation reasoning, making them insufficient for real-world robotic scenarios that require fine-grained, multi-modal perception.

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** Visual-language grounding aims to establish semantic correspondences between natural language and visual entities, enabling models to accurately identify and localize target objects based on textual ...
- **p. 1 / Abstract - extractive PDF cue:** Existing VLG approaches focus on coarse-grained, object-level localization, while traditional robotic grasping methods rely predominantly on geometric cues and lack language guidance, which limits their ...
- **p. 1 / Abstract - extractive PDF cue:** To address these limitations, we propose the RealVLG framework, which integrates the RealVLG11B dataset and the RealVLG-R1 model to unify real-world visual-language grounding and grasping ...
- **p. 1 / Abstract - extractive PDF cue:** RealVLG11B dataset provides multi-granularity annotations including bounding boxes, segmentation masks, grasp poses, contact points, and human-verified fine-grained language descriptions, covering approximately 165,000 images, over 800 ...
- **p. 1 / Abstract - extractive PDF cue:** Experimental results demonstrate that RealVLG supports zeroshot perception and manipulation in real-world unseen environments, establishing a unified semantic-visual multimodal benchmark that provides a comprehensive data ...
- **p. 2 / 1. Introduction - extractive PDF cue:** In summary, current VLG and grasping research highlight a clear gap between semantic understanding and manipulation reasoning, making them insufficient for real-world robotic scenarios that ...
- **p. 2 / 1. Introduction - extractive PDF cue:** To address these challenges, as shown in Fig.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | In summary, current VLG and grasping research highlight a clear gap between semantic understanding and manipulation reasoning, making them insufficient for real-world ... | defined robot simulator/hardware task suite | body wording is the source claim |
| Observation / input | During training, input images and task prompts are processed through a policy optimization module to generate candidate outputs, which are then updated ... | standardized observation, action, task state와 evaluation split | exact sensor/frame/preprocessing from PDF |
| State / latent | During, training, input, images, task, prompts, processed, through, policy, optimization | benchmark state/goal와 method decision | notation and tensor shape require body check |
| Output / action | Input, Output, Object, image, yellow, banana, under, white | policy/controller trajectory 또는 measured result | exact unit/frame/decoder require body check |
| Target outcome | comparable score and protocol validity | success metric, robustness, generalization과 reproducibility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | standardized episode e and interface; body terms: During, training, input, images, task, prompts, processed, through, policy, optimization | p. 2 (1. Introduction), p. 6 (4.3. Task-Specific Pipelines and Verifiable Rewards), p. 6 (4.2. Policy Optimization with Verifiable Rewards) |
| Decision / output variable | method trajectory/action; body terms: RealVLG, framework, unifies, visuallanguage, grounding, grasping, tasks, within | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 5 (4.1. Overview) |
| Objective / loss / cost | benchmark score and failure cost; cue terms: Furthermore, objective, RealVLG-R1, aims, maximize, expected, reward, while | p. 5 (4.2. Policy Optimization with Verifiable Rewards), p. 5 (4.2. Policy Optimization with Verifiable Rewards), p. 6 (4.2. Policy Optimization with Verifiable Rewards), p. 7 (4.3. Task-Specific Pipelines and Verifiable Rewards), p. 6 (4.2. Policy Optimization with Verifiable Rewards), p. 7 (4.3. Task-Specific Pipelines and Verifiable Rewards) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 7 (4.3. Task-Specific Pipelines and Verifiable Rewards), p. 6 (4.2. Policy Optimization with Verifiable Rewards), p. 6 (4.2. Policy Optimization with Verifiable Rewards) |
| Success / guarantee | comparable score and protocol validity | p. 7 (5.2. RealVLG Benchmark), p. 7 (5.1. Data Quality Evaluation), p. 8 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Introduction - extractive PDF cue:** To address these challenges, as shown in Fig.

## What the Paper Changes

PDF contribution framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 5 (4.1. Overview), p. 5 (4.1. Overview), p. 8 (Method)): 1, we propose the RealVLG framework, which unifies visuallanguage grounding and grasping tasks within a single research paradigm.

- **p. 2 / 1. Introduction - extractive PDF cue:** In summary, our main contributions are as follows: • RealVLG-11B Dataset: The largest real-world grounding and grasping dataset with multi-granularity annotations from semantic localization to ...
- **p. 5 / 4.1. Overview - extractive PDF cue:** 3, we propose a unified framework, RealVLG-R1, which fine-tunes pretrained LVLMs using a reinforcement-style optimization strategy inspired by DeepSeek-R1 [22].
- **p. 5 / 4.1. Overview - extractive PDF cue:** Furthermore, we introduce a Verifiable Reward Mechanism that dynamically evaluates and guides model predictions in terms of both semantic correctness and physical feasibility.
- **p. 8 / Method - extractive PDF cue:** Building upon this, our proposed RealVLG-R1 model employs Qwen2.5-VL as its backbone and is developed within the VERL framework [68].

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | Future work will extend RealVLG to 3D space, and explore efficient models such as SmolVLM [43] to improve ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 3 | Existing grasping datasets generally suffer from two major limitations. | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | The computation is designed to ensure that contact points accurately lie on the object surface: if the midpoint ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | Linguistic and grounding quality comparison. grasp points located within segmentation masks (Rg), and proportion of contact centers falling ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

benchmark writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 2 (1. Introduction), p. 6 (4.3. Task-Specific Pipelines and Verifiable Rewards), p. 6 (4.2. Policy Optimization with Verifiable Rewards), p. 2 (1. Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (1. Introduction), p. 2 (1. Introduction), interface p. 2 (1. Introduction), p. 6 (4.3. Task-Specific Pipelines and Verifiable Rewards), p. 6 (4.2. Policy Optimization with Verifiable Rewards), p. 2 (1. Introduction), objective p. 5 (4.2. Policy Optimization with Verifiable Rewards), p. 5 (4.2. Policy Optimization with Verifiable Rewards), p. 6 (4.2. Policy Optimization with Verifiable Rewards), p. 7 (4.3. Task-Specific Pipelines and Verifiable Rewards), p. 6 (4.2. Policy Optimization with Verifiable Rewards), p. 7 (4.3. Task-Specific Pipelines and Verifiable Rewards).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
