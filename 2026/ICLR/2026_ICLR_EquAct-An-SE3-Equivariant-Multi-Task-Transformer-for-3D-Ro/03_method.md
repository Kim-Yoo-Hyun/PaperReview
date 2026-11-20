# Method - EquAct: An SE(3)-Equivariant Multi-Task Transformer for 3D Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.iclr.cc/paper_files/paper/2026/hash/0dadf17389895a1d660a178d1140e07c-Abstract-Conference.html; PDF retrieval source: https://openreview.net/pdf/7d1ac63392c225113c314e6263f1d18dfbff895e.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> DOC-QA1 (2026-10-23): 제어문자·깨진 추출 구간과 직접 연결된 표 항목을 PDF 페이지 이미지와 대조했다. 확인 범위·원문 URL·페이지·수정 이력은 [대조 기록](../../../work/sources/pdf_note_review_2026-10-23.json)에 있다. 노트 전체의 정독이나 모든 기존 주장에 대한 재검증을 뜻하지 않으며 reading status는 유지한다.

## Method in One Sentence

PDF body method statement (p. 7 (4 Method), p. 7 (4 Method), p. 6 (4 Method), p. 6 (4 Method), p. 4 (4 Method), p. 4 (4 Method)): For translational action value evaluation, given the query translational action at and the latent point cloud h, the field network qt builds a graph with h as the source and ...

## Method Body Digest

