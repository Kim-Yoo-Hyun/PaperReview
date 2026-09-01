# Evaluation - XR-1: Towards Versatile Vision-Language-Action Models via Learning Unified Vision-Motion Representations

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (45 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=JO0IsGJg16; PDF retrieval source: https://openreview.net/pdf/181715f87df4dd5677ebf2619dcb456e071c95dd.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (4.4. Generalization Analysis), p. 8 (4.4. Generalization Analysis), p. 7 (4.1. Experiment Setup), p. 6 (4.1. Experiment Setup), p. 9 (4.4. Generalization Analysis), p. 6 (Figure/Table caption)): As shown in Figure 7, XR-1 achieves significantly higher success rates than ACT and DP, despite the setting favoring 8

## Evaluation Body Digest

- **p. 7 / 4.2. Results on Real-World Robotic Tasks - extractive PDF cue:** Unlike the UR-5e, this robot is unseen during pretraining (e.g., Stages 1 and 2 for XR1), making the evaluation a stringent embodiment-transfer benchmark.
- **p. 6 / 4. Experiments - extractive PDF cue:** We evaluate XR-1 across six robotic embodiments and over 120 tasks, including bimanual collaboration, dexterous manipulation, and long-horizon tasks, to address four key questions: (i) ...
- **p. 8 / 4.3. Ablation Study - extractive PDF cue:** This trend unequivocally demonstrates the foundational importance of leveraging large and diverse datasets to learn generalizable robotic policies.
- **p. 8 / 4.4. Generalization Analysis - extractive PDF cue:** These results highlight XR-1's strong generalization not only across embodiments and tasks but also under diverse environmental shifts never encountered during pretraining or fine-tuning, underscoring ...
- **p. 9 / 4.5. Additional Analyses - extractive PDF cue:** The full benchmark specification, including task images, language instructions, and collected demonstration counts for all 120 tasks, is provided in Appendix K.1.
- **p. 5 / 3.5. Data Collection and Implementation Details - extractive PDF cue:** Dataset Episodes Frames Weight OXE 978k 59.3M 40% RoboMIND 69k 21.4M 15% XR-D 158k 69.1M 35% Ego4D 59k 14.3M 10% Implementation Details.
- **p. 5 / 3.5. Data Collection and Implementation Details - extractive PDF cue:** Since the number of episodes and frames varies significantly among different sources, we assign dataset-specific sampling weights during training to balance contributions and prevent overfitting ...
- **p. 6 / 4.1. Experiment Setup - extractive PDF cue:** We employ a threestage pipeline: (i) UVMC Pre-training: learning representations from large-scale heterogeneous datasets, including RoboMIND (Wu et al., 2025a), Open-X (O'Neill et al., 2024), ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 3.5. Data Collection and Implementation Details (p. 5); 4. Experiments (p. 6); 4.1. Experiment Setup (p. 6); 4.2. Results on Real-World Robotic Tasks (p. 7).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.4. Generalization Analysis | EMPIRICAL / REAL-ROBOT OR HARDWARE | As shown in Figure 7, XR-1 achieves significantly higher success rates than ACT and DP, despite the setting favoring 8 | p. 8 (4.4. Generalization Analysis) |
| 4.4. Generalization Analysis | EMPIRICAL / REAL-ROBOT OR HARDWARE | As shown in Figure 6, the pre-trained XR-1-oob model, despite no adaptation, achieves performance comparable to GR00T-N1.5 and π0, while outperforming RDT and UniVLA. | p. 8 (4.4. Generalization Analysis) |
| 4.1. Experiment Setup | EMPIRICAL / REAL-ROBOT OR HARDWARE | Success rate results across 20 tasks on Tien Kung 2.0. | p. 7 (4.1. Experiment Setup) |
| 4.1. Experiment Setup | EMPIRICAL / REAL-ROBOT OR HARDWARE | For evaluation, we conduct 20 rollouts per task and report success rates based on human evaluation. | p. 6 (4.1. Experiment Setup) |
| 4.4. Generalization Analysis | EMPIRICAL / REAL-ROBOT OR HARDWARE | XR-1: Towards Versatile Vision-Language-Action Models via Learning Unified Vision-Motion Representations DFR-StackPlates DFR-StackBowls DFR-CleanTable DFR-MoveCupMilk DFR-HangTowelRack DFR-StackCubes DFR-SweepTrash 0% 10% 20% 30% 40% 50 ... | p. 9 (4.4. Generalization Analysis) |

## Dataset / Benchmark Role

- **p. 7 / 4.2. Results on Real-World Robotic Tasks - extractive PDF cue:** Unlike the UR-5e, this robot is unseen during pretraining (e.g., Stages 1 and 2 for XR1), making the evaluation a stringent embodiment-transfer benchmark.
- **p. 6 / 4. Experiments - extractive PDF cue:** We evaluate XR-1 across six robotic embodiments and over 120 tasks, including bimanual collaboration, dexterous manipulation, and long-horizon tasks, to address four key questions: (i) ...
- **p. 8 / 4.3. Ablation Study - extractive PDF cue:** This trend unequivocally demonstrates the foundational importance of leveraging large and diverse datasets to learn generalizable robotic policies.
- **p. 8 / 4.4. Generalization Analysis - extractive PDF cue:** These results highlight XR-1's strong generalization not only across embodiments and tasks but also under diverse environmental shifts never encountered during pretraining or fine-tuning, underscoring ...
- **p. 9 / 4.5. Additional Analyses - extractive PDF cue:** The full benchmark specification, including task images, language instructions, and collected demonstration counts for all 120 tasks, is provided in Appendix K.1.
- **p. 5 / 3.5. Data Collection and Implementation Details - extractive PDF cue:** Dataset Episodes Frames Weight OXE 978k 59.3M 40% RoboMIND 69k 21.4M 15% XR-D 158k 69.1M 35% Ego4D 59k 14.3M 10% Implementation Details.
- **p. 5 / 3.5. Data Collection and Implementation Details - extractive PDF cue:** Since the number of episodes and frames varies significantly among different sources, we assign dataset-specific sampling weights during training to balance contributions and prevent overfitting ...
- **p. 6 / 4.1. Experiment Setup - extractive PDF cue:** We employ a threestage pipeline: (i) UVMC Pre-training: learning representations from large-scale heterogeneous datasets, including RoboMIND (Wu et al., 2025a), Open-X (O'Neill et al., 2024), ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. We introduce X Robotic Model 1 (XR-1), a versatile and scalable vision-language-action framework. XR-1 supports robust multi-task learning across diverse robot embodiments and ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2. Overview of X Robotic Model 1 (XR-1). In XR-1, we introduce the Unified Vision-Motion Codes (UVMC), a discrete latent representation that jointly encodes ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 3. Experimental Setup. We evaluate XR-1 across six robot embodiments (Tien Kung 1.0/2.0, Single-/Dual-Arm UR-5e, Dual-Arm Franka, and AgileX Cobot Magic 2.0), covering more ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 4. Success rate results across 20 tasks on Dual-Arm UR-5e.
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 2. Success rate results across 20 tasks on Tien Kung 2.0.
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 3. Ablation study of XR-1. In Stage-1 and Stage-2, "DT" indicates training directly on the downstream task data. Exp. Instantiation Stage-1 Stage-2 Stage-3 DUR-Clean ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 4. Generalization results of XR-1 on unseen scenarios. DFR-SweepTrash DFR-HangCup
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 5. Unseen scenario task setup on Dual-Arm Franka. embodiment performance, are provided in Appendix E. Lightweight Models. To validate the applicability of our methods ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Unlike the UR-5e, this robot is unseen during pretraining (e.g., Stages 1 and 2 for XR1), making the evaluation a stringent embodiment-transfer benchmark. | embodiment, simulator version and control stack | p. 7 (4.2. Results on Real-World Robotic Tasks), p. 6 (4. Experiments) |
| Task/environment | We evaluate XR-1 across six robotic embodiments and over 120 tasks, including bimanual collaboration, dexterous manipulation, and long-horizon tasks, to address four key questions: ... | reset, timeout, object/scene variation | p. 6 (4. Experiments), p. 8 (4.3. Ablation Study) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 4 (3.1. Overview), p. 4 (3.1. Overview) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 5 (3.1. Overview), p. 5 (3.1. Overview) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| For evaluation, we conduct 20 rollouts per task and report success rates based on human evaluation. | definition/direction/unit from same section | p. 6 (4.1. Experiment Setup) |
| Success rate results across 20 tasks on Tien Kung 2.0. | definition/direction/unit from same section | p. 7 (4.1. Experiment Setup) |
| 2) elevates the average success rate to 57.5%. | definition/direction/unit from same section | p. 8 (4.3. Ablation Study) |
| As shown in Figure 7, XR-1 achieves significantly higher success rates than ACT and DP, despite the setting favoring 8 | definition/direction/unit from same section | p. 8 (4.4. Generalization Analysis) |
| XR-1: Towards Versatile Vision-Language-Action Models via Learning Unified Vision-Motion Representations DFR-StackPlates DFR-StackBowls DFR-CleanTable DFR-MoveCupMilk DFR-HangTowelRack DFR-StackCubes DFR-SweepTrash 0% 10% 20% 30% 40% 50 ... | definition/direction/unit from same section | p. 9 (4.4. Generalization Analysis) |
| Figure 4. Success rate results across 20 tasks on Dual-Arm UR-5e. | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| Table 12. Success rate results across 20 tasks on Single-Arm UR-5e. | definition/direction/unit from same section | p. 22 (Figure/Table caption) |
| Failure analyses for baselines and XR-1 are provided in Appendix I and Appendix J, respectively, showing that XR-1 reduces baseline failures such as optimization ... | definition/direction/unit from same section | p. 9 (4.5. Additional Analyses) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Figure 9. Out-of-box evaluation results of 7 tasks on Dual-Arm UR-5e. Out-of-Box Evaluation. In addition to the evaluation on the Dual-Arm Franka, we also ... | comparison identity and matched condition | p. 24 (Figure/Table caption) |
| XR-1 outperforms all baselines by a wide margin (e.g., DUR-FindTapeBasket: 85% vs. | comparison identity and matched condition | p. 7 (4.2. Results on Real-World Robotic Tasks) |
| Despite this challenge, XR-1 again outperforms all baselines; e.g., in TK2-MoveCupSauce, it reaches 70% versus 60% for π0. | comparison identity and matched condition | p. 7 (4.2. Results on Real-World Robotic Tasks) |
| By benchmarking against multiple strong baselines, we demonstrate the robustness and scalability of our approach in diverse, challenging scenarios. | comparison identity and matched condition | p. 6 (4. Experiments) |
| We evaluate XR-1 across six robotic embodiments and over 120 tasks, including bimanual collaboration, dexterous manipulation, and long-horizon tasks, to address four key questions: ... | comparison identity and matched condition | p. 6 (4. Experiments) |
| 1), it achieves a respectable baseline performance of 42.5%. | comparison identity and matched condition | p. 8 (4.3. Ablation Study) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 5. Unseen scenario task setup on Dual-Arm Franka. embodiment performance, are provided in Appendix E. Lightweight Models. To validate the applicability of our ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| We first analyze the scaling behavior with respect to the volume of Stage-1 pretraining data, using the full XR-1 model without any subsequent fine-tuning. | component/input/data sensitivity | p. 8 (4.3. Ablation Study) |
| To disentangle the contribution of each component in XR1, we conduct ablations on six manipulation tasks using the Dual-Arm UR-5e. | component/input/data sensitivity | p. 7 (4.3. Ablation Study) |
| Figure 9. Out-of-box evaluation results of 7 tasks on Dual-Arm UR-5e. Out-of-Box Evaluation. In addition to the evaluation on the Dual-Arm Franka, we also ... | component/input/data sensitivity | p. 24 (Figure/Table caption) |
| Additional experimental results and analysis for the UVMC ablation study, as well as for Ego4D and crossembodied knowledge transfer ablations on enhanced single7 | component/input/data sensitivity | p. 7 (4.3. Ablation Study) |
| We also provide a lightweight variant, XR-1-Light, built upon SwitchVLA (Li et al., 2025a), which uses Florence-2 (Xiao et al., 2024) to reduce computational ... | component/input/data sensitivity | p. 5 (3.5. Data Collection and Implementation Details) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our main contributions are summarized as follows: • We propose X Robotic Model 1 (XR-1), a scalable three-stage framework for VLA learning that effectively ... | As shown in Figure 7, XR-1 achieves significantly higher success rates than ACT and DP, despite the setting favoring 8 | PDF body cue; verify exact table/figure and matched conditions | p. 8 (4.4. Generalization Analysis), p. 8 (4.4. Generalization Analysis), p. 7 (4.1. Experiment Setup), p. 6 (4.1. Experiment Setup), p. 9 (4.4. Generalization Analysis), p. 6 (Figure/Table caption) |
| Primary metric/result | As shown in Figure 6, the pre-trained XR-1-oob model, despite no adaptation, achieves performance comparable to GR00T-N1.5 and π0, while outperforming RDT and UniVLA. | numeric claim only at cited anchor | p. 8 (4.4. Generalization Analysis) |

- Numeric sentences retained from the body:
- **p. 6 / 3.5. Data Collection and Implementation Details - extractive PDF cue:** Success rate results across 20 tasks on Dual-Arm UR-5e.
- **p. 6 / 4. Experiments - extractive PDF cue:** We evaluate XR-1 across six robotic embodiments and over 120 tasks, including bimanual collaboration, dexterous manipulation, and long-horizon tasks, to address four key questions: (i) ...
- **p. 6 / 4.1. Experiment Setup - extractive PDF cue:** For each embodiment, 20 tasks were designed and expert demonstrations were collected via teleoperation, recording synchronized RGB and proprioceptive streams (e.g., joint positions and gripper ...
- **p. 6 / 4.1. Experiment Setup - extractive PDF cue:** For evaluation, we conduct 20 rollouts per task and report success rates based on human evaluation.
- **p. 7 / 4.1. Experiment Setup - extractive PDF cue:** Success rate results across 20 tasks on Tien Kung 2.0.
- **p. 7 / 4.2. Results on Real-World Robotic Tasks - extractive PDF cue:** We further evaluate transferability on Tien Kung 2.0 over another 20 tasks in Table 2.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | We presented X Robotic Model 1 (XR-1), a unified framework for versatile and scalable vision-language-action learning that addresses the key limitations of existing approaches: ... | p. 9 (5. Conclusion) |
| body limitation/failure cue | Failure analyses for baselines and XR-1 are provided in Appendix I and Appendix J, respectively, showing that XR-1 reduces baseline failures such as optimization ... | p. 9 (4.5. Additional Analyses) |
| body limitation/failure cue | Figure 15. Visualizing UVMC across different embodiments (Dual-Arm Franka and Dual-Arm UR) using t-SNE. an intermediate feature supervision signal, UVMC guides the model to ... | p. 30 (Figure/Table caption) |
| body limitation/failure cue | Figure 16. Failure cases of baseline methods. Miss Miss Drop XR-1 Precision Deficiency: TK2-CollectScrews | p. 31 (Figure/Table caption) |
| body limitation/failure cue | Figure 17. Failure Cases of XR-1. • Deformable Object Handling: DFR-HangTowelRack. The robot performs a bimanual manipulation task involving deformable object handling: the right ... | p. 31 (Figure/Table caption) |
| body limitation/failure cue | Figure 1. We introduce X Robotic Model 1 (XR-1), a versatile and scalable vision-language-action framework. XR-1 supports robust multi-task learning across diverse robot embodiments ... | p. 1 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Dataset Episodes Frames Weight OXE 978k 59.3M 40% RoboMIND 69k 21.4M 15% XR-D 158k 69.1M 35% Ego4D 59k 14.3M 10% Implementation Details. | p. 5 (3.5. Data Collection and Implementation Details) |
| Our main instantiation follows the design of π0 (Black et al., 2025), built on PaliGemma (Beyer et al., 2024) with a SigLIP visual encoder ... | p. 5 (3.5. Data Collection and Implementation Details) |
| We note a performance degradation with the Lerobot implementation of π0. | p. 7 (4.2. Results on Real-World Robotic Tasks) |
| The results of π0 reported in this paper are based on the original JAX implementation. | p. 7 (4.2. Results on Real-World Robotic Tasks) |
| To assess semantic alignment between visual codes (VC) and motion codes (MC), we perform cross-modal nearestneighbor retrieval and t-SNE visualization. | p. 9 (4.5. Additional Analyses) |
| Given two frames ct and ct+h, the vision encoder Evis(·) produces a latent code zvis = Evis(ct, ct+h), which compresses temporal changes over h ... | p. 4 (3.1. Overview) |
| The decoder reconstructs actions as 4 | p. 4 (3.1. Overview) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 9 / 5. Conclusion - extractive PDF cue:** We presented X Robotic Model 1 (XR-1), a unified framework for versatile and scalable vision-language-action learning that addresses the key limitations of existing approaches: precise ...
- **p. 9 / 4.5. Additional Analyses - extractive PDF cue:** Failure analyses for baselines and XR-1 are provided in Appendix I and Appendix J, respectively, showing that XR-1 reduces baseline failures such as optimization collapse, ...
- **p. 30 / Figure/Table caption - extractive PDF cue:** Figure 15. Visualizing UVMC across different embodiments (Dual-Arm Franka and Dual-Arm UR) using t-SNE. an intermediate feature supervision signal, UVMC guides the model to generate ...
- **p. 31 / Figure/Table caption - extractive PDF cue:** Figure 16. Failure cases of baseline methods. Miss Miss Drop XR-1 Precision Deficiency: TK2-CollectScrews
- **p. 31 / Figure/Table caption - extractive PDF cue:** Figure 17. Failure Cases of XR-1. • Deformable Object Handling: DFR-HangTowelRack. The robot performs a bimanual manipulation task involving deformable object handling: the right arm ...
- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. We introduce X Robotic Model 1 (XR-1), a versatile and scalable vision-language-action framework. XR-1 supports robust multi-task learning across diverse robot embodiments and ...

- **PDF anchors reviewed:** datasets p. 7 (4.2. Results on Real-World Robotic Tasks), p. 6 (4. Experiments), p. 8 (4.3. Ablation Study), p. 8 (4.4. Generalization Analysis), p. 9 (4.5. Additional Analyses), p. 5 (3.5. Data Collection and Implementation Details), metrics p. 6 (4.1. Experiment Setup), p. 7 (4.1. Experiment Setup), p. 8 (4.3. Ablation Study), p. 8 (4.4. Generalization Analysis), p. 9 (4.4. Generalization Analysis), p. 6 (Figure/Table caption), baselines p. 24 (Figure/Table caption), p. 7 (4.2. Results on Real-World Robotic Tasks), p. 7 (4.2. Results on Real-World Robotic Tasks), p. 6 (4. Experiments), p. 6 (4. Experiments), p. 8 (4.3. Ablation Study), results p. 8 (4.4. Generalization Analysis), p. 8 (4.4. Generalization Analysis), p. 7 (4.1. Experiment Setup), p. 6 (4.1. Experiment Setup), p. 9 (4.4. Generalization Analysis), p. 6 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
