# Evaluation - VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (26 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=QZYZ0Xm58q; PDF retrieval source: https://openreview.net/pdf/ab187b19e4f174f9a6c3f7d82d52c8f6f1abfafb.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 9 (Figure/Table caption), p. 8 (5 Experiment), p. 9 (5 Experiment), p. 23 (Figure/Table caption), p. 7 (5 Experiment), p. 8 (5 Experiment)): Figure 4: Visualization of VLA-Cache token reuse across settings. (a) LIBERO simulation with OpenVLA. (b) Real-world task under dynamic background. (c) and (d) Main and wrist camera views from OpenVLA-OFT. ...

## Evaluation Body Digest

- **p. 9 / 5 Experiment - extractive PDF cue:** (Hz) ↑ PickPot PlaceCube PutSausage WipeTable Average OpenVLA 95.0% 83.3% 80.0% 70.0% 82.1% 1.814 64.16 4.02 + VLA-Cache 90.0% 90.0% 85.0% 73.3% 84.6% 1.303 51.85 ...
- **p. 7 / 5 Experiment - extractive PDF cue:** The LIBERO Benchmark [17] covers four task suites: Spatial, Object, Goal, and Long, each testing a different aspect of manipulation generalization.
- **p. 7 / 5 Experiment - extractive PDF cue:** In simulation, we evaluate VLA-Cache on three open-source VLA models: OpenVLA [11], OpenVLA-OFT [20] and CogAct [19], using the LIBERO benchmark [17] and SIMPLER environment ...
- **p. 8 / 5 Experiment - extractive PDF cue:** Best values are in bold. #Tokens Methods SR % ↑ FLOPs ↓ Latency (ms) ↓ 0 Baseline 84.4 1.888 52.37 50 SparseVLM 79.8 1.358 88.08 ...
- **p. 9 / 5 Experiment - extractive PDF cue:** (b) Real-world task under dynamic background.
- **p. 8 / 5 Experiment - extractive PDF cue:** More details about real-world experiments are available in the AppendixE.4.
- **p. 7 / 5 Experiment - extractive PDF cue:** Success rate and control frequency respectively assess task performance and the responsiveness of action prediction in closed-loop control.
- **p. 9 / 5 Experiment - extractive PDF cue:** Overall, VLA-Cache improves the average success rate by 2.4%, likely due to reduced interference from redundant visual tokens and enhanced decision robustness.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 5 Experiment (p. 7).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 4: Visualization of VLA-Cache token reuse across settings. (a) LIBERO simulation with OpenVLA. (b) Real-world task under dynamic background. (c) and (d) Main ... | p. 9 (Figure/Table caption) |
| 5 Experiment | EMPIRICAL / REAL-ROBOT OR HARDWARE | VLACache reduces FLOPs by 27.31% and improves latency by 1.63× over standard OpenVLA, with only a 0.3% drop in success rate. | p. 8 (5 Experiment) |
| 5 Experiment | EMPIRICAL / REAL-ROBOT OR HARDWARE | Overall, VLA-Cache improves the average success rate by 2.4%, likely due to reduced interference from redundant visual tokens and enhanced decision robustness. | p. 9 (5 Experiment) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 10: Varying the relevance threshold τ (with k=100). Overall, efficiency (FLOPs and latency) improves monotonically with larger k and τ, while success rate ... | p. 23 (Figure/Table caption) |
| 5 Experiment | EMPIRICAL / REAL-ROBOT OR HARDWARE | Success rate and control frequency respectively assess task performance and the responsiveness of action prediction in closed-loop control. | p. 7 (5 Experiment) |

## Dataset / Benchmark Role

