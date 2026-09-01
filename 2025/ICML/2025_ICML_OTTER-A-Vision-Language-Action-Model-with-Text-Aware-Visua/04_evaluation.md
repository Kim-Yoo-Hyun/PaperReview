# Evaluation - OTTER: A Vision-Language-Action Model with Text-Aware Visual Feature Extraction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=UHF0km7R5M; PDF retrieval source: https://openreview.net/pdf/7fad0feb536c6adfcc1f93202cc2a447ee101254.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (4.2. Baselines), p. 7 (Figure/Table caption), p. 6 (5.1. Real-world Experiments), p. 7 (5.1. Real-world Experiments), p. 5 (4.1. Environment Setup), p. 8 (Figure/Table caption)): OTTER achieves a similar success rate on the in-distribution training tasks and unseen tasks, significantly outperforming the baselines, highlighting the benefits of extracting text-aware visual features and a frozen pre-trained ...

## Evaluation Body Digest

- **p. 5 / 4.1. Environment Setup - extractive PDF cue:** We collect robotic datasets on multi-task scenes using a Franka robot, where there are multiple tasks that can be completed in the same scene.
- **p. 6 / 5.1. Real-world Experiments - extractive PDF cue:** This enables better visual grounding and generalization capabilities of OTTER to perform better on training and unseen tasks, despite being trained on a small robotic ...
- **p. 7 / 5.1. Real-world Experiments - extractive PDF cue:** The results further suggest that OTTER's generalization capabilities can be enhanced through increased model capacity (OTTER-L) and pre-training on large robotic datasets (OTTER-OXE). on unseen ...
- **p. 2 / 3. Empirical results suggest that OTTER's performance - extractive PDF cue:** on unseen tasks scales along multiple axes: through larger pre-trained vision-language encoders, increased policy network capacity, and pre-training on larger robot datasets.
- **p. 5 / 4.1. Environment Setup - extractive PDF cue:** The training tasks involve objects encountered during model training, whereas the unseen tasks test the model's ability to generalize to unseen objects or scenes.
- **p. 6 / 5.1. Real-world Experiments - extractive PDF cue:** Single Primitive We first evaluate all models on both the training and unseen tasks of the pick and place primitive in the real robot environment, ...
- **p. 7 / 5.2. Simulation Experiments - extractive PDF cue:** From Table 3, we found all the models perform similarly on training tasks in LIBERO due to the limited variations of the tasks and sufficient ...
- **p. 5 / 4.1. Environment Setup - extractive PDF cue:** The overall performance is measured by calculating the average success rate with standard error across all trials for the training and unseen tasks.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 3. Empirical results suggest that OTTER's performance (p. 2); 4. Experiments (p. 5); 5. Results (p. 6); 5.1. Real-world Experiments (p. 6); 5.2. Simulation Experiments (p. 7).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.2. Baselines | EMPIRICAL / REAL-ROBOT OR HARDWARE | OTTER achieves a similar success rate on the in-distribution training tasks and unseen tasks, significantly outperforming the baselines, highlighting the benefits of extracting text-aware ... | p. 6 (4.2. Baselines) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 2: Multi-primitive zero-shot generalization: We train models across four manipulation primitives (pouring, drawer manipulation, poking, and pick-and-place) with a total of 1,185 human ... | p. 7 (Figure/Table caption) |
| 5.1. Real-world Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | For unseen pick up and place tasks, π0-Fast-Droid is able to achieve a success rate of 61%. | p. 6 (5.1. Real-world Experiments) |
| 5.1. Real-world Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | Finetuned π0-Fast-Droid achieves non-zero success rate on Drawer and Poking primitives, but still fails on the pouring primitive. | p. 7 (5.1. Real-world Experiments) |
| 4.1. Environment Setup | EMPIRICAL / REAL-ROBOT OR HARDWARE | The overall performance is measured by calculating the average success rate with standard error across all trials for the training and unseen tasks. | p. 5 (4.1. Environment Setup) |

## Dataset / Benchmark Role

