# Evaluation - Goal-VLA: Image-Generative VLMs As Object-Centric World Models Empowering Zero-Shot Robot Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (9 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_4.html; PDF retrieval source: https://arxiv.org/pdf/2506.23919. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (IV. EXPERIMENT), p. 7 (IV. EXPERIMENT), p. 7 (IV. EXPERIMENT), p. 6 (IV. EXPERIMENT), p. 1 (Figure/Table caption)): Our method, Goal-VLA, achieves a remarkable average success rate of 59.9%, significantly outperforming all baselines across a diverse set of eight manipulation tasks.

## Evaluation Body Digest

- **p. 5 / IV. EXPERIMENT - extractive PDF cue:** Q3: Can our framework generalize across diverse environments, tasks, object categories, and robot embodiments?
- **p. 7 / IV. EXPERIMENT - extractive PDF cue:** The framework's success across diverse tasks, objects, and environments (simulated and real), combined with its zeroshot deployment on different robot embodiments, demonstrates strong generalization, providing ...
- **p. 5 / IV. EXPERIMENT - extractive PDF cue:** The robot arm is fixed to a tabletop, and for each task, objects are placed in randomized
- **p. 6 / IV. EXPERIMENT - extractive PDF cue:** For detailed descriptions of our simulation and real-world tasks, please refer to the Appendix B and C.
- **p. 6 / IV. EXPERIMENT - extractive PDF cue:** We design four distinct real-world tasks to evaluate a range of core manipulation capabilities: Place Tomato in Pan, a foundational pick-and-place task requiring reasoning about ...
- **p. 7 / IV. EXPERIMENT - extractive PDF cue:** Real World Experiments (Q3) Our framework is tested on four diverse real-world manipulation tasks to validate its practical applicability.
- **p. 6 / IV. EXPERIMENT - extractive PDF cue:** Our method, Goal-VLA, achieves a remarkable average success rate of 59.9%, significantly outperforming all baselines across a diverse set of eight manipulation tasks.
- **p. 6 / IV. EXPERIMENT - extractive PDF cue:** For each seed, which defines a unique initial scene arrangement, we conduct 10 independent trials of each method, resulting in 100 evaluation runs per task ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** IV. EXPERIMENT (p. 5).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| IV. EXPERIMENT | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our method, Goal-VLA, achieves a remarkable average success rate of 59.9%, significantly outperforming all baselines across a diverse set of eight manipulation tasks. | p. 6 (IV. EXPERIMENT) |
| IV. EXPERIMENT | EMPIRICAL / REAL-ROBOT OR HARDWARE | As shown in Table III, our method achieves a 60% average success rate, significantly outperforming baselines like MOKA (22.5%) and MolmoAct (27.5%). | p. 7 (IV. EXPERIMENT) |
| IV. EXPERIMENT | EMPIRICAL / REAL-ROBOT OR HARDWARE | Starting from a 40.0% success rate for the baseline model, adding Input Enhancement provides the most significant single improvement (+27.5pp), while the Reflector alone ... | p. 7 (IV. EXPERIMENT) |
| IV. EXPERIMENT | EMPIRICAL / REAL-ROBOT OR HARDWARE | For each seed, which defines a unique initial scene arrangement, we conduct 10 independent trials of each method, resulting in 100 evaluation runs per ... | p. 6 (IV. EXPERIMENT) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 1: Goal-VLA maps a single-view RGB-D image and a language instruction to executable manipulation actions. Our approach employs an object-centric world model to ... | p. 1 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 5 / IV. EXPERIMENT - extractive PDF cue:** Q3: Can our framework generalize across diverse environments, tasks, object categories, and robot embodiments?
- **p. 7 / IV. EXPERIMENT - extractive PDF cue:** The framework's success across diverse tasks, objects, and environments (simulated and real), combined with its zeroshot deployment on different robot embodiments, demonstrates strong generalization, providing ...
- **p. 5 / IV. EXPERIMENT - extractive PDF cue:** The robot arm is fixed to a tabletop, and for each task, objects are placed in randomized
- **p. 6 / IV. EXPERIMENT - extractive PDF cue:** For detailed descriptions of our simulation and real-world tasks, please refer to the Appendix B and C.
- **p. 6 / IV. EXPERIMENT - extractive PDF cue:** We design four distinct real-world tasks to evaluate a range of core manipulation capabilities: Place Tomato in Pan, a foundational pick-and-place task requiring reasoning about ...
- **p. 7 / IV. EXPERIMENT - extractive PDF cue:** Real World Experiments (Q3) Our framework is tested on four diverse real-world manipulation tasks to validate its practical applicability.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Fig. 1: Goal-VLA maps a single-view RGB-D image and a language instruction to executable manipulation actions. Our approach employs an object-centric world model to generate ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Fig. 2: Overview of the Goal-VLA framework, which decouples the manipulation pipeline into three stages: (a) Goal State Reasoning: A VLM generates a goal image ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Fig. 3: An example of our Reflection-through-Synthesis process, which corrects a semantically correct but infeasible goal by refining the generation prompt.
- **p. 7 / Figure/Table caption - extractive PDF cue:** Fig. 4: Ablation Study. The performance of our full model ("World Model w/ Instruction & max 3 Reflection"), shown by the purple line, surpasses all ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Fig. 5: Visualizations of Real-World Experiments. Figure 5 provides qualitative evidence for these findings. The visualizations illustrate how the generated goal image captures the task's ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Q3: Can our framework generalize across diverse environments, tasks, object categories, and robot embodiments? | embodiment, simulator version and control stack | p. 5 (IV. EXPERIMENT), p. 7 (IV. EXPERIMENT) |
| Task/environment | The framework's success across diverse tasks, objects, and environments (simulated and real), combined with its zeroshot deployment on different robot embodiments, demonstrates strong generalization, ... | reset, timeout, object/scene variation | p. 7 (IV. EXPERIMENT), p. 5 (IV. EXPERIMENT) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 3 (III. METHOD), p. 4 (III. METHOD) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 4 (III. METHOD), p. 2 (I. INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Our method, Goal-VLA, achieves a remarkable average success rate of 59.9%, significantly outperforming all baselines across a diverse set of eight manipulation tasks. | definition/direction/unit from same section | p. 6 (IV. EXPERIMENT) |
| For each seed, which defines a unique initial scene arrangement, we conduct 10 independent trials of each method, resulting in 100 evaluation runs per ... | definition/direction/unit from same section | p. 6 (IV. EXPERIMENT) |
| As shown in Table III, our method achieves a 60% average success rate, significantly outperforming baselines like MOKA (22.5%) and MolmoAct (27.5%). | definition/direction/unit from same section | p. 7 (IV. EXPERIMENT) |
| Starting from a 40.0% success rate for the baseline model, adding Input Enhancement provides the most significant single improvement (+27.5pp), while the Reflector alone ... | definition/direction/unit from same section | p. 7 (IV. EXPERIMENT) |
| Fig. 1: Goal-VLA maps a single-view RGB-D image and a language instruction to executable manipulation actions. Our approach employs an object-centric world model to ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Fig. 2: Overview of the Goal-VLA framework, which decouples the manipulation pipeline into three stages: (a) Goal State Reasoning: A VLM generates a goal ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| In this section, we conduct comprehensive experiments and analyses to answer the following key questions: Q1: How well does our proposed method perform compared ... | comparison identity and matched condition | p. 5 (IV. EXPERIMENT) |
| Our method, Goal-VLA, achieves a remarkable average success rate of 59.9%, significantly outperforming all baselines across a diverse set of eight manipulation tasks. | comparison identity and matched condition | p. 6 (IV. EXPERIMENT) |
| As shown in Table III, our method achieves a 60% average success rate, significantly outperforming baselines like MOKA (22.5%) and MolmoAct (27.5%). | comparison identity and matched condition | p. 7 (IV. EXPERIMENT) |
| This suggests a fundamental weakness in the baselines' intermediate representations. | comparison identity and matched condition | p. 6 (IV. EXPERIMENT) |
| Starting from a 40.0% success rate for the baseline model, adding Input Enhancement provides the most significant single improvement (+27.5pp), while the Reflector alone ... | comparison identity and matched condition | p. 7 (IV. EXPERIMENT) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Fig. 4: Ablation Study. The performance of our full model ("World Model w/ Instruction & max 3 Reflection"), shown by the purple line, surpasses ... | component/input/data sensitivity | p. 7 (Figure/Table caption) |
| Ablation Study (Q2) We perform an ablation study to validate the contributions of our two key components: Input Enhancement and the Reflection-through-Synthesis process. | component/input/data sensitivity | p. 6 (IV. EXPERIMENT) |
| In all experiments, the robot starts without holding any object at the beginning of each trial. | component/input/data sensitivity | p. 6 (IV. EXPERIMENT) |
| These results demonstrate that both components are critical and complementary, confirming their effectiveness and answering our second research question (Q2). | component/input/data sensitivity | p. 7 (IV. EXPERIMENT) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To summarize, our key contributions are: • We introduce Goal-VLA, a decoupled hierarchical framework that leverages an Image-Generative VLM as a world model to ... | Our method, Goal-VLA, achieves a remarkable average success rate of 59.9%, significantly outperforming all baselines across a diverse set of eight manipulation tasks. | PDF body cue; verify exact table/figure and matched conditions | p. 6 (IV. EXPERIMENT), p. 7 (IV. EXPERIMENT), p. 7 (IV. EXPERIMENT), p. 6 (IV. EXPERIMENT), p. 1 (Figure/Table caption) |
| Primary metric/result | As shown in Table III, our method achieves a 60% average success rate, significantly outperforming baselines like MOKA (22.5%) and MolmoAct (27.5%). | numeric claim only at cited anchor | p. 7 (IV. EXPERIMENT) |

