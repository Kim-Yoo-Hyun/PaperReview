# Method - DAM-VLA: A Dynamic Action Model-Based Vision-Language-Action Framework for Robot Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_3.html; PDF retrieval source: https://arxiv.org/pdf/2603.00926v1. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 4 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD), p. 3 (III. METHOD), p. 5 (III. METHOD), p. 5 (III. METHOD)): The resulting output consists of the cognition and reasoning latents, f cog and f rea, respectively. f rea and f cog are derived from the hidden features of the second ...

## Method Body Digest

- **p. 4 / III. METHOD - extractive PDF cue:** The resulting output consists of the cognition and reasoning latents, f cog and f rea, respectively. f rea and f cog are derived from the ...
- **p. 3 / III. METHOD - extractive PDF cue:** In Figure 3, the architecture of DAM-VLA is shown to consist of three key components: 1) A vision-language model, that encodes information from observation ot ...
- **p. 4 / III. METHOD - extractive PDF cue:** Dual-Scale Action Weighting To enhance the robustness in distinguishing between arm movement and gripper manipulation, we propose a dualscale action weighting mechanism for model training, ...
- **p. 3 / III. METHOD - extractive PDF cue:** To fully leverage the specific manipulation capabilities of different action models and the VLM's inherent reasoning capabilities, we introduce an action routing mechanism and our ...
- **p. 5 / III. METHOD - extractive PDF cue:** To reflect the prior that the action model requires higher precision and supervision focus immediately before the state change, we assign a larger variance to ...
- **p. 5 / III. METHOD - extractive PDF cue:** Arm Movement Arm Movement Gripper Manipulation Gripper Manipulation Time Trajectory Weight 1.0 0.0 1.0 0.0 Action Chunk Weight Chunk Index Fig.
- **p. 4 / III. METHOD - extractive PDF cue:** The output is the predicted weight w, which is supervised by the following cross-entropy loss: Lclass = // -( ˆw log(w) + (1 -ˆw) log(1 ...
- **p. 5 / III. METHOD - extractive PDF cue:** This weight ˆw acts as the ground-truth label for the predicted weight w, supervised via the cross-entropy loss Lclass.

## Design Rationale

- **p. 2 / I. INTRODUCTION - extractive PDF cue:** Rather than loosely coupling a VLM with separate action models, we introduce the DAM-VLA framework (Figure 1), which fully exploits the strengths of VLMs to ...
- **p. 3 / III. METHOD - extractive PDF cue:** Overall Architecture Our goal is to develop a dynamic action model-based VLA framework that enables different robots to physically execute diverse tasks in dynamic environments ...
- **p. 3 / III. METHOD - extractive PDF cue:** The vision model consists of powerful

## Source Evidence Cues

