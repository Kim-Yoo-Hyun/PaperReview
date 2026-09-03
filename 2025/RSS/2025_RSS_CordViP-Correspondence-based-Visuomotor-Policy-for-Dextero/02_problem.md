# Problem - CordViP: Correspondence-based Visuomotor Policy for Dexterous Manipulation in Real-World

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p110.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p110.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 3 (A. Problem Formulation), p. 3 (A. Problem Formulation)): As a result, CordViP not only effectively addresses occlusion challenges during dexterous manipulation but also significantly improves the model's ability to comprehend spatial interactions and collaborative dynamics.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Achieving humanclevel dexterity in robots is a key ‘objective in the field of robotic manipulation, Recent advance ments in 3D-based imitation learning have shown promising ...
- **p. 1 / Abstract - extractive body cue:** However, obtaining high-quality 3D representations presents two key problems: (1) the quality of point clouds captured by a single-view camera is significantly affected by factors ...
- **p. 1 / Abstract - extractive body cue:** To eliminate these limitations, we propose CordViP, a novel framework that ‘constructs and learns correspondences by leveraging the robust 6D pose estimation of objects and ...
- **p. 1 / Abstract - extractive body cue:** Specifically, We first introduce the interaction-aware point clouds, which ‘establish correspondences between the object and the hand. ‘These point clouds are then used for our ...
- **p. 1 / Abstract - extractive body cue:** where we also incorporate object-centric contact maps and hand arm coordination information, effectively capturing both spatial
- **p. 3 / A. Problem Formulation - extractive body cue:** As a result, CordViP not only effectively addresses occlusion challenges during dexterous manipulation but also significantly improves the model's ability to comprehend spatial interactions and ...
- **p. 3 / A. Problem Formulation - extractive body cue:** robot's observations and A represents the corresponding actions, allowing the robot to generalize beyond the taining data distribution.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | As a result, CordViP not only effectively addresses occlusion challenges during dexterous manipulation but also significantly improves the model's ability to comprehend ... | rigid/articulated object와 robot manipulator contact scene | body wording is the source claim |
| Observation / input | In our approach, each observation o, is composed. of the object's point cloud P..), the hand's point cloud Phands and the robot's ... | RGB-D/point cloud, object state와 contact/task observation | exact sensor/frame/preprocessing from PDF body |
| State / latent | observation, composed, object, point, cloud, hand, Phands, robot, joint, states | object geometry, affordance, contact mode 또는 end-effector state | notation and tensor shape require body check |
| Output / action | Interaction-aware, Generation, Point, Clouds, provides, accurate, complete, cloud | grasp, pose, force 또는 end-effector trajectory | exact unit/frame/decoder require body check |
| Target outcome | completion, contact success and robustness | task completion, contact success, pose/force error와 generalization | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | object geometry/contact state; body terms: observation, composed, object, point, cloud, hand, Phands, robot, joint, states | p. 3 (A. Problem Formulation), p. 15 (B. Implementation Details), p. 4 (C. Comact and Coordination-Enhanced Feature Extraction) |
| Decision / output variable | grasp/pose/force/trajectory; body terms: interaction-aware, generation, point, clouds, enabling, reconstruction, crucial, spatial | p. 3 (B. Interaction-aware Generation of 3D Point Clouds), p. 14 (B. Implementation Details), p. 15 (B. Implementation Details) |
| Objective / loss / cost | task/contact/pose objective; cue terms: hand, real-world, point, cloud, data, typically, captured, stereo | p. 5 (C. Comact and Coordination-Enhanced Feature Extraction), p. 3 (B. Interaction-aware Generation of 3D Point Clouds), p. 3 (B. Interaction-aware Generation of 3D Point Clouds), p. 5 (C. Comact and Coordination-Enhanced Feature Extraction), p. 15 (B. Implementation Details) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (B. Interaction-aware Generation of 3D Point Clouds), p. 5 (C. Comact and Coordination-Enhanced Feature Extraction), p. 15 (B. Implementation Details) |
| Success / guarantee | completion, contact success and robustness | p. 1 (Figure/Table caption), p. 5 (IV. EXPERIMENTS), p. 15 (B. Implementation Details) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 3 / A. Problem Formulation - extractive body cue:** robot's observations and A represents the corresponding actions, allowing the robot to generalize beyond the taining data distribution.

## What the Paper Changes

PDF body contribution framing (p. 3 (B. Interaction-aware Generation of 3D Point Clouds), p. 14 (B. Implementation Details), p. 15 (B. Implementation Details), p. 5 (C. Comact and Coordination-Enhanced Feature Extraction), p. 15 (B. Implementation Details)): To this end, we propose the interaction-aware generation of 3D point clouds, enabling the reconstruction of crucial spatial information,

- **p. 14 / B. Implementation Details - extractive body cue:** The PointNet consists of three fully connected layers, each followed by LayerNorm for normalization and ReLU activation
- **p. 15 / B. Implementation Details - extractive body cue:** For our method, we use only RGB and depth data to track the ‘object's pose.
- **p. 5 / C. Comact and Coordination-Enhanced Feature Extraction - extractive body cue:** This pre-training approach enables the encoder to learn the interactions and relationships within the environment.
- **p. 15 / B. Implementation Details - extractive body cue:** We collect both the robot's state and actions using joint angles in radians, including the 6-DOF joints of the robotic the 16-DOF joints of the ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 10 | Despite the exceptional performance demonstrated by CordViP, there are still certain limitations that could be explored in future ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 10 | Fig. 8: Failure case. (a) Case / is a failure case from the | reported limitation/failure wording; scope must be verified |
| body cue at p. 1 | Fig. 1: We propose CordViP, a correspondence-based visuomotor policy for dexterous manipulation in the real world. (a) Left: ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 15 | We utilize FoundationPose (60] to perform robust 6D pose estimation for various objects across tasks. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

manipulation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 3 (A. Problem Formulation), p. 15 (B. Implementation Details), p. 4 (C. Comact and Coordination-Enhanced Feature Extraction), p. 5 (C. Comact and Coordination-Enhanced Feature Extraction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 3 (A. Problem Formulation), p. 3 (A. Problem Formulation), interface p. 3 (A. Problem Formulation), p. 15 (B. Implementation Details), p. 4 (C. Comact and Coordination-Enhanced Feature Extraction), p. 5 (C. Comact and Coordination-Enhanced Feature Extraction), objective p. 5 (C. Comact and Coordination-Enhanced Feature Extraction), p. 3 (B. Interaction-aware Generation of 3D Point Clouds), p. 3 (B. Interaction-aware Generation of 3D Point Clouds), p. 5 (C. Comact and Coordination-Enhanced Feature Extraction), p. 15 (B. Implementation Details).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (17 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** However, obtaining high-quality 3D representations presents two key problems: (1) the quality of point clouds captured by a single-view camera is significantly affected by factors such as ‘camera resolution. positioning, ... (p. 1, Abstract).
- **Formulation-changing contribution:** To eliminate these limitations, we propose CordViP, a novel framework that ‘constructs and learns correspondences by leveraging the robust 6D pose estimation of objects and robot proprioception. (p. 1, Abstract).
- **Assumption/failure evidence:** As shown in ‘Table VI, the image-based diffusion policy is highly sensitive to ‘camera viewpoints and completely fails across all three camera views. (p. 9, C. Efficiency).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
