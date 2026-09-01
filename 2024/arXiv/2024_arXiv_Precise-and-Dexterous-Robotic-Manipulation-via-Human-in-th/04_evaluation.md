# Evaluation - Precise and Dexterous Robotic Manipulation via Human-in-the-Loop Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (54 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2410.21845; PDF retrieval source: https://arxiv.org/pdf/2410.21845. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 15 (4.3. Experimental Results), p. 15 (4.3. Experimental Results), p. 17 (5. Result Analysis), p. 18 (5.1. Reliability of the Learned Policies), p. 19 (5.1. Reliability of the Learned Policies), p. 18 (5.1. Reliability of the Learned Policies)): This is a significant improvement over the HG-DAgger baseline, which achieved an average success rate of 49.7% across all tasks.

## Evaluation Body Digest

- **p. 9 / 4.1. Overview of Experiments - extractive body cue:** Each task also uses either a scripted robot motion or manually human reset to randomize the initial state of the task.
- **p. 9 / 4.1. Overview of Experiments - extractive body cue:** We solve these tasks by utilizing either a single robot arm or a dual-arm setup, together with various combinations of observations and actions.
- **p. 13 / 4.3. Experimental Results - extractive body cue:** For all tasks, BC baselines were trained using HG-DAgger with the same number of episodes and interventions as RL.
- **p. 13 / 4.3. Experimental Results - extractive body cue:** Diffusion Policy (DP) and BC are trained with 200 demonstrations, while HG-DAgger is trained with the same number of episodes and interventions as RL.
- **p. 14 / 4.3. Experimental Results - extractive body cue:** This figure presents the success rate, cycle time, and intervention rates for both HIL-SERL and DAgger across few representative tasks, displayed as a running average ...
- **p. 15 / 4.3. Experimental Results - extractive body cue:** 1, HIL-SERL achieved a success rate of 100% within 1 to 2.5 hours of real-world training on nearly all the tasks.
- **p. 10 / 4.2. Description of Tasks - extractive body cue:** HIL-SERL: Precise and Dexterous Robotic Manipulation via Human-in-the-Loop Reinforcement Learning I J F G H K
- **p. 14 / 4.3. Experimental Results - extractive body cue:** For HG-DAgger, the success rate fluctuates throughout training episodes and does not necessarily increase as training progresses.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** multi-robot demonstration/dataset ecosystem.
- **Input boundary:** multi-view observation, language/task label과 action trajectory.
- **Output/decision under evaluation:** dataset sample 또는 learned policy action.
- **Primary target:** coverage, cross-embodiment transfer, data efficiency와 task success.
- **Detected evaluation headings:** 4. Experiment Results (p. 9); 4.1. Overview of Experiments (p. 9); 4.3. Experimental Results (p. 13); 4.4. Robustness Results (p. 15); 5. Result Analysis (p. 17).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.3. Experimental Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | This is a significant improvement over the HG-DAgger baseline, which achieved an average success rate of 49.7% across all tasks. | p. 15 (4.3. Experimental Results) |
| 4.3. Experimental Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | 1, HIL-SERL achieved a success rate of 100% within 1 to 2.5 hours of real-world training on nearly all the tasks. | p. 15 (4.3. Experimental Results) |
| 5. Result Analysis | EMPIRICAL / REAL-ROBOT OR HARDWARE | We examine why the learned policies consistently achieve high success rates across diverse tasks, investigating the factors that contribute to their robustness. | p. 17 (5. Result Analysis) |
| 5.1. Reliability of the Learned Policies | EMPIRICAL / REAL-ROBOT OR HARDWARE | In contrast, imitation learning approaches, including interactive methods, lack this self-correction mechanism, making it significantly more challenging to achieve comparable performance with the same ... | p. 18 (5.1. Reliability of the Learned Policies) |
| 5.1. Reliability of the Learned Policies | EMPIRICAL / REAL-ROBOT OR HARDWARE | Consequently, to achieve similar performance, DAgger may require significantly more demonstrations and corrections, as well as careful attention from the human operator to ensure ... | p. 19 (5.1. Reliability of the Learned Policies) |

## Dataset / Benchmark Role

