# Evaluation - UP-VLA: A Unified Understanding and Prediction Model for Embodied Agent

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=V7JPraxi5j; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/168156. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (5.2. Simulation Evaluation), p. 6 (5.2. Simulation Evaluation), p. 7 (5.2. Simulation Evaluation), p. 7 (5.3. Real Robot Evaluation), p. 2 (Figure/Table caption), p. 8 (Figure/Table caption)): Compared to UPVLA-RT-2, which uses only action learning and achieves a completion length of 1.44, UP-VLA with visual prediction significantly improves the length to 4.08.

## Evaluation Body Digest

- **p. 7 / 5.3. Real Robot Evaluation - extractive body cue:** For real-world experimental results, we train RT-1 (Brohan et al., 2022), Diffusion Policy (Chi et al., 2023) on our datasets (using the open-source code and ...
- **p. 6 / 5. Experiments - extractive body cue:** In this section, we evaluate UP-VLA in two domains including the simulation CALVIN benchmark (Mees et al., 2022) and a real-world panda manipulation environment to ...
- **p. 6 / 5.1. Experiment Setup and baseline - extractive body cue:** Our real-world experiments involve multiple table-top manipulation tasks on the Franka-Emika Panda robot, including picking and placing, routing cables, pressing buttons, and opening drawers.
- **p. 7 / 5.3. Real Robot Evaluation - extractive body cue:** We report the success rate of each task over 20 attempts during real-world roll-out.
- **p. 6 / 5.2. Simulation Evaluation - extractive body cue:** Compared to prediction-based methods, the UP-VLA method demonstrates superior performance.
- **p. 6 / 5.2. Simulation Evaluation - extractive body cue:** This demonstrates that integrating visual prediction can substantially enhance the performance of original VLA methods.
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 2. Comparison between UP-VLA, VLM-based VLA mod- els and prediction-based models. The bottom-right chart illustrates the performance across multiple tasks in both simulated and ...
- **p. 7 / 5.3. Real Robot Evaluation - extractive body cue:** UP-VLA demonstrates significant improvement across all tasks.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 5. Experiments (p. 6); 5.1. Experiment Setup and baseline (p. 6); 5.2. Simulation Evaluation (p. 6); 5.3. Real Robot Evaluation (p. 7); 5.5. Quantitative Results (p. 8).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 5.2. Simulation Evaluation | EMPIRICAL / REAL-ROBOT OR HARDWARE | Compared to UPVLA-RT-2, which uses only action learning and achieves a completion length of 1.44, UP-VLA with visual prediction significantly improves the length to ... | p. 6 (5.2. Simulation Evaluation) |
| 5.2. Simulation Evaluation | EMPIRICAL / REAL-ROBOT OR HARDWARE | Compared to other baselines, which perform significantly worse on ABC→D than on ABCD→D, UP-VLA achieves higher completion lengths in both scenarios, indicating that our ... | p. 6 (5.2. Simulation Evaluation) |
| 5.2. Simulation Evaluation | EMPIRICAL / REAL-ROBOT OR HARDWARE | UP-VLA achieves the best performance, demonstrating that our approach exhibits strong generalization capabilities in simulated environments. | p. 7 (5.2. Simulation Evaluation) |
| 5.3. Real Robot Evaluation | EMPIRICAL / REAL-ROBOT OR HARDWARE | We report the success rate of each task over 20 attempts during real-world roll-out. | p. 7 (5.3. Real Robot Evaluation) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 2. Comparison between UP-VLA, VLM-based VLA mod- els and prediction-based models. The bottom-right chart illustrates the performance across multiple tasks in both simulated ... | p. 2 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 7 / 5.3. Real Robot Evaluation - extractive body cue:** For real-world experimental results, we train RT-1 (Brohan et al., 2022), Diffusion Policy (Chi et al., 2023) on our datasets (using the open-source code and ...
- **p. 6 / 5. Experiments - extractive body cue:** In this section, we evaluate UP-VLA in two domains including the simulation CALVIN benchmark (Mees et al., 2022) and a real-world panda manipulation environment to ...
- **p. 6 / 5.1. Experiment Setup and baseline - extractive body cue:** Our real-world experiments involve multiple table-top manipulation tasks on the Franka-Emika Panda robot, including picking and placing, routing cables, pressing buttons, and opening drawers.
- **p. 7 / 5.3. Real Robot Evaluation - extractive body cue:** We report the success rate of each task over 20 attempts during real-world roll-out.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. UP-VLA is pre-trained with both multi-modal under- standing objective and future prediction objective to better capture both high-level semantic information and low-level spatial ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 2. Comparison between UP-VLA, VLM-based VLA mod- els and prediction-based models. The bottom-right chart illustrates the performance across multiple tasks in both simulated and ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3. Overview of UP-VLA. Our model unifies visual-language understanding, future image generation, and action learning in an autoregressive manner. It takes the current visual ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 4. Illustration of the unified prompting and attention mechanism. We use special tokens to segment input sequences and identify task types. For MMU tasks, ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 5. Visualization of our evaluation environments. The left is Calvin (Mees et al., 2022) in which we test on both ABC→D and ABCD→D settings. ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1. Zero-shot long-horizon evaluation on the Calvin benchmark where agent is asked to complete five chained tasks sequentially. Results marked with an asterisk (*) ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2. Zero-shot long-horizon evaluation on the Calvin ABCD→D benchmark. Results of baselines are copied from original papers. image comprehension in the language prompts during ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5. UP-VLA-RT-2 outperforms UP-VLA-phi-w/o- mmu, suggesting that multi-modal understanding aids se- mantic generalization ability. UP-VLA demonstrates better visual-semantic generalization for these tasks, proving that ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | For real-world experimental results, we train RT-1 (Brohan et al., 2022), Diffusion Policy (Chi et al., 2023) on our datasets (using the open-source code ... | embodiment, simulator version and control stack | p. 7 (5.3. Real Robot Evaluation), p. 6 (5. Experiments) |
| Task/environment | In this section, we evaluate UP-VLA in two domains including the simulation CALVIN benchmark (Mees et al., 2022) and a real-world panda manipulation environment ... | reset, timeout, object/scene variation | p. 6 (5. Experiments), p. 6 (5.1. Experiment Setup and baseline) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 4 (4.2. Bridging Visual Prediction and Multi-modal), p. 4 (4.2. Bridging Visual Prediction and Multi-modal) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 3 (3. Preliminaries), p. 3 (4.2. Bridging Visual Prediction and Multi-modal) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We report the success rate of each task over 20 attempts during real-world roll-out. | definition/direction/unit from same section | p. 7 (5.3. Real Robot Evaluation) |
| Compared to prediction-based methods, the UP-VLA method demonstrates superior performance. | definition/direction/unit from same section | p. 6 (5.2. Simulation Evaluation) |
| This demonstrates that integrating visual prediction can substantially enhance the performance of original VLA methods. | definition/direction/unit from same section | p. 6 (5.2. Simulation Evaluation) |
| Figure 2. Comparison between UP-VLA, VLM-based VLA mod- els and prediction-based models. The bottom-right chart illustrates the performance across multiple tasks in both simulated ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |
| UP-VLA demonstrates significant improvement across all tasks. | definition/direction/unit from same section | p. 7 (5.3. Real Robot Evaluation) |
| Table 3. Ablating components of UP-VLA. and UP-VLA-w/o-MMU-Condition, which omits the mech- anism described in sec 4.3 that extends visual prediction prompts using MMU. ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Compared to other baselines, which perform significantly worse on ABC→D than on ABCD→D, UP-VLA achieves higher completion lengths in both scenarios, indicating that our ... | comparison identity and matched condition | p. 6 (5.2. Simulation Evaluation) |
| Compared to prediction-based methods, the UP-VLA method demonstrates superior performance. | comparison identity and matched condition | p. 6 (5.2. Simulation Evaluation) |
| As opposed to new objects, UP-VLA-Phi-w/o-mmu excels at precise operations compared to UP-VLA-RT-2. | comparison identity and matched condition | p. 7 (5.3. Real Robot Evaluation) |
| Results of baselines are copied from original papers. image comprehension in the language prompts during output. | comparison identity and matched condition | p. 7 (5.2. Simulation Evaluation) |
| Figure 2. Comparison between UP-VLA, VLM-based VLA mod- els and prediction-based models. The bottom-right chart illustrates the performance across multiple tasks in both simulated ... | comparison identity and matched condition | p. 2 (Figure/Table caption) |
| Table 3. Ablating components of UP-VLA. and UP-VLA-w/o-MMU-Condition, which omits the mech- anism described in sec 4.3 that extends visual prediction prompts using MMU. ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 3. Ablating components of UP-VLA. and UP-VLA-w/o-MMU-Condition, which omits the mech- anism described in sec 4.3 that extends visual prediction prompts using MMU. ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| This suggests that relying solely on vision-language understanding pretraining can be limiting in tasks that emphasize visual generalization. | component/input/data sensitivity | p. 6 (5.2. Simulation Evaluation) |
| This method initializes UP-VLA using a pure LLM, phi1.5 (Li et al., 2023c) and performs pretraining on the Bridge dataset for future prediction and ... | component/input/data sensitivity | p. 6 (5.2. Simulation Evaluation) |
| We compare the full UP-VLA with the following methods: UP-VLA-w/o-MMU, which does not utilize the LLava tuning dataset for multi-modal understanding, UPVLA-w/o-Bridge-Pretrain, which skips ... | component/input/data sensitivity | p. 7 (5.4. Ablation Studies) |
| Figure 7. Visualization of VQA results and predicted future images. Black, K., Nakamoto, M., Atreya, P., Walke, H., Finn, C., Kumar, A., and Levine, ... | component/input/data sensitivity | p. 9 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We introduce a novel training paradigm for VLA models that combines both vision-language understanding and future prediction objectives, enabling the capture of both high-level ... | Compared to UPVLA-RT-2, which uses only action learning and achieves a completion length of 1.44, UP-VLA with visual prediction significantly improves the length to ... | PDF body cue; verify exact table/figure and matched conditions | p. 6 (5.2. Simulation Evaluation), p. 6 (5.2. Simulation Evaluation), p. 7 (5.2. Simulation Evaluation), p. 7 (5.3. Real Robot Evaluation), p. 2 (Figure/Table caption), p. 8 (Figure/Table caption) |
| Primary metric/result | Compared to other baselines, which perform significantly worse on ABC→D than on ABCD→D, UP-VLA achieves higher completion lengths in both scenarios, indicating that our ... | numeric claim only at cited anchor | p. 6 (5.2. Simulation Evaluation) |

- Numeric sentences retained from the body:
- no numeric body cue

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Our method addresses this limitation by incorporating visual prediction into the original VLA framework. | p. 6 (5.2. Simulation Evaluation) |
| body limitation/failure cue | Unlike UP-VLA, UP-VLA-phi-w/o-mmu does not include multi-modal understanding training, nor does it incorporate 6 | p. 6 (5.2. Simulation Evaluation) |
| body limitation/failure cue | We compare the full UP-VLA with the following methods: UP-VLA-w/o-MMU, which does not utilize the LLava tuning dataset for multi-modal understanding, UPVLA-w/o-Bridge-Pretrain, which skips ... | p. 7 (5.4. Ablation Studies) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| For real-world experimental results, we train RT-1 (Brohan et al., 2022), Diffusion Policy (Chi et al., 2023) on our datasets (using the open-source code ... | p. 7 (5.3. Real Robot Evaluation) |
| During training, we fully fine-tune the parameters of the LLM and freeze all encoders. | p. 4 (4.4. Training Strategy) |
| All baselines in our experiment are listed as below: • RT-1 (Brohan et al., 2022): a small robot action transformer using pretrained Efficient-Net (Tan ... | p. 6 (5.1. Experiment Setup and baseline) |
| For image prediction tasks, we encode the currently observed image into discrete tokens using VQ-GAN (Esser et al., 2021). | p. 3 (4.1. Backbone) |
| These two types of tasks can be encoded into a unified format so they can be mixed and processed in parallel through the LLM ... | p. 3 (4.2. Bridging Visual Prediction and Multi-modal) |
| The observation O′ t, after processing through the continuous vision encoder E1 = MLP(V IT), is mapped into the language embedding space E1(O′ t) ... | p. 4 (4.3. Enhancing Action Learning with Joint Prediction) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / 5.2. Simulation Evaluation - extractive body cue:** Our method addresses this limitation by incorporating visual prediction into the original VLA framework.
- **p. 6 / 5.2. Simulation Evaluation - extractive body cue:** Unlike UP-VLA, UP-VLA-phi-w/o-mmu does not include multi-modal understanding training, nor does it incorporate 6
- **p. 7 / 5.4. Ablation Studies - extractive body cue:** We compare the full UP-VLA with the following methods: UP-VLA-w/o-MMU, which does not utilize the LLava tuning dataset for multi-modal understanding, UPVLA-w/o-Bridge-Pretrain, which skips visual ...

- **Evidence anchors reviewed:** datasets p. 7 (5.3. Real Robot Evaluation), p. 6 (5. Experiments), p. 6 (5.1. Experiment Setup and baseline), p. 7 (5.3. Real Robot Evaluation), metrics p. 7 (5.3. Real Robot Evaluation), p. 6 (5.2. Simulation Evaluation), p. 6 (5.2. Simulation Evaluation), p. 2 (Figure/Table caption), p. 7 (5.3. Real Robot Evaluation), p. 8 (Figure/Table caption), baselines p. 6 (5.2. Simulation Evaluation), p. 6 (5.2. Simulation Evaluation), p. 7 (5.3. Real Robot Evaluation), p. 7 (5.2. Simulation Evaluation), p. 2 (Figure/Table caption), p. 8 (Figure/Table caption), results p. 6 (5.2. Simulation Evaluation), p. 6 (5.2. Simulation Evaluation), p. 7 (5.2. Simulation Evaluation), p. 7 (5.3. Real Robot Evaluation), p. 2 (Figure/Table caption), p. 8 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
