# DeXtreme: Transfer of Agile In-hand Manipulation from Simulation to Reality

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (28 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://research.nvidia.com/publication/2023-06_dextreme-transfer-agile-hand-manipulation-simulation-reality.
> PDF retrieval source: https://research.nvidia.com/publication/2023-06_dextreme-transfer-agile-hand-manipulation-simulation-reality. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2023 / ICRA
- Authors: not duplicated here when not verified in the registry source
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: NEXT
- Tags: Robotics, dexterous manipulation, sim-to-real, Reinforcement Learning, NVIDIA
- Official paper: https://research.nvidia.com/publication/2023-06_dextreme-transfer-agile-hand-manipulation-simulation-reality
- Full-text retrieval: https://research.nvidia.com/publication/2023-06_dextreme-transfer-agile-hand-manipulation-simulation-reality
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (28 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Manipulation, contact, tactile, and dexterity의 manipulation 문제를 이해하기 위해 읽는다. 본문은 However, due to the complexity of their training architecture, and the sui generis nature of their work on sim-to-real transfer, reproducing and building upon their success has proven to be a challenge ...를 문제로 두고, 2.1 Task We propose a method for performing object reorientation on an anthropomorphic hand.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Recent work has demonstrated the ability of deep reinforcement learning (RL) algorithms to learn complex robotic behaviours in simulation, including in the domain of multi-fingered ...
- **p. 1 / Abstract - extractive body cue:** However, such models can be challenging to transfer to the real world due to the gap between simulation and reality.
- **p. 1 / Abstract - extractive body cue:** In this paper, we present our techniques to train a) a policy that can perform robust dexterous manipulation on an anthropomorphic robot hand and b) ...
- **p. 1 / Abstract - extractive body cue:** Our policies are trained to adapt to a wide range of conditions in simulation.
- **p. 1 / Abstract - extractive body cue:** Consequently, our vision-based policies significantly outperform the best vision policies in the literature on the same reorientation task and are competitive with policies that are ...
- **p. 3 / 1 Introduction - extractive body cue:** However, due to the complexity of their training architecture, and the sui generis nature of their work on sim-to-real transfer, reproducing and building upon their ...
- **p. 3 / 1 Introduction - extractive body cue:** While the NLP and computer vision communities have reproduced and extended the successes of large-scale models like GPT-3 [3] and DALL-E [4, 5] respectively, similar ...

## Core Idea

- **p. 3 / 2 Method - extractive body cue:** 2.1 Task We propose a method for performing object reorientation on an anthropomorphic hand.
- **p. 4 / 2 Method - extractive body cue:** 2.2 Hardware Our hardware setup (see Fig 2) consists of an Allegro Hand rigidly mounted at the wrist.
- **p. 7 / 2 Method - extractive body cue:** To help overcome this, we introduce various kinds of randomisations [15] into the simulated environment as listed in Table 3.
- **p. 2 / 1 Introduction - extractive body cue:** Multi-fingered robotic hands offer an exciting platform to develop and enable human-level dexterity.
- **p. 3 / 1 Introduction - extractive body cue:** We seek to provide a much broader segment of the research community with access to a novel state-of-the-art in-hand manipulation system in hopes of catalyzing ...
- **p. 4 / 2 Method - extractive body cue:** We use Proximal Policy Optimisation (PPO) [9] to learn a parametric stochastic policy πθ (actor), mapping from observations o ∈O to actions a ∈A.
- **p. 10 / 2 Method - extractive body cue:** To account for unmodelled dynamics, we use a Random Network Adversary (RNA, see below).
- **p. 6 / 2 Method - extractive body cue:** Input Dimensionality Actor Critic Object position with noise 3D ✓ ✓ Object orientation with noise 4D (quaternion) ✓ ✓ Target position 3D ✓ ✓ Target ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Input Dimensionality Actor Critic Object position with noise 3D ✓ ✓ Object orientation with noise 4D (quaternion) ✓ ✓ Target position 3D ✓ ✓ Target orientation 4D (quaternion) ✓ ✓ Relative target ... | RGB-D/point cloud, object state와 contact/task observation | p. 6 (2 Method), p. 4 (2 Method) |
| State/latent | Input, Dimensionality, Actor, Critic, Object, position, noise, orientation, quaternion, Target, Relative, Last | object geometry, affordance, contact mode 또는 end-effector state | p. 6 (2 Method), p. 4 (2 Method), p. 6 (2 Method) |
| Output/action | We use Proximal Policy Optimisation (PPO) [9] to learn a parametric stochastic policy πθ (actor), mapping from observations o ∈O to actions a ∈A. | grasp, pose, force 또는 end-effector trajectory | p. 4 (2 Method), p. 6 (2 Method), p. 10 (2 Method) |
| Objective/outcome | 2.3 Policy Learning with RL RL Formulation: The task of manipulating the cube to the desired orientation is modelled as a sequential decision making problem where the agent interacts with the environment ... | task completion, contact success, pose/force error와 generalization | p. 4 (2 Method), p. 6 (2 Method), p. 16 (Method) |

## Main Claims and Actual Contribution

