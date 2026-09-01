# Insights — Scaling Proprioceptive-Visual Learning with Heterogeneous Pre-trained Transformers

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (24 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://papers.nips.cc/paper_files/paper/2024/hash/e0f393e7980a24fd12fa6f15adfa25fb-Abstract-Conference.html; PDF retrieval source: https://arxiv.org/pdf/2409.20537. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1 Introduction - extractive body cue:** We introduce Heterogeneous Pre-trained Transformers (HPT), a family of architecture designed to scalably learn from data across heterogeneous embodiments.
- **p. 2 / 1 Introduction - extractive body cue:** In this work, we propose to address this issue by aligning the proprioception and vision information from different embodiments to a shared "language" of policies ...
- **p. 5 / 1 Introduction - extractive body cue:** This is used as the input sequence to the trunk that we introduce below.
- **p. 4 / 1 Introduction - extractive body cue:** These tokenizers map heterogeneous inputs from different embodiments to a fixed number of tokens with fixed dimensions, which enables the trunk to treat them in ...
- **p. 5 / 1 Introduction - extractive body cue:** We show illustrations of dataset mixtures (each color is a distinct embodiment) from different domains including real robot teleop [14], deployed robots [38], simulations, and ...
- **p. 17 / A Implementation Details - extractive body cue:** Different from previous work [55, 86], we use minimal amounts of processing and cleaning of the observation and actions in the raw trajectories.
- **p. 17 / A.1 Dataset Details - extractive body cue:** Since the human datasets do not contain proprioception and action information, we use hand poses and 2D positions in the image space as surrogates for ...
- **Contribution anchor:** p. 2 (1 Introduction), p. 2 (1 Introduction), p. 5 (1 Introduction), p. 4 (1 Introduction), p. 5 (1 Introduction), p. 17 (A Implementation Details)

### Strongest assumption and failure boundary

- **p. 1 / 1 Introduction - extractive body cue:** Recent progress in open-source large-scale data collection [14, 75] has made this path possible, but the heterogeneity (such as varying robot hardware and different environments) ...
- **p. 2 / 1 Introduction - extractive body cue:** The heterogeneity in robotics presents a distinct challenge: different robots are physically different embodiments1 of hardware acting in different environments.
- **p. 6 / 1 Introduction - extractive body cue:** Strictly increasing data while keeping others bottlenecked (HPT-S 6
- **p. 6 / 1 Introduction - extractive body cue:** Admittedly, there are several caveats to this metric including the closed-loop performance gap and the task success rate gap.
- **p. 8 / 1 Introduction - extractive body cue:** For the human datasets that lack proprioception and action information, we use poses and 2D positions as surrogates for the supervised policy learning objectives.
- **p. 10 / 6 Conclusion - extractive body cue:** See Appendix §C for some failure modes.
- **p. 23 / Figure/Table caption - extractive body cue:** Figure 18: Ablation Study on HPT Stem. We ablate the pre-training performance for (a) proprioception, (b) vision stems, and (c) vision encoders. Setting: HPT-S, batch ...
- **Boundary to test:** See Appendix §C for some failure modes.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | We introduce Heterogeneous Pre-trained Transformers (HPT), a family of architecture designed to scalably learn from data across heterogeneous embodiments. | p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Reported outcome | Figure 17: Simulation Task Performance compared with Single-Task Policy in LeRobot Implementation. We do evaluation in a different implementation in unseen simulation benchmarks. Left) we show that an improvement in performance can ... | p. 22 (Figure/Table caption), p. 9 (Figure/Table caption) |
| Failure/limitation | See Appendix §C for some failure modes. | p. 10 (6 Conclusion), p. 23 (Figure/Table caption) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `multi-view observation, language/task label과 action trajectory → shared representation, embodiment/task identity와 data distribution → dataset sample 또는 learned policy action`.
- 이 논문의 재사용 가능한 지점은 We reinitialize the head and stem parameters with embodiment-specific input and output dimensions (such as different proprioception and action dimensions), and freeze the weights of the trunk.를 3 Heterogenoues Pre-trained Transformers (HPT) In heterogeneous robot learning with cross embodiments, the data are generated from different domains such as simulation and real robots, across sensory modalities such as RGB images, ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 shared representation, embodiment/task identity와 data distribution가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 See Appendix §C for some failure modes.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: We introduce Heterogeneous Pre-trained Transformers (HPT), a family of architecture designed to scalably learn from data across heterogeneous embodiments.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `VLA and generalist robot policies`; tags: `Robotics, cross-embodiment, proprioception, visual representation, heterogeneous data, Transformer`.
- **Reading predecessor in the generated track queue:** XSkill: Cross Embodiment Skill Discovery (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** FAST: Efficient Action Tokenization for Vision-Language-Action Models (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** See Appendix §C for some failure modes.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: For the additional 7 simulation dataset, we use the simulator benchmarks across all popular simulators Drake [81], Mujoco [89, 49], Isaac Sim [20], and PyBullet [80], as well as Sapien [52] and ....
3. Compare against the body-reported baseline or a matched simpler baseline: Figure 17: Simulation Task Performance compared with Single-Task Policy in LeRobot Implementation. We do evaluation in a different implementation in unseen simulation benchmarks. Left) we show that an improvement in performance can ....
4. Report the body metric and its denominator/aggregation: Figure 12: Transfer Learning in the Real World. We evaluate the pre-trained HPTs on four tasks / two embodiments. The average success rate with standard deviations is computed for 45 trials per ....
5. Re-run the body-reported ablation/failure condition: Figure 3: Stem Architecture in HPT. In the HPT stem, the proprioceptive tokenizer uses an MLP to map proprioceptive information to a feature which is then attended by 16 learnable tokens. The ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 17 (A Implementation Details), p. 17 (A.1 Dataset Details); the primary result is directionally consistent at p. 22 (Figure/Table caption), p. 9 (Figure/Table caption), p. 10 (Figure/Table caption); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 introduce, Heterogeneous, Pre-trained mechanism이 Figure 17: Simulation Task Performance compared with Single-Task Policy in LeRobot Implementation. We do evaluation in ... 대비 Figure 12: Transfer Learning in the Real World. We evaluate the pre-trained HPTs on four tasks / two ...을 개선하고, See Appendix §C for some failure modes. 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
