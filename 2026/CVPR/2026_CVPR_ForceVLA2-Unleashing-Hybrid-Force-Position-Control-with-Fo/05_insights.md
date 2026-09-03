# Insights — ForceVLA2: Unleashing Hybrid Force-Position Control with Force Awareness for Contact-Rich Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Li_ForceVLA2_Unleashing_Hybrid_Force-Position_Control_with_Force_Awareness_for_Contact-Rich_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Li_ForceVLA2_Unleashing_Hybrid_Force-Position_Control_with_Force_Awareness_for_Contact-Rich_CVPR_2026_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1. Introduction - extractive body cue:** Our contributions are summarized as follows: • We introduce ForceVLA2, the first end-to-end hybrid force-position control framework with force awareness for VLAs, enhancing contact-rich manipulation ...
- **p. 2 / 1. Introduction - extractive body cue:** To overcome these limitations, we propose ForceVLA2, a novel framework that equips VLAs with active hybrid force-position control with force awareness to enhance contact-rich manipulation, ...
- **p. 1 / Abstract - extractive body cue:** We propose ForceVLA2, an end-to-end vision-language-action framework that equips robots with hybrid force-position control and explicit force awareness.
- **p. 3 / 3.1. Long-Horizon Force Awareness via Prompting - extractive body cue:** To address this, we introduce force prompts as textual cues that indicate the current subtask and encode stage-specific physical context, thereby constructing force-aware task concepts.
- **p. 3 / 3. ForceVLA2 Framework - extractive body cue:** Building upon these principles, we propose the ForceVLA2 architecture, which integrates multi-scale perception, contextual reasoning, and force-aware manipulation into a unified VLA framework.
- **p. 4 / 3.2. Short-Horizon Force-to-Control Loop - extractive body cue:** (3) The encoded EE 6D pose and force tokens are concatenated to form a multi-modal state representation, Estate = [EP ; EF ], which is ...
- **p. 5 / 3.2.2. Adaptive Routing and Decoding - extractive body cue:** By conditioning the denoising process on the fused visual-language-force representation, the model achieves closed-loop, context-aware control that adapts fluidly to contact-rich interaction.
- **Contribution anchor:** p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (Abstract), p. 3 (3.1. Long-Horizon Force Awareness via Prompting), p. 3 (3. ForceVLA2 Framework), p. 4 (3.2. Short-Horizon Force-to-Control Loop)

### Strongest assumption and failure boundary

