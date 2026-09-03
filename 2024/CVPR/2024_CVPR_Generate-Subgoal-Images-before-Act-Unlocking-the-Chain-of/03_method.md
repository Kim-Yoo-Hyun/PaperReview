# Method - Generate Subgoal Images before Act: Unlocking the Chain-of-Thought Reasoning in Diffusion Model for Robot Manipulation with Multimodal Prompts

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Ni_Generate_Subgoal_Images_before_Act_Unlocking_the_Chain-of-Thought_Reasoning_in_CVPR_2024_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Ni_Generate_Subgoal_Images_before_Act_Unlocking_the_Chain-of-Thought_Reasoning_in_CVPR_2024_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 3 (3.1. Pipeline Overview), p. 4 (3.1. Pipeline Overview), p. 4 (3.2. Pre-training Coarse Semantic Alignment), p. 5 (3.4. Goal-conditioned Policy Model), p. 5 (3.4. Goal-conditioned Policy Model), p. 3 (3. Method)): Under the Markovian assumption, the overall framework can be formulated as: p⇥({⌧i a}N i=1/P, x0) = N Y i=1 pφ(xi/P, x0) ! / {z } visual planning N Y i=1 ...

## Method Body Digest

- **p. 3 / 3.1. Pipeline Overview - extractive body cue:** Under the Markovian assumption, the overall framework can be formulated as: p⇥({⌧i a}N i=1/P, x0) = N Y i=1 pφ(xi/P, x0) ! / {z } ...
- **p. 4 / 3.1. Pipeline Overview - extractive body cue:** Method overview: CoTDiffusion consists of a multi-modal encoder and vision encoder V , semantic alignment module S, conditional diffusion model E and foundation model F ...
- **p. 4 / 3.2. Pre-training Coarse Semantic Alignment - extractive body cue:** Then they are refined through fusion module which consists of several self-attention blocks separately to obtain attention tokens z0 and zi aligned to the prompts.
- **p. 5 / 3.4. Goal-conditioned Policy Model - extractive body cue:** The final component in our framework is the low-level policy model for action planning, generating an action trajectory ⌧i a when given observation trajectory ⌧i ...
- **p. 5 / 3.4. Goal-conditioned Policy Model - extractive body cue:** The policy model can be parameterized as an image-conditioned planner that infers the action ai,t given the current observation xi,t and the generated subgoal image ...
- **p. 3 / 3. Method - extractive body cue:** We propose CoTDiffusion, a hierarchical framework that integrates the diffusion model as the high-level module to decompose multi-modal prompts in a chain-of-thought manner and progressively ...
- **p. 6 / 3.4. Goal-conditioned Policy Model - extractive body cue:** Initial Observation Generated Subgoal Images Visual Reasoning Visual Rearrange Visual Constraints Rearrange objects to this setup and then restore.
- **p. 5 / 3.3. Fine-grained Diffusion Training - extractive body cue:** The training objective can be formulated as: L = Exi2D[k ˆxi -E ⇣ xi-1, zi align , P) / {z } Forward Generation k+kˆxi-1 -E ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** The contributions of this work are as follows: • We propose a hierarchical framework CoTDiffusion that the high-level diffusion model translates the multi-modal prompts into ...
- **p. 3 / 3.1. Pipeline Overview - extractive body cue:** Under the Markovian assumption, the overall framework can be formulated as: p⇥({⌧i a}N i=1/P, x0) = N Y i=1 pφ(xi/P, x0) ! / {z } ...
- **p. 4 / 3.2. Pre-training Coarse Semantic Alignment - extractive body cue:** Thus, we propose a two-stage coarse-to-fine approach decoupling semantic alignment pretraining from diffusion model finetuning, illustrated in Fig.

## Source Evidence Cues

