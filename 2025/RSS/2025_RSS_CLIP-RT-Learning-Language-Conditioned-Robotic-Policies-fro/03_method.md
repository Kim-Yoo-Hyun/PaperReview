# Method - CLIP-RT: Learning Language-Conditioned Robotic Policies from Natural Language Supervision

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (12 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p016.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p016.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 4 (C. In-Domain Data Collection), p. 2 (Abstract), p. 2 (Abstract), p. 4 (B. CLIP-Based Robotics Transformer (CLIP-RT)), p. 1 (Abstract), p. 3 (B. CLIP-Based Robotics Transformer (CLIP-RT))): Stochastic Trajectory Augmentation (STA) aims to augment the demonstration data collected from language-based teleoperation, Before delving into the details, we fist define & waypoint as a key state in demonstrations ...

## Method Body Digest

- **p. 4 / C. In-Domain Data Collection - extractive body cue:** Stochastic Trajectory Augmentation (STA) aims to augment the demonstration data collected from language-based teleoperation, Before delving into the details, we fist define & waypoint as ...
- **p. 2 / Abstract - extractive body cue:** First, we propose CLIP-RT, 4 vision-language-action (VLA) model that learns languageconditioned policies from natural language supervision.
- **p. 2 / Abstract - extractive body cue:** We introduce a vision-language-action (VLA) model that Jearns language-conditioned visuomotor policies from natural language supervision, which we call CLIP-RT (CLIP-based Robotics Transformer).
- **p. 4 / B. CLIP-Based Robotics Transformer (CLIP-RT) - extractive body cue:** It consists of an image encoder {12] and a text encoder [44], both built on Transformer [57].
- **p. 1 / Abstract - extractive body cue:** We then present CLIP-RT, a new vision-language-action (VLA) model that learns language-conditioned visuomotor polices from this supervision.
- **p. 3 / B. CLIP-Based Robotics Transformer (CLIP-RT) - extractive body cue:** Specifically, CLIP-RT first extracts vector embeddings of vj, é and uj using the CLIP model's image encoder f(-) and the text encoder g(-), and
- **p. 1 / Abstract - extractive body cue:** We thus explore a method for training robotic skills through natural language. ‘To this tend, we propose a data collection framework that enables non-experts to ...
- **p. 3 / B. CLIP-Based Robotics Transformer (CLIP-RT) - extractive body cue:** The loss function maximizes the cosine similarity between context and language supervision for positive pairs, while minimizing it for negative pairs.

## Design Rationale

- **p. 2 / Abstract - extractive body cue:** Sec- ‘ond, we propose a data collection framework that enables non-experts to collect robot data only through natural language and augment the human-collected demonstration data, ...
- **p. 1 / Abstract - extractive body cue:** We thus explore a method for training robotic skills through natural language. ‘To this tend, we propose a data collection framework that enables non-experts to ...
- **p. 1 / Abstract - extractive body cue:** It consists of two steps: Ianguage-based teleoperation and stochastic trajectory augmentation (STA).

## Source Evidence Cues