- **p. 9 / 4.1. Overview of Experiments - extractive body cue:** Each task also uses either a scripted robot motion or manually human reset to randomize the initial state of the task.
- **p. 9 / 4.1. Overview of Experiments - extractive body cue:** We solve these tasks by utilizing either a single robot arm or a dual-arm setup, together with various combinations of observations and actions.
- **p. 13 / 4.3. Experimental Results - extractive body cue:** For all tasks, BC baselines were trained using HG-DAgger with the same number of episodes and interventions as RL.
- **p. 13 / 4.3. Experimental Results - extractive body cue:** Diffusion Policy (DP) and BC are trained with 200 demonstrations, while HG-DAgger is trained with the same number of episodes and interventions as RL.
- **p. 14 / 4.3. Experimental Results - extractive body cue:** This figure presents the success rate, cycle time, and intervention rates for both HIL-SERL and DAgger across few representative tasks, displayed as a running average ...
- **p. 15 / 4.3. Experimental Results - extractive body cue:** 1, HIL-SERL achieved a success rate of 100% within 1 to 2.5 hours of real-world training on nearly all the tasks.
- **p. 10 / 4.2. Description of Tasks - extractive body cue:** HIL-SERL: Precise and Dexterous Robotic Manipulation via Human-in-the-Loop Reinforcement Learning I J F G H K
- **p. 14 / 4.3. Experimental Results - extractive body cue:** For HG-DAgger, the success rate fluctuates throughout training episodes and does not necessarily increase as training progresses.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: Overview of experimental tasks. A subset of tasks considered in this paper, they include whipping out a Jenga block from its tower, flipping ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 2: Overview of HIL-SERL. This figure illustrates the architecture of HIL-SERL, which comprises three primary components: the actor process, the learner process, and replay ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 3: This diagram illustrates the process for training HIL-SERL. First, we tele-operate the robot to collect positive and negative samples and train a binary ...
- **p. 10 / Figure/Table caption - extractive body cue:** Figure 4: Illustrations of the tasks in our experiments. (A)-(E) A sequence of motherboard assembly tasks: SSD installation, RAM insertion, USB cable grasping and insertion ...
- **p. 13 / Figure/Table caption - extractive body cue:** Table 1: Experiment results. (a) HIL-SERL against imitation learning baselines. (b) HIL-SERL against various other baselines. In this subsection, we present the experimental results for ...
- **p. 14 / Figure/Table caption - extractive body cue:** Figure 5: Learning curves for experimental tasks. This figure presents the success rate, cycle time, and intervention rates for both HIL-SERL and DAgger across few ...
- **p. 16 / Figure/Table caption - extractive body cue:** Figure 6: Robustness evaluation for policies learned by our method. (A) RAM insertion under external perturbations, such as a moving motherboard. (B) Retrying behavior during ...
- **p. 18 / Figure/Table caption - extractive body cue:** Figure 7: Visualization of policy training dynamics. (A) State visitation heatmaps during HIL-SERL training: The policy progressively forms a "funnel" shape, concentrating more on areas ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Each task also uses either a scripted robot motion or manually human reset to randomize the initial state of the task. | embodiment, simulator version and control stack | p. 9 (4.1. Overview of Experiments), p. 9 (4.1. Overview of Experiments) |
| Task/environment | We solve these tasks by utilizing either a single robot arm or a dual-arm setup, together with various combinations of observations and actions. | reset, timeout, object/scene variation | p. 9 (4.1. Overview of Experiments), p. 13 (4.3. Experimental Results) |
| Observation/sensor | multi-view observation, language/task label과 action trajectory | calibration, preprocessing, privileged input | p. 4 (3.1. Preliminaries and Problem Statement), p. 5 (3.1. Preliminaries and Problem Statement) |
| Output/decision | dataset sample 또는 learned policy action | action frame, controller and termination | p. 5 (3.1. Preliminaries and Problem Statement), p. 2 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Figure 3: This diagram illustrates the process for training HIL-SERL. First, we tele-operate the robot to collect positive and negative samples and train a ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| We examine why the learned policies consistently achieve high success rates across diverse tasks, investigating the factors that contribute to their robustness. | definition/direction/unit from same section | p. 17 (5. Result Analysis) |
| One key aspect of HIL-SERL's performance is its high reliability, achieving a 100% success rate across all tasks. | definition/direction/unit from same section | p. 18 (5.1. Reliability of the Learned Policies) |
| For each task, we report the success rate, cycle time, and training time. | definition/direction/unit from same section | p. 13 (4.3. Experimental Results) |
| In all our experiments, we use success rates and cycle time as primary metrics to compare different methods. | definition/direction/unit from same section | p. 14 (4.3. Experimental Results) |
| For HG-DAgger, the success rate fluctuates throughout training episodes and does not necessarily increase as training progresses. | definition/direction/unit from same section | p. 14 (4.3. Experimental Results) |
| 1, HIL-SERL achieved a success rate of 100% within 1 to 2.5 hours of real-world training on nearly all the tasks. | definition/direction/unit from same section | p. 15 (4.3. Experimental Results) |
| This is a significant improvement over the HG-DAgger baseline, which achieved an average success rate of 49.7% across all tasks. | definition/direction/unit from same section | p. 15 (4.3. Experimental Results) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| In the remainder of this section, we will first describe each task in detail, and present relevant results as well as comparisons to other ... | comparison identity and matched condition | p. 9 (4.1. Overview of Experiments) |
| (b) HIL-SERL against various other baselines. | comparison identity and matched condition | p. 13 (4.3. Experimental Results) |
| (a) HIL-SERL against imitation learning baselines. | comparison identity and matched condition | p. 13 (4.3. Experimental Results) |
| For these tasks, we instead collect 50 and 200 offline demonstrations and train BC policies as baselines. | comparison identity and matched condition | p. 14 (4.3. Experimental Results) |
| Therefore, we compare our approach to imitation learning by training a baseline with HG-DAgger (Kelly et al., 2018), using the same amount of human ... | comparison identity and matched condition | p. 14 (4.3. Experimental Results) |
| Our method outperforms HG-DAgger due to key advantages of RL. | comparison identity and matched condition | p. 15 (4.3. Experimental Results) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Our method is also ablated with two versions: one initialized from scratch without demonstrations or corrections, and another initialized from demonstrations but without corrections. | component/input/data sensitivity | p. 13 (4.3. Experimental Results) |
| DAgger and its variants (Ross et al., 2011; Kelly et al., 2018) address this problem by incorporating human corrections to refine the policy through ... | component/input/data sensitivity | p. 14 (4.3. Experimental Results) |
| Figure 4: Illustrations of the tasks in our experiments. (A)-(E) A sequence of motherboard assembly tasks: SSD installation, RAM insertion, USB cable grasping and ... | component/input/data sensitivity | p. 10 (Figure/Table caption) |
| These tasks encompass a range of manipulation challenges, including dynamic object manipulation (e.g., flipping an object in a pan), precise and delicate manipulation (e.g., ... | component/input/data sensitivity | p. 9 (4.1. Overview of Experiments) |
| We first pretrain a base policy with behavioral cloning (BC) using an equivalent amount of offline human demonstrations as provided to our method. | component/input/data sensitivity | p. 14 (4.3. Experimental Results) |
| Figure 2: Overview of HIL-SERL. This figure illustrates the architecture of HIL-SERL, which comprises three primary components: the actor process, the learner process, and ... | component/input/data sensitivity | p. 6 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To assess the effectiveness of our system, we compare it against several state-of-the-art RL methods and conduct ablation studies to understand the contribution of ... | This is a significant improvement over the HG-DAgger baseline, which achieved an average success rate of 49.7% across all tasks. | PDF body cue; verify exact table/figure and matched conditions | p. 15 (4.3. Experimental Results), p. 15 (4.3. Experimental Results), p. 17 (5. Result Analysis), p. 18 (5.1. Reliability of the Learned Policies), p. 19 (5.1. Reliability of the Learned Policies), p. 18 (5.1. Reliability of the Learned Policies) |
| Primary metric/result | 1, HIL-SERL achieved a success rate of 100% within 1 to 2.5 hours of real-world training on nearly all the tasks. | numeric claim only at cited anchor | p. 15 (4.3. Experimental Results) |

- Numeric sentences retained from the body:
- **p. 13 / 4.3. Experimental Results - extractive body cue:** All metrics were reported over 100 trials per task, except for the IKEA whole assembly task, which involved 10 trials.
- **p. 13 / 4.3. Experimental Results - extractive body cue:** Task DP HG-DAgger BC IBRL Residual RL DAPG HIL-SERL no demo no itv HIL-SERL no itv HIL-SERL (ours) RAM Insertion 27 29 12 75 0 ...
- **p. 13 / 4.3. Experimental Results - extractive body cue:** The training time includes all scripted motion, policy rollouts, intended stops, as well as onboard computation which is carried on a single NVIDIA RTX 4090 ...
- **p. 14 / 4.3. Experimental Results - extractive body cue:** This figure presents the success rate, cycle time, and intervention rates for both HIL-SERL and DAgger across few representative tasks, displayed as a running average ...
- **p. 15 / 4.3. Experimental Results - extractive body cue:** 1, HIL-SERL achieved a success rate of 100% within 1 to 2.5 hours of real-world training on nearly all the tasks.
- **p. 15 / 4.3. Experimental Results - extractive body cue:** Specifically, we report the intervention rate, for which we calculate the ratio of intervened timesteps to total timesteps within an episode and report a running ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | We also see some limitations of our approach. | p. 21 (6. Discussion) |
| body limitation/failure cue | For all tasks, unless otherwise noted, we trained a binary classifier as reward detector, it takes images from wrist and/or side cameras as inputs, ... | p. 9 (4.1. Overview of Experiments) |
| body limitation/failure cue | We argue this reliability comes from reinforcement learning's inherent ability to self-correct through policy sampling, allowing the agent to continuously improve by learning from ... | p. 18 (5.1. Reliability of the Learned Policies) |
| body limitation/failure cue | We see a number of opportunities for future work. | p. 21 (6. Discussion) |
| body limitation/failure cue | Figure 6: Robustness evaluation for policies learned by our method. (A) RAM insertion under external perturbations, such as a moving motherboard. (B) Retrying behavior ... | p. 16 (Figure/Table caption) |
| body limitation/failure cue | For HG-DAgger, the success rate fluctuates throughout training episodes and does not necessarily increase as training progresses. | p. 14 (4.3. Experimental Results) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The training time includes all scripted motion, policy rollouts, intended stops, as well as onboard computation which is carried on a single NVIDIA RTX ... | p. 13 (4.3. Experimental Results) |
| We then run this policy and collect human expert corrections, such that the total amount of trials and interventions matches RL training. | p. 14 (4.3. Experimental Results) |
| For each task, we report the success rate, cycle time, and training time. | p. 13 (4.3. Experimental Results) |
| Additionally, it achieves such performance within practical training times, even for highdimensional observations and action spaces, such as those required for bimanual manipulation. | p. 15 (4.3. Experimental Results) |
| Using our data collection pipeline, as detailed in the supplementary code, it usually takes around 5 minutes to collect these data points. | p. 8 (3.5. Training Process) |
| To articulate the training process of our system and assist readers in reproducing our results, we provide a detailed walkthrough of the steps involved ... | p. 8 (3.5. Training Process) |
| Specifically, we run it for the same number of episodes as our method and aim to provide a comparable number of interventions per episode. | p. 14 (4.3. Experimental Results) |
| Specifically, we report the intervention rate, for which we calculate the ratio of intervened timesteps to total timesteps within an episode and report a ... | p. 15 (4.3. Experimental Results) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 21 / 6. Discussion - extractive body cue:** We also see some limitations of our approach.
- **p. 9 / 4.1. Overview of Experiments - extractive body cue:** For all tasks, unless otherwise noted, we trained a binary classifier as reward detector, it takes images from wrist and/or side cameras as inputs, and ...
- **p. 18 / 5.1. Reliability of the Learned Policies - extractive body cue:** We argue this reliability comes from reinforcement learning's inherent ability to self-correct through policy sampling, allowing the agent to continuously improve by learning from both ...
- **p. 21 / 6. Discussion - extractive body cue:** We see a number of opportunities for future work.
- **p. 16 / Figure/Table caption - extractive body cue:** Figure 6: Robustness evaluation for policies learned by our method. (A) RAM insertion under external perturbations, such as a moving motherboard. (B) Retrying behavior during ...
- **p. 14 / 4.3. Experimental Results - extractive body cue:** For HG-DAgger, the success rate fluctuates throughout training episodes and does not necessarily increase as training progresses.

- **PDF anchors reviewed:** datasets p. 9 (4.1. Overview of Experiments), p. 9 (4.1. Overview of Experiments), p. 13 (4.3. Experimental Results), p. 13 (4.3. Experimental Results), p. 14 (4.3. Experimental Results), p. 15 (4.3. Experimental Results), metrics p. 8 (Figure/Table caption), p. 17 (5. Result Analysis), p. 18 (5.1. Reliability of the Learned Policies), p. 13 (4.3. Experimental Results), p. 14 (4.3. Experimental Results), p. 14 (4.3. Experimental Results), baselines p. 9 (4.1. Overview of Experiments), p. 13 (4.3. Experimental Results), p. 13 (4.3. Experimental Results), p. 14 (4.3. Experimental Results), p. 14 (4.3. Experimental Results), p. 15 (4.3. Experimental Results), results p. 15 (4.3. Experimental Results), p. 15 (4.3. Experimental Results), p. 17 (5. Result Analysis), p. 18 (5.1. Reliability of the Learned Policies), p. 19 (5.1. Reliability of the Learned Policies), p. 18 (5.1. Reliability of the Learned Policies).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
