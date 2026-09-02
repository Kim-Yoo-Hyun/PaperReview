# Problem - Consistency Policy: Accelerated Visuomotor Policies via Consistency Distillation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss20/p071.html; PDF retrieval source: https://www.roboticsproceedings.org/rss20/p071.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (I. INTRODUCTION)): 1: Both Diffusion and Consistency Policy work by sampling random actions and denoising them into predictions of actions. xt denotes the current action distribution at a time t ∈[0, T], ...

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Many robotic systems, such as mobile manipulators or quadrotors, cannot be equipped with high-end GPUs due to space, weight, and power constraints.
- **p. 1 / Abstract - extractive body cue:** These constraints prevent these systems from leveraging recent developments in visuomotor policy architectures that require high-end GPUs to achieve fast policy inference.
- **p. 1 / Abstract - extractive body cue:** In this paper, we propose Consistency Policy, a faster and similarly powerful alternative to Diffusion Policy for learning visuomotor robot control.
- **p. 1 / Abstract - extractive body cue:** By virtue of its fast inference speed, Consistency Policy can enable low latency decision making in resource-constrained robotic setups.
- **p. 1 / Abstract - extractive body cue:** A Consistency Policy is distilled from a pretrained Diffusion Policy by enforcing selfconsistency along the Diffusion Policy's learned trajectories.
- **p. 1 / I. INTRODUCTION - extractive body cue:** 1: Both Diffusion and Consistency Policy work by sampling random actions and denoising them into predictions of actions. xt denotes the current action distribution at ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Overall, we demonstrate that inference speed of our approach is on average about an order of magnitude faster than the fastest baseline (see Table I) ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | 1: Both Diffusion and Consistency Policy work by sampling random actions and denoising them into predictions of actions. xt denotes the current ... | multi-robot demonstration/dataset ecosystem | body wording is the source claim |
| Observation / input | The figure shows distributions of predicted action sequences (indicated by the sequences of red to green dots) at different stages of the ... | multi-view observation, language/task label과 action trajectory | exact sensor/frame/preprocessing from PDF body |
| State / latent | figure, distributions, predicted, action, sequences, indicated, green, dots, different, stages | shared representation, embodiment/task identity와 data distribution | notation and tensor shape require body check |
| Output / action | diffusion, models, learn, random, actions, sampled, unit, Gaussian | dataset sample 또는 learned policy action | exact unit/frame/decoder require body check |
| Target outcome | cross-domain transfer and task performance | coverage, cross-embodiment transfer, data efficiency와 task success | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | trajectory D with task/embodiment metadata; body terms: figure, distributions, predicted, action, sequences, indicated, green, dots, different, stages | p. 1 (I. INTRODUCTION), p. 4 (2) Student Model (Consistency Policy)), p. 3 (III. CONSISTENCY POLICY) |
| Decision / output variable | normalized sample or downstream action; body terms: Overall, demonstrate, inference, speed, average, about, order, magnitude | p. 2 (I. INTRODUCTION) |
| Objective / loss / cost | coverage/data efficiency/transfer objective; cue terms: Following, optimize, Denoising, Score, Matching, DSM, loss, train | p. 3 (1) Teacher Model (EDM)), p. 4 (2) Student Model (Consistency Policy)), p. 4 (2) Student Model (Consistency Policy)), p. 3 (III. CONSISTENCY POLICY) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (2) Student Model (Consistency Policy)), p. 4 (2) Student Model (Consistency Policy)), p. 3 (III. CONSISTENCY POLICY) |
| Success / guarantee | cross-domain transfer and task performance | p. 6 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 8 (IV. EXPERIMENTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / I. INTRODUCTION - extractive body cue:** 1: Both Diffusion and Consistency Policy work by sampling random actions and denoising them into predictions of actions. xt denotes the current action distribution at ...

## What the Paper Changes

PDF body contribution framing (p. 2 (I. INTRODUCTION)): Overall, we demonstrate that inference speed of our approach is on average about an order of magnitude faster than the fastest baseline (see Table I) and maintains similar or higher ...

- additional contribution cue 없음

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 9 | In future work, we will explore how we can potentially re-introduce multimodality to Consistency Policy through more complex ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | Single-step CP often falls in between DDPM and DDiM in terms of success rate, especially on the harder ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | More discussion about the mobile task in particular is present in Limitations see Sec. | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | Note that we are optimistic in assuming that speeding up the baseline DDPM and DDiM Policies [6] with ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

robot_data writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 1 (I. INTRODUCTION), p. 4 (2) Student Model (Consistency Policy)), p. 3 (III. CONSISTENCY POLICY), p. 1 (I. INTRODUCTION). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (I. INTRODUCTION), interface p. 1 (I. INTRODUCTION), p. 4 (2) Student Model (Consistency Policy)), p. 3 (III. CONSISTENCY POLICY), p. 1 (I. INTRODUCTION), objective p. 3 (1) Teacher Model (EDM)), p. 4 (2) Student Model (Consistency Policy)), p. 4 (2) Student Model (Consistency Policy)), p. 3 (III. CONSISTENCY POLICY).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
