# Method - DiffSkill: Skill Abstraction from Differentiable Physics for Deformable Object Manipulations with Tools

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2203.17275; PDF retrieval source: https://arxiv.org/pdf/2203.17275. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 3 (2 METHOD), p. 2 (2 METHOD), p. 4 (2 METHOD), p. 4 (2 METHOD), p. 5 (2 METHOD), p. 14 (A IMPLEMENTATION DETAILS)): Given an initial state s0, a goal state sg and the transition dynamics p of a differentiable simulator, we use gradient-based trajectory optimization to solve for an open-loop action sequence ...

## Method Body Digest

- **p. 3 / 2 METHOD - extractive body cue:** Given an initial state s0, a goal state sg and the transition dynamics p of a differentiable simulator, we use gradient-based trajectory optimization to solve ...
- **p. 2 / 2 METHOD - extractive body cue:** Since it is not feasible to directly use a standalone differentiable physics solver to find an optimal solution for long-horizontal tasks, we propose to first ...
- **p. 4 / 2 METHOD - extractive body cue:** Our neural skill abstraction consists of a goal-conditioned policy that takes a sensory observation (RGB-D images in our case) as input, a feasibility and reward ...
- **p. 4 / 2 METHOD - extractive body cue:** We use an MSE loss Lfea for model training, which was shown empirically to work better than a cross-entropy loss.
- **p. 5 / 2 METHOD - extractive body cue:** Algorithm 1: Solve long-horizon planning with DiffSkill Input : Trajectory optimizer, skill horizon T, planning horizon H Initialize modules for neural skill abstraction πk, fk, ...
- **p. 14 / A IMPLEMENTATION DETAILS - extractive body cue:** Model parameter Value dimension of latent space 8 MLP hidden node number 1024 Training parameters Value learning rate 0.001 batch size 128 optimizer Adam beta1 ...
- **p. 3 / 2 METHOD - extractive body cue:** 2.1 PROBLEM FORMULATION We consider a Markov Decision Process (MDP) defined by a set of states s ∈S, actions a ∈A and a deterministic, differentiable ...
- **p. 5 / 2 METHOD - extractive body cue:** For the continuous variables, we start with N initial solutions {z1, . . . zH}j, j = 1, . . . , N and use ...

## Design Rationale

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Our method consists of three components, (1) a trajectory optimizer that acts as an expert that applies gradient-based optimization on the differentiable simulator to obtain ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To extend the use of differentiable physics models to these long-horizon tasks and enable the agent to directly consume visual observations, we propose DiffSkill: a ...
- **p. 4 / 2 METHOD - extractive body cue:** As such, we propose to learn a neural skill abstractor that learns skills from the demonstration videos of a trajectory optimizer; we will then leverage ...

## Source Evidence Cues

