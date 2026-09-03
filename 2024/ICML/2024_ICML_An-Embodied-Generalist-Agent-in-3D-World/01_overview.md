# An Embodied Generalist Agent in 3D World

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (39 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2311.12871.
> PDF retrieval source: https://arxiv.org/pdf/2311.12871. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / ICML
- Authors: not duplicated here when not verified in the registry source
- Primary track: Planning and control
- Tier: REFERENCE
- Tags: LLM, 3D Vision, Planning, Robotics
- Official paper: https://arxiv.org/abs/2311.12871
- Full-text retrieval: https://arxiv.org/pdf/2311.12871
- Code/Project: https://embodied-generalist.github.io/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (39 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Planning and control의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 The development of such generalist agents encounters three primary challenges: the lack of suitable datasets, unified models, and effective learning strategies.를 문제로 두고, We present the results of CLIPort manipulation and object navigation in Tabs.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Leveraging massive knowledge from large language models (LLMs), recent machine learning models show notable successes in generalpurpose task solving in diverse domains such as computer ...
- **p. 1 / Abstract - extractive body cue:** However, several significant challenges remain: (i) most of these models rely on 2D images yet exhibit a limited capacity for 3D input; (ii) these models ...
- **p. 1 / Abstract - extractive body cue:** We argue these limitations significantly hinder current models from performing real-world tasks and approaching general intelligence.
- **p. 1 / Abstract - extractive body cue:** To this end, we introduce LEO, an embodied multimodal generalist agent that excels in perceiving, grounding, reasoning, planning, and acting in the 3D world.
- **p. 1 / Abstract - extractive body cue:** LEO is trained with a unified task interface, model architecture, and objective in two stages: (i) 3D vision-language (VL) alignment and (ii) 3D vision-language-action (VLA) ...
- **p. 1 / 1. Introduction - extractive body cue:** The development of such generalist agents encounters three primary challenges: the lack of suitable datasets, unified models, and effective learning strategies.
- **p. 1 / 1. Introduction - extractive body cue:** This limitation stands as an obstacle that prevents current models from solving realworld tasks and approaching general intelligence.

## Core Idea

- **p. 7 / 4.3. Embodied Action in 3D World - extractive body cue:** We present the results of CLIPort manipulation and object navigation in Tabs.
- **p. 1 / 1. Introduction - extractive body cue:** The development of such generalist agents encounters three primary challenges: the lack of suitable datasets, unified models, and effective learning strategies.
- **p. 1 / 1. Introduction - extractive body cue:** Furthermore, large-scale unified pretraining and efficient finetuning are under-explored by previous 3D VL models, which are often designed with strong priors (Zhao et al., 2021; ...
- **p. 7 / 4.3. Embodied Action in 3D World - extractive body cue:** Underlined figures indicate zero-shot results on novel scenes (3RScan).
- **p. 3 / 2. Model - extractive body cue:** Next, we will detail the tokenization of multimodal data, model architecture, training loss, and inference settings.
- **p. 3 / 2.3. Training & Inference - extractive body cue:** During training, we freeze the pretrained 3D point cloud encoder and the LLM and finetune the 2D image encoder, the Spatial Transformer, and the LoRA ...
- **p. 4 / 2.3. Training & Inference - extractive body cue:** For tasks that require action commands, we map the textual outputs to action commands as discussed in Sec.
- **p. 4 / 2.3. Training & Inference - extractive body cue:** More details on the model and training can be found in Appendix D.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The leading design principles of LEO are two-fold: 1) It should handle the multi-modal input of egocentric 2D, global 3D, and textual instruction, and the output of textual response as well as ... | RGB-D, image set, point cloud, depth와 camera pose | p. 3 (2. Model), p. 4 (2.3. Training & Inference) |
| State/latent | leading, design, principles, LEO, two-fold, should, handle, multi-modal, input, egocentric, global, textual | geometry, map, object/relationship state | p. 3 (2. Model), p. 4 (2.3. Training & Inference), p. 6 (4.2. Scene-grounded Dialogue and Planning) |
| Output/action | For tasks that require action commands, we map the textual outputs to action commands as discussed in Sec. | point map, pose, scene graph, affordance 또는 query result | p. 4 (2.3. Training & Inference), p. 6 (4.2. Scene-grounded Dialogue and Planning), p. 3 (2.1. Tokenization) |
| Objective/outcome | We formulate the learning objective of LEO following (Brown et al., 2020; Raffel et al., 2020) in a prefix language modeling fashion. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 3 (2.3. Training & Inference), p. 3 (2. Model), p. 7 (4.3. Embodied Action in 3D World) |

## Main Claims and Actual Contribution

- **p. 7 / 4.3. Embodied Action in 3D World - extractive body cue:** We present the results of CLIPort manipulation and object navigation in Tabs.
- **p. 1 / 1. Introduction - extractive body cue:** The development of such generalist agents encounters three primary challenges: the lack of suitable datasets, unified models, and effective learning strategies.
- **p. 1 / 1. Introduction - extractive body cue:** Furthermore, large-scale unified pretraining and efficient finetuning are under-explored by previous 3D VL models, which are often designed with strong priors (Zhao et al., 2021; ...
- **p. 7 / 4.3. Embodied Action in 3D World - extractive body cue:** Underlined figures indicate zero-shot results on novel scenes (3RScan).
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 2: Our proposed LLM-assisted 3D-language data generation pipeline and data examples.. (Top-left) Messages with 3D scene graphs, including object attributes and relations in a ...
- **p. 8 / 4.5. Scaling Law Analysis - extractive body cue:** 2) Scaling up LLM leads to consistent improvements.
- **p. 8 / 4.5. Scaling Law Analysis - extractive body cue:** In contrast, despite the consistent improvements, the gap between Aligned Vicuna-7B and Vicuna-13B appears less significant, suggesting potential saturation if we continue to scale up ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 6: Results on object navigation. † indi- cates zero-shot evaluation. MP3D-val HM3D-val Success(↑) SPL(↑) Success(↑) SPL(↑) Habitat-web (shortest) 4.4

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | SYSTEM / EVALUATION SCOPE UNRESOLVED | do not infer unreported downstream behavior | p. 5 (Figure/Table caption), p. 8 (4.5. Scaling Law Analysis) |
| Embodiment/environment | Next, we manually design some examples as seed tasks (Liu et al., 2023b), including scene and object captioning, QA, dialogue, and planning, and ask LLM to produce more tasks as well as ... | hardware/simulator version and reset protocol | p. 4 (3.3. LLM-assisted 3D-language Data Generation), p. 4 (3. Datasets) |
| Dataset/benchmark | An Embodied Generalist Agent in 3D World Dialogue(O-CoT): Dialogue Context: high level task: organize the bedroom. low level task: check some objects. | role, split, size and leakage | p. 4 (3.3. LLM-assisted 3D-language Data Generation), p. 4 (3. Datasets), p. 5 (3.3. LLM-assisted 3D-language Data Generation), p. 5 (3.3. LLM-assisted 3D-language Data Generation) |
| Metric | Table 4: Quantitative comparison with state-of-the-art models on 3D VL under- standing and embodied reasoning tasks. "C" stands for "CIDEr", "B-4" for "BLEU- 4", "M" for "METEOR", "R" for "ROUGE", "Sim" for ... | definition, denominator, direction and uncertainty | p. 6 (Figure/Table caption), p. 4 (Figure/Table caption), p. 6 (Figure/Table caption) |
| Baseline/ablation | Compared to counterparts that utilize object boxes (Yin et al., 2023; Hong et al., 2023; Wang et al., 2023e), it offers both rich object attributes and accurate spatial relation information among objects, ... | fair input/data/compute/action matching | p. 4 (3.3. LLM-assisted 3D-language Data Generation), p. 6 (Figure/Table caption), p. 7 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: The proposed embodied generalist agent LEO. It takes egocentric 2D images, 3D point clouds, and texts as input and formulates comprehensive 3D tasks ...

## Why Read It

Planning and control의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 The development of such generalist agents encounters three primary challenges: the lack of suitable datasets, unified models, and effective learning strategies.를 문제로 두고, We present the results of CLIPort manipulation and object navigation in Tabs.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 1 (1. Introduction), p. 3 (2. Model), p. 3 (2.3. Training & Inference), p. 4 (2.3. Training & Inference), p. 4 (2.3. Training & Inference) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
