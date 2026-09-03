# AT-VLA: Adaptive Tactile Injection for Enhanced Feedback Reaction in Vision-Language-Action Models

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Li_AT-VLA_Adaptive_Tactile_Injection_for_Enhanced_Feedback_Reaction_in_Vision-Language-Action_CVPR_2026_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Li_AT-VLA_Adaptive_Tactile_Injection_for_Enhanced_Feedback_Reaction_in_Vision-Language-Action_CVPR_2026_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: NEXT
- Tags: Robotics, VLA, tactile sensing, contact-rich manipulation, real-time control
- Official paper: https://openaccess.thecvf.com/content/CVPR2026/html/Li_AT-VLA_Adaptive_Tactile_Injection_for_Enhanced_Feedback_Reaction_in_Vision-Language-Action_CVPR_2026_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2026/papers/Li_AT-VLA_Adaptive_Tactile_Injection_for_Enhanced_Feedback_Reaction_in_Vision-Language-Action_CVPR_2026_paper.pdf
- Code/Project: https://openaccess.thecvf.com/content/CVPR2026/html/Li_AT-VLA_Adaptive_Tactile_Injection_for_Enhanced_Feedback_Reaction_in_Vision-Language-Action_CVPR_2026_paper.html
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Manipulation, contact, tactile, and dexterity의 tactile 문제를 이해하기 위해 읽는다. 본문은 Since pretrained open-source manipulation datasets rarely include tactile information, researchers [4, 21, 43] often address this limitation by incorporating these modalities during downstream tasks finetuning.를 문제로 두고, Our main contributions are as follows: 1) We propose Adaptive Tactile Injection, making the first attempt to balance pretrained knowledge with the learning of newly introduced tactile representations.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Vision-Language-Action (VLA) models have significantly advanced the capabilities of robotic agents in executing diverse tasks; however, they still face challenges in contactrich manipulation scenarios that ...
- **p. 1 / Abstract - extractive body cue:** To address this limitation, recent studies have attempted to incorporate tactile signals during downstream tasks, enabling pretrained VLAs to interpret tactile feedback.
- **p. 1 / Abstract - extractive body cue:** Nevertheless, introducing new modalities during finetuning, which are rarely present in the pretrain stage, may disrupt the pretrained capabilities of VLAs.
- **p. 1 / Abstract - extractive body cue:** In addition, the inherently slow inference speed of VLAs hampers real-time responsiveness and limits the effective utilization of tactile feedback for action adjustment.
- **p. 1 / Abstract - extractive body cue:** To overcome these challenges, we propose Adaptive Tactile Vision-Language-Action (AT-VLA), which introduces a novel Adaptive Tactile Injection mechanism.
- **p. 2 / 1. Introduction - extractive body cue:** Since pretrained open-source manipulation datasets rarely include tactile information, researchers [4, 21, 43] often address this limitation by incorporating these modalities during downstream tasks finetuning.
- **p. 2 / 1. Introduction - extractive body cue:** 4) Unlike prior tactilebased policies that heavily rely on tactile inputs, AT-VLA, although trained with tactile feedback, maintains strong performance even in the absence of ...

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** Our main contributions are as follows: 1) We propose Adaptive Tactile Injection, making the first attempt to balance pretrained knowledge with the learning of newly ...
- **p. 4 / 3.2. Adaptive Tactile Injection - extractive body cue:** Therefore, to address these issues, we propose the Adaptive Tactile Injection module, which dynamically controls when and where tactile feedback is injected and enables the ...
- **p. 5 / 3.3. Effective Tactile Reaction Dual-Stream - extractive body cue:** Concretely, we propose a Tactile Generation strategy, which enables the model to forecast both the 3D normal and tangential forces for the next time step.
- **p. 2 / 1. Introduction - extractive body cue:** Specifically, a learnable Tactile Gate is designed to automatically modulate the contribution of each modality across different manipulation phases, determining whether tactile features should be ...
- **p. 4 / 3.1. Framework of AT-VLA - extractive body cue:** To enable the model to handle contact-rich tasks, we introduce an additional tactile encoder.
- **p. 3 / 3.1. Framework of AT-VLA - extractive body cue:** 2, the policy πθ takes as input the image observations I = {Ih, Ir, Il} from the head camera, right wrist camera, and left wrist ...
- **p. 5 / 3.3. Effective Tactile Reaction Dual-Stream - extractive body cue:** These designs encourage the model to develop a more comprehensive representation of physical dynamics and tactile semantics, bridging instantaneous contact perception and predictive interaction reasoning.
- **p. 5 / 3.3. Effective Tactile Reaction Dual-Stream - extractive body cue:** We extract the tactile token after the Action Expert module and employ a lightweight decoder network to generate the next-step tactile signal, supervised by an ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | 2, the policy πθ takes as input the image observations I = {Ih, Ir, Il} from the head camera, right wrist camera, and left wrist camera, respectively; the language instruction L; the ... | tactile image/force, vision과 proprioceptive history | p. 3 (3.1. Framework of AT-VLA), p. 4 (3.2. Adaptive Tactile Injection) |
| State/latent | policy, takes, input, image, observations, head, camera, right, wrist, left, respectively, language | contact geometry, force state 또는 latent dynamics | p. 3 (3.1. Framework of AT-VLA), p. 4 (3.2. Adaptive Tactile Injection), p. 2 (1. Introduction) |
| Output/action | With the tactile gate to determine when to incorporate tactile feedback, the action expert's architecture must be able to handle inputs under both states of the tactile gate, whether or not tactile ... | grasp/contact action, force command 또는 object motion | p. 4 (3.2. Adaptive Tactile Injection), p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Objective/outcome | All objectives are trained simultaneously, under the overall supervision L = La + λ1 ∗Lg + λ2 ∗Lr, λ1 and λ2 are all both to 0.01 to balance different losses' scale. | slip/contact success, force/pose error와 robustness | p. 5 (3.4. Training Objectives and Inference Pipeline), p. 4 (3.2. Adaptive Tactile Injection), p. 4 (3.1. Framework of AT-VLA) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** Our main contributions are as follows: 1) We propose Adaptive Tactile Injection, making the first attempt to balance pretrained knowledge with the learning of newly ...
- **p. 4 / 3.2. Adaptive Tactile Injection - extractive body cue:** Therefore, to address these issues, we propose the Adaptive Tactile Injection module, which dynamically controls when and where tactile feedback is injected and enables the ...
- **p. 5 / 3.3. Effective Tactile Reaction Dual-Stream - extractive body cue:** Concretely, we propose a Tactile Generation strategy, which enables the model to forecast both the 3D normal and tangential forces for the next time step.
- **p. 2 / 1. Introduction - extractive body cue:** Specifically, a learnable Tactile Gate is designed to automatically modulate the contribution of each modality across different manipulation phases, determining whether tactile features should be ...
- **p. 4 / 3.1. Framework of AT-VLA - extractive body cue:** To enable the model to handle contact-rich tasks, we introduce an additional tactile encoder.
- **p. 5 / 4.2. Contact-rich Task Evaluation - extractive body cue:** It can reflect how much improvement our method achieves.
- **p. 6 / 4.2. Contact-rich Task Evaluation - extractive body cue:** During the contact-rich stage, AT-VLA achieves an improvement over them, clearly demonstrating the necessity of tactile signals for complex manipulation tasks.
- **p. 6 / 4.2. Contact-rich Task Evaluation - extractive body cue:** Furthermore, when compared with policies that incorporate tactile feedback like VTLA and RDP, our model still achieves superior performance in contact-rich phase manipulation, validating the ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 5 (4.2. Contact-rich Task Evaluation), p. 6 (4.2. Contact-rich Task Evaluation) |
| Embodiment/environment | 2) In contrast, VTLA and RDP, which do not have pretrained models on large-scale datasets, are trained only on the subset of our downstream tasks corresponding to the contact-rich manipulation phases. | hardware/simulator version and reset protocol | p. 6 (4.2. Contact-rich Task Evaluation), p. 6 (4.2. Contact-rich Task Evaluation) |
| Dataset/benchmark | The robot is required to stamp within a designated region. | role, split, size and leakage | p. 6 (4.2. Contact-rich Task Evaluation), p. 6 (4.2. Contact-rich Task Evaluation), p. 5 (4.1. Setup), p. 5 (4.1. Setup) |
| Metric | We report the success rate of each subtask, reflecting the progress. | definition, denominator, direction and uncertainty | p. 6 (4.2. Contact-rich Task Evaluation), p. 6 (4.2. Contact-rich Task Evaluation), p. 5 (4.1. Setup) |
| Baseline/ablation | Compared with state-of-the-art VLA models GO-1 and π0.5, which are trained without tactile feedback, our model demonstrates comparable performance during the pre-contact manipulation phase, indicating that it effectively preserves the p ... | fair input/data/compute/action matching | p. 6 (4.2. Contact-rich Task Evaluation), p. 6 (4.2. Contact-rich Task Evaluation), p. 5 (4.2. Contact-rich Task Evaluation) |

