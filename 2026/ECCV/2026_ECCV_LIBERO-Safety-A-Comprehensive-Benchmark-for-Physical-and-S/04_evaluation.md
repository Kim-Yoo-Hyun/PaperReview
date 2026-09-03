# Evaluation - LIBERO-Safety: A Comprehensive Benchmark for Physical and Semantic Safety in Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (42 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2606.23686; PDF retrieval source: https://arxiv.org/pdf/2606.23686. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 11 (4 Experiment), p. 10 (4 Experiment), p. 12 (4 Experiment), p. 12 (4 Experiment), p. 13 (4 Experiment), p. 10 (4 Experiment)): Among the evaluated standard VLAs, π0.5 achieves the highest overall success rate across all suites and difficulty levels.

## Evaluation Body Digest

- **p. 40 / C.3 Additional Experimental Results - extractive body cue:** In our benchmark, the barrier function is defined by a distance-based safety margin: \la b el {e q:d i stance_barrier} h(z_t)= d(z_t,\mathcal {O}_t)-d_{\mathrm {safe}}, (A.4) ...
- **p. 14 / 4 Experiment - extractive body cue:** While the policy is capable of generating collision-free trajectories, perceptual errors in multi-object scenes can lead the end-effector toward incorrect targets. yields a collision-free task ...
- **p. 37 / C.2 Training Configurations - extractive body cue:** To ensure unbiased representation learning across tasks, dataset and trajectory weight balancing are explicitly enabled.
- **p. 41 / C.3 Additional Experimental Results - extractive body cue:** This example highlights that the proposed chunk-level formulation is effective not only in simulation but also in real-world deployment, where it improves safety while maintaining ...
- **p. 13 / 4 Experiment - extractive body cue:** Perturbation SR(%) LDLJ Time(s) CR(%) Noise 58.0 -17.82 365.9 3.3 Init State 60.3 -17.45 342.8 4.7 View 60.7 -17.72 362.6 4.7 Scene 60.0 -17.72 357.6 ...
- **p. 13 / 4 Experiment - extractive body cue:** Across diverse axes of visual and state stochasticity, including image noise (Noise), robot initial state (Init State), viewpoint shifts (View), and scene variations (Scene), the ...
- **p. 14 / 4 Experiment - extractive body cue:** 6, models often misdirect mechanically stable, collision-free grasps toward semantic distractors, particularly in scenes where multiple objects share high visual similarity.
- **p. 37 / C.2 Training Configurations - extractive body cue:** To enforce precise spatial grounding, the dataset incorporates Chain-of-Thought (CoT) bounding box predictions, with the loss objectives scaled asymmetrically (1.0 for VLA action formulation and ...

## Evaluation Type and Scope

- **Evaluation type:** `BENCHMARK / DATASET`.
- **Target system/task:** defined robot simulator/hardware task suite.
- **Input boundary:** standardized observation, action, task state와 evaluation split.
- **Output/decision under evaluation:** policy/controller trajectory 또는 measured result.
- **Primary target:** success metric, robustness, generalization과 reproducibility.
- **Detected evaluation headings:** 4 Experiment (p. 9); A.3 Additional Data-Generation and Evaluation-Split Details (p. 24); C Experiment Implementation (p. 30); C.3 Additional Experimental Results (p. 38).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4 Experiment | BENCHMARK / DATASET | Among the evaluated standard VLAs, π0.5 achieves the highest overall success rate across all suites and difficulty levels. | p. 11 (4 Experiment) |
| 4 Experiment | BENCHMARK / DATASET | Notably, the foundational OpenVLA model fails to achieve meaningful success | p. 10 (4 Experiment) |
| 4 Experiment | BENCHMARK / DATASET | While RoboBrain2.0 achieves a high RR (80%) at L0, its performance drops precipitously on more complex and deceptive prompts (L1 and L2). | p. 12 (4 Experiment) |
| 4 Experiment | BENCHMARK / DATASET | Standard evaluations often conflate generalization with task success, overlooking the critical risk that a model might achieve its objective through unsafe kinematic behaviors when ... | p. 12 (4 Experiment) |
| 4 Experiment | BENCHMARK / DATASET | Furthermore, improved LDLJ scores and reduced execution times indicate superior kinematic fluency. | p. 13 (4 Experiment) |

## Dataset / Benchmark Role

- **p. 40 / C.3 Additional Experimental Results - extractive body cue:** In our benchmark, the barrier function is defined by a distance-based safety margin: \la b el {e q:d i stance_barrier} h(z_t)= d(z_t,\mathcal {O}_t)-d_{\mathrm {safe}}, (A.4) ...
- **p. 14 / 4 Experiment - extractive body cue:** While the policy is capable of generating collision-free trajectories, perceptual errors in multi-object scenes can lead the end-effector toward incorrect targets. yields a collision-free task ...
- **p. 37 / C.2 Training Configurations - extractive body cue:** To ensure unbiased representation learning across tasks, dataset and trajectory weight balancing are explicitly enabled.
- **p. 41 / C.3 Additional Experimental Results - extractive body cue:** This example highlights that the proposed chunk-level formulation is effective not only in simulation but also in real-world deployment, where it improves safety while maintaining ...
- **p. 13 / 4 Experiment - extractive body cue:** Perturbation SR(%) LDLJ Time(s) CR(%) Noise 58.0 -17.82 365.9 3.3 Init State 60.3 -17.45 342.8 4.7 View 60.7 -17.72 362.6 4.7 Scene 60.0 -17.72 357.6 ...
- **p. 13 / 4 Experiment - extractive body cue:** Across diverse axes of visual and state stochasticity, including image noise (Noise), robot initial state (Init State), viewpoint shifts (View), and scene variations (Scene), the ...
- **p. 14 / 4 Experiment - extractive body cue:** 6, models often misdirect mechanically stable, collision-free grasps toward semantic distractors, particularly in scenes where multiple objects share high visual similarity.
- **p. 37 / C.2 Training Configurations - extractive body cue:** To enforce precise spatial grounding, the dataset incorporates Chain-of-Thought (CoT) bounding box predictions, with the loss objectives scaled asymmetrically (1.0 for VLA action formulation and ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: Real-world VLA deployment is severely bottlenecked by physical safety and semantic reasoning, constituting critical (a) VLA Safety Challenges. To systemati- cally evaluate these ...
- **p. 4 / Figure/Table caption - extractive body cue:** Table 1: Comparison with existing VLA benchmarks. Our benchmark jointly covers perceptual perturbations, parametric task definitions (L0-L2), scene dynam- ics (static/dynamic), physical and semantic safety, ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 2: Overview of our VLA Safety Benchmark. (a) Comprehensive En- vironments: Powered by our UBDDL, we construct massive, stochastic simulation environments featuring multi-dimensional visual/physical ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 2: Quantitative Comparison between Human Teleoperation and Our Keypose- driven Data Generation Pipeline. Metric Human Teleoperation Ours Human Effort (min/task) 7.4 1.8
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 3: Comparison of State Space Distributions. Compared to the LIBERO [28] benchmark, our dataset demonstrates significantly broader spatial coverage and a sub- stantially larger ...
- **p. 11 / Figure/Table caption - extractive body cue:** Table 3: Evaluation results on the Embodied Physical Safety Track. Metrics are reported as mean Success Rate (SR, %), with standard deviations computed across three ...
- **p. 11 / Figure/Table caption - extractive body cue:** Fig. 4: Emergent Spatial Reasoning. High-diversity training enables the model to transition from (a) non-linear avoid- ance to (b) optimal trajectory synthe- sis in obstacle-free ...
- **p. 12 / Figure/Table caption - extractive body cue:** Table 4: Evaluation results on the Se- mantic Safety Reasoning Track. Met- rics are reported as Refusal Rate (RR, %).

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | In our benchmark, the barrier function is defined by a distance-based safety margin: \la b el {e q:d i stance_barrier} h(z_t)= d(z_t,\mathcal {O}_t)-d_{\mathrm {safe}}, ... | embodiment, simulator version and control stack | p. 40 (C.3 Additional Experimental Results), p. 14 (4 Experiment) |
| Task/environment | While the policy is capable of generating collision-free trajectories, perceptual errors in multi-object scenes can lead the end-effector toward incorrect targets. yields a collision-free ... | reset, timeout, object/scene variation | p. 14 (4 Experiment), p. 37 (C.2 Training Configurations) |
| Observation/sensor | standardized observation, action, task state와 evaluation split | calibration, preprocessing, privileged input | p. 1 (462 Hand-Object Pairs), p. 1 (462 Hand-Object Pairs) |
| Output/decision | policy/controller trajectory 또는 measured result | action frame, controller and termination | p. 6 (462 Hand-Object Pairs), p. 7 (462 Hand-Object Pairs) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Metrics are reported as mean Success Rate (SR, %), with standard deviations computed across three training seeds shown in parentheses. | definition/direction/unit from same section | p. 11 (4 Experiment) |
| Consequently, we use the Success Rate (SR) as our primary metric, which strictly requires goal completion without any constraint violations. | definition/direction/unit from same section | p. 10 (4 Experiment) |
| A.10, zero-shot models exhibit near-zero success rates and severe collision rates. | definition/direction/unit from same section | p. 38 (C.3 Additional Experimental Results) |
| This vulnerability is particularly evident in L2 scenarios, where out-of-distribution (OOD) conditions lead to a near-total collapse in success rates for several prominent architectures. | definition/direction/unit from same section | p. 10 (4 Experiment) |
| Among the evaluated standard VLAs, π0.5 achieves the highest overall success rate across all suites and difficulty levels. | definition/direction/unit from same section | p. 11 (4 Experiment) |
| Sparklines show L0-L2 trends from left to right with a shared 0-1 y-axis; values above/below each plot are success rate / safety violation rate. ... | definition/direction/unit from same section | p. 32 (C.1 Model Details) |
| While the policy is capable of generating collision-free trajectories, perceptual errors in multi-object scenes can lead the end-effector toward incorrect targets. yields a collision-free ... | definition/direction/unit from same section | p. 14 (4 Experiment) |
| The F1 score is computed as \ mat hrm {F 1 }=\frac {2\mathrm {TP}}{2\mathrm {TP}+\mathrm {FP}+\mathrm {FN}}. | definition/direction/unit from same section | p. 38 (C.3 Additional Experimental Results) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Across diverse axes of visual and state stochasticity, including image noise (Noise), robot initial state (Init State), viewpoint shifts (View), and scene variations (Scene), ... | comparison identity and matched condition | p. 13 (4 Experiment) |
| In stark contrast to standard benchmarks such as LIBERO [28], in which state-of-the-art (SOTA) models frequently exhibit performance saturation, our safety-centric evaluation reveals critical ... | comparison identity and matched condition | p. 10 (4 Experiment) |
| These baselines are systematically categorized into 4 dominant paradigms to ensure a holistic assessment: (1) Standard VLA models (OpenVLA [23], OpenVLA-OFT [22], π0 [5], ... | comparison identity and matched condition | p. 9 (4 Experiment) |
| 4 summarize the comprehensive evaluation of the baseline models across our proposed multi-level safety-centric task taxonomy. | comparison identity and matched condition | p. 10 (4 Experiment) |
| CuRobo serves as a privileged planner baseline. | comparison identity and matched condition | p. 12 (4 Experiment) |
| Specifically, the introduction of unseen objects (Unseen Object) induces only a marginal CR increase from the 2.7% baseline to 3.3%. | comparison identity and matched condition | p. 13 (4 Experiment) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| To distinguish the safety-evaluation difficulty from the effect of training on LIBERO-Safety, we additionally evaluate two representative policies under two control settings: zero-shot inference ... | component/input/data sensitivity | p. 38 (C.3 Additional Experimental Results) |
| Functioning as a generative world model, it is pretrained on internet-scale video data to predict future visual observations from interleaved multi-modal histories, effectively deriving ... | component/input/data sensitivity | p. 32 (C.1 Model Details) |
| This architecture leverages large-scale vision-language pre-training to execute complex, language-conditioned manipulation tasks through standard text-generation pipelines. - OpenVLA-OFT [22]: A parameter-efficient variant of the ... | component/input/data sensitivity | p. 31 (C.1 Model Details) |
| To effectively balance the pre-trained components with the newly initialized action head, we implement a differential learning rate strategy using the AdamW optimizer (β1 ... | component/input/data sensitivity | p. 37 (C.2 Training Configurations) |
| Zero-shot models are evaluated without task-specific fine-tuning, while obstacle-free SFT models are fine-tuned on demonstrations without explicit safety-critical obstacle interactions. | component/input/data sensitivity | p. 38 (C.2 Training Configurations) |
| Method SR (%) ↑LDLJ ↑Time (s) ↓CR (%) ↓ OpenVLA-OFT, 50 demos/task 35.3 -17.94 380.5 20.0 OpenVLA-OFT, 500 demos/task 42.7 -17.67 372.0 11.7 The ... | component/input/data sensitivity | p. 39 (C.3 Additional Experimental Results) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In summary, we establish this evaluation framework through four core technical and empirical contributions: - Parametric Safety Benchmark and Taxonomy: We introduce the Unified ... | Among the evaluated standard VLAs, π0.5 achieves the highest overall success rate across all suites and difficulty levels. | PDF body cue; verify exact table/figure and matched conditions | p. 11 (4 Experiment), p. 10 (4 Experiment), p. 12 (4 Experiment), p. 12 (4 Experiment), p. 13 (4 Experiment), p. 10 (4 Experiment) |
| Primary metric/result | Notably, the foundational OpenVLA model fails to achieve meaningful success | numeric claim only at cited anchor | p. 10 (4 Experiment) |

- Numeric sentences retained from the body:
- **p. 13 / 4 Experiment - extractive body cue:** Perturbation SR(%) LDLJ Time(s) CR(%) Noise 58.0 -17.82 365.9 3.3 Init State 60.3 -17.45 342.8 4.7 View 60.7 -17.72 362.6 4.7 Scene 60.0 -17.72 357.6 ...
- **p. 33 / C.1 Model Details - extractive body cue:** Architecturally, it upgrades the core Vision-Language backbone with flexible resolution encoding (eliminating padding artifacts) and significantly expands the downstream action-generation Diffusion Transformer (DiT) from 16 ...
- **p. 33 / C.2 Training Configurations - extractive body cue:** The training is conducted on 8 GPUs with a local batch size of 16 per device, yielding a total effective batch size of 128.
- **p. 34 / C.2 Training Configurations - extractive body cue:** Training Parameter Value Optimization Steps 200, 000 Local Batch Size (per GPU) 16 Peak Learning Rate (η) 5.0 × 10-4 Gradient Accumulation Steps 1 Image ...
- **p. 34 / C.2 Training Configurations - extractive body cue:** The model is trained on 8 GPUs with a local batch size of 8 per device, resulting in a total effective batch size of 64.
- **p. 34 / C.2 Training Configurations - extractive body cue:** The optimization process is conducted over 150k gradient steps using a learning rate of η = 5.0 × 10-4 with a 10× decay scheduled after ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | This suggests that broader trajectory coverage can improve safety-aware execution across multiple VLA architectures, although it does not fully eliminate collision or task-completion failures. | p. 39 (C.3 Additional Experimental Results) |
| body limitation/failure cue | To further assess execution quality, we employ 3 supplementary metrics: Collision Rate (CR) isolates collision-induced terminations from standard task failures, Execution Time evaluates operational ... | p. 10 (4 Experiment) |
| body limitation/failure cue | These dynamic guardrails will allow the control policy to trigger verified safe fallback maneuvers prior to any catastrophic physical failure. | p. 42 (C.3 Additional Experimental Results) |
| body limitation/failure cue | E Limitations and Future Work While the proposed evaluation framework establishes a rigorous safety benchmark for visual language action models, several limitations regarding simulation ... | p. 41 (C.3 Additional Experimental Results) |
| body limitation/failure cue | Meanwhile, LIBEROSafety remains a simulation-based benchmark; it cannot fully capture realworld contact dynamics, hardware latency, or unpredictable human behavior. | p. 14 (5 Conclusion) |
| body limitation/failure cue | We introduce a UBDDL-powered parametric framework that procedurally generates diverse safety-critical scenes, together with a keypose-driven data generation pipeline that alleviates the scalability constraints ... | p. 14 (5 Conclusion) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Parameter Value Optimization Steps 30, 000 Local Batch Size (per GPU) 8 Gradient Accumulation Steps 2 Constant Learning Rate 3.5 × 10-4 Image Augmentation ... | p. 36 (C.2 Training Configurations) |
| Hyperparameter Value Total Training Steps 30, 000 Global Batch Size 256 Peak Learning Rate 5.0 × 10-5 Warmup Steps 10, 000 Training Precision bfloat16 ... | p. 35 (C.2 Training Configurations) |
| Hyperparameter Value Total Training Steps 30, 000 Global Batch Size 32 Peak Learning Rate (η) 2.5 × 10-5 Training Precision bfloat16 Learning Rate Schedule ... | p. 35 (C.2 Training Configurations) |
| Training Setting Value Total Optimization Steps 20, 000 Global Batch Size 640 Initial Learning Rate 1.0 × 10-4 Warmup Ratio 5% State Dropout (p) ... | p. 37 (C.2 Training Configurations) |
| Training Setting Value Total Optimization Steps 60, 000 Global Batch Size 1, 024 Initial Learning Rate 1.0 × 10-4 Warmup Ratio 5% GR00T N1.5 ... | p. 37 (C.2 Training Configurations) |
| The model is optimized over 20,000 steps with a substantially expanded global batch size of 640. | p. 38 (C.2 Training Configurations) |
| Each task is evaluated over 10 independent trials, and all reported results are averaged across three distinct random seeds to ensure statistical robustness. | p. 10 (4 Experiment) |
| Metrics are reported as mean Success Rate (SR, %), with standard deviations computed across three training seeds shown in parentheses. | p. 11 (4 Experiment) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 39 / C.3 Additional Experimental Results - extractive body cue:** This suggests that broader trajectory coverage can improve safety-aware execution across multiple VLA architectures, although it does not fully eliminate collision or task-completion failures.
- **p. 10 / 4 Experiment - extractive body cue:** To further assess execution quality, we employ 3 supplementary metrics: Collision Rate (CR) isolates collision-induced terminations from standard task failures, Execution Time evaluates operational efficiency ...
- **p. 42 / C.3 Additional Experimental Results - extractive body cue:** These dynamic guardrails will allow the control policy to trigger verified safe fallback maneuvers prior to any catastrophic physical failure.
- **p. 41 / C.3 Additional Experimental Results - extractive body cue:** E Limitations and Future Work While the proposed evaluation framework establishes a rigorous safety benchmark for visual language action models, several limitations regarding simulation fidelity ...
- **p. 14 / 5 Conclusion - extractive body cue:** Meanwhile, LIBEROSafety remains a simulation-based benchmark; it cannot fully capture realworld contact dynamics, hardware latency, or unpredictable human behavior.
- **p. 14 / 5 Conclusion - extractive body cue:** We introduce a UBDDL-powered parametric framework that procedurally generates diverse safety-critical scenes, together with a keypose-driven data generation pipeline that alleviates the scalability constraints of ...

- **Evidence anchors reviewed:** datasets p. 40 (C.3 Additional Experimental Results), p. 14 (4 Experiment), p. 37 (C.2 Training Configurations), p. 41 (C.3 Additional Experimental Results), p. 13 (4 Experiment), p. 13 (4 Experiment), metrics p. 11 (4 Experiment), p. 10 (4 Experiment), p. 38 (C.3 Additional Experimental Results), p. 10 (4 Experiment), p. 11 (4 Experiment), p. 32 (C.1 Model Details), baselines p. 13 (4 Experiment), p. 10 (4 Experiment), p. 9 (4 Experiment), p. 10 (4 Experiment), p. 12 (4 Experiment), p. 13 (4 Experiment), results p. 11 (4 Experiment), p. 10 (4 Experiment), p. 12 (4 Experiment), p. 12 (4 Experiment), p. 13 (4 Experiment), p. 10 (4 Experiment).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (42 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Across diverse axes of visual and state stochasticity, including image noise (Noise), robot initial state (Init State), viewpoint shifts (View), and scene variations (Scene), the SR remains relatively stable, fluctuating ... (p. 13, 4 Experiment).
- **Metric evidence:** Consequently, we use the Success Rate (SR) as our primary metric, which strictly requires goal completion without any constraint violations. (p. 10, 4 Experiment).
- **Baseline/ablation evidence:** Across diverse axes of visual and state stochasticity, including image noise (Noise), robot initial state (Init State), viewpoint shifts (View), and scene variations (Scene), the SR remains relatively stable, fluctuating ... (p. 13, 4 Experiment).
- **Failure/negative evidence:** This suggests that broader trajectory coverage can improve safety-aware execution across multiple VLA architectures, although it does not fully eliminate collision or task-completion failures. (p. 39, C.3 Additional Experimental Results).
