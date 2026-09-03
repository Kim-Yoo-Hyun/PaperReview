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

- **Paper-specific interface:** At each time step, the input to each arm is a voxel observation v, proprioception data of both robot arms ρ, a language goal l ∈{ℓas, ℓsa}, and an arm ... (p. 4, 4 Method).
- **Paper-specific mechanism:** To this end, we propose VoxAct-B, a novel voxel-based, language-conditioned method for bimanual manipulation. (p. 1, 1 Introduction).
- **Evidence boundary:** the reported outcome is Figure 4: Example successful rollouts (one per row) of VoxAct-B on a real-world bimanual setup with UR5s. Ablation experiments. Table 2 reports results on Open Drawer in simulation, based on ... (p. 8, Figure/Table caption); the relevant task/metric cue is We adapt the Mobile ALOHA repository for ACT and a CNN-based Diffusion Policy, and we tune their parameters (e.g., chunk size and action horizon) to improve performance. (p. 6, 5 Experiments). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** 6.3 Limitations and Failure Cases VoxAct-B implicitly assumes the object of interest does not encompass most of the workspace. (p. 8, 6 Results).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `VLA and generalist robot policies`; tags: `VLM, 3D manipulation, bimanual, Robotics`.
- **Reading predecessor in the generated track queue:** ReKep: Spatio-Temporal Reasoning of Relational Keypoint Constraints for Robotic Manipulation (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** 3DS-VLA: A 3D Spatial-Aware Vision Language Action Model for Robust Multi-Task Manipulation (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** 6.3 Limitations and Failure Cases VoxAct-B implicitly assumes the object of interest does not encompass most of the workspace.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: At each time step, the input to each arm is a voxel observation v, proprioception data of both robot arms ρ, a language goal l ∈{ℓas, ℓsa}, and an arm ... (p. 4, 4 Method); preserve the objective/update rule: While one can increase the number of voxels, this would consume more memory, slow down training, and adversely affect learning as the policy is optimizing over a larger state space. (p. 5, 4 Method).
2. Use the paper-reported task/data/environment cue: For simulation experiments, we build on top of RLBench [14], a popular robot manipulation benchmark widely used in prior work, including VoxPoser and PerAct. (p. 6, 5 Experiments).
3. Compare against the reported or matched baseline: 5.1 Baselines and Ablations In simulation, we compare against several strong baseline methods: Action Chunking with Transformers (ACT) [3], Diffusion Policy [15], and VoxPoser [16]. (p. 6, 5 Experiments).
4. Report the body metric with its denominator and aggregation: We adapt the Mobile ALOHA repository for ACT and a CNN-based Diffusion Policy, and we tune their parameters (e.g., chunk size and action horizon) to improve performance. (p. 6, 5 Experiments).
5. Re-run the reported ablation or stress/failure condition: Note that the real-world jar and drawer cannot be opened without the use of a second arm. (p. 6, 5 Experiments); if none is reported, design one around: 6.3 Limitations and Failure Cases VoxAct-B implicitly assumes the object of interest does not encompass most of the workspace. (p. 8, 6 Results).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 1 (1 Introduction), p. 1 (1 Introduction), match the reported outcome at p. 8 (Figure/Table caption), p. 17 (Figure/Table caption), p. 7 (Figure/Table caption), and measure the boundary at p. 8 (6 Results), p. 8 (6 Results).

## Falsifiable research question

Under the paper's stated interface (At each time step, the input to each arm is a voxel observation v, proprioception data of both robot arms ρ, a ...), does the paper-specific mechanism (To this end, we propose VoxAct-B, a novel voxel-based, language-conditioned method for bimanual manipulation.) retain the reported evaluation outcome (We adapt the Mobile ALOHA repository for ACT and a CNN-based Diffusion Policy, and we tune their parameters ...) when tested against the paper's strongest explicit boundary (6.3 Limitations and Failure Cases VoxAct-B implicitly assumes the object of interest does not encompass most of the ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (We adapt the Mobile ALOHA repository for ACT and a CNN-based Diffusion Policy, and we tune their parameters ...) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (17 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** To this end, we propose VoxAct-B, a novel voxel-based, language-conditioned method for bimanual manipulation. (p. 1, 1 Introduction).
- **Paper-supported outcome:** Figure 4: Example successful rollouts (one per row) of VoxAct-B on a real-world bimanual setup with UR5s. Ablation experiments. Table 2 reports results on Open Drawer in simulation, based on ... (p. 8, Figure/Table caption).
- **Strongest explicit boundary:** 6.3 Limitations and Failure Cases VoxAct-B implicitly assumes the object of interest does not encompass most of the workspace. (p. 8, 6 Results).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
