# 3D Weakly Supervised Semantic Segmentation with 2D Vision-Language Guidance

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/9223_ECCV_2024_paper.php.
> PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/09223.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / ECCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Vision-Language Model, 3D Vision, semantic
- Official paper: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/9223_ECCV_2024_paper.php
- Full-text retrieval: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/09223.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Therefore, how to design a network that achieves good performance despite the lack of 2D anno를 문제로 두고, In summary, the main contributions of this paper are as follows: - We propose a weakly supervised method 3DSS-VLG for 3D WSSS, which takes 2D images as a bridge, and leverages natural ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / 1 Introduction - extractive body cue:** 3D point cloud semantic segmentation [13, 16, 27-29, 43] can provide valuable geometric and semantic data about the 3D environment and has gained considerable attention ...
- **p. 2 / X. Xu et al - extractive body cue:** Therefore, how to design a network that achieves good performance despite the lack of 2D anno
- **p. 2 / X. Xu et al - extractive body cue:** Given the simple GAP connectivity structure, these methods can easily identify the importance of each point by projecting back the output classification weight onto the ...
- **p. 3 / X. Xu et al - extractive body cue:** 3DSS with 2D Vision-Language Guidance 3 tations still remains a big challenge.
- **p. 1 / Body text (section not recovered) - extractive body cue:** Specifically, our method exploits the superior generalization ability of the 2D visionlanguage models and proposes the Embeddings Soft-Guidance Stage to utilize it to implicitly align ...
- **p. 1 / Body text (section not recovered) - extractive body cue:** Moreover, with extensive quantitative and qualitative experiments, we present that our 3DSS-VLG is able not only to achieve the state-ofthe-art performance on both S3DIS and ...

## Core Idea

- **p. 4 / X. Xu et al - extractive body cue:** In summary, the main contributions of this paper are as follows: - We propose a weakly supervised method 3DSS-VLG for 3D WSSS, which takes 2D ...
- **p. 1 / Body text (section not recovered) - extractive body cue:** Moreover, we introduce the Embeddings Specialization Stage to purify the feature representation with the help of a given scene-level label, specifying a better feature supervised ...
- **p. 1 / Body text (section not recovered) - extractive body cue:** Specifically, our method exploits the superior generalization ability of the 2D visionlanguage models and proposes the Embeddings Soft-Guidance Stage to utilize it to implicitly align ...
- **p. 3 / X. Xu et al - extractive body cue:** Therefore, we propose to alleviate this problem by three stages.
- **p. 3 / X. Xu et al - extractive body cue:** 3 (a), we propose the Embeddings Specialization Stage, which transfers the 2D-projected embeddings with an adapter module to obtain adapted 3D embeddings, and the
- **p. 2 / X. Xu et al - extractive body cue:** Point clouds are first processed by several Multi-Layer Perception (MLP) layers and thus get a point cloud feature map, and then this point cloud feature ...
- **p. 8 / X. Xu et al - extractive body cue:** Finally, we use the pseudo labels Y to supervise the model, and the green dashed lines denote back-propagation of the loss La.
- **p. 3 / X. Xu et al - extractive body cue:** We first process these multi-view images using the image encoder of the pretrained off-the-shelf 2D OVSS model such as Openseg [12] to get the 2D ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Moreover, we propose Embeddings Specialization Stage to make the embedding space to be more robust based on the pseudo label filtering with indoor point cloud scene knowledge. - Extensive experiments on the ... | RGB-D, image set, point cloud, depth와 camera pose | p. 4 (X. Xu et al), p. 3 (X. Xu et al) |
| State/latent | Moreover, Embeddings, Specialization, Stage, make, embedding, space, more, robust, pseudo, label, filtering | geometry, map, object/relationship state | p. 4 (X. Xu et al), p. 3 (X. Xu et al), p. 6 (X. Xu et al) |
| Output/action | Specifically, for the input 3D point cloud, the dataset also provides a set of multi-view images corresponding to it. | point map, pose, scene graph, affordance 또는 query result | p. 3 (X. Xu et al), p. 6 (X. Xu et al), p. 6 (X. Xu et al) |
| Objective/outcome | The red dashed lines denote back-propagation of the loss Ls. a classification cross-entropy loss La is introduced to supervise the procedure. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 8 (X. Xu et al), p. 8 (X. Xu et al) |

