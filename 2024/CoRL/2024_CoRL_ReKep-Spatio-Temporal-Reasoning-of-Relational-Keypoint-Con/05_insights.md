# Insights — ReKep: Spatio-Temporal Reasoning of Relational Keypoint Constraints for Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (30 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v270/huang25g.html; PDF retrieval source: https://raw.githubusercontent.com/mlresearch/v270/main/assets/huang25g/huang25g.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1 Introduction - extractive body cue:** Our contributions are summarized as follows: 1) We formulate manipulation tasks as a hierarchical optimization problem with Relational Keypoint Constraints; 2) We devise a pipeline ...
- **p. 2 / 1 Introduction - extractive body cue:** In this work, we propose Relational Keypoint Constraints (ReKep).
- **p. 4 / 3 Method - extractive body cue:** 2, which consists of three stages: grasp, align, and pour.
- **p. 1 / 1 Introduction - extractive body cue:** 1: the robot must grasp at the handle, keep the cup upright while transporting *Denotes.
- **p. 6 / 3 Method - extractive body cue:** This enables VLM to reason about 3D rotations with arithmetic operations in 3D Cartesian space, effectively circumventing the need for dealing with alternative 3D rotation ...
- **p. 5 / 3 Method - extractive body cue:** 3.4 Keypoint Proposal and ReKep Generation To enable the system to perform tasks in-the-wild given a free-form task instruction, we devise a pipeline using large ...
- **p. 24 / A.8 Implementation Details of Sub-Goal Solver - extractive body cue:** We use sampling-based global optimization Dual Annealing [129] in the first iteration to quickly search the full space, which is followed by a gradient-based local ...
- **Contribution anchor:** p. 2 (1 Introduction), p. 2 (1 Introduction), p. 4 (3 Method), p. 1 (1 Introduction), p. 6 (3 Method), p. 5 (3 Method)

### Strongest assumption and failure boundary

