# Insights — Domain Randomization for Transferring Deep Neural Networks from Simulation to the Real World

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1703.06907; PDF retrieval source: https://arxiv.org/pdf/1703.06907. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 4 / III. METHOD - extractive body cue:** Our method avoids calibration and precise placement of the camera in the real world by randomizing characteristics of the cameras used to render images in ...
- **p. 3 / III. METHOD - extractive body cue:** Our approach is to train a deep neural network in simulation using domain randomization.
- **p. 3 / III. METHOD - extractive body cue:** The remainder of this section describes the specific domain randomization and neural network training methodology we use.
- **p. 3 / III. METHOD - extractive body cue:** We randomize the following aspects of the domain for each sample used during training: • Number and shape of distractor objects on the table • ...
- **p. 4 / III. METHOD - extractive body cue:** In particular, we use a modified version the VGG-16 architecture [39] shown in Figure 2.
- **p. 4 / III. METHOD - extractive body cue:** For the majority of our experiments, we use weights obtained by pretraining on ImageNet to initialize the convolutional layers, which we hypothesized would be essential ...
- **Contribution anchor:** p. 4 (III. METHOD), p. 3 (III. METHOD), p. 3 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD), p. 4 (III. METHOD)

### Strongest assumption and failure boundary

- **p. 1 / I. INTRODUCTION - extractive body cue:** Though in principle domain randomization could be applied to any component of the reality gap, we focus on the challenge of transferring from low-fidelity simulated ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** This paper explores domain randomization, a simple but promising method for addressing the reality gap.
- **p. 2 / I. INTRODUCTION - extractive body cue:** Object localization from pixels is a well-studied problem in robotics, and state-ofthe-art methods employ complex, hand-engineered image processing pipelines (e.g., [6], [5], [44]).
- **p. 3 / II. RELATED WORK - extractive body cue:** However, their experiments - collision avoidance in hallways and open spaces - do not demonstrate the ability to deal with high-precision tasks.
- **p. 3 / II. RELATED WORK - extractive body cue:** Our approach also does not rely on precise camera information or calibration, instead randomizing the position, orientation, and field of view of the camera in ...
- **p. 4 / IV. EXPERIMENTS - extractive body cue:** The goals of our experiments are: (a) Evaluate the localization accuracy of our trained detectors in the real world, including in the presence of distractor ...
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Adding noise during pretraining appears to have a negligible effect.
- **Boundary to test:** However, their experiments - collision avoidance in hallways and open spaces - do not demonstrate the ability to deal with high-precision tasks.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Our method avoids calibration and precise placement of the camera in the real world by randomizing characteristics of the cameras used to render images in training. | p. 4 (III. METHOD), p. 3 (III. METHOD) |
| Reported outcome | However, using a pre-trained model can significantly improve performance when less training data is used. | p. 5 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS) |
| Failure/limitation | However, their experiments - collision avoidance in hallways and open spaces - do not demonstrate the ability to deal with high-precision tasks. | p. 3 (II. RELATED WORK), p. 3 (II. RELATED WORK) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `state 또는 observation, action, reward와 transition history → policy/value state와 action-selection variable → action policy와 induced trajectory`.
- 이 논문의 재사용 가능한 지점은 The input is an image from an external webcam downsized to (224 × 224) and the output of the network predicts the (x, y, z) coordinates of object(s) of interest.를 Object localization from pixels is a well-studied problem in robotics, and state-ofthe-art methods employ complex, hand-engineered image processing pipelines (e.g., [6], [5], [44]).로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 policy/value state와 action-selection variable가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 However, their experiments - collision avoidance in hallways and open spaces - do not demonstrate the ability to deal with high-precision tasks.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Our method avoids calibration and precise placement of the camera in the real world by randomizing characteristics of the cameras used to render images in training.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `CORE` in `RL, IL, offline learning, and robot data`; tags: `Robotics, sim-to-real, domain randomization, perception`.
- **Reading predecessor in the generated track queue:** Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** What Matters in Learning from Offline Human Demonstrations for Robot Manipulation (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** However, their experiments - collision avoidance in hallways and open spaces - do not demonstrate the ability to deal with high-precision tasks.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: The goals of our experiments are: (a) Evaluate the localization accuracy of our trained detectors in the real world, including in the presence of distractor objects and partial occlusions (b) Assess which ....
3. Compare against the body-reported baseline or a matched simpler baseline: Randomizing the position of the camera also consistently provides a slight accuracy boost, but reasonably high accuracy is achievable without it..
4. Report the body metric and its denominator/aggregation: The goals of our experiments are: (a) Evaluate the localization accuracy of our trained detectors in the real world, including in the presence of distractor objects and partial occlusions (b) Assess which ....
5. Re-run the body-reported ablation/failure condition: Ablation study To evaluate the importance of different factors of our training methodology, we assessed the sensitivity of the algorithm to the following: • Number of training images • Number of unique ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 3 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD); the primary result is directionally consistent at p. 5 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 avoids, calibration, precise mechanism이 Randomizing the position of the camera also consistently provides a slight accuracy boost, but reasonably high ... 대비 The goals of our experiments are: (a) Evaluate the localization accuracy of our trained detectors in the real ...을 개선하고, However, their experiments - collision avoidance in hallways and open spaces - do not demonstrate the ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
