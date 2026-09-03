# SaPaVe: Towards Active Perception and Manipulation in Vision-Language Action Models for Robotics

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Liu_SaPaVe_Towards_Active_Perception_and_Manipulation_in_Vision-Language_Action_Models_CVPR_2026_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_SaPaVe_Towards_Active_Perception_and_Manipulation_in_Vision-Language_Action_Models_CVPR_2026_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, active perception, Robotics
- Official paper: https://openaccess.thecvf.com/content/CVPR2026/html/Liu_SaPaVe_Towards_Active_Perception_and_Manipulation_in_Vision-Language_Action_Models_CVPR_2026_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_SaPaVe_Towards_Active_Perception_and_Manipulation_in_Vision-Language_Action_Models_CVPR_2026_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 However, this discretization hinders fine-grained camera control and manipulation, as it fails to connect high-level semantics with the continuous camera pose space.를 문제로 두고, In summary, our contributions are threefold: • We propose SaPaVe, a novel end-to-end framework that first achieves active manipulation with a bottom-up learning strategy in a data-efficient way. • We introduce ActiveViewPose-200K, ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Active perception and manipulation are crucial for robots to interact with complex scenes.
- **p. 1 / Abstract - extractive body cue:** Existing methods struggle to unify semantic-driven perception actively with robust, viewpoint-invariant execution accordingly.
- **p. 1 / Abstract - extractive body cue:** To this end, we propose SaPaVe, an end-to-end framework that jointly learns these capabilities in a data-efficient manner.
- **p. 1 / Abstract - extractive body cue:** Central to our approach is a decoupling of camera and manipulation actions, contrary to shared-action-space, and learning in a bottom-up strategy: we first train semantic ...
- **p. 1 / Abstract - extractive body cue:** To support this, we introduce ActiveViewPose-200K, comprising † Corresponding author ‡ Project leader 200k image-language-camera movement pairs for semantic camera movement learning, and a 3D ...
- **p. 2 / 1. Introduction - extractive body cue:** However, this discretization hinders fine-grained camera control and manipulation, as it fails to connect high-level semantics with the continuous camera pose space.
- **p. 2 / 1. Introduction - extractive body cue:** To address the limitations of fixed-viewpoint manipulation evaluation, we introduce the first simulated active manipulation benchmark, featuring 12 richly annotated tasks across 100 objects and ...

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** In summary, our contributions are threefold: • We propose SaPaVe, a novel end-to-end framework that first achieves active manipulation with a bottom-up learning strategy in ...
- **p. 2 / 1. Introduction - extractive body cue:** To address the limitations of fixed-viewpoint manipulation evaluation, we introduce the first simulated active manipulation benchmark, featuring 12 richly annotated tasks across 100 objects and ...
- **p. 4 / Model - extractive body cue:** To bridge this gap, we propose Universal Spatial Knowledge Injection, which efficiently leverages as much 3D information as possible to directly optimize the action output.
- **p. 4 / Model - extractive body cue:** Therefore, we propose Decoupled Action Heads and Camera Adapter to enable our model to acquire rich semantic active perception priors and retain general manipulation knowledge ...
- **p. 5 / 3.3. Two-Stage Training Strategy - extractive body cue:** To fill this gap, we propose a large-scale, high-quality dataset, ActiveViewPose-200K, comprising 200k image-language and camera movement pairs (see Sec.
- **p. 3 / 3.1. Problem Formulation - extractive body cue:** Given an observation Ot ∈O and a language instruction L ∈L, the policy predicts a joint action trajectory At = {Ahead,t, Aother,t} ∈A.
- **p. 3 / 3.2. Architecture - extractive body cue:** First, directly adding camera movement into the existing VLA action space would break the large-scale fixed-view manipulation priors learned from previous training.
- **p. 4 / 3.2. Architecture - extractive body cue:** VLM Vision Encoder Text Tokenizer Camera Adapter Get a white bowl from the cabinet then stack the bowls on the right Task Instruction Active Ego ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Given an observation Ot ∈O and a language instruction L ∈L, the policy predicts a joint action trajectory At = {Ahead,t, Aother,t} ∈A. | image/video, language instruction, proprioception과 history | p. 3 (3.1. Problem Formulation), p. 4 (Model) |
| State/latent | Given, observation, language, instruction, policy, predicts, joint, action, trajectory, Ahead, Aother, SaPaVe | language-grounded task state와 action-policy context | p. 3 (3.1. Problem Formulation), p. 4 (Model), p. 3 (3.1. Problem Formulation) |
| Output/action | SaPaVe can process RGB images and task instructions and output camera movement and manipulation actions in a decoupled action space. | continuous action, pose 또는 action chunk | p. 4 (Model), p. 3 (3.1. Problem Formulation), p. 4 (3.2. Architecture) |
| Objective/outcome | The objective is to minimize the Mean Squared Error between the predicted ego camera movement Ahead and the groundtruth A∗ head,t, defined as Lstage1 = LMSE(Ahead,t, A∗ head,t). | instruction following, task success, generalization과 latency | p. 5 (3.3. Two-Stage Training Strategy), p. 5 (3.3. Two-Stage Training Strategy), p. 4 (Model) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** In summary, our contributions are threefold: • We propose SaPaVe, a novel end-to-end framework that first achieves active manipulation with a bottom-up learning strategy in ...
- **p. 2 / 1. Introduction - extractive body cue:** To address the limitations of fixed-viewpoint manipulation evaluation, we introduce the first simulated active manipulation benchmark, featuring 12 richly annotated tasks across 100 objects and ...
- **p. 4 / Model - extractive body cue:** To bridge this gap, we propose Universal Spatial Knowledge Injection, which efficiently leverages as much 3D information as possible to directly optimize the action output.
- **p. 4 / Model - extractive body cue:** Therefore, we propose Decoupled Action Heads and Camera Adapter to enable our model to acquire rich semantic active perception priors and retain general manipulation knowledge ...
- **p. 5 / 3.3. Two-Stage Training Strategy - extractive body cue:** To fill this gap, we propose a large-scale, high-quality dataset, ActiveViewPose-200K, comprising 200k image-language and camera movement pairs (see Sec.
- **p. 7 / Figure/Table caption - extractive body cue:** Table 3. Performance on active manipulation in real-world set- tings. We report the success rate (%) compared to the existing VLA models. Our approach achieves ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. We propose SaPaVe, an end-to-end active manipulation framework that jointly integrates semantic active perception and active- view execution; the former selectively shifting viewpoints ...
- **p. 7 / 4.2. Semantic Active Perception Evaluation - extractive body cue:** As shown in Table 1, our model significantly outperforms powerful VLMs across all test splits, especially on test2, where semantic understanding is paramount.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (Figure/Table caption), p. 1 (Figure/Table caption) |
| Embodiment/environment | Pick-and-Place Pick-and-Place Arti-Manip Arti-Manip π0 [6] 55 45 45 35 45.00 GR00T-N1 [5] 60 55 50 50 53.75 Ours 90 85 85 80 85.00 robot teleoperated dataset, including 4 task categories: Occluded/Out-of-View ... | hardware/simulator version and reset protocol | p. 7 (4.1. Experimental Setup), p. 6 (4.1. Experimental Setup) |
| Dataset/benchmark | Our model demonstrates robust generalization when performing active manipulation across unseen objects, varying lighting conditions, and diverse scenes. | role, split, size and leakage | p. 7 (4.1. Experimental Setup), p. 6 (4.1. Experimental Setup), p. 8 (4.4. Comparison with existing VLA models), p. 8 (4.6. Ablation Studies) |
| Metric | For all experiments, we report the success rate. | definition, denominator, direction and uncertainty | p. 7 (4.1. Experimental Setup), p. 7 (4.3. Fixed and Dynamic Cameras Evaluation), p. 8 (4.6. Ablation Studies) |
| Baseline/ablation | Figure 1. We propose SaPaVe, an end-to-end active manipulation framework that jointly integrates semantic active perception and active- view execution; the former selectively shifting viewpoints to reveal task-critical cues in cluttered ... | fair input/data/compute/action matching | p. 1 (Figure/Table caption), p. 7 (4.1. Experimental Setup), p. 6 (4. Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 7 / 4.4. Comparison with existing VLA models - extractive body cue:** Two main factors account for this shortfall: (1) Direct VLA fine-tuning does not provide sufficient active perception priors.
- **p. 7 / 4.3. Fixed and Dynamic Cameras Evaluation - extractive body cue:** This result indicates that a fixed camera greatly limits the model's ability to explore the accessible space, leading to failures for active manipulation.
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. We propose SaPaVe, an end-to-end active manipulation framework that jointly integrates semantic active perception and active- view execution; the former selectively shifting viewpoints ...
- **p. 8 / 4.5. Generalization Ability Evaluation - extractive body cue:** 4, our model demonstrates strong generalization to previously unseen objects, indicating robust high-level semantic understanding that enables it to interpret out-of-distribution objects and correctly follow ...
- **p. 6 / 4. Experiments - extractive body cue:** (4) How well does our model generalize to out-of-distribution (OOD) scenarios (Sec.
- **p. 8 / 4.6. Ablation Studies - extractive body cue:** Universal Spatial Knowledge Injection greatly enhances the model's robustness for basic operations under active views.

## Why Read It

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 However, this discretization hinders fine-grained camera control and manipulation, as it fails to connect high-level semantics with the continuous camera pose space.를 문제로 두고, In summary, our contributions are threefold: • We propose SaPaVe, a novel end-to-end framework that first achieves active manipulation with a bottom-up learning strategy in a data-efficient way. • We introduce ActiveViewPose-200K, ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Problem Formulation), p. 3 (3.1. Problem Formulation), p. 4 (Model), p. 3 (3.1. Problem Formulation) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
