# Method - FAST: Efficient Action Tokenization for Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (19 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p012.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p012.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 4 (B. The FAST Tokenization Algorithm), p. 5 (B. The FAST Tokenization Algorithm), p. 4 (B. The FAST Tokenization Algorithm), p. 9 (C. Universal Action Tokenizer), p. 5 (B. The FAST Tokenization Algorithm), p. 8 (B. Comparing Action Tokenizers for VLA Training)): We first normalize the input actions, such that the Ist and 99th quantile of values in the training dataset for each action dimension maps to the range [-1,...,1]- This initial ...

## Method Body Digest

- **p. 4 / B. The FAST Tokenization Algorithm - extractive body cue:** We first normalize the input actions, such that the Ist and 99th quantile of values in the training dataset for each action dimension maps to ...
- **p. 5 / B. The FAST Tokenization Algorithm - extractive body cue:** xerleaving action di ‘mensions by including all low-frequency components first, and train a byte pair encoding (BPE) tokenizer [27] to losslessly ‘compress it into dense ...
- **p. 4 / B. The FAST Tokenization Algorithm - extractive body cue:** We use quantiles to be robust to outlier actions which occasionally occur in large robot datasets.
- **p. 9 / C. Universal Action Tokenizer - extractive body cue:** However, without BPE; there is a large number of repeated 0-tokens which dilute the learning signal and also significantly slow down inference, since models need ...
- **p. 5 / B. The FAST Tokenization Algorithm - extractive body cue:** We then quantize the DCT coefficients and use byte-pair encoding (BPE) to compress the flattened sequence of per-dimension DCT coefficients into the final action token ...
- **p. 8 / B. Comparing Action Tokenizers for VLA Training - extractive body cue:** Notably, FAST tokenization enables the first successful training of a strong generalist policy on the DROID dataset [39], which can be evaluated zevo-shor in unseen ...
- **p. 7 / B. Comparing Action Tokenizers for VLA Training - extractive body cue:** We use -second action chunks from datasets with various action dimensionalities and control frequencies.
- **p. 4 / B. The FAST Tokenization Algorithm - extractive body cue:** After the data is normalized, we apply the discrete cosine transform to each action dimension separately. ‘To compress the DCT-converted signal we can simply omit ...

## Design Rationale

- **p. 1 / 1. INTRODUCTION - extractive body cue:** 1: We propose FAS nple yet effective approach for tokenization of robot action trajectories via time-series compression, FAST enables training of autoregressive VLAs that solve ...
- **p. 3 / 1. INTRODUCTION - extractive body cue:** We introduce a new action tokenization approach that allows us to train the first autoregressive VLAs ‘on dexterous and high-frequency robot data
- **p. 3 / 1. INTRODUCTION - extractive body cue:** We find that this scheme struggles to scale to high-frequency robot control tasks, We propose a new tokenization scheme for robot actions, based on time-series ...

## Source Evidence Cues