- **p. 7 / 4 Method - extractive body cue:** For translational action value evaluation, given the query translational action at and the latent point cloud h, the field network qt builds a graph with ...
- **p. 7 / 4 Method - extractive body cue:** For rotational action value evaluation, given the query trans-rotal action at, ar and the latent point cloud h, the field network qr first aggregates features ...
- **p. 6 / 4 Method - extractive body cue:** 4.3 Invariant Feature-wise Linear Modulation Layers (iFiLM) We propose invariant Feature-wise Linear Modulation (iFiLM) layers (Figure 3 (b) left) to enforce the geometric invariance of ...
- **p. 6 / 4 Method - extractive body cue:** Specifically, the iFiLM layer takes as input a spherical Fourier feature c and a type-0 (invariant) condition feature k, and outputs a semantically modulated feature ...
- **p. 4 / 4 Method - extractive body cue:** We model the policy as an implicit function Qa(o, n, a) ∈R that estimates the action value given an observation and a query action.
- **p. 4 / 4 Method - extractive body cue:** 1) The SE(3)-Equivariant Point Transformer U-Net encodes the observation o that includes a point cloud s and the gripper pose e into a set of ...
- **p. 5 / 4 Method - extractive body cue:** Methodologically, EquAct achieves equivariance between the observation and action by employing a novel SE(3)-equivariant Point Transformer U-Net (Section 4.2) and SE(3)-equivariant field networks (Section 4.4).
- **원문 대조:** 학습은 expert action을 후보 action 중 선택하는 classification으로 다루고 translation, rotation, gripper-open 예측에 cross-entropy를 사용한다. 식의 H는 cross-entropy이며 일반적인 RL return objective가 아니다. ([PDF p. 5](https://arxiv.org/pdf/2505.21351#page=5), §4 Method, training-loss equation).

## Design Rationale

- **p. 2 / 1 Introduction - extractive body cue:** We propose a continuous SE(3)-equivariant keyframe policy that includes a novel equivariant U-net architecture, a novel invariant FiLM layer, and a novel equivariant field network.
- **p. 6 / 4 Method - extractive body cue:** To extend this operation to the spherical Fourier domain, we propose a novel spherical Fourier upsampling method (Figure 3 (b) right).
- **p. 2 / 1 Introduction - extractive body cue:** While achieving state-of-the-art performance on 18 RLBench SE(2) and SE(3) benchmarks, our method leverages a spherical Fourier representation to achieve computational efficiency during both training ...

## Source Evidence Cues

- **p. 7 / 4 Method - extractive body cue:** For translational action value evaluation, given the query translational action at and the latent point cloud h, the field network qt builds a graph with ...
- **p. 7 / 4 Method - extractive body cue:** For rotational action value evaluation, given the query trans-rotal action at, ar and the latent point cloud h, the field network qr first aggregates features ...
- **p. 6 / 4 Method - extractive body cue:** 4.3 Invariant Feature-wise Linear Modulation Layers (iFiLM) We propose invariant Feature-wise Linear Modulation (iFiLM) layers (Figure 3 (b) left) to enforce the geometric invariance of ...
- **p. 6 / 4 Method - extractive body cue:** Specifically, the iFiLM layer takes as input a spherical Fourier feature c and a type-0 (invariant) condition feature k, and outputs a semantically modulated feature ...
- **p. 4 / 4 Method - extractive body cue:** We model the policy as an implicit function Qa(o, n, a) ∈R that estimates the action value given an observation and a query action.
- **p. 4 / 4 Method - extractive body cue:** 1) The SE(3)-Equivariant Point Transformer U-Net encodes the observation o that includes a point cloud s and the gripper pose e into a set of ...
- **p. 5 / 4 Method - extractive body cue:** Methodologically, EquAct achieves equivariance between the observation and action by employing a novel SE(3)-equivariant Point Transformer U-Net (Section 4.2) and SE(3)-equivariant field networks (Section 4.4).
- **Detected method headings:** 4 Method (p. 4)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | For translational action value evaluation, given the query translational action at and the latent point cloud h, the field network qt builds ... | p. 7 (4 Method), p. 7 (4 Method) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | For rotational action value evaluation, given the query trans-rotal action at, ar and the latent point cloud h, the field network qr ... | p. 7 (4 Method), p. 6 (4 Method) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | 4.3 Invariant Feature-wise Linear Modulation Layers (iFiLM) We propose invariant Feature-wise Linear Modulation (iFiLM) layers (Figure 3 (b) left) to enforce the ... | p. 6 (4 Method), p. 6 (4 Method) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **원문 대조:** 학습은 expert action을 후보 action 중 선택하는 classification으로 다루고 translation, rotation, gripper-open 예측에 cross-entropy를 사용한다. 식의 H는 cross-entropy이며 일반적인 RL return objective가 아니다. ([PDF p. 5](https://arxiv.org/pdf/2505.21351#page=5), §4 Method, training-loss equation).
- **p. 5 / 4 Method - extractive body cue:** EquAct is SE(3)-equivariant in observation-action mapping and SE(3)-invariant to nature language instruction, as described in Equation 2.
- **p. 6 / 4 Method - extractive body cue:** The spherical Fourier maxpooling operation defined in Equation 3 is SE(3)- equivariant.
- **p. 6 / 4 Method - extractive body cue:** 4.3 Invariant Feature-wise Linear Modulation Layers (iFiLM) We propose invariant Feature-wise Linear Modulation (iFiLM) layers (Figure 3 (b) left) to enforce the geometric invariance of ...
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 5 (4 Method), p. 5 (4 Method), p. 6 (4 Method), p. 6 (4 Method).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | EquAct, multi-task, keyframe, action, policy, takes, observation, natural, language, instruction, input, predicts, next, best | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | EquAct, multi-task, keyframe, action, policy, takes, observation, natural, language, instruction | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | continuous, equivariant, keyframe, policy, includes, novel, U-net, architecture, invariant, FiLM | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | During, training, EquAct, minimizes, following, loss, Qopen, aopen, where, expert | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 4 Method - extractive body cue:** EquAct is a multi-task keyframe action policy that takes an observation o and a natural language instruction n as input and predicts the next best ...
- **p. 2 / 2 Background - extractive body cue:** The keyframe action formulation [24, 26] defines an open-loop policy setting, where the policy predicts the next goal pose of the gripper based on the ...
- **p. 5 / 4 Method - extractive body cue:** EquAct is SE(3)-equivariant in observation-action mapping and SE(3)-invariant to nature language instruction, as described in Equation 2.
- **p. 5 / 4 Method - extractive body cue:** Under the invariance assumption, given a fixed natural language instruction n, the action transformation depends solely on the transformation applied to the observation.
- **p. 3 / 2 Background - extractive body cue:** Building on this idea, PerAct [52] proposes a transformer-based agent that learns a multi-task policy-executing different keyframe actions conditioned on natural language instructions.
- **p. 1 / 1 Introduction - extractive body cue:** Recent breakthroughs in multi-task keyframe action policy learning[52, 13, 14, 29, 15, 8] have been driven by the success of transformer architectures[59], which excel at ...
- **p. 1 / 1 Introduction - extractive body cue:** We first identify the equivariance inherent to keyframe policies, where the keyframe action adapts to the transformation of the observation, and the invariance of natural ...
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | We report the task success rate over 25 evaluation episodes per task, with a maximum of 25 steps per episode. | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | This formulation decomposes complex trajectories into a sequence of keyframe poses, thereby simplifying policy learning while preserving the ability to solve a ... | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | We report the task success rate over 25 evaluation episodes per task, with a maximum of 25 steps per episode. | hardware, batch and throughput |

## Training vs Inference

- **p. 9 / 5 Experiments - extractive body cue:** Besides success rate, EquAct matches the training/inference time and GPU memory consumption of other baselines.
- **p. 7 / 5 Experiments - extractive body cue:** All the baselines are trained and evaluated on a single RTX 4090 GPU with 24 GB memory.
- **p. 4 / 4 Method - extractive body cue:** The inference procedure is illustrated in Figure 1 and has the following steps.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** translational, action, value, evaluation, given, query, latent, point, cloud, field, network, builds, graph, source, destination, then, performs, attention, aggregate, spherical.
- **Relevant PDF headings:** 4 Method (p. 4).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | In the 10 SE(3) setting, the training set contains 10 demo per task and both the training and testing scenes have randomly ... | p. 8 (5 Experiments), p. 7 (5 Experiments) |
| Action / skill decoding | In the end, EquAct outperforms SOTA baselines by 2.6% and 6.2% when trained with 100 or 10 demos in SE(2) setting, and ... | p. 9 (5 Experiments), p. 7 (5 Experiments) |
| Receding execution / feedback | On average, EquAct outperforms all the baselines on all 3 settings. avg. success rate ↑ open drawer slide block sweep dust. meat ... | p. 8 (5 Experiments), p. 9 (5 Experiments) |

## Failure and Ablation Link

- **p. 9 / 5 Experiments - extractive body cue:** 12.3 14 0 35 0 We perform the ablations on the 10 demo setting: Ours: the full EquAct model. aug. →no aug. removes data augmentation ...
- **p. 9 / 5 Experiments - extractive body cue:** Even though only a single equivariant layer is replaced, equ. →no equ. results in the largest performance drop, underscoring the critical role of maintaining geometric ...
- **p. 8 / 5 Experiments - extractive body cue:** A language instruction specifies each variant of the task.
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 1: Overview of EquAct. EquAct first encodes the observation o = {s, e} into latent spherical features h using a SE(3)-equivariant U-Net, enco, while ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3: SE(3)-Equivariant Point Transformer U-net (EPTU). Spherical Fourier maxpooling. Analogous to the maxpooling operation in convolutional neural networks [33], the spherical Fourier maxpooling layer ...
- **p. 7 / 5 Experiments - extractive body cue:** SAM2ACT[8] is the current state-of-the-art baseline on 18 RLBench, which leverages pretrained image tokenizer from SAM2 [45] and projects point cloud into image planes [15].
- **p. 7 / 5 Experiments - extractive body cue:** Performance is measured by a binary reward, where 0% and 100% correspond to failure and successful completion of the task according to the natural language ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 7 (4 Method), p. 7 (4 Method), p. 6 (4 Method), p. 6 (4 Method), p. 4 (4 Method), p. 4 (4 Method), objective p. 5 (4 Method), p. 5 (4 Method), p. 6 (4 Method), p. 6 (4 Method), temporal p. 7 (5 Experiments), p. 2 (2 Background), p. 4 (4 Method), p. 4 (4 Method), p. 5 (4 Method), p. 5 (4 Method).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (18 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** EquAct is a multi-task keyframe action policy that takes an observation o and a natural language instruction n as input and predicts the next best keyframe action of the gripper ... (p. 4, 4 Method).
- **Objective/update evidence:** EquAct is SE(3)-equivariant in observation-action mapping and SE(3)-invariant to nature language instruction, as described in Equation 2. (p. 5, 4 Method).
- **Temporal/runtime evidence:** We report the task success rate over 25 evaluation episodes per task, with a maximum of 25 steps per episode. (p. 7, 5 Experiments).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
