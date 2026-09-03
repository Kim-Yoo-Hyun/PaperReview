# Evaluation - Unified Video Action Model

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (13 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p074.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p074.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (B. Real-world Benchmarks), p. 8 (B. Real-world Benchmarks), p. 7 (B. Real-world Benchmarks), p. 5 (A. Simulation Benchmarks), p. 5 (B. Real-world Benchmarks), p. 7 (B. Real-world Benchmarks)): For example, with changes in goal color, UniPi achieves a success rate of 40%, UVA achieves 64%, while OpenVLA only reaches 32%.

## Evaluation Body Digest

- **p. 6 / B. Real-world Benchmarks - extractive body cue:** Trained on a diverse dataset spanning multiple robot embodiments and tasks, xo demonstrates. strong zero-shot and fine-tuned performance.
- **p. 5 / B. Real-world Benchmarks - extractive body cue:** Since the training data were collected independently in prior work, all evaluation cases are Out-of-Distribution (OOD), involving unseen environments, objects, and robots.
- **p. 6 / B. Real-world Benchmarks - extractive body cue:** significantly out-of-distribution with unseen environments, objects, robots, and even gripper colors.
- **p. 5 / B. Real-world Benchmarks - extractive body cue:** We randomly selected 500 episodes from each dataset and combined them into a dataset to train both our ‘model and Diffusion Policy (11).
- **p. 7 / B. Real-world Benchmarks - extractive body cue:** We ensure a fair comparison by keeping the initial placement of objects and grippers identical across different methods for each test rollout Real-World Single-Task: First, ...
- **p. 8 / B. Real-world Benchmarks - extractive body cue:** All tests are unseen during training, and even with more challenging distractor objects and backgrounds, UVA achieves higher success rates than DP-UML To more rigorously ...
- **p. 7 / B. Real-world Benchmarks - extractive body cue:** Action Prediction Accuracy (Real-World Tasks): Table Il shows the results of real-world tasks.
- **p. 8 / B. Real-world Benchmarks - extractive body cue:** This explains why DP-C is slower than UVA in Table I and DP-UMI is faster in Table I, ‘Overall, UVA achieves a good balance between ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** uncertain robot state와 safe/unsafe operating region.
- **Input boundary:** observation, uncertainty/risk estimate와 task command.
- **Output/decision under evaluation:** shielded, recovery 또는 safe action.
- **Primary target:** task return과 violation/failure probability.
- **Detected evaluation headings:** A. Simulation Benchmarks (p. 5); B. Real-world Benchmarks (p. 5).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| B. Real-world Benchmarks | EMPIRICAL / REAL-ROBOT OR HARDWARE | For example, with changes in goal color, UniPi achieves a success rate of 40%, UVA achieves 64%, while OpenVLA only reaches 32%. | p. 8 (B. Real-world Benchmarks) |
| B. Real-world Benchmarks | EMPIRICAL / REAL-ROBOT OR HARDWARE | All tests are unseen during training, and even with more challenging distractor objects and backgrounds, UVA achieves higher success rates than DP-UML To more ... | p. 8 (B. Real-world Benchmarks) |
| B. Real-world Benchmarks | EMPIRICAL / REAL-ROBOT OR HARDWARE | We found that the UVA Attention module in the Transformer accounts for half of the inference time, making UVA slightly slower than DP-UML With ... | p. 7 (B. Real-world Benchmarks) |
| A. Simulation Benchmarks | EMPIRICAL / REAL-ROBOT OR HARDWARE | UVA has higher success rate than the baselines in most settings, with a strong performance in multi-task scenatios, Speed is measured by a single ... | p. 5 (A. Simulation Benchmarks) |
| B. Real-world Benchmarks | EMPIRICAL / REAL-ROBOT OR HARDWARE | We evaluate each method over 20 rollouts with varying initial configurations and report the average success rate MulticTask Evaluation: We train one model with ... | p. 5 (B. Real-world Benchmarks) |

## Dataset / Benchmark Role

