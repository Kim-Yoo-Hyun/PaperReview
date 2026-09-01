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
- **p. 1 / 1 Introduction - extractive body cue:** 1: the robot must grasp at the handle, keep the cup upright while transporting *Denotes equal contribution.
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

- **Closed-loop position:** `image/video, language instruction, proprioception과 history → language-grounded task state와 action-policy context → continuous action, pose 또는 action chunk`.
- 이 논문의 재사용 가능한 지점은 Our contributions are summarized as follows: 1) We formulate manipulation tasks as a hierarchical optimization problem with Relational Keypoint Constraints; 2) We devise a pipeline to automatically specify keypoints and constraints usin ...를 (4) How to automatically obtain ReKep from RGB-D observations and language instructions (Sec.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 language-grounded task state와 action-policy context가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 The optimization module, on the other hand, does not contribute as much to the failures despite given limited time budget, since there often exist many possible solutions for each problem.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Our contributions are summarized as follows: 1) We formulate manipulation tasks as a hierarchical optimization problem with Relational Keypoint Constraints; 2) We devise a pipeline to automatically specify keypoints and constraints usin ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `VLA and generalist robot policies`; tags: `Planning, 3D geometry, Robotics, VLM`.
- **Reading predecessor in the generated track queue:** Grounding Actions in Camera Space: Observation-Centric Vision-Language-Action Policy (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** VoxAct-B: Voxel-Based Acting and Stabilizing Policy for Bimanual Manipulation (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** The optimization module, on the other hand, does not contribute as much to the failures despite given limited time budget, since there often exist many possible solutions for each problem.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: 5 Conclusion & Limitations In this work, we presented Relational Keypoint Constraints (ReKep), a structural task representation using constraints that operates on semantic keypoints to specify desired relations between robot arms, objec ....
3. Compare against the body-reported baseline or a matched simpler baseline: Compared to baselines, ReKep can effectively handle core challenges of each task..
4. Report the body metric and its denominator/aggregation: Folding 0/10 4/10 7/10 Total (%) 10.0% 44.3% 68.6% Table 1: Success rate on wheeled singlearm and stationary bimanual platforms..
5. Re-run the body-reported ablation/failure condition: We evaluate two variants of the system: "Auto" uses foundation models to automatically generate ReKep, and "Annotated (Annot.)" uses human-annotated ReKep..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 5 (3 Method), p. 24 (A.8 Implementation Details of Sub-Goal Solver), p. 22 (A.6 Querying Vision-Language Model); the primary result is directionally consistent at p. 7 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 contributions, summarized, follows mechanism이 Compared to baselines, ReKep can effectively handle core challenges of each task. 대비 Folding 0/10 4/10 7/10 Total (%) 10.0% 44.3% 68.6% Table 1: Success rate on wheeled singlearm and stationary ...을 개선하고, The optimization module, on the other hand, does not contribute as much to the failures despite ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
