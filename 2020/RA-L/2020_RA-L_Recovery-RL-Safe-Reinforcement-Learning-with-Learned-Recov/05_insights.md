# Insights — Recovery RL: Safe Reinforcement Learning with Learned Recovery Zones

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2010.15920; PDF retrieval source: https://arxiv.org/pdf/2010.15920. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / I. INTRODUCTION - extractive body cue:** Thus, endowing RL agents with the ability to satisfy constraints during learning not only enables robots to interact safely, but also allows them to more ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** We present Recovery RL, a new algorithm for safe robotic RL.
- **p. 1 / I. INTRODUCTION - extractive body cue:** If it tips over the carton, then not only can this possibly break the carton and create a mess, but it also requires laborious human ...
- **p. 3 / III. PROBLEM STATEMENT - extractive body cue:** We present an algorithm to optimize equation (III.1) by utilizing a pair of policies, a task policy πtask, which is trained to maximize Rπ over ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Separating the task and recovery policies makes it easier to balance task performance and safety, and allows using off-the-shelf RL algorithms for both.
- **p. 5 / IV. RECOVERY RL - extractive body cue:** [8] to plan over a learned stochastic dynamics model, while for tasks with visual observations, we use a VAE based latent dynamics model.
- **p. 1 / Abstract - extractive body cue:** We propose Recovery RL, an algorithm which navigates this tradeoff by (1) leveraging offline data to learn about constraint violating zones before policy learning and ...
- **Contribution anchor:** p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 3 (III. PROBLEM STATEMENT), p. 2 (I. INTRODUCTION), p. 5 (IV. RECOVERY RL)

### Strongest assumption and failure boundary

- **p. 1 / I. INTRODUCTION - extractive body cue:** However, when deploying RL agents in the real world, unconstrained exploration can result in highly suboptimal behaviors which can damage the robot, break surroundings objects, ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** While these approaches are appealing for their generality and simplicity, there are two key aspects which make them difficult to use in practice.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Most prior work in safe RL integrates constraint satisfaction into the task objective to arXiv:2010.15920v2 [cs.LG] 17 May 2021
- **p. 2 / I. INTRODUCTION - extractive body cue:** We evaluate Recovery RL on an imagebased obstacle avoidance task on a physical robot and find that it trades off constraint violations and task successes ...
- **p. 3 / III. PROBLEM STATEMENT - extractive body cue:** Setting εrisk = 0 as well results in a robust optimal control problem.
- **p. 6 / V. EXPERIMENTS - extractive body cue:** In all navigation tasks, we find that Recovery RL significantly outperforms prior methods with both model-free and model-based recovery policies, while for the object extraction ...
- **p. 7 / V. EXPERIMENTS - extractive body cue:** We hypothesize that the model-based recovery mechanism is better able to compensate for approximation errors in ˆQπ φ,risk, resulting in a more robust recovery policy.
- **Boundary to test:** In all navigation tasks, we find that Recovery RL significantly outperforms prior methods with both model-free and model-based recovery policies, while for the object extraction environments, Recovery RL with a model-based recovery ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Thus, endowing RL agents with the ability to satisfy constraints during learning not only enables robots to interact safely, but also allows them to more efficiently learn in the real world. | p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| Reported outcome | Results suggest that Recovery RL with both model-free and modelbased recovery mechanisms significantly outperform prior algorithms across all 3 2D pointmass navigation environments | p. 6 (V. EXPERIMENTS), p. 6 (Figure/Table caption) |
| Failure/limitation | In all navigation tasks, we find that Recovery RL significantly outperforms prior methods with both model-free and model-based recovery policies, while for the object extraction environments, Recovery RL with a model-based recovery ... | p. 6 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `observation, uncertainty/risk estimate와 task command → safe set, recovery state 또는 constraint margin → shielded, recovery 또는 safe action`.
- 이 논문의 재사용 가능한 지점은 We present an algorithm to optimize equation (III.1) by utilizing a pair of policies, a task policy πtask, which is trained to maximize Rπ over πtask ∈Π and a recovery policy πrec, ...를 If the task policy πtask proposes an action aπtask at state s such that (s,aπtask)̸ ∈T π safe, then a recovery action sampled from πrec is executed instead of aπtask.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 safe set, recovery state 또는 constraint margin가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 In all navigation tasks, we find that Recovery RL significantly outperforms prior methods with both model-free and model-based recovery policies, while for the object extraction environments, Recovery RL with a model-based recovery ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Thus, endowing RL agents with the ability to satisfy constraints during learning not only enables robots to interact safely, but also allows them to more efficiently learn in the real world.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `CORE` in `World models, safety, uncertainty, and recovery`; tags: `Robotics, safe reinforcement learning, recovery policy, real robot`.
- **Reading predecessor in the generated track queue:** Control Barrier Function Based Quadratic Programs for Safety Critical Systems (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** DreamGen: Unlocking Generalization in Robot Learning through Video World Models (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** In all navigation tasks, we find that Recovery RL significantly outperforms prior methods with both model-free and model-based recovery policies, while for the object extraction environments, Recovery RL with a model-based recovery ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Domains: We evaluate Recovery RL on a set of 6 simulation domains (Figure 3) and an image-based obstacle avoidance task on a physical robot (Figure 6)..
3. Compare against the body-reported baseline or a matched simpler baseline: Results suggest that Recovery RL with both model-free and modelbased recovery mechanisms significantly outperform prior algorithms across all 3 2D pointmass navigation environments.
4. Report the body metric and its denominator/aggregation: We find that Recovery RL violates constraints less often than comparisons while maintaining a similar task success rate and more efficiently optimizing the task reward..
5. Re-run the body-reported ablation/failure condition: Ablations: We ablate different components of Recovery RL and study the sensitivity of Recovery RL to the number of transitions in Doffline for the Object Extraction domain in Figure 7..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 5 (IV. RECOVERY RL), p. 1 (Abstract), p. 2 (I. INTRODUCTION); the primary result is directionally consistent at p. 6 (V. EXPERIMENTS), p. 6 (Figure/Table caption), p. 7 (V. EXPERIMENTS); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 Thus, endowing, agents mechanism이 Results suggest that Recovery RL with both model-free and modelbased recovery mechanisms significantly outperform prior algorithms ... 대비 We find that Recovery RL violates constraints less often than comparisons while maintaining a similar task success rate ...을 개선하고, In all navigation tasks, we find that Recovery RL significantly outperforms prior methods with both model-free ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
