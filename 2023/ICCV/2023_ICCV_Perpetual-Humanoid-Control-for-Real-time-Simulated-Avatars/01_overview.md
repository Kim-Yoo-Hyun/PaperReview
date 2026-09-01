# Perpetual Humanoid Control for Real-time Simulated Avatars

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/ICCV2023/html/Luo_Perpetual_Humanoid_Control_for_Real-time_Simulated_Avatars_ICCV_2023_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2023/html/Luo_Perpetual_Humanoid_Control_for_Real-time_Simulated_Avatars_ICCV_2023_paper.html. Reading tracker status/evidence was not changed.

- Year/Venue: 2023 / ICCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: NEXT
- Tags: Robotics, humanoid, whole-body control, motion imitation
- Official paper: https://openaccess.thecvf.com/content/ICCV2023/html/Luo_Perpetual_Humanoid_Control_for_Real-time_Simulated_Avatars_ICCV_2023_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/ICCV2023/html/Luo_Perpetual_Humanoid_Control_for_Real-time_Simulated_Avatars_ICCV_2023_paper.html
- Code/Project: https://zhengyiluo.github.io/PHC-Site/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-02 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Locomotion, whole-body, mobile manipulation, and humanoids의 humanoid 문제를 이해하기 위해 읽는다. 본문은 These limitations prevent the widespread adoption of physics-based methods, as current control policies cannot handle noisy observations such as video or language.를 문제로 두고, To summarize, our contributions are as follows: (1) we propose a Perpetual Humanoid Controller that can successfully imitate 98.9% of the AMASS dataset without applying any external forces; (2) we propose the ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** We present a physics-based humanoid controller that achieves high-fidelity motion imitation and fault-tolerant behavior in the presence of noisy input (e.g. pose estimates from video ...
- **p. 1 / Abstract - extractive body cue:** Our controller scales up to learning ten thousand motion clips without using any external stabilizing forces and learns to naturally recover from fail-state.
- **p. 1 / Abstract - extractive body cue:** Given reference motion, our controller can perpetually control simulated avatars without requiring resets.
- **p. 1 / Abstract - extractive body cue:** At its core, we propose the progressive multiplicative control policy (PMCP), which dynamically allocates new network capacity to learn harder and harder motion sequences.
- **p. 1 / Abstract - extractive body cue:** PMCP allows efficient scaling for learning from large-scale motion databases and adding new tasks, such as fail-state recovery, without catastrophic forgetting.
- **p. 1 / 1. Introduction - extractive body cue:** These limitations prevent the widespread adoption of physics-based methods, as current control policies cannot handle noisy observations such as video or language.
- **p. 1 / 1. Introduction - extractive body cue:** However, controlling high-degree-of-freedom (DOF) humanoids in simulation presents significant challenges, as they can fall, trip, or deviate from their reference motions, and struggle to recover.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** To summarize, our contributions are as follows: (1) we propose a Perpetual Humanoid Controller that can successfully imitate 98.9% of the AMASS dataset without applying ...
- **p. 5 / 3.1. Goal Conditioned Motion Imitation with Ad - extractive body cue:** Thus, we propose Relaxed Early Termination (RET), which allows the humanoid's ankle and toes to slightly deviate from the MoCap motion to remain balanced.
- **p. 3 / 3.1. Goal Conditioned Motion Imitation with Ad - extractive body cue:** The simulation state st ≜(sp t, sg t) consists of humanoid proprioception sp t and the goal state sg t.
- **p. 4 / 3.1. Goal Conditioned Motion Imitation with Ad - extractive body cue:** Unlike prior motion tracking policies that only use a motion imitation reward, we use the recently proposed Adversarial Motion Prior [33] and include a discriminator ...
- **p. 5 / 3.2. Progressive Multiplicative Control Policy - extractive body cue:** Thus, we propose a progressive multiplicative control policy (PMCP), which allocates new subnetworks (primitives P) to learn harder sequences.
- **p. 4 / 3.1. Goal Conditioned Motion Imitation with Ad - extractive body cue:** (1) For the discriminator, we use the same observations, loss formulation, and gradient penalty as AMP [33].
- **p. 4 / 3.1. Goal Conditioned Motion Imitation with Ad - extractive body cue:** We use a proportional derivative (PD) controller at each DoF of the humanoid and the action at specifies the PD target.
- **p. 3 / 3.1. Goal Conditioned Motion Imitation with Ad - extractive body cue:** The physics simulation determines state st ∈S and transition dynamics T while our policy πPHC computes per-step action at ∈A.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The physics simulation determines state st ∈S and transition dynamics T while our policy πPHC computes per-step action at ∈A. | proprioception, reference pose/motion, visual or language command | p. 3 (3.1. Goal Conditioned Motion Imitation with Ad), p. 5 (3.2. Progressive Multiplicative Control Policy) |
| State/latent | physics, simulation, determines, state, transition, dynamics, while, policy, PHC, computes, per-step, action | whole-body pose, balance/contact state와 skill/mode | p. 3 (3.1. Goal Conditioned Motion Imitation with Ad), p. 5 (3.2. Progressive Multiplicative Control Policy), p. 2 (1. Introduction) |
| Output/action | P(F ) shares the same input and output space as P(1) · · · P(k), but since the reference motion does not provide useful information about failstate recovery (the humanoid should not ... | joint/whole-body action, motion target 또는 task trajectory | p. 5 (3.2. Progressive Multiplicative Control Policy), p. 2 (1. Introduction), p. 6 (3.2. Progressive Multiplicative Control Policy) |
| Objective/outcome | The policy's goal is to maximize the discounted reward E hPT t=1 γt-1rt i , and we use the proximal policy gradient (PPO) [35] to learn πPHC. | tracking, balance, skill/task success와 recovery | p. 3 (3.1. Goal Conditioned Motion Imitation with Ad), p. 4 (3.1. Goal Conditioned Motion Imitation with Ad), p. 4 (3.1. Goal Conditioned Motion Imitation with Ad) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** To summarize, our contributions are as follows: (1) we propose a Perpetual Humanoid Controller that can successfully imitate 98.9% of the AMASS dataset without applying ...
- **p. 5 / 3.1. Goal Conditioned Motion Imitation with Ad - extractive body cue:** Thus, we propose Relaxed Early Termination (RET), which allows the humanoid's ankle and toes to slightly deviate from the MoCap motion to remain balanced.
- **p. 3 / 3.1. Goal Conditioned Motion Imitation with Ad - extractive body cue:** The simulation state st ≜(sp t, sg t) consists of humanoid proprioception sp t and the goal state sg t.
- **p. 4 / 3.1. Goal Conditioned Motion Imitation with Ad - extractive body cue:** Unlike prior motion tracking policies that only use a motion imitation reward, we use the recently proposed Adversarial Motion Prior [33] and include a discriminator ...
- **p. 5 / 3.2. Progressive Multiplicative Control Policy - extractive body cue:** Thus, we propose a progressive multiplicative control policy (PMCP), which allocates new subnetworks (primitives P) to learn harder sequences.
- **p. 8 / 4.1. Motion Imitation - extractive body cue:** H36M-Test-Video* RET MCP PNN Rotation Fail-Recover Succ ↑ Eg-mpjpe ↓ Empjpe ↓ ✗ ✗ ✗ ✓ ✗ 51.2% 56.2 34.4 ✓ ✗ ✗ ✓ ✗ ...
- **p. 7 / 4.1. Motion Imitation - extractive body cue:** Similar to results on MoCap Imitation, PHC outperforms the baselines 10901
- **p. 7 / 4.1. Motion Imitation - extractive body cue:** On testing, PHC shows a high success rate on unseen MoCap sequences from both the AMASS and H36M data.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | SYSTEM / EVALUATION SCOPE UNRESOLVED | do not infer unreported downstream behavior | p. 8 (4.1. Motion Imitation), p. 7 (4.1. Motion Imitation) |
| Embodiment/environment | PHC is trained on the training split of the AMASS [23] dataset. | hardware/simulator version and reset protocol | p. 7 (4. Experiments), p. 7 (4.1. Motion Imitation) |
| Dataset/benchmark | Fig.4 shows a qualitative result on a live demonstration of using poses estimated from an office environment. | role, split, size and leakage | p. 7 (4. Experiments), p. 7 (4.1. Motion Imitation), p. 8 (4.1. Motion Imitation), p. 8 (4.1. Motion Imitation) |
| Metric | On testing, PHC shows a high success rate on unseen MoCap sequences from both the AMASS and H36M data. | definition, denominator, direction and uncertainty | p. 7 (4.1. Motion Imitation), p. 7 (4.1. Motion Imitation), p. 8 (4.2. Fail-state Recovery) |
| Baseline/ablation | Similar to results on MoCap Imitation, PHC outperforms the baselines 10901 | fair input/data/compute/action matching | p. 7 (4.1. Motion Imitation), p. 7 (4.1. Motion Imitation), p. 8 (4.1. Motion Imitation) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 5. Discussions - extractive body cue:** Although we can train single-clip controller to overfit on these sequences (see the supplement), our full controller often fails to learn these sequences.
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4: (a) Imitating high-quality MoCap - spin and kick. (b) Recover from fallen state and go back to reference motion (indicated by red dots). ...
- **p. 7 / 4. Experiments - extractive body cue:** We uses four primitives (including failstate recovery) for all our evaluations.
- **p. 8 / Figure/Table caption - extractive body cue:** Table 4: We measure whether our controller can recover from the fail-states by generating these scenarios (dropping the humanoid on the ground & far from ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: We propose a motion imitator that can naturally recover from falls and walk to far-away reference motion, perpetually controlling simulated avatars without requiring ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: Our progressive training procedure to train primitives P(1), P(2), · · · , P(K) by gradually learning harder and harder sequences. Fail recovery ...
- **p. 6 / 4. Experiments - extractive body cue:** In Sec.4.2, we test our controller's ability to recovery from fail-state.

## Why Read It

Locomotion, whole-body, mobile manipulation, and humanoids의 humanoid 문제를 이해하기 위해 읽는다. 본문은 These limitations prevent the widespread adoption of physics-based methods, as current control policies cannot handle noisy observations such as video or language.를 문제로 두고, To summarize, our contributions are as follows: (1) we propose a Perpetual Humanoid Controller that can successfully imitate 98.9% of the AMASS dataset without applying any external forces; (2) we propose the ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (3.1. Goal Conditioned Motion Imitation with Ad), p. 4 (3.1. Goal Conditioned Motion Imitation with Ad) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