- **p. 3 / 2 Method - extractive body cue:** 2.1 Task We propose a method for performing object reorientation on an anthropomorphic hand.
- **p. 4 / 2 Method - extractive body cue:** 2.2 Hardware Our hardware setup (see Fig 2) consists of an Allegro Hand rigidly mounted at the wrist.
- **p. 7 / 2 Method - extractive body cue:** To help overcome this, we introduce various kinds of randomisations [15] into the simulated environment as listed in Table 3.
- **p. 2 / 1 Introduction - extractive body cue:** Multi-fingered robotic hands offer an exciting platform to develop and enable human-level dexterity.
- **p. 3 / 1 Introduction - extractive body cue:** We seek to provide a much broader segment of the research community with access to a novel state-of-the-art in-hand manipulation system in hopes of catalyzing ...
- **p. 14 / 3 Results - extractive body cue:** We demonstrate performance which significantly improves upon the best vision policies 8Although [8] focused on the Rubik's cube, they also trained for block reorientation (pp.
- **p. 14 / 3 Results - extractive body cue:** We note that due to differences in physics engines and hand morphology, our simulation average consecutive successes are not directly comparable, but we achieve performance ...
- **p. 13 / 3 Results - extractive body cue:** In the following section, we present the results we achieved in object reorientation in the simulations and then real world using the methods described in ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 14 (3 Results), p. 14 (3 Results) |
| Embodiment/environment | We believe such inter-day variations are important to benchmark in robotics [20] and have endeavoured to highlight this specifically in this challenging task. | hardware/simulator version and reset protocol | p. 14 (3 Results), p. 13 (Experiment) |
| Dataset/benchmark | Translation Error X Y Z Sim 5.3±0.11◦ 1.9±0.1 mm 4.1±0.2 mm 6.9±0.4 mm Table 6: Rotation and translation error on test dataset with 90% confidence intervals. | role, split, size and leakage | p. 14 (3 Results), p. 13 (Experiment), p. 13 (Experiment), p. 14 (3 Results) |
| Metric | This also lets us separate the drop in performance due to LSTM instability from pose estimation errors in the real world. | definition, denominator, direction and uncertainty | p. 15 (3 Results), p. 13 (Figure/Table caption), p. 15 (3 Results) |
| Baseline/ablation | Table 11: Our hardware setup compared against the one used in OpenAI et al. [1] and OpenAI et al. [8]. Note that the experiment pertaining to the block reorientation in [8] was ... | fair input/data/compute/action matching | p. 25 (Figure/Table caption), p. 13 (Experiment), p. 15 (3 Results) |

## Explicit Limitations and Failure Boundary

- **p. 8 / Figure/Table caption - extractive body cue:** Figure 4: Parameter range adjustments, pi_lo and pi_hi, with ADR based on the performance of policy at the boundaries Qi_lo and Qi_hi with respect to ...
- **p. 18 / 4 Related work - extractive body cue:** However, these often fail to reproduce the agile dexterity present in human hands, as the limitations of such a sequential approach to control place corresponding ...
- **p. 17 / 4 Related work - extractive body cue:** These approaches work well while an object maintains no-slip 10While extrinsics change with different camera configurations, the intrinsics remain the same.
- **p. 18 / 4 Related work - extractive body cue:** 5 Limitations Despite our best efforts, the gap between simulations and the real world is still noticeable.
- **p. 17 / Method - extractive body cue:** We suspect that this is because, despite the extreme levels of randomisation we do, there is a "null space" of possible policies which perform similarly ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: The hardware setup used in this work, unlike [1], is not housed in a cage, and our system is robust enough to perform ...
- **p. 11 / Figure/Table caption - extractive body cue:** Figure 5: The functioning of the Random Network Adversary Then each step we sample a variable m ∼Bern(·; p), and the cube pose becomes: pose_obs ...

## Why Read It

Manipulation, contact, tactile, and dexterity의 manipulation 문제를 이해하기 위해 읽는다. 본문은 However, due to the complexity of their training architecture, and the sui generis nature of their work on sim-to-real transfer, reproducing and building upon their success has proven to be a challenge ...를 문제로 두고, 2.1 Task We propose a method for performing object reorientation on an anthropomorphic hand.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 3 (1 Introduction), p. 3 (1 Introduction), p. 4 (2 Method), p. 10 (2 Method), p. 6 (2 Method), p. 17 (Method) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (28 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** However, due to the complexity of their training architecture, and the sui generis nature of their work on sim-to-real transfer, reproducing and building upon their success has proven to be ... (p. 3, 1 Introduction).
- **Actual contribution:** 2.1 Task We propose a method for performing object reorientation on an anthropomorphic hand. (p. 3, 2 Method).
- **Evaluation boundary:** Table 7: The results of running different models on the real robot. We run 10 trials per policy [1] to benchmark the average consecutive successes. Individual rows within each experiment ... (p. 14, Figure/Table caption).
- **Explicit failure boundary:** However, we did not observe this as a significant limitation for our experiments, and our policies nevertheless achieved rollouts with high consecutive successes in the real world. (p. 10, 2 Method).
