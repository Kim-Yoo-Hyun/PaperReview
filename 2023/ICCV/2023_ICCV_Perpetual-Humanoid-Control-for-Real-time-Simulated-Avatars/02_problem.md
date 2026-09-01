# Problem - Perpetual Humanoid Control for Real-time Simulated Avatars

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2023/html/Luo_Perpetual_Humanoid_Control_for_Real-time_Simulated_Avatars_ICCV_2023_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2023/html/Luo_Perpetual_Humanoid_Control_for_Real-time_Simulated_Avatars_ICCV_2023_paper.html. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction)): These limitations prevent the widespread adoption of physics-based methods, as current control policies cannot handle noisy observations such as video or language.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** We present a physics-based humanoid controller that achieves high-fidelity motion imitation and fault-tolerant behavior in the presence of noisy input (e.g. pose estimates from video ...
- **p. 1 / Abstract - extractive body cue:** Our controller scales up to learning ten thousand motion clips without using any external stabilizing forces and learns to naturally recover from fail-state.
- **p. 1 / Abstract - extractive body cue:** Given reference motion, our controller can perpetually control simulated avatars without requiring resets.
- **p. 1 / Abstract - extractive body cue:** At its core, we propose the progressive multiplicative control policy (PMCP), which dynamically allocates new network capacity to learn harder and harder motion sequences.
- **p. 1 / Abstract - extractive body cue:** PMCP allows efficient scaling for learning from large-scale motion databases and adding new tasks, such as fail-state recovery, without catastrophic forgetting.
- **p. 1 / 1. Introduction - extractive body cue:** These limitations prevent the widespread adoption of physics-based methods, as current control policies cannot handle noisy observations such as video or language.
- **p. 1 / 1. Introduction - extractive body cue:** However, controlling high-degree-of-freedom (DOF) humanoids in simulation presents significant challenges, as they can fall, trip, or deviate from their reference motions, and struggle to recover.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | These limitations prevent the widespread adoption of physics-based methods, as current control policies cannot handle noisy observations such as video or language. | high-DoF humanoid whole-body dynamics와 contacts | body wording is the source claim |
| Observation / input | The physics simulation determines state st ∈S and transition dynamics T while our policy πPHC computes per-step action at ∈A. | proprioception, reference pose/motion, visual or language command | exact sensor/frame/preprocessing from PDF |
| State / latent | physics, simulation, determines, state, transition, dynamics, while, policy, PHC, computes | whole-body pose, balance/contact state와 skill/mode | notation and tensor shape require body check |
| Output / action | summarize, contributions, follows, Perpetual, Humanoid, Controller, successfully, imitate | joint/whole-body action, motion target 또는 task trajectory | exact unit/frame/decoder require body check |
| Target outcome | motion/task success and recovery | tracking, balance, skill/task success와 recovery | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | whole-body pose/contact/reference state; body terms: physics, simulation, determines, state, transition, dynamics, while, policy, PHC, computes | p. 3 (3.1. Goal Conditioned Motion Imitation with Ad), p. 5 (3.2. Progressive Multiplicative Control Policy), p. 2 (1. Introduction) |
| Decision / output variable | joint/whole-body action; body terms: summarize, contributions, follows, Perpetual, Humanoid, Controller, successfully, imitate | p. 2 (1. Introduction), p. 5 (3.1. Goal Conditioned Motion Imitation with Ad), p. 3 (3.1. Goal Conditioned Motion Imitation with Ad) |
| Objective / loss / cost | tracking/balance/task objective; cue terms: policy, goal, maximize, discounted, reward, hPT, t-1rt, proximal | p. 4 (3.1. Goal Conditioned Motion Imitation with Ad), p. 3 (3.1. Goal Conditioned Motion Imitation with Ad), p. 4 (3.1. Goal Conditioned Motion Imitation with Ad), p. 5 (3.2. Progressive Multiplicative Control Policy) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (3.1. Goal Conditioned Motion Imitation with Ad), p. 5 (3.1. Goal Conditioned Motion Imitation with Ad), p. 5 (3.2. Progressive Multiplicative Control Policy) |
| Success / guarantee | motion/task success and recovery | p. 7 (4.1. Motion Imitation), p. 7 (4.1. Motion Imitation), p. 8 (4.2. Fail-state Recovery) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. Introduction - extractive body cue:** However, controlling high-degree-of-freedom (DOF) humanoids in simulation presents significant challenges, as they can fall, trip, or deviate from their reference motions, and struggle to recover.
- **p. 2 / 1. Introduction - extractive body cue:** However, resetting successfully requires a high-quality reference pose, which is often difficult to obtain due to the noisy nature of the pose estimates, leading to ...
- **p. 2 / 1. Introduction - extractive body cue:** Another important aspect of controlling simulated humanoids is how to handle noisy input and failure cases.

## What the Paper Changes

PDF contribution framing (p. 2 (1. Introduction), p. 5 (3.1. Goal Conditioned Motion Imitation with Ad), p. 3 (3.1. Goal Conditioned Motion Imitation with Ad), p. 4 (3.1. Goal Conditioned Motion Imitation with Ad), p. 5 (3.2. Progressive Multiplicative Control Policy)): To summarize, our contributions are as follows: (1) we propose a Perpetual Humanoid Controller that can successfully imitate 98.9% of the AMASS dataset without applying any external forces; (2) we ...

- **p. 5 / 3.1. Goal Conditioned Motion Imitation with Ad - extractive body cue:** Thus, we propose Relaxed Early Termination (RET), which allows the humanoid's ankle and toes to slightly deviate from the MoCap motion to remain balanced.
- **p. 3 / 3.1. Goal Conditioned Motion Imitation with Ad - extractive body cue:** The simulation state st ≜(sp t, sg t) consists of humanoid proprioception sp t and the goal state sg t.
- **p. 4 / 3.1. Goal Conditioned Motion Imitation with Ad - extractive body cue:** Unlike prior motion tracking policies that only use a motion imitation reward, we use the recently proposed Adversarial Motion Prior [33] and include a discriminator ...
- **p. 5 / 3.2. Progressive Multiplicative Control Policy - extractive body cue:** Thus, we propose a progressive multiplicative control policy (PMCP), which allocates new subnetworks (primitives P) to learn harder sequences.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | Although we can train single-clip controller to overfit on these sequences (see the supplement), our full controller often ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | Figure 4: (a) Imitating high-quality MoCap - spin and kick. (b) Recover from fallen state and go back ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | We uses four primitives (including failstate recovery) for all our evaluations. | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Table 4: We measure whether our controller can recover from the fail-states by generating these scenarios (dropping the ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

humanoid writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 3 (3.1. Goal Conditioned Motion Imitation with Ad), p. 5 (3.2. Progressive Multiplicative Control Policy), p. 2 (1. Introduction), p. 6 (3.2. Progressive Multiplicative Control Policy). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), interface p. 3 (3.1. Goal Conditioned Motion Imitation with Ad), p. 5 (3.2. Progressive Multiplicative Control Policy), p. 2 (1. Introduction), p. 6 (3.2. Progressive Multiplicative Control Policy), objective p. 4 (3.1. Goal Conditioned Motion Imitation with Ad), p. 3 (3.1. Goal Conditioned Motion Imitation with Ad), p. 4 (3.1. Goal Conditioned Motion Imitation with Ad), p. 5 (3.2. Progressive Multiplicative Control Policy).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
