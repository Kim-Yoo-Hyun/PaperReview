# ConceptFusion: Open-set Multimodal 3D Mapping

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (19 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2302.07241.
> PDF retrieval source: https://arxiv.org/pdf/2302.07241. Reading tracker status/evidence was not changed.

- Year/Venue: 2023 / RSS
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: CORE
- Tags: sensor fusion, open-vocabulary, SLAM, Robotics
- Official paper: https://arxiv.org/abs/2302.07241
- Full-text retrieval: https://arxiv.org/pdf/2302.07241
- Code/Project: https://concept-fusion.github.io/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-02 (19 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 In this work, we bridge the gap between the rich open-set capabilities enabled by large foundation models and the semantic reasoning abilities expected of futuristic 3D mapping systems.를 문제로 두고, To mitigate this, we introduce a novel mechanism to construct pixel-aligned features that combine global (image-level) context encapsulated in models like CLIP, with local (region-level) information.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Building 3D maps of the environment is central to robot navigation, planning, and interaction with objects in a scene.
- **p. 1 / Abstract - extractive body cue:** Most existing approaches that integrate semantic concepts with 3D maps largely remain confined to the closed-set setting: they can only reason about a finite set ...
- **p. 1 / Abstract - extractive body cue:** Further, these maps can only be queried using class labels, or in more recent work, using text prompts.
- **p. 1 / Abstract - extractive body cue:** We address both these issues with ConceptFusion, a scene representation that is: (i) fundamentally open-set, enabling reasoning beyond a closed set of concepts (ii) inherently ...
- **p. 1 / Abstract - extractive body cue:** ConceptFusion leverages the open-set capabilities of today's foundation models that have been pretrained on internet-scale data to reason about concepts across modalities such as natural ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** In this work, we bridge the gap between the rich open-set capabilities enabled by large foundation models and the semantic reasoning abilities expected of futuristic ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** This major limitation exists because most foundation models consume images (e.g., CLIP [6], ALIGN [9], AudioCLIP [8]) and produce only a single vector encoding of ...

## Core Idea

- **p. 4 / IV. THE ConceptFusion APPROACH - extractive body cue:** To mitigate this, we introduce a novel mechanism to construct pixel-aligned features that combine global (image-level) context encapsulated in models like CLIP, with local (region-level) ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Our key contributions are the following: • An approach to open-set multimodal 3D mapping that constructs map representations queryable by text, image, audio, and click ...
- **p. 4 / IV. THE ConceptFusion APPROACH - extractive body cue:** Given an input image X ∈R3×H×W , our method uses a foundation model F as a feature extractor to produce three types of embeddings, which ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Crucially, we show that this approach is conceptually simple, principled, and effective even in the zero-shot setting (requiring no additional training or finetuning of foundation ...
- **p. 5 / IV. THE ConceptFusion APPROACH - extractive body cue:** To the right, we show sample reconstructions and semantic annotations over two sub-sequences.
- **p. 4 / IV. THE ConceptFusion APPROACH - extractive body cue:** We then present our algorithm to compute pixel-aligned features zero-shot from off-the-shelf foundation models (such as CLIP [6], AudioCLIP [8], and variants).
- **p. 6 / IV. THE ConceptFusion APPROACH - extractive body cue:** Real-time inference: To optimize the performance and efficiency of the foundation models employed (SAM [57], DINO [7], and CLIP [6]), we use standard quantization and ...
- **p. 6 / IV. THE ConceptFusion APPROACH - extractive body cue:** For generating class-agnostic (generic) object masks, we use the Mask2Former [60] or the segment anything (SAM) [57] models for category-agnostic instance segmentation.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The open-set multimodal 3D mapping problem: Given a sequence of image (and depth) observations of an environment | camera/depth stream, pose, map와 language goal | p. 3 (IV. THE ConceptFusion APPROACH), p. 4 (IV. THE ConceptFusion APPROACH) |
| State/latent | open-set, multimodal, mapping, problem, Given, sequence, image, depth, observations, environment, IV-B, compute | robot pose, free-space/semantic map와 local goal | p. 3 (IV. THE ConceptFusion APPROACH), p. 4 (IV. THE ConceptFusion APPROACH), p. 4 (IV. THE ConceptFusion APPROACH) |
| Output/action | IV-B, we compute the semantic context embedding fP u,v,t ∈fP Xt for each pixel in the input image Xt. | collision-free trajectory 또는 velocity command | p. 4 (IV. THE ConceptFusion APPROACH), p. 4 (IV. THE ConceptFusion APPROACH), p. 6 (IV. THE ConceptFusion APPROACH) |
| Objective/outcome | The centroid of the point set returned by the query term refrigerator and television are shown as blue circles, and the estimated distance between them (6.303 metres) as a straight line. | goal reach, safety, localization error와 replanning latency | p. 5 (IV. THE ConceptFusion APPROACH), p. 6 (IV. THE ConceptFusion APPROACH), p. 6 (IV. THE ConceptFusion APPROACH) |

## Main Claims and Actual Contribution

- **p. 4 / IV. THE ConceptFusion APPROACH - extractive body cue:** To mitigate this, we introduce a novel mechanism to construct pixel-aligned features that combine global (image-level) context encapsulated in models like CLIP, with local (region-level) ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Our key contributions are the following: • An approach to open-set multimodal 3D mapping that constructs map representations queryable by text, image, audio, and click ...
- **p. 4 / IV. THE ConceptFusion APPROACH - extractive body cue:** Given an input image X ∈R3×H×W , our method uses a foundation model F as a feature extractor to produce three types of embeddings, which ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Crucially, we show that this approach is conceptually simple, principled, and effective even in the zero-shot setting (requiring no additional training or finetuning of foundation ...
- **p. 5 / IV. THE ConceptFusion APPROACH - extractive body cue:** To the right, we show sample reconstructions and semantic annotations over two sub-sequences.
- **p. 6 / IV. THE ConceptFusion APPROACH - extractive body cue:** By applying both quantization and tracing techniques to our models, we are able to achieve significant improvements in their efficiency, without compromising their accuracy.
- **p. 10 / 4) What previously infeasible downstream use-cases can - extractive body cue:** We see that, each component of the proposed method results in clear, significant improvement in performance.
- **p. 8 / 4) What previously infeasible downstream use-cases can - extractive body cue:** Here, we again observe that ConceptFusion outperforms other finetuned foundation models by a significant margin in terms of both 3D mIoU and detection accuracy.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 6 (IV. THE ConceptFusion APPROACH), p. 10 (4) What previously infeasible downstream use-cases can) |
| Embodiment/environment | This real-world dataset comprises 3D scans of 78 commonly found household and office objects on a tabletop surface (see Fig. | hardware/simulator version and reset protocol | p. 7 (4) What previously infeasible downstream use-cases can), p. 8 (4) What previously infeasible downstream use-cases can) |
| Dataset/benchmark | Experimental setup: Our experimental benchmark comprises of sequences from multiple publicly available datasets, and sequences we collect. | role, split, size and leakage | p. 7 (4) What previously infeasible downstream use-cases can), p. 8 (4) What previously infeasible downstream use-cases can), p. 6 (4) What previously infeasible downstream use-cases can), p. 6 (4) What previously infeasible downstream use-cases can) |
| Metric | Accuracy (%) IoU source-ambiguous Random 7.14% N/A AudioCLIP [8] 23.81% N/A ConceptFusion 64.29% 0.287 ecological Random 5.56% N/A AudioCLIP [8] 22.22% N/A ConceptFusion 66.67% 0.301 TABLE IV: Audio-query based detection and classificat ... | definition, denominator, direction and uncertainty | p. 6 (IV. THE ConceptFusion APPROACH), p. 10 (VI. OUTLOOK), p. 6 (IV. THE ConceptFusion APPROACH) |
| Baseline/ablation | Fig. 7: Text queries over ScanNet [61]: ConceptFusion is able to handle long-form text queries and accurately localize objects referenced by the query. In the first two scenarios, OpenSeg [18] is distracted ... | fair input/data/compute/action matching | p. 7 (Figure/Table caption), p. 8 (4) What previously infeasible downstream use-cases can), p. 10 (VI. OUTLOOK) |

