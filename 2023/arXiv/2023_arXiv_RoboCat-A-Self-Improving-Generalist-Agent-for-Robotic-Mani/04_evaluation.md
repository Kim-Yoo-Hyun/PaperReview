# Evaluation - RoboCat: A Self-Improving Generalist Agent for Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (60 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2306.11706; PDF retrieval source: https://arxiv.org/pdf/2306.11706. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 17 (5 Experiments), p. 13 (5 Experiments), p. 10 (Figure/Table caption), p. 55 (Figure/Table caption), p. 13 (5 Experiments), p. 45 (Figure/Table caption)): The results in Figure 10 show that the self-improved agent outperforms the baseline agent in all four of these tasks.

## Evaluation Body Digest

- **p. 13 / 5 Experiments - extractive PDF cue:** All three methods were evaluated on the same Sawyer robots with identical conditions, evaluation protocol, and successful episodes visually counted. this is even more apparent ...
- **p. 15 / 5 Experiments - extractive PDF cue:** This trend of positive transfer also holds when adapting to new real-world 2 The Gato model was fine-tuned with additional simulation episodes of the task, ...
- **p. 15 / 5 Experiments - extractive PDF cue:** Overall, we show that RoboCat-lim adapts with only 100-500 episodes to a broad set of downstream tasks, including unseen variations and objects, different data sources ...
- **p. 11 / 4.3 Evaluation - extractive PDF cue:** This comparison also demonstrates the utility of robotics data in the case of RoboCat, versus vision datasets for the VFM baselines, when adapting to robotics ...
- **p. 11 / 4.3 Evaluation - extractive PDF cue:** We compare RoboCat with Gato on the robotics tasks used in their work, namely the RGB-Stacking Benchmark (Lee et al., 2021), and fine-tuning to blue-on-green ...
- **p. 12 / 5 Experiments - extractive PDF cue:** RoboCat is able to fine-tune to tasks that not only include previously unseen task families (e.g. fruit insertion into a bowl), but also new object ...
- **p. 14 / 5 Experiments - extractive PDF cue:** RoboCat-lim can be effectively fine-tuned, given a limited number of demonstrations, to tasks that are novel in terms of objects or task variants, and even ...
- **p. 12 / 5 Experiments - extractive PDF cue:** In the real world, where we have limited data compared to simulation, RoboCat can take advantage of multi-task joint training on robotics data to perform ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** multi-robot demonstration/dataset ecosystem.
- **Input boundary:** multi-view observation, language/task label과 action trajectory.
- **Output/decision under evaluation:** dataset sample 또는 learned policy action.
- **Primary target:** coverage, cross-embodiment transfer, data efficiency와 task success.
- **Detected evaluation headings:** 4.3 Evaluation (p. 11); 5 Experiments (p. 11).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 5 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | The results in Figure 10 show that the self-improved agent outperforms the baseline agent in all four of these tasks. | p. 17 (5 Experiments) |
| 5 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | We see from Figure 5(a) that the performance of this smaller model is comparable to RoboCat on the stacking tasks, but significantly lower for ... | p. 13 (5 Experiments) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 1: Final RoboCat performance on evaluation tasks. This table lists the tasks used for training and fine-tuning of the final RoboCat agent, and ... | p. 10 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 24: RoboCat vs training data: Panda 7-DoF YCB lifting tasks (self-improvement, real). This plot compares the performance of RoboCat on the self-improvement tasks ... | p. 55 (Figure/Table caption) |
| 5 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | All three methods were evaluated on the same Sawyer robots with identical conditions, evaluation protocol, and successful episodes visually counted. this is even more ... | p. 13 (5 Experiments) |

## Dataset / Benchmark Role

