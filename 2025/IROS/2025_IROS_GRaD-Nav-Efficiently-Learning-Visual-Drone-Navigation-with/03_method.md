# Method - GRaD-Nav: Efficiently Learning Visual Drone Navigation with Gaussian Radiance Fields and Differentiable Dynamics

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2503.03984; PDF retrieval source: https://arxiv.org/pdf/2503.03984. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 3 (III. METHOD), p. 3 (III. METHOD), p. 5 (4) Curriculum training for generalizable navigation pol), p. 5 (4) Curriculum training for generalizable navigation pol)): The differentiable drone dynamics model is also implemented with PyTorch, which enables efficient Jacobian computation through autograd for training the policy using our GRaD-Nav algorithm.

## Method Body Digest

- **p. 3 / III. METHOD - extractive PDF cue:** The differentiable drone dynamics model is also implemented with PyTorch, which enables efficient Jacobian computation through autograd for training the policy using our GRaD-Nav algorithm.
- **p. 3 / III. METHOD - extractive PDF cue:** 2) Hybrid simulation with 3DGS: We used a pre-trained 3DGS model to deliver the drone's first person perspective visual information and to imitate the drone's ...
- **p. 5 / 4) Curriculum training for generalizable navigation pol - extractive PDF cue:** icy: Beyond training a single policy for a long horizon trajectory, our method can also train generalizable policies that can adapt to different surrounding environments ...
- **p. 5 / 4) Curriculum training for generalizable navigation pol - extractive PDF cue:** By rolling training across these different environments, we finally trained a policy that can adapt to different gate positions and achieve generalizable navigation.
- **p. 3 / III. METHOD - extractive PDF cue:** Simulator Setting 1) Differentiable Quadrotor Dynamics Simulation: We implemented a parallelized, differentiable quadrotor dynamics simulator in PyTorch that computes gradients through full state transitions.
- **p. 3 / III. METHOD - extractive PDF cue:** Meanwhile, 3DGS also provides us with a ready-made point cloud model for the same environment, which can be used to set up reward waypoints and ...
- **p. 5 / 4) Curriculum training for generalizable navigation pol - extractive PDF cue:** We trained the policy in each environment for 5 times, 100 epochs per time; we return the learning rate to the initial value during every ...
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** The policy transfers zero-shot to drone hardware and adapts to new navigation task instances at runtime. directly map sensor inputs to control outputs, bypassing the ...

## Design Rationale

- **p. 2 / I. INTRODUCTION - extractive PDF cue:** Our main contributions are: • We introduce a simulator for training robot vision-based control policies by integrating 3DGS for high-fidelity visuals with a differentiable dynamics ...
- **p. 2 / I. INTRODUCTION - extractive PDF cue:** To achieve the goal of visual-motor navigation, we propose a novel approach that leverages 3DGS in conjunction with DDRL, using SHAC-like training algorithm and a ...
- **p. 3 / III. METHOD - extractive PDF cue:** (10) The state st = [pt, vt, qt, ωt] consists of position, velocity, orientation (quaternion), and angular velocity.

## Source Evidence Cues

