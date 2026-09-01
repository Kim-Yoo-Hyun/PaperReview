# Insights — Move to Understand a 3D Scene: Bridging Visual Grounding and Exploration for Efficient and Versatile Embodied Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (13 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Zhu_Move_to_Understand_a_3D_Scene_Bridging_Visual_Grounding_and_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Zhu_Move_to_Understand_a_3D_Scene_Bridging_Visual_Grounding_and_ICCV_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 3 / Method - extractive body cue:** Our main contributions can be summarized as follows: • We present MTU3D, bridging visual grounding and exploration for efficient and versatile embodied navigation. • We ...
- **p. 2 / 1. Introduction - extractive body cue:** To address these challenges, we propose Move to Understand (MTU3D), a unified framework that bridges visual grounding and exploration for versatile embodied navigation as shown ...
- **p. 2 / 1. Introduction - extractive body cue:** Our approach introduces three key innovations:
- **p. 3 / Method - extractive body cue:** When combined with a large vision-language model, serving as its trajectory generator, our approach improves the embodied question answering for LM-SR by 2.4% and LLM-SPL ...
- **p. 5 / 3.4. Vision-Language-Exploration Training - extractive body cue:** The unified decision scores SU t are optimized with binary cross-entropy loss, teaching the model to assign higher scores to appropriate query locations based on ...
- **p. 5 / 3.4. Vision-Language-Exploration Training - extractive body cue:** We utilize RGBD trajectories from ScanNet and HM3D to train query representation with instance segmentation loss.
- **Contribution anchor:** p. 3 (Method), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (Method), p. 5 (3.4. Vision-Language-Exploration Training), p. 5 (3.4. Vision-Language-Exploration Training)

### Strongest assumption and failure boundary

- **p. 2 / 1. Introduction - extractive body cue:** Our approach bridges online exploration with dynamically spatial memory updates for lifelong grounding. ries presents significant challenges, and methods for effectively leveraging such data remain ...
- **p. 2 / 1. Introduction - extractive body cue:** In contrast, reinforcement learning (RL)-based embodied agents can explore environments but often struggle with sample inefficiency [71], poor generalization due to limited training data [20, ...
- **p. 7 / 4.3. Discussions - extractive body cue:** Does Vision-Langauge-Exploration Pe-training benefit navigation?
- **p. 7 / 4.3. Discussions - extractive body cue:** 4a show that VisionLanguage Exploration (VLE) Pre-training significantly improves navigation performance, as indicated by the SR across all datasets.
- **p. 7 / 4.3. Discussions - extractive body cue:** Specifically, SR increases from 27.8% to 33.3% in OVON, 22.2% to 36.1% in GOAT, and 22.9% to 27.9% in SG3D, demonstrating a consistent benefit of ...
- **p. 7 / 4.3. Discussions - extractive body cue:** Does grounded training lead to efficient exploration?
- **Boundary to test:** Does Vision-Langauge-Exploration Pe-training benefit navigation?

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Our main contributions can be summarized as follows: • We present MTU3D, bridging visual grounding and exploration for efficient and versatile embodied navigation. • We propose a unified objective that jointly optimizes ... | p. 3 (Method), p. 2 (1. Introduction) |
| Reported outcome | While MTU3D significantly outperforms Embodied Video Agent [21] and SenseAct-NN Monolithic [37, 87], overall success rates remain lower than in GOAT-Bench and HM3D-OVON, highlighting SG3D's inherent difficulty in requiring both navigati ... | p. 6 (4.2. Quantitative Results), p. 6 (Figure/Table caption) |
| Failure/limitation | Does Vision-Langauge-Exploration Pe-training benefit navigation? | p. 7 (4.3. Discussions), p. 7 (4.3. Discussions) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `camera/depth stream, pose, map와 language goal → robot pose, free-space/semantic map와 local goal → collision-free trajectory 또는 velocity command`.
- 이 논문의 재사용 가능한 지점은 (a) 3D-VL Model (b) End-to-End RL (c) MTU3D (Ours) Full RGB-D Video Time World Visual Grounding Model Explicit Mesh Open loop Single RGB-D image World State Action Model Closed loop Implicit state ...를 Specifically, MTU3D improves the state-of-the-art results by 13.7%, 23.0%, and 9.1% in SR, and 2.4%, 13.0%, and 6.3% in SPL on HM3D-OVON [79], GOAT-Bench [37], and SG3D [87], respectively.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 robot pose, free-space/semantic map와 local goal가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Does Vision-Langauge-Exploration Pe-training benefit navigation?에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Our main contributions can be summarized as follows: • We present MTU3D, bridging visual grounding and exploration for efficient and versatile embodied navigation. • We propose a unified objective that jointly optimizes ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `Robotics-enabling 3D perception`; tags: `Navigation, grounding, exploration`.
- **Reading predecessor in the generated track queue:** IGL-Nav: Incremental 3D Gaussian Localization for Image-goal Navigation (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** end of this track queue (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Does Vision-Langauge-Exploration Pe-training benefit navigation?; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Unlike other benchmarks, SG3D emphasizes task consistency across multiple steps, making it more complex..
3. Compare against the body-reported baseline or a matched simpler baseline: 3 demonstrate that our proposed MTU3D significantly outperforms all baselines in terms of SR across both Val Seen and Val Unseen settings..
4. Report the body metric and its denominator/aggregation: While MTU3D significantly outperforms Embodied Video Agent [21] and SenseAct-NN Monolithic [37, 87], overall success rates remain lower than in GOAT-Bench and HM3D-OVON, highlighting SG3D's inherent difficulty in requiring both navigati ....
5. Re-run the body-reported ablation/failure condition: Ablation studies showing (a) the impact of vision-language-exploration pretraining, (b) exploration efficiency on seen environments, and (c) the contribution of spatial memory to navigation performance..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 3 (Method), p. 3 (Method), p. 5 (3.4. Vision-Language-Exploration Training); the primary result is directionally consistent at p. 6 (4.2. Quantitative Results), p. 6 (Figure/Table caption), p. 7 (4.3. Discussions); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 main, contributions, summarized mechanism이 3 demonstrate that our proposed MTU3D significantly outperforms all baselines in terms of SR across both ... 대비 While MTU3D significantly outperforms Embodied Video Agent [21] and SenseAct-NN Monolithic [37, 87], overall success rates remain lower ...을 개선하고, the paper's strongest untested assumption 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
