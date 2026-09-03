# Insights — Robot Learning with Super-Linear Scaling

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p025.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p025.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / Abstract - extractive body cue:** We show that CASHER enables fine-tuning of prestrained to a target scenario using a video sean without any additional hbuman effort.
- **p. 1 / 1. Iyrropucrion - extractive body cue:** Our contributions include 1) a novel continual data collection system based on real-to-sim-to-real for training generalist policies, 2) a novel scanned deployment fine-tuning technique for ...
- **p. 2 / 1. Iyrropucrion - extractive body cue:** Overview of CASHER, we propose « system for taining generalist policies leveraging real-o-sim simulation on crowdsouced scans.
- **p. 3 / 1. Iyrropucrion - extractive body cue:** CASHER consists of three elements - 1) fast, accessible digital twin generation with 3-D reconstruction methods, 2) multi-environment model learning that amortizes the data collection ...
- **p. 12 / IX. IMPLEMENTATION DETAILS - extractive body cue:** To encode the point cloud observation, we use the volumetric 3D point cloud encoder proposed in Convolutional Occupancy Networks [31], which consists ofa local point ...
- **p. 12 / IX. IMPLEMENTATION DETAILS - extractive body cue:** The poticy model is a simple Multi-Layer Perceptron (MLP) network, with input as the privileged state in simulation as specified in VII and outputs a ...
- **Contribution anchor:** p. 1 (Abstract), p. 1 (1. Iyrropucrion), p. 2 (1. Iyrropucrion), p. 3 (1. Iyrropucrion), p. 12 (IX. IMPLEMENTATION DETAILS), p. 12 (IX. IMPLEMENTATION DETAILS)

### Strongest assumption and failure boundary

- **p. 2 / 1. Iyrropucrion - extractive body cue:** Continual learning also faces challenges, such as catastrophic forgetting, as discussed in prior work [18].
- **p. 2 / 1. Iyrropucrion - extractive body cue:** Generating procedurally accurate training environ- ‘ments remains an open challenge.
- **p. 3 / 1. Iyrropucrion - extractive body cue:** are available, generating valid robot trajectories that solve the task is another challenge.
- **p. 3 / 1. Iyrropucrion - extractive body cue:** However, these policies often fail to generalize to different scenarios, requiring significant human effort for each new environment.
- **p. 1 / 1. Iyrropucrion - extractive body cue:** CASHER (1) creates a data flywheel, where data begets more data through model generalization.
- **p. 4 / B. Amortized Data Collection - extractive body cue:** For these environments F, we fall back to querying the human demonstrator for high-quality demonstrations and learn a second state-based policy *+a(a,/s) using demonstration-bootstrapped reinforcement ...
- **p. 5 / B. Amortized Data Collection - extractive body cue:** This reduces the amount of human effort required for data collection as training progresses, Importantly, the generalization across environments does not need to achieve perfect ...
- **Boundary to test:** For these environments F, we fall back to querying the human demonstrator for high-quality demonstrations and learn a second state-based policy *+a(a,/s) using demonstration-bootstrapped reinforcement learning on F

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | We show that CASHER enables fine-tuning of prestrained to a target scenario using a video sean without any additional hbuman effort. | p. 1 (Abstract), p. 1 (1. Iyrropucrion) |
| Reported outcome | To verify the robustness of the learned policies, we ran evaluation on eight additional kitchens, ‘The results highlight an improvement of 16% to 60% rate as the number of training environments increased ... | p. 6 (A. Zero-Shot Scaling Laws Analysis), p. 6 (A. Zero-Shot Scaling Laws Analysis) |
| Failure/limitation | For these environments F, we fall back to querying the human demonstrator for high-quality demonstrations and learn a second state-based policy *+a(a,/s) using demonstration-bootstrapped reinforcement learning on F | p. 4 (B. Amortized Data Collection), p. 5 (B. Amortized Data Collection) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `observation history와 expert trajectory/action → behavior policy와 temporal action context → predicted action 또는 action chunk`.
- 이 논문의 재사용 가능한 지점은 We train an MLP network of size 256,256, that takes the embedding of the point cloud observation, which has 128 ‘dimensions, together With the state of the robot (end-effector scaled pose, postion, ...를 The poticy model is a simple Multi-Layer Perceptron (MLP) network, with input as the privileged state in simulation as specified in VII and outputs a probability <istribution of 14 classes, corresponding t0 ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 behavior policy와 temporal action context가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 For these environments F, we fall back to querying the human demonstrator for high-quality demonstrations and learn a second state-based policy *+a(a,/s) using demonstration-bootstrapped reinforcement learning on F에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: We show that CASHER enables fine-tuning of prestrained to a target scenario using a video sean without any additional hbuman effort.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `RL, IL, offline learning, and robot data`; tags: `Robotics, Imitation Learning, scaling laws, robot data`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** For these environments F, we fall back to querying the human demonstrator for high-quality demonstrations and learn a second state-based policy *+a(a,/s) using demonstration-bootstrapped reinforcement learning on F; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: The first experiment involves a thorough real-world evaluation of these policies across two institutions, using three different kitchens and six different objects, with six rollouts ‘each (a total of 108 rollouts per ....
3. Compare against the body-reported baseline or a matched simpler baseline: In Section IV-B, ‘we compare this baseline to the autonomous data collection system presented in Section III-B..
4. Report the body metric and its denominator/aggregation: As shown in Figure 3 a, we confirm the real-to-sim-to-real pipeline scaling law: as the number of trained environments increases, the zeroshot success rate also increases, reaching a 62% when trained ‘on ....
5. Re-run the body-reported ablation/failure condition: lef: results fr few-sot fine-tuning on the ask of pick and place « box om a shelf middle: results opening a cabinet right: muli-object evaluation.
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 12 (IX. IMPLEMENTATION DETAILS), p. 12 (IX. IMPLEMENTATION DETAILS); the primary result is directionally consistent at p. 6 (A. Zero-Shot Scaling Laws Analysis), p. 6 (A. Zero-Shot Scaling Laws Analysis); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 CASHER, enables, fine-tuning mechanism이 In Section IV-B, ‘we compare this baseline to the autonomous data collection system presented in Section ... 대비 As shown in Figure 3 a, we confirm the real-to-sim-to-real pipeline scaling law: as the number of trained ...을 개선하고, For these environments F, we fall back to querying the human demonstrator for high-quality demonstrations and ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
