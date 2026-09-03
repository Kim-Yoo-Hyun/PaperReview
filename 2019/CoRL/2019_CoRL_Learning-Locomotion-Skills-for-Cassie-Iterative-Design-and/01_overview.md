# Learning Locomotion Skills for Cassie: Iterative Design and Sim-to-Real

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=0.875); canonical paper source: https://www.cs.ubc.ca/~van/papers/2019-CORL-cassie/index.html.
> PDF retrieval source: https://arxiv.org/pdf/1903.09537. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2019 / CoRL
- Authors: not duplicated here when not verified in the registry source
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: REFERENCE
- Tags: Robotics, bipedal locomotion, Reinforcement Learning, sim-to-real, Cassie
- Official paper: https://www.cs.ubc.ca/~van/papers/2019-CORL-cassie/index.html
- Full-text retrieval: https://arxiv.org/pdf/1903.09537
- Code/Project: https://www.cs.ubc.ca/~van/papers/2019-CORL-cassie/index.html
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=0.875)

## Why This Paper Is Here

Locomotion, whole-body, mobile manipulation, and humanoids의 locomotion 문제를 이해하기 위해 읽는다. 본문은 However, these systems are relatively stable in comparison to human-scale bipeds, for which convincing demonstrations of DRL methods to dynamic locomotion on real hardware are still lacking, to the best of our ...를 문제로 두고, In this section, we present our method for collecting stateaction pairs as a dataset for imitation learning, and how this dataset can be used to combine imitation learning and reinforcement learning.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Deep reinforcement learning (DRL) is a promising approach for developing legged locomotion skills.
- **p. 1 / Abstract - extractive body cue:** However, the iterative design process that is inevitable in practice is poorly supported by the default methodology.
- **p. 1 / Abstract - extractive body cue:** It is difficult to predict the outcomes of changes made to the reward functions, policy architectures, and the set of tasks being trained on.
- **p. 1 / Abstract - extractive body cue:** In this paper, we propose a practical method that allows the reward function to be fully redefined on each successive design iteration while limiting the ...
- **p. 1 / Abstract - extractive body cue:** We characterize policies via sets of Deterministic Action Stochastic State (DASS) tuples, which represent the deterministic policy state-action pairs as sampled from the states visited ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** However, these systems are relatively stable in comparison to human-scale bipeds, for which convincing demonstrations of DRL methods to dynamic locomotion on real hardware are ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** This offers a strong alternative to "fine-tuning" approaches, where an existing policy may be adapted via small changes and additions to an existing reward function, ...

## Core Idea

