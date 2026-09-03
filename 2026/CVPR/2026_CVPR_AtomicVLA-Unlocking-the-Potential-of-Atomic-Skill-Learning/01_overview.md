# AtomicVLA: Unlocking the Potential of Atomic Skill Learning in Robots

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_AtomicVLA_Unlocking_the_Potential_of_Atomic_Skill_Learning_in_Robots_CVPR_2026_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_AtomicVLA_Unlocking_the_Potential_of_Atomic_Skill_Learning_in_Robots_CVPR_2026_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: Robotics, VLA, atomic skills, skill composition, long-horizon manipulation
- Official paper: https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_AtomicVLA_Unlocking_the_Potential_of_Atomic_Skill_Learning_in_Robots_CVPR_2026_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_AtomicVLA_Unlocking_the_Potential_of_Atomic_Skill_Learning_in_Robots_CVPR_2026_paper.pdf
- Code/Project: https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_AtomicVLA_Unlocking_the_Potential_of_Atomic_Skill_Learning_in_Robots_CVPR_2026_paper.html
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 However, recent studies [23, 52, 53] suggest that modular decoupling leads to a lack of mutual awareness between the planner and controller, causing suboptimal task coordination.를 문제로 두고, Overall, our contributions are as follows: • We introduce AtomicVLA, an end-to-end framework that unifies task planning and action execution for longhorizon tasks and continual skill expansion. • We propose a Skill-Guided ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Recent advances in Visual-Language-Action (VLA) models have shown promising potential for robotic manipulation tasks.
- **p. 1 / Abstract - extractive body cue:** However, real-world robotic tasks often involve longhorizon, multi-step problem-solving and require generalization for continual skill acquisition, extending beyond single actions or skills.
- **p. 1 / Abstract - extractive body cue:** These challenges present significant barriers for existing VLA models, which use monolithic action decoders trained on aggregated data, resulting in poor scalability.
- **p. 1 / Abstract - extractive body cue:** To address these challenges, we propose AtomicVLA, a unified planning-and-execution framework that jointly generates task-level plans, atomic skill abstractions, and fine-grained actions.
- **p. 1 / Abstract - extractive body cue:** AtomicVLA constructs a scalable atomic skill library through a Skill-Guided Mixture-ofExperts (SG-MoE), where each expert specializes in mastering generic yet precise atomic skills.
- **p. 1 / 1. Introduction - extractive body cue:** However, recent studies [23, 52, 53] suggest that modular decoupling leads to a lack of mutual awareness between the planner and controller, causing suboptimal task ...
- **p. 1 / 1. Introduction - extractive body cue:** Despite this progress, current VLA models still face challenges in real- † Co-corresponding author VLM Action Head Skill Expandable Skill Decoupled SG-MoE Skill 1 Skill ...

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** Overall, our contributions are as follows: • We introduce AtomicVLA, an end-to-end framework that unifies task planning and action execution for longhorizon tasks and continual ...
- **p. 2 / 1. Introduction - extractive body cue:** To this end, we propose AtomicVLA, as illustrated in Fig.
- **p. 3 / 3.1. Overview - extractive body cue:** To further ensure the generation of high-quality task planning data, we introduce an embodiment data generation pipeline (Sec.
- **p. 4 / 3.2. Unified Task Planning and Action Execution - extractive body cue:** To enable seamless switching between the two output modalities, we introduce two special output tokens: [think] and [act].
- **p. 4 / 3.3. Skill-guided Mixture of Experts Architecture - extractive body cue:** 2(b), our skill library consists of three key components: (1) a skill router, (2) a shared expert that maintains the pre-trained action generation capabilities of ...
- **p. 5 / 3.4. Continual Learning with Skill Expansion - extractive body cue:** The left row shows the initial task state (top) and the skill-expert activation during inference (bottom). design inherently enables incremental learning in lifelong settings: when ...
- **p. 4 / 3.2. Unified Task Planning and Action Execution - extractive body cue:** As illustrated in Algorithm 1, given the current visual observations O1:n t and task instruction ℓ, the model first predicts identifier either [think] or [act].
- **p. 4 / 3.1. Overview - extractive body cue:** Algorithm 1 Inference Pipeline of AtomicVLA Require: VLA model πθ, language instruction ℓ 1: t ←0, O1:n t ←initial image, Atomic ←none 2: while "task ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Specifically, in thinking mode, the policy takes multiple cameras observations O1:n t and a language instruction ℓas input and outputs a high-level task plan [C0-k, Ct, σ] in textual form. | image/video, language instruction, proprioception과 history | p. 4 (3.2. Unified Task Planning and Action Execution), p. 4 (3.2. Unified Task Planning and Action Execution) |
| State/latent | Specifically, thinking, mode, policy, takes, multiple, cameras, observations, language, instruction, input, outputs | language-grounded task state와 action-policy context | p. 4 (3.2. Unified Task Planning and Action Execution), p. 4 (3.2. Unified Task Planning and Action Execution), p. 2 (1. Introduction) |
| Output/action | In contrast, in acting mode, the policy generates a concrete action command conditioned on the robot's proprioceptive state St and the most recent planning output σ. | continuous action, pose 또는 action chunk | p. 4 (3.2. Unified Task Planning and Action Execution), p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Objective/outcome | The router computes a probability distribution over experts as: w _{k} = \tex t {Ro ut e r } ( Z_\sigma ), \quad k \in \{1, 2, \dots , K\}, (2) where ... | instruction following, task success, generalization과 latency | p. 4 (3.3. Skill-guided Mixture of Experts Architecture), p. 4 (3.2. Unified Task Planning and Action Execution), p. 5 (3.5. Task Planning Embodied Data Generation) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** Overall, our contributions are as follows: • We introduce AtomicVLA, an end-to-end framework that unifies task planning and action execution for longhorizon tasks and continual ...
- **p. 2 / 1. Introduction - extractive body cue:** To this end, we propose AtomicVLA, as illustrated in Fig.
- **p. 3 / 3.1. Overview - extractive body cue:** To further ensure the generation of high-quality task planning data, we introduce an embodiment data generation pipeline (Sec.
- **p. 4 / 3.2. Unified Task Planning and Action Execution - extractive body cue:** To enable seamless switching between the two output modalities, we introduce two special output tokens: [think] and [act].
- **p. 4 / 3.3. Skill-guided Mixture of Experts Architecture - extractive body cue:** 2(b), our skill library consists of three key components: (1) a skill router, (2) a shared expert that maintains the pre-trained action generation capabilities of ...
- **p. 8 / 4.4. Ablation Study - extractive body cue:** 5, AtomicVLA achieves a success rate of 95.2%, outperforming the MoE baseline by 6.6% and the timestep-conditioned MoDE variant by 5.7%.
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4. Error Recovery Capability Demonstration. When encountering a skill execution failure, AtomicVLA automatically assesses the progress and re-executes the current skill. suites, outperforming the ...
- **p. 6 / 4.2. Results on Simulation - extractive body cue:** 1, AtomicVLA achieves an average success rate of 96.6% across the four Calvin LIBERO Figure 4.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 8 (4.4. Ablation Study), p. 6 (Figure/Table caption) |
| Embodiment/environment | We use 5 skill experts for both the LIBERO benchmark suite and real-world robot experiments. | hardware/simulator version and reset protocol | p. 6 (4.1. Experiments Setup), p. 6 (4.1. Experiments Setup) |
| Dataset/benchmark | Previous real-world studies on robotic manipulation typically focus on training and evaluating a single specific task, while joint training across multiple heterogeneous tasks has been relatively uncommon. | role, split, size and leakage | p. 6 (4.1. Experiments Setup), p. 6 (4.1. Experiments Setup), p. 7 (4.3. Results on Real-world Robot), p. 5 (4.1. Experiments Setup) |
| Metric | Figure 4. Error Recovery Capability Demonstration. When encountering a skill execution failure, AtomicVLA automatically assesses the progress and re-executes the current skill. suites, outperforming the strong baseline by 2.4%. Notably, ... | definition, denominator, direction and uncertainty | p. 6 (Figure/Table caption), p. 6 (4.2. Results on Simulation), p. 7 (4.3. Results on Real-world Robot) |
| Baseline/ablation | When encountering a skill execution failure, AtomicVLA automatically assesses the progress and re-executes the current skill. suites, outperforming the strong baseline by 2.4%. | fair input/data/compute/action matching | p. 6 (4.2. Results on Simulation), p. 7 (4.3. Results on Real-world Robot), p. 7 (4.2. Results on Simulation) |

## Explicit Limitations and Failure Boundary

- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4. Error Recovery Capability Demonstration. When encountering a skill execution failure, AtomicVLA automatically assesses the progress and re-executes the current skill. suites, outperforming the ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 6. Mixed-Training Skill Interference and Continual- Learning Degradation. The top two rows illustrate skill interfer- ence in long-horizon tasks: the first shows successful single-skill ...
- **p. 6 / 4.2. Results on Simulation - extractive body cue:** Importantly, when an execution failure occurs, for example, the butter is grasped but subsequently dropped as illustrated in Fig.
- **p. 7 / 4.2. Results on Simulation - extractive body cue:** However, due to the evaluation constraints of the CALVIN benchmark, successful recoveries after failures are not considered valid completions, which prevents subsequent tasks from being ...
- **p. 7 / 4.3. Results on Real-world Robot - extractive body cue:** AtomicVLA* reliably completes the experimental configurations that π0.5 fails to accomplish, and this advantage becomes more evident in tasks involving door-closing operations.
- **p. 8 / 5. Conclusion - extractive body cue:** Notably, it effectively mitigates skill interference arising from joint training and alleviates knowledge forgetting and performance degradation during continual skill acquisition, highlighting its significant potential ...

## Why Read It

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 However, recent studies [23, 52, 53] suggest that modular decoupling leads to a lack of mutual awareness between the planner and controller, causing suboptimal task coordination.를 문제로 두고, Overall, our contributions are as follows: • We introduce AtomicVLA, an end-to-end framework that unifies task planning and action execution for longhorizon tasks and continual skill expansion. • We propose a Skill-Guided ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 5 (3.4. Continual Learning with Skill Expansion), p. 4 (3.2. Unified Task Planning and Action Execution) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (12 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** However, recent studies [23, 52, 53] suggest that modular decoupling leads to a lack of mutual awareness between the planner and controller, causing suboptimal task coordination. (p. 1, 1. Introduction).
- **Actual contribution:** Overall, our contributions are as follows: • We introduce AtomicVLA, an end-to-end framework that unifies task planning and action execution for longhorizon tasks and continual skill expansion. • We propose ... (p. 2, 1. Introduction).
- **Evaluation boundary:** Figure 4. Error Recovery Capability Demonstration. When encountering a skill execution failure, AtomicVLA automatically assesses the progress and re-executes the current skill. suites, outperforming the strong baseline by 2.4%. Notably, ... (p. 6, Figure/Table caption).
- **Explicit failure boundary:** Importantly, when an execution failure occurs, for example, the butter is grasped but subsequently dropped as illustrated in Fig. (p. 6, 4.2. Results on Simulation).
