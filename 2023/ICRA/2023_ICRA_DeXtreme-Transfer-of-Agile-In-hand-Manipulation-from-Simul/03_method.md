# Method - DeXtreme: Transfer of Agile In-hand Manipulation from Simulation to Reality

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (28 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://research.nvidia.com/publication/2023-06_dextreme-transfer-agile-hand-manipulation-simulation-reality; PDF retrieval source: https://research.nvidia.com/publication/2023-06_dextreme-transfer-agile-hand-manipulation-simulation-reality. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 4 (2 Method), p. 10 (2 Method), p. 6 (2 Method), p. 17 (Method), p. 6 (2 Method), p. 7 (2 Method)): We use Proximal Policy Optimisation (PPO) [9] to learn a parametric stochastic policy πθ (actor), mapping from observations o ∈O to actions a ∈A.

## Method Body Digest

- **p. 4 / 2 Method - extractive body cue:** We use Proximal Policy Optimisation (PPO) [9] to learn a parametric stochastic policy πθ (actor), mapping from observations o ∈O to actions a ∈A.
- **p. 10 / 2 Method - extractive body cue:** To account for unmodelled dynamics, we use a Random Network Adversary (RNA, see below).
- **p. 6 / 2 Method - extractive body cue:** Input Dimensionality Actor Critic Object position with noise 3D ✓ ✓ Object orientation with noise 4D (quaternion) ✓ ✓ Target position 3D ✓ ✓ Target ...
- **p. 17 / Method - extractive body cue:** The slow turnaround time involved in repairing the hardware motivated us to do it ourselves regularly during the experiments, but it was only a temporary ...
- **p. 6 / 2 Method - extractive body cue:** Our best policy πθ : O × H →A was a Long Short-Term Memory (LSTM) network [12] taking in environment observations o and previous hidden ...
- **p. 7 / 2 Method - extractive body cue:** Noise Additive gaussian [0.0, 0.04] [0.0, 0.48] RNA α Set Value uniform [0.0, 0.0] [0.0, 0.16] Environment Gravity (each coord.) Additive normal [0, 0.5] [0, ...
- **p. 10 / 2 Method - extractive body cue:** Similarly to the aforementioned action latency, we use ADR to sample a categorical action delay d ∈{1, . . . , delaymax}.
- **p. 4 / 2 Method - extractive body cue:** 2.3 Policy Learning with RL RL Formulation: The task of manipulating the cube to the desired orientation is modelled as a sequential decision making problem ...

## Design Rationale

- **p. 3 / 2 Method - extractive body cue:** 2.1 Task We propose a method for performing object reorientation on an anthropomorphic hand.
- **p. 4 / 2 Method - extractive body cue:** 2.2 Hardware Our hardware setup (see Fig 2) consists of an Allegro Hand rigidly mounted at the wrist.
- **p. 7 / 2 Method - extractive body cue:** To help overcome this, we introduce various kinds of randomisations [15] into the simulated environment as listed in Table 3.

## Source Evidence Cues

- **p. 4 / 2 Method - extractive body cue:** We use Proximal Policy Optimisation (PPO) [9] to learn a parametric stochastic policy πθ (actor), mapping from observations o ∈O to actions a ∈A.
- **p. 10 / 2 Method - extractive body cue:** To account for unmodelled dynamics, we use a Random Network Adversary (RNA, see below).
- **p. 6 / 2 Method - extractive body cue:** Input Dimensionality Actor Critic Object position with noise 3D ✓ ✓ Object orientation with noise 4D (quaternion) ✓ ✓ Target position 3D ✓ ✓ Target ...
- **p. 17 / Method - extractive body cue:** The slow turnaround time involved in repairing the hardware motivated us to do it ourselves regularly during the experiments, but it was only a temporary ...
- **p. 6 / 2 Method - extractive body cue:** Our best policy πθ : O × H →A was a Long Short-Term Memory (LSTM) network [12] taking in environment observations o and previous hidden ...
- **p. 7 / 2 Method - extractive body cue:** Noise Additive gaussian [0.0, 0.04] [0.0, 0.48] RNA α Set Value uniform [0.0, 0.0] [0.0, 0.16] Environment Gravity (each coord.) Additive normal [0, 0.5] [0, ...
- **p. 10 / 2 Method - extractive body cue:** Similarly to the aforementioned action latency, we use ADR to sample a categorical action delay d ∈{1, . . . , delaymax}.
- **Detected method headings:** 2 Method (p. 2); 2 Method (p. 3); Method (p. 16)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / affordance state | object와 contact-relevant scene을 표현한다 | RGB-D, point cloud, object/task observation | pose, affordance, grasp/contact graph 또는 SE(3) descriptor를 구성 | object/contact state | We use Proximal Policy Optimisation (PPO) [9] to learn a parametric stochastic policy πθ (actor), mapping from observations o ∈O to actions ... | p. 4 (2 Method), p. 10 (2 Method) |
| Grasp / trajectory generation | goal을 feasible manipulation candidate로 바꾼다 | geometry/contact state와 task goal | grasp sampling, pose planning, trajectory optimization 또는 policy decoding을 적용 | grasp, pose, force 또는 trajectory | To account for unmodelled dynamics, we use a Random Network Adversary (RNA, see below). | p. 10 (2 Method), p. 6 (2 Method) |
| Contact execution / correction | interaction outcome으로 action을 닫힌 loop로 수정한다 | candidate와 visual/force/tactile feedback | tracking, regrasp, correction, termination 또는 recovery를 수행 | next action/task state | Input Dimensionality Actor Critic Object position with noise 3D ✓ ✓ Object orientation with noise 4D (quaternion) ✓ ✓ Target position 3D ... | p. 6 (2 Method), p. 17 (Method) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 2 Method - extractive body cue:** 2.3 Policy Learning with RL RL Formulation: The task of manipulating the cube to the desired orientation is modelled as a sequential decision making problem ...
- **p. 6 / 2 Method - extractive body cue:** 2.4 Reward Formulation The reward formulation is inspired by the Shadow hand environment in Isaac Gym[6], and described and justified in Table 2.
- **p. 16 / Method - extractive body cue:** 9To fully hold the cube stationary in hand for a target orientation means zero velocities at the target, which requires changing the reward function.
- **p. 6 / 2 Method - extractive body cue:** While in some experiments the learning rate was updated adaptively based on a fixed KL threshold 0.016, our best result was obtained using linear scheduling ...
- **p. 4 / 2 Method - extractive body cue:** PPO additionally learns a function V π ϕ (s, o) (critic) to approximate the on-policy value function.
- **p. 7 / 2 Method - extractive body cue:** Isaac Gym gives the advantage of being able to simulate thousands of robots in parallel on a single GPU, mitigating the need for large amounts ...
- **Formal bridge:** object geometry/contact state -> grasp/pose/force/trajectory -> task/contact/pose objective -> completion, contact success and robustness.
- **Equation/algorithm anchors:** p. 8 (2 Method), p. 6 (2 Method), p. 9 (2 Method), p. 10 (2 Method), p. 16 (Method).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Input, Dimensionality, Actor, Critic, Object, position, noise, orientation, quaternion, Target, Relative, Last, actions, Hand | RGB-D/point cloud, object state와 contact/task observation | body cue; exact tensor/frame verify |
| State/latent | Input, Dimensionality, Actor, Critic, Object, position, noise, orientation, quaternion, Target | object geometry, affordance, contact mode 또는 end-effector state | body cue; notation verify |
| Action/output | Task, performing, object, reorientation, anthropomorphic, hand, Hardware, setup, Fig, consists | grasp, pose, force 또는 end-effector trajectory | body cue; unit/decoder verify |
| Objective/constraint | Policy, Learning, Formulation, task, manipulating, cube, desired, orientation, modelled, sequential | task/contact/pose objective | equation anchor required |

## Observation–State–Action Interface

- **p. 6 / 2 Method - extractive body cue:** Input Dimensionality Actor Critic Object position with noise 3D ✓ ✓ Object orientation with noise 4D (quaternion) ✓ ✓ Target position 3D ✓ ✓ Target ...
- **p. 4 / 2 Method - extractive body cue:** We use Proximal Policy Optimisation (PPO) [9] to learn a parametric stochastic policy πθ (actor), mapping from observations o ∈O to actions a ∈A.
- **p. 6 / 2 Method - extractive body cue:** Our best policy πθ : O × H →A was a Long Short-Term Memory (LSTM) network [12] taking in environment observations o and previous hidden ...
- **p. 10 / 2 Method - extractive body cue:** This delay case, applied to both observations of cube pose and actions, mimics random jitter in latency times.
- **p. 10 / 2 Method - extractive body cue:** To ensure that the policy performance did not deteriorate and LSTM hidden state become corrupted by this, we occasionally inject completely random cube poses into ...
- **p. 4 / 2 Method - extractive body cue:** [10], the critic does not take in the same observations as the actor, but receives additional observations including states s ∈S in the POMDP.
- **p. 11 / 2 Method - extractive body cue:** Actions from the RNA network are blended with those from the policy by a = α · aRNA + (1 -α) · apolicy, where α ...
- **Normalized interface:** observation=RGB-D/point cloud, object state와 contact/task observation; state=object geometry, affordance, contact mode 또는 end-effector state; output/action=grasp, pose, force 또는 end-effector trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | grasp/pose proposal에서 contact episode까지의 task horizon; trajectory chunk 여부 확인 필요. | The second form of delay is action latency, where the action from n timesteps ago is executed. | episode/sequence/action-chunk boundary |
| Rate / latency | perception/planning rate와 low-level contact control rate가 분리된다. | To make our policies more robust to the changing inference frequency and jitter resulting from our ROS-based inference system, we add stochastic ... | Hz/fps, inference time and control rate |
| Memory | object/contact state, current pose와 tactile/force history; exact window 확인 필요. | As we are doing simulation on GPU rather than CPU, instead of using a new network per environment-episode and wasting memory on ... | window and reset |
| Compute | point/pose encoding, candidate sampling/optimization과 collision/contact checking이 결정한다. | However, because the policy was trained with a control frequency of 30Hz in simulation, the pose estimator was locked to run at ... | hardware, batch and throughput |

## Training vs Inference

- **p. 17 / Method - extractive body cue:** The slow turnaround time involved in repairing the hardware motivated us to do it ourselves regularly during the experiments, but it was only a temporary ...
- **p. 13 / Experiment - extractive body cue:** The network runs on three cameras at an inference rate of 20Hz on an NVIDIA RTX 3090 GPU and a 32-core AMD Ryzen Threadripper CPU.
- **p. 13 / Experiment - extractive body cue:** However, because the policy was trained with a control frequency of 30Hz in simulation, the pose estimator was locked to run at 15Hz to ensure ...
- **p. 16 / Method - extractive body cue:** DR type Pose estimation type Training time Cons.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Proximal, Policy, Optimisation, PPO, learn, parametric, stochastic, actor, mapping, observations, actions, account, unmodelled, dynamics, Random, Network, Adversary, RNA, below, Input.
- **Relevant PDF headings:** 2 Method (p. 2); 2 Method (p. 3); Method (p. 16).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / affordance state | We believe such inter-day variations are important to benchmark in robotics [20] and have endeavoured to highlight this specifically in this challenging ... | p. 14 (3 Results), p. 13 (Experiment) |
| Grasp / trajectory generation | Table 11: Our hardware setup compared against the one used in OpenAI et al. [1] and OpenAI et al. [8]. Note that ... | p. 25 (Figure/Table caption), p. 13 (Experiment) |
| Contact execution / correction | We demonstrate performance which significantly improves upon the best vision policies 8Although [8] focused on the Rubik's cube, they also trained for ... | p. 14 (3 Results), p. 14 (3 Results) |

## Failure and Ablation Link

- **p. 13 / Experiment - extractive body cue:** Our ablation studies in Section 3.2 do test the strength of the pose estimator for manipulation in the real world.
- **p. 15 / 3 Results - extractive body cue:** In the basic experiment of goal reaching without the hold, the cube may shoot past the target, making it difficult to tell if the target ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: The hardware setup used in this work, unlike [1], is not housed in a cage, and our system is robust enough to perform ...
- **p. 14 / 3 Results - extractive body cue:** We use three separate machines to run various components.
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 4: Parameter range adjustments, pi_lo and pi_hi, with ADR based on the performance of policy at the boundaries Qi_lo and Qi_hi with respect to ...
- **p. 18 / 4 Related work - extractive body cue:** However, these often fail to reproduce the agile dexterity present in human hands, as the limitations of such a sequential approach to control place corresponding ...
- **p. 17 / 4 Related work - extractive body cue:** These approaches work well while an object maintains no-slip 10While extrinsics change with different camera configurations, the intrinsics remain the same.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 4 (2 Method), p. 10 (2 Method), p. 6 (2 Method), p. 17 (Method), p. 6 (2 Method), p. 7 (2 Method), objective p. 4 (2 Method), p. 6 (2 Method), p. 16 (Method), p. 6 (2 Method), p. 4 (2 Method), p. 7 (2 Method), temporal p. 10 (2 Method), p. 10 (2 Method), p. 7 (2 Method), p. 11 (2 Method), p. 13 (Experiment), p. 17 (Method).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
