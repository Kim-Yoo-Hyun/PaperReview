# VLM-Grounder: A VLM Agent for Zero-Shot 3D Visual Grounding

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (25 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.mlr.press/v270/xu25c.html.
> PDF retrieval source: https://raw.githubusercontent.com/mlresearch/v270/main/assets/xu25c/xu25c.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / CoRL
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: 3D visual grounding, VLM, zero-shot
- Official paper: https://proceedings.mlr.press/v270/xu25c.html
- Full-text retrieval: https://raw.githubusercontent.com/mlresearch/v270/main/assets/xu25c/xu25c.pdf
- Code/Project: https://github.com/InternRobotics/VLM-Grounder
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (25 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, existing visual grounding datasets[1, 2] are scarce and limited to a pre-defined vocabulary, challenging the development of general models for open-world applications.를 문제로 두고, While these methods achieve strong performance, they use only objectcentric information and often miss detailed scene context, making it challenging to handle queries like "find the room with the most abundant natural ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** 3D visual grounding is crucial for robots, requiring integration of natural language and 3D scene understanding.
- **p. 1 / Abstract - extractive body cue:** Traditional methods depending on supervised learning with 3D point clouds are limited by scarce datasets.
- **p. 1 / Abstract - extractive body cue:** Recently zero-shot methods leveraging LLMs have been proposed to address the data issue.
- **p. 1 / Abstract - extractive body cue:** While effective, these methods only use object-centric information, limiting their ability to handle complex queries.
- **p. 1 / Abstract - extractive body cue:** In this work, we present VLM-Grounder, a novel framework using vision-language models (VLMs) for zero-shot 3D visual grounding based solely on 2D images.
- **p. 1 / 1 Introduction - extractive body cue:** However, existing visual grounding datasets[1, 2] are scarce and limited to a pre-defined vocabulary, challenging the development of general models for open-world applications.
- **p. 1 / 1 Introduction - extractive body cue:** Since LLMs cannot directly process 3D environments, these methods employ a point cloud-based 3D localization module [10, 11] to detect objects and convert their attributes ...

## Core Idea

- **p. 1 / 1 Introduction - extractive body cue:** While these methods achieve strong performance, they use only objectcentric information and often miss detailed scene context, making it challenging to handle queries like "find ...
- **p. 2 / 1 Introduction - extractive body cue:** Further, we propose a dynamic stitching strategy that dynamically uses the optimal layouts identified by the benchmark to stitch images, enhancing VLM's performance.
- **p. 3 / 3 Methodology - extractive body cue:** In this section, we present the overall framework of VLM-Grounder (Sec.
- **p. 4 / 3 Methodology - extractive body cue:** To study the effects of stitching, we designed a novel benchmark called the VisualRetrieval Benchmark, detailed in Sec.
- **p. 1 / 1 Introduction - extractive body cue:** Our approach involves a VLM that analyzes user queries and sequences of images capturing the scene to locate the target object, whose 2D mask is ...
- **p. 7 / 3 Methodology - extractive body cue:** Without model training, VLM-Grounder's overall performance also competes with supervised learning methods like InstanceRefer (38.8%) and 3DVG-Transformer (40.8%).
- **p. 8 / 3 Methodology - extractive body cue:** VLM-Grounder has several appealing properties: it leverages foundation models from the language and 2D domains without training, and offers a more transparent and explainable grounding ...
- **p. 3 / 3 Methodology - extractive body cue:** 3.1), and detail the motivations and specifics of three key modules: dynamic stitching (Sec.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | 2) Inputting many images quickly consumes the VLM's context length, limiting output content and potentially affecting performance. | RGB-D, image set, point cloud, depth와 camera pose | p. 4 (3 Methodology), p. 4 (3 Methodology) |
| State/latent | Inputting, many, images, quickly, consumes, VLM, context, length, limiting, output, content, potentially | geometry, map, object/relationship state | p. 4 (3 Methodology), p. 4 (3 Methodology), p. 7 (3 Methodology) |
| Output/action | The target image and bounding box are input into the Segment Anything Model (SAM) [52] to obtain a fine-grained mask. | point map, pose, scene graph, affordance 또는 query result | p. 4 (3 Methodology), p. 7 (3 Methodology), p. 7 (3 Methodology) |
| Objective/outcome | 3) More images increase inference costs, including token usage, latency, and timeout risk. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 4 (3 Methodology), p. 4 (3 Methodology), p. 5 (3 Methodology) |

## Main Claims and Actual Contribution

- **p. 1 / 1 Introduction - extractive body cue:** While these methods achieve strong performance, they use only objectcentric information and often miss detailed scene context, making it challenging to handle queries like "find ...
- **p. 2 / 1 Introduction - extractive body cue:** Further, we propose a dynamic stitching strategy that dynamically uses the optimal layouts identified by the benchmark to stitch images, enhancing VLM's performance.
- **p. 3 / 3 Methodology - extractive body cue:** In this section, we present the overall framework of VLM-Grounder (Sec.
- **p. 4 / 3 Methodology - extractive body cue:** To study the effects of stitching, we designed a novel benchmark called the VisualRetrieval Benchmark, detailed in Sec.
- **p. 1 / 1 Introduction - extractive body cue:** Our approach involves a VLM that analyzes user queries and sequences of images capturing the scene to locate the target object, whose 2D mask is ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1: 3D visual grounding results on ScanRefer. Without using geometric information from point clouds, VLM-Grounder outperforms previous zero-shot methods and achieves performance comparable to ...
- **p. 8 / 3 Methodology - extractive body cue:** As shown in our results, the proposed dynamic stitching outperforms the others, demonstrating its efficacy.
- **p. 8 / 3 Methodology - extractive body cue:** 5 shows a clear performance improvement with each additional component, confirming the importance and effectiveness of these operations.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | SYSTEM / EVALUATION SCOPE UNRESOLVED | do not infer unreported downstream behavior | p. 6 (Figure/Table caption), p. 8 (3 Methodology) |
| Embodiment/environment | We introduced a novel Visual-Retrieval benchmark to evaluate the impact of stitching operations on VLM's visual understanding. | hardware/simulator version and reset protocol | p. 8 (3 Methodology), p. 8 (3 Methodology) |
| Dataset/benchmark | We introduced a novel Visual-Retrieval benchmark to evaluate the impact of stitching operations on VLM's visual understanding. | role, split, size and leakage | p. 8 (3 Methodology), p. 8 (3 Methodology) |
| Metric | Table 10: Success rates of different modules. Query Analysis View Pre-Selection Image Selection by VLM OV-Detection 100% 96% 77% | definition, denominator, direction and uncertainty | p. 19 (Figure/Table caption), p. 7 (Figure/Table caption), p. 8 (Figure/Table caption) |
| Baseline/ablation | Table 1: 3D visual grounding results on ScanRefer. Without using geometric information from point clouds, VLM-Grounder outperforms previous zero-shot methods and achieves performance comparable to supervised learning baselines. * indica ... | fair input/data/compute/action matching | p. 6 (Figure/Table caption), p. 8 (Figure/Table caption), p. 8 (3 Methodology) |

## Explicit Limitations and Failure Boundary

- **p. 20 / Figure/Table caption - extractive body cue:** Figure 5: Failure cases of the VLM grounding module. 20
- **p. 21 / Figure/Table caption - extractive body cue:** Figure 8: A failure case of the projection module. 21
- **p. 6 / 3 Methodology - extractive body cue:** Although our multi-view ensemble projection module helps mitigate this issue, it cannot entirely eliminate it.
- **p. 8 / 3 Methodology - extractive body cue:** 5 Conclusion and Limitations In this paper, we presented VLM-Grounder, a VLM agent that excels in zero-shot 3D visual grounding.
- **p. 8 / 3 Methodology - extractive body cue:** Further discussions on limitations, error analysis, inferencing time, and qualitative results are provided in the supplementary material.
- **p. 5 / 3 Methodology - extractive body cue:** VLM-Grounder does not need such priors for input, so we match our predicted box to the ground truth box with the closest center and use ...
- **p. 6 / 3 Methodology - extractive body cue:** These estimated parameters often contain noise, causing inaccuracies in the predicted 3D bounding boxes, e.g., a single outlier can result in an overly large bounding ...

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, existing visual grounding datasets[1, 2] are scarce and limited to a pre-defined vocabulary, challenging the development of general models for open-world applications.를 문제로 두고, While these methods achieve strong performance, they use only objectcentric information and often miss detailed scene context, making it challenging to handle queries like "find the room with the most abundant natural ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 7 (3 Methodology), p. 8 (3 Methodology) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
