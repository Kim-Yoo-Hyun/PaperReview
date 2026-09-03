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

- **Paper-specific interface:** An alternative approach directly trains VLAS to output ow-level robot control commands given image and language instruction inputs. (p. 3, 1. INTRODUCTION).
- **Paper-specific mechanism:** 1: We propose FAS nple yet effective approach for tokenization of robot action trajectories via time-series compression, FAST enables training of autoregressive VLAs that solve complex dexterous manipulation tasks and ... (p. 1, 1. INTRODUCTION).
- **Evidence boundary:** the reported outcome is We develop a suite of 7 evaluation tasks 6 real robot, 1 simulated; see Figure 5), designed to test VLA performance on both, highly dexterous tasks like laundry folding, and ... (p. 6, A. Experimental Setup); the relevant task/metric cue is We develop a suite of 7 evaluation tasks 6 real robot, 1 simulated; see Figure 5), designed to test VLA performance on both, highly dexterous tasks like laundry folding, and ... (p. 6, A. Experimental Setup). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** We do ‘not measure success rates during these evaluations, but provide ‘numerous qualitative videos of successes and failures to help readers get a sense of the policy's capabilities (p. 18, B. Discussion of Alternative Compression Approaches).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `VLA and generalist robot policies`; tags: `Robotics, VLA, action tokenization, high-frequency control, cross-embodiment, efficiency`.
- **Reading predecessor in the generated track queue:** Scaling Proprioceptive-Visual Learning with Heterogeneous Pre-trained Transformers (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Even unsuccessful trials show sensible behavior, like approaching the handles of microwave and dish washer doors, even if ultimately failing to open them, We show success and failure videos on our ‘website.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: An alternative approach directly trains VLAS to output ow-level robot control commands given image and language instruction inputs. (p. 3, 1. INTRODUCTION); preserve the objective/update rule: After the data is normalized, we apply the discrete cosine transform to each action dimension separately. ‘To compress the DCT-converted signal we can simply omit insignificant coefficients, which we implement ... (p. 4, B. The FAST Tokenization Algorithm).
2. Use the paper-reported task/data/environment cue: We test FAST across 7 evaluation environments: 6 real-robot tasks and / simulation environment. (p. 6, A. Experimental Setup).
3. Compare against the reported or matched baseline: We fine-tune the VLA models for robot action prediction, without weight freezing. (p. 6, A. Experimental Setup).
4. Report the body metric with its denominator and aggregation: We develop a suite of 7 evaluation tasks 6 real robot, 1 simulated; see Figure 5), designed to test VLA performance on both, highly dexterous tasks like laundry folding, and ... (p. 6, A. Experimental Setup).
5. Re-run the reported ablation or stress/failure condition: We fine-tune the VLA models for robot action prediction, without weight freezing. (p. 6, A. Experimental Setup); if none is reported, design one around: We do ‘not measure success rates during these evaluations, but provide ‘numerous qualitative videos of successes and failures to help readers get a sense of the policy's capabilities (p. 18, B. Discussion of Alternative Compression Approaches).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 1 (1. INTRODUCTION), p. 2 (1. INTRODUCTION), match the reported outcome at p. 6 (A. Experimental Setup), p. 7 (A. Experimental Setup), p. 6 (A. Experimental Setup), and measure the boundary at p. 18 (B. Discussion of Alternative Compression Approaches), p. 4 (1. INTRODUCTION).

## Falsifiable research question

Under the paper's stated interface (An alternative approach directly trains VLAS to output ow-level robot control commands given image and language instruction inputs.), does the paper-specific mechanism (1: We propose FAS nple yet effective approach for tokenization of robot action trajectories via time-series compression, FAST enables training of autoregressive ...) retain the reported evaluation outcome (We develop a suite of 7 evaluation tasks 6 real robot, 1 simulated; see Figure 5), designed to ...) when tested against the paper's strongest explicit boundary (We do ‘not measure success rates during these evaluations, but provide ‘numerous qualitative videos of successes and failures ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (We develop a suite of 7 evaluation tasks 6 real robot, 1 simulated; see Figure 5), designed to ...) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (19 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** 1: We propose FAS nple yet effective approach for tokenization of robot action trajectories via time-series compression, FAST enables training of autoregressive VLAs that solve complex dexterous manipulation tasks and ... (p. 1, 1. INTRODUCTION).
- **Paper-supported outcome:** We develop a suite of 7 evaluation tasks 6 real robot, 1 simulated; see Figure 5), designed to test VLA performance on both, highly dexterous tasks like laundry folding, and ... (p. 6, A. Experimental Setup).
- **Strongest explicit boundary:** We do ‘not measure success rates during these evaluations, but provide ‘numerous qualitative videos of successes and failures to help readers get a sense of the policy's capabilities (p. 18, B. Discussion of Alternative Compression Approaches).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
