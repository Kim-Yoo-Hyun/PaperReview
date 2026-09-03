# Insights — AT-VLA: Adaptive Tactile Injection for Enhanced Feedback Reaction in Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Li_AT-VLA_Adaptive_Tactile_Injection_for_Enhanced_Feedback_Reaction_in_Vision-Language-Action_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Li_AT-VLA_Adaptive_Tactile_Injection_for_Enhanced_Feedback_Reaction_in_Vision-Language-Action_CVPR_2026_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1. Introduction - extractive body cue:** Our main contributions are as follows: 1) We propose Adaptive Tactile Injection, making the first attempt to balance pretrained knowledge with the learning of newly ...
- **p. 4 / 3.2. Adaptive Tactile Injection - extractive body cue:** Therefore, to address these issues, we propose the Adaptive Tactile Injection module, which dynamically controls when and where tactile feedback is injected and enables the ...
- **p. 5 / 3.3. Effective Tactile Reaction Dual-Stream - extractive body cue:** Concretely, we propose a Tactile Generation strategy, which enables the model to forecast both the 3D normal and tangential forces for the next time step.
- **p. 2 / 1. Introduction - extractive body cue:** Specifically, a learnable Tactile Gate is designed to automatically modulate the contribution of each modality across different manipulation phases, determining whether tactile features should be ...
- **p. 4 / 3.1. Framework of AT-VLA - extractive body cue:** To enable the model to handle contact-rich tasks, we introduce an additional tactile encoder.
- **p. 3 / 3.1. Framework of AT-VLA - extractive body cue:** 2, the policy πθ takes as input the image observations I = {Ih, Ir, Il} from the head camera, right wrist camera, and left wrist ...
- **p. 5 / 3.3. Effective Tactile Reaction Dual-Stream - extractive body cue:** These designs encourage the model to develop a more comprehensive representation of physical dynamics and tactile semantics, bridging instantaneous contact perception and predictive interaction reasoning.
- **Contribution anchor:** p. 2 (1. Introduction), p. 4 (3.2. Adaptive Tactile Injection), p. 5 (3.3. Effective Tactile Reaction Dual-Stream), p. 2 (1. Introduction), p. 4 (3.1. Framework of AT-VLA), p. 3 (3.1. Framework of AT-VLA)

### Strongest assumption and failure boundary