- **p. 6 / B. Real-world Benchmarks - extractive body cue:** Trained on a diverse dataset spanning multiple robot embodiments and tasks, xo demonstrates. strong zero-shot and fine-tuned performance.
- **p. 5 / B. Real-world Benchmarks - extractive body cue:** Since the training data were collected independently in prior work, all evaluation cases are Out-of-Distribution (OOD), involving unseen environments, objects, and robots.
- **p. 6 / B. Real-world Benchmarks - extractive body cue:** significantly out-of-distribution with unseen environments, objects, robots, and even gripper colors.
- **p. 5 / B. Real-world Benchmarks - extractive body cue:** We randomly selected 500 episodes from each dataset and combined them into a dataset to train both our ‘model and Diffusion Policy (11).
- **p. 7 / B. Real-world Benchmarks - extractive body cue:** We ensure a fair comparison by keeping the initial placement of objects and grippers identical across different methods for each test rollout Real-World Single-Task: First, ...
- **p. 8 / B. Real-world Benchmarks - extractive body cue:** All tests are unseen during training, and even with more challenging distractor objects and backgrounds, UVA achieves higher success rates than DP-UML To more rigorously ...
- **p. 7 / B. Real-world Benchmarks - extractive body cue:** Action Prediction Accuracy (Real-World Tasks): Table Il shows the results of real-world tasks.
- **p. 8 / B. Real-world Benchmarks - extractive body cue:** This explains why DP-C is slower than UVA in Table I and DP-UMI is faster in Table I, ‘Overall, UVA achieves a good balance between ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: Unified Video Action Model. (a) UVA features a joint video-action latent representation and decoupled video-action decoding. The Joint latent representation effectively models the ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 3: Simulation Environments. We evaluate UVA and baselines in both single-task and multi-task settings. n the multi-task scenario, the goal can be defined through ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 5: Visual Disturbances on Push, Tasks are performed under altered visual conditions, including changes in background color, distracting background objects, and goal color.
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 6: Robustness to History Length on Push EM. Typical policy learning frameworks such as DP-C [10] often experience performance ‘drops with increased history length ...
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 7: Video Generation Results on Validation Set. UVA generates high-quality videos that closely match the ground truth, with 8
- **p. 10 / Figure/Table caption - extractive body cue:** Fig. 8: Forward Dynamics Model on Block Pushing Task. During training, the robot pushes two blocks randomly to any target. During testing, the generated future ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Trained on a diverse dataset spanning multiple robot embodiments and tasks, xo demonstrates. strong zero-shot and fine-tuned performance. | embodiment, simulator version and control stack | p. 6 (B. Real-world Benchmarks), p. 5 (B. Real-world Benchmarks) |
| Task/environment | Since the training data were collected independently in prior work, all evaluation cases are Out-of-Distribution (OOD), involving unseen environments, objects, and robots. | reset, timeout, object/scene variation | p. 5 (B. Real-world Benchmarks), p. 6 (B. Real-world Benchmarks) |
| Observation/sensor | observation, uncertainty/risk estimate와 task command | calibration, preprocessing, privileged input | p. 2 (1. Iyrropucrion), p. 3 (1. Iyrropucrion) |
| Output/decision | shielded, recovery 또는 safe action | action frame, controller and termination | p. 1 (Body text (section boundary not confidently recovered)), p. 2 (1. Iyrropucrion) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| UVA has higher success rate than the baselines in most settings, with a strong performance in multi-task scenatios, Speed is measured by a single ... | definition/direction/unit from same section | p. 5 (A. Simulation Benchmarks) |
| We evaluate each method over 20 rollouts with varying initial configurations and report the average success rate MulticTask Evaluation: We train one model with ... | definition/direction/unit from same section | p. 5 (B. Real-world Benchmarks) |
| Our approach demonstrates. superior performance in the multi-task setting, achieving a 15% higher success rate on the Cup task and a 40% higher success ... | definition/direction/unit from same section | p. 7 (B. Real-world Benchmarks) |
| Our method and UniPi, both video generation models, have higher success rates compared to other policy learning approaches. | definition/direction/unit from same section | p. 7 (B. Real-world Benchmarks) |
| For example, with changes in goal color, UniPi achieves a success rate of 40%, UVA achieves 64%, while OpenVLA only reaches 32%. | definition/direction/unit from same section | p. 8 (B. Real-world Benchmarks) |
| All tests are unseen during training, and even with more challenging distractor objects and backgrounds, UVA achieves higher success rates than DP-UML To more ... | definition/direction/unit from same section | p. 8 (B. Real-world Benchmarks) |
| We evaluate policy learning results with UVA compared to the baseline methods on a few different axes: 1) action prediction accuracy, 2) inference speed, ... | definition/direction/unit from same section | p. 6 (B. Real-world Benchmarks) |
| Action Prediction Accuracy (Simulation Tasks): In Table I, ‘we compare UVA with baseline methods in both single-task | definition/direction/unit from same section | p. 6 (B. Real-world Benchmarks) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| This evaluation aims to compare ‘our method with a strong baseline in prior works by replicating 4 similar evaluation setup. | comparison identity and matched condition | p. 7 (B. Real-world Benchmarks) |
| We evaluate policy learning results with UVA compared to the baseline methods on a few different axes: 1) action prediction accuracy, 2) inference speed, ... | comparison identity and matched condition | p. 6 (B. Real-world Benchmarks) |
| Simulation Single~Task: Our method is able to match the performance of the state-of-the-art model DP-C and signifi- ‘cantly outperform other video-based methods such as ... | comparison identity and matched condition | p. 7 (B. Real-world Benchmarks) |
| We ‘compare UVA with the baselines on the PushT (10, 16} and ‘Toolhang [32] tasks. | comparison identity and matched condition | p. 5 (A. Simulation Benchmarks) |
| UVA has higher success rate than the baselines in most settings, with a strong performance in multi-task scenatios, Speed is measured by a single ... | comparison identity and matched condition | p. 5 (A. Simulation Benchmarks) |
| This baseline aims to evaluate the effectiveness of joint video and action training. | comparison identity and matched condition | p. 6 (B. Real-world Benchmarks) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| This highlights the better potential of UVA for tasks that require reasoning over extended temporal contexts, Effect of Joint Video-Action Modeling: We evaluate this ... | component/input/data sensitivity | p. 8 (B. Real-world Benchmarks) |
| Training Data: We use two publicly available datasets introduced by [11] and [29] without collecting any additional training data. | component/input/data sensitivity | p. 5 (B. Real-world Benchmarks) |
| + UVA-action is an ablation of UVA, where the video generation part is excluded, and the model is trained solely as a policy model. | component/input/data sensitivity | p. 6 (B. Real-world Benchmarks) |
| Its visual understanding could be enhanced by training on additional video data without action labels. | component/input/data sensitivity | p. 7 (B. Real-world Benchmarks) |
| We noticed that the dataset contains extensive recovery data from the moments of failure to correct the policy. ‘This data is particularly useful for ... | component/input/data sensitivity | p. 7 (B. Real-world Benchmarks) |
| Trained on a diverse dataset spanning multiple robot embodiments and tasks, xo demonstrates. strong zero-shot and fine-tuned performance. | component/input/data sensitivity | p. 6 (B. Real-world Benchmarks) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| ‘To address these limitations, we propose UVA, « Unified Video and Action Mode! designed to simultaneously model videos and actions - capturing the underlying ... | For example, with changes in goal color, UniPi achieves a success rate of 40%, UVA achieves 64%, while OpenVLA only reaches 32%. | PDF body cue; verify exact table/figure and matched conditions | p. 8 (B. Real-world Benchmarks), p. 8 (B. Real-world Benchmarks), p. 7 (B. Real-world Benchmarks), p. 5 (A. Simulation Benchmarks), p. 5 (B. Real-world Benchmarks), p. 7 (B. Real-world Benchmarks) |
| Primary metric/result | All tests are unseen during training, and even with more challenging distractor objects and backgrounds, UVA achieves higher success rates than DP-UML To more ... | numeric claim only at cited anchor | p. 8 (B. Real-world Benchmarks) |

