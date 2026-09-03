# Evaluation - VLA-Reasoner: Empowering Vision-Language-Action Models with Reasoning Via Online Monte Carlo Tree Search

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_3.html; PDF retrieval source: https://arxiv.org/pdf/2509.22643. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 5 (3) Robustness. Can VLA-Reasoner adapt to varied set), p. 6 (3) Robustness. Can VLA-Reasoner adapt to varied set), p. 2 (I. INTRODUCTION), p. 6 (2 Cups), p. 2 (I. INTRODUCTION), p. 5 (3) Robustness. Can VLA-Reasoner adapt to varied set)): As the success rate is the primary metric of evaluation in two benchmarks, our method improves the absolute task-set performance on OpenVLA-SFT by 5% on average, the reasoner also improves ...

## Evaluation Body Digest

- **p. 6 / 3) Robustness. Can VLA-Reasoner adapt to varied set - extractive body cue:** Deployment in Real-world Environment a) Experiment Setup: To evaluate the performance of the VLA-Reasoner in the real world with real robots.
- **p. 6 / 2 Cups - extractive body cue:** Circle Overall OpenVLA 5% 15% 22% +VLA-Reasoner 15% 40% 41% π0 -FAST 40% 70% 64% +VLA-Reasoner 50% 75% 74% embodiment gap, we analyze a specific ...
- **p. 5 / 3) Robustness. Can VLA-Reasoner adapt to varied set - extractive body cue:** For Q1, we conduct experiments in 2 simulation environment (LIBERO [39] and SimplerEnv [40]) with 8 specific tasks based on 3 popular general robot policies.
- **p. 3 / III. METHOD - extractive body cue:** We embed robot actions into its latent space and finetune it on a small robot dataset, aligning multimodal inputs for plausible transition generation. c) Backpropagation: ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** The method is plug-and-play, and it can be attached to any VLA-based manipulation policy and consistently improves performance across tasks, environments, and robot embodiments. exploration ...
- **p. 4 / IV. EXPERIMENTS - extractive body cue:** In this section, we present both simulation and real-world experiments to explore the following key questions:
- **p. 3 / III. METHOD - extractive body cue:** Problem Statement VLAs aim to generalize robot manipulation by mapping multimodal inputs (states from the environment st, language instructions of the task l) to actions ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Our method delivers consistent gains in both simulation and on real robots.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** IV. EXPERIMENTS (p. 4).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 3) Robustness. Can VLA-Reasoner adapt to varied set | EMPIRICAL / REAL-ROBOT OR HARDWARE | As the success rate is the primary metric of evaluation in two benchmarks, our method improves the absolute task-set performance on OpenVLA-SFT by 5% ... | p. 5 (3) Robustness. Can VLA-Reasoner adapt to varied set) |
| 3) Robustness. Can VLA-Reasoner adapt to varied set | EMPIRICAL / REAL-ROBOT OR HARDWARE | It averages an improvement of OpenVLA with an absolute gain of 19%, a relative gain of 86.4%, as the baseline shows a poor performance ... | p. 6 (3) Robustness. Can VLA-Reasoner adapt to varied set) |
| I. INTRODUCTION | EMPIRICAL / REAL-ROBOT OR HARDWARE | In real-world deployments, our approach achieves higher success rates compared to popular VLAs fine-tuned with a few demonstrations, indicating stronger generalization and adaptivity at ... | p. 2 (I. INTRODUCTION) |
| 2 Cups | EMPIRICAL / REAL-ROBOT OR HARDWARE | The base model remains identical to the main experiments. a) Choices of Injection Strength: Figure 5 shows that injecting a value-guided action by MCTS ... | p. 6 (2 Cups) |
| I. INTRODUCTION | EMPIRICAL / REAL-ROBOT OR HARDWARE | We also show the potential to achieve great real-world performance with a few data acquisitions. | p. 2 (I. INTRODUCTION) |

## Dataset / Benchmark Role

