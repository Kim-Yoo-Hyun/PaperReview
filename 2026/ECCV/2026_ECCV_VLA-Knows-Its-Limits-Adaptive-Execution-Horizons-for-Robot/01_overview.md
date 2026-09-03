# VLA Knows Its Limits: Adaptive Execution Horizons for Robot Policies

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2602.21445.
> PDF retrieval source: https://arxiv.org/pdf/2602.21445. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ECCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, Robotics
- Official paper: https://arxiv.org/abs/2602.21445
- Full-text retrieval: https://arxiv.org/pdf/2602.21445
- Code/Project: https://hatchetproject.github.io/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 1, varying the execution horizon leads to substantial performance fluctuations-ranging from consistent successes to frequent failures.를 문제로 두고, (2) Building on these insights, we propose AutoHorizon, a novel attention-guided strategy that dynamically estimates the execution horizon for each action chunk, allowing the policy to adapt to varying perceptual conditions.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Action chunking has recently emerged as a standard practice in flow-based Vision-Language-Action (VLA) models.
- **p. 1 / Abstract - extractive body cue:** However, the effect and choice of the execution horizon-the number of actions to be executed from each predicted chunk-remains underexplored.
- **p. 1 / Abstract - extractive body cue:** In this work, we first show that varying the execution horizon leads to substantial performance deviations, with performance initially improving and then declining as the ...
- **p. 1 / Abstract - extractive body cue:** To uncover the reasons, we analyze the cross- and self-attention weights in flow-based VLAs and reveal two key phenomena: (i) intrachunk actions attend invariantly to ...
- **p. 1 / Abstract - extractive body cue:** Motivated by these insights, we interpret action self-attention weights as a proxy for the model's predictive limit and propose AutoHorizon, the first test-time method that ...
- **p. 1 / 1. Introduction - extractive body cue:** 1, varying the execution horizon leads to substantial performance fluctuations-ranging from consistent successes to frequent failures.
- **p. 1 / 1. Introduction - extractive body cue:** Prior works [3, 8, 12, 24, 39] typically set a fixed execu1.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** (2) Building on these insights, we propose AutoHorizon, a novel attention-guided strategy that dynamically estimates the execution horizon for each action chunk, allowing the policy ...
- **p. 2 / 1. Introduction - extractive body cue:** Specifically, we introduce a bidirectional soft-pointer mechanism that locates the first turning points where the attention mass ceases to advance and begins to plateau.
- **p. 3 / 3.1. Preliminary - extractive body cue:** Building on these insights, we introduce an efficient strategy for execution 3
- **p. 5 / 3.4. AutoHorizon - extractive body cue:** Motivated by the above analysis, we propose leveraging attention weights as a proxy to estimate the execution horizon for each action chunk.
- **p. 5 / 3.4. AutoHorizon - extractive body cue:** To this end, we introduce AutoHorizon-a dataadaptive approach that estimates execution horizons directly from the model's intrinsic attention dynamics.
- **p. 6 / 3.4. AutoHorizon - extractive body cue:** Intuitively, St[i, j] quantifies how strongly the i-th query action attends to the j-th key action, revealing how far the model effectively "looks ahead." Our ...
- **p. 5 / 3.3. VLA Knows Its Limits - extractive body cue:** We infer that, due to the strong vision-language pretraining of the backbone model, most linguistic semantics are already embedded within the visual representations during action ...
- **p. 3 / 3.1. Preliminary - extractive body cue:** Within a standard transformer-based attention mechanism, the attention weight matrix S is defined as the post-softmax similarity between the query and key embeddings: S = ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Denote the pretrained diffusion-/flow-based VisionLanguage-Action (VLA) model as π(At/ot, c), where ot represents the input visual observations at time step t, and c denotes the corresponding language command. | image/video, language instruction, proprioception과 history | p. 3 (3.1. Preliminary), p. 3 (3.1. Preliminary) |
| State/latent | Denote, pretrained, diffusion-/flow-based, VisionLanguage-Action, VLA, model, At/ot, where, represents, input, visual, observations | language-grounded task state와 action-policy context | p. 3 (3.1. Preliminary), p. 3 (3.1. Preliminary), p. 1 (1. Introduction) |
| Output/action | During execution, the agent typically performs the first e actions from the predicted chunk before re-sampling new input observations and generating the next action chunk, where e ∈N defines the execution horizon. | continuous action, pose 또는 action chunk | p. 3 (3.1. Preliminary), p. 1 (1. Introduction), p. 5 (3.3. VLA Knows Its Limits) |
| Objective/outcome | Let δc denote the loss in final task reward incurred at each chunk transition, assumed to be independent of e. | instruction following, task success, generalization과 latency | p. 4 (3.2. Existence of Optimal Execution Horizon), p. 6 (3.4. AutoHorizon), p. 6 (3.4. AutoHorizon) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** (2) Building on these insights, we propose AutoHorizon, a novel attention-guided strategy that dynamically estimates the execution horizon for each action chunk, allowing the policy ...
- **p. 2 / 1. Introduction - extractive body cue:** Specifically, we introduce a bidirectional soft-pointer mechanism that locates the first turning points where the attention mass ceases to advance and begins to plateau.
- **p. 3 / 3.1. Preliminary - extractive body cue:** Building on these insights, we introduce an efficient strategy for execution 3
- **p. 5 / 3.4. AutoHorizon - extractive body cue:** Motivated by the above analysis, we propose leveraging attention weights as a proxy to estimate the execution horizon for each action chunk.
- **p. 5 / 3.4. AutoHorizon - extractive body cue:** To this end, we introduce AutoHorizon-a dataadaptive approach that estimates execution horizons directly from the model's intrinsic attention dynamics.
- **p. 8 / 4.2. Simulation Results - extractive body cue:** 8, and find that AutoHorizon consistently achieves higher success rates.
- **p. 13 / Figure/Table caption - extractive body cue:** Figure 7. Average success rates on the LIBERO benchmark with a prediction horizon of 10 using π0.5. Fig. 7 reports results under a shorter prediction ...
- **p. 7 / 4.2. Simulation Results - extractive body cue:** The enhanced Static Oracle+ consistently achieves strong results, and the specific horizon values used for this baseline are listed in Sec.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 8 (4.2. Simulation Results), p. 13 (Figure/Table caption) |
| Embodiment/environment | Our experiments leverage two benchmark datasets: the LIBERO dataset [20], which offers a diverse suite of single-arm manipulation tasks, and the RoboTwin dataset [7, 23], which focuses on bimanual coordination tasks. | hardware/simulator version and reset protocol | p. 7 (4.2. Simulation Results), p. 7 (4.2. Simulation Results) |
| Dataset/benchmark | We further evaluate AutoHorizon in real-world robotic manipulation scenarios. | role, split, size and leakage | p. 7 (4.2. Simulation Results), p. 7 (4.2. Simulation Results), p. 8 (4.3. Real-World Results), p. 8 (4.3. Real-World Results) |
| Metric | 8, and find that AutoHorizon consistently achieves higher success rates. | definition, denominator, direction and uncertainty | p. 8 (4.2. Simulation Results), p. 13 (Figure/Table caption), p. 1 (Figure/Table caption) |
| Baseline/ablation | Compared with the strong Static Oracle+ baseline, it always achieves comparable or even superior results, demonstrating robustness to hyperparameter choices. | fair input/data/compute/action matching | p. 8 (4.2. Simulation Results), p. 6 (4.1. Experimental Settings), p. 7 (4.2. Simulation Results) |

## Explicit Limitations and Failure Boundary

- **p. 7 / 4.2. Simulation Results - extractive body cue:** Most estimated horizons fall within moderately low values-favoring reactivity-while occasional larger horizons facilitate faster task 7
- **p. 7 / 4.1. Experimental Settings - extractive body cue:** For all experiments, we report both the mean and standard deviation to ensure fair comparison and robust evaluation.
- **p. 8 / 4.3. Real-World Results - extractive body cue:** Object positions and orientations are randomized across trials to ensure robustness and generalization.
- **p. 8 / 4.2. Simulation Results - extractive body cue:** Compared with the strong Static Oracle+ baseline, it always achieves comparable or even superior results, demonstrating robustness to hyperparameter choices.

## Why Read It

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 1, varying the execution horizon leads to substantial performance fluctuations-ranging from consistent successes to frequent failures.를 문제로 두고, (2) Building on these insights, we propose AutoHorizon, a novel attention-guided strategy that dynamically estimates the execution horizon for each action chunk, allowing the policy to adapt to varying perceptual conditions.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Preliminary), p. 6 (3.4. AutoHorizon), p. 5 (3.4. AutoHorizon) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
