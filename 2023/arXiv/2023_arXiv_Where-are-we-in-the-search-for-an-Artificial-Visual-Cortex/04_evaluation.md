# Evaluation - Where are we in the search for an Artificial Visual Cortex for Embodied Intelligence?

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (23 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2303.18240; PDF retrieval source: https://arxiv.org/abs/2303.18240. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 2 (Figure/Table caption), p. 8 (Results), p. 8 (Results), p. 7 (Results), p. 9 (Results), p. 5 (Results)): Figure 1: An artificial visual cortex for embodied in- telligence must support a diverse range of sensorimotor skills, environments, and embodiments; we curate COR- TEXBENCH to systematically measure progress towards ...

## Evaluation Body Digest

- **p. 21 / A.11 TriFinger Hardware Experiment Setup - extractive body cue:** We carried out experiments on the real TriFinger robot (shown in Figure 9) for the Push-Cube task, after training a model using behavior cloning on ...
- **p. 5 / Results - extractive body cue:** Interestingly, while the model pre-trained on the largest dataset (CLIP) performs well on one benchmark (ObjectNav) it does not perform well across all tasks.
- **p. 5 / Results - extractive body cue:** Habitat 2.0 [15] includes mobile manipulation tasks in which agents control a Fetch robot with a 7-DoF arm, mobile base [46], and suction gripper to ...
- **p. 6 / Results - extractive body cue:** This dataset is used to study the role of internet images for our benchmark tasks.
- **p. 7 / Results - extractive body cue:** Finally, our largest model (ViT-L) pre-trained on all datasets (Ego4D+MNI), achieves the best rank when averaged across all benchmark tasks (Table 4 row 11), with ...
- **p. 9 / Results - extractive body cue:** In the remaining two benchmarks (ImageNav and Mobile Pick) we sample frames from training environments to create adaptation datasets.
- **p. 22 / A.12 Franka Hardware Experiment Setup - extractive body cue:** This results in poor trajectory tracking performance, yet both human teleoperators and learned policy can control the robot to complete the tasks.
- **p. 4 / Results - extractive body cue:** MetaWorld (MW) [11] is a collection of tasks in which agents command a Sawyer robot arm to manipulate objects in a tabletop environment.

## Evaluation Type and Scope

- **Evaluation type:** `BENCHMARK / DATASET`.
- **Target system/task:** defined robot simulator/hardware task suite.
- **Input boundary:** standardized observation, action, task state와 evaluation split.
- **Output/decision under evaluation:** policy/controller trajectory 또는 measured result.
- **Primary target:** success metric, robustness, generalization과 reproducibility.
- **Detected evaluation headings:** Dataset (p. 4); Evaluation (p. 4); Results (p. 4); A.5 Scaling Hypothesis Datasets (p. 18); A.5.1 OpenHouse24 Dataset (p. 18); A.7 Additional Analysis of Scaling Hypothesis Results (p. 18); A.11 TriFinger Hardware Experiment Setup (p. 21); A.12 Franka Hardware Experiment Setup (p. 22).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | BENCHMARK / DATASET | Figure 1: An artificial visual cortex for embodied in- telligence must support a diverse range of sensorimotor skills, environments, and embodiments; we curate COR- ... | p. 2 (Figure/Table caption) |
| Results | BENCHMARK / DATASET | Specifically, we see an improvement in ObjectNav success rate (SR) of +7.4 (60.3 →67.7), ImageNav SR of +11.3 (70.3 →81.6), and Mobile Pick SR ... | p. 8 (Results) |
| Results | BENCHMARK / DATASET | In domains that involve large-scale IL or RL (ObjectNav, ImageNav, and Mobile Pick), the strategy proposed in [5] of adapting VC-1 with E2E fine-tuning ... | p. 8 (Results) |
| Results | BENCHMARK / DATASET | In these results, we find that increasing diversity by adding indoor navigation data improves performance more than adding additional manipulation data to Ego4D. | p. 7 (Results) |
| Results | BENCHMARK / DATASET | In the CORTEXBENCH results in Table 5, we observe MAE adaptation substantially improves performance in few-shot learning domains. | p. 9 (Results) |

## Dataset / Benchmark Role

- **p. 21 / A.11 TriFinger Hardware Experiment Setup - extractive body cue:** We carried out experiments on the real TriFinger robot (shown in Figure 9) for the Push-Cube task, after training a model using behavior cloning on ...
- **p. 5 / Results - extractive body cue:** Interestingly, while the model pre-trained on the largest dataset (CLIP) performs well on one benchmark (ObjectNav) it does not perform well across all tasks.
- **p. 5 / Results - extractive body cue:** Habitat 2.0 [15] includes mobile manipulation tasks in which agents control a Fetch robot with a 7-DoF arm, mobile base [46], and suction gripper to ...
- **p. 6 / Results - extractive body cue:** This dataset is used to study the role of internet images for our benchmark tasks.
- **p. 7 / Results - extractive body cue:** Finally, our largest model (ViT-L) pre-trained on all datasets (Ego4D+MNI), achieves the best rank when averaged across all benchmark tasks (Table 4 row 11), with ...
- **p. 9 / Results - extractive body cue:** In the remaining two benchmarks (ImageNav and Mobile Pick) we sample frames from training environments to create adaptation datasets.
- **p. 22 / A.12 Franka Hardware Experiment Setup - extractive body cue:** This results in poor trajectory tracking performance, yet both human teleoperators and learned policy can control the robot to complete the tasks.
- **p. 4 / Results - extractive body cue:** MetaWorld (MW) [11] is a collection of tasks in which agents command a Sawyer robot arm to manipulate objects in a tabletop environment.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: An artificial visual cortex for embodied in- telligence must support a diverse range of sensorimotor skills, environments, and embodiments; we curate COR- TEXBENCH ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: CORTEXBENCH: We systematically evaluate pre-trained visual representations by varying datasets and representation learning algorithms, coupled with reinforcement or imitation learning on diverse EAI ...
- **p. 4 / Figure/Table caption - extractive body cue:** Table 1: CORTEXBENCH includes tasks from 7 diverse benchmarks with different combinations of observations, actions, goals, and standard policy learning paradigms. Benchmark Suite Observation Space ...
- **p. 5 / Figure/Table caption - extractive body cue:** Table 2: Performance of frozen pre-trained visual representations (PVRs) on CORTEXBENCH. Best prior results are the best reported in literature prior to this work. Overall, ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3: Visualization of scaling hypothesis model performance averaged over CORTEXBENCH. We see modest but positive scaling trends in both (a) scaling model size and ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 3: Datasets assembled to study effects of pre- training dataset size, diversity, and relevance - the largest (Ego4D+MNI) has 5.6M frames. More details in ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 4: Performance of scaling hypothesis models on CORTEXBENCH. We find that on average the VC-1 EGO4D+MNI (VIT-L) model performs best, but is not the ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 4: Comparison of VC-1 with existing PVRs. VC-1 matches or exceeds existing PVRs on all benchmarks except R3M on AD, MW, and DMC, indicating ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We carried out experiments on the real TriFinger robot (shown in Figure 9) for the Push-Cube task, after training a model using behavior cloning ... | embodiment, simulator version and control stack | p. 21 (A.11 TriFinger Hardware Experiment Setup), p. 5 (Results) |
| Task/environment | Interestingly, while the model pre-trained on the largest dataset (CLIP) performs well on one benchmark (ObjectNav) it does not perform well across all tasks. | reset, timeout, object/scene variation | p. 5 (Results), p. 5 (Results) |
| Observation/sensor | standardized observation, action, task state와 evaluation split | calibration, preprocessing, privileged input | p. 17 (A.2 Overview of Downstream Policy Learning in CORTEXBENCH), p. 1 (1 Introduction) |
| Output/decision | policy/controller trajectory 또는 measured result | action frame, controller and termination | p. 17 (A.2 Overview of Downstream Policy Learning in CORTEXBENCH), p. 16 (A.2 Overview of Downstream Policy Learning in CORTEXBENCH) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Mean Success: the average success rate across all benchmarks. | definition/direction/unit from same section | p. 4 (Results) |
| Specifically, we see an improvement in ObjectNav success rate (SR) of +7.4 (60.3 →67.7), ImageNav SR of +11.3 (70.3 →81.6), and Mobile Pick SR ... | definition/direction/unit from same section | p. 8 (Results) |
| Figure 1: An artificial visual cortex for embodied in- telligence must support a diverse range of sensorimotor skills, environments, and embodiments; we curate COR- ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |
| Table 8: The success rate for each task and each model we evaluate during the study before being aggregated by benchmark. TASK | definition/direction/unit from same section | p. 20 (Figure/Table caption) |
| Table 9: Franka manipulation task success rates. Reaching Bottle Pickup Open Drawer Plunge Toaster Success Count Success % Demos | definition/direction/unit from same section | p. 23 (Figure/Table caption) |
| The variance in performance of existing PVRs on CORTEXBENCH is further illustrated in Figure 5 in Appendix A.4 and highlights that we do not ... | definition/direction/unit from same section | p. 5 (Results) |
| We strategically select dataset combinations (shown in Table 3) to answer the following questions: - What is the impact of scaling dataset size and ... | definition/direction/unit from same section | p. 6 (Results) |
| Interestingly, these results demonstrate that including static internet images can significantly boost performance on EAI tasks. | definition/direction/unit from same section | p. 7 (Results) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| However, we find that several of these pre-trained models often outperform a random training from scratch baseline. | comparison identity and matched condition | p. 5 (Results) |
| Figure 4: Comparison of VC-1 with existing PVRs. VC-1 matches or exceeds existing PVRs on all benchmarks except R3M on AD, MW, and DMC, ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| Figure 1: An artificial visual cortex for embodied in- telligence must support a diverse range of sensorimotor skills, environments, and embodiments; we curate COR- ... | comparison identity and matched condition | p. 2 (Figure/Table caption) |
| For instance, when pre-trained on Ego4D+MNI, the ViT-B model outperforms the ViT-L model on MetaWorld and TriFinger. | comparison identity and matched condition | p. 7 (Results) |
| The gains with Ego4D+N are larger and it outperforms Ego4D by 1.6 points using ViT-B (62.2 →63.8) and by 3.6 points for ViT-L (63.5 ... | comparison identity and matched condition | p. 7 (Results) |
| Together, these results demonstrate that adaptation of PVRs can be a powerful paradigm for EAI, especially when compared to training representations from scratch. | comparison identity and matched condition | p. 9 (Results) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| For all evaluations preceding Section 6, we consider frozen visual representations to disentangle the effect of learned representations from downstream task learning. | component/input/data sensitivity | p. 5 (Results) |
| 5.2 Scaling Hypothesis Findings We now turn to analyzing the effect of increasing model size, dataset size, and dataset diversity. | component/input/data sensitivity | p. 6 (Results) |
| Figure 7: Scaling model size has a positive effect on (a) every benchmark and on (b) fifteen out of the seventeen tasks. A.10 Attention ... | component/input/data sensitivity | p. 20 (Figure/Table caption) |
| Figure 8: Attention Visualization: (left) Random ViT-L; (middle) VC-1 frozen; (right) VC-1 E2E finetuned. We overlay the mean attention matrix in the last layer ... | component/input/data sensitivity | p. 21 (Figure/Table caption) |
| Adroit Dexterous … … … 7 datasets 7 methods 17 tasks Ego4D RealEstate10K encoder .... .... decoder input target MAE "stirs the snacks…" Time ... | component/input/data sensitivity | p. 4 (Dataset) |
| 5.1 Constructing a Pre-training Dataset for EAI Table 3: Datasets assembled to study effects of pretraining dataset size, diversity, and relevance - the largest ... | component/input/data sensitivity | p. 6 (Results) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| The visual cortex is a region of an organism's brain, which together with the motor cortex, enables sight to be converted into movement. | Figure 1: An artificial visual cortex for embodied in- telligence must support a diverse range of sensorimotor skills, environments, and embodiments; we curate COR- ... | PDF body cue; verify exact table/figure and matched conditions | p. 2 (Figure/Table caption), p. 8 (Results), p. 8 (Results), p. 7 (Results), p. 9 (Results), p. 5 (Results) |
| Primary metric/result | Specifically, we see an improvement in ObjectNav success rate (SR) of +7.4 (60.3 →67.7), ImageNav SR of +11.3 (70.3 →81.6), and Mobile Pick SR ... | numeric claim only at cited anchor | p. 8 (Results) |

- Numeric sentences retained from the body:
- **p. 4 / Dataset - extractive body cue:** Adroit Dexterous … … … 7 datasets 7 methods 17 tasks Ego4D RealEstate10K encoder .... .... decoder input target MAE "stirs the snacks…" Time Contrastive ...
- **p. 7 / Results - extractive body cue:** For instance, Ego4D+M slightly improves upon Ego4D by 0.6 and 0.9 points (62.2 →62.8 and 63.5 →64.4) in the case of ViT-B and ViT-L, respectively.
- **p. 7 / Results - extractive body cue:** The gains with Ego4D+N are larger and it outperforms Ego4D by 1.6 points using ViT-B (62.2 →63.8) and by 3.6 points for ViT-L (63.5 → ...
- **p. 7 / Results - extractive body cue:** We see a 0.3 and 0.1 point difference (63.8 →64.1 and 67.1 →67.2) for ViT-B and ViT-L, respectively, even though Ego4D+MN has about 800K more ...
- **p. 7 / Results - extractive body cue:** For example, models pre-trained on Ego4D+MNI outperform those pre-trained on Ego4D+MN by 1.9 points (64.1 →66.2) for ViT-B and 1.5 points (67.2 →68.7) for ViT-L.
- **p. 7 / Results - extractive body cue:** In terms of mean success, VC-1 (Table 4 row 11) outperforms MVP (ViT-L) by +1.2 points (67.5 →68.7), R3M by +10.7 (58.0 →68.7), CLIP by ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | This study presents a thorough examination of visual foundation models but has several limitations. | p. 16 (A.1 Limitations) |
| body limitation/failure cue | Additionally, we include randomly initialized ViTs with frozen- and finetuned weights to assess the necessity of pre-training and the limitations of pure in-domain learning. | p. 5 (Results) |
| body limitation/failure cue | While this adaptation strategy cannot address task-specialization, it may serve to mitigate domain gap. | p. 9 (Results) |
| body limitation/failure cue | In aggregate, these results suggests that MAE adaptation can be explored as a powerful alternative in few-shot domains or where E2E fine-tuning fails. | p. 9 (Results) |
| body limitation/failure cue | Interestingly, while the model pre-trained on the largest dataset (CLIP) performs well on one benchmark (ObjectNav) it does not perform well across all tasks. | p. 5 (Results) |
| body limitation/failure cue | While larger than Ego4D+M and Ego4D+N, it does not include any new types of data beyond the manipulation and navigation videos in the previous ... | p. 6 (Results) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| For PVR (frozen encoders), we use Adam optimizer with a learning rate 10-3 to train the policies. | p. 22 (A.12 Franka Hardware Experiment Setup) |
| For fine-tuning, we use the same learning rate for policies but a lower learning rate (10-5) for the visual encoders. | p. 22 (A.12 Franka Hardware Experiment Setup) |
| We choose the number of epochs per run such that the number of model updates remain constant across all runs and match the number ... | p. 18 (A.6 Scaling Hypothesis Pretraining Details) |
| To train the MAE models, we use the official codebase released by the authors on GitHub [18] and use the default hyperparameters provided by ... | p. 18 (A.6 Scaling Hypothesis Pretraining Details) |
| Specifically, we used a learning rate of 10-4 for the visual encoder and 10-3 for all other elements, with the AdamW optimizer. | p. 17 (A.2 Overview of Downstream Policy Learning in CORTEXBENCH) |
| Similar to our previous image-based navigation (ImageNav) experiments, we employed a weight decay of 10-6 and utilized different learning rates for the visual encoder ... | p. 17 (A.2 Overview of Downstream Policy Learning in CORTEXBENCH) |
| The episode length for this task is 20 steps. | p. 21 (A.11 TriFinger Hardware Experiment Setup) |
| For each model, we chose 1 seed and ran it on 12 different start and goal configurations, mostly centered in the arena. | p. 21 (A.11 TriFinger Hardware Experiment Setup) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 16 / A.1 Limitations - extractive body cue:** This study presents a thorough examination of visual foundation models but has several limitations.
- **p. 5 / Results - extractive body cue:** Additionally, we include randomly initialized ViTs with frozen- and finetuned weights to assess the necessity of pre-training and the limitations of pure in-domain learning.
- **p. 9 / Results - extractive body cue:** While this adaptation strategy cannot address task-specialization, it may serve to mitigate domain gap.
- **p. 9 / Results - extractive body cue:** In aggregate, these results suggests that MAE adaptation can be explored as a powerful alternative in few-shot domains or where E2E fine-tuning fails.
- **p. 5 / Results - extractive body cue:** Interestingly, while the model pre-trained on the largest dataset (CLIP) performs well on one benchmark (ObjectNav) it does not perform well across all tasks.
- **p. 6 / Results - extractive body cue:** While larger than Ego4D+M and Ego4D+N, it does not include any new types of data beyond the manipulation and navigation videos in the previous subsets.

- **Evidence anchors reviewed:** datasets p. 21 (A.11 TriFinger Hardware Experiment Setup), p. 5 (Results), p. 5 (Results), p. 6 (Results), p. 7 (Results), p. 9 (Results), metrics p. 4 (Results), p. 8 (Results), p. 2 (Figure/Table caption), p. 20 (Figure/Table caption), p. 23 (Figure/Table caption), p. 5 (Results), baselines p. 5 (Results), p. 8 (Figure/Table caption), p. 2 (Figure/Table caption), p. 7 (Results), p. 7 (Results), p. 9 (Results), results p. 2 (Figure/Table caption), p. 8 (Results), p. 8 (Results), p. 7 (Results), p. 9 (Results), p. 5 (Results).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (23 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Figure 4: Comparison of VC-1 with existing PVRs. VC-1 matches or exceeds existing PVRs on all benchmarks except R3M on AD, MW, and DMC, indicating an opportunity for model adaptation. ... (p. 8, Figure/Table caption).
- **Metric evidence:** Mean Success: the average success rate across all benchmarks. (p. 4, Results).
- **Baseline/ablation evidence:** However, we find that several of these pre-trained models often outperform a random training from scratch baseline. (p. 5, Results).
- **Failure/negative evidence:** In aggregate, these results suggests that MAE adaptation can be explored as a powerful alternative in few-shot domains or where E2E fine-tuning fails. (p. 9, Results).
