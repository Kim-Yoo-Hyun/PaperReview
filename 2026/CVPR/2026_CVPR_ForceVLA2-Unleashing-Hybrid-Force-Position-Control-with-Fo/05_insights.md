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

- **Closed-loop position:** `tactile image/force, vision과 proprioceptive history → contact geometry, force state 또는 latent dynamics → grasp/contact action, force command 또는 object motion`.
- 이 논문의 재사용 가능한 지점은 A 6D force/torque sensor attached to the end-effector recorded interaction forces at 300 Hz, while the robot joint states and end-effector (EE) 6D poses were logged synchronously.를 ForceVLA2 takes multi-view images, task and force prompts, and proprioceptive states (EE pose and force) as input.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 contact geometry, force state 또는 latent dynamics가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 The model also consistently reduces failures caused by arm overload and unstable contact, and ablation studies show monotonically improved performance as force prompts, the CrossScale MoE, and multimodal fusion are added, with ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Our contributions are summarized as follows: • We introduce ForceVLA2, the first end-to-end hybrid force-position control framework with force awareness for VLAs, enhancing contact-rich manipulation by integrating force-prompt-driven VL ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `Manipulation, contact, tactile, and dexterity`; tags: `Robotics, VLA, force sensing, hybrid force-position control, contact-rich manipulation`.
- **Reading predecessor in the generated track queue:** AT-VLA: Adaptive Tactile Injection for Enhanced Feedback Reaction in Vision-Language-Action Models (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Dexterous World Models (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** The model also consistently reduces failures caused by arm overload and unstable contact, and ablation studies show monotonically improved performance as force prompts, the CrossScale MoE, and multimodal fusion are added, with ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Our experimental benchmark consists of 5 contact-rich manipulation tasks within the proposed ForceVLA2-Dataset: Press the bottle, Clean the vase, Clean the board, Retrieve the plate, and Assemble gears..
3. Compare against the body-reported baseline or a matched simpler baseline: 1, ForceVLA2 significantly outperforms all baselines, achieving a 66% average success rate across all tasks..
4. Report the body metric and its denominator/aggregation: 1, ForceVLA2 significantly outperforms all baselines, achieving a 66% average success rate across all tasks..
5. Re-run the body-reported ablation/failure condition: In particular, we conduct an ablation on the CrossScale MoE module by varying its modality inputs and outputs to verify the effectiveness of our design..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 2 (1. Introduction), p. 4 (3.2. Short-Horizon Force-to-Control Loop), p. 5 (3.2.2. Adaptive Routing and Decoding); the primary result is directionally consistent at p. 6 (5.2. Main Experiment Results), p. 7 (5.2. Main Experiment Results), p. 6 (5. Experiments); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 contributions, summarized, follows mechanism이 1, ForceVLA2 significantly outperforms all baselines, achieving a 66% average success rate across all tasks. 대비 1, ForceVLA2 significantly outperforms all baselines, achieving a 66% average success rate across all tasks.을 개선하고, The model also consistently reduces failures caused by arm overload and unstable contact, and ablation studies ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
