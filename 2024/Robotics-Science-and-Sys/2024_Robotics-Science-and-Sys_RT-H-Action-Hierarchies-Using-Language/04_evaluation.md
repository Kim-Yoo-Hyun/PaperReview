# Evaluation - RT-H: Action Hierarchies Using Language

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (23 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss20/p049.html; PDF retrieval source: https://www.roboticsproceedings.org/rss20/p049.html. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (Figure/Table caption), p. 9 (Figure/Table caption), p. 9 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS)): Fig. 3: Results on Diverse+Kitchen multi-task dataset, consisting of eight challenging evaluation tasks. 95% Wilson Score confidence intervals [54] are shown on the average success rates (left). RT-H outperforms RT-2 ...

## Evaluation Body Digest

- **p. 10 / V. EXPERIMENTS - extractive body cue:** We use RT-H trained on only the Kitchen dataset [6] unless otherwise noted (i.e., not including the Diverse data), which consists of the following training ...
- **p. 5 / V. EXPERIMENTS - extractive body cue:** Dataset: We utilize a large multi-task dataset consisting of 100K demonstrations with randomized object poses and backgrounds.
- **p. 5 / V. EXPERIMENTS - extractive body cue:** To comprehensively evaluate the performance of RT-H, we study four key experimental questions: • Q1 (Performance): Do action hierarchies with language improve policy performance on ...
- **p. 6 / V. EXPERIMENTS - extractive body cue:** • Kitchen: The dataset used in RT-1 [6] and RT-2 [4], consisting of 6 semantic task categories in 70K demonstrations. • Diverse: A new dataset ...
- **p. 7 / V. EXPERIMENTS - extractive body cue:** Finally, in Section V-D we test the robustness of RT-H to variations in scenes, objects, and tasks (Q4).
- **p. 7 / V. EXPERIMENTS - extractive body cue:** Train Dataset Eval Dataset RT-2 RT-H-Joint RT-H RT-H (GT) Kitchen Kitchen 30.2 28.22 24.9 17.9 D+K Diverse 27.7 25.44 23.6 17.8 TABLE I: Best checkpoint ...
- **p. 8 / V. EXPERIMENTS - extractive body cue:** 4: Examples showing how language motions depend on the context of the scene and task, taken from online evaluations of RTH trained on the Diverse+Kitchen ...
- **p. 10 / V. EXPERIMENTS - extractive body cue:** Generalization To evaluate Q4, we study three types of generalization: generalization to new scenes (with similar objects but new backgrounds and lighting), to novel objects, ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** V. EXPERIMENTS (p. 5).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Fig. 3: Results on Diverse+Kitchen multi-task dataset, consisting of eight challenging evaluation tasks. 95% Wilson Score confidence intervals [54] are shown on the average ... | p. 6 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Fig. 6: Results for Corrections on models trained on the Diverse+Kitchen multi-task dataset, for the same eight evaluation tasks as in Fig. 3. 95% ... | p. 9 (Figure/Table caption) |
| V. EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | RT-H-InterveneAction also improves upon RT-H, outperforming it by 9% on average. | p. 9 (V. EXPERIMENTS) |
| V. EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | To comprehensively evaluate the performance of RT-H, we study four key experimental questions: • Q1 (Performance): Do action hierarchies with language improve policy performance ... | p. 5 (V. EXPERIMENTS) |
| V. EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | In Section V-C, we collect and train on language motion corrections on top of RT-H, demonstrating that training on language motion corrections improves policy ... | p. 7 (V. EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 10 / V. EXPERIMENTS - extractive body cue:** We use RT-H trained on only the Kitchen dataset [6] unless otherwise noted (i.e., not including the Diverse data), which consists of the following training ...
- **p. 5 / V. EXPERIMENTS - extractive body cue:** Dataset: We utilize a large multi-task dataset consisting of 100K demonstrations with randomized object poses and backgrounds.
- **p. 5 / V. EXPERIMENTS - extractive body cue:** To comprehensively evaluate the performance of RT-H, we study four key experimental questions: • Q1 (Performance): Do action hierarchies with language improve policy performance on ...
- **p. 6 / V. EXPERIMENTS - extractive body cue:** • Kitchen: The dataset used in RT-1 [6] and RT-2 [4], consisting of 6 semantic task categories in 70K demonstrations. • Diverse: A new dataset ...
- **p. 7 / V. EXPERIMENTS - extractive body cue:** Finally, in Section V-D we test the robustness of RT-H to variations in scenes, objects, and tasks (Q4).
- **p. 7 / V. EXPERIMENTS - extractive body cue:** Train Dataset Eval Dataset RT-2 RT-H-Joint RT-H RT-H (GT) Kitchen Kitchen 30.2 28.22 24.9 17.9 D+K Diverse 27.7 25.44 23.6 17.8 TABLE I: Best checkpoint ...
- **p. 8 / V. EXPERIMENTS - extractive body cue:** 4: Examples showing how language motions depend on the context of the scene and task, taken from online evaluations of RTH trained on the Diverse+Kitchen ...
- **p. 10 / V. EXPERIMENTS - extractive body cue:** Generalization To evaluate Q4, we study three types of generalization: generalization to new scenes (with similar objects but new backgrounds and lighting), to novel objects, ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: Given a task in language like "close the pistachio jar" and an image of the scene, RT-H utilizes a Vision Language Model (VLM) ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 2: RT-H Overview. Left: Our method leverages language to create an action hierarchy for policy learning. We separate the action prediction problem into a ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 3: Results on Diverse+Kitchen multi-task dataset, consisting of eight challenging evaluation tasks. 95% Wilson Score confidence intervals [54] are shown on the average success ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 4: Examples showing how language motions depend on the context of the scene and task, taken from online evaluations of RT- H trained on ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 5: Examples of the flexibility of learned language motions. In the top row (a) we correct RT-H using two different task-completing language motions for ...
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 6: Results for Corrections on models trained on the Diverse+Kitchen multi-task dataset, for the same eight evaluation tasks as in Fig. 3. 95% Wilson ...
- **p. 11 / Figure/Table caption - extractive body cue:** Fig. 7: Results when models trained on Kitchen data [6] are deployed on the same tasks, but in a new building with novel backgrounds, lighting, ...
- **p. 12 / Figure/Table caption - extractive body cue:** Fig. 8: We show the generalization capabilities of RT-H with completely unseen tasks with minimal correction. By breaking down tasks into language motions, RT-H learns ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We use RT-H trained on only the Kitchen dataset [6] unless otherwise noted (i.e., not including the Diverse data), which consists of the following ... | embodiment, simulator version and control stack | p. 10 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS) |
| Task/environment | Dataset: We utilize a large multi-task dataset consisting of 100K demonstrations with randomized object poses and backgrounds. | reset, timeout, object/scene variation | p. 5 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 1 (Abstract), p. 1 (Abstract) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| 95% Wilson Score confidence intervals [54] are shown on the average success rates (left). | definition/direction/unit from same section | p. 6 (V. EXPERIMENTS) |
| See Appendix D for the success rates for each stage of each task, where we see that RT-H makes more progress towards success in ... | definition/direction/unit from same section | p. 7 (V. EXPERIMENTS) |
| See Appendix D for quantitative analysis of contextuality and a qualitative look at language motion multimodality in RT-H, along with staged success rates for ... | definition/direction/unit from same section | p. 8 (V. EXPERIMENTS) |
| First, we see how amenable RT-H is to language motion corrections with RT-H + Human Intervention, which gets very high success rates even for ... | definition/direction/unit from same section | p. 9 (V. EXPERIMENTS) |
| Of course, the base policy for RT-2 performs worse than Diverse+Kitchen on these tasks than RT-H, so to ensure a fair comparison we focus ... | definition/direction/unit from same section | p. 9 (V. EXPERIMENTS) |
| Overall, we see that language motion corrections bring the average success rates of RT-H from 40% to 63% with just 30 episodes of correction ... | definition/direction/unit from same section | p. 10 (V. EXPERIMENTS) |
| Fig. 10: Open Pistachio Jar: Cumulative success rates for each method. | definition/direction/unit from same section | p. 20 (Figure/Table caption) |
| Fig. 9: Place Bowl Upright on Counter: Cumulative success rates for each method. | definition/direction/unit from same section | p. 20 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Fig. 7: Results when models trained on Kitchen data [6] are deployed on the same tasks, but in a new building with novel backgrounds, ... | comparison identity and matched condition | p. 11 (Figure/Table caption) |
| Training on Online Corrections In this section we are interested in how well RT-H can learn from language motion corrections compared to methods without ... | comparison identity and matched condition | p. 8 (V. EXPERIMENTS) |
| RT-H outperforms RT-2 by 15% on average, getting higher performance on 6/8 of the tasks. | comparison identity and matched condition | p. 6 (V. EXPERIMENTS) |
| We discuss this in Section V-C. • RT-2-IWR is the interactive version of RT-2, which is additionally trained with human interventions in the form ... | comparison identity and matched condition | p. 6 (V. EXPERIMENTS) |
| RT-H outperforms RT-2 on most of the tasks, surpassing RT-2 by 15% on average, which strongly supports the benefit of action hierarchies (Q1), despite ... | comparison identity and matched condition | p. 7 (V. EXPERIMENTS) |
| RT-H and RT-H-Joint achieve lower MSE on both datasets compared to RT-2, illustrating the benefits of action hierarchies for ingesting multi-task datasets compared to ... | comparison identity and matched condition | p. 7 (V. EXPERIMENTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Offline Performance: We investigate if language motions as an intermediate layer for action prediction has any noticeable effect by comparing the offline validation mean ... | component/input/data sensitivity | p. 7 (V. EXPERIMENTS) |
| RTH-Cluster replaces the automating labeling procedure with action clustering, and without language it performs slightly worse than RT-H on average. | component/input/data sensitivity | p. 7 (V. EXPERIMENTS) |
| See Appendix A for exact queries and a deeper dive into each RT-H variant implementation. | component/input/data sensitivity | p. 6 (V. EXPERIMENTS) |
| Note that RT-H-Joint, RT-H-Cluster, and RT-H-OneHot are variants of RT-H that still utilize an action hierarchy. | component/input/data sensitivity | p. 6 (V. EXPERIMENTS) |
| Training on Online Corrections In this section we are interested in how well RT-H can learn from language motion corrections compared to methods without ... | component/input/data sensitivity | p. 8 (V. EXPERIMENTS) |
| 8 also shows the shared structure between seemingly diverse tasks: each of these tasks require some picking behavior to begin the task, and by ... | component/input/data sensitivity | p. 10 (V. EXPERIMENTS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Motivated by the benefits of language motions, we propose an end-to-end framework, RT-H (Robot Transformer with Action Hierarchies), for learning these action hierarchies: at ... | Fig. 3: Results on Diverse+Kitchen multi-task dataset, consisting of eight challenging evaluation tasks. 95% Wilson Score confidence intervals [54] are shown on the average ... | PDF body cue; verify exact table/figure and matched conditions | p. 6 (Figure/Table caption), p. 9 (Figure/Table caption), p. 9 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS) |
| Primary metric/result | Fig. 6: Results for Corrections on models trained on the Diverse+Kitchen multi-task dataset, for the same eight evaluation tasks as in Fig. 3. 95% ... | numeric claim only at cited anchor | p. 9 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 7 / V. EXPERIMENTS - extractive body cue:** See Appendix D for the success rates for each stage of each task, where we see that RT-H makes more progress towards success in 7/8 ...
- **p. 7 / V. EXPERIMENTS - extractive body cue:** Furthermore, whereas RT-2 achieves nonzero performance on only 4/8 tasks, RT-H is nonzero on 6/8 tasks and RT-H-Joint is nonzero on all the tasks, suggesting ...
- **p. 9 / V. EXPERIMENTS - extractive body cue:** RT-H-Intervene and RT-H-InterveneAction: We collect 30 episodes (failed episodes filtered out) of language motion corrections for each of the eight tasks, using the correction procedure ...
- **p. 9 / V. EXPERIMENTS - extractive body cue:** RT-2-IWR: We collect 30 episodes (failed episodes filtered out) of teleoperated corrections for the same eight tasks, using VR-based teleoperation instead of language motion corrections.
- **p. 10 / V. EXPERIMENTS - extractive body cue:** Overall, we see that language motion corrections bring the average success rates of RT-H from 40% to 63% with just 30 episodes of correction per ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Fig. 1: Given a task in language like "close the pistachio jar" and an image of the scene, RT-H utilizes a Vision Language Model ... | p. 1 (Figure/Table caption) |
| body limitation/failure cue | The oatmeal example also highlights how language motion corrections can make the policy's behavior interpretable and thus more intuitive to debug - more effectively ... | p. 9 (V. EXPERIMENTS) |
| body limitation/failure cue | Since we only care about learning to correct the failure modes of RT-2, we must use RT-2 trained on the Diverse+Kitchen dataset (same as ... | p. 9 (V. EXPERIMENTS) |
| body limitation/failure cue | This failure mode rarely happens for in-distribution tasks, but as tasks diverge from the data distribution, it becomes more likely. | p. 10 (V. EXPERIMENTS) |
| body limitation/failure cue | Failure Modes: RT-H demonstrates performance boosts on a wide variety of tasks, however the action hierarchy paradigm does lead to interesting failure modes. | p. 10 (V. EXPERIMENTS) |
| body limitation/failure cue | Fig. 8: We show the generalization capabilities of RT-H with completely unseen tasks with minimal correction. By breaking down tasks into language motions, RT-H ... | p. 12 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Checkpoints are chosen using validation action MSE, and then run for 10 controlled trials for each task (80 total trials per method). | p. 7 (V. EXPERIMENTS) |
| See Appendix A for exact queries and a deeper dive into each RT-H variant implementation. | p. 6 (V. EXPERIMENTS) |
| More specifically, RT-H passes the language motion to the Encoder in the action query, while RT-H-Joint treats the language motion as a Decoder input ... | p. 6 (V. EXPERIMENTS) |
| In Table I, we report the minimum MSE across training checkpoints for RT-H, RT-H-Joint, and RT-2 when trained on either the Diverse+Kitchen dataset or ... | p. 7 (V. EXPERIMENTS) |
| The advantage of language in these settings is to encode the shared structure between similar tasks (e.g., "pick coke can" vs. "pick an apple"), ... | p. 2 (I. INTRODUCTION) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: Given a task in language like "close the pistachio jar" and an image of the scene, RT-H utilizes a Vision Language Model (VLM) ...
- **p. 9 / V. EXPERIMENTS - extractive body cue:** The oatmeal example also highlights how language motion corrections can make the policy's behavior interpretable and thus more intuitive to debug - more effectively allowing ...
- **p. 9 / V. EXPERIMENTS - extractive body cue:** Since we only care about learning to correct the failure modes of RT-2, we must use RT-2 trained on the Diverse+Kitchen dataset (same as RT-H-Intervene) ...
- **p. 10 / V. EXPERIMENTS - extractive body cue:** This failure mode rarely happens for in-distribution tasks, but as tasks diverge from the data distribution, it becomes more likely.
- **p. 10 / V. EXPERIMENTS - extractive body cue:** Failure Modes: RT-H demonstrates performance boosts on a wide variety of tasks, however the action hierarchy paradigm does lead to interesting failure modes.
- **p. 12 / Figure/Table caption - extractive body cue:** Fig. 8: We show the generalization capabilities of RT-H with completely unseen tasks with minimal correction. By breaking down tasks into language motions, RT-H learns ...

- **Evidence anchors reviewed:** datasets p. 10 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), metrics p. 6 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 8 (V. EXPERIMENTS), p. 9 (V. EXPERIMENTS), p. 9 (V. EXPERIMENTS), p. 10 (V. EXPERIMENTS), baselines p. 11 (Figure/Table caption), p. 8 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), results p. 6 (Figure/Table caption), p. 9 (Figure/Table caption), p. 9 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (23 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Fig. 3: Results on Diverse+Kitchen multi-task dataset, consisting of eight challenging evaluation tasks. 95% Wilson Score confidence intervals [54] are shown on the average success rates (left). RT-H outperforms RT-2 ... (p. 6, Figure/Table caption).
- **Metric evidence:** 95% Wilson Score confidence intervals [54] are shown on the average success rates (left). (p. 6, V. EXPERIMENTS).
- **Baseline/ablation evidence:** Training on Online Corrections In this section we are interested in how well RT-H can learn from language motion corrections compared to methods without action hierarchy that use teleoperated correction ... (p. 8, V. EXPERIMENTS).
- **Failure/negative evidence:** RT-2-IWR: We collect 30 episodes (failed episodes filtered out) of teleoperated corrections for the same eight tasks, using VR-based teleoperation instead of language motion corrections. (p. 9, V. EXPERIMENTS).
