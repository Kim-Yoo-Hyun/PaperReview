# Evaluation - RDT-1B: a Diffusion Foundation Model for Bimanual Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (28 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=yAzN4tz7oI; PDF retrieval source: https://openreview.net/pdf/29d56379d000b8c0e05906c5958e67e2e870ab0c.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 9 (5 EXPERIMENTS), p. 10 (Figure/Table caption), p. 9 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS), p. 26 (Figure/Table caption), p. 6 (Figure/Table caption)): In Wash Cup and Pour Water, RDT can still achieve a high success rate on unseen scenarios, and its performance is not much different from that on seen ones.

## Evaluation Body Digest

- **p. 7 / 5 EXPERIMENTS - extractive body cue:** We aim to answer the following questions through real-robot experiments: Q1: Can RDT zero-shot generalize to unseen objects and scenes?
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** TASK NAME DIMENSION EXPLANATION Wash Cup Unseen Object (Q1) To wash one seen and two unseen cups with the faucet Pour Water Unseen Scene (Q1) ...
- **p. 7 / 5 EXPERIMENTS - extractive body cue:** We select 7 challenging tasks to evaluate the generalizability and capabilities of RDT from different dimensions, including complex scenarios that the model may encounter in ...
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** Here is a detailed analysis: • Q1 & Q2: RDT can zero-shot generalize to unseen objects, scenes, and modalities.
- **p. 10 / 5 EXPERIMENTS - extractive body cue:** Sub-columns in each sub-task cell represent different elements (objects, instructions, scenes).
- **p. 10 / 5 EXPERIMENTS - extractive body cue:** In particular, RDT (scratch) performs poorly on unseen objects and scenes, indicating that the knowledge from pre-training is critical for generalization.
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** The robot needs to Pick Up Bottle (#1), Pour Water (#2), and Place Back Bottle (#3).
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** The robot needs to Pick Up Pen (#1), Switch Hand (#2), Drop Pen (#3), and ensure it can Fall into Box (#4).

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 5 EXPERIMENTS (p. 7).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 5 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | In Wash Cup and Pour Water, RDT can still achieve a high success rate on unseen scenarios, and its performance is not much different ... | p. 9 (5 EXPERIMENTS) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 3: Quantitative results. We report success rates (%) of ACT, OpenVLA, RDT (from scratch, no pre-trained), and RDT (ours, pre-trained) for 7 tasks. ... | p. 10 (Figure/Table caption) |
| 5 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Besides, the large number of parameters after large-scale pre-training provides a lot of prior knowledge, which significantly improves the generalizability. | p. 9 (5 EXPERIMENTS) |
| 5 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | In Handover and Fold Shorts, RDT has learned new and complex skills of handover and folding through few-shot learning, whose action patterns are very ... | p. 10 (5 EXPERIMENTS) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 11: Adapetd hyper-parameters of ACT. at https://huggingface.co/openvla/openvla-7b. For each task in evaluation, we further fine-tune the officially pre-trained OpenVLA with all the task-relevant ... | p. 26 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 7 / 5 EXPERIMENTS - extractive body cue:** We aim to answer the following questions through real-robot experiments: Q1: Can RDT zero-shot generalize to unseen objects and scenes?
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** TASK NAME DIMENSION EXPLANATION Wash Cup Unseen Object (Q1) To wash one seen and two unseen cups with the faucet Pour Water Unseen Scene (Q1) ...
- **p. 7 / 5 EXPERIMENTS - extractive body cue:** We select 7 challenging tasks to evaluate the generalizability and capabilities of RDT from different dimensions, including complex scenarios that the model may encounter in ...
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** Here is a detailed analysis: • Q1 & Q2: RDT can zero-shot generalize to unseen objects, scenes, and modalities.
- **p. 10 / 5 EXPERIMENTS - extractive body cue:** Sub-columns in each sub-task cell represent different elements (objects, instructions, scenes).
- **p. 10 / 5 EXPERIMENTS - extractive body cue:** In particular, RDT (scratch) performs poorly on unseen objects and scenes, indicating that the knowledge from pre-training is critical for generalization.
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** The robot needs to Pick Up Bottle (#1), Pour Water (#2), and Place Back Bottle (#3).
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** The robot needs to Pick Up Pen (#1), Switch Hand (#2), Drop Pen (#3), and ensure it can Fall into Box (#4).

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: Overview of Robotics Diffusion Transformer with 1B-Parameters (RDT-1B), a language-conditioned visuomotor policy for bimanual manipulation,with state-of-the-art generaliz- ability to unseen scenarios (See App. ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2: (a) Schematic diagram of the ALOHA dual-arm robot. (b) A toy example of grasping a cube. Compared with unimanual manipulation, bimanual manipulation has ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3: RDT framework. Heterogeneous action spaces of various robots are embedded into a unified action space for multi-robot training. Inputs: proprioception zt, noisy action ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4: (a) Unstable loss curve during training without QKNorm & RMSNorm. (b) Success rates of RDT (w/o MLP Decoder or w/o ACI) in tasks ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5: Task definitions and visualizations. For 7 challenging tasks, we describe their language instruction, randomization, and definitions of each sub-task. For Pour Water-L-1/3 and ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 1: Dimensions when designing tasks. For Pour Water-L-1/3 and Pour Water-R-2/3, only the water levels of little, half (i.e., 1/2), and full are seen ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 2: Ablation study results. Here are the success rates (%) of the original RDT and its three variants in tasks of Wash Cup (unseen ...
- **p. 10 / Figure/Table caption - extractive body cue:** Table 3: Quantitative results. We report success rates (%) of ACT, OpenVLA, RDT (from scratch, no pre-trained), and RDT (ours, pre-trained) for 7 tasks. Sub-columns ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We aim to answer the following questions through real-robot experiments: Q1: Can RDT zero-shot generalize to unseen objects and scenes? | embodiment, simulator version and control stack | p. 7 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS) |
| Task/environment | TASK NAME DIMENSION EXPLANATION Wash Cup Unseen Object (Q1) To wash one seen and two unseen cups with the faucet Pour Water Unseen Scene ... | reset, timeout, object/scene variation | p. 9 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 1 (ABSTRACT), p. 2 (1 INTRODUCTION) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| In Wash Cup and Pour Water, RDT can still achieve a high success rate on unseen scenarios, and its performance is not much different ... | definition/direction/unit from same section | p. 9 (5 EXPERIMENTS) |
| We employ the success rate as our main metric, which is calculated by dividing successful trials by total trials. | definition/direction/unit from same section | p. 9 (5 EXPERIMENTS) |
| We report success rates (%) of ACT, OpenVLA, RDT (from scratch, no pre-trained), and RDT (ours, pre-trained) for 7 tasks. | definition/direction/unit from same section | p. 10 (5 EXPERIMENTS) |
| In Handover and Fold Shorts, RDT has learned new and complex skills of handover and folding through few-shot learning, whose action patterns are very ... | definition/direction/unit from same section | p. 10 (5 EXPERIMENTS) |
| Figure 4: (a) Unstable loss curve during training without QKNorm & RMSNorm. (b) Success rates of RDT (w/o MLP Decoder or w/o ACI) in ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| Figure 8: The accuracy of action token prediction fluctuates rather than converges with the number of training steps when fine-tuning OpenVLA with the full ... | definition/direction/unit from same section | p. 26 (Figure/Table caption) |
| Table 11: Adapetd hyper-parameters of ACT. at https://huggingface.co/openvla/openvla-7b. For each task in evaluation, we further fine-tune the officially pre-trained OpenVLA with all the task-relevant ... | definition/direction/unit from same section | p. 26 (Figure/Table caption) |
| Q4: Is RDT capable of completing tasks that require delicate operations? and Q5: Are large model sizes, extensive data, and diffusion modeling helpful for ... | definition/direction/unit from same section | p. 7 (5 EXPERIMENTS) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| 5.2 RESULTS ANALYSIS From the results in Table 3, we can see that RDT consistently outperforms other baselines. | comparison identity and matched condition | p. 9 (5 EXPERIMENTS) |
| To comprehensively evaluate RDT, we consider the most advanced baselines in robotic foundation models and bimanual manipulation, including Action Chunking with Transformers 8 | comparison identity and matched condition | p. 8 (5 EXPERIMENTS) |
| In contrast, the other baselines cannot even complete the entire task. | comparison identity and matched condition | p. 9 (5 EXPERIMENTS) |
| RDT (ours) consistently outperforms others. | comparison identity and matched condition | p. 10 (5 EXPERIMENTS) |
| Figure 1: Overview of Robotics Diffusion Transformer with 1B-Parameters (RDT-1B), a language-conditioned visuomotor policy for bimanual manipulation,with state-of-the-art generaliz- ability to unseen scenarios (See ... | comparison identity and matched condition | p. 2 (Figure/Table caption) |
| Figure 2: (a) Schematic diagram of the ALOHA dual-arm robot. (b) A toy example of grasping a cube. Compared with unimanual manipulation, bimanual manipulation ... | comparison identity and matched condition | p. 3 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| VARIANT NAME UNSEEN OBJECT UNSEEN SCENE INSTRUCTION FOLLOWING RDT (regress) 12.5 50 12.5 RDT (small) 37.5 62.5 25 RDT (scratch) 0 25 62.5 RDT ... | component/input/data sensitivity | p. 9 (5 EXPERIMENTS) |
| Table 2: Ablation study results. Here are the success rates (%) of the original RDT and its three variants in tasks of Wash Cup ... | component/input/data sensitivity | p. 9 (Figure/Table caption) |
| In Table 2, there is a serious performance drop without any of these factors, demonstrating the necessity of our contributions. | component/input/data sensitivity | p. 10 (5 EXPERIMENTS) |
| Figure 1: Overview of Robotics Diffusion Transformer with 1B-Parameters (RDT-1B), a language-conditioned visuomotor policy for bimanual manipulation,with state-of-the-art generaliz- ability to unseen scenarios (See ... | component/input/data sensitivity | p. 2 (Figure/Table caption) |
| Figure 4: (a) Unstable loss curve during training without QKNorm & RMSNorm. (b) Success rates of RDT (w/o MLP Decoder or w/o ACI) in ... | component/input/data sensitivity | p. 6 (Figure/Table caption) |
| Table 7: Comparision of different baselines. We compare baselines as well as different variants of our model in terms of model size, data size, ... | component/input/data sensitivity | p. 25 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In this paper, we introduce the Robotics Diffusion Transformer (RDT), the largest bimanual manipulation foundation model with strong generalizability. | In Wash Cup and Pour Water, RDT can still achieve a high success rate on unseen scenarios, and its performance is not much different ... | PDF body cue; verify exact table/figure and matched conditions | p. 9 (5 EXPERIMENTS), p. 10 (Figure/Table caption), p. 9 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS), p. 26 (Figure/Table caption), p. 6 (Figure/Table caption) |
| Primary metric/result | Table 3: Quantitative results. We report success rates (%) of ACT, OpenVLA, RDT (from scratch, no pre-trained), and RDT (ours, pre-trained) for 7 tasks. ... | numeric claim only at cited anchor | p. 10 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** It can reduce the diffusion steps required to sample an action chunk from 100 steps to 5 steps, achieving an action chunk inference frequency of ...
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** Wash Cup is tested with 8 trials for each cup (one seen cup, two unseen cups, 24 trials in total).
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** Pour Water is tested with 8 trials for each room (three unseen rooms, 24 trials in total).
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** Pour Water-L-1/3 and Pour Water-R-2/3 are tested with 8 trials each.
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** Handover, Fold Shorts, and Robot Dog are tested with 25 trials each.
- **p. 10 / 5 EXPERIMENTS - extractive body cue:** We report success rates (%) of ACT, OpenVLA, RDT (from scratch, no pre-trained), and RDT (ours, pre-trained) for 7 tasks.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | It probably makes ACT prone to failure. | p. 10 (5 EXPERIMENTS) |
| body limitation/failure cue | Figure 4: (a) Unstable loss curve during training without QKNorm & RMSNorm. (b) Success rates of RDT (w/o MLP Decoder or w/o ACI) in ... | p. 6 (Figure/Table caption) |
| body limitation/failure cue | The robot needs to Pick Up Pen (#1), Switch Hand (#2), Drop Pen (#3), and ensure it can Fall into Box (#4). | p. 8 (5 EXPERIMENTS) |
| body limitation/failure cue | The robot needs to Pick Up Cup (#1), Turn On Faucet (#2), Get Water (#3, to ensure that the water falls into the cup), ... | p. 8 (5 EXPERIMENTS) |
| body limitation/failure cue | In contrast, the other baselines cannot even complete the entire task. | p. 9 (5 EXPERIMENTS) |
| body limitation/failure cue | We further introduce a Physically Interpretable Unified Action Space to unify action representations across different robots, enhancing robustness and transferability. | p. 10 (6 CONCLUSION) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| It can reduce the diffusion steps required to sample an action chunk from 100 steps to 5 steps, achieving an action chunk inference frequency ... | p. 8 (5 EXPERIMENTS) |
| It takes three days to fine-tune this model using the same GPUs for 130K steps. | p. 8 (5 EXPERIMENTS) |
| Pour Water-L-1/3 and Pour Water-R-2/3 are tested with 8 trials each. | p. 9 (5 EXPERIMENTS) |
| Handover, Fold Shorts, and Robot Dog are tested with 25 trials each. | p. 9 (5 EXPERIMENTS) |
| We refer to the project page for the code and videos. | p. 1 (ABSTRACT) |
| Following the success in natural language processing (Achiam et al., 2023; Touvron et al., 2023) and computer vision (Radford et al., 2021; Kirillov et ... | p. 1 (1 INTRODUCTION) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 10 / 5 EXPERIMENTS - extractive body cue:** It probably makes ACT prone to failure.
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4: (a) Unstable loss curve during training without QKNorm & RMSNorm. (b) Success rates of RDT (w/o MLP Decoder or w/o ACI) in tasks ...
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** The robot needs to Pick Up Pen (#1), Switch Hand (#2), Drop Pen (#3), and ensure it can Fall into Box (#4).
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** The robot needs to Pick Up Cup (#1), Turn On Faucet (#2), Get Water (#3, to ensure that the water falls into the cup), Pour ...
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** In contrast, the other baselines cannot even complete the entire task.
- **p. 10 / 6 CONCLUSION - extractive body cue:** We further introduce a Physically Interpretable Unified Action Space to unify action representations across different robots, enhancing robustness and transferability.

- **PDF anchors reviewed:** datasets p. 7 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS), metrics p. 9 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS), p. 6 (Figure/Table caption), p. 26 (Figure/Table caption), baselines p. 9 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS), p. 2 (Figure/Table caption), p. 3 (Figure/Table caption), results p. 9 (5 EXPERIMENTS), p. 10 (Figure/Table caption), p. 9 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS), p. 26 (Figure/Table caption), p. 6 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
