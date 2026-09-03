# Problem - OpenScene: 3D Scene Understanding with Open Vocabularies

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (24 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2211.15654; PDF retrieval source: https://arxiv.org/pdf/2211.15654. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (Abstract), p. 1 (Abstract)): Traditional 3D scene understanding approaches rely on labeled 3D datasets to train a model for a single task with supervision.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Traditional 3D scene understanding approaches rely on labeled 3D datasets to train a model for a single task with supervision.
- **p. 1 / Abstract - extractive body cue:** We propose OpenScene, an alternative approach where a model predicts dense features for 3D scene points that are co-embedded with text and image pixels in ...
- **p. 1 / Abstract - extractive body cue:** This zero-shot approach enables taskagnostic training and open-vocabulary queries.
- **p. 1 / Abstract - extractive body cue:** For example, to perform SOTA zero-shot 3D semantic segmentation it first infers CLIP features for every 3D point and later classifies them based on similarities ...
- **p. 1 / Abstract - extractive body cue:** More interestingly, it enables a suite of open-vocabulary scene understanding applications that have never been done before.
- **p. 2 / 1. Introduction - extractive body cue:** Overall, our contributions are summarized as follows: • We introduce open vocabulary 3D scene understanding tasks where arbitrary text queries are used for semantic segmentation, ...
- **p. 2 / 1. Introduction - extractive body cue:** We present OpenScene, a simple yet effective zero-shot approach for open-vocabulary 3D scene understanding.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Traditional 3D scene understanding approaches rely on labeled 3D datasets to train a model for a single task with supervision. | mapped 3D environment과 mobile robot | body wording is the source claim |
| Observation / input | Specifically, given an input point cloud P, we seek to learn an encoder that outputs per-point embeddings: \ b F ^\tex t ... | camera/depth stream, pose, map와 language goal | exact sensor/frame/preprocessing from PDF body |
| State / latent | Specifically, given, input, point, cloud, seek, learn, encoder, outputs, per-point | robot pose, free-space/semantic map와 local goal | notation and tensor shape require body check |
| Output / action | Therefore, distill, visual-language, knowledge, point, network, only, takes | collision-free trajectory 또는 velocity command | exact unit/frame/decoder require body check |
| Target outcome | goal reach with collision-free execution | goal reach, safety, localization error와 replanning latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | sensor/map state and goal; body terms: Specifically, given, input, point, cloud, seek, learn, encoder, outputs, per-point | p. 4 (3.2. 3D Distillation), p. 3 (3. Method), p. 4 (3.2. 3D Distillation) |
| Decision / output variable | path/waypoint/velocity; body terms: Overall, contributions, summarized, follows, introduce, open, vocabulary, scene | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (3.3. 2D-3D Feature Ensemble) |
| Objective / loss / cost | path cost, risk or goal utility; cue terms: enforce, output, network, F3D, consistent, fused, features, F2D | p. 4 (3.4. Inference), p. 4 (3.2. 3D Distillation) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (3.2. 3D Distillation) |
| Success / guarantee | goal reach with collision-free execution | p. 6 (4.1. Comparisons), p. 6 (4.2. Ablation Studies & Analysis), p. 3 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / Abstract - extractive body cue:** We propose OpenScene, an alternative approach where a model predicts dense features for 3D scene points that are co-embedded with text and image pixels in ...

## What the Paper Changes

PDF body contribution framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (3.3. 2D-3D Feature Ensemble), p. 3 (3. Method), p. 3 (3.1. Image Feature Fusion)): Overall, our contributions are summarized as follows: • We introduce open vocabulary 3D scene understanding tasks where arbitrary text queries are used for semantic segmentation, affordance estimation, room type classification, ...

- **p. 2 / 1. Introduction - extractive body cue:** We present OpenScene, a simple yet effective zero-shot approach for open-vocabulary 3D scene understanding.
- **p. 4 / 3.3. 2D-3D Feature Ensemble - extractive body cue:** Although one can already perform open-vocabulary queries with the 2D fused features F2D or 3D distilled features F3D, here we introduce a 2D-3D ensemble method ...
- **p. 3 / 3. Method - extractive body cue:** An overview of our approach is illustrated in Fig.
- **p. 3 / 3.1. Image Feature Fusion - extractive body cue:** The first step in our approach is to extract dense perpixel embeddings for each RGB image from a 2D visuallanguage segmentation model, and then back-project ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | There are several limitations of our work and still much to do to realize the full potential of ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | In future work, it will be interesting to design experiments to quantify the success of open vocabulary queries ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | Unlike [39], which requires training on 16 seen classes, our approach does not train with any 2D or ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | Our results on those classes is significantly better than [39] (7.7% vs 62.8% mIoU), even though 3DGenz [39] ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

navigation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 4 (3.2. 3D Distillation), p. 3 (3. Method), p. 4 (3.2. 3D Distillation), p. 1 (1. Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (Abstract), p. 1 (Abstract), interface p. 4 (3.2. 3D Distillation), p. 3 (3. Method), p. 4 (3.2. 3D Distillation), p. 1 (1. Introduction), objective p. 4 (3.4. Inference), p. 4 (3.2. 3D Distillation).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
