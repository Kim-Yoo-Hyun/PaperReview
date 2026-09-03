# Evaluation - On-Device Diffusion Transformer Policy for Efficient Robot Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Wu_On-Device_Diffusion_Transformer_Policy_for_Efficient_Robot_Manipulation_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Wu_On-Device_Diffusion_Transformer_Policy_for_Efficient_Robot_Manipulation_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (5.3. Evaluation on DiffusionPolicy Transformer), p. 6 (5.3. Evaluation on DiffusionPolicy Transformer), p. 7 (5.4. Evaluation on MDT-V), p. 7 (5.4. Evaluation on MDT-V), p. 8 (5.6. Qualitative Results), p. 8 (5.6. Qualitative Results)): The results show that through our method, the pruned model can achieve a comparable success rate with the vanilla model.

## Evaluation Body Digest

- **p. 6 / 5.1. Benchmarks and Evaluation Metrics - extractive body cue:** The benchmark dataset is split into four manipulation environments, A, B, C, and D.
- **p. 8 / 5.6. Qualitative Results - extractive body cue:** Except for the experiments on simulation environments, we also conduct the real-world experiments on robotic arms as presented in Section I.
- **p. 6 / 5.1. Benchmarks and Evaluation Metrics - extractive body cue:** The benchmark comprises 130 tasks across 4 suites: LIBERO-Spatial, LIBEROObject, LIBERO-Goal, LIBERO-100.
- **p. 7 / 5.4. Evaluation on MDT-V - extractive body cue:** Besides, we also conduct the experiments on the LIBERO datasets shown in Table 4, by comparing MDT-V and MDT-V/E3-D3 across LIBERO task suites, we find ...
- **p. 5 / 5. Experiments - extractive body cue:** In this section, we introduce the experimental settings, including the baselines, benchmarks, and evaluation metrics in Section 5.1.
- **p. 5 / 5.1. Benchmarks and Evaluation Metrics - extractive body cue:** We evaluate our method on the following benchmarks: • Push-T was first introduced in IBC [12] used to evaluate the performance of Diffusion Policies.
- **p. 3 / 4.2. Latency Analysis of Diffusion Policies - extractive body cue:** Since the diffusion policy is designed for real-time robot manipulation, it is crucial to assess the on-device latency of the policy models.
- **p. 4 / 4.2. Latency Analysis of Diffusion Policies - extractive body cue:** IE: Image Encoder, DT: Diffusion Transformer, GLE: Goal Language Encoder, NFE is short for the number of score function evaluations, i.e., inference steps., M: Million, ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 5. Experiments (p. 5); 5.1. Benchmarks and Evaluation Metrics (p. 5); 5.2. Implementation Details (p. 6); 5.3. Evaluation on DiffusionPolicy Transformer (p. 6); 5.4. Evaluation on MDT-V (p. 7); 5.6. Qualitative Results (p. 7).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 5.3. Evaluation on DiffusionPolicy Transformer | EMPIRICAL / REAL-ROBOT OR HARDWARE | The results show that through our method, the pruned model can achieve a comparable success rate with the vanilla model. | p. 6 (5.3. Evaluation on DiffusionPolicy Transformer) |
| 5.3. Evaluation on DiffusionPolicy Transformer | EMPIRICAL / REAL-ROBOT OR HARDWARE | Especially, we find a 2-layer diffusion transformer can achieve a success rate with 0.724, which is quite close to the original 14078 | p. 6 (5.3. Evaluation on DiffusionPolicy Transformer) |
| 5.4. Evaluation on MDT-V | EMPIRICAL / REAL-ROBOT OR HARDWARE | Similarly, in the D→D scenario, all models register lower performance, with the most compressed model suffering from a steep decline in both success rate ... | p. 7 (5.4. Evaluation on MDT-V) |
| 5.4. Evaluation on MDT-V | EMPIRICAL / REAL-ROBOT OR HARDWARE | Compared with the original model, the 6-layer model achieves comparable performance, while the 4-layer model has a significant performance drop and the 2-layer model ... | p. 7 (5.4. Evaluation on MDT-V) |
| 5.6. Qualitative Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | And in the LIBERO task suite that requires the agent to follow the instructions to manipulate the objects on the table to achieve the ... | p. 8 (5.6. Qualitative Results) |

## Dataset / Benchmark Role

