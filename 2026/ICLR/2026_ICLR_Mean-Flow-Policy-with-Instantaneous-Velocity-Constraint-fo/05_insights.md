# Insights — Mean Flow Policy with Instantaneous Velocity Constraint for One-step Action Generation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (23 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=mIeKe74W43; PDF retrieval source: https://arxiv.org/pdf/2602.13810. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Our contributions are summarized threefold: • We propose a new flow-based policy, namely mean velocity policy (MVP), that enables fastest one-step action generation.
- **p. 3 / 3 METHOD - extractive body cue:** First, we introduce the mean velocity policy (MVP), showing how its integration with a "generateand-select" mechanism enables a direct mapping from noise to optimal actions.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** In this paper, we propose the mean velocity policy (MVP) as an affirmative answer.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To address this, we introduce an instantaneous velocity constraint (IVC) to compensate for the lack of boundary conditions.
- **p. 5 / 3 METHOD - extractive body cue:** Inspired by this, we introduce the instantaneous velocity constraint (IVC), a training objective that explicitly enforces a boundary condition at t.
- **p. 4 / 3 METHOD - extractive body cue:** The resulting action, a⋆, then serves three purposes: (1) interacting with the environment, (2) acting as the target action for policy training, and (3) calculating ...
- **p. 6 / 3 METHOD - extractive body cue:** The policy training loss Lpolicy combines the mean velocity model loss in Eq.
- **Contribution anchor:** p. 2 (1 INTRODUCTION), p. 3 (3 METHOD), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 5 (3 METHOD), p. 4 (3 METHOD)

### Strongest assumption and failure boundary

- **p. 1 / 1 INTRODUCTION - extractive body cue:** However, a key limitation of existing generative policies is their dependence on iterative multi-step refinement from noise to actions (Wang et al., 2024a; 2025; Ding ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** However, this ODE theoretically suffers from the problem of multiple solutions due to a lack of explicit boundary conditions, that is, the value at any ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Although the time-efficiency gains of MVP are very promising, its learning difficulty is higher than that of a standard flow policy.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** While existing flow policies learn instantaneous velocities and require multistep iterative sampling (Lipman et al., 2023; Park et al., 2025; Bharadhwaj et al., 2024), MVP ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2: Velocity field: blue arrows de- note the mean velocity over a time in- terval, with red arrows representing the instantaneous velocity at a ...
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** The poor performance of BFN and QC is primarily because they rely on a 10-step flow policy, which requires iterative computation to transform noise into ...
- **Boundary to test:** Figure 2: Velocity field: blue arrows de- note the mean velocity over a time in- terval, with red arrows representing the instantaneous velocity at a time point. In RL, a policy π(·/s) ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Our contributions are summarized threefold: • We propose a new flow-based policy, namely mean velocity policy (MVP), that enables fastest one-step action generation. | p. 2 (1 INTRODUCTION), p. 3 (3 METHOD) |
| Reported outcome | Specifically, MVP consistently outperforms all baselines on Robomimic-square, Cube-doubletask4, and all Cube-triple tasks, where it consistently achieves the highest success rates. | p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS) |
| Failure/limitation | Figure 2: Velocity field: blue arrows de- note the mean velocity over a time in- terval, with red arrows representing the instantaneous velocity at a time point. In RL, a policy π(·/s) ... | p. 3 (Figure/Table caption), p. 9 (4 EXPERIMENTS) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `multi-view observation, language/task label과 action trajectory → shared representation, embodiment/task identity와 data distribution → dataset sample 또는 learned policy action`.
- 이 논문의 재사용 가능한 지점은 For standard flow-based policies, this mapping is framed as a generative process: a velocity model, v(a(t), t, s), transforms a standard Gaussian noise (source) into the optimal action (target), with the state ...를 (1) Grounded in the off-policy learning paradigm, our approach utilizes an action-value function (Qfunction) to guide policy improvement, which denotes the expected cumulative return for taking an action a in a state ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 shared representation, embodiment/task identity와 data distribution가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Figure 2: Velocity field: blue arrows de- note the mean velocity over a time in- terval, with red arrows representing the instantaneous velocity at a time point. In RL, a policy π(·/s) ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Our contributions are summarized threefold: • We propose a new flow-based policy, namely mean velocity policy (MVP), that enables fastest one-step action generation.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `Manipulation, contact, tactile, and dexterity`; tags: `Robotics, flow policy, one-step generation, manipulation`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Figure 2: Velocity field: blue arrows de- note the mean velocity over a time in- terval, with red arrows representing the instantaneous velocity at a time point. In RL, a policy π(·/s) ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: We consider a total of 9 sparse-reward robotic manipulation tasks with varying difficulties..
3. Compare against the body-reported baseline or a matched simpler baseline: Figure 4: Training curves of ablation on the IVC. (2) Comparison with one-step variants of the aforementioned baselines. We compared our MVP against one-step variants of the aforementioned baselines: FQL-Onestep, BFN-Onestep, and ....
4. Report the body metric and its denominator/aggregation: Overall, our MVP secures the top position with an average success rate of 0.88 ± 0.05..
5. Re-run the body-reported ablation/failure condition: Our full version (λ = 1.0) was compared against variants with a reduced constraint (λ = 0.5) and without the constraint (λ = 0.0)..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 3 (3 METHOD), p. 5 (3 METHOD), p. 4 (3 METHOD); the primary result is directionally consistent at p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 contributions, summarized, threefold mechanism이 Figure 4: Training curves of ablation on the IVC. (2) Comparison with one-step variants of the ... 대비 Overall, our MVP secures the top position with an average success rate of 0.88 ± 0.05.을 개선하고, Figure 2: Velocity field: blue arrows de- note the mean velocity over a time in- terval, ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
