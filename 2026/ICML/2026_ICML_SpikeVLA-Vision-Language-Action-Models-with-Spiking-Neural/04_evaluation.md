# Evaluation - SpikeVLA: Vision-Language-Action Models with Spiking Neural Networks

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=W86R5sIsxE; PDF retrieval source: https://openreview.net/pdf/27ac3094b9d6afc1c8c39e0ae99418fd937e0219.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (4.2. Main Results), p. 6 (4.2. Main Results), p. 15 (Figure/Table caption), p. 7 (4.2. Main Results), p. 7 (Figure/Table caption), p. 8 (Figure/Table caption)): As shown in Table 2, it achieves a strong and stable navigation performance, maintaining high metric scores compared to NaVILA (Cheng et al., 2025).

## Evaluation Body Digest

- **p. 6 / 4.2. Main Results - extractive body cue:** Navigation Performance on VLN-CE Benchmarks.
- **p. 6 / 4.1. Experimental Setups - extractive body cue:** We use a unified benchmark that jointly evaluates navigation and low-level control.
- **p. 6 / 4.1. Experimental Setups - extractive body cue:** We evaluated VLN-CE R2R/RxR and VLN-CE-Isaac using a unified set of metrics, including NE, OS, SR, SPL, and nDTW, which capture goal-reaching accuracy, feasibility, success ...
- **p. 15 / Figure/Table caption - extractive body cue:** Figure 8: Ablation of Actor Network Dimensions. It shows the performance of different Actor network dimensions (A = [128, 128], A = [256, 128], A ...
- **p. 7 / 4.2. Main Results - extractive body cue:** SpikeVLA: Vision-Language-Action Models with Spiking Neural Networks 5.28 53.9 49.3 61.5 5.28 53.9 49.3 61.5 5.17 54.7 49.8 63.1 5.38 53.3 47.9 63.4 6.12 52.3 ...
- **p. 6 / 4.1. Experimental Setups - extractive body cue:** For low-level locomotion, we quantify command tracking and safety using linear and angular velocity tracking errors and the collision rate.
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 4: SNN action policy network ablations. The top row compares different spike encoding kernels (Laplacian, Gaussian, Triangular, and IMQ) in terms of reward, linear ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 6: Rewards across different population encoders. MEL donates Mean Episode Length, where higher values indicate better survival and task persistence. Kernel Classes Rewards MEL↑ ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 4. Experiments (p. 6); 4.1. Experimental Setups (p. 6); 4.2. Main Results (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4.2. Main Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | As shown in Table 2, it achieves a strong and stable navigation performance, maintaining high metric scores compared to NaVILA (Cheng et al., 2025). | p. 6 (4.2. Main Results) |
| 4.2. Main Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | The current results suggest that SpikeVLA achieves performance comparable to strong baselines (Zhang et al., 2024a; Cheng et al., 2025) under the same RGB-only, ... | p. 6 (4.2. Main Results) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 8: Ablation of Actor Network Dimensions. It shows the performance of different Actor network dimensions (A = [128, 128], A = [256, 128], ... | p. 15 (Figure/Table caption) |
| 4.2. Main Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | SpikeVLA: Vision-Language-Action Models with Spiking Neural Networks 5.28 53.9 49.3 61.5 5.28 53.9 49.3 61.5 5.17 54.7 49.8 63.1 5.38 53.3 47.9 63.4 6.12 ... | p. 7 (4.2. Main Results) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 3: Comparison of resource consumption and performance between ANN-based and SNN-based architectures. | p. 7 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 6 / 4.2. Main Results - extractive body cue:** Navigation Performance on VLN-CE Benchmarks.
- **p. 6 / 4.1. Experimental Setups - extractive body cue:** We use a unified benchmark that jointly evaluates navigation and low-level control.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: SpikeVLA: Vision-Language-Action Models with Spik- ing Neural Networks.
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2: Architecture of SpikeVLA. We introduce an SNN-based VLA architecture composed of a spiking neural network vision encoder, a multimodal spiking large language model, ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 3. The left side shows a comparison of resource con- sumption between the different components of SpikeVLA and NaVILA (Cheng et al., 2025), while ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 3: Comparison of resource consumption and performance between ANN-based and SNN-based architectures.
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1: Comparison with SOTA methods on the VLN-CE Benchmarks. The table summarizes navigation performance metrics NE, OS, SR, and SPL, together with resource-efficiency metric, ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2: VLN-CE-Isaac evaluation results. NaVILA result is reproduced under the same conditions. All experiments evaluated on 1,077 episodes in the VLN-CE-Isaac. VLN-CE-Isaac Resource Efficiency ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 4: SNN action policy network ablations. The top row compares different spike encoding kernels (Laplacian, Gaussian, Triangular, and IMQ) in terms of reward, linear ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 3: Comparison with SOTA methods on the Val-Unseen split of RxR-CE. The table summarizes navigation performance metrics NE, SR, SPL and nDTW, together with ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Navigation Performance on VLN-CE Benchmarks. | embodiment, simulator version and control stack | p. 6 (4.2. Main Results), p. 6 (4.1. Experimental Setups) |
| Task/environment | We use a unified benchmark that jointly evaluates navigation and low-level control. | reset, timeout, object/scene variation | p. 6 (4.1. Experimental Setups) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 6 (3.4. Spiking Neural Network for Action Policy), p. 5 (3.4. Spiking Neural Network for Action Policy) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 6 (3.4. Spiking Neural Network for Action Policy), p. 3 (3.1. Architecture) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We evaluated VLN-CE R2R/RxR and VLN-CE-Isaac using a unified set of metrics, including NE, OS, SR, SPL, and nDTW, which capture goal-reaching accuracy, feasibility, ... | definition/direction/unit from same section | p. 6 (4.1. Experimental Setups) |
| Figure 8: Ablation of Actor Network Dimensions. It shows the performance of different Actor network dimensions (A = [128, 128], A = [256, 128], ... | definition/direction/unit from same section | p. 15 (Figure/Table caption) |
| SpikeVLA: Vision-Language-Action Models with Spiking Neural Networks 5.28 53.9 49.3 61.5 5.28 53.9 49.3 61.5 5.17 54.7 49.8 63.1 5.38 53.3 47.9 63.4 6.12 ... | definition/direction/unit from same section | p. 7 (4.2. Main Results) |
| For low-level locomotion, we quantify command tracking and safety using linear and angular velocity tracking errors and the collision rate. | definition/direction/unit from same section | p. 6 (4.1. Experimental Setups) |
| Figure 4: SNN action policy network ablations. The top row compares different spike encoding kernels (Laplacian, Gaussian, Triangular, and IMQ) in terms of reward, ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Table 1: Comparison with SOTA methods on the VLN-CE Benchmarks. The table summarizes navigation performance metrics NE, OS, SR, and SPL, together with resource-efficiency ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Table 6: Rewards across different population encoders. MEL donates Mean Episode Length, where higher values indicate better survival and task persistence. Kernel Classes Rewards ... | definition/direction/unit from same section | p. 9 (Figure/Table caption) |
| Table 4: Closed-loop performance of the low-level policy. | definition/direction/unit from same section | p. 8 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| The current results suggest that SpikeVLA achieves performance comparable to strong baselines (Zhang et al., 2024a; Cheng et al., 2025) under the same RGB-only, ... | comparison identity and matched condition | p. 6 (4.2. Main Results) |
| As shown in Table 2, it achieves a strong and stable navigation performance, maintaining high metric scores compared to NaVILA (Cheng et al., 2025). | comparison identity and matched condition | p. 6 (4.2. Main Results) |
| Table 9: Ablation study of time step T of SNN action policy network. The baseline configuration is marked with ∗. | comparison identity and matched condition | p. 14 (Figure/Table caption) |
| Table 10: Ablation study of population encoding size P. The baseline configuration is marked with ∗. | comparison identity and matched condition | p. 15 (Figure/Table caption) |
| Table 1: Comparison with SOTA methods on the VLN-CE Benchmarks. The table summarizes navigation performance metrics NE, OS, SR, and SPL, together with resource-efficiency ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| Figure 3: Comparison of resource consumption and performance between ANN-based and SNN-based architectures. | comparison identity and matched condition | p. 7 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 4: SNN action policy network ablations. The top row compares different spike encoding kernels (Laplacian, Gaussian, Triangular, and IMQ) in terms of reward, ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| Table 9: Ablation study of time step T of SNN action policy network. The baseline configuration is marked with ∗. | component/input/data sensitivity | p. 14 (Figure/Table caption) |
| Table 8: Ablation study on the Val-Unseen split of R2R-CE and RxR-CE across different modules of the SpikeVLA. T R2R-CE Val Unseen RxR-CE Val ... | component/input/data sensitivity | p. 14 (Figure/Table caption) |
| Table 10: Ablation study of population encoding size P. The baseline configuration is marked with ∗. | component/input/data sensitivity | p. 15 (Figure/Table caption) |
| Figure 7: Ablation study of the population encoding size hyperparameter. It shows the performance of different population encoding dimensions (P = 2, 3, 5) ... | component/input/data sensitivity | p. 15 (Figure/Table caption) |
| The left side shows a comparison of resource consumption between the different components of SpikeVLA and NaVILA (Cheng et al., 2025), while the right ... | component/input/data sensitivity | p. 6 (4.2. Main Results) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| SpikeVLA consists of three complementary modules. | As shown in Table 2, it achieves a strong and stable navigation performance, maintaining high metric scores compared to NaVILA (Cheng et al., 2025). | PDF body cue; verify exact table/figure and matched conditions | p. 6 (4.2. Main Results), p. 6 (4.2. Main Results), p. 15 (Figure/Table caption), p. 7 (4.2. Main Results), p. 7 (Figure/Table caption), p. 8 (Figure/Table caption) |
| Primary metric/result | The current results suggest that SpikeVLA achieves performance comparable to strong baselines (Zhang et al., 2024a; Cheng et al., 2025) under the same RGB-only, ... | numeric claim only at cited anchor | p. 6 (4.2. Main Results) |

- Numeric sentences retained from the body:
- **p. 4 / 3.3. Multimodal Spiking Large Language Model - extractive body cue:** It =  Vh, Vc, T  ∈R(196×t+196+Ntext)×d, (6) where Vh ∈R(196×t)×d are history visual tokens, Vc ∈ R196×d are current visual tokens, T ∈RNtext×d ...
- **p. 5 / 3.3. Multimodal Spiking Large Language Model - extractive body cue:** To stabilize training, we merge L consecutive fine-grained steps into a multi-level spike token: si[t′] = (t′+1)L-1 X t=t′L Si,t, t′ = 0, . . ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | For low-level locomotion, we quantify command tracking and safety using linear and angular velocity tracking errors and the collision rate. | p. 6 (4.1. Experimental Setups) |
| body limitation/failure cue | This approach transforms continuous observations into sparse and robust spike events, improving the stability and noise robustness of quadruped locomotion control. | p. 5 (3.4. Spiking Neural Network for Action Policy) |
| body limitation/failure cue | Therefore, SpikeVLA does not simply trade accuracy for efficiency. instead, it achieves higher energy efficiency through a sparse, event-driven computational paradigm. | p. 8 (A ANN) |
| body limitation/failure cue | We evaluated SpikeVLA in the VLN-CE-Isaac simulator using the Unitree Go2 platform to assess its transferability to closedloop embodied execution under realistic dynamics and ... | p. 6 (4.2. Main Results) |
| body limitation/failure cue | Resource Efficiency Error ↓ Error ↓ Mem(MB)↓Eng(µJ)↓ACEs(106)↓ NaVILA 0.23 0.38 1.20 5.80 161.48 SpikeVLA 0.42 0.29 2.35 0.31 5.53 mance degradation. | p. 8 (A ANN) |
| body limitation/failure cue | Figure 8: Ablation of Actor Network Dimensions. It shows the performance of different Actor network dimensions (A = [128, 128], A = [256, 128], ... | p. 15 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| SpikeVLA substantially reduces inference cost, lowering GPU memory usage from 16.1 GB to 6.2 GB and achieving an energy metric of E=49.09J, which is ... | p. 6 (4.2. Main Results) |
| In the decoding module, we accumulate the spike count for each action dimension over T time steps and compute the firing rate fr(i) as ... | p. 5 (3.4. Spiking Neural Network for Action Policy) |
| We train the spiking action policy network using surrogate-gradient spatiotemporal backpropagation, accumulating gradients over discrete timesteps t = 1, . . . , T ... | p. 6 (3.4. Spiking Neural Network for Action Policy) |
| Built upon a spiking Transformer, it replaces dense continuous feature extraction with sparse, spike-driven computation over discrete timesteps. | p. 3 (3.2. Spike Neural Network Vision Encoder) |
| We propose an SNN-based visual encoder that fuses the current frame with history frames to provide temporal context for time-dependent VLA tasks. | p. 3 (3.2. Spike Neural Network Vision Encoder) |
| We build our visual encoder on SigLIPv2 and apply the proposed operation to linear layers, such as MLP blocks and attention projection matrices. | p. 4 (3.2. Spike Neural Network Vision Encoder) |
| We model compute-intensive mapping operations as linear layers and drive their computation with time-step increments generated by differential spiking neurons, resulting in event-driven execution. | p. 4 (3.2. Spike Neural Network Vision Encoder) |
| To encode continuous observation inputs into discrete spike outputs, we adopt population encoding. | p. 5 (3.4. Spiking Neural Network for Action Policy) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / 4.1. Experimental Setups - extractive body cue:** For low-level locomotion, we quantify command tracking and safety using linear and angular velocity tracking errors and the collision rate.
- **p. 5 / 3.4. Spiking Neural Network for Action Policy - extractive body cue:** This approach transforms continuous observations into sparse and robust spike events, improving the stability and noise robustness of quadruped locomotion control.
- **p. 8 / A ANN - extractive body cue:** Therefore, SpikeVLA does not simply trade accuracy for efficiency. instead, it achieves higher energy efficiency through a sparse, event-driven computational paradigm.
- **p. 6 / 4.2. Main Results - extractive body cue:** We evaluated SpikeVLA in the VLN-CE-Isaac simulator using the Unitree Go2 platform to assess its transferability to closedloop embodied execution under realistic dynamics and sensor ...
- **p. 8 / A ANN - extractive body cue:** Resource Efficiency Error ↓ Error ↓ Mem(MB)↓Eng(µJ)↓ACEs(106)↓ NaVILA 0.23 0.38 1.20 5.80 161.48 SpikeVLA 0.42 0.29 2.35 0.31 5.53 mance degradation.
- **p. 15 / Figure/Table caption - extractive body cue:** Figure 8: Ablation of Actor Network Dimensions. It shows the performance of different Actor network dimensions (A = [128, 128], A = [256, 128], A ...

- **Evidence anchors reviewed:** datasets p. 6 (4.2. Main Results), p. 6 (4.1. Experimental Setups), metrics p. 6 (4.1. Experimental Setups), p. 15 (Figure/Table caption), p. 7 (4.2. Main Results), p. 6 (4.1. Experimental Setups), p. 8 (Figure/Table caption), p. 7 (Figure/Table caption), baselines p. 6 (4.2. Main Results), p. 6 (4.2. Main Results), p. 14 (Figure/Table caption), p. 15 (Figure/Table caption), p. 7 (Figure/Table caption), p. 7 (Figure/Table caption), results p. 6 (4.2. Main Results), p. 6 (4.2. Main Results), p. 15 (Figure/Table caption), p. 7 (4.2. Main Results), p. 7 (Figure/Table caption), p. 8 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
