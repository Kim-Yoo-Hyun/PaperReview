# Insights — 3DS-VLA: A 3D Spatial-Aware Vision Language Action Model for Robust Multi-Task Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (16 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v305/li25g.html; PDF retrieval source: https://raw.githubusercontent.com/mlresearch/v305/main/assets/li25g/li25g.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1 Introduction - extractive body cue:** Our contributions are as follows: 1) We propose 3DS-VLA, equipping pretrained 2D VLMs with comprehensive 3D awareness for robust end-effector pose prediction.
- **p. 4 / 3 Method - extractive body cue:** Therefore, we propose a 2D-to-3D positional alignment mechanism that allows the original 2D PEs, which are interpretable to pretrained models, to encode semantically aligned 2D ...
- **p. 2 / 1 Introduction - extractive body cue:** 1 (left), we propose 3DS-VLA, which equips pretrained 2D vision-language models (2D VLMs) with 3D spatial awareness for robust action generation.
- **p. 3 / 3 Method - extractive body cue:** 3.1 Task Formulation and Model Architecture Given a dataset D = {τ1, . . . , τN} of N expert demonstrations, each demonstration τ is ...
- **p. 4 / 3 Method - extractive body cue:** The model π consists of a 2D visual encoder, LLM (LLaMA) [63], a cross-modality projection module [62], and LoRA adapters [64].
- **p. 3 / 3 Method - extractive body cue:** The objective of policy model π is to learn action generation in SE(3) space: π : (ot, l, kt, rt) →ˆat+1.
- **p. 4 / 3 Method - extractive body cue:** 3.2), 2D images and 3D point clouds are first tokenized and encoded using pretrained 2D positional embeddings (PEa), then fused and processed by the shared ...
- **Contribution anchor:** p. 2 (1 Introduction), p. 4 (3 Method), p. 2 (1 Introduction), p. 3 (3 Method), p. 4 (3 Method), p. 3 (3 Method)

### Strongest assumption and failure boundary

