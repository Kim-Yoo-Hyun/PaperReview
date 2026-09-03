# Insights — MoTo: A Zero-shot Plug-in Interaction-aware Navigation for General Mobile Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v305/wu25c.html; PDF retrieval source: https://raw.githubusercontent.com/mlresearch/v305/main/assets/wu25c/wu25c.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1 Introduction - extractive body cue:** In this paper, we propose to solve the problem of mobile manipulation with an interaction-aware navigation policy, namely Move and Touch (MoTo).
- **p. 3 / 1 Introduction - extractive body cue:** Inspired by ReKep, we propose a multi-view voting strategy to generate scene-level interaction keypoints to fine-grain guide mobile manipulation trajectory generation.
- **p. 5 / 4 Approach - extractive body cue:** Therefore, we propose a two-stage VLM-based method to generate keypoints for an image, which is divided into keypoint proposal stage and keypoint selection stage.
- **p. 3 / 1 Introduction - extractive body cue:** With the fast development of manipulation foundation models [37, 11, 12, 38], we believe this assumption is reasonable and feasible.
- **p. 6 / 4 Approach - extractive body cue:** Firstly, extracting the wrist keypoint from the RGB-D observation sw t , then projecting it to 3D space using Et.
- **p. 5 / 4 Approach - extractive body cue:** VLM(Tk, {Ik 1 , ..., Ik m}) generates target keypoint proposals in different images, which are then aggregated with a voting module V.
- **p. 5 / 4 Approach - extractive body cue:** Current segmentation models can only segment a laptop into screen and keyboard, and a table into surface and legs, which cannot provide detailed, actionable locations.
- **Contribution anchor:** p. 2 (1 Introduction), p. 3 (1 Introduction), p. 5 (4 Approach), p. 3 (1 Introduction), p. 6 (4 Approach), p. 5 (4 Approach)

### Strongest assumption and failure boundary

- **p. 2 / 1 Introduction - extractive body cue:** Get the Water Cook Food Pick up the Fruit Mobile Trajectory Arm Trajectory Fixed-base Manipulation MoTo AnyGrasp OpenVLA RDT-1B iDP3 Figure 1: MoTo can be ...
- **p. 1 / 1 Introduction - extractive body cue:** However, the requirements to perform diverse tasks in unstructured environments (e.g., assisting humans in their daily lives) present significant challenges.
- **p. 2 / 1 Introduction - extractive body cue:** However, naive combining navigation and manipulation results in compounding errors since the large gap between the goals of navigation and manipulation [17].
- **p. 3 / 1 Introduction - extractive body cue:** 3 Problem Statement Our goal is to enable robots to perform long-horizon mobile manipulation tasks with strong generalization ability to unseen environments and goals.
- **p. 3 / 1 Introduction - extractive body cue:** More recently, foundation-model-based frameworks like VoxPoser [37] and ReKep [38] leverage pretrained priors to infer physical constraints, which significantly improve generalization.
- **p. 16 / Figure/Table caption - extractive body cue:** Figure 6: Visualization results for keypoint generation. MoTo selects keypoint proposals (red points) from multi-views, projects them into 3D space and votes to generate keypoints ...
- **p. 16 / Figure/Table caption - extractive body cue:** Figure 7: Failure Cases in real-world experiments. D.1 Manipulation Visualization Figure 6 demonstrates the scene keypoint generation and mobile trajectory in task "Serve me water". ...
- **Boundary to test:** Figure 6: Visualization results for keypoint generation. MoTo selects keypoint proposals (red points) from multi-views, projects them into 3D space and votes to generate keypoints for manipulation. Workspace Out of Range Not ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | In this paper, we propose to solve the problem of mobile manipulation with an interaction-aware navigation policy, namely Move and Touch (MoTo). | p. 2 (1 Introduction), p. 3 (1 Introduction) |
| Reported outcome | All methods are run 10 times on the three types of mobile manipulation tasks, where the dots represent the performance of each test (Best view in color). success rate further improves by ... | p. 8 (5 Experiment), p. 7 (5 Experiment) |
| Failure/limitation | Figure 6: Visualization results for keypoint generation. MoTo selects keypoint proposals (red points) from multi-views, projects them into 3D space and votes to generate keypoints for manipulation. Workspace Out of Range Not ... | p. 16 (Figure/Table caption), p. 16 (Figure/Table caption) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `egocentric RGB-D, language/task goal, base-arm proprioception → map/object/contact state와 base-arm coordination decision → base motion plus arm/gripper action`.
- 이 논문의 재사용 가능한 지점은 Based on robot scanning RGB-D observation to get 3D scene point clouds and graphs, we utilize VLM and multi-view consistency voting to get interaction keypoints, and generate mobile manipulation trajectories via proposed ...를 In this paper, we propose to solve the problem of mobile manipulation with an interaction-aware navigation policy, namely Move and Touch (MoTo).로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 map/object/contact state와 base-arm coordination decision가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Figure 6: Visualization results for keypoint generation. MoTo selects keypoint proposals (red points) from multi-views, projects them into 3D space and votes to generate keypoints for manipulation. Workspace Out of Range Not ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: In this paper, we propose to solve the problem of mobile manipulation with an interaction-aware navigation policy, namely Move and Touch (MoTo).
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `Locomotion, whole-body, mobile manipulation, and humanoids`; tags: `Navigation, mobile manipulation, VLM`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Figure 6: Visualization results for keypoint generation. MoTo selects keypoint proposals (red points) from multi-views, projects them into 3D space and votes to generate keypoints for manipulation. Workspace Out of Range Not ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: The OVMM benchmark consists of 60 extensive indoor scenes and contains more than 18k 3D models of everyday objects.OVMM utilizes Hello Robot as an agent to perform the "Move a target object ....
3. Compare against the body-reported baseline or a matched simpler baseline: 5.1 Comparison with State-of-the-art Methods Table 1 demonstrates the performance of MoTo on the OVMM [18] validation set compared to the baseline, decomposing it into four sequential stages: finding the target (FindObj), ....
4. Report the body metric and its denominator/aggregation: All methods are run 10 times on the three types of mobile manipulation tasks, where the dots represent the performance of each test (Best view in color). success rate further improves by ....
5. Re-run the body-reported ablation/failure condition: Table 2: Ablation experiments for optimization cost terms and keypoint generation variants..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 6 (4 Approach), p. 5 (4 Approach), p. 5 (4 Approach); the primary result is directionally consistent at p. 8 (5 Experiment), p. 7 (5 Experiment), p. 8 (5 Experiment); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 solve, problem, mobile mechanism이 5.1 Comparison with State-of-the-art Methods Table 1 demonstrates the performance of MoTo on the OVMM [18] ... 대비 All methods are run 10 times on the three types of mobile manipulation tasks, where the dots represent ...을 개선하고, Figure 6: Visualization results for keypoint generation. MoTo selects keypoint proposals (red points) from multi-views, projects ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