- **p. 2 / 1. Introduction - extractive body cue:** Since pretrained open-source manipulation datasets rarely include tactile information, researchers [4, 21, 43] often address this limitation by incorporating these modalities during downstream tasks finetuning.
- **p. 2 / 1. Introduction - extractive body cue:** 4) Unlike prior tactilebased policies that heavily rely on tactile inputs, AT-VLA, although trained with tactile feedback, maintains strong performance even in the absence of ...
- **p. 6 / 4.2. Contact-rich Task Evaluation - extractive body cue:** In contrast, our model, although capable of grasping the lid, does not always guarantee a sufficiently firm grip, occasionally leading to failure cases where the ...
- **p. 5 / 4.1. Setup - extractive body cue:** Failure to do so may cause the zipper to get stuck or jammed. b).
- **p. 6 / 4.2. Contact-rich Task Evaluation - extractive body cue:** We found that training them on the full sequence often leads to failures during the grasping stage, which makes it difficult to reveal their core ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4. Visualization. We visualize the execution progress of four typical contact-rich tasks. is crucial for real-world robotic applications where sensor failures or missing modalities ...
- **p. 8 / 5. Conclusion - extractive body cue:** Future work may explore scaling this framework to more complex tasks and diverse real-world environments, further advancing general-purpose embodied intelligence.
- **Boundary to test:** In contrast, our model, although capable of grasping the lid, does not always guarantee a sufficiently firm grip, occasionally leading to failure cases where the gripper slips during unscrewing.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Our main contributions are as follows: 1) We propose Adaptive Tactile Injection, making the first attempt to balance pretrained knowledge with the learning of newly introduced tactile representations. | p. 2 (1. Introduction), p. 4 (3.2. Adaptive Tactile Injection) |
| Reported outcome | It can reflect how much improvement our method achieves. | p. 5 (4.2. Contact-rich Task Evaluation), p. 6 (4.2. Contact-rich Task Evaluation) |
| Failure/limitation | In contrast, our model, although capable of grasping the lid, does not always guarantee a sufficiently firm grip, occasionally leading to failure cases where the gripper slips during unscrewing. | p. 6 (4.2. Contact-rich Task Evaluation), p. 5 (4.1. Setup) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Paper-specific interface:** 2, the policy πθ takes as input the image observations I = {Ih, Ir, Il} from the head camera, right wrist camera, and left wrist camera, respectively; the language instruction ... (p. 3, 3.1. Framework of AT-VLA).
- **Paper-specific mechanism:** Our main contributions are as follows: 1) We propose Adaptive Tactile Injection, making the first attempt to balance pretrained knowledge with the learning of newly introduced tactile representations. (p. 2, 1. Introduction).
- **Evidence boundary:** the reported outcome is As shown in Table 1, our model outperforms all baseline methods. (p. 6, 4.2. Contact-rich Task Evaluation); the relevant task/metric cue is We report the success rate of each subtask, reflecting the progress. (p. 6, 4.2. Contact-rich Task Evaluation). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** In contrast, our model, although capable of grasping the lid, does not always guarantee a sufficiently firm grip, occasionally leading to failure cases where the gripper slips during unscrewing. (p. 6, 4.2. Contact-rich Task Evaluation).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `Manipulation, contact, tactile, and dexterity`; tags: `Robotics, VLA, tactile sensing, contact-rich manipulation, real-time control`.
- **Reading predecessor in the generated track queue:** Reactive Diffusion Policy: Slow-Fast Visual-Tactile Policy Learning for Contact-Rich Manipulation (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** ForceVLA2: Unleashing Hybrid Force-Position Control with Force Awareness for Contact-Rich Manipulation (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** In contrast, our model, although capable of grasping the lid, does not always guarantee a sufficiently firm grip, occasionally leading to failure cases where the gripper slips during unscrewing.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: 2, the policy πθ takes as input the image observations I = {Ih, Ir, Il} from the head camera, right wrist camera, and left wrist camera, respectively; the language instruction ... (p. 3, 3.1. Framework of AT-VLA); preserve the objective/update rule: All objectives are trained simultaneously, under the overall supervision L = La + λ1 ∗Lg + λ2 ∗Lr, λ1 and λ2 are all both to 0.01 to balance different losses' ... (p. 5, 3.4. Training Objectives and Inference Pipeline).
2. Use the paper-reported task/data/environment cue: 2) In contrast, VTLA and RDP, which do not have pretrained models on large-scale datasets, are trained only on the subset of our downstream tasks corresponding to the contact-rich manipulation ... (p. 6, 4.2. Contact-rich Task Evaluation).
3. Compare against the reported or matched baseline: Compared with state-of-the-art VLA models GO-1 and π0.5, which are trained without tactile feedback, our model demonstrates comparable performance during the pre-contact manipulation phase, indicating that it effectively preserves the ... (p. 6, 4.2. Contact-rich Task Evaluation).
4. Report the body metric with its denominator and aggregation: We report the success rate of each subtask, reflecting the progress. (p. 6, 4.2. Contact-rich Task Evaluation).
5. Re-run the reported ablation or stress/failure condition: Modality-agnostic evaluation.The AT-VLA variants with (w/.) and without (w/o.) tactile input share identical model weights, differing only in whether tactile information is provided during inference. (p. 6, 4.3. Modality-agnostic Evaluation); if none is reported, design one around: In contrast, our model, although capable of grasping the lid, does not always guarantee a sufficiently firm grip, occasionally leading to failure cases where the gripper slips during unscrewing. (p. 6, 4.2. Contact-rich Task Evaluation).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 2 (1. Introduction), p. 4 (3.2. Adaptive Tactile Injection), match the reported outcome at p. 6 (4.2. Contact-rich Task Evaluation), p. 7 (Figure/Table caption), p. 6 (4.2. Contact-rich Task Evaluation), and measure the boundary at p. 6 (4.2. Contact-rich Task Evaluation), p. 7 (4.4.1. Contribution of Each Component).

## Falsifiable research question

Under the paper's stated interface (2, the policy πθ takes as input the image observations I = {Ih, Ir, Il} from the head camera, right wrist camera, ...), does the paper-specific mechanism (Our main contributions are as follows: 1) We propose Adaptive Tactile Injection, making the first attempt to balance pretrained knowledge with the ...) retain the reported evaluation outcome (We report the success rate of each subtask, reflecting the progress.) when tested against the paper's strongest explicit boundary (In contrast, our model, although capable of grasping the lid, does not always guarantee a sufficiently firm grip, ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (We report the success rate of each subtask, reflecting the progress.) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (11 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** Our main contributions are as follows: 1) We propose Adaptive Tactile Injection, making the first attempt to balance pretrained knowledge with the learning of newly introduced tactile representations. (p. 2, 1. Introduction).
- **Paper-supported outcome:** As shown in Table 1, our model outperforms all baseline methods. (p. 6, 4.2. Contact-rich Task Evaluation).
- **Strongest explicit boundary:** In contrast, our model, although capable of grasping the lid, does not always guarantee a sufficiently firm grip, occasionally leading to failure cases where the gripper slips during unscrewing. (p. 6, 4.2. Contact-rich Task Evaluation).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