- **p. 2 / 1 Introduction - extractive body cue:** All these limitations lead us to consider: "How can we build a robust VLA model that incorporates comprehensive 3D spatial awareness?" To address the above ...
- **p. 1 / 1 Introduction - extractive body cue:** However, since robots operate in a complex 3D world, they face challenges in perceiving 3D geometry and reasoning about spatial context solely from 2D image ...
- **p. 1 / 1 Introduction - extractive body cue:** However, unlike 2D policy models that have access to large-scale datasets, the scarcity of large-scale 3D data limits these methods' scalability in complex robotic environments.
- **p. 2 / 1 Introduction - extractive body cue:** Yet, robotic manipulation requires intricate environmental interactions, and such methods [32, 33, 34, 35, 36] often lack a broader understanding of the robot's action with ...
- **p. 8 / 4 Experiment - extractive body cue:** This makes the pipeline prone to failure if the underlying models are inaccurate-for example, if GroundingDINO [71] misses critical keypoints on the cup handle that ...
- **p. 6 / 4 Experiment - extractive body cue:** Compared with 2D VLA methods, we observe frequent failures during the critical final stage of 3D contact.
- **p. 8 / 4 Experiment - extractive body cue:** Please refer to Appendix for more details: Section 7.2 for visualization of tasks in RLBench and real world and Section 7.3 for discussion of failure ...
- **Boundary to test:** This makes the pipeline prone to failure if the underlying models are inaccurate-for example, if GroundingDINO [71] misses critical keypoints on the cup handle that needs to be grasped, or if GPT-4 ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Our contributions are as follows: 1) We propose 3DS-VLA, equipping pretrained 2D VLMs with comprehensive 3D awareness for robust end-effector pose prediction. | p. 2 (1 Introduction), p. 4 (3 Method) |
| Reported outcome | Both Ours and Ours-s achieve the same average success rate of 0.66 on single-arm tasks, demonstrating that our model can effectively handle different embodiments within a unified training pipeline, without requiring architectural ... | p. 7 (4 Experiment), p. 8 (4 Experiment) |
| Failure/limitation | This makes the pipeline prone to failure if the underlying models are inaccurate-for example, if GroundingDINO [71] misses critical keypoints on the cup handle that needs to be grasped, or if GPT-4 ... | p. 8 (4 Experiment), p. 6 (4 Experiment) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Paper-specific interface:** It takes visual inputs ot = {it, pt}, where it is the image and pt is the point cloud, while language l, keypoints kt, and robot state rt are provided ... (p. 3, 3 Method).
- **Paper-specific mechanism:** Our contributions are as follows: 1) We propose 3DS-VLA, equipping pretrained 2D VLMs with comprehensive 3D awareness for robust end-effector pose prediction. (p. 2, 1 Introduction).
- **Evidence boundary:** the reported outcome is Additionally, we perform an extra experiment where we first fine-tune the pretrained VLM on the OXE dataset [74], which only takes 2D images as input, and then continue finetuning on ... (p. 7, 4 Experiment); the relevant task/metric cue is 1, in the single-arm setting, our method surpasses all baselines by at least 4% average success rate. (p. 6, 4 Experiment). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** This makes the pipeline prone to failure if the underlying models are inaccurate-for example, if GroundingDINO [71] misses critical keypoints on the cup handle that needs to be grasped, or ... (p. 8, 4 Experiment).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `VLA and generalist robot policies`; tags: `VLA, 3D Vision, Robotics`.
- **Reading predecessor in the generated track queue:** VoxAct-B: Voxel-Based Acting and Stabilizing Policy for Bimanual Manipulation (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** GraspVLA: a Grasping Foundation Model Pre-trained on Billion-scale Synthetic Action Data (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** This makes the pipeline prone to failure if the underlying models are inaccurate-for example, if GroundingDINO [71] misses critical keypoints on the cup handle that needs to be grasped, or if GPT-4 ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: It takes visual inputs ot = {it, pt}, where it is the image and pt is the point cloud, while language l, keypoints kt, and robot state rt are provided ... (p. 3, 3 Method); preserve the objective/update rule: The objective of policy model π is to learn action generation in SE(3) space: π : (ot, l, kt, rt) →ˆat+1. (p. 3, 3 Method).
2. Use the paper-reported task/data/environment cue: Since we establish associations between the robot and its environment through structured text input, our model learns to focus on task-relevant objects while disregarding irrelevant background disturbances. (p. 8, 4 Experiment).
3. Compare against the reported or matched baseline: 2, in the dual-arm setting, our method outperforms all baselines by a significant margin. (p. 6, 4 Experiment).
4. Report the body metric with its denominator and aggregation: 1, in the single-arm setting, our method surpasses all baselines by at least 4% average success rate. (p. 6, 4 Experiment).
5. Re-run the reported ablation or stress/failure condition: This stems from their reliance on single-view 2D images without explicit 3D geometric understanding, which is essential for precise action prediction. (p. 6, 4 Experiment); if none is reported, design one around: This makes the pipeline prone to failure if the underlying models are inaccurate-for example, if GroundingDINO [71] misses critical keypoints on the cup handle that needs to be grasped, or ... (p. 8, 4 Experiment).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 2 (1 Introduction), p. 2 (1 Introduction), match the reported outcome at p. 7 (4 Experiment), p. 6 (4 Experiment), p. 8 (4 Experiment), and measure the boundary at p. 8 (4 Experiment), p. 16 (7 Appendix).

## Falsifiable research question

Under the paper's stated interface (It takes visual inputs ot = {it, pt}, where it is the image and pt is the point cloud, while language l, ...), does the paper-specific mechanism (Our contributions are as follows: 1) We propose 3DS-VLA, equipping pretrained 2D VLMs with comprehensive 3D awareness for robust end-effector pose prediction.) retain the reported evaluation outcome (1, in the single-arm setting, our method surpasses all baselines by at least 4% average success rate.) when tested against the paper's strongest explicit boundary (This makes the pipeline prone to failure if the underlying models are inaccurate-for example, if GroundingDINO [71] misses ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (1, in the single-arm setting, our method surpasses all baselines by at least 4% average success rate.) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (16 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** Our contributions are as follows: 1) We propose 3DS-VLA, equipping pretrained 2D VLMs with comprehensive 3D awareness for robust end-effector pose prediction. (p. 2, 1 Introduction).
- **Paper-supported outcome:** Additionally, we perform an extra experiment where we first fine-tune the pretrained VLM on the OXE dataset [74], which only takes 2D images as input, and then continue finetuning on ... (p. 7, 4 Experiment).
- **Strongest explicit boundary:** This makes the pipeline prone to failure if the underlying models are inaccurate-for example, if GroundingDINO [71] misses critical keypoints on the cup handle that needs to be grasped, or ... (p. 8, 4 Experiment).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
