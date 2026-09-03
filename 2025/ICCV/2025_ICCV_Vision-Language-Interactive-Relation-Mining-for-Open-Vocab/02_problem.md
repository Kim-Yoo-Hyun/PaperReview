# Problem - Vision-Language Interactive Relation Mining for Open-Vocabulary Scene Graph Generation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Min_Vision-Language_Interactive_Relation_Mining_for_Open-Vocabulary_Scene_Graph_Generation_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Min_Vision-Language_Interactive_Relation_Mining_for_Open-Vocabulary_Scene_Graph_Generation_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction)): Since existing pre-trained VLMs lack relation-aware knowledge [5], directly building a VLM for OV-SGG is challenging.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** To promote the deployment of scenario understanding in the real world, Open-Vocabulary Scene Graph Generation (OV-SGG) has attracted much attention recently, aiming to generalize beyond ...
- **p. 1 / Abstract - extractive body cue:** Towards OV-SGG, one feasible solution is to leverage the large-scale pre-trained vision-language models (VLMs) containing plentiful category-level content to capture accurate correspondences between images and ...
- **p. 1 / Abstract - extractive body cue:** However, due to the lack of quadratic relation-aware knowledge in VLMs, directly using the category-level correspondence in the base dataset could not sufficiently represent generalized ...
- **p. 1 / Abstract - extractive body cue:** Therefore, designing an effective open-vocabulary relation mining framework is challenging and meaningful.
- **p. 1 / Abstract - extractive body cue:** To this end, we propose a novel Vision-Language Interactive Relation Mining model (VL-IRM) for OV-SGG, which explores learning generalized relation-aware knowledge through multimodal interaction.
- **p. 2 / 1. Introduction - extractive body cue:** Since existing pre-trained VLMs lack relation-aware knowledge [5], directly building a VLM for OV-SGG is challenging.
- **p. 2 / 1. Introduction - extractive body cue:** Unlike existing methods, this approach does not rely on a large amount of additional pre-training data or carefully set instruction prompts. • We develop a ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Since existing pre-trained VLMs lack relation-aware knowledge [5], directly building a VLM for OV-SGG is challenging. | mapped 3D environment과 mobile robot | body wording is the source claim |
| Observation / input | Moreover, recent advancements propose using an instruction prompt sequence, thus the model could more efficiently utilize the image-text pair knowledge of pre-trained ... | camera/depth stream, pose, map와 language goal | exact sensor/frame/preprocessing from PDF body |
| State / latent | Moreover, recent, advancements, instruction, prompt, sequence, thus, model, could, more | robot pose, free-space/semantic map와 local goal | notation and tensor shape require body check |
| Output / action | further, improve, performance, VLM, OV-SGG, address, existing, challenge | collision-free trajectory 또는 velocity command | exact unit/frame/decoder require body check |
| Target outcome | goal reach with collision-free execution | goal reach, safety, localization error와 replanning latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | sensor/map state and goal; body terms: Moreover, recent, advancements, instruction, prompt, sequence, thus, model, could, more | p. 2 (1. Introduction), p. 3 (3.1. OV-SGG Architecture), p. 4 (3.1. OV-SGG Architecture) |
| Decision / output variable | path/waypoint/velocity; body terms: mitigate, overfitting, VLM, base, dataset, semantical, level, construct | p. 4 (3.3. Hierarchical Relation Extension), p. 4 (3.2. Generative Relation Recognition), p. 6 (Method) |
| Objective / loss / cost | path cost, risk or goal utility; cue terms: Specifically, cross-entropy, loss, word, generated, text, language, modeling | p. 5 (3.4. Training Objectives), p. 5 (3.3. Hierarchical Relation Extension) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (3.4. Training Objectives), p. 4 (3.2. Generative Relation Recognition), p. 6 (Method) |
| Success / guarantee | goal reach with collision-free execution | p. 8 (4.4. Qualitative Results), p. 8 (4.4. Qualitative Results), p. 7 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Introduction - extractive body cue:** Unlike existing methods, this approach does not rely on a large amount of additional pre-training data or carefully set instruction prompts. • We develop a ...
- **p. 1 / 1. Introduction - extractive body cue:** (b) In this work, we consider the lack of quadratic relation-aware knowledge in VLMs, and construct an Interactive Relation Mining model for OV-SGG. tiple objects.
- **p. 1 / 1. Introduction - extractive body cue:** Though existing methods have been verified to be effective, they usually follow a closed-set assumption, i.e., the training and testing data share the same predicate ...

## What the Paper Changes

PDF body contribution framing (p. 4 (3.3. Hierarchical Relation Extension), p. 4 (3.2. Generative Relation Recognition), p. 6 (Method), p. 6 (Method), p. 2 (1. Introduction)): To mitigate the overfitting of VLM to the base dataset from the semantical level, we propose to construct a semantic-unbiased VLM.

- **p. 4 / 3.2. Generative Relation Recognition - extractive body cue:** We propose directly linking the relation predictor with a language model, and activating both the image encoder and the language model as trainable components, as ...
- **p. 6 / Method - extractive body cue:** Our method achieves comparable performance to prior models, without requiring access to various instruction prompts or additional pretraining.
- **p. 6 / Method - extractive body cue:** Since the task evaluation of OV-SGG requires the score of relation triplets based on the relation logits for ranking [5, 43], to assess the effectiveness ...
- **p. 2 / 1. Introduction - extractive body cue:** The contributions can be summarized as follows, • We consider a new perspective for OV-SGG, i.e., optimizing the structure of the VLM.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| no explicit assumption/failure cue | domain stress test only | not a paper claim |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

navigation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 2 (1. Introduction), p. 3 (3.1. OV-SGG Architecture), p. 4 (3.1. OV-SGG Architecture), p. 4 (3.2. Generative Relation Recognition). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction), interface p. 2 (1. Introduction), p. 3 (3.1. OV-SGG Architecture), p. 4 (3.1. OV-SGG Architecture), p. 4 (3.2. Generative Relation Recognition), objective p. 5 (3.4. Training Objectives), p. 5 (3.3. Hierarchical Relation Extension).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
