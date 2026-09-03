# NavGPT-2: Unleashing Navigational Reasoning Capability for Large Vision-Language Models

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (20 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/1143_ECCV_2024_paper.php.
> PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/01143.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / ECCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: Vision-Language Model, Navigation
- Official paper: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/1143_ECCV_2024_paper.php
- Full-text retrieval: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/01143.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (20 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 However, these approaches reveal a notable performance gap towards agents designed and trained tailored for solving VLN [10, 46, 81], usually lie at two extremes that carry significant limitations: - For the ...를 문제로 두고, Our contributions are as follows: (1) We propose a pipeline to incorporate VLN specialists with VLMs free from LLM training.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / 1 Introduction - extractive body cue:** Motivating by the considerable advances in Large Language Models (LLMs), there is an emerging effort to utilize these models for instructional tasks within robotic navigation ...
- **p. 1 / 1 Introduction - extractive body cue:** This development highlights two core capacities of LLMs: Firstly, the ability to generalize commonsense knowledge reasoning and efficiently process free-form linguistic inputs, thanks to learning ...
- **p. 1 / 1 Introduction - extractive body cue:** Secondly, the interpretative of LLMs to provide navigational reasoning explicitly in a human interpretable way and the associated communicative potential during interaction with humans.
- **p. 2 / 1 Introduction - extractive body cue:** NavGPT-2: …, I am currently positioned in a spacious room with a wall to my right, visible as a couch and a round table.
- **p. 2 / 1 Introduction - extractive body cue:** Directly ahead, there is a picture on the wall.
- **p. 2 / 1 Introduction - extractive body cue:** However, these approaches reveal a notable performance gap towards agents designed and trained tailored for solving VLN [10, 46, 81], usually lie at two extremes ...
- **p. 4 / 1 Introduction - extractive body cue:** However, a large performance gap is observed compared to supervised methods, even if the most powerful GPT-4 [52] models are used.

## Core Idea

- **p. 3 / 1 Introduction - extractive body cue:** Our contributions are as follows: (1) We propose a pipeline to incorporate VLN specialists with VLMs free from LLM training.
- **p. 3 / 1 Introduction - extractive body cue:** In light of this, we propose NavGPT-2, a system that finds a balance between the two aforementioned extremes, incorporating effective navigational modules to facilitate navigational ...
- **p. 5 / 3 Method - extractive body cue:** Moreover, we introduce special tokens <IMG>, </IMG>, <INST> and </INST> to insert images tokens and instructions into the prompt.
- **p. 6 / 3 Method - extractive body cue:** 2: Model architecture of NavGPT-2, it consists of a multimodality Large Language Model and a topological graph-based navigation policy network.
- **p. 7 / 3 Method - extractive body cue:** We introduce the graph-based policy in the following sections.
- **p. 5 / 3 Method - extractive body cue:** 3.1 VLMs Latent as Visual-Linguistic Representation In this section, we discuss the model design within the Large Vision-Language Model, how to enable frozen LLMs to ...
- **p. 5 / 3 Method - extractive body cue:** For action prediction, the model employs both hidden representations of image tokens and instruction text tokens that have been processed by the LLM encoder as ...
- **p. 4 / 3 Method - extractive body cue:** The architecture of NavGPT-2, as depicted in Figure 2, comprises two primary components: a Large Vision-Language Model (VLM) and a navigation policy network.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | For action prediction, the model employs both hidden representations of image tokens and instruction text tokens that have been processed by the LLM encoder as the input features. | camera/depth stream, pose, map와 language goal | p. 5 (3 Method), p. 4 (3 Method) |
| State/latent | action, prediction, model, employs, hidden, representations, image, tokens, instruction, text, have, been | robot pose, free-space/semantic map와 local goal | p. 5 (3 Method), p. 4 (3 Method), p. 5 (3 Method) |
| Output/action | Within the VLM, visual observations and instructions are processed by | collision-free trajectory 또는 velocity command | p. 4 (3 Method), p. 5 (3 Method), p. 8 (3 Method) |
| Objective/outcome | Furthermore, we generate 10K navigational reasoning data from the R2R training set [6] and perform instruction-tuning to the Q-former and the projection layer on the prediction tokens, using its original auto-regressive training ... | goal reach, safety, localization error와 replanning latency | p. 5 (3 Method), p. 9 (3 Method), p. 9 (3 Method) |

## Main Claims and Actual Contribution

- **p. 3 / 1 Introduction - extractive body cue:** Our contributions are as follows: (1) We propose a pipeline to incorporate VLN specialists with VLMs free from LLM training.
- **p. 3 / 1 Introduction - extractive body cue:** In light of this, we propose NavGPT-2, a system that finds a balance between the two aforementioned extremes, incorporating effective navigational modules to facilitate navigational ...
- **p. 5 / 3 Method - extractive body cue:** Moreover, we introduce special tokens <IMG>, </IMG>, <INST> and </INST> to insert images tokens and instructions into the prompt.
- **p. 6 / 3 Method - extractive body cue:** 2: Model architecture of NavGPT-2, it consists of a multimodality Large Language Model and a topological graph-based navigation policy network.
- **p. 7 / 3 Method - extractive body cue:** We introduce the graph-based policy in the following sections.
- **p. 13 / 4 Experiments - extractive body cue:** Additionally, we can see from Model#3 of Table 5 that the pretraining of Q-former on reasonings brings slight improvement to the success rates of the ...
- **p. 9 / 4 Experiments - extractive body cue:** We adopt a comprehensive set of navigation metrics to evaluate performance [6], including Trajectory Length (TL), which measures the average path length in meters; Navigation ...
- **p. 13 / 4 Experiments - extractive body cue:** As shown in Table 4, NavGPT-2 significantly outperforms DUET.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 13 (4 Experiments), p. 9 (4 Experiments) |
| Embodiment/environment | 4.5 Cross Dataset Generalization Ability We evaluate the generalization ability of NavGPT-2 in two aspects: generalize to free-form language instructions and to various unseen environments. | hardware/simulator version and reset protocol | p. 12 (4 Experiments), p. 13 (4 Experiments) |
| Dataset/benchmark | The current SOTA method [75] is achieved by scaling up the training environment for DUET with HM3D [60] and Gibson [76], besides the original 61 scenes in MP3D [9]. | role, split, size and leakage | p. 12 (4 Experiments), p. 13 (4 Experiments), p. 11 (4 Experiments), p. 12 (4 Experiments) |
| Metric | We adopt a comprehensive set of navigation metrics to evaluate performance [6], including Trajectory Length (TL), which measures the average path length in meters; Navigation Error (NE), the average distance between the ... | definition, denominator, direction and uncertainty | p. 9 (4 Experiments), p. 12 (4 Experiments), p. 13 (4 Experiments) |
| Baseline/ablation | Compared to the baseline methods, NavGPT-2 bypass it by 4% SR and 2% SPL on the test split even if we do not incorporate with VLN pertaining. | fair input/data/compute/action matching | p. 11 (4 Experiments), p. 9 (4 Experiments), p. 10 (4 Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 14 / 4 Experiments - extractive body cue:** We will leave a detailed investigation of this problem for future work.
- **p. 13 / 4 Experiments - extractive body cue:** We hypothesize this improvement is due to the projection of visual features into the same LLM hidden space as language, leading to a more robust ...

## Why Read It

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 However, these approaches reveal a notable performance gap towards agents designed and trained tailored for solving VLN [10, 46, 81], usually lie at two extremes that carry significant limitations: - For the ...를 문제로 두고, Our contributions are as follows: (1) We propose a pipeline to incorporate VLN specialists with VLMs free from LLM training.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 Introduction), p. 4 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction), p. 1 (1 Introduction), p. 6 (3 Method) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
