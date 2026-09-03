# LangOcc: Open Vocabulary Occupancy Estimation via Volume Rendering

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://3dvconf.github.io/2025/accepted-papers/.
> PDF retrieval source: https://openreview.net/attachment?id=KhjlXNbYea&name=pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / 3DV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: sensor fusion, LiDAR, 3D Vision
- Official paper: https://3dvconf.github.io/2025/accepted-papers/
- Full-text retrieval: https://openreview.net/attachment?id=KhjlXNbYea&name=pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, most existing 3D occupancy estimation methods rely on expensive 3D ground-truth labels [15, 25, 50].를 문제로 두고, In this paper we propose a novel self-supervised occupancy estimation method which aligns geometric estimations with open vocabulary natural language features, hence allowing representations of any semantics and therefore eliminating th ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** The 3D occupancy estimation task has become an important challenge in the area of vision-based autonomous driving recently.
- **p. 1 / Abstract - extractive body cue:** However, most existing camera-based methods rely on costly 3D voxel labels or LiDAR scans for training, limiting their practicality and scalability.
- **p. 1 / Abstract - extractive body cue:** Moreover, most methods are tied to a predefined set of classes which they can detect.
- **p. 1 / Abstract - extractive body cue:** In this work we present a novel approach for open vocabulary occupancy estimation called LangOcc, that is trained only via camera images, and can detect ...
- **p. 1 / Abstract - extractive body cue:** In particular, we distill the knowledge of the strong vision-language aligned encoder CLIP into a 3D occupancy model via differentiable volume rendering.
- **p. 1 / 1. Introduction - extractive body cue:** However, most existing 3D occupancy estimation methods rely on expensive 3D ground-truth labels [15, 25, 50].
- **p. 1 / 1. Introduction - extractive body cue:** These limitations hinder the adaptability and flexibility of autonomous systems in comprehending diverse and evolving environments.

## Core Idea

