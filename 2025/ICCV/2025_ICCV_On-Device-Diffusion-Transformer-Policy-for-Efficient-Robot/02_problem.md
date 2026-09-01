# Problem - On-Device Diffusion Transformer Policy for Efficient Robot Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Wu_On-Device_Diffusion_Transformer_Policy_for_Efficient_Robot_Manipulation_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Wu_On-Device_Diffusion_Transformer_Policy_for_Efficient_Robot_Manipulation_ICCV_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 1 (1. Introduction)): However, this endeavor presents multifaceted challenges: 1) Diffusion Policies require multiple denoising steps, which slows down the generation process; 2) the standard architectures [8, 36, 37] involve billions of parameters, ...

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** Diffusion Policies have significantly advanced robotic manipulation tasks via imitation learning, but their application on resource-constrained mobile platforms remains challenging due to computational inefficiency and ...
- **p. 1 / Abstract - extractive PDF cue:** In this paper, we propose LightDP, a novel framework specifically designed to accelerate Diffusion Policies for real-time deployment on mobile devices.
- **p. 1 / Abstract - extractive PDF cue:** LightDP addresses the computational bottleneck through two core strategies: network compression of the denoising modules and reduction of the required sampling steps.
- **p. 1 / Abstract - extractive PDF cue:** We first conduct an extensive computational analysis on existing Diffusion Policy architectures, identifying the denoising network as the primary contributor to latency.
- **p. 1 / Abstract - extractive PDF cue:** To overcome performance degradation typically associated with conventional pruning methods, we introduce a unified pruning and retraining pipeline, optimizing the model's postpruning recoverability explicitly.
- **p. 1 / 1. Introduction - extractive PDF cue:** However, this endeavor presents multifaceted challenges: 1) Diffusion Policies require multiple denoising steps, which slows down the generation process; 2) the standard architectures [8, 36, ...
- **p. 1 / 1. Introduction - extractive PDF cue:** Through the comprehensive component evaluation, we observe that the denoiser is the major bottleneck for Diffusion Policies (as shown in Table 1).

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, this endeavor presents multifaceted challenges: 1) Diffusion Policies require multiple denoising steps, which slows down the generation process; 2) the standard ... | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | A diffusion policy πϕ(a/o, g) is trained to imitate the expert's behavior by maximizing the log-likelihood of the action a Diffusion Transformer ... | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF |
| State / latent | diffusion, policy, trained, imitate, expert, behavior, maximizing, log-likelihood, action, Transformer | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | Action, Moving, Aerage, Target, Model, Transformer, Block, Pruned | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: diffusion, policy, trained, imitate, expert, behavior, maximizing, log-likelihood, action, Transformer | p. 3 (4.1. Problem Formulation), p. 3 (4.1. Problem Formulation), p. 5 (4.3. Prune the Model by Learning) |
| Decision / output variable | action, pose, option or chunk a; body terms: introduce, novel, framework, named, LightDP, Diffusion, Policies, enables | p. 1 (1. Introduction), p. 2 (1. Introduction), p. 5 (4.3. Prune the Model by Learning) |
| Objective / loss / cost | policy/action modeling objective; cue terms: address, issue, single-stage, pruning, where, mask, weight, jointly | p. 4 (4.3. Prune the Model by Learning), p. 4 (4.3. Prune the Model by Learning), p. 5 (4.3. Prune the Model by Learning), p. 5 (4.3. Prune the Model by Learning) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (4.1. Problem Formulation), p. 5 (4.3. Prune the Model by Learning), p. 5 (4.3. Prune the Model by Learning) |
| Success / guarantee | instruction-conditioned task success | p. 6 (5.1. Benchmarks and Evaluation Metrics), p. 7 (5.4. Evaluation on MDT-V), p. 6 (5.3. Evaluation on DiffusionPolicy Transformer) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. Introduction - extractive PDF cue:** Through the comprehensive component evaluation, we observe that the denoiser is the major bottleneck for Diffusion Policies (as shown in Table 1).

## What the Paper Changes

PDF contribution framing (p. 1 (1. Introduction), p. 2 (1. Introduction), p. 5 (4.3. Prune the Model by Learning), p. 5 (4.3. Prune the Model by Learning), p. 4 (4.3. Prune the Model by Learning)): In this work, we introduce a novel framework named LightDP for Diffusion Policies that enables models to achieve real-time generation on mobile devices.

- **p. 2 / 1. Introduction - extractive PDF cue:** Our contributions are summarized as follows: • We present a novel framework for Diffusion Policies to obtain the efficient diffusion transformer that achieves real-time action ...
- **p. 5 / 4.3. Prune the Model by Learning - extractive PDF cue:** In the left figure, we present the consistency distillation pipeline adopted in our method.
- **p. 5 / 4.3. Prune the Model by Learning - extractive PDF cue:** In the right figure, we present the prune by learning technique used in our method, where a set of Bernoulli variables (gate score) is learned ...
- **p. 4 / 4.3. Prune the Model by Learning - extractive PDF cue:** To address this issue, we propose to use a single-stage pruning method [10], where the mask M and weight ˆϕ are jointly optimized to minimize ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 7 | In the Push-T task, the pruned model successfully pushed the T-shaped block into the goal zone, without any ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | Figure 2. The training pipeline of our proposed LightDP. In the left figure, we present the consistency distillation ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | Our consistency distillation is applied to the model's x0 prediction (predicting the denoised action), following common practice, and ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 3 (4.1. Problem Formulation), p. 3 (4.1. Problem Formulation), p. 5 (4.3. Prune the Model by Learning), p. 4 (4.3. Prune the Model by Learning). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1. Introduction), p. 1 (1. Introduction), interface p. 3 (4.1. Problem Formulation), p. 3 (4.1. Problem Formulation), p. 5 (4.3. Prune the Model by Learning), p. 4 (4.3. Prune the Model by Learning), objective p. 4 (4.3. Prune the Model by Learning), p. 4 (4.3. Prune the Model by Learning), p. 5 (4.3. Prune the Model by Learning), p. 5 (4.3. Prune the Model by Learning).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
