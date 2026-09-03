# Evaluation - AHA: A Vision-Language-Model for Detecting and Reasoning Over Failures in Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=JVkdSi7Ekg; PDF retrieval source: https://openreview.net/pdf/baa69f167306f963174767be4974c69528aa6379.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 9 (Figure/Table caption), p. 3 (Figure/Table caption), p. 10 (4 Method), p. 10 (4 Method), p. 9 (4 Method), p. 7 (4 Method)): Figure 3: (Left) Scaling law with the AHA dataset. Scaling of effect of model performance with varying domain specific fine-tuning data. (Right) Downstream Robotic Application Performance. AHA-13B outperforms GPT-4o in ...

## Evaluation Body Digest

- **p. 8 / 4 Method - extractive body cue:** Lastly, we adapted a failure benchmark from the RoboFail dataset [48], which features real-world robot failures in seven UR5 robot tasks.
- **p. 8 / 4 Method - extractive body cue:** MMBench [54] ScienceQA [55] TextVQA [56] POPE [57] VizWiz[58] LLaVA-13B (LLama-2) [24] 67.70 73.21 67.40 88.00 53.01 AHA-13B (LLama-2) 65.20 71.94 65.20 85.74 53.45 5.1 ...
- **p. 7 / 4 Method - extractive body cue:** The evaluation spans three diverse datasets, covering out-of-domain tasks, various simulation environments, and cross-embodiment scenarios.
- **p. 9 / 4 Method - extractive body cue:** Lastly, to demonstrate generalization to real-world robots and different embodiments, we evaluated AHA-13B on RoboFail [48], where it outperforms GPT-4o-ICL by 4.9% difference.
- **p. 7 / 4 Method - extractive body cue:** To achieve this, we developed FailGen, an environment wrapper that can be easily applied to any robot manipulation simulator.
- **p. 9 / 4 Method - extractive body cue:** AHA-13B outperforms GPT-4o in reasoning about failures within these robotic applications, leading to improved performance of the downstream tasks. model-specifically, Anthropic's unseen model, claude-3-sonnet-to evaluate ...
- **p. 10 / 4 Method - extractive body cue:** The PRoC3S system solves tasks specified in natural language by prompting an LLM for a Language-Model Program (LMP) that generates plans, and then testing a ...
- **p. 10 / 4 Method - extractive body cue:** We demonstrated that AHA can be integrated into existing LLM/VLM-assisted robotic applications to provide failure reasoning and feedback, helping to accelerate and improve task success ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** not reliably recovered.

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 3: (Left) Scaling law with the AHA dataset. Scaling of effect of model performance with varying domain specific fine-tuning data. (Right) Downstream Robotic ... | p. 9 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 1: AHA is a Vision-Language Model designed to detect and reason about failures in robotic manipulation. As an instruction-tuned VLM, it can enhance ... | p. 3 (Figure/Table caption) |
| 4 Method | EMPIRICAL / REAL-ROBOT OR HARDWARE | This resulted in success across all five tasks within the budget constraints, and our approach outperformed GPT4o by a significant margin of 22.34% in ... | p. 10 (4 Method) |
| 4 Method | EMPIRICAL / REAL-ROBOT OR HARDWARE | We demonstrated that AHA can be integrated into existing LLM/VLM-assisted robotic applications to provide failure reasoning and feedback, helping to accelerate and improve task ... | p. 10 (4 Method) |
| 4 Method | EMPIRICAL / REAL-ROBOT OR HARDWARE | This suggests that further scaling of the generated data may lead to improved model performance. | p. 9 (4 Method) |

## Dataset / Benchmark Role

