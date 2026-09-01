# Insights — Manual2Skill: Learning to Read Manuals and Acquire Robotic Skills for Furniture Assembly Using Vision-Language Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (26 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p150.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p150.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / Abstract - extractive body cue:** In this paper, we present Manual2Skill, a novel framework that enables robots to perform complex assembly tasks guided by highleyel manual instructions.
- **p. 2 / I. INrRopuction - extractive body cue:** In this paper, we propose Manual2Skill, a novel robot learn
- **p. 2 / I. INrRopuction - extractive body cue:** + We propose Manual2Skill, a novel framework that leverages VLM to learn robotic skills from manuals, enabling 4 generalizable assembly pipeline for IKEA furniture
- **p. 1 / Front matter - extractive body cue:** We propose Manual2 ‘enabling robots to understand and execute complex manipulation tasks in mi the input of our pipeline: the pictures of the assembly manual ...
- **p. 3 / A. VLM Guided Hierarchical Assembly Graph Generation - extractive body cue:** Every VLM prompt consists of two components:
- **p. 14 / B. Pose Estimation Implementation - extractive body cue:** where tr(:) denotes the trace of a matrix and RT is the transpose of R. ‘Translation MSE Loss: Following [29], we use the mean
- **p. 15 / B. Pose Estimation Implementation - extractive body cue:** We then use this feature as input for the pose regressor MLP.
- **Contribution anchor:** p. 1 (Abstract), p. 2 (I. INrRopuction), p. 2 (I. INrRopuction), p. 1 (Front matter), p. 3 (A. VLM Guided Hierarchical Assembly Graph Generation), p. 14 (B. Pose Estimation Implementation)

### Strongest assumption and failure boundary

- **p. 1 / Abstract - extractive body cue:** For robots, however, this capability remains a substantial challenge, as they cannot interpret abstract instructions and translate them into executable actions.
- **p. 2 / A. Furniture Assembly - extractive body cue:** However, existing works typically focus on specific subproblems rather than addressing the entire assembly pipeline.
- **p. 3 / B. VLM Guided Robot Learning - extractive body cue:** However, they are mostly limited to tabletop manipulation tasks and do not generalize well to more complex, long-horizon assembly problems.
- **p. 1 / I. INrRopuction - extractive body cue:** Replicating the human ability to transfer abstract manuals to real-world actions re- ‘mains a significant challenge for robots.
- **p. 2 / A. Furniture Assembly - extractive body cue:** Part assembly is a long-standing challenge with extensive research exploring how to construct a complete shape from individual components or parts (6, 13, 20, 27, ...
- **p. 9 / C. Overall Performance Evaluation - extractive body cue:** Failures occur when the RRTConnect algorithm cannot find a feasible trajectory when the planned path results in collisions with the robotic arm or surrounding objects ...
- **p. 9 / C. Overall Performance Evaluation - extractive body cue:** failure mode arises from planning limitations, particularly in handling complex obstacles.
- **Boundary to test:** Failures occur when the RRTConnect algorithm cannot find a feasible trajectory when the planned path results in collisions with the robotic arm or surrounding objects or due to suboptimal grasping poses.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | In this paper, we present Manual2Skill, a novel framework that enables robots to perform complex assembly tasks guided by highleyel manual instructions. | p. 1 (Abstract), p. 2 (I. INrRopuction) |
| Reported outcome | We present the results in Table IV, showing that our method outperforms the baseline and achieves a high success rate in real-world assembly tasks. | p. 9 (C. Overall Performance Evaluation), p. 8 (C. Overall Performance Evaluation) |
| Failure/limitation | Failures occur when the RRTConnect algorithm cannot find a feasible trajectory when the planned path results in collisions with the robotic arm or surrounding objects or due to suboptimal grasping poses. | p. 9 (C. Overall Performance Evaluation), p. 9 (C. Overall Performance Evaluation) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `image/video, language instruction, proprioception과 history → language-grounded task state와 action-policy context → continuous action, pose 또는 action chunk`.
- 이 논문의 재사용 가능한 지점은 This triplet format enhances interpretability and ensures consistency by structuring all outputs into the same data format, We use the Image Set and Text Instructions as the input prompt for the VLM ...를 During each step of the assembly proces the mesh-along with the RGB and depth images and an object mask-is input into the FoundationPose model, which then generates the precise 6D pose and ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 language-grounded task state와 action-policy context가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Failures occur when the RRTConnect algorithm cannot find a feasible trajectory when the planned path results in collisions with the robotic arm or surrounding objects or due to suboptimal grasping poses.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: In this paper, we present Manual2Skill, a novel framework that enables robots to perform complex assembly tasks guided by highleyel manual instructions.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `VLA and generalist robot policies`; tags: `Robotics, VLM, assembly, task planning, 6D pose, long-horizon`.
- **Reading predecessor in the generated track queue:** PartInstruct: Part-level Instruction Following for Fine-grained Robot Manipulation (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Failures occur when the RRTConnect algorithm cannot find a feasible trajectory when the planned path results in collisions with the robotic arm or surrounding objects or due to suboptimal grasping poses.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Failures occur when the RRTConnect algorithm cannot find a feasible trajectory when the planned path results in collisions with the robotic arm or surrounding objects or due to suboptimal grasping poses..
3. Compare against the body-reported baseline or a matched simpler baseline: We present the results in Table IV, showing that our method outperforms the baseline and achieves a high success rate in real-world assembly tasks..
4. Report the body metric and its denominator/aggregation: As shown in Table X (Ours (w/o Segmentation)), this method significantly impair VLM performance in generating assembly graphs, leading to more than double accuracy drops in success rate..
5. Re-run the body-reported ablation/failure condition: To evaluate the effectiveness of each component in our pipeline, we conduct an ablation study on the chair category..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 14 (B. Pose Estimation Implementation), p. 15 (B. Pose Estimation Implementation), p. 17 (B. Pose Estimation Implementation); the primary result is directionally consistent at p. 9 (C. Overall Performance Evaluation), p. 8 (C. Overall Performance Evaluation), p. 16 (B. Pose Estimation Implementation); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 present, Manual2Skill, novel mechanism이 We present the results in Table IV, showing that our method outperforms the baseline and achieves ... 대비 As shown in Table X (Ours (w/o Segmentation)), this method significantly impair VLM performance in generating assembly graphs, ...을 개선하고, Failures occur when the RRTConnect algorithm cannot find a feasible trajectory when the planned path results ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
