# GroundFlow: A Plug-in Module for Temporal Reasoning on 3D Point Cloud Sequential Grounding

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Lin_GroundFlow_A_Plug-in_Module_for_Temporal_Reasoning_on_3D_Point_ICCV_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Lin_GroundFlow_A_Plug-in_Module_for_Temporal_Reasoning_on_3D_Point_ICCV_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: 3D Vision
- Official paper: https://openaccess.thecvf.com/content/ICCV2025/html/Lin_GroundFlow_A_Plug-in_Module_for_Temporal_Reasoning_on_3D_Point_ICCV_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/ICCV2025/papers/Lin_GroundFlow_A_Plug-in_Module_for_Temporal_Reasoning_on_3D_Point_ICCV_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 While 3D LLMs achieve state-of-the-art results in various 3D tasks, they still face significant difficulty adapting to the complex SG3D problem [52].를 문제로 두고, In summary, we make the following contributions: • We propose the GroundFlow module with a recurrent framework, which can be integrated into previous 3DVG baselines and introduce important temporal reasoning capabilities to ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Sequential grounding in 3D point clouds (SG3D) refers to locating sequences of objects by following text instructions for a daily activity with detailed steps.
- **p. 1 / Abstract - extractive body cue:** Current 3D visual grounding (3DVG) methods treat text instructions with multiple steps as a whole, without extracting useful temporal information from each step.
- **p. 1 / Abstract - extractive body cue:** However, the instructions in SG3D often contain pronouns such as "it", "here" and "the same" to make language expressions concise.
- **p. 1 / Abstract - extractive body cue:** This requires grounding methods to understand the context and retrieve relevant information from previous steps to correctly locate object sequences.
- **p. 1 / Abstract - extractive body cue:** Due to the lack of an effective module for collecting related historical information, state-of-theart 3DVG methods face significant challenges in adapting to the SG3D task.
- **p. 2 / 1. Introduction - extractive body cue:** While 3D LLMs achieve state-of-the-art results in various 3D tasks, they still face significant difficulty adapting to the complex SG3D problem [52].
- **p. 2 / 1. Introduction - extractive body cue:** The main reason for the huge performance gap between the two tasks is that current 3DVG methods are not designed to reason over historical information.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** In summary, we make the following contributions: • We propose the GroundFlow module with a recurrent framework, which can be integrated into previous 3DVG baselines ...
- **p. 2 / 1. Introduction - extractive body cue:** In addition, we propose GroundFlow module, which can be built on top of the existing 3DVG methods to perform temporal fusion with previous step embeddings, ...
- **p. 5 / 3.3. Training Objective - extractive body cue:** Detailed illustration of Memory component in GroundFlow, which enables the module to extract relevant information of both short-term ( ˆJt-1) and long-term ( ˆJm) effectively.
- **p. 5 / 3.3. Training Objective - extractive body cue:** Following the SG3D benchmark [52], we use the same cross-entropy loss to optimize the dual-stream model and the query-based model.
- **p. 5 / 3.3. Training Objective - extractive body cue:** In addition to the loss of token predictions when pre-trained on other datasets, an extra cross-entropy loss is incorporated to fine-tune the model on SG3D ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | As shown, GroundFlow module's output ˆJt will be treated as input in the next step t + 1. studied task that requires the agent to locate the target objects in 3D scenes ... | RGB-D, image set, point cloud, depth와 camera pose | p. 1 (1. Introduction), p. 2 (1. Introduction) |
| State/latent | GroundFlow, module, output, will, treated, input, next, step, studied, task, requires, agent | geometry, map, object/relationship state | p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Output/action | This framework sequentially takes each step instruction and processes only the current step instruction as input rather than handling all prior text instructions simultaneously. | point map, pose, scene graph, affordance 또는 query result | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction) |
| Objective/outcome | As defined in Equation 7, the loss compares the predicted object score f(P, S) and the ground truth score O. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 5 (3.3. Training Objective), p. 5 (3.3. Training Objective) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** In summary, we make the following contributions: • We propose the GroundFlow module with a recurrent framework, which can be integrated into previous 3DVG baselines ...
- **p. 2 / 1. Introduction - extractive body cue:** In addition, we propose GroundFlow module, which can be built on top of the existing 3DVG methods to perform temporal fusion with previous step embeddings, ...
- **p. 5 / 3.3. Training Objective - extractive body cue:** Detailed illustration of Memory component in GroundFlow, which enables the module to extract relevant information of both short-term ( ˆJt-1) and long-term ( ˆJm) effectively.
- **p. 6 / 4.3. Comparison on SG3D Benchmark - extractive body cue:** On the other hand, significant performance improvements can be observed when these models are integrated with GroundFlow, as shown in the rows highlighted in orange.
- **p. 6 / 4.3. Comparison on SG3D Benchmark - extractive body cue:** However, the 3DVG methods combined with our proposed GroundFlow module outperform LEO across all five datasets, setting new state-of-the-art performance on SG3D benchmark.
- **p. 7 / 4.4. Ablation Study - extractive body cue:** To investigate whether GroundFlow can consistently improve task accuracy of the 3DVG methods in more challenging scenarios with a high number of steps, we create ...
- **p. 7 / 4.4. Ablation Study - extractive body cue:** Improvements after GroundFlow module is integrated in terms of task accuracy of 3D-VisTA and PQ3D across different step count subsets. various settings of short-term and ...
- **p. 5 / 4.1. Dataset and Evaluation Metrics - extractive body cue:** As defined in SG3D benchmark [52], all models' grounding performances is evaluated based on two key metrics: step accuracy (s-acc) and task accuracy (tacc).

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 6 (4.3. Comparison on SG3D Benchmark), p. 6 (4.3. Comparison on SG3D Benchmark) |
| Embodiment/environment | The benchmark utilizes real-world scenes from the SceneVerse [26], incorporating indoor scans from 5 different datasets - ScanNet [11], 3RScan [40], MultiScan [31], ARKitScenes [3] and HM3D [36]. | hardware/simulator version and reset protocol | p. 5 (4.1. Dataset and Evaluation Metrics), p. 6 (4.2. Implementation Details) |
| Dataset/benchmark | It is pre-trained on an extensive range of 3D tasks, including object captioning [30, 51], object referring [1, 18, 48], 3D QA [12, 15, 47] and 3D navigation [28, 33], achieving top ... | role, split, size and leakage | p. 5 (4.1. Dataset and Evaluation Metrics), p. 6 (4.2. Implementation Details), p. 6 (4.3. Comparison on SG3D Benchmark), p. 5 (4.2. Implementation Details) |
| Metric | To address these limitations, the memory component in GroundFlow computes similarity scores to selectively retrieve and integrate context-specific past information based on its relevance to the current step, leading to superior performa ... | definition, denominator, direction and uncertainty | p. 7 (4.4. Ablation Study), p. 5 (4.1. Dataset and Evaluation Metrics), p. 6 (4.3. Comparison on SG3D Benchmark) |
| Baseline/ablation | However, the 3DVG methods combined with our proposed GroundFlow module outperform LEO across all five datasets, setting new state-of-the-art performance on SG3D benchmark. | fair input/data/compute/action matching | p. 6 (4.3. Comparison on SG3D Benchmark), p. 5 (4.2. Implementation Details), p. 6 (4.4. Ablation Study) |

## Explicit Limitations and Failure Boundary

- **p. 6 / 4.3. Comparison on SG3D Benchmark - extractive body cue:** Their degraded performance is particularly reflected in their overall task accuracy, with three of the models are falling below 30%.
- **p. 7 / 4.4. Ablation Study - extractive body cue:** This advantage could stem from the limitations of existing methods: LSTM or GRU tends to forget longterm information.
- **p. 7 / 4.4. Ablation Study - extractive body cue:** Since previous step embeddings do not attend to this lost information, it cannot be carried forward to subsequent steps, even if it is essential for ...
- **p. 8 / 4.5. Qualitative Visualization - extractive body cue:** It is shown that PQ3D fails to correctly choose the target "Telephone", while PQ3D+GroundFlow makes the correct predictions of "Telephone" for both steps.

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 While 3D LLMs achieve state-of-the-art results in various 3D tasks, they still face significant difficulty adapting to the complex SG3D problem [52].를 문제로 두고, In summary, we make the following contributions: • We propose the GroundFlow module with a recurrent framework, which can be integrated into previous 3DVG baselines and introduce important temporal reasoning capabilities to ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction), p. 5 (3.3. Training Objective), p. 5 (3.3. Training Objective) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
