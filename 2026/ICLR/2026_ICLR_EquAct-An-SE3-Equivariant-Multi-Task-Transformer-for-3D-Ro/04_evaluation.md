# Evaluation - EquAct: An SE(3)-Equivariant Multi-Task Transformer for 3D Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=d1wuA8oIH0; PDF retrieval source: https://openreview.net/pdf/7d1ac63392c225113c314e6263f1d18dfbff895e.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (5 Experiments), p. 9 (5 Experiments), p. 7 (5 Experiments), p. 9 (5 Experiments), p. 8 (5 Experiments), p. 7 (5 Experiments)): On average, EquAct outperforms all the baselines on all 3 settings. avg. success rate ↑ open drawer slide block sweep dust. meat off grill Method 10∗ 10 100 10∗ 10 ...

## Evaluation Body Digest

- **p. 8 / 5 Experiments - extractive body cue:** In the 10 SE(3) setting, the training set contains 10 demo per task and both the training and testing scenes have randomly SE(3) initialized objects.
- **p. 7 / 5 Experiments - extractive body cue:** The benchmark uses a Franka Panda robot equipped with a parallel gripper.
- **p. 9 / 5 Experiments - extractive body cue:** 5.2 Physical experiments Table 2: Physical experiments. avg. disass. pluck pick install SR ↑ pipe flower fruit toilet roll Var × Demo 3 × 10 ...
- **p. 7 / 5 Experiments - extractive body cue:** We benchmark multi-task algorithms on 18 RLBench [52, 25] tasks.
- **p. 9 / 5 Experiments - extractive body cue:** We evaluate 10 episodes for each task and report the binary success rate.
- **p. 8 / 5 Experiments - extractive body cue:** 10* denotes 10 demonstrations per task with random SE(3) objects poses.
- **p. 7 / 5 Experiments - extractive body cue:** Performance is measured by a binary reward, where 0% and 100% correspond to failure and successful completion of the task according to the natural language ...
- **p. 7 / 5 Experiments - extractive body cue:** We report the task success rate over 25 evaluation episodes per task, with a maximum of 25 steps per episode.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 5 Experiments (p. 7).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 5 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | On average, EquAct outperforms all the baselines on all 3 settings. avg. success rate ↑ open drawer slide block sweep dust. meat off grill ... | p. 8 (5 Experiments) |
| 5 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | Finally, aug. →no aug. indicates using data augmentation can further improve performance, we hypothesize that data augmentation reduces numerical error in the equivariant neural ... | p. 9 (5 Experiments) |
| 5 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | We report the task success rate over 25 evaluation episodes per task, with a maximum of 25 steps per episode. | p. 7 (5 Experiments) |
| 5 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | We evaluate 10 episodes for each task and report the binary success rate. | p. 9 (5 Experiments) |
| 5 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | Furthermore, the more difficult the setting is, the more EquAct outperforms the baselines, demonstrating strong sample efficiency and 3D generalization. | p. 8 (5 Experiments) |

## Dataset / Benchmark Role

