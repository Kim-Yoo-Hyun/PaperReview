# Method - GravMAD: Grounded Spatial Value Maps Guided Action Diffusion for Generalized 3D Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (33 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.iclr.cc/paper_files/paper/2025/hash/fce176458ff542940fa3ed16e6f9c852-Abstract-Conference.html; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/114266. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> DOC-QA1 (2026-10-23): 제어문자·깨진 추출 구간과 직접 연결된 표 항목을 PDF 페이지 이미지와 대조했다. 확인 범위·원문 URL·페이지·수정 이력은 [대조 기록](../../../work/sources/pdf_note_review_2026-10-23.json)에 있다. 노트 전체의 정독이나 모든 기존 주장에 대한 재검증을 뜻하지 않으며 reading status는 유지한다.

## Method in One Sentence

- **원문 대조:** 세 번째 prediction head는 gripper의 open/close 상태를 예측하며 ground-truth openness에 대한 binary cross-entropy로 학습한다. Position·rotation noise head의 L1 loss 및 subgoal auxiliary head와 구분된다. ([PDF p. 7](https://arxiv.org/pdf/2409.20154#page=7), §3, Eq. (3)).

## Method Body Digest

- **원문 대조:** 세 번째 prediction head는 gripper의 open/close 상태를 예측하며 ground-truth openness에 대한 binary cross-entropy로 학습한다. Position·rotation noise head의 L1 loss 및 subgoal auxiliary head와 구분된다. ([PDF p. 7](https://arxiv.org/pdf/2409.20154#page=7), §3, Eq. (3)).
- **p. 7 / 3 METHOD - extractive body cue:** A self-attention layer then refines this representation to produce end-effector contextual features.
- **p. 18 / A.4 DETAIL OF MODEL ARCHITECTURE AND HYPER-PARAMETERS FOR GRAVMAD - extractive body cue:** First, the visual input is processed by a 2D Visual Encoder, transforming image data into feature representations.
- **p. 18 / A.4 DETAIL OF MODEL ARCHITECTURE AND HYPER-PARAMETERS FOR GRAVMAD - extractive body cue:** These 2D features are then passed through a 3D lifting module, converting them into 3D representations using depth information.
- **p. 6 / 3 METHOD - extractive body cue:** During the inference phase, we use pre-trained foundation models to synthesize GravMaps.
- **p. 5 / 3 METHOD - extractive body cue:** Our model progressively predicts the next keypose based on current observations and uses a sampling-based motion planner (Klemm et al., 2015) to plan the trajectory ...
- **p. 6 / 3 METHOD - extractive body cue:** GravMaps m are then downsampled using farthest point sampling (FPS) and encoded into token tm with the DP3 (Ze et al., 2024) encoder, a lightweight ...
- **p. 7 / 3 METHOD - extractive body cue:** The loss maximizes similarity between positive pairs and minimizes it between negative pairs: Lcon = -1 N N X i=1 log exp(fgi · fg + ...

## Design Rationale

- **p. 3 / 1 INTRODUCTION - extractive body cue:** In summary, our contributions are: 1) We propose leveraging key sub-goals in 3D manipulation tasks to bridge the gap between foundation models and learned policies.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To this end, inspired by the approach of introducing task sub-goals to achieve efficient execution in robotic manipulation (Black et al., 2024; Kang et al., ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** 3) We propose a new action diffusion framework, GravMAD, guided by GravMaps.

## Source Evidence Cues

- **원문 대조:** 세 번째 prediction head는 gripper의 open/close 상태를 예측하며 ground-truth openness에 대한 binary cross-entropy로 학습한다. Position·rotation noise head의 L1 loss 및 subgoal auxiliary head와 구분된다. ([PDF p. 7](https://arxiv.org/pdf/2409.20154#page=7), §3, Eq. (3)).
- **p. 7 / 3 METHOD - extractive body cue:** A self-attention layer then refines this representation to produce end-effector contextual features.
- **p. 18 / A.4 DETAIL OF MODEL ARCHITECTURE AND HYPER-PARAMETERS FOR GRAVMAD - extractive body cue:** First, the visual input is processed by a 2D Visual Encoder, transforming image data into feature representations.
- **p. 18 / A.4 DETAIL OF MODEL ARCHITECTURE AND HYPER-PARAMETERS FOR GRAVMAD - extractive body cue:** These 2D features are then passed through a 3D lifting module, converting them into 3D representations using depth information.
- **p. 6 / 3 METHOD - extractive body cue:** During the inference phase, we use pre-trained foundation models to synthesize GravMaps.
- **p. 5 / 3 METHOD - extractive body cue:** Our model progressively predicts the next keypose based on current observations and uses a sampling-based motion planner (Klemm et al., 2015) to plan the trajectory ...
- **p. 6 / 3 METHOD - extractive body cue:** GravMaps m are then downsampled using farthest point sampling (FPS) and encoded into token tm with the DP3 (Ze et al., 2024) encoder, a lightweight ...
- **Detected method headings:** 3 METHOD (p. 4); A.4 DETAIL OF MODEL ARCHITECTURE AND HYPER-PARAMETERS FOR GRAVMAD (p. 18); A.5 COMPARISON BETWEEN GRAVMAD AND OTHER BASELINE MODELS (p. 18)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | The third prediction head is used to predict the gripper's open/close state, and we use binary crossentropy (BCE) loss for supervision: Lopen ... | p. 7 (3 METHOD), p. 7 (3 METHOD) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | A self-attention layer then refines this representation to produce end-effector contextual features. | p. 7 (3 METHOD), p. 18 (A.4 DETAIL OF MODEL ARCHITECTURE AND HYPER-PARAMETERS FOR GRAVMAD) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | First, the visual input is processed by a 2D Visual Encoder, transforming image data into feature representations. | p. 18 (A.4 DETAIL OF MODEL ARCHITECTURE AND HYPER-PARAMETERS FOR GRAVMAD), p. 18 (A.4 DETAIL OF MODEL ARCHITECTURE AND HYPER-PARAMETERS FOR GRAVMAD) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 7 / 3 METHOD - extractive body cue:** The loss maximizes similarity between positive pairs and minimizes it between negative pairs: Lcon = -1 N N X i=1 log exp(fgi · fg + ...
- **p. 7 / 3 METHOD - extractive body cue:** At this stage, the training objective of GravMAD can be formulated by combining the losses from Eq.2, 3, 4, and 5 as follows: LGravMAD = ...
- **p. 5 / 3 METHOD - extractive body cue:** To address potential discontinuities from quaternion constraints and ensure smooth optimization, we utilize the 6D rotation representation (Ke et al., 2024).
- **p. 5 / 3 METHOD - extractive body cue:** Each GravMap m contains two voxel maps: (1) a spatial cost map mc, with lower values near the sub-goal and higher costs further away, and ...
- **p. 6 / 3 METHOD - extractive body cue:** The function SK can incorporate multiple constraints.
- **p. 6 / 3 METHOD - extractive body cue:** In our paper, we define two constraints for SK, depending on the type of manipulation task, as shown in Fig.
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 7 (3 METHOD), p. 5 (3 METHOD), p. 6 (3 METHOD), p. 6 (3 METHOD), p. 7 (3 METHOD).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | goal, learn, policy, maps, observations, sub-goals, instructions, actions, keypose, corresponding, observation-action, pair, oKip, aKip | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | goal, learn, policy, maps, observations, sub-goals, instructions, actions, keypose, corresponding | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | summary, contributions, leveraging, sub-goals, manipulation, tasks, bridge, between, foundation, models | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | loss, maximizes, similarity, between, positive, pairs, minimizes, negative, Lcon, fgj/T | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 5 / 3 METHOD - extractive body cue:** Our goal is to learn a policy π : (O, L, G) 7→A, which maps observations ot, sub-goals gt, and instructions ℓto actions at.
- **p. 6 / 3 METHOD - extractive body cue:** For each keypose, the corresponding observation-action pair (oKip, aKip) is passed to the function SK, which outputs a Boolean value to determine whether the given ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** By designing various learning frameworks, such as incorporating different 3D representations (Shridhar et al., 2023; Chen et al., 2023a; Goyal et al., 2023), policy representations ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** (a) Imitation learning-based methods learn end-to-end policies that map language and 3D observations to actions for precise manipulation.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** This enables the robot to utilize 3D visual observations, task language instructions, and GravMaps guidance to denoise random noise into precise end-effector poses.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** In the inference phase, pre-trained foundation models are leveraged to interpret the robot's 3D visual observations and task language instructions, directly identifying task sub-goals.
- **p. 4 / 1 INTRODUCTION - extractive body cue:** During inference, the Detector, Planner, and Composer pipeline interprets visual observations and language instructions to derive gpos and gopen, which are processed into a GravMap ...
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | During testing, except for the novel task "push buttons light", which must be completed in 3 time steps, all other tasks must ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | The implementation of the Sub-goal Keypose Discovery algorithm starts with a set of pre-computed keyposes, which are frames selected from the demonstration ... | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not recovered | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | For each base task, we collect 20 demonstrations for training and evaluate the final checkpoints using 3 random seeds over 25 episodes. | hardware, batch and throughput |

## Training vs Inference

- **p. 6 / 3 METHOD - extractive body cue:** During the inference phase, we use pre-trained foundation models to synthesize GravMaps.
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** All models complete 600k training iterations on an NVIDIA RTX4090 GPU, with the final checkpoint selected using three random seeds for evaluation.
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** For each base task, we collect 20 demonstrations for training and evaluate the final checkpoints using 3 random seeds over 25 episodes.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** third, prediction, head, predict, gripper, open/close, state, binary, crossentropy, BCE, loss, supervision, Lopen, open, aopen, last, heads, enable, GravMAD, better.
- **Relevant PDF headings:** 3 METHOD (p. 4); A.4 DETAIL OF MODEL ARCHITECTURE AND HYPER-PARAMETERS FOR GRAVMAD (p. 18); A.5 COMPARISON BETWEEN GRAVMAD AND OTHER BASELINE MODELS (p. 18).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | Additionally, we further validate GravMAD on 10 real-world robotic tasks, with details provided in Appendix D.6. | p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS) |
| Action / skill decoding | Performance gains are compared to the best-performing baselines, indicated by underlines. | p. 8 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS) |
| Receding execution / feedback | GravMAD (Manual) outperforms Act3D and Voxposer across all tasks and exceeds the best baseline, 3D Diffuser Actor, in 9 out of 12 ... | p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS) |

## Failure and Ablation Link

- **p. 10 / Figure/Table caption - extractive body cue:** Figure 4: Ablation Studies. We evaluate the impact of key design elements by reporting the average success rates across 12 base tasks and 8 novel ...
- **p. 31 / Figure/Table caption - extractive body cue:** Table 10: Generalization Performance Comparison on Additional Novel Tasks. to effectively harness the potential of large-scale data. Without such improvements, the diminishing returns observed with ...
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** Without GravMaps, the policy lacks regional context, becoming overly sensitive to precise positions and unable to generalize to 9
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** 4.4 ABLATIONS Extensive ablation studies are conducted to analyze the role of each key design element in GravMAD, with the results shown in Fig 4.
- **p. 31 / Figure/Table caption - extractive body cue:** Figure 16: Additional Ablation Studies. We represent the gripper closure in the gripper map under "w/o. Cost map" as -1 instead of 0, enabling the ...
- **p. 17 / A.3.2 INFERENCE PHASE - extractive body cue:** Our pipeline consists of the following three components: 17
- **p. 26 / Figure/Table caption - extractive body cue:** Figure 11: Failure cause analysis, including (a) visualization of failure examples; (b) comparison of imprecise labels and expected labels. identify ideal areas, leading to imprecise ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 7 (3 METHOD), p. 7 (3 METHOD), p. 18 (A.4 DETAIL OF MODEL ARCHITECTURE AND HYPER-PARAMETERS FOR GRAVMAD), p. 18 (A.4 DETAIL OF MODEL ARCHITECTURE AND HYPER-PARAMETERS FOR GRAVMAD), p. 6 (3 METHOD), p. 5 (3 METHOD), objective p. 7 (3 METHOD), p. 7 (3 METHOD), p. 5 (3 METHOD), p. 5 (3 METHOD), p. 6 (3 METHOD), p. 6 (3 METHOD), temporal p. 8 (4 EXPERIMENTS), p. 15 (A.2 HEURISTICS FOR SUB-GOAL KEYPOSE DISCOVERY), p. 4 (3 METHOD), p. 5 (3 METHOD), p. 6 (3 METHOD), p. 6 (3 METHOD).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
