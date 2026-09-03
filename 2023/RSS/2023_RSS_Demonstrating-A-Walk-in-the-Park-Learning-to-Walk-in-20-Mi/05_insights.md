# Insights — Demonstrating A Walk in the Park: Learning to Walk in 20 Minutes With Model-Free Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (9 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://roboticsproceedings.org/rss19/p056.html; PDF retrieval source: https://arxiv.org/pdf/2208.07860. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / I. INTRODUCTION - extractive body cue:** Our main contribution is an empirical demonstration that current deep RL methods can effectively learn quadrupedal locomotion directly in the real world in under 20 ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Crucially, this does not require novel algorithmic components or any other unexpected innovation, but rather careful implementation of one of several existing algorithmic frameworks (and ...
- **p. 4 / B. Efficient Model-Free RL - extractive body cue:** DroQ [60] similarly allows for a higher update to data ratio by regularizing the critic networks with dropout [61] and layer normalization [65].
- **p. 4 / B. Efficient Model-Free RL - extractive body cue:** Our choice of algorithm and implementation is aimed at enabling real-time synchronous training, which we expand on in Section V.
- **p. 4 / B. Efficient Model-Free RL - extractive body cue:** Actor-critic methods have recently become significantly more sample-efficient by improving the training of the critic, thereby allowing more updates to the critic network for the ...
- **Contribution anchor:** p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 4 (B. Efficient Model-Free RL), p. 4 (B. Efficient Model-Free RL), p. 4 (B. Efficient Model-Free RL)

### Strongest assumption and failure boundary

- **p. 1 / I. INTRODUCTION - extractive body cue:** This result runs counter to the principles articulated in several prior works, which suggest either than simulated training is critical for robotic locomotion because the ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** While our results largely build on existing methods, we demonstrate for the first time that a careful combination of existing components can enable direct real-world ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Our main contribution is an empirical demonstration that current deep RL methods can effectively learn quadrupedal locomotion directly in the real world in under 20 ...
- **p. 4 / IV. SYSTEM DESIGN - extractive body cue:** In the simulator, we used p = [0.05, 0.7, -1.4]; however, during the early experiments in the real world, we found that p = [0.05, ...
- **p. 4 / IV. SYSTEM DESIGN - extractive body cue:** As such, such policies cannot trivially be further trained in the real world.
- **p. 5 / IV. SYSTEM DESIGN - extractive body cue:** During early experiments with the real robot, we found that using the forward velocity in the robot's local frame caused it to dive forward as ...
- **p. 5 / V. SIMULATION ANALYSIS - extractive body cue:** In particular, we confirm the efficacy of constraining the action space: we observe that the simulated agent cannot make any progress in the unconstrained action ...
- **Boundary to test:** In the simulator, we used p = [0.05, 0.7, -1.4]; however, during the early experiments in the real world, we found that p = [0.05, 0.9, -1.8] promotes safer exploration on a ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Our main contribution is an empirical demonstration that current deep RL methods can effectively learn quadrupedal locomotion directly in the real world in under 20 minutes. | p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION) |
| Reported outcome | From these results, we can conclude that a variety of regularization or normalization methods, if implemented and applied carefully, can all achieve a similar level of improvement in performance over their underlying ... | p. 6 (V. SIMULATION ANALYSIS), p. 5 (V. SIMULATION ANALYSIS) |
| Failure/limitation | In the simulator, we used p = [0.05, 0.7, -1.4]; however, during the early experiments in the real world, we found that p = [0.05, 0.9, -1.8] promotes safer exploration on a ... | p. 4 (IV. SYSTEM DESIGN), p. 4 (IV. SYSTEM DESIGN) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `proprioception, terrain/perception observation과 velocity command → body/contact state, foothold 또는 behavior mode → joint target, torque, footstep 또는 locomotion action`.
- 이 논문의 재사용 가능한 지점은 Reinforcement learning offers a promising alternative, acquiring effective control strategies directly through interaction with the real system, potentially right in the environment in which the robot will be situated.를 Experimental Design Training Statistics Simulation Real World Hardware Actions Resets Terrains Samples Hours Samples Hours Ours A1 PD targets Learned In/Outdoor 0 0 20 · 103 0.3 Wu et al.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 body/contact state, foothold 또는 behavior mode가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 In the simulator, we used p = [0.05, 0.7, -1.4]; however, during the early experiments in the real world, we found that p = [0.05, 0.9, -1.8] promotes safer exploration on a ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Our main contribution is an empirical demonstration that current deep RL methods can effectively learn quadrupedal locomotion directly in the real world in under 20 minutes.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `Locomotion, whole-body, mobile manipulation, and humanoids`; tags: `Robotics, quadruped locomotion, real-world reinforcement learning, sample efficiency`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** In the simulator, we used p = [0.05, 0.7, -1.4]; however, during the early experiments in the real world, we found that p = [0.05, 0.9, -1.8] promotes safer exploration on a ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: 3: Experimental evaluation of (a) performance for different value of the damping parameter for the position PD controller; (b) ablations of various task setup choices; (d) regularization and normalization methods for efficient ....
3. Compare against the body-reported baseline or a matched simpler baseline: Therefore, for the remaining ablations, we used the value of damping set to 10..
4. Report the body metric and its denominator/aggregation: To match the real-world setup, we simulate the official A1 model in MuJoCo, and used the same position controller and rewards as discussed in Section III-B..
5. Re-run the body-reported ablation/failure condition: 3: Experimental evaluation of (a) performance for different value of the damping parameter for the position PD controller; (b) ablations of various task setup choices; (d) regularization and normalization methods for efficient ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 4 (B. Efficient Model-Free RL), p. 4 (B. Efficient Model-Free RL); the primary result is directionally consistent at p. 6 (V. SIMULATION ANALYSIS), p. 5 (V. SIMULATION ANALYSIS), p. 5 (V. SIMULATION ANALYSIS); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 main, contribution, empirical mechanism이 Therefore, for the remaining ablations, we used the value of damping set to 10. 대비 To match the real-world setup, we simulate the official A1 model in MuJoCo, and used the same position ...을 개선하고, In the simulator, we used p = [0.05, 0.7, -1.4]; however, during the early experiments in ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