- **p. 9 / 5 Experiment - extractive PDF cue:** (Hz) ↑ PickPot PlaceCube PutSausage WipeTable Average OpenVLA 95.0% 83.3% 80.0% 70.0% 82.1% 1.814 64.16 4.02 + VLA-Cache 90.0% 90.0% 85.0% 73.3% 84.6% 1.303 51.85 ...
- **p. 7 / 5 Experiment - extractive PDF cue:** The LIBERO Benchmark [17] covers four task suites: Spatial, Object, Goal, and Long, each testing a different aspect of manipulation generalization.
- **p. 7 / 5 Experiment - extractive PDF cue:** In simulation, we evaluate VLA-Cache on three open-source VLA models: OpenVLA [11], OpenVLA-OFT [20] and CogAct [19], using the LIBERO benchmark [17] and SIMPLER environment ...
- **p. 8 / 5 Experiment - extractive PDF cue:** Best values are in bold. #Tokens Methods SR % ↑ FLOPs ↓ Latency (ms) ↓ 0 Baseline 84.4 1.888 52.37 50 SparseVLM 79.8 1.358 88.08 ...
- **p. 9 / 5 Experiment - extractive PDF cue:** (b) Real-world task under dynamic background.
- **p. 8 / 5 Experiment - extractive PDF cue:** More details about real-world experiments are available in the AppendixE.4.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 1: During the inference of the VLA model, static tokens of the input image remain largely consistent across steps. This consistency allows for caching ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Table 1. To mitigate this, VLA-Cache incorporates a lightweight filtering mechanism based on decoder attention scores to exclude task- relevant tokens from reuse, ensuring that ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2: VLA-Cache accelerates the VLA's language decoding process across timesteps via the following two steps: (a) Dynamic Token Selection reuses static tokens across frames ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Table 1: Comparison of VLA-Cache's core token selection strategies on OpenVLA using the LIBERO Spatial benchmark.
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 3: Tasks on LIBERO Benchmark, the SIMPLER Environment and Real World. Total Complexity Reduction. Bringing all components together, the theoretical overall FLOP reduction per ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 2: Comparison of different VLA acceleration methods on the LIBERO benchmark.
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 3: Comparison of VLA-Cache within the CogACT model in the SIMPLER environment. SIMPLER
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 4: Ablation on token pruning/reuse in LIBERO-Spatial using OpenVLA (256 vision tokens). Best values are in bold. #Tokens Methods SR % ↑ FLOPs ↓ ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | (Hz) ↑ PickPot PlaceCube PutSausage WipeTable Average OpenVLA 95.0% 83.3% 80.0% 70.0% 82.1% 1.814 64.16 4.02 + VLA-Cache 90.0% 90.0% 85.0% 73.3% 84.6% 1.303 ... | embodiment, simulator version and control stack | p. 9 (5 Experiment), p. 7 (5 Experiment) |
| Task/environment | The LIBERO Benchmark [17] covers four task suites: Spatial, Object, Goal, and Long, each testing a different aspect of manipulation generalization. | reset, timeout, object/scene variation | p. 7 (5 Experiment), p. 7 (5 Experiment) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 3 (3 Methodology), p. 3 (3 Methodology) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 1 (1 Introduction), p. 1 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Figure 4: Visualization of VLA-Cache token reuse across settings. (a) LIBERO simulation with OpenVLA. (b) Real-world task under dynamic background. (c) and (d) Main ... | definition/direction/unit from same section | p. 9 (Figure/Table caption) |
| Success rate and control frequency respectively assess task performance and the responsiveness of action prediction in closed-loop control. | definition/direction/unit from same section | p. 7 (5 Experiment) |
| Overall, VLA-Cache improves the average success rate by 2.4%, likely due to reduced interference from redundant visual tokens and enhanced decision robustness. | definition/direction/unit from same section | p. 9 (5 Experiment) |
| We evaluate VLA-Cache using four metrics: success rate, control frequency, FLOPs, and CUDA latency. | definition/direction/unit from same section | p. 7 (5 Experiment) |
| Method Success Rate ↑ FLOPs (T)↓ Latency (ms)↓ Control Freq. | definition/direction/unit from same section | p. 8 (5 Experiment) |
| For all methods, aggressive token reduction harms success rate, underscoring the need to preserve informative content. | definition/direction/unit from same section | p. 8 (5 Experiment) |
| Table 6: Comparison of success rates across different tasks in the LIBERO-Spatial benchmark. | definition/direction/unit from same section | p. 22 (Figure/Table caption) |
| Table 10: Varying the relevance threshold τ (with k=100). Overall, efficiency (FLOPs and latency) improves monotonically with larger k and τ, while success rate ... | definition/direction/unit from same section | p. 23 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Specifically, we adopt two state-of-the-art token-level acceleration techniques SparseVLM [30] and FastV [29] on OpenVLA as compared methods in the LIBERO benchmark. | comparison identity and matched condition | p. 7 (5 Experiment) |
| Figure 5: VLA-Cache test results and attention heat map in a simulated environment E.3 Additional Ablations and Comparisons Attention vs. object-mask proxies for task ... | comparison identity and matched condition | p. 22 (Figure/Table caption) |
| 5.1 Experiment Setup Compared Methods. | comparison identity and matched condition | p. 7 (5 Experiment) |
| It performs robustly across tasks and exceeds the baseline on goal-oriented manipulation. | comparison identity and matched condition | p. 8 (5 Experiment) |
| Best values are in bold. #Tokens Methods SR % ↑ FLOPs ↓ Latency (ms) ↓ 0 Baseline 84.4 1.888 52.37 50 SparseVLM 79.8 1.358 ... | comparison identity and matched condition | p. 8 (5 Experiment) |
| As shown in Table 7, success rate of baseline dropped from 95% to 80% under noise. | comparison identity and matched condition | p. 9 (5 Experiment) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 10: Varying the relevance threshold τ (with k=100). Overall, efficiency (FLOPs and latency) improves monotonically with larger k and τ, while success rate ... | component/input/data sensitivity | p. 23 (Figure/Table caption) |
| The SIMPLER simulator [18] offers two settings, Visual Matching and Variant Aggregation, designed to bridge simulation-to-reality gaps. | component/input/data sensitivity | p. 7 (5 Experiment) |
| Ablation on Token Reusing/Pruning Rate. | component/input/data sensitivity | p. 8 (5 Experiment) |
| When applied to OpenVLA-OFT, a faster variant with action chunking, VLA-Cache further boosts control frequency by nearly 14 Hz, showing strong compatibility with high-frequency ... | component/input/data sensitivity | p. 8 (5 Experiment) |
| Figure 5: VLA-Cache test results and attention heat map in a simulated environment E.3 Additional Ablations and Comparisons Attention vs. object-mask proxies for task ... | component/input/data sensitivity | p. 22 (Figure/Table caption) |
| Table 8: Attention vs. object-mask proxies for task relevance on LIBERO-SPATIAL. While object masks provide spatial localization, they can miss fine-grained or contextual signals ... | component/input/data sensitivity | p. 23 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To address the inefficiency introduced by repeatedly processing static visual information, we present VLA-Cache, a training-free inference acceleration method that exploits temporal continuity in ... | Figure 4: Visualization of VLA-Cache token reuse across settings. (a) LIBERO simulation with OpenVLA. (b) Real-world task under dynamic background. (c) and (d) Main ... | PDF body cue; verify exact table/figure and matched conditions | p. 9 (Figure/Table caption), p. 8 (5 Experiment), p. 9 (5 Experiment), p. 23 (Figure/Table caption), p. 7 (5 Experiment), p. 8 (5 Experiment) |
| Primary metric/result | VLACache reduces FLOPs by 27.31% and improves latency by 1.63× over standard OpenVLA, with only a 0.3% drop in success rate. | numeric claim only at cited anchor | p. 8 (5 Experiment) |