- **p. 3 / 3.1. Pipeline Overview - extractive body cue:** Under the Markovian assumption, the overall framework can be formulated as: p⇥({⌧i a}N i=1/P, x0) = N Y i=1 pφ(xi/P, x0) ! / {z } ...
- **p. 4 / 3.1. Pipeline Overview - extractive body cue:** Method overview: CoTDiffusion consists of a multi-modal encoder and vision encoder V , semantic alignment module S, conditional diffusion model E and foundation model F ...
- **p. 4 / 3.2. Pre-training Coarse Semantic Alignment - extractive body cue:** Then they are refined through fusion module which consists of several self-attention blocks separately to obtain attention tokens z0 and zi aligned to the prompts.
- **p. 5 / 3.4. Goal-conditioned Policy Model - extractive body cue:** The final component in our framework is the low-level policy model for action planning, generating an action trajectory ⌧i a when given observation trajectory ⌧i ...
- **p. 5 / 3.4. Goal-conditioned Policy Model - extractive body cue:** The policy model can be parameterized as an image-conditioned planner that infers the action ai,t given the current observation xi,t and the generated subgoal image ...
- **p. 3 / 3. Method - extractive body cue:** We propose CoTDiffusion, a hierarchical framework that integrates the diffusion model as the high-level module to decompose multi-modal prompts in a chain-of-thought manner and progressively ...
- **p. 6 / 3.4. Goal-conditioned Policy Model - extractive body cue:** Initial Observation Generated Subgoal Images Visual Reasoning Visual Rearrange Visual Constraints Rearrange objects to this setup and then restore.
- **Detected method headings:** 2.1. Diffusion Models for Text-to-Image Generation (p. 2); 3. Method (p. 3); 3.4. Goal-conditioned Policy Model (p. 5)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | Under the Markovian assumption, the overall framework can be formulated as: p⇥({⌧i a}N i=1/P, x0) = N Y i=1 pφ(xi/P, x0) ! ... | p. 3 (3.1. Pipeline Overview), p. 4 (3.1. Pipeline Overview) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | Method overview: CoTDiffusion consists of a multi-modal encoder and vision encoder V , semantic alignment module S, conditional diffusion model E and ... | p. 4 (3.1. Pipeline Overview), p. 4 (3.2. Pre-training Coarse Semantic Alignment) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | Then they are refined through fusion module which consists of several self-attention blocks separately to obtain attention tokens z0 and zi aligned ... | p. 4 (3.2. Pre-training Coarse Semantic Alignment), p. 5 (3.4. Goal-conditioned Policy Model) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3.3. Fine-grained Diffusion Training - extractive body cue:** The training objective can be formulated as: L = Exi2D[k ˆxi -E ⇣ xi-1, zi align , P) / {z } Forward Generation k+kˆxi-1 -E ...
- **p. 5 / 3.3. Fine-grained Diffusion Training - extractive body cue:** In the backward pass, the same aligned token can guide diffusion model to reconstruct the current subgoal xi from the next subgoal image xi+1, acting ...
- **p. 6 / 3.4. Goal-conditioned Policy Model - extractive body cue:** Initial Observation Generated Subgoal Images Visual Reasoning Visual Rearrange Visual Constraints Rearrange objects to this setup and then restore.
- **p. 3 / 3.1. Pipeline Overview - extractive body cue:** With the decoupled foundation model for action prediction, highlevel visual planning focuses solely on comprehending instructions and visualizing subgoals without confusion from joint action prediction ...
- **p. 3 / 3. Method - extractive body cue:** We propose CoTDiffusion, a hierarchical framework that integrates the diffusion model as the high-level module to decompose multi-modal prompts in a chain-of-thought manner and progressively ...
- **p. 4 / 3.2. Pre-training Coarse Semantic Alignment - extractive body cue:** Thus, tracking the progress critically relies on extracting semantic information from the generated subgoal xi.
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 5 (3.3. Fine-grained Diffusion Training), p. 5 (3.3. Fine-grained Diffusion Training), p. 6 (3.4. Goal-conditioned Policy Model).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | policy, model, parameterized, image-conditioned, planner, infers, action, given, current, observation, generated, subgoal, image, t/xi | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | policy, model, parameterized, image-conditioned, planner, infers, action, given, current, observation | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | contributions, follows, hierarchical, framework, CoTDiffusion, high-level, diffusion, model, translates, multi-modal | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | training, objective, formulated, Exi2D, xi-1, align, Forward, Generation, Backward, Bi-directional | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 5 / 3.4. Goal-conditioned Policy Model - extractive body cue:** The policy model can be parameterized as an image-conditioned planner that infers the action ai,t given the current observation xi,t and the generated subgoal image ...
- **p. 3 / 3.1. Pipeline Overview - extractive body cue:** Given the initial observation x0 and a multi-modal prompt P as task instruction potentially needs to be reached by N subgoal steps, robots are required ...
- **p. 4 / 3.1. Pipeline Overview - extractive body cue:** Generated Subgoal #"#$ Current Observation #% … Environment Multi Modal Instructions Action Sequences Vision Encoder Cross Attention Cross Attention Fusion Module Vision Encoder Loop × ...
- **p. 3 / 3.1. Pipeline Overview - extractive body cue:** Under the Markovian assumption, the overall framework can be formulated as: p⇥({⌧i a}N i=1/P, x0) = N Y i=1 pφ(xi/P, x0) ! / {z } ...
- **p. 5 / 3.4. Goal-conditioned Policy Model - extractive body cue:** The final component in our framework is the low-level policy model for action planning, generating an action trajectory ⌧i a when given observation trajectory ⌧i ...
- **p. 2 / 1. Introduction - extractive body cue:** The subgoal images act as a unified interface bridging the high-level visual planning and low-level action planning, decoupling the instruction understanding and action execution.
- **p. 1 / 1. Introduction - extractive body cue:** The subgoal images are worth a thousand words, inspiring us to propose a novel framework CoTDiffusion to generate goal images step-by-step before act. vances in ...
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | The generated keyframes are further fed to the foundation model which predicts action sequences to achieve the imagined goal scene and this ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | We propose CoTDiffusion, a hierarchical framework that integrates the diffusion model as the high-level module to decompose multi-modal prompts in a chain-of-thought ... | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not recovered | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 6 / 3.4. Goal-conditioned Policy Model - extractive body cue:** Initial Observation Generated Subgoal Images Visual Reasoning Visual Rearrange Visual Constraints Rearrange objects to this setup and then restore.
- **p. 8 / 4.4. Further Analysis - extractive body cue:** As the initial observation and prompt remain fixed across different generation steps, the align tokens at various stage tend to so similar that may confuse ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Under, Markovian, assumption, overall, framework, formulated, xi/P, visual, planning, t/xi, action, module, consists, multi-modal, encoder, understand, complex, task, instructions, conditioned.
- **Relevant PDF headings:** 2.1. Diffusion Models for Text-to-Image Generation (p. 2); 3. Method (p. 3); 3.4. Goal-conditioned Policy Model (p. 5).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | Benchmark & Tasks We conduct evaluation on VIMABENCH, a benchmark suite for multimodal robot learning, which is built on the Ravens robot ... | p. 6 (4.1. Experiment Setup), p. 6 (4.1. Experiment Setup) |
| Action / skill decoding | 1 demonstrate CoTDiffusion significantly outperforms other baselines in success rate. | p. 6 (4.3. Quantitative Results of Success Rate), p. 6 (4.2. Baselines) |
| Receding execution / feedback | 1 demonstrate CoTDiffusion significantly outperforms other baselines in success rate. | p. 6 (4.3. Quantitative Results of Success Rate), p. 7 (4.4. Further Analysis) |