- **p. 6 / 3) Robustness. Can VLA-Reasoner adapt to varied set - extractive body cue:** Deployment in Real-world Environment a) Experiment Setup: To evaluate the performance of the VLA-Reasoner in the real world with real robots.
- **p. 6 / 2 Cups - extractive body cue:** Circle Overall OpenVLA 5% 15% 22% +VLA-Reasoner 15% 40% 41% π0 -FAST 40% 70% 64% +VLA-Reasoner 50% 75% 74% embodiment gap, we analyze a specific ...
- **p. 5 / 3) Robustness. Can VLA-Reasoner adapt to varied set - extractive body cue:** For Q1, we conduct experiments in 2 simulation environment (LIBERO [39] and SimplerEnv [40]) with 8 specific tasks based on 3 popular general robot policies.
- **p. 3 / III. METHOD - extractive body cue:** We embed robot actions into its latent space and finetune it on a small robot dataset, aligning multimodal inputs for plausible transition generation. c) Backpropagation: ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** The method is plug-and-play, and it can be attached to any VLA-based manipulation policy and consistently improves performance across tasks, environments, and robot embodiments. exploration ...
- **p. 4 / IV. EXPERIMENTS - extractive body cue:** In this section, we present both simulation and real-world experiments to explore the following key questions:
- **p. 3 / III. METHOD - extractive body cue:** Problem Statement VLAs aim to generalize robot manipulation by mapping multimodal inputs (states from the environment st, language instructions of the task l) to actions ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Our method delivers consistent gains in both simulation and on real robots.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: VLA-Reasoner augments VLA models with test-time rea- soning via online tree search, enabling more robust and interpretable robotic manipulation than baselines. becoming a ...
- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 2: The overall pipeline of VLA-Reasoner. At test time, a lightweight and modified MCTS searches for the optimal action conditioned on the VLA prediction. ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 3: Setup of real world experiments. We conduct diverse tasks in the real world to identify the limitations of current VLAs and validate our ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 4: Case Visualization. The baseline policy (π0-FAST, top row) suffers from excessive action drift and fails by such deviations. With reasoning, VLA-Reasoner (bottom row) ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 5: Analysis on injection strength α. α controls the trade-off between the VLA action and the reasoner action; a larger α assigns greater weight ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 6: Analysis on Techniques. The comparison validates the design in our method, which is reflected by the significant growth in the success rate. chosen ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Deployment in Real-world Environment a) Experiment Setup: To evaluate the performance of the VLA-Reasoner in the real world with real robots. | embodiment, simulator version and control stack | p. 6 (3) Robustness. Can VLA-Reasoner adapt to varied set), p. 6 (2 Cups) |
| Task/environment | Circle Overall OpenVLA 5% 15% 22% +VLA-Reasoner 15% 40% 41% π0 -FAST 40% 70% 64% +VLA-Reasoner 50% 75% 74% embodiment gap, we analyze a ... | reset, timeout, object/scene variation | p. 6 (2 Cups), p. 5 (3) Robustness. Can VLA-Reasoner adapt to varied set) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 4 (III. METHOD), p. 3 (III. METHOD) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 1 (I. INTRODUCTION), p. 3 (III. METHOD) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Baseline Gaussian Noise KDE (Ours) 80.0% 85.0% 90.0% 95.0% 100.0% Success Rate (%) 82.0% 85.0% 91.5% Strategies of Action Sampling Baseline Token Reward Image ... | definition/direction/unit from same section | p. 7 (2 Cups) |
| As the success rate is the primary metric of evaluation in two benchmarks, our method improves the absolute task-set performance on OpenVLA-SFT by 5% ... | definition/direction/unit from same section | p. 5 (3) Robustness. Can VLA-Reasoner adapt to varied set) |
| It averages an improvement of OpenVLA with an absolute gain of 19%, a relative gain of 86.4%, as the baseline shows a poor performance ... | definition/direction/unit from same section | p. 6 (3) Robustness. Can VLA-Reasoner adapt to varied set) |
| The base model remains identical to the main experiments. a) Choices of Injection Strength: Figure 5 shows that injecting a value-guided action by MCTS ... | definition/direction/unit from same section | p. 6 (2 Cups) |
| In real-world deployments, our approach achieves higher success rates compared to popular VLAs fine-tuned with a few demonstrations, indicating stronger generalization and adaptivity at ... | definition/direction/unit from same section | p. 2 (I. INTRODUCTION) |
| Bold entries mark the highest success rates, underlined for second-best. | definition/direction/unit from same section | p. 5 (2) Real-world Applicability. How does VLA-Reasoner) |
| The comparison validates the design in our method, which is reflected by the significant growth in the success rate. chosen as the hyperparameter for ... | definition/direction/unit from same section | p. 7 (2 Cups) |
| Fig. 1: VLA-Reasoner augments VLA models with test-time rea- soning via online tree search, enabling more robust and interpretable robotic manipulation than baselines. becoming ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| It is noticeable that compared to those variants developed from OpenVLA, our plug-and-play method can directly improve the performance of the backbone to the ... | comparison identity and matched condition | p. 5 (3) Robustness. Can VLA-Reasoner adapt to varied set) |
| When compared to SpatialVLA, which is augmented with better spatial understanding capability, our method outperforms it in all task suites. | comparison identity and matched condition | p. 5 (3) Robustness. Can VLA-Reasoner adapt to varied set) |
| Fig. 1: VLA-Reasoner augments VLA models with test-time rea- soning via online tree search, enabling more robust and interpretable robotic manipulation than baselines. becoming ... | comparison identity and matched condition | p. 1 (Figure/Table caption) |
| On the LIBERO benchmark, wrapping a modest baseline VLA with VLA-Reasoner lifts it beyond competing VLAs. | comparison identity and matched condition | p. 2 (I. INTRODUCTION) |
| In real-world deployments, our approach achieves higher success rates compared to popular VLAs fine-tuned with a few demonstrations, indicating stronger generalization and adaptivity at ... | comparison identity and matched condition | p. 2 (I. INTRODUCTION) |
| For action ai, the expansion can be formulated as: Sample: ˜ Ai = {a(n)}N n=1 ∼πθ, Top-k: ATop-k i = arg min A⊆˜ Ai, ... | comparison identity and matched condition | p. 3 (III. METHOD) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| It is noticeable that compared to those variants developed from OpenVLA, our plug-and-play method can directly improve the performance of the backbone to the ... | component/input/data sensitivity | p. 5 (3) Robustness. Can VLA-Reasoner adapt to varied set) |
| Ablation Analysis This section aims to evaluate the robustness and sensitivity of VLA-Reasoner under different injection strengths, and to validate whether its outstanding performance ... | component/input/data sensitivity | p. 6 (2 Cups) |
| We also conduct ablation on specific technique designs to test the effectiveness. | component/input/data sensitivity | p. 5 (3) Robustness. Can VLA-Reasoner adapt to varied set) |
| We adapt MCTS (Section III-B) for efficient test-time expansion and backpropagation on the VLA prediction without disturbing real world execution. | component/input/data sensitivity | p. 3 (III. METHOD) |
| We conduct controlled ablations on LIBERO-Spatial. | component/input/data sensitivity | p. 6 (2 Cups) |
| Spatial Goal Object Long α=1.0 α=0.8 α=0.6 α=0.4 α=0.2 82% 78% 86% 54.5% 88% 83.5% 87.5% 58% 91.5% 83.5% 90.5% 60.5% 90.5% 81.5% 88.5% ... | component/input/data sensitivity | p. 7 (2 Cups) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our contributions are summarized as follows: • We propose a plug-in framework named VLA-Reasoner that empowers VLAs with structured reasoning to address their incremental ... | As the success rate is the primary metric of evaluation in two benchmarks, our method improves the absolute task-set performance on OpenVLA-SFT by 5% ... | PDF body cue; verify exact table/figure and matched conditions | p. 5 (3) Robustness. Can VLA-Reasoner adapt to varied set), p. 6 (3) Robustness. Can VLA-Reasoner adapt to varied set), p. 2 (I. INTRODUCTION), p. 6 (2 Cups), p. 2 (I. INTRODUCTION), p. 5 (3) Robustness. Can VLA-Reasoner adapt to varied set) |
| Primary metric/result | It averages an improvement of OpenVLA with an absolute gain of 19%, a relative gain of 86.4%, as the baseline shows a poor performance ... | numeric claim only at cited anchor | p. 6 (3) Robustness. Can VLA-Reasoner adapt to varied set) |

