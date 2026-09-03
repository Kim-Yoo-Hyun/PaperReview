# Evaluation - DynaRend: Learning 3D Dynamics via Masked Future Rendering for Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (20 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=r4dzaP61QH; PDF retrieval source: https://arxiv.org/pdf/2510.24261. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments), p. 9 (4 Experiments), p. 8 (4 Experiments), p. 9 (4 Experiments)): Notably, compared to the baseline RVT [13] model, DynaRend achieves an average success rate improvement of 32.3%.

## Evaluation Body Digest

- **p. 6 / 4 Experiments - extractive body cue:** We conduct simulation experiments on two challenging robotic manipulation benchmarks: RLBench [21] and Colosseum [32].
- **p. 9 / 4 Experiments - extractive body cue:** We evaluate our method on five real-world robotic manipulation tasks and compare it against prior state-of-the-art approach.
- **p. 6 / 4 Experiments - extractive body cue:** Colosseum [32] is a benchmark for evaluating the generalization capabilities of manipulation policies under 12 types of environmental perturbations across 20 tasks, including changes in ...
- **p. 9 / 4 Experiments - extractive body cue:** For each task, we collect 30 expert demonstrations, with spatial configurations of objects randomized across episodes.
- **p. 7 / 4 Experiments - extractive body cue:** This highlights the efficiency and task-adaptiveness of DynaRend, making it practical for scalable deployment in real-world setups.
- **p. 7 / 4 Experiments - extractive body cue:** Moreover, unlike prior methods that rely on large-scale external pretraining datasets, our method is pretrained solely on task-relevant multi-view RGB-D data without additional external supervision.
- **p. 8 / 4 Experiments - extractive body cue:** We present the results on the Colosseum benchmark in Fig.
- **p. 14 / A Implementation Details - extractive body cue:** In both simulation and real-world experiments, we maintain fixed camera setups and viewpoints, with the view augmentation process described above applied consistently.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 4 Experiments (p. 6); A Implementation Details (p. 14); B Simulation Experiment Details (p. 15); C Real-world Experiment Details (p. 16).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | Notably, compared to the baseline RVT [13] model, DynaRend achieves an average success rate improvement of 32.3%. | p. 7 (4 Experiments) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our model achieves the best trade-off between success rate and inference speed when compared to other baseline methods, demonstrating strong manipulation performance without sacrificing ... | p. 7 (4 Experiments) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | Compared to existing 2D pretraining methods, such as MVP [43] and R3M [30], as well as 3D pretraining approaches like 3D-MVP [33], DynaRend achieves ... | p. 8 (4 Experiments) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | This leads to a noticeable improvement in downstream success rates, confirming the benefit of view diversity in supervision. | p. 9 (4 Experiments) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | The results indicate that pretraining consistently improves downstream policy performance, showcasing the effectiveness of the proposed pretraining strategy. | p. 8 (4 Experiments) |

## Dataset / Benchmark Role

