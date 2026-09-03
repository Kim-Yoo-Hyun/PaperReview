# Evaluation - FAST: Efficient Action Tokenization for Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (19 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p012.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p012.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (A. Experimental Setup), p. 2 (Figure/Table caption), p. 10 (Figure/Table caption), p. 6 (A. Experimental Setup), p. 6 (A. Experimental Setup), p. 7 (A. Experimental Setup)): We report success rate on individual clothing items.

## Evaluation Body Digest

- **p. 7 / A. Experimental Setup - extractive body cue:** fon a large dataset of IM action sequences trained the universal tokenizer on the most diverse real robot dataset we could assemble, which includes data ...
- **p. 6 / A. Experimental Setup - extractive body cue:** We test FAST across 7 evaluation environments: 6 real-robot tasks and / simulation environment.
- **p. 6 / VI. EXPERIMENTS - extractive body cue:** We then compare 7 models trained with FAST tokenization to the state-of-the-art 79 flow-matching (diffusion) VLA, and test the scaling of autoregressive VLA training with ...
- **p. 7 / A. Experimental Setup - extractive body cue:** + Zero-shot DROID tabletop manipulation [9] (15 Hz): wwe test a policy trained on the full DROID dataset across various table-top manipulation tasks like picking ...
- **p. 7 / A. Experimental Setup - extractive body cue:** We report success rate on individual clothing items.
- **p. 6 / A. Experimental Setup - extractive body cue:** We develop a suite of 7 evaluation tasks 6 real robot, 1 simulated; see Figure 5), designed to test VLA performance on both, highly dexterous ...
- **p. 6 / A. Experimental Setup - extractive body cue:** The tasks are designed to test VLA performance on highly dexterous tasks, like folding cloths from a laundry basket ("Laundry Folding"), and generalization, e.g, zer0-shot ...
- **p. 7 / A. Experimental Setup - extractive body cue:** We measure average performance across LiberoSpatial, Libero-Object, Libero-Goal, and Libero-10.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** VI. EXPERIMENTS (p. 6); A. Experimental Setup (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| A. Experimental Setup | EMPIRICAL / REAL-ROBOT OR HARDWARE | We report success rate on individual clothing items. | p. 7 (A. Experimental Setup) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 2: Left: FAST tokenization enables training of autoregres- sive Transformers for dexterous robot control via simple next token prediction. Right: FAST outperforms popular ... | p. 2 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 11: Comparison of x)-FAST and diffusion x [7] generalist policies. zp-FAST matches the performance of Aiffusion 7p while requiring significantly less compute for ... | p. 10 (Figure/Table caption) |
| A. Experimental Setup | EMPIRICAL / REAL-ROBOT OR HARDWARE | We develop a suite of 7 evaluation tasks 6 real robot, 1 simulated; see Figure 5), designed to test VLA performance on both, highly ... | p. 6 (A. Experimental Setup) |
| A. Experimental Setup | EMPIRICAL / REAL-ROBOT OR HARDWARE | The tasks are designed to test VLA performance on highly dexterous tasks, like folding cloths from a laundry basket ("Laundry Folding"), and generalization, e.g, ... | p. 6 (A. Experimental Setup) |

## Dataset / Benchmark Role

