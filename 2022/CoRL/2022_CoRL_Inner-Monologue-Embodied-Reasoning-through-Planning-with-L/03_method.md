# Method - Inner Monologue: Embodied Reasoning through Planning with Language Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (25 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v205/huang23c.html; PDF retrieval source: https://arxiv.org/pdf/2207.05608. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 16 (A.2 Inner Monologue for Real-World Tabletop Rearrangement), p. 17 (A.2 Inner Monologue for Real-World Tabletop Rearrangement), p. 17 (A.2 Inner Monologue for Real-World Tabletop Rearrangement), p. 15 (A.1 Inner Monologue for Simulated Tabletop Rearrangement), p. 16 (A.2 Inner Monologue for Real-World Tabletop Rearrangement), p. 15 (A.1 Inner Monologue for Simulated Tabletop Rearrangement)): Low-level Policies We use a single low-level policy for the real tabletop rearrangement environment that is responsible for performing object-centric pick and place actions as instructed by the language model.

## Method Body Digest

- **p. 16 / A.2 Inner Monologue for Real-World Tabletop Rearrangement - extractive body cue:** Low-level Policies We use a single low-level policy for the real tabletop rearrangement environment that is responsible for performing object-centric pick and place actions as ...
- **p. 17 / A.2 Inner Monologue for Real-World Tabletop Rearrangement - extractive body cue:** The input to the model consists of: (1) o0, the initial image observation, (2) of, the final image observation after the policy chose to terminate ...
- **p. 17 / A.2 Inner Monologue for Real-World Tabletop Rearrangement - extractive body cue:** Given the first and last observation, the model outputs a probability distribution over all the possible skills.
- **p. 15 / A.1 Inner Monologue for Simulated Tabletop Rearrangement - extractive body cue:** At the start of the action plan, the language model first generates a list of desired sub-goals given the high-level instruction.
- **p. 16 / A.2 Inner Monologue for Real-World Tabletop Rearrangement - extractive body cue:** To perform the pick and place motions, the robot moves to a position 15cm above the intended pick or place position, and then it slowly ...
- **p. 15 / A.1 Inner Monologue for Simulated Tabletop Rearrangement - extractive body cue:** Large Language Model We use InstructGPT [91], a 1.3B parameter language model fine-tuned from GPT-3 [9] with human feedback, accessed through OpenAI API.
- **p. 18 / A.2 Inner Monologue for Real-World Tabletop Rearrangement - extractive body cue:** (Left) The foresight model predicts whether a given instruction was successfully achieved between the first and last image.
- **p. 17 / A.2 Inner Monologue for Real-World Tabletop Rearrangement - extractive body cue:** The model is trained with the binary cross entropy loss with respect to the ground truth binary label.

## Design Rationale

- **p. 1 / 1 Introduction - extractive body cue:** Inspired by the human thought process, we propose that such an inner monologue is a natural framework for incorporating feedback for LLMs.
- **p. 2 / 1 Introduction - extractive body cue:** Robot Success Detector Scene Descriptor (b) (c) (a) Human Figure 1: Inner Monologue enables grounded closed-loop feedback for robot planning with large language models by ...
- **p. 17 / A.2 Inner Monologue for Real-World Tabletop Rearrangement - extractive body cue:** The input to the model consists of: (1) o0, the initial image observation, (2) of, the final image observation after the policy chose to terminate ...

## Source Evidence Cues

