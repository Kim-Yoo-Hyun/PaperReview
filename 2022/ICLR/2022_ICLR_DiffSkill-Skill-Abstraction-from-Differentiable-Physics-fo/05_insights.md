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
- **p. 3 / 2 METHOD - extractive body cue:** f(o, g) s0 sim s1 a0 ... sT sim back propagation Loss a1 policy feasibility predictor skill ...
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

- **Paper-specific interface:** Our neural skill abstraction consists of a goal-conditioned policy that takes a sensory observation (RGB-D images in our case) as input, a feasibility and reward predictor, as well as a ... (p. 4, 2 METHOD).
- **Paper-specific mechanism:** To extend the use of differentiable physics models to these long-horizon tasks and enable the agent to directly consume visual observations, we propose DiffSkill: a novel framework where the agent ... (p. 2, 1 INTRODUCTION).
- **Evidence boundary:** the reported outcome is Method Task LiftSpread GatherTransport CutRearrange No Discrete Planning 0.758 / 20% 0.312 / 0% 0.118 / 0% Direct Execution (Random) 0.593 / 15% 0.369 / 0% 0.018 / 2.5% Direct ... (p. 8, 3 EXPERIMENTS); the relevant task/metric cue is After training, we find the feasibility and score predictor to perform well on the held out trajectories, achieving a L2 error of less than 0.05 for the score predictor and ... (p. 6, 3 EXPERIMENTS). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** This threshold is manually picked by observing the performance gap between successful and failed trajectories. (p. 6, 3 EXPERIMENTS).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `Manipulation, contact, tactile, and dexterity`; tags: `Robotics, deformable object, tool use, differentiable physics, skill abstraction, Planning`.
- **Reading predecessor in the generated track queue:** SoftGym: Benchmarking Deep Reinforcement Learning for Deformable Object Manipulation (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Neural Descriptor Fields: SE(3)-Equivariant Object Representations for Manipulation (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** In Table 3, we can see that the learned skills (labeled as Behavior Cloning) approach the normalized performance of the trajectory optimization (Trajectory Opt) on single-tool use, although they cannot solve the ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: Our neural skill abstraction consists of a goal-conditioned policy that takes a sensory observation (RGB-D images in our case) as input, a feasibility and reward predictor, as well as a ... (p. 4, 2 METHOD); preserve the objective/update rule: Specifically, after each gradient update step of Adam, we project the current zi to the constraint set by setting zi = zi max(//zi//2/ √ M),1). (p. 5, 2 METHOD).
2. Use the paper-reported task/data/environment cue: We build our simulation environments on top of PlasticineLab (Huang et al., 2021), a differentiable physics benchmark using the DiffTaichi system (Hu et al., 2019a) that could simulate plasticine-like objects ... (p. 5, 3 EXPERIMENTS).
3. Compare against the reported or matched baseline: Method Task LiftSpread GatherTransport CutRearrange No Discrete Planning 0.758 / 20% 0.312 / 0% 0.118 / 0% Direct Execution (Random) 0.593 / 15% 0.369 / 0% 0.018 / 2.5% Direct ... (p. 8, 3 EXPERIMENTS).
4. Report the body metric with its denominator and aggregation: After training, we find the feasibility and score predictor to perform well on the held out trajectories, achieving a L2 error of less than 0.05 for the score predictor and ... (p. 6, 3 EXPERIMENTS).
5. Re-run the reported ablation or stress/failure condition: 3.5 ABLATION ANALYSIS We perform two ablations on DiffSkill. (p. 7, 3 EXPERIMENTS); if none is reported, design one around: This threshold is manually picked by observing the performance gap between successful and failed trajectories. (p. 6, 3 EXPERIMENTS).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), match the reported outcome at p. 8 (3 EXPERIMENTS), p. 5 (3 EXPERIMENTS), p. 6 (3 EXPERIMENTS), and measure the boundary at p. 6 (3 EXPERIMENTS), p. 8 (3 EXPERIMENTS).

## Falsifiable research question

Under the paper's stated interface (Our neural skill abstraction consists of a goal-conditioned policy that takes a sensory observation (RGB-D images in our case) as input, a ...), does the paper-specific mechanism (To extend the use of differentiable physics models to these long-horizon tasks and enable the agent to directly consume visual observations, we ...) retain the reported evaluation outcome (After training, we find the feasibility and score predictor to perform well on the held out trajectories, achieving ...) when tested against the paper's strongest explicit boundary (This threshold is manually picked by observing the performance gap between successful and failed trajectories.)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (After training, we find the feasibility and score predictor to perform well on the held out trajectories, achieving ...) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (14 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** To extend the use of differentiable physics models to these long-horizon tasks and enable the agent to directly consume visual observations, we propose DiffSkill: a novel framework where the agent ... (p. 2, 1 INTRODUCTION).
- **Paper-supported outcome:** Method Task LiftSpread GatherTransport CutRearrange No Discrete Planning 0.758 / 20% 0.312 / 0% 0.118 / 0% Direct Execution (Random) 0.593 / 15% 0.369 / 0% 0.018 / 2.5% Direct ... (p. 8, 3 EXPERIMENTS).
- **Strongest explicit boundary:** This threshold is manually picked by observing the performance gap between successful and failed trajectories. (p. 6, 3 EXPERIMENTS).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
