# Insights — VoxAct-B: Voxel-Based Acting and Stabilizing Policy for Bimanual Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v270/liu25i.html; PDF retrieval source: https://raw.githubusercontent.com/mlresearch/v270/main/assets/liu25i/liu25i.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / 1 Introduction - extractive body cue:** To this end, we propose VoxAct-B, a novel voxel-based, language-conditioned method for bimanual manipulation.
- **p. 4 / 4 Method - extractive body cue:** This allows our method to learn to map the appropriate acting or stabilizing actions to a given arm during training.
- **p. 1 / 1 Introduction - extractive body cue:** To address this, we propose utilizing VLMs to focus on the most pertinent regions within the scene by cropping out less relevant regions.
- **p. 2 / 1 Introduction - extractive body cue:** We introduce a bimanual version of Open Drawer, Open Jar, Put Item in Drawer, and Hand Over Item tasks.
- **p. 5 / 4 Method - extractive body cue:** The overall training loss for VoxAct-B is: Ltotal = Lacting + Lstabilizing (1) and where for both values of arm ∈{acting, stabilizing}, we have Larm ...
- **p. 5 / 4 Method - extractive body cue:** Then, we use Segment Anything [65], a foundational image segmentation model, to obtain the segmentation mask of the object and use the mask's centroid along ...
- **p. 14 / A.1 Additional Implementation Details - extractive body cue:** We use 2048 latents of dimension 512 in the Perceiver Transformer [70] and optimize the entire network using the LAMB [71] optimizer.
- **Contribution anchor:** p. 1 (1 Introduction), p. 4 (4 Method), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 5 (4 Method), p. 5 (4 Method)

### Strongest assumption and failure boundary

- **p. 1 / 1 Introduction - extractive body cue:** However, they are generally sample inefficient, and using primitives can hinder generalization to different tasks as they are not easily adaptable to other types of ...
- **p. 1 / 1 Introduction - extractive body cue:** They typically require two-hand coordination and high-precision, fine-grained manipulation, which are challenging for current robotic manipulation systems.
- **p. 8 / 6 Results - extractive body cue:** 6.3 Limitations and Failure Cases VoxAct-B implicitly assumes the object of interest does not encompass most of the workspace.
- **p. 8 / 6 Results - extractive body cue:** VoxAct-B succeeds in 6 out of 10 trials; the failures include robot joints hitting their limits, imprecision in grasping the handle, and collisions with the ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: Overview of VoxAct-B. Given RGB-D images and a language goal, we input an RGB image from the front camera and a text query ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3: Top: VLMs usage as part of VoxAct-B, visualizing the Open Jar task in simulation, showing the role of OWL-ViT and Segment Anything. The ...
- **p. 6 / 5 Experiments - extractive body cue:** Note that the real-world jar and drawer cannot be opened without the use of a second arm.
- **Boundary to test:** 6.3 Limitations and Failure Cases VoxAct-B implicitly assumes the object of interest does not encompass most of the workspace.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | To this end, we propose VoxAct-B, a novel voxel-based, language-conditioned method for bimanual manipulation. | p. 1 (1 Introduction), p. 4 (4 Method) |
| Reported outcome | We found the Time-series Diffusion Transformer to outperform the CNN-based Diffusion Policy on Open Drawer and Open Jar, while both of them achieved comparable success rates on Put Item in Drawer. | p. 16 (C Additional Implementation Details for the Baselines), p. 6 (5 Experiments) |
| Failure/limitation | 6.3 Limitations and Failure Cases VoxAct-B implicitly assumes the object of interest does not encompass most of the workspace. | p. 8 (6 Results), p. 8 (6 Results) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `image/video, language instruction, proprioception과 history → language-grounded task state와 action-policy context → continuous action, pose 또는 action chunk`.
- 이 논문의 재사용 가능한 지점은 At each time step, the input to each arm is a voxel observation v, proprioception data of both robot arms ρ, a language goal l ∈{ℓas, ℓsa}, and an arm ID ξ ...를 Voxel representations, when coupled with discretized action spaces, can increase sample efficiency and generalization by introducing spatial equivariance into a learned system, where transformations of the input lead to corresponding tr ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 language-grounded task state와 action-policy context가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 6.3 Limitations and Failure Cases VoxAct-B implicitly assumes the object of interest does not encompass most of the workspace.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: To this end, we propose VoxAct-B, a novel voxel-based, language-conditioned method for bimanual manipulation.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `VLA and generalist robot policies`; tags: `VLM, 3D manipulation, bimanual, Robotics`.
- **Reading predecessor in the generated track queue:** ReKep: Spatio-Temporal Reasoning of Relational Keypoint Constraints for Robotic Manipulation (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** 3DS-VLA: A 3D Spatial-Aware Vision Language Action Model for Robust Multi-Task Manipulation (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** 6.3 Limitations and Failure Cases VoxAct-B implicitly assumes the object of interest does not encompass most of the workspace.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: For simulation experiments, we build on top of RLBench [14], a popular robot manipulation benchmark widely used in prior work, including VoxPoser and PerAct..
3. Compare against the body-reported baseline or a matched simpler baseline: When we train all methods using more demonstrations (100), VoxAct-B still outperforms all baselines..
4. Report the body metric and its denominator/aggregation: Then, we use the bestperforming acting and stabilizing checkpoints to obtain the test success rate..
5. Re-run the body-reported ablation/failure condition: Table 5: Ablation results of ACT and Diffusion Policy trained on 100 demonstrations and evaluated across five training seeds. "FAS" refers to the demonstrations with fixed acting and stabilizing arms (i.e., right ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 5 (4 Method), p. 5 (4 Method), p. 14 (A.1 Additional Implementation Details); the primary result is directionally consistent at p. 16 (C Additional Implementation Details for the Baselines), p. 6 (5 Experiments), p. 7 (6 Results); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 VoxAct-B, novel, voxel-based mechanism이 When we train all methods using more demonstrations (100), VoxAct-B still outperforms all baselines. 대비 Then, we use the bestperforming acting and stabilizing checkpoints to obtain the test success rate.을 개선하고, 6.3 Limitations and Failure Cases VoxAct-B implicitly assumes the object of interest does not encompass most ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