- **p. 4 / C. In-Domain Data Collection - extractive body cue:** Stochastic Trajectory Augmentation (STA) aims to augment the demonstration data collected from language-based teleoperation, Before delving into the details, we fist define & waypoint as ...
- **p. 2 / Abstract - extractive body cue:** First, we propose CLIP-RT, 4 vision-language-action (VLA) model that learns languageconditioned policies from natural language supervision.
- **p. 2 / Abstract - extractive body cue:** We introduce a vision-language-action (VLA) model that Jearns language-conditioned visuomotor policies from natural language supervision, which we call CLIP-RT (CLIP-based Robotics Transformer).
- **p. 4 / B. CLIP-Based Robotics Transformer (CLIP-RT) - extractive body cue:** It consists of an image encoder {12] and a text encoder [44], both built on Transformer [57].
- **p. 1 / Abstract - extractive body cue:** We then present CLIP-RT, a new vision-language-action (VLA) model that learns language-conditioned visuomotor polices from this supervision.
- **p. 3 / B. CLIP-Based Robotics Transformer (CLIP-RT) - extractive body cue:** Specifically, CLIP-RT first extracts vector embeddings of vj, é and uj using the CLIP model's image encoder f(-) and the text encoder g(-), and
- **p. 1 / Abstract - extractive body cue:** We thus explore a method for training robotic skills through natural language. ‘To this tend, we propose a data collection framework that enables non-experts to ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | Stochastic Trajectory Augmentation (STA) aims to augment the demonstration data collected from language-based teleoperation, Before delving into the details, we fist define ... | p. 4 (C. In-Domain Data Collection), p. 2 (Abstract) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | First, we propose CLIP-RT, 4 vision-language-action (VLA) model that learns languageconditioned policies from natural language supervision. | p. 2 (Abstract), p. 2 (Abstract) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | We introduce a vision-language-action (VLA) model that Jearns language-conditioned visuomotor policies from natural language supervision, which we call CLIP-RT (CLIP-based Robotics Transformer). | p. 2 (Abstract), p. 4 (B. CLIP-Based Robotics Transformer (CLIP-RT)) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / B. CLIP-Based Robotics Transformer (CLIP-RT) - extractive body cue:** The loss function maximizes the cosine similarity between context and language supervision for positive pairs, while minimizing it for negative pairs.
- **p. 3 / A. Preliminaries - extractive body cue:** Given a mini-batch of .M image-text pairs {(Js,T;)}2,. the two encoders are jointly optimized to ‘maximize the similarity between the correct pairs of image and ...
- **p. 2 / A. Preliminaries - extractive body cue:** The goal of languageconditioned imitation learning is minimizing the negative loglikelihood of the expert action «, given the observation history Diy = (Uieoe-s U4) and ...
- **p. 7 / 256 33% - extractive body cue:** "Move arm to the right", but GPT labels this motion as inappropriate and provide positive rewards to the motion, "Move arm to the left", leading ...
- **p. 4 / B. CLIP-Based Robotics Transformer (CLIP-RT) - extractive body cue:** A key advantage of this codebase is that strong CLIP models are continuously updated to the dashboard, enabling users to easily use them through a ...
- **p. 2 / Abstract - extractive body cue:** During deployment, humans provide language feedback to correct robotic behaviors, and policies are updated based on this feedback.
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 3 (A. Preliminaries), p. 3 (A. Preliminaries), p. 2 (Abstract), p. 4 (B. CLIP-Based Robotics Transformer (CLIP-RT)).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | goal, languageconditioned, imitation, learning, minimizing, negative, loglikelihood, expert, action, given, observation, history, Diy, Uieoe-s | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | goal, languageconditioned, imitation, learning, minimizing, negative, loglikelihood, expert, action, given | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | Sec-, data, collection, framework, enables, non-experts, collect, robot, only, through | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | loss, function, maximizes, cosine, similarity, between, context, language, supervision, positive | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / A. Preliminaries - extractive body cue:** The goal of languageconditioned imitation learning is minimizing the negative loglikelihood of the expert action «, given the observation history Diy = (Uieoe-s U4) and ...
- **p. 2 / A. Preliminaries - extractive body cue:** To ‘maintain consistency with the pretraining setup of the VLMs, existing VLA models (7, 29, 3] typically use a single-image observation v, rather than utilizing ...
- **p. 7 / 256 33% - extractive body cue:** We also investigate how CLIP-RT can collaborate with a large pretrained model-GPT-4o [24] (GPT for short)-through action refinement, As shown in Figure 8, at each ...
- **p. 3 / B. CLIP-Based Robotics Transformer (CLIP-RT) - extractive body cue:** CLIP-RT takes amini-batch of M triplets {(v,., us) 4. where v, 6, and u denote image observation, instruction, and language supervision.
- **p. 7 / 256 33% - extractive body cue:** Given an image and language instruction (top), CLIP-RT produces initial scores for candidate actions (left).
- **p. 1 / Abstract - extractive body cue:** One key challenge for intelligent robots is grounding natural language to vision and action, bridging the abstraction gap between natural language instruction and visuomotor control ...
- **p. 3 / B. CLIP-Based Robotics Transformer (CLIP-RT) - extractive body cue:** Consequently, CLIP-RT learns to measure the likelihood of each motion described in language, given visual observation and language instruction,
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | Current vision-language-action models, including CLIP-RT, do not predict sequences of actions or consider the history of actions taken, This absence of temporal ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | At each time step, CLIP-RT computes pairwise similarities between the context and a list of language-based motion primitives. | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | Current vision-language-action models, including CLIP-RT, do not predict sequences of actions or consider the history of actions taken, This absence of temporal ... | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | Finally, the camera captures the cutent image observation and the robot executes the translated action, Consequently, we can obtain a sequence of ... | hardware, batch and throughput |

## Training vs Inference

- **p. 1 / Abstract - extractive body cue:** We thus explore a method for training robotic skills through natural language. ‘To this tend, we propose a data collection framework that enables non-experts to ...
- **p. 8 / B. Adapting CLIP-RT to the LIBERO Benchmark - extractive body cue:** We train CLIP-RT+ using 8 NVIDIA H100 GPUs for 128 epochs with a batch size of 256.
- **p. 5 / C. Experiments on Common and Novel Tasks - extractive body cue:** ‘+ OpenVLA [29] is a state-of-the-art, open-source visionlanguage-action (VLA) model. ‘This model leverages the 7B-parameter Llama2 language model [55] and a sual encoder that combines ...
- **p. 1 / Abstract - extractive body cue:** In simulated environments, CLIP-RP also yields strong performance, achieving a 92.8% average success rate on the LIBERO benchmark with an inference throughput of 163 Hz.
- **p. 2 / Abstract - extractive body cue:** CLIP-RT achieves strong results, an average success rate of 92.8%, with an improved inference throughput of 163Hz.
- **p. 3 / A. Preliminaries - extractive body cue:** Using the contrastive objective, CLIP trains an image encoder f(:) and a text encoder q(-) on 400M image-text pairs.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Stochastic, Trajectory, Augmentation, STA, aims, augment, demonstration, data, collected, language-based, teleoperation, Before, delving, details, fist, define, waypoint, state, demonstrations, satisfies.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | This set of tasks serves as a benchmark for evaluating the model's ability to acquire new skills using in-domain data, We first ... | p. 5 (A. Tasks & Dataset), p. 9 (B. Adapting CLIP-RT to the LIBERO Benchmark) |
| Action / skill decoding | We introduce baseline ‘models and then discuss the results in detail | p. 5 (C. Experiments on Common and Novel Tasks), p. 5 (C. Experiments on Common and Novel Tasks) |
| Receding execution / feedback | As shown in Table I, the recent state-of-the-art VLA model, OpenVLA-OFT [30], achieves the highest average success rate of 95.3%. | p. 9 (B. Adapting CLIP-RT to the LIBERO Benchmark), p. 9 (B. Adapting CLIP-RT to the LIBERO Benchmark) |

## Failure and Ablation Link

- **p. 5 / C. Experiments on Common and Novel Tasks - extractive body cue:** «+ CLIP-RT-Zero is an ablated model trained solely on the ‘OXE dataset without accessing any in-domain data,
- **p. 5 / C. Experiments on Common and Novel Tasks - extractive body cue:** We also fine-tune OpenVLA, ‘on the same in-domain data as CLIP-RT by using lowlevel 7D end-effector actions as supervision.
- **p. 9 / B. Adapting CLIP-RT to the LIBERO Benchmark - extractive body cue:** This modification enables us to evaluate the core architectural strengths of CLIP-RT-language-based policy pretraining and lightweight design-on a widely used simulation benchmark (LIBERO), ‘The results ...
- **p. 9 / B. Adapting CLIP-RT to the LIBERO Benchmark - extractive body cue:** All models, except Diffusion Policy (DP) [10], were fine-tuned.
- **p. 9 / B. Limitations and Future Work - extractive body cue:** Inherent Limitations in Human Language Supervision.
- **p. 9 / B. Limitations and Future Work - extractive body cue:** Without incorporating action history into the context, the model cannot make informed
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 9: Example failure cases of CLIP-RT. (a) CLIP-RT

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 4 (C. In-Domain Data Collection), p. 2 (Abstract), p. 2 (Abstract), p. 4 (B. CLIP-Based Robotics Transformer (CLIP-RT)), p. 1 (Abstract), p. 3 (B. CLIP-Based Robotics Transformer (CLIP-RT)), objective p. 3 (B. CLIP-Based Robotics Transformer (CLIP-RT)), p. 3 (A. Preliminaries), p. 2 (A. Preliminaries), p. 7 (256 33%), p. 4 (B. CLIP-Based Robotics Transformer (CLIP-RT)), p. 2 (Abstract), temporal p. 9 (B. Limitations and Future Work), p. 4 (B. CLIP-Based Robotics Transformer (CLIP-RT)), p. 4 (C. In-Domain Data Collection), p. 9 (B. Adapting CLIP-RT to the LIBERO Benchmark), p. 1 (Abstract), p. 1 (Abstract).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
