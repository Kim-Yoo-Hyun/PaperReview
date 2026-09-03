# Towards CLIP-driven Language-free 3D Visual Grounding via 2D-3D Relational Enhancement and Consistency

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Zhang_Towards_CLIP-driven_Language-free_3D_Visual_Grounding_via_2D-3D_Relational_Enhancement_CVPR_2024_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Zhang_Towards_CLIP-driven_Language-free_3D_Visual_Grounding_via_2D-3D_Relational_Enhancement_CVPR_2024_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: 3D visual grounding, CLIP, consistency
- Official paper: https://openaccess.thecvf.com/content/CVPR2024/html/Zhang_Towards_CLIP-driven_Language-free_3D_Visual_Grounding_via_2D-3D_Relational_Enhancement_CVPR_2024_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2024/papers/Zhang_Towards_CLIP-driven_Language-free_3D_Visual_Grounding_via_2D-3D_Relational_Enhancement_CVPR_2024_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Although language-free training based on implicit feature substitution looks promising for various 2D visionlanguage tasks, it encounters several specific challenges when applied to 3D point clouds: (1) Insufficient 3Dlanguage alignment ...를 문제로 두고, Overall, our contributions can be summarized as follows: • We introduce a CLIP-driven language-free 3DVG framework, which requires no manually annotated texts to effectively achieve 3D visual grounding on point clouds. • ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** 3D visual grounding plays a crucial role in scene understanding, with extensive applications in AR/VR.
- **p. 1 / Abstract - extractive body cue:** Despite the significant progress made in recent methods, the requirement of dense textual descriptions for each individual object, which is time-consuming and costly, hinders their ...
- **p. 1 / Abstract - extractive body cue:** To mitigate reliance on text annotations during training, researchers have explored language-free training paradigms in the 2D field via explicit text generation or implicit feature ...
- **p. 1 / Abstract - extractive body cue:** Nevertheless, unlike 2D images, the complexity of spatial relations in 3D, coupled with the absence of robust 3D visual language pre-trained models, makes it challenging ...
- **p. 1 / Abstract - extractive body cue:** To tackle the above issues, in this paper, we introduce a language-free training framework for 3D visual grounding.
- **p. 2 / 1. Introduction - extractive body cue:** Although language-free training based on implicit feature substitution looks promising for various 2D visionlanguage tasks, it encounters several specific challenges when applied to 3D point ...
- **p. 1 / 1. Introduction - extractive body cue:** However, training current 3DVG models demands sufficient detailed text descriptions of each object, which are time-consuming and costly to acquire.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** Overall, our contributions can be summarized as follows: • We introduce a CLIP-driven language-free 3DVG framework, which requires no manually annotated texts to effectively achieve ...
- **p. 2 / 1. Introduction - extractive body cue:** To address the above issues, we propose a LanguageFree training method for 3D Visual Grounding, named 3DLFVG.
- **p. 3 / 3.1. Overview - extractive body cue:** The objective of our method is to train a model to localize specified objects without using any language queries during training, yet capable of identifying ...
- **p. 4 / 3.1. Overview - extractive body cue:** Since our method capitalizes on the image-text feature alignment provided by CLIP, and incorporates extra modules that enhance the features with relation-aware capabilities.
- **p. 4 / 3.3. Relation Injection - extractive body cue:** (2) Since there is no supervision of this relation during our training process, we introduce the proxy task of predicting the target object to achieve ...
- **p. 5 / 3.4. Training and Inference - extractive body cue:** Here we first detail the network training objectives of learning with pseudolanguage features, and then outline the inference process using point clouds with authentic language ...
- **p. 3 / 3.1. Overview - extractive body cue:** Our language-free 3DVG training framework comprises three key modules: Pseudo-Language Feature Generation (PFG), Neighboring Relation-aware Modeling (NRM), and Cross-modality Relation Consistency (CRC).
- **p. 4 / 3.3. Relation Injection - extractive body cue:** To bridge this gap and enhance the relation representation ability of our CLIP-driven pseudo-language features, we further introduce a neighboring relation-aware module and a cross-modality ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | During training phase, the inputs consist of two parts: a point cloud P ∈RN×(3+F ) (with 3D coordinates and F-dimensional auxiliary features) of N points, and corresponding multi-view images M = {Ii}NI ... | RGB-D, image set, point cloud, depth와 camera pose | p. 3 (3.1. Overview), p. 3 (3.1. Overview) |
| State/latent | During, training, phase, inputs, consist, parts, point, cloud, coordinates, F-dimensional, auxiliary, features | geometry, map, object/relationship state | p. 3 (3.1. Overview), p. 3 (3.1. Overview), p. 5 (3.4. Training and Inference) |
| Output/action | At inference stage, the inputs shift to include a point cloud P ∈RN×(3+F ) and a sentence query Q ∈RL designed to describe the target object. | point map, pose, scene graph, affordance 또는 query result | p. 3 (3.1. Overview), p. 5 (3.4. Training and Inference), p. 2 (1. Introduction) |
| Objective/outcome | 3.3, we describe the methods for augmenting the pseudo-language features with more neighboring relation information and the construction of 2D and 3D relational consistency constraints. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 3 (3. Methodology), p. 3 (3.1. Overview), p. 5 (3.4. Training and Inference) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** Overall, our contributions can be summarized as follows: • We introduce a CLIP-driven language-free 3DVG framework, which requires no manually annotated texts to effectively achieve ...
- **p. 2 / 1. Introduction - extractive body cue:** To address the above issues, we propose a LanguageFree training method for 3D Visual Grounding, named 3DLFVG.
- **p. 3 / 3.1. Overview - extractive body cue:** The objective of our method is to train a model to localize specified objects without using any language queries during training, yet capable of identifying ...
- **p. 4 / 3.1. Overview - extractive body cue:** Since our method capitalizes on the image-text feature alignment provided by CLIP, and incorporates extra modules that enhance the features with relation-aware capabilities.
- **p. 4 / 3.3. Relation Injection - extractive body cue:** (2) Since there is no supervision of this relation during our training process, we introduce the proxy task of predicting the target object to achieve ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Quantitative comparison of language-free (LF) 3DVG on ScanRefer [4] dataset. Results of relevant fully supervised (Fully) meth- ods are also provided. Accuracy (Acc) ...
- **p. 6 / 4.3. Compared Methods - extractive body cue:** Pseudo-Q [16] is currently a method that has achieved good performance in 2D language-free grounding.
- **p. 7 / 4.3. Compared Methods - extractive body cue:** Qualitative results from Pseudo-Q [16], Zero-shot-RIS [40] and our method.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | SYSTEM / EVALUATION SCOPE UNRESOLVED | do not infer unreported downstream behavior | p. 6 (Figure/Table caption), p. 6 (4.3. Compared Methods) |
| Embodiment/environment | We follow the ScanRefer benchmark to divide our dataset into the train/val/test set with 36,655, 9,508, and 5,410 samples respectively, and utilize val set to evaluate our framework. | hardware/simulator version and reset protocol | p. 5 (4.1. Datasets), p. 5 (4.1. Datasets) |
| Dataset/benchmark | Given its ability to perform 3DVG without text-based training, akin to our proposed paradigm, OpenScene serves as a benchmark for comparison. | role, split, size and leakage | p. 5 (4.1. Datasets), p. 5 (4.1. Datasets), p. 6 (4.3. Compared Methods), p. 6 (4.2. Implementation Details) |
| Metric | Accuracy (Acc) under 0.25 and 0.5 IoU thresholds in "Unique", "Multiple", and "Overall" is reported respectively. | definition, denominator, direction and uncertainty | p. 6 (4.2. Implementation Details), p. 6 (Figure/Table caption), p. 5 (4.2. Implementation Details) |
| Baseline/ablation | Without language supervision, our method significantly outperforms previous methods. † indicates our re-implemented method on 3D. | fair input/data/compute/action matching | p. 6 (4.2. Implementation Details), p. 5 (4.2. Implementation Details), p. 7 (4.3. Compared Methods) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 5. Conclusion - extractive body cue:** Extensive experiments conducted on mainstream datasets demonstrate the robustness and efficiency of our approach.
- **p. 7 / 4.3. Compared Methods - extractive body cue:** It does not have a red chair near it.
- **p. 8 / Figure/Table caption - extractive body cue:** Table 3. Ablation study on main components of our method. We report the "overall" results in terms of Acc@0.25 and Acc@0.5. PFG Relation Acc@0.25 Acc@0.5 ...

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Although language-free training based on implicit feature substitution looks promising for various 2D visionlanguage tasks, it encounters several specific challenges when applied to 3D point clouds: (1) Insufficient 3Dlanguage alignment ...를 문제로 두고, Overall, our contributions can be summarized as follows: • We introduce a CLIP-driven language-free 3DVG framework, which requires no manually annotated texts to effectively achieve 3D visual grounding on point clouds. • ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 5 (3.4. Training and Inference), p. 4 (3.3. Relation Injection), p. 3 (3.1. Overview) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
