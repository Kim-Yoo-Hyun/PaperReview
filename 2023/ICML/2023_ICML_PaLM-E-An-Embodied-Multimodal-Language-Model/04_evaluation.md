# Evaluation - PaLM-E: An Embodied Multimodal Language Model

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2303.03378; PDF retrieval source: https://arxiv.org/pdf/2303.03378. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (Figure/Table caption), p. 9 (6.5. Performance on General Visual-Language Tasks), p. 6 (6. Experiments), p. 7 (6.2. TAMP Environment), p. 9 (7. Summary of Experiments & Discussion), p. 7 (6.3. Language-Table Environment)): Table 1: Comparison of different input representations on TAMP environment (in terms of success rates), where data from TAMP constitutes only 1% (i.e., 320 samples for p1, p2 each) of ...

## Evaluation Body Digest

- **p. 7 / 6.3. Language-Table Environment - extractive body cue:** 7, c) and to tasks involving objects that were unseen in either the original robot dataset or the finetuning datasets, e.g. a toy turtle (Fig.
- **p. 6 / 6. Experiments - extractive body cue:** Here we show that a single model, trained on a mixture of many datasets, across diverse tasks, and across robot embodiments, can simultaneously achieve high ...
- **p. 7 / 6.2. TAMP Environment - extractive body cue:** 7, the input representations are trained on a dataset containing 96,000 training scenes of solely the TAMP environment, i.e. no other data is part of ...
- **p. 6 / 6. Experiments - extractive body cue:** 1) include a Task and Motion Planning (TAMP) domain where a robot has to manipulate (grasp and stack) objects, a table-top pushing environment, and a ...
- **p. 9 / 7. Summary of Experiments & Discussion - extractive body cue:** Compared to available massive language or vision-language datasets, robotics data is significantly less abundant.
- **p. 8 / 6.4. Mobile Manipulation Environment - extractive body cue:** ObjectLLM Embodied VQA Planning centric pre-train q1 q2 q3 q4 p1 p2 SayCan (oracle afford.) (Ahn et al., 2022)  - - - - 38.7 ...
- **p. 9 / 6.5. Performance on General Visual-Language Tasks - extractive body cue:** PaLM-E: An Embodied Multimodal Language Model Zero-shot Baselines Task 1 Task 2 Task 3 SayCan (oracle afford.) (Ahn et al., 2022) 0.0 - - PaLI ...
- **p. 8 / 6.4. Mobile Manipulation Environment - extractive body cue:** The prompt structure for this task is Human: <instruction> Robot: <step history>.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SIMULATION`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 6. Experiments (p. 6); 7. Summary of Experiments & Discussion (p. 9).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / SIMULATION | Table 1: Comparison of different input representations on TAMP environment (in terms of success rates), where data from TAMP constitutes only 1% (i.e., 320 ... | p. 8 (Figure/Table caption) |
| 6.5. Performance on General Visual-Language Tasks | EMPIRICAL / SIMULATION | PaLM-E-562B model achieves the highest reported number on OK-VQA, including outperforming models finetuned specifically on OK-VQA. | p. 9 (6.5. Performance on General Visual-Language Tasks) |
| 6. Experiments | EMPIRICAL / SIMULATION | Here we show that a single model, trained on a mixture of many datasets, across diverse tasks, and across robot embodiments, can simultaneously achieve ... | p. 6 (6. Experiments) |
| 6.2. TAMP Environment | EMPIRICAL / SIMULATION | However, when increasing the number of objects, it turns out that using a pre-trained LLM improves performance considerably, especially with entity referrals. | p. 7 (6.2. TAMP Environment) |
| 7. Summary of Experiments & Discussion | EMPIRICAL / SIMULATION | 4, co-training on the "full mixture" achieves more than double the performance. | p. 9 (7. Summary of Experiments & Discussion) |

## Dataset / Benchmark Role

- **p. 7 / 6.3. Language-Table Environment - extractive body cue:** 7, c) and to tasks involving objects that were unseen in either the original robot dataset or the finetuning datasets, e.g. a toy turtle (Fig.
- **p. 6 / 6. Experiments - extractive body cue:** Here we show that a single model, trained on a mixture of many datasets, across diverse tasks, and across robot embodiments, can simultaneously achieve high ...
- **p. 7 / 6.2. TAMP Environment - extractive body cue:** 7, the input representations are trained on a dataset containing 96,000 training scenes of solely the TAMP environment, i.e. no other data is part of ...
- **p. 6 / 6. Experiments - extractive body cue:** 1) include a Task and Motion Planning (TAMP) domain where a robot has to manipulate (grasp and stack) objects, a table-top pushing environment, and a ...
- **p. 9 / 7. Summary of Experiments & Discussion - extractive body cue:** Compared to available massive language or vision-language datasets, robotics data is significantly less abundant.
- **p. 8 / 6.4. Mobile Manipulation Environment - extractive body cue:** ObjectLLM Embodied VQA Planning centric pre-train q1 q2 q3 q4 p1 p2 SayCan (oracle afford.) (Ahn et al., 2022)  - - - - 38.7 ...
- **p. 9 / 6.5. Performance on General Visual-Language Tasks - extractive body cue:** PaLM-E: An Embodied Multimodal Language Model Zero-shot Baselines Task 1 Task 2 Task 3 SayCan (oracle afford.) (Ahn et al., 2022) 0.0 - - PaLI ...
- **p. 8 / 6.4. Mobile Manipulation Environment - extractive body cue:** The prompt structure for this task is Human: <instruction> Robot: <step history>.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: PaLM-E is a single general-purpose multimodal language model for embodied reasoning tasks, visual-language tasks, and language tasks. PaLM-E transfers knowledge from visual-language domains ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 2: PaLM-E-562B can do zero-shot multimodal chain-of-thought reasoning, can tell visually-conditioned jokes given an image, and demonstrates an array of robot-relevant multimodal-informed capabilities including ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3: Overview of transfer learning demonstrated by PaLM- E: across three different robotics domains, using PaLM and ViT pretraining together with the full mixture ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4: Planning success results in the TAMP environment (1% data) for PaLM-E-12B, comparing of the effects of PaLM-E models (i) using the full training ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5: A single PaLM-E model directs the low-level policies of two real robots. Shown is a long-horizon mobile manipulation task in a kitchen, and ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 1: Comparison of different input representations on TAMP environment (in terms of success rates), where data from TAMP constitutes only 1% (i.e., 320 samples ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 2: Results on planning tasks in the simulated environment from Lynch et al. (2022). Task 1. Q: There is a block that is closest ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 3: Task prompts for Tab. 2. Baselines Failure det. Affordance PaLI (Zero-shot) (Chen et al., 2022) 0.73 0.62 CLIP-FT (Xiao et al., 2022)

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | 7, c) and to tasks involving objects that were unseen in either the original robot dataset or the finetuning datasets, e.g. a toy turtle ... | embodiment, simulator version and control stack | p. 7 (6.3. Language-Table Environment), p. 6 (6. Experiments) |
| Task/environment | Here we show that a single model, trained on a mixture of many datasets, across diverse tasks, and across robot embodiments, can simultaneously achieve ... | reset, timeout, object/scene variation | p. 6 (6. Experiments), p. 7 (6.2. TAMP Environment) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 2 (1. Introduction), p. 1 (1. Introduction) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 5 (5. Training Recipes), p. 2 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| 7 (appendix) shows planning success rates and VQA performance for the TAMP environment. | definition/direction/unit from same section | p. 6 (6.2. TAMP Environment) |
| 2 reports success rates on long-horizon tasks from the Language-Table environment (Lynch et al., 2022). | definition/direction/unit from same section | p. 7 (6.3. Language-Table Environment) |
| ObjectLLM Embodied VQA Planning centric pre-train q1 q2 q3 q4 p1 p2 SayCan (oracle afford.) (Ahn et al., 2022)  - - - - ... | definition/direction/unit from same section | p. 8 (6.4. Mobile Manipulation Environment) |
| Table 7: Success rates on TAMP environment for different input representations. 3-5 objects in the scene correspond to the training distribution. OOD tasks means ... | definition/direction/unit from same section | p. 16 (Figure/Table caption) |
| Affordance PaLI (Zero-shot) (Chen et al., 2022) 0.73 0.62 CLIP-FT (Xiao et al., 2022) 0.65 - CLIP-FT-hindsight (Xiao et al., 2022) 0.89 - QT-OPT ... | definition/direction/unit from same section | p. 9 (6.5. Performance on General Visual-Language Tasks) |
| Table 9: Mobile manipulation environment: failure detection, showing individual precision and recall scores. | definition/direction/unit from same section | p. 18 (Figure/Table caption) |
| We study the influence on performance, generalization, and data efficiency with respect to co-training strategies and model parameter size. | definition/direction/unit from same section | p. 6 (6. Experiments) |
| We demonstrate the performance of PaLM-E on challenging and diverse mobile manipulation tasks. | definition/direction/unit from same section | p. 7 (6.4. Mobile Manipulation Environment) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| As baselines, we consider the state-of-the art visual language model PaLI (Chen et al., 2022), which has not been trained on embodiment robot data, ... | comparison identity and matched condition | p. 6 (6. Experiments) |
| The SayCan baseline (Ahn et al., 2022) utilizes oracle affordance functions and has difficulties solving this environment, since affordance functions only constrain what is ... | comparison identity and matched condition | p. 7 (6.2. TAMP Environment) |
| PaLM-E: An Embodied Multimodal Language Model Zero-shot Baselines Task 1 Task 2 Task 3 SayCan (oracle afford.) (Ahn et al., 2022) 0.0 - - ... | comparison identity and matched condition | p. 9 (6.5. Performance on General Visual-Language Tasks) |
| Table 5: Results on general visual-language tasks. For the gen- eralist models, they are the same checkpoint across the different evaluations, while task-specific finetuned ... | comparison identity and matched condition | p. 9 (Figure/Table caption) |
| Table 7: Success rates on TAMP environment for different input representations. 3-5 objects in the scene correspond to the training distribution. OOD tasks means ... | comparison identity and matched condition | p. 16 (Figure/Table caption) |
| ObjectLLM Embodied VQA Planning centric pre-train q1 q2 q3 q4 p1 p2 SayCan (oracle afford.) (Ahn et al., 2022)  - - - - ... | comparison identity and matched condition | p. 8 (6.4. Mobile Manipulation Environment) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| 0% LLM finetune (full mixture) LLM finetune (single robot) without pretraining LLM frozen (full mixture) LLM frozen (single robot) 20% 40% 60% 80% 100% ... | component/input/data sensitivity | p. 7 (6.3. Language-Table Environment) |
| Furthermore, we show that a 62B LLM shows better out-of-distribution generalization compared to the 8B variant, while a non-pretrained LLM shows basically no outof-distribution ... | component/input/data sensitivity | p. 7 (6.2. TAMP Environment) |
| The non-object centric ViT-4B variant utilizes color to reference objects, hence q1 cannot be evaluated here. | component/input/data sensitivity | p. 8 (6.4. Mobile Manipulation Environment) |
| Q: How to push all the blocks that are on the {left/right} side together, without bringing over any of the blocks that are on ... | component/input/data sensitivity | p. 9 (6.5. Performance on General Visual-Language Tasks) |
| Affordance PaLI (Zero-shot) (Chen et al., 2022) 0.73 0.62 CLIP-FT (Xiao et al., 2022) 0.65 - CLIP-FT-hindsight (Xiao et al., 2022) 0.89 - QT-OPT ... | component/input/data sensitivity | p. 9 (6.5. Performance on General Visual-Language Tasks) |
| Figure 3: Overview of transfer learning demonstrated by PaLM- E: across three different robotics domains, using PaLM and ViT pretraining together with the full ... | component/input/data sensitivity | p. 6 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In this paper we propose embodied language models, which | Table 1: Comparison of different input representations on TAMP environment (in terms of success rates), where data from TAMP constitutes only 1% (i.e., 320 ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (Figure/Table caption), p. 9 (6.5. Performance on General Visual-Language Tasks), p. 6 (6. Experiments), p. 7 (6.2. TAMP Environment), p. 9 (7. Summary of Experiments & Discussion), p. 7 (6.3. Language-Table Environment) |
| Primary metric/result | PaLM-E-562B model achieves the highest reported number on OK-VQA, including outperforming models finetuned specifically on OK-VQA. | numeric claim only at cited anchor | p. 9 (6.5. Performance on General Visual-Language Tasks) |

- Numeric sentences retained from the body:
- **p. 7 / 6.2. TAMP Environment - extractive body cue:** For 3-5 objects in the scene, which is the same number as in the training set, most input representations perform similarly well.
- **p. 7 / 6.2. TAMP Environment - extractive body cue:** 1 shows results for 3-5 objects when training on 1% of the dataset, which corresponds to only 320 examples for each of the two planning ...
- **p. 7 / 6.3. Language-Table Environment - extractive body cue:** Scaling the 12B model to the 84B model leads to improvements on 2 of 3 tasks.
- **p. 7 / 6.3. Language-Table Environment - extractive body cue:** Given the observed image and a long-horizon goal, e.g. "sort the blocks by colors into corners", PaLM-E outputs language subgoals at 1 Hz to the ...
- **p. 7 / 6.3. Language-Table Environment - extractive body cue:** (2022), that output low-level robot actions at 5 Hz.
- **p. 8 / 6.4. Mobile Manipulation Environment - extractive body cue:** ObjectLLM Embodied VQA Planning centric pre-train q1 q2 q3 q4 p1 p2 SayCan (oracle afford.) (Ahn et al., 2022)  - - - - 38.7 ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | For the mobile manipulation and Language-Table environments, PaLM-E is integrated into the control loop to execute the plans in the real world, and has ... | p. 6 (6. Experiments) |
| body limitation/failure cue | Put down the sponge." Inspired by these tasks, we develop 3 use cases to test the embodied reasoning abilities of PaLM-E: affordance prediction, failure ... | p. 7 (6.4. Mobile Manipulation Environment) |
| body limitation/failure cue | For a robot to do closed-loop planning, it is also important to detect failures, as is shown in (Huang et al., 2022c). | p. 8 (6.4. Mobile Manipulation Environment) |
| body limitation/failure cue | This method has access to more information than our method, and was specifically designed to just solve failure detection on this dataset. | p. 8 (6.4. Mobile Manipulation Environment) |
| body limitation/failure cue | Table 4: Mobile manipulation environment: failure detection and affordance prediction (F1 score). VQAv2 OK-VQA COCO | p. 9 (Figure/Table caption) |
| body limitation/failure cue | Table 3: Task prompts for Tab. 2. Baselines Failure det. Affordance PaLI (Zero-shot) (Chen et al., 2022) 0.73 0.62 CLIP-FT (Xiao et al., 2022) | p. 9 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Those encoders are either pre-trained or trained from scratch, see Sec. | p. 5 (5. Training Recipes) |
| Most of our architectures consist of three parts, an encoder ˜φ, a projector ψ, and the LLM pLM. | p. 5 (5. Training Recipes) |
| PaLM-E has to generate plans that consist of multiple steps, with complicated decision boundaries. | p. 6 (6. Experiments) |
| PaLM-E: An Embodied Multimodal Language Model input encoders, and if so, how different-modality encoders compare. | p. 6 (5. Training Recipes) |
| After each step is decoded, we map them to a low-level policy as defined in Ahn et al. | p. 8 (6.4. Mobile Manipulation Environment) |
| PaLM-E is trained to generate the next step of the plan, conditioned on the history of taken steps and the current image observation of ... | p. 8 (6.4. Mobile Manipulation Environment) |
| For the generalist models, they are the same checkpoint across the different evaluations, while task-specific finetuned models use differentfinetuned models for the different tasks. | p. 9 (6.5. Performance on General Visual-Language Tasks) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / 6. Experiments - extractive body cue:** For the mobile manipulation and Language-Table environments, PaLM-E is integrated into the control loop to execute the plans in the real world, and has to ...
- **p. 7 / 6.4. Mobile Manipulation Environment - extractive body cue:** Put down the sponge." Inspired by these tasks, we develop 3 use cases to test the embodied reasoning abilities of PaLM-E: affordance prediction, failure detection, ...
- **p. 8 / 6.4. Mobile Manipulation Environment - extractive body cue:** For a robot to do closed-loop planning, it is also important to detect failures, as is shown in (Huang et al., 2022c).
- **p. 8 / 6.4. Mobile Manipulation Environment - extractive body cue:** This method has access to more information than our method, and was specifically designed to just solve failure detection on this dataset.
- **p. 9 / Figure/Table caption - extractive body cue:** Table 4: Mobile manipulation environment: failure detection and affordance prediction (F1 score). VQAv2 OK-VQA COCO
- **p. 9 / Figure/Table caption - extractive body cue:** Table 3: Task prompts for Tab. 2. Baselines Failure det. Affordance PaLI (Zero-shot) (Chen et al., 2022) 0.73 0.62 CLIP-FT (Xiao et al., 2022)

- **Evidence anchors reviewed:** datasets p. 7 (6.3. Language-Table Environment), p. 6 (6. Experiments), p. 7 (6.2. TAMP Environment), p. 6 (6. Experiments), p. 9 (7. Summary of Experiments & Discussion), p. 8 (6.4. Mobile Manipulation Environment), metrics p. 6 (6.2. TAMP Environment), p. 7 (6.3. Language-Table Environment), p. 8 (6.4. Mobile Manipulation Environment), p. 16 (Figure/Table caption), p. 9 (6.5. Performance on General Visual-Language Tasks), p. 18 (Figure/Table caption), baselines p. 6 (6. Experiments), p. 7 (6.2. TAMP Environment), p. 9 (6.5. Performance on General Visual-Language Tasks), p. 9 (Figure/Table caption), p. 16 (Figure/Table caption), p. 8 (6.4. Mobile Manipulation Environment), results p. 8 (Figure/Table caption), p. 9 (6.5. Performance on General Visual-Language Tasks), p. 6 (6. Experiments), p. 7 (6.2. TAMP Environment), p. 9 (7. Summary of Experiments & Discussion), p. 7 (6.3. Language-Table Environment).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (18 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Table 1: Comparison of different input representations on TAMP environment (in terms of success rates), where data from TAMP constitutes only 1% (i.e., 320 samples for p1, p2 each) of ... (p. 8, Figure/Table caption).
- **Metric evidence:** 7 (appendix) shows planning success rates and VQA performance for the TAMP environment. (p. 6, 6.2. TAMP Environment).
- **Baseline/ablation evidence:** As baselines, we consider the state-of-the art visual language model PaLI (Chen et al., 2022), which has not been trained on embodiment robot data, as well as the SayCan algorithm ... (p. 6, 6. Experiments).
- **Failure/negative evidence:** For the mobile manipulation and Language-Table environments, PaLM-E is integrated into the control loop to execute the plans in the real world, and has to adjust the plan in presence ... (p. 6, 6. Experiments).