- **p. 6 / 4 Experiments - extractive body cue:** We conduct simulation experiments on two challenging robotic manipulation benchmarks: RLBench [21] and Colosseum [32].
- **p. 9 / 4 Experiments - extractive body cue:** We evaluate our method on five real-world robotic manipulation tasks and compare it against prior state-of-the-art approach.
- **p. 6 / 4 Experiments - extractive body cue:** Colosseum [32] is a benchmark for evaluating the generalization capabilities of manipulation policies under 12 types of environmental perturbations across 20 tasks, including changes in ...
- **p. 9 / 4 Experiments - extractive body cue:** For each task, we collect 30 expert demonstrations, with spatial configurations of objects randomized across episodes.
- **p. 7 / 4 Experiments - extractive body cue:** This highlights the efficiency and task-adaptiveness of DynaRend, making it practical for scalable deployment in real-world setups.
- **p. 7 / 4 Experiments - extractive body cue:** Moreover, unlike prior methods that rely on large-scale external pretraining datasets, our method is pretrained solely on task-relevant multi-view RGB-D data without additional external supervision.
- **p. 8 / 4 Experiments - extractive body cue:** We present the results on the Colosseum benchmark in Fig.
- **p. 14 / A Implementation Details - extractive body cue:** In both simulation and real-world experiments, we maintain fixed camera setups and viewpoints, with the view augmentation process described above applied consistently.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: Comparison of representation learning paradigms for robot learning. (a) Learning predictive 2D representations [17] by forecasting future frames from the current observation to ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: DynaRend framework overview. (a) We reconstruct the point cloud from multi-view RGB-D inputs, encode it with an MLP, and project it onto three ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1: Evaluation results on 18 RLBench tasks. Each task is evaluated with 25 rollouts under 5 different seeds. We report the average success rate ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2: Results on 71 RLBench tasks. We further evaluate the scalability of our ap- proach on the larger 71-task RLBench set- ting, comparing DynaRend ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 4: Results on Colosseum. Ablation Avg. S.R.(%) ∆ DynaRend 83.2 - w/o. pretraining
- **p. 8 / Figure/Table caption - extractive body cue:** Table 3: Ablations. Average success rates are reported over RLBench 18 tasks to evaluate the impact of different design choices. Results on COLOSSEUM. We present ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 3: Ablation on mask ratio. Impact of mask ratio. Additionally, we perform an abla- tion study on the effect of the masking ratio applied ...
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 5: Real-world setup and task examples. We evaluate on five manipulation tasks: Put Item in Drawer, Close Pot, Stack Blocks, Sort Shape, Stack Cups. ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We conduct simulation experiments on two challenging robotic manipulation benchmarks: RLBench [21] and Colosseum [32]. | embodiment, simulator version and control stack | p. 6 (4 Experiments), p. 9 (4 Experiments) |
| Task/environment | We evaluate our method on five real-world robotic manipulation tasks and compare it against prior state-of-the-art approach. | reset, timeout, object/scene variation | p. 9 (4 Experiments), p. 6 (4 Experiments) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 3 (3 Methodology), p. 3 (3 Methodology) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 4 (3 Methodology), p. 4 (3 Methodology) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We report the average success rate and standard deviation for all tasks. policy architectures and pretraining strategies. | definition/direction/unit from same section | p. 7 (4 Experiments) |
| We report the average success rate across each perturbation category to assess the robustness of the policy to different types of environmental changes. | definition/direction/unit from same section | p. 6 (4 Experiments) |
| Our model achieves the best trade-off between success rate and inference speed when compared to other baseline methods, demonstrating strong manipulation performance without sacrificing ... | definition/direction/unit from same section | p. 7 (4 Experiments) |
| We evaluate the contribution of each loss term, including RGB reconstruction, semantic alignment, and depth supervision, by selectively enabling them and measuring the resulting ... | definition/direction/unit from same section | p. 8 (4 Experiments) |
| For both settings, each task is evaluated over 25 rollout episodes, and we report the average task success rate. | definition/direction/unit from same section | p. 6 (4 Experiments) |
| Average success rates are reported over RLBench 18 tasks to evaluate the impact of different design choices. | definition/direction/unit from same section | p. 8 (4 Experiments) |
| 4, we report the average success rates across the five real-world tasks. | definition/direction/unit from same section | p. 9 (4 Experiments) |
| This leads to a noticeable improvement in downstream success rates, confirming the benefit of view diversity in supervision. | definition/direction/unit from same section | p. 9 (4 Experiments) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Our model achieves the best trade-off between success rate and inference speed when compared to other baseline methods, demonstrating strong manipulation performance without sacrificing ... | comparison identity and matched condition | p. 7 (4 Experiments) |
| Notably, compared to the baseline RVT [13] model, DynaRend achieves an average success rate improvement of 32.3%. | comparison identity and matched condition | p. 7 (4 Experiments) |
| Additionally, when compared to the RVT baseline trained from scratch, DynaRend demonstrates significantly greater robustness to various types of environmental variations. | comparison identity and matched condition | p. 8 (4 Experiments) |
| Table 3: Ablations. Average success rates are reported over RLBench 18 tasks to evaluate the impact of different design choices. Results on COLOSSEUM. We ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| We compare the proposed method against various baselines across both benchmarks. | comparison identity and matched condition | p. 6 (4 Experiments) |
| The results show that our method consistently outperforms prior method. | comparison identity and matched condition | p. 9 (4 Experiments) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Additionally, we perform an ablation study on the effect of the masking ratio applied to the triplane features in Fig. | component/input/data sensitivity | p. 8 (4 Experiments) |
| Moreover, unlike prior methods that rely on large-scale external pretraining datasets, our method is pretrained solely on task-relevant multi-view RGB-D data without additional external ... | component/input/data sensitivity | p. 7 (4 Experiments) |
| We attribute these gains to the robust spatial and physical priors captured during the 3D-aware masked future rendering pretraining, which enables the policy to ... | component/input/data sensitivity | p. 8 (4 Experiments) |
| Incorporating synthetic views during pretraining helps mitigate overfitting to the limited camera viewpoints and encourages the model to learn more viewinvariant and robust 3D ... | component/input/data sensitivity | p. 9 (4 Experiments) |
| Even relative to RVT-2, a two-stage variant of RVT that incorporates additional refinement, our method still shows noticeable gains. | component/input/data sensitivity | p. 7 (4 Experiments) |
| We further conduct an ablation on the target view augmentation strategy, as shown in Tab. | component/input/data sensitivity | p. 9 (4 Experiments) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our contribution can be summarized as follows: • We propose DynaRend, a novel representation learning framework that learns generalizable triplane features via masked future ... | Notably, compared to the baseline RVT [13] model, DynaRend achieves an average success rate improvement of 32.3%. | PDF body cue; verify exact table/figure and matched conditions | p. 7 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments), p. 9 (4 Experiments), p. 8 (4 Experiments), p. 9 (4 Experiments) |
| Primary metric/result | Our model achieves the best trade-off between success rate and inference speed when compared to other baseline methods, demonstrating strong manipulation performance without sacrificing ... | numeric claim only at cited anchor | p. 7 (4 Experiments) |

