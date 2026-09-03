# Insights — CordViP: Correspondence-based Visuomotor Policy for Dexterous Manipulation in Real-World

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (17 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p110.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p110.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 3 / B. Interaction-aware Generation of 3D Point Clouds - extractive body cue:** To this end, we propose the interaction-aware generation of 3D point clouds, enabling the reconstruction of crucial spatial information,
- **p. 14 / B. Implementation Details - extractive body cue:** The PointNet consists of three fully connected layers, each followed by LayerNorm for normalization and ReLU activation
- **p. 15 / B. Implementation Details - extractive body cue:** For our method, we use only RGB and depth data to track the ‘object's pose.
- **p. 5 / C. Comact and Coordination-Enhanced Feature Extraction - extractive body cue:** This pre-training approach enables the encoder to learn the interactions and relationships within the environment.
- **p. 15 / B. Implementation Details - extractive body cue:** We collect both the robot's state and actions using joint angles in radians, including the 6-DOF joints of the robotic the 16-DOF joints of the ...
- **p. 5 / C. Comact and Coordination-Enhanced Feature Extraction - extractive body cue:** Similarly, we also predict the action sequence of the hand using point clouds and the arm state, We use MSE loss to compute the loss ...
- **p. 5 / C. Comact and Coordination-Enhanced Feature Extraction - extractive body cue:** To help the robot system learn the features of hand-arm coordination, we also propose & correspondence-based design for action prediction. ‘The arm and hand states ...
- **Contribution anchor:** p. 3 (B. Interaction-aware Generation of 3D Point Clouds), p. 14 (B. Implementation Details), p. 15 (B. Implementation Details), p. 5 (C. Comact and Coordination-Enhanced Feature Extraction), p. 15 (B. Implementation Details), p. 5 (C. Comact and Coordination-Enhanced Feature Extraction)

### Strongest assumption and failure boundary

- **p. 3 / A. Problem Formulation - extractive body cue:** As a result, CordViP not only effectively addresses occlusion challenges during dexterous manipulation but also significantly improves the model's ability to comprehend spatial interactions and ...
- **p. 3 / A. Problem Formulation - extractive body cue:** robot's observations and A represents the corresponding actions, allowing the robot to generalize beyond the taining data distribution.
- **p. 10 / V. CONCLUSIONS AND LimiTATIONS - extractive body cue:** Despite the exceptional performance demonstrated by CordViP, there are still certain limitations that could be explored in future work.
- **p. 10 / Figure/Table caption - extractive body cue:** Fig. 8: Failure case. (a) Case / is a failure case from the
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: We propose CordViP, a correspondence-based visuomotor policy for dexterous manipulation in the real world. (a) Left: We present the interaction-aware point clouds, which ...
- **p. 15 / B. Implementation Details - extractive body cue:** We utilize FoundationPose (60] to perform robust 6D pose estimation for various objects across tasks.
- **Boundary to test:** Despite the exceptional performance demonstrated by CordViP, there are still certain limitations that could be explored in future work.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | To this end, we propose the interaction-aware generation of 3D point clouds, enabling the reconstruction of crucial spatial information, | p. 3 (B. Interaction-aware Generation of 3D Point Clouds), p. 14 (B. Implementation Details) |
| Reported outcome | Fig. 1: We propose CordViP, a correspondence-based visuomotor policy for dexterous manipulation in the real world. (a) Left: We present the interaction-aware point clouds, which demonstrate robustness to different viewpoints while estab ... | p. 1 (Figure/Table caption), p. 5 (IV. EXPERIMENTS) |
| Failure/limitation | Despite the exceptional performance demonstrated by CordViP, there are still certain limitations that could be explored in future work. | p. 10 (V. CONCLUSIONS AND LimiTATIONS), p. 10 (Figure/Table caption) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Paper-specific interface:** In our approach, each observation o, is composed. of the object's point cloud P..), the hand's point cloud Phands and the robot's joint states, including a 6-Dof arm and 16Dof ... (p. 3, A. Problem Formulation).
- **Paper-specific mechanism:** To eliminate these limitations, we propose CordViP, a novel framework that ‘constructs and learns correspondences by leveraging the robust 6D pose estimation of objects and robot proprioception. (p. 1, Abstract).
- **Evidence boundary:** the reported outcome is The visual results are shown in the figure 10. (p. 15, B. Implementation Details); the relevant task/metric cue is ‘+ What role does each of the system components play enhancing its overall performance (Section IV-E, IV-F)? (p. 5, IV. EXPERIMENTS). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** As shown in ‘Table VI, the image-based diffusion policy is highly sensitive to ‘camera viewpoints and completely fails across all three camera views. (p. 9, C. Efficiency).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `Manipulation, contact, tactile, and dexterity`; tags: `Robotics, 3D perception, dexterous manipulation, correspondence, contact maps, bimanual`.
- **Reading predecessor in the generated track queue:** FACTR: Force-Attending Curriculum Training for Contact-Rich Policy Learning (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** FlowPolicy: Enabling Fast and Robust 3D Flow-Based Policy via Consistency Flow Matching for Robot Manipulation (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Despite the exceptional performance demonstrated by CordViP, there are still certain limitations that could be explored in future work.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: In our approach, each observation o, is composed. of the object's point cloud P..), the hand's point cloud Phands and the robot's joint states, including a 6-Dof arm and 16Dof ... (p. 3, A. Problem Formulation); preserve the objective/update rule: On the one hand, real-world point cloud data, typically captured using stereo cameras or low-cost RGB-D scanners, suffers from geometric and semantic loss due to factors such as light reflection, ... (p. 3, B. Interaction-aware Generation of 3D Point Clouds).
2. Use the paper-reported task/data/environment cue: ‘We conduct comprehensive real-world experiments to answer the following questions: (p. 5, IV. EXPERIMENTS).
3. Compare against the reported or matched baseline: ‘+ What role does each of the system components play enhancing its overall performance (Section IV-E, IV-F)? (p. 5, IV. EXPERIMENTS).
4. Report the body metric with its denominator and aggregation: ‘+ What role does each of the system components play enhancing its overall performance (Section IV-E, IV-F)? (p. 5, IV. EXPERIMENTS).
5. Re-run the reported ablation or stress/failure condition: ‘+ What role does each of the system components play enhancing its overall performance (Section IV-E, IV-F)? (p. 5, IV. EXPERIMENTS); if none is reported, design one around: As shown in ‘Table VI, the image-based diffusion policy is highly sensitive to ‘camera viewpoints and completely fails across all three camera views. (p. 9, C. Efficiency).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 1 (Abstract), p. 3 (A. Problem Formulation), match the reported outcome at p. 15 (B. Implementation Details), p. 5 (IV. EXPERIMENTS), p. 15 (B. Implementation Details), and measure the boundary at p. 9 (C. Efficiency), p. 10 (V. CONCLUSIONS AND LimiTATIONS).

## Falsifiable research question

Under the paper's stated interface (In our approach, each observation o, is composed. of the object's point cloud P..), the hand's point cloud Phands and the robot's ...), does the paper-specific mechanism (To eliminate these limitations, we propose CordViP, a novel framework that ‘constructs and learns correspondences by leveraging the robust 6D pose estimation ...) retain the reported evaluation outcome (‘+ What role does each of the system components play enhancing its overall performance (Section IV-E, IV-F)?) when tested against the paper's strongest explicit boundary (As shown in ‘Table VI, the image-based diffusion policy is highly sensitive to ‘camera viewpoints and completely fails ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (‘+ What role does each of the system components play enhancing its overall performance (Section IV-E, IV-F)?) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (17 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** To eliminate these limitations, we propose CordViP, a novel framework that ‘constructs and learns correspondences by leveraging the robust 6D pose estimation of objects and robot proprioception. (p. 1, Abstract).
- **Paper-supported outcome:** The visual results are shown in the figure 10. (p. 15, B. Implementation Details).
- **Strongest explicit boundary:** As shown in ‘Table VI, the image-based diffusion policy is highly sensitive to ‘camera viewpoints and completely fails across all three camera views. (p. 9, C. Efficiency).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
