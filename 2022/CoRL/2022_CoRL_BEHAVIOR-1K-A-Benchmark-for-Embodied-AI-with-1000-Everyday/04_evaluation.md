# Evaluation - BEHAVIOR-1K: A Benchmark for Embodied AI with 1,000 Everyday Activities and Realistic Simulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (43 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v205/li23s.html; PDF retrieval source: https://arxiv.org/pdf/2403.09227. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (Figure/Table caption), p. 8 (Method), p. 8 (Figure/Table caption), p. 7 (Method), p. 4 (C C), p. 6 (C C)): Table 2: Task success rates across three baseline methods. RL-VMC with end-to-end visuomotor control completely fails to solve any of the activities, whereas RL-Prim. and RL-Prim.Hist. with action primitives are ...

## Evaluation Body Digest

- **p. 2 / 1 Introduction - extractive PDF cue:** The survey reveals systematicity in what activities people want robots to do, but more importantly, highlights two key factors that we should prioritize when designing ...
- **p. 2 / 1 Introduction - extractive PDF cue:** Developing simulation environments is a natural alternative: one can train and test robotic agents in many activities with diverse scenes, objects, and conditions efficiently and ...
- **p. 1 / Abstract - extractive PDF cue:** We present BEHAVIOR-1K, a comprehensive simulation benchmark for human-centered robotics.
- **p. 3 / 6. Clean a shower - extractive PDF cue:** For instance, instruction-following benchmarks such as VirtualHome [20] and ALFRED [20, 21] are diverse in the number of scenes, objects, and state changes, but offer ...
- **p. 4 / C C - extractive PDF cue:** Left: BEHAVIOR-1K DATASET includes 1,000 BDDL activity definitions (top left), 50 realistic and diverse scenes (top right), and 9,000+ objects with properties annotated in the ...
- **p. 3 / 6. Clean a shower - extractive PDF cue:** To create a benchmark that reflects these needs, we conduct a survey targeting the general U.S. population that asks: what do you want robots to ...
- **p. 4 / C C - extractive PDF cue:** Our benchmark comprises two elements: BEHAVIOR-1K DATASET and OMNIGIBSON.
- **p. 1 / Abstract - extractive PDF cue:** To calibrate the simulation-to-reality gap of BEHAVIOR-1K, we provide an initial study on transferring solutions learned with a mobile manipulator in a simulated apartment to ...

## Evaluation Type and Scope