- Numeric sentences retained from the body:
- **p. 7 / 5 Experiment - extractive PDF cue:** All experiments are conducted on an NVIDIA RTX 4090 GPU.
- **p. 8 / 5 Experiment - extractive PDF cue:** Demonstrations are collected via teleoperation at 10 Hz using an Xbox controller, resulting in 150-200 trajectories per task.
- **p. 8 / 5 Experiment - extractive PDF cue:** When applied to OpenVLA-OFT, a faster variant with action chunking, VLA-Cache further boosts control frequency by nearly 14 Hz, showing strong compatibility with high-frequency architectures ...
- **p. 8 / 5 Experiment - extractive PDF cue:** Moreover, these methods target long output sequences, whereas VLA models generate short action outputs (e.g., 7 tokens), rendering the speedups marginal.
- **p. 8 / 5 Experiment - extractive PDF cue:** VLA-Cache maintains stable performance at moderate reuse rates (i.e., 100 tokens), while FastV and SparseVLM suffer larger drops due to loss of critical visual details.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Table 11: Real-world results with trial counts and success rates. Results with Counts and Rates. Table 11 reports per-task successes and failures, along with ... | p. 25 (Figure/Table caption) |
| body limitation/failure cue | In contrast, FastV and SparseVLM fail to improve inference speed and often degrade task performance. | p. 8 (5 Experiment) |
| body limitation/failure cue | It performs robustly across tasks and exceeds the baseline on goal-oriented manipulation. | p. 8 (5 Experiment) |
| body limitation/failure cue | As shown in Table 7, success rate of baseline dropped from 95% to 80% under noise. | p. 9 (5 Experiment) |
| body limitation/failure cue | To assess robustness, we introduced background motion (e.g., human hands and moving objects) in the PickPot task. | p. 9 (5 Experiment) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| FLOPs measure theoretical computation, while CUDA latency captures actual GPU runtime. | p. 7 (5 Experiment) |
| The method also achieves considerable reductions in FLOPs and inference time. | p. 9 (5 Experiment) |
| The efficiency gains are evident in the FLOPs and inference time measurements. | p. 9 (5 Experiment) |
| All experiments are conducted on an NVIDIA RTX 4090 GPU. | p. 7 (5 Experiment) |
| By filtering out task-relevant tokens based on decoder attention, our method recovers 8 | p. 8 (5 Experiment) |
| Initially proposed in the Transformer architecture [37], KV caching enables the model to reuse previously computed key (K) and value (V) vectors for each ... | p. 3 (3 Methodology) |
| Concretely, given a sequence of input tokens X, the self-attention mechanism computes: Q = XWQ, K = XWK, V = XWV , (1) Attn(Q, ... | p. 3 (3 Methodology) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 25 / Figure/Table caption - extractive PDF cue:** Table 11: Real-world results with trial counts and success rates. Results with Counts and Rates. Table 11 reports per-task successes and failures, along with the ...
- **p. 8 / 5 Experiment - extractive PDF cue:** In contrast, FastV and SparseVLM fail to improve inference speed and often degrade task performance.
- **p. 8 / 5 Experiment - extractive PDF cue:** It performs robustly across tasks and exceeds the baseline on goal-oriented manipulation.
- **p. 9 / 5 Experiment - extractive PDF cue:** As shown in Table 7, success rate of baseline dropped from 95% to 80% under noise.
- **p. 9 / 5 Experiment - extractive PDF cue:** To assess robustness, we introduced background motion (e.g., human hands and moving objects) in the PickPot task.

- **PDF anchors reviewed:** datasets p. 9 (5 Experiment), p. 7 (5 Experiment), p. 7 (5 Experiment), p. 8 (5 Experiment), p. 9 (5 Experiment), p. 8 (5 Experiment), metrics p. 9 (Figure/Table caption), p. 7 (5 Experiment), p. 9 (5 Experiment), p. 7 (5 Experiment), p. 8 (5 Experiment), p. 8 (5 Experiment), baselines p. 7 (5 Experiment), p. 22 (Figure/Table caption), p. 7 (5 Experiment), p. 8 (5 Experiment), p. 8 (5 Experiment), p. 9 (5 Experiment), results p. 9 (Figure/Table caption), p. 8 (5 Experiment), p. 9 (5 Experiment), p. 23 (Figure/Table caption), p. 7 (5 Experiment), p. 8 (5 Experiment).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