- Numeric sentences retained from the body:
- **p. 3 / III. METHOD - extractive body cue:** For action ai, the expansion can be formulated as: Sample: ˜ Ai = {a(n)}N n=1 ∼πθ, Top-k: ATop-k i = arg min A⊆˜ Ai, /A/=k ...
- **p. 5 / 2) Real-world Applicability. How does VLA-Reasoner - extractive body cue:** Average success rates across 500 episodes for LIBERO and 100 episodes for SimplerEnv.
- **p. 5 / 2) Real-world Applicability. How does VLA-Reasoner - extractive body cue:** Our method outperforms OpenVLA-SFT on all 4 direction tasks and Octo-Small/SpatialVLA on 4 tasks.
- **p. 5 / 3) Robustness. Can VLA-Reasoner adapt to varied set - extractive body cue:** For LIBERO, we utilize 4 task suites: Spatial, Object, Goal, and Long.
- **p. 5 / 3) Robustness. Can VLA-Reasoner adapt to varied set - extractive body cue:** All the training processes are conducted on a server with 6 NVIDIA RTX 6000 GPUs. b) Quantitative Study: Experiment results are shown in Table I.
- **p. 6 / 3) Robustness. Can VLA-Reasoner adapt to varied set - extractive body cue:** Real-world inference is conducted on an NVIDIA RTX 4090 GPU.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | We identified a core limitation of current short-sighted VLA deployment and introduced VLA-Reasoner, a plug-in framework that injects test-time reasoning into off-the-shelf VLAs, to ... | p. 7 (V. CONCLUSION) |
| body limitation/failure cue | For the world model, we additionally collect a small set of failure demonstrations to finetune it for predicting failure cases. | p. 4 (III. METHOD) |
| body limitation/failure cue | For the world model, we additionally supplement its training with a small set of failure demonstrations collected from the rollouts of the pretrained VLA ... | p. 5 (3) Robustness. Can VLA-Reasoner adapt to varied set) |
| body limitation/failure cue | The training phases use the same datasets, and we collect 10 failure cases for each task to supplement the training of the world model. | p. 6 (3) Robustness. Can VLA-Reasoner adapt to varied set) |
| body limitation/failure cue | Besides the strengths shown in Section IV-A, we find that injecting a directional future-conditioned feedback to action can improve the awareness of current execution, ... | p. 6 (3) Robustness. Can VLA-Reasoner adapt to varied set) |
| body limitation/failure cue | We expect future work to build on VLA-Reasoner and explore scalable test-time computation 7 | p. 7 (V. CONCLUSION) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We follow the MCTS manner for efficient tree search, and adapt MCTS to a simple implementation in test time. | p. 3 (III. METHOD) |
| At each step t, VLA-Reasoner proceeds through four steps: (a) Expansion, (b) Simulation, (c) Backpropagation, and (d) Selection. | p. 3 (III. METHOD) |
| Pseudocode for VLA-Reasoner is provided above (Algorithm 1). | p. 4 (III. METHOD) |
| These four steps are repeated in a round of iteration, where it takes real state and action as input. | p. 4 (III. METHOD) |
| Real-world inference is conducted on an NVIDIA RTX 4090 GPU. | p. 6 (3) Robustness. Can VLA-Reasoner adapt to varied set) |
| The results are shown in the right part of Figure 6, where the image-wise value estimation can better reflect explicit task progress with a ... | p. 7 (2 Cups) |
| The comparison validates the design in our method, which is reflected by the significant growth in the success rate. chosen as the hyperparameter for ... | p. 7 (2 Cups) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / V. CONCLUSION - extractive body cue:** We identified a core limitation of current short-sighted VLA deployment and introduced VLA-Reasoner, a plug-in framework that injects test-time reasoning into off-the-shelf VLAs, to mitigate ...
- **p. 4 / III. METHOD - extractive body cue:** For the world model, we additionally collect a small set of failure demonstrations to finetune it for predicting failure cases.
- **p. 5 / 3) Robustness. Can VLA-Reasoner adapt to varied set - extractive body cue:** For the world model, we additionally supplement its training with a small set of failure demonstrations collected from the rollouts of the pretrained VLA itself, ...
- **p. 6 / 3) Robustness. Can VLA-Reasoner adapt to varied set - extractive body cue:** The training phases use the same datasets, and we collect 10 failure cases for each task to supplement the training of the world model.
- **p. 6 / 3) Robustness. Can VLA-Reasoner adapt to varied set - extractive body cue:** Besides the strengths shown in Section IV-A, we find that injecting a directional future-conditioned feedback to action can improve the awareness of current execution, and ...
- **p. 7 / V. CONCLUSION - extractive body cue:** We expect future work to build on VLA-Reasoner and explore scalable test-time computation 7

