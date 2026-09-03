# Method - Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2304.13705; PDF retrieval source: https://arxiv.org/pdf/2304.13705. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 5 (IV. ACTION CHUNKING WITH TRANSFORMERS), p. 6 (IV. ACTION CHUNKING WITH TRANSFORMERS), p. 5 (IV. ACTION CHUNKING WITH TRANSFORMERS), p. 4 (IV. ACTION CHUNKING WITH TRANSFORMERS), p. 6 (IV. ACTION CHUNKING WITH TRANSFORMERS), p. 4 (IV. ACTION CHUNKING WITH TRANSFORMERS)): We use ResNet image encoders, a transformer encoder, and a transformer decoder to implement the CVAE decoder.

## Method Body Digest

- **p. 5 / IV. ACTION CHUNKING WITH TRANSFORMERS - extractive body cue:** We use ResNet image encoders, a transformer encoder, and a transformer decoder to implement the CVAE decoder.
- **p. 6 / IV. ACTION CHUNKING WITH TRANSFORMERS - extractive body cue:** We use L1 loss for reconstruction instead of the more common L2 loss: we noted that L1 loss leads to more precise modeling of the ...
- **p. 5 / IV. ACTION CHUNKING WITH TRANSFORMERS - extractive body cue:** The whole model is trained to maximize the log-likelihood of demonstration action chunks, i.e. minθ -P st,at:t+k∈D log πθ(at:t+k/st), with the standard VAE objective which ...
- **p. 4 / IV. ACTION CHUNKING WITH TRANSFORMERS - extractive body cue:** We first summarize the pipeline of training ACT, then dive into each of the design choices.
- **p. 6 / IV. ACTION CHUNKING WITH TRANSFORMERS - extractive body cue:** The transformer decoder conditions on the encoder output through cross-attention, where the input sequence is a fixed position embedding, with dimensions k × 512, and ...
- **p. 4 / IV. ACTION CHUNKING WITH TRANSFORMERS - extractive body cue:** We therefore develop a novel algorithm, Action Chunking with Transformers (ACT), to leverage the data collected by ALOHA.
- **p. 4 / IV. ACTION CHUNKING WITH TRANSFORMERS - extractive body cue:** At test time, we load the policy that achieves the lowest validation loss and roll it out in the environment.
- **p. 5 / IV. ACTION CHUNKING WITH TRANSFORMERS - extractive body cue:** This procedure also incurs no additional training cost, only extra inference-time computation.

## Design Rationale

- **p. 2 / I. INTRODUCTION - extractive body cue:** The key contribution of this paper is a low-cost system for learning fine manipulation, comprising a teleoperation system and a novel imitation learning algorithm.
- **p. 2 / I. INTRODUCTION - extractive body cue:** To further improve the smoothness of the policy, we propose temporal ensembling, which queries the policy more frequently and averages across the overlapping action chunks.
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this work, we seek to develop a low-cost system for fine manipulation that is, in contrast, accessible and reproducible.

## Source Evidence Cues

