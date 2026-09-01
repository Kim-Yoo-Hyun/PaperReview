# Evaluation - CoA-VLA: Improving Vision-Language-Action Models via Visual-Text Chain-of-Affordance

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Li_CoA-VLA_Improving_Vision-Language-Action_Models_via_Visual-Text_Chain-of-Affordance_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Li_CoA-VLA_Improving_Vision-Language-Action_Models_via_Visual-Text_Chain-of-Affordance_ICCV_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (5.2. Evaluation on Simulation), p. 7 (5.2. Evaluation on Simulation), p. 6 (Figure/Table caption), p. 8 (5.3. More Experiments), p. 8 (5.3. More Experiments), p. 1 (Figure/Table caption)): Specifically, CoA-VLA achieves an overall success rate of 79.8%, outperforming OpenVLA, the previous best-performing method, by a margin of 3.3%.

## Evaluation Body Digest

- **p. 7 / 5.2. Evaluation on Simulation - extractive PDF cue:** LIBERO is a robot learning benchmark comprising over 130 language-conditioned manipulation tasks.
- **p. 7 / 5. Experiments - extractive PDF cue:** 2) What is the performance of CoAVLA in simulation benchmarks?
- **p. 8 / 5.3. More Experiments - extractive PDF cue:** CoAVLA can avoid obstacles and operate safely. robot is presented with a plate on which three distinct objects are already placed, and it is instructed ...
- **p. 8 / 5.3. More Experiments - extractive PDF cue:** In the second task, we introduced a series of obstacles on a table, rearranging them in different configurations to assess the robot's adaptability in maneuvering ...
- **p. 8 / 5.3. More Experiments - extractive PDF cue:** We report the success rate and standard error for four task suites.
- **p. 7 / 5.2. Evaluation on Simulation - extractive PDF cue:** Our findings indicate that CoA-VLA consistently achieves superior performance across all evaluated settings, securing the highest success rate among the methods tested.
- **p. 8 / 5.3. More Experiments - extractive PDF cue:** This experiment underscores the crucial role of spatial affordance in enhancing the model's ability to recognize and utilize available space, ultimately improving task completion accuracy ...
- **p. 7 / 5.1. Evaluation on Real Robot - extractive PDF cue:** In the in-distribution setup, our method surpasses all SOTA robot foundation models in terms of average success rate.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SIMULATION`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 5. Experiments (p. 7); 5.1. Evaluation on Real Robot (p. 7); 5.2. Evaluation on Simulation (p. 7); 5.3. More Experiments (p. 7).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 5.2. Evaluation on Simulation | EMPIRICAL / SIMULATION | Specifically, CoA-VLA achieves an overall success rate of 79.8%, outperforming OpenVLA, the previous best-performing method, by a margin of 3.3%. | p. 7 (5.2. Evaluation on Simulation) |
| 5.2. Evaluation on Simulation | EMPIRICAL / SIMULATION | Our findings indicate that CoA-VLA consistently achieves superior performance across all evaluated settings, securing the highest success rate among the methods tested. | p. 7 (5.2. Evaluation on Simulation) |
| Figure/Table caption | EMPIRICAL / SIMULATION | Table 1. Experimental results for multi-task learning. Our method achieved the best performance in both the in-distribution test setup and under visual changes. Seven ... | p. 6 (Figure/Table caption) |
| 5.3. More Experiments | EMPIRICAL / SIMULATION | We report the success rate and standard error for four task suites. | p. 8 (5.3. More Experiments) |
| 5.3. More Experiments | EMPIRICAL / SIMULATION | LIBERO-Spatial LIBERO-Object LIBERO-Goal LIBERO-Long Average Method / Task Success Rate (↗) Success Rate (↗) Success Rate (↗) Success Rate (↗) Success Rate (↗) Diffusion ... | p. 8 (5.3. More Experiments) |

## Dataset / Benchmark Role

- **p. 7 / 5.2. Evaluation on Simulation - extractive PDF cue:** LIBERO is a robot learning benchmark comprising over 130 language-conditioned manipulation tasks.
- **p. 7 / 5. Experiments - extractive PDF cue:** 2) What is the performance of CoAVLA in simulation benchmarks?
- **p. 8 / 5.3. More Experiments - extractive PDF cue:** CoAVLA can avoid obstacles and operate safely. robot is presented with a plate on which three distinct objects are already placed, and it is instructed ...
- **p. 8 / 5.3. More Experiments - extractive PDF cue:** In the second task, we introduced a series of obstacles on a table, rearranging them in different configurations to assess the robot's adaptability in maneuvering ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. This figure illustrates the overall framework of our CoA-VLA model, which empowers vision-language-action models with chain-of-thought reasoning capabilities for generalizable visuomotor policy learning. ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2. An example of the chain-of-affordance for the PourTea task. The first row presents the text affordance and the second row shows the visual ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 3. Robot setup and examples for real-world manipulation tasks. We evaluate seven real-world tasks on Franka robot arm equipped with two external Zed cameras ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 1. Experimental results for multi-task learning. Our method achieved the best performance in both the in-distribution test setup and under visual changes. Seven Tasks ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 2. Experimental results for LIBERO benchmark. We report the success rate and standard error for four task suites. LIBERO-Spatial LIBERO-Object LIBERO-Goal LIBERO-Long Average Method ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 4. Spatial affordance for CoA-VLA. CoA-VLA can identify free space for object placement.. Method \ Obstacle Avoidance OpenVLA DiffusionVLA CoA-VLA
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 5. Movement generalization for CoA-VLA. CoA- VLA can avoid obstacles and operate safely. robot is presented with a plate on which three distinct ob- ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | LIBERO is a robot learning benchmark comprising over 130 language-conditioned manipulation tasks. | embodiment, simulator version and control stack | p. 7 (5.2. Evaluation on Simulation), p. 7 (5. Experiments) |
| Task/environment | 2) What is the performance of CoAVLA in simulation benchmarks? | reset, timeout, object/scene variation | p. 7 (5. Experiments), p. 8 (5.3. More Experiments) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 3 (4.1. Definition of Chain-of-Affordance), p. 5 (4.1. Definition of Chain-of-Affordance) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 5 (4.1. Definition of Chain-of-Affordance), p. 2 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We report the success rate and standard error for four task suites. | definition/direction/unit from same section | p. 8 (5.3. More Experiments) |
| Our findings indicate that CoA-VLA consistently achieves superior performance across all evaluated settings, securing the highest success rate among the methods tested. | definition/direction/unit from same section | p. 7 (5.2. Evaluation on Simulation) |
| This experiment underscores the crucial role of spatial affordance in enhancing the model's ability to recognize and utilize available space, ultimately improving task completion ... | definition/direction/unit from same section | p. 8 (5.3. More Experiments) |
| In the in-distribution setup, our method surpasses all SOTA robot foundation models in terms of average success rate. | definition/direction/unit from same section | p. 7 (5.1. Evaluation on Real Robot) |
| Figure 1. This figure illustrates the overall framework of our CoA-VLA model, which empowers vision-language-action models with chain-of-thought reasoning capabilities for generalizable visuomotor policy ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Table 1. Experimental results for multi-task learning. Our method achieved the best performance in both the in-distribution test setup and under visual changes. Seven ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Compared to our baseline model, which employs vanilla reasoning, our method achieves a 14.29% increase in accuracy. | comparison identity and matched condition | p. 7 (5.1. Evaluation on Real Robot) |
| 4) How important is our proposed visual-textual affordance approach, compared to the vanilla VLA? | comparison identity and matched condition | p. 7 (5. Experiments) |
| Our method successfully identifies open areas on the plate, allowing it to accurately position the bread without interference, thereby enabling CoA-VLA to complete all ... | comparison identity and matched condition | p. 8 (5.3. More Experiments) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Detailed descriptions of each task and the experimental setup, and our ablation experiments are provided in the Appendix. | component/input/data sensitivity | p. 7 (5.1. Evaluation on Real Robot) |
| We use the Droid dataset [21] as an external data source, filtering out samples without language annotations, leaving 39K trajectories. | component/input/data sensitivity | p. 7 (5.1. Evaluation on Real Robot) |
| Our method successfully identifies open areas on the plate, allowing it to accurately position the bread without interference, thereby enabling CoA-VLA to complete all ... | component/input/data sensitivity | p. 8 (5.3. More Experiments) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In this work, we propose Chain-of-Affordance, namely CoA-VLA, a novel perspective on generalizing model reasoning at test-time, and leverage such generated reasoning to facilitate ... | Specifically, CoA-VLA achieves an overall success rate of 79.8%, outperforming OpenVLA, the previous best-performing method, by a margin of 3.3%. | PDF body cue; verify exact table/figure and matched conditions | p. 7 (5.2. Evaluation on Simulation), p. 7 (5.2. Evaluation on Simulation), p. 6 (Figure/Table caption), p. 8 (5.3. More Experiments), p. 8 (5.3. More Experiments), p. 1 (Figure/Table caption) |
| Primary metric/result | Our findings indicate that CoA-VLA consistently achieves superior performance across all evaluated settings, securing the highest success rate among the methods tested. | numeric claim only at cited anchor | p. 7 (5.2. Evaluation on Simulation) |

- Numeric sentences retained from the body:
- **p. 7 / 5.1. Evaluation on Real Robot - extractive PDF cue:** The model is then post-trained on 692 trajectories across seven tasks.
- **p. 8 / 5.3. More Experiments - extractive PDF cue:** LIBERO-Spatial LIBERO-Object LIBERO-Goal LIBERO-Long Average Method / Task Success Rate (↗) Success Rate (↗) Success Rate (↗) Success Rate (↗) Success Rate (↗) Diffusion Policy ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Our approach successfully completed all three scenarios, demonstrating robust collision avoidance and spatial adaptability. | p. 8 (5.3. More Experiments) |
| body limitation/failure cue | Collision avoidance is essential for safe and effective physical interactions, as improper maneuvers can lead to significant damage or even catastrophic outcomes. | p. 8 (5.3. More Experiments) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| All models are trained with the same number of iterations, and the last checkpoint is used for evaluation. | p. 7 (5.1. Evaluation on Real Robot) |
| We follow the setting as in OpenVLA [22] opensourced code and test on four task suites: LIBERO-Spatial, LIBERO-Goal, LIBERO-Object, and LIBERO-Long. | p. 7 (5.2. Evaluation on Simulation) |
| The encoder's output embeddings are projected into the diffusion model using FiLM conditioning layers, inspired by MT-ACT [4]. | p. 5 (4.1. Definition of Chain-of-Affordance) |
| This approach encodes affordances by overlaying coordinate markers (e.g., bounding boxes, interaction points) or motion trajectories onto the robot's historical observation frames (Figure 2, ... | p. 5 (4.1. Definition of Chain-of-Affordance) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 5.3. More Experiments - extractive PDF cue:** Our approach successfully completed all three scenarios, demonstrating robust collision avoidance and spatial adaptability.
- **p. 8 / 5.3. More Experiments - extractive PDF cue:** Collision avoidance is essential for safe and effective physical interactions, as improper maneuvers can lead to significant damage or even catastrophic outcomes.

- **PDF anchors reviewed:** datasets p. 7 (5.2. Evaluation on Simulation), p. 7 (5. Experiments), p. 8 (5.3. More Experiments), p. 8 (5.3. More Experiments), metrics p. 8 (5.3. More Experiments), p. 7 (5.2. Evaluation on Simulation), p. 8 (5.3. More Experiments), p. 7 (5.1. Evaluation on Real Robot), p. 1 (Figure/Table caption), p. 6 (Figure/Table caption), baselines p. 7 (5.1. Evaluation on Real Robot), p. 7 (5. Experiments), p. 8 (5.3. More Experiments), results p. 7 (5.2. Evaluation on Simulation), p. 7 (5.2. Evaluation on Simulation), p. 6 (Figure/Table caption), p. 8 (5.3. More Experiments), p. 8 (5.3. More Experiments), p. 1 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
