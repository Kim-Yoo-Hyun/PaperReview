# GaussianVLM: Scene-Centric 3D Vision-Language Models Using Language-Aligned Gaussian Splats for Embodied Reasoning and Beyond

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_4.html.
> PDF retrieval source: https://arxiv.org/pdf/2507.00886. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICRA
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Vision-Language Model, 3D Vision, Gaussian Splatting
- Official paper: https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_4.html
- Full-text retrieval: https://arxiv.org/pdf/2507.00886
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 We argue that using the existing solutions, meaningfully understanding such representations via LLMs is a very challenging task - due to the high density of high-dimensional language features.를 문제로 두고, Overall, this work makes the following contributions: • We introduce a fully scene-centric 3D VLM that achieves SOTA results, without requiring any dependencies on object detectors, on benchmark datasets for reasoning tasks ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** As multimodal language models advance, their application to 3D scene understanding is a fast-growing frontier, driving the development of 3D Vision-Language Models (VLMs).
- **p. 1 / Abstract - extractive body cue:** Current methods show strong dependence on object detectors, introducing processing bottlenecks and limitations in taxonomic flexibility.
- **p. 1 / Abstract - extractive body cue:** To address these limitations, we propose a scenecentric 3D VLM for 3D Gaussian splat scenes that employs language- and task-aware scene representations.
- **p. 1 / Abstract - extractive body cue:** Our approach directly embeds rich linguistic features into the 3D scene representation by associating language with each Gaussian primitive, achieving early modality alignment.
- **p. 1 / Abstract - extractive body cue:** To process the resulting dense representations, we introduce a dual sparsifier that distills them into compact, task-relevant tokens via taskguided and location-guided pathways, producing sparse, ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** We argue that using the existing solutions, meaningfully understanding such representations via LLMs is a very challenging task - due to the high density of ...

## Core Idea

- **p. 2 / I. INTRODUCTION - extractive body cue:** Overall, this work makes the following contributions: • We introduce a fully scene-centric 3D VLM that achieves SOTA results, without requiring any dependencies on object ...
- **p. 4 / III. METHOD - extractive body cue:** The resulting sparse scene representation (ROI tokens + task-selected tokens), along with the task tokens, is input to an LLM for response generation. demands of ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this work, we propose to shift from object-centric to scene-centric representations by embedding language features directly into the spatial structure of the environment.
- **p. 2 / I. INTRODUCTION - extractive body cue:** To address this, we introduce a dual sparsifier module that efficiently utlizes dense language representations while preserving semantic fidelity.
- **p. 3 / III. METHOD - extractive body cue:** We introduce GaussianVLM, a 3D VLM for indoor scene understanding.
- **p. 3 / III. METHOD - extractive body cue:** The sparsifier takes as input the dense language features and outputs sparse task-aware tokens.
- **p. 4 / III. METHOD - extractive body cue:** To mitigate the computational overhead of cross-attention on a large number of tokens, we first apply a simple uniform downsampling strategy to reduce the representation ...
- **p. 3 / III. METHOD - extractive body cue:** To sparsify the resulting dense language features with a task-awareness, we introduce a dual sparsifier module.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The sparsifier takes as input the dense language features and outputs sparse task-aware tokens. | RGB-D, image set, point cloud, depth와 camera pose | p. 3 (III. METHOD), p. 3 (III. METHOD) |
| State/latent | sparsifier, takes, input, dense, language, features, outputs, sparse, task-aware, tokens, GaussianVLM, relies | geometry, map, object/relationship state | p. 3 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD) |
| Output/action | GaussianVLM relies on three key innovations: (1) a language-aware Gaussian splatting backbone [27] that predicts language features for each Gaussian, enabling direct language-based alignment between the scene and the prompt; (2) a ... | point map, pose, scene graph, affordance 또는 query result | p. 3 (III. METHOD), p. 4 (III. METHOD), p. 4 (III. METHOD) |
| Objective/outcome | Both stages share a unified training objective. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 3 (III. METHOD), p. 3 (III. METHOD) |

## Main Claims and Actual Contribution

- **p. 2 / I. INTRODUCTION - extractive body cue:** Overall, this work makes the following contributions: • We introduce a fully scene-centric 3D VLM that achieves SOTA results, without requiring any dependencies on object ...
- **p. 4 / III. METHOD - extractive body cue:** The resulting sparse scene representation (ROI tokens + task-selected tokens), along with the task tokens, is input to an LLM for response generation. demands of ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this work, we propose to shift from object-centric to scene-centric representations by embedding language features directly into the spatial structure of the environment.
- **p. 2 / I. INTRODUCTION - extractive body cue:** To address this, we introduce a dual sparsifier module that efficiently utlizes dense language representations while preserving semantic fidelity.
- **p. 3 / III. METHOD - extractive body cue:** We introduce GaussianVLM, a 3D VLM for indoor scene understanding.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** On the scene-centric SQA3D benchmark, GaussianVLM achieves an exact match accuracy of 49.4%, surpassing LEO's 47.0% by 2.4 percentage points.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Results and Analysis The evaluation results, shown in Tab.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Embodiment/environment | Scene-Centric Tasks, in contrast, require holistic reasoning about the environment, its layout, and the agent's situated context-without reducing the scene to individual object tokens. | hardware/simulator version and reset protocol | p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Dataset/benchmark | Dataset We evaluate our model under the LL3DA, a SOTA 3D VLM, training protocol [9]. | role, split, size and leakage | p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS) |
| Metric | ROUGE captures structural similarity and emphasizes recall without over-rewarding redundant context. | definition, denominator, direction and uncertainty | p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Baseline/ablation | Implementation Details Following prior work, we represent each 3D scene using 40k randomly sampled Gaussians from the GaussianWorld [27] Gaussian splats scene. | fair input/data/compute/action matching | p. 5 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 7 / V. CONCLUSION - extractive body cue:** By directly embedding language features into the spatial structure of 3D scenes, GaussianVLM, overcomes the inherent limitations of object detector dependencies, enabling a more natural ...
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** These tasks fall into two broad categories: object-centric and scene-centric, reflecting differing demands on spatial grounding and semantic abstraction.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** SentenceBERT directly evaluates semantic similarity in embedding space for robustness to paraphrasing.

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 We argue that using the existing solutions, meaningfully understanding such representations via LLMs is a very challenging task - due to the high density of high-dimensional language features.를 문제로 두고, Overall, this work makes the following contributions: • We introduce a fully scene-centric 3D VLM that achieves SOTA results, without requiring any dependencies on object detectors, on benchmark datasets for reasoning tasks ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (I. INTRODUCTION), p. 3 (III. METHOD), p. 4 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD), p. 5 (IV. EXPERIMENTS) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
