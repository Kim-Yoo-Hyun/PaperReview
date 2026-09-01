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

- **Closed-loop position:** `RGB-D/point cloud, object state와 contact/task observation → object geometry, affordance, contact mode 또는 end-effector state → grasp, pose, force 또는 end-effector trajectory`.
- 이 논문의 재사용 가능한 지점은 In our approach, each observation o, is composed. of the object's point cloud P..), the hand's point cloud Phands and the robot's joint states, including a 6-Dof arm and 16Dof hand configuration.를 ‘The BCRNNSD is trained for 3000 epochs with horizon=10, n_obs_steps=1, n_action_steps=l, where the observations are replaced from images to point clouds.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 object geometry, affordance, contact mode 또는 end-effector state가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Despite the exceptional performance demonstrated by CordViP, there are still certain limitations that could be explored in future work.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: To this end, we propose the interaction-aware generation of 3D point clouds, enabling the reconstruction of crucial spatial information,
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `Manipulation, contact, tactile, and dexterity`; tags: `Robotics, 3D perception, dexterous manipulation, correspondence, contact maps, bimanual`.
- **Reading predecessor in the generated track queue:** FACTR: Force-Attending Curriculum Training for Contact-Rich Policy Learning (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** FlowPolicy: Enabling Fast and Robust 3D Flow-Based Policy via Consistency Flow Matching for Robot Manipulation (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Despite the exceptional performance demonstrated by CordViP, there are still certain limitations that could be explored in future work.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: ‘We conduct comprehensive real-world experiments to answer the following questions:.
3. Compare against the body-reported baseline or a matched simpler baseline: The Diffusion Policy baseline utilizes ResNetI8 as the visual encoder and employs CNN-based backbones..
4. Report the body metric and its denominator/aggregation: Fig. 1: We propose CordViP, a correspondence-based visuomotor policy for dexterous manipulation in the real world. (a) Left: We present the interaction-aware point clouds, which demonstrate robustness to different viewpoints while estab ....
5. Re-run the body-reported ablation/failure condition: Network Architecture, For point cloud encoding, we first use PointNetl41] to process point cloud data without RGB information, outputting a set of point feature vectors at the dimension of 1024..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 5 (C. Comact and Coordination-Enhanced Feature Extraction), p. 5 (C. Comact and Coordination-Enhanced Feature Extraction), p. 14 (B. Implementation Details); the primary result is directionally consistent at p. 1 (Figure/Table caption), p. 5 (IV. EXPERIMENTS), p. 8 (Figure/Table caption); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 interaction-aware, generation, point mechanism이 The Diffusion Policy baseline utilizes ResNetI8 as the visual encoder and employs CNN-based backbones. 대비 Fig. 1: We propose CordViP, a correspondence-based visuomotor policy for dexterous manipulation in the real world. (a) Left: ...을 개선하고, Despite the exceptional performance demonstrated by CordViP, there are still certain limitations that could be explored ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
