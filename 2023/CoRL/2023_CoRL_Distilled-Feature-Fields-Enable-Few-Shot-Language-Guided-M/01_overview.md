# Distilled Feature Fields Enable Few-Shot Language-Guided Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (20 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.mlr.press/v229/shen23a.html.
> PDF retrieval source: https://proceedings.mlr.press/v229/shen23a/shen23a.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2023 / CoRL
- Authors: not duplicated here when not verified in the registry source
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: NEXT
- Tags: Robotics, NeRF, Vision-Language, manipulation
- Official paper: https://proceedings.mlr.press/v229/shen23a.html
- Full-text retrieval: https://proceedings.mlr.press/v229/shen23a/shen23a.pdf
- Code/Project: https://f3rm.github.io/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (20 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Manipulation, contact, tactile, and dexterity의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 What form of scene representation would facilitate open-set generalization for robotic manipulation systems?를 문제로 두고, 3 Feature Fields for Robotic Manipulation (F3RM) We present Feature Fields for Robotic Manipulation (F3RM), our approach for distilling pre-trained representations from vision and vision-language models into 3D feature fields for open-e ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Self-supervised and language-supervised image models contain rich knowledge of the world that is important for generalization.
- **p. 1 / Abstract - extractive body cue:** Many robotic tasks, however, require a detailed understanding of 3D geometry, which is often lacking in 2D image features.
- **p. 1 / Abstract - extractive body cue:** This work bridges this 2D-to-3D gap for robotic manipulation by leveraging distilled feature fields to combine accurate 3D geometry with rich semantics from 2D foundation ...
- **p. 1 / Abstract - extractive body cue:** We present a few-shot learning method for 6-DOF grasping and placing that harnesses these strong spatial and semantic priors to achieve in-the-wild generalization to unseen ...
- **p. 1 / Abstract - extractive body cue:** Using features distilled from a vision-language model, CLIP, we present a way to designate novel objects for manipulation via free-text natural language, and demonstrate its ...
- **p. 1 / 1 Introduction - extractive body cue:** What form of scene representation would facilitate open-set generalization for robotic manipulation systems?
- **p. 1 / 1 Introduction - extractive body cue:** We evaluate the robot's ability to generalize using features sourced from self-supervised vision transformers (DINO ViT, see [4]).

## Core Idea

- **p. 3 / 3. Language-Guided Manipulation - extractive body cue:** 3 Feature Fields for Robotic Manipulation (F3RM) We present Feature Fields for Robotic Manipulation (F3RM), our approach for distilling pre-trained representations from vision and vision-language ...
- **p. 1 / Abstract - extractive body cue:** Using features distilled from a vision-language model, CLIP, we present a way to designate novel objects for manipulation via free-text natural language, and demonstrate its ...
- **p. 1 / 1 Introduction - extractive body cue:** The main contribution of this work is to study the use of DFFs instead for robotic manipulation.
- **p. 2 / 3. Language-Guided Manipulation - extractive body cue:** During learning, each demonstration D consists of the tuple ⟨{I}, T∗⟩, where {I}N i=1 are N RGB camera views of the scene and T∗is a ...
- **p. 2 / 3. Language-Guided Manipulation - extractive body cue:** We present few-shot learning experiments on grasping and placing tasks, where our robot is able to handle open-set generalization to objects that differ significantly in ...
- **p. 4 / 6 DOF Gripper Pose - extractive body cue:** (c) We concatenate feature vectors at these query points, then average over n (we use n = 2) demonstrations.
- **p. 5 / 6 DOF Gripper Pose - extractive body cue:** We speed up grasp pose inference by first running a coarse proposal step where we filter out regions in the feature field that are irrelevant ...
- **p. 5 / 6 DOF Gripper Pose - extractive body cue:** We use the selected demo from (a) in Jpose, and compute the language-guidance weight with the text features and average query point features. valid motion ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The robot then references demonstrations and language instructions to grasp objects specified by a user (Figure 1, right). | RGB-D, image set, point cloud, depth와 camera pose | p. 1 (1 Introduction), p. 1 (Body text (section boundary not confidently recovered)) |
| State/latent | robot, then, references, demonstrations, language, instructions, grasp, objects, specified, user, Figure, right | geometry, map, object/relationship state | p. 1 (1 Introduction), p. 1 (Body text (section boundary not confidently recovered)), p. 3 (3. Language-Guided Manipulation) |
| Output/action | Distilled Feature Fields Enable Few-Shot Language-Guided Manipulation William Shen∗1, Ge Yang∗1,2, Alan Yu1, Jansen Wong1, Leslie Pack Kaelbling1, Phillip Isola1 1MIT CSAIL, 2Institute for Artificial Intelligence and Fundamental Interac ... | point map, pose, scene graph, affordance 또는 query result | p. 1 (Body text (section boundary not confidently recovered)), p. 3 (3. Language-Guided Manipulation), p. 3 (3. Language-Guided Manipulation) |
| Objective/outcome | We optimize f by minimizing the quadratic loss Lfeat = P r∈R | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 3 (3. Language-Guided Manipulation), p. 4 (6 DOF Gripper Pose), p. 5 (6 DOF Gripper Pose) |

