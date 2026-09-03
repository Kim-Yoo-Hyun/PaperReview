# Dense Multimodal Alignment for Open-Vocabulary 3D Scene Understanding

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/6612_ECCV_2024_paper.php.
> PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/06612.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / ECCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: 3D Vision, semantic
- Official paper: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/6612_ECCV_2024_paper.php
- Full-text retrieval: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/06612.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 To build dense associations across different modalities, the primary bottleneck is how to obtain rich and reliable text descriptions without relying on manual labeling.를 문제로 두고, In order to leverage the synergistic benefits of multiple modalities for dense prediction tasks, we propose a dense multimodal alignment (DMA) strategy to co-embed 3D points, image pixels, and text strings into ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / 1 Introduction - extractive body cue:** 3D scene understanding, which aims to achieve accurate comprehension of objects as well as their attributes and relationships within a scene, has gained significant attention ...
- **p. 1 / 1 Introduction - extractive body cue:** However, the annotation of large-scale 3D data is very costly [7,11], impeding the training of generalizable models for open-vocabulary scene understanding.
- **p. 1 / 1 Introduction - extractive body cue:** Though many existing methods [9,10,20,29-31,41,46,58] have achieved significant advancements in recognizing closed-set categories for specific tasks, they fail to identify novel categories and other types ...
- **p. 2 / 1 Introduction - extractive body cue:** In contrast to the limited 3D data, modalities such as images and texts are more abundantly available.
- **p. 2 / 1 Introduction - extractive body cue:** Existing pre-trained multimodal models, such as CLIP [43] and ALIGN [24], have shown impressive zero-shot recognition ability by training on large-scale noisy image-text pairs, and ...
- **p. 2 / 1 Introduction - extractive body cue:** To build dense associations across different modalities, the primary bottleneck is how to obtain rich and reliable text descriptions without relying on manual labeling.
- **p. 2 / 1 Introduction - extractive body cue:** On the other hand, by fine-tuning its mask head, we incorporate 3D structural priors into 2D features, better adapting the model to 3D dense tasks.

## Core Idea

- **p. 2 / 1 Introduction - extractive body cue:** In order to leverage the synergistic benefits of multiple modalities for dense prediction tasks, we propose a dense multimodal alignment (DMA) strategy to co-embed 3D ...
- **p. 4 / 3 Method - extractive body cue:** 1, we propose a dense multimodal alignment (DMA) framework for open-vocabulary 3D scene understanding, where we construct dense correspondences across 2D image pixels, 3D points ...
- **p. 9 / 3 Method - extractive body cue:** By densely aligning these modalities in a shared space, our method can maximize the synergistic benefits among them and achieve outstanding segmentation performance without compromising ...
- **p. 1 / 1 Introduction - extractive body cue:** Though many existing methods [9,10,20,29-31,41,46,58] have achieved significant advancements in recognizing closed-set categories for specific tasks, they fail to identify novel categories and other types ...
- **p. 5 / 3 Method - extractive body cue:** Firstly, we use the image tagging foundation model such as RAM [23] to extract all possible categories from an image, and utilize category names and ...
- **p. 7 / 3 Method - extractive body cue:** On one hand, we use the frozen CLIP visual encoder to ensure the intactness of image-text alignment, obtaining CLIP features f2D clip.
- **p. 8 / 3 Method - extractive body cue:** Firstly, we extract 3D features for the point cloud by utilizing a 3D network, denoted as ε3D.
- **p. 8 / 3 Method - extractive body cue:** We use the text-to-3D label map M 3D as the pseudo label to facilitate the alignment of point and text features.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Given the input list, we instruct GPT to examine the words one by one and perform reasoning according to the chain of thought, outputting a boolean list indicating whether a word is ... | RGB-D, image set, point cloud, depth와 camera pose | p. 5 (3 Method), p. 6 (3 Method) |
| State/latent | Given, input, list, instruct, GPT, examine, words, perform, reasoning, according, chain, thought | geometry, map, object/relationship state | p. 5 (3 Method), p. 6 (3 Method), p. 6 (3 Method) |
| Output/action | Owing to the exposure to a diverse range of linguistic patterns and contextual nuances, the MLLMs can generate comprehensive and in-depth descriptions based on input images. | point map, pose, scene graph, affordance 또는 query result | p. 6 (3 Method), p. 6 (3 Method), p. 2 (1 Introduction) |
| Objective/outcome | For 3D-2D pairs, we follow the previous work [42] to fuse pixel embeddings across K different views, represented as [f2D 1 , · · · , f2D K ], into a single ... | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 9 (3 Method), p. 8 (3 Method), p. 8 (3 Method) |

