# GaussianGrasper: 3D Language Gaussian Splatting for Open-vocabulary Robotic Grasping

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2403.09637.
> PDF retrieval source: https://arxiv.org/pdf/2403.09637. Reading tracker status/evidence was not changed.

- Year/Venue: 2024 / RA-L
- Authors: not duplicated here when not verified in the registry source
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: NEXT
- Tags: Robotics, 3D Vision, Gaussian Splatting, semantic
- Official paper: https://arxiv.org/abs/2403.09637
- Full-text retrieval: https://arxiv.org/pdf/2403.09637
- Code/Project: https://github.com/MrSecant/GaussianGrasper
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-02 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Manipulation, contact, tactile, and dexterity의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Other methods [8], [9], [10], [11], [12], [13] that use 3D backbone to extract features and are supervised by 3D annotation or manipulation feedback can effectively make robots explicitly understand 3D scenes ...를 문제로 두고, In summary, the contributions of this paper are as follows: • We introduce GaussianGrasper, a robot manipulation system implemented by a 3D Gaussian field endowed with open-vocabulary semantics and accurate geometry that ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Constructing a 3D scene capable of accommodating open-ended language queries, is a pivotal pursuit, particularly within the domain of robotics.
- **p. 1 / Abstract - extractive body cue:** Such technology facilitates robots in executing object manipulations based on human language directives.
- **p. 1 / Abstract - extractive body cue:** To tackle this challenge, some research efforts have been dedicated to the development of language-embedded implicit fields.
- **p. 1 / Abstract - extractive body cue:** NeRF) encounter limitations due to the necessity of processing a large number of input views for reconstruction, coupled with their inherent inefficiencies in inference.
- **p. 1 / Abstract - extractive body cue:** Thus, we present the GaussianGrasper, which utilizes 3D Gaussian Splatting to explicitly represent the scene as a collection of Gaussian primitives.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Other methods [8], [9], [10], [11], [12], [13] that use 3D backbone to extract features and are supervised by 3D annotation or manipulation feedback can ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** In summary, the contributions of this paper are as follows: • We introduce GaussianGrasper, a robot manipulation system implemented by a 3D Gaussian field endowed ...

## Core Idea

- **p. 2 / I. INTRODUCTION - extractive body cue:** In summary, the contributions of this paper are as follows: • We introduce GaussianGrasper, a robot manipulation system implemented by a 3D Gaussian field endowed ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** We present a comparison between our method, 2D feature fusion, and LERF.
- **p. 2 / I. INTRODUCTION - extractive body cue:** More specifically, our method enables language-guided manipulation via the following steps: (1) Initialization: we scan RGB-D images of a few viewpoints to initialize the 3DGS, ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** In contrast, our method reconstructs a consistent feature field and achieves more precise 3D localization. to afford language-guided manipulation.
- **p. 3 / III. METHODOLOGY - extractive body cue:** EFD: Efficient Feature Distillation Multi-view RGB-D Initialize 3D Gaussian Field Locate Normal-guided Grasp Pick up the hamburger Query Filter Grasping Generate Grasp Pose Candidates 3D ...
- **p. 2 / III. METHODOLOGY - extractive body cue:** 2 (a) where our method (1) collects multi-view RGB-D images as input to initialize 3D Gaussian field; (2) reconstructs 3D feature field via efficient feature ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | EFD: Efficient Feature Distillation Multi-view RGB-D Initialize 3D Gaussian Field Locate Normal-guided Grasp Pick up the hamburger Query Filter Grasping Generate Grasp Pose Candidates 3D Localization (a) Our Proposed Pipeline Execute De ... | RGB-D, image set, point cloud, depth와 camera pose | p. 3 (III. METHODOLOGY), p. 2 (III. METHODOLOGY) |
| State/latent | EFD, Efficient, Feature, Distillation, Multi-view, RGB-D, Initialize, Gaussian, Field, Locate, Normal-guided, Grasp | geometry, map, object/relationship state | p. 3 (III. METHODOLOGY), p. 2 (III. METHODOLOGY), p. 2 (III. METHODOLOGY) |
| Output/action | 2 (a) where our method (1) collects multi-view RGB-D images as input to initialize 3D Gaussian field; (2) reconstructs 3D feature field via efficient feature distillation module and (3) achieves languagedguided manipulation. | point map, pose, scene graph, affordance 또는 query result | p. 2 (III. METHODOLOGY), p. 2 (III. METHODOLOGY), p. 1 (I. INTRODUCTION) |
| Objective/outcome | EFD: Efficient Feature Distillation Multi-view RGB-D Initialize 3D Gaussian Field Locate Normal-guided Grasp Pick up the hamburger Query Filter Grasping Generate Grasp Pose Candidates 3D Localization (a) Our Proposed Pipeline Execute De ... | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 3 (III. METHODOLOGY) |

