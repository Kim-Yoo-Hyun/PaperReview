# Evaluation - RT-1: Robotics Transformer for Real-World Control at Scale

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (31 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2212.06817; PDF retrieval source: https://arxiv.org/pdf/2212.06817. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 13 (Figure/Table caption), p. 13 (6 EXPERIMENTS), p. 12 (Figure/Table caption), p. 8 (6 EXPERIMENTS), p. 12 (6 EXPERIMENTS), p. 9 (6 EXPERIMENTS)): Table 5: Experimental results for mixing data from two different robots. Incorporating Kuka bin- picking data from QT-Opt (Kalashnikov et al., 2018) in RT-1 minimally impacts the standard class- room ...

## Evaluation Body Digest

- **p. 12 / 6 EXPERIMENTS - extractive body cue:** It also improves real-world generalization on simulated objects used with skills seen only in the real world (+26%), e.g. "move X to Y" where X ...
- **p. 9 / 6 EXPERIMENTS - extractive body cue:** Note, however, that all models are trained on the same data as RT-1, and the evaluation only compares the model architectures, not the task sets, ...
- **p. 11 / 6 EXPERIMENTS - extractive body cue:** RT-1 trained across large datasets of different tasks, originally collected by different robots.
- **p. 12 / 6 EXPERIMENTS - extractive body cue:** The Kuka data contains all the successful examples collected in QT-Opt (Kalashnikov et al., 2018), which corresponds to 209k episodes, where the robot was indiscriminately ...
- **p. 8 / 6 EXPERIMENTS - extractive body cue:** Throughout this section, we evaluate our approach and baselines with over 3000 real-world trials, making one of the largest scale evaluation of a robot learning ...
- **p. 13 / 6 EXPERIMENTS - extractive body cue:** Kitchen2 constitutes a much more challenging generalization scene, since the Robot Classroom training scenes are modeled after Kitchen1 (see the pictures of the kitchens in ...
- **p. 13 / 6 EXPERIMENTS - extractive body cue:** These results indicate that RT-1's absorption properties also include the ability to acquire new skills through observing other robots' experiences and present an exciting avenue ...
- **p. 14 / 6 EXPERIMENTS - extractive body cue:** Instead, in this study we focus on ablating the influence of dataset size and diversity, as they play an important role in the traditionally data-limited ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 6 EXPERIMENTS (p. 8).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 5: Experimental results for mixing data from two different robots. Incorporating Kuka bin- picking data from QT-Opt (Kalashnikov et al., 2018) in RT-1 ... | p. 13 (Figure/Table caption) |
| 6 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Due to this generalization difficulty, SayCan with Gato is not able to finish any long horizon task, and SayCan with BC-Z is able to ... | p. 13 (6 EXPERIMENTS) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 4: Experimental results for incorporating simulation data in RT-1. Adding simulation data does not impact the performance on real objects, while significantly improving ... | p. 12 (Figure/Table caption) |
| 6 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | We evaluate the success rate in experiments to measure performance on training instructions, generalization to unseen instructions, robustness to backgrounds and distractors, and performance ... | p. 8 (6 EXPERIMENTS) |
| 6 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Preprint Real Objects Sim Objects (not seen in real) Seen Skill Seen Skill Unseen Skill Models Training Data w/ Objects w/ Objects w/ Objects ... | p. 12 (6 EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 12 / 6 EXPERIMENTS - extractive body cue:** It also improves real-world generalization on simulated objects used with skills seen only in the real world (+26%), e.g. "move X to Y" where X ...
- **p. 9 / 6 EXPERIMENTS - extractive body cue:** Note, however, that all models are trained on the same data as RT-1, and the evaluation only compares the model architectures, not the task sets, ...
- **p. 11 / 6 EXPERIMENTS - extractive body cue:** RT-1 trained across large datasets of different tasks, originally collected by different robots.
- **p. 12 / 6 EXPERIMENTS - extractive body cue:** The Kuka data contains all the successful examples collected in QT-Opt (Kalashnikov et al., 2018), which corresponds to 209k episodes, where the robot was indiscriminately ...
- **p. 8 / 6 EXPERIMENTS - extractive body cue:** Throughout this section, we evaluate our approach and baselines with over 3000 real-world trials, making one of the largest scale evaluation of a robot learning ...
- **p. 13 / 6 EXPERIMENTS - extractive body cue:** Kitchen2 constitutes a much more challenging generalization scene, since the Robot Classroom training scenes are modeled after Kitchen1 (see the pictures of the kitchens in ...
- **p. 13 / 6 EXPERIMENTS - extractive body cue:** These results indicate that RT-1's absorption properties also include the ability to acquire new skills through observing other robots' experiences and present an exciting avenue ...
- **p. 14 / 6 EXPERIMENTS - extractive body cue:** Instead, in this study we focus on ablating the influence of dataset size and diversity, as they play an important role in the traditionally data-limited ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: A high-level overview of RT-1's architecture, dataset, and evaluation. The two main challenges lie in assembling the right dataset and designing the right ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 2: (a) Robot classroom where we collect data at scale; (b) a real office kitchen, one of the two realistic environments used for evaluation ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3: The architecture diagram of RT-1. The instruction is transformed into a USE embedding and used to condition a pre-trained EfficientNet via FiLM layers. ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1: The list of skills collected for RT-1 together with their descriptions and example instruc- tions. Our goal is to build a system that ...
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 4: Evaluation scenarios for distractors (first row), from left to right: easy (0-5 distractors), medium (9 distractors), hard (9 distractors and occluded object); background ...
- **p. 10 / Figure/Table caption - extractive body cue:** Table 2: Overall performance of RT-1 and baselines across seen tasks, generalization to unseen tasks, and robustness to distractors and backgrounds. tions successfully, which is ...
- **p. 11 / Figure/Table caption - extractive body cue:** Figure 5: Example evaluation trajectories for RT-1 across various instructions. Generalization Scenario Levels Models All L1 L2 L3 Gato Reed et al. (2022)
- **p. 11 / Figure/Table caption - extractive body cue:** Table 3: Realistic generalization scenarios: we compare model success rate in a realistic Google kitchen scenarios across three levels of generalization: L1 for generalization to ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | It also improves real-world generalization on simulated objects used with skills seen only in the real world (+26%), e.g. "move X to Y" where ... | embodiment, simulator version and control stack | p. 12 (6 EXPERIMENTS), p. 9 (6 EXPERIMENTS) |
| Task/environment | Note, however, that all models are trained on the same data as RT-1, and the evaluation only compares the model architectures, not the task ... | reset, timeout, object/scene variation | p. 9 (6 EXPERIMENTS), p. 11 (6 EXPERIMENTS) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 4 (3 PRELIMINARIES), p. 2 (3 Hz) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 3 (3 PRELIMINARIES), p. 2 (3 Hz) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We evaluate the success rate in experiments to measure performance on training instructions, generalization to unseen instructions, robustness to backgrounds and distractors, and performance ... | definition/direction/unit from same section | p. 8 (6 EXPERIMENTS) |
| We report the per-task success rate in these realistic scenarios along with the varying generalization levels in Table 3 and find RT-1 to be ... | definition/direction/unit from same section | p. 10 (6 EXPERIMENTS) |
| (2021) 45 38 50 50 BC-Z XL 55 63 75 38 RT-1 (ours) 70 88 75 50 Table 3: Realistic generalization scenarios: we compare ... | definition/direction/unit from same section | p. 11 (6 EXPERIMENTS) |
| Preprint Real Objects Sim Objects (not seen in real) Seen Skill Seen Skill Unseen Skill Models Training Data w/ Objects w/ Objects w/ Objects ... | definition/direction/unit from same section | p. 12 (6 EXPERIMENTS) |
| Except for original SayCan, all methods get 87% as planning success rate, and RT-1 performs the best, with 67% execution success rate in Kitchen1. | definition/direction/unit from same section | p. 13 (6 EXPERIMENTS) |
| Due to this generalization difficulty, SayCan with Gato is not able to finish any long horizon task, and SayCan with BC-Z is able to ... | definition/direction/unit from same section | p. 13 (6 EXPERIMENTS) |
| (*Original SayCan eval uses a slightly different prompt so the planning success rate is lower.) 6.5 HOW DO GENERALIZATION METRICS CHANGE WITH VARYING AMOUNTS ... | definition/direction/unit from same section | p. 14 (6 EXPERIMENTS) |
| Table 11: SayCan style long horizon tasks in Kitchen1 and Kitchen2. (*Original SayCan eval uses a slightly different prompt so the planning success rate ... | definition/direction/unit from same section | p. 29 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| (Appendix Section D.4) Throughout this section we will compare to two baseline state of the art architectures, Gato (Reed et al., 2022) and BC-Z ... | comparison identity and matched condition | p. 8 (6 EXPERIMENTS) |
| Throughout this section, we evaluate our approach and baselines with over 3000 real-world trials, making one of the largest scale evaluation of a robot ... | comparison identity and matched condition | p. 8 (6 EXPERIMENTS) |
| Across each category, we find that RT-1 outperforms the prior models significantly. | comparison identity and matched condition | p. 9 (6 EXPERIMENTS) |
| To answer our first question, we analyze the overall performance, generalization, and robustness capabilities of RT-1 compared to previously proposed models. | comparison identity and matched condition | p. 9 (6 EXPERIMENTS) |
| On unseen tasks, RT-1 shows it is capable of generalizing to novel instructions, performing 76% of the never-before-seen instructions, 24% more than the next ... | comparison identity and matched condition | p. 10 (6 EXPERIMENTS) |
| While such generalization to novel instructions is made possible due to natural language conditioning of the policy, as the policy is able to understand ... | comparison identity and matched condition | p. 10 (6 EXPERIMENTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 5: Experimental results for mixing data from two different robots. Incorporating Kuka bin- picking data from QT-Opt (Kalashnikov et al., 2018) in RT-1 ... | component/input/data sensitivity | p. 13 (Figure/Table caption) |
| First, it computes image tokens without the notion of language and each image token embedding is computed separately for each image patch, as opposed ... | component/input/data sensitivity | p. 8 (6 EXPERIMENTS) |
| We demonstrate how RT1 can incorporate and learn from vastly different data sources and improve from such data without sacrificing its original-tasks performance across ... | component/input/data sensitivity | p. 10 (6 EXPERIMENTS) |
| Generalization Models % Tasks % Data Seen Tasks All Unseen Tasks Distractors Backgrounds Smaller Data RT-1 (ours) 100 100 97 73 76 83 59 ... | component/input/data sensitivity | p. 14 (6 EXPERIMENTS) |
| Figure 11: "Realistic instructions" evaluations propose realistic scenarios multiple distribution shifts that incrementally increase in difficulty. L1 generalization introduces a new real office kitchen ... | component/input/data sensitivity | p. 24 (Figure/Table caption) |
| Table 11: SayCan style long horizon tasks in Kitchen1 and Kitchen2. (*Original SayCan eval uses a slightly different prompt so the planning success rate ... | component/input/data sensitivity | p. 29 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We propose a novel architecture that we call RT-1 (Robotics Transformer 1), which by encoding high-dimensional inputs and outputs, including camera images, instructions and ... | Table 5: Experimental results for mixing data from two different robots. Incorporating Kuka bin- picking data from QT-Opt (Kalashnikov et al., 2018) in RT-1 ... | PDF body cue; verify exact table/figure and matched conditions | p. 13 (Figure/Table caption), p. 13 (6 EXPERIMENTS), p. 12 (Figure/Table caption), p. 8 (6 EXPERIMENTS), p. 12 (6 EXPERIMENTS), p. 9 (6 EXPERIMENTS) |
| Primary metric/result | Due to this generalization difficulty, SayCan with Gato is not able to finish any long horizon task, and SayCan with BC-Z is able to ... | numeric claim only at cited anchor | p. 13 (6 EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 8 / 6 EXPERIMENTS - extractive body cue:** In order to run Gato on real robots at a high enough frequency, we also limit the size of the model compared to the original ...
- **p. 8 / 6 EXPERIMENTS - extractive body cue:** In all, we test over 200 tasks in this evaluation: 36 for picking objects, 35 for knocking objects, 35 for placing things upright, 48 for ...
- **p. 9 / 6 EXPERIMENTS - extractive body cue:** To evaluate robustness, we perform 30 real-world tasks for distractor robustness and 22 tasks for background robustness.
- **p. 9 / 6 EXPERIMENTS - extractive body cue:** BC-Z uses 100 tasks and the original Gato model trains a stacking task with various shapes), and thus this comparison should be viewed as rather ...
- **p. 12 / 6 EXPERIMENTS - extractive body cue:** This is a 17% performance difference (almost 2x).
- **p. 13 / 6 EXPERIMENTS - extractive body cue:** Incorporating Kuka binpicking data from QT-Opt (Kalashnikov et al., 2018) in RT-1 minimally impacts the standard classroom evaluation performance and results in almost a 2x ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Table 13: Various model ablations of RT-1 across seen tasks, generalization to unseen tasks, and robustness to distractors and backgrounds. for all the models, ... | p. 30 (Figure/Table caption) |
| body limitation/failure cue | Second, it does not use a pre-trained text embedding to encode the language string. | p. 8 (6 EXPERIMENTS) |
| body limitation/failure cue | It also does not include inference time considerations that are necessary for real robots as discussed in Sec. | p. 8 (6 EXPERIMENTS) |
| body limitation/failure cue | Adding simulation data does not impact the performance on real objects, while significantly improving real performance on objects that were only introduced in simulation ... | p. 12 (6 EXPERIMENTS) |
| body limitation/failure cue | Surprisingly, the manipulation performance does not 13 | p. 13 (6 EXPERIMENTS) |
| body limitation/failure cue | These results indicate that RT-1's absorption properties also include the ability to acquire new skills through observing other robots' experiences and present an exciting ... | p. 13 (6 EXPERIMENTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| In order to run Gato on real robots at a high enough frequency, we also limit the size of the model compared to the ... | p. 8 (6 EXPERIMENTS) |
| It also does not include inference time considerations that are necessary for real robots as discussed in Sec. | p. 8 (6 EXPERIMENTS) |
| These evaluations consist of 15 long-horizon instructions in two real kitchens, which require executing sequences of skills consisting of ∼10 distinct steps, with each ... | p. 9 (6 EXPERIMENTS) |
| These steps are obtained automatically from higher level instructions, such as "how would you throw away all the items on the table?" by using ... | p. 9 (6 EXPERIMENTS) |
| In the supplementary video, we show that this enables us to operate unseen drawers in Kitchen2, and that we can use SayCan-RT1 to plan ... | p. 14 (6 EXPERIMENTS) |
| Based on our experiments this requirement corresponds to at least 3Hz control frequency and the resulting inference time budget for the model, given other ... | p. 7 (3 PRELIMINARIES) |
| This workflow mirrors the classic approach to supervised learning in other domains, such as computer vision and NLP, where task-specific datasets would be collected, ... | p. 1 (1 INTRODUCTION) |
| While this capability has been demonstrated in other fields such as computer vision, natural language processing or speech recognition, it remains to be shown ... | p. 1 (ABSTRACT) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 30 / Figure/Table caption - extractive body cue:** Table 13: Various model ablations of RT-1 across seen tasks, generalization to unseen tasks, and robustness to distractors and backgrounds. for all the models, and ...
- **p. 8 / 6 EXPERIMENTS - extractive body cue:** Second, it does not use a pre-trained text embedding to encode the language string.
- **p. 8 / 6 EXPERIMENTS - extractive body cue:** It also does not include inference time considerations that are necessary for real robots as discussed in Sec.
- **p. 12 / 6 EXPERIMENTS - extractive body cue:** Adding simulation data does not impact the performance on real objects, while significantly improving real performance on objects that were only introduced in simulation (+64%).
- **p. 13 / 6 EXPERIMENTS - extractive body cue:** Surprisingly, the manipulation performance does not 13
- **p. 13 / 6 EXPERIMENTS - extractive body cue:** These results indicate that RT-1's absorption properties also include the ability to acquire new skills through observing other robots' experiences and present an exciting avenue ...

- **Evidence anchors reviewed:** datasets p. 12 (6 EXPERIMENTS), p. 9 (6 EXPERIMENTS), p. 11 (6 EXPERIMENTS), p. 12 (6 EXPERIMENTS), p. 8 (6 EXPERIMENTS), p. 13 (6 EXPERIMENTS), metrics p. 8 (6 EXPERIMENTS), p. 10 (6 EXPERIMENTS), p. 11 (6 EXPERIMENTS), p. 12 (6 EXPERIMENTS), p. 13 (6 EXPERIMENTS), p. 13 (6 EXPERIMENTS), baselines p. 8 (6 EXPERIMENTS), p. 8 (6 EXPERIMENTS), p. 9 (6 EXPERIMENTS), p. 9 (6 EXPERIMENTS), p. 10 (6 EXPERIMENTS), p. 10 (6 EXPERIMENTS), results p. 13 (Figure/Table caption), p. 13 (6 EXPERIMENTS), p. 12 (Figure/Table caption), p. 8 (6 EXPERIMENTS), p. 12 (6 EXPERIMENTS), p. 9 (6 EXPERIMENTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (31 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Table 4: Experimental results for incorporating simulation data in RT-1. Adding simulation data does not impact the performance on real objects, while significantly improving real performance on objects that were ... (p. 12, Figure/Table caption).
- **Metric evidence:** We evaluate the success rate in experiments to measure performance on training instructions, generalization to unseen instructions, robustness to backgrounds and distractors, and performance in long-horizon scenarios, as detailed below. (p. 8, 6 EXPERIMENTS).
- **Baseline/ablation evidence:** (Appendix Section D.4) Throughout this section we will compare to two baseline state of the art architectures, Gato (Reed et al., 2022) and BC-Z (Jang et al., 2021). (p. 8, 6 EXPERIMENTS).
- **Failure/negative evidence:** 7 CONCLUSIONS, LIMITATIONS AND FUTURE WORK We presented Robotics Transformer 1, RT-1, a robot learning method that can effectively absorb large amounts of data and scales with data quantity and ... (p. 15, 6 EXPERIMENTS).
