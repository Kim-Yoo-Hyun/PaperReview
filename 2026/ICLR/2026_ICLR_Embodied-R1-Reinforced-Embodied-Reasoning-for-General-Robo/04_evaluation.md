# Evaluation - Embodied-R1: Reinforced Embodied Reasoning for General Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (26 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=i5wlozMFsQ; PDF retrieval source: https://openreview.net/pdf/f96c92cfad0bb9a981c9646c6a5bbcfc1992f8fc.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 24 (Figure/Table caption), p. 8 (4 EXPERIMENTS), p. 3 (Figure/Table caption)): 5, Embodied-R1 achieves an 87.5% zero-shot success rate, an improvement of over 60% compared to the RoboPoint and FSD baselines.

## Evaluation Body Digest

- **p. 6 / 4 EXPERIMENTS - extractive PDF cue:** Our evaluation encompassed 11 QA benchmarks, 4 simulated tasks (SIMPLEREnv) (Li et al., 2024b), and 8 real-world robot (xArm platform) tasks.
- **p. 9 / 4 EXPERIMENTS - extractive PDF cue:** We conducted zero-shot real-world evaluations on an xArm 6 robot across eight tabletop manipulation tasks.
- **p. 9 / 4 EXPERIMENTS - extractive PDF cue:** The setup used a third-person Intel RealSense L515 camera (640×480), with all objects, scenes, and tasks being OOD to test generalization.
- **p. 10 / 4 EXPERIMENTS - extractive PDF cue:** Despite being trained exclusively on real-world data, Embodied-R1 demonstrates remarkable zero-shot generalization on VTG tasks across entirely unseen scenarios (Fig.
- **p. 8 / 4 EXPERIMENTS - extractive PDF cue:** Where2Place & VABench-P -- Region Referring Grounding (RRG) Put the banana in the pot cardboard fence. you need to grasp the mug you need to ...
- **p. 6 / 4 EXPERIMENTS - extractive PDF cue:** To validate Embodied-R1's generalization in robotic manipulation, we conducted extensive experiments evaluating its Seeing (spatial reasoning and pointing capabilities) and Doing (manipulation tasks) dimensions.
- **p. 8 / 4 EXPERIMENTS - extractive PDF cue:** 4, a single Embodied-R1 model masters this diverse skill set, demonstrating high accuracy even with small objects and complex spatial relationships in cluttered scenes.
- **p. 7 / 4 EXPERIMENTS - extractive PDF cue:** Published as a conference paper at ICLR 2026 Table 1: Performance comparison on spatial reasoning benchmarks.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 4 EXPERIMENTS (p. 6); B IMPLEMENTATION DETAILS OF EMBODIED-R1 (p. 18).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | 5, Embodied-R1 achieves an 87.5% zero-shot success rate, an improvement of over 60% compared to the RoboPoint and FSD baselines. | p. 9 (4 EXPERIMENTS) |
| 4 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | We attribute this significant improvement to the baselines' poor performance on tasks requiring spatial reasoning (e.g., moving the nearest object) and their low success ... | p. 9 (4 EXPERIMENTS) |
| 4 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | It achieves an average rank of 2.1, significantly outperforming its variants trained without common-sense data (Embodied-R1 w/o CS, Rank 3.4) or with only SFT ... | p. 7 (4 EXPERIMENTS) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 12: Case Analysis: Embodied-R1 possesses embodied reasoning capabilities. It can progressively locate relevant objects and infer spatial relationships according to task instructions, and ... | p. 24 (Figure/Table caption) |
| 4 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | (O4) Embodied-R1 significantly outperforms models trained solely with SFT. | p. 8 (4 EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 6 / 4 EXPERIMENTS - extractive PDF cue:** Our evaluation encompassed 11 QA benchmarks, 4 simulated tasks (SIMPLEREnv) (Li et al., 2024b), and 8 real-world robot (xArm platform) tasks.
- **p. 9 / 4 EXPERIMENTS - extractive PDF cue:** We conducted zero-shot real-world evaluations on an xArm 6 robot across eight tabletop manipulation tasks.
- **p. 9 / 4 EXPERIMENTS - extractive PDF cue:** The setup used a third-person Intel RealSense L515 camera (640×480), with all objects, scenes, and tasks being OOD to test generalization.
- **p. 10 / 4 EXPERIMENTS - extractive PDF cue:** Despite being trained exclusively on real-world data, Embodied-R1 demonstrates remarkable zero-shot generalization on VTG tasks across entirely unseen scenarios (Fig.
- **p. 8 / 4 EXPERIMENTS - extractive PDF cue:** Where2Place & VABench-P -- Region Referring Grounding (RRG) Put the banana in the pot cardboard fence. you need to grasp the mug you need to ...
- **p. 6 / 4 EXPERIMENTS - extractive PDF cue:** To validate Embodied-R1's generalization in robotic manipulation, we conducted extensive experiments evaluating its Seeing (spatial reasoning and pointing capabilities) and Doing (manipulation tasks) dimensions.
- **p. 8 / 4 EXPERIMENTS - extractive PDF cue:** 4, a single Embodied-R1 model masters this diverse skill set, demonstrating high accuracy even with small objects and complex spatial relationships in cluttered scenes.
- **p. 7 / 4 EXPERIMENTS - extractive PDF cue:** Published as a conference paper at ICLR 2026 Table 1: Performance comparison on spatial reasoning benchmarks.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 1: Overview of the Embodied-R1 framework and its zero-shot manipulation performance. Embodied-R1 performs explicit reasoning to generate "pointing" commands, enabling robust execution across a ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2: Overview of four embodied pointing abilities. a VLM trained with RFT to resolve the multi-solution dilemma for embodied pointing, delivering powerful reasoning. 4 ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 3: Overview of training data: In stage 1, we focus on improving the model's spatial reasoning capability, while incorporating a small amount of general ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 1: Performance comparison on spatial reasoning benchmarks. Bold indicates the highest value among open-source models, and underlined values show the second-highest scores. CVBench CRPE ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 2: Performance on 4 Pointing benchmarks. The score is the accuracy of points falling within the target region.
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 3: Performance on VABench-V. Lower values are better for RMSE/MAE, higher is better for LLM Score.
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 4: Visualizing Embodied-R1's Performance on Various Pointing Tasks.The model can follow diverse text instructions and generalize its capabilities to novel, unseen environments. (O1) Powerful ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 4: SimplerEnv Evaluation on WidowX Robot. Each task is tested 24 episodes. Most of the results for end-to-end VLAs are sourced from Chen et ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Our evaluation encompassed 11 QA benchmarks, 4 simulated tasks (SIMPLEREnv) (Li et al., 2024b), and 8 real-world robot (xArm platform) tasks. | embodiment, simulator version and control stack | p. 6 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS) |
| Task/environment | We conducted zero-shot real-world evaluations on an xArm 6 robot across eight tabletop manipulation tasks. | reset, timeout, object/scene variation | p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 18 (B IMPLEMENTATION DETAILS OF EMBODIED-R1), p. 18 (B IMPLEMENTATION DETAILS OF EMBODIED-R1) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We attribute this significant improvement to the baselines' poor performance on tasks requiring spatial reasoning (e.g., moving the nearest object) and their low success ... | definition/direction/unit from same section | p. 9 (4 EXPERIMENTS) |
| 4, Embodied-R1 achieves a state-of-the-art average success rate of 56.2%. | definition/direction/unit from same section | p. 9 (4 EXPERIMENTS) |
| Figure 12: Case Analysis: Embodied-R1 possesses embodied reasoning capabilities. It can progressively locate relevant objects and infer spatial relationships according to task instructions, and ... | definition/direction/unit from same section | p. 24 (Figure/Table caption) |
| The score is the accuracy of points falling within the target region. | definition/direction/unit from same section | p. 7 (4 EXPERIMENTS) |
| Figure 10: Visualizing Embodied-R1's Prediction on VTG Tasks across Various Scenarios (since the format reward is not satisfied, subsequent analysis will not be performed). ... | definition/direction/unit from same section | p. 22 (Figure/Table caption) |
| Table 10: Comparasion of w/ and w/o Point Num Reward. Bolds are better. VABench-VisualTrace RMSE↓ MAE↓ GPT Score↑ w/ Point Num Constraint 77.83 44.97 | definition/direction/unit from same section | p. 22 (Figure/Table caption) |
| Figure 8: The process of Embodied-R1 performing real-world tasks. F ADDITIONAL EXPERIMENTS The Phenomenon of Reward Hacking in VTG Tasks We carefully designed the ... | definition/direction/unit from same section | p. 21 (Figure/Table caption) |
| Bold indicates the highest value among open-source models, and underlined values show the second-highest scores. | definition/direction/unit from same section | p. 7 (4 EXPERIMENTS) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Figure 2: Overview of four embodied pointing abilities. a VLM trained with RFT to resolve the multi-solution dilemma for embodied pointing, delivering powerful reasoning. ... | comparison identity and matched condition | p. 3 (Figure/Table caption) |
| 2 and 3, across all benchmarks for REG, RRG, OFG, and VTG, Embodied-R1 consistently outperforms both general and specialized baselines, including other pointing-focused models ... | comparison identity and matched condition | p. 8 (4 EXPERIMENTS) |
| We compared performance against a comprehensive suite of baselines across three categories: (1) End-to-end VLAs, including standard models (Octo, OpenVLA, π0) and stronger variants ... | comparison identity and matched condition | p. 8 (4 EXPERIMENTS) |
| 5, Embodied-R1 achieves an 87.5% zero-shot success rate, an improvement of over 60% compared to the RoboPoint and FSD baselines. | comparison identity and matched condition | p. 9 (4 EXPERIMENTS) |
| Notably, while recent end-to-end methods such as π0-fast (48.3%) and OpenVLA-OFT (41.8%) show improved robustness compared to the base OpenVLA (5.2%), Embodied-R1 still outperforms ... | comparison identity and matched condition | p. 9 (4 EXPERIMENTS) |
| Table 12: Performance on the full LIBERO benchmark suite. Integration with Embodied-R1 yields significant improvements across all task categories compared to the DP baseline. ... | comparison identity and matched condition | p. 24 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We also included two key ablations: Embodied-R1 w/o CS, which excludes the ViRL common-sense dataset, and Embodied-SFT, a variant trained only with SFT. | component/input/data sensitivity | p. 7 (4 EXPERIMENTS) |
| It achieves an average rank of 2.1, significantly outperforming its variants trained without common-sense data (Embodied-R1 w/o CS, Rank 3.4) or with only SFT ... | component/input/data sensitivity | p. 7 (4 EXPERIMENTS) |
| These results suggest that explicit visual reasoning provides superior zero-shot generalization compared to end-to-end policy learning, particularly when facing unseen instructions and background variations ... | component/input/data sensitivity | p. 9 (4 EXPERIMENTS) |
| We compared performance against a comprehensive suite of baselines across three categories: (1) End-to-end VLAs, including standard models (Octo, OpenVLA, π0) and stronger variants ... | component/input/data sensitivity | p. 8 (4 EXPERIMENTS) |
| We trained four variants on RRG benchmarks. | component/input/data sensitivity | p. 10 (4 EXPERIMENTS) |
| 4.4 FURTHER ANALYSIS AND ABLATIONS Embodied-R1 Exhibits Strong Generalization. | component/input/data sensitivity | p. 10 (4 EXPERIMENTS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To bridge this gap, we propose pointing as an intuitive and effective paradigm to connect high-level understanding with generalizable action. | 5, Embodied-R1 achieves an 87.5% zero-shot success rate, an improvement of over 60% compared to the RoboPoint and FSD baselines. | PDF body cue; verify exact table/figure and matched conditions | p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 24 (Figure/Table caption), p. 8 (4 EXPERIMENTS), p. 3 (Figure/Table caption) |
| Primary metric/result | We attribute this significant improvement to the baselines' poor performance on tasks requiring spatial reasoning (e.g., moving the nearest object) and their low success ... | numeric claim only at cited anchor | p. 9 (4 EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 9 / 4 EXPERIMENTS - extractive PDF cue:** We conducted zero-shot real-world evaluations on an xArm 6 robot across eight tabletop manipulation tasks.
- **p. 9 / 4 EXPERIMENTS - extractive PDF cue:** The setup used a third-person Intel RealSense L515 camera (640×480), with all objects, scenes, and tasks being OOD to test generalization.
- **p. 18 / B IMPLEMENTATION DETAILS OF EMBODIED-R1 - extractive PDF cue:** The first phase was trained for 2 epochs, and the second phase for 1 epoch, with each phase taking approximately 48 hours.
- **p. 18 / B IMPLEMENTATION DETAILS OF EMBODIED-R1 - extractive PDF cue:** As for Embodied-SFT, we used exactly the same data but trained with a supervised learning loss, kept the batch size at 128, and trained for ...
- **p. 18 / B IMPLEMENTATION DETAILS OF EMBODIED-R1 - extractive PDF cue:** Second, for the VTG task, we introduced an additional constraint on the format: the generated visual trace must consist of exactly 8 points.
- **p. 18 / B IMPLEMENTATION DETAILS OF EMBODIED-R1 - extractive PDF cue:** The first phase was trained for 2 epochs, and the second phase for 1 epoch, with each phase taking approximately 48 hours.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | We would like to add two clarifying points: First, if the task output fails to meet the required parsing format, subsequent analysis cannot proceed ... | p. 18 (B IMPLEMENTATION DETAILS OF EMBODIED-R1) |
| body limitation/failure cue | A detailed discussion of limitations is provided in App. | p. 10 (5 CONCLUSION) |
| body limitation/failure cue | D, we conducted an in-depth analysis of failure cases and execution time. | p. 9 (4 EXPERIMENTS) |
| body limitation/failure cue | The score is the accuracy of points falling within the target region. | p. 7 (4 EXPERIMENTS) |
| body limitation/failure cue | Empirically, Embodied-R1 achieves state-of-the-art results across multiple benchmark tests and demonstrates robust zero-shot generalization in robotic manipulation tasks, offering a promising pathway toward more ... | p. 10 (5 CONCLUSION) |
| body limitation/failure cue | Middle: Demonstration of the robustness under significant visual disturbances, such as background and lighting changes. | p. 9 (4 EXPERIMENTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| As for Embodied-SFT, we used exactly the same data but trained with a supervised learning loss, kept the batch size at 128, and trained ... | p. 18 (B IMPLEMENTATION DETAILS OF EMBODIED-R1) |
| For all experiments, we focus on comparing SFT models trained with the same batch size and data, which we refer to as Embodied-SFT. | p. 7 (4 EXPERIMENTS) |
| The optimizer selected is AdamW, with a learning rate of 1e-6 and a weight decay coefficient of 1e-2. | p. 18 (B IMPLEMENTATION DETAILS OF EMBODIED-R1) |
| (2025a), while the results for the remaining models are reproduced in accordance with the official code. | p. 8 (4 EXPERIMENTS) |
| [x]: The instruction for each trial is a randomly selected color. | p. 9 (4 EXPERIMENTS) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 18 / B IMPLEMENTATION DETAILS OF EMBODIED-R1 - extractive PDF cue:** We would like to add two clarifying points: First, if the task output fails to meet the required parsing format, subsequent analysis cannot proceed successfully, ...
- **p. 10 / 5 CONCLUSION - extractive PDF cue:** A detailed discussion of limitations is provided in App.
- **p. 9 / 4 EXPERIMENTS - extractive PDF cue:** D, we conducted an in-depth analysis of failure cases and execution time.
- **p. 7 / 4 EXPERIMENTS - extractive PDF cue:** The score is the accuracy of points falling within the target region.
- **p. 10 / 5 CONCLUSION - extractive PDF cue:** Empirically, Embodied-R1 achieves state-of-the-art results across multiple benchmark tests and demonstrates robust zero-shot generalization in robotic manipulation tasks, offering a promising pathway toward more capable ...
- **p. 9 / 4 EXPERIMENTS - extractive PDF cue:** Middle: Demonstration of the robustness under significant visual disturbances, such as background and lighting changes.

- **PDF anchors reviewed:** datasets p. 6 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS), metrics p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 24 (Figure/Table caption), p. 7 (4 EXPERIMENTS), p. 22 (Figure/Table caption), p. 22 (Figure/Table caption), baselines p. 3 (Figure/Table caption), p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 24 (Figure/Table caption), results p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 24 (Figure/Table caption), p. 8 (4 EXPERIMENTS), p. 3 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