- **p. 3 / III. METHOD - extractive PDF cue:** The differentiable drone dynamics model is also implemented with PyTorch, which enables efficient Jacobian computation through autograd for training the policy using our GRaD-Nav algorithm.
- **p. 3 / III. METHOD - extractive PDF cue:** 2) Hybrid simulation with 3DGS: We used a pre-trained 3DGS model to deliver the drone's first person perspective visual information and to imitate the drone's ...
- **p. 5 / 4) Curriculum training for generalizable navigation pol - extractive PDF cue:** icy: Beyond training a single policy for a long horizon trajectory, our method can also train generalizable policies that can adapt to different surrounding environments ...
- **p. 5 / 4) Curriculum training for generalizable navigation pol - extractive PDF cue:** By rolling training across these different environments, we finally trained a policy that can adapt to different gate positions and achieve generalizable navigation.
- **Detected method headings:** III. METHOD (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Map / localization state | sensor stream을 pose와 world map으로 누적한다 | camera/depth/LiDAR, odometry, history | mapping, localization, scene graph 또는 map update를 수행 | pose/map/free-space state | The differentiable drone dynamics model is also implemented with PyTorch, which enables efficient Jacobian computation through autograd for training the policy using ... | p. 3 (III. METHOD), p. 3 (III. METHOD) |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | 2) Hybrid simulation with 3DGS: We used a pre-trained 3DGS model to deliver the drone's first person perspective visual information and to ... | p. 3 (III. METHOD), p. 5 (4) Curriculum training for generalizable navigation pol) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | icy: Beyond training a single policy for a long horizon trajectory, our method can also train generalizable policies that can adapt to ... | p. 5 (4) Curriculum training for generalizable navigation pol), p. 5 (4) Curriculum training for generalizable navigation pol) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / III. METHOD - extractive PDF cue:** Simulator Setting 1) Differentiable Quadrotor Dynamics Simulation: We implemented a parallelized, differentiable quadrotor dynamics simulator in PyTorch that computes gradients through full state transitions.
- **p. 3 / III. METHOD - extractive PDF cue:** Meanwhile, 3DGS also provides us with a ready-made point cloud model for the same environment, which can be used to set up reward waypoints and ...
- **p. 5 / 4) Curriculum training for generalizable navigation pol - extractive PDF cue:** We trained the policy in each environment for 5 times, 100 epochs per time; we return the learning rate to the initial value during every ...
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** p. 3 (III. METHOD), p. 3 (III. METHOD).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | policy, transfers, zero-shot, drone, hardware, adapts, navigation, task, instances, runtime, directly, sensor, inputs, control | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | policy, transfers, zero-shot, drone, hardware, adapts, navigation, task, instances, runtime | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | main, contributions, introduce, simulator, training, robot, vision-based, control, policies, integrating | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | Simulator, Setting, Differentiable, Quadrotor, Dynamics, Simulation, implemented, parallelized, PyTorch, computes | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / I. INTRODUCTION - extractive PDF cue:** The policy transfers zero-shot to drone hardware and adapts to new navigation task instances at runtime. directly map sensor inputs to control outputs, bypassing the ...
- **p. 3 / III. METHOD - extractive PDF cue:** Our system takes body rates ωd t ∈ R3 and normalized thrust ct ∈[0, 1] as control inputs, and outputs the next state st+1 = ...
- **p. 2 / II. BACKGROUND - extractive PDF cue:** Differentiable simulation allows for backpropagation of the gradient through states and actions within the sub-windows, providing an accurate policy gradient.
- **p. 2 / II. BACKGROUND - extractive PDF cue:** The differentiable simulator is crucial here as it enables full utilization of the underlying dynamics connecting states and actions, optimizing the policy to achieve better ...
- **p. 3 / III. METHOD - extractive PDF cue:** The control input ut = (ωd t , ct) includes desired body rates and normalized thrust.
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** (𝑠𝑡) Critic Net 512×256×128 Policy grad. 𝑎𝑡 Training in Simulator 3D-GS Model Current obs.
- **p. 5 / 4) Curriculum training for generalizable navigation pol - extractive PDF cue:** By rolling training across these different environments, we finally trained a policy that can adapt to different gate positions and achieve generalizable navigation.
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | It is to be noted that BPTT samples the whole trajectory for policy updating, meaning the horizon length equals the episode length, ... | episode/sequence/action-chunk boundary |
| Rate / latency | mapping/localization, global planner, local planner와 base controller rate를 구분한다. | When parallel simulating 128 drones flying in a highly unstructured and cluttered area (room size ≈100 m2, 3DGS model size ≈ 1.5GB), ... | Hz/fps, inference time and control rate |
| Memory | map/scene graph, pose history와 current local goal. | It is to be noted that BPTT samples the whole trajectory for policy updating, meaning the horizon length equals the episode length, ... | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | When parallel simulating 128 drones flying in a highly unstructured and cluttered area (room size ≈100 m2, 3DGS model size ≈ 1.5GB), ... | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / III. METHOD - extractive PDF cue:** The differentiable drone dynamics model is also implemented with PyTorch, which enables efficient Jacobian computation through autograd for training the policy using our GRaD-Nav algorithm.
- **p. 3 / III. METHOD - extractive PDF cue:** 2) Hybrid simulation with 3DGS: We used a pre-trained 3DGS model to deliver the drone's first person perspective visual information and to imitate the drone's ...
- **p. 5 / 4) Curriculum training for generalizable navigation pol - extractive PDF cue:** icy: Beyond training a single policy for a long horizon trajectory, our method can also train generalizable policies that can adapt to different surrounding environments ...
- **p. 5 / 4) Curriculum training for generalizable navigation pol - extractive PDF cue:** By rolling training across these different environments, we finally trained a policy that can adapt to different gate positions and achieve generalizable navigation.
- **p. 5 / 4) Curriculum training for generalizable navigation pol - extractive PDF cue:** We trained the policy in each environment for 5 times, 100 epochs per time; we return the learning rate to the initial value during every ...
- **p. 6 / IV. EXPERIMENTAL RESULTS - extractive PDF cue:** We train each policy with the same reward function as in Table II and the same hyperparameters setting as Table VI for 600 epochs.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** differentiable, drone, dynamics, model, implemented, PyTorch, enables, efficient, Jacobian, computation, through, autograd, training, policy, GRaD-Nav, algorithm, Hybrid, simulation, DGS, pre-trained.
- **Relevant PDF headings:** III. METHOD (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | 7: Robot hardware experiments of drone flying through middle gate. | p. 7 (IV. EXPERIMENTAL RESULTS), p. 7 (IV. EXPERIMENTAL RESULTS) |
| Global / local decision | Without CENet, our method can still train a policy network that achieves high rewards compared to other ablation cases. | p. 6 (IV. EXPERIMENTAL RESULTS), p. 5 (IV. EXPERIMENTAL RESULTS) |
| Motion execution / recovery | The experiment results show that our proposed method achieves the highest training and evaluation rewards as well as success rate on both ... | p. 6 (IV. EXPERIMENTAL RESULTS), p. 7 (IV. EXPERIMENTAL RESULTS) |

## Failure and Ablation Link

- **p. 6 / IV. EXPERIMENTAL RESULTS - extractive PDF cue:** Without CENet, our method can still train a policy network that achieves high rewards compared to other ablation cases.
- **p. 5 / IV. EXPERIMENTAL RESULTS - extractive PDF cue:** Ablation study of our methods To validate that each module of our method is not redundant but necessary for safe navigation, and to determine each ...
- **p. 6 / IV. EXPERIMENTAL RESULTS - extractive PDF cue:** 4 demonstrates the generalizable policy's variant trajectories in different environments.
- **p. 7 / IV. EXPERIMENTAL RESULTS - extractive PDF cue:** In real-world experiments, the drone was initialized under the same conditions for each test, and success was determined by whether it flew through the gate ...
- **p. 7 / IV. EXPERIMENTAL RESULTS - extractive PDF cue:** 5: Comparison on drone's first person perspective image rendered with 3DGS in simulator (left) and captured with Intel Realsense D435 camera in real robot deployment ...
- **p. 7 / V. CONCLUSIONS - extractive PDF cue:** Limitations: Our method relies on hand-crafted reward shaping (e.g., trajectory waypoints), limiting it to singletask execution like gate traversal.
- **p. 6 / IV. EXPERIMENTAL RESULTS - extractive PDF cue:** All of the failure cases without CENet on two trajectories "crash" due to unsuccessful obstacle avoidance.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 3 (III. METHOD), p. 3 (III. METHOD), p. 5 (4) Curriculum training for generalizable navigation pol), p. 5 (4) Curriculum training for generalizable navigation pol), objective p. 3 (III. METHOD), p. 3 (III. METHOD), p. 5 (4) Curriculum training for generalizable navigation pol), temporal p. 5 (IV. EXPERIMENTAL RESULTS), p. 3 (III. METHOD), p. 4 (1) Perception), p. 6 (IV. EXPERIMENTAL RESULTS), p. 1 (I. INTRODUCTION), p. 2 (II. BACKGROUND).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
