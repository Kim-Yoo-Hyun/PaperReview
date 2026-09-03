# Open-Vocabulary 3D Semantic Segmentation with Text-to-Image Diffusion Models

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/4252_ECCV_2024_paper.php.
> PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/04252.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / ECCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: 3D Vision, Diffusion, semantic
- Official paper: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/4252_ECCV_2024_paper.php
- Full-text retrieval: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/04252.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Several existing methods have been proposed to solve the lack of data issue in a zero-shot fashion by leveraging the CLIP model pre-trained on large-scale text-image data [37,62,79].를 문제로 두고, In summary, we make the following contributions: - To the best of our knowledge, we are the first to leverage text-image diffusion to perform open-vocabulary 3D semantic segmentation. - We propose a ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 2 / 1 Introduction - extractive body cue:** 3D semantic scene understanding, with the task of assigning semantics to every 3D point, plays a fundamental role in many computer vision applications, such as ...
- **p. 2 / 1 Introduction - extractive body cue:** Traditional studies in this field usually target solving this problem in a closed-set fashion [16,73], resulting in models that can only be used to make ...
- **p. 2 / 1 Introduction - extractive body cue:** Recent progress in computer vision have witnessed the emerging interests in solving semantic understanding tasks in open-vocabulary settings [35,62,67,78, 94].
- **p. 2 / 1 Introduction - extractive body cue:** In contrast to closed-set setting, models targeting open-vocabulary tasks must make predictions for any semantics described in text, including object category and fine-grained attributes (e.g., ...
- **p. 2 / 1 Introduction - extractive body cue:** However, this is a challenging task due to the wide diversity and complexity of possible queries.
- **p. 2 / 1 Introduction - extractive body cue:** Several existing methods have been proposed to solve the lack of data issue in a zero-shot fashion by leveraging the CLIP model pre-trained on large-scale ...
- **p. 2 / 1 Introduction - extractive body cue:** Motivated by the advance of aligning text and image embeddings with large-scale foundation models [2, 39,48,65], existing methods mitigate this challenge by lifting the image ...

## Core Idea

- **p. 3 / 1 Introduction - extractive body cue:** In summary, we make the following contributions: - To the best of our knowledge, we are the first to leverage text-image diffusion to perform open-vocabulary ...
- **p. 3 / 1 Introduction - extractive body cue:** To mitigate these issues, we propose a novel mask distillation method tailored to distill knowledge from the Mask2Former style 2D branch [10, 87] to the ...
- **p. 1 / 4 HKUST - extractive body cue:** We propose Diff2Scene, a 3D model that performs open-vocabulary semantic segmentation and visual grounding tasks given novel text prompts, without relying on any annotated 3D ...
- **p. 1 / 4 HKUST - extractive body cue:** We propose a novel method, namely Diff2Scene, which leverages frozen representations from text-image generative models, along with salient-aware and geometric-aware masks, for open-vocabulary 3D semantic ...
- **p. 2 / 1 Introduction - extractive body cue:** Despite these achievements, contrastively trained CLIP-based models exhibit limitations in handling fine-grained classes [66] and novel compositional text queries [58], restricting their performance in open-vocabulary ...
- **p. 4 / X. Zhu et al - extractive body cue:** (b) Directly using a 3D mask proposal network trained on labeled 3D data to produce class-agnostic masks, and then pool corresponding representations from the CLIP ...
- **p. 3 / 1 Introduction - extractive body cue:** The frozen features extracted from the decoder of the U-Net in the diffusion model are trained with generative objectives, and cannot be directly used for ...
- **p. 8 / X. Zhu et al - extractive body cue:** It serves as an implicit distillation objective to make the 3D model learn high-resolution, semantically-rich feature representations.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | It takes posed RGB images and the reconstructed 3D point cloud as model inputs. | RGB-D, image set, point cloud, depth와 camera pose | p. 5 (X. Zhu et al), p. 8 (X. Zhu et al) |
| State/latent | takes, posed, RGB, images, reconstructed, point, cloud, model, inputs, Open-Vocabulary, Inference, During | geometry, map, object/relationship state | p. 5 (X. Zhu et al), p. 8 (X. Zhu et al), p. 3 (1 Introduction) |
| Output/action | 3.4 Open-Vocabulary Inference During inference, Diff2Scene takes a 3D point cloud and its multiview 2D images as inputs. | point map, pose, scene graph, affordance 또는 query result | p. 8 (X. Zhu et al), p. 3 (1 Introduction), p. 5 (X. Zhu et al) |
| Objective/outcome | The frozen features extracted from the decoder of the U-Net in the diffusion model are trained with generative objectives, and cannot be directly used for the perception task. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 3 (1 Introduction), p. 4 (X. Zhu et al), p. 4 (X. Zhu et al) |

## Main Claims and Actual Contribution

- **p. 3 / 1 Introduction - extractive body cue:** In summary, we make the following contributions: - To the best of our knowledge, we are the first to leverage text-image diffusion to perform open-vocabulary ...
- **p. 3 / 1 Introduction - extractive body cue:** To mitigate these issues, we propose a novel mask distillation method tailored to distill knowledge from the Mask2Former style 2D branch [10, 87] to the ...
- **p. 1 / 4 HKUST - extractive body cue:** We propose Diff2Scene, a 3D model that performs open-vocabulary semantic segmentation and visual grounding tasks given novel text prompts, without relying on any annotated 3D ...
- **p. 1 / 4 HKUST - extractive body cue:** We propose a novel method, namely Diff2Scene, which leverages frozen representations from text-image generative models, along with salient-aware and geometric-aware masks, for open-vocabulary 3D semantic ...
- **p. 2 / 1 Introduction - extractive body cue:** Despite these achievements, contrastively trained CLIP-based models exhibit limitations in handling fine-grained classes [66] and novel compositional text queries [58], restricting their performance in open-vocabulary ...
- **p. 12 / Figure/Table caption - extractive body cue:** Table 3: Performance of different model ablations. We observe that each com- ponent of our model gains consistent improvements.
- **p. 9 / 4 Experiment - extractive body cue:** We train our 3D branch using the images in the training splits and report the results on test split.
- **p. 9 / 4 Experiment - extractive body cue:** This enables us to evaluate the performance of our method on the long-tail distribution, making ScanNet200 a natural choice as an evaluation dataset.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 12 (Figure/Table caption), p. 9 (4 Experiment) |
| Embodiment/environment | It splits 61 scenes for training, 11 scenes for validation and 18 for testing. | hardware/simulator version and reset protocol | p. 9 (4 Experiment), p. 9 (4 Experiment) |
| Dataset/benchmark | It splits 61 scenes for training, 11 scenes for validation and 18 for testing. | role, split, size and leakage | p. 9 (4 Experiment), p. 9 (4 Experiment) |
| Metric | Fig. 2: Illustration of open-vocabulary 3D perception methods. LP D and LMD denote point-based distillation loss and mask-based distillation loss. M3D denote a set of predicted 3D masks; M2D and Zmf denote ... | definition, denominator, direction and uncertainty | p. 4 (Figure/Table caption), p. 9 (4 Experiment), p. 9 (4 Experiment) |
| Baseline/ablation | Table 1: Comparison to state-of-the-art models. We report mIoU for all benchmarks. Best results in zero-shot, open-vocabulary setting are shown in bold. ScanNet Matterport3D ScanNet200 Replica All All Head Common Tail All ... | fair input/data/compute/action matching | p. 10 (Figure/Table caption), p. 13 (Figure/Table caption), p. 9 (4 Experiment) |

## Explicit Limitations and Failure Boundary

- **p. 13 / 5 Conclusion - extractive body cue:** There are several limitations of the proposed model.
- **p. 9 / 4 Experiment - extractive body cue:** As Replica does not provide the training data, we perform training on ScanNet and perform evaluation on Replica, following the setting in [79].
- **p. 14 / Figure/Table caption - extractive body cue:** Fig. 5: Qualitative results from our model and OpenScene on zero-shot vi- sual grounding. Our open-vocabulary semantic understanding model is capable of handling different types ...

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Several existing methods have been proposed to solve the lack of data issue in a zero-shot fashion by leveraging the CLIP model pre-trained on large-scale text-image data [37,62,79].를 문제로 두고, In summary, we make the following contributions: - To the best of our knowledge, we are the first to leverage text-image diffusion to perform open-vocabulary 3D semantic segmentation. - We propose a ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction), p. 4 (X. Zhu et al) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