## Explicit Limitations and Failure Boundary

- **p. 6 / 4.2. Contact-rich Task Evaluation - extractive body cue:** In contrast, our model, although capable of grasping the lid, does not always guarantee a sufficiently firm grip, occasionally leading to failure cases where the ...
- **p. 5 / 4.1. Setup - extractive body cue:** Failure to do so may cause the zipper to get stuck or jammed. b).
- **p. 6 / 4.2. Contact-rich Task Evaluation - extractive body cue:** We found that training them on the full sequence often leads to failures during the grasping stage, which makes it difficult to reveal their core ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4. Visualization. We visualize the execution progress of four typical contact-rich tasks. is crucial for real-world robotic applications where sensor failures or missing modalities ...
- **p. 8 / 5. Conclusion - extractive body cue:** Future work may explore scaling this framework to more complex tasks and diverse real-world environments, further advancing general-purpose embodied intelligence.
- **p. 5 / 4.1. Setup - extractive body cue:** Insufficient compliance could result in collisions with the neck of the vase. d).

## Why Read It

Manipulation, contact, tactile, and dexterity의 tactile 문제를 이해하기 위해 읽는다. 본문은 Since pretrained open-source manipulation datasets rarely include tactile information, researchers [4, 21, 43] often address this limitation by incorporating these modalities during downstream tasks finetuning.를 문제로 두고, Our main contributions are as follows: 1) We propose Adaptive Tactile Injection, making the first attempt to balance pretrained knowledge with the learning of newly introduced tactile representations.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (3.2. Adaptive Tactile Injection), p. 3 (3.1. Framework of AT-VLA), p. 4 (3.1. Framework of AT-VLA), p. 5 (3.3. Effective Tactile Reaction Dual-Stream) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (11 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** Since pretrained open-source manipulation datasets rarely include tactile information, researchers [4, 21, 43] often address this limitation by incorporating these modalities during downstream tasks finetuning. (p. 2, 1. Introduction).
- **Actual contribution:** Our main contributions are as follows: 1) We propose Adaptive Tactile Injection, making the first attempt to balance pretrained knowledge with the learning of newly introduced tactile representations. (p. 2, 1. Introduction).
- **Evaluation boundary:** As shown in Table 1, our model outperforms all baseline methods. (p. 6, 4.2. Contact-rich Task Evaluation).
- **Explicit failure boundary:** In contrast, our model, although capable of grasping the lid, does not always guarantee a sufficiently firm grip, occasionally leading to failure cases where the gripper slips during unscrewing. (p. 6, 4.2. Contact-rich Task Evaluation).
