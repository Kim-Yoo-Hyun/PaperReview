# Evaluation - RoboCasa: Large-Scale Simulation of Everyday Tasks for Generalist Robots

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (16 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2406.02523; PDF retrieval source: https://arxiv.org/pdf/2406.02523. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (Figure/Table caption), p. 6 (3) Can large-scale simulation datasets facilitate knowledge), p. 7 (3) Can large-scale simulation datasets facilitate knowledge), p. 8 (3) Can large-scale simulation datasets facilitate knowledge), p. 8 (3) Can large-scale simulation datasets facilitate knowledge), p. 6 (3) Can large-scale simulation datasets facilitate knowledge)): Fig. 7: Comparison between human demonstrations and machine-generated datasets. We present learning results across 24 atomic tasks spanning diverse robot skills. We compare training on four different multi-task datasets, including ...

## Evaluation Body Digest

- **p. 8 / 3) Can large-scale simulation datasets facilitate knowledge - extractive PDF cue:** We conduct experiments in a real-world kitchen environment with a Franka Emika Panda robot running on the DROID hardware infrastructure [20].
- **p. 6 / 3) Can large-scale simulation datasets facilitate knowledge - extractive PDF cue:** 2) Generated-3000: A dataset of 72,000 demonstrations synthesized by MimicGen1 across 24 atomic tasks2 1These experiments feature Objaverse objects.
- **p. 8 / 3) Can large-scale simulation datasets facilitate knowledge - extractive PDF cue:** For each seed, we evaluate the model over five seen object categories and 3 unseen object categories (unseen with respect to the real-world demonstrations).
- **p. 6 / 3) Can large-scale simulation datasets facilitate knowledge - extractive PDF cue:** In these datasets, our focus is specifically on a Franka Panda robot with an Omron mobile base, resembling the Omni-Frankie robot [13].
- **p. 7 / 3) Can large-scale simulation datasets facilitate knowledge - extractive PDF cue:** We compare training on four different multi-task datasets, including a human dataset with 50 demonstrations per task, a machine generated dataset with 3000 demonstrations per ...
- **p. 7 / 3) Can large-scale simulation datasets facilitate knowledge - extractive PDF cue:** For each task, we collected 50 human demonstrations and compared the following settings: • Scratch: learning a policy from scratch on these 50 demonstrations; • ...
- **p. 4 / IV. ROBOCASA ACTIVITY DATASET - extractive PDF cue:** This section outlines these tasks and our large multi-task dataset accompanying them.
- **p. 5 / IV. ROBOCASA ACTIVITY DATASET - extractive PDF cue:** Atomic Tasks: Building Blocks of Behavior For a robot to perform complex tasks, it must master the foundational skills needed to solve these tasks.

## Evaluation Type and Scope

- **Evaluation type:** `BENCHMARK / DATASET`.
- **Target system/task:** defined robot simulator/hardware task suite.
- **Input boundary:** standardized observation, action, task state와 evaluation split.
- **Output/decision under evaluation:** policy/controller trajectory 또는 measured result.
- **Primary target:** success metric, robustness, generalization과 reproducibility.
- **Detected evaluation headings:** IV. ROBOCASA ACTIVITY DATASET (p. 4); V. EXPERIMENTS (p. 6); 3) Can large-scale simulation datasets facilitate knowledge (p. 6).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | BENCHMARK / DATASET | Fig. 7: Comparison between human demonstrations and machine-generated datasets. We present learning results across 24 atomic tasks spanning diverse robot skills. We compare training ... | p. 7 (Figure/Table caption) |
| 3) Can large-scale simulation datasets facilitate knowledge | BENCHMARK / DATASET | The overall performance on human data is 28.8% success rate, and with the fully generated dataset, we observe a significant improvement at 47.6% success ... | p. 6 (3) Can large-scale simulation datasets facilitate knowledge) |
| 3) Can large-scale simulation datasets facilitate knowledge | BENCHMARK / DATASET | The fine-tuning method achieves non-zero success rates on 4/5 tasks. | p. 7 (3) Can large-scale simulation datasets facilitate knowledge) |
| 3) Can large-scale simulation datasets facilitate knowledge | BENCHMARK / DATASET | On seen objects, we see that cotraining with simulated data yields a 24.4% average success rate, compared to 13.6% with using real data only, ... | p. 8 (3) Can large-scale simulation datasets facilitate knowledge) |
| 3) Can large-scale simulation datasets facilitate knowledge | BENCHMARK / DATASET | While performance suffers on unseen objects, we still see a significant improvement in incorporating simulation data. | p. 8 (3) Can large-scale simulation datasets facilitate knowledge) |