- Numeric sentences retained from the body:
- **p. 6 / IV. EXPERIMENT - extractive PDF cue:** We conduct 10 trials for each task, with detailed results presented in Table III and Figure 5.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Reflection's Necessary: Figure 3 highlights a typical failure mode of image generation. | p. 6 (IV. EXPERIMENT) |
| body limitation/failure cue | Failures originating from the Spatial Grounding module are the primary obstacle in several precision-demanding tasks. | p. 7 (IV. EXPERIMENT) |
| body limitation/failure cue | Failure Cases Analysis In our real-world experiments, we observe several typical failure modes as different tasks place varying demands on each module of our ... | p. 7 (IV. EXPERIMENT) |
| body limitation/failure cue | Fig. 1: Goal-VLA maps a single-view RGB-D image and a language instruction to executable manipulation actions. Our approach employs an object-centric world model to ... | p. 1 (Figure/Table caption) |
| body limitation/failure cue | To robustly assess performance and account for variations in object placement, each task is evaluated across 10 random seeds. | p. 6 (IV. EXPERIMENT) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| For each seed, which defines a unique initial scene arrangement, we conduct 10 independent trials of each method, resulting in 100 evaluation runs per ... | p. 6 (IV. EXPERIMENT) |
| We conduct 10 trials for each task, with detailed results presented in Table III and Figure 5. | p. 6 (IV. EXPERIMENT) |
| Similarly, the Bottle Stand-Up task's success is contingent on orientation precision, where even minor inaccuracies in the computed orientation from this module may lead ... | p. 7 (IV. EXPERIMENT) |
| Subsequently, the Spatial Grounding module takes this visual representation and computes a precise 3D transformation (Sec. | p. 3 (III. METHOD) |
| Algorithm 1 Goal-VLA Execution Framework Require: Initial observation O = (I, D), Language instruction L, Initial End-effector pose Pinit Ensure: Action sequence {a}i 1: ... | p. 3 (III. METHOD) |
| The objective of this module is to compute the rotation R ∈SO(3) and translation t ∈R3 that maps the object from its initial pose ... | p. 4 (III. METHOD) |
| (b) Spatial Grounding: The object's transformation is computed by feature matching and point cloud registration between the initial and goal states. | p. 4 (III. METHOD) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / IV. EXPERIMENT - extractive PDF cue:** Reflection's Necessary: Figure 3 highlights a typical failure mode of image generation.
- **p. 7 / IV. EXPERIMENT - extractive PDF cue:** Failures originating from the Spatial Grounding module are the primary obstacle in several precision-demanding tasks.
- **p. 7 / IV. EXPERIMENT - extractive PDF cue:** Failure Cases Analysis In our real-world experiments, we observe several typical failure modes as different tasks place varying demands on each module of our framework.
- **p. 1 / Figure/Table caption - extractive PDF cue:** Fig. 1: Goal-VLA maps a single-view RGB-D image and a language instruction to executable manipulation actions. Our approach employs an object-centric world model to generate ...
- **p. 6 / IV. EXPERIMENT - extractive PDF cue:** To robustly assess performance and account for variations in object placement, each task is evaluated across 10 random seeds.

- **PDF anchors reviewed:** datasets p. 5 (IV. EXPERIMENT), p. 7 (IV. EXPERIMENT), p. 5 (IV. EXPERIMENT), p. 6 (IV. EXPERIMENT), p. 6 (IV. EXPERIMENT), p. 7 (IV. EXPERIMENT), metrics p. 6 (IV. EXPERIMENT), p. 6 (IV. EXPERIMENT), p. 7 (IV. EXPERIMENT), p. 7 (IV. EXPERIMENT), p. 1 (Figure/Table caption), p. 4 (Figure/Table caption), baselines p. 5 (IV. EXPERIMENT), p. 6 (IV. EXPERIMENT), p. 7 (IV. EXPERIMENT), p. 6 (IV. EXPERIMENT), p. 7 (IV. EXPERIMENT), results p. 6 (IV. EXPERIMENT), p. 7 (IV. EXPERIMENT), p. 7 (IV. EXPERIMENT), p. 6 (IV. EXPERIMENT), p. 1 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