- **p. 7 / A. Experimental Setup - extractive body cue:** fon a large dataset of IM action sequences trained the universal tokenizer on the most diverse real robot dataset we could assemble, which includes data ...
- **p. 6 / A. Experimental Setup - extractive body cue:** We test FAST across 7 evaluation environments: 6 real-robot tasks and / simulation environment.
- **p. 6 / VI. EXPERIMENTS - extractive body cue:** We then compare 7 models trained with FAST tokenization to the state-of-the-art 79 flow-matching (diffusion) VLA, and test the scaling of autoregressive VLA training with ...
- **p. 7 / A. Experimental Setup - extractive body cue:** + Zero-shot DROID tabletop manipulation [9] (15 Hz): wwe test a policy trained on the full DROID dataset across various table-top manipulation tasks like picking ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: We propose FAS nple yet effective approach for tokenization of robot action trajectories via time-series compression, FAST enables training of autoregressive VLAs that ...
- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 2: Left: FAST tokenization enables training of autoregres- sive Transformers for dexterous robot control via simple next token prediction. Right: FAST outperforms popular binning ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 3: Effect of sampling rate on prediction performance. We train a small autoregressive transformer model on a didactic interpolation task, in which the network ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 4: Overview of the FAST action tokenization pipeline. Given a normalized chunk of actions, we apply discrete cosine transform (DCT) to convert the signal ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 5: Evaluation environments. We test FAST across 7 evaluation environments: 6 real-robot tasks and / simulation environment. The tasks are designed to test VLA ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 6: Comparison of policy performance using different tokenization approaches. We find that tokeni
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 7: Evaluation environments of FAST policy trained ‘on DROID [39]. We find that the same policy checkpoint generalizes robustly, and performs various simple table-top ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 8: Universal tokenizer, We test the compression rate

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | fon a large dataset of IM action sequences trained the universal tokenizer on the most diverse real robot dataset we could assemble, which includes ... | embodiment, simulator version and control stack | p. 7 (A. Experimental Setup), p. 6 (A. Experimental Setup) |
| Task/environment | We test FAST across 7 evaluation environments: 6 real-robot tasks and / simulation environment. | reset, timeout, object/scene variation | p. 6 (A. Experimental Setup), p. 6 (VI. EXPERIMENTS) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 3 (1. INTRODUCTION), p. 1 (1. INTRODUCTION) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 10 (C. Universal Action Tokenizer), p. 2 (1. INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We report success rate on individual clothing items. | definition/direction/unit from same section | p. 7 (A. Experimental Setup) |
| We develop a suite of 7 evaluation tasks 6 real robot, 1 simulated; see Figure 5), designed to test VLA performance on both, highly ... | definition/direction/unit from same section | p. 6 (A. Experimental Setup) |
| The tasks are designed to test VLA performance on highly dexterous tasks, like folding cloths from a laundry basket ("Laundry Folding"), and generalization, e.g, ... | definition/direction/unit from same section | p. 6 (A. Experimental Setup) |
| We measure average performance across LiberoSpatial, Libero-Object, Libero-Goal, and Libero-10. | definition/direction/unit from same section | p. 7 (A. Experimental Setup) |
| Fig. 3: Effect of sampling rate on prediction performance. We train a small autoregressive transformer model on a didactic interpolation task, in which the ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |
| Fig. 1: We propose FAS nple yet effective approach for tokenization of robot action trajectories via time-series compression, FAST enables training of autoregressive VLAs ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Fig. 2: Left: FAST tokenization enables training of autoregres- sive Transformers for dexterous robot control via simple next token prediction. Right: FAST outperforms popular ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |
| Fig. 8: Universal tokenizer, We test the compression rate | definition/direction/unit from same section | p. 8 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We then compare 7 models trained with FAST tokenization to the state-of-the-art 79 flow-matching (diffusion) VLA, and test the scaling of autoregressive VLA training ... | comparison identity and matched condition | p. 6 (VI. EXPERIMENTS) |
| Fig. 1: We propose FAS nple yet effective approach for tokenization of robot action trajectories via time-series compression, FAST enables training of autoregressive VLAs ... | comparison identity and matched condition | p. 1 (Figure/Table caption) |
| Fig. 2: Left: FAST tokenization enables training of autoregres- sive Transformers for dexterous robot control via simple next token prediction. Right: FAST outperforms popular ... | comparison identity and matched condition | p. 2 (Figure/Table caption) |
| We fine-tune the VLA models for robot action prediction, without weight freezing. | comparison identity and matched condition | p. 6 (A. Experimental Setup) |
| To our knowledge, this is the first "zero-shot" evaluation of DROID policies, in a completely unseen environment, without co-training or fine-tuning, simply by prompting ... | comparison identity and matched condition | p. 7 (A. Experimental Setup) |
| This tokenization strategy has been previously used to tokenize high-dimensional image data (50, 69], and can be viewed as an ablation of our compression-based ... | comparison identity and matched condition | p. 7 (A. Experimental Setup) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We fine-tune the VLA models for robot action prediction, without weight freezing. | component/input/data sensitivity | p. 6 (A. Experimental Setup) |
| To our knowledge, this is the first "zero-shot" evaluation of DROID policies, in a completely unseen environment, without co-training or fine-tuning, simply by prompting ... | component/input/data sensitivity | p. 7 (A. Experimental Setup) |
| + Toast out of toaster [7] (50 Hz): a bimanual Trossen Viper-X robot needs to remove two slices of bread from toaster and place ... | component/input/data sensitivity | p. 7 (A. Experimental Setup) |
| Fig. 3: Effect of sampling rate on prediction performance. We train a small autoregressive transformer model on a didactic interpolation task, in which the ... | component/input/data sensitivity | p. 3 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| 1: We propose FAS nple yet effective approach for tokenization of robot action trajectories via time-series compression, FAST enables training of autoregressive VLAs that ... | We report success rate on individual clothing items. | PDF body cue; verify exact table/figure and matched conditions | p. 7 (A. Experimental Setup), p. 2 (Figure/Table caption), p. 10 (Figure/Table caption), p. 6 (A. Experimental Setup), p. 6 (A. Experimental Setup), p. 7 (A. Experimental Setup) |
| Primary metric/result | Fig. 2: Left: FAST tokenization enables training of autoregres- sive Transformers for dexterous robot control via simple next token prediction. Right: FAST outperforms popular ... | numeric claim only at cited anchor | p. 2 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 7 / A. Experimental Setup - extractive body cue:** «+ Table bussing [7] (20 Hz): a URS single-arm robot needs to clean a table, sorting 12 objects into a trash bin (for trash) and ...
- **p. 7 / A. Experimental Setup - extractive body cue:** + TShirt folding [7] (50 Hz): a bi-manual ARX robot setup needs to fold various shirts on a stationary table top.
- **p. 7 / A. Experimental Setup - extractive body cue:** + Grocery bagging [7] (20 Hz): a URS single-arm robot needs to pack seven objects from a table into a grocery bag. taking care to ...
- **p. 7 / A. Experimental Setup - extractive body cue:** + Toast out of toaster [7] (50 Hz): a bimanual Trossen Viper-X robot needs to remove two slices of bread from toaster and place them ...
- **p. 7 / A. Experimental Setup - extractive body cue:** + Laundry folding [7] (50 Hz): a bi-manual ARX robot needs to take shirts and shorts from a basket, flatten them (on a table, fold ...
- **p. 7 / A. Experimental Setup - extractive body cue:** + Zero-shot DROID tabletop manipulation [9] (15 Hz): wwe test a policy trained on the full DROID dataset across various table-top manipulation tasks like picking ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Even unsuccessful trials show sensible behavior, like approaching the handles of microwave and dish washer doors, even if ultimately failing to open them, We ... | p. 8 (B. Comparing Action Tokenizers for VLA Training) |
| body limitation/failure cue | One current limitation of the autoregressive VLA is its inference speed: while 7» with diffusion typically predicts one second action chunks within 100ms on ... | p. 9 (C. Universal Action Tokenizer) |
| body limitation/failure cue | We will leave a detailed investigation of the language following abilities of diffusion and autoregressive VLAS to future work. | p. 9 (C. Universal Action Tokenizer) |
| body limitation/failure cue | While far from perfect, the level of generality and robustness of this policy substantially exceeds that of prior DROID policies. | p. 8 (B. Comparing Action Tokenizers for VLA Training) |
| body limitation/failure cue | ‘To summarize, we have demonstrated that FAST tokenization allows us to train autoregressive VLA on complex, dexterous robot tasks that prior tokenization schemes completely ... | p. 10 (C. Universal Action Tokenizer) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| One current limitation of the autoregressive VLA is its inference speed: while 7» with diffusion typically predicts one second action chunks within 100ms on ... | p. 9 (C. Universal Action Tokenizer) |
| For both approaches we use the default hyperparameters, which have comparable tokenization errors. | p. 7 (B. Comparing Action Tokenizers for VLA Training) |
| We find that the same policy checkpoint generalizes robustly, and performs various simple table-top tasks zero-shor across three test buildings. | p. 8 (B. Comparing Action Tokenizers for VLA Training) |
| Even unsuccessful trials show sensible behavior, like approaching the handles of microwave and dish washer doors, even if ultimately failing to open them, We ... | p. 8 (B. Comparing Action Tokenizers for VLA Training) |
| For state-of-the-art VLA training runs, which can often use thousands of GPU hours, a Sx reduction in required compute is significant. | p. 10 (C. Universal Action Tokenizer) |
| We include a full comparison across all tasks for a compute-matched 79 checkpoint in Appendix, Figure 15 and find that the same conclusions hold: ... | p. 10 (C. Universal Action Tokenizer) |
| We detail the steps from raw robot actions to action tokens in Figure 4. | p. 4 (B. The FAST Tokenization Algorithm) |
| After the data is normalized, we apply the discrete cosine transform to each action dimension separately. ‘To compress the DCT-converted signal we can simply ... | p. 4 (B. The FAST Tokenization Algorithm) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / B. Comparing Action Tokenizers for VLA Training - extractive body cue:** Even unsuccessful trials show sensible behavior, like approaching the handles of microwave and dish washer doors, even if ultimately failing to open them, We show ...
- **p. 9 / C. Universal Action Tokenizer - extractive body cue:** One current limitation of the autoregressive VLA is its inference speed: while 7» with diffusion typically predicts one second action chunks within 100ms on an ...
- **p. 9 / C. Universal Action Tokenizer - extractive body cue:** We will leave a detailed investigation of the language following abilities of diffusion and autoregressive VLAS to future work.
- **p. 8 / B. Comparing Action Tokenizers for VLA Training - extractive body cue:** While far from perfect, the level of generality and robustness of this policy substantially exceeds that of prior DROID policies.
- **p. 10 / C. Universal Action Tokenizer - extractive body cue:** ‘To summarize, we have demonstrated that FAST tokenization allows us to train autoregressive VLA on complex, dexterous robot tasks that prior tokenization schemes completely fail ...

- **Evidence anchors reviewed:** datasets p. 7 (A. Experimental Setup), p. 6 (A. Experimental Setup), p. 6 (VI. EXPERIMENTS), p. 7 (A. Experimental Setup), metrics p. 7 (A. Experimental Setup), p. 6 (A. Experimental Setup), p. 6 (A. Experimental Setup), p. 7 (A. Experimental Setup), p. 3 (Figure/Table caption), p. 1 (Figure/Table caption), baselines p. 6 (VI. EXPERIMENTS), p. 1 (Figure/Table caption), p. 2 (Figure/Table caption), p. 6 (A. Experimental Setup), p. 7 (A. Experimental Setup), p. 7 (A. Experimental Setup), results p. 7 (A. Experimental Setup), p. 2 (Figure/Table caption), p. 10 (Figure/Table caption), p. 6 (A. Experimental Setup), p. 6 (A. Experimental Setup), p. 7 (A. Experimental Setup).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (19 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** We develop a suite of 7 evaluation tasks 6 real robot, 1 simulated; see Figure 5), designed to test VLA performance on both, highly dexterous tasks like laundry folding, and ... (p. 6, A. Experimental Setup).
- **Metric evidence:** We develop a suite of 7 evaluation tasks 6 real robot, 1 simulated; see Figure 5), designed to test VLA performance on both, highly dexterous tasks like laundry folding, and ... (p. 6, A. Experimental Setup).
- **Baseline/ablation evidence:** We fine-tune the VLA models for robot action prediction, without weight freezing. (p. 6, A. Experimental Setup).
- **Failure/negative evidence:** We do ‘not measure success rates during these evaluations, but provide ‘numerous qualitative videos of successes and failures to help readers get a sense of the policy's capabilities (p. 18, B. Discussion of Alternative Compression Approaches).
