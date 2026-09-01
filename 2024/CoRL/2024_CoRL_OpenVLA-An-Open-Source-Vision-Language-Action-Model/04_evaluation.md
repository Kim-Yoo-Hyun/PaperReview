# Evaluation - OpenVLA: An Open-Source Vision-Language-Action Model

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (35 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v270/kim25c.html; PDF retrieval source: https://raw.githubusercontent.com/mlresearch/v270/main/assets/kim25c/kim25c.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (Figure/Table caption), p. 25 (Figure/Table caption), p. 7 (4 Experiments), p. 29 (Figure/Table caption), p. 35 (Figure/Table caption), p. 23 (Figure/Table caption)): Figure 3: Bridge V2 WidowX evaluation task categories and results. We evaluate OpenVLA and prior state-of- the-art generalist robot policies on a comprehensive suite of tasks covering several axes of ...

## Evaluation Body Digest

- **p. 7 / 4 Experiments - extractive body cue:** Qualitatively, both RT-2-X and OpenVLA exhibit markedly more robust behaviors than the other tested models, such as approaching the correct object when distractor objects are ...
- **p. 7 / 4 Experiments - extractive body cue:** We test OpenVLA in two setups: Franka-Tabletop, a stationary, table-mounted Franka Emika Panda 7-DoF robot arm; and Franka-DROID, the Franka setup from the DROID dataset ...
- **p. 8 / 7.0 GB - extractive body cue:** 2In Section 4.3, we experiment with a version of the OpenVLA model that is pretrained with a smaller robot data mixture (the same OpenX dataset ...
- **p. 6 / 4 Experiments - extractive body cue:** We define a comprehensive set of evaluation tasks in each environment that covers various axes of generalization, such as visual (unseen backgrounds, distractor objects, colors/appearances ...
- **p. 5 / 4 Experiments - extractive body cue:** (2) Can OpenVLA be effectively fine-tuned on a new robot setup and task, and how does it compare to state-of-the-art data-efficient imitation learning approaches?
- **p. 5 / 4 Experiments - extractive body cue:** The goal of our experimental evaluations is to test OpenVLA's ability to serve as a powerful multirobot control policy out of the box, as well ...
- **p. 6 / 4 Experiments - extractive body cue:** 4.1 Direct Evaluations on Multiple Robot Platforms Robot Setups and Tasks.
- **p. 8 / 7.0 GB - extractive body cue:** We also demonstrated that OpenVLA can be easily adapted to new robot setups via parameter-efficient fine-tuning techniques.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SIMULATION`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 4 Experiments (p. 5); B Evaluation Tasks and Detailed Results (p. 18); B.1 Bridge V2 WidowX Evaluation Details (p. 18); B.1.1 Bridge V2 Evaluation Tasks (p. 18); B.1.3 Detailed Bridge V2 Evaluation Results (p. 23); B.2 Google Robot Evaluation Details (p. 23); B.2.1 Google Robot Evaluation Tasks (p. 23); B.2.2 Detailed Google Robot Evaluation Results (p. 25); B.3 Data-Efficient Adaptation Experiment Details (p. 25); B.3.2 Detailed Franka-Tabletop and Franka-DROID Evaluation Results (p. 28).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / SIMULATION | Figure 3: Bridge V2 WidowX evaluation task categories and results. We evaluate OpenVLA and prior state-of- the-art generalist robot policies on a comprehensive suite ... | p. 6 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / SIMULATION | Table 6: Detailed Google robot evaluation results. We report full evaluation results for Google robot evaluations discussed in Section 4.1. Each generalist policy is ... | p. 25 (Figure/Table caption) |
| 4 Experiments | EMPIRICAL / SIMULATION | Notably, prior works achieve strong performance only in either precise or diverse tasks, resulting in widely varying success rates. | p. 7 (4 Experiments) |
| Figure/Table caption | EMPIRICAL / SIMULATION | Table 7: Detailed data-efficient adaptation experiment results. We report the performance of Diffusion Policy trained from scratch on new robot tasks, as well as ... | p. 29 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / SIMULATION | Table 12: LIBERO simulation benchmark results. We report the success rate (SR) and standard error of each method for the four task suites in ... | p. 35 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 7 / 4 Experiments - extractive body cue:** Qualitatively, both RT-2-X and OpenVLA exhibit markedly more robust behaviors than the other tested models, such as approaching the correct object when distractor objects are ...
- **p. 7 / 4 Experiments - extractive body cue:** We test OpenVLA in two setups: Franka-Tabletop, a stationary, table-mounted Franka Emika Panda 7-DoF robot arm; and Franka-DROID, the Franka setup from the DROID dataset ...
- **p. 8 / 7.0 GB - extractive body cue:** 2In Section 4.3, we experiment with a version of the OpenVLA model that is pretrained with a smaller robot data mixture (the same OpenX dataset ...
- **p. 6 / 4 Experiments - extractive body cue:** We define a comprehensive set of evaluation tasks in each environment that covers various axes of generalization, such as visual (unseen backgrounds, distractor objects, colors/appearances ...
- **p. 5 / 4 Experiments - extractive body cue:** (2) Can OpenVLA be effectively fine-tuned on a new robot setup and task, and how does it compare to state-of-the-art data-efficient imitation learning approaches?
- **p. 5 / 4 Experiments - extractive body cue:** The goal of our experimental evaluations is to test OpenVLA's ability to serve as a powerful multirobot control policy out of the box, as well ...
- **p. 6 / 4 Experiments - extractive body cue:** 4.1 Direct Evaluations on Multiple Robot Platforms Robot Setups and Tasks.
- **p. 8 / 7.0 GB - extractive body cue:** We also demonstrated that OpenVLA can be easily adapted to new robot setups via parameter-efficient fine-tuning techniques.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: We present OpenVLA, a 7B-parameter open-source vision-language-action model (VLA), trained on 970k robot episodes from the Open X-Embodiment dataset [1]. OpenVLA sets a ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: OpenVLA model architecture. Given an image observation and a language instruction, the model predicts 7-dimensional robot control actions. The architecture consists of three ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3: Bridge V2 WidowX evaluation task categories and results. We evaluate OpenVLA and prior state-of- the-art generalist robot policies on a comprehensive suite of ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4: Google robot evaluation results. We evaluate generalist robot policies on in-distribution and out-of- distribution (OOD) tasks on the mobile manipulator used in RT-1 ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5: Fine-tuning to new robot setups. We fine-tune OpenVLA on 10-100 demonstrations across 7 Franka Emika Panda tasks, ranging from single-instruction tasks to diverse ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 1: Parameter-Efficient Fine-Tuning Evaluation. LoRA fine-tuning achieves the best performance-compute trade-off, matching full fine-tuning performance while training only 1.4% of the parameters. Mean success ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 2: Performance with quantized in- ference. 4-bit quantization matches the per- formance of bfloat16 inference (our default approach) while reducing the GPU memory footprint ...
- **p. 18 / Figure/Table caption - extractive body cue:** Table 3: OpenVLA training data mixture using datasets from the Open X-Embodiment dataset [1], following [5] with a few additions. B Evaluation Tasks and Detailed ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Qualitatively, both RT-2-X and OpenVLA exhibit markedly more robust behaviors than the other tested models, such as approaching the correct object when distractor objects ... | embodiment, simulator version and control stack | p. 7 (4 Experiments), p. 7 (4 Experiments) |
| Task/environment | We test OpenVLA in two setups: Franka-Tabletop, a stationary, table-mounted Franka Emika Panda 7-DoF robot arm; and Franka-DROID, the Franka setup from the DROID ... | reset, timeout, object/scene variation | p. 7 (4 Experiments), p. 8 (7.0 GB) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | 본문 anchor 없음 |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Table 11: Quantized inference experiment results with blocking control. We report the success rate and standard error of OpenVLA on various BridgeData V2 WidowX ... | definition/direction/unit from same section | p. 33 (Figure/Table caption) |
| Table 6: Detailed Google robot evaluation results. We report full evaluation results for Google robot evaluations discussed in Section 4.1. Each generalist policy is ... | definition/direction/unit from same section | p. 25 (Figure/Table caption) |
| Table 12: LIBERO simulation benchmark results. We report the success rate (SR) and standard error of each method for the four task suites in ... | definition/direction/unit from same section | p. 35 (Figure/Table caption) |
| Notably, prior works achieve strong performance only in either precise or diverse tasks, resulting in widely varying success rates. | definition/direction/unit from same section | p. 7 (4 Experiments) |
| Average success rates ± StdErr are computed across 170 total rollouts per approach. fine-tuning and quantization to reduce the computational requirements for training and ... | definition/direction/unit from same section | p. 6 (4 Experiments) |
| 4.3 Efficient OpenVLA Fine-Tuning and Inference Strategy Success Rate Train Params (×106) VRAM (batch 16) Full FT 69.7 ± 7.2 % 7,188.1 | definition/direction/unit from same section | p. 8 (4 Experiments) |
| Mean success rate ± StdErr computed across 8 representative Bridge V2 tasks [6] and 80 rollouts per approach (see Table 5 for details). | definition/direction/unit from same section | p. 8 (7.0 GB) |
| Table 7: Detailed data-efficient adaptation experiment results. We report the performance of Diffusion Policy trained from scratch on new robot tasks, as well as ... | definition/direction/unit from same section | p. 29 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| (2) Can OpenVLA be effectively fine-tuned on a new robot setup and task, and how does it compare to state-of-the-art data-efficient imitation learning approaches? | comparison identity and matched condition | p. 5 (4 Experiments) |
| We find that OpenVLA and RT-2-X attain comparable performance and significantly outperform RT-1-X and Octo overall. | comparison identity and matched condition | p. 6 (4 Experiments) |
| RT-2-X clearly outperforms both RT-1-X and Octo, demonstrating the benefits of large, pretrained VLMs for robotics. | comparison identity and matched condition | p. 6 (4 Experiments) |
| We compare to Diffusion Policy [3], a state-of-the-art data-efficient imitation learning approach, trained from scratch. | comparison identity and matched condition | p. 7 (4 Experiments) |
| It clearly outperforms Octo while being trained on the same robot data, attesting to the benefits of Internet-scale pretraining. | comparison identity and matched condition | p. 7 (4 Experiments) |
| 5 Conclusion and Limitations In this work, we presented OpenVLA, a state-of-the-art, open-source vision-language-action model that obtains strong performance for cross-embodiment robot control out-of-the-box. | comparison identity and matched condition | p. 8 (7.0 GB) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 9: BridgeData V2 WidowX ablation experiment results. We evaluate various methods on a subset of 8 representative tasks to assess the importance of ... | component/input/data sensitivity | p. 31 (Figure/Table caption) |
| Finally, as an ablation, we compare to OpenVLA (scratch), which omits OpenX pretraining and directly fine-tunes our base Prismatic VLM on the target robot ... | component/input/data sensitivity | p. 7 (4 Experiments) |
| See Appendix F for ablation analyses of these components. | component/input/data sensitivity | p. 7 (4 Experiments) |
| (2) Can OpenVLA be effectively fine-tuned on a new robot setup and task, and how does it compare to state-of-the-art data-efficient imitation learning approaches? | component/input/data sensitivity | p. 5 (4 Experiments) |
| We test various parameter-efficient fine-tuning approaches for OpenVLA2 across multiple FrankaTabletop tasks in Table 1: last layer only fine-tunes only the last layer of ... | component/input/data sensitivity | p. 8 (7.0 GB) |
| Figure 11: OpenVLA inference speed for various GPUs. Both bfloat16 and int4 quantization achieve high throughput, especially on GPUs with Ada Lovelace architecture (RTX ... | component/input/data sensitivity | p. 30 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To this end, we introduce OpenVLA, a 7B-parameter open-source VLA that establishes a new state of the art for generalist robot manipulation policies. | Figure 3: Bridge V2 WidowX evaluation task categories and results. We evaluate OpenVLA and prior state-of- the-art generalist robot policies on a comprehensive suite ... | PDF body cue; verify exact table/figure and matched conditions | p. 6 (Figure/Table caption), p. 25 (Figure/Table caption), p. 7 (4 Experiments), p. 29 (Figure/Table caption), p. 35 (Figure/Table caption), p. 23 (Figure/Table caption) |
| Primary metric/result | Table 6: Detailed Google robot evaluation results. We report full evaluation results for Google robot evaluations discussed in Section 4.1. Each generalist policy is ... | numeric claim only at cited anchor | p. 25 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 6 / 4 Experiments - extractive body cue:** Notably, OpenVLA performs comparably to RT-2-X on Google robot evaluations and significantly outperforms RT-2-X on Bridge V2 evaluations despite being 7x smaller (7B vs.
- **p. 7 / 4 Experiments - extractive body cue:** Mean success ± StdErr computed across 99 and 30 rollouts per approach for Franka-Tabletop and Franka-DROID, respectively.
- **p. 8 / 4 Experiments - extractive body cue:** 4.3 Efficient OpenVLA Fine-Tuning and Inference Strategy Success Rate Train Params (×106) VRAM (batch 16) Full FT 69.7 ± 7.2 % 7,188.1
- **p. 8 / 60.5 GB - extractive body cue:** Mean success ± StdErr across 33 rollouts per approach on select Franka-Tabletop tasks (see Table 8 for details). ∗: Sharded across 2 GPUs with FSDP ...
- **p. 8 / 60.5 GB - extractive body cue:** Precision Bridge Success VRAM bfloat16 71.3 ± 4.8%
- **p. 8 / 7.0 GB - extractive body cue:** Mean success rate ± StdErr computed across 8 representative Bridge V2 tasks [6] and 80 rollouts per approach (see Table 5 for details).

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | The current OpenVLA model has several limitations. | p. 8 (7.0 GB) |
| body limitation/failure cue | 5 Conclusion and Limitations In this work, we presented OpenVLA, a state-of-the-art, open-source vision-language-action model that obtains strong performance for cross-embodiment robot control out-of-the-box. | p. 8 (7.0 GB) |
| body limitation/failure cue | Table 10: Fine-tuned vs. frozen vision encoder experiment results. We evaluate the performance of fine-tuning ("Fine-Tuned") vs. freezing the vision encoder ("Frozen Vision") in ... | p. 32 (Figure/Table caption) |
| body limitation/failure cue | Additionally, we evaluate Octo [5] fine-tuned on the target dataset (RT-2-X does not support fine-tuning). | p. 7 (4 Experiments) |
| body limitation/failure cue | We find that both RT-1-X and Octo struggle on the tested tasks, often failing to manipulate the correct object, especially when distractors are present. | p. 6 (4 Experiments) |
| body limitation/failure cue | Franka-Tabletop Franka-DROID 66.7 53.5 33.3 93.3 80.0 0.0 83.3 63.3 26.7 Narrow Single-Instruction Tasks 19.4 27.8 30.6 27.8 22.2 66.7 16.7 25.0 91.7 Diverse ... | p. 7 (4 Experiments) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| 4-bit inference achieves higher throughput due to reduced GPU memory transfer and thus recovers performance of the original bfloat16 model, while requiring less than ... | p. 8 (7.0 GB) |
| Importantly, LoRA matches full fine-tuning performance while fine-tuning only 1.4% of the parameters (r = 32), enabling us to fine-tune OpenVLA on a new ... | p. 8 (7.0 GB) |
| What are the performance-compute trade-offs? | p. 6 (4 Experiments) |
| Average success rates ± StdErr are computed across 170 total rollouts per approach. fine-tuning and quantization to reduce the computational requirements for training and ... | p. 6 (4 Experiments) |
| Mean success ± StdErr computed across 99 and 30 rollouts per approach for Franka-Tabletop and Franka-DROID, respectively. | p. 7 (4 Experiments) |
| 350k for RT-2-X; we performed more careful cleaning of the training dataset and, e.g., filter out all-zero actions in the Bridge dataset (see Appendix ... | p. 7 (4 Experiments) |
| Yet, there are two key reasons preventing the widespread use of existing VLAs: 1) current models [1, 7, 17, 18] are closed, with limited ... | p. 2 (1 Introduction) |
| of compute efficient fine-tuning methods leveraging low-rank adaptation [LoRA; 25] and model quantization [26] to facilitate adapting OpenVLA models on consumer-grade GPUs instead of ... | p. 3 (1 Introduction) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 7.0 GB - extractive body cue:** The current OpenVLA model has several limitations.
- **p. 8 / 7.0 GB - extractive body cue:** 5 Conclusion and Limitations In this work, we presented OpenVLA, a state-of-the-art, open-source vision-language-action model that obtains strong performance for cross-embodiment robot control out-of-the-box.
- **p. 32 / Figure/Table caption - extractive body cue:** Table 10: Fine-tuned vs. frozen vision encoder experiment results. We evaluate the performance of fine-tuning ("Fine-Tuned") vs. freezing the vision encoder ("Frozen Vision") in two ...
- **p. 7 / 4 Experiments - extractive body cue:** Additionally, we evaluate Octo [5] fine-tuned on the target dataset (RT-2-X does not support fine-tuning).
- **p. 6 / 4 Experiments - extractive body cue:** We find that both RT-1-X and Octo struggle on the tested tasks, often failing to manipulate the correct object, especially when distractors are present.
- **p. 7 / 4 Experiments - extractive body cue:** Franka-Tabletop Franka-DROID 66.7 53.5 33.3 93.3 80.0 0.0 83.3 63.3 26.7 Narrow Single-Instruction Tasks 19.4 27.8 30.6 27.8 22.2 66.7 16.7 25.0 91.7 Diverse Multi-Instruction ...

- **PDF anchors reviewed:** datasets p. 7 (4 Experiments), p. 7 (4 Experiments), p. 8 (7.0 GB), p. 6 (4 Experiments), p. 5 (4 Experiments), p. 5 (4 Experiments), metrics p. 33 (Figure/Table caption), p. 25 (Figure/Table caption), p. 35 (Figure/Table caption), p. 7 (4 Experiments), p. 6 (4 Experiments), p. 8 (4 Experiments), baselines p. 5 (4 Experiments), p. 6 (4 Experiments), p. 6 (4 Experiments), p. 7 (4 Experiments), p. 7 (4 Experiments), p. 8 (7.0 GB), results p. 6 (Figure/Table caption), p. 25 (Figure/Table caption), p. 7 (4 Experiments), p. 29 (Figure/Table caption), p. 35 (Figure/Table caption), p. 23 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
