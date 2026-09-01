# MP1: MeanFlow Tames Policy Learning in 1-step for Robotic Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://ojs.aaai.org/index.php/AAAI/article/view/38919.
> PDF retrieval source: https://ojs.aaai.org/index.php/AAAI/article/view/38919. Reading tracker status/evidence was not changed.

- Year/Venue: 2026 / AAAI
- Authors: not duplicated here when not verified in the registry source
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: Robotics, Imitation Learning, 3D point cloud, Flow Matching, action policy, inference efficiency, real-world manipulation
- Official paper: https://ojs.aaai.org/index.php/AAAI/article/view/38919
- Full-text retrieval: https://ojs.aaai.org/index.php/AAAI/article/view/38919
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-02 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

RL, IL, offline learning, and robot data의 il 문제를 이해하기 위해 읽는다. 본문은 However, diffusion still faces challenges related to inference time.를 문제로 두고, Our contributions are as follows: • We introduce MP1, the first MeanFlow-based robot learning framework.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** In robot manipulation, robot learning has become a prevailing approach.
- **p. 1 / Abstract - extractive body cue:** However, generative models within this field face a fundamental trade-off between the slow, iterative sampling of diffusion models and the architectural constraints of faster Flow-based ...
- **p. 1 / Abstract - extractive body cue:** To address these limitations, we introduce MP1, which pairs 3D point-cloud inputs with the MeanFlow paradigm to generate action trajectories in one network function evaluation ...
- **p. 1 / Abstract - extractive body cue:** By directly learning the interval-averaged velocity via the "MeanFlow Identity", our policy avoids any additional consistency constraints.
- **p. 1 / Abstract - extractive body cue:** This formulation eliminates numerical ODE-solver errors during inference, yielding more precise trajectories.
- **p. 2 / Abstract - extractive body cue:** However, diffusion still faces challenges related to inference time.
- **p. 2 / Abstract - extractive body cue:** However, 2D inputs often lack depth information, which limits the accuracy in completing tasks.

## Core Idea

