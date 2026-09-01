# Evaluation - SERL: A Software Suite for Sample-Efficient Robotic Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (14 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://ieeexplore.ieee.org/document/10610040/; PDF retrieval source: https://arxiv.org/pdf/2401.16013. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (5. Experiments), p. 9 (5. Experiments), p. 8 (5. Experiments), p. 7 (Figure/Table caption), p. 9 (5. Experiments), p. 7 (Figure/Table caption)): The learned RL policies not only outperformed their BC counterparts by as much as 10x in terms of success rate but also improved on the cycle time of the initial ...

## Evaluation Body Digest

- **p. 8 / 5. Experiments - extractive body cue:** SERL: A Software Suite for Sample-Efficient Robotic Reinforcement Learning Task # of Demos Image Input Random Reset Reward Specification Bin Size Training Time PCB Component ...
- **p. 7 / 5. Experiments - extractive body cue:** Our experimental evaluation aims to study how efficiently our system can learn a variety of robotic manipulation tasks, including contact-rich tasks, deformable object manipulation, and ...
- **p. 8 / 5. Experiments - extractive body cue:** The free-floating object relocation task learns two policies (forward and backward), and total Figure 7: Cycle time comparison: We recorded the average time taken for ...
- **p. 7 / 5. Experiments - extractive body cue:** This task requires the robot to perceive the cable and carefully manipulate it so that it fits into the clip while holding it at another ...
- **p. 9 / 5. Experiments - extractive body cue:** Researchers at the University of Washington set up a Peg Insertion task using 3D printed parts from the Functional Manipulation Benchmark (Luo et al., 2024) ...
- **p. 9 / 5. Experiments - extractive body cue:** SERL: A Software Suite for Sample-Efficient Robotic Reinforcement Learning Figure 8: Peg Insertion Task at University of Washington these prior works generally have either lower ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5: Illustration of the robot performing each task with our method: PCB Insertion (top left), Cable Routing (top right), Object Relocation - Forward (bottom ...
- **p. 8 / 5. Experiments - extractive body cue:** We report the results in terms of success rate and cycle time in Fig.

## Evaluation Type and Scope

- **Evaluation type:** `BENCHMARK / DATASET`.
- **Target system/task:** demonstration으로 정의된 robot task distribution.
- **Input boundary:** observation history와 expert trajectory/action.
- **Output/decision under evaluation:** predicted action 또는 action chunk.
- **Primary target:** imitation error, task success, robustness와 compounding error.
- **Detected evaluation headings:** 5. Experiments (p. 7).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 5. Experiments | BENCHMARK / DATASET | The learned RL policies not only outperformed their BC counterparts by as much as 10x in terms of success rate but also improved on ... | p. 8 (5. Experiments) |
| 5. Experiments | BENCHMARK / DATASET | The policy converged in 19 minutes and achieved a 100/100 success rate with 20 initial human demonstrations, successfully reproducing our results. | p. 9 (5. Experiments) |
| 5. Experiments | BENCHMARK / DATASET | Our RL policies achieve perfect success rates on all three tasks over all 100 trials. | p. 8 (5. Experiments) |
| Figure/Table caption | BENCHMARK / DATASET | Table 1: Comparison to results reported on similar tasks in prior work. The overall success rates for our method are generally higher, and the ... | p. 7 (Figure/Table caption) |
| 5. Experiments | BENCHMARK / DATASET | SERL: A Software Suite for Sample-Efficient Robotic Reinforcement Learning Figure 8: Peg Insertion Task at University of Washington these prior works generally have either ... | p. 9 (5. Experiments) |

## Dataset / Benchmark Role

- **p. 8 / 5. Experiments - extractive body cue:** SERL: A Software Suite for Sample-Efficient Robotic Reinforcement Learning Task # of Demos Image Input Random Reset Reward Specification Bin Size Training Time PCB Component ...
- **p. 7 / 5. Experiments - extractive body cue:** Our experimental evaluation aims to study how efficiently our system can learn a variety of robotic manipulation tasks, including contact-rich tasks, deformable object manipulation, and ...
- **p. 8 / 5. Experiments - extractive body cue:** The free-floating object relocation task learns two policies (forward and backward), and total Figure 7: Cycle time comparison: We recorded the average time taken for ...
- **p. 7 / 5. Experiments - extractive body cue:** This task requires the robot to perceive the cable and carefully manipulate it so that it fits into the clip while holding it at another ...
- **p. 9 / 5. Experiments - extractive body cue:** Researchers at the University of Washington set up a Peg Insertion task using 3D printed parts from the Functional Manipulation Benchmark (Luo et al., 2024) ...
- **p. 9 / 5. Experiments - extractive body cue:** SERL: A Software Suite for Sample-Efficient Robotic Reinforcement Learning Figure 8: Peg Insertion Task at University of Washington these prior works generally have either lower ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: Depiction of various tasks solved using SERL in the real world. These include PCB board insertion (left), cable routing (middle), and object relocation ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 2: Software architecture and real-world robot training example code. SERL runs three parallel processes, consisting of the actor, which chooses actions, and the learner ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3: Visualization of controller logs from the robot when commanded with different movements, for the z-axis of the end- effector. The orange line is ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4: A typical controller hierarchy for robotics RL. The output from the RL policy is tracked within a block of time by the downstream ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5: Illustration of the robot performing each task with our method: PCB Insertion (top left), Cable Routing (top right), Object Relocation - Forward (bottom ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1: Comparison to results reported on similar tasks in prior work. The overall success rates for our method are generally higher, and the training ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 2: Task parameters: During demo collection for both BC and RL, as well as online training, each episode's initial end-effector pose resets uniformly at ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 6: Success rate comparisons: When evaluated for 100 trials per task, learned RL policies outperformed BC policies by a large margin, by 1.7x for ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | SERL: A Software Suite for Sample-Efficient Robotic Reinforcement Learning Task # of Demos Image Input Random Reset Reward Specification Bin Size Training Time PCB ... | embodiment, simulator version and control stack | p. 8 (5. Experiments), p. 7 (5. Experiments) |
| Task/environment | Our experimental evaluation aims to study how efficiently our system can learn a variety of robotic manipulation tasks, including contact-rich tasks, deformable object manipulation, ... | reset, timeout, object/scene variation | p. 7 (5. Experiments), p. 8 (5. Experiments) |
| Observation/sensor | observation history와 expert trajectory/action | calibration, preprocessing, privileged input | p. 3 (3. Preliminaries and Problem Statement), p. 7 (4.6. Relative Observation and Action Frame) |
| Output/decision | predicted action 또는 action chunk | action frame, controller and termination | p. 6 (4.5. Impedance Controller for Contact-Rich), p. 6 (4.5. Impedance Controller for Contact-Rich) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Figure 5: Illustration of the robot performing each task with our method: PCB Insertion (top left), Cable Routing (top right), Object Relocation - Forward ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| SERL: A Software Suite for Sample-Efficient Robotic Reinforcement Learning Figure 8: Peg Insertion Task at University of Washington these prior works generally have either ... | definition/direction/unit from same section | p. 9 (5. Experiments) |
| We report the results in terms of success rate and cycle time in Fig. | definition/direction/unit from same section | p. 8 (5. Experiments) |
| Our RL policies achieve perfect success rates on all three tasks over all 100 trials. | definition/direction/unit from same section | p. 8 (5. Experiments) |
| The policy converged in 19 minutes and achieved a 100/100 success rate with 20 initial human demonstrations, successfully reproducing our results. | definition/direction/unit from same section | p. 9 (5. Experiments) |
| Table 1: Comparison to results reported on similar tasks in prior work. The overall success rates for our method are generally higher, and the ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Figure 1: Depiction of various tasks solved using SERL in the real world. These include PCB board insertion (left), cable routing (middle), and object ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Figure 2: Software architecture and real-world robot training example code. SERL runs three parallel processes, consisting of the actor, which chooses actions, and the ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| For the cable routing task and PCB insertion task, our policies outperform BC baselines by a large margin, despite training with 5x fewer demonstrations ... | comparison identity and matched condition | p. 8 (5. Experiments) |
| Compared to these prior works, our experiments do not use shaped rewards, which might require extensive engineering, though we do utilize a small amount ... | comparison identity and matched condition | p. 8 (5. Experiments) |
| SERL: A Software Suite for Sample-Efficient Robotic Reinforcement Learning Figure 8: Peg Insertion Task at University of Washington these prior works generally have either ... | comparison identity and matched condition | p. 9 (5. Experiments) |
| Table 1: Comparison to results reported on similar tasks in prior work. The overall success rates for our method are generally higher, and the ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| Although the components of our system are all based on (recent) prior work, the stateof-the-art performance of this combination illustrates our main thesis: the ... | comparison identity and matched condition | p. 9 (5. Experiments) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| SERL: A Software Suite for Sample-Efficient Robotic Reinforcement Learning Task # of Demos Image Input Random Reset Reward Specification Bin Size Training Time PCB ... | component/input/data sensitivity | p. 8 (5. Experiments) |
| Although the components of our system are all based on (recent) prior work, the stateof-the-art performance of this combination illustrates our main thesis: the ... | component/input/data sensitivity | p. 9 (5. Experiments) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| However, in the process of evaluating our framework, we also make a scientifically interesting empirical observation: when implemented properly in a carefully engineered software ... | The learned RL policies not only outperformed their BC counterparts by as much as 10x in terms of success rate but also improved on ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (5. Experiments), p. 9 (5. Experiments), p. 8 (5. Experiments), p. 7 (Figure/Table caption), p. 9 (5. Experiments), p. 7 (Figure/Table caption) |
| Primary metric/result | The policy converged in 19 minutes and achieved a 100/100 success rate with 20 initial human demonstrations, successfully reproducing our results. | numeric claim only at cited anchor | p. 9 (5. Experiments) |

- Numeric sentences retained from the body:
- **p. 8 / 5. Experiments - extractive body cue:** All training was done on a single Nvidia RTX 4090 GPU.
- **p. 8 / 5. Experiments - extractive body cue:** Our RL policies achieve perfect success rates on all three tasks over all 100 trials.
- **p. 8 / 5. Experiments - extractive body cue:** RL policies are at least 2x faster than BC policies trained with 100 high-quality human teleoperated demonstrations for all three tasks. time amounts to less ...
- **p. 8 / 5. Experiments - extractive body cue:** For the cable routing task and PCB insertion task, our policies outperform BC baselines by a large margin, despite training with 5x fewer demonstrations than ...
- **p. 8 / 5. Experiments - extractive body cue:** The learned RL policies not only outperformed their BC counterparts by as much as 10x in terms of success rate but also improved on the ...
- **p. 9 / 5. Experiments - extractive body cue:** The overall preparation time including setting up the relevant hardware and software is less than 3 hours.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Our framework does have a number of limitations. | p. 9 (6. Discussion) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Comparison to prior systems: While it's difficult to directly compare our results to those of prior systems due to numerous differences in the setup, ... | p. 8 (5. Experiments) |
| SERL: A Software Suite for Sample-Efficient Robotic Reinforcement Learning Figure 8: Peg Insertion Task at University of Washington these prior works generally have either ... | p. 9 (5. Experiments) |
| SERL: A Software Suite for Sample-Efficient Robotic Reinforcement Learning Task # of Demos Image Input Random Reset Reward Specification Bin Size Training Time PCB ... | p. 8 (5. Experiments) |
| The overall preparation time including setting up the relevant hardware and software is less than 3 hours. | p. 9 (5. Experiments) |
| Package Task Training time Success rate Demos Shaping? | p. 7 (4.6. Relative Observation and Action Frame) |
| The overall success rates for our method are generally higher, and the training times are generally lower, as compared to prior results. | p. 7 (4.6. Relative Observation and Action Frame) |
| 4, where a high-level RL controller 𝜋(𝐚/𝐬) sends control targets at 10HZ for the low-level impedance controller to track at 1K HZ, so one ... | p. 5 (4.5. Impedance Controller for Contact-Rich) |
| A typical impedance control objective for this controller is 𝐹= 𝑘𝑝⋅𝑒+ 𝑘𝑑⋅̇ 𝑒+ 𝐹𝑓𝑓+ 𝐹𝑐𝑜𝑟, where 𝑒= 𝑝-𝑝𝑟𝑒𝑓, 𝑝is the measured pose, and 𝑝𝑟𝑒𝑓is ... | p. 5 (4.5. Impedance Controller for Contact-Rich) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 9 / 6. Discussion - extractive body cue:** Our framework does have a number of limitations.

- **PDF anchors reviewed:** datasets p. 8 (5. Experiments), p. 7 (5. Experiments), p. 8 (5. Experiments), p. 7 (5. Experiments), p. 9 (5. Experiments), p. 9 (5. Experiments), metrics p. 7 (Figure/Table caption), p. 9 (5. Experiments), p. 8 (5. Experiments), p. 8 (5. Experiments), p. 9 (5. Experiments), p. 7 (Figure/Table caption), baselines p. 8 (5. Experiments), p. 8 (5. Experiments), p. 9 (5. Experiments), p. 7 (Figure/Table caption), p. 9 (5. Experiments), results p. 8 (5. Experiments), p. 9 (5. Experiments), p. 8 (5. Experiments), p. 7 (Figure/Table caption), p. 9 (5. Experiments), p. 7 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
