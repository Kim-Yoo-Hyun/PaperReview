# Insights — Offline Imitation Learning Through Graph Search and Retrieval

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss20/p054.html; PDF retrieval source: https://www.roboticsproceedings.org/rss20/p054.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / I. INTRODUCTION - extractive body cue:** As a direct approach that uses graph search rather than deep RL, our method enjoys high time efficiency.
- **p. 2 / I. INTRODUCTION - extractive body cue:** We also provide various quantitative and qualitative analyses to show that our method is capable of identifying good behaviors in the dataset.
- **p. 3 / IV. POLICY LEARNING - extractive body cue:** We introduce the implementation details in the remaining sections.
- **p. 4 / IV. POLICY LEARNING - extractive body cue:** To address the first problem, we propose to identify and connect similar states in the dataset to form a better distance estimate in section IV-B.
- **p. 5 / IV. POLICY LEARNING - extractive body cue:** The pseudo-code of our method is summarized in Algorithm 1.
- **p. 4 / IV. POLICY LEARNING - extractive body cue:** To identify similar states, we use the off-shelf pretrained vision models to compute features for similarity computation.
- **p. 4 / IV. POLICY LEARNING - extractive body cue:** Algorithm 1: GSR 1 [Optional] Finetune pretrained fθ on D; 2 Build graph G(V, E) using procedure in Section IV-B; 3 Set w[v] = 0 ...
- **Contribution anchor:** p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (IV. POLICY LEARNING), p. 4 (IV. POLICY LEARNING), p. 5 (IV. POLICY LEARNING), p. 4 (IV. POLICY LEARNING)

### Strongest assumption and failure boundary

- **p. 2 / I. INTRODUCTION - extractive body cue:** Moreover, there usually exist suboptimal behaviors within a successful demonstration, such as retrying to grip the item if the first attempt fails.
- **p. 2 / I. INTRODUCTION - extractive body cue:** Despite numerous challenges in both perception and action, our method can consistently improve baselines' success rate by 10% to 30% and proficiency by over 30%.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Despite the remarkable strides made so far, we notice that most existing works usually assume expert-level task demonstrations, while many real-world robotic manipulation tasks involve ...
- **p. 3 / III. PRELIMINARIES - extractive body cue:** Problem Formulation In this paper, we study an offline policy learning setup.
- **p. 8 / V. EXPERIMENTS - extractive body cue:** However, in many cases, they will get stuck or go out of distribution, leading to a complete failure.
- **p. 8 / V. EXPERIMENTS - extractive body cue:** Interestingly, we have the following findings: (1) All the temporal segments that lead to the failures are weakened and have low weights.
- **p. 6 / V. EXPERIMENTS - extractive body cue:** The robot is required to push a blue cylinder toward a green cube on the table. • Spoon Scooping In this task, the robot is ...
- **Boundary to test:** However, in many cases, they will get stuck or go out of distribution, leading to a complete failure.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | As a direct approach that uses graph search rather than deep RL, our method enjoys high time efficiency. | p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| Reported outcome | We find that our method can achieve a success rate greater than 80% in the considered task and outperform all baselines in execution time. | p. 7 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS) |
| Failure/limitation | However, in many cases, they will get stuck or go out of distribution, leading to a complete failure. | p. 8 (V. EXPERIMENTS), p. 8 (V. EXPERIMENTS) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `dataset state/observation, action, reward와 return-to-go → Q/value 또는 sequence-policy state → dataset-supported action sequence`.
- 이 논문의 재사용 가능한 지점은 If we define w(o, a) = exp(A(o, a)) where A is the advantage of taking action a at observation o, this corresponds to the policy extraction objective used in Advantage-Weighted Regression (AWR) ...를 Each trajectory τ is a sequence of observations o0:T and corresponding actions a0:T , i.e., τ = (o0, a0, o1, a1, ..., oT , aT ).로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 Q/value 또는 sequence-policy state가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 However, in many cases, they will get stuck or go out of distribution, leading to a complete failure.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: As a direct approach that uses graph search rather than deep RL, our method enjoys high time efficiency.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `RL, IL, offline learning, and robot data`; tags: `Robotics, Imitation Learning, offline learning, graph search, retrieval`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** However, in many cases, they will get stuck or go out of distribution, leading to a complete failure.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Bottom: Our real-world tasks. and Worse-Better20 (the whole worse-human dataset with 20% data of the better-human dataset). • Nut Assembly In this task, the robot is required to pick up a square ....
3. Compare against the body-reported baseline or a matched simpler baseline: We first study how much performance gain our method can achieve compared to the state-of-the-art imitation learning baseline..
4. Report the body metric and its denominator/aggregation: 3) Evaluation Metric: To evaluate the performance of a trained policy, we use the following metrics. • Success rate (SR) is defined as the number of task successes divided by the number ....
5. Re-run the body-reported ablation/failure condition: Hyperparameter Analysis Having known that our method indeed strengthened desired behavior, in this section, we further study the effect of the main hyperparameters in our algorithm: a) β1 and β2: These temperatures ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 4 (IV. POLICY LEARNING), p. 4 (IV. POLICY LEARNING), p. 5 (IV. POLICY LEARNING); the primary result is directionally consistent at p. 7 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 direct, uses, graph mechanism이 We first study how much performance gain our method can achieve compared to the state-of-the-art imitation ... 대비 3) Evaluation Metric: To evaluate the performance of a trained policy, we use the following metrics. • Success ...을 개선하고, However, in many cases, they will get stuck or go out of distribution, leading to a ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