- **p. 2 / Abstract - extractive body cue:** Our contributions are as follows: • We introduce MP1, the first MeanFlow-based robot learning framework.
- **p. 1 / Abstract - extractive body cue:** We validate our method on the Adroit and Meta-World benchmarks, as well as in real-world scenarios.
- **p. 1 / Abstract - extractive body cue:** To address these limitations, we introduce MP1, which pairs 3D point-cloud inputs with the MeanFlow paradigm to generate action trajectories in one network function evaluation ...
- **p. 2 / Abstract - extractive body cue:** We present the first adaptation of the MeanFlow (Geng et al.
- **p. 3 / Abstract - extractive body cue:** To address these challenges, we propose the MP1 (Fig.
- **p. 1 / Abstract - extractive body cue:** Because subtle scene-context variations are critical for robot learning, especially in few-shot learning, we introduce a lightweight Dispersive Loss that repels state embeddings during training, ...
- **p. 4 / Abstract - extractive body cue:** This can lead to a form of "feature collapse", where the policy network maps distinct environmental states that demand fundamentally different actions to nearly identical ...
- **p. 3 / Abstract - extractive body cue:** MP1: One-Step Trajectory Generation In the context of robot learning, the policy's task is to map a sequence of observations, including 3D point clouds P ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | MP1: One-Step Trajectory Generation In the context of robot learning, the policy's task is to map a sequence of observations, including 3D point clouds P and robotic states S, to a future ... | observation history와 expert trajectory/action | p. 3 (Abstract), p. 3 (Abstract) |
| State/latent | MP1, One-Step, Trajectory, Generation, context, robot, learning, policy, task, sequence, observations, including | behavior policy와 temporal action context | p. 3 (Abstract), p. 3 (Abstract), p. 4 (Abstract) |
| Output/action | The MP1 takes the historical observation point cloud and the robot's state as inputs. | predicted action 또는 action chunk | p. 3 (Abstract), p. 4 (Abstract), p. 4 (Abstract) |
| Objective/outcome | However, generative models within this field face a fundamental trade-off between the slow, iterative sampling of diffusion models and the architectural constraints of faster Flow-based methods, which often rely on explicit consistency ... | imitation error, task success, robustness와 compounding error | p. 1 (Abstract), p. 4 (Abstract), p. 4 (Abstract) |

## Main Claims and Actual Contribution

- **p. 2 / Abstract - extractive body cue:** Our contributions are as follows: • We introduce MP1, the first MeanFlow-based robot learning framework.
- **p. 1 / Abstract - extractive body cue:** We validate our method on the Adroit and Meta-World benchmarks, as well as in real-world scenarios.
- **p. 1 / Abstract - extractive body cue:** To address these limitations, we introduce MP1, which pairs 3D point-cloud inputs with the MeanFlow paradigm to generate action trajectories in one network function evaluation ...
- **p. 2 / Abstract - extractive body cue:** We present the first adaptation of the MeanFlow (Geng et al.
- **p. 3 / Abstract - extractive body cue:** To address these challenges, we propose the MP1 (Fig.
- **p. 5 / Figure/Table caption - extractive body cue:** Table 1: Performance of different methods on 37 Tasks. We evaluate the performance of our method on 3 Adroit and 34 Meta- World tasks with ...
- **p. 6 / Abstract - extractive body cue:** On the 21 "Easy" tasks in Meta-World, the proposed approach achieves a success rate of 88.2%, representing a 3.4% improvement over the FlowPolicy.
- **p. 6 / Abstract - extractive body cue:** As the number of training steps increases, all methods demonstrate improved success rates; however, MP1 achieves faster convergence and higher final success rates across all ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 5 (Figure/Table caption), p. 6 (Abstract) |
| Embodiment/environment | Conditioning on 3D point-cloud features, it learns effectively from a handful of demonstrations, yet delivers one-step sampling with SOTA success rates and millisecond-level inference latency. • We incorporate a lightweight Dispersive L ... | hardware/simulator version and reset protocol | p. 2 (Abstract), p. 7 (Abstract) |
| Dataset/benchmark | 3, we present the performance of MP1 and Flowpolicy on the hammer task in the simulation environment, as well as the experimental results for the hammer task in the real-world environment. | role, split, size and leakage | p. 2 (Abstract), p. 7 (Abstract), p. 7 (Abstract), p. 3 (Abstract) |
| Metric | Figure 4: Success rate curves of different methods on multi- ple Meta-World tasks. We compare the performance of MP1, FlowPolicy, and DP3 on four tasks. The x-axis represents training steps, and the ... | definition, denominator, direction and uncertainty | p. 6 (Figure/Table caption), p. 7 (Abstract), p. 7 (Abstract) |
| Baseline/ablation | MP1 is capable of one-step inference and, compared to state-of-the-art (SOTA) methods, improves the average success rate by 7.3% (Tab. | fair input/data/compute/action matching | p. 2 (Abstract), p. 5 (Figure/Table caption), p. 1 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 4 / Abstract - extractive body cue:** MP1 FlowPolicy Adroit: Hammer (FlowPolicy: 15.3ms/ MP1:7.1ms) Real-world: Hammer (FlowPolicy: 22.3s/ MP1:18.6s) failure success Figure 3: Qualitative comparison of the proposed MP1 and the previous ...
- **p. 2 / Abstract - extractive body cue:** 3D Input Robot Learning To overcome the limitations of 2D inputs, 3D inputs have gained prominence.
- **p. 2 / Abstract - extractive body cue:** However, a purely regression-based objective fails to impose explicit regularization on the policy's internal feature space (Wang and He 2025).
- **p. 4 / Abstract - extractive body cue:** Moreover, our method successfully completes the real-world hammer task, whereas FlowPolicy fails. estimate of the total derivative, with a stop-gradient sg(·) to ensure stability: utgt ...
- **p. 7 / Abstract - extractive body cue:** Conclusion In this paper, we address the limitations of existing Diffusion-based and Flow-based approaches by introducing MeanFlow into robot learning.
- **p. 3 / Abstract - extractive body cue:** Unlike Diffusion-based methods, our approach does not require multi-step denoising; distinct from existing Flowbased approaches, the MP1 does not rely on ODE solvers, consistency constraints, ...
- **p. 3 / Abstract - extractive body cue:** After passing through the MeanFlow, the model computes regression loss (Lcfg) between the mean velocity generated from the initial noise and the target velocity.

## Why Read It

RL, IL, offline learning, and robot data의 il 문제를 이해하기 위해 읽는다. 본문은 However, diffusion still faces challenges related to inference time.를 문제로 두고, Our contributions are as follows: • We introduce MP1, the first MeanFlow-based robot learning framework.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (Abstract), p. 2 (Abstract), p. 1 (Abstract), p. 1 (Abstract), p. 3 (Abstract), p. 1 (Abstract) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
