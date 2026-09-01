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

- **Closed-loop position:** `tactile image/force, vision과 proprioceptive history → contact geometry, force state 또는 latent dynamics → grasp/contact action, force command 또는 object motion`.
- 이 논문의 재사용 가능한 지점은 2, the policy πθ takes as input the image observations I = {Ih, Ir, Il} from the head camera, right wrist camera, and left wrist camera, respectively; the language instruction L; the ...를 With the tactile gate to determine when to incorporate tactile feedback, the action expert's architecture must be able to handle inputs under both states of the tactile gate, whether or not tactile ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 contact geometry, force state 또는 latent dynamics가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 In contrast, our model, although capable of grasping the lid, does not always guarantee a sufficiently firm grip, occasionally leading to failure cases where the gripper slips during unscrewing.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Our main contributions are as follows: 1) We propose Adaptive Tactile Injection, making the first attempt to balance pretrained knowledge with the learning of newly introduced tactile representations.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `Manipulation, contact, tactile, and dexterity`; tags: `Robotics, VLA, tactile sensing, contact-rich manipulation, real-time control`.
- **Reading predecessor in the generated track queue:** Reactive Diffusion Policy: Slow-Fast Visual-Tactile Policy Learning for Contact-Rich Manipulation (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** ForceVLA2: Unleashing Hybrid Force-Position Control with Force Awareness for Contact-Rich Manipulation (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** In contrast, our model, although capable of grasping the lid, does not always guarantee a sufficiently firm grip, occasionally leading to failure cases where the gripper slips during unscrewing.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: 2) In contrast, VTLA and RDP, which do not have pretrained models on large-scale datasets, are trained only on the subset of our downstream tasks corresponding to the contact-rich manipulation phases..
3. Compare against the body-reported baseline or a matched simpler baseline: Compared with state-of-the-art VLA models GO-1 and π0.5, which are trained without tactile feedback, our model demonstrates comparable performance during the pre-contact manipulation phase, indicating that it effectively preserves the p ....
4. Report the body metric and its denominator/aggregation: We report the success rate of each subtask, reflecting the progress..
5. Re-run the body-reported ablation/failure condition: Table 3. Ablation study. Each variant selectively removes or changes components to assess their contributions. Components Tactile Format Tasks Tactile Gate Adaptive Cross Attention.
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 4 (3.2. Adaptive Tactile Injection), p. 3 (3.1. Framework of AT-VLA), p. 4 (3.1. Framework of AT-VLA); the primary result is directionally consistent at p. 5 (4.2. Contact-rich Task Evaluation), p. 6 (4.2. Contact-rich Task Evaluation), p. 6 (4.2. Contact-rich Task Evaluation); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 main, contributions, follows mechanism이 Compared with state-of-the-art VLA models GO-1 and π0.5, which are trained without tactile feedback, our model ... 대비 We report the success rate of each subtask, reflecting the progress.을 개선하고, In contrast, our model, although capable of grasping the lid, does not always guarantee a sufficiently ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
