# GenSplat: Bridging the Generalization Gap in 3DGS Language Comprehension

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Liu_GenSplat_Bridging_the_Generalization_Gap_in_3DGS_Language_Comprehension_CVPR_2026_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_GenSplat_Bridging_the_Generalization_Gap_in_3DGS_Language_Comprehension_CVPR_2026_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Gaussian Splatting, language, generalization
- Official paper: https://openaccess.thecvf.com/content/CVPR2026/html/Liu_GenSplat_Bridging_the_Generalization_Gap_in_3DGS_Language_Comprehension_CVPR_2026_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_GenSplat_Bridging_the_Generalization_Gap_in_3DGS_Language_Comprehension_CVPR_2026_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Although large-scale training enables the generalization of SceneSplat [40] across scenes, its formulation remains restricted to a predefined vocabulary and thus fails to handle free-form language queries.를 문제로 두고, In summary, our key contributions are: • We introduce GenSplat, the first generalizable 3DGS framework that enables open-vocabulary language understanding and spatial reasoning, through a tailored structured learning process to systemat ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** In this paper, we propose GenSplat, a novel approach for language comprehension in 3D Gaussian Splatting (3DGS).
- **p. 1 / Abstract - extractive body cue:** Unlike previous methods that either achieve cross-scene generalization by being bounded to a predefined vocabulary or handle free-form language by overfitting to individual scenes, GenSplat ...
- **p. 1 / Abstract - extractive body cue:** Our key insight for this problem is to formulate a structured learning process to progressively align linguistic concepts with 3D Gaussians.
- **p. 1 / Abstract - extractive body cue:** It contains two novel technical contributions.
- **p. 1 / Abstract - extractive body cue:** First, we propose a Progressive Language Grounding Curriculum that structurally guides the model through learning semantic-level representations to instance-level concepts and free-form language, preventing overfitting ...
- **p. 1 / 1. Introduction - extractive body cue:** Although large-scale training enables the generalization of SceneSplat [40] across scenes, its formulation remains restricted to a predefined vocabulary and thus fails to handle free-form ...
- **p. 1 / 1. Introduction - extractive body cue:** However, they inherently lack cross-scene generalization (as they require per-scene optimization) and do not support comprehensive spatial reasoning beyond segmentation, e.g., for visual question answering ...

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** In summary, our key contributions are: • We introduce GenSplat, the first generalizable 3DGS framework that enables open-vocabulary language understanding and spatial reasoning, through a ...
- **p. 1 / 1. Introduction - extractive body cue:** First, we propose a multi-stage training strategy, Progressive Language Grounding Curriculum, to gradually guide the model from learning semantic-level representations to fine-grained instance-level concepts, and ...
- **p. 2 / 1. Introduction - extractive body cue:** We propose GenSplat, the first approach to achieve generalizable language-guided understanding in 3DGS.
- **p. 3 / 3. The GenSplat Method - extractive body cue:** 2, GenSplat consists of three main components: the Gaussian Encoder, the Instance Decoder, and the MLLMguided Referring Decoder.
- **p. 3 / 3.1. Progressive Language Grounding Curriculum - extractive body cue:** To address this limitation, we propose the Progressive Language Grounding Curriculum, which aligns 3D Gaussian primitives with multi-level linguistic concepts hierarchically: grounding fundamental spatial and ...
- **p. 4 / 3.1. Progressive Language Grounding Curriculum - extractive body cue:** Given a set of multi-view RGB images {Ii}N i=1 and a text query Q (e.g., for Referring Segmentation (RS) or VQA), GenSplat first reconstructs a ...
- **p. 5 / 3.2. MLLM-guided Reasoning Model - extractive body cue:** First, each image is encoded by the VLM vision encoder to extract visual features {Vi}N i=1, which are then refined through a linear projection and ...
- **p. 3 / 3. The GenSplat Method - extractive body cue:** The Gaussian Encoder then encodes Gaussian primitives to semantic latents L = {lj}M j=1, which the Instance Decoder further decodes to obtain instance-level queries Oins ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Specifically, for the referring segmentation task [21, 66], the MLLM outputs a special segmentation token <SEG>, whose final hidden state tseg is linearly projected to match the instance query dimension, yielding ˆtseg ... | RGB-D, image set, point cloud, depth와 camera pose | p. 5 (3.1. Progressive Language Grounding Curriculum), p. 4 (3.1. Progressive Language Grounding Curriculum) |
| State/latent | Specifically, referring, segmentation, task, MLLM, outputs, special, token, SEG, whose, final, hidden | geometry, map, object/relationship state | p. 5 (3.1. Progressive Language Grounding Curriculum), p. 4 (3.1. Progressive Language Grounding Curriculum), p. 3 (3.1. Progressive Language Grounding Curriculum) |
| Output/action | To provide semantic-level supervision, we follow LangSplat [54] to extract 2D language features {ˆFi}N i=1 from the input RGB images using pre-trained vision-language models (SAM [82] + CLIP [56]). | point map, pose, scene graph, affordance 또는 query result | p. 4 (3.1. Progressive Language Grounding Curriculum), p. 3 (3.1. Progressive Language Grounding Curriculum), p. 2 (1. Introduction) |
| Objective/outcome | In this stage, the model is optimized for both referring segmentation and text generation objectives: Lalign = Ltext + λmLmask, (1) where Ltext denotes the text generation loss (next-token prediction), and Lmask ... | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 5 (3.1. Progressive Language Grounding Curriculum), p. 5 (3.2. MLLM-guided Reasoning Model), p. 4 (3.1. Progressive Language Grounding Curriculum) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** In summary, our key contributions are: • We introduce GenSplat, the first generalizable 3DGS framework that enables open-vocabulary language understanding and spatial reasoning, through a ...
- **p. 1 / 1. Introduction - extractive body cue:** First, we propose a multi-stage training strategy, Progressive Language Grounding Curriculum, to gradually guide the model from learning semantic-level representations to fine-grained instance-level concepts, and ...
- **p. 2 / 1. Introduction - extractive body cue:** We propose GenSplat, the first approach to achieve generalizable language-guided understanding in 3DGS.
- **p. 3 / 3. The GenSplat Method - extractive body cue:** 2, GenSplat consists of three main components: the Gaussian Encoder, the Instance Decoder, and the MLLMguided Referring Decoder.
- **p. 3 / 3.1. Progressive Language Grounding Curriculum - extractive body cue:** To address this limitation, we propose the Progressive Language Grounding Curriculum, which aligns 3D Gaussian primitives with multi-level linguistic concepts hierarchically: grounding fundamental spatial and ...
- **p. 7 / 4.3. Comparison with State-of-the-Art Models - extractive body cue:** Our GenSplat achieves consistently better results over the expert model SplatTalk [61] (e.g., a +26.8% CIDEr (C) improvement on ScanQA [2]), as well as the ...
- **p. 7 / 4.3. Comparison with State-of-the-Art Models - extractive body cue:** Results in Table 2 show that our GenSplat method significantly outperforms other methods without requiring per-scene optimization, showcasing its robust generalization capabilities.
- **p. 6 / 4.3. Comparison with State-of-the-Art Models - extractive body cue:** We report comparison results on the ScanRefer [5] (featuring single referred object) and Multi3DRefer [76] (featuring varying numbers of referred objects) datasets, as shown in ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 7 (4.3. Comparison with State-of-the-Art Models), p. 7 (4.3. Comparison with State-of-the-Art Models) |
| Embodiment/environment | Comparison of 3D referring segmentation on five scenes (selected by ReferSplat [22]) from the ScanRefer [5] dataset. | hardware/simulator version and reset protocol | p. 6 (4.2. Evaluation Datasets and Metrics), p. 7 (4.4. Ablation Study) |
| Dataset/benchmark | We report comparison results on the ScanRefer [5] (featuring single referred object) and Multi3DRefer [76] (featuring varying numbers of referred objects) datasets, as shown in Table 1. | role, split, size and leakage | p. 6 (4.2. Evaluation Datasets and Metrics), p. 7 (4.4. Ablation Study), p. 6 (4.3. Comparison with State-of-the-Art Models), p. 7 (4.3. Comparison with State-of-the-Art Models) |
| Metric | For the question answering task, we follow [18, 26] to evaluate the generated responses on ScanQA [2] using CIDEr (C), BLEU-4 (B-4), METEOR (M), and ROUGE-L (R), while using the exact match ... | definition, denominator, direction and uncertainty | p. 6 (4.2. Evaluation Datasets and Metrics), p. 6 (4.1. Implementation Details), p. 7 (4.3. Comparison with State-of-the-Art Models) |
| Baseline/ablation | The (I) Baseline model contains the randomly-initialized Gaussian Encoder and Instance Decoder (i.e., without the MLLM-guided reasoning and Referring Decoder). | fair input/data/compute/action matching | p. 7 (4.4. Ablation Study), p. 7 (4.3. Comparison with State-of-the-Art Models), p. 8 (4.4. Ablation Study) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 5. Conclusion - extractive body cue:** An example failure case of our method.
- **p. 8 / 5. Conclusion - extractive body cue:** Extensive experiments across diverse tasks, such as 3D referring segmentation, visual question answering, and open-vocabulary understanding, have demonstrated its robust generalization and reasoning abilities.
- **p. 6 / 4.1. Implementation Details - extractive body cue:** Since SQA3D [50] does not provide frame-level annotations, we apply GPT-5 [52] for annotation.
- **p. 6 / 4.1. Implementation Details - extractive body cue:** Note that our method does not require test-time per-scene optimization beyond 3DGS reconstruction.
- **p. 7 / 4.3. Comparison with State-of-the-Art Models - extractive body cue:** In contrast, 2D-based methods such as Grounded-SAM and per-scene optimization approaches fail under these challenging scenarios.
- **p. 7 / 4.3. Comparison with State-of-the-Art Models - extractive body cue:** Results in Table 2 show that our GenSplat method significantly outperforms other methods without requiring per-scene optimization, showcasing its robust generalization capabilities.

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Although large-scale training enables the generalization of SceneSplat [40] across scenes, its formulation remains restricted to a predefined vocabulary and thus fails to handle free-form language queries.를 문제로 두고, In summary, our key contributions are: • We introduce GenSplat, the first generalizable 3DGS framework that enables open-vocabulary language understanding and spatial reasoning, through a tailored structured learning process to systemat ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (3.1. Progressive Language Grounding Curriculum), p. 5 (3.2. MLLM-guided Reasoning Model) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
