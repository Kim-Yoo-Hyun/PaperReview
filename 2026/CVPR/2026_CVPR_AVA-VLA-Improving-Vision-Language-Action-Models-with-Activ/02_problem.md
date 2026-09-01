# Problem - AVA-VLA: Improving Vision-Language-Action Models with Active Visual Attention

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Xiao_AVA-VLA_Improving_Vision-Language-Action_models_with_Active_Visual_Attention_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Xiao_AVA-VLA_Improving_Vision-Language-Action_models_with_Active_Visual_Attention_CVPR_2026_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 3 (3.1. Preliminaries)): Our contributions are threefold: • We propose the novel AVA-VLA framework to solve the critical limitation of lacking historical context in MDPbased VLA models.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Vision-Language-Action (VLA) models have shown remarkable progress in embodied tasks recently, but most methods process visual observations independently at each timestep.
- **p. 1 / Abstract - extractive body cue:** This history-agnostic design treats robot manipulation as a Markov Decision Process, even though realworld robotic control is inherently partially observable and requires reasoning over past ...
- **p. 1 / Abstract - extractive body cue:** To address this mismatch, we reformulate VLA policy learning from a Partially Observable Markov Decision Process perspective and propose AVA-VLA, a framework that conditions action ...
- **p. 1 / Abstract - extractive body cue:** Built on this recurrent state, we introduce Active Visual Attention (AVA), which dynamically reweights visual tokens in the current observation to focus on regions most ...
- **p. 1 / Abstract - extractive body cue:** Extensive experiments show that AVA-VLA achieves state-of-the-art performance on standard robotic benchmarks, including LIBERO and CALVIN, and transfers effectively to real-world dualarm manipulation tasks.
- **p. 2 / 1. Introduction - extractive body cue:** Our contributions are threefold: • We propose the novel AVA-VLA framework to solve the critical limitation of lacking historical context in MDPbased VLA models.
- **p. 1 / 1. Introduction - extractive body cue:** (b) Qualitative comparison of visual focus from two viewpoints while executing the task "turn on the stove and put the moka pot on it." The ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Our contributions are threefold: • We propose the novel AVA-VLA framework to solve the critical limitation of lacking historical context in MDPbased ... | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | In a POMDP framework, the optimal policy at timestep t should be conditioned not only on the current observation xt but also ... | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF |
| State / latent | POMDP, framework, optimal, policy, timestep, should, conditioned, only, current, observation | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | Therefore, forward, pass, timestep, incorporating, AVA, module, statebased | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: POMDP, framework, optimal, policy, timestep, should, conditioned, only, current, observation | p. 3 (3.2. AVA-VLA Framework), p. 3 (3.1. Preliminaries), p. 4 (3.2. AVA-VLA Framework) |
| Decision / output variable | action, pose, option or chunk a; body terms: contributions, threefold, novel, AVA-VLA, framework, solve, critical, limitation | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Methods) |
| Objective / loss / cost | policy/action modeling objective; cue terms: However, given, substantial, memory, constraint, computational, cost, modern | p. 5 (3.4. Training and Inference Procedure), p. 5 (3.4. Training and Inference Procedure) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (3.4. Training and Inference Procedure), p. 5 (3.4. Training and Inference Procedure) |
| Success / guarantee | instruction-conditioned task success | p. 6 (4.2. Evaluation Results), p. 6 (4.1. Experimental Setup), p. 7 (4.3. Ablation Studies) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. Introduction - extractive body cue:** (b) Qualitative comparison of visual focus from two viewpoints while executing the task "turn on the stove and put the moka pot on it." The ...
- **p. 2 / 1. Introduction - extractive body cue:** In fact, the inability to anticipate perceptual intent a priori makes active visual modules difficult to realize in computer vision.
- **p. 1 / 1. Introduction - extractive body cue:** This implicitly formulates robot manipulation as a Markov Decision Process (MDP) [16, 31], where actions are generated from the current visual observation, assumed to represent ...
- **p. 3 / 3.1. Preliminaries - extractive body cue:** (2) Regardless of whether AR or parallel decoding is used, these VLA models learn to predict the action ¯ At only from the current observation ...

## What the Paper Changes

PDF contribution framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Methods), p. 3 (3.1. Preliminaries), p. 4 (3.2. AVA-VLA Framework)): Our contributions are threefold: • We propose the novel AVA-VLA framework to solve the critical limitation of lacking historical context in MDPbased VLA models.

- **p. 2 / 1. Introduction - extractive body cue:** To our knowledge, it is the first VLA framework to explicitly address this limitation via a POMDP-inspired approach. • We introduce an Active Visual Attention ...
- **p. 3 / 3. Methods - extractive body cue:** In this section, we present our proposed VLA method.
- **p. 3 / 3.1. Preliminaries - extractive body cue:** A typical VLA model Pθ, parameterized by θ, consists of four main components: a Large-Language-Model (LLM) backbone M, a vision encoder E, a language tokenizer ...
- **p. 4 / 3.2. AVA-VLA Framework - extractive body cue:** For simplicity, our framework is built upon the OpenVLA-OFT foundation model.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | Furthermore, a direct comparison in Figure 1 reveals that while the vanilla OpenVLA-OFT baseline fails to localize the ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 1 | Figure 1. (a) Visualized comparison of the proposed AVA-VLA framework and vanilla VLAs. (b) Qualitative comparison of vi- ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | Due to space limitations, implementation details are provided in Appendix A. | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | LIBERO+ [11] is a challenging LIBERO-based benchmark, which offers a robust benchmarking framework with 7 perturbation dimensions and ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 3 (3.2. AVA-VLA Framework), p. 3 (3.1. Preliminaries), p. 4 (3.2. AVA-VLA Framework), p. 4 (3.2. AVA-VLA Framework). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 3 (3.1. Preliminaries), interface p. 3 (3.2. AVA-VLA Framework), p. 3 (3.1. Preliminaries), p. 4 (3.2. AVA-VLA Framework), p. 4 (3.2. AVA-VLA Framework), objective p. 5 (3.4. Training and Inference Procedure), p. 5 (3.4. Training and Inference Procedure).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
