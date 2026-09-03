# Evaluation - RoboOmni: Actions Are Just Another Modality for Vision-Language Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (25 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=qdXOfyGMuB; PDF retrieval source: https://openreview.net/pdf/b090562c668703f4568061335c66e0e592e16d9d.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (4.3. Real Robot Experiments), p. 7 (4.4. Ablation Study), p. 8 (Figure/Table caption), p. 6 (4.2. Evaluation on SimplerEnv), p. 8 (4.4. Ablation Study), p. 6 (4.1. Evaluation on Calvin)): On average, RoboOmni achieves a 91% success rate, significantly surpassing π0-FAST (68%) and RoboVLMs (60%).

## Evaluation Body Digest

- **p. 5 / 4. Experiment - extractive body cue:** We evaluate RoboOmni across three complementary settings: (1) long-horizon multi-task manipulation on the CALVIN benchmark, (2) Google Robot tasks in the SimplerEnv simulator, and (3) ...
- **p. 6 / 4.2. Evaluation on SimplerEnv - extractive body cue:** We evaluate RoboOmni on the Google Robot tasks within SimplerEnv (Li et al., 2024), which is designed to assess real-to-sim transfer for VLAs trained on ...
- **p. 5 / 4.1. Evaluation on Calvin - extractive body cue:** CALVIN (Mees et al., 2022b) is a simulation benchmark for multi-task tabletop manipulation.
- **p. 7 / 4.3. Real Robot Experiments - extractive body cue:** The training dataset consists of 18k human demonstrations across 37 tasks, including both pick-and-place and non-pick-and-place manipulation.
- **p. 7 / 4.2. Evaluation on SimplerEnv - extractive body cue:** Real-to-Sim performance comparison on Google Robot tasks in SimplerEnv (Visual Matching setting).
- **p. 6 / 4.1. Evaluation on Calvin - extractive body cue:** Performance comparison on the CALVIN benchmark.
- **p. 8 / 4.4. Ablation Study - extractive body cue:** Comparison of success rates in the real-world setting.
- **p. 8 / 4.4. Ablation Study - extractive body cue:** We conducted extensive ablation studies on the CALVIN benchmark to systematically evaluate the contribution of each key design choice within the RoboOmni framework.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 4. Experiment (p. 5); 4.1. Evaluation on Calvin (p. 5); 4.2. Evaluation on SimplerEnv (p. 6); 4.3. Real Robot Experiments (p. 7).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4.3. Real Robot Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | On average, RoboOmni achieves a 91% success rate, significantly surpassing π0-FAST (68%) and RoboVLMs (60%). | p. 7 (4.3. Real Robot Experiments) |
| 4.4. Ablation Study | EMPIRICAL / REAL-ROBOT OR HARDWARE | For the FAST tokenizer, enabling MTAP improves the 5-task success rate from 80.1% to 88.1%. | p. 7 (4.4. Ablation Study) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 3. Comparison of success rates in the real-world setting. RoboOmni consistently outperforms baselines, including π0-FAST and RoboVLMs, particularly in the challenging Unseen Objects ... | p. 8 (Figure/Table caption) |
| 4.2. Evaluation on SimplerEnv | EMPIRICAL / REAL-ROBOT OR HARDWARE | As presented in Table 2, RoboOmni establishes a new performance standard, significantly outperforming prior unified and continuous baselines. | p. 6 (4.2. Evaluation on SimplerEnv) |
| 4.4. Ablation Study | EMPIRICAL / REAL-ROBOT OR HARDWARE | For the FAST tokenizer, performance peaks with 256 bins, achieving a 88.1% 5-task success rate. | p. 8 (4.4. Ablation Study) |

## Dataset / Benchmark Role

