# Insights — Contact-GraspNet: Efficient 6-DoF Grasp Generation in Cluttered Scenes

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (7 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2103.14127; PDF retrieval source: https://arxiv.org/pdf/2103.14127. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / I. INTRODUCTION - extractive body cue:** Our method is closely related to the work of Murali et al.
- **p. 2 / I. INTRODUCTION - extractive body cue:** To address these issues, our method instead directly processes a full scene point cloud or a local region around a target object.
- **p. 3 / III. METHOD - extractive body cue:** We used the ACRONYM dataset [32], which consists of 8872 meshes from the Shapenet dataset [35] and 17.7 million
- **p. 4 / III. METHOD - extractive body cue:** Instead of supervising all network heads in isolation, we propose to combine the predictions to the 6-DoF grasp pose ˆg ∈G given in Eq.
- **p. 2 / I. INTRODUCTION - extractive body cue:** Thus, our main contributions are the following: • A new end-to-end method for 6-DoF grasping of unknown objects in cluttered real world scenes where we ...
- **p. 4 / III. METHOD - extractive body cue:** The network has four heads with two 1DConv layers each and per-point outputs s ∈R, z1 ∈R3, z2 ∈ R3, o ∈R10, from which we ...
- **p. 3 / III. METHOD - extractive body cue:** In pink we show the five gripper points v that we used in the ladd-s loss. been shown to be difficult in grasping [11] and ...
- **Contribution anchor:** p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (III. METHOD), p. 4 (III. METHOD), p. 2 (I. INTRODUCTION), p. 4 (III. METHOD)

### Strongest assumption and failure boundary

- **p. 1 / I. INTRODUCTION - extractive body cue:** To address the limitations of planar grasping, there has been a recent interest in tackling the problem of 6-DoF grasping of unknown objects [10, 11, ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Grasping objects from cluttered scenes with structure introduces extra challenges.
- **p. 2 / I. INTRODUCTION - extractive body cue:** Our representation has only 4-DoF which facilitates the learning problem significantly. • Comprehensive ablation studies in a physics simulator to evaluate the effects of different ...
- **p. 6 / V. CONCLUSIONS - extractive body cue:** Gripper collisions are effectively avoided by considering them during training and by predicting grasps directly in scenes.
- **p. 6 / IV. EXPERIMENTAL EVALUATION - extractive body cue:** Failure Cases: We observe some failure cases for thick objects that only allow grasps almost at maximum grasp width.
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1. Contact-GraspNet efficiently predicts diverse and stable grasps in cluttered scenes while avoiding collisions. space of possible grasps to planar grasping, where grasps are ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2. Training Data Pipeline. We place object meshes with dense grasp annotations from the ACRONYM dataset [32] at random stable poses in scenes. Grasp ...
- **Boundary to test:** Gripper collisions are effectively avoided by considering them during training and by predicting grasps directly in scenes.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Our method is closely related to the work of Murali et al. | p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| Reported outcome | We observe a significantly higher grasp success rate of our method compared to [11] and [12] which themselves outperform other learning-based methods and analytic/heuristic baselines. | p. 6 (IV. EXPERIMENTAL EVALUATION), p. 6 (IV. EXPERIMENTAL EVALUATION) |
| Failure/limitation | Gripper collisions are effectively avoided by considering them during training and by predicting grasps directly in scenes. | p. 6 (V. CONCLUSIONS), p. 6 (IV. EXPERIMENTAL EVALUATION) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Paper-specific interface:** Their predictions can be directly associated to 3D points in the input point cloud and our proposed grasp representation exploits this ability. (p. 3, III. METHOD).
- **Paper-specific mechanism:** Thus, our main contributions are the following: • A new end-to-end method for 6-DoF grasping of unknown objects in cluttered real world scenes where we achieve 90% grasp success rate. (p. 2, I. INTRODUCTION).
- **Evidence boundary:** the reported outcome is We observe a significantly higher grasp success rate of our method compared to [11] and [12] which themselves outperform other learning-based methods and analytic/heuristic baselines. (p. 6, IV. EXPERIMENTAL EVALUATION); the relevant task/metric cue is The average distance loss ladd-s improves the success rate of high confidence contacts which is important because most grasps that we execute lie in the first decimal of coverage. (p. 6, IV. EXPERIMENTAL EVALUATION). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** Failure Cases: We observe some failure cases for thick objects that only allow grasps almost at maximum grasp width. (p. 6, IV. EXPERIMENTAL EVALUATION).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `CORE` in `Manipulation, contact, tactile, and dexterity`; tags: `Robotics, grasping, contact prediction, 6-DoF grasp`.
- **Reading predecessor in the generated track queue:** GraspNet-1Billion: A Large-Scale Benchmark for General Object Grasping (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Factory: Fast Contact for Robotic Assembly (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Gripper collisions are effectively avoided by considering them during training and by predicting grasps directly in scenes.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: Their predictions can be directly associated to 3D points in the input point cloud and our proposed grasp representation exploits this ability. (p. 3, III. METHOD); preserve the objective/update rule: On the grasp width bin predictions, we optimize a weighted, multi-label binary cross entropy loss lwidth. (p. 4, III. METHOD).
2. Use the paper-reported task/data/environment cue: We evaluate our method in a grasping study with a Franka robot where we pick unknown objects in cluttered scenes. (p. 5, IV. EXPERIMENTAL EVALUATION).
3. Compare against the reported or matched baseline: We observe a significantly higher grasp success rate of our method compared to [11] and [12] which themselves outperform other learning-based methods and analytic/heuristic baselines. (p. 6, IV. EXPERIMENTAL EVALUATION).
4. Report the body metric with its denominator and aggregation: The average distance loss ladd-s improves the success rate of high confidence contacts which is important because most grasps that we execute lie in the first decimal of coverage. (p. 6, IV. EXPERIMENTAL EVALUATION).
5. Re-run the reported ablation or stress/failure condition: Ablations Optimization Targets: In Fig. (p. 6, IV. EXPERIMENTAL EVALUATION); if none is reported, design one around: Failure Cases: We observe some failure cases for thick objects that only allow grasps almost at maximum grasp width. (p. 6, IV. EXPERIMENTAL EVALUATION).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), match the reported outcome at p. 6 (IV. EXPERIMENTAL EVALUATION), p. 6 (IV. EXPERIMENTAL EVALUATION), p. 5 (IV. EXPERIMENTAL EVALUATION), and measure the boundary at p. 6 (IV. EXPERIMENTAL EVALUATION), p. 1 (Abstract).

## Falsifiable research question

Under the paper's stated interface (Their predictions can be directly associated to 3D points in the input point cloud and our proposed grasp representation exploits this ability.), does the paper-specific mechanism (Thus, our main contributions are the following: • A new end-to-end method for 6-DoF grasping of unknown objects in cluttered real world ...) retain the reported evaluation outcome (The average distance loss ladd-s improves the success rate of high confidence contacts which is important because most ...) when tested against the paper's strongest explicit boundary (Failure Cases: We observe some failure cases for thick objects that only allow grasps almost at maximum grasp ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (The average distance loss ladd-s improves the success rate of high confidence contacts which is important because most ...) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (7 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** Thus, our main contributions are the following: • A new end-to-end method for 6-DoF grasping of unknown objects in cluttered real world scenes where we achieve 90% grasp success rate. (p. 2, I. INTRODUCTION).
- **Paper-supported outcome:** We observe a significantly higher grasp success rate of our method compared to [11] and [12] which themselves outperform other learning-based methods and analytic/heuristic baselines. (p. 6, IV. EXPERIMENTAL EVALUATION).
- **Strongest explicit boundary:** Failure Cases: We observe some failure cases for thick objects that only allow grasps almost at maximum grasp width. (p. 6, IV. EXPERIMENTAL EVALUATION).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
