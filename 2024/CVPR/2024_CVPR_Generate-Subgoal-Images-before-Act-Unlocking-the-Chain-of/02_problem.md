# Problem - Generate Subgoal Images before Act: Unlocking the Chain-of-Thought Reasoning in Diffusion Model for Robot Manipulation with Multimodal Prompts

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Ni_Generate_Subgoal_Images_before_Act_Unlocking_the_Chain-of-Thought_Reasoning_in_CVPR_2024_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Ni_Generate_Subgoal_Images_before_Act_Unlocking_the_Chain-of-Thought_Reasoning_in_CVPR_2024_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction)): However, robotics agents still face significant challenges in following instructions for long-horizon manipulation tasks, especially when the given general instructions are not progressive step-wise prompts, but implicitly contain sever ...

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** Robotics agents often struggle to understand and follow the multi-modal prompts in complex manipulation scenes which are challenging to be sufficiently and accurately described by ...
- **p. 1 / Abstract - extractive PDF cue:** Moreover, for long-horizon manipulation tasks, the deviation from general instruction tends to accumulate if lack of intermediate guidance from high-level subgoals.
- **p. 1 / Abstract - extractive PDF cue:** For this, we consider can we generate subgoal images before act to enhance the instruction following in long-horizon manipulation with multi-modal prompts?
- **p. 1 / Abstract - extractive PDF cue:** Inspired by the great success of diffusion model in image generation tasks, we propose a novel hierarchical framework named as CoTDiffusion that incorporates diffusion model ...
- **p. 1 / Abstract - extractive PDF cue:** We design a semantic alignment module that can anchor the progress of generated keyframes along a coherent generation chain, unlocking the chain-of-thought reasoning ability of ...
- **p. 1 / 1. Introduction - extractive PDF cue:** However, robotics agents still face significant challenges in following instructions for long-horizon manipulation tasks, especially when the given general instructions are not progressive step-wise prompts, ...
- **p. 2 / 1. Introduction - extractive PDF cue:** However, the compounding small errors over long horizons will lead to catastrophic deviations from the original task instructions due to the lack of intermediate guidance ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, robotics agents still face significant challenges in following instructions for long-horizon manipulation tasks, especially when the given general instructions are not ... | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | The policy model can be parameterized as an image-conditioned planner that infers the action ai,t given the current observation xi,t and the ... | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF |
| State / latent | policy, model, parameterized, image-conditioned, planner, infers, action, given, current, observation | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | Generated, Subgoal, Current, Observation, Environment, Multi, Modal, Instructions | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: policy, model, parameterized, image-conditioned, planner, infers, action, given, current, observation | p. 5 (3.4. Goal-conditioned Policy Model), p. 3 (3.1. Pipeline Overview), p. 4 (3.1. Pipeline Overview) |
| Decision / output variable | action, pose, option or chunk a; body terms: contributions, follows, hierarchical, framework, CoTDiffusion, high-level, diffusion, model | p. 2 (1. Introduction), p. 3 (3.1. Pipeline Overview), p. 4 (3.2. Pre-training Coarse Semantic Alignment) |
| Objective / loss / cost | policy/action modeling objective; cue terms: training, objective, formulated, Exi2D, xi-1, align, Forward, Generation | p. 5 (3.3. Fine-grained Diffusion Training), p. 5 (3.3. Fine-grained Diffusion Training), p. 6 (3.4. Goal-conditioned Policy Model) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (3.1. Pipeline Overview), p. 3 (3. Method), p. 4 (3.2. Pre-training Coarse Semantic Alignment) |
| Success / guarantee | instruction-conditioned task success | p. 7 (4.3. Quantitative Results of Success Rate), p. 6 (4.1. Experiment Setup), p. 6 (4.3. Quantitative Results of Success Rate) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Introduction - extractive PDF cue:** However, the compounding small errors over long horizons will lead to catastrophic deviations from the original task instructions due to the lack of intermediate guidance ...
- **p. 1 / 1. Introduction - extractive PDF cue:** Moreover, complex manipulation scenarios with rich visual contexts are often challenging to be sufficiently and accurately described through text-only prompts, requiring multi-modal prompts to convey ...
- **p. 2 / 1. Introduction - extractive PDF cue:** The key challenge to enabling CoTDiffusion to progressively generate subgoal images in a chain-of-thought manner lies in tracking the generated subgoal's progress on task prompts.

## What the Paper Changes

PDF contribution framing (p. 2 (1. Introduction), p. 3 (3.1. Pipeline Overview), p. 4 (3.2. Pre-training Coarse Semantic Alignment), p. 4 (3.2. Pre-training Coarse Semantic Alignment), p. 5 (3.3. Fine-grained Diffusion Training)): The contributions of this work are as follows: • We propose a hierarchical framework CoTDiffusion that the high-level diffusion model translates the multi-modal prompts into coherent subgoal images in a ...

- **p. 3 / 3.1. Pipeline Overview - extractive PDF cue:** Under the Markovian assumption, the overall framework can be formulated as: p⇥({⌧i a}N i=1/P, x0) = N Y i=1 pφ(xi/P, x0) ! / {z } ...
- **p. 4 / 3.2. Pre-training Coarse Semantic Alignment - extractive PDF cue:** Thus, we propose a two-stage coarse-to-fine approach decoupling semantic alignment pretraining from diffusion model finetuning, illustrated in Fig.
- **p. 4 / 3.2. Pre-training Coarse Semantic Alignment - extractive PDF cue:** Then they are refined through fusion module which consists of several self-attention blocks separately to obtain attention tokens z0 and zi aligned to the prompts.
- **p. 5 / 3.3. Fine-grained Diffusion Training - extractive PDF cue:** Here we propose bi-directional aligned generation, where the aligned token zi align not only guides forward prediction but also reconstructs the current frame through backward ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | Incorporating commonsense knowledge from pre-trained MLLM like GPT-4V provides an avenue for more generalizable and promising reasoning in ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | Additionally, ablating coarse pretraining and bi-directional generation degrades performance, validating their benefits. | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | Robustness to Insufficient Perception Rich visual observations from diverse views are crucial for complex robot manipulation tasks. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 5 (3.4. Goal-conditioned Policy Model), p. 3 (3.1. Pipeline Overview), p. 4 (3.1. Pipeline Overview), p. 3 (3.1. Pipeline Overview). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), interface p. 5 (3.4. Goal-conditioned Policy Model), p. 3 (3.1. Pipeline Overview), p. 4 (3.1. Pipeline Overview), p. 3 (3.1. Pipeline Overview), objective p. 5 (3.3. Fine-grained Diffusion Training), p. 5 (3.3. Fine-grained Diffusion Training), p. 6 (3.4. Goal-conditioned Policy Model).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
