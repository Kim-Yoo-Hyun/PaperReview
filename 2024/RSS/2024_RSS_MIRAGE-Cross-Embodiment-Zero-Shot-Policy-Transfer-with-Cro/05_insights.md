# Insights — MIRAGE: Cross-Embodiment Zero-Shot Policy Transfer with Cross-Painting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (16 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss20/p069.html; PDF retrieval source: https://www.roboticsproceedings.org/rss20/p069.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / I. INTRODUCTION - extractive body cue:** To summarize, our key contributions are:
- **p. 1 / Abstract - extractive body cue:** To address robot visual disparities for vision-based policies, we introduce Mirage, which uses "cross-painting"-masking out the unseen target robot and inpainting the seen source robot-during ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Through extensive experiments on 9 manipulation tasks in both simulation and real across 6 different robot and gripper setups, we show that Mirage, despite its ...
- **p. 3 / 1) We assume knowledge of the two robots' coordinate - extractive body cue:** This allows us to render robots in a camera pose that is within the distribution of the training image poses.
- **p. 3 / 1) We assume knowledge of the two robots' coordinate - extractive body cue:** This allows us to transfer between robots with different numbers of joints and compensate for alternate gripper shapes across embodiments.
- **p. 4 / 4) We assume that the background and lighting conditions - extractive body cue:** Given a source policy action aS t+1 = πS(sS t , oS t ), we would like to transform it into a target policy action ...
- **p. 4 / 4) We assume that the background and lighting conditions - extractive body cue:** We consider the setting where there is a policy πS trained on a dataset of the source robot D = {(sS 1 , oS 1 ...
- **Contribution anchor:** p. 2 (I. INTRODUCTION), p. 1 (Abstract), p. 2 (I. INTRODUCTION), p. 3 (1) We assume knowledge of the two robots' coordinate), p. 3 (1) We assume knowledge of the two robots' coordinate), p. 4 (4) We assume that the background and lighting conditions)

### Strongest assumption and failure boundary

- **p. 2 / I. INTRODUCTION - extractive body cue:** This poses several challenges, as outlined in prior work [108], stemming from variations in kinematic configuration, control scheme, camera viewpoint, and end-effector morphology.
- **p. 4 / 4) We assume that the background and lighting conditions - extractive body cue:** This allows us to separate any challenges that arise due to changes in the background environment and focus on the impact of visual differences between ...
- **p. 3 / III. PROBLEM STATEMENT - extractive body cue:** Mirage leverages the following assumptions and design choices to reduce the gap between robots and enable zero-shot transfer:
- **p. 3 / III. PROBLEM STATEMENT - extractive body cue:** Prior work [108] has found aligning the action and observation spaces can facilitate policy transfer.
- **p. 5 / IV. STATE-BASED TRANSFER EXPERIMENTS - extractive body cue:** Less robust source policies leave little room for error, while more robust ones tend to retry even if the target robot fails to grasp the ...
- **p. 9 / 2) Can Mirage successfully zero-shot transfer trained vision - extractive body cue:** On the other hand, the failure modes we observe on the different robots or grippers are all very similar to those from the source policy ...
- **p. 10 / Figure/Table caption - extractive body cue:** Fig. 6: (a) An example of camera calibration error resulting in failure to mask all of the target robot out; (b) An example of the ...
- **Boundary to test:** Less robust source policies leave little room for error, while more robust ones tend to retry even if the target robot fails to grasp the object the first time.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | To summarize, our key contributions are: | p. 2 (I. INTRODUCTION), p. 1 (Abstract) |
| Reported outcome | Study Results Table I shows that when the target robots have the same gripper as the source robot, most unseen target robots achieve very high task success rates. | p. 5 (IV. STATE-BASED TRANSFER EXPERIMENTS), p. 9 (Figure/Table caption) |
| Failure/limitation | Less robust source policies leave little room for error, while more robust ones tend to retry even if the target robot fails to grasp the object the first time. | p. 5 (IV. STATE-BASED TRANSFER EXPERIMENTS), p. 9 (2) Can Mirage successfully zero-shot transfer trained vision) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `image/video, language instruction, proprioception과 history → language-grounded task state와 action-policy context → continuous action, pose 또는 action chunk`.
- 이 논문의 재사용 가능한 지점은 Given a source policy action aS t+1 = πS(sS t , oS t ), we would like to transform it into a target policy action aT t+1 = πT (sT t , ...를 We consider the setting where there is a policy πS trained on a dataset of the source robot D = {(sS 1 , oS 1 , aS 1 , ..., sS Hi, ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 language-grounded task state와 action-policy context가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Less robust source policies leave little room for error, while more robust ones tend to retry even if the target robot fails to grasp the object the first time.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: To summarize, our key contributions are:
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `VLA and generalist robot policies`; tags: `Robotics, cross-embodiment, zero-shot transfer, policy transfer, manipulation, domain adaptation`.
- **Reading predecessor in the generated track queue:** VLMimic: Vision Language Models are Visual Imitation Learner for Fine-grained Actions (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Pushing the Limits of Cross-Embodiment Learning for Manipulation and Navigation (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Less robust source policies leave little room for error, while more robust ones tend to retry even if the target robot fails to grasp the object the first time.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: For simulation experiments, we take into account potential occlusions between the robot and objects by comparing the pixel-wise depth values between the camera observation of the scene and the rendered robot..
3. Compare against the body-reported baseline or a matched simpler baseline: that Mirage successfully transfers between robots and grippers on 4 manipulation tasks, suffering only minimal performance degradation from the source policy and significantly outperforming a state-of-the-art generalist model..
4. Report the body metric and its denominator/aggregation: For all tasks, we train the source state-based policy on the Franka robot and evaluate the success rates on different target robots using the test-time execution strategy mentioned above..
5. Re-run the body-reported ablation/failure condition: Bridging the Visual Gap To replace the robots, we leverage the knowledge of the robot URDFs and camera poses to perform cross-painting at test time..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 4 (4) We assume that the background and lighting conditions), p. 4 (4) We assume that the background and lighting conditions), p. 2 (I. INTRODUCTION); the primary result is directionally consistent at p. 5 (IV. STATE-BASED TRANSFER EXPERIMENTS), p. 9 (Figure/Table caption), p. 2 (3) Physical experiments with Franka and UR5 demonstrating); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 summarize, contributions, address mechanism이 that Mirage successfully transfers between robots and grippers on 4 manipulation tasks, suffering only minimal performance ... 대비 For all tasks, we train the source state-based policy on the Franka robot and evaluate the success rates ...을 개선하고, Less robust source policies leave little room for error, while more robust ones tend to retry ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
