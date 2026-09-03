# Method - Uncertainty-Aware Gaussian Map for Vision-Language Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (24 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=LPv59noPAy; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/246583. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 6 (3 METHOD), p. 6 (3 METHOD), p. 3 (3 METHOD), p. 4 (3 METHOD), p. 4 (3 METHOD), p. 5 (3 METHOD)): Following the conventional procedure [11, 17, 30], our agent is optimized with a two-stage training scheme: pretraining with auxiliary objectives such as masked language modeling and single-step action prediction to ...

## Method Body Digest

- **p. 6 / 3 METHOD - extractive body cue:** Following the conventional procedure [11, 17, 30], our agent is optimized with a two-stage training scheme: pretraining with auxiliary objectives such as masked language modeling ...
- **p. 6 / 3 METHOD - extractive body cue:** To supervise SGM construction, we apply a pixel-wise rendering loss between the rendered outputs and ground-truth observations.
- **p. 3 / 3 METHOD - extractive body cue:** Based on these observations, the agent learns a navigation policy π(at/X, It, Dt) that predicts actions at ∈At, which includes navigable neighbor nodes, previously observed ...
- **p. 4 / 3 METHOD - extractive body cue:** Given multi-view RGB-D observations Ot = {It, Dt} at step t, the agent first generates a sparse pseudo-lidar point cloud via camera-to-world transformation.
- **p. 4 / 3 METHOD - extractive body cue:** For s, we apply SAM2 [68] to segment the panoramic observation I into spatially coherent regions {mk}K k=1 and extract their CLIP [69] embeddings, which ...
- **p. 5 / 3 METHOD - extractive body cue:** Because computing this matrix directly is infeasible, like [63, 67], we adopt the Fisher Information as a tractable approximation: ∇2 GLr = ∇G ˆI ∇G ...
- **p. 7 / 3 METHOD - extractive body cue:** At each navigable viewpoint, our agent constructs a SGM from panoramic observations and extends it into a 3D Value Map for reliable action prediction.
- **p. 7 / 3 METHOD - extractive body cue:** Once the 3D Value Map is established, action prediction incurs negligible additional cost compared to existing VLN agents [11].

## Design Rationale

- **p. 4 / 3 METHOD - extractive body cue:** To approximate it, like [66], we introduce variational distributions qϕ(χ) = {qϕµ i (χµ i ), qϕe i (χe i)}i and optimize them by minimizing ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Extensive ablation studies confirm the contribution of each component (§4.4).
- **p. 6 / 3 METHOD - extractive body cue:** This fusion enables the agent to jointly reason about geometric structure and perceptual confidence, thereby promoting reliable and uncertainty-aware decision-making.

## Source Evidence Cues

