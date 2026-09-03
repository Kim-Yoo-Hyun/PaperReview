# Evaluation - Code as Policies: Language Model Programs for Embodied Control

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2209.07753; PDF retrieval source: https://arxiv.org/pdf/2209.07753. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 11 (Figure/Table caption)): Within each model family, performance improves with larger models.

## Evaluation Body Digest

- **p. 6 / IV. EXPERIMENTS - extractive body cue:** CaP: Mobile Robot Navigation and Manipulation In this domain, a robot with a mobile base and a 7 DoF arm is tasked to perform navigation ...
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Hierarchical LMPs on Code-Generation Benchmarks We evaluate our code-generation approach on two codegeneration benchmarks: (i) a robotics-themed RoboCodeGen and (ii) HumanEval [1], which consists of ...
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** RoboCodeGen: we introduce a new benchmark with 37 function generation problems with several key differences from previous code-gen benchmarks: (i) it is robotics-themed with questions ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** CaP: Pick & Place Policies for Table-Top Manipulation The table-top manipulation domain tasks a UR5e robot arm to pick and place various plastic toy objects ...
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: Given examples (via few-shot prompting), robots can use code-writing large language models (LLMs) to translate natural language commands into robot policy code which ...
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Within each model family, performance improves with larger models.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Two Codex models [1]: cushman and davinci, trained to generate code. davinci is larger and better.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** Examples of successful on-robot executions of unseen language commands are in Fig.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** IV. EXPERIMENTS (p. 5).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| IV. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Within each model family, performance improves with larger models. | p. 5 (IV. EXPERIMENTS) |
| IV. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Numbers achieved are higher than in recent works [1], [11], [58]. | p. 5 (IV. EXPERIMENTS) |
| IV. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | With unseen task attributes, CLIPort's performance degrades significantly, while LLM-based methods retain similar performance. | p. 6 (IV. EXPERIMENTS) |
| IV. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | On unseen tasks and attributes, endto-end systems like CLIPort struggle to generalize, and CaP outperforms LLM reasoning directly with language (also observed in [20]). | p. 6 (IV. EXPERIMENTS) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 4: Robot Code-Generation Benchmark Performance across Generalization Types for Flat (top) and Hierarchical (middle) Code- Generation, as well as the performance improvements made ... | p. 11 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 6 / IV. EXPERIMENTS - extractive body cue:** CaP: Mobile Robot Navigation and Manipulation In this domain, a robot with a mobile base and a 7 DoF arm is tasked to perform navigation ...
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Hierarchical LMPs on Code-Generation Benchmarks We evaluate our code-generation approach on two codegeneration benchmarks: (i) a robotics-themed RoboCodeGen and (ii) HumanEval [1], which consists of ...
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** RoboCodeGen: we introduce a new benchmark with 37 function generation problems with several key differences from previous code-gen benchmarks: (i) it is robotics-themed with questions ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** CaP: Pick & Place Policies for Table-Top Manipulation The table-top manipulation domain tasks a UR5e robot arm to pick and place various plastic toy objects ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: Given examples (via few-shot prompting), robots can use code-writing large language models (LLMs) to translate natural language commands into robot policy code which ...
- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 2: Code as Policies can follow natural language instructions across diverse domains and robots: table-top manipulation (a)-(b), 2D shape drawing (c), and mobile manipulation ...
- **p. 11 / Figure/Table caption - extractive body cue:** Fig. 4: Robot Code-Generation Benchmark Performance across Generalization Types for Flat (top) and Hierarchical (middle) Code- Generation, as well as the performance improvements made by ...
- **p. 12 / Figure/Table caption - extractive body cue:** Fig. 5: LMPs can balance a cartpole LMPs can likewise be prompted to express impedance control: # define function: tau = ee_impedance_control(x_curr, x_goal, x_dot, K_x_mat, ...
- **p. 14 / Figure/Table caption - extractive body cue:** Fig. 6: Experiment Setup for mobile manipulation with a Everyday Robots robot. Prompts. • mobile_ui: the high-level UI for parsing user commands and calling other ...
- **p. 16 / Figure/Table caption - extractive body cue:** Fig. 7: LMPs inherit benefits of LLMs, such as parsing commands from non- English languages and emojis. # omnidirectional robot. # available actions: move_up(dist), move_right(dist), ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | CaP: Mobile Robot Navigation and Manipulation In this domain, a robot with a mobile base and a 7 DoF arm is tasked to perform ... | embodiment, simulator version and control stack | p. 6 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Task/environment | Hierarchical LMPs on Code-Generation Benchmarks We evaluate our code-generation approach on two codegeneration benchmarks: (i) a robotics-themed RoboCodeGen and (ii) HumanEval [1], which consists ... | reset, timeout, object/scene variation | p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 1 (I. INTRODUCTION), p. 3 (III. METHOD) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 1 (I. INTRODUCTION), p. 3 (III. METHOD) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Fig. 1: Given examples (via few-shot prompting), robots can use code-writing large language models (LLMs) to translate natural language commands into robot policy code ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Within each model family, performance improves with larger models. | definition/direction/unit from same section | p. 5 (IV. EXPERIMENTS) |
| Two Codex models [1]: cushman and davinci, trained to generate code. davinci is larger and better. | definition/direction/unit from same section | p. 5 (IV. EXPERIMENTS) |
| Examples of successful on-robot executions of unseen language commands are in Fig. | definition/direction/unit from same section | p. 6 (IV. EXPERIMENTS) |
| With unseen task attributes, CLIPort's performance degrades significantly, while LLM-based methods retain similar performance. | definition/direction/unit from same section | p. 6 (IV. EXPERIMENTS) |
| Fig. 2: Code as Policies can follow natural language instructions across diverse domains and robots: table-top manipulation (a)-(b), 2D shape drawing (c), and mobile ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |
| Fig. 4: Robot Code-Generation Benchmark Performance across Generalization Types for Flat (top) and Hierarchical (middle) Code- Generation, as well as the performance improvements made ... | definition/direction/unit from same section | p. 11 (Figure/Table caption) |
| Fig. 6: Experiment Setup for mobile manipulation with a Everyday Robots robot. Prompts. • mobile_ui: the high-level UI for parsing user commands and calling ... | definition/direction/unit from same section | p. 14 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Due to the difficulty of evaluating open-ended tasks and a lack of comparable baselines, quantitative evaluations of a robot system using CaP is limited ... | comparison identity and matched condition | p. 5 (IV. EXPERIMENTS) |
| The goals of our experiments are threefold: (i) evaluate the impact of using hierarchical code generation (across different language models) and analyze modes of ... | comparison identity and matched condition | p. 5 (IV. EXPERIMENTS) |
| On unseen tasks and attributes, endto-end systems like CLIPort struggle to generalize, and CaP outperforms LLM reasoning directly with language (also observed in [20]). | comparison identity and matched condition | p. 6 (IV. EXPERIMENTS) |
| CaP compares competitively to the supervised CLIPort baseline on tasks with seen attributes and instructions, despite only few-shot prompted with one example rollout for ... | comparison identity and matched condition | p. 6 (IV. EXPERIMENTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Due to the difficulty of evaluating open-ended tasks and a lack of comparable baselines, quantitative evaluations of a robot system using CaP is limited ... | component/input/data sensitivity | p. 5 (IV. EXPERIMENTS) |
| Prompts are similar to those from the last domain, except trajectory parsing is replaced with position parsing. | component/input/data sensitivity | p. 6 (IV. EXPERIMENTS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our approach enables robots to perform spatial-geometric reasoning, parse object relationships, and form multi-step behaviors using off-the-shelf models and few-shot prompting with no additional ... | Within each model family, performance improves with larger models. | PDF body cue; verify exact table/figure and matched conditions | p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 11 (Figure/Table caption) |
| Primary metric/result | Numbers achieved are higher than in recent works [1], [11], [58]. | numeric claim only at cited anchor | p. 5 (IV. EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** We inherit all 8 tasks, referred as "long-horizon" tasks due to their multi-step nature (e.g., "put the blocks in matching bowls").

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Our approach also assumes all given instructions are feasible, and we cannot tell if a response will be correct a priori. | p. 6 (V. DISCUSSION AND LIMITATIONS) |
| body limitation/failure cue | It also illustrates the ability to follow long-horizon reactive commands with control structures as well as precise spatial reasoning, which cannot be easily accomplished ... | p. 6 (IV. EXPERIMENTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Sizes of Codex models are not public. | p. 5 (IV. EXPERIMENTS) |
| Domain-specific language models (Codex model) generally perform better. | p. 5 (IV. EXPERIMENTS) |
| Each task is parameterized by some attributes (e.g., "pick up <obj> and place it in <corner>"), which are sampled during each trial. | p. 6 (IV. EXPERIMENTS) |
| We consider two baselines: (i) language-conditioned multi-task CLIPort [36] policies trained via imitation learning on 30k demonstrations, and (ii) few-shot prompted LLM planner using ... | p. 6 (IV. EXPERIMENTS) |
| Predicted outputs from the LLM (highlighted) are expected to be valid Python code, generated autoregressively [11], [12]. | p. 3 (III. METHOD) |
| Hierarchical code-gen with verbose variable names can be viewed as a variant of chain of thought prompting [47] via functional programming. | p. 3 (III. METHOD) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / V. DISCUSSION AND LIMITATIONS - extractive body cue:** Our approach also assumes all given instructions are feasible, and we cannot tell if a response will be correct a priori.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** It also illustrates the ability to follow long-horizon reactive commands with control structures as well as precise spatial reasoning, which cannot be easily accomplished by ...

- **Evidence anchors reviewed:** datasets p. 6 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), metrics p. 1 (Figure/Table caption), p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 2 (Figure/Table caption), baselines p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), results p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 11 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
