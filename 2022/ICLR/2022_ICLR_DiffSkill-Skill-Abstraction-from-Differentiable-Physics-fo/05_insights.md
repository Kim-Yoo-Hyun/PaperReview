# Insights — DiffSkill: Skill Abstraction from Differentiable Physics for Deformable Object Manipulations with Tools

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (14 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2203.17275; PDF retrieval source: https://arxiv.org/pdf/2203.17275. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Our method consists of three components, (1) a trajectory optimizer that acts as an expert that applies gradient-based optimization on the differentiable simulator to obtain ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To extend the use of differentiable physics models to these long-horizon tasks and enable the agent to directly consume visual observations, we propose DiffSkill: a ...
- **p. 4 / 2 METHOD - extractive body cue:** As such, we propose to learn a neural skill abstractor that learns skills from the demonstration videos of a trajectory optimizer; we will then leverage ...
- **p. 4 / 2 METHOD - extractive body cue:** Our neural skill abstraction consists of a goal-conditioned policy that takes a sensory observation (RGB-D images in our case) as input, a feasibility and reward ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** The recent development of differentiable physics simulators for deformable objects has shown promising results for solving soft-body control problems (Hu et al., 2019b; Murthy et ...
- **p. 3 / 2 METHOD - extractive body cue:** Given an initial state s0, a goal state sg and the transition dynamics p of a differentiable simulator, we use gradient-based trajectory optimization to solve ...
- **p. 3 / 2 METHOD - extractive body cue:** Published as a conference paper at ICLR 2022 f(o, g) s0 sim s1 a0 ... sT sim back propagation Loss a1 policy feasibility predictor skill ...
- **Contribution anchor:** p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 4 (2 METHOD), p. 4 (2 METHOD), p. 1 (1 INTRODUCTION), p. 3 (2 METHOD)

### Strongest assumption and failure boundary

- **p. 1 / 1 INTRODUCTION - extractive body cue:** These differentiable simulators have facilitated gradient-based trajectory optimizers to find a motion trajectory with much fewer samples, compared with black box optimizers such as CEM ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** This work aims to narrow the gap and develop a method named DiffSkill that learns to use tools like a rolling pin, spatula, knife, etc., ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** For example, while standard skills such as grasping an object or moving the robot arm from one pose to another may be manually specified (Toussaint ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** The recent development of differentiable physics simulators for deformable objects has shown promising results for solving soft-body control problems (Hu et al., 2019b; Murthy et ...
- **p. 6 / 3 EXPERIMENTS - extractive body cue:** In Table 3, we can see that the learned skills (labeled as Behavior Cloning) approach the normalized performance of the trajectory optimization (Trajectory Opt) on ...
- **p. 7 / 3 EXPERIMENTS - extractive body cue:** 3.4 RESULT ANALYSIS We show that DiffSkill is able to solve the challenging long-horizon, tool-use tasks from the sensory observation (RGB-D) while the baselines cannot.
- **p. 8 / 3 EXPERIMENTS - extractive body cue:** On the other hand, if we do not optimize for the intermediate goals, we also cannot determine which tools to use at evaluation time, since ...
- **Boundary to test:** In Table 3, we can see that the learned skills (labeled as Behavior Cloning) approach the normalized performance of the trajectory optimization (Trajectory Opt) on single-tool use, although they cannot solve the ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Our method consists of three components, (1) a trajectory optimizer that acts as an expert that applies gradient-based optimization on the differentiable simulator to obtain demonstration trajectories, which requires the full state ... | p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Reported outcome | Each entry shows the normalized improvement / success rate. | p. 7 (3 EXPERIMENTS), p. 7 (3 EXPERIMENTS) |
| Failure/limitation | In Table 3, we can see that the learned skills (labeled as Behavior Cloning) approach the normalized performance of the trajectory optimization (Trajectory Opt) on single-tool use, although they cannot solve the ... | p. 6 (3 EXPERIMENTS), p. 7 (3 EXPERIMENTS) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `RGB-D/point cloud, object state와 contact/task observation → object geometry, affordance, contact mode 또는 end-effector state → grasp, pose, force 또는 end-effector trajectory`.
- 이 논문의 재사용 가능한 지점은 Our neural skill abstraction consists of a goal-conditioned policy that takes a sensory observation (RGB-D images in our case) as input, a feasibility and reward predictor, as well as a variational auto-encoder ...를 Our method consists of three components, (1) a trajectory optimizer that acts as an expert that applies gradient-based optimization on the differentiable simulator to obtain demonstration trajectories, which requires the full state ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 object geometry, affordance, contact mode 또는 end-effector state가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 In Table 3, we can see that the learned skills (labeled as Behavior Cloning) approach the normalized performance of the trajectory optimization (Trajectory Opt) on single-tool use, although they cannot solve the ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Our method consists of three components, (1) a trajectory optimizer that acts as an expert that applies gradient-based optimization on the differentiable simulator to obtain demonstration trajectories, which requires the full state ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `Manipulation, contact, tactile, and dexterity`; tags: `Robotics, deformable object, tool use, differentiable physics, skill abstraction, Planning`.
- **Reading predecessor in the generated track queue:** SoftGym: Benchmarking Deep Reinforcement Learning for Deformable Object Manipulation (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Neural Descriptor Fields: SE(3)-Equivariant Object Representations for Manipulation (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** In Table 3, we can see that the learned skills (labeled as Behavior Cloning) approach the normalized performance of the trajectory optimization (Trajectory Opt) on single-tool use, although they cannot solve the ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: We build our simulation environments on top of PlasticineLab (Huang et al., 2021), a differentiable physics benchmark using the DiffTaichi system (Hu et al., 2019a) that could simulate plasticine-like objects based on ....
3. Compare against the body-reported baseline or a matched simpler baseline: 3.3 BASELINES We compare with three strong baselines: Model-free Reinforcement Learning (RL) We compare with two model-free RL methods: TD3 (Fujimoto et al., 2018) and SAC (Haarnoja et al., 2018)..
4. Report the body metric and its denominator/aggregation: After training, we find the feasibility and score predictor to perform well on the held out trajectories, achieving a L2 error of less than 0.05 for the score predictor and an accuracy ....
5. Re-run the body-reported ablation/failure condition: Figure 3: Visualization of the generated plan and the corresponding execution. The plan generated by DiffSkill is shown in the left, where the first and the last image are the given initial ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 3 (2 METHOD), p. 3 (2 METHOD), p. 2 (2 METHOD); the primary result is directionally consistent at p. 7 (3 EXPERIMENTS), p. 7 (3 EXPERIMENTS), p. 8 (3 EXPERIMENTS); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 consists, three, components mechanism이 3.3 BASELINES We compare with three strong baselines: Model-free Reinforcement Learning (RL) We compare with two ... 대비 After training, we find the feasibility and score predictor to perform well on the held out trajectories, achieving ...을 개선하고, In Table 3, we can see that the learned skills (labeled as Behavior Cloning) approach the ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
