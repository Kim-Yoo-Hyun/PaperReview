# Evaluation - AtomicVLA: Unlocking the Potential of Atomic Skill Learning in Robots

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_AtomicVLA_Unlocking_the_Potential_of_Atomic_Skill_Learning_in_Robots_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_AtomicVLA_Unlocking_the_Potential_of_Atomic_Skill_Learning_in_Robots_CVPR_2026_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (4.4. Ablation Study), p. 6 (Figure/Table caption), p. 6 (4.2. Results on Simulation), p. 7 (4.2. Results on Simulation), p. 8 (4.3. Results on Real-world Robot), p. 7 (4.3. Results on Real-world Robot)): 5, AtomicVLA achieves a success rate of 95.2%, outperforming the MoE baseline by 6.6% and the timestep-conditioned MoDE variant by 5.7%.

## Evaluation Body Digest

- **p. 6 / 4.1. Experiments Setup - extractive body cue:** We use 5 skill experts for both the LIBERO benchmark suite and real-world robot experiments.
- **p. 6 / 4.1. Experiments Setup - extractive body cue:** We conduct real-world experiments using a Franka robotic arm, which includes three long-horizon tasks and five different types of short tasks.
- **p. 7 / 4.3. Results on Real-world Robot - extractive body cue:** Previous real-world studies on robotic manipulation typically focus on training and evaluating a single specific task, while joint training across multiple heterogeneous tasks has been ...
- **p. 5 / 4.1. Experiments Setup - extractive body cue:** We evaluate AtomicVLA and AtomicVLA* on two widely adopted robotic manipulation benchmarks: LIBERO [25] and CALVIN [29].
- **p. 5 / 4.1. Experiments Setup - extractive body cue:** For the LIBERO benchmark, we assess model performance across all four task suites.
- **p. 7 / 4.2. Results on Simulation - extractive body cue:** However, due to the evaluation constraints of the CALVIN benchmark, successful recoveries after failures are not considered valid completions, which prevents subsequent tasks from being ...
- **p. 8 / 4.4. Ablation Study - extractive body cue:** We conduct ablation experiments on the LIBERO-LONG benchmark to evaluate the effectiveness of our skill-aware routing mechanism.
- **p. 8 / 4.3. Results on Real-world Robot - extractive body cue:** The top two rows illustrate skill interference in long-horizon tasks: the first shows successful single-skill executions, while the second shows failures after mixed training.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 4. Experiments (p. 5); 4.1. Experiments Setup (p. 5); 4.2. Results on Simulation (p. 6); 4.3. Results on Real-world Robot (p. 7).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.4. Ablation Study | EMPIRICAL / REAL-ROBOT OR HARDWARE | 5, AtomicVLA achieves a success rate of 95.2%, outperforming the MoE baseline by 6.6% and the timestep-conditioned MoDE variant by 5.7%. | p. 8 (4.4. Ablation Study) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 4. Error Recovery Capability Demonstration. When encountering a skill execution failure, AtomicVLA automatically assesses the progress and re-executes the current skill. suites, outperforming ... | p. 6 (Figure/Table caption) |
| 4.2. Results on Simulation | EMPIRICAL / REAL-ROBOT OR HARDWARE | 1, AtomicVLA achieves an average success rate of 96.6% across the four Calvin LIBERO Figure 4. | p. 6 (4.2. Results on Simulation) |
| 4.2. Results on Simulation | EMPIRICAL / REAL-ROBOT OR HARDWARE | 2, AtomicVLA achieves an average task length of 4.09, outperforming the π0 baseline by 0.22, while AtomicVLA* reaches an average task length of 4.27, ... | p. 7 (4.2. Results on Simulation) |
| 4.3. Results on Real-world Robot | EMPIRICAL / REAL-ROBOT OR HARDWARE | Red and green boxes highlight the key differences. number of training steps, AtomicVLA* acquires new skills more efficiently and achieves an overall improvement of ... | p. 8 (4.3. Results on Real-world Robot) |

## Dataset / Benchmark Role

