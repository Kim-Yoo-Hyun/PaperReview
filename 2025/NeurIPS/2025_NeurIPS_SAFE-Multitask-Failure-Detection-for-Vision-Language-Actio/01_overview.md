# SAFE: Multitask Failure Detection for Vision-Language-Action Models

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (36 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.neurips.cc/paper_files/paper/2025/hash/392d0d05e2f514063e6ce6f8b370834c-Abstract-Conference.html.
> PDF retrieval source: https://proceedings.neurips.cc/paper_files/paper/2025/file/392d0d05e2f514063e6ce6f8b370834c-Paper-Conference.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / NeurIPS
- Authors: not duplicated here when not verified in the registry source
- Primary track: World models, safety, uncertainty, and recovery
- Tier: NEXT
- Tags: Robotics, VLA, failure detection, conformal prediction, uncertainty
- Official paper: https://proceedings.neurips.cc/paper_files/paper/2025/hash/392d0d05e2f514063e6ce6f8b370834c-Abstract-Conference.html
- Full-text retrieval: https://proceedings.neurips.cc/paper_files/paper/2025/file/392d0d05e2f514063e6ce6f8b370834c-Paper-Conference.pdf
- Code/Project: https://vla-safe.github.io/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (36 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

World models, safety, uncertainty, and recovery의 safety 문제를 이해하기 위해 읽는다. 본문은 However, when VLAs are directly deployed on unseen tasks without collecting additional demonstrations and finetuning the model, they still suffer from limited success rates and a wide range of failure modes.를 문제로 두고, The contributions of our paper can be summarized as follows: • We analyze the VLA feature space and show that, across different task instructions and environments, the internal features of the VLA ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** While vision-language-action models (VLAs) have shown promising robotic behaviors across a diverse set of manipulation tasks, they achieve limited success rates when deployed on novel ...
- **p. 1 / Abstract - extractive body cue:** To allow these policies to safely interact with their environments, we need a failure detector that gives a timely alert such that the robot can ...
- **p. 1 / Abstract - extractive body cue:** However, existing failure detectors are trained and tested only on one or a few specific tasks, while generalist VLAs require the detector to generalize and ...
- **p. 1 / Abstract - extractive body cue:** In this paper, we introduce the multitask failure detection problem and propose SAFE, a failure detector for generalist robot policies such as VLAs.
- **p. 1 / Abstract - extractive body cue:** We analyze the VLA feature space and find that VLAs have sufficient highlevel knowledge about task success and failure, which is generic across different tasks.
- **p. 1 / 1 Introduction - extractive body cue:** However, when VLAs are directly deployed on unseen tasks without collecting additional demonstrations and finetuning the model, they still suffer from limited success rates and ...
- **p. 1 / 1 Introduction - extractive body cue:** Most existing failure detection methods train a separate failure detector for each task, and evaluate the detector only on that task [8-17].

## Core Idea

- **p. 2 / 1 Introduction - extractive body cue:** The contributions of our paper can be summarized as follows: • We analyze the VLA feature space and show that, across different task instructions and ...
- **p. 2 / 1 Introduction - extractive body cue:** Based on this insight, we introduce SAFE, a ScAlable Failure Estimation method that scales across diverse tasks for generalist policies like VLAs.
- **p. 1 / 1 Introduction - extractive body cue:** VLAs are designed to accomplish diverse tasks and may frequently encounter novel task instructions and unseen environments during deployment.
- **p. 1 / 1 Introduction - extractive body cue:** Recently, scaling up robot manipulation datasets has enabled the development of large visionlanguage-action (VLA) models, which are generalist manipulation policies that can follow language instructions ...
- **p. 5 / 4 Method - extractive body cue:** Encoder 𝒐𝑡 𝑙𝑡 Decoder 𝒆𝑡 Action: 𝑨𝑡 Observation Instruction VLA Model 𝒆1 SAFE-MLP SAFE-LSTM MLP ǁ𝑠1 𝒆2 MLP ǁ𝑠2 𝒆3 MLP ǁ𝑠3 𝒆𝑇 MLP ǁ𝑠𝑇 ...
- **p. 4 / 4 Method - extractive body cue:** 4.1 Visual Analysis on VLA Latent Space VLAs process multi-modal inputs and extract rich semantic information in their internal feature space.
- **p. 4 / 4 Method - extractive body cue:** We study this hypothesis by visualizing the VLA features in Fig.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Encoder 𝒐𝑡 𝑙𝑡 Decoder 𝒆𝑡 Action: 𝑨𝑡 Observation Instruction VLA Model 𝒆1 SAFE-MLP SAFE-LSTM MLP ǁ𝑠1 𝒆2 MLP ǁ𝑠2 𝒆3 MLP ǁ𝑠3 𝒆𝑇 MLP ǁ𝑠𝑇 𝒆1 LSTM 𝑠1 𝒆2 LSTM 𝑠2 𝒆3 ... | observation, uncertainty/risk estimate와 task command | p. 5 (4 Method), p. 1 (1 Introduction) |
| State/latent | Encoder, Decoder, Action, Observation, Instruction, VLA, Model, SAFE-MLP, SAFE-LSTM, MLP, LSTM, Recently | safe set, recovery state 또는 constraint margin | p. 5 (4 Method), p. 1 (1 Introduction), p. 2 (1 Introduction) |
| Output/action | Recently, scaling up robot manipulation datasets has enabled the development of large visionlanguage-action (VLA) models, which are generalist manipulation policies that can follow language instructions and accomplish a wide range of ta ... | shielded, recovery 또는 safe action | p. 1 (1 Introduction), p. 2 (1 Introduction), p. 4 (4 Method) |
| Objective/outcome | 1(c) further illustrates how VLA's features evolve in the feature space when VLA progresses temporally. | task return과 violation/failure probability | p. 4 (4 Method), p. 4 (4 Method) |

## Main Claims and Actual Contribution

- **p. 2 / 1 Introduction - extractive body cue:** The contributions of our paper can be summarized as follows: • We analyze the VLA feature space and show that, across different task instructions and ...
- **p. 2 / 1 Introduction - extractive body cue:** Based on this insight, we introduce SAFE, a ScAlable Failure Estimation method that scales across diverse tasks for generalist policies like VLAs.
- **p. 1 / 1 Introduction - extractive body cue:** VLAs are designed to accomplish diverse tasks and may frequently encounter novel task instructions and unseen environments during deployment.
- **p. 1 / 1 Introduction - extractive body cue:** Recently, scaling up robot manipulation datasets has enabled the development of large visionlanguage-action (VLA) models, which are generalist manipulation policies that can follow language instructions ...
- **p. 10 / 6 Results - extractive body cue:** 75.54 53.93 82.37 70.00 Euclid. k-NN 80.35 60.27 72.01 53.64 Cosine k-NN 80.23 59.51 74.76 65.88 PCA-KMeans 49.98 51.03 75.62 47.22 RND 62.00 45.83 66.68 ...
- **p. 10 / Figure/Table caption - extractive body cue:** Figure 6: SAFE-MLP achieves the best failure detection performance in real-world experiments with both π0-FAST Franka and OpenVLA WidowX. Plot (a) presents quantitative results, while ...
- **p. 9 / 6 Results - extractive body cue:** With a higher ROC-AUC metric, a failure detector achieves higher accuracy averaged over all possible thresholds.
- **p. 9 / 6 Results - extractive body cue:** Averaged across simulation benchmarks, SAFE-MLP and SAFE-LSTM have similar performance, both outperforming the best baseline by 4-5% on unseen tasks, while still achieving the best ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 10 (6 Results), p. 10 (Figure/Table caption) |
| Embodiment/environment | Real-world WidowX Experiments: We also deploy the OpenVLA model pretrained on the "Open-X Magic Soup++" dataset [2] on a WidowX robot manipulator in our lab. | hardware/simulator version and reset protocol | p. 6 (5 Experiments), p. 6 (5 Experiments) |
| Dataset/benchmark | Averaged across simulation benchmarks, SAFE-MLP and SAFE-LSTM have similar performance, both outperforming the best baseline by 4-5% on unseen tasks, while still achieving the best performance on seen tasks. | role, split, size and leakage | p. 6 (5 Experiments), p. 6 (5 Experiments), p. 9 (6 Results), p. 10 (6 Results) |
| Metric | We exclude the "pick up coke" task because π∗ 0 rarely fails on it (success rate at 98%). | definition, denominator, direction and uncertainty | p. 6 (5 Experiments), p. 10 (6 Results), p. 10 (6 Results) |
| Baseline/ablation | Averaged across simulation benchmarks, SAFE-MLP and SAFE-LSTM have similar performance, both outperforming the best baseline by 4-5% on unseen tasks, while still achieving the best performance on seen tasks. | fair input/data/compute/action matching | p. 9 (6 Results), p. 27 (Figure/Table caption), p. 9 (6 Results) |

## Explicit Limitations and Failure Boundary

- **p. 4 / Figure/Table caption - extractive body cue:** Figure 1: The internal features of a VLA capture high-level information about task success and failure. When the VLA is failing, the features, even those ...
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 5: Failures detected by SAFE-LSTM align well with the actual robot failures, as shown in the corresponding camera observations from simulation experiments. The blue-shaded ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1: Failure detection results on simulation benchmarks, measured by area under ROC (ROC- AUC). "-" indicates that the failure detection method does not apply. ...
- **p. 5 / 3. Calibrate failure detection - extractive body cue:** Inspired by this observation, we design SAFE, which uses the internal features of VLAs for failure detection.
- **p. 5 / 3. Calibrate failure detection - extractive body cue:** If the predicted score exceeds the threshold during testing, SAFE confidently detects a failure. timely manner.
- **p. 6 / 3. Calibrate failure detection - extractive body cue:** We use uppert as the failure flag threshold δt, and more details about functional CP can be found in Appendix.
- **p. 10 / 7 Conclusion - extractive body cue:** Experiments show that SAFE achieves SOTA results in failure detection, and aligns with human intuition.

## Why Read It

World models, safety, uncertainty, and recovery의 safety 문제를 이해하기 위해 읽는다. 본문은 However, when VLAs are directly deployed on unseen tasks without collecting additional demonstrations and finetuning the model, they still suffer from limited success rates and a wide range of failure modes.를 문제로 두고, The contributions of our paper can be summarized as follows: • We analyze the VLA feature space and show that, across different task instructions and environments, the internal features of the VLA ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 5 (4 Method), p. 4 (4 Method) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (36 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** However, when VLAs are directly deployed on unseen tasks without collecting additional demonstrations and finetuning the model, they still suffer from limited success rates and a wide range of failure ... (p. 1, 1 Introduction).
- **Actual contribution:** VLAs are designed to accomplish diverse tasks and may frequently encounter novel task instructions and unseen environments during deployment. (p. 1, 1 Introduction).
- **Evaluation boundary:** Figure 6: SAFE-MLP achieves the best failure detection performance in real-world experiments with both π0-FAST Franka and OpenVLA WidowX. Plot (a) presents quantitative results, while (b-e) show qualitative examples from ... (p. 10, Figure/Table caption).
- **Explicit failure boundary:** This means that the human annotator does not think these rollouts are failures until the very last moment, where the VLA model is probably on the right track and fails ... (p. 28, C.3 Failure Detection Time).