- **p. 8 / 5 Experiments - extractive body cue:** In the 10 SE(3) setting, the training set contains 10 demo per task and both the training and testing scenes have randomly SE(3) initialized objects.
- **p. 7 / 5 Experiments - extractive body cue:** The benchmark uses a Franka Panda robot equipped with a parallel gripper.
- **p. 9 / 5 Experiments - extractive body cue:** 5.2 Physical experiments Table 2: Physical experiments. avg. disass. pluck pick install SR ↑ pipe flower fruit toilet roll Var × Demo 3 × 10 ...
- **p. 7 / 5 Experiments - extractive body cue:** We benchmark multi-task algorithms on 18 RLBench [52, 25] tasks.
- **p. 9 / 5 Experiments - extractive body cue:** We evaluate 10 episodes for each task and report the binary success rate.
- **p. 8 / 5 Experiments - extractive body cue:** 10* denotes 10 demonstrations per task with random SE(3) objects poses.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 4 / Figure/Table caption - extractive body cue:** Figure 1: Overview of EquAct. EquAct first encodes the observation o = {s, e} into latent spherical features h using a SE(3)-equivariant U-Net, enco, while ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 2: The equivariance and invariance of the multi-task keyframe policy. Under the equivariance assumption, when the obser- vation is transformed to g · o, ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3: SE(3)-Equivariant Point Transformer U-net (EPTU). Spherical Fourier maxpooling. Analogous to the maxpooling operation in convolutional neural networks [33], the spherical Fourier maxpooling layer ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 4: Simulation and physical experiments. First row: 18 standard RLBench tasks[52, 25]. Second row: 18 RLBench tasks with SE(3) randomization. Third row: 4 physical ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 1: Multi-task success rate (%) on 18 RLBench. 100 and 10 denote the number of training demonstrations per task with random SE(2) objects poses. ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 2: Physical experiments. avg. disass. pluck pick install SR ↑ pipe
- **p. 9 / Figure/Table caption - extractive body cue:** Table 3: Ablation study. avg. place place reach insert SR ↑wine cups drag peg Ours
- **p. 16 / Figure/Table caption - extractive body cue:** Table 4: 18 Language-conditioned tasks in RLBench [25] with SE(3) initializations. Task Variation Type Perturbed Object SO(3) Perturbation (r, p) Language Template open drawer placement ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | In the 10 SE(3) setting, the training set contains 10 demo per task and both the training and testing scenes have randomly SE(3) initialized ... | embodiment, simulator version and control stack | p. 8 (5 Experiments), p. 7 (5 Experiments) |
| Task/environment | The benchmark uses a Franka Panda robot equipped with a parallel gripper. | reset, timeout, object/scene variation | p. 7 (5 Experiments), p. 9 (5 Experiments) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 4 (4 Method), p. 2 (2 Background) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 5 (4 Method), p. 5 (4 Method) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Performance is measured by a binary reward, where 0% and 100% correspond to failure and successful completion of the task according to the natural ... | definition/direction/unit from same section | p. 7 (5 Experiments) |
| We report the task success rate over 25 evaluation episodes per task, with a maximum of 25 steps per episode. | definition/direction/unit from same section | p. 7 (5 Experiments) |
| On average, EquAct outperforms all the baselines on all 3 settings. avg. success rate ↑ open drawer slide block sweep dust. meat off grill ... | definition/direction/unit from same section | p. 8 (5 Experiments) |
| We evaluate 10 episodes for each task and report the binary success rate. | definition/direction/unit from same section | p. 9 (5 Experiments) |
| Besides success rate, EquAct matches the training/inference time and GPU memory consumption of other baselines. | definition/direction/unit from same section | p. 9 (5 Experiments) |
| This indicates that the equivariance is crucial for a policy adapting precisely to objects pose. | definition/direction/unit from same section | p. 8 (5 Experiments) |
| Figure 6: Real world experimental setup Number of keyframe actions: 4. Variations: "top flower", "middle flower", "bottom flower". Objects: Three artificial flowers and one ... | definition/direction/unit from same section | p. 17 (Figure/Table caption) |
| Figure 2: The equivariance and invariance of the multi-task keyframe policy. Under the equivariance assumption, when the obser- vation is transformed to g · ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| In the end, EquAct outperforms SOTA baselines by 2.6% and 6.2% when trained with 100 or 10 demos in SE(2) setting, and by 15.4% ... | comparison identity and matched condition | p. 9 (5 Experiments) |
| SAM2ACT[8] is the current state-of-the-art baseline on 18 RLBench, which leverages pretrained image tokenizer from SAM2 [45] and projects point cloud into image planes ... | comparison identity and matched condition | p. 7 (5 Experiments) |
| Furthermore, the more difficult the setting is, the more EquAct outperforms the baselines, demonstrating strong sample efficiency and 3D generalization. | comparison identity and matched condition | p. 8 (5 Experiments) |
| On average, EquAct outperforms all the baselines on all 3 settings. avg. success rate ↑ open drawer slide block sweep dust. meat off grill ... | comparison identity and matched condition | p. 8 (5 Experiments) |
| We benchmark our method with two strong baselines. | comparison identity and matched condition | p. 7 (5 Experiments) |
| Besides success rate, EquAct matches the training/inference time and GPU memory consumption of other baselines. | comparison identity and matched condition | p. 9 (5 Experiments) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| 12.3 14 0 35 0 We perform the ablations on the 10 demo setting: Ours: the full EquAct model. aug. →no aug. removes data ... | component/input/data sensitivity | p. 9 (5 Experiments) |
| Even though only a single equivariant layer is replaced, equ. →no equ. results in the largest performance drop, underscoring the critical role of maintaining ... | component/input/data sensitivity | p. 9 (5 Experiments) |
| A language instruction specifies each variant of the task. | component/input/data sensitivity | p. 8 (5 Experiments) |
| Figure 1: Overview of EquAct. EquAct first encodes the observation o = {s, e} into latent spherical features h using a SE(3)-equivariant U-Net, enco, ... | component/input/data sensitivity | p. 4 (Figure/Table caption) |
| Figure 3: SE(3)-Equivariant Point Transformer U-net (EPTU). Spherical Fourier maxpooling. Analogous to the maxpooling operation in convolutional neural networks [33], the spherical Fourier maxpooling ... | component/input/data sensitivity | p. 6 (Figure/Table caption) |
| SAM2ACT[8] is the current state-of-the-art baseline on 18 RLBench, which leverages pretrained image tokenizer from SAM2 [45] and projects point cloud into image planes ... | component/input/data sensitivity | p. 7 (5 Experiments) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We propose a continuous SE(3)-equivariant keyframe policy that includes a novel equivariant U-net architecture, a novel invariant FiLM layer, and a novel equivariant field ... | On average, EquAct outperforms all the baselines on all 3 settings. avg. success rate ↑ open drawer slide block sweep dust. meat off grill ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (5 Experiments), p. 9 (5 Experiments), p. 7 (5 Experiments), p. 9 (5 Experiments), p. 8 (5 Experiments), p. 7 (5 Experiments) |
| Primary metric/result | Finally, aug. →no aug. indicates using data augmentation can further improve performance, we hypothesize that data augmentation reduces numerical error in the equivariant neural ... | numeric claim only at cited anchor | p. 9 (5 Experiments) |

