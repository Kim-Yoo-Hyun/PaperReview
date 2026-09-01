# Method - CodeDiffuser: Attention-Enhanced Diffusion Policy via VLM-Generated Code for Instruction Ambiguity

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (15 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p072.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p072.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 9 (B. Analysis of Existing Imitation Learning Algorithm), p. 6 (B. Analysis of Existing Imitation Learning Algorithm), p. 7 (B. Analysis of Existing Imitation Learning Algorithm), p. 7 (B. Analysis of Existing Imitation Learning Algorithm), p. 8 (B. Analysis of Existing Imitation Learning Algorithm), p. 8 (B. Analysis of Existing Imitation Learning Algorithm)): The training and testing scenarios coasist of a mixture of 1 10 4 picking optioas with 1 placing option, The success rate curve indicates that, given a sufficient ‘number of ...

## Method Body Digest

- **p. 9 / B. Analysis of Existing Imitation Learning Algorithm - extractive body cue:** The training and testing scenarios coasist of a mixture of 1 10 4 picking optioas with 1 placing option, The success rate curve indicates that, ...
- **p. 6 / B. Analysis of Existing Imitation Learning Algorithm - extractive body cue:** Specifically, We consider two state-of-the-art methods, Action Chunking Transformer (ACT) [6] and Diffusion Policy (DP) [1] in ‘comprehensive simulation evaluations.
- **p. 7 / B. Analysis of Existing Imitation Learning Algorithm - extractive body cue:** In this section, we investigate whether 3D attention is a suitable representation for visuomotor policy learning and evaluate the pipeline from 3D attention maps to ...
- **p. 7 / B. Analysis of Existing Imitation Learning Algorithm - extractive body cue:** These results confirm that the 3D attention map is a robust representation for downstream isuomotor policy learning in ambiguous task scenarios. ‘Additionally, we stress-test our ...
- **p. 8 / B. Analysis of Existing Imitation Learning Algorithm - extractive body cue:** + Lang-ACT with 3D Attention: Unlike the original ACT, which uses multi-view RGB observations, this baseline inputs 3D attention maps into Lang-ACT to assess whether ...
- **p. 8 / B. Analysis of Existing Imitation Learning Algorithm - extractive body cue:** The ‘masked observation is then input into visuomotor policy.
- **p. 3 / B. Foundational Vision Model for Roboties - extractive body cue:** In contrast, our approach uses VLM-generated code to compute 3D attention map, which highlights task-relevant regions and possesses much lower dimension compared to 3D Diffuser ...
- **p. 7 / B. Analysis of Existing Imitation Learning Algorithm - extractive body cue:** While the performance of ACT and DP initially improves, they generally show diminishing returns while success rate is still low, and in some cases plateaus ...

## Design Rationale

- **p. 3 / B. Foundational Vision Model for Roboties - extractive body cue:** In contrast, our framework is capable of understanding potentially ambiguous natural language instructions by using visual-semantic reasoning capabilities of VLM and generated code as an ...
- **p. 4 / A. Problem Statement - extractive body cue:** CodeDitfuser consists of three primary components: code generation, 3D attention map computation, and low level policy.
- **p. 7 / B. Analysis of Existing Imitation Learning Algorithm - extractive body cue:** We frst evaluate our method by varying the number of demonstrations on the Pack Bat.tezy task in simulation, as shown in Figure 7 (a).

## Source Evidence Cues