- **p. 5 / 4.1. Environment Setup - extractive PDF cue:** We collect robotic datasets on multi-task scenes using a Franka robot, where there are multiple tasks that can be completed in the same scene.
- **p. 6 / 5.1. Real-world Experiments - extractive PDF cue:** This enables better visual grounding and generalization capabilities of OTTER to perform better on training and unseen tasks, despite being trained on a small robotic ...
- **p. 7 / 5.1. Real-world Experiments - extractive PDF cue:** The results further suggest that OTTER's generalization capabilities can be enhanced through increased model capacity (OTTER-L) and pre-training on large robotic datasets (OTTER-OXE). on unseen ...
- **p. 2 / 3. Empirical results suggest that OTTER's performance - extractive PDF cue:** on unseen tasks scales along multiple axes: through larger pre-trained vision-language encoders, increased policy network capacity, and pre-training on larger robot datasets.
- **p. 5 / 4.1. Environment Setup - extractive PDF cue:** The training tasks involve objects encountered during model training, whereas the unseen tasks test the model's ability to generalize to unseen objects or scenes.
- **p. 6 / 5.1. Real-world Experiments - extractive PDF cue:** Single Primitive We first evaluate all models on both the training and unseen tasks of the pick and place primitive in the real robot environment, ...
- **p. 7 / 5.2. Simulation Experiments - extractive PDF cue:** From Table 3, we found all the models perform similarly on training tasks in LIBERO due to the limited variations of the tasks and sufficient ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1: (Top) Different feature extraction approaches in VLA models. (a) Direct Feature Passing: existing approaches, exem- plified by Octo and OpenVLA, extract and pass ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 2: OTTER Model architecture. At each timestep t, text- aware visual features fvl are extracted from a pre-trained CLIP model (see Figure 3). Then ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 3: Text-aware Visual Features Extraction We calcu- late the similarity between the visual patch features and per-token language features, then take the softmax over ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 4: Example scenes in the simulation (left) and in the physical environments (right) using a Franka robot. to the proprioception representation, we express the ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 1: Physical Single Primitive Multi-task Experiments. For each model, we conduct physical robot pick and place exper- iments, with 100 trials on in-distribution training ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 2: Multi-primitive zero-shot generalization: We train models across four manipulation primitives (pouring, drawer manipulation, poking, and pick-and-place) with a total of 1,185 human tele-operated ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 3: Simulation results on LIBERO. We evaluate OTTER and other baselines on 30 in-distribution tasks in LIBERO- Spatial/Object/Goal and on 10 unseen tasks we ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 4: Ablation results on LIBERO Object tasks and unseen tasks. We evaluate OTTER and other baselines on 100 trials of in- distribution LIBERO-Object tasks, ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We collect robotic datasets on multi-task scenes using a Franka robot, where there are multiple tasks that can be completed in the same scene. | embodiment, simulator version and control stack | p. 5 (4.1. Environment Setup), p. 6 (5.1. Real-world Experiments) |
| Task/environment | This enables better visual grounding and generalization capabilities of OTTER to perform better on training and unseen tasks, despite being trained on a small ... | reset, timeout, object/scene variation | p. 6 (5.1. Real-world Experiments), p. 7 (5.1. Real-world Experiments) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 1 (1. Introduction), p. 4 (3.2. Model Architecture) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 3 (3. Method), p. 1 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| The overall performance is measured by calculating the average success rate with standard error across all trials for the training and unseen tasks. | definition/direction/unit from same section | p. 5 (4.1. Environment Setup) |
| While baseline models struggle with generalization, particularly on pouring task (0% success rate), OTTER maintains substantial performance (60-93% success rate) on unseen tasks. | definition/direction/unit from same section | p. 7 (5.1. Real-world Experiments) |
| For unseen pick up and place tasks, π0-Fast-Droid is able to achieve a success rate of 61%. | definition/direction/unit from same section | p. 6 (5.1. Real-world Experiments) |
| In both the training and unseen tasks, Octo struggles to accurately identify the object of interest and determine the correct placement location, leading to ... | definition/direction/unit from same section | p. 6 (5.1. Real-world Experiments) |
| Finetuned π0-Fast-Droid achieves non-zero success rate on Drawer and Poking primitives, but still fails on the pouring primitive. | definition/direction/unit from same section | p. 7 (5.1. Real-world Experiments) |
| Figure 1: (Top) Different feature extraction approaches in VLA models. (a) Direct Feature Passing: existing approaches, exem- plified by Octo and OpenVLA, extract and ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Table 6: The 10 in-distribution tasks and 7 unseen tasks we used in our real-world setting. For each experiment trial of poking and pouring, ... | definition/direction/unit from same section | p. 12 (Figure/Table caption) |
| We consider a task with unseen target objects for task completion as an unseen task. | definition/direction/unit from same section | p. 5 (4.1. Environment Setup) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Table 3: Simulation results on LIBERO. We evaluate OTTER and other baselines on 30 in-distribution tasks in LIBERO- Spatial/Object/Goal and on 10 unseen tasks ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| To evaluate if the text-aware visual features extracted in OTTER can better leverage the semantic understanding capabilities of the pre-trained VLMs, we consider four ... | comparison identity and matched condition | p. 5 (4.2. Baselines) |
| OTTER achieves a similar success rate on the in-distribution training tasks and unseen tasks, significantly outperforming the baselines, highlighting the benefits of extracting text-aware ... | comparison identity and matched condition | p. 6 (4.2. Baselines) |
| Despite the inherent difficulty of zero-shot generalization across multiple primitives, OTTER achieves significantly higher success rates compared to baselines across all primitives. | comparison identity and matched condition | p. 7 (5.1. Real-world Experiments) |
| In unseen tasks, OTTER can outperform other baselines by a large margin, demonstrating its generalization capabilities to novel scenarios, which is consistent with the ... | comparison identity and matched condition | p. 7 (5.2. Simulation Experiments) |
| We introduce our experimental setup to evaluate the instruction-following and text-aware visual features extraction generalization of OTTER in Section 4.1 and the baselines considered ... | comparison identity and matched condition | p. 5 (4. Experiments) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 3: Simulation results on LIBERO. We evaluate OTTER and other baselines on 30 in-distribution tasks in LIBERO- Spatial/Object/Goal and on 10 unseen tasks ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| Figure 7: Examples of attention maps of frozen CLIP's attention features (Xattn) on Open-X dataset. The bottom texts are the corresponding text tokens. D. ... | component/input/data sensitivity | p. 15 (Figure/Table caption) |
| To evaluate if the text-aware visual features extracted in OTTER can better leverage the semantic understanding capabilities of the pre-trained VLMs, we consider four ... | component/input/data sensitivity | p. 5 (4.2. Baselines) |
| Direct Feature Passing OTTER (DFP-OTTER): a variant of OTTER where the text tokens, vision tokens are passed to an attention pooling layer separately to ... | component/input/data sensitivity | p. 6 (4.2. Baselines) |
| Addition ablation studies can be found in Appendix D. | component/input/data sensitivity | p. 7 (5.3. Ablations) |
| We consider the following ablations on the design choices of OTTER. | component/input/data sensitivity | p. 7 (5.3. Ablations) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To this end, we propose OTTER, a novel VLA architecture that freezes pre-trained vision and language encoders and extracts taskrelevant visual features guided by ... | OTTER achieves a similar success rate on the in-distribution training tasks and unseen tasks, significantly outperforming the baselines, highlighting the benefits of extracting text-aware ... | PDF body cue; verify exact table/figure and matched conditions | p. 6 (4.2. Baselines), p. 7 (Figure/Table caption), p. 6 (5.1. Real-world Experiments), p. 7 (5.1. Real-world Experiments), p. 5 (4.1. Environment Setup), p. 8 (Figure/Table caption) |
| Primary metric/result | Table 2: Multi-primitive zero-shot generalization: We train models across four manipulation primitives (pouring, drawer manipulation, poking, and pick-and-place) with a total of 1,185 human ... | numeric claim only at cited anchor | p. 7 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 5 / 4.1. Environment Setup - extractive PDF cue:** The in-distribution tasks are the 30 tasks in the original LIBERO-Spatial/Object/Goal, which can evaluate the model's multi-task learning capabilities.
- **p. 6 / 4.2. Baselines - extractive PDF cue:** For each model, we conduct physical robot pick and place experiments, with 100 trials on in-distribution training tasks and 70 trials on unseen tasks.
- **p. 7 / 5.1. Real-world Experiments - extractive PDF cue:** Err. π0-Fast-Droid 0% 0% 0% 61% 29% ± 3.5% Finetuned π0-Fast-Droid 0% 45% 27% 51% 35% ± 3.8% Finetuned Octo 0% 0% 0% 5% 4% ...
- **p. 7 / 5.1. Real-world Experiments - extractive PDF cue:** The results further suggest that OTTER's generalization capabilities can be enhanced through increased model capacity (OTTER-L) and pre-training on large robotic datasets (OTTER-OXE). on unseen ...
- **p. 7 / 5.2. Simulation Experiments - extractive PDF cue:** For the unseen tasks, we change 10 tasks in LIBERO-90 with different objects and distractors to test the generalizability of all the models on unseen ...
- **p. 4 / 3.2. Model Architecture - extractive PDF cue:** Policy Network and Action Head OTTER uses a transformer as the policy network, consisting of 4 layers and 8 heads, with a hidden dimension of ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | As OpenVLA has many tokens per timestep, its context length cannot be extended and we use its default context length. | p. 6 (5.1. Real-world Experiments) |
| body limitation/failure cue | For a fair comparison, we extended the context history length of Octo to 10 (Octo cannot exceed a context length of 10 due to ... | p. 6 (5.1. Real-world Experiments) |
| body limitation/failure cue | Finetuned π0-Fast-Droid achieves non-zero success rate on Drawer and Poking primitives, but still fails on the pouring primitive. | p. 7 (5.1. Real-world Experiments) |
| body limitation/failure cue | While π0-Fast-Droid achieves decent performance on the pick and place primitives, it fails on all the other three primitives as the majority of the ... | p. 7 (5.1. Real-world Experiments) |
| body limitation/failure cue | Table 6: The 10 in-distribution tasks and 7 unseen tasks we used in our real-world setting. For each experiment trial of poking and pouring, ... | p. 12 (Figure/Table caption) |
| body limitation/failure cue | This suggests that pretrained VLM provides more robust and transferable visual representations. | p. 8 (2. OTTER w.o. f ′) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| For each task, we evaluate the model for 10 experiment trials. | p. 5 (4.1. Environment Setup) |
| The trial is terminated either when the task is completed or when a time limit is reached. | p. 5 (4.1. Environment Setup) |
| For fair comparisons, we fine-tune Octo and OpenVLA on DS-PnP using the same amount of learning steps. | p. 6 (5.1. Real-world Experiments) |
| For each model, we conduct physical robot pick and place experiments, with 100 trials on in-distribution training tasks and 70 trials on unseen tasks. | p. 6 (4.2. Baselines) |
| The results further suggest that OTTER's generalization capabilities can be enhanced through increased model capacity (OTTER-L) and pre-training on large robotic datasets (OTTER-OXE). on ... | p. 7 (5.1. Real-world Experiments) |
| Err. π0-Fast-Droid 0% 0% 0% 61% 29% ± 3.5% Finetuned π0-Fast-Droid 0% 45% 27% 51% 35% ± 3.8% Finetuned Octo 0% 0% 0% 5% ... | p. 7 (5.1. Real-world Experiments) |
| on unseen tasks scales along multiple axes: through larger pre-trained vision-language encoders, increased policy network capacity, and pre-training on larger robot datasets. | p. 2 (3. Empirical results suggest that OTTER's performance) |
| In OTTER, we extract text per-token features from CLIP's language encoder fl (m tokens). | p. 3 (3.1. Text-Aware Visual Feature Extraction) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / 5.1. Real-world Experiments - extractive PDF cue:** As OpenVLA has many tokens per timestep, its context length cannot be extended and we use its default context length.
- **p. 6 / 5.1. Real-world Experiments - extractive PDF cue:** For a fair comparison, we extended the context history length of Octo to 10 (Octo cannot exceed a context length of 10 due to its ...
- **p. 7 / 5.1. Real-world Experiments - extractive PDF cue:** Finetuned π0-Fast-Droid achieves non-zero success rate on Drawer and Poking primitives, but still fails on the pouring primitive.
- **p. 7 / 5.1. Real-world Experiments - extractive PDF cue:** While π0-Fast-Droid achieves decent performance on the pick and place primitives, it fails on all the other three primitives as the majority of the Droid ...
- **p. 12 / Figure/Table caption - extractive PDF cue:** Table 6: The 10 in-distribution tasks and 7 unseen tasks we used in our real-world setting. For each experiment trial of poking and pouring, we ...
- **p. 8 / 2. OTTER w.o. f ′ - extractive PDF cue:** This suggests that pretrained VLM provides more robust and transferable visual representations.

- **PDF anchors reviewed:** datasets p. 5 (4.1. Environment Setup), p. 6 (5.1. Real-world Experiments), p. 7 (5.1. Real-world Experiments), p. 2 (3. Empirical results suggest that OTTER's performance), p. 5 (4.1. Environment Setup), p. 6 (5.1. Real-world Experiments), metrics p. 5 (4.1. Environment Setup), p. 7 (5.1. Real-world Experiments), p. 6 (5.1. Real-world Experiments), p. 6 (5.1. Real-world Experiments), p. 7 (5.1. Real-world Experiments), p. 1 (Figure/Table caption), baselines p. 8 (Figure/Table caption), p. 5 (4.2. Baselines), p. 6 (4.2. Baselines), p. 7 (5.1. Real-world Experiments), p. 7 (5.2. Simulation Experiments), p. 5 (4. Experiments), results p. 6 (4.2. Baselines), p. 7 (Figure/Table caption), p. 6 (5.1. Real-world Experiments), p. 7 (5.1. Real-world Experiments), p. 5 (4.1. Environment Setup), p. 8 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
