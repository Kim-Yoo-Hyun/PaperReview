# Evaluation - SafeMimic: Towards Safe and Autonomous Human-to-Robot Imitation for Mobile Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (15 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p128.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p128.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (C. Learning from Previous Successful Exploration), p. 7 (C. Learning from Previous Successful Exploration), p. 6 (C. Learning from Previous Successful Exploration), p. 6 (Figure/Table caption), p. 3 (Figure/Table caption), p. 8 (C. Learning from Previous Successful Exploration)): We observe that SAFEMIMIC achieves a minimum of 40% final suc- ‘cess rate over the seven tasks, significantly outperforming all baselines.

## Evaluation Body Digest

- **p. 6 / C. Learning from Previous Successful Exploration - extractive body cue:** We also evaluate if the data generated to train our safety Qfunctions would suffice for training task policies: we include Imitation Learning (1L) baselines based ...
- **p. 8 / C. Learning from Previous Successful Exploration - extractive body cue:** We also tested one human demonstrator across three environments on the shelving task to ensure SAFEMIMIC is robust to different objects and room layouts We ...
- **p. 6 / C. Learning from Previous Successful Exploration - extractive body cue:** In our experiments, we aim to answer four questions: QI) Does SAFEMIMIC enable a robot to successfully complete a multi-step mobile manipulation task from a ...
- **p. 7 / C. Learning from Previous Successful Exploration - extractive body cue:** The Direct Execution baseline achieves 0% final success rate on all the seven tasks, demonstrating the need for exploration in order to effectively adapt the ...
- **p. 8 / C. Learning from Previous Successful Exploration - extractive body cue:** Interestingly, the robot had to adapt the grasping strategy for each of the three provided demonstrations, as all humans preferred a topdown grasp but such ...
- **p. 5 / B. Safe and Autonomous Real-World Adaptation - extractive body cue:** However, human monitoring would still be necessary to reset the robot and the environment and attempt new sequences of actions.
- **p. 5 / C. Learning from Previous Successful Exploration - extractive body cue:** ‘+ boxing an item: Pick the object from the table and place it in a box, requiring a top-down grasp by the robot to avoid ...
- **p. 7 / C. Learning from Previous Successful Exploration - extractive body cue:** Similarly, for the store_in_dzawer task, the human-like grasp leads to joint limits being reached and so the robot explores and adapts its grasp to successfully ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SIMULATION`.
- **Target system/task:** mobile base와 one/two-arm manipulation environment.
- **Input boundary:** egocentric RGB-D, language/task goal, base-arm proprioception.
- **Output/decision under evaluation:** base motion plus arm/gripper action.
- **Primary target:** long-horizon task success, reachability, collision과 recovery.
- **Detected evaluation headings:** not reliably recovered.

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| C. Learning from Previous Successful Exploration | EMPIRICAL / SIMULATION | We observe that SAFEMIMIC achieves a minimum of 40% final suc- ‘cess rate over the seven tasks, significantly outperforming all baselines. | p. 7 (C. Learning from Previous Successful Exploration) |
| C. Learning from Previous Successful Exploration | EMPIRICAL / SIMULATION | The Direct Execution baseline achieves 0% final success rate on all the seven tasks, demonstrating the need for exploration in order to effectively adapt ... | p. 7 (C. Learning from Previous Successful Exploration) |
| C. Learning from Previous Successful Exploration | EMPIRICAL / SIMULATION | Note as well hat some lines overlap at the Same ly outperforms all baselines and achieves upto 100% sucess ia exploratory adaptation, indcaling © ... | p. 6 (C. Learning from Previous Successful Exploration) |
| Figure/Table caption | EMPIRICAL / SIMULATION | Fig. 4. Accumulated Success on Mult-Step Tasks. Accumulated success rate at each stage of each ofthe seven evaluated multi-step mobile manipulation tasks, indicating the ... | p. 6 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / SIMULATION | Fig. 2. Overview of SArEMIMEC. From an RGB-D video ofa human performing a multi-step mobile manipulation task acquired by the robot, SAFEMIMIC uses combination ... | p. 3 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 6 / C. Learning from Previous Successful Exploration - extractive body cue:** We also evaluate if the data generated to train our safety Qfunctions would suffice for training task policies: we include Imitation Learning (1L) baselines based ...
- **p. 8 / C. Learning from Previous Successful Exploration - extractive body cue:** We also tested one human demonstrator across three environments on the shelving task to ensure SAFEMIMIC is robust to different objects and room layouts We ...
- **p. 6 / C. Learning from Previous Successful Exploration - extractive body cue:** In our experiments, we aim to answer four questions: QI) Does SAFEMIMIC enable a robot to successfully complete a multi-step mobile manipulation task from a ...
- **p. 7 / C. Learning from Previous Successful Exploration - extractive body cue:** The Direct Execution baseline achieves 0% final success rate on all the seven tasks, demonstrating the need for exploration in order to effectively adapt the ...
- **p. 8 / C. Learning from Previous Successful Exploration - extractive body cue:** Interestingly, the robot had to adapt the grasping strategy for each of the three provided demonstrations, as all humans preferred a topdown grasp but such ...
- **p. 5 / B. Safe and Autonomous Real-World Adaptation - extractive body cue:** However, human monitoring would still be necessary to reset the robot and the environment and attempt new sequences of actions.
- **p. 5 / C. Learning from Previous Successful Exploration - extractive body cue:** ‘+ boxing an item: Pick the object from the table and place it in a box, requiring a top-down grasp by the robot to avoid ...
- **p. 7 / C. Learning from Previous Successful Exploration - extractive body cue:** Similarly, for the store_in_dzawer task, the human-like grasp leads to joint limits being reached and so the robot explores and adapts its grasp to successfully ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1. Robot imitating «single video of a human ‘manipulation wsk safely and autonomously with SAFEMIMC. From a video ‘oa muli-step mbile manipulation ask (op), ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2. Overview of SArEMIMEC. From an RGB-D video ofa human performing a multi-step mobile manipulation task acquired by the robot, SAFEMIMIC uses combination of ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 4. Accumulated Success on Mult-Step Tasks. Accumulated success rate at each stage of each ofthe seven evaluated multi-step mobile manipulation tasks, indicating the percentage ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 5. Grasping mode adaptation. Two examples (top and bottom rows) of SAFEMIMIC's grasping mode adeptation. Left column: human ‘demonstrated grasp. Middle column. robot failing ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 6. Safe exploration with Safety Q-unetion predictions Examples of predictions ofthe Safety Q-unction (SOF for two tasks: the opening drawer Segment in store_in drawer ...
- **p. 14 / Figure/Table caption - extractive body cue:** Fig. 8. Human video pursing by SAFEMIMIC. An inital ROB-D video ‘demonsration is processed by SAFEMIMIC using a body tracking solution to obtain segments where ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We also evaluate if the data generated to train our safety Qfunctions would suffice for training task policies: we include Imitation Learning (1L) baselines ... | embodiment, simulator version and control stack | p. 6 (C. Learning from Previous Successful Exploration), p. 8 (C. Learning from Previous Successful Exploration) |
| Task/environment | We also tested one human demonstrator across three environments on the shelving task to ensure SAFEMIMIC is robust to different objects and room layouts ... | reset, timeout, object/scene variation | p. 8 (C. Learning from Previous Successful Exploration), p. 6 (C. Learning from Previous Successful Exploration) |
| Observation/sensor | egocentric RGB-D, language/task goal, base-arm proprioception | calibration, preprocessing, privileged input | p. 6 (C. Learning from Previous Successful Exploration), p. 4 (B. Safe and Autonomous Real-World Adaptation) |
| Output/decision | base motion plus arm/gripper action | action frame, controller and termination | p. 5 (C. Learning from Previous Successful Exploration), p. 2 (I. INrRopucTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Fig. 4. Accumulated Success on Mult-Step Tasks. Accumulated success rate at each stage of each ofthe seven evaluated multi-step mobile manipulation tasks, indicating the ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| Each task is attempted five times, and success rates are reported at each stage of each task. | definition/direction/unit from same section | p. 7 (C. Learning from Previous Successful Exploration) |
| The success rate for each segment (¢.g., "Navigated to object," "Picked object") reflects the proportion of trials successfully completed up to and including that ... | definition/direction/unit from same section | p. 7 (C. Learning from Previous Successful Exploration) |
| We evaluate SaFEMIMIC in 7 challenging multi-step mobile ‘manipulation tasks demonstrated by humans. ‘The tasks all consist of multiple stages and require navigation, rigid-body ... | definition/direction/unit from same section | p. 5 (C. Learning from Previous Successful Exploration) |
| However, successful strategies need to be learned in order to prevent re | definition/direction/unit from same section | p. 5 (C. Learning from Previous Successful Exploration) |
| To evaluate SAFEMIMIC'S task performance, we measure its ability to successfully imitate and adapt demonstrations of the aforementioned tasks. | definition/direction/unit from same section | p. 6 (C. Learning from Previous Successful Exploration) |
| For all three demonstrators, SAFEMIMIC was able to successfully recover, parse and translate the demonstrated behavior. | definition/direction/unit from same section | p. 8 (C. Learning from Previous Successful Exploration) |
| Both the IL baselines, 1L (a12 safe actions) and 12 (successful episodes) observe slightly lower unsafe action rates at 10.8% and 9.5% respectively, but ... | definition/direction/unit from same section | p. 8 (C. Learning from Previous Successful Exploration) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Note as well hat some lines overlap at the Same ly outperforms all baselines and achieves upto 100% sucess ia exploratory adaptation, indcaling © ... | comparison identity and matched condition | p. 6 (C. Learning from Previous Successful Exploration) |
| We observe that SAFEMIMIC achieves a minimum of 40% final suc- ‘cess rate over the seven tasks, significantly outperforming all baselines. | comparison identity and matched condition | p. 7 (C. Learning from Previous Successful Exploration) |
| This baseline is SAFEMIMIC without the use of SQFs. | comparison identity and matched condition | p. 6 (C. Learning from Previous Successful Exploration) |
| The Direct Execution baseline achieves 0% final success rate on all the seven tasks, demonstrating the need for exploration in order to effectively adapt ... | comparison identity and matched condition | p. 7 (C. Learning from Previous Successful Exploration) |
| Both the IL baselines, 1L (a12 safe actions) and 12 (successful episodes) observe slightly lower unsafe action rates at 10.8% and 9.5% respectively, but ... | comparison identity and matched condition | p. 8 (C. Learning from Previous Successful Exploration) |
| explored hy" SAFEMIMIC with (cgh0) and without policy memory lef, Successful attempts from an ial exploration are recorded and use to tain the policy ... | comparison identity and matched condition | p. 8 (C. Learning from Previous Successful Exploration) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| This baseline is SAFEMIMIC without the use of SQFs. | component/input/data sensitivity | p. 6 (C. Learning from Previous Successful Exploration) |
| We compare SAFEMIMC's tsk performance 10 five baselines: direct exccution without safety Q-unctions (SQFs), which equires human supervsia, dict execution with SQFs, exploration without ... | component/input/data sensitivity | p. 6 (C. Learning from Previous Successful Exploration) |
| Exploration alone (Explozat Lon without SO®) similarly results in 14.2% unsafe actions, demonstrating the critical need for safety during exploration | component/input/data sensitivity | p. 7 (C. Learning from Previous Successful Exploration) |
| The Direct Execution (without safety Q-functions) gen erates 13.4% unsafe actions and incurs safety violations in nearly every task, commonly colliding during both navigation ... | component/input/data sensitivity | p. 7 (C. Learning from Previous Successful Exploration) |
| explored hy" SAFEMIMIC with (cgh0) and without policy memory lef, Successful attempts from an ial exploration are recorded and use to tain the policy ... | component/input/data sensitivity | p. 8 (C. Learning from Previous Successful Exploration) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| environments with different human teachers, and observe experimentally that our framework enables the robot to suc cessfully acquire the desired behaviors safely and more ... | We observe that SAFEMIMIC achieves a minimum of 40% final suc- ‘cess rate over the seven tasks, significantly outperforming all baselines. | PDF body cue; verify exact table/figure and matched conditions | p. 7 (C. Learning from Previous Successful Exploration), p. 7 (C. Learning from Previous Successful Exploration), p. 6 (C. Learning from Previous Successful Exploration), p. 6 (Figure/Table caption), p. 3 (Figure/Table caption), p. 8 (C. Learning from Previous Successful Exploration) |
| Primary metric/result | The Direct Execution baseline achieves 0% final success rate on all the seven tasks, demonstrating the need for exploration in order to effectively adapt ... | numeric claim only at cited anchor | p. 7 (C. Learning from Previous Successful Exploration) |

- Numeric sentences retained from the body:
- **p. 8 / C. Learning from Previous Successful Exploration - extractive body cue:** We also tested one human demonstrator across three environments on the shelving task to ensure SAFEMIMIC is robust to different objects and room layouts We ...
- **p. 8 / C. Learning from Previous Successful Exploration - extractive body cue:** We also tested one human demonstrator across three environments on the shelving task to ensure SAFEMIMIC is robust to different objects and room layouts We ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Scaling to other types of safety violations or task failures presents an opportunity for future work. | p. 8 (V. LIMITATIONS AND FUTURE WORK) |
| body limitation/failure cue | We evaluate SaFEMIMIC in 7 challenging multi-step mobile ‘manipulation tasks demonstrated by humans. ‘The tasks all consist of multiple stages and require navigation, rigid-body ... | p. 5 (C. Learning from Previous Successful Exploration) |
| body limitation/failure cue | While SAFEMIMIC is generic and can include many possible failure modes, we consider the following in this work: arm collisions, base collisions, joint limit ... | p. 6 (C. Learning from Previous Successful Exploration) |
| body limitation/failure cue | However, there are some limitations of the method that offer exciting avenues for future work. | p. 8 (V. LIMITATIONS AND FUTURE WORK) |
| body limitation/failure cue | Q2) How effectively does SAFEMIMIC reduce safetycritical failures? | p. 7 (C. Learning from Previous Successful Exploration) |
| body limitation/failure cue | This task requires differentiating the human's semantic goal, and avoiding collisions and adapting grasps for successful placement. | p. 5 (C. Learning from Previous Successful Exploration) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The architecture for the action prediction policy network is composed by a PointNet [66] encoder for the visual information, and a SentenceTransformer [67] for ... | p. 5 (C. Learning from Previous Successful Exploration) |
| When executed, the initial translated motion may fail due 10 morphological differences or noise in the video parsing; while finding small adaptations have been ... | p. 1 (I. INrRopucTION) |
| This would bypass the need for costly teleoperated data collection (1, 2, 3}, which is significantly complex and time-consuming for multi-step tasks and those ... | p. 1 (I. INrRopucTION) |
| These works address the requirement of autonomy, but generally sidestep the question of safety - ‘critical challenge when learning mobile manipulation in the real ... | p. 2 (I. INrRopucTION) |
| Constrained RL methods (48, 49, 50, 51] similarly allow for policy learning while obeying constraints, though typically require closed-form constraints available at runtime. | p. 3 (I. INrRopucTION) |
| To that end, SAFEMIMIC explores actions for each of the segments in turn, until the semantic goal of the segment is achieved in a ... | p. 4 (B. Safe and Autonomous Real-World Adaptation) |
| Similarly, for ‘manipulation segments, SAFEMIMIC first transforms the hand pose to be relative to the human body and then computes the relative motion of ... | p. 4 (I. INrRopucTION) |
| If the segment has not been ‘completed, the process repeats with a new set of actions around the human demonstrated one (see pseudocode in ... | p. 5 (B. Safe and Autonomous Real-World Adaptation) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / V. LIMITATIONS AND FUTURE WORK - extractive body cue:** Scaling to other types of safety violations or task failures presents an opportunity for future work.
- **p. 5 / C. Learning from Previous Successful Exploration - extractive body cue:** We evaluate SaFEMIMIC in 7 challenging multi-step mobile ‘manipulation tasks demonstrated by humans. ‘The tasks all consist of multiple stages and require navigation, rigid-body pick-and-place, ...
- **p. 6 / C. Learning from Previous Successful Exploration - extractive body cue:** While SAFEMIMIC is generic and can include many possible failure modes, we consider the following in this work: arm collisions, base collisions, joint limit violations, ...
- **p. 8 / V. LIMITATIONS AND FUTURE WORK - extractive body cue:** However, there are some limitations of the method that offer exciting avenues for future work.
- **p. 7 / C. Learning from Previous Successful Exploration - extractive body cue:** Q2) How effectively does SAFEMIMIC reduce safetycritical failures?
- **p. 5 / C. Learning from Previous Successful Exploration - extractive body cue:** This task requires differentiating the human's semantic goal, and avoiding collisions and adapting grasps for successful placement.

- **PDF anchors reviewed:** datasets p. 6 (C. Learning from Previous Successful Exploration), p. 8 (C. Learning from Previous Successful Exploration), p. 6 (C. Learning from Previous Successful Exploration), p. 7 (C. Learning from Previous Successful Exploration), p. 8 (C. Learning from Previous Successful Exploration), p. 5 (B. Safe and Autonomous Real-World Adaptation), metrics p. 6 (Figure/Table caption), p. 7 (C. Learning from Previous Successful Exploration), p. 7 (C. Learning from Previous Successful Exploration), p. 5 (C. Learning from Previous Successful Exploration), p. 5 (C. Learning from Previous Successful Exploration), p. 6 (C. Learning from Previous Successful Exploration), baselines p. 6 (C. Learning from Previous Successful Exploration), p. 7 (C. Learning from Previous Successful Exploration), p. 6 (C. Learning from Previous Successful Exploration), p. 7 (C. Learning from Previous Successful Exploration), p. 8 (C. Learning from Previous Successful Exploration), p. 8 (C. Learning from Previous Successful Exploration), results p. 7 (C. Learning from Previous Successful Exploration), p. 7 (C. Learning from Previous Successful Exploration), p. 6 (C. Learning from Previous Successful Exploration), p. 6 (Figure/Table caption), p. 3 (Figure/Table caption), p. 8 (C. Learning from Previous Successful Exploration).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