## Main Claims and Actual Contribution

- **p. 3 / 3. Language-Guided Manipulation - extractive body cue:** 3 Feature Fields for Robotic Manipulation (F3RM) We present Feature Fields for Robotic Manipulation (F3RM), our approach for distilling pre-trained representations from vision and vision-language ...
- **p. 1 / Abstract - extractive body cue:** Using features distilled from a vision-language model, CLIP, we present a way to designate novel objects for manipulation via free-text natural language, and demonstrate its ...
- **p. 1 / 1 Introduction - extractive body cue:** The main contribution of this work is to study the use of DFFs instead for robotic manipulation.
- **p. 2 / 3. Language-Guided Manipulation - extractive body cue:** During learning, each demonstration D consists of the tuple ⟨{I}, T∗⟩, where {I}N i=1 are N RGB camera views of the scene and T∗is a ...
- **p. 2 / 3. Language-Guided Manipulation - extractive body cue:** We present few-shot learning experiments on grasping and placing tasks, where our robot is able to handle open-set generalization to objects that differ significantly in ...
- **p. 7 / 4 Results - extractive body cue:** Although this success rate is far from practical for industrial use, our overall strategy of using 2D visual priors for 3D scene understanding can leverage ...
- **p. 6 / 4 Results - extractive body cue:** While the baselines using density, RGB color values, or intermediate features from NeRF achieve respectable performance, they struggle to identify the semantic category of the ...
- **p. 6 / 4 Results - extractive body cue:** We present the success rates in Table 1 and examples of robot executions in Figure 5.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 7 (4 Results), p. 6 (4 Results) |
| Embodiment/environment | For each task, we evaluate in ten scenes that contain novel objects in arbitrary poses and distractor objects. | hardware/simulator version and reset protocol | p. 6 (4 Results), p. 7 (4 Results) |
| Dataset/benchmark | We consider a run successful if the robot grasps or places the correct corresponding object part for the task. | role, split, size and leakage | p. 6 (4 Results), p. 7 (4 Results), p. 7 (4 Results), p. 6 (4 Results) |
| Metric | Although this success rate is far from practical for industrial use, our overall strategy of using 2D visual priors for 3D scene understanding can leverage the rapid advancements in VLMs, which hold ... | definition, denominator, direction and uncertainty | p. 7 (4 Results), p. 6 (4 Results), p. 7 (4 Results) |
| Baseline/ablation | We reset the scenes to about the same configuration for each compared method. | fair input/data/compute/action matching | p. 6 (4 Results), p. 6 (4 Results), p. 8 (4 Results) |

## Explicit Limitations and Failure Boundary

- **p. 6 / 4 Results - extractive body cue:** In comparison, 21/27 failures for CLIP ViT and ResNet combined may be attributed to this issue.
- **p. 6 / 4 Results - extractive body cue:** The DINO ViT has a good part-level understanding of object geometry with 7/19 failure cases caused by inaccuracies in the grasp rotations and occasionally, the ...
- **p. 7 / 4 Results - extractive body cue:** This is a typical failure case - six out of 19 failures stem from these poor grasp predictions with rotational or translational errors.
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3: Pipeline for Language-Guided Manipulation. (a) Encode the language query with CLIP, and compare its similarity to the average query point features over a ...
- **p. 7 / 4 Results - extractive body cue:** The robot failed to grasp the stainless steel jug by its handle due to a small error in the grasp rotation.

## Why Read It

Manipulation, contact, tactile, and dexterity의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 What form of scene representation would facilitate open-set generalization for robotic manipulation systems?를 문제로 두고, 3 Feature Fields for Robotic Manipulation (F3RM) We present Feature Fields for Robotic Manipulation (F3RM), our approach for distilling pre-trained representations from vision and vision-language models into 3D feature fields for open-e ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1 Introduction), p. 1 (1 Introduction), p. 4 (6 DOF Gripper Pose), p. 5 (6 DOF Gripper Pose), p. 5 (6 DOF Gripper Pose), p. 3 (3. Language-Guided Manipulation) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (20 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** Many robotic tasks, however, require a detailed understanding of 3D geometry, which is often lacking in 2D image features. (p. 1, Abstract).
- **Actual contribution:** The main contribution of this work is to study the use of DFFs instead for robotic manipulation. (p. 1, 1 Introduction).
- **Evaluation boundary:** We present the success rates in Table 1 and examples of robot executions in Figure 5. (p. 6, 4 Results).
- **Explicit failure boundary:** The remaining 13/19 failed grasps are due to CLIP features behaving like a bag-of-words and struggling to capture relationships, attributes, and ordinal information within sentences [22]. (p. 7, 4 Results).
