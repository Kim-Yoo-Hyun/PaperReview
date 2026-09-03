# Method - Uni-NaVid: A Video-based Vision-Language-Action Model for Unifying Embodied Navigation Tasks

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p013.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p013.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 7 (B. Training Strategy of Uni-NaVid), p. 7 (B. Training Strategy of Uni-NaVid)): To incorporate openworld knowledge, we follow previous Vision-and-Language Action models (100, 9]. integrating open-world video questionanswering during training, Specifically, we adopt a two-stage training process (a common strategy in ...

## Method Body Digest

- **p. 7 / B. Training Strategy of Uni-NaVid - extractive body cue:** To incorporate openworld knowledge, we follow previous Vision-and-Language Action models (100, 9]. integrating open-world video questionanswering during training, Specifically, we adopt a two-stage training process ...
- **p. 7 / B. Training Strategy of Uni-NaVid - extractive body cue:** During training, the vision encoder (EVACLIP (77) and large language model (Vicuna-7B [20)) are preloaded with default pre-trained weight.
- **p. 7 / B. Training Strategy of Uni-NaVid - extractive body cue:** Following the training strategy of VLM [SI], we optimize the trainable parameters for only 1 epoch
- **p. 1 / Abstract - extractive body cue:** This VLA model can directly take natural language instructions and RGB video streams as inputs and output low-level robotic actions in an end-to-end manner.
- **p. 2 / 1. Ivrropuction - extractive body cue:** Uni-NaVid_ takes egocentric RGB video streams and natural language instructions as inputs, and directly generates low-level actions for navigation in continuous environments. ‘To achieve multi-task ...
- **p. 3 / 1. Ivrropuction - extractive body cue:** Navigation task definition, We define the general-purpose navigation of Uni-NaVid_as follows: At the time 7', given a natural language instruction Z consisting of { words ...
- **p. 3 / 1. Ivrropuction - extractive body cue:** However, abstracting dense visual information into text and relying on discrete landmarks results in sparse enVironmental observations and is limited to static environments Another approach ...
- **p. 2 / 1. Ivrropuction - extractive body cue:** Utilizing only RGB video streams and instructions as inputs, our method demonstrates the superiority of a single VLA model across diverse benchmarks, achieving SOTA or ...

## Design Rationale

- **p. 3 / 1. Ivrropuction - extractive body cue:** However, our goal is to train and ‘evaluate our method on mainstream datasets to clearly justify the performance of our approach.
- **p. 2 / 1. Ivrropuction - extractive body cue:** ‘We conduct extensive experiments on benchmarks across the aforementioned four navigation tasks and compared our method with strong baselines specifically designed for each task.
- **p. 1 / Abstract - extractive body cue:** To efficiently process extensive RGB video streams, we propose an online token merge strategy that spatially and {temporally consolidates similar visual information which improves the ...

## Source Evidence Cues

- **p. 7 / B. Training Strategy of Uni-NaVid - extractive body cue:** To incorporate openworld knowledge, we follow previous Vision-and-Language Action models (100, 9]. integrating open-world video questionanswering during training, Specifically, we adopt a two-stage training process ...
- **p. 7 / B. Training Strategy of Uni-NaVid - extractive body cue:** During training, the vision encoder (EVACLIP (77) and large language model (Vicuna-7B [20)) are preloaded with default pre-trained weight.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Map / localization state | sensor stream을 pose와 world map으로 누적한다 | camera/depth/LiDAR, odometry, history | mapping, localization, scene graph 또는 map update를 수행 | pose/map/free-space state | To incorporate openworld knowledge, we follow previous Vision-and-Language Action models (100, 9]. integrating open-world video questionanswering during training, Specifically, we adopt a ... | p. 7 (B. Training Strategy of Uni-NaVid), p. 7 (B. Training Strategy of Uni-NaVid) |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | During training, the vision encoder (EVACLIP (77) and large language model (Vicuna-7B [20)) are preloaded with default pre-trained weight. | p. 7 (B. Training Strategy of Uni-NaVid) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | To incorporate openworld knowledge, we follow previous Vision-and-Language Action models (100, 9]. integrating open-world video questionanswering during training, Specifically, we adopt a ... | p. 7 (B. Training Strategy of Uni-NaVid) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 7 / B. Training Strategy of Uni-NaVid - extractive body cue:** Following the training strategy of VLM [SI], we optimize the trainable parameters for only 1 epoch
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | VLA, model, directly, take, natural, language, instructions, RGB, video, streams, inputs, output, low-level, robotic | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | VLA, model, directly, take, natural, language, instructions, RGB, video, streams | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | However, goal, train, evaluate, mainstream, datasets, clearly, justify, performance, conduct | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | Following, training, strategy, VLM, optimize, trainable, parameters, only, epoch | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / Abstract - extractive body cue:** This VLA model can directly take natural language instructions and RGB video streams as inputs and output low-level robotic actions in an end-to-end manner.
- **p. 2 / 1. Ivrropuction - extractive body cue:** Uni-NaVid_ takes egocentric RGB video streams and natural language instructions as inputs, and directly generates low-level actions for navigation in continuous environments. ‘To achieve multi-task ...
- **p. 3 / 1. Ivrropuction - extractive body cue:** Navigation task definition, We define the general-purpose navigation of Uni-NaVid_as follows: At the time 7', given a natural language instruction Z consisting of { words ...
- **p. 3 / 1. Ivrropuction - extractive body cue:** However, abstracting dense visual information into text and relying on discrete landmarks results in sparse enVironmental observations and is limited to static environments Another approach ...
- **p. 2 / 1. Ivrropuction - extractive body cue:** Utilizing only RGB video streams and instructions as inputs, our method demonstrates the superiority of a single VLA model across diverse benchmarks, achieving SOTA or ...
- **p. 4 / 1. Ivrropuction - extractive body cue:** As common, the instructions are also tokenized as a set of tokens, known as language observation tokens.
- **p. 4 / 1. Ivrropuction - extractive body cue:** Both the visual observation tokens and language observation tokens are ‘concatenated and passed to the Large Language Model (LLM), ‘which infers four action tokens that ...
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | During navigation, the agent is required to process a substantial volume of online captured frames, which results in memory overload and computational ... | episode/sequence/action-chunk boundary |
| Rate / latency | mapping/localization, global planner, local planner와 base controller rate를 구분한다. | To efficiently process extensive RGB video streams, we propose an online token merge strategy that spatially and {temporally consolidates similar visual information ... | Hz/fps, inference time and control rate |
| Memory | map/scene graph, pose history와 current local goal. | During navigation, the agent is required to process a substantial volume of online captured frames, which results in memory overload and computational ... | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | To efficiently process extensive RGB video streams, we propose an online token merge strategy that spatially and {temporally consolidates similar visual information ... | hardware, batch and throughput |

## Training vs Inference

- **p. 7 / B. Training Strategy of Uni-NaVid - extractive body cue:** To incorporate openworld knowledge, we follow previous Vision-and-Language Action models (100, 9]. integrating open-world video questionanswering during training, Specifically, we adopt a two-stage training process ...
- **p. 7 / B. Training Strategy of Uni-NaVid - extractive body cue:** During training, the vision encoder (EVACLIP (77) and large language model (Vicuna-7B [20)) are preloaded with default pre-trained weight.
- **p. 7 / B. Training Strategy of Uni-NaVid - extractive body cue:** Uni-NaVid is trained on a cluster server with 40 NVIDIA H800 GPUs for approximately 35 hours, totaling 1400 GPU hours.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** incorporate, openworld, knowledge, follow, previous, Vision-and-Language, Action, models, integrating, open-world, video, questionanswering, during, training, Specifically, adopt, two-stage, process, common, strategy.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | The robot then executes the predicted actions and calls STOP once the first predicted action is a stop action, For VLN and ... | p. 7 (VI. EXPERIMENT), p. 7 (VI. EXPERIMENT) |
| Global / local decision | Compared to ‘mainstream baselines, we find that Uni-NaVid archives the best performance on four metrics, including BLUE-1 (417.9%), ROUGE (5.7%), METEOR (+ ... | p. 9 (B. Individual Task Results), p. 7 (VI. EXPERIMENT) |
| Motion execution / recovery | The results in Table V demonstrate that our method achieves significant improvement over the zero-shot method (VLFM [93] and even outperforms the ... | p. 8 (B. Individual Task Results), p. 8 (B. Individual Task Results) |

## Failure and Ablation Link

- **p. 7 / VI. EXPERIMENT - extractive body cue:** It is worth noting that for EQA [21] task, the agent executes navigation actions until a stop command is issued, We then remove the navigation-specific ...
- **p. 11 / C. Qualitative Results in Real-World - extractive body cue:** Ablation on training strategy and architecture.
- **p. 11 / C. Qualitative Results in Real-World - extractive body cue:** Additional ablation studies on architecture and hyperparameters are provided in the Supplementary Materia
- **p. 8 / B. Individual Task Results - extractive body cue:** We add experiments of removing RXR samples in Supplemntal Material, where our method still achive STOA performance (+23.9 SR(%)) against NaVid.
- **p. 8 / B. Individual Task Results - extractive body cue:** The results in Table V demonstrate that our method achieves significant improvement over the zero-shot method (VLFM [93] and even outperforms the fine-tuned method (DAgRL+0D ...
- **p. 7 / VI. EXPERIMENT - extractive body cue:** standard evaluation metrics [4], including success rate (SR), oracle success rate (OS), success weighted by path length (SPL) [3], trajectory length (TL), following rate (FR) ...
- **p. 11 / C. Qualitative Results in Real-World - extractive body cue:** Despite the promising results, Uni-NaVid has several limitations.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 7 (B. Training Strategy of Uni-NaVid), p. 7 (B. Training Strategy of Uni-NaVid), objective p. 7 (B. Training Strategy of Uni-NaVid), temporal p. 2 (1. Ivrropuction), p. 1 (Abstract), p. 7 (VI. EXPERIMENT), p. 4 (B. Online Visual Token Merging), p. 4 (1. Ivrropuction), p. 5 (1 Xan 7p (A Xgl HY + Xedos)).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (17 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** Uni-NaVid_ takes egocentric RGB video streams and natural language instructions as inputs, and directly generates low-level actions for navigation in continuous environments. ‘To achieve multi-task navigation While supporting efficient ... (p. 2, 1. Ivrropuction).
- **Objective/update evidence:** Following the training strategy of VLM [SI], we optimize the trainable parameters for only 1 epoch (p. 7, B. Training Strategy of Uni-NaVid).
- **Temporal/runtime evidence:** During navigation, the agent is required to process a substantial volume of online captured frames, which results in memory overload and computational latency, particularly in LLM-based approaches {100, 58]. (p. 2, 1. Ivrropuction).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
