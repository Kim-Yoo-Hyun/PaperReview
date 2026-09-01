# Method - Act the Part: Learning Interaction Strategies for Articulated Object Part Discovery

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (16 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2105.01047; PDF retrieval source: https://arxiv.org/pdf/2105.01047. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 4 (3.2. Learning to Act to Discover Parts), p. 2 (3. Approach), p. 4 (3.5. Reward), p. 3 (3.2. Learning to Act to Discover Parts), p. 3 (3.1. Problem Formulation), p. 2 (3. Approach)): Mask 𝑀!"# Part Network Mask Decoder Mask Decoder ResNet18 Image Observation Action Applied Figure 4.

## Method Body Digest

- **p. 4 / 3.2. Learning to Act to Discover Parts - extractive body cue:** Mask 𝑀!"# Part Network Mask Decoder Mask Decoder ResNet18 Image Observation Action Applied Figure 4.
- **p. 2 / 3. Approach - extractive body cue:** We then explain the three components of our approach: an interaction network (Sec.
- **p. 4 / 3.5. Reward - extractive body cue:** At inference, we first predict and execute an action.
- **p. 3 / 3.2. Learning to Act to Discover Parts - extractive body cue:** 3, we use a shared ResNet18 [16] with two residual decoder heads wired with U-Net [39] skip connections.
- **p. 3 / 3.1. Problem Formulation - extractive body cue:** To enable large-scale training and ground truth part segmentation (for benchmarking only), we use a simulated environment.
- **p. 2 / 3. Approach - extractive body cue:** 3.2) to determine what actions to take, a part network (Sec.
- **p. 4 / 3.2. Learning to Act to Discover Parts - extractive body cue:** We use pixel-wise binary cross entropy loss to supervise the hold and push reward maps.
- **p. 3 / 3.1. Problem Formulation - extractive body cue:** First, a hold action parameterized by its location and implemented as a fixed point constraint between the gripper and a part.

## Design Rationale

- **p. 1 / 1. Introduction - extractive body cue:** To address these challenges, we introduce Act the Part arXiv:2105.01047v1 [cs.CV] 3 May 2021
- **p. 2 / 1. Introduction - extractive body cue:** (2) Our method generalizes to unseen object instances and categories with different numbers of parts and joints.
- **p. 4 / 3.4. History Aggregation - extractive body cue:** We introduce a history aggregation algorithm to updated part memory V , based on predicted Mt and Mt+1.

## Source Evidence Cues

- **p. 4 / 3.2. Learning to Act to Discover Parts - extractive body cue:** Mask 𝑀!"# Part Network Mask Decoder Mask Decoder ResNet18 Image Observation Action Applied Figure 4.
- **p. 2 / 3. Approach - extractive body cue:** We then explain the three components of our approach: an interaction network (Sec.
- **p. 4 / 3.5. Reward - extractive body cue:** At inference, we first predict and execute an action.
- **p. 3 / 3.2. Learning to Act to Discover Parts - extractive body cue:** 3, we use a shared ResNet18 [16] with two residual decoder heads wired with U-Net [39] skip connections.
- **p. 3 / 3.1. Problem Formulation - extractive body cue:** To enable large-scale training and ground truth part segmentation (for benchmarking only), we use a simulated environment.
- **p. 2 / 3. Approach - extractive body cue:** 3.2) to determine what actions to take, a part network (Sec.
- **Detected method headings:** 3. Approach (p. 2)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | Mask 𝑀!"# Part Network Mask Decoder Mask Decoder ResNet18 Image Observation Action Applied Figure 4. | p. 4 (3.2. Learning to Act to Discover Parts), p. 2 (3. Approach) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | We then explain the three components of our approach: an interaction network (Sec. | p. 2 (3. Approach), p. 4 (3.5. Reward) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | At inference, we first predict and execute an action. | p. 4 (3.5. Reward), p. 3 (3.2. Learning to Act to Discover Parts) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 3.2. Learning to Act to Discover Parts - extractive body cue:** We use pixel-wise binary cross entropy loss to supervise the hold and push reward maps.
- **p. 3 / 3.1. Problem Formulation - extractive body cue:** First, a hold action parameterized by its location and implemented as a fixed point constraint between the gripper and a part.
- **p. 4 / 3.3. Learning to Discover Parts from Action - extractive body cue:** We supervise predictions using binary cross-entropy loss.
- **p. 2 / 3. Approach - extractive body cue:** Finally, we explain the reward formulation (Sec.
- **p. 3 / 3.2. Learning to Act to Discover Parts - extractive body cue:** The action space directly motivates network and reward design.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 3 (3.1. Problem Formulation), p. 4 (3.3. Learning to Discover Parts from Action), p. 4 (3.2. Learning to Act to Discover Parts), p. 3 (3.1. Problem Formulation).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Given, sequence, observations, sensor, readings, actions, goal, infer, part, mask, where, pixel, assigned, value | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | Given, sequence, observations, sensor, readings, actions, goal, infer, part, mask | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | address, challenges, introduce, Act, Part, arXiv, generalizes, unseen, object, instances | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | pixel-wise, binary, cross, entropy, loss, supervise, hold, push, reward, maps | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 3.1. Problem Formulation - extractive body cue:** Given the sequence of T observations, sensor readings, and actions, the goal is to infer part mask MT ∈{1, 2, ..., N +1}H×W , where ...
- **p. 3 / 3.1. Problem Formulation - extractive body cue:** (a) The interaction network computes hold and push from an image observation and current part memory.
- **p. 4 / 3.2. Learning to Act to Discover Parts - extractive body cue:** Mask 𝑀!"# Part Network Mask Decoder Mask Decoder ResNet18 Image Observation Action Applied Figure 4.
- **p. 2 / 3.1. Problem Formulation - extractive body cue:** At each timestep t, an agent gets an observation It ∈RH×W ×C, and executes an action at ∈A on an object o ∈O, where A ...
- **p. 2 / 1. Introduction - extractive body cue:** Given an RGB input image and the part segmentation belief, our interaction network reasons about where to hold and push to move undiscovered parts.
- **p. 4 / 3.3. Learning to Discover Parts from Action - extractive body cue:** 4) takes the observations before and after the interaction.
- **p. 1 / 1. Introduction - extractive body cue:** Our work, Act the Part, learns interaction strategies that expose parts and generalize to unseen categories. that objects are fixed to a ground plane [28].
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | 2, we consider metrics after the fifth timestep. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | We compute the average of perceptual metrics for each category at every timestep over five models trained with different random seeds. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | A next frame image is sent back to the model, at which point it runs the part network, history aggregation, and another ... | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / 3.5. Reward - extractive body cue:** At inference, we first predict and execute an action.
- **p. 3 / 3.1. Problem Formulation - extractive body cue:** To enable large-scale training and ground truth part segmentation (for benchmarking only), we use a simulated environment.
- **p. 5 / 4.1. Metrics and Points of Comparison - extractive body cue:** We compute the average of perceptual metrics for each category at every timestep over five models trained with different random seeds.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Mask, Part, Network, Decoder, ResNet18, Image, Observation, Action, Applied, Figure, then, explain, three, components, interaction, Sec, inference, first, predict, execute.
- **Relevant PDF headings:** 3. Approach (p. 2).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | Dataset, test initialization, and pre-trained models will be released for reproducibility and benchmarking. | p. 5 (4. Evaluation), p. 8 (4.3. Real World Results) |
| Semantic / temporal fusion | Results on two unseen object categories show our methods (pink and brown) approach the oracle baseline over time. | p. 7 (4.2. Benchmark Results), p. 5 (4.1. Metrics and Points of Comparison) |
| Robot query / planning handoff | While other algorithms' performance saturate quickly with one or two interactions, [Ours-Touch] and [Ours-NoTouch] are able to improve with more interactions. | p. 5 (4.2. Benchmark Results), p. 7 (4.2. Benchmark Results) |

## Failure and Ablation Link

- **p. 8 / 4.3. Real World Results - extractive body cue:** Without any fine-tuning, the algorithm shows promising results on inferring interaction strategies and reasoning about the observed motion for part discovery.
- **p. 7 / 4.2. Benchmark Results - extractive body cue:** In this experiment, we want to evaluate the effect of touch feedback.
- **p. 5 / 4.1. Metrics and Points of Comparison - extractive body cue:** To provide a better metric for these structures, we measure dH95, which is a part-aware variant of a common metric in medical image segmentation [8].
- **p. 5 / 4.1. Metrics and Points of Comparison - extractive body cue:** We compare the AtP framework trained with and without touch reward, [Ours-Touch] and [Ours-NoTouch] respectively, with the following alternative approaches to study the efficacy of ...
- **p. 7 / 4.2. Benchmark Results - extractive body cue:** However, we are still able to learn helpful interaction strategies even without touch.
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 3. Interaction network. Given an image and the current belief of part segmentation, our network predicts a hold and a push conditioned on the ...
- **p. 12 / Figure/Table caption - extractive body cue:** Table 4. Act-NoHold Reward. Reward cases related to holding are removed. Optical Flow Touch Sensor Hold Reward Push Reward x 1/0

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 4 (3.2. Learning to Act to Discover Parts), p. 2 (3. Approach), p. 4 (3.5. Reward), p. 3 (3.2. Learning to Act to Discover Parts), p. 3 (3.1. Problem Formulation), p. 2 (3. Approach), objective p. 4 (3.2. Learning to Act to Discover Parts), p. 3 (3.1. Problem Formulation), p. 4 (3.3. Learning to Discover Parts from Action), p. 2 (3. Approach), p. 3 (3.2. Learning to Act to Discover Parts), temporal p. 5 (4.1. Metrics and Points of Comparison), p. 5 (4.1. Metrics and Points of Comparison), p. 8 (4.3. Real World Results), p. 3 (3.2. Learning to Act to Discover Parts), p. 4 (3.5. Reward), p. 1 (1. Introduction).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
