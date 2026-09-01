# Method - RT-1: Robotics Transformer for Real-World Control at Scale

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (31 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2212.06817; PDF retrieval source: https://arxiv.org/pdf/2212.06817. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 2 (3 Hz), p. 6 (3 PRELIMINARIES), p. 4 (3 PRELIMINARIES), p. 4 (3 PRELIMINARIES), p. 5 (3 PRELIMINARIES), p. 6 (3 PRELIMINARIES)): We propose a novel architecture that we call RT-1 (Robotics Transformer 1), which by encoding high-dimensional inputs and outputs, including camera images, instructions and motor commands into compact token representations ...

## Method Body Digest

- **p. 2 / 3 Hz - extractive body cue:** We propose a novel architecture that we call RT-1 (Robotics Transformer 1), which by encoding high-dimensional inputs and outputs, including camera images, instructions and motor ...
- **p. 6 / 3 PRELIMINARIES - extractive body cue:** The Transformer is a decoder-only sequence model with 8 self-attention layers and 19M total parameters that outputs action tokens.
- **p. 4 / 3 PRELIMINARIES - extractive body cue:** 5 RT-1: ROBOTICS TRANSFORMER In this section, we describe how we tokenize the images, text, and actions, and then discuss the RT-1 model architecture.
- **p. 4 / 3 PRELIMINARIES - extractive body cue:** To this end, the architecture (shown in Figure 1a) leverages several elements: first the images and text are processed via an ImageNet pretrained convolutional network ...
- **p. 5 / 3 PRELIMINARIES - extractive body cue:** 5.1 MODEL Our model is built on a Transformer architecture (Vaswani et al., 2017) and takes a history of images and task description as input ...
- **p. 6 / 3 PRELIMINARIES - extractive body cue:** We use a standard categorical cross-entropy entropy objective and causal masking that was utilized in prior Transformer-based controllers (Reed et al., 2022; Lee et al., ...
- **p. 5 / 3 PRELIMINARIES - extractive body cue:** RT-1 tokenizes a history of 6 images by passing images through an ImageNet pretrained EfficientNet-B3 (Tan & Le, 2019) model, which takes 6 images of ...
- **p. 3 / 3 PRELIMINARIES - extractive body cue:** The goal is to learn a policy π that maximizes the average reward, in expectation over a distribution of instructions, starting states x0, and transition ...

## Design Rationale

- **p. 2 / 3 Hz - extractive body cue:** We propose a novel architecture that we call RT-1 (Robotics Transformer 1), which by encoding high-dimensional inputs and outputs, including camera images, instructions and motor ...
- **p. 1 / ABSTRACT - extractive body cue:** In this paper, we present a model class, dubbed Robotics Transformer, that exhibits promising scalable model properties.
- **p. 4 / 3 PRELIMINARIES - extractive body cue:** 2 (a), consists of partial counters and is constructed for large scale data collection.

## Source Evidence Cues

- **p. 2 / 3 Hz - extractive body cue:** We propose a novel architecture that we call RT-1 (Robotics Transformer 1), which by encoding high-dimensional inputs and outputs, including camera images, instructions and motor ...
- **p. 6 / 3 PRELIMINARIES - extractive body cue:** The Transformer is a decoder-only sequence model with 8 self-attention layers and 19M total parameters that outputs action tokens.
- **p. 4 / 3 PRELIMINARIES - extractive body cue:** 5 RT-1: ROBOTICS TRANSFORMER In this section, we describe how we tokenize the images, text, and actions, and then discuss the RT-1 model architecture.
- **p. 4 / 3 PRELIMINARIES - extractive body cue:** To this end, the architecture (shown in Figure 1a) leverages several elements: first the images and text are processed via an ImageNet pretrained convolutional network ...
- **p. 5 / 3 PRELIMINARIES - extractive body cue:** 5.1 MODEL Our model is built on a Transformer architecture (Vaswani et al., 2017) and takes a history of images and task description as input ...
- **p. 6 / 3 PRELIMINARIES - extractive body cue:** We use a standard categorical cross-entropy entropy objective and causal masking that was utilized in prior Transformer-based controllers (Reed et al., 2022; Lee et al., ...
- **p. 5 / 3 PRELIMINARIES - extractive body cue:** RT-1 tokenizes a history of 6 images by passing images through an ImageNet pretrained EfficientNet-B3 (Tan & Le, 2019) model, which takes 6 images of ...
- **Detected method headings:** B MODEL CARD (p. 20); C MODEL AND DATA (p. 20); C.1 MODEL INFERENCE (p. 20); C.3 MODEL SELECTION AT SCALE (p. 22)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | We propose a novel architecture that we call RT-1 (Robotics Transformer 1), which by encoding high-dimensional inputs and outputs, including camera images, ... | p. 2 (3 Hz), p. 6 (3 PRELIMINARIES) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | The Transformer is a decoder-only sequence model with 8 self-attention layers and 19M total parameters that outputs action tokens. | p. 6 (3 PRELIMINARIES), p. 4 (3 PRELIMINARIES) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | 5 RT-1: ROBOTICS TRANSFORMER In this section, we describe how we tokenize the images, text, and actions, and then discuss the RT-1 ... | p. 4 (3 PRELIMINARIES), p. 4 (3 PRELIMINARIES) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / 3 PRELIMINARIES - extractive body cue:** The goal is to learn a policy π that maximizes the average reward, in expectation over a distribution of instructions, starting states x0, and transition ...
- **p. 4 / 3 PRELIMINARIES - extractive body cue:** We learn π using behavioral cloning (Pomerleau, 1988), which optimizes π by minimizing the negative log-likelihood of actions at given the images and language instructions.
- **p. 6 / 3 PRELIMINARIES - extractive body cue:** We use a standard categorical cross-entropy entropy objective and causal masking that was utilized in prior Transformer-based controllers (Reed et al., 2022; Lee et al., ...
- **p. 3 / 3 PRELIMINARIES - extractive body cue:** At the end of an episode, the agent will be given a binary reward r ∈{0, 1} indicating whether the robot performed the instruction i.
- **p. 4 / 3 PRELIMINARIES - extractive body cue:** Specifically, we assume access to a dataset D = {(i(n), {(x(n) t , a(n) t )}T (n) t=0 )}N n=0 of episodes, all of which ...
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 6 (3 PRELIMINARIES).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | RT-1, takes, short, sequence, images, natural, language, instruction, input, outputs, action, robot, time, step | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | RT-1, takes, short, sequence, images, natural, language, instruction, input, outputs | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | novel, architecture, call, RT-1, Robotics, Transformer, encoding, high-dimensional, inputs, outputs | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | goal, learn, policy, maximizes, average, reward, expectation, over, distribution, instructions | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 3 PRELIMINARIES - extractive body cue:** RT-1 takes a short sequence of images and a natural language instruction as input and outputs an action for the robot at each time step.
- **p. 2 / 3 Hz - extractive body cue:** We propose a novel architecture that we call RT-1 (Robotics Transformer 1), which by encoding high-dimensional inputs and outputs, including camera images, instructions and motor ...
- **p. 3 / 3 PRELIMINARIES - extractive body cue:** At timestep t = 0, the policy π is presented with a language instruction i and an initial image observation x0.
- **p. 2 / 3 Hz - extractive body cue:** (1+γ) β · + Action (a) RT-1 takes images and natural language instructions and outputs discretized base and arm actions.
- **p. 3 / 3 PRELIMINARIES - extractive body cue:** The goal is to learn a policy π that maximizes the average reward, in expectation over a distribution of instructions, starting states x0, and transition ...
- **p. 5 / 3 PRELIMINARIES - extractive body cue:** 5.1 MODEL Our model is built on a Transformer architecture (Vaswani et al., 2017) and takes a history of images and task description as input ...
- **p. 4 / 3 PRELIMINARIES - extractive body cue:** As detailed in the next section, we parameterize π by first mapping inputs i, {xj}t j=0 to a sequence {ξh}H h=0 and action outputs at ...
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | These evaluations consist of 15 long-horizon instructions in two real kitchens, which require executing sequences of skills consisting of ∼10 distinct steps, ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | RT-1 takes a short sequence of images and a natural language instruction as input and outputs an action for the robot at ... | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not recovered | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | RT-1 performs closed-loop control and commands actions at 3 Hz until it either yields a "terminate" action or hits a pre-set time ... | hardware, batch and throughput |

## Training vs Inference

- **p. 2 / 3 Hz - extractive body cue:** We propose a novel architecture that we call RT-1 (Robotics Transformer 1), which by encoding high-dimensional inputs and outputs, including camera images, instructions and motor ...
- **p. 4 / 3 PRELIMINARIES - extractive body cue:** To this end, the architecture (shown in Figure 1a) leverages several elements: first the images and text are processed via an ImageNet pretrained convolutional network ...
- **p. 5 / 3 PRELIMINARIES - extractive body cue:** RT-1 tokenizes a history of 6 images by passing images through an ImageNet pretrained EfficientNet-B3 (Tan & Le, 2019) model, which takes 6 images of ...
- **p. 8 / 6 EXPERIMENTS - extractive body cue:** In order to run Gato on real robots at a high enough frequency, we also limit the size of the model compared to the original ...
- **p. 8 / 6 EXPERIMENTS - extractive body cue:** It also does not include inference time considerations that are necessary for real robots as discussed in Sec.
- **p. 9 / 6 EXPERIMENTS - extractive body cue:** These evaluations consist of 15 long-horizon instructions in two real kitchens, which require executing sequences of skills consisting of ∼10 distinct steps, with each step ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** novel, architecture, call, RT-1, Robotics, Transformer, encoding, high-dimensional, inputs, outputs, including, camera, images, instructions, motor, commands, compact, token, representations, allows.
- **Relevant PDF headings:** B MODEL CARD (p. 20); C MODEL AND DATA (p. 20); C.1 MODEL INFERENCE (p. 20); C.3 MODEL SELECTION AT SCALE (p. 22).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | It also improves real-world generalization on simulated objects used with skills seen only in the real world (+26%), e.g. "move X to ... | p. 12 (6 EXPERIMENTS), p. 9 (6 EXPERIMENTS) |
| Action / skill decoding | (Appendix Section D.4) Throughout this section we will compare to two baseline state of the art architectures, Gato (Reed et al., 2022) ... | p. 8 (6 EXPERIMENTS), p. 8 (6 EXPERIMENTS) |
| Receding execution / feedback | Table 5: Experimental results for mixing data from two different robots. Incorporating Kuka bin- picking data from QT-Opt (Kalashnikov et al., 2018) ... | p. 13 (Figure/Table caption), p. 13 (6 EXPERIMENTS) |

## Failure and Ablation Link

- **p. 13 / Figure/Table caption - extractive body cue:** Table 5: Experimental results for mixing data from two different robots. Incorporating Kuka bin- picking data from QT-Opt (Kalashnikov et al., 2018) in RT-1 minimally ...
- **p. 8 / 6 EXPERIMENTS - extractive body cue:** First, it computes image tokens without the notion of language and each image token embedding is computed separately for each image patch, as opposed to ...
- **p. 10 / 6 EXPERIMENTS - extractive body cue:** We demonstrate how RT1 can incorporate and learn from vastly different data sources and improve from such data without sacrificing its original-tasks performance across the ...
- **p. 14 / 6 EXPERIMENTS - extractive body cue:** Generalization Models % Tasks % Data Seen Tasks All Unseen Tasks Distractors Backgrounds Smaller Data RT-1 (ours) 100 100 97 73 76 83 59 RT-1 ...
- **p. 24 / Figure/Table caption - extractive body cue:** Figure 11: "Realistic instructions" evaluations propose realistic scenarios multiple distribution shifts that incrementally increase in difficulty. L1 generalization introduces a new real office kitchen with ...
- **p. 29 / Figure/Table caption - extractive body cue:** Table 11: SayCan style long horizon tasks in Kitchen1 and Kitchen2. (*Original SayCan eval uses a slightly different prompt so the planning success rate is ...
- **p. 10 / 6 EXPERIMENTS - extractive body cue:** We further ablate different components of RT-1 in the next section to better understand what aspects of our method contribute the most to this difference.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 2 (3 Hz), p. 6 (3 PRELIMINARIES), p. 4 (3 PRELIMINARIES), p. 4 (3 PRELIMINARIES), p. 5 (3 PRELIMINARIES), p. 6 (3 PRELIMINARIES), objective p. 3 (3 PRELIMINARIES), p. 4 (3 PRELIMINARIES), p. 6 (3 PRELIMINARIES), p. 3 (3 PRELIMINARIES), p. 4 (3 PRELIMINARIES), temporal p. 9 (6 EXPERIMENTS), p. 4 (3 PRELIMINARIES), p. 4 (3 PRELIMINARIES), p. 8 (6 EXPERIMENTS), p. 9 (6 EXPERIMENTS), p. 14 (6 EXPERIMENTS).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
