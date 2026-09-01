# Evaluation - RVT: Robotic View Transformer for 3D Object Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (16 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2306.14896; PDF retrieval source: https://arxiv.org/pdf/2306.14896. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (4 Experiments), p. 8 (4 Experiments), p. 8 (4 Experiments), p. 6 (4 Experiments), p. 7 (4 Experiments), p. 3 (Figure/Table caption)): Overall, RVT outperforms all baselines with the best rank and success rate when averaged across all tasks.

## Evaluation Body Digest

- **p. 5 / 4 Experiments - extractive body cue:** Just like the baselines, we use the RLBench training dataset with 100 expert demonstrations per task (1800 demonstrations over all tasks).
- **p. 8 / 4 Experiments - extractive body cue:** We also found that RVT can work on real-world manipulation tasks with only a few demonstrations.
- **p. 8 / 4 Experiments - extractive body cue:** Given a sampled task and scene configuration, we ask the human demonstrator to specify a sequence of gripper target poses by kinesthetically moving the robot ...
- **p. 5 / 4 Experiments - extractive body cue:** A Franka Panda robot with a parallel gripper is controlled to complete the tasks.
- **p. 7 / 4 Experiments - extractive body cue:** Right: Results of the real-world experiments.
- **p. 7 / 4 Experiments - extractive body cue:** 3) with respect to the table (and robot) decreases performance.
- **p. 6 / 4 Experiments - extractive body cue:** These results overestimate the performance of Image-BC and C2F-ARMBC, as they select the best model for each of the 18 tasks independently based on the ...
- **p. 6 / 4 Experiments - extractive body cue:** RVT outperforms PerAct on 88.9% (16/18) of the tasks.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 4 Experiments (p. 5).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | Overall, RVT outperforms all baselines with the best rank and success rate when averaged across all tasks. | p. 6 (4 Experiments) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our model overall achieves an 82.5% success rate on non-marker tasks. | p. 8 (4 Experiments) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | Overall, RVT achieves high success rates for the stack block task (100%) and the press sanitizer task (80%). | p. 8 (4 Experiments) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | It outperforms prior state-of-the-art methods, C2F-ARM, by 42 percentage points (213% relative improvement); and PerAct by 13 percentage points (26% relative improvement). | p. 6 (4 Experiments) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | A larger res., adding view correspondence, adding depth channel, separating initial attention layers, orthographic projection, using rotation aug., and rerendered views around cube improve ... | p. 7 (4 Experiments) |

## Dataset / Benchmark Role