- **p. 3 / IV. METHODS - extractive body cue:** In this section, we present our method for collecting stateaction pairs as a dataset for imitation learning, and how this dataset can be used to ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** To summarize, this paper makes the following contributions: • We present a simple-yet-effective technique to reconstruct policies from only a small number of samples, and ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this paper, we propose a DRL design process that reflects and supports the iterative nature of control policy design.
- **p. 5 / VI. POLICY COMPRESSION AND DISTILLATION - extractive body cue:** In this section, we present results for using DASS to compress and distill multiple policies.
- **p. 3 / IV. METHODS - extractive body cue:** For policies such as walking that produce a limit cycle trajectory, recording the actions of Algorithm 1 DASS 1: Initialize D = {} 2: Reset ...
- **p. 3 / IV. METHODS - extractive body cue:** 2: A walking policy produces a limit cycle, represented by the blue closed curve, and the green arrows indicate the required feedback to return to ...
- **p. 4 / IV. METHODS - extractive body cue:** At each iteration, we will estimate ∇θtJrl using the usual policy gradient algorithm, and update θ according to θt+1 = θt + α(∇θtJrl -w∇θtJsp).
- **p. 4 / IV. METHODS - extractive body cue:** Finally, we can design rewards so that the new policy satisfies additional specific objectives that we desire, such as smoother movement or lifting the feet ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | 2, where the blue curves represent the limit cycle produced by a deterministic policy, and the green arrows represent the deterministic feedback actions associated with the additional states resulting from the execution ... | proprioception, terrain/perception observation과 velocity command | p. 3 (IV. METHODS), p. 3 (IV. METHODS) |
| State/latent | where, blue, curves, represent, limit, cycle, produced, deterministic, policy, green, arrows, feedback | body/contact state, foothold 또는 behavior mode | p. 3 (IV. METHODS), p. 3 (IV. METHODS), p. 2 (III. PRELIMINARIES) |
| Output/action | 2: A walking policy produces a limit cycle, represented by the blue closed curve, and the green arrows indicate the required feedback to return to the limit cycle. an expert with no ... | joint target, torque, footstep 또는 locomotion action | p. 3 (IV. METHODS), p. 2 (III. PRELIMINARIES), p. 2 (III. PRELIMINARIES) |
| Objective/outcome | Data Collection If we assume πe(. / s) and πθ(. / s) are Gaussian distributions with the same covariance, minimizing the imitation objective function (1) is equivalent to minimizing J(θ) = Es∼pe(s)[(me(s) ... | velocity/progress, stability, energy와 terrain generalization | p. 3 (IV. METHODS), p. 4 (IV. METHODS), p. 4 (IV. METHODS) |

## Main Claims and Actual Contribution

- **p. 3 / IV. METHODS - extractive body cue:** In this section, we present our method for collecting stateaction pairs as a dataset for imitation learning, and how this dataset can be used to ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** To summarize, this paper makes the following contributions: • We present a simple-yet-effective technique to reconstruct policies from only a small number of samples, and ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this paper, we propose a DRL design process that reflects and supports the iterative nature of control policy design.
- **p. 5 / VI. POLICY COMPRESSION AND DISTILLATION - extractive body cue:** In this section, we present results for using DASS to compress and distill multiple policies.
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: Cassie walking on a treadmill with a neural network policy. gradient updates that combine the supervised learning samples and conventional DRL policy-gradient samples, ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 5: Network sizes impact the final result for reinforce- ment learning. We observe that larger network sizes typically learn faster and yield more stable ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 7: Comparison of the norm of the angular velocity of the pelvis before and after optimization. We extend this iterative-improvement approach to an tracking-based ...
- **p. 5 / V. EXPERIMENTAL SETUP - extractive body cue:** Several intermediate policies are also successfully tested on the robot, but are not shown due to videoduration constraints.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 1 (Figure/Table caption), p. 6 (Figure/Table caption) |
| Embodiment/environment | Rapid deployment and testing is aided by the simulator using the same network-based interface as the physical robot, which means that tests can be moved from simulation to hardware by copying files ... | hardware/simulator version and reset protocol | p. 5 (V. EXPERIMENTAL SETUP), p. 5 (V. EXPERIMENTAL SETUP) |
| Dataset/benchmark | The simulator includes a detailed model of the robot's rigid-bodydynamics, including the reflected inertia of the robot's motors, as well as empirically measured noise and delay for the robot's sensors and actuators. | role, split, size and leakage | p. 5 (V. EXPERIMENTAL SETUP), p. 5 (V. EXPERIMENTAL SETUP), p. 4 (V. EXPERIMENTAL SETUP), p. 4 (V. EXPERIMENTAL SETUP) |
| Metric | Training Framework We adopt the framework used in [41] for training several initial policies πe, where we reward the agent for producing motion that approximately reproduces a set of specified reference motions. | definition, denominator, direction and uncertainty | p. 4 (V. EXPERIMENTAL SETUP), p. 5 (V. EXPERIMENTAL SETUP), p. 5 (V. EXPERIMENTAL SETUP) |
| Baseline/ablation | Fig. 5: Network sizes impact the final result for reinforce- ment learning. We observe that larger network sizes typically learn faster and yield more stable policies. Compared to the (256, 256) network, ... | fair input/data/compute/action matching | p. 6 (Figure/Table caption), p. 7 (Figure/Table caption), p. 5 (V. EXPERIMENTAL SETUP) |

## Explicit Limitations and Failure Boundary

- **p. 8 / VIII. CONCLUSION AND DISCUSSION - extractive body cue:** The final policies obtained are robust to unmodeled noise and enable us to transfer them from simulation to the physical robot without difficulty.
- **p. 8 / VIII. CONCLUSION AND DISCUSSION - extractive body cue:** We hypothesize the robustness stems from learning stochastic policies that operate at a low control rate, allowing the final policies to adapt to other noise.
- **p. 5 / V. EXPERIMENTAL SETUP - extractive body cue:** [25], where each rollout is started from some states sampled from the reference motions and is terminated when the height of the pelvis is less ...
- **p. 4 / V. EXPERIMENTAL SETUP - extractive body cue:** A benefit of the fixed covariance is that because of the noise constantly injected into the system during training, the resulting policy will adapt itself ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 5: Network sizes impact the final result for reinforce- ment learning. We observe that larger network sizes typically learn faster and yield more stable ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2: A walking policy produces a limit cycle, represented by the blue closed curve, and the green arrows indicate the required feedback to return ...
- **p. 4 / V. EXPERIMENTAL SETUP - extractive body cue:** We use the commonlyadopted Gaussian Policy as output, where the neural network will output the mean of the policy and Gaussian noise is injected on ...

## Why Read It

Locomotion, whole-body, mobile manipulation, and humanoids의 locomotion 문제를 이해하기 위해 읽는다. 본문은 However, these systems are relatively stable in comparison to human-scale bipeds, for which convincing demonstrations of DRL methods to dynamic locomotion on real hardware are still lacking, to the best of our ...를 문제로 두고, In this section, we present our method for collecting stateaction pairs as a dataset for imitation learning, and how this dataset can be used to combine imitation learning and reinforcement learning.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (III. PRELIMINARIES), p. 2 (III. PRELIMINARIES), p. 3 (III. PRELIMINARIES), p. 3 (IV. METHODS) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
