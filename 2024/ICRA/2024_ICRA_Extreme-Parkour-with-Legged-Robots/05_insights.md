# Insights — Extreme Parkour with Legged Robots

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2309.14341; PDF retrieval source: https://arxiv.org/pdf/2309.14341. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 3 / 1 Introduction - extractive body cue:** To allow the robot to adjust itself as per the obstacle type at deployment, we propose a novel dual distillation method.
- **p. 3 / 1 Introduction - extractive body cue:** Below, we summarize the main contributions: • A novel dual distillation method for distilling both agile motor commands and rapidly fluctuating heading directions from depth ...
- **p. 5 / 3 Method - extractive body cue:** We present a simple, unified reward formulation from which diverse behaviors emerge automatically and are perfectly adapted to the terrain geometry.
- **p. 6 / 3 Method - extractive body cue:** To overcome this issue, we propose to use a mixture of teacher and student (MTS).
- **p. 6 / 3 Method - extractive body cue:** To explore this diversity, we introduce a term to track a desired forward vector using the same inner product design principle, which can be controlled ...
- **p. 6 / 3 Method - extractive body cue:** 3.2 Reinforcement Learning from Scandots (Phase 1) We use the above rewards to learn a policy using model-free RL [33] in simulation.
- **p. 5 / 3 Method - extractive body cue:** We use Regularized Online Adaptation (ROA)[9] to train an estimator to recover environmental information from the history of observations.
- **Contribution anchor:** p. 3 (1 Introduction), p. 3 (1 Introduction), p. 5 (3 Method), p. 6 (3 Method), p. 6 (3 Method), p. 6 (3 Method)

### Strongest assumption and failure boundary

- **p. 3 / 1 Introduction - extractive body cue:** However, low cost poses a new challenge for parkour which is not as prominent in prior walking works.
- **p. 3 / 1 Introduction - extractive body cue:** All these challenges are not feasible with such an approach.
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 7: For each terrain, we run 5 trials and record the number of successes. We find that ours has 20-80% higher success rate on ...
- **p. 8 / 4 Results - extractive body cue:** Noisy is able to get some performance but has very large variance since it can rely on collisions with its legs to sense terrain geometry ...
- **p. 9 / 4 Results - extractive body cue:** These sudden adjustments are out-ofdistribution for the policy and it cannot adapt fast enough, causing it to fail.
- **p. 8 / 4 Results - extractive body cue:** NoClear achieves slightly higher performance but it places feet close to the obstacle edges which is unstable in the real world.
- **Boundary to test:** Figure 7: For each terrain, we run 5 trials and record the number of successes. We find that ours has 20-80% higher success rate on the most difficult instance of each terrain. ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | To allow the robot to adjust itself as per the obstacle type at deployment, we propose a novel dual distillation method. | p. 3 (1 Introduction), p. 3 (1 Introduction) |
| Reported outcome | In addition, its feet clearance also helps it to achieve some performance with noisy measurements. | p. 8 (4 Results), p. 8 (4 Results) |
| Failure/limitation | Figure 7: For each terrain, we run 5 trials and record the number of successes. We find that ours has 20-80% higher success rate on the most difficult instance of each terrain. ... | p. 9 (Figure/Table caption), p. 8 (4 Results) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `proprioception, terrain/perception observation과 velocity command → body/contact state, foothold 또는 behavior mode → joint target, torque, footstep 또는 locomotion action`.
- 이 논문의 재사용 가능한 지점은 As a result at deployment, the policy not only outputs agile motor commands but also rapidly adjusts heading directions all from input depth image.를 This policy takes as input, the proprioception x, scandots m, target heading ˆd, walking flag W and commanded speed vcmd.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 body/contact state, foothold 또는 behavior mode가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Figure 7: For each terrain, we run 5 trials and record the number of successes. We find that ours has 20-80% higher success rate on the most difficult instance of each terrain. ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: To allow the robot to adjust itself as per the obstacle type at deployment, we propose a novel dual distillation method.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `Locomotion, whole-body, mobile manipulation, and humanoids`; tags: `Robotics, quadruped locomotion, parkour, Reinforcement Learning`.
- **Reading predecessor in the generated track queue:** Learning Quadrupedal Locomotion over Challenging Terrain (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Walk These Ways: Tuning Robot Control for Generalization with Multiplicity of Behavior (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Figure 7: For each terrain, we run 5 trials and record the number of successes. We find that ours has 20-80% higher success rate on the most difficult instance of each terrain. ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Starred is recent concurrent work [47]. baseline comparison in simulation since it is infeasible to provide human joystick commands and provide real-world comparisons instead..
3. Compare against the body-reported baseline or a matched simpler baseline: We find that our method outperforms the baselines in terms of both metrics..
4. Report the body metric and its denominator/aggregation: We find that ours has much higher success rate in all environments..
5. Re-run the body-reported ablation/failure condition: Figure 1: Extreme Parkour: Low-cost robot with imprecise actuation can perform precise athletic behaviors directly from a high-dimensional image without any explicit mapping and planning. The robot is able to long jump ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 6 (3 Method), p. 5 (3 Method), p. 5 (3 Method); the primary result is directionally consistent at p. 8 (4 Results), p. 8 (4 Results), p. 9 (4 Results); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 allow, robot, adjust mechanism이 We find that our method outperforms the baselines in terms of both metrics. 대비 We find that ours has much higher success rate in all environments.을 개선하고, Figure 7: For each terrain, we run 5 trials and record the number of successes. We ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
