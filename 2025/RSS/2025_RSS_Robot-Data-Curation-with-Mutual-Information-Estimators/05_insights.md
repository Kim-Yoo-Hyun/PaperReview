# Insights — Robot Data Curation with Mutual Information Estimators

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (19 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p023.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p023.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 4 / V. MetHop - extractive body cue:** come this challenge we propose Demonstration Information Estimation, which uses k-nearest-neighbor (k-NN) estimates of mutual information, Our method involves three steps - representation learning, mutual ...
- **p. 4 / V. MetHop - extractive body cue:** In this section we propose the Demonstration Information Estimation (DemInf) method for computationally estimating mutual information for demonstration data, Though mutual information is usually considered ...
- **p. 1 / Abstract - extractive body cue:** Moreover, training polices based on data filtered bby our method leads to a §-10% improvement in RoboMimic and better performance on real ALOHA and Franka ...
- **p. 2 / 1. Iyrropucrion - extractive body cue:** To address this problem, we introduce Demonstration Information Estimation ‘or Deming for short.
- **p. 2 / 1. Iyrropucrion - extractive body cue:** For text data, this often consists of simple n-gram classifiers, or metadata filtering, which have been shown to have a large impact oon performance [72].
- **p. 18 / C. Implementation Derails - extractive body cue:** For action encoders and decoders, we use the same architecture as for state.
- **p. 18 / C. Implementation Derails - extractive body cue:** For all methods using a state encoder, we use this architecture.
- **Contribution anchor:** p. 4 (V. MetHop), p. 4 (V. MetHop), p. 1 (Abstract), p. 2 (1. Iyrropucrion), p. 2 (1. Iyrropucrion), p. 18 (C. Implementation Derails)

### Strongest assumption and failure boundary

- **p. 1 / 1. Iyrropucrion - extractive body cue:** In robotics, we often do not have access to data at a similar scale due to the difficulty and cost of collection Moreover. even if ...
- **p. 3 / B. Demonstration Curation - extractive body cue:** This is a more difficult problem than considered in prior work.
- **p. 3 / B. Demonstration Curation - extractive body cue:** Moreover, choices made Within individual demonstrations 7, such as using differing strategies or varied approaches to complete a task, might make learning from the overall ...
- **p. 4 / V. MetHop - extractive body cue:** ‘Though mutual information is perhaps a natural metric for data curation, it can be practically difficult to estimate [19].
- **p. 4 / I N\ - extractive body cue:** It can be difficult for a policy to fit ‘demonstrations when the data collector has access to information unavailable to the policy.
- **p. 8 / C. Mutual Information Estimators - extractive body cue:** variance across seeds, while the parametric estimators were more unstable and had one or two runs that performed far worse than the others.
- **p. 6 / A. Experimental Setup - extractive body cue:** Note that while this metric makes sense for active learning, it does not necessarily make sense in the offline setting, and in some ways may ...
- **Boundary to test:** variance across seeds, while the parametric estimators were more unstable and had one or two runs that performed far worse than the others.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | come this challenge we propose Demonstration Information Estimation, which uses k-nearest-neighbor (k-NN) estimates of mutual information, Our method involves three steps - representation learning, mutual information estimation, and sco ... | p. 4 (V. MetHop), p. 4 (V. MetHop) |
| Reported outcome | Following Gandhi et al, [25], we use a measure of demonstration "compatibility" to score data. | p. 6 (A. Experimental Setup), p. 6 (A. Experimental Setup) |
| Failure/limitation | variance across seeds, while the parametric estimators were more unstable and had one or two runs that performed far worse than the others. | p. 8 (C. Mutual Information Estimators), p. 6 (A. Experimental Setup) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `observation history와 expert trajectory/action → behavior policy와 temporal action context → predicted action 또는 action chunk`.
- 이 논문의 재사용 가능한 지점은 In contrast, we believe metrics for imitation learning should be able to measure the relative predictability of the state-action distribution directly, which affects how well a policy is able to fit the ...를 Broadly, the objective of imitation learning is to learn a policy x» : S > A parameterized by 6 that is able to effectively reproduce the behavior of an expert x within ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 behavior policy와 temporal action context가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 variance across seeds, while the parametric estimators were more unstable and had one or two runs that performed far worse than the others.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: come this challenge we propose Demonstration Information Estimation, which uses k-nearest-neighbor (k-NN) estimates of mutual information, Our method involves three steps - representation learning, mutual information estimation, and sco ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `RL, IL, offline learning, and robot data`; tags: `Robotics, Imitation Learning, data curation, demonstrations`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** variance across seeds, while the parametric estimators were more unstable and had one or two runs that performed far worse than the others.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: The multi-human datasets from the RoboMimic benchmark [50] include 100 demonstrations from each of three robot operators for three tasks in increasing difficulty: "Lift" where the robot simply lifts a cube, "Can" ....
3. Compare against the body-reported baseline or a matched simpler baseline: 2) Baselines: We compare against a number of different data quality estimators from prior work in addition to a number of alternative mutual information estimators, which we label with "(MI)"..
4. Report the body metric and its denominator/aggregation: Following Gandhi et al, [25], we use a measure of demonstration "compatibility" to score data..
5. Re-run the body-reported ablation/failure condition: We additionally evaluate on versions of these datasets ("HiChew", "TootsieRoll, "HersheyKiss") where the unstructured play data has been removed, but where demonstrations still contain task-relevant data of varying quality..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 18 (C. Implementation Derails), p. 18 (C. Implementation Derails), p. 4 (B. Maximizing Marginal Action Entropy); the primary result is directionally consistent at p. 6 (A. Experimental Setup), p. 6 (A. Experimental Setup), p. 7 (A. Experimental Setup); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 come, challenge, Demonstration mechanism이 2) Baselines: We compare against a number of different data quality estimators from prior work in ... 대비 Following Gandhi et al, [25], we use a measure of demonstration "compatibility" to score data.을 개선하고, variance across seeds, while the parametric estimators were more unstable and had one or two runs ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