- Numeric sentences retained from the body:
- **p. 7 / 5 Experiments - extractive body cue:** We report the task success rate over 25 evaluation episodes per task, with a maximum of 25 steps per episode.
- **p. 7 / 5 Experiments - extractive body cue:** All the baselines are trained and evaluated on a single RTX 4090 GPU with 24 GB memory.
- **p. 9 / 5 Experiments - extractive body cue:** We evaluate 10 episodes for each task and report the binary success rate.
- **p. 5 / 4 Method - extractive body cue:** During training, EquAct minimizes the following loss: L = E(o,n,¯a)∼D,a∼A h H  Qa(o, n, a), ¯a i = E h H( 3 X i=1 Qt(ai ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Performance is measured by a binary reward, where 0% and 100% correspond to failure and successful completion of the task according to the natural ... | p. 7 (5 Experiments) |
| body limitation/failure cue | In comparison, 3DDA struggles in these experiments, often skipping keyframe actions and resulting in failure. | p. 9 (5 Experiments) |
| body limitation/failure cue | 6 Conclusion and limitations Conclusion. | p. 9 (5 Experiments) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Besides success rate, EquAct matches the training/inference time and GPU memory consumption of other baselines. | p. 9 (5 Experiments) |
| We report hyperparameters in Appendix D. | p. 7 (5 Experiments) |
| All the baselines are trained and evaluated on a single RTX 4090 GPU with 24 GB memory. | p. 7 (5 Experiments) |
| Specifically we use a novel equivariant point transformer U-net (EPTU) to encode the observation and use equivariant field networks to evaluate action candidates. | p. 9 (5 Experiments) |
| The inference procedure is illustrated in Figure 1 and has the following steps. | p. 4 (4 Method) |
| Here, k is the encoding of the natural language instruction n, by using a CLIP [44] tokenlizer and a Transformer [59] encoder. | p. 4 (4 Method) |
| 4.2 Equivariant Point Transformer U-net (EPTU) The SE(3)-equivariant Point Transformer U-Net (EPTU, Figure 3) encodes a point cloud s into equivariant latent features by ... | p. 5 (4 Method) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / 5 Experiments - extractive body cue:** Performance is measured by a binary reward, where 0% and 100% correspond to failure and successful completion of the task according to the natural language ...
- **p. 9 / 5 Experiments - extractive body cue:** In comparison, 3DDA struggles in these experiments, often skipping keyframe actions and resulting in failure.
- **p. 9 / 5 Experiments - extractive body cue:** 6 Conclusion and limitations Conclusion.

- **PDF anchors reviewed:** datasets p. 8 (5 Experiments), p. 7 (5 Experiments), p. 9 (5 Experiments), p. 7 (5 Experiments), p. 9 (5 Experiments), p. 8 (5 Experiments), metrics p. 7 (5 Experiments), p. 7 (5 Experiments), p. 8 (5 Experiments), p. 9 (5 Experiments), p. 9 (5 Experiments), p. 8 (5 Experiments), baselines p. 9 (5 Experiments), p. 7 (5 Experiments), p. 8 (5 Experiments), p. 8 (5 Experiments), p. 7 (5 Experiments), p. 9 (5 Experiments), results p. 8 (5 Experiments), p. 9 (5 Experiments), p. 7 (5 Experiments), p. 9 (5 Experiments), p. 8 (5 Experiments), p. 7 (5 Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
