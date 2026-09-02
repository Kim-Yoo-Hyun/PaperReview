# Evaluation - Vision-Language Foundation Models as Effective Robot Imitators

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (19 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.iclr.cc/paper_files/paper/2024/hash/71639c317fb0bf398835627b4418693e-Abstract-Conference.html; PDF retrieval source: https://proceedings.iclr.cc/paper_files/paper/2024/file/71639c317fb0bf398835627b4418693e-Paper-Conference.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (5 EXPERIMENTS), p. 8 (Figure/Table caption), p. 7 (5 EXPERIMENTS), p. 16 (Figure/Table caption), p. 14 (Figure/Table caption), p. 8 (5 EXPERIMENTS)): Among all methods, RoboFlamingo achieves the highest success rate over the latter tasks.

## Evaluation Body Digest

- **p. 6 / 5 EXPERIMENTS - extractive body cue:** 5.1 BENCHMARK AND BASELINES We choose CALVIN (Mees et al., 2022b), an open-source simulated benchmark to learn long-horizon language-conditioned tasks, as our testbed, and the ...
- **p. 6 / 5 EXPERIMENTS - extractive body cue:** The dataset contains four splits for environments A, B, C, and D.
- **p. 7 / 5 EXPERIMENTS - extractive body cue:** 5.2 IMITATION PERFORMANCE We train RoboFlamingo (with the M-3B-IFT backbone) using demonstrations only with language annotation from all 4 splits (A, B, C, and D), ...
- **p. 7 / 5 EXPERIMENTS - extractive body cue:** This demonstrates the effectiveness of RoboFlamingo as the solution for robotics manipulation, enabling VLMs to become effective robot imitators.
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** Pre-train denotes the original performance of VLM on the pre-training VL dataset, Best Avg.
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** Note that the success rate of RoboFlamingo on subsequent tasks dropped more than HULC does.
- **p. 7 / 5 EXPERIMENTS - extractive body cue:** Among all methods, RoboFlamingo achieves the highest success rate over the latter tasks.
- **p. 7 / 5 EXPERIMENTS - extractive body cue:** In addition, the success rate of the subsequent tasks can be regarded as a notion of the generalizability of the manipulation policies, since the initial ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SIMULATION`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 5 EXPERIMENTS (p. 6); A.1 THE CALVIN BENCHMARK (p. 13); B EXTENDED EXPERIMENTAL RESULTS (p. 14).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 5 EXPERIMENTS | EMPIRICAL / SIMULATION | Among all methods, RoboFlamingo achieves the highest success rate over the latter tasks. | p. 7 (5 EXPERIMENTS) |
| Figure/Table caption | EMPIRICAL / SIMULATION | Figure 3: Ablation studies on the ABCD →D setting. Note that the success rate of RoboFlamingo on subsequent tasks dropped more than HULC does. ... | p. 8 (Figure/Table caption) |
| 5 EXPERIMENTS | EMPIRICAL / SIMULATION | Our method significantly outperforms baselines in this vision generalization scenario (ABC →D), as shown in Tab. | p. 7 (5 EXPERIMENTS) |
| Figure/Table caption | EMPIRICAL / SIMULATION | Figure 8: The performance of VLMs at each epoch on ABC →D split. B.5 QUALITATIVE EXAMPLES We visualize the task frames and analyze how ... | p. 16 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / SIMULATION | Tab. 4. We can see that the enriched instructions do have the same meaning as the original one, yet they are organized with different ... | p. 14 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 6 / 5 EXPERIMENTS - extractive body cue:** 5.1 BENCHMARK AND BASELINES We choose CALVIN (Mees et al., 2022b), an open-source simulated benchmark to learn long-horizon language-conditioned tasks, as our testbed, and the ...
- **p. 6 / 5 EXPERIMENTS - extractive body cue:** The dataset contains four splits for environments A, B, C, and D.
- **p. 7 / 5 EXPERIMENTS - extractive body cue:** 5.2 IMITATION PERFORMANCE We train RoboFlamingo (with the M-3B-IFT backbone) using demonstrations only with language annotation from all 4 splits (A, B, C, and D), ...
- **p. 7 / 5 EXPERIMENTS - extractive body cue:** This demonstrates the effectiveness of RoboFlamingo as the solution for robotics manipulation, enabling VLMs to become effective robot imitators.
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** Pre-train denotes the original performance of VLM on the pre-training VL dataset, Best Avg.
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** Note that the success rate of RoboFlamingo on subsequent tasks dropped more than HULC does.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: Comparison among RoboFlamingo and existing vision-language manipulation solutions. co-fine-tuning on extensive vision-language data to fully showcase its effectiveness. Consequently, there is an urgent ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: The illustration of the proposed RoboFlamingo framework. The Flamingo backbone models single-step observations, and the temporal features are modeled by the policy head. ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1: The imitation performance on various settings, all results are reported using the best-behaved model checkpoints. Full and Lang denote if the model is ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 2: Variants of VLMs tested. Pre-train denotes the original performance of VLM on the pre-training VL dataset, Best Avg. Len. denotes the best performance ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 3: Ablation studies on the ABCD →D setting. Note that the success rate of RoboFlamingo on subsequent tasks dropped more than HULC does. This ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 3: The performance on 10% language annotated data on ABCD →D setting. All variants are trained and evaluated for the same training epochs.
- **p. 13 / Figure/Table caption - extractive body cue:** Figure 4: The visualization of the four splits (left) and a full task sequence demonstration in CALVIN (right). The ID in the blue circle represents ...
- **p. 13 / Figure/Table caption - extractive body cue:** Table 4: Examples of original and enriched instructions in the CALVIN benchmark. Task Type rotate red block right push pink block move slider left open ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | 5.1 BENCHMARK AND BASELINES We choose CALVIN (Mees et al., 2022b), an open-source simulated benchmark to learn long-horizon language-conditioned tasks, as our testbed, and ... | embodiment, simulator version and control stack | p. 6 (5 EXPERIMENTS), p. 6 (5 EXPERIMENTS) |
| Task/environment | The dataset contains four splits for environments A, B, C, and D. | reset, timeout, object/scene variation | p. 6 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 5 (3 BACKGROUND), p. 4 (3 BACKGROUND) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 4 (3 BACKGROUND), p. 2 (1 INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Among all methods, RoboFlamingo achieves the highest success rate over the latter tasks. | definition/direction/unit from same section | p. 7 (5 EXPERIMENTS) |
| In addition, the success rate of the subsequent tasks can be regarded as a notion of the generalizability of the manipulation policies, since the ... | definition/direction/unit from same section | p. 7 (5 EXPERIMENTS) |
| Note that the success rate of RoboFlamingo on subsequent tasks dropped more than HULC does. | definition/direction/unit from same section | p. 8 (5 EXPERIMENTS) |
| Table 9: Success rates by task of variants of RoboFlamingo. Each task is evaluated 100 times. Task Name M-3B M-3B-IFT G-4B G-4B-IFT L-9B M-9B | definition/direction/unit from same section | p. 17 (Figure/Table caption) |
| Len. denotes the best performance of the average success length of VLMs within 5 epochs, and Mean Avg. | definition/direction/unit from same section | p. 8 (5 EXPERIMENTS) |
| We wonder the imitation learning performance of RoboFlamingo by training it on the given demonstration data. | definition/direction/unit from same section | p. 6 (5 EXPERIMENTS) |
| In each experiment, the robot is required to successfully complete sequences of up to five language instructions consecutively. | definition/direction/unit from same section | p. 6 (5 EXPERIMENTS) |
| Figure 8: The performance of VLMs at each epoch on ABC →D split. B.5 QUALITATIVE EXAMPLES We visualize the task frames and analyze how ... | definition/direction/unit from same section | p. 16 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Our method exhibits superior performance compared to all baselines in this language generalization setting. | comparison identity and matched condition | p. 7 (5 EXPERIMENTS) |
| Our method significantly outperforms baselines in this vision generalization scenario (ABC →D), as shown in Tab. | comparison identity and matched condition | p. 7 (5 EXPERIMENTS) |
| 5.1 BENCHMARK AND BASELINES We choose CALVIN (Mees et al., 2022b), an open-source simulated benchmark to learn long-horizon language-conditioned tasks, as our testbed, and ... | comparison identity and matched condition | p. 6 (5 EXPERIMENTS) |
| This may be due to our approach directly using word tokens as input during training, which can result in larger variations for synonymous sentences ... | comparison identity and matched condition | p. 8 (5 EXPERIMENTS) |
| Tab. 4. We can see that the enriched instructions do have the same meaning as the original one, yet they are organized with different ... | comparison identity and matched condition | p. 14 (Figure/Table caption) |
| 5.4 ABLATION STUDIES In this section, we conduct ablation studies for RoboFlamingo to answer the following questions: 1) How does RoboFlamingo perform with different ... | comparison identity and matched condition | p. 8 (5 EXPERIMENTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Full and Lang denote if the model is trained using unpaired vision data (i.e., vision data without language pairs); Freeze-emb refers to freezing the ... | component/input/data sensitivity | p. 7 (5 EXPERIMENTS) |
| 5.4 ABLATION STUDIES In this section, we conduct ablation studies for RoboFlamingo to answer the following questions: 1) How does RoboFlamingo perform with different ... | component/input/data sensitivity | p. 8 (5 EXPERIMENTS) |
| Figure 3: Ablation studies on the ABCD →D setting. Note that the success rate of RoboFlamingo on subsequent tasks dropped more than HULC does. ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| Figure 1: Comparison among RoboFlamingo and existing vision-language manipulation solutions. co-fine-tuning on extensive vision-language data to fully showcase its effectiveness. Consequently, there is an ... | component/input/data sensitivity | p. 2 (Figure/Table caption) |
| Table 3: The performance on 10% language annotated data on ABCD →D setting. All variants are trained and evaluated for the same training epochs. | component/input/data sensitivity | p. 9 (Figure/Table caption) |
| Table 9: Success rates by task of variants of RoboFlamingo. Each task is evaluated 100 times. Task Name M-3B M-3B-IFT G-4B G-4B-IFT L-9B M-9B | component/input/data sensitivity | p. 17 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To this end, we introduce RoboFlamingo, a novel vision-language manipulation framework that leverages publicly accessible pre-trained VLMs to effectively construct manipulation policies for robotics. | Among all methods, RoboFlamingo achieves the highest success rate over the latter tasks. | PDF body cue; verify exact table/figure and matched conditions | p. 7 (5 EXPERIMENTS), p. 8 (Figure/Table caption), p. 7 (5 EXPERIMENTS), p. 16 (Figure/Table caption), p. 14 (Figure/Table caption), p. 8 (5 EXPERIMENTS) |
| Primary metric/result | Figure 3: Ablation studies on the ABCD →D setting. Note that the success rate of RoboFlamingo on subsequent tasks dropped more than HULC does. ... | numeric claim only at cited anchor | p. 8 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 6 / 5 EXPERIMENTS - extractive body cue:** Each consists of 6 hours of human-teleoperated recording data (more than 2 million steps) that might contain sub-optimal behavior, and only 1% of that data ...
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** Len. denotes the best performance of the average success length of VLMs within 5 epochs, and Mean Avg.
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** Len. denotes the mean performance of the average success length of VLMs of the last 3 epochs on CALVIN.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | We hypothesize that this may stem from the fact that the VLM (OpenFlamingo) has only seen image-text pairs during pre-training and cannot process consequent ... | p. 8 (2) Does vision-language (VL) pre-training improve downstream robotic tasks?) |
| body limitation/failure cue | Figure 8: The performance of VLMs at each epoch on ABC →D split. B.5 QUALITATIVE EXAMPLES We visualize the task frames and analyze how ... | p. 16 (Figure/Table caption) |
| body limitation/failure cue | Due to the lack of real-robot data, this paper does not deploy on real-world robotics. | p. 9 (2) Does vision-language (VL) pre-training improve downstream robotic tasks?) |
| body limitation/failure cue | 6 CONCLUSION AND FUTURE WORK This paper explores the potential of pre-trained vision-language models in advancing languageconditioned robotic manipulation. | p. 9 (2) Does vision-language (VL) pre-training improve downstream robotic tasks?) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Each consists of 6 hours of human-teleoperated recording data (more than 2 million steps) that might contain sub-optimal behavior, and only 1% of that ... | p. 6 (5 EXPERIMENTS) |
| We re-implement RT-1 and take the original code of HULC provided by Mees et al. | p. 7 (5 EXPERIMENTS) |
| RT-2 (Brohan et al., 2023) is not experimentally compared since we have no access to their code, data, and model weights. | p. 7 (5 EXPERIMENTS) |
| LSTM implicitly maintains a hidden state to encode memory and predict the action. | p. 8 (2) Does vision-language (VL) pre-training improve downstream robotic tasks?) |
| Len. denotes the best performance of the average success length of VLMs within 5 epochs, and Mean Avg. | p. 8 (5 EXPERIMENTS) |
| All variants are trained and evaluated for the same training epochs. | p. 9 (2) Does vision-language (VL) pre-training improve downstream robotic tasks?) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 2) Does vision-language (VL) pre-training improve downstream robotic tasks? - extractive body cue:** We hypothesize that this may stem from the fact that the VLM (OpenFlamingo) has only seen image-text pairs during pre-training and cannot process consequent frames ...
- **p. 16 / Figure/Table caption - extractive body cue:** Figure 8: The performance of VLMs at each epoch on ABC →D split. B.5 QUALITATIVE EXAMPLES We visualize the task frames and analyze how RoboFlamingo ...
- **p. 9 / 2) Does vision-language (VL) pre-training improve downstream robotic tasks? - extractive body cue:** Due to the lack of real-robot data, this paper does not deploy on real-world robotics.
- **p. 9 / 2) Does vision-language (VL) pre-training improve downstream robotic tasks? - extractive body cue:** 6 CONCLUSION AND FUTURE WORK This paper explores the potential of pre-trained vision-language models in advancing languageconditioned robotic manipulation.

- **Evidence anchors reviewed:** datasets p. 6 (5 EXPERIMENTS), p. 6 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), metrics p. 7 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 17 (Figure/Table caption), p. 8 (5 EXPERIMENTS), p. 6 (5 EXPERIMENTS), baselines p. 7 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), p. 6 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 14 (Figure/Table caption), p. 8 (5 EXPERIMENTS), results p. 7 (5 EXPERIMENTS), p. 8 (Figure/Table caption), p. 7 (5 EXPERIMENTS), p. 16 (Figure/Table caption), p. 14 (Figure/Table caption), p. 8 (5 EXPERIMENTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
