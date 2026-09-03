# RoboRefer: Towards Spatial Referring with Reasoning in Vision-Language Models for Robotics

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (71 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=OGxalNUHbJ.
> PDF retrieval source: https://openreview.net/pdf/81387e1e7f5169279b63c293ca88b1e4a8bc7e35.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / NeurIPS
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: NEXT
- Tags: Vision-Language Model, Robotics, 3D Vision
- Official paper: https://openreview.net/forum?id=OGxalNUHbJ
- Full-text retrieval: https://openreview.net/pdf/81387e1e7f5169279b63c293ca88b1e4a8bc7e35.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (71 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Thus, this work attempts to address this gap by integrating both levels for comprehensive spatial referring.를 문제로 두고, Our contributions are summarized as follows: (1) We propose RoboRefer, a 3D-aware reasoning VLM trained using a sequential SFT-RFT strategy with metric-sensitive process reward functions to achieve spatial referring.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Spatial referring is a fundamental capability of embodied robots to interact with the 3D physical world.
- **p. 1 / Abstract - extractive body cue:** However, even with the powerful pretrained vision language models (VLMs), recent approaches are still not qualified to accurately understand the complex 3D scenes and dynamically ...
- **p. 1 / Abstract - extractive body cue:** To this end, we propose RoboRefer, a 3D-aware VLM that can first achieve precise spatial understanding by integrating a disentangled but dedicated depth encoder via ...
- **p. 1 / Abstract - extractive body cue:** Moreover, RoboRefer advances generalized multi-step spatial reasoning via reinforcement fine-tuning (RFT), with metric-sensitive process reward functions tailored for spatial referring tasks.
- **p. 1 / Abstract - extractive body cue:** To support SFT and RFT training, we introduce RefSpatial, a large-scale dataset of 20M QA pairs (2× prior), covering 31 spatial relations (vs.
- **p. 2 / 1 Introduction - extractive body cue:** Thus, this work attempts to address this gap by integrating both levels for comprehensive spatial referring.
- **p. 3 / 1 Introduction - extractive body cue:** To address the lack of multi-step spatial referring benchmarks, we introduce RefSpatial-Bench, comprising 200 real-world images with manually annotated tasks for object location and placement.

## Core Idea

- **p. 3 / 1 Introduction - extractive body cue:** Our contributions are summarized as follows: (1) We propose RoboRefer, a 3D-aware reasoning VLM trained using a sequential SFT-RFT strategy with metric-sensitive process reward functions ...
- **p. 2 / 1 Introduction - extractive body cue:** To advance spatial referring, we introduce RefSpatial, a large-scale dataset of 2.5M high-quality examples with 20M QA pairs (2× prior [3]).
- **p. 2 / 1 Introduction - extractive body cue:** In this work, we propose RoboRefer, a 3D-aware VLM that not only acquires precise spatial understanding via SFT but also exhibits generalized strong reasoning capabilities ...
- **p. 3 / 1 Introduction - extractive body cue:** To address the lack of multi-step spatial referring benchmarks, we introduce RefSpatial-Bench, comprising 200 real-world images with manually annotated tasks for object location and placement.
- **p. 4 / 3 Method - extractive body cue:** To address this, we propose a simple yet effective approach: a dedicated depth encoder and projector, initialized from their RGB counterparts.
- **p. 3 / 3 Method - extractive body cue:** Then, we elaborate on RoboRefer, including its architecture and training strategies (Sec.
- **p. 4 / 3 Method - extractive body cue:** 2, RoboRefer employs separate RGB and depth encoders to extract features, which are then aligned via projectors with the LLM for VQA or point prediction.
- **p. 49 / C Implementation Details and Samples of RefSpatial-Bench - extractive body cue:** D.4.1 Sampling Action Groups Given an input state s = (O, Q), where O denotes the visual encoding of the RGB or RGB-D observation and ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | D.4.1 Sampling Action Groups Given an input state s = (O, Q), where O denotes the visual encoding of the RGB or RGB-D observation and Q the textual encoding of the question, ... | RGB-D, image set, point cloud, depth와 camera pose | p. 49 (C Implementation Details and Samples of RefSpatial-Bench), p. 4 (3 Method) |
| State/latent | Sampling, Action, Groups, Given, input, state, where, denotes, visual, encoding, RGB, RGB-D | geometry, map, object/relationship state | p. 49 (C Implementation Details and Samples of RefSpatial-Bench), p. 4 (3 Method), p. 4 (3 Method) |
| Output/action | 3.1 Problem Formulation We formulate spatial referring as predicting a single 2D point (x, y) in image space to specify a target location or destination, given visual inputs O (e.g., RGB or ... | point map, pose, scene graph, affordance 또는 query result | p. 4 (3 Method), p. 4 (3 Method), p. 7 (3 Method) |
| Objective/outcome | Unlike PPO [154], which relies on a costly value network, GRPO estimates relative advantages by comparing intra-group rewards, reducing computation, and simplifying optimization. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 49 (C Implementation Details and Samples of RefSpatial-Bench), p. 48 (C Implementation Details and Samples of RefSpatial-Bench), p. 5 (3 Method) |

## Main Claims and Actual Contribution

- **p. 3 / 1 Introduction - extractive body cue:** Our contributions are summarized as follows: (1) We propose RoboRefer, a 3D-aware reasoning VLM trained using a sequential SFT-RFT strategy with metric-sensitive process reward functions ...
- **p. 2 / 1 Introduction - extractive body cue:** To advance spatial referring, we introduce RefSpatial, a large-scale dataset of 2.5M high-quality examples with 20M QA pairs (2× prior [3]).
- **p. 2 / 1 Introduction - extractive body cue:** In this work, we propose RoboRefer, a 3D-aware VLM that not only acquires precise spatial understanding via SFT but also exhibits generalized strong reasoning capabilities ...
- **p. 3 / 1 Introduction - extractive body cue:** To address the lack of multi-step spatial referring benchmarks, we introduce RefSpatial-Bench, comprising 200 real-world images with manually annotated tasks for object location and placement.
- **p. 4 / 3 Method - extractive body cue:** To address this, we propose a simple yet effective approach: a dedicated depth encoder and projector, initialized from their RGB counterparts.
- **p. 9 / 4 Experiments - extractive body cue:** By using a single target point predicted by RoboRefer, the system can generate more accurate masks and corresponding grasp poses than those from 2D boxes ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 4: RefSpatial-Bench results. G.P., M.M., and R.P. donate Gemini-2.5-Pro [9], Molmo- 72B [15], and RoboPoint [5]. RoboRefer-RFT excels in unseen and multi-step cases. SFT ...
- **p. 9 / 4 Experiments - extractive body cue:** Our model achieves comparable or slightly superior results, corroborating insights from SpatialVLM [6] and SpatialRGPT [1].

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 9 (4 Experiments), p. 8 (Figure/Table caption) |
| Embodiment/environment | To evaluate more complex multi-step spatial referring, we propose RefSpatial-Bench, a challenging benchmark based on real-world cluttered scenes. | hardware/simulator version and reset protocol | p. 8 (4 Experiments), p. 9 (4 Experiments) |
| Dataset/benchmark | Stage Categories Datasets SFT (D.A) Spatial RefSpatial (RGB-D) SFT (S.U.E) Spatial RefSpatial (RGB), RefSpatial (RGB-D), SAT [4], EmbSpatial [22] General COCO [150], GQA [18], OCR-VQA [151], TextVQA [152], VG [153], LRV [133] ... | role, split, size and leakage | p. 8 (4 Experiments), p. 9 (4 Experiments), p. 48 (C Implementation Details and Samples of RefSpatial-Bench), p. 7 (4 Experiments) |
| Metric | Method CV-Bench [15] BLINKval [16] RoboSpatial [2] SAT [4] EmbSpatial [22] 2D-Relation 3D-Depth 3D-Distance 2D-Relation 3D-Depth Qwen-2.5-VL-7B (base) 82.15 60.17 69.00 64.34 60.98 49.59 30.00 40.20 Qwen-2.5-VL-7B (finetuned) 95.85 95.0 ... | definition, denominator, direction and uncertainty | p. 23 (B.1.1 Multi-Stage Image Filtering), p. 8 (4 Experiments), p. 9 (4 Experiments) |
| Baseline/ablation | 2, the 2B-RFT variant outperforms all baselines, exceeding the prior SOTA (Gemini-2.5-Pro [9]) by 17.4% (absolute) on RefSpatial-Bench. | fair input/data/compute/action matching | p. 8 (4 Experiments), p. 10 (4 Experiments), p. 8 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 52 / C Implementation Details and Samples of RefSpatial-Bench - extractive body cue:** Notably, we find that our model achieves nearly 100% success in the perception stage (i.e., determining location and placement), with failures primarily attributed to motion ...
- **p. 21 / B.3.5 Question-Answer Pair Generation - extractive body cue:** 53 F More Demonstrations 54 G More Discussion on Limitations and Future Work 54 H Broader Impacts 54 I Licenses 54
- **p. 54 / C Implementation Details and Samples of RefSpatial-Bench - extractive body cue:** G More Discussion on Limitations and Future Work Despite achieving promising results, our model still has limitations.
- **p. 20 / B.2.2 Inherent Challenges and Limitations in CA-1M - extractive body cue:** 33 B.2.3 Addressing Limitations: Object Annotation and Bounding Box Filtering . .
- **p. 50 / C Implementation Details and Samples of RefSpatial-Bench - extractive body cue:** Thus, a failed match implies that the model cannot accurately refer to the object linguistically, and no reward is assigned.
- **p. 22 / B Implementation Details and Samples of RefSpatial Dataset - extractive body cue:** B.2): This section outlines the 3D data selection process from CA1M [136], discusses its limitations and mitigation strategies, and presents methods for enriched scene graph ...
- **p. 24 / B.1.1 Multi-Stage Image Filtering - extractive body cue:** Stage 2: Fine-grained Filtering Due to SigLIP2's limitations in handling certain visual content mentioned above, we introduce a fine-grained filtering stage using the Qwen2.5-VL-7B model ...

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Thus, this work attempts to address this gap by integrating both levels for comprehensive spatial referring.를 문제로 두고, Our contributions are summarized as follows: (1) We propose RoboRefer, a 3D-aware reasoning VLM trained using a sequential SFT-RFT strategy with metric-sensitive process reward functions to achieve spatial referring.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction), p. 2 (1 Introduction), p. 3 (3 Method), p. 4 (3 Method) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (71 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** To address the lack of multi-step spatial referring benchmarks, we introduce RefSpatial-Bench, comprising 200 real-world images with manually annotated tasks for object location and placement. (p. 3, 1 Introduction).
- **Actual contribution:** Our contributions are summarized as follows: (1) We propose RoboRefer, a 3D-aware reasoning VLM trained using a sequential SFT-RFT strategy with metric-sensitive process reward functions to achieve spatial referring. (p. 3, 1 Introduction).
- **Evaluation boundary:** Figure 4: RefSpatial-Bench results. G.P., M.M., and R.P. donate Gemini-2.5-Pro [9], Molmo- 72B [15], and RoboPoint [5]. RoboRefer-RFT excels in unseen and multi-step cases. SFT stage enables strong spatial understanding. ... (p. 8, Figure/Table caption).
- **Explicit failure boundary:** Another major limitation of CA-1M is the lack of semantic labels for most annotated objects. (p. 34, B.2.2 Inherent Challenges and Limitations in CA-1M).
