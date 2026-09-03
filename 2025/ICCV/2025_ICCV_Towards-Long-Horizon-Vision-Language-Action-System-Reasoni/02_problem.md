# Problem - Towards Long-Horizon Vision-Language-Action System: Reasoning, Acting and Memory

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Li_Towards_Long-Horizon_Vision-Language-Action_System_Reasoning_Acting_and_Memory_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Li_Towards_Long-Horizon_Vision-Language-Action_System_Reasoning_Acting_and_Memory_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (1. Introduction), p. 2 (1. Introduction)): Consequently, this remains an open and worthwhile challenge so far.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Vision-Language-Action (VLA) is crucial for autonomous decision-making in embodied systems.
- **p. 1 / Abstract - extractive body cue:** While current methods have advanced single-skill abilities, their short-horizon capability limits applicability in real-world scenarios.
- **p. 1 / Abstract - extractive body cue:** To address this challenge, we innovatively propose MindExplore, a general hierarchical VLA system with cross-skill for long-horizon tasks in highly dynamic sand.
- **p. 1 / Abstract - extractive body cue:** The key insight is to iteratively align the knowledge domain of task planning and action execution.
- **p. 1 / Abstract - extractive body cue:** Thus, this task-oriented action enables outstanding generalization across a wide range of real-world scenarios.
- **p. 2 / 1. Introduction - extractive body cue:** Consequently, this remains an open and worthwhile challenge so far.
- **p. 2 / 1. Introduction - extractive body cue:** However, these approaches fail to generalize for long-horizon tasks in real-world scenarios, particularly in complex terrain action [14, 33].

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Consequently, this remains an open and worthwhile challenge so far. | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | To achieve this, three key challenges must be addressed: (1) Task-oriented Chain of Thought (CoT) reasoning requires the hierarchical decomposition of coarse-grained ... | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF body |
| State / latent | achieve, three, challenges, must, addressed, Task-oriented, Chain, Thought, CoT, reasoning | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | expert, performs, meta-actions, grasping, placing, outputting, only, pose | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: achieve, three, challenges, must, addressed, Task-oriented, Chain, Thought, CoT, reasoning | p. 2 (1. Introduction), p. 5 (4.2.2. Mixture of Policy Experts), p. 5 (4.2.2. Mixture of Policy Experts) |
| Decision / output variable | action, pose, option or chunk a; body terms: contributions, summarized, follows, MindExplore, novel, expert-level, hierarchical, embodied | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 5 (4.2.2. Mixture of Policy Experts) |
| Objective / loss / cost | policy/action modeling objective; cue terms: denoising, network, then, predict, random, noise, training, loss | p. 5 (4.2.1. Multimodal Diffusion Policy) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (4.2.1. Multimodal Diffusion Policy) |
| Success / guarantee | instruction-conditioned task success | p. 8 (5.3. Ablation Study), p. 8 (5.3. Ablation Study), p. 6 (5.1. Implementation Details) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Introduction - extractive body cue:** However, these approaches fail to generalize for long-horizon tasks in real-world scenarios, particularly in complex terrain action [14, 33].

## What the Paper Changes

PDF body contribution framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 5 (4.2.2. Mixture of Policy Experts), p. 5 (4.2.1. Multimodal Diffusion Policy)): Our key contributions are summarized as follows: • We propose MindExplore, a novel expert-level hierarchical embodied system to adapt long-horizon tasks in unstructured and dynamic environments.

- **p. 2 / 1. Introduction - extractive body cue:** Our MindExplore is inspired by the discovery that continuous iterative alignment of the knowledge domain between task planning and action execution enables strong generalization across ...
- **p. 5 / 4.2.2. Mixture of Policy Experts - extractive body cue:** Therefore, we propose a Mixture of Policy Experts Model that decouples manipulation of the robot's base and arm.
- **p. 5 / 4.2.1. Multimodal Diffusion Policy - extractive body cue:** To address these, we propose a multimodal diffusion Policy model (MMDP) that jointly exploits information of multi-sensor data and textual instructions.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 3 | The high dynamic fluidity of sand demands adaptive adjustments, while its visual noise complicates perception and calibration. | reported limitation/failure wording; scope must be verified |
| body cue at p. 3 | Enhancing generalization in unstructured environments remains a key challenge, and our experiments show that a system robust in ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Similarly, the point-cloud-based BE also shows lower success rates, as point cloud data failed to align effectively with ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 2 (1. Introduction), p. 5 (4.2.2. Mixture of Policy Experts), p. 5 (4.2.2. Mixture of Policy Experts), p. 2 (1. Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1. Introduction), p. 2 (1. Introduction), interface p. 2 (1. Introduction), p. 5 (4.2.2. Mixture of Policy Experts), p. 5 (4.2.2. Mixture of Policy Experts), p. 2 (1. Introduction), objective p. 5 (4.2.1. Multimodal Diffusion Policy).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
