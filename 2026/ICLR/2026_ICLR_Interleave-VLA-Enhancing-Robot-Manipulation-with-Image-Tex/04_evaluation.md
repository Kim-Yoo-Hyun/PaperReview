# Evaluation - Interleave-VLA: Enhancing Robot Manipulation with Image-Text Interleaved Instructions

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (31 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=ULTWUuGhC3; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/245105. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 27 (Figure/Table caption), p. 10 (4 EXPERIMENTS), p. 24 (Figure/Table caption), p. 8 (Figure/Table caption), p. 18 (Figure/Table caption), p. 28 (Figure/Table caption)): Table 13: Detailed evaluation results on 9 Out-of-Domain generalization tasks based on SimplerEnv. Success rates (%) are reported for π0, Interleave-VLA (adapted from π0), and Interleave-VLA co- trained with our ...

## Evaluation Body Digest

- **p. 8 / 4 EXPERIMENTS - extractive body cue:** Notably, although the pretraining dataset does not include FANUC robot arm data, it still enables strong cross-embodiment transfer to FANUC.
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** Unlike the SimplerEnv experiments, where large-scale BridgeData V2 supports strong performance, the real-robot setup relies on a smaller self-collected dataset.
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** 4.2 REAL ROBOT COMPARISON Task setup.
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** The interleaved instruction format naturally accommodates diverse input types, making human-robot interaction more intuitive by removing the need for users to precisely describe complex objectives ...
- **p. 10 / 4 EXPERIMENTS - extractive body cue:** This occurs because many common robot-instruction templates, e.g., "Put object A [near / to the left of / on] object B", become ambiguous when expressed ...
- **p. 10 / 4 EXPERIMENTS - extractive body cue:** Instruction image diversity is crucial as well, Table 5 demonstrates that combining Internet images with task-specific images cropped from robot observations yields the best overall ...
- **p. 6 / 4 EXPERIMENTS - extractive body cue:** Performances are tested on SimplerEnv-Bridge setup, which uses a WidowX robot configuration compatible with the BridgeData V2 (Walke et al., 2023b).
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** We evaluate on a FANUC LRMate 200iD/7L robotic arm equipped with an SMC gripper.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 4 EXPERIMENTS (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 13: Detailed evaluation results on 9 Out-of-Domain generalization tasks based on SimplerEnv. Success rates (%) are reported for π0, Interleave-VLA (adapted from π0), ... | p. 27 (Figure/Table caption) |
| 4 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Move Near Text 69.2 71.4 30.2 21.0 66.6 Visual Goal 67.8 74.6 48.0 51.9 0.0 Interleaved Img-Text 71.3 73.4 53.9 54.2 68.8 paring the ... | p. 10 (4 EXPERIMENTS) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 11: Quantitative hallucination analysis of π0 with text-only instructions (Text-VLA) and interleaved image-text instructions (Interleave-VLA). Across all task categories, Interleave-VLA achieves higher overall ... | p. 24 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 3: Comparison of success rates (Succ) and correct object picking rates (Acc) in real-robot experiments. All the baselines use the base VLA model ... | p. 8 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 8: Performance across sketch styles. Success Rate and Intention Accuracy (in %) of Interleave-VLA when the target object is specified by sketches with ... | p. 18 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 8 / 4 EXPERIMENTS - extractive body cue:** Notably, although the pretraining dataset does not include FANUC robot arm data, it still enables strong cross-embodiment transfer to FANUC.
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** Unlike the SimplerEnv experiments, where large-scale BridgeData V2 supports strong performance, the real-robot setup relies on a smaller self-collected dataset.
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** 4.2 REAL ROBOT COMPARISON Task setup.
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** The interleaved instruction format naturally accommodates diverse input types, making human-robot interaction more intuitive by removing the need for users to precisely describe complex objectives ...
- **p. 10 / 4 EXPERIMENTS - extractive body cue:** This occurs because many common robot-instruction templates, e.g., "Put object A [near / to the left of / on] object B", become ambiguous when expressed ...
- **p. 10 / 4 EXPERIMENTS - extractive body cue:** Instruction image diversity is crucial as well, Table 5 demonstrates that combining Internet images with task-specific images cropped from robot observations yields the best overall ...
- **p. 6 / 4 EXPERIMENTS - extractive body cue:** Performances are tested on SimplerEnv-Bridge setup, which uses a WidowX robot configuration compatible with the BridgeData V2 (Walke et al., 2023b).
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** We evaluate on a FANUC LRMate 200iD/7L robotic arm equipped with an SMC gripper.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: (a) Our Interleaved X-Embodiment Dataset features diverse, high-quality object-centric images automatically generated from real-world robot demonstrations. (b) Interleave-VLA achieves 2× stronger out-of-domain generalization ...
- **p. 4 / Figure/Table caption - extractive body cue:** Table 1: Comparing Interleave-VLA with representative VLA methods. Unlike prior systems that depend on fixed backbones, source external Internet or simulation data, and accept only ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 2: Overview of the Interleave-VLA paradigm, featuring an extendable adaptation of Text- VLA to handle interleaved inputs, scalable training on a constructed large interleaved ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3: Left: Our open interleaved X-Embodiment dataset features a large number of high-quality cropped images with diversity across objects. Right: Interleave dataset generation pipeline: ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4: Left: Illustration of generalization settings in SIMPLER. (a) Visual generalization: unseen environments, tablecloths, and lighting conditions. (b) Semantic generalization with novel objects from ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2: Interleave-VLA and Text-VLA comparison on SimplerEnv. In-Domain includes 4 tasks following SimplerEnv-Bridge setup. We add 3 Out-of-Domain evaluation suites, namely: Visual, Novel Object, ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5: Qualitative analysis of Interleave-VLA's improved performance over the Text-VLA paradigm. In out-of-domain SimplerEnv tasks with unfamiliar objects, Text-VLA displays at- tentional hallucination, which ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 3: Comparison of success rates (Succ) and correct object picking rates (Acc) in real-robot experiments. All the baselines use the base VLA model π0. ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Notably, although the pretraining dataset does not include FANUC robot arm data, it still enables strong cross-embodiment transfer to FANUC. | embodiment, simulator version and control stack | p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS) |
| Task/environment | Unlike the SimplerEnv experiments, where large-scale BridgeData V2 supports strong performance, the real-robot setup relies on a smaller self-collected dataset. | reset, timeout, object/scene variation | p. 8 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 2 (1 INTRODUCTION), p. 1 (Body text (section not recovered)) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 1 (ABSTRACT), p. 2 (1 INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Table 8: Performance across sketch styles. Success Rate and Intention Accuracy (in %) of Interleave-VLA when the target object is specified by sketches with ... | definition/direction/unit from same section | p. 18 (Figure/Table caption) |
| Table 7: Grounding under image-text contradiction. Success Rate and Intention Accuracy (in %) of Interleave-VLA on the color-conditioned block manipulation task under different instruction ... | definition/direction/unit from same section | p. 18 (Figure/Table caption) |
| Figure 11: Quantitative hallucination analysis of π0 with text-only instructions (Text-VLA) and interleaved image-text instructions (Interleave-VLA). Across all task categories, Interleave-VLA achieves higher overall ... | definition/direction/unit from same section | p. 24 (Figure/Table caption) |
| L1 L2 L3 L4 0 20 40 60 80 100 Success Rate (%) VIMA-Bench Interleave-VLA OpenVLA VIMA-Gato VIMA-Flamingo VIMA-GPT Figure 6: VIMA-Bench results across ... | definition/direction/unit from same section | p. 9 (4 EXPERIMENTS) |
| Table 3: Comparison of success rates (Succ) and correct object picking rates (Acc) in real-robot experiments. All the baselines use the base VLA model ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Table 13: Detailed evaluation results on 9 Out-of-Domain generalization tasks based on SimplerEnv. Success rates (%) are reported for π0, Interleave-VLA (adapted from π0), ... | definition/direction/unit from same section | p. 27 (Figure/Table caption) |
| To qualitatively illustrate this, we compute the attention scores of target object tokens relative to the tokenized observation in out-of-domain settings. | definition/direction/unit from same section | p. 7 (4 EXPERIMENTS) |
| Overall, our results underscore the importance of the curated large-scale Interleaved X-Embodiment Dataset (Section 3.3) in fostering robust and generalizable Interleave-VLA. | definition/direction/unit from same section | p. 9 (4 EXPERIMENTS) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| In contrast, Interleave-VLA outperforms Text-VLA baselines by leveraging in-context visual grounding and cross-modality training to reduce attentional hallucinations. | comparison identity and matched condition | p. 7 (4 EXPERIMENTS) |
| To validate this, we extend Interleave-VLA to OpenVLA (Kim et al., 2024), a state-of-the-art VLA model with a distinct architecture and training objective compared ... | comparison identity and matched condition | p. 8 (4 EXPERIMENTS) |
| Table 3: Comparison of success rates (Succ) and correct object picking rates (Acc) in real-robot experiments. All the baselines use the base VLA model ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| Each baseline is finetuned on 20 teleoperated demonstrations per object, collected using a space mouse. | comparison identity and matched condition | p. 7 (4 EXPERIMENTS) |
| InterleaveVLA outperforms Text-VLA by 2× across all difficulty levels, further highlighting its superior generalization capabilities with evidence from new task sets and a different ... | comparison identity and matched condition | p. 9 (4 EXPERIMENTS) |
| Figure 10: Red: QwenVL+SAM and Yellow: Owlv2. Individual error rates are 22.1% and 17.4%, respectively. The combined error rate is reduced to 4.4%. and ... | comparison identity and matched condition | p. 23 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Pretraining on the Interleaved X-Embodiment dataset significantly boosts performance through effective crossembodiment transfer, reducing the need for laborious data collection. | component/input/data sensitivity | p. 8 (4 EXPERIMENTS) |
| Across all four generalization levels, our general Interleave-VLA paradigm, when directly extended to OpenVLA, achieves the best performance without relying on any task-specific designs. | component/input/data sensitivity | p. 8 (4 EXPERIMENTS) |
| Building on its versatile inference interface, Interleave-VLA further showcases an emergent capability to interpret instructions in a completely zero-shot manner, directly handling unseen input ... | component/input/data sensitivity | p. 9 (4 EXPERIMENTS) |
| To isolate the contribution of the visual goal signal, we perform an ablation in the SimplerEnvBridge setting (Table 2). | component/input/data sensitivity | p. 10 (4 EXPERIMENTS) |
| Table 1: Comparing Interleave-VLA with representative VLA methods. Unlike prior systems that depend on fixed backbones, source external Internet or simulation data, and accept ... | component/input/data sensitivity | p. 4 (Figure/Table caption) |
| Table 4: Interleave-VLA unlocks powerful zero-shot generalization to diverse instruction modali- ties, including hand-drawn sketches, user-cropped images, and Internet photos, without ever seeing them ... | component/input/data sensitivity | p. 9 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| As illustrated in Figure 2, Interleave-VLA consists of three key components: (1) a lightweight adaptation module that introduces special separator tokens into the tokenizer, ... | Table 13: Detailed evaluation results on 9 Out-of-Domain generalization tasks based on SimplerEnv. Success rates (%) are reported for π0, Interleave-VLA (adapted from π0), ... | PDF body cue; verify exact table/figure and matched conditions | p. 27 (Figure/Table caption), p. 10 (4 EXPERIMENTS), p. 24 (Figure/Table caption), p. 8 (Figure/Table caption), p. 18 (Figure/Table caption), p. 28 (Figure/Table caption) |
| Primary metric/result | Move Near Text 69.2 71.4 30.2 21.0 66.6 Visual Goal 67.8 74.6 48.0 51.9 0.0 Interleaved Img-Text 71.3 73.4 53.9 54.2 68.8 paring the ... | numeric claim only at cited anchor | p. 10 (4 EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** In-Domain includes 4 tasks following SimplerEnv-Bridge setup.
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** RT-1-X (O'Neill et al., 2024) Text-VLA Text/Text 1.1 ± 0.5 0.0 ± 0.0 3.5 ± 0.4 5.8 ± 0.3 3.2 ± 0.2 Octo (Team et ...
- **p. 10 / 4 EXPERIMENTS - extractive body cue:** Data In-Domain Out-of-Domain Internet Only 59.2 69.1 Task-specific Only 67.5 67.1 Mixed 71.0 71.7 Table 6: Interleaved instructions contribute through both format and content.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 9: Interleave-VLA Inference time w.r.t number of images. When number of images is 1 - 2, it is typically the cost of Text-VLA ... | p. 22 (Figure/Table caption) |
| body limitation/failure cue | (2) What are the common failure modes of Text-VLA, and how does Interleave-VLA address them? | p. 6 (4 EXPERIMENTS) |
| body limitation/failure cue | For quantitative breakdown of failure modes, please refer to Figure 11. | p. 7 (4 EXPERIMENTS) |
| body limitation/failure cue | These failures can be attributed to semantic ambiguity in cluttered visual contexts and distributional bias in the training data. | p. 7 (4 EXPERIMENTS) |
| body limitation/failure cue | For more styles of sketches and potential failure modes, please refer to Table 8 and 9 in Apppendix C. | p. 9 (4 EXPERIMENTS) |
| body limitation/failure cue | Table 9: Example sketches for each style. Yellow-cube and green-cube sketches representing each drawing style. The examples are sourced from multiple individuals and are ... | p. 19 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| To qualitatively illustrate this, we compute the attention scores of target object tokens relative to the tokenized observation in out-of-domain settings. | p. 7 (4 EXPERIMENTS) |
| As illustrated in Figure 2, Interleave-VLA consists of three key components: (1) a lightweight adaptation module that introduces special separator tokens into the tokenizer, ... | p. 2 (1 INTRODUCTION) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 22 / Figure/Table caption - extractive body cue:** Figure 9: Interleave-VLA Inference time w.r.t number of images. When number of images is 1 - 2, it is typically the cost of Text-VLA model. ...
- **p. 6 / 4 EXPERIMENTS - extractive body cue:** (2) What are the common failure modes of Text-VLA, and how does Interleave-VLA address them?
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** For quantitative breakdown of failure modes, please refer to Figure 11.
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** These failures can be attributed to semantic ambiguity in cluttered visual contexts and distributional bias in the training data.
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** For more styles of sketches and potential failure modes, please refer to Table 8 and 9 in Apppendix C.
- **p. 19 / Figure/Table caption - extractive body cue:** Table 9: Example sketches for each style. Yellow-cube and green-cube sketches representing each drawing style. The examples are sourced from multiple individuals and are designed ...

- **Evidence anchors reviewed:** datasets p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS), metrics p. 18 (Figure/Table caption), p. 18 (Figure/Table caption), p. 24 (Figure/Table caption), p. 9 (4 EXPERIMENTS), p. 8 (Figure/Table caption), p. 27 (Figure/Table caption), baselines p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 8 (Figure/Table caption), p. 7 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 23 (Figure/Table caption), results p. 27 (Figure/Table caption), p. 10 (4 EXPERIMENTS), p. 24 (Figure/Table caption), p. 8 (Figure/Table caption), p. 18 (Figure/Table caption), p. 28 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