- Numeric sentences retained from the body:
- **p. 6 / 4 Experiments - extractive body cue:** For both settings, each task is evaluated over 25 rollout episodes, and we report the average task success rate.
- **p. 6 / 4 Experiments - extractive body cue:** Colosseum [32] is a benchmark for evaluating the generalization capabilities of manipulation policies under 12 types of environmental perturbations across 20 tasks, including changes in ...
- **p. 6 / 4 Experiments - extractive body cue:** During test time, for each task, we separately apply each of the 12 perturbation types, and rollout 25 episodes per perturbation.
- **p. 7 / 4 Experiments - extractive body cue:** Each task is evaluated with 25 rollouts under 5 different seeds.
- **p. 7 / 4 Experiments - extractive body cue:** Specifically, we perform random translations along the x, y, and z axes by up to 0.125 m, and random rotations around the z-axis by up ...
- **p. 7 / 4 Experiments - extractive body cue:** Training is conducted using 8 NVIDIA RTX 3090 GPUs.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Notably, on tasks involving distractor objects, RVT-2 struggles to distinguish between different unseen items, leading to frequent failure cases. | p. 9 (4 Experiments) |
| body limitation/failure cue | To address this limitation, we leverage a pretrained visual-conditioned multi-view diffusion model to generate novel target views as additional supervision. | p. 14 (A Implementation Details) |
| body limitation/failure cue | We report the average success rate across each perturbation category to assess the robustness of the policy to different types of environmental changes. | p. 6 (4 Experiments) |
| body limitation/failure cue | Removing masking entirely or applying an excessively high mask ratio both lead to degraded performance. | p. 8 (4 Experiments) |
| body limitation/failure cue | Additionally, when compared to the RVT baseline trained from scratch, DynaRend demonstrates significantly greater robustness to various types of environmental variations. | p. 8 (4 Experiments) |
| body limitation/failure cue | In contrast, our method maintains robust performance, benefiting from the pretrained spatially grounded and semantically coherent representations. | p. 9 (4 Experiments) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Hyperparameter Value triplane resolution 16×16×16 transformer depth 8 transformer width 768 attention heads 12 MLP ratio 4.0 render head width 768 render head layers ... | p. 14 (A Implementation Details) |
| In both stages, we use a batch size of 256 and set the initial learning rate to 1 × 10-4 with cosine decay schedule. | p. 7 (4 Experiments) |
| Each task is evaluated with 25 rollouts under 5 different seeds. | p. 7 (4 Experiments) |
| The training hyperparameters are kept consistent with the simulation experiments. | p. 9 (4 Experiments) |
| We pretrain our model on the collected real-world dataset for 30k steps with augmented views and fine-tune it for an additional 10k steps. | p. 9 (4 Experiments) |
| We present the hyperparameters used in DynaRend as shown in Tab. | p. 14 (A Implementation Details) |
| The resulting point cloud is then encoded through an MLP to extract per-point features. | p. 4 (3 Methodology) |
| (c) For finetuning, two networks serve as a triplane encoder and are trained with an action decoder on demonstration data. | p. 4 (3 Methodology) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 9 / 4 Experiments - extractive body cue:** Notably, on tasks involving distractor objects, RVT-2 struggles to distinguish between different unseen items, leading to frequent failure cases.
- **p. 14 / A Implementation Details - extractive body cue:** To address this limitation, we leverage a pretrained visual-conditioned multi-view diffusion model to generate novel target views as additional supervision.
- **p. 6 / 4 Experiments - extractive body cue:** We report the average success rate across each perturbation category to assess the robustness of the policy to different types of environmental changes.
- **p. 8 / 4 Experiments - extractive body cue:** Removing masking entirely or applying an excessively high mask ratio both lead to degraded performance.
- **p. 8 / 4 Experiments - extractive body cue:** Additionally, when compared to the RVT baseline trained from scratch, DynaRend demonstrates significantly greater robustness to various types of environmental variations.
- **p. 9 / 4 Experiments - extractive body cue:** In contrast, our method maintains robust performance, benefiting from the pretrained spatially grounded and semantically coherent representations.

- **Evidence anchors reviewed:** datasets p. 6 (4 Experiments), p. 9 (4 Experiments), p. 6 (4 Experiments), p. 9 (4 Experiments), p. 7 (4 Experiments), p. 7 (4 Experiments), metrics p. 7 (4 Experiments), p. 6 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments), p. 6 (4 Experiments), p. 8 (4 Experiments), baselines p. 7 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments), p. 8 (Figure/Table caption), p. 6 (4 Experiments), p. 9 (4 Experiments), results p. 7 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments), p. 9 (4 Experiments), p. 8 (4 Experiments), p. 9 (4 Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