- Numeric sentences retained from the body:
- **p. 5 / A. Simulation Benchmarks - extractive body cue:** We report the success rates of the bestperforming checkpoint, averaging across 50 rollouts for PushT and Toolhang, respectively
- **p. 5 / A. Simulation Benchmarks - extractive body cue:** We evaluate the best-performing, checkpoint over 50 rollouts and report its average reward, Libero10 [30] has 10 tasks.
- **p. 5 / A. Simulation Benchmarks - extractive body cue:** We evaluate each task in 50 different environments with varying random seeds and report the average rewards across all 10 tasks.
- **p. 5 / A. Simulation Benchmarks - extractive body cue:** bP-€ [10] 095 / 068 053 / 050s DP-T [10] 076 sk / 0.365 OpenvLA 25) os ost / 1535 nibs (18) 0.00 0.00 / ...
- **p. 5 / B. Real-world Benchmarks - extractive body cue:** We evaluate each method over 20 rollouts with varying initial configurations and report the average success rate MulticTask Evaluation: We train one model with all ...
- **p. 5 / B. Real-world Benchmarks - extractive body cue:** We randomly selected 500 episodes from each dataset and combined them into a dataset to train both our ‘model and Diffusion Policy (11).

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Limitation and Future Work: One limitation of our frame- ‘work is that it does not currently leverage large amounts of actionless video data, which ... | p. 10 (IX. Discussion) |
| body limitation/failure cue | However, in this case, the collected failure recovery data is less impactful for our model, as its longer memory window prioritizes learning from extended ... | p. 7 (B. Real-world Benchmarks) |
| body limitation/failure cue | We noticed that the dataset contains extensive recovery data from the moments of failure to correct the policy. ‘This data is particularly useful for ... | p. 7 (B. Real-world Benchmarks) |
| body limitation/failure cue | We believe that pretraining the model on web-scale video datasets could significantly enhance its generalization capabilites, and we leave this exploration for future work. | p. 10 (IX. Discussion) |
| body limitation/failure cue | We evaluate policy learning results with UVA compared to the baseline methods on a few different axes: 1) action prediction accuracy, 2) inference speed, ... | p. 6 (B. Real-world Benchmarks) |
| body limitation/failure cue | Robustness to History Length: Prior policy learning meth- ‘ods, such as DP-C, often experience performance degradation as the history length increases as shown in ... | p. 8 (B. Real-world Benchmarks) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| OpenVLA infers fone action ata time, so itis run 8 times to match the inference time for 8 executed actions. | p. 5 (A. Simulation Benchmarks) |
| Since the official implementation is not available, we used the code from [26]. | p. 6 (B. Real-world Benchmarks) |
| For DPC and DP-T, we follow their original implementations and also perform denoising over 100 steps. | p. 7 (B. Real-world Benchmarks) |
| This design preserves the generative strengths of diffusion models while significantly reducing inference time. | p. 4 (C. Decoupled Video and Action Diffusions) |
| We found that the UVA Attention module in the Transformer accounts for half of the inference time, making UVA slightly slower than DP-UML With ... | p. 7 (B. Real-world Benchmarks) |
| We introduce two lightweight diffusion decoders for action and video prediction (see Figure 2). | p. 4 (C. Decoupled Video and Action Diffusions) |
| All methods, except OpenVLA, infer 16 faction steps per trajectory with 8 executed steps. | p. 5 (A. Simulation Benchmarks) |
| Both UVA and DP-UMI use 16 denoising steps. | p. 6 (B. Real-world Benchmarks) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 10 / IX. Discussion - extractive body cue:** Limitation and Future Work: One limitation of our frame- ‘work is that it does not currently leverage large amounts of actionless video data, which could ...
- **p. 7 / B. Real-world Benchmarks - extractive body cue:** However, in this case, the collected failure recovery data is less impactful for our model, as its longer memory window prioritizes learning from extended temporal ...
- **p. 7 / B. Real-world Benchmarks - extractive body cue:** We noticed that the dataset contains extensive recovery data from the moments of failure to correct the policy. ‘This data is particularly useful for models ...
- **p. 10 / IX. Discussion - extractive body cue:** We believe that pretraining the model on web-scale video datasets could significantly enhance its generalization capabilites, and we leave this exploration for future work.
- **p. 6 / B. Real-world Benchmarks - extractive body cue:** We evaluate policy learning results with UVA compared to the baseline methods on a few different axes: 1) action prediction accuracy, 2) inference speed, 3) ...
- **p. 8 / B. Real-world Benchmarks - extractive body cue:** Robustness to History Length: Prior policy learning meth- ‘ods, such as DP-C, often experience performance degradation as the history length increases as shown in Figure ...