- **p. 16 / A.2 Inner Monologue for Real-World Tabletop Rearrangement - extractive body cue:** Low-level Policies We use a single low-level policy for the real tabletop rearrangement environment that is responsible for performing object-centric pick and place actions as ...
- **p. 17 / A.2 Inner Monologue for Real-World Tabletop Rearrangement - extractive body cue:** The input to the model consists of: (1) o0, the initial image observation, (2) of, the final image observation after the policy chose to terminate ...
- **p. 17 / A.2 Inner Monologue for Real-World Tabletop Rearrangement - extractive body cue:** Given the first and last observation, the model outputs a probability distribution over all the possible skills.
- **p. 15 / A.1 Inner Monologue for Simulated Tabletop Rearrangement - extractive body cue:** At the start of the action plan, the language model first generates a list of desired sub-goals given the high-level instruction.
- **p. 16 / A.2 Inner Monologue for Real-World Tabletop Rearrangement - extractive body cue:** To perform the pick and place motions, the robot moves to a position 15cm above the intended pick or place position, and then it slowly ...
- **p. 15 / A.1 Inner Monologue for Simulated Tabletop Rearrangement - extractive body cue:** Large Language Model We use InstructGPT [91], a 1.3B parameter language model fine-tuned from GPT-3 [9] with human feedback, accessed through OpenAI API.
- **p. 18 / A.2 Inner Monologue for Real-World Tabletop Rearrangement - extractive body cue:** (Left) The foresight model predicts whether a given instruction was successfully achieved between the first and last image.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | Low-level Policies We use a single low-level policy for the real tabletop rearrangement environment that is responsible for performing object-centric pick and ... | p. 16 (A.2 Inner Monologue for Real-World Tabletop Rearrangement), p. 17 (A.2 Inner Monologue for Real-World Tabletop Rearrangement) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | The input to the model consists of: (1) o0, the initial image observation, (2) of, the final image observation after the policy ... | p. 17 (A.2 Inner Monologue for Real-World Tabletop Rearrangement), p. 17 (A.2 Inner Monologue for Real-World Tabletop Rearrangement) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | Given the first and last observation, the model outputs a probability distribution over all the possible skills. | p. 17 (A.2 Inner Monologue for Real-World Tabletop Rearrangement), p. 15 (A.1 Inner Monologue for Simulated Tabletop Rearrangement) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 17 / A.2 Inner Monologue for Real-World Tabletop Rearrangement - extractive body cue:** The model is trained with the binary cross entropy loss with respect to the ground truth binary label.
- **p. 17 / A.2 Inner Monologue for Real-World Tabletop Rearrangement - extractive body cue:** To train this model, we use the symmetric contrastive loss as used in CLIP (Fig 7b).
- **p. 18 / A.2 Inner Monologue for Real-World Tabletop Rearrangement - extractive body cue:** (Right) The hindsight model fine-tuned via contrastive loss as used in CLIP [65].
- **p. 15 / A.1 Inner Monologue for Simulated Tabletop Rearrangement - extractive body cue:** Environment Feedback: Passive Scene Description For Object + Scene method, we provide task-progress scene description as a list of achieved sub-goals after each pick-and-place execution.
- **p. 16 / A.2 Inner Monologue for Real-World Tabletop Rearrangement - extractive body cue:** The detector returns success if the difference between the two positions is less than a threshold.
- **p. 18 / A.2 Inner Monologue for Real-World Tabletop Rearrangement - extractive body cue:** We combine the foresight and hindsight model by first thresholding the probability from the foresight model by some value τ.
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 17 (A.2 Inner Monologue for Real-World Tabletop Rearrangement), p. 17 (A.2 Inner Monologue for Real-World Tabletop Rearrangement), p. 18 (A.2 Inner Monologue for Real-World Tabletop Rearrangement), p. 18 (A.2 Inner Monologue for Real-World Tabletop Rearrangement).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | demonstration, versatility, LLMs, grounded, closed-loop, feedback, additionally, several, surprising, capabilities, emerging, inner, monologue, formulation | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | demonstration, versatility, LLMs, grounded, closed-loop, feedback, additionally, several, surprising, capabilities | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | Inspired, human, thought, process, inner, monologue, natural, framework, incorporating, feedback | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | model, trained, binary, cross, entropy, loss, respect, ground, truth, label | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1 Introduction - extractive body cue:** As a demonstration of the versatility of LLMs and grounded closed-loop feedback, we additionally show several surprising capabilities emerging from the inner monologue formulation, including ...
- **p. 15 / A.1 Inner Monologue for Simulated Tabletop Rearrangement - extractive body cue:** The policy is trained on 20000 pre-collected demonstrations, where each demonstration contains 1) language instruction of the format "pick up [x] and place it on ...
- **p. 17 / A.2 Inner Monologue for Real-World Tabletop Rearrangement - extractive body cue:** The input to the model consists of: (1) o0, the initial image observation, (2) of, the final image observation after the policy chose to terminate ...
- **p. 16 / A.2 Inner Monologue for Real-World Tabletop Rearrangement - extractive body cue:** The policy takes as input 1) the bounding boxes of all the objects in the scene, 2) the names of the object to pick and ...
- **p. 2 / 1 Introduction - extractive body cue:** Our proposed system Inner Monologue chains together these various components (perception models, robotic skills, and human feedback) in a shared language prompt, enabling it to ...
- **p. 15 / A.1 Inner Monologue for Simulated Tabletop Rearrangement - extractive body cue:** At the start of the action plan, the language model first generates a list of desired sub-goals given the high-level instruction.
- **p. 1 / 1 Introduction - extractive body cue:** This raises an intriguing possibility: beyond their ability to interpret natural language instructions, can language models further serve as reasoning models that combine multiple sources ...
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | Intelligent and flexible embodied interaction requires robots to be able to deploy large repertoires of basic behaviors in appropriate ways, sequence these ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | Similar to ours are recent task planning approaches that leverage pre-trained autoregressive LLMs to decompose abstract, high-level instructions into a sequence of ... | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not recovered | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 15 / A.1 Inner Monologue for Simulated Tabletop Rearrangement - extractive body cue:** Large Language Model We use InstructGPT [91], a 1.3B parameter language model fine-tuned from GPT-3 [9] with human feedback, accessed through OpenAI API.
- **p. 17 / A.2 Inner Monologue for Real-World Tabletop Rearrangement - extractive body cue:** At inference time, similar to the CLIP 17
- **p. 17 / A.2 Inner Monologue for Real-World Tabletop Rearrangement - extractive body cue:** At inference time within Inner Monologue, we output the text "[success: no]" when the probability is below a certain threshold.
- **p. 18 / A.2 Inner Monologue for Real-World Tabletop Rearrangement - extractive body cue:** At inference time, the model is used infer among the possible instructions which one was achieved.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Low-level, Policies, single, policy, real, tabletop, rearrangement, environment, responsible, performing, object-centric, pick, place, actions, instructed, language, model, input, consists, initial.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | For the object sorting task, the scene description contains a list of currently visible objects and a list of objects that the ... | p. 16 (A.2 Inner Monologue for Real-World Tabletop Rearrangement), p. 17 (A.2 Inner Monologue for Real-World Tabletop Rearrangement) |
| Action / skill decoding | Table 2: Inner Monologue (with object recognition and success detection feedback) on a real pick and place robot exceeds the performance of ... | p. 6 (Figure/Table caption), p. 6 (Figure/Table caption) |
| Receding execution / feedback | Table 2: Inner Monologue (with object recognition and success detection feedback) on a real pick and place robot exceeds the performance of ... | p. 6 (Figure/Table caption), p. 7 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 6 / Figure/Table caption - extractive body cue:** Table 1: Success rates for various methods, averaged across 50 episodes in Ravens-based environment with test-time disturbances. CLIPort + oracle indicates that CLIPort was provided ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4: Failure causes on 120 evaluations. When disturbances are added (red), only the Inner Mono- logue variants consistently complete the instructions. Analysis. The results ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5: Informing LLM with embodied feedback enables many emergent capabilities, all of which are achieved without similar prompted examples. For instance, Inner Monologue can ...
- **p. 17 / A.2 Inner Monologue for Real-World Tabletop Rearrangement - extractive body cue:** We find that two such models, ViLD [77] and MDETR [92], perform worse than humans but still quite resonably at providing Object feedback, even without ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 2: Inner Monologue (with object recognition and success detection feedback) on a real pick and place robot exceeds the performance of baseline alternatives, as ...
- **p. 15 / A.1 Inner Monologue for Simulated Tabletop Rearrangement - extractive body cue:** Environment Feedback: Object Recognition We provide the list of objects present in the scene at the start of each episode for the language model (without ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: Inner Monologue enables grounded closed-loop feedback for robot planning with large language models by leveraging a collection of perception models (e.g., scene descriptors ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 16 (A.2 Inner Monologue for Real-World Tabletop Rearrangement), p. 17 (A.2 Inner Monologue for Real-World Tabletop Rearrangement), p. 17 (A.2 Inner Monologue for Real-World Tabletop Rearrangement), p. 15 (A.1 Inner Monologue for Simulated Tabletop Rearrangement), p. 16 (A.2 Inner Monologue for Real-World Tabletop Rearrangement), p. 15 (A.1 Inner Monologue for Simulated Tabletop Rearrangement), objective p. 17 (A.2 Inner Monologue for Real-World Tabletop Rearrangement), p. 17 (A.2 Inner Monologue for Real-World Tabletop Rearrangement), p. 18 (A.2 Inner Monologue for Real-World Tabletop Rearrangement), p. 15 (A.1 Inner Monologue for Simulated Tabletop Rearrangement), p. 16 (A.2 Inner Monologue for Real-World Tabletop Rearrangement), p. 18 (A.2 Inner Monologue for Real-World Tabletop Rearrangement), temporal p. 1 (1 Introduction), p. 2 (2 Related Work), p. 15 (A.1 Inner Monologue for Simulated Tabletop Rearrangement), p. 15 (A.1 Inner Monologue for Simulated Tabletop Rearrangement), p. 16 (A.2 Inner Monologue for Real-World Tabletop Rearrangement), p. 16 (A.2 Inner Monologue for Real-World Tabletop Rearrangement).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
