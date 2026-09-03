# Insights — Hearing Touch: Audio-Visual Pretraining for Contact-Rich Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2405.08576; PDF retrieval source: https://arxiv.org/pdf/2405.08576. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / I. INTRODUCTION - extractive body cue:** Our method makes use of Audio-Visual Instance Discrimination (AVID) [14], a selfsupervised learning approach to learn audio-visual representations, pre-trained on Audioset [15], a dataset containing ...
- **p. 3 / III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING - extractive body cue:** Similar to [41], [42] our method is quasi open-loop-at time step t the policy predicts H steps of actions, of which h ≤H steps of ...
- **p. 3 / III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING - extractive body cue:** Audio and Visual Representation Pretraining Our method uses large-scale audio-visual pre-training to initialize our audio encoder and large-scale visual pretraining to initialize our visual encoder.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Furthermore, our approach outperforms equivalent policies with audio encoders trained from scratch.
- **p. 2 / III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING - extractive body cue:** We outline further details of our approach in the following sections.
- **p. 3 / III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING - extractive body cue:** To isolate the effect of large-scale pre-training for our audio encoder, we use R3M [1], a proven method for pre-training visual features in robotic applications, ...
- **p. 3 / III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING - extractive body cue:** We apply learned positional embeddings to each of the encoded representations and pass the result as input to a transformer decoder network similar to [6].
- **Contribution anchor:** p. 1 (I. INTRODUCTION), p. 3 (III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING), p. 3 (III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING), p. 1 (I. INTRODUCTION), p. 2 (III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING), p. 3 (III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING)

### Strongest assumption and failure boundary

- **p. 1 / I. INTRODUCTION - extractive body cue:** This gap arises due to the lack of relevant data at a comparable scale for tactile sensing.
- **p. 1 / I. INTRODUCTION - extractive body cue:** As a result, current approaches using non-visual sensory modalities are restricted to learning from a limited amount of task-specific data [10], [12].
- **p. 6 / V. CONCLUSION - extractive body cue:** Future work may investigate which properties of pre-training datasets are most conducive to learning audio-visual representations for manipulation policies.
- **p. 4 / IV. EXPERIMENTS - extractive body cue:** As a result, the baselines suffer heavily from the domain shift and fail to generalize, often moving in jerk motions or away from the object ...
- **p. 4 / IV. EXPERIMENTS - extractive body cue:** Further, our method outperforms or matches the performance of all baselines in 8/9 tasks, displaying a lower variation in performance between different configurations of each ...
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Despite having access to the same information as our method, the BYOL-A and Scratch baselines fail to reason effectively over the audio and utilize the ...
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** This is more like the behavior of the training data than the baselines, which often fail to begin digging the spoon into the material as ...
- **Boundary to test:** Future work may investigate which properties of pre-training datasets are most conducive to learning audio-visual representations for manipulation policies.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Our method makes use of Audio-Visual Instance Discrimination (AVID) [14], a selfsupervised learning approach to learn audio-visual representations, pre-trained on Audioset [15], a dataset containing 1Robotics Institute, Carnegie Mellon ... | p. 1 (I. INTRODUCTION), p. 3 (III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING) |
| Reported outcome | Flipping Scooping Zipping Success % Reward Success % Reward Success % Ours 50.0% 15.4 78.1% 8.9 88.9% BYOL-A 25.0% 2.3 25.0% 3.8 66.7% Scratch 15.4% 7.7 50.0% 6.9 72.2% Vision-Only 0.0% 2.5 ... | p. 4 (IV. EXPERIMENTS), p. 4 (Figure/Table caption) |
| Failure/limitation | Future work may investigate which properties of pre-training datasets are most conducive to learning audio-visual representations for manipulation policies. | p. 6 (V. CONCLUSION), p. 4 (IV. EXPERIMENTS) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `tactile image/force, vision과 proprioceptive history → contact geometry, force state 또는 latent dynamics → grasp/contact action, force command 또는 object motion`.
- 이 논문의 재사용 가능한 지점은 Initializing our encoder with AVID weights, we train a policy with behavior cloning that fuses visual and audio inputs with self-attention in order to predict actions.를 This approach allows the policy to remain responsive to subtle changes in the audio input while encouraging temporal action consistency and mitigating the effect of non-Markovian behaviors such as pauses in demonstrations.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 contact geometry, force state 또는 latent dynamics가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Future work may investigate which properties of pre-training datasets are most conducive to learning audio-visual representations for manipulation policies.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Our method makes use of Audio-Visual Instance Discrimination (AVID) [14], a selfsupervised learning approach to learn audio-visual representations, pre-trained on Audioset [15], a dataset containing 1Robotics Institute, Carnegie Mellon ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `Manipulation, contact, tactile, and dexterity`; tags: `Robotics, tactile sensing, audio-visual pretraining, contact-rich manipulation`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Future work may investigate which properties of pre-training datasets are most conducive to learning audio-visual representations for manipulation policies.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: 2) Scaling Performance: We run evaluations on the scooping task for models trained with dataset sizes 50% (30 demos) and 150% (90 demos) of the original data after collecting more demonstrations..
3. Compare against the body-reported baseline or a matched simpler baseline: Our method, shown in blue, outperforms baselines in all but one setup of the zipping task..
4. Report the body metric and its denominator/aggregation: The selfattention mechanism for fusing audio and visual features is crucial to attaining good performance; both the success rate and the average reward drop by nearly 50% when replacing the transformer with ....
5. Re-run the body-reported ablation/failure condition: Fig. 6: Ablations. We evaluate the zero-shot transfer of frozen pre-trained audio representations (a), the effect of dataset size (b), the generalization ability of our method (c), and the importance of self-attention ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 3 (III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING), p. 3 (III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING), p. 2 (III. MANIPULATION WITH AUDIO-VISUAL PRETRAINING); the primary result is directionally consistent at p. 4 (IV. EXPERIMENTS), p. 4 (Figure/Table caption), p. 5 (IV. EXPERIMENTS); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 makes, Audio-Visual, Instance mechanism이 Our method, shown in blue, outperforms baselines in all but one setup of the zipping task. 대비 The selfattention mechanism for fusing audio and visual features is crucial to attaining good performance; both the success ...을 개선하고, Future work may investigate which properties of pre-training datasets are most conducive to learning audio-visual representations ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