## Failure and Ablation Link

- **p. 8 / 4.4. Further Analysis - extractive body cue:** Additionally, we observe that the bi-directional generation may impedes the diffusion model training if without coarse semantic pretraining.
- **p. 7 / 4.3. Quantitative Results of Success Rate - extractive body cue:** Gato and Flamingo gets low success rates on longhorizon tasks without explicit subgoal generation to correct the accumulative deviation errors from the instructions.
- **p. 7 / 4.3. Quantitative Results of Success Rate - extractive body cue:** In contrast, CoTDiffusion develops intrinsic chainof-thought reasoning and alignment for generated subgoal images for flexible visual planning directly from the raw multi-modal prompts, without the ...
- **p. 8 / 4.4. Further Analysis - extractive body cue:** Without chain-of-thought reasoning abilities, SuSIE struggles to follow instructions when given general multi-modal prompts, let alone generate subgoal images with smooth progressions.
- **p. 6 / 4.2. Baselines - extractive body cue:** VIMA adpots an object-centric approach to flatten all the observation and prompts into object tokens sequence and predicts motor actions autoregressively and demonstrates SOTA performance ...
- **p. 8 / 5. Conclusion - extractive body cue:** Incorporating commonsense knowledge from pre-trained MLLM like GPT-4V provides an avenue for more generalizable and promising reasoning in CoTDiffusion, which leaves as our future work.
- **p. 7 / 4.4. Further Analysis - extractive body cue:** Additionally, ablating coarse pretraining and bi-directional generation degrades performance, validating their benefits.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (3.1. Pipeline Overview), p. 4 (3.1. Pipeline Overview), p. 4 (3.2. Pre-training Coarse Semantic Alignment), p. 5 (3.4. Goal-conditioned Policy Model), p. 5 (3.4. Goal-conditioned Policy Model), p. 3 (3. Method), objective p. 5 (3.3. Fine-grained Diffusion Training), p. 5 (3.3. Fine-grained Diffusion Training), p. 6 (3.4. Goal-conditioned Policy Model), p. 3 (3.1. Pipeline Overview), p. 3 (3. Method), p. 4 (3.2. Pre-training Coarse Semantic Alignment), temporal p. 4 (3.1. Pipeline Overview), p. 3 (3. Method), p. 3 (3.1. Pipeline Overview), p. 4 (3.2. Pre-training Coarse Semantic Alignment), p. 5 (3.4. Goal-conditioned Policy Model), p. 5 (3.2. Pre-training Coarse Semantic Alignment).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