- **p. 4 / B. The FAST Tokenization Algorithm - extractive body cue:** We first normalize the input actions, such that the Ist and 99th quantile of values in the training dataset for each action dimension maps to ...
- **p. 5 / B. The FAST Tokenization Algorithm - extractive body cue:** xerleaving action di ‘mensions by including all low-frequency components first, and train a byte pair encoding (BPE) tokenizer [27] to losslessly ‘compress it into dense ...
- **p. 4 / B. The FAST Tokenization Algorithm - extractive body cue:** We use quantiles to be robust to outlier actions which occasionally occur in large robot datasets.
- **p. 9 / C. Universal Action Tokenizer - extractive body cue:** However, without BPE; there is a large number of repeated 0-tokens which dilute the learning signal and also significantly slow down inference, since models need ...
- **p. 5 / B. The FAST Tokenization Algorithm - extractive body cue:** We then quantize the DCT coefficients and use byte-pair encoding (BPE) to compress the flattened sequence of per-dimension DCT coefficients into the final action token ...
- **p. 8 / B. Comparing Action Tokenizers for VLA Training - extractive body cue:** Notably, FAST tokenization enables the first successful training of a strong generalist policy on the DROID dataset [39], which can be evaluated zevo-shor in unseen ...
- **p. 7 / B. Comparing Action Tokenizers for VLA Training - extractive body cue:** We use -second action chunks from datasets with various action dimensionalities and control frequencies.
- **Detected method headings:** B. The FAST Tokenization Algorithm (p. 4); B. Discussion of Alternative Compression Approaches (p. 16)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | We first normalize the input actions, such that the Ist and 99th quantile of values in the training dataset for each action ... | p. 4 (B. The FAST Tokenization Algorithm), p. 5 (B. The FAST Tokenization Algorithm) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | xerleaving action di ‘mensions by including all low-frequency components first, and train a byte pair encoding (BPE) tokenizer [27] to losslessly ‘compress ... | p. 5 (B. The FAST Tokenization Algorithm), p. 4 (B. The FAST Tokenization Algorithm) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | We use quantiles to be robust to outlier actions which occasionally occur in large robot datasets. | p. 4 (B. The FAST Tokenization Algorithm), p. 9 (C. Universal Action Tokenizer) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / B. The FAST Tokenization Algorithm - extractive body cue:** After the data is normalized, we apply the discrete cosine transform to each action dimension separately. ‘To compress the DCT-converted signal we can simply omit ...
- **p. 5 / B. The FAST Tokenization Algorithm - extractive body cue:** xerleaving action di ‘mensions by including all low-frequency components first, and train a byte pair encoding (BPE) tokenizer [27] to losslessly ‘compress it into dense ...
- **p. 5 / B. The FAST Tokenization Algorithm - extractive body cue:** Other lossless compression algorithms like Huffman coding [33] or Lempel-Ziv methods [7S] (the algorithms underlying the gzip compression approach) could be used instead, but we ...
- **p. 7 / B. Comparing Action Tokenizers for VLA Training - extractive body cue:** We note that this compression is not entirely lossless, with a trade-off between compression ratio and reconstruction accuracy determined by the scale parameter 7 from ...
- **p. 8 / B. Comparing Action Tokenizers for VLA Training - extractive body cue:** On both tasks, policies trained with naive tokenization are unable to make progress ‘on the task.
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 4 (B. The FAST Tokenization Algorithm), p. 5 (B. The FAST Tokenization Algorithm), p. 5 (B. The FAST Tokenization Algorithm), p. 7 (B. Comparing Action Tokenizers for VLA Training).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | alternative, directly, trains, VLAS, output, ow-level, robot, control, commands, given, image, language, instruction, inputs | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | alternative, directly, trains, VLAS, output, ow-level, robot, control, commands, given | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | FAS, nple, effective, tokenization, robot, action, trajectories, time-series, compression, FAST | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | After, data, normalized, apply, discrete, cosine, transform, action, dimension, separately | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 1. INTRODUCTION - extractive body cue:** An alternative approach directly trains VLAS to output ow-level robot control commands given image and language instruction inputs.
- **p. 1 / 1. INTRODUCTION - extractive body cue:** 1: We propose FAS nple yet effective approach for tokenization of robot action trajectories via time-series compression, FAST enables training of autoregressive VLAs that solve ...
- **p. 10 / C. Universal Action Tokenizer - extractive body cue:** We also developed FAST, a universal action tokenizer, that can serve as a strong default tokenizer for any robot action sequence, and used it to ...
- **p. 2 / 1. INTRODUCTION - extractive body cue:** approach: input images can be represented as "soft token: produced by a pre-trained vision encoder [46], and full autoregressive image input-output can be achieved with ...
- **p. 9 / C. Universal Action Tokenizer - extractive body cue:** To comply with the tak setup, we modify the OpenVLA model code to accept multiple input images and predict I-second action chunks.
- **p. 3 / 1. INTRODUCTION - extractive body cue:** We assume that policies output an "action chunk" [72, 41], a sequence of Hf actions (15, 7, 72], which makes it easier to produce temporally-consistent ...
- **p. 4 / B. The FAST Tokenization Algorithm - extractive body cue:** We first normalize the input actions, such that the Ist and 99th quantile of values in the training dataset for each action dimension maps to ...
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | naive tokenization, We apply the binning tokenization to each time step in the action chunk separately and then concatenate, Finally, while our ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | We observe that correlations between time steps are a major challenge for naive tokenization strategies when predicting sequences of | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not recovered | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | One current limitation of the autoregressive VLA is its inference speed: while 7» with diffusion typically predicts one second action chunks within ... | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / B. The FAST Tokenization Algorithm - extractive body cue:** We first normalize the input actions, such that the Ist and 99th quantile of values in the training dataset for each action dimension maps to ...
- **p. 5 / B. The FAST Tokenization Algorithm - extractive body cue:** xerleaving action di ‘mensions by including all low-frequency components first, and train a byte pair encoding (BPE) tokenizer [27] to losslessly ‘compress it into dense ...
- **p. 9 / C. Universal Action Tokenizer - extractive body cue:** However, without BPE; there is a large number of repeated 0-tokens which dilute the learning signal and also significantly slow down inference, since models need ...
- **p. 8 / B. Comparing Action Tokenizers for VLA Training - extractive body cue:** Notably, FAST tokenization enables the first successful training of a strong generalist policy on the DROID dataset [39], which can be evaluated zevo-shor in unseen ...
- **p. 9 / C. Universal Action Tokenizer - extractive body cue:** One current limitation of the autoregressive VLA is its inference speed: while 7» with diffusion typically predicts one second action chunks within 100ms on an ...
- **p. 10 / C. Universal Action Tokenizer - extractive body cue:** For state-of-the-art VLA training runs, which can often use thousands of GPU hours, a Sx reduction in required compute is significant.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** first, normalize, input, actions, Ist, quantile, values, training, dataset, action, dimension, maps, range, initial, normalization, step, useful, bring, data, specitied.
- **Relevant PDF headings:** B. The FAST Tokenization Algorithm (p. 4); B. Discussion of Alternative Compression Approaches (p. 16).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | fon a large dataset of IM action sequences trained the universal tokenizer on the most diverse real robot dataset we could assemble, ... | p. 7 (A. Experimental Setup), p. 6 (A. Experimental Setup) |
| Action / skill decoding | We then compare 7 models trained with FAST tokenization to the state-of-the-art 79 flow-matching (diffusion) VLA, and test the scaling of autoregressive ... | p. 6 (VI. EXPERIMENTS), p. 1 (Figure/Table caption) |
| Receding execution / feedback | We report success rate on individual clothing items. | p. 7 (A. Experimental Setup), p. 2 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 6 / A. Experimental Setup - extractive body cue:** We fine-tune the VLA models for robot action prediction, without weight freezing.
- **p. 7 / A. Experimental Setup - extractive body cue:** To our knowledge, this is the first "zero-shot" evaluation of DROID policies, in a completely unseen environment, without co-training or fine-tuning, simply by prompting a ...
- **p. 7 / A. Experimental Setup - extractive body cue:** + Toast out of toaster [7] (50 Hz): a bimanual Trossen Viper-X robot needs to remove two slices of bread from toaster and place them ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 3: Effect of sampling rate on prediction performance. We train a small autoregressive transformer model on a didactic interpolation task, in which the network ...
- **p. 8 / B. Comparing Action Tokenizers for VLA Training - extractive body cue:** Even unsuccessful trials show sensible behavior, like approaching the handles of microwave and dish washer doors, even if ultimately failing to open them, We show ...
- **p. 9 / C. Universal Action Tokenizer - extractive body cue:** One current limitation of the autoregressive VLA is its inference speed: while 7» with diffusion typically predicts one second action chunks within 100ms on an ...
- **p. 9 / C. Universal Action Tokenizer - extractive body cue:** We will leave a detailed investigation of the language following abilities of diffusion and autoregressive VLAS to future work.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 4 (B. The FAST Tokenization Algorithm), p. 5 (B. The FAST Tokenization Algorithm), p. 4 (B. The FAST Tokenization Algorithm), p. 9 (C. Universal Action Tokenizer), p. 5 (B. The FAST Tokenization Algorithm), p. 8 (B. Comparing Action Tokenizers for VLA Training), objective p. 4 (B. The FAST Tokenization Algorithm), p. 5 (B. The FAST Tokenization Algorithm), p. 5 (B. The FAST Tokenization Algorithm), p. 7 (B. Comparing Action Tokenizers for VLA Training), p. 8 (B. Comparing Action Tokenizers for VLA Training), temporal p. 7 (A. Experimental Setup), p. 1 (1. INTRODUCTION), p. 3 (1. INTRODUCTION), p. 1 (Abstract), p. 3 (1. INTRODUCTION), p. 4 (1. INTRODUCTION).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
