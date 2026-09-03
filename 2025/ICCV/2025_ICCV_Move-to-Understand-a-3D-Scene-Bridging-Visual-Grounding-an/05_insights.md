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

- **Paper-specific interface:** Our main contributions can be summarized as follows: • We present MTU3D, bridging visual grounding and exploration for efficient and versatile embodied navigation. • We propose a unified objective that ... (p. 3, Method).
- **Paper-specific mechanism:** Our main contributions can be summarized as follows: • We present MTU3D, bridging visual grounding and exploration for efficient and versatile embodied navigation. • We propose a unified objective that ... (p. 3, Method).
- **Evidence boundary:** the reported outcome is Table 4. Sequential task navigation results on SG3D-Nav [87]. Multi-modal Lifelong Navigation. The results in Tab. 5 highlight the significant performance improvement of our MTU3D over baseline methods in lifelong ... (p. 6, Figure/Table caption); the relevant task/metric cue is Furthermore, GPT4o with MTU3D achieves even better performance, reaching 51.1% LLM-SR and 42.6% LLM-SPL. (p. 7, 4.2. Quantitative Results). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** In contrast, reinforcement learning (RL)-based embodied agents can explore environments but often struggle with sample inefficiency [71], poor generalization due to limited training data [20, 57, 62] and the lack ... (p. 2, 1. Introduction).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `Robotics-enabling 3D perception`; tags: `Navigation, grounding, exploration`.
- **Reading predecessor in the generated track queue:** IGL-Nav: Incremental 3D Gaussian Localization for Image-goal Navigation (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** end of this track queue (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Does Vision-Langauge-Exploration Pe-training benefit navigation?; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: Our main contributions can be summarized as follows: • We present MTU3D, bridging visual grounding and exploration for efficient and versatile embodied navigation. • We propose a unified objective that ... (p. 3, Method); preserve the objective/update rule: The unified decision scores SU t are optimized with binary cross-entropy loss, teaching the model to assign higher scores to appropriate query locations based on the current state and goal. (p. 5, 3.4. Vision-Language-Exploration Training).
2. Use the paper-reported task/data/environment cue: Unlike other benchmarks, SG3D emphasizes task consistency across multiple steps, making it more complex. (p. 6, 4.2. Quantitative Results).
3. Compare against the reported or matched baseline: 3 demonstrate that our proposed MTU3D significantly outperforms all baselines in terms of SR across both Val Seen and Val Unseen settings. (p. 6, 4.2. Quantitative Results).
4. Report the body metric with its denominator and aggregation: Furthermore, GPT4o with MTU3D achieves even better performance, reaching 51.1% LLM-SR and 42.6% LLM-SPL. (p. 7, 4.2. Quantitative Results).
5. Re-run the reported ablation or stress/failure condition: OVON GOAT SG3D Dataset 15 20 25 30 35 40 SR (%) 27.8 22.2 22.9 33.3 36.1 27.9 VLE w/o vle w/ vle (a) Effect of VLE. (p. 8, 4.4. Qualitative results); if none is reported, design one around: In contrast, reinforcement learning (RL)-based embodied agents can explore environments but often struggle with sample inefficiency [71], poor generalization due to limited training data [20, 57, 62] and the lack ... (p. 2, 1. Introduction).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 3 (Method), p. 2 (1. Introduction), match the reported outcome at p. 6 (Figure/Table caption), p. 3 (Figure/Table caption), p. 7 (Figure/Table caption), and measure the boundary at p. 2 (1. Introduction), p. 1 (Abstract).

## Falsifiable research question

Under the paper's stated interface (Our main contributions can be summarized as follows: • We present MTU3D, bridging visual grounding and exploration for efficient and versatile embodied ...), does the paper-specific mechanism (Our main contributions can be summarized as follows: • We present MTU3D, bridging visual grounding and exploration for efficient and versatile embodied ...) retain the reported evaluation outcome (Furthermore, GPT4o with MTU3D achieves even better performance, reaching 51.1% LLM-SR and 42.6% LLM-SPL.) when tested against the paper's strongest explicit boundary (In contrast, reinforcement learning (RL)-based embodied agents can explore environments but often struggle with sample inefficiency [71], poor ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (Furthermore, GPT4o with MTU3D achieves even better performance, reaching 51.1% LLM-SR and 42.6% LLM-SPL.) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (13 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** Our main contributions can be summarized as follows: • We present MTU3D, bridging visual grounding and exploration for efficient and versatile embodied navigation. • We propose a unified objective that ... (p. 3, Method).
- **Paper-supported outcome:** Table 4. Sequential task navigation results on SG3D-Nav [87]. Multi-modal Lifelong Navigation. The results in Tab. 5 highlight the significant performance improvement of our MTU3D over baseline methods in lifelong ... (p. 6, Figure/Table caption).
- **Strongest explicit boundary:** In contrast, reinforcement learning (RL)-based embodied agents can explore environments but often struggle with sample inefficiency [71], poor generalization due to limited training data [20, 57, 62] and the lack ... (p. 2, 1. Introduction).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