- **p. 8 / 4 Method - extractive body cue:** Lastly, we adapted a failure benchmark from the RoboFail dataset [48], which features real-world robot failures in seven UR5 robot tasks.
- **p. 8 / 4 Method - extractive body cue:** MMBench [54] ScienceQA [55] TextVQA [56] POPE [57] VizWiz[58] LLaVA-13B (LLama-2) [24] 67.70 73.21 67.40 88.00 53.01 AHA-13B (LLama-2) 65.20 71.94 65.20 85.74 53.45 5.1 ...
- **p. 7 / 4 Method - extractive body cue:** The evaluation spans three diverse datasets, covering out-of-domain tasks, various simulation environments, and cross-embodiment scenarios.
- **p. 9 / 4 Method - extractive body cue:** Lastly, to demonstrate generalization to real-world robots and different embodiments, we evaluated AHA-13B on RoboFail [48], where it outperforms GPT-4o-ICL by 4.9% difference.
- **p. 7 / 4 Method - extractive body cue:** To achieve this, we developed FailGen, an environment wrapper that can be easily applied to any robot manipulation simulator.
- **p. 9 / 4 Method - extractive body cue:** AHA-13B outperforms GPT-4o in reasoning about failures within these robotic applications, leading to improved performance of the downstream tasks. model-specifically, Anthropic's unseen model, claude-3-sonnet-to evaluate ...
- **p. 10 / 4 Method - extractive body cue:** The PRoC3S system solves tasks specified in natural language by prompting an LLM for a Language-Model Program (LMP) that generates plans, and then testing a ...
- **p. 10 / 4 Method - extractive body cue:** We demonstrated that AHA can be integrated into existing LLM/VLM-assisted robotic applications to provide failure reasoning and feedback, helping to accelerate and improve task success ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 3 / Figure/Table caption - extractive body cue:** Figure 1: AHA is a Vision-Language Model designed to detect and reason about failures in robotic manipulation. As an instruction-tuned VLM, it can enhance task ...
- **p. 4 / Figure/Table caption - extractive body cue:** Table 1: AHA datasets for instruction-tuning. We combined the AHA dataset, our large-scale robotic manipulation failure dataset, with VQA and object detection data. By incorporating ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 2: Overview of AHA Pipeline. (Top) The data generation for AHA is accomplished by taking a normal task trajectory in simulation and procedurally perturbing ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 2: Quantitative Evaluation on Failure Detection and Reasoning. AHA-13B was evaluated and benchmarked against three open and three proprietary VLMs and one visual prompting ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 3: Quantitative Evaluation on Standard VQA Benchmarks. AHA-13B performs on par with LLaVA-13B [24], the VLM from which AHA adapts its fine-tuning strategy. MMBench ...
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 3: (Left) Scaling law with the AHA dataset. Scaling of effect of model performance with varying domain specific fine-tuning data. (Right) Downstream Robotic Application ...
- **p. 10 / Figure/Table caption - extractive body cue:** Figure 4: Downstream Robotic Application. We demonstrated that AHA can be integrated into existing LLM/VLM-assisted robotic applications to provide failure reasoning and feedback, helping to ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Lastly, we adapted a failure benchmark from the RoboFail dataset [48], which features real-world robot failures in seven UR5 robot tasks. | embodiment, simulator version and control stack | p. 8 (4 Method), p. 8 (4 Method) |
| Task/environment | MMBench [54] ScienceQA [55] TextVQA [56] POPE [57] VizWiz[58] LLaVA-13B (LLama-2) [24] 67.70 73.21 67.40 88.00 53.01 AHA-13B (LLama-2) 65.20 71.94 65.20 85.74 53.45 ... | reset, timeout, object/scene variation | p. 8 (4 Method), p. 7 (4 Method) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 7 (4 Method), p. 6 (4 Method) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 10 (4 Method), p. 6 (4 Method) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Comparing the evaluated policy success rates using different failure feedback VLMs, we observed that AHA-13B provided intuitive, human-level failure reasoning that aided in modifying ... | definition/direction/unit from same section | p. 10 (4 Method) |
| Figure 4: Downstream Robotic Application. We demonstrated that AHA can be integrated into existing LLM/VLM-assisted robotic applications to provide failure reasoning and feedback, helping ... | definition/direction/unit from same section | p. 10 (Figure/Table caption) |
| Figure 1: AHA is a Vision-Language Model designed to detect and reason about failures in robotic manipulation. As an instruction-tuned VLM, it can enhance ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |
| Figure 3: (Left) Scaling law with the AHA dataset. Scaling of effect of model performance with varying domain specific fine-tuning data. (Right) Downstream Robotic ... | definition/direction/unit from same section | p. 9 (Figure/Table caption) |
| First, the ROUGE-L score measures the quality of generated text by focusing on the longest common subsequence between candidate and reference texts. | definition/direction/unit from same section | p. 8 (4 Method) |
| This suggests that further scaling of the generated data may lead to improved model performance. | definition/direction/unit from same section | p. 9 (4 Method) |
| Next, we discuss the curated data mix used for co-finetuning AHA (Sec.4.2). | definition/direction/unit from same section | p. 6 (4 Method) |
| If the answer is "No", the VLM is expected to generate a concise, free-form natural language explanation detailing why the task is perceived as ... | definition/direction/unit from same section | p. 6 (4 Method) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Table 2: Quantitative Evaluation on Failure Detection and Reasoning. AHA-13B was evaluated and benchmarked against three open and three proprietary VLMs and one visual ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| 5 Experimental Results In this section, we evaluate AHA's detection and reasoning performance against six state-of-the-art VLMs, including both open-source and proprietary models, some ... | comparison identity and matched condition | p. 7 (4 Method) |
| To fairly evaluate success detection and free language reasoning across all datasets and baselines, we employ four metrics. | comparison identity and matched condition | p. 8 (4 Method) |
| Lastly, to demonstrate generalization to real-world robots and different embodiments, we evaluated AHA-13B on RoboFail [48], where it outperforms GPT-4o-ICL by 4.9% difference. | comparison identity and matched condition | p. 9 (4 Method) |
| Second, we assessed AHA-13B on a dataset generated by the Failgen wrapper in a different simulation domain, ManiSkill, showing that our model outperforms GPT-4o-ICL ... | comparison identity and matched condition | p. 9 (4 Method) |
| We compared GPT-4o and AHA-13B as the VLM-based failure reasoning modules within this implementation of PRoC3S across three tasks (shown in Figure 4). | comparison identity and matched condition | p. 10 (4 Method) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Scaling of effect of model performance with varying domain specific fine-tuning data. | component/input/data sensitivity | p. 9 (4 Method) |
| The first dataset, AHA dataset (Test), includes 11k image-question pairs from 10 RLBench tasks, generated similarly to the fine-tuning data via FailGen (Section 3.2) ... | component/input/data sensitivity | p. 8 (4 Method) |
| An average quadratic fit gradient of 0.0022 across all four metrics demonstrates a scaling effect with fine-tuning on our procedurally generated data pipeline. | component/input/data sensitivity | p. 9 (4 Method) |
| Table 1: AHA datasets for instruction-tuning. We combined the AHA dataset, our large-scale robotic manipulation failure dataset, with VQA and object detection data. By ... | component/input/data sensitivity | p. 4 (Figure/Table caption) |
| For the input formulation in VLMs for instruction fine-tuning and evaluation, we required a query prompt 6 | component/input/data sensitivity | p. 6 (4 Method) |
| This section outlines the failure reasoning problem formulation (Sec.4.1) used to fine-tune and evaluate AHA. | component/input/data sensitivity | p. 6 (4 Method) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We introduce AHA, an open-source vision-language model (VLM) that uses natural language to detect and reason about failures in robotic manipulation. | Figure 3: (Left) Scaling law with the AHA dataset. Scaling of effect of model performance with varying domain specific fine-tuning data. (Right) Downstream Robotic ... | PDF body cue; verify exact table/figure and matched conditions | p. 9 (Figure/Table caption), p. 3 (Figure/Table caption), p. 10 (4 Method), p. 10 (4 Method), p. 9 (4 Method), p. 7 (4 Method) |
| Primary metric/result | Figure 1: AHA is a Vision-Language Model designed to detect and reason about failures in robotic manipulation. As an instruction-tuned VLM, it can enhance ... | numeric claim only at cited anchor | p. 3 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 10 / 4 Method - extractive body cue:** Each task was evaluated over 10 trials, with a 10
- **p. 10 / 4 Method - extractive body cue:** Each task was evaluated over 10 trials, with a 10

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Importantly, as is typical of TAMP methods, the original approach checks for a finite set of failures (inverse kinematics, collisions, etc.) from the environment, ... | p. 10 (4 Method) |
| body limitation/failure cue | Figure 1: AHA is a Vision-Language Model designed to detect and reason about failures in robotic manipulation. As an instruction-tuned VLM, it can enhance ... | p. 3 (Figure/Table caption) |
| body limitation/failure cue | Table 1: AHA datasets for instruction-tuning. We combined the AHA dataset, our large-scale robotic manipulation failure dataset, with VQA and object detection data. By ... | p. 4 (Figure/Table caption) |
| body limitation/failure cue | This section outlines the failure reasoning problem formulation (Sec.4.1) used to fine-tune and evaluate AHA. | p. 6 (4 Method) |
| body limitation/failure cue | If the answer is "No", the VLM is expected to generate a concise, free-form natural language explanation detailing why the task is perceived as ... | p. 6 (4 Method) |
| body limitation/failure cue | 4.2 Synthetic Data for Instruction-tuning To facilitate the instruction-tuning of AHA, we needed to systematically generate failure demonstration data. | p. 7 (4 Method) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| During fine-tuning, only the projector and transformer weights are updated, while the vision encoder and tokenizer remain frozen. | p. 7 (4 Method) |
| The image encoder processes images into tokens, projected by a 2-layer linear projector into the same space as the language tokens. | p. 7 (4 Method) |
| We evaluated Aha's performance using a range of AHA data for instruction fine-tuning, spanning [3k, 6k, 12k, 34k, 48k, 60k], and co-trained individual checkpoints ... | p. 9 (4 Method) |
| Each task was evaluated over 10 trials, with a 10 | p. 10 (4 Method) |
| Each policy was trained using PPO over task-specific training steps and evaluated across 1,000 test steps. | p. 10 (4 Method) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 10 / 4 Method - extractive body cue:** Importantly, as is typical of TAMP methods, the original approach checks for a finite set of failures (inverse kinematics, collisions, etc.) from the environment, and ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 1: AHA is a Vision-Language Model designed to detect and reason about failures in robotic manipulation. As an instruction-tuned VLM, it can enhance task ...
- **p. 4 / Figure/Table caption - extractive body cue:** Table 1: AHA datasets for instruction-tuning. We combined the AHA dataset, our large-scale robotic manipulation failure dataset, with VQA and object detection data. By incorporating ...
- **p. 6 / 4 Method - extractive body cue:** This section outlines the failure reasoning problem formulation (Sec.4.1) used to fine-tune and evaluate AHA.
- **p. 6 / 4 Method - extractive body cue:** If the answer is "No", the VLM is expected to generate a concise, free-form natural language explanation detailing why the task is perceived as a ...
- **p. 7 / 4 Method - extractive body cue:** 4.2 Synthetic Data for Instruction-tuning To facilitate the instruction-tuning of AHA, we needed to systematically generate failure demonstration data.