- **Evidence anchors reviewed:** datasets p. 6 (B. Real-world Benchmarks), p. 5 (B. Real-world Benchmarks), p. 6 (B. Real-world Benchmarks), p. 5 (B. Real-world Benchmarks), p. 7 (B. Real-world Benchmarks), p. 8 (B. Real-world Benchmarks), metrics p. 5 (A. Simulation Benchmarks), p. 5 (B. Real-world Benchmarks), p. 7 (B. Real-world Benchmarks), p. 7 (B. Real-world Benchmarks), p. 8 (B. Real-world Benchmarks), p. 8 (B. Real-world Benchmarks), baselines p. 7 (B. Real-world Benchmarks), p. 6 (B. Real-world Benchmarks), p. 7 (B. Real-world Benchmarks), p. 5 (A. Simulation Benchmarks), p. 5 (A. Simulation Benchmarks), p. 6 (B. Real-world Benchmarks), results p. 8 (B. Real-world Benchmarks), p. 8 (B. Real-world Benchmarks), p. 7 (B. Real-world Benchmarks), p. 5 (A. Simulation Benchmarks), p. 5 (B. Real-world Benchmarks), p. 7 (B. Real-world Benchmarks).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (13 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** We evaluate policy learning results with UVA compared to the baseline methods on a few different axes: 1) action prediction accuracy, 2) inference speed, 3) robustness to visual disturbances, 4) ... (p. 6, B. Real-world Benchmarks).
- **Metric evidence:** Our approach demonstrates. superior performance in the multi-task setting, achieving a 15% higher success rate on the Cup task and a 40% higher success rate ‘on the Mouse task compared ... (p. 7, B. Real-world Benchmarks).
- **Baseline/ablation evidence:** We evaluate policy learning results with UVA compared to the baseline methods on a few different axes: 1) action prediction accuracy, 2) inference speed, 3) robustness to visual disturbances, 4) ... (p. 6, B. Real-world Benchmarks).
- **Failure/negative evidence:** Limitation and Future Work: One limitation of our frame- ‘work is that it does not currently leverage large amounts of actionless video data, which could provide valuable additional supervision. (p. 10, IX. Discussion).
