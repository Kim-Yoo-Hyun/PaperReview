# Method - Gaussian Splatting Visual MPC for Granular Media Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (7 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.proceedings.com/content/081/081087webtoc.pdf; PDF retrieval source: https://arxiv.org/pdf/2410.09740v3. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 3 (IV. OUR APPROACH), p. 3 (IV. OUR APPROACH), p. 4 (IV. OUR APPROACH), p. 4 (IV. OUR APPROACH)): We form the node features of the GNN as (ci t,σi t ,Ri t,gi t,si t) for node vi t. f consists of node encoder fenc with node representation ¯vi ...

## Method Body Digest

- **p. 3 / IV. OUR APPROACH - extractive body cue:** We form the node features of the GNN as (ci t,σi t ,Ri t,gi t,si t) for node vi t. f consists of node encoder ...
- **p. 3 / IV. OUR APPROACH - extractive body cue:** The trajectory optimization problem over a horizon T can be defined as follows: u0:T-1 = argminu0:T-1c(ZT,Ztarget) (6) Z0 = h(O0), Ztarget = h(Otarget), Zt+1 = ...
- **p. 4 / IV. OUR APPROACH - extractive body cue:** In the end, we obtain a set of Gaussians that represents the next image: ˆZt+1 = {(ci t,αi t , ˆR i t+1, ˆgi t+1,si ...
- **p. 4 / IV. OUR APPROACH - extractive body cue:** After the first action in the sequence is executed by the robot, we re-run the planning algorithm to generate a new action sequence.
- **p. 3 / IV. OUR APPROACH - extractive body cue:** This optimization process aims to acquire the sequence of actions {ut} to minimize the cost function c(ZT,Ztarget).
- **p. 4 / IV. OUR APPROACH - extractive body cue:** We perform the optimization shown in Equation 6 as part of a gradient-based MPC loop (as shown in Alg.
- **p. 3 / IV. OUR APPROACH - extractive body cue:** Problem Formulation Given multi-view RGBD observations Otarget = {ov,mv}N v=1 of the target pattern of the granular material, where ov represents the RGBD image and ...
- **p. 4 / IV. OUR APPROACH - extractive body cue:** The cost function used in the planning algorithm is the following: c(Zt,Ztarget) = 1 /P/ ∑ x∈P /dt(x)-dtarget(x)/2 (16) where P is a pre-defined set ...

## Design Rationale

- **p. 3 / IV. OUR APPROACH - extractive body cue:** We form the node features of the GNN as (ci t,σi t ,Ri t,gi t,si t) for node vi t. f consists of node encoder ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Our method takes a few multi-view images of a scene and their corresponding camera poses as input, and (a) converts them into their Gaussian splatting ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Our contribution: We use the Gaussian splats representing the scene at each time as a state vector that can be manipulated via MPC, effectively lowering ...

## Source Evidence Cues

- **p. 3 / IV. OUR APPROACH - extractive body cue:** We form the node features of the GNN as (ci t,σi t ,Ri t,gi t,si t) for node vi t. f consists of node encoder ...
- **p. 3 / IV. OUR APPROACH - extractive body cue:** The trajectory optimization problem over a horizon T can be defined as follows: u0:T-1 = argminu0:T-1c(ZT,Ztarget) (6) Z0 = h(O0), Ztarget = h(Otarget), Zt+1 = ...
- **p. 4 / IV. OUR APPROACH - extractive body cue:** In the end, we obtain a set of Gaussians that represents the next image: ˆZt+1 = {(ci t,αi t , ˆR i t+1, ˆgi t+1,si ...
- **p. 4 / IV. OUR APPROACH - extractive body cue:** After the first action in the sequence is executed by the robot, we re-run the planning algorithm to generate a new action sequence.
- **Detected method headings:** IV. OUR APPROACH (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | We form the node features of the GNN as (ci t,σi t ,Ri t,gi t,si t) for node vi t. f consists ... | p. 3 (IV. OUR APPROACH), p. 3 (IV. OUR APPROACH) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | The trajectory optimization problem over a horizon T can be defined as follows: u0:T-1 = argminu0:T-1c(ZT,Ztarget) (6) Z0 = h(O0), Ztarget = ... | p. 3 (IV. OUR APPROACH), p. 4 (IV. OUR APPROACH) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | In the end, we obtain a set of Gaussians that represents the next image: ˆZt+1 = {(ci t,αi t , ˆR i ... | p. 4 (IV. OUR APPROACH), p. 4 (IV. OUR APPROACH) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / IV. OUR APPROACH - extractive body cue:** This optimization process aims to acquire the sequence of actions {ut} to minimize the cost function c(ZT,Ztarget).
- **p. 4 / IV. OUR APPROACH - extractive body cue:** We perform the optimization shown in Equation 6 as part of a gradient-based MPC loop (as shown in Alg.
- **p. 3 / IV. OUR APPROACH - extractive body cue:** Problem Formulation Given multi-view RGBD observations Otarget = {ov,mv}N v=1 of the target pattern of the granular material, where ov represents the RGBD image and ...
- **p. 4 / IV. OUR APPROACH - extractive body cue:** The cost function used in the planning algorithm is the following: c(Zt,Ztarget) = 1 /P/ ∑ x∈P /dt(x)-dtarget(x)/2 (16) where P is a pre-defined set ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 4 (IV. OUR APPROACH), p. 3 (IV. OUR APPROACH), p. 4 (IV. OUR APPROACH).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | dynamics, model, predicts, temporal, evolution, Gaussian, Splatting, representation, input, action, Problem, Formulation, Given, multi-view | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | dynamics, model, predicts, temporal, evolution, Gaussian, Splatting, representation, input, action | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | form, node, features, GNN, consists, encoder, fenc, representation, Then, have | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | optimization, process, aims, acquire, sequence, actions, minimize, cost, function, Ztarget | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / III. PRELIMINARIES - extractive body cue:** (b) The dynamics model f predicts the temporal evolution of the Gaussian Splatting representation Zt with input action ut.
- **p. 3 / IV. OUR APPROACH - extractive body cue:** Problem Formulation Given multi-view RGBD observations Otarget = {ov,mv}N v=1 of the target pattern of the granular material, where ov represents the RGBD image and ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Second, accounting for all particles in planning requires a high-dimensional state [10], [11], which creates challenges for downstream policy learning or planning algorithms.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Our method takes a few multi-view images of a scene and their corresponding camera poses as input, and (a) converts them into their Gaussian splatting ...
- **p. 2 / III. PRELIMINARIES - extractive body cue:** Gaussian splatting [4] has emerged as a powerful rendering technique that can capture the state of the visual world with a discrete set of 3D ...
- **p. 4 / IV. OUR APPROACH - extractive body cue:** 1) and we execute the optimized action sequence in a closed-loop fashion.
- **p. 4 / IV. OUR APPROACH - extractive body cue:** After the first action in the sequence is executed by the robot, we re-run the planning algorithm to generate a new action sequence.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | We directly Algorithm 1: Our Visual MPC Planning Algorithm Data: Current observation Ot, target Otarget, planning horizon T, the dynamics model f, ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | Both of the rollout results show that the dynamics model prediction is accurate for a few steps. • NFD[29] uses a fully ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | We directly Algorithm 1: Our Visual MPC Planning Algorithm Data: Current observation Ot, target Otarget, planning horizon T, the dynamics model f, ... | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / IV. OUR APPROACH - extractive body cue:** In the end, we obtain a set of Gaussians that represents the next image: ˆZt+1 = {(ci t,αi t , ˆR i t+1, ˆgi t+1,si ...
- **p. 5 / V. EXPERIMENTAL RESULTS - extractive body cue:** Both of the rollout results show that the dynamics model prediction is accurate for a few steps. • NFD[29] uses a fully convolutional neural network ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** form, node, features, GNN, consists, encoder, fenc, representation, Then, have, message-passing, fmsg, allows, multi-step, message, passing, mean, Niqj, where, nodes.
- **Relevant PDF headings:** IV. OUR APPROACH (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | (b) The granular materials used in real-world experiments include coffee beans, peanuts, pistachios, and almonds. transfer our model trained in the simulation ... | p. 4 (V. EXPERIMENTAL RESULTS), p. 5 (V. EXPERIMENTAL RESULTS) |
| Semantic / temporal fusion | Manipulation Results TABLE I MANIPULATION SUCCESS RATE IN SIMULATION (MAX = 1.0) Collection Splitting Redistributing NeRF-dy [38] 0.67 0.43 0.31 Dyn-Res [16] ... | p. 5 (V. EXPERIMENTAL RESULTS), p. 6 (V. EXPERIMENTAL RESULTS) |
| Robot query / planning handoff | Manipulation Results TABLE I MANIPULATION SUCCESS RATE IN SIMULATION (MAX = 1.0) Collection Splitting Redistributing NeRF-dy [38] 0.67 0.43 0.31 Dyn-Res [16] ... | p. 5 (V. EXPERIMENTAL RESULTS), p. 5 (V. EXPERIMENTAL RESULTS) |

## Failure and Ablation Link

- **p. 5 / V. EXPERIMENTAL RESULTS - extractive body cue:** Generalization Studies In this section, we conduct ablation studies to evaluate the effectiveness of each component.
- **p. 5 / V. EXPERIMENTAL RESULTS - extractive body cue:** This approach leverages the spatial locality of inter-object interactions and translation equivariance through convolutional operations. • NeRF-dy [38] leverages NeRF to learn viewpointinvariant and 3D-aware ...
- **p. 6 / VI. LIMITATIONS - extractive body cue:** This limitation stems from the difficulty in accurately reconstructing such tiny particles using Gaussian splatting, which struggles to maintain precision at smaller scales.
- **p. 6 / VII. CONCLUSION - extractive body cue:** Future work could extend this framework to other non-rigid materials, further enhancing the capabilities of robotic systems in dynamic tasks.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (IV. OUR APPROACH), p. 3 (IV. OUR APPROACH), p. 4 (IV. OUR APPROACH), p. 4 (IV. OUR APPROACH), objective p. 3 (IV. OUR APPROACH), p. 4 (IV. OUR APPROACH), p. 3 (IV. OUR APPROACH), p. 4 (IV. OUR APPROACH), temporal p. 4 (V. EXPERIMENTAL RESULTS), p. 5 (V. EXPERIMENTAL RESULTS), p. 4 (V. EXPERIMENTAL RESULTS), p. 5 (V. EXPERIMENTAL RESULTS), p. 6 (V. EXPERIMENTAL RESULTS), p. 6 (V. EXPERIMENTAL RESULTS).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (7 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** The trajectory optimization problem over a horizon T can be defined as follows: u0:T-1 = argminu0:T-1c(ZT,Ztarget) (6) Z0 = h(O0), Ztarget = h(Otarget), Zt+1 = f(Zt,ut) (7) where h is ... (p. 3, IV. OUR APPROACH).
- **Objective/update evidence:** We perform the optimization shown in Equation 6 as part of a gradient-based MPC loop (as shown in Alg. (p. 4, IV. OUR APPROACH).
- **Temporal/runtime evidence:** We directly Algorithm 1: Our Visual MPC Planning Algorithm Data: Current observation Ot, target Otarget, planning horizon T, the dynamics model f, Number of sampled action sequence K and gradient ... (p. 4, V. EXPERIMENTAL RESULTS).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