## Main Claims and Actual Contribution

- **p. 4 / X. Xu et al - extractive body cue:** In summary, the main contributions of this paper are as follows: - We propose a weakly supervised method 3DSS-VLG for 3D WSSS, which takes 2D ...
- **p. 1 / Body text (section not recovered) - extractive body cue:** Moreover, we introduce the Embeddings Specialization Stage to purify the feature representation with the help of a given scene-level label, specifying a better feature supervised ...
- **p. 1 / Body text (section not recovered) - extractive body cue:** Specifically, our method exploits the superior generalization ability of the 2D visionlanguage models and proposes the Embeddings Soft-Guidance Stage to utilize it to implicitly align ...
- **p. 3 / X. Xu et al - extractive body cue:** Therefore, we propose to alleviate this problem by three stages.
- **p. 3 / X. Xu et al - extractive body cue:** 3 (a), we propose the Embeddings Specialization Stage, which transfers the 2D-projected embeddings with an adapter module to obtain adapted 3D embeddings, and the
- **p. 10 / Figure/Table caption - extractive body cue:** Table 1: Performance comparison on the S3DIS dataset. "Sup." indicates the type of supervision. "100%" represents full annotation. "scene." denotes scene-level annotation.
- **p. 12 / Figure/Table caption - extractive body cue:** Table 4: Performance comparisons of the generalization capability. Domain mIoU mAcc S3DIS ->ScanNet 13.4 23.0 ScanNet ->S3DIS 33.3 50.9 labels to supervised 3D model. Meanwhile, ...
- **p. 13 / Figure/Table caption - extractive body cue:** Table 5: Performance comparisons with different 3D backbones and ESS module back- bones on the S3DIS dataset. Module Backbone mIoU 3D MinkowskiNet14A 44.5 MinkowskiNet18A 45.3

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | SYSTEM / EVALUATION SCOPE UNRESOLVED | do not infer unreported downstream behavior | p. 10 (Figure/Table caption), p. 12 (Figure/Table caption) |
| Embodiment/environment | We adopt the default train-val split setting, where there are 1201 training scenes and 312 validation scenes. | hardware/simulator version and reset protocol | p. 9 (4 Experiments), p. 9 (4 Experiments) |
| Dataset/benchmark | We adopt the default train-val split setting, where there are 1201 training scenes and 312 validation scenes. | role, split, size and leakage | p. 9 (4 Experiments), p. 9 (4 Experiments) |
| Metric | We reduce the learning rate by a multiplying factor of 0.7 every 20 epochs for a total of 80 epochs. | definition, denominator, direction and uncertainty | p. 9 (4 Experiments), p. 9 (4 Experiments), p. 6 (Figure/Table caption) |
| Baseline/ablation | The competing methods are then presented and compared. | fair input/data/compute/action matching | p. 9 (4 Experiments), p. 14 (Figure/Table caption), p. 9 (4 Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 13 / 5 Conclusion - extractive body cue:** In this paper, we propose 3DSS-VLG to address the shortage of point-level annotations.
- **p. 13 / 5 Conclusion - extractive body cue:** Specifically, our 3DSS-VLG exploits the superior ability of current vision-language models on aligning the semantics between texts and 2D images, as well as the naturally ...

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Therefore, how to design a network that achieves good performance despite the lack of 2D anno를 문제로 두고, In summary, the main contributions of this paper are as follows: - We propose a weakly supervised method 3DSS-VLG for 3D WSSS, which takes 2D images as a bridge, and leverages natural ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (X. Xu et al), p. 2 (X. Xu et al), p. 3 (X. Xu et al), p. 1 (Body text (section not recovered)), p. 1 (Body text (section not recovered)), p. 1 (Body text (section not recovered)) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
