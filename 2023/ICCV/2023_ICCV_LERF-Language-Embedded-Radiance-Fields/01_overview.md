# LERF: Language Embedded Radiance Fields

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2303.09553.
> PDF retrieval source: https://arxiv.org/pdf/2303.09553. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2023 / ICCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: NeRF, Vision-Language, grounding
- Official paper: https://arxiv.org/abs/2303.09553
- Full-text retrieval: https://arxiv.org/pdf/2303.09553
- Code/Project: https://www.lerf.io/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 To regularize the optimized language field, self-supervised DINO [5] features are also incorporated through a shared bottleneck.를 문제로 두고, In this work, we propose Language Embedded Radiance Fields (LERF), a novel approach that grounds language within NeRF by optimizing embeddings from an offthe-shelf vision-language model like CLIP into 3D scenes.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Humans describe the physical world using natural language to refer to specific 3D locations based on a vast range of properties: visual appearance, semantics, abstract ...
- **p. 1 / Abstract - extractive body cue:** In this work we propose Language Embedded Radiance Fields (LERFs), a method for grounding language embeddings from off-the-shelf models like CLIP into NeRF, which enable ...
- **p. 1 / Abstract - extractive body cue:** LERF learns a dense, multiscale language field inside NeRF by volume rendering CLIP embeddings along training rays, supervising these embeddings across training views to provide ...
- **p. 1 / Abstract - extractive body cue:** After optimization, LERF can extract 3D relevancy maps for a broad range of language prompts interactively in real-time, which has potential use cases in robotics, ...
- **p. 1 / Abstract - extractive body cue:** LERF enables pixel-aligned, zero-shot queries on the distilled 3D 1.
- **p. 2 / 1. Introduction - extractive body cue:** To regularize the optimized language field, self-supervised DINO [5] features are also incorporated through a shared bottleneck.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** In this work, we propose Language Embedded Radiance Fields (LERF), a novel approach that grounds language within NeRF by optimizing embeddings from an offthe-shelf vision-language ...
- **p. 2 / 1. Introduction - extractive body cue:** Upon completion of the training process, LERF allows for the generation of 3D relevancy maps for a wide range of language prompts in realtime.
- **p. 6 / 3.4. Field Architecture - extractive body cue:** We adopt the Nerfacto method from Nerfstudio [35] as the backbone for our approach, leveraging the same proposal sampling, scene contraction, and appearance embeddings
- **p. 6 / 3.4. Field Architecture - extractive body cue:** We capture this inductive bias in LERF by training two separate networks: one for feature vectors (DINO, CLIP), and the other for standard NeRF outputs ...
- **p. 7 / 3.6. Implementation Details - extractive body cue:** We use the Adam optimizer for proposal networks and fields with weight decay 10-9, with an exponential learning rate scheduler from 10-2 to 10-3 over ...
- **p. 7 / 3.6. Implementation Details - extractive body cue:** We use the OpenClip [10] ViTB/16 model trained on the LAION-2B dataset, with an image pyramid varying from smin = .05 to smin = .5 ...
- **p. 6 / 3.4. Field Architecture - extractive body cue:** Scale s is passed into the CLIP MLP as an extra input in addition to the concatenated hashgrid features.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | We construct a LERF by optimizing a language field jointly with NeRF, which takes both position and physical scale as input and outputs a single CLIP vector. | RGB-D, image set, point cloud, depth와 camera pose | p. 2 (1. Introduction), p. 2 (1. Introduction) |
| State/latent | construct, LERF, optimizing, language, field, jointly, NeRF, takes, position, physical, scale, input | geometry, map, object/relationship state | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 6 (3.4. Field Architecture) |
| Output/action | This requires not only the capacity to handle natural language input queries but also the ability to incorporate semantics at multiple scales and relate to long-tail and abstract concepts. | point map, pose, scene graph, affordance 또는 query result | p. 2 (1. Introduction), p. 6 (3.4. Field Architecture), p. 6 (3.4. Field Architecture) |
| Objective/outcome | Gradients from Llang and Ldino do not affect the NeRF outputs, and can be viewed as jointly optimizing a language field in conjunction with a radiance field. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 6 (3.4. Field Architecture), p. 7 (3.6. Implementation Details), p. 6 (3.4. Field Architecture) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** In this work, we propose Language Embedded Radiance Fields (LERF), a novel approach that grounds language within NeRF by optimizing embeddings from an offthe-shelf vision-language ...
- **p. 2 / 1. Introduction - extractive body cue:** Upon completion of the training process, LERF allows for the generation of 3D relevancy maps for a wide range of language prompts in realtime.
- **p. 6 / 3.4. Field Architecture - extractive body cue:** We adopt the Nerfacto method from Nerfstudio [35] as the backbone for our approach, leveraging the same proposal sampling, scene contraction, and appearance embeddings
- **p. 8 / 4.3. Localization - extractive body cue:** OwL-ViT outperforms LSeg in 3D, but suffers compared to LERF on long-tail queries.
- **p. 8 / 4.4. Ablations - extractive body cue:** We show two illustrative examples where DINO improves the quality of relevancy maps in Fig.
- **p. 7 / 4. Experiments - extractive body cue:** Overall performance is calculated by aggregating scene results.
- **p. 7 / 4.1. Qualitative Results - extractive body cue:** We visualize relevancy score by normalizing the colormap for each query from 50% (less relevant than canonical phrases) to the maximum relevancy.
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3: Results with LERF for 5 in-the-wild scenes. Each image shows a visual rendering of the LERF (Sec. 3), along with relevancy renderings (Sec. ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 8 (4.3. Localization), p. 8 (4.4. Ablations) |
| Embodiment/environment | Emphasizing the capability of LERF to handle real-world data, we collect 13 scenes containing a mixture of in-the-wild (grocery store, kitchen, bookstore) and posed long-tail (teatime, figurines, hand) scenes. | hardware/simulator version and reset protocol | p. 7 (4. Experiments), p. 7 (4. Experiments) |
| Dataset/benchmark | To evaluate how well LERF can localize text prompts in a scene we render novel views and label bounding boxes for 72 objects across 5 scenes. | role, split, size and leakage | p. 7 (4. Experiments), p. 7 (4. Experiments), p. 8 (4.3. Localization), p. 8 (4.1. Qualitative Results) |
| Metric | We report precision-recall curves over relevancy score thresholds in Fig. | definition, denominator, direction and uncertainty | p. 8 (4.2. Existence Determination), p. 8 (4.3. Localization), p. 3 (Figure/Table caption) |
| Baseline/ablation | OwL-ViT outperforms LSeg in 3D, but suffers compared to LERF on long-tail queries. | fair input/data/compute/action matching | p. 8 (4.3. Localization), p. 8 (4.3. Localization), p. 7 (4. Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 5. Limitations - extractive body cue:** LERF has limitations associated with both CLIP and NeRF; some are visualized in Fig.
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 7: Comparison to LSeg in 3D: LSeg performs well on "glass of water" since cups are in the COCO dataset, but cannot locate an ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 9: Failure cases: LERF struggles with identifying objects that appear visually similar to the query: "Zucchini" also acti- vates on other long, green-ish vegetables, ...
- **p. 11 / Figure/Table caption - extractive body cue:** Figure 10: Language and visual ambiguities from CLIP: Cases with incorrect relevancy renders. Some failures can be attributed to visual similarity to the query (eg ...
- **p. 13 / Figure/Table caption - extractive body cue:** Figure 15: Geometric separation impacts quality: Queries without much geometric separation can blur between objects and foreground-background. In the toaster case, very few viewing an- ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 5: Ablations: We ablate DINO regularization and multi- scale training (Sec. 4.4), and highlight qualitative degradation in relevancy maps here. by a constant λlang ...
- **p. 13 / Figure/Table caption - extractive body cue:** Figure 14: Degradation with poor NeRF geometry: Floaters and incomplete geometry can produce unreliable rendered CLIP em- beddings.

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 To regularize the optimized language field, self-supervised DINO [5] features are also incorporated through a shared bottleneck.를 문제로 두고, In this work, we propose Language Embedded Radiance Fields (LERF), a novel approach that grounds language within NeRF by optimizing embeddings from an offthe-shelf vision-language model like CLIP into 3D scenes.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 6 (3.4. Field Architecture), p. 7 (3.6. Implementation Details), p. 7 (3.6. Implementation Details), p. 6 (3.4. Field Architecture), p. 8 (4.3. Localization) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
