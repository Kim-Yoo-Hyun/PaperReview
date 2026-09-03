# Walk These Ways: Tuning Robot Control for Generalization with Multiplicity of Behavior

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.mlr.press/v205/margolis23a.html.
> PDF retrieval source: https://arxiv.org/pdf/2212.03238. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2022 / CoRL
- Authors: not duplicated here when not verified in the registry source
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: NEXT
- Tags: Robotics, quadruped locomotion, Reinforcement Learning, behavior diversity
- Official paper: https://proceedings.mlr.press/v205/margolis23a.html
- Full-text retrieval: https://arxiv.org/pdf/2212.03238
- Code/Project: https://sites.google.com/view/walk-these-ways
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Locomotion, whole-body, mobile manipulation, and humanoids의 locomotion 문제를 이해하기 위해 읽는다. 본문은 The difficulty of designing a single set of auxiliary rewards that promote generalization in diverse set of downstream tasks is illustrated in the top row insets of Figure 1: each shows an ...를 문제로 두고, We present a framework for policy learning that enables improved performance in out-of-distribution scenarios under some assumptions detailed below.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Learned locomotion policies can rapidly adapt to diverse environments similar to those experienced during training but lack a mechanism for fast tuning when they fail ...
- **p. 1 / Abstract - extractive body cue:** This necessitates a slow and iterative cycle of reward and environment redesign to achieve good performance on a new task.
- **p. 1 / Abstract - extractive body cue:** As an alternative, we propose learning a single policy that encodes a structured family of locomotion strategies that solve training tasks in different ways, resulting ...
- **p. 1 / Abstract - extractive body cue:** Different strategies generalize differently and can be chosen in real-time for new tasks or environments, bypassing the need for time-consuming retraining.
- **p. 1 / Abstract - extractive body cue:** We release a fast, robust open-source MoB locomotion controller, Walk These Ways, that can execute diverse gaits with variable footswing, posture, and speed, unlocking diverse ...
- **p. 3 / 2 Background - extractive body cue:** The difficulty of designing a single set of auxiliary rewards that promote generalization in diverse set of downstream tasks is illustrated in the top row ...
- **p. 2 / 1 Introduction - extractive body cue:** However, this creates a hard learning problem due to creation of challenging or infeasible locomotion scenarios.

## Core Idea

- **p. 2 / 1 Introduction - extractive body cue:** We present a framework for policy learning that enables improved performance in out-of-distribution scenarios under some assumptions detailed below.
- **p. 2 / 1 Introduction - extractive body cue:** To facilitate generalization to diverse scenarios, we propose a technique, Multiplicity of Behavior (MoB), that given the same observation history and a small set of ...
- **p. 5 / 3 Method - extractive body cue:** The action at consists of position targets for each of the twelve joints.
- **p. 5 / 3 Method - extractive body cue:** The observation space ot consists of joint positions and velocities qt, ˙qt (measured by joint encoders) and the gravity vector in the body frame gt ...
- **p. 6 / 3 Method - extractive body cue:** Gait 0.0 m/s 1.0 m/s 2.0 m/s 3.0 m/s Trotting 9±1 24±1 53±5 98±9 Pronking 32±1 43±2 68±5 112±5 Pacing 13±3 25±2 55±3 99±6 Bounding ...
- **p. 6 / 3 Method - extractive body cue:** 4 Experimental Results 4.1 Sim-to-Real Transfer and Gait Switching We deploy the controller learned in simulation in the real world and first evaluate its performance ...
- **p. 6 / 3 Method - extractive body cue:** After training using a generic locomotion objective, one might wish to tune a controller's behavior to optimize a new metric in the original environment.
- **p. 8 / 3 Method - extractive body cue:** MoB confers a single learned policy a structured and controllable space of diverse locomotion behaviors for each state and task in the training distribution.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The input to the policy is a 30-step history of observations ot-H...t, commands ct-H...t, behaviors bt-H...t, previous actions at-H-1...t-1, and timing reference variables tt-H...t. | proprioception, terrain/perception observation과 velocity command | p. 5 (3 Method), p. 5 (3 Method) |
| State/latent | input, policy, step, history, observations, ot-H, commands, ct-H, behaviors, bt-H, previous, actions | body/contact state, foothold 또는 behavior mode | p. 5 (3 Method), p. 5 (3 Method), p. 2 (1 Introduction) |
| Output/action | Besides the above, the policy input also includes estimated domain parameters: the velocity of the robot body and the ground friction, which are predicted from the observation history using supervised learning in ... | joint target, torque, footstep 또는 locomotion action | p. 5 (3 Method), p. 2 (1 Introduction), p. 4 (3 Method) |
| Objective/outcome | This way, the agent is always rewarded for progress towards the task, more when auxiliary objectives are satisfied and less when they are not. | velocity/progress, stability, energy와 terrain generalization | p. 5 (3 Method), p. 5 (3 Method), p. 6 (3 Method) |

## Main Claims and Actual Contribution