## Main Claims and Actual Contribution

- **p. 2 / I. INTRODUCTION - extractive body cue:** In summary, the contributions of this paper are as follows: • We introduce GaussianGrasper, a robot manipulation system implemented by a 3D Gaussian field endowed ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** We present a comparison between our method, 2D feature fusion, and LERF.
- **p. 2 / I. INTRODUCTION - extractive body cue:** More specifically, our method enables language-guided manipulation via the following steps: (1) Initialization: we scan RGB-D images of a few viewpoints to initialize the 3DGS, ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** In contrast, our method reconstructs a consistent feature field and achieves more precise 3D localization. to afford language-guided manipulation.
- **p. 6 / IV. EXPERIMENT - extractive body cue:** The results of segmentation and localization are shown in Table I where our method significantly outperforms other approaches.
- **p. 7 / IV. EXPERIMENT - extractive body cue:** Leveraging the normal filter significantly increases the success rate by 7.7%, further demonstrating the effectiveness of our proposed normal-guided grasp.
- **p. 7 / IV. EXPERIMENT - extractive body cue:** Besides, we report the quantitative results of the grasping success rate with and without the normal filter, as shown in Table II.
- **p. 6 / IV. EXPERIMENT - extractive body cue:** It can be seen that our method achieves an approximate 180 × speedup over LERF.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 6 (IV. EXPERIMENT), p. 7 (IV. EXPERIMENT) |
| Embodiment/environment | 2) Data Collection and Processing: We first use the robot arm equipped with a Realsense D455 to scan the desktop scene from 16 viewpoints. | hardware/simulator version and reset protocol | p. 5 (IV. EXPERIMENT), p. 5 (IV. EXPERIMENT) |
| Dataset/benchmark | Therefore, our method can help robots reduce the ambiguity of object perception. | role, split, size and leakage | p. 5 (IV. EXPERIMENT), p. 5 (IV. EXPERIMENT), p. 6 (IV. EXPERIMENT), p. 6 (IV. EXPERIMENT) |
| Metric | Method Grasping Success Rate (%) LSeg + Depth[45] 26.7 LERF + AnyGrasp[16] 55.8 Ours w/o. | definition, denominator, direction and uncertainty | p. 7 (IV. EXPERIMENT), p. 7 (IV. EXPERIMENT), p. 6 (IV. EXPERIMENT) |
| Baseline/ablation | Our baselines are Lseg [45] and LERF [16] (All mention of LERF in our experiments includes an extra depth supervision to ensure a fair comparison with our method.) In qualitative results, we ... | fair input/data/compute/action matching | p. 6 (IV. EXPERIMENT), p. 6 (IV. EXPERIMENT), p. 7 (IV. EXPERIMENT) |

## Explicit Limitations and Failure Boundary

- **p. 7 / V. LIMITATION - extractive body cue:** One limitation is that our reconstructed scene remains static.

## Why Read It

Manipulation, contact, tactile, and dexterity의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Other methods [8], [9], [10], [11], [12], [13] that use 3D backbone to extract features and are supervised by 3D annotation or manipulation feedback can effectively make robots explicitly understand 3D scenes ...를 문제로 두고, In summary, the contributions of this paper are as follows: • We introduce GaussianGrasper, a robot manipulation system implemented by a 3D Gaussian field endowed with open-vocabulary semantics and accurate geometry that ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (III. METHODOLOGY), p. 2 (III. METHODOLOGY) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