- **p. 6 / 3 METHOD - extractive body cue:** Following the conventional procedure [11, 17, 30], our agent is optimized with a two-stage training scheme: pretraining with auxiliary objectives such as masked language modeling ...
- **p. 6 / 3 METHOD - extractive body cue:** To supervise SGM construction, we apply a pixel-wise rendering loss between the rendered outputs and ground-truth observations.
- **p. 3 / 3 METHOD - extractive body cue:** Based on these observations, the agent learns a navigation policy π(at/X, It, Dt) that predicts actions at ∈At, which includes navigable neighbor nodes, previously observed ...
- **p. 4 / 3 METHOD - extractive body cue:** Given multi-view RGB-D observations Ot = {It, Dt} at step t, the agent first generates a sparse pseudo-lidar point cloud via camera-to-world transformation.
- **p. 4 / 3 METHOD - extractive body cue:** For s, we apply SAM2 [68] to segment the panoramic observation I into spatially coherent regions {mk}K k=1 and extract their CLIP [69] embeddings, which ...
- **p. 5 / 3 METHOD - extractive body cue:** Because computing this matrix directly is infeasible, like [63, 67], we adopt the Fisher Information as a tractable approximation: ∇2 GLr = ∇G ˆI ∇G ...
- **p. 7 / 3 METHOD - extractive body cue:** At each navigable viewpoint, our agent constructs a SGM from panoramic observations and extends it into a 3D Value Map for reliable action prediction.
- **Detected method headings:** 3 METHOD (p. 3); B MODEL DETAILS (p. 18)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Map / localization state | sensor stream을 pose와 world map으로 누적한다 | camera/depth/LiDAR, odometry, history | mapping, localization, scene graph 또는 map update를 수행 | pose/map/free-space state | Following the conventional procedure [11, 17, 30], our agent is optimized with a two-stage training scheme: pretraining with auxiliary objectives such as ... | p. 6 (3 METHOD), p. 6 (3 METHOD) |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | To supervise SGM construction, we apply a pixel-wise rendering loss between the rendered outputs and ground-truth observations. | p. 6 (3 METHOD), p. 3 (3 METHOD) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | Based on these observations, the agent learns a navigation policy π(at/X, It, Dt) that predicts actions at ∈At, which includes navigable neighbor ... | p. 3 (3 METHOD), p. 4 (3 METHOD) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 6 / 3 METHOD - extractive body cue:** Following the conventional procedure [11, 17, 30], our agent is optimized with a two-stage training scheme: pretraining with auxiliary objectives such as masked language modeling ...
- **p. 7 / 3 METHOD - extractive body cue:** Once the 3D Value Map is established, action prediction incurs negligible additional cost compared to existing VLN agents [11].
- **p. 4 / 3 METHOD - extractive body cue:** Therefore, after several rounds of differentiable rendering optimization, we further refine SGM by retaining only Gaussians subject to the constraints ∥ei∥2 > τe ∧αi > ...
- **p. 4 / 3 METHOD - extractive body cue:** To approximate it, like [66], we introduce variational distributions qϕ(χ) = {qϕµ i (χµ i ), qϕe i (χe i)}i and optimize them by minimizing ...
- **p. 5 / 3 METHOD - extractive body cue:** Following the same variational inference framework, we learn a posterior qϕs(χs) by maximizing the corresponding ELBO, regularized by a zero-mean Gaussian prior p(χs) = N(0, ...
- **p. 3 / 3 METHOD - extractive body cue:** These uncertainties are then integrated into a 3D Value Map, encoding affordances and constraints in the agent's perceptual space for decision-making (§3.3).
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** p. 3 (3 METHOD), p. 4 (3 METHOD), p. 5 (3 METHOD), p. 5 (3 METHOD), p. 6 (3 METHOD), p. 6 (3 METHOD).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | observations, agent, learns, navigation, policy, at/X, predicts, actions, includes, navigable, neighbor, nodes, previously, observed | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | observations, agent, learns, navigation, policy, at/X, predicts, actions, includes, navigable | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | approximate, like, introduce, variational, distributions, optimize, them, minimizing, Kullback-Leibler, divergence | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | Following, conventional, procedure, agent, optimized, two-stage, training, scheme, pretraining, auxiliary | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 3 METHOD - extractive body cue:** Based on these observations, the agent learns a navigation policy π(at/X, It, Dt) that predicts actions at ∈At, which includes navigable neighbor nodes, previously observed ...
- **p. 6 / 3 METHOD - extractive body cue:** Following the conventional procedure [11, 17, 30], our agent is optimized with a two-stage training scheme: pretraining with auxiliary objectives such as masked language modeling ...
- **p. 7 / 3 METHOD - extractive body cue:** At each navigable viewpoint, our agent constructs a SGM from panoramic observations and extends it into a 3D Value Map for reliable action prediction.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Early agents adopted sequence-to-sequence frameworks [1, 10], directly mapping language and visual observations into actions.
- **p. 6 / 3 METHOD - extractive body cue:** To supervise SGM construction, we apply a pixel-wise rendering loss between the rendered outputs and ground-truth observations.
- **p. 3 / 3 METHOD - extractive body cue:** At each step t, the agent receives a panoramic observation composed of multiple RGB views It = {It,k ∈RH×W ×3}K k=1 and associated depth maps ...
- **p. 4 / 3 METHOD - extractive body cue:** Given multi-view RGB-D observations Ot = {It, Dt} at step t, the agent first generates a sparse pseudo-lidar point cloud via camera-to-world transformation.
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | To support long-horizon reasoning, similar to [11, 17, 30], our agent maintains a dynamic topological memory that records both visited and navigable ... | episode/sequence/action-chunk boundary |
| Rate / latency | mapping/localization, global planner, local planner와 base controller rate를 구분한다. | Early agents adopted sequence-to-sequence frameworks [1, 10], directly mapping language and visual observations into actions. | Hz/fps, inference time and control rate |
| Memory | map/scene graph, pose history와 current local goal. | To support long-horizon reasoning, similar to [11, 17, 30], our agent maintains a dynamic topological memory that records both visited and navigable ... | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 6 / 3 METHOD - extractive body cue:** Following the conventional procedure [11, 17, 30], our agent is optimized with a two-stage training scheme: pretraining with auxiliary objectives such as masked language modeling ...
- **p. 6 / 3 METHOD - extractive body cue:** Pretraining is conducted for 100k iterations with a batch size of 64, optimized by Adam [78] with a learning rate of 1e-4.
- **p. 8 / 4 EXPERIMENT - extractive body cue:** These cases show how uncertainty helps disambiguate confounding structures and encode traversability constraints.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Following, conventional, procedure, agent, optimized, two-stage, training, scheme, pretraining, auxiliary, objectives, masked, language, modeling, single-step, action, prediction, strengthen, multimodal, representations.
- **Relevant PDF headings:** 3 METHOD (p. 3); B MODEL DETAILS (p. 18).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | All datasets are built upon the Matterport3D simulator [80], and are split into train, val-seen, val-unseen, and test sets according to scenes. | p. 7 (4 EXPERIMENT), p. 7 (4 EXPERIMENT) |
| Global / local decision | For R2R [1], we report Success Rate (SR), Trajectory Length (TL), Navigation Error (NE), Oracle Success Rate (OSR), and Success weighted by ... | p. 7 (4 EXPERIMENT), p. 7 (4 EXPERIMENT) |
| Motion execution / recovery | On the val unseen split, it achieves an SR of 78% compared to 76% from VER [17] and improves SPL from 65% ... | p. 8 (4 EXPERIMENT), p. 9 (4 EXPERIMENT) |

## Failure and Ablation Link

- **p. 9 / 4 EXPERIMENT - extractive body cue:** Components R2R [1] REVERIE [28] # SGM 3DVM SR ↑ SPL ↑ SR ↑ RGS ↑ RGSPL ↑ 1 - - 72.22 60.41 46.98 32.15 ...
- **p. 8 / 4 EXPERIMENT - extractive body cue:** (b) Our agent bypasses the obstacle and enters the designated region, while VER halts at the "table" without completing the task.
- **p. 9 / 4 EXPERIMENT - extractive body cue:** For row #2, the scores are obtained by using SGM as the 3D scene representation without uncertainty values.
- **p. 20 / Figure/Table caption - extractive body cue:** Table 10: Sensitivity Analysis of uncertainty-related hyperparameters on R2R val unseen split. (a) δ and (b) η regulate geometric uncertainty, while (c) ε governs semantic ...
- **p. 21 / Figure/Table caption - extractive body cue:** Table 12: Robustness to observation noise on R2R val unseen split. We evaluate an epistemic only variant (geometric + semantic), an aleatoric only variant (appearance), ...
- **p. 22 / Figure/Table caption - extractive body cue:** Figure 7: Failure Cases. (a) Our agent stops once "the sofa" comes into view, as the current observation already provides sufficient evidence of the target, ...
- **p. 9 / 4 EXPERIMENT - extractive body cue:** 5 illustrates our diverse perceptual forms. i) SGM preserves detailed geometric structures while maintaining high-fidelity rendering of the scene. ii) Geometric uncertainty reveals structural reliability, ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 6 (3 METHOD), p. 6 (3 METHOD), p. 3 (3 METHOD), p. 4 (3 METHOD), p. 4 (3 METHOD), p. 5 (3 METHOD), objective p. 6 (3 METHOD), p. 7 (3 METHOD), p. 4 (3 METHOD), p. 4 (3 METHOD), p. 5 (3 METHOD), p. 3 (3 METHOD), temporal p. 6 (3 METHOD), p. 1 (1 INTRODUCTION), p. 2 (2 RELATED WORK), p. 2 (2 RELATED WORK), p. 3 (3 METHOD), p. 3 (3 METHOD).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
