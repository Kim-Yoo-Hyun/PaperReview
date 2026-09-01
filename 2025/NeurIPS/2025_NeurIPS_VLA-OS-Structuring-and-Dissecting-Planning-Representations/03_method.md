# Method - VLA-OS: Structuring and Dissecting Planning Representations and Paradigms in Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (32 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=PQYazNKEYo; PDF retrieval source: https://openreview.net/pdf/05a810d8dce16f520e115b9ee80b8096e6512276.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 6 (3.1 Preliminaries), p. 1 (Abstract), p. 4 (3.1 Preliminaries), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction)): As shown in Figure 2, we use the VLM together with planning heads for task planning, and modify the action head to an encoder-decoder transformer for policy learning.

## Method Body Digest

- **p. 6 / 3.1 Preliminaries - extractive PDF cue:** As shown in Figure 2, we use the VLM together with planning heads for task planning, and modify the action head to an encoder-decoder transformer ...
- **p. 1 / Abstract - extractive PDF cue:** To systematically investigate the impacts of different planning paradigms and representations isolating from network architectures and training data, in this paper, we introduce VLA-OS, a ...
- **p. 4 / 3.1 Preliminaries - extractive PDF cue:** Then, we use a separate set of weights as an action head for the robotics-specific tokens (action and proprioception states).
- **p. 2 / 1 Introduction - extractive PDF cue:** This motivates future work on improving training and inference algorithms for Hierarchical-VLA models. actions, these methods demonstrate stronger capabilities in task reasoning and comprehension for ...
- **p. 3 / 1 Introduction - extractive PDF cue:** Pioneering works mainly focus on verifying the effectiveness of large-scale robot learning [10, 11, 59, 75], while later works start to explore different model architectures, ...
- **p. 3 / 1 Introduction - extractive PDF cue:** Our experiments yield three primary findings: 1) Visually grounded planning representations (visual reasoning and image foresight planning) outperform language-based planning representations across multiple dimensions including ...
- **p. 7 / 3.1 Preliminaries - extractive PDF cue:** Analysis: The implicit planning paradigm leverages various auxiliary task planning objectives as additional losses for training, and during inference, there is no difference between it ...
- **p. 4 / 1 Introduction - extractive PDF cue:** For implicit planning, MDT [69] and PIDM [77] use goal image foresight generation loss as an auxiliary objective for planning, while RoboBrain [39] and ChatVLA ...

## Design Rationale

- **p. 1 / Abstract - extractive PDF cue:** To systematically investigate the impacts of different planning paradigms and representations isolating from network architectures and training data, in this paper, we introduce VLA-OS, a ...
- **p. 3 / 1 Introduction - extractive PDF cue:** Furthermore, to answer the bottleneck question, we designed a novel set of evaluation metrics tailored to separately assess the performance of task planning and policy ...
- **p. 3 / 1 Introduction - extractive PDF cue:** We show in Table 1 that VLA-OS exhibits superior performance compared to most existing VLA methods with fewer parameters and without pretraining.

## Source Evidence Cues

