# DiffSkill: Skill Abstraction from Differentiable Physics for Deformable Object Manipulations with Tools

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (14 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2203.17275.
> PDF retrieval source: https://arxiv.org/pdf/2203.17275. Reading tracker status/evidence was not changed.

- Year/Venue: 2022 / ICLR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: NEXT
- Tags: Robotics, deformable object, tool use, differentiable physics, skill abstraction, Planning
- Official paper: https://arxiv.org/abs/2203.17275
- Full-text retrieval: https://arxiv.org/pdf/2203.17275
- Code/Project: https://diffskill.github.io/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-02 (14 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Manipulation, contact, tactile, and dexterity의 manipulation 문제를 이해하기 위해 읽는다. 본문은 These differentiable simulators have facilitated gradient-based trajectory optimizers to find a motion trajectory with much fewer samples, compared with black box optimizers such as CEM or reinforcement learning algorithms (Huang et al. ...를 문제로 두고, Our method consists of three components, (1) a trajectory optimizer that acts as an expert that applies gradient-based optimization on the differentiable simulator to obtain demonstration trajectories, which requires the full state ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** We consider the problem of sequential robotic manipulation of deformable objects using tools.
- **p. 1 / ABSTRACT - extractive body cue:** Previous works have shown that differentiable physics simulators provide gradients to the environment state and help trajectory optimization to converge orders of magnitude faster than ...
- **p. 1 / ABSTRACT - extractive body cue:** However, such gradient-based trajectory optimization typically requires access to the full simulator states and can only solve short-horizon, single-skill tasks due to local optima.
- **p. 1 / ABSTRACT - extractive body cue:** In this work, we propose a novel framework, named DiffSkill, that uses a differentiable physics simulator for skill abstraction to solve long-horizon deformable object manipulation ...
- **p. 1 / ABSTRACT - extractive body cue:** In particular, we first obtain short-horizon skills using individual tools from a gradient-based optimizer, using the full state information in a differentiable simulator; we then ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** These differentiable simulators have facilitated gradient-based trajectory optimizers to find a motion trajectory with much fewer samples, compared with black box optimizers such as CEM ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** This work aims to narrow the gap and develop a method named DiffSkill that learns to use tools like a rolling pin, spatula, knife, etc., ...

## Core Idea

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Our method consists of three components, (1) a trajectory optimizer that acts as an expert that applies gradient-based optimization on the differentiable simulator to obtain ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To extend the use of differentiable physics models to these long-horizon tasks and enable the agent to directly consume visual observations, we propose DiffSkill: a ...
- **p. 4 / 2 METHOD - extractive body cue:** As such, we propose to learn a neural skill abstractor that learns skills from the demonstration videos of a trajectory optimizer; we will then leverage ...
- **p. 4 / 2 METHOD - extractive body cue:** Our neural skill abstraction consists of a goal-conditioned policy that takes a sensory observation (RGB-D images in our case) as input, a feasibility and reward ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** The recent development of differentiable physics simulators for deformable objects has shown promising results for solving soft-body control problems (Hu et al., 2019b; Murthy et ...
- **p. 3 / 2 METHOD - extractive body cue:** Given an initial state s0, a goal state sg and the transition dynamics p of a differentiable simulator, we use gradient-based trajectory optimization to solve ...
- **p. 3 / 2 METHOD - extractive body cue:** Published as a conference paper at ICLR 2022 f(o, g) s0 sim s1 a0 ... sT sim back propagation Loss a1 policy feasibility predictor skill ...
- **p. 2 / 2 METHOD - extractive body cue:** Since it is not feasible to directly use a standalone differentiable physics solver to find an optimal solution for long-horizontal tasks, we propose to first ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Our neural skill abstraction consists of a goal-conditioned policy that takes a sensory observation (RGB-D images in our case) as input, a feasibility and reward predictor, as well as a variational auto-encoder ... | RGB-D/point cloud, object state와 contact/task observation | p. 4 (2 METHOD), p. 2 (1 INTRODUCTION) |
| State/latent | neural, skill, abstraction, consists, goal-conditioned, policy, takes, sensory, observation, RGB-D, images, case | object geometry, affordance, contact mode 또는 end-effector state | p. 4 (2 METHOD), p. 2 (1 INTRODUCTION), p. 3 (2 METHOD) |
| Output/action | Our method consists of three components, (1) a trajectory optimizer that acts as an expert that applies gradient-based optimization on the differentiable simulator to obtain demonstration trajectories, which requires the full state ... | grasp, pose, force 또는 end-effector trajectory | p. 2 (1 INTRODUCTION), p. 3 (2 METHOD), p. 2 (2 METHOD) |
| Objective/outcome | Published as a conference paper at ICLR 2022 f(o, g) s0 sim s1 a0 ... sT sim back propagation Loss a1 policy feasibility predictor skill 0 skill 0 skill 1 ... f(o, ... | task completion, contact success, pose/force error와 generalization | p. 3 (2 METHOD), p. 14 (A IMPLEMENTATION DETAILS), p. 5 (2 METHOD) |

## Main Claims and Actual Contribution

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Our method consists of three components, (1) a trajectory optimizer that acts as an expert that applies gradient-based optimization on the differentiable simulator to obtain ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To extend the use of differentiable physics models to these long-horizon tasks and enable the agent to directly consume visual observations, we propose DiffSkill: a ...
- **p. 4 / 2 METHOD - extractive body cue:** As such, we propose to learn a neural skill abstractor that learns skills from the demonstration videos of a trajectory optimizer; we will then leverage ...
- **p. 4 / 2 METHOD - extractive body cue:** Our neural skill abstraction consists of a goal-conditioned policy that takes a sensory observation (RGB-D images in our case) as input, a feasibility and reward ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** The recent development of differentiable physics simulators for deformable objects has shown promising results for solving soft-body control problems (Hu et al., 2019b; Murthy et ...
- **p. 7 / 3 EXPERIMENTS - extractive body cue:** Each entry shows the normalized improvement / success rate.
- **p. 7 / 3 EXPERIMENTS - extractive body cue:** Method Task (H) LiftSpread (2) GatherTransport (2) CutRearrange (3) Tool A only Trajectory Opt (Oracle) 0.755 / 0% 0.386 / 0% 0.033 / 0% Behavior ...
- **p. 8 / 3 EXPERIMENTS - extractive body cue:** Method Task LiftSpread GatherTransport CutRearrange No Discrete Planning 0.758 / 20% 0.312 / 0% 0.118 / 0% Direct Execution (Random) 0.593 / 15% 0.369 / ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SIMULATION | do not infer unreported downstream behavior | p. 7 (3 EXPERIMENTS), p. 7 (3 EXPERIMENTS) |
| Embodiment/environment | We build our simulation environments on top of PlasticineLab (Huang et al., 2021), a differentiable physics benchmark using the DiffTaichi system (Hu et al., 2019a) that could simulate plasticine-like objects based on ... | hardware/simulator version and reset protocol | p. 5 (3 EXPERIMENTS), p. 6 (3 EXPERIMENTS) |
| Dataset/benchmark | We found behavior cloning to be sufficient for learning short-horizon skills from the demonstration dataset. | role, split, size and leakage | p. 5 (3 EXPERIMENTS), p. 6 (3 EXPERIMENTS), p. 6 (3 EXPERIMENTS), p. 5 (3 EXPERIMENTS) |
| Metric | After training, we find the feasibility and score predictor to perform well on the held out trajectories, achieving a L2 error of less than 0.05 for the score predictor and an accuracy ... | definition, denominator, direction and uncertainty | p. 6 (3 EXPERIMENTS), p. 7 (Figure/Table caption), p. 6 (3 EXPERIMENTS) |
| Baseline/ablation | 3.3 BASELINES We compare with three strong baselines: Model-free Reinforcement Learning (RL) We compare with two model-free RL methods: TD3 (Fujimoto et al., 2018) and SAC (Haarnoja et al., 2018). | fair input/data/compute/action matching | p. 6 (3 EXPERIMENTS), p. 8 (3 EXPERIMENTS), p. 2 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 6 / 3 EXPERIMENTS - extractive body cue:** In Table 3, we can see that the learned skills (labeled as Behavior Cloning) approach the normalized performance of the trajectory optimization (Trajectory Opt) on ...
- **p. 7 / 3 EXPERIMENTS - extractive body cue:** 3.4 RESULT ANALYSIS We show that DiffSkill is able to solve the challenging long-horizon, tool-use tasks from the sensory observation (RGB-D) while the baselines cannot.
- **p. 8 / 3 EXPERIMENTS - extractive body cue:** On the other hand, if we do not optimize for the intermediate goals, we also cannot determine which tools to use at evaluation time, since ...
- **p. 6 / 3 EXPERIMENTS - extractive body cue:** In this way, a normalized performance of 0 representing a policy that does nothing and a normalized performance of 1 representing an upper bound of ...
- **p. 7 / 3 EXPERIMENTS - extractive body cue:** This is because the trajectory optimizer is more reliable at finding partial solutions that transport part of the dough to the target locations but does ...
- **p. 9 / 4 RELATED WORK - extractive body cue:** There are a few interesting directions for future work.

## Why Read It

Manipulation, contact, tactile, and dexterity의 manipulation 문제를 이해하기 위해 읽는다. 본문은 These differentiable simulators have facilitated gradient-based trajectory optimizers to find a motion trajectory with much fewer samples, compared with black box optimizers such as CEM or reinforcement learning algorithms (Huang et al. ...를 문제로 두고, Our method consists of three components, (1) a trajectory optimizer that acts as an expert that applies gradient-based optimization on the differentiable simulator to obtain demonstration trajectories, which requires the full state ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 3 (2 METHOD), p. 3 (2 METHOD) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
