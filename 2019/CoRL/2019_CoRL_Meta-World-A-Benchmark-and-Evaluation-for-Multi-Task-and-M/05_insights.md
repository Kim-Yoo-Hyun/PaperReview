# Insights — Meta-World: A Benchmark and Evaluation for Multi-Task and Meta Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v100/yu20a.html; PDF retrieval source: https://proceedings.mlr.press/v100/yu20a/yu20a.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1 Introduction - extractive body cue:** To this end, we present a benchmark of simulated manipulation tasks with everyday objects, all of which are contained in a shared, table-top environment with ...
- **p. 2 / 1 Introduction - extractive body cue:** For example, one popular evaluation of metalearning involves choosing different running directions for simulated legged robots [10], which then enables fast adaptation to new directions.
- **p. 1 / Abstract - extractive body cue:** In this paper, we propose an open-source simulated benchmark for meta-reinforcement learning and multitask learning consisting of 50 distinct robotic manipulation tasks.
- **p. 1 / Abstract - extractive body cue:** Our aim is to make it possible to develop algorithms that generalize to accelerate the acquisition of entirely new, held-out tasks.
- **p. 1 / Abstract - extractive body cue:** We evaluate 6 state-of-the-art meta-reinforcement learning and multi-task learning algorithms on these tasks.
- **p. 2 / 1 Introduction - extractive body cue:** This opens the door for future developments in multi-task and meta reinforcement learning: instead of focusing on further increasing performance on current narrow task suites, ...
- **p. 2 / 1 Introduction - extractive body cue:** In order to study the capabilities of current multi-task and meta-reinforcement learning methods and make it feasible to design new algorithms that actually generalize and ...
- **Contribution anchor:** p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (Abstract), p. 1 (Abstract), p. 1 (Abstract), p. 2 (1 Introduction)

### Strongest assumption and failure boundary

- **p. 2 / 1 Introduction - extractive body cue:** We provide an evaluation protocol with evaluation modes of varying difficulty, and observe that current methods only show success in the easiest modes.
- **p. 2 / 1 Introduction - extractive body cue:** Our empirical evaluation of existing methods on this benchmark reveals that, despite some impressive progress in multi-task and meta-reinforcement learning over the past few years, ...
- **p. 1 / 1 Introduction - extractive body cue:** Recent works in meta-learning and multi-task reinforcement learning have shown promise for addressing this gap.
- **p. 1 / 1 Introduction - extractive body cue:** Recent advances in machine learning have provided unparalleled generalization capabilities in domains such as images [6] and speech [7], suggesting that this should be possible; ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5: Quantitative results on MT10, MT50, ML10, and ML45. Note that, even on the challenging ML10 and ML45 benchmarks, current methods already exhibit some ...
- **p. 1 / Abstract - extractive body cue:** When policies are meta-trained on such narrow task distributions, they cannot possibly generalize to more quickly acquire entirely new tasks.
- **p. 7 / 2 Related Work - extractive body cue:** Our experiments show that current meta-RL methods in fact cannot yet generalize effectively to entirely new tasks and do not even learn the meta-training tasks ...
- **Boundary to test:** Figure 5: Quantitative results on MT10, MT50, ML10, and ML45. Note that, even on the challenging ML10 and ML45 benchmarks, current methods already exhibit some degree of generalization, but meta-training per- formance ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | To this end, we present a benchmark of simulated manipulation tasks with everyday objects, all of which are contained in a shared, table-top environment with a simulated Sawyer arm. | p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Reported outcome | Figure 5: Quantitative results on MT10, MT50, ML10, and ML45. Note that, even on the challenging ML10 and ML45 benchmarks, current methods already exhibit some degree of generalization, but meta-training per- formance ... | p. 8 (Figure/Table caption), p. 1 (1 Introduction) |
| Failure/limitation | Figure 5: Quantitative results on MT10, MT50, ML10, and ML45. Note that, even on the challenging ML10 and ML45 benchmarks, current methods already exhibit some degree of generalization, but meta-training per- formance ... | p. 8 (Figure/Table caption), p. 1 (Abstract) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `standardized observation, action, task state와 evaluation split → benchmark state/goal와 method decision → policy/controller trajectory 또는 measured result`.
- 이 논문의 재사용 가능한 지점은 We evaluate 6 state-of-the-art meta-reinforcement learning and multi-task learning algorithms on these tasks.를 While reinforcement learning (RL) has achieved some success in domains such as assembly [1], ping pong [2], in-hand manipulation [3], and hockey [4], state-of-the-art methods require substantially more experience than humans to ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 benchmark state/goal와 method decision가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Figure 5: Quantitative results on MT10, MT50, ML10, and ML45. Note that, even on the challenging ML10 and ML45 benchmarks, current methods already exhibit some degree of generalization, but meta-training per- formance ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: To this end, we present a benchmark of simulated manipulation tasks with everyday objects, all of which are contained in a shared, table-top environment with a simulated Sawyer arm.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `Manipulation, contact, tactile, and dexterity`; tags: `Robotics, Benchmark, Reinforcement Learning, manipulation`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Figure 5: Quantitative results on MT10, MT50, ML10, and ML45. Note that, even on the challenging ML10 and ML45 benchmarks, current methods already exhibit some degree of generalization, but meta-training per- formance ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: For example, a commonly used meta-reinforcement learning benchmark uses different running velocities for a simulated robot as different tasks..
3. Compare against the body-reported baseline or a matched simpler baseline: We evaluate 6 state-of-the-art meta-reinforcement learning and multi-task learning algorithms on these tasks..
4. Report the body metric and its denominator/aggregation: Figure 8: Learning curves of all methods on MT10, ML10, MT50, and ML45 benchmarks. Y- axis represents success rate averaged over tasks in percentage (%). Off-policy algorithms such as multi-task SAC and ....
5. Re-run the body-reported ablation/failure condition: Figure 2. Introducing this parametric variability not only creates a substantially larger (infinite) variety of tasks, but also makes it substantially more practical to expect that a meta-trained model will generalize to ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 1 (Abstract), p. 1 (Abstract), p. 2 (1 Introduction); the primary result is directionally consistent at p. 8 (Figure/Table caption), p. 1 (1 Introduction), p. 13 (Figure/Table caption); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 present, benchmark, simulated mechanism이 We evaluate 6 state-of-the-art meta-reinforcement learning and multi-task learning algorithms on these tasks. 대비 Figure 8: Learning curves of all methods on MT10, ML10, MT50, and ML45 benchmarks. Y- axis represents success ...을 개선하고, Figure 5: Quantitative results on MT10, MT50, ML10, and ML45. Note that, even on the challenging ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