- **Evaluation type:** `BENCHMARK / DATASET`.
- **Target system/task:** defined robot simulator/hardware task suite.
- **Input boundary:** standardized observation, action, task state와 evaluation split.
- **Output/decision under evaluation:** policy/controller trajectory 또는 measured result.
- **Primary target:** success metric, robustness, generalization과 reproducibility.
- **Detected evaluation headings:** not reliably recovered.

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | BENCHMARK / DATASET | Table 2: Task success rates across three baseline methods. RL-VMC with end-to-end visuomotor control completely fails to solve any of the activities, whereas RL-Prim. ... | p. 7 (Figure/Table caption) |
| Method | BENCHMARK / DATASET | We achieve different success rates in simulation (50 runs, ∼40% success) and in the real world with optimal (27 runs, ∼22%) and trained policies ... | p. 8 (Method) |
| Figure/Table caption | BENCHMARK / DATASET | Table 3: Efficiency metrics across three base- line methods. RL-VMC has low spatial and temporal efficiency because it fails to learn, whereas history information ... | p. 8 (Figure/Table caption) |
| Method | BENCHMARK / DATASET | Following the metrics proposed in BEHAVIOR-100 [27], we report the success rate and efficiency metrics (distance traveled, time invested, and disarrangement caused) in Table ... | p. 7 (Method) |
| C C | BENCHMARK / DATASET | The realism achieved in rendering by OMNIGIBSON for BEHAVIOR-1K is also significantly higher than what was possible in BEHAVIOR-100 and other benchmarks (see Fig. | p. 4 (C C) |

## Dataset / Benchmark Role

- **p. 2 / 1 Introduction - extractive PDF cue:** The survey reveals systematicity in what activities people want robots to do, but more importantly, highlights two key factors that we should prioritize when designing ...
- **p. 2 / 1 Introduction - extractive PDF cue:** Developing simulation environments is a natural alternative: one can train and test robotic agents in many activities with diverse scenes, objects, and conditions efficiently and ...
- **p. 1 / Abstract - extractive PDF cue:** We present BEHAVIOR-1K, a comprehensive simulation benchmark for human-centered robotics.
- **p. 3 / 6. Clean a shower - extractive PDF cue:** For instance, instruction-following benchmarks such as VirtualHome [20] and ALFRED [20, 21] are diverse in the number of scenes, objects, and state changes, but offer ...
- **p. 4 / C C - extractive PDF cue:** Left: BEHAVIOR-1K DATASET includes 1,000 BDDL activity definitions (top left), 50 realistic and diverse scenes (top right), and 9,000+ objects with properties annotated in the ...
- **p. 3 / 6. Clean a shower - extractive PDF cue:** To create a benchmark that reflects these needs, we conduct a survey targeting the general U.S. population that asks: what do you want robots to ...
- **p. 4 / C C - extractive PDF cue:** Our benchmark comprises two elements: BEHAVIOR-1K DATASET and OMNIGIBSON.
- **p. 1 / Abstract - extractive PDF cue:** To calibrate the simulation-to-reality gap of BEHAVIOR-1K, we provide an initial study on transferring solutions learned with a mobile manipulator in a simulated apartment to ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 1: Developing a Human-Centered Benchmark for Embodied AI. Left: human preference score over 2,090 activities, ranked based on a survey on 1,461 participants. The ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Table 1: Comparison of Embodied AI Benchmarks: BEHAVIOR-1K contains 1,000 diverse activities that are grounded by human needs. It achieves a new level of diversity ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2: Elements of BEHAVIOR-1K. Our benchmark comprises two elements: BEHAVIOR-1K DATASET and OMNIGIBSON. Left: BEHAVIOR-1K DATASET includes 1,000 BDDL activity definitions (top left), 50 ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 3: Comparison of Visual Realism: We evaluate OMNIGIBSON's visual realism against other simulation environments by running a survey with 60 human subjects. We ask ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 4: Objects and States in Activity Definitions: Left: the number of activities unlocked by each simulation capability that OMNIGIBSON has. None of the other ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 2: Task success rates across three baseline methods. RL-VMC with end-to-end visuomotor control completely fails to solve any of the activities, whereas RL-Prim. and ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 3: Efficiency metrics across three base- line methods. RL-VMC has low spatial and temporal efficiency because it fails to learn, whereas history information helps ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 4: Ablation study of RL-Prim. on the impact of removing the simplifying assumptions of grasping and motion execution during evaluation. We observe a large ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The survey reveals systematicity in what activities people want robots to do, but more importantly, highlights two key factors that we should prioritize when ... | embodiment, simulator version and control stack | p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Task/environment | Developing simulation environments is a natural alternative: one can train and test robotic agents in many activities with diverse scenes, objects, and conditions efficiently ... | reset, timeout, object/scene variation | p. 2 (1 Introduction), p. 1 (Abstract) |
| Observation/sensor | standardized observation, action, task state와 evaluation split | calibration, preprocessing, privileged input | p. 7 (Method), p. 7 (Method) |
| Output/decision | policy/controller trajectory 또는 measured result | action frame, controller and termination | p. 8 (Method), p. 2 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Following the metrics proposed in BEHAVIOR-100 [27], we report the success rate and efficiency metrics (distance traveled, time invested, and disarrangement caused) in Table ... | definition/direction/unit from same section | p. 7 (Method) |
| Table 2: Task success rates across three baseline methods. RL-VMC with end-to-end visuomotor control completely fails to solve any of the activities, whereas RL-Prim. ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| We achieve different success rates in simulation (50 runs, ∼40% success) and in the real world with optimal (27 runs, ∼22%) and trained policies ... | definition/direction/unit from same section | p. 8 (Method) |
| Table 3: Efficiency metrics across three base- line methods. RL-VMC has low spatial and temporal efficiency because it fails to learn, whereas history information ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Figure 3: Comparison of Visual Realism: We evaluate OMNIGIBSON's visual realism against other simulation environments by running a survey with 60 human subjects. We ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| Figure 1: Developing a Human-Centered Benchmark for Embodied AI. Left: human preference score over 2,090 activities, ranked based on a survey on 1,461 participants. ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |
| 1 (left), in which we rank the activities based on their human preference score. | definition/direction/unit from same section | p. 3 (6. Clean a shower) |
| To calibrate the simulation-to-reality gap of BEHAVIOR-1K, we provide an initial study on transferring solutions learned with a mobile manipulator in a simulated apartment ... | definition/direction/unit from same section | p. 1 (Abstract) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We evaluate three different baselines based on state-of-the-art reinforcement learning algorithms (RL) [60]: • RL-VMC, a visuomotor control (from image to low-level joint commands) ... | comparison identity and matched condition | p. 7 (Method) |
| Our experiments indicate that the activities in BEHAVIOR-1K are long-horizon and dependent on complex manipulation skills, both of which remain a challenge for even ... | comparison identity and matched condition | p. 1 (Abstract) |
| Our analysis indicates that even a single activity in BEHAVIOR-1K is extremely challenging for current AI algorithms, and the baselines can only solve it ... | comparison identity and matched condition | p. 2 (1 Introduction) |
| We evaluate state-of-the-art reinforcement learning algorithms [47, 48] in several activities of BEHAVIOR-1K, both with visuomotor control in the original action space, and with ... | comparison identity and matched condition | p. 2 (1 Introduction) |
| This is unprecedented compared to other benchmarks (see Table 1). | comparison identity and matched condition | p. 5 (C C) |
| These features significantly boost the realism of BEHAVIOR-1K compared to other benchmarks. | comparison identity and matched condition | p. 6 (C C) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We include an ablation analysis of the effect of these assumptions and simplifications in our evaluation (see Table 4). | component/input/data sensitivity | p. 7 (Method) |
| Table 4: Ablation study of RL-Prim. on the impact of removing the simplifying assumptions of grasping and motion execution during evaluation. We observe a ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| Realism Task success rate Grasping Full Motion StoreDecoration CollectTrash CleanTable Ë Ë 0.0 ± 0.0 0.0 ± 0.0 0.0 ± 0.0 é Ë 0.46 ... | component/input/data sensitivity | p. 8 (Method) |
| Finally, annotators and researchers also create transition rules, e.g., turning tomatoes and salt into sauces, or requiring sandpaper to remove rust. | component/input/data sensitivity | p. 5 (C C) |
| Indeed, without these features, over half of BEHAVIOR-1K activities would not be simulatable, highlighting how crucial these features are for capturing everyday activities. | component/input/data sensitivity | p. 6 (C C) |
| All agents are trained with a sparse task success reward without any reward engineering. | component/input/data sensitivity | p. 7 (Method) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In this work, we present BEHAVIOR-1K, a Benchmark of 1,000 Everyday Household Activities in Virtual, Interactive, and Ecological Environments-the next generation of BEHAVIOR-100 [27]. | Table 2: Task success rates across three baseline methods. RL-VMC with end-to-end visuomotor control completely fails to solve any of the activities, whereas RL-Prim. ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (Figure/Table caption), p. 8 (Method), p. 8 (Figure/Table caption), p. 7 (Method), p. 4 (C C), p. 6 (C C) |
| Primary metric/result | We achieve different success rates in simulation (50 runs, ∼40% success) and in the real world with optimal (27 runs, ∼22%) and trained policies ... | numeric claim only at cited anchor | p. 8 (Method) |

- Numeric sentences retained from the body:
- **p. 1 / Abstract - extractive PDF cue:** The first is the definition of 1,000 everyday activities, grounded in 50 scenes (houses, gardens, restaurants, offices, etc.) with more than 9,000 objects annotated with ...
- **p. 2 / 1 Introduction - extractive PDF cue:** The BEHAVIOR-1K DATASET is a large-scale dataset comprising 1) a commonsense knowledge base for 1,000 activities with definitions in predicate logic (initial and goal conditions), ...
- **p. 4 / 6. Clean a shower - extractive PDF cue:** T2 (OCRTOC) IKEA Furniture Assembly RLBench Metaworld Robosuite SoftGym DeepMind Control Suite OpenAIGym Habitat 1.0 Gibson Mobile manipulation Static manipulation Navigation Activities from human preference ...
- **p. 4 / C C - extractive PDF cue:** Furthermore, BEHAVIOR-100 includes only 15 scenes (all houses) and 300+ object categories, while BEHAVIOR-1K increases to 50 scenes (houses, stores, restaurants, offices, etc.) and 1,900+ ...
- **p. 5 / C C - extractive PDF cue:** OMNIGIBSON 3.20 ± 1.23 Habitat 2.0 1.74 ± 1.33 AI2-THOR 1.73 ± 1.37 iGibson 2.0 1.69 ± 1.24 ThreeDWorld 1.65 ± 1.23 Figure 3: Comparison ...
- **p. 6 / C C - extractive PDF cue:** Several top-10 object synsets are fluids and flexible materials, necessitating the development of OMNIGIBSON.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | The failure cases are depicted in Fig. | p. 8 (Method) |
| body limitation/failure cue | 6.1), policy failures (i.e., selecting the wrong action primitive) dominate. | p. 8 (Method) |
| body limitation/failure cue | RL-VMC with end-to-end visuomotor control completely fails to solve any of the activities, whereas RL-Prim. and RL-Prim.Hist. with action primitives are able achieve decent ... | p. 7 (Method) |
| body limitation/failure cue | Furthermore, to accelerate training, the action primitives check only the feasibility (e.g., reachability, collisions) of the final configuration, e.g. the grasping pose for pick ... | p. 7 (Method) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Karen Liu1,8, Jiajun Wu1,8, Li Fei-Fei1,8 Department of Computer Science1, Department of Mechanical Engineering2 Neurosciences IDP3, Department of Aeronautics and Astronautics4 Institute for Computational ... | p. 1 (Front matter) |
| Inspired by the progress that benchmarking brought to computer vision [1-11] and natural language processing [12-16], the robotics community has developed several benchmarks in ... | p. 2 (1 Introduction) |
| We observe that longer-horizon activities are more challenging: while CleanTable can be accomplished by executing the optimal sequence of 6 primitive steps, CollectTrash requires ... | p. 7 (Method) |
| The policy outputs a discrete selection of a primitive applied on an object; • RL-Prim.Hist., a variant of RL-Prim. that takes in the history ... | p. 7 (Method) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / Method - extractive PDF cue:** The failure cases are depicted in Fig.
- **p. 8 / Method - extractive PDF cue:** 6.1), policy failures (i.e., selecting the wrong action primitive) dominate.
- **p. 7 / Method - extractive PDF cue:** RL-VMC with end-to-end visuomotor control completely fails to solve any of the activities, whereas RL-Prim. and RL-Prim.Hist. with action primitives are able achieve decent performance.
- **p. 7 / Method - extractive PDF cue:** Furthermore, to accelerate training, the action primitives check only the feasibility (e.g., reachability, collisions) of the final configuration, e.g. the grasping pose for pick or ...

- **PDF anchors reviewed:** datasets p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (Abstract), p. 3 (6. Clean a shower), p. 4 (C C), p. 3 (6. Clean a shower), metrics p. 7 (Method), p. 7 (Figure/Table caption), p. 8 (Method), p. 8 (Figure/Table caption), p. 5 (Figure/Table caption), p. 3 (Figure/Table caption), baselines p. 7 (Method), p. 1 (Abstract), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 5 (C C), p. 6 (C C), results p. 7 (Figure/Table caption), p. 8 (Method), p. 8 (Figure/Table caption), p. 7 (Method), p. 4 (C C), p. 6 (C C).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