- **p. 9 / B. Analysis of Existing Imitation Learning Algorithm - extractive body cue:** The training and testing scenarios coasist of a mixture of 1 10 4 picking optioas with 1 placing option, The success rate curve indicates that, ...
- **p. 6 / B. Analysis of Existing Imitation Learning Algorithm - extractive body cue:** Specifically, We consider two state-of-the-art methods, Action Chunking Transformer (ACT) [6] and Diffusion Policy (DP) [1] in ‘comprehensive simulation evaluations.
- **p. 7 / B. Analysis of Existing Imitation Learning Algorithm - extractive body cue:** In this section, we investigate whether 3D attention is a suitable representation for visuomotor policy learning and evaluate the pipeline from 3D attention maps to ...
- **p. 7 / B. Analysis of Existing Imitation Learning Algorithm - extractive body cue:** These results confirm that the 3D attention map is a robust representation for downstream isuomotor policy learning in ambiguous task scenarios. ‘Additionally, we stress-test our ...
- **p. 8 / B. Analysis of Existing Imitation Learning Algorithm - extractive body cue:** + Lang-ACT with 3D Attention: Unlike the original ACT, which uses multi-view RGB observations, this baseline inputs 3D attention maps into Lang-ACT to assess whether ...
- **p. 8 / B. Analysis of Existing Imitation Learning Algorithm - extractive body cue:** The ‘masked observation is then input into visuomotor policy.
- **p. 3 / B. Foundational Vision Model for Roboties - extractive body cue:** In contrast, our approach uses VLM-generated code to compute 3D attention map, which highlights task-relevant regions and possesses much lower dimension compared to 3D Diffuser ...
- **Detected method headings:** B. Foundational Vision Model for Roboties (p. 3); B. Analysis of Existing Imitation Learning Algorithm (p. 6)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | The training and testing scenarios coasist of a mixture of 1 10 4 picking optioas with 1 placing option, The success rate ... | p. 9 (B. Analysis of Existing Imitation Learning Algorithm), p. 6 (B. Analysis of Existing Imitation Learning Algorithm) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | Specifically, We consider two state-of-the-art methods, Action Chunking Transformer (ACT) [6] and Diffusion Policy (DP) [1] in ‘comprehensive simulation evaluations. | p. 6 (B. Analysis of Existing Imitation Learning Algorithm), p. 7 (B. Analysis of Existing Imitation Learning Algorithm) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | In this section, we investigate whether 3D attention is a suitable representation for visuomotor policy learning and evaluate the pipeline from 3D ... | p. 7 (B. Analysis of Existing Imitation Learning Algorithm), p. 7 (B. Analysis of Existing Imitation Learning Algorithm) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 7 / B. Analysis of Existing Imitation Learning Algorithm - extractive body cue:** While the performance of ACT and DP initially improves, they generally show diminishing returns while success rate is still low, and in some cases plateaus ...
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | plalz, z1lor, Where, task-relevant, latent, representation, state, contains, enough, information, about, observation, instruction, predict | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | plalz, z1lor, Where, task-relevant, latent, representation, state, contains, enough, information | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | contrast, framework, capable, understanding, potentially, ambiguous, natural, language, instructions, visual-semantic | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | While, performance, ACT, initially, improves, they, generally, diminishing, returns, success | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / A. Problem Statement - extractive body cue:** [ plalz = =)p(= = z1lor,2), Where 2 is a task-relevant latent representation of the state such that p(ajo,l,2 = =) = plalz = =). ...
- **p. 4 / A. Problem Statement - extractive body cue:** In Section II-C, we describe the API provided to the code generation process used to construct our state representation 44, 3D attention map that highlights ...
- **p. 3 / A. Problem Statement - extractive body cue:** For instance, in the packing battery task illustrated in Figure 2, specifying the mug or branch instance, the probability of each battery-slot pair is 1/18, ...
- **p. 6 / B. Analysis of Existing Imitation Learning Algorithm - extractive body cue:** Specifically, We consider two state-of-the-art methods, Action Chunking Transformer (ACT) [6] and Diffusion Policy (DP) [1] in ‘comprehensive simulation evaluations.
- **p. 8 / B. Analysis of Existing Imitation Learning Algorithm - extractive body cue:** The ‘masked observation is then input into visuomotor policy.
- **p. 4 / A. Problem Statement - extractive body cue:** We first generate intermediate code from the instruction {and multiView RGBD observations 0, € RA*!W 4, where AC is the number of camera views, and ...
- **p. 6 / B. Analysis of Existing Imitation Learning Algorithm - extractive body cue:** note that here we do not consider language inputs and focus oon studying the low-level policy capabilities.
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | For methods conditioned on language ‘or attention, we consider a rollout successful if the task is completed in the desired manner, such ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | To address these challenges, we introduce novel robotic manipulation framework that can accomplish tasks specified by potentially ambiguous natural language. | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not recovered | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 9 / B. Analysis of Existing Imitation Learning Algorithm - extractive body cue:** The training and testing scenarios coasist of a mixture of 1 10 4 picking optioas with 1 placing option, The success rate curve indicates that, ...
- **p. 7 / B. Analysis of Existing Imitation Learning Algorithm - extractive body cue:** These results confirm that the 3D attention map is a robust representation for downstream isuomotor policy learning in ambiguous task scenarios. ‘Additionally, we stress-test our ...
- **p. 3 / B. Foundational Vision Model for Roboties - extractive body cue:** In contrast, our approach uses VLM-generated code to compute 3D attention map, which highlights task-relevant regions and possesses much lower dimension compared to 3D Diffuser ...
- **p. 7 / B. Analysis of Existing Imitation Learning Algorithm - extractive body cue:** Second, while training on a 1x1 scenario dloes not generalize to scenarios with multiple placing options, the generalization of CodeDiffuser quickly improves. after seeing more ...
- **p. 3 / B. Foundational Vision Model for Roboties - extractive body cue:** In contrast, our approach uses VLM-generated code to compute 3D attention map, which highlights task-relevant regions and possesses much lower dimension compared to 3D Diffuser ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** training, testing, scenarios, coasist, mixture, picking, optioas, placing, option, success, rate, curve, indicates, given, sufficient, number, demonstrations, attention-conditioned, policy, converges.
- **Relevant PDF headings:** B. Foundational Vision Model for Roboties (p. 3); B. Analysis of Existing Imitation Learning Algorithm (p. 6).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | and the full system in both simulation and real-world tasks, including contact-rich 6-DoF manipulation with multi-object interactions, demonstrating the effectiveness of our ... | p. 2 (3) We conduct extensive evaluations of individual modules), p. 5 (IV. EXPERIMENTS) |
| Action / skill decoding | We find that our policy consistently outperforms the baselines by leveraging VLMgenerated code as an interpretable and executable intermediate representation, effectively utilizing ... | p. 9 (B. Analysis of Existing Imitation Learning Algorithm), p. 10 (Figure/Table caption) |
| Receding execution / feedback | While the performance of ACT and DP initially improves, they generally show diminishing returns while success rate is still low, and in ... | p. 7 (B. Analysis of Existing Imitation Learning Algorithm), p. 9 (B. Analysis of Existing Imitation Learning Algorithm) |