- **p. 6 / 3.1 Preliminaries - extractive PDF cue:** As shown in Figure 2, we use the VLM together with planning heads for task planning, and modify the action head to an encoder-decoder transformer ...
- **p. 1 / Abstract - extractive PDF cue:** To systematically investigate the impacts of different planning paradigms and representations isolating from network architectures and training data, in this paper, we introduce VLA-OS, a ...
- **p. 4 / 3.1 Preliminaries - extractive PDF cue:** Then, we use a separate set of weights as an action head for the robotics-specific tokens (action and proprioception states).
- **p. 2 / 1 Introduction - extractive PDF cue:** This motivates future work on improving training and inference algorithms for Hierarchical-VLA models. actions, these methods demonstrate stronger capabilities in task reasoning and comprehension for ...
- **p. 3 / 1 Introduction - extractive PDF cue:** Pioneering works mainly focus on verifying the effectiveness of large-scale robot learning [10, 11, 59, 75], while later works start to explore different model architectures, ...
- **p. 3 / 1 Introduction - extractive PDF cue:** Our experiments yield three primary findings: 1) Visually grounded planning representations (visual reasoning and image foresight planning) outperform language-based planning representations across multiple dimensions including ...
- **p. 7 / 3.1 Preliminaries - extractive PDF cue:** Analysis: The implicit planning paradigm leverages various auxiliary task planning objectives as additional losses for training, and during inference, there is no difference between it ...
- **Detected method headings:** C VLA-OS Model Details and Continual Learning Experiments (p. 31)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | As shown in Figure 2, we use the VLM together with planning heads for task planning, and modify the action head to ... | p. 6 (3.1 Preliminaries), p. 1 (Abstract) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | To systematically investigate the impacts of different planning paradigms and representations isolating from network architectures and training data, in this paper, we ... | p. 1 (Abstract), p. 4 (3.1 Preliminaries) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | Then, we use a separate set of weights as an action head for the robotics-specific tokens (action and proprioception states). | p. 4 (3.1 Preliminaries), p. 2 (1 Introduction) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 1 Introduction - extractive PDF cue:** For implicit planning, MDT [69] and PIDM [77] use goal image foresight generation loss as an auxiliary objective for planning, while RoboBrain [39] and ChatVLA ...
- **p. 7 / 3.1 Preliminaries - extractive PDF cue:** Analysis: The implicit planning paradigm leverages various auxiliary task planning objectives as additional losses for training, and during inference, there is no difference between it ...
- **p. 3 / 1 Introduction - extractive PDF cue:** They break up the given task into simpler sub-tasks that can be performed by either using a set of pre-trained sub-skills [36, 2, 65, 71, ...
- **p. 6 / 3.1 Preliminaries - extractive PDF cue:** The language and visual planning heads are trained with cross-entropy loss, while the image foresight planning head is trained with the special loss in [31].
- **p. 8 / 3.1 Preliminaries - extractive PDF cue:** We also illustrate the inference speed and training cost in Figure 6b (introduced in Section 4.5) to show the speed and cost advantages of visually ...
- **p. 1 / Abstract - extractive PDF cue:** Our results demonstrate that: 1) visually grounded planning representations are generally better than language planning representations; 2) the Hierarchical-VLA paradigm generally achieves superior or comparable ...
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 4 (1 Introduction), p. 7 (3.1 Preliminaries), p. 3 (1 Introduction), p. 4 (1 Introduction), p. 6 (3.1 Preliminaries), p. 6 (3.1 Preliminaries).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | action, head, take, input, images, proprioception, observations, planning, representations, generate, actions, Instead, Hierarchical-VLA, will | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | action, head, take, input, images, proprioception, observations, planning, representations, generate | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | systematically, investigate, impacts, different, planning, paradigms, representations, isolating, network, architectures | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | implicit, planning, MDT, PIDM, goal, image, foresight, generation, loss, auxiliary | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 6 / 3.1 Preliminaries - extractive PDF cue:** This action head can take as input the images, proprioception observations, and the planning representations to generate actions.
- **p. 8 / 3.1 Preliminaries - extractive PDF cue:** Instead, Hierarchical-VLA will not only take in the raw visual observation and language instruction as inputs, but also confine the planning accumulation errors exclusively to ...
- **p. 5 / 3.1 Preliminaries - extractive PDF cue:** For 3D action head, we also take in multi-view depth images as input, and fuse the multi-view RGBD images to 3D point cloud using camera ...
- **p. 4 / 3.1 Preliminaries - extractive PDF cue:** Specifically, for each task T , we assume a set of demonstrations DT = {(o1 i , a1 i ), (o2 i , a2 i ...
- **p. 6 / 3.1 Preliminaries - extractive PDF cue:** We also give frozen image features from AM-Radio [67] and language features from Qwen2.5 [89] for the inputs of the action head to compensate for ...
- **p. 5 / 3.1 Preliminaries - extractive PDF cue:** Each point from the downsampled point cloud will be seen as a token and these 3D tokens are sent to the action head as additional ...
- **p. 2 / 1 Introduction - extractive PDF cue:** ActionOnly-VLA Integrated-VLA Hierarchical-VLA PlanningOnly-VLA VLA Images Action Language VLM Images Plan Language VLA Images Action Language Plan Planner Action Policy Plan Images Language Figure 1: ...
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | The image foresight reasoning data is a third-person view image at the K-th future step as the short-horizon goal image. | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | The language reasoning data contains 8 different keys [95] for each timestep, including Task, Plan, Subtask, Subtask Reason, Move, Move Reason, Gripper ... | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | We use a history of multi-view images and proprioception information as observations. | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 1 / Abstract - extractive PDF cue:** To systematically investigate the impacts of different planning paradigms and representations isolating from network architectures and training data, in this paper, we introduce VLA-OS, a ...
- **p. 2 / 1 Introduction - extractive PDF cue:** This motivates future work on improving training and inference algorithms for Hierarchical-VLA models. actions, these methods demonstrate stronger capabilities in task reasoning and comprehension for ...
- **p. 3 / 1 Introduction - extractive PDF cue:** Pioneering works mainly focus on verifying the effectiveness of large-scale robot learning [10, 11, 59, 75], while later works start to explore different model architectures, ...
- **p. 3 / 1 Introduction - extractive PDF cue:** Our experiments yield three primary findings: 1) Visually grounded planning representations (visual reasoning and image foresight planning) outperform language-based planning representations across multiple dimensions including ...
- **p. 7 / 3.1 Preliminaries - extractive PDF cue:** Analysis: The implicit planning paradigm leverages various auxiliary task planning objectives as additional losses for training, and during inference, there is no difference between it ...
- **p. 8 / 3.1 Preliminaries - extractive PDF cue:** (b) Training cost and inference time for different representations.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Figure, VLM, together, planning, heads, task, modify, action, head, encoder-decoder, transformer, policy, learning, systematically, investigate, impacts, different, paradigms, representations, isolating.
- **Relevant PDF headings:** C VLA-OS Model Details and Continual Learning Experiments (p. 31).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | The limitations of this paper are: 1) despite the VLA-OS family encompassing a wide array of task planning paradigms for VLA, there ... | p. 10 (3. Integrated-VLA and Hierarchical-VLA outperform ActionOnly-VLA on task performance), p. 10 (3. Integrated-VLA and Hierarchical-VLA outperform ActionOnly-VLA on task performance) |
| Action / skill decoding | Table 1: Sanity check. Success rates on four LIBERO benchmarks. Baseline results are from their papers [43, 8, 44]. Our results are ... | p. 7 (Figure/Table caption), p. 5 (Figure/Table caption) |
| Receding execution / feedback | Figure 1: Left: four different VLA paradigms. Note that in this paper, we didn't explore PlanningOnly- VLA since they usually cannot be ... | p. 2 (Figure/Table caption), p. 7 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 10 / 3. Integrated-VLA and Hierarchical-VLA outperform ActionOnly-VLA on task performance - extractive PDF cue:** The limitations of this paper are: 1) despite the VLA-OS family encompassing a wide array of task planning paradigms for VLA, there remain several designs ...
- **p. 10 / 3. Integrated-VLA and Hierarchical-VLA outperform ActionOnly-VLA on task performance - extractive PDF cue:** Integrated-VLA and Hierarchical-VLA perform comparably on task performance and Planning Head Pretraining, but Hierarchical-VLA generalizes better, has better task-planning performance, and performs better when using ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 1: Left: four different VLA paradigms. Note that in this paper, we didn't explore PlanningOnly- VLA since they usually cannot be trained with the ...
- **p. 9 / 3.1 Preliminaries - extractive PDF cue:** L V IF DCS IFS DCS IFS DCS IFS VLA-OS-I-I 0.79 - 0.83 - 0.92 - VLA-OS-H 0.81 0.84 0.86 0.93 0.94 0.90 It is ...
- **p. 8 / 3.1 Preliminaries - extractive PDF cue:** For qualitative comparisons, we show in Figure 5 an example that when VLA-OS-H uses the same planning heads as VLA-OS-I-E where there are some planning ...
- **p. 10 / 3.1 Preliminaries - extractive PDF cue:** 5 Conclusion and Limitation We provide a systematic investigation across different VLA paradigms and task planning representations through various kinds of manipulation tasks.
- **p. 10 / 3. Integrated-VLA and Hierarchical-VLA outperform ActionOnly-VLA on task performance - extractive PDF cue:** The limitations of this paper are: 1) despite the VLA-OS family encompassing a wide array of task planning paradigms for VLA, there remain several designs ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 6 (3.1 Preliminaries), p. 1 (Abstract), p. 4 (3.1 Preliminaries), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction), objective p. 4 (1 Introduction), p. 7 (3.1 Preliminaries), p. 3 (1 Introduction), p. 6 (3.1 Preliminaries), p. 8 (3.1 Preliminaries), p. 1 (Abstract), temporal p. 5 (3.1 Preliminaries), p. 5 (3.1 Preliminaries), p. 1 (Abstract), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 4 (3.1 Preliminaries).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
