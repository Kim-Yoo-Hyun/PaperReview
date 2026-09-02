# Method - Latent Action Pretraining from Videos

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (27 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.iclr.cc/paper_files/paper/2025/hash/45d74e190008c7bff2845ffc8e3facd3-Abstract-Conference.html; PDF retrieval source: https://arxiv.org/pdf/2410.11758.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 4 (2. Latent Pretraining), p. 4 (2. Latent Pretraining), p. 3 (2. Latent Pretraining), p. 3 (2. Latent Pretraining), p. 5 (2. Latent Pretraining)): 3.2 LATENT PRETRAINING We use the encoder of the latent action quantization model as an inverse dynamics model to label all frames xt, given frame xt+1, with latent action zt.

## Method Body Digest

- **p. 4 / 2. Latent Pretraining - extractive body cue:** 3.2 LATENT PRETRAINING We use the encoder of the latent action quantization model as an inverse dynamics model to label all frames xt, given frame ...
- **p. 4 / 2. Latent Pretraining - extractive body cue:** Our latent action quantization model is an encoder-decoder architecture where the encoder takes the current frame xt and the future frame xt+H of a video ...
- **p. 3 / 2. Latent Pretraining - extractive body cue:** 3 LAPA: LATENT ACTION PRETRAINING FOR GENERAL ACTION MODELS Latent Action Pretraining consists of two models that are learned sequentially: Latent Action Quantization and Latent ...
- **p. 3 / 2. Latent Pretraining - extractive body cue:** Note that we use the same pretraining dataset for Latent Action Quantization and Latent Pretraining.
- **p. 5 / 2. Latent Pretraining - extractive body cue:** As with latent pretraining, we freeze the vision encoder and unfreeze all of the parameters of the underlying language model.3
- **p. 3 / 2. Latent Pretraining - extractive body cue:** (1) Latent Action Quantization: We first learn discrete latent actions in a fully unsupervised manner using the VQ-VAE objective (Detail in Figure 8).
- **p. 3 / 2. Latent Pretraining - extractive body cue:** Incorporating auxiliary objectives, such as visual traces (Niu et al., 2024), language reasoning paths (Michał et al., 2024), or creating conversational-style instruction datasets from robot ...
- **p. 4 / 2. Latent Pretraining - extractive body cue:** (2024) conditioned on multiple past observations, we exclude previous frames due to computational constraints.

## Design Rationale

- **p. 1 / 1 INTRODUCTION - extractive body cue:** Vision-Language-Action Models (VLA) for robotics (Brohan et al., 2023; Kim et al., 2024) are trained by aligning large language models with vision encoders, and then ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Latent Action Pretraining consists of two models that are learned sequentially, followed by a finetuning stage to map the latent actions to real robot actions.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** We expect that our method opens up the potential for building foundation models for robotics by pretraining on much larger web-scale video data.

## Source Evidence Cues

- **p. 4 / 2. Latent Pretraining - extractive body cue:** 3.2 LATENT PRETRAINING We use the encoder of the latent action quantization model as an inverse dynamics model to label all frames xt, given frame ...
- **p. 4 / 2. Latent Pretraining - extractive body cue:** Our latent action quantization model is an encoder-decoder architecture where the encoder takes the current frame xt and the future frame xt+H of a video ...
- **p. 3 / 2. Latent Pretraining - extractive body cue:** 3 LAPA: LATENT ACTION PRETRAINING FOR GENERAL ACTION MODELS Latent Action Pretraining consists of two models that are learned sequentially: Latent Action Quantization and Latent ...
- **p. 3 / 2. Latent Pretraining - extractive body cue:** Note that we use the same pretraining dataset for Latent Action Quantization and Latent Pretraining.
- **p. 5 / 2. Latent Pretraining - extractive body cue:** As with latent pretraining, we freeze the vision encoder and unfreeze all of the parameters of the underlying language model.3
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | 3.2 LATENT PRETRAINING We use the encoder of the latent action quantization model as an inverse dynamics model to label all frames ... | p. 4 (2. Latent Pretraining), p. 4 (2. Latent Pretraining) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | Our latent action quantization model is an encoder-decoder architecture where the encoder takes the current frame xt and the future frame xt+H ... | p. 4 (2. Latent Pretraining), p. 3 (2. Latent Pretraining) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | 3 LAPA: LATENT ACTION PRETRAINING FOR GENERAL ACTION MODELS Latent Action Pretraining consists of two models that are learned sequentially: Latent Action ... | p. 3 (2. Latent Pretraining), p. 3 (2. Latent Pretraining) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / 2. Latent Pretraining - extractive body cue:** (1) Latent Action Quantization: We first learn discrete latent actions in a fully unsupervised manner using the VQ-VAE objective (Detail in Figure 8).
- **p. 3 / 2. Latent Pretraining - extractive body cue:** Incorporating auxiliary objectives, such as visual traces (Niu et al., 2024), language reasoning paths (Michał et al., 2024), or creating conversational-style instruction datasets from robot ...
- **p. 4 / 2. Latent Pretraining - extractive body cue:** (2024) conditioned on multiple past observations, we exclude previous frames due to computational constraints.
- **p. 4 / 2. Latent Pretraining - extractive body cue:** Codebook replacement technique from NSVQ is applied during early training steps to maximize codebook utilization.
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 3 (2. Latent Pretraining), p. 3 (2. Latent Pretraining), p. 4 (2. Latent Pretraining), p. 4 (2. Latent Pretraining).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Then, action, pretraining, pretrained, VLM, predict, given, language, instruction, video, clip, current, image, second | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | Then, action, pretraining, pretrained, VLM, predict, given, language, instruction, video | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | Vision-Language-Action, Models, VLA, robotics, Brohan, Kim, trained, aligning, large, language | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | Latent, Action, Quantization, first, learn, discrete, actions, fully, unsupervised, manner | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 2. Latent Pretraining - extractive body cue:** Then, we do action pretraining by using a pretrained VLM to predict the zt given the language instruction of a video clip and the current ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** In the second stage, we perform behavior cloning by pretraining a Vision-Language Model to predict latent actions derived from the first stage based on video ...
- **p. 4 / 2. Latent Pretraining - extractive body cue:** Since latent pretraining does not rely on ground truth actions, it opens the possibility of using any type of raw video paired with language instructions.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Vision-Language-Action Models (VLA) for robotics (Brohan et al., 2023; Kim et al., 2024) are trained by aligning large language models with vision encoders, and then ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Furthermore, on real-world manipulation tasks, our method leads to a new monolithic VLA model, outperforming OPENVLA, the current state-of-the-art model Vision Language Action (VLA) model ...
- **p. 3 / 2. Latent Pretraining - extractive body cue:** Finally, some train inverse dynamics models (IDMs), optical flow, or reinforcement learning models that predict actions from future state rollouts generated by world models (Du ...
- **p. 3 / 2. Latent Pretraining - extractive body cue:** (2024), our approach derives latent actions directly from observations, not ground-truth actions.
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | Second, similar to prior VLAs, LAPA also encounters latency challenges during real-time inference. | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | Since SIMPLER lacks fine-tuning trajectories, we collect 100 multi-task trajectories using successful rollouts from a VLA model trained on BridgeV2 data (Walke ... | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not recovered | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | We evaluate on a total of 54 rollouts for each model encompassing unseen object combinations, unseen objects and unseen instructions. | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / 2. Latent Pretraining - extractive body cue:** 3.2 LATENT PRETRAINING We use the encoder of the latent action quantization model as an inverse dynamics model to label all frames xt, given frame ...
- **p. 3 / 2. Latent Pretraining - extractive body cue:** 3 LAPA: LATENT ACTION PRETRAINING FOR GENERAL ACTION MODELS Latent Action Pretraining consists of two models that are learned sequentially: Latent Action Quantization and Latent ...
- **p. 3 / 2. Latent Pretraining - extractive body cue:** Note that we use the same pretraining dataset for Latent Action Quantization and Latent Pretraining.
- **p. 5 / 2. Latent Pretraining - extractive body cue:** As with latent pretraining, we freeze the vision encoder and unfreeze all of the parameters of the underlying language model.3
- **p. 4 / 2. Latent Pretraining - extractive body cue:** Codebook replacement technique from NSVQ is applied during early training steps to maximize codebook utilization.
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** For pretraining LAPA (Open-X), the best-performing model, we use 8 H100 GPUs for 34 hours with a batch size of 128 (total of 272 H100-hours).

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** LATENT, PRETRAINING, encoder, action, quantization, model, inverse, dynamics, label, frames, given, frame, encoder-decoder, architecture, where, takes, current, future, video, fixed.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | 4.1 BENCHMARKS AND ENVIRONMENTS We evaluate the effectiveness of LAPA on 9 different task categories in 2 different simulation environments and 3 ... | p. 5 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS) |
| Action / skill decoding | (2024) since it is not a behavior cloning baseline. | p. 5 (4 EXPERIMENTS), p. 5 (4 EXPERIMENTS) |
| Receding execution / feedback | Furthermore, by comparing LAPA which does not leverage action-labeled trajectories during pretraining with models that use action-labeled trajectories during pretraining (ACTIONVLA and ... | p. 7 (4 EXPERIMENTS), p. 9 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: Problem Formulation. We investigate building a generalist robotic foundation model from human motion videos without action labels. VQ-VAE-based objective (Van Den Oord et ...
- **p. 6 / 4 EXPERIMENTS - extractive body cue:** 4.4 REAL-WORLD RESULTS We pretrain our models on (1) Bridgev2 (Walke et al., 2023) to measure the cross-embodiment performance (WidowX embodiment for pretraining and Franka ...
- **p. 10 / 4 EXPERIMENTS - extractive body cue:** We use a LAPA model that has only undergone pretraining, without any action finetuning.
- **p. 10 / 4 EXPERIMENTS - extractive body cue:** 6 LIMITATIONS AND CONCLUSION In this paper, we introduce Latent Action Pretraining, a scalable pretraining method for building VLAs without using ground-truth action labels.
- **p. 5 / 4 EXPERIMENTS - extractive body cue:** In this section, we demonstrate the effectiveness of Latent Action Pretraining as a general-purpose pretaining method.
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** This highlights LAPA's effectiveness in a multi-embodiment setting by showcasing its ability to leverage a shared latent action space during pretraining, akin to how language ...
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** 5 ABLATION AND ANALYSIS 5.1 SCALING MODEL, DATA, AND LATENT ACTION SIZE 30 75 150 300 54 55 56 57 AVG Success Rate (%) (a) ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (2. Latent Pretraining), p. 4 (2. Latent Pretraining), p. 3 (2. Latent Pretraining), p. 3 (2. Latent Pretraining), p. 5 (2. Latent Pretraining), objective p. 3 (2. Latent Pretraining), p. 3 (2. Latent Pretraining), p. 4 (2. Latent Pretraining), p. 4 (2. Latent Pretraining), temporal p. 10 (4 EXPERIMENTS), p. 5 (4 EXPERIMENTS), p. 5 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
