# Evaluation - Uni-NaVid: A Video-based Vision-Language-Action Model for Unifying Embodied Navigation Tasks

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p013.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p013.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (B. Individual Task Results), p. 8 (B. Individual Task Results), p. 11 (C. Qualitative Results in Real-World), p. 9 (B. Individual Task Results), p. 9 (B. Individual Task Results), p. 11 (C. Qualitative Results in Real-World)): The results in Table V demonstrate that our method achieves significant improvement over the zero-shot method (VLFM [93] and even outperforms the fine-tuned method (DAgRL+0D [94]) on the VAL SEEN ...

## Evaluation Body Digest

- **p. 7 / VI. EXPERIMENT - extractive body cue:** The robot then executes the predicted actions and calls STOP once the first predicted action is a stop action, For VLN and EQA tasks, we ...
- **p. 7 / VI. EXPERIMENT - extractive body cue:** + Object goal navigation: We use the validation split of the Habitat Matterport 3D (HM3D) dataset [67], which requires the agent to find target objects ...
- **p. 8 / VI. EXPERIMENT - extractive body cue:** During navigation, the robot asynchronously compresses and uploads the latest ‘observations to the model while executing pending actions, Refer to the supplementary video for real-world ...
- **p. 11 / C. Qualitative Results in Real-World - extractive body cue:** We believe that collecting data from these datasets could further enhance the navigation capabilities of our method. ‘Second, our method is designed to acquire multi-task ...
- **p. 8 / VI. EXPERIMENT - extractive body cue:** Comparison on VLN-CE R2R [42] Val-Unseen. *: Methods use highlevel action space. {: Methods use the same waypoint predictor proposed in [30]. {: Methods use ...
- **p. 10 / B. Individual Task Results - extractive body cue:** We provide third-person views with robot's trajectory, showing effective navigation performance.
- **p. 10 / C. Qualitative Results in Real-World - extractive body cue:** We conducted extensive experiments on real-world environ- ‘ments (experiment details are provided in the supplemental material) under diverse environments in a zero-shot manner, Notably, both ...
- **p. 11 / C. Qualitative Results in Real-World - extractive body cue:** First, Uni-NaVid is trained and evaluated on four welldefined navigation tasks, while there exists a large body of literature on insightful and practical navigation datasets ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** VI. EXPERIMENT (p. 7); B. Individual Task Results (p. 8); C. Qualitative Results in Real-World (p. 10).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| B. Individual Task Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | The results in Table V demonstrate that our method achieves significant improvement over the zero-shot method (VLFM [93] and even outperforms the fine-tuned method ... | p. 8 (B. Individual Task Results) |
| B. Individual Task Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | significant improvements, with a +25.7% increase in Success Rate (SR) on R2R. | p. 8 (B. Individual Task Results) |
| C. Qualitative Results in Real-World | EMPIRICAL / REAL-ROBOT OR HARDWARE | The results demonstrate the synergistic benefits of multi-task learning, which yields consistent performance improvements across all navigation tasks, Notably, VLN, ObjectNav, and EQA exhibit ... | p. 11 (C. Qualitative Results in Real-World) |
| B. Individual Task Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | IV-B), Uni-NaVidachieves performance comparable to state-of-the-art methods. | p. 9 (B. Individual Task Results) |
| B. Individual Task Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our method achieves ‘comparable performance to GPT-4V with scene captions [60]. | p. 9 (B. Individual Task Results) |

## Dataset / Benchmark Role

- **p. 7 / VI. EXPERIMENT - extractive body cue:** The robot then executes the predicted actions and calls STOP once the first predicted action is a stop action, For VLN and EQA tasks, we ...
- **p. 7 / VI. EXPERIMENT - extractive body cue:** + Object goal navigation: We use the validation split of the Habitat Matterport 3D (HM3D) dataset [67], which requires the agent to find target objects ...
- **p. 8 / VI. EXPERIMENT - extractive body cue:** During navigation, the robot asynchronously compresses and uploads the latest ‘observations to the model while executing pending actions, Refer to the supplementary video for real-world ...
- **p. 11 / C. Qualitative Results in Real-World - extractive body cue:** We believe that collecting data from these datasets could further enhance the navigation capabilities of our method. ‘Second, our method is designed to acquire multi-task ...
- **p. 8 / VI. EXPERIMENT - extractive body cue:** Comparison on VLN-CE R2R [42] Val-Unseen. *: Methods use highlevel action space. {: Methods use the same waypoint predictor proposed in [30]. {: Methods use ...
- **p. 10 / B. Individual Task Results - extractive body cue:** We provide third-person views with robot's trajectory, showing effective navigation performance.
- **p. 10 / C. Qualitative Results in Real-World - extractive body cue:** We conducted extensive experiments on real-world environ- ‘ments (experiment details are provided in the supplemental material) under diverse environments in a zero-shot manner, Notably, both ...
- **p. 11 / C. Qualitative Results in Real-World - extractive body cue:** First, Uni-NaVid is trained and evaluated on four welldefined navigation tasks, while there exists a large body of literature on insightful and practical navigation datasets ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: Uni-NaVid learns general navigation skills across four embodied navigation tasks using 3.6 million navigation samples.
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 3: Visualization of training data. We visualize the combination of training data (5.9M), video frame counts, and the most common words in navigation instructions.
- **p. 10 / Figure/Table caption - extractive body cue:** Fig. 5: Visual results of Uni-NaVid i
- **p. 10 / Figure/Table caption - extractive body cue:** Fig. 6: Vivusal results of Uni-NaVid on compostional tasks. The agent is required to execute complex instructions involving multiple navigation tasks. Our method successfully accomplishes ...
- **p. 11 / Figure/Table caption - extractive body cue:** Fig. 7: Action prediction on the VIN tasks. We evaluate Uni-NaVid on challenging open-vocabulary objects, requiring it to recognize the target objects and follow the ...
- **p. 11 / Figure/Table caption - extractive body cue:** Fig. 8: Comparsion on multi-task training and data scale. (a) We present the multi-task synergy of our method, illustrating the performance comparison between training with ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The robot then executes the predicted actions and calls STOP once the first predicted action is a stop action, For VLN and EQA tasks, ... | embodiment, simulator version and control stack | p. 7 (VI. EXPERIMENT), p. 7 (VI. EXPERIMENT) |
| Task/environment | + Object goal navigation: We use the validation split of the Habitat Matterport 3D (HM3D) dataset [67], which requires the agent to find target ... | reset, timeout, object/scene variation | p. 7 (VI. EXPERIMENT), p. 8 (VI. EXPERIMENT) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 1 (Abstract), p. 2 (1. Ivrropuction) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 3 (1. Ivrropuction), p. 3 (1. Ivrropuction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| standard evaluation metrics [4], including success rate (SR), oracle success rate (OS), success weighted by path length (SPL) [3], trajectory length (TL), following rate ... | definition/direction/unit from same section | p. 7 (VI. EXPERIMENT) |
| significant improvements, with a +25.7% increase in Success Rate (SR) on R2R. | definition/direction/unit from same section | p. 8 (B. Individual Task Results) |
| Nevertheless, Uni-NaVid still achieves significant gains in SR (44.7%) and SPL. | definition/direction/unit from same section | p. 8 (B. Individual Task Results) |
| MSVD-QA [MSRVTEQAAciivigyNecQA Method ‘Acct Seore?/Acct Score? /Acct Scoret VideoLLaMA [98] / 51.6 25 4 LL VideoChat [46] / 56.3 2.8 265 VideoChatGPT (59]] 689 ... | definition/direction/unit from same section | p. 9 (B. Individual Task Results) |
| Our method consistently demonstrates SOTA performance across these settings. | definition/direction/unit from same section | p. 9 (B. Individual Task Results) |
| We present a visualization of the training strategy's performance in Figure 8. | definition/direction/unit from same section | p. 10 (C. Qualitative Results in Real-World) |
| Our model demonstrates impressiove performance in aligning the current navigation process with the instructions to reason about the current state of navigation Furthermore, we ... | definition/direction/unit from same section | p. 10 (C. Qualitative Results in Real-World) |
| (a) We present the multi-task synergy of our method, illustrating the performance comparison between training with a single task and training with multiple tasks; ... | definition/direction/unit from same section | p. 11 (C. Qualitative Results in Real-World) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Compared to ‘mainstream baselines, we find that Uni-NaVid archives the best performance on four metrics, including BLUE-1 (417.9%), ROUGE (5.7%), METEOR (+ 16.2%), and ... | comparison identity and matched condition | p. 9 (B. Individual Task Results) |
| To evaluate the general-purpose na we conduct extensive experiments on individual navigation tasks, employing corresponding strong baselines. | comparison identity and matched condition | p. 7 (VI. EXPERIMENT) |
| Comparison on vision-and-language navigation, We evaluate our method with mainstream baselines on two publicly available benchmarks: VLN-CE R2R [42] and RxR [45]. | comparison identity and matched condition | p. 8 (B. Individual Task Results) |
| As shown in ‘Table VIL, Uni-NaVid outperforms the comparison methods fon both SR. | comparison identity and matched condition | p. 9 (B. Individual Task Results) |
| standard evaluation metrics [4], including success rate (SR), oracle success rate (OS), success weighted by path length (SPL) [3], trajectory length (TL), following rate ... | comparison identity and matched condition | p. 7 (VI. EXPERIMENT) |
| (48.8%) compared to previous state-of-theart methods. | comparison identity and matched condition | p. 8 (B. Individual Task Results) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| It is worth noting that for EQA [21] task, the agent executes navigation actions until a stop command is issued, We then remove the ... | component/input/data sensitivity | p. 7 (VI. EXPERIMENT) |
| Ablation on training strategy and architecture. | component/input/data sensitivity | p. 11 (C. Qualitative Results in Real-World) |
| Additional ablation studies on architecture and hyperparameters are provided in the Supplementary Materia | component/input/data sensitivity | p. 11 (C. Qualitative Results in Real-World) |
| We add experiments of removing RXR samples in Supplemntal Material, where our method still achive STOA performance (+23.9 SR(%)) against NaVid. | component/input/data sensitivity | p. 8 (B. Individual Task Results) |
| The results in Table V demonstrate that our method achieves significant improvement over the zero-shot method (VLFM [93] and even outperforms the fine-tuned method ... | component/input/data sensitivity | p. 8 (B. Individual Task Results) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| However, our goal is to train and ‘evaluate our method on mainstream datasets to clearly justify the performance of our approach. | The results in Table V demonstrate that our method achieves significant improvement over the zero-shot method (VLFM [93] and even outperforms the fine-tuned method ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (B. Individual Task Results), p. 8 (B. Individual Task Results), p. 11 (C. Qualitative Results in Real-World), p. 9 (B. Individual Task Results), p. 9 (B. Individual Task Results), p. 11 (C. Qualitative Results in Real-World) |
| Primary metric/result | significant improvements, with a +25.7% increase in Success Rate (SR) on R2R. | numeric claim only at cited anchor | p. 8 (B. Individual Task Results) |

- Numeric sentences retained from the body:
- **p. 8 / VI. EXPERIMENT - extractive body cue:** SRP WDNR [ee 762631 aU 360 EMA" 0) vay 1090 620 $20 410, MINCBERT G0) 7 YY 1228 574 530440 390, Sinasinr a] In 607 ...
- **p. 8 / VI. EXPERIMENT - extractive body cue:** (17) ve 2 6s 63 INavid® (100), Y /inso sar 34s 288 212 UnkNavid Y [iss 624 58s 4x7 409
- **p. 9 / B. Individual Task Results - extractive body cue:** 27819 7s DAgkL aos ass [183 79 VLEME (93) / 35 324173 [382196 DAgRL+OD (94) / 385 soo ars [3719s Unknaviay [413 211 489 aus ...
- **p. 9 / B. Individual Task Results - extractive body cue:** SRGB/ SRP FRY CR, PolFormer 197] v / 219 2035293 PoliFormer* [97]] Vv / 1467 37.14 4.29 PoliFormert [97]] ¢ ¥ / 2529 47.16 6.78 ...
- **p. 9 / B. Individual Task Results - extractive body cue:** VNGMCAN DS] ITT 394520 SROMCAN [96] 2056 785 MGS 11975736 SD-LLMiflamingo) (31) 20 48S 656 Naval (103), 73 40231656 80.77 BridgeQa (62) Ma 4325 test ...
- **p. 11 / C. Qualitative Results in Real-World - extractive body cue:** Dp [VEN (SRF) ObjNav (SRF) FON (ACC) Fatow (SR No hws ken) S2 «TT aa 31 No VOA data 405506 19 588 Care 561 ms ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | standard evaluation metrics [4], including success rate (SR), oracle success rate (OS), success weighted by path length (SPL) [3], trajectory length (TL), following rate ... | p. 7 (VI. EXPERIMENT) |
| body limitation/failure cue | Despite the promising results, Uni-NaVid has several limitations. | p. 11 (C. Qualitative Results in Real-World) |
| body limitation/failure cue | This limitation could be alleviated by extending the moel to predict | p. 11 (C. Qualitative Results in Real-World) |
| body limitation/failure cue | gies, while also highlighting robust open-world understanding capabilities. | p. 10 (B. Individual Task Results) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| For real-world deployment, we utilize a remote server with an NVIDIA A100 GPU to run Uni-NaVid, which processes observations (along with text | p. 7 (VI. EXPERIMENT) |
| Uni-NaVid is trained on a cluster server with 40 NVIDIA H800 GPUs for approximately 35 hours, totaling 1400 GPU hours. | p. 7 (B. Training Strategy of Uni-NaVid) |
| Additional ablation studies on architecture and hyperparameters are provided in the Supplementary Materia | p. 11 (C. Qualitative Results in Real-World) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / VI. EXPERIMENT - extractive body cue:** standard evaluation metrics [4], including success rate (SR), oracle success rate (OS), success weighted by path length (SPL) [3], trajectory length (TL), following rate (FR) ...
- **p. 11 / C. Qualitative Results in Real-World - extractive body cue:** Despite the promising results, Uni-NaVid has several limitations.
- **p. 11 / C. Qualitative Results in Real-World - extractive body cue:** This limitation could be alleviated by extending the moel to predict
- **p. 10 / B. Individual Task Results - extractive body cue:** gies, while also highlighting robust open-world understanding capabilities.

- **Evidence anchors reviewed:** datasets p. 7 (VI. EXPERIMENT), p. 7 (VI. EXPERIMENT), p. 8 (VI. EXPERIMENT), p. 11 (C. Qualitative Results in Real-World), p. 8 (VI. EXPERIMENT), p. 10 (B. Individual Task Results), metrics p. 7 (VI. EXPERIMENT), p. 8 (B. Individual Task Results), p. 8 (B. Individual Task Results), p. 9 (B. Individual Task Results), p. 9 (B. Individual Task Results), p. 10 (C. Qualitative Results in Real-World), baselines p. 9 (B. Individual Task Results), p. 7 (VI. EXPERIMENT), p. 8 (B. Individual Task Results), p. 9 (B. Individual Task Results), p. 7 (VI. EXPERIMENT), p. 8 (B. Individual Task Results), results p. 8 (B. Individual Task Results), p. 8 (B. Individual Task Results), p. 11 (C. Qualitative Results in Real-World), p. 9 (B. Individual Task Results), p. 9 (B. Individual Task Results), p. 11 (C. Qualitative Results in Real-World).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (17 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** The results in Table V demonstrate that our method achieves significant improvement over the zero-shot method (VLFM [93] and even outperforms the fine-tuned method (DAgRL+0D [94]) on the VAL SEEN ... (p. 8, B. Individual Task Results).
- **Metric evidence:** significant improvements, with a +25.7% increase in Success Rate (SR) on R2R. (p. 8, B. Individual Task Results).
- **Baseline/ablation evidence:** Comparison on vision-and-language navigation, We evaluate our method with mainstream baselines on two publicly available benchmarks: VLN-CE R2R [42] and RxR [45]. (p. 8, B. Individual Task Results).
- **Failure/negative evidence:** Despite the promising results, Uni-NaVid has several limitations. (p. 11, C. Qualitative Results in Real-World).
