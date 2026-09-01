# Sparsh: Self-supervised touch representations for vision-based tactile sensing

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (31 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2410.24090.
> PDF retrieval source: https://arxiv.org/pdf/2410.24090. Reading tracker status/evidence was not changed.

- Year/Venue: 2024 / CoRL
- Authors: not duplicated here when not verified in the registry source
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: NEXT
- Tags: Robotics, tactile sensing, self-supervised learning, foundation model, contact
- Official paper: https://arxiv.org/abs/2410.24090
- Full-text retrieval: https://arxiv.org/pdf/2410.24090
- Code/Project: https://sparsh-ssl.github.io/
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-02 (31 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Manipulation, contact, tactile, and dexterity의 tactile 문제를 이해하기 위해 읽는다. 본문은 Curation of new & existing datasets, unlabeled for SSL and labeled for benchmarking.를 문제로 두고, In this work, we introduce a family of touch representations for vision-based tactile sensors trained with SSL.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** In this work, we introduce general purpose touch representations for the increasingly accessible class of vision-based tactile sensors.
- **p. 1 / Abstract - extractive body cue:** Such sensors have led to many recent advances in robot manipulation as they markedly complement vision, yet solutions today often rely on task and sensor ...
- **p. 1 / Abstract - extractive body cue:** Collecting real data at scale with task centric ground truth labels, like contact forces and slip, is a challenge further compounded by sensors of various ...
- **p. 1 / Abstract - extractive body cue:** To tackle this we turn to self-supervised learning (SSL) that has demonstrated remarkable performance in computer vision.
- **p. 1 / Abstract - extractive body cue:** We present Sparsh, a family of SSL models that can support various vision-based tactile sensors, alleviating the need for custom labels through pre-training on 460k+ ...
- **p. 2 / 1 Introduction - extractive body cue:** Curation of new & existing datasets, unlabeled for SSL and labeled for benchmarking.
- **p. 2 / 1 Introduction - extractive body cue:** Pulling together additional unlabeled data points from the existing datasets we train our models on a total of 460k+ tactile images.

## Core Idea

- **p. 2 / 1 Introduction - extractive body cue:** In this work, we introduce a family of touch representations for vision-based tactile sensors trained with SSL.
- **p. 2 / 1 Introduction - extractive body cue:** Our contributions are as follows: 1.
- **p. 1 / Abstract - extractive body cue:** We present Sparsh, a family of SSL models that can support various vision-based tactile sensors, alleviating the need for custom labels through pre-training on 460k+ ...
- **p. 8 / 8 Discussion - extractive body cue:** We evaluated five SSL approaches (see Figure 2) comparing their performance against task and sensor specific models through TacBench, a benchmark of six touch-centric tasks ...
- **p. 2 / 1 Introduction - extractive body cue:** For example, feature extractors trained on GelSight with markers may not transfer to other sensors, and encoders optimized for texture recognition [15] may not be ...
- **p. 8 / 8 Discussion - extractive body cue:** Open-source tactile datasets we considered in this study predominantly feature discrete contact interactions.
- **p. 8 / 8 Discussion - extractive body cue:** Notably, models pre-trained in latent space perform better in downstream tasks when fully fine-tuned, especially in regression tasks like force and pose estimation.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Vision-based tactile sensors [1, 2, 3, 4] have emerged as the leading form factor capable of capturing images of physical interactions at the sensor-objectenvironment interface, often inaccessible through vision. | tactile image/force, vision과 proprioceptive history | p. 2 (1 Introduction), p. 8 (8 Discussion) |
| State/latent | Vision-based, tactile, sensors, have, emerged, leading, form, factor, capable, capturing, images, physical | contact geometry, force state 또는 latent dynamics | p. 2 (1 Introduction), p. 8 (8 Discussion), p. 2 (1 Introduction) |
| Output/action | In particular, we find Sparsh (DINO) is well suited for physics-based tasks like force and pose estimation, while Sparsh (IJEPA) performs better at touch semantic understanding like slip state, stability of a ... | grasp/contact action, force command 또는 object motion | p. 8 (8 Discussion), p. 2 (1 Introduction), p. 8 (8 Discussion) |
| Objective/outcome | Specifically, we provide a recipe to adapt masking-based objectives from computer vision to the tactile domain, and train general-purpose touch encoders by curating a new Touch-Slide dataset and existing datasets of tactile ... | slip/contact success, force/pose error와 robustness | p. 2 (1 Introduction), p. 2 (1 Introduction), p. 8 (8 Discussion) |

## Main Claims and Actual Contribution

- **p. 2 / 1 Introduction - extractive body cue:** In this work, we introduce a family of touch representations for vision-based tactile sensors trained with SSL.
- **p. 2 / 1 Introduction - extractive body cue:** Our contributions are as follows: 1.
- **p. 1 / Abstract - extractive body cue:** We present Sparsh, a family of SSL models that can support various vision-based tactile sensors, alleviating the need for custom labels through pre-training on 460k+ ...
- **p. 8 / 8 Discussion - extractive body cue:** We evaluated five SSL approaches (see Figure 2) comparing their performance against task and sensor specific models through TacBench, a benchmark of six touch-centric tasks ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4: Summary of results comparing Sparsh and E2E on [T1]-[T6] tasks in TacBench across varying amounts of labeled data. Pre-training with SSL yields general ...
- **p. 8 / 8 Discussion - extractive body cue:** On average, Sparsh achieves a 95.1% improvement compared to an end-to-end approach when all models have access to only 33% -50% of the labeled dataset ...
- **p. 8 / 8 Discussion - extractive body cue:** In contrast, partial fine-tuning offers minor improvements, aligning closely with the performance of frozen models.
- **p. 26 / Figure/Table caption - extractive body cue:** Figure 14: Confusion matrix on test data for ∆Tx, ∆Ty, ∆Yaw for E2E, Sparsh (DINO) and Sparsh (IJEPA) trained on 33% of the available labeled ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | SYSTEM / EVALUATION SCOPE UNRESOLVED | do not infer unreported downstream behavior | p. 7 (Figure/Table caption), p. 8 (8 Discussion) |
| Embodiment/environment | Finally, we construct TacBench, a benchmark consisting of six touch-centric tasks that cover the space of relevant problems on tactile properties such as force estimation and slip detection, on perception such as ... | hardware/simulator version and reset protocol | p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Dataset/benchmark | Such sensors have led to many recent advances in robot manipulation as they markedly complement vision, yet solutions today often rely on task and sensor specific handcrafted perception models. | role, split, size and leakage | p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (Abstract), p. 1 (Front matter) |
| Metric | Table 11: Mean and variance of distance traversed (in cm) before failure for policies based on Sparsh and E2E. Results over 10 randomized novel starting locations on the bead maze. In Table ... | definition, denominator, direction and uncertainty | p. 28 (Figure/Table caption), p. 24 (Figure/Table caption), p. 24 (Figure/Table caption) |
| Baseline/ablation | Figure 2: (a) We curate new and existing datasets of vision-based tactile sensors to train touch representations by adapting state-of-the-art SSL vision methods to the tactile domain, namely (b) Masked Autoencoder (MAE) ... | fair input/data/compute/action matching | p. 3 (Figure/Table caption), p. 1 (Front matter), p. 1 (Abstract) |

## Explicit Limitations and Failure Boundary

- **p. 25 / Figure/Table caption - extractive body cue:** Figure 13: Failure case where the ground truth does not reflect slip since it relies on an experimental coefficient of friction. Despite the inaccuracies in ...
- **p. 24 / Figure/Table caption - extractive body cue:** Figure 12: Contrast between Sparsh (VJEPA) and E2E for a test trajectory with a spherical probe sliding on the DIGIT sensor. Sparsh (VJEPA), even though ...
- **p. 28 / Figure/Table caption - extractive body cue:** Table 11: Mean and variance of distance traversed (in cm) before failure for policies based on Sparsh and E2E. Results over 10 randomized novel starting ...
- **p. 8 / 8 Discussion - extractive body cue:** Both models perform similarly in bead maze test demonstrations, which require implicit knowledge of shear forces and slip.
- **p. 8 / 8 Discussion - extractive body cue:** Using as little as 10% or 1% of the labeled data for force estimation and slip detection still yields acceptable results (e.g. force error below ...
- **p. 25 / Figure/Table caption - extractive body cue:** Table 8: Accuracy and 95% confidence interval for pose estimation task following the regression-by- classification paradigm. Relative pose between object and ring finger. Metrics computed ...
- **p. 28 / Figure/Table caption - extractive body cue:** Table 10: Accuracy for textile classification over 20 classes using GelSight with markers dataset under different budget of labeled data. Results over 26k tactile images, ...

## Why Read It

Manipulation, contact, tactile, and dexterity의 tactile 문제를 이해하기 위해 읽는다. 본문은 Curation of new & existing datasets, unlabeled for SSL and labeled for benchmarking.를 문제로 두고, In this work, we introduce a family of touch representations for vision-based tactile sensors trained with SSL.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (Abstract), p. 1 (Abstract), p. 2 (1 Introduction), p. 8 (8 Discussion) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
