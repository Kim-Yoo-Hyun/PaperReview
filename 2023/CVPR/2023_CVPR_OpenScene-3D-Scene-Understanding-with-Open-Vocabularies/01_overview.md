# OpenScene: 3D Scene Understanding with Open Vocabularies

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (24 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2211.15654.
> PDF retrieval source: https://arxiv.org/pdf/2211.15654. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2023 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: open-vocabulary, 3D semantic, CLIP
- Official paper: https://arxiv.org/abs/2211.15654
- Full-text retrieval: https://arxiv.org/pdf/2211.15654
- Code/Project: https://pengsongyou.github.io/openscene
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (24 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 Traditional 3D scene understanding approaches rely on labeled 3D datasets to train a model for a single task with supervision.를 문제로 두고, Overall, our contributions are summarized as follows: • We introduce open vocabulary 3D scene understanding tasks where arbitrary text queries are used for semantic segmentation, affordance estimation, room type classification, 3D objec ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Traditional 3D scene understanding approaches rely on labeled 3D datasets to train a model for a single task with supervision.
- **p. 1 / Abstract - extractive body cue:** We propose OpenScene, an alternative approach where a model predicts dense features for 3D scene points that are co-embedded with text and image pixels in ...
- **p. 1 / Abstract - extractive body cue:** This zero-shot approach enables taskagnostic training and open-vocabulary queries.
- **p. 1 / Abstract - extractive body cue:** For example, to perform SOTA zero-shot 3D semantic segmentation it first infers CLIP features for every 3D point and later classifies them based on similarities ...
- **p. 1 / Abstract - extractive body cue:** More interestingly, it enables a suite of open-vocabulary scene understanding applications that have never been done before.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** Overall, our contributions are summarized as follows: • We introduce open vocabulary 3D scene understanding tasks where arbitrary text queries are used for semantic segmentation, ...
- **p. 2 / 1. Introduction - extractive body cue:** We present OpenScene, a simple yet effective zero-shot approach for open-vocabulary 3D scene understanding.
- **p. 4 / 3.3. 2D-3D Feature Ensemble - extractive body cue:** Although one can already perform open-vocabulary queries with the 2D fused features F2D or 3D distilled features F3D, here we introduce a 2D-3D ensemble method ...
- **p. 3 / 3. Method - extractive body cue:** An overview of our approach is illustrated in Fig.
- **p. 3 / 3.1. Image Feature Fusion - extractive body cue:** The first step in our approach is to extract dense perpixel embeddings for each RGB image from a 2D visuallanguage segmentation model, and then back-project ...
- **p. 4 / 3.2. 3D Distillation - extractive body cue:** To enforce the output of the network F3D to be consistent with the fused features F2D, we use a cosine similarity loss: \ c L ...
- **p. 3 / 3. Method - extractive body cue:** We first compute per-pixel features for every image using a model pre-trained for open-vocabulary 2D semantic segmentation.
- **p. 4 / 3.3. 2D-3D Feature Ensemble - extractive body cue:** We first compute the embeddings for all the text prompts using the CLIP [43] text encoder Etext, denoted as T = {t1, · · · ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Specifically, given an input point cloud P, we seek to learn an encoder that outputs per-point embeddings: \ b F ^\tex t { 3 D} = \ cE ^\text {3D}(\bP ), \quad ... | camera/depth stream, pose, map와 language goal | p. 4 (3.2. 3D Distillation), p. 3 (3. Method) |
| State/latent | Specifically, given, input, point, cloud, seek, learn, encoder, outputs, per-point, embeddings, text | robot pose, free-space/semantic map와 local goal | p. 4 (3.2. 3D Distillation), p. 3 (3. Method), p. 4 (3.2. 3D Distillation) |
| Output/action | We next distill a 3D network to reproduce the fused features using only the 3D point cloud as input Sec. | collision-free trajectory 또는 velocity command | p. 3 (3. Method), p. 4 (3.2. 3D Distillation), p. 1 (1. Introduction) |
| Objective/outcome | To enforce the output of the network F3D to be consistent with the fused features F2D, we use a cosine similarity loss: \ c L = 1 - \text {cos}(\bF ^\text {2D}, ... | goal reach, safety, localization error와 replanning latency | p. 4 (3.2. 3D Distillation) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** Overall, our contributions are summarized as follows: • We introduce open vocabulary 3D scene understanding tasks where arbitrary text queries are used for semantic segmentation, ...
- **p. 2 / 1. Introduction - extractive body cue:** We present OpenScene, a simple yet effective zero-shot approach for open-vocabulary 3D scene understanding.
- **p. 4 / 3.3. 2D-3D Feature Ensemble - extractive body cue:** Although one can already perform open-vocabulary queries with the 2D fused features F2D or 3D distilled features F3D, here we introduce a 2D-3D ensemble method ...
- **p. 3 / 3. Method - extractive body cue:** An overview of our approach is illustrated in Fig.
- **p. 3 / 3.1. Image Feature Fusion - extractive body cue:** The first step in our approach is to extract dense perpixel embeddings for each RGB image from a 2D visuallanguage segmentation model, and then back-project ...
- **p. 5 / 4.1. Comparisons - extractive body cue:** Again, we outperform the zero-shot baseline (MSeg Voting) on both mIoU and mAcc metrics all three datasets.
- **p. 5 / 4. Experiments - extractive body cue:** Still, both of our variants show significantly better performance in both mIoU and mAcc. detailed scenes, and thus provides the opportunity to stress open-vocabulary queries.
- **p. 6 / 4.1. Comparisons - extractive body cue:** Comparison of semantic segmentation performance of different 3D features computed by our method. the mean accuracy for groups of 20 classes ranked by frequency.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 5 (4.1. Comparisons), p. 5 (4. Experiments) |
| Embodiment/environment | To test our method in a variety of settings, we evaluate on three popular public benchmarks: ScanNet [11,46], Matterport3D [4], and nuScenes Lidarseg [3]. | hardware/simulator version and reset protocol | p. 4 (4. Experiments), p. 4 (4. Experiments) |
| Dataset/benchmark | We compare our method with both zero-shot and fully-supervised baselines for semantic segmentation of one outdoor dataset (nuScenes) and two indoor datasets (ScanNet and Matterport). | role, split, size and leakage | p. 4 (4. Experiments), p. 4 (4. Experiments), p. 5 (4.1. Comparisons), p. 5 (4.1. Comparisons) |
| Metric | Comparison of semantic segmentation performance of different 3D features computed by our method. the mean accuracy for groups of 20 classes ranked by frequency. | definition, denominator, direction and uncertainty | p. 6 (4.1. Comparisons), p. 6 (4.2. Ablation Studies & Analysis), p. 3 (Figure/Table caption) |
| Baseline/ablation | Again, we outperform the zero-shot baseline (MSeg Voting) on both mIoU and mAcc metrics all three datasets. | fair input/data/compute/action matching | p. 5 (4.1. Comparisons), p. 5 (4. Experiments), p. 6 (4.1. Comparisons) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 6. Limitations and Future Work - extractive body cue:** There are several limitations of our work and still much to do to realize the full potential of the proposed approach.
- **p. 8 / 6. Limitations and Future Work - extractive body cue:** In future work, it will be interesting to design experiments to quantify the success of open vocabulary queries for tasks where ground truth is not ...
- **p. 5 / 4. Experiments - extractive body cue:** Unlike [39], which requires training on 16 seen classes, our approach does not train with any 2D or 3D ground labels on any classes.
- **p. 5 / 4.1. Comparisons - extractive body cue:** Our results on those classes is significantly better than [39] (7.7% vs 62.8% mIoU), even though 3DGenz [39] utilizes ground truth data for 16 seen ...
- **p. 6 / 4.1. Comparisons - extractive body cue:** In contrast, we are more robust to such rare objects since we do not rely upon any 3D labeled data.
- **p. 6 / 4.2. Ablation Studies & Analysis - extractive body cue:** This suggests that leveraging patterns in both 2D and 3D domains makes the ensemble features more robust and descriptive.

## Why Read It

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 Traditional 3D scene understanding approaches rely on labeled 3D datasets to train a model for a single task with supervision.를 문제로 두고, Overall, our contributions are summarized as follows: • We introduce open vocabulary 3D scene understanding tasks where arbitrary text queries are used for semantic segmentation, affordance estimation, room type classification, 3D objec ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 4 (3.2. 3D Distillation), p. 3 (3.1. Image Feature Fusion), p. 3 (3. Method), p. 4 (3.3. 2D-3D Feature Ensemble), p. 5 (4.1. Comparisons), p. 5 (4. Experiments) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