- **p. 3 / 2 METHOD - extractive body cue:** Given an initial state s0, a goal state sg and the transition dynamics p of a differentiable simulator, we use gradient-based trajectory optimization to solve ...
- **p. 2 / 2 METHOD - extractive body cue:** Since it is not feasible to directly use a standalone differentiable physics solver to find an optimal solution for long-horizontal tasks, we propose to first ...
- **p. 4 / 2 METHOD - extractive body cue:** Our neural skill abstraction consists of a goal-conditioned policy that takes a sensory observation (RGB-D images in our case) as input, a feasibility and reward ...
- **p. 4 / 2 METHOD - extractive body cue:** We use an MSE loss Lfea for model training, which was shown empirically to work better than a cross-entropy loss.
- **p. 5 / 2 METHOD - extractive body cue:** Algorithm 1: Solve long-horizon planning with DiffSkill Input : Trajectory optimizer, skill horizon T, planning horizon H Initialize modules for neural skill abstraction πk, fk, ...
- **p. 14 / A IMPLEMENTATION DETAILS - extractive body cue:** Model parameter Value dimension of latent space 8 MLP hidden node number 1024 Training parameters Value learning rate 0.001 batch size 128 optimizer Adam beta1 ...
- **p. 3 / 2 METHOD - extractive body cue:** 2.1 PROBLEM FORMULATION We consider a Markov Decision Process (MDP) defined by a set of states s ∈S, actions a ∈A and a deterministic, differentiable ...
- **Detected method headings:** 2 METHOD (p. 2); B COMPARISON WITH MODEL-FREE RL ON SINGLE-TOOL TASKS (p. 14)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / affordance state | object와 contact-relevant scene을 표현한다 | RGB-D, point cloud, object/task observation | pose, affordance, grasp/contact graph 또는 SE(3) descriptor를 구성 | object/contact state | Given an initial state s0, a goal state sg and the transition dynamics p of a differentiable simulator, we use gradient-based trajectory ... | p. 3 (2 METHOD), p. 2 (2 METHOD) |
| Grasp / trajectory generation | goal을 feasible manipulation candidate로 바꾼다 | geometry/contact state와 task goal | grasp sampling, pose planning, trajectory optimization 또는 policy decoding을 적용 | grasp, pose, force 또는 trajectory | Since it is not feasible to directly use a standalone differentiable physics solver to find an optimal solution for long-horizontal tasks, we ... | p. 2 (2 METHOD), p. 4 (2 METHOD) |
| Contact execution / correction | interaction outcome으로 action을 닫힌 loop로 수정한다 | candidate와 visual/force/tactile feedback | tracking, regrasp, correction, termination 또는 recovery를 수행 | next action/task state | Our neural skill abstraction consists of a goal-conditioned policy that takes a sensory observation (RGB-D images in our case) as input, a ... | p. 4 (2 METHOD), p. 4 (2 METHOD) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 14 / A IMPLEMENTATION DETAILS - extractive body cue:** Model parameter Value dimension of latent space 8 MLP hidden node number 1024 Training parameters Value learning rate 0.001 batch size 128 optimizer Adam beta1 ...
- **p. 5 / 2 METHOD - extractive body cue:** For the continuous variables, we start with N initial solutions {z1, . . . zH}j, j = 1, . . . , N and use ...
- **p. 5 / 2 METHOD - extractive body cue:** Specifically, after each gradient update step of Adam, we project the current zi to the constraint set by setting zi = zi max(//zi//2/ √ M),1).
- **p. 3 / 2 METHOD - extractive body cue:** The objective is to find a policy at = π(o, og) that minimizes the final distance to the goal D(sT , sg), where T is ...
- **p. 4 / 2 METHOD - extractive body cue:** Reward Predictor: We further train a reward predictor r(ot, og) ∈R that predicts the negative of the Sinkhorn divergence between the corresponding states -D(st, sg) ...
- **p. 3 / 2 METHOD - extractive body cue:** Given an initial state s0, a goal state sg and the transition dynamics p of a differentiable simulator, we use gradient-based trajectory optimization to solve ...
- **Formal bridge:** object geometry/contact state -> grasp/pose/force/trajectory -> task/contact/pose objective -> completion, contact success and robustness.
- **Equation/algorithm anchors:** p. 5 (2 METHOD), p. 5 (2 METHOD), p. 14 (A IMPLEMENTATION DETAILS), p. 3 (2 METHOD), p. 3 (2 METHOD), p. 4 (2 METHOD).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | neural, skill, abstraction, consists, goal-conditioned, policy, takes, sensory, observation, RGB-D, images, case, input, feasibility | RGB-D/point cloud, object state와 contact/task observation | body cue; exact tensor/frame verify |
| State/latent | neural, skill, abstraction, consists, goal-conditioned, policy, takes, sensory, observation, RGB-D | object geometry, affordance, contact mode 또는 end-effector state | body cue; notation verify |
| Action/output | consists, three, components, trajectory, optimizer, acts, expert, applies, gradient-based, optimization | grasp, pose, force 또는 end-effector trajectory | body cue; unit/decoder verify |
| Objective/constraint | Model, parameter, Value, dimension, latent, space, MLP, hidden, node, number | task/contact/pose objective | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 2 METHOD - extractive body cue:** Our neural skill abstraction consists of a goal-conditioned policy that takes a sensory observation (RGB-D images in our case) as input, a feasibility and reward ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Our method consists of three components, (1) a trajectory optimizer that acts as an expert that applies gradient-based optimization on the differentiable simulator to obtain ...
- **p. 2 / 2 METHOD - extractive body cue:** Our goal is to learn a policy to perform sequential deformable object manipulation using tools from sensory observations.
- **p. 4 / 2 METHOD - extractive body cue:** Furthermore, to make the policy more robust to goal observations outside of the training goal images, we adopt hindsight relabeling (Andrychowicz et al., 2017).
- **p. 3 / 2 METHOD - extractive body cue:** At each timestep, the agent only has access to an observation o ∈O (such as an image) instead of directly observing the state.
- **p. 3 / 2 METHOD - extractive body cue:** In this paper, we define a "skill" as a policy that uses a single tool to achieve a short-horizon goal sg, starting from an initial ...
- **p. 5 / 2 METHOD - extractive body cue:** 2 to obtain cost C(k, z) ; Choose k, z that minimizes C(k, z); for i ←0 to H do Reset tools to initial poses ...
- **Normalized interface:** observation=RGB-D/point cloud, object state와 contact/task observation; state=object geometry, affordance, contact mode 또는 end-effector state; output/action=grasp, pose, force 또는 end-effector trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | grasp/pose proposal에서 contact episode까지의 task horizon; trajectory chunk 여부 확인 필요. | When collecting demonstration for learning the skills, for each short-horizon goal sg, we run the trajectory optimizer for each tool separately, by ... | episode/sequence/action-chunk boundary |
| Rate / latency | perception/planning rate와 low-level contact control rate가 분리된다. | At each timestep, the agent only has access to an observation o ∈O (such as an image) instead of directly observing the ... | Hz/fps, inference time and control rate |
| Memory | object/contact state, current pose와 tactile/force history; exact window 확인 필요. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | point/pose encoding, candidate sampling/optimization과 collision/contact checking이 결정한다. | Model parameter Value dimension of latent space 8 MLP hidden node number 1024 Training parameters Value learning rate 0.001 batch size 128 ... | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / 2 METHOD - extractive body cue:** We use an MSE loss Lfea for model training, which was shown empirically to work better than a cross-entropy loss.
- **p. 5 / 2 METHOD - extractive body cue:** Algorithm 1: Solve long-horizon planning with DiffSkill Input : Trajectory optimizer, skill horizon T, planning horizon H Initialize modules for neural skill abstraction πk, fk, ...
- **p. 14 / A IMPLEMENTATION DETAILS - extractive body cue:** Model parameter Value dimension of latent space 8 MLP hidden node number 1024 Training parameters Value learning rate 0.001 batch size 128 optimizer Adam beta1 ...
- **p. 14 / A IMPLEMENTATION DETAILS - extractive body cue:** Model parameter Value dimension of latent space 8 MLP hidden node number 1024 Training parameters Value learning rate 0.001 batch size 128 optimizer Adam beta1 ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Given, initial, state, goal, transition, dynamics, differentiable, simulator, gradient-based, trajectory, optimization, solve, open-loop, action, sequence, Kelley, where, case, deformable, object.
- **Relevant PDF headings:** 2 METHOD (p. 2); B COMPARISON WITH MODEL-FREE RL ON SINGLE-TOOL TASKS (p. 14).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / affordance state | We build our simulation environments on top of PlasticineLab (Huang et al., 2021), a differentiable physics benchmark using the DiffTaichi system (Hu ... | p. 5 (3 EXPERIMENTS), p. 6 (3 EXPERIMENTS) |
| Grasp / trajectory generation | 3.3 BASELINES We compare with three strong baselines: Model-free Reinforcement Learning (RL) We compare with two model-free RL methods: TD3 (Fujimoto et ... | p. 6 (3 EXPERIMENTS), p. 8 (3 EXPERIMENTS) |
| Contact execution / correction | Each entry shows the normalized improvement / success rate. | p. 7 (3 EXPERIMENTS), p. 7 (3 EXPERIMENTS) |

## Failure and Ablation Link

- **p. 8 / Figure/Table caption - extractive body cue:** Figure 3: Visualization of the generated plan and the corresponding execution. The plan generated by DiffSkill is shown in the left, where the first and ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: Humans use various tools to manipulate deformable objects much more effectively than state-of-the-art robotic systems. This work aims to narrow the gap and ...
- **p. 7 / 3 EXPERIMENTS - extractive body cue:** 3.5 ABLATION ANALYSIS We perform two ablations on DiffSkill.
- **p. 7 / 3 EXPERIMENTS - extractive body cue:** This is because it requires three stages of manipulation; further, it is non-trivial to transport the dough without deforming it too much.
- **p. 8 / 3 EXPERIMENTS - extractive body cue:** Without discrete planning, the policy performs poorly.
- **p. 14 / Figure/Table caption - extractive body cue:** Table 3: Summary of all hyper-parameters. B COMPARISON WITH MODEL-FREE RL ON SINGLE-TOOL TASKS In this work, we focus on solving long-horizon multi-tool tasks. But ...
- **p. 6 / 3 EXPERIMENTS - extractive body cue:** In Table 3, we can see that the learned skills (labeled as Behavior Cloning) approach the normalized performance of the trajectory optimization (Trajectory Opt) on ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (2 METHOD), p. 2 (2 METHOD), p. 4 (2 METHOD), p. 4 (2 METHOD), p. 5 (2 METHOD), p. 14 (A IMPLEMENTATION DETAILS), objective p. 14 (A IMPLEMENTATION DETAILS), p. 5 (2 METHOD), p. 5 (2 METHOD), p. 3 (2 METHOD), p. 4 (2 METHOD), p. 3 (2 METHOD), temporal p. 4 (2 METHOD), p. 3 (2 METHOD), p. 6 (3 EXPERIMENTS), p. 14 (A IMPLEMENTATION DETAILS), p. 2 (2 METHOD), p. 2 (2 METHOD).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (14 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** Algorithm 1: Solve long-horizon planning with DiffSkill Input : Trajectory optimizer, skill horizon T, planning horizon H Initialize modules for neural skill abstraction πk, fk, r, G, Q ; Generate ... (p. 5, 2 METHOD).
- **Objective/update evidence:** Specifically, after each gradient update step of Adam, we project the current zi to the constraint set by setting zi = zi max(//zi//2/ √ M),1). (p. 5, 2 METHOD).
- **Temporal/runtime evidence:** When collecting demonstration for learning the skills, for each short-horizon goal sg, we run the trajectory optimizer for each tool separately, by masking the actions for other tools to be ... (p. 4, 2 METHOD).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
