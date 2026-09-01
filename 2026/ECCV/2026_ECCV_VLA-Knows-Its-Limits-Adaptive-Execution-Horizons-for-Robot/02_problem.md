# Problem - VLA Knows Its Limits: Adaptive Execution Horizons for Robot Policies

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2602.21445; PDF retrieval source: https://arxiv.org/pdf/2602.21445. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Preliminary)): 1, varying the execution horizon leads to substantial performance fluctuations-ranging from consistent successes to frequent failures.

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** Action chunking has recently emerged as a standard practice in flow-based Vision-Language-Action (VLA) models.
- **p. 1 / Abstract - extractive PDF cue:** However, the effect and choice of the execution horizon-the number of actions to be executed from each predicted chunk-remains underexplored.
- **p. 1 / Abstract - extractive PDF cue:** In this work, we first show that varying the execution horizon leads to substantial performance deviations, with performance initially improving and then declining as the ...
- **p. 1 / Abstract - extractive PDF cue:** To uncover the reasons, we analyze the cross- and self-attention weights in flow-based VLAs and reveal two key phenomena: (i) intrachunk actions attend invariantly to ...
- **p. 1 / Abstract - extractive PDF cue:** Motivated by these insights, we interpret action self-attention weights as a proxy for the model's predictive limit and propose AutoHorizon, the first test-time method that ...
- **p. 1 / 1. Introduction - extractive PDF cue:** 1, varying the execution horizon leads to substantial performance fluctuations-ranging from consistent successes to frequent failures.
- **p. 1 / 1. Introduction - extractive PDF cue:** Prior works [3, 8, 12, 24, 39] typically set a fixed execu1 arXiv:2602.21445v2 [cs.RO] 20 Jun 2026

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | 1, varying the execution horizon leads to substantial performance fluctuations-ranging from consistent successes to frequent failures. | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | Denote the pretrained diffusion-/flow-based VisionLanguage-Action (VLA) model as π(At/ot, c), where ot represents the input visual observations at time step t, and ... | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF |
| State / latent | Denote, pretrained, diffusion-/flow-based, VisionLanguage-Action, VLA, model, At/ot, where, represents, input | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | Instead, predicting, single, action, step, policy, outputs, sequence | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: Denote, pretrained, diffusion-/flow-based, VisionLanguage-Action, VLA, model, At/ot, where, represents, input | p. 3 (3.1. Preliminary), p. 3 (3.1. Preliminary), p. 1 (1. Introduction) |
| Decision / output variable | action, pose, option or chunk a; body terms: Building, insights, AutoHorizon, novel, attention-guided, strategy, dynamically, estimates | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Preliminary) |
| Objective / loss / cost | policy/action modeling objective; cue terms: Let, denote, loss, final, task, reward, incurred, chunk | p. 6 (3.4. AutoHorizon), p. 4 (3.2. Existence of Optimal Execution Horizon), p. 4 (3.2. Existence of Optimal Execution Horizon), p. 5 (3.3. VLA Knows Its Limits), p. 6 (3.4. AutoHorizon) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (3.2. Existence of Optimal Execution Horizon), p. 5 (3.3. VLA Knows Its Limits), p. 3 (3.1. Preliminary) |
| Success / guarantee | instruction-conditioned task success | p. 8 (4.2. Simulation Results), p. 13 (Figure/Table caption), p. 1 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. Introduction - extractive PDF cue:** Prior works [3, 8, 12, 24, 39] typically set a fixed execu1 arXiv:2602.21445v2 [cs.RO] 20 Jun 2026
- **p. 2 / 1. Introduction - extractive PDF cue:** (3) Extensive experiments on simulated and real-world robot manipulation tasks demonstrate that our method generalizes across different flow-based policies, incurs negligible computational overhead, and outperforms ...
- **p. 3 / 3.1. Preliminary - extractive PDF cue:** Here, the parameter p ∈N specifies the prediction horizon, i.e., the temporal window over which the model forecasts future actions conditioned on the current perceptual-linguistic ...

## What the Paper Changes

PDF contribution framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Preliminary), p. 5 (3.4. AutoHorizon), p. 5 (3.4. AutoHorizon)): (2) Building on these insights, we propose AutoHorizon, a novel attention-guided strategy that dynamically estimates the execution horizon for each action chunk, allowing the policy to adapt to varying perceptual ...

- **p. 2 / 1. Introduction - extractive PDF cue:** Specifically, we introduce a bidirectional soft-pointer mechanism that locates the first turning points where the attention mass ceases to advance and begins to plateau.
- **p. 3 / 3.1. Preliminary - extractive PDF cue:** Building on these insights, we introduce an efficient strategy for execution 3
- **p. 5 / 3.4. AutoHorizon - extractive PDF cue:** Motivated by the above analysis, we propose leveraging attention weights as a proxy to estimate the execution horizon for each action chunk.
- **p. 5 / 3.4. AutoHorizon - extractive PDF cue:** To this end, we introduce AutoHorizon-a dataadaptive approach that estimates execution horizons directly from the model's intrinsic attention dynamics.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 7 | Most estimated horizons fall within moderately low values-favoring reactivity-while occasional larger horizons facilitate faster task 7 | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | For all experiments, we report both the mean and standard deviation to ensure fair comparison and robust evaluation. | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Object positions and orientations are randomized across trials to ensure robustness and generalization. | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Compared with the strong Static Oracle+ baseline, it always achieves comparable or even superior results, demonstrating robustness to ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 3 (3.1. Preliminary), p. 3 (3.1. Preliminary), p. 1 (1. Introduction), p. 5 (3.3. VLA Knows Its Limits). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Preliminary), interface p. 3 (3.1. Preliminary), p. 3 (3.1. Preliminary), p. 1 (1. Introduction), p. 5 (3.3. VLA Knows Its Limits), objective p. 6 (3.4. AutoHorizon), p. 4 (3.2. Existence of Optimal Execution Horizon), p. 4 (3.2. Existence of Optimal Execution Horizon), p. 5 (3.3. VLA Knows Its Limits), p. 6 (3.4. AutoHorizon).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
