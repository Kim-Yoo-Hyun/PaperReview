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

- **Closed-loop position:** `image/video, language instruction, proprioception과 history → language-grounded task state와 action-policy context → continuous action, pose 또는 action chunk`.
- 이 논문의 재사용 가능한 지점은 It takes visual inputs ot = {it, pt}, where it is the image and pt is the point cloud, while language l, keypoints kt, and robot state rt are provided as structured ...를 3.1 Task Formulation and Model Architecture Given a dataset D = {τ1, . . . , τN} of N expert demonstrations, each demonstration τ is paired with a task description l and ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 language-grounded task state와 action-policy context가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 This makes the pipeline prone to failure if the underlying models are inaccurate-for example, if GroundingDINO [71] misses critical keypoints on the cup handle that needs to be grasped, or if GPT-4 ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Our contributions are as follows: 1) We propose 3DS-VLA, equipping pretrained 2D VLMs with comprehensive 3D awareness for robust end-effector pose prediction.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `VLA and generalist robot policies`; tags: `VLA, 3D Vision, Robotics`.
- **Reading predecessor in the generated track queue:** VoxAct-B: Voxel-Based Acting and Stabilizing Policy for Bimanual Manipulation (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** GraspVLA: a Grasping Foundation Model Pre-trained on Billion-scale Synthetic Action Data (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** This makes the pipeline prone to failure if the underlying models are inaccurate-for example, if GroundingDINO [71] misses critical keypoints on the cup handle that needs to be grasped, or if GPT-4 ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Since we establish associations between the robot and its environment through structured text input, our model learns to focus on task-relevant objects while disregarding irrelevant background disturbances..
3. Compare against the body-reported baseline or a matched simpler baseline: 2, in the dual-arm setting, our method outperforms all baselines by a significant margin..
4. Report the body metric and its denominator/aggregation: 1, in the single-arm setting, our method surpasses all baselines by at least 4% average success rate..
5. Re-run the body-reported ablation/failure condition: Both Ours and Ours-s achieve the same average success rate of 0.66 on single-arm tasks, demonstrating that our model can effectively handle different embodiments within a unified training pipeline, without requiring architectural ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 3 (3 Method), p. 4 (3 Method), p. 3 (3 Method); the primary result is directionally consistent at p. 7 (4 Experiment), p. 8 (4 Experiment), p. 6 (4 Experiment); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 contributions, follows, DS-VLA mechanism이 2, in the dual-arm setting, our method outperforms all baselines by a significant margin. 대비 1, in the single-arm setting, our method surpasses all baselines by at least 4% average success rate.을 개선하고, This makes the pipeline prone to failure if the underlying models are inaccurate-for example, if GroundingDINO ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
