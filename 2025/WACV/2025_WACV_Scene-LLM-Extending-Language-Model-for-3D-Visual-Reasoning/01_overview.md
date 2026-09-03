# Scene-LLM: Extending Language Model for 3D Visual Reasoning

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/WACV2025/html/Fu_Scene-LLM_Extending_Language_Model_for_3D_Visual_Reasoning_WACV_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/WACV2025/papers/Fu_Scene-LLM_Extending_Language_Model_for_3D_Visual_Reasoning_WACV_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / WACV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: LLM, 3D visual reasoning, Vision-Language
- Official paper: https://openaccess.thecvf.com/content/WACV2025/html/Fu_Scene-LLM_Extending_Language_Model_for_3D_Visual_Reasoning_WACV_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/WACV2025/papers/Fu_Scene-LLM_Extending_Language_Model_for_3D_Visual_Reasoning_WACV_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Current models [15, 19, 42] typically focus on one of these aspects or process them with separate models, hindering their effectiveness in tasks like interactive indoor planning that require both.를 문제로 두고, In summary, our primary contributions are: • We introduce Scene-LLM, a 3D-VLM that connecting 3D visual information with LLM and sets new stateof-the-art on 3D-VQA and interactive planning benchmarks; • We show ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** This paper introduces Scene-LLM, a 3D-visuallanguage model that enhances embodied agents' abilities in interactive 3D indoor environments by integrating the reasoning strengths of Large Language ...
- **p. 1 / Abstract - extractive body cue:** Scene-LLM adopts a unified 3D visual feature representation, that incorporates dense spatial information and supports scene state updates.
- **p. 1 / Abstract - extractive body cue:** The model employs a projection layer to efficiently project these features in the pre-trained textual embedding space, enabling effective interpretation of 3D visual information.
- **p. 1 / Abstract - extractive body cue:** Unique to our approach is the integration of both scene-level and egocentric 3D information with a compact hybrid representation.
- **p. 1 / Abstract - extractive body cue:** This combination is pivotal for interactive 1*Work done as an intern at Meta AI.
- **p. 2 / 1. Introduction - extractive body cue:** Current models [15, 19, 42] typically focus on one of these aspects or process them with separate models, hindering their effectiveness in tasks like interactive ...
- **p. 2 / 1. Introduction - extractive body cue:** While existing visuallanguage models (VLMs) [5, 15, 34] have made strides in 2D visual-language understanding, their limited grasp of persistent 3D spatial information often renders ...

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** In summary, our primary contributions are: • We introduce Scene-LLM, a 3D-VLM that connecting 3D visual information with LLM and sets new stateof-the-art on 3D-VQA ...
- **p. 2 / 1. Introduction - extractive body cue:** To overcome this, we propose integrating both types of 3D visual information to an unified visual feature in Scene-LLM.
- **p. 1 / Abstract - extractive body cue:** Unique to our approach is the integration of both scene-level and egocentric 3D information with a compact hybrid representation.
- **p. 1 / Body text (section not recovered) - extractive body cue:** We showcase some applications, including describing scene details (scene captioning), identifying and describing objects (object captioning), breaking down complex tasks into simpler steps (task decomposition), ...
- **p. 3 / 3. 3D-Visual-Language Data Generation - extractive body cue:** Our dataset comprises about 9, 000 indoor scenes from three sources: real indoor scans [14], single rooms from the Habitat-Matterport 3D dataset (hm3d) [53], and ...
- **p. 4 / 4. Scene-LLM - extractive body cue:** This section outlines the 3D visual feature extraction process, model architecture, 3D visual information alignment, and the inference process.
- **p. 5 / 4.1. 3D Visual Feature - extractive body cue:** The scene semantic feature is then updated using: \l abe l {eq u a ti o n: u p da te} \t extbf {F}^{vox}_{t+1} = ...
- **p. 1 / Abstract - extractive body cue:** Notably, we use egocentric 3D frame features for feature alignment, an efficient technique that incorporates the model with fine-grained concepts.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | At the egocentric step, 3D frame data and a egocentric instruction are first input to Scene-LLM to describe the current state. | RGB-D, image set, point cloud, depth와 camera pose | p. 5 (4.3. Inference), p. 5 (4.3. Inference) |
| State/latent | egocentric, step, frame, data, instruction, first, input, Scene-LLM, describe, current, state, updated | geometry, map, object/relationship state | p. 5 (4.3. Inference), p. 5 (4.3. Inference), p. 7 (C VoteNet+MCAN [78]) |
| Output/action | The updated scene feature, along with the state description and user instructions, are fed into Scene-LLM to yield the corresponding response. | point map, pose, scene graph, affordance 또는 query result | p. 5 (4.3. Inference), p. 7 (C VoteNet+MCAN [78]), p. 4 (3.1. Frame Data Generation) |
| Objective/outcome | Then, the 3D scene feature is updated as per Equation 1. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 5 (4.3. Inference), p. 1 (Abstract), p. 2 (1. Introduction) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** In summary, our primary contributions are: • We introduce Scene-LLM, a 3D-VLM that connecting 3D visual information with LLM and sets new stateof-the-art on 3D-VQA ...
- **p. 2 / 1. Introduction - extractive body cue:** To overcome this, we propose integrating both types of 3D visual information to an unified visual feature in Scene-LLM.
- **p. 1 / Abstract - extractive body cue:** Unique to our approach is the integration of both scene-level and egocentric 3D information with a compact hybrid representation.
- **p. 1 / Body text (section not recovered) - extractive body cue:** We showcase some applications, including describing scene details (scene captioning), identifying and describing objects (object captioning), breaking down complex tasks into simpler steps (task decomposition), ...
- **p. 3 / 3. 3D-Visual-Language Data Generation - extractive body cue:** Our dataset comprises about 9, 000 indoor scenes from three sources: real indoor scans [14], single rooms from the Habitat-Matterport 3D dataset (hm3d) [53], and ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 5. High-level planning accuracy(HLP) on Alfred dataset valid unseen/seen set with different inference strategy. Full model outperform strategies without egocentric and scene state updates. ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 3. Result on Alfred dataset on test unseen/seen set and valid unseen/seen set. The metrics reported include success rate (SR), goal-conditioned success rate(GC), and ...
- **p. 5 / 5. Experiments - extractive body cue:** The inference setup, more results and analysis are detailed in the supplementary material.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 8 (Figure/Table caption), p. 7 (Figure/Table caption) |
| Embodiment/environment | This benchmark tests a model's ability to understand 3D scenes using questionanswering tasks using ScanNet dataset [14]. | hardware/simulator version and reset protocol | p. 5 (5.1. Results and Benchmark Evaluation), p. 5 (5.1. Results and Benchmark Evaluation) |
| Dataset/benchmark | Responses for the top 3 non-interactive scenes are generated without task-specific finetuning, and those for the bottom interactive scene are generated with finetuning. | role, split, size and leakage | p. 5 (5.1. Results and Benchmark Evaluation), p. 5 (5.1. Results and Benchmark Evaluation), p. 6 (5.1. Results and Benchmark Evaluation), p. 6 (5.1. Results and Benchmark Evaluation) |
| Metric | Table 3. Result on Alfred dataset on test unseen/seen set and valid unseen/seen set. The metrics reported include success rate (SR), goal-conditioned success rate(GC), and high-level planning accu- racy(HLP). The notation "(s)" ... | definition, denominator, direction and uncertainty | p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 5 (5. Experiments) |
| Baseline/ablation | Our evaluation of Scene-LLM on 3D visual question answering (3D-VQA) benchmarks is summarized in Table 1 for ScanQA and Table 2 for SQA3D, comparing it against other baseline methods. | fair input/data/compute/action matching | p. 6 (5.1. Results and Benchmark Evaluation), p. 8 (Figure/Table caption), p. 5 (5. Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 6. Conclusion - extractive body cue:** Scene-LLM faces limitations such as LLM input token length, challenges in processing dynamic scenes without a state detector, lacking geometry feature, and language hallucinations.
- **p. 6 / 5.1. Results and Benchmark Evaluation - extractive body cue:** A: To enhance safety, consider laying down anti-slip mats by the sink and in any zones where spills are likely to happen.
- **p. 8 / 5.2. Ablation Studies and Discussions - extractive body cue:** While Q-Former is a robust downsampling technique, it exhibits slightly lower performance compared to direct spatial down-sampling in our benchmarks, aligning with findings from [38].
- **p. 6 / 5.1. Results and Benchmark Evaluation - extractive body cue:** It measures the ability to create precise and robust plans from a high-level goal in 3D interactive environments from iTHOR [1].

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Current models [15, 19, 42] typically focus on one of these aspects or process them with separate models, hindering their effectiveness in tasks like interactive indoor planning that require both.를 문제로 두고, In summary, our primary contributions are: • We introduce Scene-LLM, a 3D-VLM that connecting 3D visual information with LLM and sets new stateof-the-art on 3D-VQA and interactive planning benchmarks; • We show ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (4. Scene-LLM), p. 5 (4.1. 3D Visual Feature), p. 1 (Abstract) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