## Dataset / Benchmark Role

- **p. 8 / 3) Can large-scale simulation datasets facilitate knowledge - extractive PDF cue:** We conduct experiments in a real-world kitchen environment with a Franka Emika Panda robot running on the DROID hardware infrastructure [20].
- **p. 6 / 3) Can large-scale simulation datasets facilitate knowledge - extractive PDF cue:** 2) Generated-3000: A dataset of 72,000 demonstrations synthesized by MimicGen1 across 24 atomic tasks2 1These experiments feature Objaverse objects.
- **p. 8 / 3) Can large-scale simulation datasets facilitate knowledge - extractive PDF cue:** For each seed, we evaluate the model over five seen object categories and 3 unseen object categories (unseen with respect to the real-world demonstrations).
- **p. 6 / 3) Can large-scale simulation datasets facilitate knowledge - extractive PDF cue:** In these datasets, our focus is specifically on a Franka Panda robot with an Omron mobile base, resembling the Omni-Frankie robot [13].
- **p. 7 / 3) Can large-scale simulation datasets facilitate knowledge - extractive PDF cue:** We compare training on four different multi-task datasets, including a human dataset with 50 demonstrations per task, a machine generated dataset with 3000 demonstrations per ...
- **p. 7 / 3) Can large-scale simulation datasets facilitate knowledge - extractive PDF cue:** For each task, we collected 50 human demonstrations and compared the following settings: • Scratch: learning a policy from scratch on these 50 demonstrations; • ...
- **p. 4 / IV. ROBOCASA ACTIVITY DATASET - extractive PDF cue:** This section outlines these tasks and our large multi-task dataset accompanying them.
- **p. 5 / IV. ROBOCASA ACTIVITY DATASET - extractive PDF cue:** Atomic Tasks: Building Blocks of Behavior For a robot to perform complex tasks, it must master the foundational skills needed to solve these tasks.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Fig. 1: Overview of RoboCasa. RoboCasa is a simulation framework for training generalist robot agents. Four pillars underlie RoboCasa: (1) Diverse assets, including 120 kitchen ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Fig. 3: Kitchen Floor Plans. We consult home planning and architecture magazines and compile a list of common kitchen floor plans. Our floor plans take ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Fig. 4: Examples of Interactable Appliances. Our simulation framework comes with dozens of appliances. Several types of appliances are articulated. For example, we can open ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Fig. 5: Diverse High-Quality 3D Objects. RoboCasa offers 2,509 high- quality 3D objects across 153 diverse categories spanning vegetables, poultry, drinks, and more. Here we ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Fig. 6: Creating Diverse Tasks with Large Language Models. We employ LLMs to generate diverse tasks. First, we prompt GPT-4 to give diverse high-level kitchen ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Fig. 7: Comparison between human demonstrations and machine-generated datasets. We present learning results across 24 atomic tasks spanning diverse robot skills. We compare training on ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Fig. 8: Learning Results on Composite Tasks. We learn single-task policies for five representative composite tasks. We compare learning these tasks from scratch with 50 ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Fig. 9: Real-World Experiment Setup. We conduct experiments in a real- world kitchen environment with a Franka Emika Panda arm on a wheeled mobile platform. ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We conduct experiments in a real-world kitchen environment with a Franka Emika Panda robot running on the DROID hardware infrastructure [20]. | embodiment, simulator version and control stack | p. 8 (3) Can large-scale simulation datasets facilitate knowledge), p. 6 (3) Can large-scale simulation datasets facilitate knowledge) |
| Task/environment | 2) Generated-3000: A dataset of 72,000 demonstrations synthesized by MimicGen1 across 24 atomic tasks2 1These experiments feature Objaverse objects. | reset, timeout, object/scene variation | p. 6 (3) Can large-scale simulation datasets facilitate knowledge), p. 8 (3) Can large-scale simulation datasets facilitate knowledge) |
| Observation/sensor | standardized observation, action, task state와 evaluation split | calibration, preprocessing, privileged input | p. 4 (III. ROBOCASA SIMULATION), p. 4 (III. ROBOCASA SIMULATION) |
| Output/decision | policy/controller trajectory 또는 measured result | action frame, controller and termination | p. 5 (8) Navigation. These skills do not constitute an exhaustive), p. 6 (3) Can large-scale simulation datasets facilitate knowledge) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| In Figure 10, we report policy success rates (mean and standard deviation, in percentage) averaged over 3 seeds. | definition/direction/unit from same section | p. 8 (3) Can large-scale simulation datasets facilitate knowledge) |
| The overall performance on human data is 28.8% success rate, and with the fully generated dataset, we observe a significant improvement at 47.6% success ... | definition/direction/unit from same section | p. 6 (3) Can large-scale simulation datasets facilitate knowledge) |
| We see a clear scaling trend: increasing the size of the generated dataset can yield consistently higher overall success rates, eventually significantly outperforming performance ... | definition/direction/unit from same section | p. 7 (3) Can large-scale simulation datasets facilitate knowledge) |
| The fine-tuning method achieves non-zero success rates on 4/5 tasks. | definition/direction/unit from same section | p. 7 (3) Can large-scale simulation datasets facilitate knowledge) |
| On seen objects, we see that cotraining with simulated data yields a 24.4% average success rate, compared to 13.6% with using real data only, ... | definition/direction/unit from same section | p. 8 (3) Can large-scale simulation datasets facilitate knowledge) |
| We aim to explore the following research questions in our experiments: 1) How effective are machine-generated trajectories from MimicGen in learning multi-task policies, in ... | definition/direction/unit from same section | p. 6 (V. EXPERIMENTS) |
| Here we illustrate a small subset of these objects. | definition/direction/unit from same section | p. 5 (IV. ROBOCASA ACTIVITY DATASET) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Fig. 7: Comparison between human demonstrations and machine-generated datasets. We present learning results across 24 atomic tasks spanning diverse robot skills. We compare training ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| Learning on these composite tasks is very challenging, with the Scratch baseline failing to achieve any non-zero success rate on 4/5 tasks. | comparison identity and matched condition | p. 7 (3) Can large-scale simulation datasets facilitate knowledge) |
| Compared to training policies exclusively on in-domain realworld demonstrations, co-training substantially improves policy performance. | comparison identity and matched condition | p. 8 (3) Can large-scale simulation datasets facilitate knowledge) |
| On seen objects, we see that cotraining with simulated data yields a 24.4% average success rate, compared to 13.6% with using real data only, ... | comparison identity and matched condition | p. 8 (3) Can large-scale simulation datasets facilitate knowledge) |
| We aim to explore the following research questions in our experiments: 1) How effective are machine-generated trajectories from MimicGen in learning multi-task policies, in ... | comparison identity and matched condition | p. 6 (V. EXPERIMENTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We compare training on four different multi-task datasets, including a human dataset with 50 demonstrations per task, a machine generated dataset with 3000 demonstrations ... | component/input/data sensitivity | p. 7 (3) Can large-scale simulation datasets facilitate knowledge) |
| The fine-tuning method achieves non-zero success rates on 4/5 tasks. | component/input/data sensitivity | p. 7 (3) Can large-scale simulation datasets facilitate knowledge) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We summarize our contributions as follows: • We develop the RoboCasa simulation framework featuring diverse, realistic kitchen scenes, thousands of high-quality object assets, and ... | Fig. 7: Comparison between human demonstrations and machine-generated datasets. We present learning results across 24 atomic tasks spanning diverse robot skills. We compare training ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (Figure/Table caption), p. 6 (3) Can large-scale simulation datasets facilitate knowledge), p. 7 (3) Can large-scale simulation datasets facilitate knowledge), p. 8 (3) Can large-scale simulation datasets facilitate knowledge), p. 8 (3) Can large-scale simulation datasets facilitate knowledge), p. 6 (3) Can large-scale simulation datasets facilitate knowledge) |
| Primary metric/result | The overall performance on human data is 28.8% success rate, and with the fully generated dataset, we observe a significant improvement at 47.6% success ... | numeric claim only at cited anchor | p. 6 (3) Can large-scale simulation datasets facilitate knowledge) |

