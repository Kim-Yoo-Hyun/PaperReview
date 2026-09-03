# FlowPolicy: Enabling Fast and Robust 3D Flow-Based Policy via Consistency Flow Matching for Robot Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (9 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://ojs.aaai.org/index.php/AAAI/article/view/33617.
> PDF retrieval source: https://ojs.aaai.org/index.php/AAAI/article/view/33617. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / AAAI
- Authors: not duplicated here when not verified in the registry source
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: NEXT
- Tags: Robotics, Imitation Learning, 3D point cloud, Flow Matching, diffusion policy, inference efficiency, manipulation
- Official paper: https://ojs.aaai.org/index.php/AAAI/article/view/33617
- Full-text retrieval: https://ojs.aaai.org/index.php/AAAI/article/view/33617
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (9 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Manipulation, contact, tactile, and dexterity의 manipulation 문제를 이해하기 위해 읽는다. 본문은 However, lack of a prior knowledge about u and pt, conditional flow matching (Lipman et al.를 문제로 두고, In summary, our main contributions are threefold: • We first propose a 3D flow-based policy generation framework that conditions the 3D visual representation and can generate robust robotic actions with few demonstrations, ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Robots can acquire complex manipulation skills by learning policies from expert demonstrations, which is often known as vision-based imitation learning.
- **p. 1 / Abstract - extractive body cue:** Generating policies based on diffusion and flow matching models has been shown to be effective, particularly in robotic manipulation tasks.
- **p. 1 / Abstract - extractive body cue:** However, recursion-based approaches are inference inefficient in working from noise distributions to policy distributions, posing a challenging trade-off between efficiency and quality.
- **p. 1 / Abstract - extractive body cue:** This motivates us to propose FlowPolicy, a novel framework for fast policy generation based on consistency flow matching and 3D vision.
- **p. 1 / Abstract - extractive body cue:** Our approach refines the flow dynamics by normalizing the self-consistency of the velocity field, enabling the model to derive task execution policies in a single ...
- **p. 4 / Abstract - extractive body cue:** However, lack of a prior knowledge about u and pt, conditional flow matching (Lipman et al.
- **p. 1 / Abstract - extractive body cue:** Conversely, energy-based models face challenges with training stability, primarily due to the necessity of negative sample extraction during the training process (Chi et al.

## Core Idea

- **p. 2 / Abstract - extractive body cue:** In summary, our main contributions are threefold: • We first propose a 3D flow-based policy generation framework that conditions the 3D visual representation and can ...
- **p. 3 / Abstract - extractive body cue:** To address this issue, we propose FlowPolicy, a real-time 3D policy generation framework based on consistency flow matching.
- **p. 3 / Abstract - extractive body cue:** Method Our method expects a limited number of expert demonstrations to teach an agent to learn a policy π : O =⇒A, i.e., mapping from ...
- **p. 2 / Abstract - extractive body cue:** By avoiding estimating noise and instead matching a path from the noise to the target, FM enables faster inference, which is crucial in real-time robot ...
- **p. 4 / Abstract - extractive body cue:** Learning straight-line flows enables faster inference efficiency.
- **p. 3 / Abstract - extractive body cue:** Therefore, we propose FlowPolicy, a conditional consistency flow matching model, which guarantees the generation of high-quality actions while also accomplishing one-step inference for realtime applications.
- **p. 1 / Abstract - extractive body cue:** Specifically, FlowPolicy conditions on the observed 3D point cloud, where consistency flow matching directly defines straight-line flows from different time states to the same action ...
- **p. 3 / Abstract - extractive body cue:** Expert demonstrations Policy FlowPolicy State Noise a1 a0 Action Flow Network Execute Single-view Images Robot state Encoder Sparse 3D Encoder Compact 3D Repr.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Specifically, FlowPolicy conditions on the observed 3D point cloud, where consistency flow matching directly defines straight-line flows from different time states to the same action space, while simultaneously constraining their veloci ... | RGB-D/point cloud, object state와 contact/task observation | p. 1 (Abstract), p. 3 (Abstract) |
| State/latent | Specifically, FlowPolicy, conditions, observed, point, cloud, where, consistency, flow, matching, directly, defines | object geometry, affordance, contact mode 또는 end-effector state | p. 1 (Abstract), p. 3 (Abstract), p. 5 (Abstract) |
| Output/action | Visual observations include the robot state and scene point clouds, and actions are usually sequences of trajectories of the robot to accomplish a specific task. | grasp, pose, force 또는 end-effector trajectory | p. 3 (Abstract), p. 5 (Abstract), p. 2 (Abstract) |
| Objective/outcome | We evaluate 37 tasks from Adroit and Metaworld across 3 random seeds and report the success rate (%) with standard deviation. ‘∗' indicates that the NFE of Adaflow is not fixed. simply ... | task completion, contact success, pose/force error와 generalization | p. 5 (Abstract), p. 2 (Abstract), p. 3 (Abstract) |

## Main Claims and Actual Contribution

- **p. 2 / Abstract - extractive body cue:** In summary, our main contributions are threefold: • We first propose a 3D flow-based policy generation framework that conditions the 3D visual representation and can ...
- **p. 3 / Abstract - extractive body cue:** To address this issue, we propose FlowPolicy, a real-time 3D policy generation framework based on consistency flow matching.
- **p. 3 / Abstract - extractive body cue:** Method Our method expects a limited number of expert demonstrations to teach an agent to learn a policy π : O =⇒A, i.e., mapping from ...
- **p. 2 / Abstract - extractive body cue:** By avoiding estimating noise and instead matching a path from the noise to the target, FM enables faster inference, which is crucial in real-time robot ...
- **p. 4 / Abstract - extractive body cue:** Learning straight-line flows enables faster inference efficiency.
- **p. 7 / Abstract - extractive body cue:** Both generally improve the accuracy with more demonstrations, but FlowPolicy typically has a higher success rate and avoids the performance bottleneck as presented in DP3.
- **p. 7 / Abstract - extractive body cue:** For hard-level tasks (i.e., ‘Pick-Place'), the success rate of the task can be significantly improved by increasing the number of expert presentations, as shown in ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4: Illustrations of the learning curves. Compared to Simple DP3 and DP3, FlowPolicy demonstrates higher sta- bility, learning efficiency, and success rates. all success ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SIMULATION | do not infer unreported downstream behavior | p. 7 (Abstract), p. 7 (Abstract) |
| Embodiment/environment | Experiments Dataset and Implementation Details Simulation Benchmarks We choose two preeminent environmental simulators, Adroit (Rajeswaran et al. | hardware/simulator version and reset protocol | p. 5 (Abstract), p. 5 (Abstract) |
| Dataset/benchmark | Visual observations include the robot state and scene point clouds, and actions are usually sequences of trajectories of the robot to accomplish a specific task. | role, split, size and leakage | p. 5 (Abstract), p. 5 (Abstract), p. 3 (Abstract), p. 3 (Abstract) |
| Metric | Both generally improve the accuracy with more demonstrations, but FlowPolicy typically has a higher success rate and avoids the performance bottleneck as presented in DP3. | definition, denominator, direction and uncertainty | p. 7 (Abstract), p. 5 (Abstract), p. 7 (Abstract) |
| Baseline/ablation | We also compared state-of-the-art 2D-based approaches, including diffusion policy (DP) (Chi et al. | fair input/data/compute/action matching | p. 5 (Abstract), p. 6 (Abstract), p. 6 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 6 / Abstract - extractive body cue:** Our method successfully generates high-quality actions at real-time speeds, completing these tasks effectively, whereas DP3 either produces lower-quality actions (left) or fails to complete the ...
- **p. 7 / Abstract - extractive body cue:** DP3 unsuccessfully picks up the red cube and fails the task.
- **p. 7 / Abstract - extractive body cue:** Although DP3 accomplishes the dexterity task, the diffusion policy generated based on DP3 fails to ensure consistency with the target pen in 3D space compared ...
- **p. 4 / Abstract - extractive body cue:** Due to the complexity of the target distribution solution, Consistency-FM does not regress directly on the ground truth vector field, instead, it directly defines a ...
- **p. 3 / Abstract - extractive body cue:** Expert demonstrations Policy FlowPolicy State Noise a1 a0 Action Flow Network Execute Single-view Images Robot state Encoder Sparse 3D Encoder Compact 3D Repr.
- **p. 3 / Abstract - extractive body cue:** The top section visualizes FlowPolicy, where a straight-line flow enables the fastest data transition from the noise distribution to the action distribution (Adroit: Open the ...
- **p. 4 / Abstract - extractive body cue:** The expectation is to find an ODE whose solution transmits the noise x0 ∼p0 to the data x1 ∼p1:  dξx(t) dt = νθ(t, ξx(t)) ...

## Why Read It

Manipulation, contact, tactile, and dexterity의 manipulation 문제를 이해하기 위해 읽는다. 본문은 However, lack of a prior knowledge about u and pt, conditional flow matching (Lipman et al.를 문제로 두고, In summary, our main contributions are threefold: • We first propose a 3D flow-based policy generation framework that conditions the 3D visual representation and can generate robust robotic actions with few demonstrations, ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 4 (Abstract), p. 1 (Abstract), p. 2 (Abstract), p. 2 (Abstract), p. 3 (Abstract), p. 2 (Abstract) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (9 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** However, lack of a prior knowledge about u and pt, conditional flow matching (Lipman et al. (p. 4, Abstract).
- **Actual contribution:** In summary, our main contributions are threefold: • We first propose a 3D flow-based policy generation framework that conditions the 3D visual representation and can generate robust robotic actions with ... (p. 2, Abstract).
- **Evaluation boundary:** Figure 5: Ablation on the number of expert demonstrations. We choose four typical tasks to explore the impact of dif- ferent numbers of demonstrations on FlowPolicy and DP3. Both generally ... (p. 7, Figure/Table caption).
- **Explicit failure boundary:** Our method successfully generates high-quality actions at real-time speeds, completing these tasks effectively, whereas DP3 either produces lower-quality actions (left) or fails to complete the task (right). task. (p. 6, Abstract).