- **Evidence anchors reviewed:** datasets p. 8 (4 Method), p. 8 (4 Method), p. 7 (4 Method), p. 9 (4 Method), p. 7 (4 Method), p. 9 (4 Method), metrics p. 10 (4 Method), p. 10 (Figure/Table caption), p. 3 (Figure/Table caption), p. 9 (Figure/Table caption), p. 8 (4 Method), p. 9 (4 Method), baselines p. 8 (Figure/Table caption), p. 7 (4 Method), p. 8 (4 Method), p. 9 (4 Method), p. 9 (4 Method), p. 10 (4 Method), results p. 9 (Figure/Table caption), p. 3 (Figure/Table caption), p. 10 (4 Method), p. 10 (4 Method), p. 9 (4 Method), p. 7 (4 Method).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (15 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Table 2: Quantitative Evaluation on Failure Detection and Reasoning. AHA-13B was evaluated and benchmarked against three open and three proprietary VLMs and one visual prompting baseline across three evaluation datasets. ... (p. 8, Figure/Table caption).
- **Metric evidence:** Figure 1: AHA is a Vision-Language Model designed to detect and reason about failures in robotic manipulation. As an instruction-tuned VLM, it can enhance task performance in robotic applications that ... (p. 3, Figure/Table caption).
- **Baseline/ablation evidence:** Table 2: Quantitative Evaluation on Failure Detection and Reasoning. AHA-13B was evaluated and benchmarked against three open and three proprietary VLMs and one visual prompting baseline across three evaluation datasets. ... (p. 8, Figure/Table caption).
- **Failure/negative evidence:** Importantly, as is typical of TAMP methods, the original approach checks for a finite set of failures (inverse kinematics, collisions, etc.) from the environment, and returns any sampled plan that ... (p. 10, 4 Method).