## Failure and Ablation Link

- **p. 6 / B. Analysis of Existing Imitation Learning Algorithm - extractive body cue:** For DP, we consider two variants - DP with RGB inputs, denoted as "DP (RGB)", and DP with point cloud inputs, denoted as "DP (PCD)".
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** For methods conditioned on language ‘or attention, we consider a rollout successful if the task is completed in the desired manner, such as successfully following ...
- **p. 7 / B. Analysis of Existing Imitation Learning Algorithm - extractive body cue:** Furthermore, ‘even with ambiguous commands like "Hang a mug on a branch" (without specifying a particular mug or branch), ‘our system autonomously selects and highlights ...
- **p. 8 / B. Analysis of Existing Imitation Learning Algorithm - extractive body cue:** + Prompt without slackness: All objects are strictly specified, such as "Hang the left-most mug on the top branch."
- **p. 8 / B. Analysis of Existing Imitation Learning Algorithm - extractive body cue:** First, our 3D attention maps successfully highlight the correct object instances even under ambiguous instructions, such as "Hang a mug on a branch" for "Put ...
- **p. 9 / B. Analysis of Existing Imitation Learning Algorithm - extractive body cue:** (4) ‘Our ablation study demonstrates that incorporating the residual ‘connection into PointNet++ improves performance from 61% to 86.5%.
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3: Method Overview. CodeDitfuser consists of three primary components: code generation, 3D attention map computation, and low level policy. (a) CodeDitfuser first leverages the ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 9 (B. Analysis of Existing Imitation Learning Algorithm), p. 6 (B. Analysis of Existing Imitation Learning Algorithm), p. 7 (B. Analysis of Existing Imitation Learning Algorithm), p. 7 (B. Analysis of Existing Imitation Learning Algorithm), p. 8 (B. Analysis of Existing Imitation Learning Algorithm), p. 8 (B. Analysis of Existing Imitation Learning Algorithm), objective p. 7 (B. Analysis of Existing Imitation Learning Algorithm), temporal p. 6 (IV. EXPERIMENTS), p. 1 (Abstract), p. 1 (Abstract), p. 2 (1. Ivrropuction), p. 2 (1. Ivrropuction), p. 3 (A. Problem Statement).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