- **p. 4 / III. METHOD - extractive PDF cue:** The resulting output consists of the cognition and reasoning latents, f cog and f rea, respectively. f rea and f cog are derived from the ...
- **p. 3 / III. METHOD - extractive PDF cue:** In Figure 3, the architecture of DAM-VLA is shown to consist of three key components: 1) A vision-language model, that encodes information from observation ot ...
- **p. 4 / III. METHOD - extractive PDF cue:** Dual-Scale Action Weighting To enhance the robustness in distinguishing between arm movement and gripper manipulation, we propose a dualscale action weighting mechanism for model training, ...
- **p. 3 / III. METHOD - extractive PDF cue:** To fully leverage the specific manipulation capabilities of different action models and the VLM's inherent reasoning capabilities, we introduce an action routing mechanism and our ...
- **p. 5 / III. METHOD - extractive PDF cue:** To reflect the prior that the action model requires higher precision and supervision focus immediately before the state change, we assign a larger variance to ...
- **p. 5 / III. METHOD - extractive PDF cue:** Arm Movement Arm Movement Gripper Manipulation Gripper Manipulation Time Trajectory Weight 1.0 0.0 1.0 0.0 Action Chunk Weight Chunk Index Fig.
- **Detected method headings:** III. METHOD (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | The resulting output consists of the cognition and reasoning latents, f cog and f rea, respectively. f rea and f cog are ... | p. 4 (III. METHOD), p. 3 (III. METHOD) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | In Figure 3, the architecture of DAM-VLA is shown to consist of three key components: 1) A vision-language model, that encodes information ... | p. 3 (III. METHOD), p. 4 (III. METHOD) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | Dual-Scale Action Weighting To enhance the robustness in distinguishing between arm movement and gripper manipulation, we propose a dualscale action weighting mechanism ... | p. 4 (III. METHOD), p. 3 (III. METHOD) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / III. METHOD - extractive PDF cue:** The output is the predicted weight w, which is supervised by the following cross-entropy loss: Lclass = // -( ˆw log(w) + (1 -ˆw) log(1 ...
- **p. 5 / III. METHOD - extractive PDF cue:** This weight ˆw acts as the ground-truth label for the predicted weight w, supervised via the cross-entropy loss Lclass.
- **p. 4 / III. METHOD - extractive PDF cue:** The total loss is computed as a weighted sum of the movement loss, the manipulation loss, and the classification loss.
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 4 (III. METHOD), p. 4 (III. METHOD), p. 5 (III. METHOD).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Overall, Architecture, goal, develop, dynamic, action, model-based, VLA, framework, enables, different, robots, physically, execute | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | Overall, Architecture, goal, develop, dynamic, action, model-based, VLA, framework, enables | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | Rather, loosely, coupling, VLM, separate, action, models, introduce, DAM-VLA, framework | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | output, predicted, weight, supervised, following, cross-entropy, loss, Lclass, acts, ground-truth | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / III. METHOD - extractive PDF cue:** Overall Architecture Our goal is to develop a dynamic action model-based VLA framework that enables different robots to physically execute diverse tasks in dynamic environments ...
- **p. 3 / III. METHOD - extractive PDF cue:** Formally, given the language instruction l and visual observation ot at time t, the model π predicts a temporal action sequence [at, at+1, ..., at+N] ...
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** By enabling robots to interpret visual observations and language instructions, VLA models can generate generalizable action sequences.
- **p. 4 / III. METHOD - extractive PDF cue:** The resulting output consists of the cognition and reasoning latents, f cog and f rea, respectively. f rea and f cog are derived from the ...
- **p. 4 / III. METHOD - extractive PDF cue:** Action Routing Mechanism and Dynamic Action Model To determine whether the action state is in arm movement or gripper manipulation, we design an action routing ...
- **p. 5 / III. METHOD - extractive PDF cue:** To reflect the prior that the action model requires higher precision and supervision focus immediately before the state change, we assign a larger variance to ...
- **p. 5 / III. METHOD - extractive PDF cue:** Given that prediction confidence typically decays as the temporal distance from the current state increases, we apply an exponentially decreasing function: wa j = γj, ...
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | Action-chunk-level Weights (wa): From a local perspective, we account for the inherent temporal uncertainty in action sequences. | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | These methods either condition on VLM-extracted features or jointly embed the denoising timestep and noisy actions into the token sequence during diffusion. | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not recovered | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / III. METHOD - extractive PDF cue:** Dual-Scale Action Weighting To enhance the robustness in distinguishing between arm movement and gripper manipulation, we propose a dualscale action weighting mechanism for model training, ...
- **p. 5 / IV. EXPERIMENTS - extractive PDF cue:** The fine-tuning process adopts the same hyperparameters as pre-training: a learning rate of 2 × 10-5 and a batch size of 256, utilizing 8 NVIDIA ...
- **p. 5 / IV. EXPERIMENTS - extractive PDF cue:** Our VLA model is trained using a constant learning rate of 2 × 10-5 and a batch size of 256 on 8 NVIDIA H100 GPUs ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** resulting, output, consists, cognition, reasoning, latents, respectively, derived, hidden, features, second, last, transformer, layers, LLM, serves, input, subsequent, action, routing.
- **Relevant PDF headings:** III. METHOD (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | Simulated Evaluations We first evaluate our method using the SIMPLER simulation [14], a suite of open-source simulated environments designed to mirror common ... | p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |
| Action / skill decoding | Fig. 1: DAM-VLA framework and experimental results. (a) We propose a DAM-VLA framework that dynamically integrates the inherent reasoning capabilities of VLMs ... | p. 1 (Figure/Table caption), p. 6 (Figure/Table caption) |
| Receding execution / feedback | Fig. 1: DAM-VLA framework and experimental results. (a) We propose a DAM-VLA framework that dynamically integrates the inherent reasoning capabilities of VLMs ... | p. 1 (Figure/Table caption), p. 6 (IV. EXPERIMENTS) |

## Failure and Ablation Link

- **p. 5 / IV. EXPERIMENTS - extractive PDF cue:** Section IV-D provides an ablation study to analyze the contribution of each component in our framework.
- **p. 5 / IV. EXPERIMENTS - extractive PDF cue:** Method / Google(VA) Success Rates on Different Tasks Avg PCC MN OCD ODPA RT-1 [3] 90% 46% 35% 3% 44% RT-1-X [44] 49% 33% 29% ...
- **p. 6 / IV. EXPERIMENTS - extractive PDF cue:** For the Google robot, evaluations are conducted under both Visual Matching (VM) and Variant Aggregation (VA) settings across four tasks, whereas the WidowX robot is ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Fig. 3: The architecture of our DAM-VLA. Given an RGB image observation and a task description, the model predicts a sequence of temporal actions. The ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Fig. 6: The evaluation encompasses both in-distribution and out-of-distribution scenarios. The in-distribution setting includes variations in object positions and lighting conditions consistent with the training ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Fig. 3: The architecture of our DAM-VLA. Given an RGB image observation and a task description, the model predicts a sequence of temporal actions. The ...
- **p. 4 / III. METHOD - extractive PDF cue:** Additionally, both models receive random noise nrand as input to facilitate the diffusion process.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 4 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD), p. 3 (III. METHOD), p. 5 (III. METHOD), p. 5 (III. METHOD), objective p. 4 (III. METHOD), p. 5 (III. METHOD), p. 4 (III. METHOD), temporal p. 5 (III. METHOD), p. 2 (I. INTRODUCTION), p. 3 (III. METHOD), p. 4 (III. METHOD), p. 4 (III. METHOD), p. 5 (III. METHOD).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