- Numeric sentences retained from the body:
- **p. 4 / IV. ROBOCASA ACTIVITY DATASET - extractive PDF cue:** Our simulator supports a wide array of possible kitchen activities, and we represent these activities with a comprehensive suite of 100 tasks.
- **p. 6 / 3) Can large-scale simulation datasets facilitate knowledge - extractive PDF cue:** We take the 50 human demonstrations as input for each task and use them to generate 3,000 trajectories autonomously.
- **p. 6 / 3) Can large-scale simulation datasets facilitate knowledge - extractive PDF cue:** This results in a total of 7,200 trajectories.
- **p. 6 / 3) Can large-scale simulation datasets facilitate knowledge - extractive PDF cue:** This results in a total of 2,400 trajectories.
- **p. 6 / 3) Can large-scale simulation datasets facilitate knowledge - extractive PDF cue:** For each task, we evaluate the model performance across 50 trials across five fixed evaluation scenes, each with a distinct floor plan and style.
- **p. 7 / 3) Can large-scale simulation datasets facilitate knowledge - extractive PDF cue:** Learning on these composite tasks is very challenging, with the Scratch baseline failing to achieve any non-zero success rate on 4/5 tasks.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | We now pinpoint limitations and discuss exciting avenues for future future. | p. 8 (VI. CONCLUSION) |
| body limitation/failure cue | While the generated trajectories are technically considered successful, many exhibited undesirable effects, such as jerky motions and collisions. | p. 8 (VI. CONCLUSION) |
| body limitation/failure cue | Some common failure modes include difficulty with fine-grained manipulation and difficulty effectively transitioning to the next stage of the task. | p. 7 (3) Can large-scale simulation datasets facilitate knowledge) |
| body limitation/failure cue | The choice of policy architecture, learning algorithm, and finetuning strategy may play a critical role in performance, and these factors warrant investigation in future ... | p. 7 (3) Can large-scale simulation datasets facilitate knowledge) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We compile 75 task blueprints in total from the LLM and proceed to code implementations for them. | p. 5 (8) Navigation. These skills do not constitute an exhaustive) |
| Videos and open-source code are available on the project website. | p. 1 (Abstract) |
| Unlike computer vision and natural language processing domains, where massive visual and text data are abundant from online sources, robotic data is relatively scarce. | p. 1 (I. INTRODUCTION) |
| Today's generative AI tools are capable of generating images, synthesizing 3D assets, and writing source code [38, 35, 42]. | p. 2 (I. INTRODUCTION) |
| RoboCasa inherits these features and goes far beyond by offering a large array of scenes, objects, and hardware platforms suited for building a general-purpose ... | p. 2 (I. INTRODUCTION) |
| After consulting architecture magazines, we compile the popular kitchen styles, including Industrial, Scandinavian, Coastal, Modern, Traditional, Mediterranean, Rustic, and more. | p. 4 (III. ROBOCASA SIMULATION) |
| We generate tasks across two steps (see Figure 6). | p. 5 (8) Navigation. These skills do not constitute an exhaustive) |
| We specifically use the publicly available BC-Transformer implementation in RoboMimic [33]. | p. 6 (3) Can large-scale simulation datasets facilitate knowledge) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / VI. CONCLUSION - extractive PDF cue:** We now pinpoint limitations and discuss exciting avenues for future future.
- **p. 8 / VI. CONCLUSION - extractive PDF cue:** While the generated trajectories are technically considered successful, many exhibited undesirable effects, such as jerky motions and collisions.
- **p. 7 / 3) Can large-scale simulation datasets facilitate knowledge - extractive PDF cue:** Some common failure modes include difficulty with fine-grained manipulation and difficulty effectively transitioning to the next stage of the task.
- **p. 7 / 3) Can large-scale simulation datasets facilitate knowledge - extractive PDF cue:** The choice of policy architecture, learning algorithm, and finetuning strategy may play a critical role in performance, and these factors warrant investigation in future work.