- **p. 3 / 1 Introduction - extractive body cue:** However, manual annotation is required per task, thus lacking scalability in open-world settings, which we aim to address in this work.
- **p. 2 / 1 Introduction - extractive body cue:** However, effectively formulating these constraints for a large variety of real-world tasks presents significant challenges.
- **p. 2 / 1 Introduction - extractive body cue:** While representing constraints using relative poses between robots and objects is a direct and widely-used approach [1], rigid-body transformations do not depict geometric details, require ...
- **p. 3 / 1 Introduction - extractive body cue:** Self-supervised vision models (e.g., DINO [5, 118]), on the other hand, provide fine-grained pixellevel features useful for various vision and robotic tasks [31, 119-124], but ...
- **p. 8 / 4 Experiments - extractive body cue:** The optimization module, on the other hand, does not contribute as much to the failures despite given limited time budget, since there often exist many ...
- **p. 19 / Figure/Table caption - extractive body cue:** Figure 7: Stationary Dual-Arm Platform. A.2 Wheeled Single-Arm Platform One of our investigated platform is a Franka arm mounted on a wheeled base built with ...
- **p. 27 / A.11 Extended Discusssions on Limitations - extractive body cue:** Herein we present additional limitations of the existing system.
- **Boundary to test:** The optimization module, on the other hand, does not contribute as much to the failures despite given limited time budget, since there often exist many possible solutions for each problem.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Our contributions are summarized as follows: 1) We formulate manipulation tasks as a hierarchical optimization problem with Relational Keypoint Constraints; 2) We devise a pipeline to automatically specify keypoints and constraints usin ... | p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Reported outcome | Folding 0/10 4/10 7/10 Total (%) 10.0% 44.3% 68.6% Table 1: Success rate on wheeled singlearm and stationary bimanual platforms. | p. 7 (4 Experiments), p. 7 (4 Experiments) |
| Failure/limitation | The optimization module, on the other hand, does not contribute as much to the failures despite given limited time budget, since there often exist many possible solutions for each problem. | p. 8 (4 Experiments), p. 19 (Figure/Table caption) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Paper-specific interface:** 3.4 Keypoint Proposal and ReKep Generation To enable the system to perform tasks in-the-wild given a free-form task instruction, we devise a pipeline using large vision models and vision-language models ... (p. 5, 3 Method).
- **Paper-specific mechanism:** Our contributions are summarized as follows: 1) We formulate manipulation tasks as a hierarchical optimization problem with Relational Keypoint Constraints; 2) We devise a pipeline to automatically specify keypoints and ... (p. 2, 1 Introduction).
- **Evidence boundary:** the reported outcome is Folding 0/10 3/10 5/10 Total (%) 6.7% 26.7% 46.7% Table 2: Success rate under external disturbances across both robot platforms. (p. 7, 4 Experiments); the relevant task/metric cue is Folding 0/10 4/10 7/10 Total (%) 10.0% 44.3% 68.6% Table 1: Success rate on wheeled singlearm and stationary bimanual platforms. (p. 7, 4 Experiments). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** The optimization module, on the other hand, does not contribute as much to the failures despite given limited time budget, since there often exist many possible solutions for each problem. (p. 8, 4 Experiments).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `VLA and generalist robot policies`; tags: `Planning, 3D geometry, Robotics, VLM`.
- **Reading predecessor in the generated track queue:** Grounding Actions in Camera Space: Observation-Centric Vision-Language-Action Policy (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** VoxAct-B: Voxel-Based Acting and Stabilizing Policy for Bimanual Manipulation (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** The optimization module, on the other hand, does not contribute as much to the failures despite given limited time budget, since there often exist many possible solutions for each problem.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: 3.4 Keypoint Proposal and ReKep Generation To enable the system to perform tasks in-the-wild given a free-form task instruction, we devise a pipeline using large vision models and vision-language models ... (p. 5, 3 Method); preserve the objective/update rule: Namely, for each stage i, the optimization shall find an end-effector pose as next sub-goal, along with its timing, and a sequence of poses egi-1:gi that achieves the sub-goal, subject ... (p. 4, 3 Method).
2. Use the paper-reported task/data/environment cue: Results are shown on two robot platforms and on a variety of tasks featuring multi-stage, in-the-wild, bimanual, and reactive behaviors, all without task-specific data, additional training, or environment models. (p. 8, 4 Experiments).
3. Compare against the reported or matched baseline: Compared to baselines, ReKep can effectively handle core challenges of each task. (p. 7, 4 Experiments).
4. Report the body metric with its denominator and aggregation: Folding 0/10 4/10 7/10 Total (%) 10.0% 44.3% 68.6% Table 1: Success rate on wheeled singlearm and stationary bimanual platforms. (p. 7, 4 Experiments).
5. Re-run the reported ablation or stress/failure condition: We evaluate two variants of the system: "Auto" uses foundation models to automatically generate ReKep, and "Annotated (Annot.)" uses human-annotated ReKep. (p. 7, 4 Experiments); if none is reported, design one around: The optimization module, on the other hand, does not contribute as much to the failures despite given limited time budget, since there often exist many possible solutions for each problem. (p. 8, 4 Experiments).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 2 (1 Introduction), p. 2 (1 Introduction), match the reported outcome at p. 7 (4 Experiments), p. 8 (4 Experiments), p. 7 (4 Experiments), and measure the boundary at p. 8 (4 Experiments), p. 7 (4 Experiments).

## Falsifiable research question

Under the paper's stated interface (3.4 Keypoint Proposal and ReKep Generation To enable the system to perform tasks in-the-wild given a free-form task instruction, we devise a ...), does the paper-specific mechanism (Our contributions are summarized as follows: 1) We formulate manipulation tasks as a hierarchical optimization problem with Relational Keypoint Constraints; 2) We ...) retain the reported evaluation outcome (Folding 0/10 4/10 7/10 Total (%) 10.0% 44.3% 68.6% Table 1: Success rate on wheeled singlearm and stationary ...) when tested against the paper's strongest explicit boundary (The optimization module, on the other hand, does not contribute as much to the failures despite given limited ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (Folding 0/10 4/10 7/10 Total (%) 10.0% 44.3% 68.6% Table 1: Success rate on wheeled singlearm and stationary ...) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (30 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** Our contributions are summarized as follows: 1) We formulate manipulation tasks as a hierarchical optimization problem with Relational Keypoint Constraints; 2) We devise a pipeline to automatically specify keypoints and ... (p. 2, 1 Introduction).
- **Paper-supported outcome:** Folding 0/10 3/10 5/10 Total (%) 6.7% 26.7% 46.7% Table 2: Success rate under external disturbances across both robot platforms. (p. 7, 4 Experiments).
- **Strongest explicit boundary:** The optimization module, on the other hand, does not contribute as much to the failures despite given limited time budget, since there often exist many possible solutions for each problem. (p. 8, 4 Experiments).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