## Main Claims and Actual Contribution

- **p. 2 / 1 Introduction - extractive body cue:** In order to leverage the synergistic benefits of multiple modalities for dense prediction tasks, we propose a dense multimodal alignment (DMA) strategy to co-embed 3D ...
- **p. 4 / 3 Method - extractive body cue:** 1, we propose a dense multimodal alignment (DMA) framework for open-vocabulary 3D scene understanding, where we construct dense correspondences across 2D image pixels, 3D points ...
- **p. 9 / 3 Method - extractive body cue:** By densely aligning these modalities in a shared space, our method can maximize the synergistic benefits among them and achieve outstanding segmentation performance without compromising ...
- **p. 1 / 1 Introduction - extractive body cue:** Though many existing methods [9,10,20,29-31,41,46,58] have achieved significant advancements in recognizing closed-set categories for specific tasks, they fail to identify novel categories and other types ...
- **p. 10 / 4 Experiments - extractive body cue:** Our DMA(OpenSeg) using only 3D model for prediction outperforms OpenScene(OpenSeg)-2D3D by 5.4% mIoU at a significantly lower latency, wherein the mIoU (F) and mIoU (B) ...
- **p. 14 / Figure/Table caption - extractive body cue:** Fig. 7: Open-vocabulary segmentation results on rare categories and different forms of queries. The same color corresponds to the same query/category. priors into mask features. ...
- **p. 10 / 4 Experiments - extractive body cue:** 2, by densely aligning with the tagging information and the detailed description extracted from each scene, our DMA(OpenSeg) using only 3D encoder significantly improves the ...
- **p. 13 / Figure/Table caption - extractive body cue:** Table 6: Comparisons of dif- ferent fine-tuning methods. performance to using both 2D and 3D encoders by solely utilizing the 3D encoder, i.e., 53.3% vs. ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 10 (4 Experiments), p. 14 (Figure/Table caption) |
| Embodiment/environment | As for nuScenes dataset, we use 8 GPUs for training and set the batch size as 16. | hardware/simulator version and reset protocol | p. 9 (4 Experiments), p. 9 (4 Experiments) |
| Dataset/benchmark | To validate the effectiveness of our method on outdoor point clouds, we evaluate the performance of DMA on the nuScenes dataset [4]. | role, split, size and leakage | p. 9 (4 Experiments), p. 9 (4 Experiments), p. 10 (4 Experiments), p. 11 (4 Experiments) |
| Metric | The mean Intersection-of-Union (mIoU), mean Accuracy (mACC), Precision, and Recall are employed as the evaluation metrics. | definition, denominator, direction and uncertainty | p. 9 (4 Experiments), p. 11 (4 Experiments), p. 12 (4 Experiments) |
| Baseline/ablation | We conduct comparisons with state-of-the-art methods on each of these datasets. | fair input/data/compute/action matching | p. 9 (4 Experiments), p. 10 (4 Experiments), p. 10 (4 Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 2: Scene tagging generation. (1) We first employ RAM [57] to generate view-level tags, and then (2) reduce the tag noise with GPT. Finally, ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 3: Segmentation results using 2D and 3D models. 2D model has advantages in segmenting background objects (in blue boxes), while 3D model is more ...
- **p. 12 / 4 Experiments - extractive body cue:** Our method, however, directly aligns with the textual modality, overcoming the limitations of 2D models.
- **p. 11 / 4 Experiments - extractive body cue:** Our method does not rely on ground truth 3D labels but instead distill knowledge from pretrained vision-language models, thus it is more robust to rare ...
- **p. 14 / 5 Conclusion - extractive body cue:** We presented a dense multimodal alignment (DMA) framework for open-vocabulary 3D scene understanding by establishing dense correspondences between 3D points, 2D images and 1D texts, ...
- **p. 11 / 4 Experiments - extractive body cue:** This is because there are only a few instances available on these long-tail categories, which is not sufficient to train a robust model from scratch.

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 To build dense associations across different modalities, the primary bottleneck is how to obtain rich and reliable text descriptions without relying on manual labeling.를 문제로 두고, In order to leverage the synergistic benefits of multiple modalities for dense prediction tasks, we propose a dense multimodal alignment (DMA) strategy to co-embed 3D points, image pixels, and text strings into ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction), p. 5 (3 Method) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