- **p. 5 / IV. ACTION CHUNKING WITH TRANSFORMERS - extractive body cue:** We use ResNet image encoders, a transformer encoder, and a transformer decoder to implement the CVAE decoder.
- **p. 6 / IV. ACTION CHUNKING WITH TRANSFORMERS - extractive body cue:** We use L1 loss for reconstruction instead of the more common L2 loss: we noted that L1 loss leads to more precise modeling of the ...
- **p. 5 / IV. ACTION CHUNKING WITH TRANSFORMERS - extractive body cue:** The whole model is trained to maximize the log-likelihood of demonstration action chunks, i.e. minθ -P st,at:t+k∈D log πθ(at:t+k/st), with the standard VAE objective which ...
- **p. 4 / IV. ACTION CHUNKING WITH TRANSFORMERS - extractive body cue:** We first summarize the pipeline of training ACT, then dive into each of the design choices.
- **p. 6 / IV. ACTION CHUNKING WITH TRANSFORMERS - extractive body cue:** The transformer decoder conditions on the encoder output through cross-attention, where the input sequence is a fixed position embedding, with dimensions k × 512, and ...
- **p. 4 / IV. ACTION CHUNKING WITH TRANSFORMERS - extractive body cue:** We therefore develop a novel algorithm, Action Chunking with Transformers (ACT), to leverage the data collected by ALOHA.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / affordance state | object와 contact-relevant scene을 표현한다 | RGB-D, point cloud, object/task observation | pose, affordance, grasp/contact graph 또는 SE(3) descriptor를 구성 | object/contact state | We use ResNet image encoders, a transformer encoder, and a transformer decoder to implement the CVAE decoder. | p. 5 (IV. ACTION CHUNKING WITH TRANSFORMERS), p. 6 (IV. ACTION CHUNKING WITH TRANSFORMERS) |
| Grasp / trajectory generation | goal을 feasible manipulation candidate로 바꾼다 | geometry/contact state와 task goal | grasp sampling, pose planning, trajectory optimization 또는 policy decoding을 적용 | grasp, pose, force 또는 trajectory | We use L1 loss for reconstruction instead of the more common L2 loss: we noted that L1 loss leads to more precise ... | p. 6 (IV. ACTION CHUNKING WITH TRANSFORMERS), p. 5 (IV. ACTION CHUNKING WITH TRANSFORMERS) |
| Contact execution / correction | interaction outcome으로 action을 닫힌 loop로 수정한다 | candidate와 visual/force/tactile feedback | tracking, regrasp, correction, termination 또는 recovery를 수행 | next action/task state | The whole model is trained to maximize the log-likelihood of demonstration action chunks, i.e. minθ -P st,at:t+k∈D log πθ(at:t+k/st), with the standard ... | p. 5 (IV. ACTION CHUNKING WITH TRANSFORMERS), p. 4 (IV. ACTION CHUNKING WITH TRANSFORMERS) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / IV. ACTION CHUNKING WITH TRANSFORMERS - extractive body cue:** The whole model is trained to maximize the log-likelihood of demonstration action chunks, i.e. minθ -P st,at:t+k∈D log πθ(at:t+k/st), with the standard VAE objective which ...
- **p. 4 / IV. ACTION CHUNKING WITH TRANSFORMERS - extractive body cue:** At test time, we load the policy that achieves the lowest validation loss and roll it out in the environment.
- **p. 5 / IV. ACTION CHUNKING WITH TRANSFORMERS - extractive body cue:** This procedure also incurs no additional training cost, only extra inference-time computation.
- **p. 6 / IV. ACTION CHUNKING WITH TRANSFORMERS - extractive body cue:** We use L1 loss for reconstruction instead of the more common L2 loss: we noted that L1 loss leads to more precise modeling of the ...
- **Formal bridge:** object geometry/contact state -> grasp/pose/force/trajectory -> task/contact/pose objective -> completion, contact success and robustness.
- **Equation/algorithm anchors:** p. 5 (IV. ACTION CHUNKING WITH TRANSFORMERS), p. 4 (IV. ACTION CHUNKING WITH TRANSFORMERS), p. 5 (IV. ACTION CHUNKING WITH TRANSFORMERS), p. 6 (IV. ACTION CHUNKING WITH TRANSFORMERS).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Thus, action, chunking, policy, outputs, tensor, given, current, observation, CVAE, decoder, takes, observations, input | RGB-D/point cloud, object state와 contact/task observation | body cue; exact tensor/frame verify |
| State/latent | Thus, action, chunking, policy, outputs, tensor, given, current, observation, CVAE | object geometry, affordance, contact mode 또는 end-effector state | body cue; notation verify |
| Action/output | contribution, low-cost, system, learning, fine, manipulation, comprising, teleoperation, novel, imitation | grasp, pose, force 또는 end-effector trajectory | body cue; unit/decoder verify |
| Objective/constraint | whole, model, trained, maximize, log-likelihood, demonstration, action, chunks, k/st, standard | task/contact/pose objective | equation anchor required |

