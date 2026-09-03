# Fin3R: Fine-tuning Feed-forward 3D Reconstruction Models via Monocular Knowledge Distillation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (22 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=pZIeK0Xvph.
> PDF retrieval source: https://arxiv.org/pdf/2511.22429. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / NeurIPS
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: 3D reconstruction, depth, 3D Vision
- Official paper: https://openreview.net/forum?id=pZIeK0Xvph
- Full-text retrieval: https://arxiv.org/pdf/2511.22429
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (22 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 This persistent gap in performance raises a crucial question: why do these feed-forward models consistently struggle to capture high-fidelity geometry?를 문제로 두고, To directly address this challenge, we propose a refined integration of LoRA with a re-normalization strategy specifically designed to constrain feature norm drift.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 2 / Abstract - extractive body cue:** We present Fin3R, a simple, effective, and general fine-tuning method for feedforward 3D reconstruction models.
- **p. 2 / Abstract - extractive body cue:** The family of feed-forward reconstruction model regresses pointmap of all input images to a reference frame coordinate system, along with other auxiliary outputs, in a ...
- **p. 2 / Abstract - extractive body cue:** However, we find that current models struggle with fine geometry and robustness due to (i) the scarcity of high-fidelity depth and pose supervision and (ii) ...
- **p. 2 / Abstract - extractive body cue:** Fin3R jointly tackles two issues with an extra lightweight fine-tuning step.
- **p. 2 / Abstract - extractive body cue:** We freeze the decoder, which handles view matching, and fine-tune only the image encoder-the component dedicated to feature extraction.
- **p. 2 / 1 Introduction - extractive body cue:** This persistent gap in performance raises a crucial question: why do these feed-forward models consistently struggle to capture high-fidelity geometry?
- **p. 2 / 1 Introduction - extractive body cue:** Fine structures are frequently over-smoothed, object boundaries become blurred, and transparent or glossy surfaces are reconstructed with significant inaccuracies, yielding point clouds that lack crisp ...

## Core Idea

- **p. 5 / 3 Method - extractive body cue:** To directly address this challenge, we propose a refined integration of LoRA with a re-normalization strategy specifically designed to constrain feature norm drift.
- **p. 3 / 1 Introduction - extractive body cue:** To summarize, we propose a simple, effective, and general fine-tuning approach.
- **p. 5 / 3 Method - extractive body cue:** Teacher 𝐿!"#$"%% 𝐿&'"($)*& Unlabeled SingleView ~90% Figure 4: Pipeline of our method.
- **p. 6 / 3 Method - extractive body cue:** enforces robust multi-view matching while mitigating potential feature shift; to ensure this loss is applied only to multi-view samples, we introduce an indicator function 1mv(i) ...
- **p. 3 / 1 Introduction - extractive body cue:** Our contributions are threefold: (i) a general encoder-only distillation strategy that enhances local geometric detail and overall robustness in feed-forward 3D reconstruction models; (ii) a ...
- **p. 5 / 3 Method - extractive body cue:** Recall that feed-forward 3D reconstruction models typically consist of a shared encoder, which extracts features from input images, followed by a decoder that correlates these ...
- **p. 6 / 3 Method - extractive body cue:** The overall training objective is the average loss over all N images, given by L = 1 N PN i=1  L(i) distill + L(i) ...
- **p. 4 / 3 Method - extractive body cue:** Although CUT3R [65] leverages extensive depth supervision and VGGT [61] employs gradient-based loss to refine local geometry-with both methods incorporating dedicated self-view pointmap or depth ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | (a) Input Image (b) VGGT Avg: 9.61 (c) LoRA Only Avg: 10.53 (d) LoRA+Replay Avg: 10.34 (e) Full Avg: 9.73 Figure 3: Heatmaps show spatial variations in L2 norms of encoder patch ... | RGB-D, image set, point cloud, depth와 camera pose | p. 5 (3 Method), p. 4 (3 Method) |
| State/latent | Input, Image, VGGT, Avg, LoRA, Only, Replay, Full, Figure, Heatmaps, spatial, variations | geometry, map, object/relationship state | p. 5 (3 Method), p. 4 (3 Method), p. 5 (3 Method) |
| Output/action | Although CUT3R [65] leverages extensive depth supervision and VGGT [61] employs gradient-based loss to refine local geometry-with both methods incorporating dedicated self-view pointmap or depth estimation heads-the resulting outputs re ... | point map, pose, scene graph, affordance 또는 query result | p. 4 (3 Method), p. 5 (3 Method), p. 2 (1 Introduction) |
| Objective/outcome | Although CUT3R [65] leverages extensive depth supervision and VGGT [61] employs gradient-based loss to refine local geometry-with both methods incorporating dedicated self-view pointmap or depth estimation heads-the resulting outputs re ... | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 4 (3 Method), p. 6 (3 Method), p. 5 (3 Method) |

## Main Claims and Actual Contribution

- **p. 5 / 3 Method - extractive body cue:** To directly address this challenge, we propose a refined integration of LoRA with a re-normalization strategy specifically designed to constrain feature norm drift.
- **p. 3 / 1 Introduction - extractive body cue:** To summarize, we propose a simple, effective, and general fine-tuning approach.
- **p. 5 / 3 Method - extractive body cue:** Teacher 𝐿!"#$"%% 𝐿&'"($)*& Unlabeled SingleView ~90% Figure 4: Pipeline of our method.
- **p. 6 / 3 Method - extractive body cue:** enforces robust multi-view matching while mitigating potential feature shift; to ensure this loss is applied only to multi-view samples, we introduce an indicator function 1mv(i) ...
- **p. 3 / 1 Introduction - extractive body cue:** Our contributions are threefold: (i) a general encoder-only distillation strategy that enhances local geometric detail and overall robustness in feed-forward 3D reconstruction models; (ii) a ...
- **p. 8 / 4 Experiment - extractive body cue:** The results indicate that models enhanced with our distillation method consistently achieve lower Acc and Comp as well as improved NC scores across most baselines.
- **p. 9 / 4 Experiment - extractive body cue:** Together, these results highlight that monocular finetuning with high-quality pseudo-labels from the diverse dataset improves both single-view and multi-view accuracy.
- **p. 10 / 4.7 Discussion - extractive body cue:** This underscores the necessity of including in-the-wild data alongside highquality datasets during training to achieve optimal results.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 8 (4 Experiment), p. 9 (4 Experiment) |
| Embodiment/environment | Method ETH3D [49] T&T [27] KITTI [58] Sintel [6] Bonn [40] rel ↓ δ1 ↑ rel ↓ δ1 ↑ rel ↓ δ1 ↑ rel ↓ δ1 ↑ rel ↓ δ1 ↑ CUT3R ... | hardware/simulator version and reset protocol | p. 8 (4 Experiment), p. 7 (4 Experiment) |
| Dataset/benchmark | The fine-tuned versions of CUT3R and VGGT consistently outperform their respective baselines across datasets spanning diverse domains. | role, split, size and leakage | p. 8 (4 Experiment), p. 7 (4 Experiment), p. 7 (4 Experiment), p. 9 (4 Experiment) |
| Metric | The table shows that our integrated models consistently achieve lower relative depth error and higher δ1 scores. | definition, denominator, direction and uncertainty | p. 6 (4 Experiment), p. 4 (Figure/Table caption), p. 9 (4 Experiment) |
| Baseline/ablation | Interestingly, we observe that although DUSt3R's depth estimates rank last among the evaluated models, they exhibit the sharpest boundaries compared with the other two baseline models. | fair input/data/compute/action matching | p. 6 (4 Experiment), p. 7 (4 Experiment), p. 6 (4 Experiment) |

## Explicit Limitations and Failure Boundary

- **p. 7 / 4 Experiment - extractive body cue:** Note that VGGT is not trained on dynamic datasets, so its performance bottleneck may stem from dataset limitations rather than our fine-tuning method.
- **p. 10 / 4.7 Discussion - extractive body cue:** This demonstrates that a robustly trained encoder benefits downstream heads even without direct supervision.
- **p. 10 / 4.7 Discussion - extractive body cue:** We attribute this improvement primarily to the incorporation of unlabeled datasets, which enhance the model's robustness and overall performance.
- **p. 6 / 4 Experiment - extractive body cue:** This is likely because CUT3R and VGGT are trained on long sequences and are consequently more affected by the long-sequence degradation 6

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 This persistent gap in performance raises a crucial question: why do these feed-forward models consistently struggle to capture high-fidelity geometry?를 문제로 두고, To directly address this challenge, we propose a refined integration of LoRA with a re-normalization strategy specifically designed to constrain feature norm drift.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 6 (3 Method), p. 5 (3 Method), p. 6 (3 Method) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