- **p. 13 / 5 Experiments - extractive PDF cue:** All three methods were evaluated on the same Sawyer robots with identical conditions, evaluation protocol, and successful episodes visually counted. this is even more apparent ...
- **p. 15 / 5 Experiments - extractive PDF cue:** This trend of positive transfer also holds when adapting to new real-world 2 The Gato model was fine-tuned with additional simulation episodes of the task, ...
- **p. 15 / 5 Experiments - extractive PDF cue:** Overall, we show that RoboCat-lim adapts with only 100-500 episodes to a broad set of downstream tasks, including unseen variations and objects, different data sources ...
- **p. 11 / 4.3 Evaluation - extractive PDF cue:** This comparison also demonstrates the utility of robotics data in the case of RoboCat, versus vision datasets for the VFM baselines, when adapting to robotics ...
- **p. 11 / 4.3 Evaluation - extractive PDF cue:** We compare RoboCat with Gato on the robotics tasks used in their work, namely the RGB-Stacking Benchmark (Lee et al., 2021), and fine-tuning to blue-on-green ...
- **p. 12 / 5 Experiments - extractive PDF cue:** RoboCat is able to fine-tune to tasks that not only include previously unseen task families (e.g. fruit insertion into a bowl), but also new object ...
- **p. 14 / 5 Experiments - extractive PDF cue:** RoboCat-lim can be effectively fine-tuned, given a limited number of demonstrations, to tasks that are novel in terms of objects or task variants, and even ...
- **p. 12 / 5 Experiments - extractive PDF cue:** In the real world, where we have limited data compared to simulation, RoboCat can take advantage of multi-task joint training on robotics data to perform ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 1: The self-improvement process. RoboCat is a multi-task, multi-embodiment visual goal-conditioned agent that can iteratively self-improve. A diverse training set is used to train ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 2: RoboCat supports multiple robotic embodiments and control modes. These are all the different embodiments RoboCat is tested on, and the dimensionality of the ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 3: The real-world object sets used by RoboCat. The first two object sets are used to systematically study structure-building and insertion affordances, respectively. The ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 4: Example goal images. These images correspond to a subset of the embodiments, task families, and object sets used by RoboCat. The first two ...
- **p. 10 / Figure/Table caption - extractive PDF cue:** Table 1: Final RoboCat performance on evaluation tasks. This table lists the tasks used for training and fine-tuning of the final RoboCat agent, and highlights ...
- **p. 12 / Figure/Table caption - extractive PDF cue:** Figure 5: RoboCat compared to VFM baselines on training tasks. RoboCat performs better on the vast majority of training tasks, compared to single-task baseline agents ...
- **p. 13 / Figure/Table caption - extractive PDF cue:** Figure 6: RoboCat fine-tuning compared to VFM baselines. RoboCat efficiently adapts to each of these pre- viously unseen tasks which include unseen object sets and ...
- **p. 13 / Figure/Table caption - extractive PDF cue:** Table 2: RGB Stacking Mastery Benchmark. RoboCat performs, on average, similarly to prior works BC- IMP (Lee et al., 2021) and Gato (Reed et al., ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | All three methods were evaluated on the same Sawyer robots with identical conditions, evaluation protocol, and successful episodes visually counted. this is even more ... | embodiment, simulator version and control stack | p. 13 (5 Experiments), p. 15 (5 Experiments) |
| Task/environment | This trend of positive transfer also holds when adapting to new real-world 2 The Gato model was fine-tuned with additional simulation episodes of the ... | reset, timeout, object/scene variation | p. 15 (5 Experiments), p. 15 (5 Experiments) |
| Observation/sensor | multi-view observation, language/task label과 action trajectory | calibration, preprocessing, privileged input | p. 2 (1 Introduction), p. 3 (1 Introduction) |
| Output/decision | dataset sample 또는 learned policy action | action frame, controller and termination | p. 7 (1 Introduction), p. 4 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| (Section 5.3) 5.1 Overall RoboCat performance We evaluated RoboCat over all the training tasks and we report task success rates averaged within each embodiment, ... | definition/direction/unit from same section | p. 12 (5 Experiments) |
| We see from Figure 5(a) that the performance of this smaller model is comparable to RoboCat on the stacking tasks, but significantly lower for ... | definition/direction/unit from same section | p. 13 (5 Experiments) |
| Figure 24: RoboCat vs training data: Panda 7-DoF YCB lifting tasks (self-improvement, real). This plot compares the performance of RoboCat on the self-improvement tasks ... | definition/direction/unit from same section | p. 55 (Figure/Table caption) |
| Although the relative success rates vary per object triplet, RoboCat is comparable to prior methods on average on this benchmark, despite being able to ... | definition/direction/unit from same section | p. 14 (5 Experiments) |
| Table 1: Final RoboCat performance on evaluation tasks. This table lists the tasks used for training and fine-tuning of the final RoboCat agent, and ... | definition/direction/unit from same section | p. 10 (Figure/Table caption) |
| Figure 19: Tokenisation and obs prediction ablations on the red_on_green generalisation problem. Unless otherwise specified, we use a vocabulary size of 4096 and image ... | definition/direction/unit from same section | p. 45 (Figure/Table caption) |
| Table 15: Per-task RoboCat performance on training and fine-tuning tasks. This table expands Table 1 by providing the success rate for each task variant ... | definition/direction/unit from same section | p. 52 (Figure/Table caption) |
| Figure 20: RoboCat vs experts performance: Panda 7-DoF structure-building training tasks (sim). RoboCat performance compared to the success rate of the training data for ... | definition/direction/unit from same section | p. 53 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Figure 5: RoboCat compared to VFM baselines on training tasks. RoboCat performs better on the vast majority of training tasks, compared to single-task baseline ... | comparison identity and matched condition | p. 12 (Figure/Table caption) |
| Table 2: RGB Stacking Mastery Benchmark. RoboCat performs, on average, similarly to prior works BC- IMP (Lee et al., 2021) and Gato (Reed et ... | comparison identity and matched condition | p. 13 (Figure/Table caption) |
| Published in Transactions on Machine Learning Research (12/2023) 0% 25% 50% 75% 100% Sawyer 7-DoF RGB stacking (single task) Panda 7-DoF RGB stacking (single ... | comparison identity and matched condition | p. 12 (5 Experiments) |
| Indeed, the full 1.18B RoboCat model can outperform the single-task baselines with only 3-6 times the capacity, despite being trained on 250 tasks. | comparison identity and matched condition | p. 13 (5 Experiments) |
| Published in Transactions on Machine Learning Research (12/2023) 0% 25% 50% 75% 100% Perceptual variation: Sim Sawyer 7-DoF RGB stacking (blue on green) Perceptual ... | comparison identity and matched condition | p. 16 (5 Experiments) |
| The results in Figure 10 show that the self-improved agent outperforms the baseline agent in all four of these tasks. | comparison identity and matched condition | p. 17 (5 Experiments) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 3: RoboCat-lim fine-tuning using different sources of data. Despite RoboCat-lim only being trained on agent data originally, the model can be fine-tuned with ... | component/input/data sensitivity | p. 15 (Figure/Table caption) |
| RoboCat-lim can be effectively fine-tuned, given a limited number of demonstrations, to tasks that are novel in terms of objects or task variants, and ... | component/input/data sensitivity | p. 14 (5 Experiments) |
| However, the model is effective at fine-tuning to this task variant with as little as 100 demonstrations. | component/input/data sensitivity | p. 15 (5 Experiments) |
| For each comparison, the VFM models are trained with the same behavioural cloning loss and the same successful episodes that the RoboCat model uses ... | component/input/data sensitivity | p. 11 (4.3 Evaluation) |
| Published in Transactions on Machine Learning Research (12/2023) 0% 25% 50% 75% 100% Sawyer 7-DoF RGB stacking (single task) Panda 7-DoF RGB stacking (single ... | component/input/data sensitivity | p. 12 (5 Experiments) |
| The results here are for single task variants, unlike the results in Figure 7(c). | component/input/data sensitivity | p. 16 (5 Experiments) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our main contributions in this work are outlined below: (1) we demonstrate, for the first time, that a large transformer sequence model can solve ... | The results in Figure 10 show that the self-improved agent outperforms the baseline agent in all four of these tasks. | PDF body cue; verify exact table/figure and matched conditions | p. 17 (5 Experiments), p. 13 (5 Experiments), p. 10 (Figure/Table caption), p. 55 (Figure/Table caption), p. 13 (5 Experiments), p. 45 (Figure/Table caption) |
| Primary metric/result | We see from Figure 5(a) that the performance of this smaller model is comparable to RoboCat on the stacking tasks, but significantly lower for ... | numeric claim only at cited anchor | p. 13 (5 Experiments) |

- Numeric sentences retained from the body:
- **p. 11 / 4.3 Evaluation - extractive PDF cue:** For each of the simulated and real tasks, we evaluate each model by averaging over 100 episodes (or more, if specified), using a different goal ...
- **p. 11 / 4.3 Evaluation - extractive PDF cue:** To address this in a systematic and reproducible way, we employ the following evaluation protocol for each task: we first evaluate the checkpoint every 5000 ...
- **p. 13 / 5 Experiments - extractive PDF cue:** Indeed, the full 1.18B RoboCat model can outperform the single-task baselines with only 3-6 times the capacity, despite being trained on 250 tasks.
- **p. 15 / 5 Experiments - extractive PDF cue:** Published in Transactions on Machine Learning Research (12/2023) Data Source Task Success 100 episodes 500 episodes Expert agent data 63% 84% Demonstration data 82% 88% ...
- **p. 15 / 5 Experiments - extractive PDF cue:** Overall, we show that RoboCat-lim adapts with only 100-500 episodes to a broad set of downstream tasks, including unseen variations and objects, different data sources ...
- **p. 7 / 1 Introduction - extractive PDF cue:** 3 Tasks and Data (a) RGB objects (b) NIST-i gears and base (c) YCB fruit, YCB-i vegetables, bowl (d) Shape-matching objects Figure 3: The real-world ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | While visual goal specification already allows the agent to learn from failures and sub-optimal data, incorporating RL would enable both learning with rewards and ... | p. 20 (6 Related Work) |
| body limitation/failure cue | Table 8: Quantities of human demonstrations and self-generated data. Embodiment Task Family Object Set Variant Human teleop demos Successes Failures | p. 38 (Figure/Table caption) |
| body limitation/failure cue | Table 20: Skill transfer analysis. Average accumulated error over all three NIST-i gear sizes. Moving from the 364M model to the full RoboCat agent ... | p. 60 (Figure/Table caption) |
| body limitation/failure cue | Figure 27: The different types of NIST-i based environments we ablate performance against. Note, in the main paper we report performance against environments from ... | p. 56 (Figure/Table caption) |
| body limitation/failure cue | In simulation, RoboCat-lim generalises 0-shot to a held-out object set on the Sawyer (third plot from the left) and the blue-on-green stacking task variant ... | p. 15 (5 Experiments) |
| body limitation/failure cue | As we are primarily concerned with goal images as task specification in a behaviour cloning setting, this work does not address the question of ... | p. 19 (6 Related Work) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| To address this in a systematic and reproducible way, we employ the following evaluation protocol for each task: we first evaluate the checkpoint every ... | p. 11 (4.3 Evaluation) |
| When fine-tuning a generalist to a specific real-world task, it can be difficult to determine the optimal number of fine-tuning steps, since there is ... | p. 11 (4.3 Evaluation) |
| RoboCat is based on the Gato architecture with a VQ-GAN encoder (Esser et al., 2021) pretrained on a broad set of images; this choice ... | p. 2 (1 Introduction) |
| We specify tasks via visual goal-conditioning, which has the desirable property that any image in a trajectory can be labelled as a valid "hindsight ... | p. 2 (1 Introduction) |
| The encoded vectors are discretised via a nearest neighbour lookup in a codebook of quantised embeddings. | p. 4 (1 Introduction) |
| We pretrain our VQ-GAN encoder on a diverse collection of images as we find this improves generalisation. | p. 4 (1 Introduction) |
| Specifically, we predict image tokens k = 5 time steps into the future as images one step apart can look very similar. | p. 5 (1 Introduction) |
| While Gato only predicted actions, we find that, when a VQ-GAN is used, performance is improved by additionally training for predicting future image tokens ... | p. 5 (1 Introduction) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 20 / 6 Related Work - extractive PDF cue:** While visual goal specification already allows the agent to learn from failures and sub-optimal data, incorporating RL would enable both learning with rewards and learning ...
- **p. 38 / Figure/Table caption - extractive PDF cue:** Table 8: Quantities of human demonstrations and self-generated data. Embodiment Task Family Object Set Variant Human teleop demos Successes Failures
- **p. 60 / Figure/Table caption - extractive PDF cue:** Table 20: Skill transfer analysis. Average accumulated error over all three NIST-i gear sizes. Moving from the 364M model to the full RoboCat agent eliminates ...
- **p. 56 / Figure/Table caption - extractive PDF cue:** Figure 27: The different types of NIST-i based environments we ablate performance against. Note, in the main paper we report performance against environments from (a) ...
- **p. 15 / 5 Experiments - extractive PDF cue:** In simulation, RoboCat-lim generalises 0-shot to a held-out object set on the Sawyer (third plot from the left) and the blue-on-green stacking task variant on ...
- **p. 19 / 6 Related Work - extractive PDF cue:** As we are primarily concerned with goal images as task specification in a behaviour cloning setting, this work does not address the question of goal ...

- **PDF anchors reviewed:** datasets p. 13 (5 Experiments), p. 15 (5 Experiments), p. 15 (5 Experiments), p. 11 (4.3 Evaluation), p. 11 (4.3 Evaluation), p. 12 (5 Experiments), metrics p. 12 (5 Experiments), p. 13 (5 Experiments), p. 55 (Figure/Table caption), p. 14 (5 Experiments), p. 10 (Figure/Table caption), p. 45 (Figure/Table caption), baselines p. 12 (Figure/Table caption), p. 13 (Figure/Table caption), p. 12 (5 Experiments), p. 13 (5 Experiments), p. 16 (5 Experiments), p. 17 (5 Experiments), results p. 17 (5 Experiments), p. 13 (5 Experiments), p. 10 (Figure/Table caption), p. 55 (Figure/Table caption), p. 13 (5 Experiments), p. 45 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
