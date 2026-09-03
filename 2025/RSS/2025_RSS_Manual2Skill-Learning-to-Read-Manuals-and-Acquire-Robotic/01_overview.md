# Manual2Skill: Learning to Read Manuals and Acquire Robotic Skills for Furniture Assembly Using Vision-Language Models

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (26 pages; tesseract OCR fallback; title-token overlap first two pages=1.0); canonical paper source: https://www.roboticsproceedings.org/rss21/p150.html.
> PDF retrieval source: https://www.roboticsproceedings.org/rss21/p150.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / RSS
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: Robotics, VLM, assembly, task planning, 6D pose, long-horizon
- Official paper: https://www.roboticsproceedings.org/rss21/p150.html
- Full-text retrieval: https://www.roboticsproceedings.org/rss21/p150.pdf
- Code/Project: https://owensun2004.github.io/Furniture-Assembly-Web/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (26 pages; tesseract OCR fallback; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 For robots, however, this capability remains a substantial challenge, as they cannot interpret abstract instructions and translate them into executable actions.를 문제로 두고, In this paper, we present Manual2Skill, a novel framework that enables robots to perform complex assembly tasks guided by highleyel manual instructions.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Humans possess an extraordinary ability to under stand and execute complex manipulation tasks by interpreting abstract instruction manuals.
- **p. 1 / Abstract - extractive body cue:** For robots, however, this capability remains a substantial challenge, as they cannot interpret abstract instructions and translate them into executable actions.
- **p. 1 / Abstract - extractive body cue:** In this paper, we present Manual2Skill, a novel framework that enables robots to perform complex assembly tasks guided by highleyel manual instructions.
- **p. 1 / Abstract - extractive body cue:** Our approach leverages a VisionLanguage Model (VLM) to extract structured information from instructional images and then uses this information to construct hierarchical assembly graphs.
- **p. 1 / Abstract - extractive body cue:** These graphs represent parts, subassemblies, and the relationships between them.
- **p. 2 / A. Furniture Assembly - extractive body cue:** However, existing works typically focus on specific subproblems rather than addressing the entire assembly pipeline.
- **p. 3 / B. VLM Guided Robot Learning - extractive body cue:** However, they are mostly limited to tabletop manipulation tasks and do not generalize well to more complex, long-horizon assembly problems.

## Core Idea

- **p. 1 / Abstract - extractive body cue:** In this paper, we present Manual2Skill, a novel framework that enables robots to perform complex assembly tasks guided by highleyel manual instructions.
- **p. 2 / I. INrRopuction - extractive body cue:** In this paper, we propose Manual2Skill, a novel robot learn
- **p. 2 / I. INrRopuction - extractive body cue:** + We propose Manual2Skill, a novel framework that leverages VLM to learn robotic skills from manuals, enabling 4 generalizable assembly pipeline for IKEA furniture
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** We propose Manual2 ‘enabling robots to understand and execute complex manipulation tasks in mi the input of our pipeline: the pictures of the assembly manual ...
- **p. 3 / A. VLM Guided Hierarchical Assembly Graph Generation - extractive body cue:** Every VLM prompt consists of two components:
- **p. 14 / B. Pose Estimation Implementation - extractive body cue:** where tr(:) denotes the trace of a matrix and RT is the transpose of R. ‘Translation MSE Loss: Following [29], we use the mean
- **p. 15 / B. Pose Estimation Implementation - extractive body cue:** We then use this feature as input for the pose regressor MLP.
- **p. 17 / B. Pose Estimation Implementation - extractive body cue:** We then inonicalize the point cloud using the same PCA algorithm, ensuring that the relative 6D pose of the same component remains consistent.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | This triplet format enhances interpretability and ensures consistency by structuring all outputs into the same data format, We use the Image Set and Text Instructions as the input prompt for the VLM ... | image/video, language instruction, proprioception과 history | p. 4 (2. Per-step Assembly Pose Estimation), p. 17 (B. Pose Estimation Implementation) |
| State/latent | triplet, format, enhances, interpretability, ensures, consistency, structuring, outputs, same, data, Image, Set | language-grounded task state와 action-policy context | p. 4 (2. Per-step Assembly Pose Estimation), p. 17 (B. Pose Estimation Implementation), p. 2 (B. VLM Guided Robot Learning) |
| Output/action | During each step of the assembly proces the mesh-along with the RGB and depth images and an object mask-is input into the FoundationPose model, which then generates the precise 6D pose and ... | continuous action, pose 또는 action chunk | p. 17 (B. Pose Estimation Implementation), p. 2 (B. VLM Guided Robot Learning), p. 3 (A. VLM Guided Hierarchical Assembly Graph Generation) |
| Objective/outcome | Chamfer Distance Loss: This loss function minimizes the holistic distance between each point in the predicted and ground truth point clouds. | instruction following, task success, generalization과 latency | p. 14 (B. Pose Estimation Implementation), p. 14 (B. Pose Estimation Implementation), p. 15 (B. Pose Estimation Implementation) |

## Main Claims and Actual Contribution