- **p. 6 / 5.1. Benchmarks and Evaluation Metrics - extractive body cue:** The benchmark dataset is split into four manipulation environments, A, B, C, and D.
- **p. 8 / 5.6. Qualitative Results - extractive body cue:** Except for the experiments on simulation environments, we also conduct the real-world experiments on robotic arms as presented in Section I.
- **p. 6 / 5.1. Benchmarks and Evaluation Metrics - extractive body cue:** The benchmark comprises 130 tasks across 4 suites: LIBERO-Spatial, LIBEROObject, LIBERO-Goal, LIBERO-100.
- **p. 7 / 5.4. Evaluation on MDT-V - extractive body cue:** Besides, we also conduct the experiments on the LIBERO datasets shown in Table 4, by comparing MDT-V and MDT-V/E3-D3 across LIBERO task suites, we find ...
- **p. 5 / 5. Experiments - extractive body cue:** In this section, we introduce the experimental settings, including the baselines, benchmarks, and evaluation metrics in Section 5.1.
- **p. 5 / 5.1. Benchmarks and Evaluation Metrics - extractive body cue:** We evaluate our method on the following benchmarks: • Push-T was first introduced in IBC [12] used to evaluate the performance of Diffusion Policies.
- **p. 3 / 4.2. Latency Analysis of Diffusion Policies - extractive body cue:** Since the diffusion policy is designed for real-time robot manipulation, it is crucial to assess the on-device latency of the policy models.
- **p. 4 / 4.2. Latency Analysis of Diffusion Policies - extractive body cue:** IE: Image Encoder, DT: Diffusion Transformer, GLE: Goal Language Encoder, NFE is short for the number of score function evaluations, i.e., inference steps., M: Million, ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 3 / Figure/Table caption - extractive body cue:** Figure 1. The network architecture of MDT-V model. The model consists of three main components: the observation encoder E, the goal encoder G, and the ...
- **p. 4 / Figure/Table caption - extractive body cue:** Table 1. Time analysis for the (a) DiffusionPolicy Transformer (DP-T) and (b) MDT-V models on iPhone 13 (the top four rows show the original models, ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 2. The training pipeline of our proposed LightDP. In the left figure, we present the consistency distillation pipeline adopted in our method. The Student ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2. Performance comparison of LightDP compressed models with varying depth and inference steps. All models are trained on the same Push-T dataset for 3K ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 3. Performance comparison of LightDP compressed MDT-V models with different depth and inference steps. All models are trained on the CALVIN D or CALVIN ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 4. Performance comparison of LightDP compressed MDT-V/E3-D3 model on the benchmark LIBERO. For each task, the achieved score is presented along with its variability ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 5. Ablation study on the effect of the proposed learnable pruning and step distillation based on MDT-V, the performance is evaluated on the CALVIN ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 3. Qualitative comparison of the pruned models and orig- inal models. We observe that the pruned models can mimic the behaviors of the original ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The benchmark dataset is split into four manipulation environments, A, B, C, and D. | embodiment, simulator version and control stack | p. 6 (5.1. Benchmarks and Evaluation Metrics), p. 8 (5.6. Qualitative Results) |
| Task/environment | Except for the experiments on simulation environments, we also conduct the real-world experiments on robotic arms as presented in Section I. | reset, timeout, object/scene variation | p. 8 (5.6. Qualitative Results), p. 6 (5.1. Benchmarks and Evaluation Metrics) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 3 (4.1. Problem Formulation), p. 3 (4.1. Problem Formulation) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 5 (4.3. Prune the Model by Learning), p. 4 (4.3. Prune the Model by Learning) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| And we follow the evaluation protocol adopted in Diffusion Policy [8] to evaluate the success rate of the manipulation task. • CALVIN [30] is ... | definition/direction/unit from same section | p. 6 (5.1. Benchmarks and Evaluation Metrics) |
| Similarly, in the D→D scenario, all models register lower performance, with the most compressed model suffering from a steep decline in both success rate ... | definition/direction/unit from same section | p. 7 (5.4. Evaluation on MDT-V) |
| The results show that through our method, the pruned model can achieve a comparable success rate with the vanilla model. | definition/direction/unit from same section | p. 6 (5.3. Evaluation on DiffusionPolicy Transformer) |
| For each task, the achieved score is presented along with its variability (mean±standard deviation) Method Param (M) GFLOPs Latency (ms) Average Length MDT-V 22.52 ... | definition/direction/unit from same section | p. 8 (5.6. Qualitative Results) |
| Table 4. Performance comparison of LightDP compressed MDT-V/E3-D3 model on the benchmark LIBERO. For each task, the achieved score is presented along with its ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| These observations underscore the trade-off between model compactness and performance, highlighting that even a slight reduction in network depth can substantially impact the ability ... | definition/direction/unit from same section | p. 7 (5.4. Evaluation on MDT-V) |
| Figure 2. The training pipeline of our proposed LightDP. In the left figure, we present the consistency distillation pipeline adopted in our method. The ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| IE: Image Encoder, DT: Diffusion Transformer, GLE: Goal Language Encoder, NFE is short for the number of score function evaluations, i.e., inference steps., M: ... | definition/direction/unit from same section | p. 4 (4.2. Latency Analysis of Diffusion Policies) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Table 2. Performance comparison of LightDP compressed models with varying depth and inference steps. All models are trained on the same Push-T dataset for ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| And introduce the details about baselines used in our experiments, as well as the implementation details in Section 5.2. | comparison identity and matched condition | p. 5 (5. Experiments) |
| In this section, we introduce the experimental settings, including the baselines, benchmarks, and evaluation metrics in Section 5.1. | comparison identity and matched condition | p. 5 (5. Experiments) |
| We also implement MoDE, which is an MoE-based policy network that achieves the state-of-the-art performance on the CALVIN and LIBERO benchmarks. | comparison identity and matched condition | p. 6 (5.2. Implementation Details) |
| Compared with the original model, the 6-layer model achieves comparable performance, while the 4-layer model has a significant performance drop and the 2-layer model ... | comparison identity and matched condition | p. 7 (5.4. Evaluation on MDT-V) |
| The similar observation can be found in the MDT-V model, where the Voltron network costs relatively less time (7.56ms) compared to the diffusion transformer ... | comparison identity and matched condition | p. 4 (4.2. Latency Analysis of Diffusion Policies) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Ablation study on the effect of the proposed learnable pruning and step distillation based on MDT-V, the performance is evaluated on the CALVIN D→D ... | component/input/data sensitivity | p. 8 (5.6. Qualitative Results) |
| In contrast, the pruned variants show a noticeable decline in performance, where MDTV/E1-D1, for instance, achieves only 92.3% initially and drops to 61.4%, with ... | component/input/data sensitivity | p. 7 (5.4. Evaluation on MDT-V) |
| In the Push-T task, the pruned model successfully pushed the T-shaped block into the goal zone, without any failure in the manipu14079 | component/input/data sensitivity | p. 7 (5.6. Qualitative Results) |
| For DP-T, the network consists of two major components, the image encoder employs a ResNet18 model for converting the input image into embedding as ... | component/input/data sensitivity | p. 4 (4.2. Latency Analysis of Diffusion Policies) |
| Components IE DT Latency (ms) 1.28 0.906 Parameter (M) 11.2 8.97 NFE 1 100 Total Latency (ms) 1.28 90.6 Latency (ms) 1.28 0.68 Parameter ... | component/input/data sensitivity | p. 4 (4.2. Latency Analysis of Diffusion Policies) |
| Figure 1. The network architecture of MDT-V model. The model consists of three main components: the observation encoder E, the goal encoder G, and ... | component/input/data sensitivity | p. 3 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In this work, we introduce a novel framework named LightDP for Diffusion Policies that enables models to achieve real-time generation on mobile devices. | The results show that through our method, the pruned model can achieve a comparable success rate with the vanilla model. | PDF body cue; verify exact table/figure and matched conditions | p. 6 (5.3. Evaluation on DiffusionPolicy Transformer), p. 6 (5.3. Evaluation on DiffusionPolicy Transformer), p. 7 (5.4. Evaluation on MDT-V), p. 7 (5.4. Evaluation on MDT-V), p. 8 (5.6. Qualitative Results), p. 8 (5.6. Qualitative Results) |
| Primary metric/result | Especially, we find a 2-layer diffusion transformer can achieve a success rate with 0.724, which is quite close to the original 14078 | numeric claim only at cited anchor | p. 6 (5.3. Evaluation on DiffusionPolicy Transformer) |

- Numeric sentences retained from the body:
- **p. 4 / 4.2. Latency Analysis of Diffusion Policies - extractive body cue:** Components IE DT Latency (ms) 1.28 0.906 Parameter (M) 11.2 8.97 NFE 1 100 Total Latency (ms) 1.28 90.6 Latency (ms) 1.28 0.68 Parameter (M) ...
- **p. 4 / 4.2. Latency Analysis of Diffusion Policies - extractive body cue:** With the aid of LightDP, the diffusion transformers in DP-T and MDT-V achieve latency reductions from 90.6 ms and 22.25 ms to 2.72 ms and ...
- **p. 4 / 4.2. Latency Analysis of Diffusion Policies - extractive body cue:** For DP-T, the network consists of two major components, the image encoder employs a ResNet18 model for converting the input image into embedding as the ...
- **p. 4 / 4.2. Latency Analysis of Diffusion Policies - extractive body cue:** The diffusion transformer is an 8-layer transformer, which is the main bottleneck of the model (90.6 ms), demands 100 iterative denoising steps to get the ...
- **p. 4 / 4.2. Latency Analysis of Diffusion Policies - extractive body cue:** The similar observation can be found in the MDT-V model, where the Voltron network costs relatively less time (7.56ms) compared to the diffusion transformer (22.25ms), ...
- **p. 6 / 5.1. Benchmarks and Evaluation Metrics - extractive body cue:** There are 6hour human-teleoperated recording data in each environment, and only 1% of the data is annotated with language instructions.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | In the Push-T task, the pruned model successfully pushed the T-shaped block into the goal zone, without any failure in the manipu14079 | p. 7 (5.6. Qualitative Results) |
| body limitation/failure cue | Figure 2. The training pipeline of our proposed LightDP. In the left figure, we present the consistency distillation pipeline adopted in our method. The ... | p. 5 (Figure/Table caption) |
| body limitation/failure cue | Our consistency distillation is applied to the model's x0 prediction (predicting the denoised action), following common practice, and we start the EMA decay rate ... | p. 6 (5.2. Implementation Details) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We adopt AdamW as the optimizer with a learning rate of 1e -4, and the batch size is set as 64. | p. 6 (5.2. Implementation Details) |
| Then, we converted the model trained on GPU to Core ML model format (mlpackage, based on Apple's ml-stable-diffusion) and measured latency in Xcode Instruments ... | p. 6 (5.2. Implementation Details) |
| And introduce the details about baselines used in our experiments, as well as the implementation details in Section 5.2. | p. 5 (5. Experiments) |
| Since MDT-V consists of 4-layer TransformerEncoder and 4-layer TransformerDecoder, we keep the number of encoder layers the same as the decoder layers, therefore, we ... | p. 7 (5.4. Evaluation on MDT-V) |
| IE: Image Encoder, DT: Diffusion Transformer, GLE: Goal Language Encoder, NFE is short for the number of score function evaluations, i.e., inference steps., M: ... | p. 4 (4.2. Latency Analysis of Diffusion Policies) |
| A diffusion policy πϕ(a/o, g) is trained to imitate the expert's behavior by maximizing the log-likelihood of the action a Diffusion Transformer Observation Encoder ... | p. 3 (4.1. Problem Formulation) |
| Since the diffusion transformer requires multiple denoising steps to generate the action prediction, which leads to a high latency of the model. | p. 4 (4.2. Latency Analysis of Diffusion Policies) |
| All models are trained on the same Push-T dataset for 3K epochs. | p. 7 (Method) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / 5.6. Qualitative Results - extractive body cue:** In the Push-T task, the pruned model successfully pushed the T-shaped block into the goal zone, without any failure in the manipu14079
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 2. The training pipeline of our proposed LightDP. In the left figure, we present the consistency distillation pipeline adopted in our method. The Student ...
- **p. 6 / 5.2. Implementation Details - extractive body cue:** Our consistency distillation is applied to the model's x0 prediction (predicting the denoised action), following common practice, and we start the EMA decay rate at ...

- **Evidence anchors reviewed:** datasets p. 6 (5.1. Benchmarks and Evaluation Metrics), p. 8 (5.6. Qualitative Results), p. 6 (5.1. Benchmarks and Evaluation Metrics), p. 7 (5.4. Evaluation on MDT-V), p. 5 (5. Experiments), p. 5 (5.1. Benchmarks and Evaluation Metrics), metrics p. 6 (5.1. Benchmarks and Evaluation Metrics), p. 7 (5.4. Evaluation on MDT-V), p. 6 (5.3. Evaluation on DiffusionPolicy Transformer), p. 8 (5.6. Qualitative Results), p. 8 (Figure/Table caption), p. 7 (5.4. Evaluation on MDT-V), baselines p. 7 (Figure/Table caption), p. 5 (5. Experiments), p. 5 (5. Experiments), p. 6 (5.2. Implementation Details), p. 7 (5.4. Evaluation on MDT-V), p. 4 (4.2. Latency Analysis of Diffusion Policies), results p. 6 (5.3. Evaluation on DiffusionPolicy Transformer), p. 6 (5.3. Evaluation on DiffusionPolicy Transformer), p. 7 (5.4. Evaluation on MDT-V), p. 7 (5.4. Evaluation on MDT-V), p. 8 (5.6. Qualitative Results), p. 8 (5.6. Qualitative Results).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