- **p. 5 / 4. Experiment - extractive body cue:** We evaluate RoboOmni across three complementary settings: (1) long-horizon multi-task manipulation on the CALVIN benchmark, (2) Google Robot tasks in the SimplerEnv simulator, and (3) ...
- **p. 6 / 4.2. Evaluation on SimplerEnv - extractive body cue:** We evaluate RoboOmni on the Google Robot tasks within SimplerEnv (Li et al., 2024), which is designed to assess real-to-sim transfer for VLAs trained on ...
- **p. 5 / 4.1. Evaluation on Calvin - extractive body cue:** CALVIN (Mees et al., 2022b) is a simulation benchmark for multi-task tabletop manipulation.
- **p. 7 / 4.3. Real Robot Experiments - extractive body cue:** The training dataset consists of 18k human demonstrations across 37 tasks, including both pick-and-place and non-pick-and-place manipulation.
- **p. 7 / 4.2. Evaluation on SimplerEnv - extractive body cue:** Real-to-Sim performance comparison on Google Robot tasks in SimplerEnv (Visual Matching setting).
- **p. 6 / 4.1. Evaluation on Calvin - extractive body cue:** Performance comparison on the CALVIN benchmark.
- **p. 8 / 4.4. Ablation Study - extractive body cue:** Comparison of success rates in the real-world setting.
- **p. 8 / 4.4. Ablation Study - extractive body cue:** We conducted extensive ablation studies on the CALVIN benchmark to systematically evaluate the contribution of each key design choice within the RoboOmni framework.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1. Overview of the RoboOmni framework and its performance. The bottom section illustrates the multi-modal interleaved data input. The top-left section details the model ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. Architectural overview of RoboOmni. The model processes multi-modal interleaved input sequences comprising visual observations (V ), text instructions (T), robot states (S), and ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Performance comparison on the CALVIN benchmark. The table evaluates models on two settings: in-distribution performance (Train: ABCD, Eval: D) and out-of-distribution generalization (Train: ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2. Real-to-Sim performance comparison on Google Robot tasks in SimplerEnv (Visual Matching setting). We report the average success rate over 3 distinct tasks. Pick ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 3. Ablation study of MTAP and different tokenizers. Settings Top K Success Rate Task Len. Speed (ms/action) MTAP Tokenizer
- **p. 7 / Figure/Table caption - extractive body cue:** Table 4. Ablation study on the number of bins for action discretiza- tion. All models are trained with MTAP. The default setting used in our ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 3. Comparison of success rates in the real-world setting. RoboOmni consistently outperforms baselines, including π0-FAST and RoboVLMs, particularly in the challenging Unseen Objects setting. ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 5. Ablation studies on window size, model size, and training strategies. The default setting is RoboOmni(Bin) with a window size of 5 and a ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We evaluate RoboOmni across three complementary settings: (1) long-horizon multi-task manipulation on the CALVIN benchmark, (2) Google Robot tasks in the SimplerEnv simulator, and ... | embodiment, simulator version and control stack | p. 5 (4. Experiment), p. 6 (4.2. Evaluation on SimplerEnv) |
| Task/environment | We evaluate RoboOmni on the Google Robot tasks within SimplerEnv (Li et al., 2024), which is designed to assess real-to-sim transfer for VLAs trained ... | reset, timeout, object/scene variation | p. 6 (4.2. Evaluation on SimplerEnv), p. 5 (4.1. Evaluation on Calvin) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 4 (3.1. MTAP for Action Chunking), p. 5 (3.2. Multi-Modal Action Co-Training) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 5 (3.3. Training VLA as VLM), p. 2 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Ablating the history length reveals that increasing the window size from 1 to 5 yields a significant performance gain (81.3% to 83.4% 5-task success ... | definition/direction/unit from same section | p. 8 (4.4. Ablation Study) |
| Crucially, RoboOmni exhibits exceptional robustness in the most challenging Unseen Objects setting, maintaining a 91% success rate. | definition/direction/unit from same section | p. 7 (4.3. Real Robot Experiments) |
| First, the high success rates on object-interaction tasks (e.g., Pick Coke Can) demonstrate that our discrete tokenization, coupled with MTAP action chunking, achieves the ... | definition/direction/unit from same section | p. 7 (4.2. Evaluation on SimplerEnv) |
| For the FAST tokenizer, performance peaks with 256 bins, achieving a 88.1% 5-task success rate. | definition/direction/unit from same section | p. 8 (4.4. Ablation Study) |
| We report the success rates of achieving 1 through 5 consecutive tasks, as well as the average number of tasks completed per trial (Task ... | definition/direction/unit from same section | p. 5 (4.1. Evaluation on Calvin) |
| Method Train Consecutive tasks success rates Task Len. | definition/direction/unit from same section | p. 6 (4.1. Evaluation on Calvin) |
| RoboOmni(FAST) achieves an average success rate of 86.8%, surpassing the strongest continuous baseline, SpatialVLA, by over 16%. | definition/direction/unit from same section | p. 6 (4.2. Evaluation on SimplerEnv) |
| Table 6. Comprehensive experimental results and ablation studies on the CALVIN (ABCD→D) benchmark. This table aggregates all configurations evaluated in our study for a ... | definition/direction/unit from same section | p. 17 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Figure 3. Comparison of success rates in the real-world setting. RoboOmni consistently outperforms baselines, including π0-FAST and RoboVLMs, particularly in the challenging Unseen Objects ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| As presented in Table 2, RoboOmni establishes a new performance standard, significantly outperforming prior unified and continuous baselines. | comparison identity and matched condition | p. 6 (4.2. Evaluation on SimplerEnv) |
| RoboOmni demonstrates superior robustness to visual domain shifts compared to baselines. | comparison identity and matched condition | p. 7 (4.2. Evaluation on SimplerEnv) |
| We compare RoboOmni against strong baselines including OpenVLA (Kim et al., 2024), Octo (Team et al., 2024), GR-1 (Wu et al., 2023), RoboVLMs (Li ... | comparison identity and matched condition | p. 7 (4.3. Real Robot Experiments) |
| Across all settings, we compare RoboOmni against three representative and widely adopted unified VLA baselines: OpenVLA (Kim et al., 2024) is an autoregressive visionlanguage-action ... | comparison identity and matched condition | p. 5 (4. Experiment) |
| Our RoboOmni models, with both Bin and FAST tokenizers, establish new state-of-the-art (SOTA) results in both settings. | comparison identity and matched condition | p. 6 (4.1. Evaluation on Calvin) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Default Configuration RoboOmni(Bin) 0.997 0.940 0.834 4.64 Ablation on Window Size Window Size = 1 0.973 0.897 0.813 4.49 Window Size = 10 0.985 ... | component/input/data sensitivity | p. 8 (4.4. Ablation Study) |
| Notably, the FAST variant exhibits superior out-of-distribution generalization (ABC→D), suggesting the frequency-domain representation effectively offloads temporal modeling pressure from the backbone. | component/input/data sensitivity | p. 6 (4.1. Evaluation on Calvin) |
| We conduct a series of ablation studies to evaluate the contributions of key components in our framework on Calvin Benchmark. | component/input/data sensitivity | p. 7 (4.4. Ablation Study) |
| Ablation on Architectural and Training Components. | component/input/data sensitivity | p. 8 (4.4. Ablation Study) |
| In our reproduction, the model is trained exclusively on manipulation data to align with the setting without VLM described in the original paper. | component/input/data sensitivity | p. 5 (4. Experiment) |
| Across all settings, we compare RoboOmni against three representative and widely adopted unified VLA baselines: OpenVLA (Kim et al., 2024) is an autoregressive visionlanguage-action ... | component/input/data sensitivity | p. 5 (4. Experiment) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To overcome these challenges, we introduce a versatile Multi-Token Action Prediction (MTAP) framework that enables efficient, parallelized action prediction within a unified discrete architecture. | On average, RoboOmni achieves a 91% success rate, significantly surpassing π0-FAST (68%) and RoboVLMs (60%). | PDF body cue; verify exact table/figure and matched conditions | p. 7 (4.3. Real Robot Experiments), p. 7 (4.4. Ablation Study), p. 8 (Figure/Table caption), p. 6 (4.2. Evaluation on SimplerEnv), p. 8 (4.4. Ablation Study), p. 6 (4.1. Evaluation on Calvin) |
| Primary metric/result | For the FAST tokenizer, enabling MTAP improves the 5-task success rate from 80.1% to 88.1%. | numeric claim only at cited anchor | p. 7 (4.4. Ablation Study) |

- Numeric sentences retained from the body:
- **p. 5 / 4.1. Evaluation on Calvin - extractive body cue:** Following prior work, we train on the ABCD and ABC splits and evaluate solely on split D with 1,000 rollouts per model.
- **p. 7 / 4.3. Real Robot Experiments - extractive body cue:** The training dataset consists of 18k human demonstrations across 37 tasks, including both pick-and-place and non-pick-and-place manipulation.
- **p. 7 / 4.4. Ablation Study - extractive body cue:** Tokenizer Bin Size Top 1 Top 3 Top 5 Task Len.
- **p. 7 / 4.4. Ablation Study - extractive body cue:** Without MTAP, the fully autoregressive Bin tokenizer is exceedingly slow (107 ms/action).
- **p. 8 / 4.4. Ablation Study - extractive body cue:** This not only makes the Bin tokenizer significantly more efficient but also faster than the MTAP-enabled FAST tokenizer (17.5 ms/action), presenting a compelling trade-off between ...
- **p. 4 / 3.1. MTAP for Action Chunking - extractive body cue:** This design enables parallel decoding of the entire action chunk from a single shared context, aggregating the loss across predictions: L = H-1 X k=0 ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | The table evaluates models on two settings: in-distribution performance (Train: ABCD, Eval: D) and out-of-distribution generalization (Train: ABC, Eval: D). | p. 6 (4.1. Evaluation on Calvin) |
| body limitation/failure cue | Notably, the FAST variant exhibits superior out-of-distribution generalization (ABC→D), suggesting the frequency-domain representation effectively offloads temporal modeling pressure from the backbone. | p. 6 (4.1. Evaluation on Calvin) |
| body limitation/failure cue | Robust Generalization to Novel Scenarios. | p. 7 (4.3. Real Robot Experiments) |
| body limitation/failure cue | RoboOmni demonstrates superior robustness to visual domain shifts compared to baselines. | p. 7 (4.2. Evaluation on SimplerEnv) |
| body limitation/failure cue | Finally, removing any of our core training strategies degrades performance. | p. 8 (4.4. Ablation Study) |
| body limitation/failure cue | A similar trend is observed for the Bin tokenizer, where performance is highest with 128 bins (83.7%) and 256 bins (83.4%), but degrades significantly ... | p. 8 (4.4. Ablation Study) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| By enabling parallel decoding over the action chunk, MTAP provides a near-linear speedup, slashing the inference time to just 12.1 7 | p. 7 (4.4. Ablation Study) |
| To support multi-modal co-training, we build a unified tokenization scheme that encodes all modalities. | p. 4 (3.2. Multi-Modal Action Co-Training) |
| See Appendix D.2 for implementation details. | p. 5 (4. Experiment) |
| We report the success rates of achieving 1 through 5 consecutive tasks, as well as the average number of tasks completed per trial (Task ... | p. 5 (4.1. Evaluation on Calvin) |
| See Appendix D.3 for detailed implementation settings. | p. 6 (4.2. Evaluation on SimplerEnv) |
| Second, the model's dominance in the Visual Matching setting indicates exceptional robustness to sim-to-real visual shifts, suggesting that preserving the VLM's pre-trained visual representations ... | p. 7 (4.2. Evaluation on SimplerEnv) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / 4.1. Evaluation on Calvin - extractive body cue:** The table evaluates models on two settings: in-distribution performance (Train: ABCD, Eval: D) and out-of-distribution generalization (Train: ABC, Eval: D).
- **p. 6 / 4.1. Evaluation on Calvin - extractive body cue:** Notably, the FAST variant exhibits superior out-of-distribution generalization (ABC→D), suggesting the frequency-domain representation effectively offloads temporal modeling pressure from the backbone.
- **p. 7 / 4.3. Real Robot Experiments - extractive body cue:** Robust Generalization to Novel Scenarios.
- **p. 7 / 4.2. Evaluation on SimplerEnv - extractive body cue:** RoboOmni demonstrates superior robustness to visual domain shifts compared to baselines.
- **p. 8 / 4.4. Ablation Study - extractive body cue:** Finally, removing any of our core training strategies degrades performance.
- **p. 8 / 4.4. Ablation Study - extractive body cue:** A similar trend is observed for the Bin tokenizer, where performance is highest with 128 bins (83.7%) and 256 bins (83.4%), but degrades significantly when ...

- **Evidence anchors reviewed:** datasets p. 5 (4. Experiment), p. 6 (4.2. Evaluation on SimplerEnv), p. 5 (4.1. Evaluation on Calvin), p. 7 (4.3. Real Robot Experiments), p. 7 (4.2. Evaluation on SimplerEnv), p. 6 (4.1. Evaluation on Calvin), metrics p. 8 (4.4. Ablation Study), p. 7 (4.3. Real Robot Experiments), p. 7 (4.2. Evaluation on SimplerEnv), p. 8 (4.4. Ablation Study), p. 5 (4.1. Evaluation on Calvin), p. 6 (4.1. Evaluation on Calvin), baselines p. 8 (Figure/Table caption), p. 6 (4.2. Evaluation on SimplerEnv), p. 7 (4.2. Evaluation on SimplerEnv), p. 7 (4.3. Real Robot Experiments), p. 5 (4. Experiment), p. 6 (4.1. Evaluation on Calvin), results p. 7 (4.3. Real Robot Experiments), p. 7 (4.4. Ablation Study), p. 8 (Figure/Table caption), p. 6 (4.2. Evaluation on SimplerEnv), p. 8 (4.4. Ablation Study), p. 6 (4.1. Evaluation on Calvin).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
