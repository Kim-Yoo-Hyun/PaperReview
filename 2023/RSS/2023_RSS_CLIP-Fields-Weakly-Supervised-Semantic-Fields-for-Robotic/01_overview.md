# CLIP-Fields: Weakly Supervised Semantic Fields for Robotic Memory

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2210.05663.
> PDF retrieval source: https://arxiv.org/pdf/2210.05663. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2023 / RSS
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: CLIP, Robotics, semantic, NeRF
- Official paper: https://arxiv.org/abs/2210.05663
- Full-text retrieval: https://arxiv.org/pdf/2210.05663
- Code/Project: https://mahis.life/clip-fields/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 However, existing representations are coarse, often relying on a preset list of classes and capturing minimal semantics [2, 11].를 문제로 두고, As a solution, we propose CLIP-Fields, which builds an implicit spatial semantic memory using webscale pretrained models as weak supervision.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** We propose CLIP-Fields, an implicit scene model that can be used for a variety of tasks, such as segmentation, instance identification, semantic search over space, ...
- **p. 1 / Abstract - extractive body cue:** CLIP-Fields learns a mapping from spatial locations to semantic embedding vectors.
- **p. 1 / Abstract - extractive body cue:** Importantly, we show that this mapping can be trained with supervision coming only from webimage and web-text trained models such as CLIP, Detic, and Sentence-BERT; ...
- **p. 1 / Abstract - extractive body cue:** When compared to baselines like Mask-RCNN, our method outperforms on few-shot instance identification or semantic segmentation on the HM3D dataset with only a fraction of ...
- **p. 1 / Abstract - extractive body cue:** Finally, we show that using CLIP-Fields as a scene memory, robots can perform semantic navigation in real-world environments.
- **p. 1 / I. INTRODUCTION - extractive body cue:** However, existing representations are coarse, often relying on a preset list of classes and capturing minimal semantics [2, 11].
- **p. 1 / I. INTRODUCTION - extractive body cue:** Concurrently, web-scale weakly-supervised vision-language models like CLIP [22] have shown that the ability to capture powerful semantic abstractions from individual 2D images.

## Core Idea

