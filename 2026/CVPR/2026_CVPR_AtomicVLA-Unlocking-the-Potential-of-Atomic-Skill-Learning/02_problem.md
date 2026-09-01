# Problem - AtomicVLA: Unlocking the Potential of Atomic Skill Learning in Robots

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_AtomicVLA_Unlocking_the_Potential_of_Atomic_Skill_Learning_in_Robots_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_AtomicVLA_Unlocking_the_Potential_of_Atomic_Skill_Learning_in_Robots_CVPR_2026_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction)): However, recent studies [23, 52, 53] suggest that modular decoupling leads to a lack of mutual awareness between the planner and controller, causing suboptimal task coordination.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Recent advances in Visual-Language-Action (VLA) models have shown promising potential for robotic manipulation tasks.
- **p. 1 / Abstract - extractive body cue:** However, real-world robotic tasks often involve longhorizon, multi-step problem-solving and require generalization for continual skill acquisition, extending beyond single actions or skills.
- **p. 1 / Abstract - extractive body cue:** These challenges present significant barriers for existing VLA models, which use monolithic action decoders trained on aggregated data, resulting in poor scalability.
- **p. 1 / Abstract - extractive body cue:** To address these challenges, we propose AtomicVLA, a unified planning-and-execution framework that jointly generates task-level plans, atomic skill abstractions, and fine-grained actions.
- **p. 1 / Abstract - extractive body cue:** AtomicVLA constructs a scalable atomic skill library through a Skill-Guided Mixture-ofExperts (SG-MoE), where each expert specializes in mastering generic yet precise atomic skills.
- **p. 1 / 1. Introduction - extractive body cue:** However, recent studies [23, 52, 53] suggest that modular decoupling leads to a lack of mutual awareness between the planner and controller, causing suboptimal task ...
- **p. 1 / 1. Introduction - extractive body cue:** Despite this progress, current VLA models still face challenges in real- † Co-corresponding author VLM Action Head Skill Expandable Skill Decoupled SG-MoE Skill 1 Skill ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, recent studies [23, 52, 53] suggest that modular decoupling leads to a lack of mutual awareness between the planner and controller, ... | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | Specifically, in thinking mode, the policy takes multiple cameras observations O1:n t and a language instruction ℓas input and outputs a high-level ... | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF |
| State / latent | Specifically, thinking, mode, policy, takes, multiple, cameras, observations, language, instruction | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | AtomicVLA, first, infers, current, execution, state, input, observations | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: Specifically, thinking, mode, policy, takes, multiple, cameras, observations, language, instruction | p. 4 (3.2. Unified Task Planning and Action Execution), p. 4 (3.2. Unified Task Planning and Action Execution), p. 2 (1. Introduction) |
| Decision / output variable | action, pose, option or chunk a; body terms: Overall, contributions, follows, introduce, AtomicVLA, end-to-end, framework, unifies | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Overview) |
| Objective / loss / cost | policy/action modeling objective; cue terms: router, computes, probability, distribution, over, experts, sigma, quad | no optimization/equation sentence selected |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (3.2. Unified Task Planning and Action Execution), p. 5 (3.5. Task Planning Embodied Data Generation), p. 5 (3.4. Continual Learning with Skill Expansion) |
| Success / guarantee | instruction-conditioned task success | p. 6 (Figure/Table caption), p. 6 (4.2. Results on Simulation), p. 7 (4.3. Results on Real-world Robot) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. Introduction - extractive body cue:** Despite this progress, current VLA models still face challenges in real- † Co-corresponding author VLM Action Head Skill Expandable Skill Decoupled SG-MoE Skill 1 Skill ...
- **p. 2 / 1. Introduction - extractive body cue:** existing models, which demands substantial computational resources and large datasets.
- **p. 2 / 1. Introduction - extractive body cue:** Given the current scarcity of robot data, fully leveraging well-pretrained VLA model weights is essential during the scaling process.

## What the Paper Changes

PDF contribution framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Overview), p. 4 (3.2. Unified Task Planning and Action Execution), p. 4 (3.3. Skill-guided Mixture of Experts Architecture)): Overall, our contributions are as follows: • We introduce AtomicVLA, an end-to-end framework that unifies task planning and action execution for longhorizon tasks and continual skill expansion. • We propose ...

- **p. 2 / 1. Introduction - extractive body cue:** To this end, we propose AtomicVLA, as illustrated in Fig.
- **p. 3 / 3.1. Overview - extractive body cue:** To further ensure the generation of high-quality task planning data, we introduce an embodiment data generation pipeline (Sec.
- **p. 4 / 3.2. Unified Task Planning and Action Execution - extractive body cue:** To enable seamless switching between the two output modalities, we introduce two special output tokens: [think] and [act].
- **p. 4 / 3.3. Skill-guided Mixture of Experts Architecture - extractive body cue:** 2(b), our skill library consists of three key components: (1) a skill router, (2) a shared expert that maintains the pre-trained action generation capabilities of ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 6 | Figure 4. Error Recovery Capability Demonstration. When encountering a skill execution failure, AtomicVLA automatically assesses the progress and ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Figure 6. Mixed-Training Skill Interference and Continual- Learning Degradation. The top two rows illustrate skill interfer- ence in ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | Importantly, when an execution failure occurs, for example, the butter is grasped but subsequently dropped as illustrated in ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | However, due to the evaluation constraints of the CALVIN benchmark, successful recoveries after failures are not considered valid ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 4 (3.2. Unified Task Planning and Action Execution), p. 4 (3.2. Unified Task Planning and Action Execution), p. 2 (1. Introduction), p. 2 (1. Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), interface p. 4 (3.2. Unified Task Planning and Action Execution), p. 4 (3.2. Unified Task Planning and Action Execution), p. 2 (1. Introduction), p. 2 (1. Introduction), objective no optimization/equation sentence selected.
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
