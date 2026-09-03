# Method - Open X-Embodiment: Robotic Learning Datasets and RT-X Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2310.08864; PDF retrieval source: https://arxiv.org/pdf/2310.08864. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 4 (IV. RT-X DESIGN), p. 4 (IV. RT-X DESIGN), p. 3 (III. THE OPEN X-EMBODIMENT REPOSITORY), p. 2 (I. INTRODUCTION), p. 3 (III. THE OPEN X-EMBODIMENT REPOSITORY), p. 5 (IV. RT-X DESIGN)): Policy architectures We consider two model architectures in our experiments: (1) RT-1 [8], an efficient Transformer-based architecture designed for robotic control, and (2) RT-2 [9] a large visionlanguage model co-fine-tuned ...

## Method Body Digest

- **p. 4 / IV. RT-X DESIGN - extractive body cue:** Policy architectures We consider two model architectures in our experiments: (1) RT-1 [8], an efficient Transformer-based architecture designed for robotic control, and (2) RT-2 [9] ...
- **p. 4 / IV. RT-X DESIGN - extractive body cue:** These tokens are fed into a decoder-only Transformer, which outputs the tokenized actions.
- **p. 3 / III. THE OPEN X-EMBODIMENT REPOSITORY - extractive body cue:** We introduce the Open X-Embodiment Repository (robotics-transformer-x.github.io) - an open-source repository which includes large-scale data along with pre-trained model checkpoints for X-embodied robot learning research.
- **p. 2 / I. INTRODUCTION - extractive body cue:** Our aim is not to innovate in terms of the particular architectures and algorithms, but rather to provide the model that we trained together with ...
- **p. 3 / III. THE OPEN X-EMBODIMENT REPOSITORY - extractive body cue:** In this section, we summarize the dataset and X-embodiment learning framework, before discussing the specific models we use to evaluate our dataset and our experimental ...
- **p. 5 / IV. RT-X DESIGN - extractive body cue:** At inference time, each model is run at the rate required for the robot (3-10 Hz), with RT-1 run locally and RT-2 hosted on a ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Inspired by the generalization made possible by pretraining large vision or language models on diverse data, we take the perspective that the goal of training ...
- **p. 4 / IV. RT-X DESIGN - extractive body cue:** Training and inference details Both models use a standard categorical cross-entropy objective over their output space (discrete buckets for RT1 and all possible language tokens ...

## Design Rationale

- **p. 2 / I. INTRODUCTION - extractive body cue:** Addressing goal (1), our empirical contribution is to demonstrate that several recent robotic learning methods, with minimal modification, can utilize X-embodiment data and enable positive ...
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** 1: We propose an open, large-scale dataset for robot learning curated from 21 institutions across the globe.
- **p. 3 / III. THE OPEN X-EMBODIMENT REPOSITORY - extractive body cue:** We introduce the Open X-Embodiment Repository (robotics-transformer-x.github.io) - an open-source repository which includes large-scale data along with pre-trained model checkpoints for X-embodied robot learning research.

## Source Evidence Cues

- **p. 4 / IV. RT-X DESIGN - extractive body cue:** Policy architectures We consider two model architectures in our experiments: (1) RT-1 [8], an efficient Transformer-based architecture designed for robotic control, and (2) RT-2 [9] ...
- **p. 4 / IV. RT-X DESIGN - extractive body cue:** These tokens are fed into a decoder-only Transformer, which outputs the tokenized actions.
- **p. 3 / III. THE OPEN X-EMBODIMENT REPOSITORY - extractive body cue:** We introduce the Open X-Embodiment Repository (robotics-transformer-x.github.io) - an open-source repository which includes large-scale data along with pre-trained model checkpoints for X-embodied robot learning research.
- **p. 2 / I. INTRODUCTION - extractive body cue:** Our aim is not to innovate in terms of the particular architectures and algorithms, but rather to provide the model that we trained together with ...
- **p. 3 / III. THE OPEN X-EMBODIMENT REPOSITORY - extractive body cue:** In this section, we summarize the dataset and X-embodiment learning framework, before discussing the specific models we use to evaluate our dataset and our experimental ...
- **p. 5 / IV. RT-X DESIGN - extractive body cue:** At inference time, each model is run at the rate required for the robot (3-10 Hz), with RT-1 run locally and RT-2 hosted on a ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Inspired by the generalization made possible by pretraining large vision or language models on diverse data, we take the perspective that the goal of training ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | Policy architectures We consider two model architectures in our experiments: (1) RT-1 [8], an efficient Transformer-based architecture designed for robotic control, and ... | p. 4 (IV. RT-X DESIGN), p. 4 (IV. RT-X DESIGN) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | These tokens are fed into a decoder-only Transformer, which outputs the tokenized actions. | p. 4 (IV. RT-X DESIGN), p. 3 (III. THE OPEN X-EMBODIMENT REPOSITORY) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | We introduce the Open X-Embodiment Repository (robotics-transformer-x.github.io) - an open-source repository which includes large-scale data along with pre-trained model checkpoints for X-embodied ... | p. 3 (III. THE OPEN X-EMBODIMENT REPOSITORY), p. 2 (I. INTRODUCTION) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / IV. RT-X DESIGN - extractive body cue:** Training and inference details Both models use a standard categorical cross-entropy objective over their output space (discrete buckets for RT1 and all possible language tokens ...
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 4 (IV. RT-X DESIGN), p. 1 (Body text (section boundary not confidently recovered)).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | RT-1-X, RT-2-X, take, images, text, instruction, input, output, discretized, end-effector, actions, models, visual, natural | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | RT-1-X, RT-2-X, take, images, text, instruction, input, output, discretized, end-effector | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | Addressing, goal, empirical, contribution, demonstrate, several, recent, robotic, learning, methods | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | Training, inference, details, models, standard, categorical, cross-entropy, objective, over, output | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 5 Hz - extractive body cue:** 3: RT-1-X and RT-2-X both take images and a text instruction as input and output discretized end-effector actions.
- **p. 4 / IV. RT-X DESIGN - extractive body cue:** Both models take in a visual input and natural language instruction describing the task, and output a tokenized action.
- **p. 3 / III. THE OPEN X-EMBODIMENT REPOSITORY - extractive body cue:** We use the RLDS data format [119], which saves data in serialized tfrecord files and accommodates the various action spaces and input modalities of different ...
- **p. 1 / Abstract - extractive body cue:** Can we instead train "generalist" X-robot policy that can be adapted efficiently to new robots, tasks.
- **p. 2 / I. INTRODUCTION - extractive body cue:** Even the largest data collection efforts still end up with datasets that are a fraction of the size and diversity of benchmark datasets in vision ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** However, these lessons are difficult to apply in robotics: any single robotic domain might be too narrow, and while computer vision and NLP can leverage ...
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** 1: We propose an open, large-scale dataset for robot learning curated from 21 institutions across the globe.
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | We note that including a short history of images significantly improves generalization performance (row (4) vs row (5)). | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | While RT-X demonstrates a step towards a X-embodied robot generalist, many more steps are needed to make this future a reality. | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | We note that including a short history of images significantly improves generalization performance (row (4) vs row (5)). | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | At inference time, each model is run at the rate required for the robot (3-10 Hz), with RT-1 run locally and RT-2 ... | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / IV. RT-X DESIGN - extractive body cue:** Policy architectures We consider two model architectures in our experiments: (1) RT-1 [8], an efficient Transformer-based architecture designed for robotic control, and (2) RT-2 [9] ...
- **p. 3 / III. THE OPEN X-EMBODIMENT REPOSITORY - extractive body cue:** We introduce the Open X-Embodiment Repository (robotics-transformer-x.github.io) - an open-source repository which includes large-scale data along with pre-trained model checkpoints for X-embodied robot learning research.
- **p. 2 / I. INTRODUCTION - extractive body cue:** Our aim is not to innovate in terms of the particular architectures and algorithms, but rather to provide the model that we trained together with ...
- **p. 5 / IV. RT-X DESIGN - extractive body cue:** At inference time, each model is run at the rate required for the robot (3-10 Hz), with RT-1 run locally and RT-2 hosted on a ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Inspired by the generalization made possible by pretraining large vision or language models on diverse data, we take the perspective that the goal of training ...
- **p. 5 / IV. RT-X DESIGN - extractive body cue:** At inference time, each model is run at the rate required for the robot (3-10 Hz), with RT-1 run locally and RT-2 hosted on a ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Policy, architectures, consider, model, experiments, RT-1, efficient, Transformer-based, architecture, designed, robotic, control, RT-2, large, visionlanguage, co-fine-tuned, output, robot, actions, natural.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | Row Model Size History Length Dataset Co-Trained w/ Web Initial Checkpoint Emergent Skills Evaluation RT-2 Generalization Evaluation (1) RT-2 55B none Google ... | p. 6 (V. EXPERIMENTAL RESULTS), p. 6 (V. EXPERIMENTAL RESULTS) |
| Action / skill decoding | In the largedataset setting, the RT-1-X model does not outperform the RT-1 baseline trained on only the embodiment-specific dataset, which indicates underfitting ... | p. 5 (V. EXPERIMENTAL RESULTS), p. 5 (V. EXPERIMENTAL RESULTS) |
| Receding execution / feedback | Our results showed that the RT-1X policy has a 50% higher success rate than the original, state-of-the-art methods contributed by different collaborating ... | p. 6 (V. EXPERIMENTAL RESULTS), p. 5 (V. EXPERIMENTAL RESULTS) |

## Failure and Ablation Link

- **p. 6 / V. EXPERIMENTAL RESULTS - extractive body cue:** Our next ablation involves removing the Bridge dataset from RT-2-X training: Row (3) shows the results for RT-2X that includes all data used for RT-2-X ...
- **p. 6 / V. EXPERIMENTAL RESULTS - extractive body cue:** Row Model Size History Length Dataset Co-Trained w/ Web Initial Checkpoint Emergent Skills Evaluation RT-2 Generalization Evaluation (1) RT-2 55B none Google Robot action Yes ...
- **p. 5 / V. EXPERIMENTAL RESULTS - extractive body cue:** Our experiments answer three questions about the effect of X-embodiment training: (1) Can policies trained on our X-embodiment dataset effectively enable positive transfer, such that ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2: The Open X-Embodiment Dataset. (a): the dataset consists of 60 individual datasets across 22 embodiments. (b): the Franka robot has the largest diversity ...
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: We propose an open, large-scale dataset for robot learning curated from 21 institutions across the globe. The dataset represents diverse behaviors, robot embodiments ...
- **p. 5 / V. EXPERIMENTAL RESULTS - extractive body cue:** In the largedataset setting, the RT-1-X model does not outperform the RT-1 baseline trained on only the embodiment-specific dataset, which indicates underfitting for that model ...
- **p. 6 / V. EXPERIMENTAL RESULTS - extractive body cue:** DISCUSSION, FUTURE WORK, AND OPEN PROBLEMS We presented a consolidated dataset that combines data from 22 robotic embodiments collected through a collaboration between 21 institutions, ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (IV. RT-X DESIGN), p. 4 (IV. RT-X DESIGN), p. 3 (III. THE OPEN X-EMBODIMENT REPOSITORY), p. 2 (I. INTRODUCTION), p. 3 (III. THE OPEN X-EMBODIMENT REPOSITORY), p. 5 (IV. RT-X DESIGN), objective p. 4 (IV. RT-X DESIGN), temporal p. 6 (V. EXPERIMENTAL RESULTS), p. 6 (V. EXPERIMENTAL RESULTS), p. 3 (III. THE OPEN X-EMBODIMENT REPOSITORY), p. 3 (III. THE OPEN X-EMBODIMENT REPOSITORY), p. 4 (IV. RT-X DESIGN), p. 4 (IV. RT-X DESIGN).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (12 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** Policy architectures We consider two model architectures in our experiments: (1) RT-1 [8], an efficient Transformer-based architecture designed for robotic control, and (2) RT-2 [9] a large visionlanguage model co-fine-tuned ... (p. 4, IV. RT-X DESIGN).
- **Objective/update evidence:** Training and inference details Both models use a standard categorical cross-entropy objective over their output space (discrete buckets for RT1 and all possible language tokens for RT-2). (p. 4, IV. RT-X DESIGN).
- **Temporal/runtime evidence:** We note that including a short history of images significantly improves generalization performance (row (4) vs row (5)). (p. 6, V. EXPERIMENTAL RESULTS).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
