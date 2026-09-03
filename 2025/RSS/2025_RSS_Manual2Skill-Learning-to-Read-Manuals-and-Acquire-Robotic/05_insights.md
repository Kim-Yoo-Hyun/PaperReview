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
- **p. 1 / body section boundary not confidently recovered - extractive body cue:** We propose Manual2 ‘enabling robots to understand and execute complex manipulation tasks in mi the input of our pipeline: the pictures of the assembly manual ...
- **p. 3 / A. VLM Guided Hierarchical Assembly Graph Generation - extractive body cue:** Every VLM prompt consists of two components:
- **p. 14 / B. Pose Estimation Implementation - extractive body cue:** where tr(:) denotes the trace of a matrix and RT is the transpose of R. ‘Translation MSE Loss: Following [29], we use the mean
- **p. 15 / B. Pose Estimation Implementation - extractive body cue:** We then use this feature as input for the pose regressor MLP.
- **Contribution anchor:** p. 1 (Abstract), p. 2 (I. INrRopuction), p. 2 (I. INrRopuction), p. 1 (body section boundary not confidently recovered), p. 3 (A. VLM Guided Hierarchical Assembly Graph Generation), p. 14 (B. Pose Estimation Implementation)

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

- **Paper-specific interface:** This triplet format enhances interpretability and ensures consistency by structuring all outputs into the same data format, We use the Image Set and Text Instructions as the input prompt for ... (p. 4, 2. Per-step Assembly Pose Estimation).
- **Paper-specific mechanism:** In this paper, we present Manual2Skill, a novel framework that enables robots to perform complex assembly tasks guided by highleyel manual instructions. (p. 1, Abstract).
- **Evidence boundary:** the reported outcome is We present the results in Table IV, showing that our method outperforms the baseline and achieves a high success rate in real-world assembly tasks. (p. 9, C. Overall Performance Evaluation); the relevant task/metric cue is Our framework achieves a success rate of $8%, demonstrating the effectiveness of our proposed framework. (p. 8, C. Overall Performance Evaluation). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** Failures occur when the RRTConnect algorithm cannot find a feasible trajectory when the planned path results in collisions with the robotic arm or surrounding objects or due to suboptimal grasping ... (p. 9, C. Overall Performance Evaluation).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `VLA and generalist robot policies`; tags: `Robotics, VLM, assembly, task planning, 6D pose, long-horizon`.
- **Reading predecessor in the generated track queue:** PartInstruct: Part-level Instruction Following for Fine-grained Robot Manipulation (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Failures occur when the RRTConnect algorithm cannot find a feasible trajectory when the planned path results in collisions with the robotic arm or surrounding objects or due to suboptimal grasping poses.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: This triplet format enhances interpretability and ensures consistency by structuring all outputs into the same data format, We use the Image Set and Text Instructions as the input prompt for ... (p. 4, 2. Per-step Assembly Pose Estimation); preserve the objective/update rule: 1) Loss Functions for Pose Estimation: (p. 14, B. Pose Estimation Implementation).
2. Use the paper-reported task/data/environment cue: We present the results in Table IV, showing that our method outperforms the baseline and achieves a high success rate in real-world assembly tasks. (p. 9, C. Overall Performance Evaluation).
3. Compare against the reported or matched baseline: As the first to propose a comprehensive pipeline for furniture assembly, there is no direct baseline for comparison, So we design a baseline method that uses previous work [29] to ... (p. 8, C. Overall Performance Evaluation).
4. Report the body metric with its denominator and aggregation: Our framework achieves a success rate of $8%, demonstrating the effectiveness of our proposed framework. (p. 8, C. Overall Performance Evaluation).
5. Re-run the reported ablation or stress/failure condition: ‘TABLE III: Success Rate on 4 Furniture Categories(*) (p. 8, C. Overall Performance Evaluation); if none is reported, design one around: Failures occur when the RRTConnect algorithm cannot find a feasible trajectory when the planned path results in collisions with the robotic arm or surrounding objects or due to suboptimal grasping ... (p. 9, C. Overall Performance Evaluation).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 1 (Abstract), p. 2 (I. INrRopuction), match the reported outcome at p. 9 (C. Overall Performance Evaluation), p. 15 (B. Pose Estimation Implementation), p. 15 (B. Pose Estimation Implementation), and measure the boundary at p. 9 (C. Overall Performance Evaluation), p. 9 (C. Overall Performance Evaluation).

## Falsifiable research question

Under the paper's stated interface (This triplet format enhances interpretability and ensures consistency by structuring all outputs into the same data format, We use the Image Set ...), does the paper-specific mechanism (In this paper, we present Manual2Skill, a novel framework that enables robots to perform complex assembly tasks guided by highleyel manual instructions.) retain the reported evaluation outcome (Our framework achieves a success rate of $8%, demonstrating the effectiveness of our proposed framework.) when tested against the paper's strongest explicit boundary (Failures occur when the RRTConnect algorithm cannot find a feasible trajectory when the planned path results in collisions ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (Our framework achieves a success rate of $8%, demonstrating the effectiveness of our proposed framework.) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (26 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** In this paper, we present Manual2Skill, a novel framework that enables robots to perform complex assembly tasks guided by highleyel manual instructions. (p. 1, Abstract).
- **Paper-supported outcome:** We present the results in Table IV, showing that our method outperforms the baseline and achieves a high success rate in real-world assembly tasks. (p. 9, C. Overall Performance Evaluation).
- **Strongest explicit boundary:** Failures occur when the RRTConnect algorithm cannot find a feasible trajectory when the planned path results in collisions with the robotic arm or surrounding objects or due to suboptimal grasping ... (p. 9, C. Overall Performance Evaluation).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
