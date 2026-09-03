# Insights — SurRoL: An Open-source Reinforcement Learning Centered and dVRK Compatible Platform for Surgical Robot Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://ieeexplore.ieee.org/document/9635867; PDF retrieval source: https://arxiv.org/pdf/2108.13035. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / I. INTRODUCTION - extractive body cue:** Our main contributions are summarized as follows: • We design an open-source surgical robot learning simulation platform centered on reinforcement learning for surgical skills, which ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Further, the designed SurRoL with carefully modeled assets can successfully deal with more realistic physical interactions.
- **p. 2 / III. METHODS - extractive body cue:** Finally, ten surgical learning-based tasks are built for algorithm development and evaluation.
- **p. 2 / I. INTRODUCTION - extractive body cue:** SurRoL provides dVRK compatible simulation environments for surgical robot learning (left), with Gym-like interfaces for reinforcement learning algorithm development and ranges of surgical contents with ...
- **p. 2 / III. METHODS - extractive body cue:** SurRoL builds on top of the open-source PyBullet because of its state-of-the-art physics simulation, wide adoption in the machine learning community, and removal of the ...
- **Contribution anchor:** p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (III. METHODS), p. 2 (I. INTRODUCTION), p. 2 (III. METHODS)

### Strongest assumption and failure boundary

- **p. 2 / I. INTRODUCTION - extractive body cue:** Ten constructed surgical relevant tasks with difficulty levels and varying scenes are presented for learning-based algorithm evaluation (right).
- **p. 1 / I. INTRODUCTION - extractive body cue:** The modeled trained on such simulated settings may suffer from the reality gap and fail to transfer to the real world [14].
- **p. 1 / I. INTRODUCTION - extractive body cue:** However, the existing learning-based platforms only support limited scenarios in the simulated environments [13], [14], detailed in Table I.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** By visually inspecting the training progress, we find that the agents can quickly learn to approach the object such as the needle and attempt to ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** Meanwhile, the needle picking point is restricted to the jaw tip to avoid unsafe jaw collisions with the holding surface.
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** Besides, we find some failure cases resulting from dynamics discrepancies between the simulation and the real world, also observed in [14].
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 7. Different levels of physical interaction. The object is attached to the jaw if the tip-object distance is below a certain threshold with limited ...
- **Boundary to test:** By visually inspecting the training progress, we find that the agents can quickly learn to approach the object such as the needle and attempt to pick reasonably, but failed because of the ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Our main contributions are summarized as follows: • We design an open-source surgical robot learning simulation platform centered on reinforcement learning for surgical skills, which benefits low-cost data collection and accelerates the ... | p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION) |
| Reported outcome | By contrast, the policy trained in the Interact manner with improved physics simulation is more robust to environment changes with a high success rate. | p. 7 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Failure/limitation | By visually inspecting the training progress, we find that the agents can quickly learn to approach the object such as the needle and attempt to pick reasonably, but failed because of the ... | p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `multi-view observation, language/task label과 action trajectory → shared representation, embodiment/task identity와 data distribution → dataset sample 또는 learned policy action`.
- 이 논문의 재사용 가능한 지점은 SurRoL builds on top of the open-source PyBullet because of its state-of-the-art physics simulation, wide adoption in the machine learning community, and removal of the commercial software limits, e.g., V-REP.를 Our main contributions are summarized as follows: • We design an open-source surgical robot learning simulation platform centered on reinforcement learning for surgical skills, which benefits low-cost data collection and accelerates the ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 shared representation, embodiment/task identity와 data distribution가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 By visually inspecting the training progress, we find that the agents can quickly learn to approach the object such as the needle and attempt to pick reasonably, but failed because of the ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Our main contributions are summarized as follows: • We design an open-source surgical robot learning simulation platform centered on reinforcement learning for surgical skills, which benefits low-cost data collection and accelerates the ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `Manipulation, contact, tactile, and dexterity`; tags: `Robotics, surgical robotics, Reinforcement Learning, simulation, sim-to-real, dexterous manipulation`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** By visually inspecting the training progress, we find that the agents can quickly learn to approach the object such as the needle and attempt to pick reasonably, but failed because of the ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: 1) Experiment Setup: In our RL environments, we set up the manipulation workspace for robots and objects to interact within..
3. Compare against the body-reported baseline or a matched simpler baseline: 4) Evaluation Results: A summary of the evaluation results for RL baselines is shown in Fig..
4. Report the body metric and its denominator/aggregation: Fig. 5. Evaluation results for ten proposed tasks. The average success rates for goal-based tasks and episode returns for the reward-based task (ActiveTrack) are shown over three random seeds, with one epoch ....
5. Re-run the body-reported ablation/failure condition: We also observe that in StaticTrack, the learned policy can smoothly center the target object without the jittering effect, which is non-trivial for the visual servoing method that requires careful parameter tuning..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 2 (III. METHODS), p. 2 (III. METHODS); the primary result is directionally consistent at p. 7 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 main, contributions, summarized mechanism이 4) Evaluation Results: A summary of the evaluation results for RL baselines is shown in Fig. 대비 Fig. 5. Evaluation results for ten proposed tasks. The average success rates for goal-based tasks and episode returns ...을 개선하고, By visually inspecting the training progress, we find that the agents can quickly learn to approach ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