- **p. 1 / I. INTRODUCTION - extractive body cue:** As a solution, we propose CLIP-Fields, which builds an implicit spatial semantic memory using webscale pretrained models as weak supervision.
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this work, we introduce a method for building weakly supervised semantic neural fields, called CLIP-Fields, which combines the advantages of both of these lines ...
- **p. 4 / IV. APPROACH - extractive body cue:** We use a Multi-resolution Hash Encoder [20] to learn a low level spatial representation mapping R3 →Rd, which is then mapped to higher dimensions and ...
- **p. 5 / IV. APPROACH - extractive body cue:** semantic label, f = heads ◦g is the associated semantic encoding function, F is a pre-trained semantic language encoder, c is the confidence associated with ...
- **p. 4 / IV. APPROACH - extractive body cue:** We use the following training objectives: Semantic Label Embedding: This objective trains the function encoding the semantic information of a 3D point as a n-dimensional ...
- **p. 5 / IV. APPROACH - extractive body cue:** In this paper's experiments, we use the CLIP ViT-B/32 model embeddings, giving the visual features 512 dimensions.
- **p. 3 / IV. APPROACH - extractive body cue:** When no human annotations are available, we use web-image trained object detection models on our RGB images.
- **p. 3 / IV. APPROACH - extractive body cue:** To train our model, we first preprocess this set of RGB-D frames into a scene dataset (Fig.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Concurrently, web-scale weakly-supervised vision-language models like CLIP [22] have shown that the ability to capture powerful semantic abstractions from individual 2D images. | camera/depth stream, pose, map와 language goal | p. 1 (I. INTRODUCTION), p. 3 (IV. APPROACH) |
| State/latent | Concurrently, web-scale, weakly-supervised, vision-language, models, like, CLIP, have, ability, capture, powerful, semantic | robot pose, free-space/semantic map와 local goal | p. 1 (I. INTRODUCTION), p. 3 (IV. APPROACH), p. 4 (IV. APPROACH) |
| Output/action | For ease of decoding, we constrain the output spaces of f, h to match the embedding space of pre-trained language and vision-language models, respectively. | collision-free trajectory 또는 velocity command | p. 3 (IV. APPROACH), p. 4 (IV. APPROACH), p. 4 (IV. APPROACH) |
| Objective/outcome | While training the contrastive loss objective, we also take into consideration the associated label weights. | goal reach, safety, localization error와 replanning latency | p. 4 (IV. APPROACH), p. 5 (IV. APPROACH), p. 5 (IV. APPROACH) |

## Main Claims and Actual Contribution

- **p. 1 / I. INTRODUCTION - extractive body cue:** As a solution, we propose CLIP-Fields, which builds an implicit spatial semantic memory using webscale pretrained models as weak supervision.
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this work, we introduce a method for building weakly supervised semantic neural fields, called CLIP-Fields, which combines the advantages of both of these lines ...
- **p. 6 / V. EXPERIMENTAL EVALUATION - extractive body cue:** In Figure 5, we see once again that CLIP-Fields outperforms the RGB-based models significantly, to the point where even with three labelled views, CLIP-Fields has ...
- **p. 7 / V. EXPERIMENTAL EVALUATION - extractive body cue:** As the base models naturally improve over time with continuous efforts in the computer vision and natural language processing fields, we expect CLIP-Fields's performance to ...
- **p. 6 / V. EXPERIMENTAL EVALUATION - extractive body cue:** As we can see in Figure 4, the average precision of the predictions retrieved from CLIP-Fields largely outperforms the RGB-models.
- **p. 7 / V. EXPERIMENTAL EVALUATION - extractive body cue:** By doing so, we simulate labelling our training data by a model whose mean accuracy is 1 -p.
- **p. 8 / V. EXPERIMENTAL EVALUATION - extractive body cue:** We consider the navigation task successful if the robot can navigate to and point the camera at an object that satisfies the query.
- **p. 8 / V. EXPERIMENTAL EVALUATION - extractive body cue:** This observation lines up with our simulated experiments in Section V-A4 where we saw that CLIP-Fields performance has a linear relationship with the base models' ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 6 (V. EXPERIMENTAL EVALUATION), p. 7 (V. EXPERIMENTAL EVALUATION) |
| Embodiment/environment | Our visual segmentation experiments are performed on a subset of Habitat-Matterport 3D Semantic (HM3D semantics) [35] dataset, while our robot experiments were performed on a Hello Robot Stretch using Hector SLAM [15]. | hardware/simulator version and reset protocol | p. 5 (V. EXPERIMENTAL EVALUATION), p. 7 (V. EXPERIMENTAL EVALUATION) |
| Dataset/benchmark | 2) Data collection and training: We ran our robot experiment in two different scenes, one in the lab kitchen, and another in the lab library (Figure 9). | role, split, size and leakage | p. 5 (V. EXPERIMENTAL EVALUATION), p. 7 (V. EXPERIMENTAL EVALUATION), p. 7 (V. EXPERIMENTAL EVALUATION), p. 8 (V. EXPERIMENTAL EVALUATION) |
| Metric | 7: Mean average accuracy on the semantic segmentation task on the HM3D Semantic dataset with label noise simulating errors in base labelling models. | definition, denominator, direction and uncertainty | p. 6 (V. EXPERIMENTAL EVALUATION), p. 7 (Figure/Table caption), p. 5 (V. EXPERIMENTAL EVALUATION) |
| Baseline/ablation | In Figure 5, we see once again that CLIP-Fields outperforms the RGB-based models significantly, to the point where even with three labelled views, CLIP-Fields has a higher AP than any of the ... | fair input/data/compute/action matching | p. 6 (V. EXPERIMENTAL EVALUATION), p. 5 (V. EXPERIMENTAL EVALUATION), p. 5 (V. EXPERIMENTAL EVALUATION) |

## Explicit Limitations and Failure Boundary

- **p. 8 / VI. CONCLUSIONS AND FUTURE WORK - extractive body cue:** In future work, we hope to explore models that share parameters across scenes, and can handle dynamic scenes and objects.
- **p. 5 / V. EXPERIMENTAL EVALUATION - extractive body cue:** Detic is absent from the first two evaluations since it is a detection model and thus cannot be fine-tuned on segmentation labels.
- **p. 8 / V. EXPERIMENTAL EVALUATION - extractive body cue:** However, if an object was misidentified during data preparation, CLIP-Fields fails to correctly identify it as well.
- **p. 6 / V. EXPERIMENTAL EVALUATION - extractive body cue:** 4) CLIP-Fields's robustness to label errors: In real-world applications, CLIP-Fields relies on labels given by large
- **p. 6 / V. EXPERIMENTAL EVALUATION - extractive body cue:** 7: Mean average accuracy on the semantic segmentation task on the HM3D Semantic dataset with label noise simulating errors in base labelling models.
- **p. 7 / V. EXPERIMENTAL EVALUATION - extractive body cue:** In this section, we examine the robustness of CLIP-Fields to such label errors.

## Why Read It

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 However, existing representations are coarse, often relying on a preset list of classes and capturing minimal semantics [2, 11].를 문제로 두고, As a solution, we propose CLIP-Fields, which builds an implicit spatial semantic memory using webscale pretrained models as weak supervision.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 4 (IV. APPROACH), p. 5 (IV. APPROACH), p. 4 (IV. APPROACH), p. 5 (IV. APPROACH) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
