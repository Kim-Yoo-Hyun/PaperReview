# Insights — PALM: Progress-Aware Policy Learning via Affordance Reasoning for Long-Horizon Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Liu_PALM_Progress-Aware_Policy_Learning_via_Affordance_Reasoning_for_Long-Horizon_Robotic_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_PALM_Progress-Aware_Policy_Learning_via_Affordance_Reasoning_for_Long-Horizon_Robotic_CVPR_2026_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1. Introduction - extractive body cue:** Our contributions are as follows: • We introduce PALM, a unified VLA framework that integrates structured affordance reasoning and progress-aware policy generation to enable reliable ...
- **p. 2 / 1. Introduction - extractive body cue:** To address these gaps, we introduce PALM, a novel end-to-end framework for learning scalable, long-horizon manipulation.
- **p. 3 / 3.1. Problem Formulation - extractive body cue:** At time t, given observations ot "O, and task specification ⌧"T , and conditioned on the predicted affordance latent, the policy jointly decodes an action ...
- **p. 5 / 3.4. Progress-aware Policy via Inverse Dynamics - extractive body cue:** In addition to predicting where to act via affordances, we introduce a progress-aware prediction task that estimates how far execution has advanced within the current ...
- **p. 3 / 3.2. PALM Architecture - extractive body cue:** Building on prior inverse-dynamics formulations [18, 38, 112], these queries aggregate current observations with the predicted affordance latent to infer action sequences that align with ...
- **p. 5 / 3.4. Progress-aware Policy via Inverse Dynamics - extractive body cue:** This explicit progress signal reduces ambiguity in long-horizon control: visually similar observations may correspond to different actions depending on stage, and pt disambiguates these cases ...
- **p. 4 / 3.2. PALM Architecture - extractive body cue:** Affordance Queries Action-progress Queries Multi-Modal Encoders Affordance prediction Frozen Trainable Unidirectional Attention Action-progress <Global> <Local> <Spatial> <Dynamic> T S V G
- **Contribution anchor:** p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Problem Formulation), p. 5 (3.4. Progress-aware Policy via Inverse Dynamics), p. 3 (3.2. PALM Architecture), p. 5 (3.4. Progress-aware Policy via Inverse Dynamics)

### Strongest assumption and failure boundary

- **p. 2 / 1. Introduction - extractive body cue:** In addition, existing VLAs lack mechanisms for continuously estimating progress within a subtask.
- **p. 2 / 1. Introduction - extractive body cue:** Although existing models may infer the final goal and produce intermediate actions [18, 38, 112, 143, 146, 148], they lack internal representations that disambiguate which ...
- **p. 3 / 3.1. Problem Formulation - extractive body cue:** At time t, given observations ot "O, and task specification ⌧"T , and conditioned on the predicted affordance latent, the policy jointly decodes an action ...
- **p. 8 / 5. Conclusion - extractive body cue:** PALM achieves stateof-the-art results on two benchmarks, with a 12.5% improvement on CALVIN ABC→D and 91.8% success on LIBEROLONG, and shows significant robustness in real-world ...
- **p. 8 / 4.3. Real-World Experiments - extractive body cue:** As shown in Table 5, results demonstrate PALM's superior generalization over baselines as the task sequence length increases, showing its robustness in longhorizon settings.
- **Boundary to test:** PALM achieves stateof-the-art results on two benchmarks, with a 12.5% improvement on CALVIN ABC→D and 91.8% success on LIBEROLONG, and shows significant robustness in real-world experiments across long-horizon generalization settings.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Our contributions are as follows: • We introduce PALM, a unified VLA framework that integrates structured affordance reasoning and progress-aware policy generation to enable reliable execution across longhorizon, contact-rich manipulati ... | p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Reported outcome | Moreover, as shown in Table 2, across all four LIBERO suites, PALM achieves state-of-the-art performance with an average success rate of 94.5%. | p. 6 (4.1. Simulation Experiments), p. 7 (Figure/Table caption) |
| Failure/limitation | PALM achieves stateof-the-art results on two benchmarks, with a 12.5% improvement on CALVIN ABC→D and 91.8% success on LIBEROLONG, and shows significant robustness in real-world experiments across long-horizon generalization settings. | p. 8 (5. Conclusion), p. 8 (4.3. Real-World Experiments) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `image/video, language instruction, proprioception과 history → language-grounded task state와 action-policy context → continuous action, pose 또는 action chunk`.
- 이 논문의 재사용 가능한 지점은 PALM processes three synchronized inputs: a language instruction l, an image observation ot, and a robot state st.를 This explicit progress signal reduces ambiguity in long-horizon control: visually similar observations may correspond to different actions depending on stage, and pt disambiguates these cases by providing a continuous indicator of "wher ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 language-grounded task state와 action-policy context가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 PALM achieves stateof-the-art results on two benchmarks, with a 12.5% improvement on CALVIN ABC→D and 91.8% success on LIBEROLONG, and shows significant robustness in real-world experiments across long-horizon generalization settings.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Our contributions are as follows: • We introduce PALM, a unified VLA framework that integrates structured affordance reasoning and progress-aware policy generation to enable reliable execution across longhorizon, contact-rich manipulati ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `VLA and generalist robot policies`; tags: `Robotics, VLA, affordance, progress estimation, long-horizon manipulation`.
- **Reading predecessor in the generated track queue:** AtomicVLA: Unlocking the Potential of Atomic Skill Learning in Robots (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** ActiveVLA: Injecting Active Perception into Vision-Language-Action Models for Precise 3D Robotic Manipulation (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** PALM achieves stateof-the-art results on two benchmarks, with a 12.5% improvement on CALVIN ABC→D and 91.8% success on LIBEROLONG, and shows significant robustness in real-world experiments across long-horizon generalization settings.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: For pre-training, we utilize a mixed dataset from the DROID [54] and BridgeData V2 [113] datasets, which together provide large-scale, in-the-wild robotic arm demonstrations to build a foundational understanding of diverse real-world ....
3. Compare against the body-reported baseline or a matched simpler baseline: PALM consistently and substantially outperforms all baselines..
4. Report the body metric and its denominator/aggregation: For each task suite (Spatial, Object, Goal, Long), we report the average success rate and standard error across 3 seeds with 500 episodes each..
5. Re-run the body-reported ablation/failure condition: Ablation studies of affordance components on CALVIN ABC→D and LIBERO-LONG benchmarks demonstrate the effectiveness of the four components of affordance prediction. increases (e.g., 82.0% for five consecutive subtasks)..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 3 (3.1. Problem Formulation), p. 3 (3.2. PALM Architecture), p. 5 (3.4. Progress-aware Policy via Inverse Dynamics); the primary result is directionally consistent at p. 6 (4.1. Simulation Experiments), p. 7 (Figure/Table caption), p. 6 (Figure/Table caption); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 contributions, follows, introduce mechanism이 PALM consistently and substantially outperforms all baselines. 대비 For each task suite (Spatial, Object, Goal, Long), we report the average success rate and standard error across ...을 개선하고, PALM achieves stateof-the-art results on two benchmarks, with a 12.5% improvement on CALVIN ABC→D and 91.8% ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