- **p. 6 / 4.1. Experiments Setup - extractive body cue:** We use 5 skill experts for both the LIBERO benchmark suite and real-world robot experiments.
- **p. 6 / 4.1. Experiments Setup - extractive body cue:** We conduct real-world experiments using a Franka robotic arm, which includes three long-horizon tasks and five different types of short tasks.
- **p. 7 / 4.3. Results on Real-world Robot - extractive body cue:** Previous real-world studies on robotic manipulation typically focus on training and evaluating a single specific task, while joint training across multiple heterogeneous tasks has been ...
- **p. 5 / 4.1. Experiments Setup - extractive body cue:** We evaluate AtomicVLA and AtomicVLA* on two widely adopted robotic manipulation benchmarks: LIBERO [25] and CALVIN [29].
- **p. 5 / 4.1. Experiments Setup - extractive body cue:** For the LIBERO benchmark, we assess model performance across all four task suites.
- **p. 7 / 4.2. Results on Simulation - extractive body cue:** However, due to the evaluation constraints of the CALVIN benchmark, successful recoveries after failures are not considered valid completions, which prevents subsequent tasks from being ...
- **p. 8 / 4.4. Ablation Study - extractive body cue:** We conduct ablation experiments on the LIBERO-LONG benchmark to evaluate the effectiveness of our skill-aware routing mechanism.
- **p. 8 / 4.3. Results on Real-world Robot - extractive body cue:** The top two rows illustrate skill interference in long-horizon tasks: the first shows successful single-skill executions, while the second shows failures after mixed training.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Overview of AtomicVLA. Unlike previous VLA mod- els with a single action head, which suffer from limited scalabil- ity and severe interference among ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. (a) AtomicVLA Pipline. AtomicVLA is a framework that unifies task planning and action execution. The VLM adaptively predicts atomic skill abstraction and latent ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3. Inference Example of AtomicVLA. We visualize two tasks from LIBERO-LONG. For each task, the top row shows the task progression, and the bottom ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Comparison of Different Methods on LIBERO Benchmark(%).
- **p. 6 / Figure/Table caption - extractive body cue:** Table 2. Long-horizon Robotic Manipulation Evaluation on CALVIN Benchmark(%).
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4. Error Recovery Capability Demonstration. When encountering a skill execution failure, AtomicVLA automatically assesses the progress and re-executes the current skill. suites, outperforming the ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5. Demonstrations show the execution process of AtomicVLA* (second row) and baselines π0.5 (first row).
- **p. 7 / Figure/Table caption - extractive body cue:** Table 3. Long-horizon Multi-task Experiments(%). InP, IntoD, and IntoM stand for Objects in plate, Object into drawer, Object into microwave, respectively.

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We use 5 skill experts for both the LIBERO benchmark suite and real-world robot experiments. | embodiment, simulator version and control stack | p. 6 (4.1. Experiments Setup), p. 6 (4.1. Experiments Setup) |
| Task/environment | We conduct real-world experiments using a Franka robotic arm, which includes three long-horizon tasks and five different types of short tasks. | reset, timeout, object/scene variation | p. 6 (4.1. Experiments Setup), p. 7 (4.3. Results on Real-world Robot) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 4 (3.2. Unified Task Planning and Action Execution), p. 4 (3.2. Unified Task Planning and Action Execution) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 2 (1. Introduction), p. 2 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Figure 4. Error Recovery Capability Demonstration. When encountering a skill execution failure, AtomicVLA automatically assesses the progress and re-executes the current skill. suites, outperforming ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| 1, AtomicVLA achieves an average success rate of 96.6% across the four Calvin LIBERO Figure 4. | definition/direction/unit from same section | p. 6 (4.2. Results on Simulation) |
| 4, the average success rate of π0.5 decreases by approximately 15%, with the stack task exhibiting the most severe interference, showing a 20% decrease. | definition/direction/unit from same section | p. 7 (4.3. Results on Real-world Robot) |
| 5, AtomicVLA achieves a success rate of 95.2%, outperforming the MoE baseline by 6.6% and the timestep-conditioned MoDE variant by 5.7%. | definition/direction/unit from same section | p. 8 (4.4. Ablation Study) |
| 4, we also observe that AtomicVLA exhibits a capability for error recovery in experiments. | definition/direction/unit from same section | p. 7 (4.2. Results on Simulation) |
| The top two rows illustrate skill interference in long-horizon tasks: the first shows successful single-skill executions, while the second shows failures after mixed training. | definition/direction/unit from same section | p. 8 (4.3. Results on Real-world Robot) |
| For the LIBERO benchmark, we assess model performance across all four task suites. | definition/direction/unit from same section | p. 5 (4.1. Experiments Setup) |
| Figure 1. Overview of AtomicVLA. Unlike previous VLA mod- els with a single action head, which suffer from limited scalabil- ity and severe interference ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| When encountering a skill execution failure, AtomicVLA automatically assesses the progress and re-executes the current skill. suites, outperforming the strong baseline by 2.4%. | comparison identity and matched condition | p. 6 (4.2. Results on Simulation) |
| 3, AtomicVLA and AtomicVLA* outperform the baseline model by 20% and 18.3%, respectively. | comparison identity and matched condition | p. 7 (4.3. Results on Real-world Robot) |
| 2, AtomicVLA achieves an average task length of 4.09, outperforming the π0 baseline by 0.22, while AtomicVLA* reaches an average task length of 4.27, ... | comparison identity and matched condition | p. 7 (4.2. Results on Simulation) |
| 5, AtomicVLA achieves a success rate of 95.2%, outperforming the MoE baseline by 6.6% and the timestep-conditioned MoDE variant by 5.7%. | comparison identity and matched condition | p. 8 (4.4. Ablation Study) |
| Red and green boxes highlight the key differences. number of training steps, AtomicVLA* acquires new skills more efficiently and achieves an overall improvement of ... | comparison identity and matched condition | p. 8 (4.3. Results on Real-world Robot) |
| Comparison of Different Methods on LIBERO Benchmark(%). | comparison identity and matched condition | p. 6 (4.1. Experiments Setup) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We conduct ablation experiments on the LIBERO-LONG benchmark to evaluate the effectiveness of our skill-aware routing mechanism. | component/input/data sensitivity | p. 8 (4.4. Ablation Study) |
| As a result, each expert still learns a mixture of skills without clear specialization. | component/input/data sensitivity | p. 8 (4.4. Ablation Study) |
| We build AtomicVLA and AtomicVLA* upon the pretrained \pi _ 0 and \pi _{0.5} foundation model. | component/input/data sensitivity | p. 6 (4.1. Experiments Setup) |
| Specifically, we first perform mixed training on four short-horizon tasks and train the "open" skill independently on top of the pretrained model. | component/input/data sensitivity | p. 7 (4.3. Results on Real-world Robot) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Overall, our contributions are as follows: • We introduce AtomicVLA, an end-to-end framework that unifies task planning and action execution for longhorizon tasks and ... | 5, AtomicVLA achieves a success rate of 95.2%, outperforming the MoE baseline by 6.6% and the timestep-conditioned MoDE variant by 5.7%. | PDF body cue; verify exact table/figure and matched conditions | p. 8 (4.4. Ablation Study), p. 6 (Figure/Table caption), p. 6 (4.2. Results on Simulation), p. 7 (4.2. Results on Simulation), p. 8 (4.3. Results on Real-world Robot), p. 7 (4.3. Results on Real-world Robot) |
| Primary metric/result | Figure 4. Error Recovery Capability Demonstration. When encountering a skill execution failure, AtomicVLA automatically assesses the progress and re-executes the current skill. suites, outperforming ... | numeric claim only at cited anchor | p. 6 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 6 / 4.1. Experiments Setup - extractive body cue:** For each shorthorizon task, we collect 50 trajectories, while each longhorizon task contains 100 trajectories, resulting in a total of 550 real-world demonstration trajectories.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 4. Error Recovery Capability Demonstration. When encountering a skill execution failure, AtomicVLA automatically assesses the progress and re-executes the current skill. suites, outperforming ... | p. 6 (Figure/Table caption) |
| body limitation/failure cue | Figure 6. Mixed-Training Skill Interference and Continual- Learning Degradation. The top two rows illustrate skill interfer- ence in long-horizon tasks: the first shows successful ... | p. 8 (Figure/Table caption) |
| body limitation/failure cue | Importantly, when an execution failure occurs, for example, the butter is grasped but subsequently dropped as illustrated in Fig. | p. 6 (4.2. Results on Simulation) |
| body limitation/failure cue | However, due to the evaluation constraints of the CALVIN benchmark, successful recoveries after failures are not considered valid completions, which prevents subsequent tasks from ... | p. 7 (4.2. Results on Simulation) |
| body limitation/failure cue | AtomicVLA* reliably completes the experimental configurations that π0.5 fails to accomplish, and this advantage becomes more evident in tasks involving door-closing operations. | p. 7 (4.3. Results on Real-world Robot) |
| body limitation/failure cue | Notably, it effectively mitigates skill interference arising from joint training and alleviates knowledge forgetting and performance degradation during continual skill acquisition, highlighting its significant ... | p. 8 (5. Conclusion) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Further implementation details are provided in the Appendix. | p. 6 (4.1. Experiments Setup) |
| Red and green boxes highlight the key differences. number of training steps, AtomicVLA* acquires new skills more efficiently and achieves an overall improvement of ... | p. 8 (4.3. Results on Real-world Robot) |
| Moreover, this notable performance gain demonstrates that routing experts based on semantically meaningful atomic skills, rather than on individual action tokens or denoising steps, ... | p. 8 (4.4. Ablation Study) |
| Typically, this mode is activated only at key time steps, such as task initiation or during the transition between sub-skills. | p. 4 (3.2. Unified Task Planning and Action Execution) |
| The router computes a probability distribution over experts as: w _{k} = \tex t {Ro ut e r } ( Z_\sigma ), \quad k ... | p. 4 (3.3. Skill-guided Mixture of Experts Architecture) |
| By aligning these refined labels with the full trajectory, we construct a structured reasoning chain comprising the sequence of executed atomic actions and the ... | p. 5 (3.5. Task Planning Embodied Data Generation) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4. Error Recovery Capability Demonstration. When encountering a skill execution failure, AtomicVLA automatically assesses the progress and re-executes the current skill. suites, outperforming the ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 6. Mixed-Training Skill Interference and Continual- Learning Degradation. The top two rows illustrate skill interfer- ence in long-horizon tasks: the first shows successful single-skill ...
- **p. 6 / 4.2. Results on Simulation - extractive body cue:** Importantly, when an execution failure occurs, for example, the butter is grasped but subsequently dropped as illustrated in Fig.
- **p. 7 / 4.2. Results on Simulation - extractive body cue:** However, due to the evaluation constraints of the CALVIN benchmark, successful recoveries after failures are not considered valid completions, which prevents subsequent tasks from being ...
- **p. 7 / 4.3. Results on Real-world Robot - extractive body cue:** AtomicVLA* reliably completes the experimental configurations that π0.5 fails to accomplish, and this advantage becomes more evident in tasks involving door-closing operations.
- **p. 8 / 5. Conclusion - extractive body cue:** Notably, it effectively mitigates skill interference arising from joint training and alleviates knowledge forgetting and performance degradation during continual skill acquisition, highlighting its significant potential ...

- **PDF anchors reviewed:** datasets p. 6 (4.1. Experiments Setup), p. 6 (4.1. Experiments Setup), p. 7 (4.3. Results on Real-world Robot), p. 5 (4.1. Experiments Setup), p. 5 (4.1. Experiments Setup), p. 7 (4.2. Results on Simulation), metrics p. 6 (Figure/Table caption), p. 6 (4.2. Results on Simulation), p. 7 (4.3. Results on Real-world Robot), p. 8 (4.4. Ablation Study), p. 7 (4.2. Results on Simulation), p. 8 (4.3. Results on Real-world Robot), baselines p. 6 (4.2. Results on Simulation), p. 7 (4.3. Results on Real-world Robot), p. 7 (4.2. Results on Simulation), p. 8 (4.4. Ablation Study), p. 8 (4.3. Results on Real-world Robot), p. 6 (4.1. Experiments Setup), results p. 8 (4.4. Ablation Study), p. 6 (Figure/Table caption), p. 6 (4.2. Results on Simulation), p. 7 (4.2. Results on Simulation), p. 8 (4.3. Results on Real-world Robot), p. 7 (4.3. Results on Real-world Robot).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