- **p. 2 / 1. Introduction - extractive body cue:** However, current VLAs still lack the ability to reason about physical dynamics and fine-grained contact interactions, which are essential for real-world, contact-rich manipulation.
- **p. 2 / 1. Introduction - extractive body cue:** Current VLAs, however, still lack mechanisms to reason about the spatiotemporal relationships required across different task stages and to integrate force perception with active force-position ...
- **p. 1 / 1. Introduction - extractive body cue:** However, these models remain confined to virtual domains, lacking the embodiment necessary for authentic physical understanding and interaction in real-world settings.
- **p. 1 / 1. Introduction - extractive body cue:** To overcome this limitation, vision-language-action models (VLAs) [2, 3, 22, 47, 50] extend VLMs toward physical intelligence by seamlessly connecting perception and reasoning to embodied ...
- **p. 8 / 6. Conclusion - extractive body cue:** The model also consistently reduces failures caused by arm overload and unstable contact, and ablation studies show monotonically improved performance as force prompts, the CrossScale ...
- **p. 8 / 5.2. Main Experiment Results - extractive body cue:** In contrast, other VLAs slowly chase the new EE 6D pose, leading to failure to maintain stable contact.
- **p. 7 / 5.2. Main Experiment Results - extractive body cue:** ForceVLA2 exhibits robust position and orientation following, and in object search tasks, it can still perform successful re-grasps even when visual observations fail. on force-sensitive ...
- **Boundary to test:** The model also consistently reduces failures caused by arm overload and unstable contact, and ablation studies show monotonically improved performance as force prompts, the CrossScale MoE, and multimodal fusion are added, with ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Our contributions are summarized as follows: • We introduce ForceVLA2, the first end-to-end hybrid force-position control framework with force awareness for VLAs, enhancing contact-rich manipulation by integrating force-prompt-driven VL ... | p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Reported outcome | 1, ForceVLA2 significantly outperforms all baselines, achieving a 66% average success rate across all tasks. | p. 6 (5.2. Main Experiment Results), p. 7 (5.2. Main Experiment Results) |
| Failure/limitation | The model also consistently reduces failures caused by arm overload and unstable contact, and ablation studies show monotonically improved performance as force prompts, the CrossScale MoE, and multimodal fusion are added, with ... | p. 8 (6. Conclusion), p. 8 (5.2. Main Experiment Results) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Paper-specific interface:** Our contributions are summarized as follows: • We introduce ForceVLA2, the first end-to-end hybrid force-position control framework with force awareness for VLAs, enhancing contact-rich manipulation by integrating force-prompt-driven VL ... (p. 2, 1. Introduction).
- **Paper-specific mechanism:** To overcome these limitations, we propose ForceVLA2, a novel framework that equips VLAs with active hybrid force-position control with force awareness to enhance contact-rich manipulation, as shown in Fig. (p. 2, 1. Introduction).
- **Evidence boundary:** the reported outcome is Entries indicate success rate (%). gray : baseline results. (p. 8, 5.2. Main Experiment Results); the relevant task/metric cue is 1, ForceVLA2 significantly outperforms all baselines, achieving a 66% average success rate across all tasks. (p. 6, 5.2. Main Experiment Results). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** ForceVLA2 exhibits robust position and orientation following, and in object search tasks, it can still perform successful re-grasps even when visual observations fail. on force-sensitive tasks such as object search, ... (p. 7, 5.2. Main Experiment Results).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `Manipulation, contact, tactile, and dexterity`; tags: `Robotics, VLA, force sensing, hybrid force-position control, contact-rich manipulation`.
- **Reading predecessor in the generated track queue:** AT-VLA: Adaptive Tactile Injection for Enhanced Feedback Reaction in Vision-Language-Action Models (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Dexterous World Models (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** The model also consistently reduces failures caused by arm overload and unstable contact, and ablation studies show monotonically improved performance as force prompts, the CrossScale MoE, and multimodal fusion are added, with ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: Our contributions are summarized as follows: • We introduce ForceVLA2, the first end-to-end hybrid force-position control framework with force awareness for VLAs, enhancing contact-rich manipulation by integrating force-prompt-driven VL ... (p. 2, 1. Introduction); preserve the objective/update rule: This mechanism enables ForceVLA2 to inherit VLM knowledge, assess subtask completion, transition across stages, and explicitly update force cues to guide force-aware manipulation. (p. 3, 3.1. Long-Horizon Force Awareness via Prompting).
2. Use the paper-reported task/data/environment cue: Our experimental benchmark consists of 5 contact-rich manipulation tasks within the proposed ForceVLA2-Dataset: Press the bottle, Clean the vase, Clean the board, Retrieve the plate, and Assemble gears. (p. 6, 5.1. Experiment Setting).
3. Compare against the reported or matched baseline: 1, ForceVLA2 significantly outperforms all baselines, achieving a 66% average success rate across all tasks. (p. 6, 5.2. Main Experiment Results).
4. Report the body metric with its denominator and aggregation: 1, ForceVLA2 significantly outperforms all baselines, achieving a 66% average success rate across all tasks. (p. 6, 5.2. Main Experiment Results).
5. Re-run the reported ablation or stress/failure condition: Compared with models without force inputs, ForceVLA2 and ForceVLA, which incorporate force feedback, show remarkable improvements 8916 (p. 6, 5.2. Main Experiment Results); if none is reported, design one around: ForceVLA2 exhibits robust position and orientation following, and in object search tasks, it can still perform successful re-grasps even when visual observations fail. on force-sensitive tasks such as object search, ... (p. 7, 5.2. Main Experiment Results).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 2 (1. Introduction), p. 2 (1. Introduction), match the reported outcome at p. 8 (5.2. Main Experiment Results), p. 8 (Figure/Table caption), p. 6 (5.2. Main Experiment Results), and measure the boundary at p. 7 (5.2. Main Experiment Results), p. 8 (6. Conclusion).

## Falsifiable research question

Under the paper's stated interface (Our contributions are summarized as follows: • We introduce ForceVLA2, the first end-to-end hybrid force-position control framework with force awareness for VLAs, ...), does the paper-specific mechanism (To overcome these limitations, we propose ForceVLA2, a novel framework that equips VLAs with active hybrid force-position control with force awareness to ...) retain the reported evaluation outcome (1, ForceVLA2 significantly outperforms all baselines, achieving a 66% average success rate across all tasks.) when tested against the paper's strongest explicit boundary (ForceVLA2 exhibits robust position and orientation following, and in object search tasks, it can still perform successful re-grasps ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (1, ForceVLA2 significantly outperforms all baselines, achieving a 66% average success rate across all tasks.) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (10 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** To overcome these limitations, we propose ForceVLA2, a novel framework that equips VLAs with active hybrid force-position control with force awareness to enhance contact-rich manipulation, as shown in Fig. (p. 2, 1. Introduction).
- **Paper-supported outcome:** Entries indicate success rate (%). gray : baseline results. (p. 8, 5.2. Main Experiment Results).
- **Strongest explicit boundary:** ForceVLA2 exhibits robust position and orientation following, and in object search tasks, it can still perform successful re-grasps even when visual observations fail. on force-sensitive tasks such as object search, ... (p. 7, 5.2. Main Experiment Results).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
