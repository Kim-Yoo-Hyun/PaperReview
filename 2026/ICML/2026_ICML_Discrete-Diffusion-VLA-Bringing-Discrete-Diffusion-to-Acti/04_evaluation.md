# Evaluation - Discrete Diffusion VLA: Bringing Discrete Diffusion to Action Decoding in Vision-Language-Action Policies

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=c3BVcHcSiR; PDF retrieval source: https://openreview.net/pdf/7c6c1101cef920f79b251ef422b6399d7e8f4ae1.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (4.3. Extended Evaluation Across Robot Platforms), p. 7 (4.4. Ablation Study), p. 7 (4.4. Ablation Study), p. 6 (4.1. Simulation Benchmarks and Baselines), p. 8 (4.4. Ablation Study), p. 8 (4.4. Ablation Study)): 5 shows Discrete Diffusion VLA achieves SOTA performance with 54.2% overall, outperforming all continuous diffusion/flowmatching policies (π0: 40.1%, +14.1%; GR00T-N1: 49.5%, +4.7%) and discrete baselines (π0-FAST: 48.3%, +5.9%).

## Evaluation Body Digest

- **p. 5 / 4.1. Simulation Benchmarks and Baselines - extractive body cue:** We evaluate Discrete Diffusion VLA on three different robot settings: (i) Franka Panda arm on LIBERO (Liu et al., 2023) (four suites: Spatial, Object, Goal, ...
- **p. 8 / 4.6. Real-Robot Evaluation - extractive body cue:** We first collect 150 demonstrations in RoboTwin simulation for domain alignment (80k steps), then fine-tune on 150 real-robot demonstrations (200k steps), with an action chunk ...
- **p. 6 / 4.1. Simulation Benchmarks and Baselines - extractive body cue:** Each column is a LIBERO task suite; values are averaged over 500 rollouts per suite (10 tasks × 50 episodes).
- **p. 6 / 4.1. Simulation Benchmarks and Baselines - extractive body cue:** OOD scenes include objects with different scale, materials, and appearance (e.g., larger bowl, metallic stove).
- **p. 8 / 4.6. Real-Robot Evaluation - extractive body cue:** Real-robot task setups on AgileX Cobot Magic.
- **p. 5 / 4.1. Simulation Benchmarks and Baselines - extractive body cue:** A complete per-table breakdown of sources, hardware, and training steps is provided in Appendix C.
- **p. 7 / 4.4. Ablation Study - extractive body cue:** Action head without robot pretraining.
- **p. 7 / 4.3. Extended Evaluation Across Robot Platforms - extractive body cue:** We report the results of all models pretrained with OXE dataset (O'Neill et al., 2024) and then fine-tuned with BridgeData V2 (Walke et al., 2023).

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 4. Experiments (p. 5); 4.1. Simulation Benchmarks and Baselines (p. 5); 4.3. Extended Evaluation Across Robot Platforms (p. 6); 4.6. Real-Robot Evaluation (p. 8).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4.3. Extended Evaluation Across Robot Platforms | EMPIRICAL / REAL-ROBOT OR HARDWARE | 5 shows Discrete Diffusion VLA achieves SOTA performance with 54.2% overall, outperforming all continuous diffusion/flowmatching policies (π0: 40.1%, +14.1%; GR00T-N1: 49.5%, +4.7%) and discrete ... | p. 6 (4.3. Extended Evaluation Across Robot Platforms) |
| 4.4. Ablation Study | EMPIRICAL / REAL-ROBOT OR HARDWARE | Discrete diffusion achieves the best average performance across all LIBERO suites, outperforming AR, FAST, parallel decoding, and continuous diffusion, confirming that the advantage is ... | p. 7 (4.4. Ablation Study) |
| 4.4. Ablation Study | EMPIRICAL / REAL-ROBOT OR HARDWARE | 8 shows that linear decay from 1.0 to 0.0 achieves 96.8%, outperforming hard argmax (96.2%) and fixed temperature (96.4%). | p. 7 (4.4. Ablation Study) |
| 4.1. Simulation Benchmarks and Baselines | EMPIRICAL / REAL-ROBOT OR HARDWARE | Notably, while OpenVLAOFT (L1) achieves the highest in-distribution (ID) accuracy, Discrete Diffusion VLA attains the best absolute OOD performance with the smallest degradation under ... | p. 6 (4.1. Simulation Benchmarks and Baselines) |
| 4.4. Ablation Study | EMPIRICAL / REAL-ROBOT OR HARDWARE | Ranking tokens by instance-wise confidence improves over one-shot parallel, and our max confidence yields the best accuracy (96.8%). | p. 8 (4.4. Ablation Study) |

## Dataset / Benchmark Role

- **p. 5 / 4.1. Simulation Benchmarks and Baselines - extractive body cue:** We evaluate Discrete Diffusion VLA on three different robot settings: (i) Franka Panda arm on LIBERO (Liu et al., 2023) (four suites: Spatial, Object, Goal, ...
- **p. 8 / 4.6. Real-Robot Evaluation - extractive body cue:** We first collect 150 demonstrations in RoboTwin simulation for domain alignment (80k steps), then fine-tune on 150 real-robot demonstrations (200k steps), with an action chunk ...
- **p. 6 / 4.1. Simulation Benchmarks and Baselines - extractive body cue:** Each column is a LIBERO task suite; values are averaged over 500 rollouts per suite (10 tasks × 50 episodes).
- **p. 6 / 4.1. Simulation Benchmarks and Baselines - extractive body cue:** OOD scenes include objects with different scale, materials, and appearance (e.g., larger bowl, metallic stove).
- **p. 8 / 4.6. Real-Robot Evaluation - extractive body cue:** Real-robot task setups on AgileX Cobot Magic.
- **p. 5 / 4.1. Simulation Benchmarks and Baselines - extractive body cue:** A complete per-table breakdown of sources, hardware, and training steps is provided in Appendix C.
- **p. 7 / 4.4. Ablation Study - extractive body cue:** Action head without robot pretraining.
- **p. 7 / 4.3. Extended Evaluation Across Robot Platforms - extractive body cue:** We report the results of all models pretrained with OXE dataset (O'Neill et al., 2024) and then fine-tuned with BridgeData V2 (Walke et al., 2023).

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Paradigm comparison. Continuous diffusion over ac- tion chunks (left) versus discrete token decoders: AR (sequential), BERT-style (parallel), and our discrete diffusion with re-masking.
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Overview of Discrete Diffusion VLA architecture. We extend the VLM backbone that encodes multi-view RGB images (SigLIP+DINOv2 ViTs) and linguistic instruction to decode ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. LIBERO task performance results (%). Each column is a LIBERO task suite; values are averaged over 500 rollouts per suite (10 tasks × ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3. Vision Augmentation Sample of LIBERO-OOD Goal Task. OOD scenes include objects with different scale, materials, and appearance (e.g., larger bowl, metallic stove).
- **p. 6 / Figure/Table caption - extractive body cue:** Table 2. Out-of-distribution performance on LIBERO-Goal
- **p. 6 / Figure/Table caption - extractive body cue:** Table 3. Out-of-distribution performance on LIBERO-Spatial
- **p. 7 / Figure/Table caption - extractive body cue:** Table 4. SimplerEnv evaluation across different policies on Google Robot tasks. We report the results of all models pretrained with OXE dataset (O'Neill et al., ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 5. SimplerEnv evaluation across different policies on WidowX Robot tasks. We report the results of all models pretrained with OXE dataset (O'Neill et al., ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We evaluate Discrete Diffusion VLA on three different robot settings: (i) Franka Panda arm on LIBERO (Liu et al., 2023) (four suites: Spatial, Object, ... | embodiment, simulator version and control stack | p. 5 (4.1. Simulation Benchmarks and Baselines), p. 8 (4.6. Real-Robot Evaluation) |
| Task/environment | We first collect 150 demonstrations in RoboTwin simulation for domain alignment (80k steps), then fine-tune on 150 real-robot demonstrations (200k steps), with an action ... | reset, timeout, object/scene variation | p. 8 (4.6. Real-Robot Evaluation), p. 6 (4.1. Simulation Benchmarks and Baselines) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 3 (3.1. Overview), p. 1 (1. Introduction) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 2 (1. Introduction), p. 1 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| On LIBERO-Goal, success rates are 95.6%, 95.8%, 96.6%, and 96.8% respectively (Tab. | definition/direction/unit from same section | p. 7 (4.4. Ablation Study) |
| Choice Temperature Hard Sample (Temp=0) Fixed Temp (Temp=1) Linear Decay Temp (Temp=1-t) Success Rates 96.2% 96.4% 96.8% Figure 4. | definition/direction/unit from same section | p. 8 (4.4. Ablation Study) |
| Notably, while OpenVLAOFT (L1) achieves the highest in-distribution (ID) accuracy, Discrete Diffusion VLA attains the best absolute OOD performance with the smallest degradation under ... | definition/direction/unit from same section | p. 6 (4.1. Simulation Benchmarks and Baselines) |
| Ranking tokens by instance-wise confidence improves over one-shot parallel, and our max confidence yields the best accuracy (96.8%). | definition/direction/unit from same section | p. 8 (4.4. Ablation Study) |
| We evaluate Discrete Diffusion VLA on three different robot settings: (i) Franka Panda arm on LIBERO (Liu et al., 2023) (four suites: Spatial, Object, ... | definition/direction/unit from same section | p. 5 (4.1. Simulation Benchmarks and Baselines) |
| We report the highest score across seeds. | definition/direction/unit from same section | p. 6 (4.1. Simulation Benchmarks and Baselines) |
| Accuracy generally improves with T while efficiency scales inversely. | definition/direction/unit from same section | p. 7 (4.4. Ablation Study) |
| Figure 2. Overview of Discrete Diffusion VLA architecture. We extend the VLM backbone that encodes multi-view RGB images (SigLIP+DINOv2 ViTs) and linguistic instruction to ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| 5 shows Discrete Diffusion VLA achieves SOTA performance with 54.2% overall, outperforming all continuous diffusion/flowmatching policies (π0: 40.1%, +14.1%; GR00T-N1: 49.5%, +4.7%) and discrete ... | comparison identity and matched condition | p. 6 (4.3. Extended Evaluation Across Robot Platforms) |
| All baseline results are cited from the original publication or reproduced under identical input modalities, backbone initialization, and training budget. | comparison identity and matched condition | p. 5 (4.1. Simulation Benchmarks and Baselines) |
| 4, Discrete Diffusion VLA achieves state-of-the-art performance across both discrete and continuous methods. | comparison identity and matched condition | p. 6 (4.3. Extended Evaluation Across Robot Platforms) |
| 8 shows that linear decay from 1.0 to 0.0 achieves 96.8%, outperforming hard argmax (96.2%) and fixed temperature (96.4%). | comparison identity and matched condition | p. 7 (4.4. Ablation Study) |
| Discrete diffusion achieves the best average performance across all LIBERO suites, outperforming AR, FAST, parallel decoding, and continuous diffusion, confirming that the advantage is ... | comparison identity and matched condition | p. 7 (4.4. Ablation Study) |
| Table 10. Source of baseline results across all main-paper tables. The reported batch size is the total batch size across all GPUs. Table | comparison identity and matched condition | p. 14 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Action head without robot pretraining. | component/input/data sensitivity | p. 7 (4.4. Ablation Study) |
| We evaluate Discrete Diffusion VLA on three different robot settings: (i) Franka Panda arm on LIBERO (Liu et al., 2023) (four suites: Spatial, Object, ... | component/input/data sensitivity | p. 5 (4.1. Simulation Benchmarks and Baselines) |
| On Variant Aggregation, Discrete Diffusion VLA attains 56.9%, competitive with RT-2-X (64.3%) and π0FAST (59.0%). | component/input/data sensitivity | p. 6 (4.3. Extended Evaluation Across Robot Platforms) |
| Model Visual Matching Variant Aggregation #Overall Average Pick Coke Mv Near Drawer Avg. | component/input/data sensitivity | p. 7 (4.3. Extended Evaluation Across Robot Platforms) |
| Ablation study on decoding strategy. | component/input/data sensitivity | p. 8 (4.4. Ablation Study) |
| (ii) Right y-axis: Ablation on denoising steps. | component/input/data sensitivity | p. 8 (4.4. Ablation Study) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In summary, our contributions are threefold: 1) We introduce the first discrete diffusion VLA, unifying action generation with vision-language modeling in one transformer, demonstrating ... | 5 shows Discrete Diffusion VLA achieves SOTA performance with 54.2% overall, outperforming all continuous diffusion/flowmatching policies (π0: 40.1%, +14.1%; GR00T-N1: 49.5%, +4.7%) and discrete ... | PDF body cue; verify exact table/figure and matched conditions | p. 6 (4.3. Extended Evaluation Across Robot Platforms), p. 7 (4.4. Ablation Study), p. 7 (4.4. Ablation Study), p. 6 (4.1. Simulation Benchmarks and Baselines), p. 8 (4.4. Ablation Study), p. 8 (4.4. Ablation Study) |
| Primary metric/result | Discrete diffusion achieves the best average performance across all LIBERO suites, outperforming AR, FAST, parallel decoding, and continuous diffusion, confirming that the advantage is ... | numeric claim only at cited anchor | p. 7 (4.4. Ablation Study) |

- Numeric sentences retained from the body:
- **p. 5 / 4.1. Simulation Benchmarks and Baselines - extractive body cue:** We evaluate Discrete Diffusion VLA on three different robot settings: (i) Franka Panda arm on LIBERO (Liu et al., 2023) (four suites: Spatial, Object, Goal, ...
- **p. 6 / 4.1. Simulation Benchmarks and Baselines - extractive body cue:** Each column is a LIBERO task suite; values are averaged over 500 rollouts per suite (10 tasks × 50 episodes).
- **p. 6 / 4.1. Simulation Benchmarks and Baselines - extractive body cue:** Against methods trained from scratch, Discrete Diffusion VLA surpasses Diffusion Policy and MDT by +24.0 and +20.3 points respectively.
- **p. 6 / 4.1. Simulation Benchmarks and Baselines - extractive body cue:** All results are averaged over 500 rollouts per suite.
- **p. 7 / 4.4. Ablation Study - extractive body cue:** Method Latency (ms) Speed (Hz) NFE OpenVLA (AR) 136.2 7.34 56 OpenVLA w/o KVcache (AR) 209.5 4.77 56 OpenVLA-OFT (Parallel Decoding) 31.1 32.14 1 OpenVLA-OFT ...
- **p. 8 / 4.5. Inference Efficiency - extractive body cue:** Discrete Diffusion VLA achieves 68.8 ms per chunk (14.53 Hz), 2× faster than AR (136.2 ms), and comparable to continuous diffusion when using same denoising ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 2. Overview of Discrete Diffusion VLA architecture. We extend the VLM backbone that encodes multi-view RGB images (SigLIP+DINOv2 ViTs) and linguistic instruction to ... | p. 3 (Figure/Table caption) |
| body limitation/failure cue | Beyond standard in-distribution (ID) evaluation, we assess out-of-distribution (OOD) generalization under two perturbation axes following LIBERO-PRO (Zhou et al., 2025): Language Augmentation, which paraphrases ... | p. 5 (4.1. Simulation Benchmarks and Baselines) |
| body limitation/failure cue | Table 2. Out-of-distribution performance on LIBERO-Goal | p. 6 (Figure/Table caption) |
| body limitation/failure cue | Vision degradation is similarly reduced at 20.4%, against 22.6%, 29.0%, and 23.2% respectively. | p. 6 (4.1. Simulation Benchmarks and Baselines) |
| body limitation/failure cue | Among these, training frequency serves as the most accessible and informative proxy, as tokens appearing more frequently tend to be learned more robustly. | p. 8 (4.7. Visualization of Adaptive Decoding Order) |
| body limitation/failure cue | Discrete Diffusion VLA denoises the entire chunk in T steps, where each step is a single forward pass predicting posteriors for all currently masked ... | p. 8 (4.5. Inference Efficiency) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| A complete per-table breakdown of sources, hardware, and training steps is provided in Appendix C. | p. 5 (4.1. Simulation Benchmarks and Baselines) |
| Details of implementation are provided in Appendix B. | p. 5 (4.1. Simulation Benchmarks and Baselines) |
| We report the highest score across seeds. | p. 6 (4.1. Simulation Benchmarks and Baselines) |
| Denoising steps and speed-quality trade-off. | p. 7 (4.4. Ablation Study) |
| 4 sweeps T and reports throughput (number of chunks per second) and success rates on LIBERO-Goal. | p. 7 (4.4. Ablation Study) |
| Each task is evaluated over 15 trials. | p. 8 (4.6. Real-Robot Evaluation) |
| (ii) Right y-axis: Ablation on denoising steps. | p. 8 (4.4. Ablation Study) |
| A key distinction from parallel decoding methods such as OpenVLA-OFT, which decode all action tokens simultaneously in a single forward pass as ˆa0 = ... | p. 4 (3.4. Algorithmic Pipeline) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Overview of Discrete Diffusion VLA architecture. We extend the VLM backbone that encodes multi-view RGB images (SigLIP+DINOv2 ViTs) and linguistic instruction to decode ...
- **p. 5 / 4.1. Simulation Benchmarks and Baselines - extractive body cue:** Beyond standard in-distribution (ID) evaluation, we assess out-of-distribution (OOD) generalization under two perturbation axes following LIBERO-PRO (Zhou et al., 2025): Language Augmentation, which paraphrases task ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 2. Out-of-distribution performance on LIBERO-Goal
- **p. 6 / 4.1. Simulation Benchmarks and Baselines - extractive body cue:** Vision degradation is similarly reduced at 20.4%, against 22.6%, 29.0%, and 23.2% respectively.
- **p. 8 / 4.7. Visualization of Adaptive Decoding Order - extractive body cue:** Among these, training frequency serves as the most accessible and informative proxy, as tokens appearing more frequently tend to be learned more robustly.
- **p. 8 / 4.5. Inference Efficiency - extractive body cue:** Discrete Diffusion VLA denoises the entire chunk in T steps, where each step is a single forward pass predicting posteriors for all currently masked tokens.

- **Evidence anchors reviewed:** datasets p. 5 (4.1. Simulation Benchmarks and Baselines), p. 8 (4.6. Real-Robot Evaluation), p. 6 (4.1. Simulation Benchmarks and Baselines), p. 6 (4.1. Simulation Benchmarks and Baselines), p. 8 (4.6. Real-Robot Evaluation), p. 5 (4.1. Simulation Benchmarks and Baselines), metrics p. 7 (4.4. Ablation Study), p. 8 (4.4. Ablation Study), p. 6 (4.1. Simulation Benchmarks and Baselines), p. 8 (4.4. Ablation Study), p. 5 (4.1. Simulation Benchmarks and Baselines), p. 6 (4.1. Simulation Benchmarks and Baselines), baselines p. 6 (4.3. Extended Evaluation Across Robot Platforms), p. 5 (4.1. Simulation Benchmarks and Baselines), p. 6 (4.3. Extended Evaluation Across Robot Platforms), p. 7 (4.4. Ablation Study), p. 7 (4.4. Ablation Study), p. 14 (Figure/Table caption), results p. 6 (4.3. Extended Evaluation Across Robot Platforms), p. 7 (4.4. Ablation Study), p. 7 (4.4. Ablation Study), p. 6 (4.1. Simulation Benchmarks and Baselines), p. 8 (4.4. Ablation Study), p. 8 (4.4. Ablation Study).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
