# Evaluation - Data Scaling Laws in Imitation Learning for Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (34 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=pISLZG7ktL; PDF retrieval source: https://arxiv.org/pdf/2410.18647. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 4 (3 APPROACH), p. 1 (ABSTRACT), p. 2 (1 INTRODUCTION), p. 9 (32 Env-Object Pairs), p. 8 (Figure/Table caption), p. 9 (32 Env-Object Pairs)): To further enhance performance, we make two improvements: (1) DINOv2 visual encoder: In our experiments, fine-tuning the DINOv2 ViT (Oquab et al., 2023) outperforms both ImageNet pre-trained ResNet (He et ...

## Evaluation Body Digest

- **p. 4 / 3 APPROACH - extractive body cue:** Existing robotic manipulation datasets do not provide enough environments and objects for a single task to meet our requirements.
- **p. 4 / 3 APPROACH - extractive body cue:** For simplicity, we consider a scenario where a demonstration dataset for a manipulation task is collected across M environments (E1, E2, . . . , ...
- **p. 1 / ABSTRACT - extractive body cue:** Throughout our research, we collect over 40,000 demonstrations and execute more than 15,000 real-world robot rollouts under a rigorous evaluation protocol.
- **p. 5 / 3 APPROACH - extractive body cue:** Finally, to minimize the tester's subjective bias, we simultaneously evaluate multiple policies trained on datasets of different sizes; each rollout is randomly selected from these ...
- **p. 1 / ABSTRACT - extractive body cue:** In this paper, we investigate whether similar data scaling laws exist in robotics, particularly in robotic manipulation, and whether appropriate data scaling can yield single-task ...
- **p. 10 / 32 Env-Object Pairs - extractive body cue:** We conduct experiments on Pour Water, using data collected from 32 environment-object pairs and selecting 50% of all valid demonstrations as the training set.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** We begin by focusing on two tasks as case studies-Pour Water and Mouse Arrangement-to thoroughly analyze how policy generalization changes with the number of environments, ...
- **p. 3 / 3 APPROACH - extractive body cue:** This generalization issue manifests across two dimensions: (1) Environment-generalization to previously unseen environments, which may involve variations in lighting conditions, distractor objects, background changes, and ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** demonstration으로 정의된 robot task distribution.
- **Input boundary:** observation history와 expert trajectory/action.
- **Output/decision under evaluation:** predicted action 또는 action chunk.
- **Primary target:** imitation error, task success, robustness와 compounding error.
- **Detected evaluation headings:** not reliably recovered.

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 3 APPROACH | EMPIRICAL / REAL-ROBOT OR HARDWARE | To further enhance performance, we make two improvements: (1) DINOv2 visual encoder: In our experiments, fine-tuning the DINOv2 ViT (Oquab et al., 2023) outperforms ... | p. 4 (3 APPROACH) |
| ABSTRACT | EMPIRICAL / REAL-ROBOT OR HARDWARE | With four data collectors working for one afternoon, we collect sufficient data to enable the policies for two tasks to achieve approximately 90% success ... | p. 1 (ABSTRACT) |
| 1 INTRODUCTION | EMPIRICAL / REAL-ROBOT OR HARDWARE | We apply this strategy to two new tasks (Fold Towels and Unplug Charger), and within a single afternoon using four data collectors, we collect ... | p. 2 (1 INTRODUCTION) |
| 32 Env-Object Pairs | EMPIRICAL / REAL-ROBOT OR HARDWARE | As the table indicates, our policies achieve around 90% success rates across all four tasks-the two from previous experiments and the two new ones. | p. 9 (32 Env-Object Pairs) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 6: Multiple objects per environment. Brighter colors indicate higher normalized scores. How to select the number of environments and objects? Previously, we consider ... | p. 8 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 4 / 3 APPROACH - extractive body cue:** Existing robotic manipulation datasets do not provide enough environments and objects for a single task to meet our requirements.
- **p. 4 / 3 APPROACH - extractive body cue:** For simplicity, we consider a scenario where a demonstration dataset for a manipulation task is collected across M environments (E1, E2, . . . , ...
- **p. 1 / ABSTRACT - extractive body cue:** Throughout our research, we collect over 40,000 demonstrations and execute more than 15,000 real-world robot rollouts under a rigorous evaluation protocol.
- **p. 5 / 3 APPROACH - extractive body cue:** Finally, to minimize the tester's subjective bias, we simultaneously evaluate multiple policies trained on datasets of different sizes; each rollout is randomly selected from these ...
- **p. 1 / ABSTRACT - extractive body cue:** In this paper, we investigate whether similar data scaling laws exist in robotics, particularly in robotic manipulation, and whether appropriate data scaling can yield single-task ...
- **p. 10 / 32 Env-Object Pairs - extractive body cue:** We conduct experiments on Pour Water, using data collected from 32 environment-object pairs and selecting 50% of all valid demonstrations as the training set.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** We begin by focusing on two tasks as case studies-Pour Water and Mouse Arrangement-to thoroughly analyze how policy generalization changes with the number of environments, ...
- **p. 3 / 3 APPROACH - extractive body cue:** This generalization issue manifests across two dimensions: (1) Environment-generalization to previously unseen environments, which may involve variations in lighting conditions, distractor objects, background changes, and ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: Illustrations of all tasks. We derive the data scaling laws through extensive experiments on Pour Water and Mouse Arrangement, and further validate these ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 2: Object generalization. Each curve corresponds to a different fraction of demonstrations used, with normalized scores shown as a function of the number of ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3: Environment generalization. Each curve corresponds to a different fraction of demon- strations used, with normalized scores shown as a function of the number ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4: Generlization across environments and objects. Each curve corresponds to a different fraction of demonstrations used, with normalized scores shown as a function of ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5: Power-law relationship. Dashed lines represent power-law fits, with the equations pro- vided in the legend. All axes are shown on a logarithmic scale. ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 6: Multiple objects per environment. Brighter colors indicate higher normalized scores. How to select the number of environments and objects? Previously, we consider only ...
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 7: Number of demonstrations. Left: In the setting where we collect the maximum number of demonstrations, we examine whether the policy's performance follows a ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 1: Success rate across all tasks. We report the average success rate and standard deviation across 8 unseen environments. The performance in each environment ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Existing robotic manipulation datasets do not provide enough environments and objects for a single task to meet our requirements. | embodiment, simulator version and control stack | p. 4 (3 APPROACH), p. 4 (3 APPROACH) |
| Task/environment | For simplicity, we consider a scenario where a demonstration dataset for a manipulation task is collected across M environments (E1, E2, . . . ... | reset, timeout, object/scene variation | p. 4 (3 APPROACH), p. 1 (ABSTRACT) |
| Observation/sensor | observation history와 expert trajectory/action | calibration, preprocessing, privileged input | p. 5 (3 APPROACH), p. 4 (3 APPROACH) |
| Output/decision | predicted action 또는 action chunk | action frame, controller and termination | p. 4 (3 APPROACH), p. 5 (3 APPROACH) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| The results, shown in Table 1, report both the policy's normalized score and the corresponding success rate (for the definition of success criteria, see ... | definition/direction/unit from same section | p. 9 (32 Env-Object Pairs) |
| 5 VERIFICATION OF DATA COLLECTION STRATEGY Pour Water Mouse Arrangement Fold Towels Unplug Charger Score 0.922 ± 0.075 0.933 ± 0.088 0.95 ± 0.062 ... | definition/direction/unit from same section | p. 9 (32 Env-Object Pairs) |
| Figure 20: Data scaling laws on MSE. Dashed lines represent power-law fits, with the equations provided in the legend. All axes are shown on ... | definition/direction/unit from same section | p. 30 (Figure/Table caption) |
| With four data collectors working for one afternoon, we collect sufficient data to enable the policies for two tasks to achieve approximately 90% success ... | definition/direction/unit from same section | p. 1 (ABSTRACT) |
| Collecting data in as many environments as possible (e.g., 32 environments), each with one unique manipulation object and 50 demonstrations, allows training a policy ... | definition/direction/unit from same section | p. 2 (1 INTRODUCTION) |
| We apply this strategy to two new tasks (Fold Towels and Unplug Charger), and within a single afternoon using four data collectors, we collect ... | definition/direction/unit from same section | p. 2 (1 INTRODUCTION) |
| Unlike the commonly used success rate-which is an overly sparse signal lacking the granularity to distinguish between policies-our scoring mechanism captures more nuanced behaviors. | definition/direction/unit from same section | p. 4 (3 APPROACH) |
| Table 12: Success rate across all tasks. For each task, we report the success rate in each evaluation environment. 34 | definition/direction/unit from same section | p. 34 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| To further enhance performance, we make two improvements: (1) DINOv2 visual encoder: In our experiments, fine-tuning the DINOv2 ViT (Oquab et al., 2023) outperforms ... | comparison identity and matched condition | p. 4 (3 APPROACH) |
| 3, we observe that when the number of environments or objects is small, increasing the number of environments results in smaller performance gains compared ... | comparison identity and matched condition | p. 6 (3 APPROACH) |
| This indicates that, compared to changing either the environment or the object alone, simultaneously changing both increases data diversity, leading to more efficient policy ... | comparison identity and matched condition | p. 6 (3 APPROACH) |
| For instance, special lighting setups might be used to change only the color of illumination, or 3D-printed objects might be designed to vary only ... | comparison identity and matched condition | p. 3 (3 APPROACH) |
| Finally, to minimize the tester's subjective bias, we simultaneously evaluate multiple policies trained on datasets of different sizes; each rollout is randomly selected from ... | comparison identity and matched condition | p. 5 (3 APPROACH) |
| The main question we seek to answer is: for a given manipulation task, how can we optimally select M, N, and K to ensure ... | comparison identity and matched condition | p. 8 (3 APPROACH) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 2: Model related experiments on Pour Water. The entries marked in gray are the same, which specify the default settings: the visual encoder ... | component/input/data sensitivity | p. 10 (Figure/Table caption) |
| Throughout all experiments, we also analyze the effect of demonstration quantity (Sec. | component/input/data sensitivity | p. 5 (3 APPROACH) |
| To explore the effect of the number of training environments on generalization, we use the same manipulation object across 32 distinct environments, collecting 120 ... | component/input/data sensitivity | p. 5 (3 APPROACH) |
| For instance, special lighting setups might be used to change only the color of illumination, or 3D-printed objects might be designed to vary only ... | component/input/data sensitivity | p. 3 (3 APPROACH) |
| The main question we seek to answer is: for a given manipulation task, how can we optimally select M, N, and K to ensure ... | component/input/data sensitivity | p. 8 (3 APPROACH) |
| Both pretraining and full fine-tuning are indispensable. | component/input/data sensitivity | p. 10 (32 Env-Object Pairs) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To answer this, we present a comprehensive empirical study on data scaling in imitation learning, which is a predominant method for learning real-world manipulation ... | To further enhance performance, we make two improvements: (1) DINOv2 visual encoder: In our experiments, fine-tuning the DINOv2 ViT (Oquab et al., 2023) outperforms ... | PDF body cue; verify exact table/figure and matched conditions | p. 4 (3 APPROACH), p. 1 (ABSTRACT), p. 2 (1 INTRODUCTION), p. 9 (32 Env-Object Pairs), p. 8 (Figure/Table caption), p. 9 (32 Env-Object Pairs) |
| Primary metric/result | With four data collectors working for one afternoon, we collect sufficient data to enable the policies for two tasks to achieve approximately 90% success ... | numeric claim only at cited anchor | p. 1 (ABSTRACT) |

- Numeric sentences retained from the body:
- **p. 4 / 3 APPROACH - extractive body cue:** Each step can receive a maximum of 3 points, and we report a normalized score, defined as Normalized score = Total test score 3×Number of ...
- **p. 5 / 3 APPROACH - extractive body cue:** Furthermore, to examine how policy performance varies with the number of demonstrations, we randomly sample 2n fractions of valid demonstrations (n = 0, -1, -2, ...
- **p. 5 / 3 APPROACH - extractive body cue:** In total, 21 policies are trained, and each is evaluated using 8 unseen objects in the same environment as the training data, with 5 trials ...
- **p. 5 / 3 APPROACH - extractive body cue:** The average normalized score across 40 trials is reported for each policy.
- **p. 5 / 3 APPROACH - extractive body cue:** For example, in Pour Water, when training with 8 objects, the performance using 12.5% of the demonstrations significantly lags behind that using 100% of the ...
- **p. 5 / 3 APPROACH - extractive body cue:** We randomly select 2m environments (m = 0, 1, 2, 3, 4, 5) from the 32 available for training, and for each selected environment, we ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | 7 DISCUSSION, LIMITATIONS, & FUTURE WORKS Data scaling is an exciting and ongoing event in robotics. | p. 10 (32 Env-Object Pairs) |
| body limitation/failure cue | While this approach allows precise control over individual factors, it cannot account for all possible variation factors. | p. 3 (3 APPROACH) |
| body limitation/failure cue | Our work has several limitations that future research can address. | p. 10 (32 Env-Object Pairs) |
| body limitation/failure cue | To ensure model capacity does not become a bottleneck when scaling data, we utilize a sufficiently large model, ViT-Large/14 (Dosovitskiy et al., 2020). | p. 4 (3 APPROACH) |
| body limitation/failure cue | Based on all the results, we summarize the following data scaling laws: 1Although we recognize the irreducible errors Y∞associated with scaling the data alone, ... | p. 7 (3 APPROACH) |
| body limitation/failure cue | We leave the verification of this prediction for future work. | p. 8 (3 APPROACH) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| In this paper, we explore the first dimension of scaling-data-as scaling data is a prerequisite for scaling models and compute. | p. 1 (1 INTRODUCTION) |
| Data scaling has revolutionized fields like natural language processing and computer vision, providing models with remarkable generalization capabilities. | p. 1 (ABSTRACT) |
| Each manipulation task is divided into several stages or steps (typically 2-3), each with well-defined scoring criteria (see Appendix D). | p. 4 (3 APPROACH) |
| Each step can receive a maximum of 3 points, and we report a normalized score, defined as Normalized score = Total test score 3×Number ... | p. 4 (3 APPROACH) |
| The average normalized score across 40 trials is reported for each policy. | p. 5 (3 APPROACH) |
| See Appendix E.2 for an example of the evaluation workflow and Appendix F for the hardware setup. | p. 5 (3 APPROACH) |
| Each policy is evaluated in 8 unseen environments, using two unseen objects per environment, with 5 trials per environment. | p. 6 (3 APPROACH) |
| Scaling visual encoder yields a consistent performance boost. | p. 10 (32 Env-Object Pairs) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 10 / 32 Env-Object Pairs - extractive body cue:** 7 DISCUSSION, LIMITATIONS, & FUTURE WORKS Data scaling is an exciting and ongoing event in robotics.
- **p. 3 / 3 APPROACH - extractive body cue:** While this approach allows precise control over individual factors, it cannot account for all possible variation factors.
- **p. 10 / 32 Env-Object Pairs - extractive body cue:** Our work has several limitations that future research can address.
- **p. 4 / 3 APPROACH - extractive body cue:** To ensure model capacity does not become a bottleneck when scaling data, we utilize a sufficiently large model, ViT-Large/14 (Dosovitskiy et al., 2020).
- **p. 7 / 3 APPROACH - extractive body cue:** Based on all the results, we summarize the following data scaling laws: 1Although we recognize the irreducible errors Y∞associated with scaling the data alone, fitting ...
- **p. 8 / 3 APPROACH - extractive body cue:** We leave the verification of this prediction for future work.

- **Evidence anchors reviewed:** datasets p. 4 (3 APPROACH), p. 4 (3 APPROACH), p. 1 (ABSTRACT), p. 5 (3 APPROACH), p. 1 (ABSTRACT), p. 10 (32 Env-Object Pairs), metrics p. 9 (32 Env-Object Pairs), p. 9 (32 Env-Object Pairs), p. 30 (Figure/Table caption), p. 1 (ABSTRACT), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), baselines p. 4 (3 APPROACH), p. 6 (3 APPROACH), p. 6 (3 APPROACH), p. 3 (3 APPROACH), p. 5 (3 APPROACH), p. 8 (3 APPROACH), results p. 4 (3 APPROACH), p. 1 (ABSTRACT), p. 2 (1 INTRODUCTION), p. 9 (32 Env-Object Pairs), p. 8 (Figure/Table caption), p. 9 (32 Env-Object Pairs).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