- **Evidence anchors reviewed:** datasets p. 6 (3) Robustness. Can VLA-Reasoner adapt to varied set), p. 6 (2 Cups), p. 5 (3) Robustness. Can VLA-Reasoner adapt to varied set), p. 3 (III. METHOD), p. 2 (I. INTRODUCTION), p. 4 (IV. EXPERIMENTS), metrics p. 7 (2 Cups), p. 5 (3) Robustness. Can VLA-Reasoner adapt to varied set), p. 6 (3) Robustness. Can VLA-Reasoner adapt to varied set), p. 6 (2 Cups), p. 2 (I. INTRODUCTION), p. 5 (2) Real-world Applicability. How does VLA-Reasoner), baselines p. 5 (3) Robustness. Can VLA-Reasoner adapt to varied set), p. 5 (3) Robustness. Can VLA-Reasoner adapt to varied set), p. 1 (Figure/Table caption), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (III. METHOD), results p. 5 (3) Robustness. Can VLA-Reasoner adapt to varied set), p. 6 (3) Robustness. Can VLA-Reasoner adapt to varied set), p. 2 (I. INTRODUCTION), p. 6 (2 Cups), p. 2 (I. INTRODUCTION), p. 5 (3) Robustness. Can VLA-Reasoner adapt to varied set).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
