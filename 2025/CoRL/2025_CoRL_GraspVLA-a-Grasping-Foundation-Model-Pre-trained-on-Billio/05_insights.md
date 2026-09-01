# Insights — GraspVLA: a Grasping Foundation Model Pre-trained on Billion-scale Synthetic Action Data

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (26 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v305/deng25a.html; PDF retrieval source: https://raw.githubusercontent.com/mlresearch/v305/main/assets/deng25a/deng25a.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1 Introduction - extractive body cue:** In summary, our contributions are as follows: a) we introduce a novel pretraining paradigm that relies entirely on synthetic action data, significantly reducing the real ...
- **p. 3 / 1 Introduction - extractive body cue:** scale globally, c) we propose Progressive Action Generation to co-train synthetic actions with Internet data, extending GraspVLA's skills to novel object categories, and d) extensive ...
- **p. 2 / 1 Introduction - extractive body cue:** To efficiently learn from this dataset, we propose GraspVLA, an end-to-end network that integrates autoregressive perception tasks and flow-matching-based action generation into a unified Chainof-Thought ...
- **p. 8 / 5 Hz - extractive body cue:** GraspVLA shows superior adaptability to novel tasks, surpassing the model without pretraining and all baselines.
- **p. 7 / 5 Hz - extractive body cue:** We benchmark GraspVLA against AnyGrasp [14], a state-of-the-art grasp detection model specialized in grasping.
- **p. 7 / 5 Hz - extractive body cue:** 5.5 Efficient Post-Training A defining characteristic of foundation models is their ability to adapt to new tasks.
- **p. 8 / 5 Hz - extractive body cue:** We experimented with three different post-training tasks to showcase that our model can quickly learn to grasp new items in (a), new grasping patterns in ...
- **Contribution anchor:** p. 2 (1 Introduction), p. 3 (1 Introduction), p. 2 (1 Introduction), p. 8 (5 Hz), p. 7 (5 Hz), p. 7 (5 Hz)

### Strongest assumption and failure boundary

- **p. 2 / 1 Introduction - extractive body cue:** However, unlike vision and language modalities, action data is absent from existing Internet datasets, demanding a new paradigm for data collection.
- **p. 2 / 1 Introduction - extractive body cue:** In addition, GraspVLA shows excellent generalization to long-tail object categories absent from synthetic action data, such as chargers, towels, and swimming goggles.
- **p. 3 / 1 Introduction - extractive body cue:** scale globally, c) we propose Progressive Action Generation to co-train synthetic actions with Internet data, extending GraspVLA's skills to novel object categories, and d) extensive ...
- **p. 9 / 6 Conclusion - extractive body cue:** 7 Limitations and Future Work Currently, our data generation and evaluation are conducted exclusively on the Franka Panda arm with front and side views.
- **p. 9 / 6 Conclusion - extractive body cue:** Like most grasping policies, we synthesize grasp labels using force-closure, which do not account for deformability-a limitation common to all such methods.
- **p. 7 / 5 Experiments - extractive body cue:** We provide failure analysis in the supplementary.
- **p. 7 / 5 Experiments - extractive body cue:** We evaluate on three LIBERO suites (Long, Goal, Object), excluding Spatial, as its focus on spatial reasoning falls outside our scope.
- **Boundary to test:** 7 Limitations and Future Work Currently, our data generation and evaluation are conducted exclusively on the Franka Panda arm with front and side views.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | In summary, our contributions are as follows: a) we introduce a novel pretraining paradigm that relies entirely on synthetic action data, significantly reducing the real world action data acquisition burden, b) we ... | p. 2 (1 Introduction), p. 3 (1 Introduction) |
| Reported outcome | Table 14: Impact of number of input views. Comparison of GraspVLA with different numbers of input views. The results demonstrate that while multiple views significantly improve performance, our single-view implementation still outperfor ... | p. 24 (Figure/Table caption), p. 6 (5 Experiments) |
| Failure/limitation | 7 Limitations and Future Work Currently, our data generation and evaluation are conducted exclusively on the Franka Panda arm with front and side views. | p. 9 (6 Conclusion), p. 9 (6 Conclusion) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `image/video, language instruction, proprioception과 history → language-grounded task state와 action-policy context → continuous action, pose 또는 action chunk`.
- 이 논문의 재사용 가능한 지점은 Compared to AnyGrasp [14], the state-of-the-art in traditional grasping detection algorithms, GraspVLA supports natural language instructions and delivers a robust closed-loop grasping policy.를 These models process robotic visual observations and human instructions to directly generate robot actions.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 language-grounded task state와 action-policy context가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 7 Limitations and Future Work Currently, our data generation and evaluation are conducted exclusively on the Franka Panda arm with front and side views.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: In summary, our contributions are as follows: a) we introduce a novel pretraining paradigm that relies entirely on synthetic action data, significantly reducing the real world action data acquisition burden, b) we ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `VLA and generalist robot policies`; tags: `VLA, grasping, synthetic data`.
- **Reading predecessor in the generated track queue:** 3DS-VLA: A 3D Spatial-Aware Vision Language Action Model for Robust Multi-Task Manipulation (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Long-VLA: Unleashing Long-Horizon Capability of Vision Language Action Model for Robot Manipulation (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** 7 Limitations and Future Work Currently, our data generation and evaluation are conducted exclusively on the Franka Panda arm with front and side views.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: We define synthetic categories as those present in our SynGrasp-1B dataset, while web categories refer to those exclusively present in Internet grounding dataset. b) Synthetic categories c) Web categories 0.2m a) Robot ....
3. Compare against the body-reported baseline or a matched simpler baseline: Additionally, the SPL metric reveals that GraspVLA grasps objects with shorter path lengths compared to π0 baselines which often exhibit hesitation..
4. Report the body metric and its denominator/aggregation: For each object group, we also report the average Success weighted by Path Length (SPL) [76], a widely used metric that weights success rate with motion efficiency by penalizing unnecessarily long paths..
5. Re-run the body-reported ablation/failure condition: Additionally, to assess the effectiveness of pre-training on SynGrasp-1B, we report results of direct fine-tuning π0 from its VLM weights [77], without its cross-embodiment robotic pre-training..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction); the primary result is directionally consistent at p. 24 (Figure/Table caption), p. 6 (5 Experiments), p. 6 (5 Experiments); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 summary, contributions, follows mechanism이 Additionally, the SPL metric reveals that GraspVLA grasps objects with shorter path lengths compared to π0 ... 대비 For each object group, we also report the average Success weighted by Path Length (SPL) [76], a widely ...을 개선하고, 7 Limitations and Future Work Currently, our data generation and evaluation are conducted exclusively on the ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