- **p. 1 / 1. Introduction - extractive body cue:** In this paper we propose a novel self-supervised occupancy estimation method which aligns geometric estimations with open vocabulary natural language features, hence allowing representations of ...
- **p. 1 / 1. Introduction - extractive body cue:** In summary, our contributions are: • Open vocabulary occupancy: A novel vision-only architecture to model arbitrary geometries and semantics by aligning the semantic feature space ...
- **p. 2 / 1. Introduction - extractive body cue:** Our model generalizes to estimate geometry and semantics in a zero-shot manner, without per-scene optimization like NeRF-approaches. • Feature subspace learning: In addition we introduce ...
- **p. 4 / 3.3. Volume Rendering Supervision - extractive body cue:** As a loss function, we propose the Cosine Similarity Guided MSE, which is a combination of the cosine similarity loss and the mean-squared error loss ...
- **p. 5 / 3.4. Feature Subspace Learning - extractive body cue:** (9) The dataset consists of just a few text prompts, enabling the training of U within seconds.
- **p. 5 / 3.4. Feature Subspace Learning - extractive body cue:** While vision-language features offer strong representational power for scene semantics, training a model with the high-dimensional embedding space of vision-language encoders like CLIP imposes a ...
- **p. 5 / 3.4. Feature Subspace Learning - extractive body cue:** Prior to training of our proposed model, we train a single linear transformation U ∈RL×L′ that maps from the original feature space L to the ...
- **p. 3 / 3.2. Model Architecture - extractive body cue:** 2D-to-3D Encoder Image features are first extracted from the input images I using a pretrained backbone architecture.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | During inference, the model just takes the 2D images as input and outputs the scene geometry and 3D vision-language features. | RGB-D, image set, point cloud, depth와 camera pose | p. 4 (3.3. Volume Rendering Supervision), p. 4 (3.3. Volume Rendering Supervision) |
| State/latent | During, inference, model, just, takes, images, input, outputs, scene, geometry, vision-language, features | geometry, map, object/relationship state | p. 4 (3.3. Volume Rendering Supervision), p. 4 (3.3. Volume Rendering Supervision), p. 3 (3.2. Model Architecture) |
| Output/action | 3.3.) ℒ𝑙𝑎𝑛𝑔 2D vision-language features Volume Render (CLIP) Image Encoder Input images Reducer Feature Subspace Learning (Sec. | point map, pose, scene graph, affordance 또는 query result | p. 4 (3.3. Volume Rendering Supervision), p. 3 (3.2. Model Architecture), p. 3 (3.2. Model Architecture) |
| Objective/outcome | We have found that the MSE loss function has a much easier-tooptimize loss landscape, while the cosine similarity gives a better notion of how close the embeddings are in the CLIP space. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 4 (3.3. Volume Rendering Supervision), p. 4 (3.3. Volume Rendering Supervision), p. 2 (3.1. Problem Definition) |

## Main Claims and Actual Contribution

- **p. 1 / 1. Introduction - extractive body cue:** In this paper we propose a novel self-supervised occupancy estimation method which aligns geometric estimations with open vocabulary natural language features, hence allowing representations of ...
- **p. 1 / 1. Introduction - extractive body cue:** In summary, our contributions are: • Open vocabulary occupancy: A novel vision-only architecture to model arbitrary geometries and semantics by aligning the semantic feature space ...
- **p. 2 / 1. Introduction - extractive body cue:** Our model generalizes to estimate geometry and semantics in a zero-shot manner, without per-scene optimization like NeRF-approaches. • Feature subspace learning: In addition we introduce ...
- **p. 4 / 3.3. Volume Rendering Supervision - extractive body cue:** As a loss function, we propose the Cosine Similarity Guided MSE, which is a combination of the cosine similarity loss and the mean-squared error loss ...
- **p. 5 / 3.4. Feature Subspace Learning - extractive body cue:** (9) The dataset consists of just a few text prompts, enabling the training of U within seconds.
- **p. 7 / 4.5. Ablations - extractive body cue:** Adding 4 future and past frames during rendering supervision already improves all scores significantly, such that LangOcc achieves a better open vocabulary retrieval performance than ...
- **p. 6 / 4.3. 3D Open Vocabulary Retrieval - extractive body cue:** We achieve a mAP score of 21.7 and 22.7 (for all points and only visible points, respectively) compared to the 17.5 and 18.4 of POP-3D, ...
- **p. 6 / 4.4. Zero-shot Semantic Occupancy Estimation - extractive body cue:** LangOcc achieves a geometric IoU score of at least 51.59, showing that our model is able to estimate the scene geometry well without any photometric ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | SYSTEM / EVALUATION SCOPE UNRESOLVED | do not infer unreported downstream behavior | p. 7 (4.5. Ablations), p. 6 (4.3. 3D Open Vocabulary Retrieval) |
| Embodiment/environment | For zero-shot occupancy estimation, we evaluate on the widely known Occ3D-nuScenes benchmark [41], which provides semantic voxel labels for the nuScenes dataset. | hardware/simulator version and reset protocol | p. 5 (4.1. Dataset and Task Description), p. 5 (4.1. Dataset and Task Description) |
| Dataset/benchmark | We evaluate our approach against other recent approaches on the Occ3D-nuScenes dataset [41] and show the results in Tab. | role, split, size and leakage | p. 5 (4.1. Dataset and Task Description), p. 5 (4.1. Dataset and Task Description), p. 6 (4.4. Zero-shot Semantic Occupancy Estimation), p. 6 (4.2. Implementation Details) |
| Metric | LangOcc achieves a geometric IoU score of at least 51.59, showing that our model is able to estimate the scene geometry well without any photometric losses or explicit depth supervision. | definition, denominator, direction and uncertainty | p. 6 (4.4. Zero-shot Semantic Occupancy Estimation), p. 7 (4.5. Ablations), p. 6 (4.1. Dataset and Task Description) |
| Baseline/ablation | As is visible, our method outperforms both baselines, even though we use just vision-based supervision. | fair input/data/compute/action matching | p. 6 (4.3. 3D Open Vocabulary Retrieval), p. 6 (4.4. Zero-shot Semantic Occupancy Estimation), p. 7 (4.5. Ablations) |

## Explicit Limitations and Failure Boundary

- **p. 7 / 4.4. Zero-shot Semantic Occupancy Estimation - extractive body cue:** As mentioned above, the reducer U finishes training within a second and thus does not impose any notable overhead.

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, most existing 3D occupancy estimation methods rely on expensive 3D ground-truth labels [15, 25, 50].를 문제로 두고, In this paper we propose a novel self-supervised occupancy estimation method which aligns geometric estimations with open vocabulary natural language features, hence allowing representations of any semantics and therefore eliminating th ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 5 (3.4. Feature Subspace Learning), p. 5 (3.4. Feature Subspace Learning), p. 3 (3.2. Model Architecture) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
