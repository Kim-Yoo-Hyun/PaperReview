# Insights — FAST: Efficient Action Tokenization for Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (19 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p012.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p012.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / 1. INTRODUCTION - extractive body cue:** 1: We propose FAS nple yet effective approach for tokenization of robot action trajectories via time-series compression, FAST enables training of autoregressive VLAs that solve ...
- **p. 3 / 1. INTRODUCTION - extractive body cue:** We introduce a new action tokenization approach that allows us to train the first autoregressive VLAs ‘on dexterous and high-frequency robot data
- **p. 3 / 1. INTRODUCTION - extractive body cue:** We find that this scheme struggles to scale to high-frequency robot control tasks, We propose a new tokenization scheme for robot actions, based on time-series ...
- **p. 2 / 1. INTRODUCTION - extractive body cue:** In this work, we propose a new tokenization strategy from first principles.
- **p. 2 / 1. INTRODUCTION - extractive body cue:** We therefore base our method off of the discrete cosine transform (DCT) encoding, which is widely used for ‘compressing continuous signals stich as images (€.g., ...
- **p. 4 / B. The FAST Tokenization Algorithm - extractive body cue:** We first normalize the input actions, such that the Ist and 99th quantile of values in the training dataset for each action dimension maps to ...
- **p. 5 / B. The FAST Tokenization Algorithm - extractive body cue:** xerleaving action di ‘mensions by including all low-frequency components first, and train a byte pair encoding (BPE) tokenizer [27] to losslessly ‘compress it into dense ...
- **Contribution anchor:** p. 1 (1. INTRODUCTION), p. 3 (1. INTRODUCTION), p. 3 (1. INTRODUCTION), p. 2 (1. INTRODUCTION), p. 2 (1. INTRODUCTION), p. 4 (B. The FAST Tokenization Algorithm)

### Strongest assumption and failure boundary

- **p. 4 / 1. INTRODUCTION - extractive body cue:** ‘To illustrate the challenge of training autoregressive poli cies with current action tokenization approaches, we star With a simple didactic example.
- **p. 4 / 1. INTRODUCTION - extractive body cue:** This greatly slows down the rate of convergence during training and can make it challenging to fit complex, high-frequency datasets Indeed, such challenges have been ...
- **p. 1 / 1. INTRODUCTION - extractive body cue:** We observe that correlations between time steps are a major challenge for naive tokenization strategies when predicting sequences of
- **p. 3 / 1. INTRODUCTION - extractive body cue:** We train a small autoregressive transformer model on a didactic interpolation task, in which the network must predict the black dashed curve given the four ...
- **p. 1 / 1. INTRODUCTION - extractive body cue:** Prior robotic policies of this sort typically use naive tokenization strategies based on a per-dimension, per-timestep binning scheme [9, 10, 40].
- **p. 8 / B. Comparing Action Tokenizers for VLA Training - extractive body cue:** Even unsuccessful trials show sensible behavior, like approaching the handles of microwave and dish washer doors, even if ultimately failing to open them, We show ...
- **p. 9 / C. Universal Action Tokenizer - extractive body cue:** One current limitation of the autoregressive VLA is its inference speed: while 7» with diffusion typically predicts one second action chunks within 100ms on an ...
- **Boundary to test:** Even unsuccessful trials show sensible behavior, like approaching the handles of microwave and dish washer doors, even if ultimately failing to open them, We show success and failure videos on our ‘website.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | 1: We propose FAS nple yet effective approach for tokenization of robot action trajectories via time-series compression, FAST enables training of autoregressive VLAs that solve complex dexterous manipulation tasks and generalize broadly ... | p. 1 (1. INTRODUCTION), p. 3 (1. INTRODUCTION) |
| Reported outcome | We report success rate on individual clothing items. | p. 7 (A. Experimental Setup), p. 2 (Figure/Table caption) |
| Failure/limitation | Even unsuccessful trials show sensible behavior, like approaching the handles of microwave and dish washer doors, even if ultimately failing to open them, We show success and failure videos on our ‘website. | p. 8 (B. Comparing Action Tokenizers for VLA Training), p. 9 (C. Universal Action Tokenizer) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `image/video, language instruction, proprioception과 history → language-grounded task state와 action-policy context → continuous action, pose 또는 action chunk`.
- 이 논문의 재사용 가능한 지점은 An alternative approach directly trains VLAS to output ow-level robot control commands given image and language instruction inputs.를 1: We propose FAS nple yet effective approach for tokenization of robot action trajectories via time-series compression, FAST enables training of autoregressive VLAs that solve complex dexterous manipulation tasks and generalize broadly ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 language-grounded task state와 action-policy context가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Even unsuccessful trials show sensible behavior, like approaching the handles of microwave and dish washer doors, even if ultimately failing to open them, We show success and failure videos on our ‘website.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: 1: We propose FAS nple yet effective approach for tokenization of robot action trajectories via time-series compression, FAST enables training of autoregressive VLAs that solve complex dexterous manipulation tasks and generalize broadly ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `VLA and generalist robot policies`; tags: `Robotics, VLA, action tokenization, high-frequency control, cross-embodiment, efficiency`.
- **Reading predecessor in the generated track queue:** Scaling Proprioceptive-Visual Learning with Heterogeneous Pre-trained Transformers (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Even unsuccessful trials show sensible behavior, like approaching the handles of microwave and dish washer doors, even if ultimately failing to open them, We show success and failure videos on our ‘website.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: fon a large dataset of IM action sequences trained the universal tokenizer on the most diverse real robot dataset we could assemble, which includes data from our real robot evaluation tasks..
3. Compare against the body-reported baseline or a matched simpler baseline: We then compare 7 models trained with FAST tokenization to the state-of-the-art 79 flow-matching (diffusion) VLA, and test the scaling of autoregressive VLA training with FAST to large, cross-embodied datasets with 10k ....
4. Report the body metric and its denominator/aggregation: We report success rate on individual clothing items..
5. Re-run the body-reported ablation/failure condition: We fine-tune the VLA models for robot action prediction, without weight freezing..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 4 (B. The FAST Tokenization Algorithm), p. 5 (B. The FAST Tokenization Algorithm), p. 4 (B. The FAST Tokenization Algorithm); the primary result is directionally consistent at p. 7 (A. Experimental Setup), p. 2 (Figure/Table caption), p. 10 (Figure/Table caption); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 FAS, nple, effective mechanism이 We then compare 7 models trained with FAST tokenization to the state-of-the-art 79 flow-matching (diffusion) VLA, ... 대비 We report success rate on individual clothing items.을 개선하고, Even unsuccessful trials show sensible behavior, like approaching the handles of microwave and dish washer doors, ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
