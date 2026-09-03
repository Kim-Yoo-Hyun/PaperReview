# Evaluation - Human2LocoMan: Learning Versatile Quadrupedal Manipulation with Human Pretraining

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p122.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p122.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 10 (Figure/Table caption), p. 1 (Figure/Table caption), p. 7 (IV. EXPERIMENTS), p. 10 (Figure/Table caption)): Fig. 6: Substep success rate. The success rate for some substep is calcuated as the percentage of trials where the robot success- fully completed the substep. For each task, we ...

## Evaluation Body Digest

- **p. 8 / IV. EXPERIMENTS - extractive body cue:** Both unimanual and bimanual toy collection tasks assess the robot's ability to grasp objects of varying shapes, colors, and positions.
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** We use 10 objects for robot finetuning, while all objects are included in human pretraining and real-robot evaluation.
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** In this task, the robot must pick up a toy randomly positioned within a rectangular area and place it into a designated basket on the ...
- **p. 8 / IV. EXPERIMENTS - extractive body cue:** This task evaluates the coordination and precision of the robot's bimanual manipulation.
- **p. 10 / Figure/Table caption - extractive body cue:** Fig. 6: Substep success rate. The success rate for some substep is calcuated as the percentage of trials where the robot success- fully completed the ...
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** (3) How does human data collected by Human2LocoMan contribute to imitation learning performance?
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** Completing this task requires the robot to coordinate its whole-body motions to efficiently and accurately reach various locations on the ground and above the basket.
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 2: Human2LocoMan framework. Our system uses an XR headset for data collection, capturing egocentric human data and teleoperated robot data, all mapped to a ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** legged robot, terrain과 contact dynamics.
- **Input boundary:** proprioception, terrain/perception observation과 velocity command.
- **Output/decision under evaluation:** joint target, torque, footstep 또는 locomotion action.
- **Primary target:** velocity/progress, stability, energy와 terrain generalization.
- **Detected evaluation headings:** IV. EXPERIMENTS (p. 7).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Fig. 6: Substep success rate. The success rate for some substep is calcuated as the percentage of trials where the robot success- fully completed ... | p. 10 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Fig. 1: Human2LocoMan provides a unified framework for collecting human demonstrations and teleoperated robot whole- body motions, along with cross-embodiment policy learning for quadrupedal ... | p. 1 (Figure/Table caption) |
| IV. EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | (3) How does human data collected by Human2LocoMan contribute to imitation learning performance? | p. 7 (IV. EXPERIMENTS) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Fig. 5: Ablation study on unimanual and bimanual toy collection. We compare MXT, its ablation MXT-Agg, and baseline HPT on SR and TS. Here, ... | p. 10 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 8 / IV. EXPERIMENTS - extractive body cue:** Both unimanual and bimanual toy collection tasks assess the robot's ability to grasp objects of varying shapes, colors, and positions.
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** We use 10 objects for robot finetuning, while all objects are included in human pretraining and real-robot evaluation.
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** In this task, the robot must pick up a toy randomly positioned within a rectangular area and place it into a designated basket on the ...
- **p. 8 / IV. EXPERIMENTS - extractive body cue:** This task evaluates the coordination and precision of the robot's bimanual manipulation.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: Human2LocoMan provides a unified framework for collecting human demonstrations and teleoperated robot whole- body motions, along with cross-embodiment policy learning for quadrupedal manipulation. ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 2: Human2LocoMan framework. Our system uses an XR headset for data collection, capturing egocentric human data and teleoperated robot data, all mapped to a ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 3: Modularized Cross-embodiment Transformer (MXT) architecture. The inputs are organized as a list of modalities and encoded each by a separate tokenizer into a ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 4: Rollouts of the MXT policy and the objects used across manipulation tasks in our experiments. Green arrows indicate end-effector motions, red arrows denote ...
- **p. 10 / Figure/Table caption - extractive body cue:** Fig. 5: Ablation study on unimanual and bimanual toy collection. We compare MXT, its ablation MXT-Agg, and baseline HPT on SR and TS. Here, "L" ...
- **p. 10 / Figure/Table caption - extractive body cue:** Fig. 6: Substep success rate. The success rate for some substep is calcuated as the percentage of trials where the robot success- fully completed the ...
- **p. 11 / Figure/Table caption - extractive body cue:** Fig. 7: Best validation loss of our method and HIT on all our tasks. MXT-Pretrained: MXT pretrained on human dataset (including unimanual and bimanual if ...
- **p. 11 / Figure/Table caption - extractive body cue:** Fig. 8: Best validation loss of our method and HPT on the unimanual Toy Collection task. MXT-Pretrained: MXT pre- trained on human dataset (including unimanual ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Both unimanual and bimanual toy collection tasks assess the robot's ability to grasp objects of varying shapes, colors, and positions. | embodiment, simulator version and control stack | p. 8 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS) |
| Task/environment | We use 10 objects for robot finetuning, while all objects are included in human pretraining and real-robot evaluation. | reset, timeout, object/scene variation | p. 7 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS) |
| Observation/sensor | proprioception, terrain/perception observation과 velocity command | calibration, preprocessing, privileged input | p. 6 (III. METHODOLOGY), p. 6 (III. METHODOLOGY) |
| Output/decision | joint target, torque, footstep 또는 locomotion action | action frame, controller and termination | p. 5 (III. METHODOLOGY), p. 7 (III. METHODOLOGY) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Fig. 6: Substep success rate. The success rate for some substep is calcuated as the percentage of trials where the robot success- fully completed ... | definition/direction/unit from same section | p. 10 (Figure/Table caption) |
| (3) How does human data collected by Human2LocoMan contribute to imitation learning performance? | definition/direction/unit from same section | p. 7 (IV. EXPERIMENTS) |
| Completing this task requires the robot to coordinate its whole-body motions to efficiently and accurately reach various locations on the ground and above the ... | definition/direction/unit from same section | p. 7 (IV. EXPERIMENTS) |
| This task evaluates the coordination and precision of the robot's bimanual manipulation. | definition/direction/unit from same section | p. 8 (IV. EXPERIMENTS) |
| Fig. 2: Human2LocoMan framework. Our system uses an XR headset for data collection, capturing egocentric human data and teleoperated robot data, all mapped to ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| Fig. 1: Human2LocoMan provides a unified framework for collecting human demonstrations and teleoperated robot whole- body motions, along with cross-embodiment policy learning for quadrupedal ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Fig. 3: Modularized Cross-embodiment Transformer (MXT) architecture. The inputs are organized as a list of modalities and encoded each by a separate tokenizer into ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| Fig. 7: Best validation loss of our method and HIT on all our tasks. MXT-Pretrained: MXT pretrained on human dataset (including unimanual and bimanual ... | definition/direction/unit from same section | p. 11 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| (2) How does MXT compare to state-of-the-art imitation learning architectures? | comparison identity and matched condition | p. 7 (IV. EXPERIMENTS) |
| Fig. 5: Ablation study on unimanual and bimanual toy collection. We compare MXT, its ablation MXT-Agg, and baseline HPT on SR and TS. Here, ... | comparison identity and matched condition | p. 10 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| The unimanual variant emphasizes coordination between the torso and end-effector, while the bimanual variant highlights synchronized control of two loco-manipulators. | component/input/data sensitivity | p. 8 (IV. EXPERIMENTS) |
| The unimanual variant additionally requires torso articulation to reach shoes placed at different heights. | component/input/data sensitivity | p. 8 (IV. EXPERIMENTS) |
| Fig. 5: Ablation study on unimanual and bimanual toy collection. We compare MXT, its ablation MXT-Agg, and baseline HPT on SR and TS. Here, ... | component/input/data sensitivity | p. 10 (Figure/Table caption) |
| We use 10 objects for robot finetuning, while all objects are included in human pretraining and real-robot evaluation. | component/input/data sensitivity | p. 7 (IV. EXPERIMENTS) |
| Fig. 1: Human2LocoMan provides a unified framework for collecting human demonstrations and teleoperated robot whole- body motions, along with cross-embodiment policy learning for quadrupedal ... | component/input/data sensitivity | p. 1 (Figure/Table caption) |
| Fig. 2: Human2LocoMan framework. Our system uses an XR headset for data collection, capturing egocentric human data and teleoperated robot data, all mapped to ... | component/input/data sensitivity | p. 4 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In summary, our paper provides the following contributions: • We propose Human2LocoMan, a framework that enables flexible and scalable collection of human demonstrations and ... | Fig. 6: Substep success rate. The success rate for some substep is calcuated as the percentage of trials where the robot success- fully completed ... | PDF body cue; verify exact table/figure and matched conditions | p. 10 (Figure/Table caption), p. 1 (Figure/Table caption), p. 7 (IV. EXPERIMENTS), p. 10 (Figure/Table caption) |
| Primary metric/result | Fig. 1: Human2LocoMan provides a unified framework for collecting human demonstrations and teleoperated robot whole- body motions, along with cross-embodiment policy learning for quadrupedal ... | numeric claim only at cited anchor | p. 1 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** As shown in Figure 4, we use 10 objects for robot finetuning and all objects for human pretraining and real-robot evaluation.
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** We use 10 objects for robot finetuning, while all objects are included in human pretraining and real-robot evaluation.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | MXT-Scratch: MXT trained only on the LocoMan data. "L" denotes the larger training set (80 trajectories for SO-Uni, 60 trajectories for Pour and Scoop), ... | p. 10 (3) Data) |
| body limitation/failure cue | Additionally, as depicted in Figure 8, MXT-Pretrained consistently achieves lower validation loss than MXT-Scratch, whereas the gap between HPT-Pretrained and HPT-Scratch is less consistent ... | p. 11 (3) Data) |
| body limitation/failure cue | As shown in Figure 4, this task involves three pairs of shoes, with one pair being out-of-distribution (OOD). | p. 7 (IV. EXPERIMENTS) |
| body limitation/failure cue | The policy is rolled out for 24 times with in-distribution (ID) objects and 12 times with out-of-distribution (OOD) objects. | p. 9 (3) Data) |
| body limitation/failure cue | Efficiency, robustness, and generalizability. | p. 11 (3) Data) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Set finetuning learning rate ηfinetune for step = 1, 2, ... do ▷Finetuning Stage Sample a batch B from DLocoMan Compute LLocoMan(B) = P ... | p. 7 (III. METHODOLOGY) |
| The substeps of this task include: push the shoe, and tap the shoe. • Unimanual Scooping (Scoop-Uni). | p. 7 (IV. EXPERIMENTS) |
| The substeps of this task include: pick up both cups, pour the ball, and place both cups. | p. 8 (IV. EXPERIMENTS) |
| For image inputs, the features are obtained from a pretrained ResNet encoder that can be finetuned during training; for proprioceptive or state-like inputs, the ... | p. 5 (III. METHODOLOGY) |
| In this section, we present the design and implementation of our system, Human2LocoMan, which integrates teleoperation, data collection, and a Transformer-based architecture for cross-embodied ... | p. 3 (III. METHODOLOGY) |
| To detect selfcollisions, we utilize the Pinocchio library [83] to compute collision pairs among the robot's body parts. | p. 5 (III. METHODOLOGY) |
| We refer the reader to Appendix Section A for more implementation details. | p. 6 (III. METHODOLOGY) |
| All the encoded modalities are concatenated to compose the input tokens to the Transformer trunk. | p. 6 (III. METHODOLOGY) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 10 / 3) Data - extractive body cue:** MXT-Scratch: MXT trained only on the LocoMan data. "L" denotes the larger training set (80 trajectories for SO-Uni, 60 trajectories for Pour and Scoop), while ...
- **p. 11 / 3) Data - extractive body cue:** Additionally, as depicted in Figure 8, MXT-Pretrained consistently achieves lower validation loss than MXT-Scratch, whereas the gap between HPT-Pretrained and HPT-Scratch is less consistent and ...
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** As shown in Figure 4, this task involves three pairs of shoes, with one pair being out-of-distribution (OOD).
- **p. 9 / 3) Data - extractive body cue:** The policy is rolled out for 24 times with in-distribution (ID) objects and 12 times with out-of-distribution (OOD) objects.
- **p. 11 / 3) Data - extractive body cue:** Efficiency, robustness, and generalizability.

- **Evidence anchors reviewed:** datasets p. 8 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 8 (IV. EXPERIMENTS), metrics p. 10 (Figure/Table caption), p. 7 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 8 (IV. EXPERIMENTS), p. 4 (Figure/Table caption), p. 1 (Figure/Table caption), baselines p. 7 (IV. EXPERIMENTS), p. 10 (Figure/Table caption), results p. 10 (Figure/Table caption), p. 1 (Figure/Table caption), p. 7 (IV. EXPERIMENTS), p. 10 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
