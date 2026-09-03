# RMA: Rapid Motor Adaptation for Legged Robots

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2107.04034.
> PDF retrieval source: https://arxiv.org/pdf/2107.04034. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2021 / RSS
- Authors: not duplicated here when not verified in the registry source
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: CORE
- Tags: Robotics, locomotion, sim-to-real, online adaptation
- Official paper: https://arxiv.org/abs/2107.04034
- Full-text retrieval: https://arxiv.org/pdf/2107.04034
- Code/Project: https://ashish-kmr.github.io/rma-legged-robots/
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Locomotion, whole-body, mobile manipulation, and humanoids의 locomotion 문제를 이해하기 위해 읽는다. 본문은 This transfer has proven quite challenging, because the sim-to-real gap itself is the result of multiple factors: (a) the physical robot and its model in the simulator differ significantly; (b) realworld terrains ...를 문제로 두고, The combination of these components enables the robot to adapt to novel situations in fractions of a second.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Successful real-world deployment of legged robots would require them to adapt in real-time to unseen scenarios like changing terrains, changing payloads, wear and tear.
- **p. 1 / Abstract - extractive body cue:** This paper presents Rapid Motor Adaptation (RMA) algorithm to solve this problem of real-time online adaptation in quadruped robots.
- **p. 1 / Abstract - extractive body cue:** RMA consists of two components: a base policy and an adaptation module.
- **p. 1 / Abstract - extractive body cue:** The combination of these components enables the robot to adapt to novel situations in fractions of a second.
- **p. 1 / Abstract - extractive body cue:** RMA is trained completely in simulation without using any domain knowledge like reference trajectories or predefined foot trajectory generators and is deployed on the A1 ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** This transfer has proven quite challenging, because the sim-to-real gap itself is the result of multiple factors: (a) the physical robot and its model in ...

## Core Idea

- **p. 1 / Abstract - extractive body cue:** The combination of these components enables the robot to adapt to novel situations in fractions of a second.
- **p. 1 / Abstract - extractive body cue:** RMA consists of two components: a base policy and an adaptation module.
- **p. 2 / 10 Hz - extractive body cue:** If we introduce the quadruped onto a rocky surface with no prior experience, the robot policy would fail often, causing serious damage to the robot.
- **p. 3 / 10 Hz - extractive body cue:** But the truly novel contribution of this paper is the adaptation module, trained in simulation, which makes RMA possible.
- **p. 3 / 10 Hz - extractive body cue:** Our novel aspects are the use of a varied terrain generator and "natural" reward functions motivated by bioenergetics which allows us to learn walking policies ...
- **p. 2 / 10 Hz - extractive body cue:** In the first phase, the base policy π takes as input the current state xt, previous action at-1 and the privileged environmental factors et which ...
- **p. 2 / 10 Hz - extractive body cue:** The environment configuration vector et is first encoded into a latent feature space zt using an encoder network µ.
- **p. 1 / I. INTRODUCTION - extractive body cue:** This transfer has proven quite challenging, because the sim-to-real gap itself is the result of multiple factors: (a) the physical robot and its model in ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | In the first phase, the base policy π takes as input the current state xt, previous action at-1 and the privileged environmental factors et which is encoded into the latent extrinsics vector ... | proprioception, terrain/perception observation과 velocity command | p. 2 (10 Hz), p. 5 (B. Adaptation Module) |
| State/latent | first, phase, base, policy, takes, input, current, state, previous, action, at-1, privileged | body/contact state, foothold 또는 behavior mode | p. 2 (10 Hz), p. 5 (B. Adaptation Module), p. 2 (10 Hz) |
| Output/action | Alternately, we could have trained a base policy which directly takes the state and action history as input without decoupling them into the two modules. | joint target, torque, footstep 또는 locomotion action | p. 5 (B. Adaptation Module), p. 2 (10 Hz), p. 5 (B. Adaptation Module) |
| Objective/outcome | First, the reward function is motivated from bioenergetic constraints of minimizing work and ground impact [42]. | velocity/progress, stability, energy와 terrain generalization | p. 4 (III. RAPID MOTOR ADAPTATION), p. 4 (III. RAPID MOTOR ADAPTATION), p. 1 (Abstract) |

## Main Claims and Actual Contribution

