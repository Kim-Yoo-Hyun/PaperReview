# Evaluation - AVA-VLA: Improving Vision-Language-Action Models with Active Visual Attention

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Xiao_AVA-VLA_Improving_Vision-Language-Action_models_with_Active_Visual_Attention_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Xiao_AVA-VLA_Improving_Vision-Language-Action_models_with_Active_Visual_Attention_CVPR_2026_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (4.3. Ablation Studies), p. 7 (4.2. Evaluation Results), p. 6 (4.1. Experimental Setup), p. 6 (4.2. Evaluation Results), p. 8 (4.4. Analysis), p. 8 (4.4. Analysis)): Each component alone improves over OpenVLA-OFT, and their combination achieves the best overall performance.

## Evaluation Body Digest

- **p. 5 / 4.1. Experimental Setup - extractive body cue:** We conduct experiments on three challenging settings: the LIBERO [28] and CALVIN [31] benchmarks for evaluation in simulation environments, and a real-world tablemounted Mobile ALOHA ...
- **p. 5 / 4. Experiments - extractive body cue:** We evaluate the effectiveness of our approach through a set of experiments spanning both simulation benchmarks and real-world robot manipulation tasks.
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** We use a stationary cobot magic dual-arm robot to assess our model's adaptability to novel real-world environments with a small number of robot demonstrations.
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** CALVIN spans 34 tasks across four environments (A-D), with 20,000+ episodes, emphasizing unseen object generalization and multi-stage sequences (e.g., "open drawer, pick blue block, push ...
- **p. 7 / 4.3. Ablation Studies - extractive body cue:** Results reported in Table 3 show that our method improves performance across different backbones, even on backbones not pre-trained on robotic datasets.
- **p. 7 / 4.3. Ablation Studies - extractive body cue:** Comparison on the LIBERO-Long task suite in the LIBERO benchmark in terms of success rates (%).
- **p. 8 / 4.4. Analysis - extractive body cue:** Ratio SR (%) SR (%) SR (%) SR (%) SR (%) 0% 97.4 99.4 97.4 97.6 98.0 50% 97.2 99.4 97.2 95.2 97.3 60% 97.6 ...
- **p. 8 / 4.4. Analysis - extractive body cue:** Pruning Spatial Object Goal Long Avg.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 4. Experiments (p. 5); 4.1. Experimental Setup (p. 5); 4.2. Evaluation Results (p. 6).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.3. Ablation Studies | EMPIRICAL / REAL-ROBOT OR HARDWARE | Each component alone improves over OpenVLA-OFT, and their combination achieves the best overall performance. | p. 7 (4.3. Ablation Studies) |
| 4.2. Evaluation Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | Results demonstrate that the proposed AVA-VLA framework achieves state-of-the-art overall performance in both singletask and multi-task settings. | p. 7 (4.2. Evaluation Results) |
| 4.1. Experimental Setup | EMPIRICAL / REAL-ROBOT OR HARDWARE | The results are reported in terms of success rates (%) and average length. | p. 6 (4.1. Experimental Setup) |
| 4.2. Evaluation Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | We use widely adopted performance evaluation metrics "Success Rate (SR)" (the same 13458 | p. 6 (4.2. Evaluation Results) |
| 4.4. Analysis | EMPIRICAL / REAL-ROBOT OR HARDWARE | The results on LIBERO in terms of success rates (%) under the "one policy for all 4 suites" setting are reported. | p. 8 (4.4. Analysis) |

## Dataset / Benchmark Role

- **p. 5 / 4.1. Experimental Setup - extractive body cue:** We conduct experiments on three challenging settings: the LIBERO [28] and CALVIN [31] benchmarks for evaluation in simulation environments, and a real-world tablemounted Mobile ALOHA ...
- **p. 5 / 4. Experiments - extractive body cue:** We evaluate the effectiveness of our approach through a set of experiments spanning both simulation benchmarks and real-world robot manipulation tasks.
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** We use a stationary cobot magic dual-arm robot to assess our model's adaptability to novel real-world environments with a small number of robot demonstrations.
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** CALVIN spans 34 tasks across four environments (A-D), with 20,000+ episodes, emphasizing unseen object generalization and multi-stage sequences (e.g., "open drawer, pick blue block, push ...
- **p. 7 / 4.3. Ablation Studies - extractive body cue:** Results reported in Table 3 show that our method improves performance across different backbones, even on backbones not pre-trained on robotic datasets.
- **p. 7 / 4.3. Ablation Studies - extractive body cue:** Comparison on the LIBERO-Long task suite in the LIBERO benchmark in terms of success rates (%).
- **p. 8 / 4.4. Analysis - extractive body cue:** Ratio SR (%) SR (%) SR (%) SR (%) SR (%) 0% 97.4 99.4 97.4 97.6 98.0 50% 97.2 99.4 97.2 95.2 97.3 60% 97.6 ...
- **p. 8 / 4.4. Analysis - extractive body cue:** Pruning Spatial Object Goal Long Avg.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. (a) Visualized comparison of the proposed AVA-VLA framework and vanilla VLAs. (b) Qualitative comparison of vi- sual focus from two viewpoints while executing ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. Overview of the proposed AVA-VLA framework. At each timestep, the recurrent state is projected from the previous hidden state to preserve historical context ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Comparison on the LIBERO benchmark. The results are reported in two groups: one policy for all 4 suites, and one policy per suite. ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 2. Comparison on the CALVIN ABC→D benchmark. The results are reported in terms of success rates (%) and average length. The best results in ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 3. Comparison on the Mobile ALOHA real-world experiments. Evaluation across four manipulation tasks, including (a) Pick and Place, (b) Sequenced Instruction Understanding, (c) Flexible ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 3. Ablation study on the model backbones. Comparison on the LIBERO-Long task suite in the LIBERO benchmark in terms of success rates (%). The ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 4. Ablation study on the two key components in the AVA-VLA framework. The results on LIBERO in terms of success rates (%) under the ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 4. Visual dynamics. The evolution of soft weights during the task "put both moka pots on the stove" from two viewpoints.

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We conduct experiments on three challenging settings: the LIBERO [28] and CALVIN [31] benchmarks for evaluation in simulation environments, and a real-world tablemounted Mobile ... | embodiment, simulator version and control stack | p. 5 (4.1. Experimental Setup), p. 5 (4. Experiments) |
| Task/environment | We evaluate the effectiveness of our approach through a set of experiments spanning both simulation benchmarks and real-world robot manipulation tasks. | reset, timeout, object/scene variation | p. 5 (4. Experiments), p. 6 (4.1. Experimental Setup) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 3 (3.2. AVA-VLA Framework), p. 3 (3.1. Preliminaries) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 4 (3.2. AVA-VLA Framework), p. 4 (3.2. AVA-VLA Framework) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We use widely adopted performance evaluation metrics "Success Rate (SR)" (the same 13458 | definition/direction/unit from same section | p. 6 (4.2. Evaluation Results) |
| The results are reported in terms of success rates (%) and average length. | definition/direction/unit from same section | p. 6 (4.1. Experimental Setup) |
| Comparison on the LIBERO-Long task suite in the LIBERO benchmark in terms of success rates (%). | definition/direction/unit from same section | p. 7 (4.3. Ablation Studies) |
| We present the success rates for each task and the average completed length across all five tasks of the CALVIN benchmark in Table 2. | definition/direction/unit from same section | p. 7 (4.2. Evaluation Results) |
| The results on LIBERO in terms of success rates (%) under the "one policy for all 4 suites" setting are reported. | definition/direction/unit from same section | p. 8 (4.4. Analysis) |
| The decline in success rate mainly comes from the most challenging LIBERO Long task suite, while the results remain consistent across the other task ... | definition/direction/unit from same section | p. 8 (4.4. Analysis) |
| Figure 2. Overview of the proposed AVA-VLA framework. At each timestep, the recurrent state is projected from the previous hidden state to preserve historical ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| It allows users to assess model performance across various challenges systemati13457 | definition/direction/unit from same section | p. 5 (4.1. Experimental Setup) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| The results show that the proposed AVA-VLA framework comprehensively outperforms baseline methods across all tasks. | comparison identity and matched condition | p. 7 (4.2. Evaluation Results) |
| Overall, AVA-VLA achieves the highest average performance compared to baseline approaches, confirming its real-world applicability. | comparison identity and matched condition | p. 7 (4.2. Evaluation Results) |
| Even after reducing 90% of the visual tokens, our method still outperforms many baseline methods listed in Table 1. | comparison identity and matched condition | p. 8 (4.4. Analysis) |
| Notably, with pruning ratios of 50%, 60%, and 70%, the proposed method continues to outperform the OpenVLAOFT and maintains performance comparable to the stateof-the-art ... | comparison identity and matched condition | p. 8 (4.4. Analysis) |
| Figure 1. (a) Visualized comparison of the proposed AVA-VLA framework and vanilla VLAs. (b) Qualitative comparison of vi- sual focus from two viewpoints while ... | comparison identity and matched condition | p. 1 (Figure/Table caption) |
| We selected recently published works' main method as baselines. | comparison identity and matched condition | p. 6 (4.2. Evaluation Results) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Additionally, we conduct a comprehensive ablation study and analysis to validate the effectiveness of our approach. | component/input/data sensitivity | p. 5 (4. Experiments) |
| To validate their individual effectiveness, we conduct ablation experiments on the LIBERO benchmark. | component/input/data sensitivity | p. 7 (4.3. Ablation Studies) |
| Ablation study on the two key components in the AVA-VLA framework. | component/input/data sensitivity | p. 8 (4.4. Analysis) |
| Ablation study on the model backbones. | component/input/data sensitivity | p. 7 (4.3. Ablation Studies) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our contributions are threefold: • We propose the novel AVA-VLA framework to solve the critical limitation of lacking historical context in MDPbased VLA models. | Each component alone improves over OpenVLA-OFT, and their combination achieves the best overall performance. | PDF body cue; verify exact table/figure and matched conditions | p. 7 (4.3. Ablation Studies), p. 7 (4.2. Evaluation Results), p. 6 (4.1. Experimental Setup), p. 6 (4.2. Evaluation Results), p. 8 (4.4. Analysis), p. 8 (4.4. Analysis) |
| Primary metric/result | Results demonstrate that the proposed AVA-VLA framework achieves state-of-the-art overall performance in both singletask and multi-task settings. | numeric claim only at cited anchor | p. 7 (4.2. Evaluation Results) |

- Numeric sentences retained from the body:
- **p. 5 / 4.1. Experimental Setup - extractive body cue:** It contains 5,000 episodes across 100 tasks.
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** CALVIN spans 34 tasks across four environments (A-D), with 20,000+ episodes, emphasizing unseen object generalization and multi-stage sequences (e.g., "open drawer, pick blue block, push ...
- **p. 7 / 4.2. Evaluation Results - extractive body cue:** The Pick and Place task is evaluated for a total of 30 trials (10 per object), while other tasks are evaluated for 24 trials each.
- **p. 5 / 3.4. Training and Inference Procedure - extractive body cue:** Therefore, the total loss of one training batch is the sum of the prediction loss and penalty loss of N truncated sequences: Ltotal = XN ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Furthermore, a direct comparison in Figure 1 reveals that while the vanilla OpenVLA-OFT baseline fails to localize the task-relevant region across viewpoints, AVAVLA maintains ... | p. 8 (4.4. Analysis) |
| body limitation/failure cue | Figure 1. (a) Visualized comparison of the proposed AVA-VLA framework and vanilla VLAs. (b) Qualitative comparison of vi- sual focus from two viewpoints while ... | p. 1 (Figure/Table caption) |
| body limitation/failure cue | Due to space limitations, implementation details are provided in Appendix A. | p. 5 (4.1. Experimental Setup) |
| body limitation/failure cue | LIBERO+ [11] is a challenging LIBERO-based benchmark, which offers a robust benchmarking framework with 7 perturbation dimensions and 21 sub-dimensions. | p. 5 (4.1. Experimental Setup) |
| body limitation/failure cue | The results demonstrate that the proposed model possesses robust semantic understanding and dexterous action capabilities after training. | p. 7 (4.2. Evaluation Results) |
| body limitation/failure cue | The results reported in Table 5, demonstrate the robustness of our method: the model suffers only a negligible drop in performance after pruning. | p. 8 (4.4. Analysis) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Therefore, the total loss of one training batch is the sum of the prediction loss and penalty loss of N truncated sequences: Ltotal = ... | p. 5 (3.4. Training and Inference Procedure) |
| Due to space limitations, implementation details are provided in Appendix A. | p. 5 (4.1. Experimental Setup) |
| We also test Flexible Object Folding, a deformable object manipulation task requiring a specific three-stage process to fold a towel ("fold towel twice"), and ... | p. 6 (4.1. Experimental Setup) |
| The Pick and Place task is evaluated for a total of 30 trials (10 per object), while other tasks are evaluated for 24 trials ... | p. 7 (4.2. Evaluation Results) |
| The corresponding recurrent state is computed by: rt-1 = B(ht-1 M ) ∈RLA×d, (5) where B is an MLP module that transforms the hidden ... | p. 3 (3.2. AVA-VLA Framework) |
| A typical VLA model Pθ, parameterized by θ, consists of four main components: a Large-Language-Model (LLM) backbone M, a vision encoder E, a language ... | p. 3 (3.1. Preliminaries) |
| (10) Then we compute the final soft weights for visual tokens at time t by ωt = ρtγ, where γ is a 2-dimensional vector. | p. 4 (3.3. Active Visual Attention) |
| Then it computes the attention matrix and feeds the output into a self-attention layer Ot = Self-Att  Cross-Att(Qt, Kt, Vt)  . | p. 4 (3.3. Active Visual Attention) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 4.4. Analysis - extractive body cue:** Furthermore, a direct comparison in Figure 1 reveals that while the vanilla OpenVLA-OFT baseline fails to localize the task-relevant region across viewpoints, AVAVLA maintains a ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. (a) Visualized comparison of the proposed AVA-VLA framework and vanilla VLAs. (b) Qualitative comparison of vi- sual focus from two viewpoints while executing ...
- **p. 5 / 4.1. Experimental Setup - extractive body cue:** Due to space limitations, implementation details are provided in Appendix A.
- **p. 5 / 4.1. Experimental Setup - extractive body cue:** LIBERO+ [11] is a challenging LIBERO-based benchmark, which offers a robust benchmarking framework with 7 perturbation dimensions and 21 sub-dimensions.
- **p. 7 / 4.2. Evaluation Results - extractive body cue:** The results demonstrate that the proposed model possesses robust semantic understanding and dexterous action capabilities after training.
- **p. 8 / 4.4. Analysis - extractive body cue:** The results reported in Table 5, demonstrate the robustness of our method: the model suffers only a negligible drop in performance after pruning.

- **PDF anchors reviewed:** datasets p. 5 (4.1. Experimental Setup), p. 5 (4. Experiments), p. 6 (4.1. Experimental Setup), p. 6 (4.1. Experimental Setup), p. 7 (4.3. Ablation Studies), p. 7 (4.3. Ablation Studies), metrics p. 6 (4.2. Evaluation Results), p. 6 (4.1. Experimental Setup), p. 7 (4.3. Ablation Studies), p. 7 (4.2. Evaluation Results), p. 8 (4.4. Analysis), p. 8 (4.4. Analysis), baselines p. 7 (4.2. Evaluation Results), p. 7 (4.2. Evaluation Results), p. 8 (4.4. Analysis), p. 8 (4.4. Analysis), p. 1 (Figure/Table caption), p. 6 (4.2. Evaluation Results), results p. 7 (4.3. Ablation Studies), p. 7 (4.2. Evaluation Results), p. 6 (4.1. Experimental Setup), p. 6 (4.2. Evaluation Results), p. 8 (4.4. Analysis), p. 8 (4.4. Analysis).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