- **p. 5 / 4 Experiments - extractive body cue:** Just like the baselines, we use the RLBench training dataset with 100 expert demonstrations per task (1800 demonstrations over all tasks).
- **p. 8 / 4 Experiments - extractive body cue:** We also found that RVT can work on real-world manipulation tasks with only a few demonstrations.
- **p. 8 / 4 Experiments - extractive body cue:** Given a sampled task and scene configuration, we ask the human demonstrator to specify a sequence of gripper target poses by kinesthetically moving the robot ...
- **p. 5 / 4 Experiments - extractive body cue:** A Franka Panda robot with a parallel gripper is controlled to complete the tasks.
- **p. 7 / 4 Experiments - extractive body cue:** Right: Results of the real-world experiments.
- **p. 7 / 4 Experiments - extractive body cue:** 3) with respect to the table (and robot) decreases performance.
- **p. 6 / 4 Experiments - extractive body cue:** These results overestimate the performance of Image-BC and C2F-ARMBC, as they select the best model for each of the 18 tasks independently based on the ...
- **p. 6 / 4 Experiments - extractive body cue:** RVT outperforms PerAct on 88.9% (16/18) of the tasks.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: RVT scales and performs better than PerAct on RLBench, achieving on- par performance in 36X less time (same hardware), and 1.26X peak performance. ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2: Overview of RVT. Given RGB-D from sensor(s), we first construct a point cloud of the scene. The point cloud is then used to ...
- **p. 5 / Figure/Table caption - extractive body cue:** Table 1: Multi-Task Performance on RLBench. RVT outperforms state-of-the-art methods while being faster to train and execute. RVT has the best success rate and rank ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3: We evaluate RVT with various camera locations for re-rendering (a-d) and find that loca- tions in (a) perform best. We also test various ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2: Left: Ablations on RLBench. A larger res., adding view correspondence, adding depth channel, separating initial attention layers, orthographic projection, using rotation aug., and ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 4: Examples of RVT in the real world. A single RVT model can perform multiple tasks (5 tasks, 13 variations) in the real world ...
- **p. 14 / Figure/Table caption - extractive body cue:** Table 3: Tasks in RLBench We evaluate on 18 RLBench tasks which are same as those used in PerAct [6]. For more details, check see ...
- **p. 15 / Figure/Table caption - extractive body cue:** Figure 5: Overview of the transformer used in RVT. The input to the transformer is a language description of the task and virtual images of ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Just like the baselines, we use the RLBench training dataset with 100 expert demonstrations per task (1800 demonstrations over all tasks). | embodiment, simulator version and control stack | p. 5 (4 Experiments), p. 8 (4 Experiments) |
| Task/environment | We also found that RVT can work on real-world manipulation tasks with only a few demonstrations. | reset, timeout, object/scene variation | p. 8 (4 Experiments), p. 8 (4 Experiments) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 4 (3 Method), p. 4 (3 Method) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 3 (3 Method), p. 3 (3 Method) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Due to the randomness of the sampling-based motion planner, we run each model five times on the same 25 variations for each task and ... | definition/direction/unit from same section | p. 6 (4 Experiments) |
| Table 1: Multi-Task Performance on RLBench. RVT outperforms state-of-the-art methods while being faster to train and execute. RVT has the best success rate and ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| Our model overall achieves an 82.5% success rate on non-marker tasks. | definition/direction/unit from same section | p. 8 (4 Experiments) |
| Overall, RVT achieves high success rates for the stack block task (100%) and the press sanitizer task (80%). | definition/direction/unit from same section | p. 8 (4 Experiments) |
| We test on the same 18 tasks as PerAct, including picking and placing, tool use, drawer opening, and high-accuracy peg insertions (see the appendix ... | definition/direction/unit from same section | p. 5 (4 Experiments) |
| The same table along with the mean and standard deviation for each task can be found in the appendix Tab. | definition/direction/unit from same section | p. 6 (4 Experiments) |
| 3) with respect to the table (and robot) decreases performance. | definition/direction/unit from same section | p. 7 (4 Experiments) |
| We hypothesize that it is because orthographic projection preserves the shape and size of an object regardless of its distance from the camera (see ... | definition/direction/unit from same section | p. 7 (4 Experiments) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Overall, RVT outperforms all baselines with the best rank and success rate when averaged across all tasks. | comparison identity and matched condition | p. 6 (4 Experiments) |
| These results demonstrate that RVT is both more accurate and scalable when compared to existing state-of-the-art voxel-based methods. | comparison identity and matched condition | p. 6 (4 Experiments) |
| We found that RVT outperforms prior state-of-the-art models like PerAct and C2F-ARM on a variety of 3D manipulation tasks, while being more scalable and ... | comparison identity and matched condition | p. 8 (4 Experiments) |
| Just like the baselines, we use the RLBench training dataset with 100 expert demonstrations per task (1800 demonstrations over all tasks). | comparison identity and matched condition | p. 5 (4 Experiments) |
| We compare against the following three baselines: (1) Image-BC [2] is an image-toaction behavior cloning agent that predicts action based on the image observations ... | comparison identity and matched condition | p. 5 (4 Experiments) |
| (h) RVT performs better with re-rendered images as compared to using sensor camera images (Tab. | comparison identity and matched condition | p. 7 (4 Experiments) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We compare with two variants with CNN and ViT vision encoders respectively. | component/input/data sensitivity | p. 5 (4 Experiments) |
| 2 (left) summarizes the ablation experiment results. | component/input/data sensitivity | p. 6 (4 Experiments) |
| We test our models (including the models in the ablation study, Tab. | component/input/data sensitivity | p. 6 (4 Experiments) |
| The sensor camera images are rendered with perspective projection (physical rendering process) and are not straightforward to apply 3D augmentations (e.g., rotation) without re-rendering. | component/input/data sensitivity | p. 7 (4 Experiments) |
| Task vari. train test (+ mark.) (- mark.) Stack 3 14 10 100% 100% blocks Press sanitizer 1 7 10 80% 80% Put marker ... | component/input/data sensitivity | p. 7 (4 Experiments) |
| Table 4: Ablations results for RVT on RLBench with metrics for each task. 16 | component/input/data sensitivity | p. 16 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To summarize, our contributions are threefold: first, we propose RVT, a multi-view transformer for 3D object manipulation that is accurate and scalable; second, we ... | Overall, RVT outperforms all baselines with the best rank and success rate when averaged across all tasks. | PDF body cue; verify exact table/figure and matched conditions | p. 6 (4 Experiments), p. 8 (4 Experiments), p. 8 (4 Experiments), p. 6 (4 Experiments), p. 7 (4 Experiments), p. 3 (Figure/Table caption) |
| Primary metric/result | Our model overall achieves an 82.5% success rate on non-marker tasks. | numeric claim only at cited anchor | p. 8 (4 Experiments) |

- Numeric sentences retained from the body:
- **p. 5 / 4 Experiments - extractive body cue:** We test on the same 18 tasks as PerAct, including picking and placing, tool use, drawer opening, and high-accuracy peg insertions (see the appendix for ...
- **p. 5 / 4 Experiments - extractive body cue:** The visual observations are captured from four noiseless RGB-D cameras positioned at the front, left shoulder, right shoulder, and wrist with a resolution of 128×128.
- **p. 6 / 4 Experiments - extractive body cue:** These results overestimate the performance of Image-BC and C2F-ARMBC, as they select the best model for each of the 18 tasks independently based on the ...
- **p. 6 / 4 Experiments - extractive body cue:** More remarkably, RVT trains 36X faster than PerAct for achieving the same performance (see Fig.
- **p. 6 / 4 Experiments - extractive body cue:** We also observe that at inference time, RVT is 2.3X faster than PerAct.
- **p. 8 / 4 Experiments - extractive body cue:** A single RVT model can perform multiple tasks (5 tasks, 13 variations) in the real world with just ∼10 demonstrations per task.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | 5 Conclusions and Limitations We proposed RVT, a multi-view transformer model for 3D object manipulation. | p. 8 (4 Experiments) |
| body limitation/failure cue | Although we found RVT to achieve state-of-the-art results, we identify some limitations that present exciting directions for future research. | p. 8 (4 Experiments) |
| body limitation/failure cue | 6.2 RVT Overview Insert peg in the blue spoke Virtual Image 1 Virtual Image 2 Virtual Image 5 Patchify Projection Attention X 4 Attention ... | p. 15 (6 Appendix) |
| body limitation/failure cue | Hence, the reported performance does not reflect a single multi-task model. | p. 6 (4 Experiments) |
| body limitation/failure cue | The visual observations are captured from four noiseless RGB-D cameras positioned at the front, left shoulder, right shoulder, and wrist with a resolution of ... | p. 5 (4 Experiments) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We train on real-world data for 10K steps, with the same optimizer, batch size, and learning rate schedule as the simulation data. | p. 8 (4 Experiments) |
| We use cosine learning rate decay with warm-start for 2K steps. | p. 6 (4 Experiments) |
| We report the total training time for both models in Tab. | p. 6 (4 Experiments) |
| The training time and inference speed of PerAct and RVT are measured on the same GPU model. we use global features (G). | p. 5 (3 Method) |
| We compare with two variants with CNN and ViT vision encoders respectively. | p. 5 (4 Experiments) |
| The key-frames represent important or bottleneck steps of the gripper during the task execution [55], such as a prepick, grasp, or place pose. | p. 3 (3 Method) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 4 Experiments - extractive body cue:** 5 Conclusions and Limitations We proposed RVT, a multi-view transformer model for 3D object manipulation.
- **p. 8 / 4 Experiments - extractive body cue:** Although we found RVT to achieve state-of-the-art results, we identify some limitations that present exciting directions for future research.
- **p. 15 / 6 Appendix - extractive body cue:** 6.2 RVT Overview Insert peg in the blue spoke Virtual Image 1 Virtual Image 2 Virtual Image 5 Patchify Projection Attention X 4 Attention X ...
- **p. 6 / 4 Experiments - extractive body cue:** Hence, the reported performance does not reflect a single multi-task model.
- **p. 5 / 4 Experiments - extractive body cue:** The visual observations are captured from four noiseless RGB-D cameras positioned at the front, left shoulder, right shoulder, and wrist with a resolution of 128×128.

- **PDF anchors reviewed:** datasets p. 5 (4 Experiments), p. 8 (4 Experiments), p. 8 (4 Experiments), p. 5 (4 Experiments), p. 7 (4 Experiments), p. 7 (4 Experiments), metrics p. 6 (4 Experiments), p. 5 (Figure/Table caption), p. 8 (4 Experiments), p. 8 (4 Experiments), p. 5 (4 Experiments), p. 6 (4 Experiments), baselines p. 6 (4 Experiments), p. 6 (4 Experiments), p. 8 (4 Experiments), p. 5 (4 Experiments), p. 5 (4 Experiments), p. 7 (4 Experiments), results p. 6 (4 Experiments), p. 8 (4 Experiments), p. 8 (4 Experiments), p. 6 (4 Experiments), p. 7 (4 Experiments), p. 3 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