- **p. 1 / Abstract - extractive body cue:** The combination of these components enables the robot to adapt to novel situations in fractions of a second.
- **p. 1 / Abstract - extractive body cue:** RMA consists of two components: a base policy and an adaptation module.
- **p. 2 / 10 Hz - extractive body cue:** If we introduce the quadruped onto a rocky surface with no prior experience, the robot policy would fail often, causing serious damage to the robot.
- **p. 3 / 10 Hz - extractive body cue:** But the truly novel contribution of this paper is the adaptation module, trained in simulation, which makes RMA possible.
- **p. 3 / 10 Hz - extractive body cue:** Our novel aspects are the use of a varied terrain generator and "natural" reward functions motivated by bioenergetics which allows us to learn walking policies ...
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: We demonstrate the performance of RMA on several challenging environments. The robot is successfully able to walk on sand, mud, hiking trails, tall ...
- **p. 6 / IV. EXPERIMENTAL SETUP - extractive body cue:** We find that RMA steps down a height of 15cm with 80% success rate and walks over unseen deformable surfaces, such as a memory foam ...
- **p. 6 / IV. EXPERIMENTAL SETUP - extractive body cue:** It is also able to successfully climb inclines and steps.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 1 (Figure/Table caption), p. 6 (IV. EXPERIMENTAL SETUP) |
| Embodiment/environment | Environment Details Hardware Details: We use A1 robot from Unitree for all our real-world experiments. | hardware/simulator version and reset protocol | p. 5 (IV. EXPERIMENTAL SETUP), p. 5 (IV. EXPERIMENTAL SETUP) |
| Dataset/benchmark | For reference, A1 robot weights 12Kg. | role, split, size and leakage | p. 5 (IV. EXPERIMENTAL SETUP), p. 5 (IV. EXPERIMENTAL SETUP), p. 6 (IV. EXPERIMENTAL SETUP), p. 6 (IV. EXPERIMENTAL SETUP) |
| Metric | Fig. 1: We demonstrate the performance of RMA on several challenging environments. The robot is successfully able to walk on sand, mud, hiking trails, tall grass and dirt pile without a single ... | definition, denominator, direction and uncertainty | p. 1 (Figure/Table caption), p. 6 (IV. EXPERIMENTAL SETUP), p. 6 (IV. EXPERIMENTAL SETUP) |
| Baseline/ablation | Overall, the proposed method consistently dominates the baseline methods. | fair input/data/compute/action matching | p. 6 (IV. EXPERIMENTAL SETUP), p. 7 (V. RESULTS AND ANALYSIS), p. 6 (IV. EXPERIMENTAL SETUP) |

## Explicit Limitations and Failure Boundary

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: We demonstrate the performance of RMA on several challenging environments. The robot is successfully able to walk on sand, mud, hiking trails, tall ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 3: We evaluate RMA in several out-of-distribution setups in the real world. We compare RMA to A1's controller and RMA without the adaptation module. ...
- **p. 8 / 6) Advantage Weighted Regression for Domain Adaptation - extractive body cue:** The controller was destabilized by unstable footholds in most of its failures.
- **p. 8 / 6) Advantage Weighted Regression for Domain Adaptation - extractive body cue:** Each trial of StepUp-n and StepDown-n is terminated after a success or a failure.
- **p. 7 / IV. EXPERIMENTAL SETUP - extractive body cue:** When the robot enters the slippery patch we see a change in the two components of the extrinsics vector ˆz, indicating that the slip event ...
- **p. 7 / IV. EXPERIMENTAL SETUP - extractive body cue:** Note that post adaptation, the recovered gait time period is similar to the original, the torque magnitudes have increased and ˆz continues to capture the ...
- **p. 6 / IV. EXPERIMENTAL SETUP - extractive body cue:** This ensures that the controller does not critically depend on a fast and accurate sensing of the local terrain, and allows the base policy to ...

## Why Read It

Locomotion, whole-body, mobile manipulation, and humanoids의 locomotion 문제를 이해하기 위해 읽는다. 본문은 This transfer has proven quite challenging, because the sim-to-real gap itself is the result of multiple factors: (a) the physical robot and its model in the simulator differ significantly; (b) realworld terrains ...를 문제로 두고, The combination of these components enables the robot to adapt to novel situations in fractions of a second.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (I. INTRODUCTION), p. 2 (10 Hz), p. 2 (10 Hz), p. 1 (Abstract), p. 4 (III. RAPID MOTOR ADAPTATION), p. 5 (B. Adaptation Module) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (15 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** This transfer has proven quite challenging, because the sim-to-real gap itself is the result of multiple factors: (a) the physical robot and its model in the simulator differ significantly; (b) ... (p. 1, I. INTRODUCTION).
- **Actual contribution:** The combination of these components enables the robot to adapt to novel situations in fractions of a second. (p. 1, Abstract).
- **Evaluation boundary:** Fig. 1: We demonstrate the performance of RMA on several challenging environments. The robot is successfully able to walk on sand, mud, hiking trails, tall grass and dirt pile without ... (p. 1, Figure/Table caption).
- **Explicit failure boundary:** RMA w/o adaptation fails to move for payloads more than 8Kg, but rarely falls. (p. 6, IV. EXPERIMENTAL SETUP).