- **PDF anchors reviewed:** datasets p. 8 (3) Can large-scale simulation datasets facilitate knowledge), p. 6 (3) Can large-scale simulation datasets facilitate knowledge), p. 8 (3) Can large-scale simulation datasets facilitate knowledge), p. 6 (3) Can large-scale simulation datasets facilitate knowledge), p. 7 (3) Can large-scale simulation datasets facilitate knowledge), p. 7 (3) Can large-scale simulation datasets facilitate knowledge), metrics p. 8 (3) Can large-scale simulation datasets facilitate knowledge), p. 6 (3) Can large-scale simulation datasets facilitate knowledge), p. 7 (3) Can large-scale simulation datasets facilitate knowledge), p. 7 (3) Can large-scale simulation datasets facilitate knowledge), p. 8 (3) Can large-scale simulation datasets facilitate knowledge), p. 6 (V. EXPERIMENTS), baselines p. 7 (Figure/Table caption), p. 7 (3) Can large-scale simulation datasets facilitate knowledge), p. 8 (3) Can large-scale simulation datasets facilitate knowledge), p. 8 (3) Can large-scale simulation datasets facilitate knowledge), p. 6 (V. EXPERIMENTS), results p. 7 (Figure/Table caption), p. 6 (3) Can large-scale simulation datasets facilitate knowledge), p. 7 (3) Can large-scale simulation datasets facilitate knowledge), p. 8 (3) Can large-scale simulation datasets facilitate knowledge), p. 8 (3) Can large-scale simulation datasets facilitate knowledge), p. 6 (3) Can large-scale simulation datasets facilitate knowledge).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