## Explicit Limitations and Failure Boundary

- **p. 9 / 4) What previously infeasible downstream use-cases can - extractive body cue:** The GenericLLM-Agent fails to achieve the specified task since it does not have an explicit 3D map representation, devoiding the LLM of the requisite context ...
- **p. 11 / VII. CONCLUSION - extractive body cue:** Limitations: The key limitations of our method are threefold.
- **p. 11 / VII. CONCLUSION - extractive body cue:** Third, we anticipate ConceptFusion to inherit the limitations and biases of foundation models [5, 75], warranting further investigations for potential harm as well as research ...
- **p. 12 / VII. CONCLUSION - extractive body cue:** As investigated in [82, 83, 73], CLIP does not inherently capture spatial relationships or compositions.
- **p. 10 / VI. OUTLOOK - extractive body cue:** However, this approach still fails for room-level containment queries of type is <OBJ> in <ROOM>); which require additional context.
- **p. 10 / 4) What previously infeasible downstream use-cases can - extractive body cue:** The "Remove uniqueness term..." variant fuses features computed from individual masks with those computed over the entire image, but does not account for mask uniqueness ...
- **p. 7 / 4) What previously infeasible downstream use-cases can - extractive body cue:** ConceptFusion exhibits more graceful performance degradation to unstructured queries (long sentences).

## Why Read It

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 In this work, we bridge the gap between the rich open-set capabilities enabled by large foundation models and the semantic reasoning abilities expected of futuristic 3D mapping systems.를 문제로 두고, To mitigate this, we introduce a novel mechanism to construct pixel-aligned features that combine global (image-level) context encapsulated in models like CLIP, with local (region-level) information.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 4 (IV. THE ConceptFusion APPROACH), p. 4 (IV. THE ConceptFusion APPROACH), p. 6 (IV. THE ConceptFusion APPROACH), p. 6 (IV. THE ConceptFusion APPROACH) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