## Observation–State–Action Interface

- **p. 5 / IV. ACTION CHUNKING WITH TRANSFORMERS - extractive body cue:** Thus with action chunking, the policy outputs a k × 14 tensor given the current observation.
- **p. 5 / IV. ACTION CHUNKING WITH TRANSFORMERS - extractive body cue:** The CVAE decoder (i.e. the policy) takes the current observations and z as the input, and predicts the next k actions (Figure 4 right).
- **p. 1 / I. INTRODUCTION - extractive body cue:** In our system, we therefore train an end-to-end policy that directly maps RGB images from commodity web cameras to the actions.
- **p. 2 / I. INTRODUCTION - extractive body cue:** To further improve the smoothness of the policy, we propose temporal ensembling, which queries the policy more frequently and averages across the overlapping action chunks.
- **p. 1 / I. INTRODUCTION - extractive body cue:** This pixel-to-action formulation is particularly suitable for fine manipulation, because fine manipulation often involves objects with complex physical properties, such that learning the manipulation policy ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Small errors in the predicted action can incur large differences in the state, exacerbating the "compounding error" problem of imitation learning [47, 64, 29].
- **p. 4 / IV. ACTION CHUNKING WITH TRANSFORMERS - extractive body cue:** Next, we train ACT to predict the sequence of future actions given the current observations.
- **Normalized interface:** observation=RGB-D/point cloud, object state와 contact/task observation; state=object geometry, affordance, contact mode 또는 end-effector state; output/action=grasp, pose, force 또는 end-effector trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | grasp/pose proposal에서 contact episode까지의 task horizon; trajectory chunk 여부 확인 필요. | Each episode takes 8-14 seconds for the human operator to perform depending on the complexity of the task, which translates to 400-700 ... | episode/sequence/action-chunk boundary |
| Rate / latency | perception/planning rate와 low-level contact control rate가 분리된다. | Action Chunking and Temporal Ensemble To combat the compounding errors of imitation learning in a way that is compatible with pixel-to-action policies ... | Hz/fps, inference time and control rate |
| Memory | object/contact state, current pose와 tactile/force history; exact window 확인 필요. | 3: for timestep t = 1, 2, ...T do 4: Predict ˆat:t+k with πθ(ˆat:t+k/ot, z) where z = 0 5: Add ˆat:t+k ... | window and reset |
| Compute | point/pose encoding, candidate sampling/optimization과 collision/contact checking이 결정한다. | Each episode takes 8-14 seconds for the human operator to perform depending on the complexity of the task, which translates to 400-700 ... | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / IV. ACTION CHUNKING WITH TRANSFORMERS - extractive body cue:** The whole model is trained to maximize the log-likelihood of demonstration action chunks, i.e. minθ -P st,at:t+k∈D log πθ(at:t+k/st), with the standard VAE objective which ...
- **p. 4 / IV. ACTION CHUNKING WITH TRANSFORMERS - extractive body cue:** We first summarize the pipeline of training ACT, then dive into each of the design choices.
- **p. 6 / IV. ACTION CHUNKING WITH TRANSFORMERS - extractive body cue:** The training takes around 5 hours on a single 11G RTX 2080 Ti GPU, and the inference time is around 0.01 seconds on the same ...
- **p. 8 / V. EXPERIMENTS - extractive body cue:** For the real-world tasks, we report training with human data, with 1 seed and 25 evaluations.
- **p. 8 / V. EXPERIMENTS - extractive body cue:** For the two simulated tasks, we report [training with scripted data / training with human data], with 3 seeds and 50 policy evaluations each.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** ResNet, image, encoders, transformer, encoder, decoder, implement, CVAE, loss, reconstruction, instead, more, common, noted, leads, precise, modeling, action, sequence, whole.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / affordance state | For all 8 tasks, the initial placement of the objects is either varied randomly along the 15cm white reference line (real-world tasks), ... | p. 6 (V. EXPERIMENTS), p. 8 (V. EXPERIMENTS) |
| Grasp / trajectory generation | ACT achieves the highest success rate compared to all prior methods, outperforming the second best algorithm by a large margin on each ... | p. 9 (V. EXPERIMENTS), p. 8 (V. EXPERIMENTS) |
| Contact execution / correction | ACT achieves the highest success rate compared to all prior methods, outperforming the second best algorithm by a large margin on each ... | p. 9 (V. EXPERIMENTS), p. 10 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 9 / V. EXPERIMENTS - extractive body cue:** Our ablations in Subsection VI-A also shows that chunking can significantly improve these prior methods when incorporated.
- **p. 10 / Figure/Table caption - extractive body cue:** Fig. 8: (a) We augment two baselines with action chunking, with different values of chunk size k on the x-axis, and success rate on the ...
- **p. 9 / V. EXPERIMENTS - extractive body cue:** The visual feature extractor is a pretrained ResNet finetuned on demonstration data with unsupervised learning.
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: ALOHA : A Low-cost Open-source Hardware System for Bimanual Teleoperation. The whole system costs <$20k with off-the-shelf robots and 3D printed components. Left: ...
- **p. 6 / V. EXPERIMENTS - extractive body cue:** Due to the small clearance between the cube and the left gripper (around 1cm), small errors could result in collisions and task failure.
- **p. 9 / V. EXPERIMENTS - extractive body cue:** The failure modes we observe are 1) at stage 2, the right arm closes its gripper too early and fails to grasp the tail of ...
- **p. 6 / V. EXPERIMENTS - extractive body cue:** Because of the cup's small size, the grippers cannot grasp the body of the cup by just approaching it from the side.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 5 (IV. ACTION CHUNKING WITH TRANSFORMERS), p. 6 (IV. ACTION CHUNKING WITH TRANSFORMERS), p. 5 (IV. ACTION CHUNKING WITH TRANSFORMERS), p. 4 (IV. ACTION CHUNKING WITH TRANSFORMERS), p. 6 (IV. ACTION CHUNKING WITH TRANSFORMERS), p. 4 (IV. ACTION CHUNKING WITH TRANSFORMERS), objective p. 5 (IV. ACTION CHUNKING WITH TRANSFORMERS), p. 4 (IV. ACTION CHUNKING WITH TRANSFORMERS), p. 5 (IV. ACTION CHUNKING WITH TRANSFORMERS), p. 6 (IV. ACTION CHUNKING WITH TRANSFORMERS), temporal p. 8 (V. EXPERIMENTS), p. 4 (IV. ACTION CHUNKING WITH TRANSFORMERS), p. 5 (IV. ACTION CHUNKING WITH TRANSFORMERS), p. 2 (I. INTRODUCTION), p. 2 (II. RELATED WORK), p. 8 (V. EXPERIMENTS).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (18 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** The transformer decoder conditions on the encoder output through cross-attention, where the input sequence is a fixed position embedding, with dimensions k × 512, and the keys and values are ... (p. 6, IV. ACTION CHUNKING WITH TRANSFORMERS).
- **Objective/update evidence:** The whole model is trained to maximize the log-likelihood of demonstration action chunks, i.e. minθ -P st,at:t+k∈D log πθ(at:t+k/st), with the standard VAE objective which has two terms: a reconstruction ... (p. 5, IV. ACTION CHUNKING WITH TRANSFORMERS).
- **Temporal/runtime evidence:** Each episode takes 8-14 seconds for the human operator to perform depending on the complexity of the task, which translates to 400-700 time steps given the control frequency of 50Hz. (p. 8, V. EXPERIMENTS).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
