# Insights — MT-Opt: Continuous Multi-Task Robotic Reinforcement Learning at Scale

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2104.08212; PDF retrieval source: https://arxiv.org/abs/2104.08212. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / I. INTRODUCTION - extractive body cue:** We further make the following contributions: • We address the challenge of providing rewards by creating a scalable and intuitive success-classifier-based approach that allows to ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** D) Sample of behaviorally and visually distinct tasks such as covering, chasing, alignment, which we show our method can adapt to.
- **p. 2 / I. INTRODUCTION - extractive body cue:** We present our multi-task system as well as examples of some of the tasks that it is capable of performing in Fig.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Can we instead amortize the cost of learning this repertoire over multiple skills, where the effort needed to learn whole repertoire is reduced, easier skills ...
- **p. 4 / III. SYSTEM OVERVIEW - extractive body cue:** First, we discuss two base choices for the impersonation function fI, then we introduce a more principled solution.
- **p. 5 / V. REWARDS VIA MULTI-TASK SUCCESS DETECTORS - extractive body cue:** In fact, we use supervised learning to train a similar neural network architecture model (excluding the inputs responsible for action representation) as for the MT-Opt ...
- **p. 3 / III. SYSTEM OVERVIEW - extractive body cue:** First, we use a single, multi-task deep neural network to learn a policy for all the tasks simultaneously, which enables parameter sharing between tasks.
- **Contribution anchor:** p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 4 (III. SYSTEM OVERVIEW), p. 5 (V. REWARDS VIA MULTI-TASK SUCCESS DETECTORS)

### Strongest assumption and failure boundary

- **p. 2 / I. INTRODUCTION - extractive body cue:** However, to realize these benefits for a real-world robotic learning system, we need to overcome a number of major challenges [64, 32, 11, 86], which ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** In addition, by collecting experience simultaneously using controllers for a variety of tasks with different difficulty, arXiv:2104.08212v2 [cs.RO] 27 Apr 2021
- **p. 2 / I. INTRODUCTION - extractive body cue:** We further make the following contributions: • We address the challenge of providing rewards by creating a scalable and intuitive success-classifier-based approach that allows to ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** While existing methods are effective and able to generalize, they require considerable on-robot training time, as well as extensive engineering effort for setting up each ...
- **p. 8 / VII. EXPERIMENTS - extractive body cue:** These include the exact same set of successful lift-sausage episodes as MT-Opt, but does not include the failures from other tasks.
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 4: Video frames for the place-anywhere task. Success and failure videos are iteratively captured in pairs to mitigate correlations with spurious workspace features such ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 3: Path of episodes through task impersonation, where episodes are routed to train relevant tasks, and data re- balancing where the ratio of success ...
- **Boundary to test:** These include the exact same set of successful lift-sausage episodes as MT-Opt, but does not include the failures from other tasks.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | We further make the following contributions: • We address the challenge of providing rewards by creating a scalable and intuitive success-classifier-based approach that allows to quickly define new tasks and their rewards. ... | p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION) |
| Reported outcome | Looking at the average performance across all task, we observe that MT-Opt significantly outperforms the baselines, in some cases with ≈3× average improvement. | p. 7 (VII. EXPERIMENTS), p. 7 (VII. EXPERIMENTS) |
| Failure/limitation | These include the exact same set of successful lift-sausage episodes as MT-Opt, but does not include the failures from other tasks. | p. 8 (VII. EXPERIMENTS), p. 5 (Figure/Table caption) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `multi-view observation, language/task label과 action trajectory → shared representation, embodiment/task identity와 data distribution → dataset sample 또는 learned policy action`.
- 이 논문의 재사용 가능한 지점은 At each time step, the policy selects an action a given the current state s and the current task Ti that is set at the beginning of the episode, and receives a ...를 2C), at each time step, a policy takes as input a camera image and a one-hot encoding of the task, and sends a motor command to the robot.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 shared representation, embodiment/task identity와 data distribution가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 These include the exact same set of successful lift-sausage episodes as MT-Opt, but does not include the failures from other tasks.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: We further make the following contributions: • We address the challenge of providing rewards by creating a scalable and intuitive success-classifier-based approach that allows to quickly define new tasks and their rewards. ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `RL, IL, offline learning, and robot data`; tags: `Robotics, Reinforcement Learning, Multi-Task Learning, robot data, Google DeepMind`.
- **Reading predecessor in the generated track queue:** Maximum a Posteriori Policy Optimisation (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Isaac Gym: High Performance GPU Based Physics Simulation For Robot Learning (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** These include the exact same set of successful lift-sausage episodes as MT-Opt, but does not include the failures from other tasks.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: The goal of our real-world experiments is to answer the following questions: (1) How does MT-Opt perform, quantitatively and qualitatively, on a large set of vision-based robotic manipulation tasks?.
3. Compare against the body-reported baseline or a matched simpler baseline: Looking at the average performance across all task, we observe that MT-Opt significantly outperforms the baselines, in some cases with ≈3× average improvement..
4. Report the body metric and its denominator/aggregation: 7 shows the success rates of MT-Opt on the 12 evaluation tasks..
5. Re-run the body-reported ablation/failure condition: Tasks such as lift-carrot and Parameter Sharing Ablation (Success Rate) Model: 2-Task Model 12-Task Model lift-any 0.82 0.89 place-any 0.63 0.85 TABLE I: The effect of parameter sharing: the policy that learns ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 5 (V. REWARDS VIA MULTI-TASK SUCCESS DETECTORS), p. 3 (III. SYSTEM OVERVIEW), p. 2 (I. INTRODUCTION); the primary result is directionally consistent at p. 7 (VII. EXPERIMENTS), p. 7 (VII. EXPERIMENTS), p. 8 (VII. EXPERIMENTS); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 further, make, following mechanism이 Looking at the average performance across all task, we observe that MT-Opt significantly outperforms the baselines, ... 대비 7 shows the success rates of MT-Opt on the 12 evaluation tasks.을 개선하고, These include the exact same set of successful lift-sausage episodes as MT-Opt, but does not include ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
