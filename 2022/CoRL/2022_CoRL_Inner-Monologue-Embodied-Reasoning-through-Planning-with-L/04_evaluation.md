# Evaluation - Inner Monologue: Embodied Reasoning through Planning with Language Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (25 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v205/huang23c.html; PDF retrieval source: https://arxiv.org/pdf/2207.05608. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (Figure/Table caption), p. 7 (Figure/Table caption), p. 6 (Figure/Table caption), p. 8 (Figure/Table caption), p. 17 (A.2 Inner Monologue for Real-World Tabletop Rearrangement), p. 18 (A.2 Inner Monologue for Real-World Tabletop Rearrangement)): Table 2: Inner Monologue (with object recognition and success detection feedback) on a real pick and place robot exceeds the performance of baseline alternatives, as measured by average task success ...

## Evaluation Body Digest

- **p. 16 / A.2 Inner Monologue for Real-World Tabletop Rearrangement - extractive body cue:** For the object sorting task, the scene description contains a list of currently visible objects and a list of objects that the robot has successfully ...
- **p. 17 / A.2 Inner Monologue for Real-World Tabletop Rearrangement - extractive body cue:** A.3 Inner Monologue for Real-World Mobile Manipulation in a Kitchen Setting Large Language Model We use PALM [8], a 540B parameter language model trained on ...
- **p. 17 / A.2 Inner Monologue for Real-World Tabletop Rearrangement - extractive body cue:** Environment Feedback: Object Recognition We use human-provided object recognition to provide feedback about the presence of objects visible to the robot camera.
- **p. 15 / A.1 Inner Monologue for Simulated Tabletop Rearrangement - extractive body cue:** Environment Feedback: Passive Scene Description For Object + Scene method, we provide task-progress scene description as a list of achieved sub-goals after each pick-and-place execution.
- **p. 15 / A.1 Inner Monologue for Simulated Tabletop Rearrangement - extractive body cue:** Environment Feedback: Object Recognition We provide the list of objects present in the scene at the start of each episode for the language model (without ...
- **p. 16 / A.2 Inner Monologue for Real-World Tabletop Rearrangement - extractive body cue:** Environment Feedback: Object Recognition For the block stacking task, the scene description contains a list of currently visible objects and a list of previously visible ...
- **p. 18 / A.2 Inner Monologue for Real-World Tabletop Rearrangement - extractive body cue:** Environment Feedback: Active Scene Description We perform a case study where we allow the LLM agent to ask questions and source Human feedback directly.
- **p. 18 / A.2 Inner Monologue for Real-World Tabletop Rearrangement - extractive body cue:** (a) Foresight success detector (b) Hindsight success detector Figure 7: Success Detection architecture used for the Kitchen Environment.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** A Inner Monologue Implementation Details (p. 15); B Experiment Details (p. 18); C Additional Results (p. 20).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 2: Inner Monologue (with object recognition and success detection feedback) on a real pick and place robot exceeds the performance of baseline alternatives, ... | p. 6 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 4: Failure causes on 120 evaluations. When disturbances are added (red), only the Inner Mono- logue variants consistently complete the instructions. Analysis. The ... | p. 7 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 1: Success rates for various methods, averaged across 50 episodes in Ravens-based environment with test-time disturbances. CLIPort + oracle indicates that CLIPort was ... | p. 6 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 5: Informing LLM with embodied feedback enables many emergent capabilities, all of which are achieved without similar prompted examples. For instance, Inner Monologue ... | p. 8 (Figure/Table caption) |
| A.2 Inner Monologue for Real-World Tabletop Rearrangement | EMPIRICAL / REAL-ROBOT OR HARDWARE | As advances in computer vision improve object detection models that can transfer zero-shot or few-shot to novel environments like our kitchen environment, we expect ... | p. 17 (A.2 Inner Monologue for Real-World Tabletop Rearrangement) |

## Dataset / Benchmark Role

- **p. 16 / A.2 Inner Monologue for Real-World Tabletop Rearrangement - extractive body cue:** For the object sorting task, the scene description contains a list of currently visible objects and a list of objects that the robot has successfully ...
- **p. 17 / A.2 Inner Monologue for Real-World Tabletop Rearrangement - extractive body cue:** A.3 Inner Monologue for Real-World Mobile Manipulation in a Kitchen Setting Large Language Model We use PALM [8], a 540B parameter language model trained on ...
- **p. 17 / A.2 Inner Monologue for Real-World Tabletop Rearrangement - extractive body cue:** Environment Feedback: Object Recognition We use human-provided object recognition to provide feedback about the presence of objects visible to the robot camera.
- **p. 15 / A.1 Inner Monologue for Simulated Tabletop Rearrangement - extractive body cue:** Environment Feedback: Passive Scene Description For Object + Scene method, we provide task-progress scene description as a list of achieved sub-goals after each pick-and-place execution.
- **p. 15 / A.1 Inner Monologue for Simulated Tabletop Rearrangement - extractive body cue:** Environment Feedback: Object Recognition We provide the list of objects present in the scene at the start of each episode for the language model (without ...
- **p. 16 / A.2 Inner Monologue for Real-World Tabletop Rearrangement - extractive body cue:** Environment Feedback: Object Recognition For the block stacking task, the scene description contains a list of currently visible objects and a list of previously visible ...
- **p. 18 / A.2 Inner Monologue for Real-World Tabletop Rearrangement - extractive body cue:** Environment Feedback: Active Scene Description We perform a case study where we allow the LLM agent to ask questions and source Human feedback directly.
- **p. 18 / A.2 Inner Monologue for Real-World Tabletop Rearrangement - extractive body cue:** (a) Foresight success detector (b) Hindsight success detector Figure 7: Success Detection architecture used for the Kitchen Environment.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: Inner Monologue enables grounded closed-loop feedback for robot planning with large language models by leveraging a collection of perception models (e.g., scene descriptors ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: Various types of textual feedback. Success Detection gives task-specific task completion information, Passive Scene Description gives structured semantic scene information at every planning ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3: Different instantiations of Inner Monologue in three distinct domains - simulated tabletop rearrangement (top), real-world tabletop rearrangement (middle), and real-world kitchen mobile manipulation ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1: Success rates for various methods, averaged across 50 episodes in Ravens-based environment with test-time disturbances. CLIPort + oracle indicates that CLIPort was provided ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 2: Inner Monologue (with object recognition and success detection feedback) on a real pick and place robot exceeds the performance of baseline alternatives, as ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 3: Averaged success rate across 120 evaluations on several task families in our real-world mobile manipulation environment. We consider a standard setting and adversarial ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4: Failure causes on 120 evaluations. When disturbances are added (red), only the Inner Mono- logue variants consistently complete the instructions. Analysis. The results ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5: Informing LLM with embodied feedback enables many emergent capabilities, all of which are achieved without similar prompted examples. For instance, Inner Monologue can ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | For the object sorting task, the scene description contains a list of currently visible objects and a list of objects that the robot has ... | embodiment, simulator version and control stack | p. 16 (A.2 Inner Monologue for Real-World Tabletop Rearrangement), p. 17 (A.2 Inner Monologue for Real-World Tabletop Rearrangement) |
| Task/environment | A.3 Inner Monologue for Real-World Mobile Manipulation in a Kitchen Setting Large Language Model We use PALM [8], a 540B parameter language model trained ... | reset, timeout, object/scene variation | p. 17 (A.2 Inner Monologue for Real-World Tabletop Rearrangement), p. 17 (A.2 Inner Monologue for Real-World Tabletop Rearrangement) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 2 (1 Introduction), p. 15 (A.1 Inner Monologue for Simulated Tabletop Rearrangement) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 17 (A.2 Inner Monologue for Real-World Tabletop Rearrangement), p. 16 (A.2 Inner Monologue for Real-World Tabletop Rearrangement) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Table 2: Inner Monologue (with object recognition and success detection feedback) on a real pick and place robot exceeds the performance of baseline alternatives, ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| Table 1: Success rates for various methods, averaged across 50 episodes in Ravens-based environment with test-time disturbances. CLIPort + oracle indicates that CLIPort was ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| Table 3: Averaged success rate across 120 evaluations on several task families in our real-world mobile manipulation environment. We consider a standard setting and ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Table 5. As for failure modes, Inner Monologue may fail due to several sources of errors: (1) success detections, (2) LLM planning errors, and ... | definition/direction/unit from same section | p. 9 (Figure/Table caption) |
| ViLD MDETR Precision 85.7% 39.6% Recall 72.0% 87.5% Accuracy 88.9% 68.2% Table 5: Comparison of ViLD [77] and MDETR [92], two open-vocabulary object detection ... | definition/direction/unit from same section | p. 17 (A.2 Inner Monologue for Real-World Tabletop Rearrangement) |
| Figure 2: Various types of textual feedback. Success Detection gives task-specific task completion information, Passive Scene Description gives structured semantic scene information at every ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| ViLD has strong overall accuracy, but still fails to detect objects 28.0% of the time. | definition/direction/unit from same section | p. 17 (A.2 Inner Monologue for Real-World Tabletop Rearrangement) |
| Figure 5: Informing LLM with embodied feedback enables many emergent capabilities, all of which are achieved without similar prompted examples. For instance, Inner Monologue ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Table 2: Inner Monologue (with object recognition and success detection feedback) on a real pick and place robot exceeds the performance of baseline alternatives, ... | comparison identity and matched condition | p. 6 (Figure/Table caption) |
| Table 1: Success rates for various methods, averaged across 50 episodes in Ravens-based environment with test-time disturbances. CLIPort + oracle indicates that CLIPort was ... | comparison identity and matched condition | p. 6 (Figure/Table caption) |
| Figure 4: Failure causes on 120 evaluations. When disturbances are added (red), only the Inner Mono- logue variants consistently complete the instructions. Analysis. The ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| Figure 5: Informing LLM with embodied feedback enables many emergent capabilities, all of which are achieved without similar prompted examples. For instance, Inner Monologue ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| Environment Feedback: Object Recognition We provide the list of objects present in the scene at the start of each episode for the language model ... | comparison identity and matched condition | p. 15 (A.1 Inner Monologue for Simulated Tabletop Rearrangement) |
| Table 4: Comparison between different versions of Inner Monologue implemented in three different environments. A.1 Inner Monologue for Simulated Tabletop Rearrangement Large Language Model ... | comparison identity and matched condition | p. 15 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 1: Success rates for various methods, averaged across 50 episodes in Ravens-based environment with test-time disturbances. CLIPort + oracle indicates that CLIPort was ... | component/input/data sensitivity | p. 6 (Figure/Table caption) |
| Figure 4: Failure causes on 120 evaluations. When disturbances are added (red), only the Inner Mono- logue variants consistently complete the instructions. Analysis. The ... | component/input/data sensitivity | p. 7 (Figure/Table caption) |
| Figure 5: Informing LLM with embodied feedback enables many emergent capabilities, all of which are achieved without similar prompted examples. For instance, Inner Monologue ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| We find that two such models, ViLD [77] and MDETR [92], perform worse than humans but still quite resonably at providing Object feedback, even ... | component/input/data sensitivity | p. 17 (A.2 Inner Monologue for Real-World Tabletop Rearrangement) |
| Table 2: Inner Monologue (with object recognition and success detection feedback) on a real pick and place robot exceeds the performance of baseline alternatives, ... | component/input/data sensitivity | p. 6 (Figure/Table caption) |
| Environment Feedback: Object Recognition We provide the list of objects present in the scene at the start of each episode for the language model ... | component/input/data sensitivity | p. 15 (A.1 Inner Monologue for Simulated Tabletop Rearrangement) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Inspired by the human thought process, we propose that such an inner monologue is a natural framework for incorporating feedback for LLMs. | Table 2: Inner Monologue (with object recognition and success detection feedback) on a real pick and place robot exceeds the performance of baseline alternatives, ... | PDF body cue; verify exact table/figure and matched conditions | p. 6 (Figure/Table caption), p. 7 (Figure/Table caption), p. 6 (Figure/Table caption), p. 8 (Figure/Table caption), p. 17 (A.2 Inner Monologue for Real-World Tabletop Rearrangement), p. 18 (A.2 Inner Monologue for Real-World Tabletop Rearrangement) |
| Primary metric/result | Figure 4: Failure causes on 120 evaluations. When disturbances are added (red), only the Inner Mono- logue variants consistently complete the instructions. Analysis. The ... | numeric claim only at cited anchor | p. 7 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 17 / A.2 Inner Monologue for Real-World Tabletop Rearrangement - extractive body cue:** The learned manipulation policies responsible for counter picking, drawer opening and closing, drawer picking, and countertop object manipulation are Behavior Cloning (BC) policies trained on ...
- **p. 17 / A.2 Inner Monologue for Real-World Tabletop Rearrangement - extractive body cue:** The learned manipulation policies responsible for counter picking, drawer opening and closing, drawer picking, and countertop object manipulation are Behavior Cloning (BC) policies trained on ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Table 5. As for failure modes, Inner Monologue may fail due to several sources of errors: (1) success detections, (2) LLM planning errors, and ... | p. 9 (Figure/Table caption) |
| body limitation/failure cue | Table 3: Averaged success rate across 120 evaluations on several task families in our real-world mobile manipulation environment. We consider a standard setting and ... | p. 7 (Figure/Table caption) |
| body limitation/failure cue | Table 1: Success rates for various methods, averaged across 50 episodes in Ravens-based environment with test-time disturbances. CLIPort + oracle indicates that CLIPort was ... | p. 6 (Figure/Table caption) |
| body limitation/failure cue | Figure 4: Failure causes on 120 evaluations. When disturbances are added (red), only the Inner Mono- logue variants consistently complete the instructions. Analysis. The ... | p. 7 (Figure/Table caption) |
| body limitation/failure cue | Table 2: Inner Monologue (with object recognition and success detection feedback) on a real pick and place robot exceeds the performance of baseline alternatives, ... | p. 6 (Figure/Table caption) |
| body limitation/failure cue | Figure 5: Informing LLM with embodied feedback enables many emergent capabilities, all of which are achieved without similar prompted examples. For instance, Inner Monologue ... | p. 8 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| At inference time, similar to the CLIP 17 | p. 17 (A.2 Inner Monologue for Real-World Tabletop Rearrangement) |
| At inference time within Inner Monologue, we output the text "[success: no]" when the probability is below a certain threshold. | p. 17 (A.2 Inner Monologue for Real-World Tabletop Rearrangement) |
| At inference time, the model is used infer among the possible instructions which one was achieved. | p. 18 (A.2 Inner Monologue for Real-World Tabletop Rearrangement) |
| We study three different implementations of Inner Monologue for each of the experimental settings. | p. 15 (A Inner Monologue Implementation Details) |
| Object Recognition Implementation Object detection is done by MDETR [92], an open-vocabulary object detection model. | p. 16 (A.2 Inner Monologue for Real-World Tabletop Rearrangement) |
| If the probability is above, then we run the hindsight model and only predict success if the argmax across all skills is indeed the ... | p. 18 (A.2 Inner Monologue for Real-World Tabletop Rearrangement) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 9 / Figure/Table caption - extractive body cue:** Table 5. As for failure modes, Inner Monologue may fail due to several sources of errors: (1) success detections, (2) LLM planning errors, and (3) ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 3: Averaged success rate across 120 evaluations on several task families in our real-world mobile manipulation environment. We consider a standard setting and adversarial ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1: Success rates for various methods, averaged across 50 episodes in Ravens-based environment with test-time disturbances. CLIPort + oracle indicates that CLIPort was provided ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4: Failure causes on 120 evaluations. When disturbances are added (red), only the Inner Mono- logue variants consistently complete the instructions. Analysis. The results ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 2: Inner Monologue (with object recognition and success detection feedback) on a real pick and place robot exceeds the performance of baseline alternatives, as ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5: Informing LLM with embodied feedback enables many emergent capabilities, all of which are achieved without similar prompted examples. For instance, Inner Monologue can ...

- **Evidence anchors reviewed:** datasets p. 16 (A.2 Inner Monologue for Real-World Tabletop Rearrangement), p. 17 (A.2 Inner Monologue for Real-World Tabletop Rearrangement), p. 17 (A.2 Inner Monologue for Real-World Tabletop Rearrangement), p. 15 (A.1 Inner Monologue for Simulated Tabletop Rearrangement), p. 15 (A.1 Inner Monologue for Simulated Tabletop Rearrangement), p. 16 (A.2 Inner Monologue for Real-World Tabletop Rearrangement), metrics p. 6 (Figure/Table caption), p. 6 (Figure/Table caption), p. 7 (Figure/Table caption), p. 9 (Figure/Table caption), p. 17 (A.2 Inner Monologue for Real-World Tabletop Rearrangement), p. 4 (Figure/Table caption), baselines p. 6 (Figure/Table caption), p. 6 (Figure/Table caption), p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 15 (A.1 Inner Monologue for Simulated Tabletop Rearrangement), p. 15 (Figure/Table caption), results p. 6 (Figure/Table caption), p. 7 (Figure/Table caption), p. 6 (Figure/Table caption), p. 8 (Figure/Table caption), p. 17 (A.2 Inner Monologue for Real-World Tabletop Rearrangement), p. 18 (A.2 Inner Monologue for Real-World Tabletop Rearrangement).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (25 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Figure 4: Failure causes on 120 evaluations. When disturbances are added (red), only the Inner Mono- logue variants consistently complete the instructions. Analysis. The results of real robot experiments are ... (p. 7, Figure/Table caption).
- **Metric evidence:** Table 1: Success rates for various methods, averaged across 50 episodes in Ravens-based environment with test-time disturbances. CLIPort + oracle indicates that CLIPort was provided a "termination" oracle. Although CLIPort ... (p. 6, Figure/Table caption).
- **Baseline/ablation evidence:** Table 2: Inner Monologue (with object recognition and success detection feedback) on a real pick and place robot exceeds the performance of baseline alternatives, as measured by average task success ... (p. 6, Figure/Table caption).
- **Failure/negative evidence:** Notably, we show that it can efficiently retry under observed stochastic failure, replan under systematic infeasibility, or request human feedback for ambiguous queries, resulting in significantly improved performance in dynamical ... (p. 2, 1 Introduction).