- **p. 2 / 1 Introduction - extractive body cue:** We present a framework for policy learning that enables improved performance in out-of-distribution scenarios under some assumptions detailed below.
- **p. 2 / 1 Introduction - extractive body cue:** To facilitate generalization to diverse scenarios, we propose a technique, Multiplicity of Behavior (MoB), that given the same observation history and a small set of ...
- **p. 5 / 3 Method - extractive body cue:** The action at consists of position targets for each of the twelve joints.
- **p. 5 / 3 Method - extractive body cue:** The observation space ot consists of joint positions and velocities qt, ˙qt (measured by joint encoders) and the gravity vector in the body frame gt ...
- **p. 6 / 3 Method - extractive body cue:** Gait 0.0 m/s 1.0 m/s 2.0 m/s 3.0 m/s Trotting 9±1 24±1 53±5 98±9 Pronking 32±1 43±2 68±5 112±5 Pacing 13±3 25±2 55±3 99±6 Bounding ...
- **p. 11 / Figure/Table caption - extractive body cue:** Table 5: Removing gait constraints results in improved velocity tracking task performance on flat ground. Heat maps (right) break down the mean task reward for ...
- **p. 7 / 3 Method - extractive body cue:** Therefore, it is possible to improve performance in an out-of-distribution terrain by modulating the parameters of the MoB policy.
- **p. 7 / Figure/Table caption - extractive body cue:** Table 4: Zero-shot generalization to platform terrain (visualized right). Pacing and trotting yield the best survival time in out-of-distribution deployment, outperforming the gait-free baseline. Pronk- ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 11 (Figure/Table caption), p. 7 (3 Method) |
| Embodiment/environment | In a real-world example, the robot was able to crawl under a 22 cm bar; the robot body thickness is 13 cm, leaving 9 cm of clearance beneath the robot. | hardware/simulator version and reset protocol | p. 8 (3 Method), p. 5 (3 Method) |
| Dataset/benchmark | However, this penalizes the robot during fast turning tasks requiring relative lateral motion of the feet. | role, split, size and leakage | p. 8 (3 Method), p. 5 (3 Method), p. 5 (3 Method), p. 7 (3 Method) |
| Metric | Table 4: Zero-shot generalization to platform terrain (visualized right). Pacing and trotting yield the best survival time in out-of-distribution deployment, outperforming the gait-free baseline. Pronk- ing attains the best velocity tra ... | definition, denominator, direction and uncertainty | p. 7 (Figure/Table caption), p. 6 (Figure/Table caption), p. 5 (3 Method) |
| Baseline/ablation | Pacing and trotting yield the best survival time in out-of-distribution deployment, outperforming the gait-free baseline. | fair input/data/compute/action matching | p. 7 (3 Method), p. 6 (3 Method), p. 5 (3 Method) |

## Explicit Limitations and Failure Boundary

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: Multiplicity of Behavior (MoB) enables a human to tune a single quadruped policy trained on flat ground to diverse unseen environments. Top row: ...
- **p. 12 / Figure/Table caption - extractive body cue:** Table 5. Forward and Backward Locomotion. During evaluation in the random platforms environment, we found that walking backward leads to fewer failures than walking forward. ...
- **p. 13 / Figure/Table caption - extractive body cue:** Figure 8: Forward vs Backward Walking on Platforms. Time to failure for different gaits and velocities in the random platforms environment (zero-shot test). The temperature ...
- **p. 14 / Figure/Table caption - extractive body cue:** Figure 9: Footswing Height vs Robustness: Impact of footswing height on time to failure on the platform terrain (Section 4.2). Increased footswing height yields better ...
- **p. 7 / 3 Method - extractive body cue:** Therefore, prior works would either attempt to climb over bushes as obstacles or fall back on a robust proprioceptive controller that is unaware of the ...
- **p. 7 / 3 Method - extractive body cue:** The gait-free baseline cannot accomplish this; in the absence of such constraints during training, it will 7
- **p. 8 / 3 Method - extractive body cue:** 5 Discussion and Limitations Our experiments show that the benefits of adding MoB can come at a cost to in-distribution task performance, specifically limiting the ...

## Why Read It

Locomotion, whole-body, mobile manipulation, and humanoids의 locomotion 문제를 이해하기 위해 읽는다. 본문은 The difficulty of designing a single set of auxiliary rewards that promote generalization in diverse set of downstream tasks is illustrated in the top row insets of Figure 1: each shows an ...를 문제로 두고, We present a framework for policy learning that enables improved performance in out-of-distribution scenarios under some assumptions detailed below.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 3 (2 Background), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 5 (3 Method), p. 6 (3 Method) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (14 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** However, this creates a hard learning problem due to creation of challenging or infeasible locomotion scenarios. (p. 2, 1 Introduction).
- **Actual contribution:** We present a framework for policy learning that enables improved performance in out-of-distribution scenarios under some assumptions detailed below. (p. 2, 1 Introduction).
- **Evaluation boundary:** Table 3: Behavior tuning enables interventional studies on the relationship between gait proper- ties and performance criteria within a single policy. Here, we illustrate how power consumption varies across speeds ... (p. 6, Figure/Table caption).
- **Explicit failure boundary:** Top row: A low-frequency gait fails to sprint on slippery terrain (Gait 2; inset) but tuning it to high frequency results in success (Gait 1). (p. 1, Body text (section boundary not confidently recovered)).