- **p. 1 / Abstract - extractive body cue:** In this paper, we present Manual2Skill, a novel framework that enables robots to perform complex assembly tasks guided by highleyel manual instructions.
- **p. 2 / I. INrRopuction - extractive body cue:** In this paper, we propose Manual2Skill, a novel robot learn
- **p. 2 / I. INrRopuction - extractive body cue:** + We propose Manual2Skill, a novel framework that leverages VLM to learn robotic skills from manuals, enabling 4 generalizable assembly pipeline for IKEA furniture
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** We propose Manual2 ‘enabling robots to understand and execute complex manipulation tasks in mi the input of our pipeline: the pictures of the assembly manual ...
- **p. 3 / A. VLM Guided Hierarchical Assembly Graph Generation - extractive body cue:** Every VLM prompt consists of two components:
- **p. 9 / C. Overall Performance Evaluation - extractive body cue:** We present the results in Table IV, showing that our method outperforms the baseline and achieves a high success rate in real-world assembly tasks.
- **p. 8 / C. Overall Performance Evaluation - extractive body cue:** Our framework achieves a success rate of $8%, demonstrating the effectiveness of our proposed framework.
- **p. 16 / B. Pose Estimation Implementation - extractive body cue:** As shown in Table X (Ours (w/o Segmentation)), this method significantly impair VLM performance in generating assembly graphs, leading to more than double accuracy drops ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 9 (C. Overall Performance Evaluation), p. 8 (C. Overall Performance Evaluation) |
| Embodiment/environment | Failures occur when the RRTConnect algorithm cannot find a feasible trajectory when the planned path results in collisions with the robotic arm or surrounding objects or due to suboptimal grasping poses. | hardware/simulator version and reset protocol | p. 9 (C. Overall Performance Evaluation), p. 8 (C. Overall Performance Evaluation) |
| Dataset/benchmark | We source all test furniture models from the IKEA-Manuals dataset [49] Given these manuals along with 3D parts, we generate the preassembly scene images as deseribed in. | role, split, size and leakage | p. 9 (C. Overall Performance Evaluation), p. 8 (C. Overall Performance Evaluation), p. 8 (C. Overall Performance Evaluation), p. 9 (C. Overall Performance Evaluation) |
| Metric | As shown in Table X (Ours (w/o Segmentation)), this method significantly impair VLM performance in generating assembly graphs, leading to more than double accuracy drops in success rate. | definition, denominator, direction and uncertainty | p. 16 (B. Pose Estimation Implementation), p. 8 (C. Overall Performance Evaluation), p. 8 (C. Overall Performance Evaluation) |
| Baseline/ablation | We present the results in Table IV, showing that our method outperforms the baseline and achieves a high success rate in real-world assembly tasks. | fair input/data/compute/action matching | p. 9 (C. Overall Performance Evaluation), p. 16 (B. Pose Estimation Implementation), p. 8 (C. Overall Performance Evaluation) |

## Explicit Limitations and Failure Boundary

- **p. 9 / C. Overall Performance Evaluation - extractive body cue:** Failures occur when the RRTConnect algorithm cannot find a feasible trajectory when the planned path results in collisions with the robotic arm or surrounding objects ...
- **p. 9 / C. Overall Performance Evaluation - extractive body cue:** failure mode arises from planning limitations, particularly in handling complex obstacles.
- **p. 8 / C. Overall Performance Evaluation - extractive body cue:** The most common failure occurs when the VLM fails to generate a fully accurate assembly graph, leading to misalignment between the point cloud and the ...
- **p. 8 / C. Overall Performance Evaluation - extractive body cue:** We adopt the assembly success rate as the evaluation metric and define the following situations as a failure: 1) A partis placed at a pose ...
- **p. 16 / B. Pose Estimation Implementation - extractive body cue:** Manually inspecting each assembly plan reveals common failure modes: the VLM frequently misidentifies parts (e.g. labeling a bench seat as a "tabletop"), generates physically plausible ...
- **p. 17 / B. Pose Estimation Implementation - extractive body cue:** We analyze the faire cases in assembly graph generation mek os The most ffequent failure modes inchude: (1) The VLM a ae]
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 3: Qualitative results. Our method significantly outper- forms the baselines. SingleStep fails on moderately complex furniture, while GeoCluster generates physically impossible subassemblies (highlighted in ...

## Why Read It

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 For robots, however, this capability remains a substantial challenge, as they cannot interpret abstract instructions and translate them into executable actions.를 문제로 두고, In this paper, we present Manual2Skill, a novel framework that enables robots to perform complex assembly tasks guided by highleyel manual instructions.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (Abstract), p. 2 (A. Furniture Assembly), p. 3 (B. VLM Guided Robot Learning), p. 1 (I. INrRopuction), p. 2 (A. Furniture Assembly), p. 14 (B. Pose Estimation Implementation) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (26 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** For robots, however, this capability remains a substantial challenge, as they cannot interpret abstract instructions and translate them into executable actions. (p. 1, Abstract).
- **Actual contribution:** In this paper, we present Manual2Skill, a novel framework that enables robots to perform complex assembly tasks guided by highleyel manual instructions. (p. 1, Abstract).
- **Evaluation boundary:** We present the results in Table IV, showing that our method outperforms the baseline and achieves a high success rate in real-world assembly tasks. (p. 9, C. Overall Performance Evaluation).
- **Explicit failure boundary:** Failures occur when the RRTConnect algorithm cannot find a feasible trajectory when the planned path results in collisions with the robotic arm or surrounding objects or due to suboptimal grasping ... (p. 9, C. Overall Performance Evaluation).
