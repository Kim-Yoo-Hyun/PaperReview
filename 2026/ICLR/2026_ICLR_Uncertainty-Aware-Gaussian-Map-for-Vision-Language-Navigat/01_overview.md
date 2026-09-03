# Uncertainty-Aware Gaussian Map for Vision-Language Navigation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (24 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=LPv59noPAy.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/246583. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICLR
- Authors: not duplicated here when not verified in the registry source
- Primary track: World models, safety, uncertainty, and recovery
- Tier: REFERENCE
- Tags: Vision-Language Model, 3D Vision, Navigation, Gaussian Splatting
- Official paper: https://openreview.net/forum?id=LPv59noPAy
- Full-text retrieval: https://chatpaper.com/api/v1/articles/download/246583
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (24 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

World models, safety, uncertainty, and recovery의 navigation 문제를 이해하기 위해 읽는다. 본문은 Despite these advances, existing agents typically ignore uncertainty in perception when making decisions.를 문제로 두고, To approximate it, like [66], we introduce variational distributions qϕ(χ) = {qϕµ i (χµ i ), qϕe i (χe i)}i and optimize them by minimizing the Kullback-Leibler (KL) divergence to true posterior ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** Vision-Language Navigation (VLN) requires an agent to navigate 3D environments following natural language instructions.
- **p. 1 / ABSTRACT - extractive body cue:** During navigation, existing agents commonly encounter perceptual uncertainty, such as insufficient evidence for reliable grounding or ambiguity in interpreting spatial cues, yet they typically ignore ...
- **p. 1 / ABSTRACT - extractive body cue:** In this work, we explicitly model three forms of perceptual uncertainty (i.e., geometric, semantic, and appearance uncertainty) and integrate them into the agent's observation space ...
- **p. 1 / ABSTRACT - extractive body cue:** Concretely, our agent first constructs a Semantic Gaussian Map (SGM), composed of differentiable 3D Gaussian primitives initialized from panoramic observations, that encodes both the geometric ...
- **p. 1 / ABSTRACT - extractive body cue:** On top of SGM, geometric uncertainty is estimated through variational perturbations of Gaussian position and scale to assess structural reliability; semantic uncertainty is captured by ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Despite these advances, existing agents typically ignore uncertainty in perception when making decisions.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Their training recipes discourage expressing uncertainty or recognizing unreliable situations, instead incentivizing them to predict actions regardless of confidence [17].

## Core Idea

- **p. 4 / 3 METHOD - extractive body cue:** To approximate it, like [66], we introduce variational distributions qϕ(χ) = {qϕµ i (χµ i ), qϕe i (χe i)}i and optimize them by minimizing ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Extensive ablation studies confirm the contribution of each component (§4.4).
- **p. 6 / 3 METHOD - extractive body cue:** This fusion enables the agent to jointly reason about geometric structure and perceptual confidence, thereby promoting reliable and uncertainty-aware decision-making.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** In the same manner, semantic uncertainty is estimated by perturbing the semantic attributes of Gaussians, which reveals ambiguous interpretations and allows the agent to down-weight ...
- **p. 6 / 3 METHOD - extractive body cue:** Following the conventional procedure [11, 17, 30], our agent is optimized with a two-stage training scheme: pretraining with auxiliary objectives such as masked language modeling ...
- **p. 6 / 3 METHOD - extractive body cue:** To supervise SGM construction, we apply a pixel-wise rendering loss between the rendered outputs and ground-truth observations.
- **p. 3 / 3 METHOD - extractive body cue:** Based on these observations, the agent learns a navigation policy π(at/X, It, Dt) that predicts actions at ∈At, which includes navigable neighbor nodes, previously observed ...
- **p. 4 / 3 METHOD - extractive body cue:** Given multi-view RGB-D observations Ot = {It, Dt} at step t, the agent first generates a sparse pseudo-lidar point cloud via camera-to-world transformation.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Based on these observations, the agent learns a navigation policy π(at/X, It, Dt) that predicts actions at ∈At, which includes navigable neighbor nodes, previously observed nodes accessible via backtracking, and a [STOP] ... | camera/depth stream, pose, map와 language goal | p. 3 (3 METHOD), p. 6 (3 METHOD) |
| State/latent | observations, agent, learns, navigation, policy, at/X, predicts, actions, includes, navigable, neighbor, nodes | robot pose, free-space/semantic map와 local goal | p. 3 (3 METHOD), p. 6 (3 METHOD), p. 7 (3 METHOD) |
| Output/action | Following the conventional procedure [11, 17, 30], our agent is optimized with a two-stage training scheme: pretraining with auxiliary objectives such as masked language modeling and single-step action prediction to strengthen multimoda ... | collision-free trajectory 또는 velocity command | p. 6 (3 METHOD), p. 7 (3 METHOD), p. 1 (1 INTRODUCTION) |
| Objective/outcome | Following the conventional procedure [11, 17, 30], our agent is optimized with a two-stage training scheme: pretraining with auxiliary objectives such as masked language modeling and single-step action prediction to strengthen multimoda ... | goal reach, safety, localization error와 replanning latency | p. 6 (3 METHOD), p. 7 (3 METHOD), p. 4 (3 METHOD) |

## Main Claims and Actual Contribution

- **p. 4 / 3 METHOD - extractive body cue:** To approximate it, like [66], we introduce variational distributions qϕ(χ) = {qϕµ i (χµ i ), qϕe i (χe i)}i and optimize them by minimizing ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Extensive ablation studies confirm the contribution of each component (§4.4).
- **p. 6 / 3 METHOD - extractive body cue:** This fusion enables the agent to jointly reason about geometric structure and perceptual confidence, thereby promoting reliable and uncertainty-aware decision-making.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** In the same manner, semantic uncertainty is estimated by perturbing the semantic attributes of Gaussians, which reveals ambiguous interpretations and allows the agent to down-weight ...
- **p. 8 / 4 EXPERIMENT - extractive body cue:** On the val unseen split, it achieves an SR of 78% compared to 76% from VER [17] and improves SPL from 65% to 66%, corresponding ...
- **p. 9 / 4 EXPERIMENT - extractive body cue:** Row #4 reports the scores of our full framework. i) Row #1 vs #2: SGM leads to notable performance improvements against the baseline (e.g., 32.15% ...
- **p. 7 / 4 EXPERIMENT - extractive body cue:** On the val unseen split, our agent outperforms the best reported results (i.e., BEVBert [15]) by a significant margin in terms of RGS (37.65% vs ...
- **p. 7 / 4 EXPERIMENT - extractive body cue:** For R2R [1], we report Success Rate (SR), Trajectory Length (TL), Navigation Error (NE), Oracle Success Rate (OSR), and Success weighted by Path Length (SPL).

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SIMULATION | do not infer unreported downstream behavior | p. 8 (4 EXPERIMENT), p. 9 (4 EXPERIMENT) |
| Embodiment/environment | All datasets are built upon the Matterport3D simulator [80], and are split into train, val-seen, val-unseen, and test sets according to scenes. | hardware/simulator version and reset protocol | p. 7 (4 EXPERIMENT), p. 7 (4 EXPERIMENT) |
| Dataset/benchmark | We compare our agent with VER [17] on the R2R val unseen split. | role, split, size and leakage | p. 7 (4 EXPERIMENT), p. 7 (4 EXPERIMENT), p. 8 (4 EXPERIMENT), p. 8 (4 EXPERIMENT) |
| Metric | For R2R [1], we report Success Rate (SR), Trajectory Length (TL), Navigation Error (NE), Oracle Success Rate (OSR), and Success weighted by Path Length (SPL). | definition, denominator, direction and uncertainty | p. 7 (4 EXPERIMENT), p. 8 (4 EXPERIMENT), p. 9 (4 EXPERIMENT) |
| Baseline/ablation | For R2R [1], we report Success Rate (SR), Trajectory Length (TL), Navigation Error (NE), Oracle Success Rate (OSR), and Success weighted by Path Length (SPL). | fair input/data/compute/action matching | p. 7 (4 EXPERIMENT), p. 7 (4 EXPERIMENT), p. 8 (4 EXPERIMENT) |

## Explicit Limitations and Failure Boundary

- **p. 22 / Figure/Table caption - extractive body cue:** Figure 7: Failure Cases. (a) Our agent stops once "the sofa" comes into view, as the current observation already provides sufficient evidence of the target, ...
- **p. 9 / 4 EXPERIMENT - extractive body cue:** 5 illustrates our diverse perceptual forms. i) SGM preserves detailed geometric structures while maintaining high-fidelity rendering of the scene. ii) Geometric uncertainty reveals structural reliability, ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: Motivation. Previous VLN agents typically ignore perceptual uncertainty when making decisions. As a result, they often confuse visually similar structures (e.g., multiple doors) ...
- **p. 21 / Figure/Table caption - extractive body cue:** Table 12: Robustness to observation noise on R2R val unseen split. We evaluate an epistemic only variant (geometric + semantic), an aleatoric only variant (appearance), ...
- **p. 9 / 4 EXPERIMENT - extractive body cue:** To control SGM scale, we apply pruning thresholds τe and τα to filter out Gaussians with small scale (∥ei∥2 < τe) or low opacity (αi ...

## Why Read It

World models, safety, uncertainty, and recovery의 navigation 문제를 이해하기 위해 읽는다. 본문은 Despite these advances, existing agents typically ignore uncertainty in perception when making decisions.를 문제로 두고, To approximate it, like [66], we introduce variational distributions qϕ(χ) = {qϕµ i (χµ i ), qϕe i (χe i)}i and optimize them by minimizing the Kullback-Leibler (KL) divergence to true posterior ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 6 (3 METHOD), p. 6 (3 METHOD) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
