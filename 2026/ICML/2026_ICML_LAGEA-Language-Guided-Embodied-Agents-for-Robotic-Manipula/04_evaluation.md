# Evaluation - LAGEA: Language Guided Embodied Agents for Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (23 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=watVfFbZGF; PDF retrieval source: https://openreview.net/pdf/28f8573440fbd9bb2ac48d0e31f3573d128fcf46.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 15 (Figure/Table caption), p. 6 (4. Experiments), p. 6 (4. Experiments), p. 7 (4.3.1. SYNERGY OF DELTA REWARDS AND ADAPTIVE), p. 5 (4. Experiments), p. 7 (4.3.1. SYNERGY OF DELTA REWARDS AND ADAPTIVE)): Table 8. Effect of different text encoders on observation-based manipulation tasks. Results are averaged over three random seeds (Standard Deviation is in brackets); higher is better. comparison highlights that while ...

## Evaluation Body Digest

- **p. 5 / 4. Experiments - extractive PDF cue:** Setup: We evaluate LAGEA framework on ten robotics tasks from the Meta-world MT10 benchmark (Yu et al., 2020) and Robotic Fetch (Plappert et al., 2018), ...
- **p. 5 / 4. Experiments - extractive PDF cue:** We also include LIV (Ma et al., 2023), a robotics reward model pre-trained on large-scale datasets, and a variant, LIV-Proj, which utilizes randomly initialized and ...
- **p. 7 / 4.1.2. RESULTS ON FETCH TASKS - extractive PDF cue:** LAGEA: Language Guided Embodied Agents for Robotic Manipulation 0.0M 0.2M 0.4M 0.6M 0.8M 1.0M Environment Steps 0 20 40 60 80 100 Success Rate (%) ...
- **p. 8 / 4.3.1. SYNERGY OF DELTA REWARDS AND ADAPTIVE - extractive PDF cue:** LAGEA: Language Guided Embodied Agents for Robotic Manipulation 0.2M 0.3M 0.4M 0.5M 0.6M 0.7M 0.8M Environment Steps 12 10 8 6 4 2 Average Logit ...
- **p. 6 / 4. Experiments - extractive PDF cue:** Experiment results on MT10 benchmarks with fixed goal.
- **p. 6 / 4.1.2. RESULTS ON FETCH TASKS - extractive PDF cue:** We further evaluate LAGEA on the Robotic Fetch (Plappert et al., 2018) manipulation suite to assess its effectiveness in sparse-reward, goal-conditioned control.
- **p. 7 / 4.1.2. RESULTS ON FETCH TASKS - extractive PDF cue:** 0.0M 0.2M 0.4M 0.6M 0.8M 1.0M Environment Steps 400 200 0 200 400 VLM Reward VLM Reward Signal Over Training 0.0M 0.2M 0.4M 0.6M 0.8M ...
- **p. 8 / 4.3.3. IMPACT OF STRUCTURED FEEDBACK - extractive PDF cue:** Task Freeform Feedback Structured Feedback Button press topdown v2 obs.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 4. Experiments (p. 5); 4.1.2. RESULTS ON FETCH TASKS (p. 6).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Table 8. Effect of different text encoders on observation-based manipulation tasks. Results are averaged over three random seeds (Standard Deviation is in brackets); higher ... | p. 15 (Figure/Table caption) |
| 4. Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | As shown in Table 1, LAGEA achieves a strong performance improvement of 5.3% over baselines, with an average success rate of 80% on hidden-fixed ... | p. 6 (4. Experiments) |
| 4. Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | In the observable-random goal setting (Table 2), LAGEA achieves a 70.4% average success rate, representing a 9% improvement over all baselines. | p. 6 (4. Experiments) |
| 4.3.1. SYNERGY OF DELTA REWARDS AND ADAPTIVE | EMPIRICAL / SOURCE-REPORTED EVALUATION | The complete LAGEA framework achieves a near-perfect average success score outperforming other baselines in these experiments. | p. 7 (4.3.1. SYNERGY OF DELTA REWARDS AND ADAPTIVE) |
| 4. Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | RQ1: How much does VLM-guided feedback improve policy learning and task success? | p. 5 (4. Experiments) |

## Dataset / Benchmark Role

- **p. 5 / 4. Experiments - extractive PDF cue:** Setup: We evaluate LAGEA framework on ten robotics tasks from the Meta-world MT10 benchmark (Yu et al., 2020) and Robotic Fetch (Plappert et al., 2018), ...
- **p. 5 / 4. Experiments - extractive PDF cue:** We also include LIV (Ma et al., 2023), a robotics reward model pre-trained on large-scale datasets, and a variant, LIV-Proj, which utilizes randomly initialized and ...
- **p. 7 / 4.1.2. RESULTS ON FETCH TASKS - extractive PDF cue:** LAGEA: Language Guided Embodied Agents for Robotic Manipulation 0.0M 0.2M 0.4M 0.6M 0.8M 1.0M Environment Steps 0 20 40 60 80 100 Success Rate (%) ...
- **p. 8 / 4.3.1. SYNERGY OF DELTA REWARDS AND ADAPTIVE - extractive PDF cue:** LAGEA: Language Guided Embodied Agents for Robotic Manipulation 0.2M 0.3M 0.4M 0.5M 0.6M 0.7M 0.8M Environment Steps 12 10 8 6 4 2 Average Logit ...
- **p. 6 / 4. Experiments - extractive PDF cue:** Experiment results on MT10 benchmarks with fixed goal.
- **p. 6 / 4.1.2. RESULTS ON FETCH TASKS - extractive PDF cue:** We further evaluate LAGEA on the Robotic Fetch (Plappert et al., 2018) manipulation suite to assess its effectiveness in sparse-reward, goal-conditioned control.
- **p. 7 / 4.1.2. RESULTS ON FETCH TASKS - extractive PDF cue:** 0.0M 0.2M 0.4M 0.6M 0.8M 1.0M Environment Steps 400 200 0 200 400 VLM Reward VLM Reward Signal Over Training 0.0M 0.2M 0.4M 0.6M 0.8M ...
- **p. 8 / 4.3.3. IMPACT OF STRUCTURED FEEDBACK - extractive PDF cue:** Task Freeform Feedback Structured Feedback Button press topdown v2 obs.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 1. Overview of LAGEA framework. (a) After each rollout, key-frame selection identifies causal moments and computes per-step weights ˆwt; a VLM queried on those ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 2. The computation of our delta-based rewards. (a) A Goal Potential ϕt is formed by aligning the current state zt with the goal image ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 1. Experiment results on MT10 benchmarks with fixed goal. Average success rate across five random seeds. Environment SAC LIV LIV-Proj Relay FuRL w/o goal-image ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 2. Experiment results on MT10 benchmarks with random goal. We present the average success rate across five random seeds. Task SAC Relay FuRL LAGEA ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 3. Experiment results on Fetch manipulation suite. Average success rate (STD) across three different seeds; higher is better. VLM feedback for reinforcement learning. As ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 3. Natural-language feedback accelerates convergence: across eight Meta-World tasks, LAGEA reaches high success in far fewer steps than FuRL and SAC, which plateau late ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 4. Ablation studies on keyframe selection and reward shaping. and finally (5) viewpoint-shift experiment ( 4.3.5) to test ro- bustness to camera changes. Our ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 5. Alignment enables control-relevant geometry: (a) success/failure logit margin increases over training, (b) policy success accelerates, and (c) BCE/InfoNCE objectives co-train the shared space ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Setup: We evaluate LAGEA framework on ten robotics tasks from the Meta-world MT10 benchmark (Yu et al., 2020) and Robotic Fetch (Plappert et al., ... | embodiment, simulator version and control stack | p. 5 (4. Experiments), p. 5 (4. Experiments) |
| Task/environment | We also include LIV (Ma et al., 2023), a robotics reward model pre-trained on large-scale datasets, and a variant, LIV-Proj, which utilizes randomly initialized ... | reset, timeout, object/scene variation | p. 5 (4. Experiments), p. 7 (4.1.2. RESULTS ON FETCH TASKS) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 4 (3.2. Reward Generation), p. 4 (3.1.3. FEEDBACK ALIGNMENT) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 5 (3.2. Reward Generation), p. 1 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Table 8. Effect of different text encoders on observation-based manipulation tasks. Results are averaged over three random seeds (Standard Deviation is in brackets); higher ... | definition/direction/unit from same section | p. 15 (Figure/Table caption) |
| 0.0M 0.2M 0.4M 0.6M 0.8M 1.0M Environment Steps 400 200 0 200 400 VLM Reward VLM Reward Signal Over Training 0.0M 0.2M 0.4M 0.6M ... | definition/direction/unit from same section | p. 7 (4.1.2. RESULTS ON FETCH TASKS) |
| As shown in Table 1, LAGEA achieves a strong performance improvement of 5.3% over baselines, with an average success rate of 80% on hidden-fixed ... | definition/direction/unit from same section | p. 6 (4. Experiments) |
| Negative Logit (Unsuccessful States) Discrimination Gap (a) Logit Divergence Over Training 0.0M 0.1M 0.2M 0.3M 0.4M 0.5M 0.6M 0.7M 0.8M Environment Steps 0 10 ... | definition/direction/unit from same section | p. 8 (4.3.1. SYNERGY OF DELTA REWARDS AND ADAPTIVE) |
| As summarized in Table 3, we report the average success rate where LAGEA consistently outperforms all baselines across the four Fetch tasks. | definition/direction/unit from same section | p. 6 (4.1.2. RESULTS ON FETCH TASKS) |
| LAGEA: Language Guided Embodied Agents for Robotic Manipulation 0.0M 0.2M 0.4M 0.6M 0.8M 1.0M Environment Steps 0 20 40 60 80 100 Success Rate ... | definition/direction/unit from same section | p. 7 (4.1.2. RESULTS ON FETCH TASKS) |
| Consequently, the agent's success rate remains at zero (Figure 5b). | definition/direction/unit from same section | p. 8 (4.3.4. FEEDBACK-REWARD ALIGNMENT) |
| Baseline: To thoroughly evaluate LAGEA, we compare its performance against a suite of relevant reward learning baselines. | definition/direction/unit from same section | p. 5 (4. Experiments) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| As summarized in Table 3, we report the average success rate where LAGEA consistently outperforms all baselines across the four Fetch tasks. | comparison identity and matched condition | p. 6 (4.1.2. RESULTS ON FETCH TASKS) |
| The complete LAGEA framework achieves a near-perfect average success score outperforming other baselines in these experiments. | comparison identity and matched condition | p. 7 (4.3.1. SYNERGY OF DELTA REWARDS AND ADAPTIVE) |
| On average, our structured feedback approach outperforms the freeform feedback baseline. | comparison identity and matched condition | p. 8 (4.3.3. IMPACT OF STRUCTURED FEEDBACK) |
| Baseline: To thoroughly evaluate LAGEA, we compare its performance against a suite of relevant reward learning baselines. | comparison identity and matched condition | p. 5 (4. Experiments) |
| To further assess the benefits of exploration strategies, we incorporate Relay (Lan et al., 2023), a simplified approach that integrates relay RL into the ... | comparison identity and matched condition | p. 5 (4. Experiments) |
| In the observable-random goal setting (Table 2), LAGEA achieves a 70.4% average success rate, representing a 9% improvement over all baselines. | comparison identity and matched condition | p. 6 (4. Experiments) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 13. Failure case with structured feedback for door-open-v2-goal-observable task. K. Ablation To quantify the contribution of each component in LAGEA, we run controlled ... | component/input/data sensitivity | p. 21 (Figure/Table caption) |
| LAGEA with keyframing learns the task efficiently, while the variant without keyframing catastrophically fails. | component/input/data sensitivity | p. 8 (4.3.2. KEYFRAME EXTRACTION & CREDIT) |
| To validate our design choices and disentangle the individual contributions of our core components, we conduct a series of comprehensive ablation studies. | component/input/data sensitivity | p. 6 (4.1.2. RESULTS ON FETCH TASKS) |
| SHAPING To isolate the contributions of our key reward components, we performed a targeted ablation study on both observable random goal and hidden fixed ... | component/input/data sensitivity | p. 7 (4.3.1. SYNERGY OF DELTA REWARDS AND ADAPTIVE) |
| We also include LIV (Ma et al., 2023), a robotics reward model pre-trained on large-scale datasets, and a variant, LIV-Proj, which utilizes randomly initialized ... | component/input/data sensitivity | p. 5 (4. Experiments) |
| We evaluate LAGEA on a suite of simulated embodied manipulation tasks, comparing against baseline RL agents and ablated LAGEA variants to measure the contributions ... | component/input/data sensitivity | p. 5 (4. Experiments) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| For this purpose, we present our framework LAGEA, which addresses this by using VLMs to generate episodic natural-language reflections on a robot's 1 arXiv:2509.23155v3 ... | Table 8. Effect of different text encoders on observation-based manipulation tasks. Results are averaged over three random seeds (Standard Deviation is in brackets); higher ... | PDF body cue; verify exact table/figure and matched conditions | p. 15 (Figure/Table caption), p. 6 (4. Experiments), p. 6 (4. Experiments), p. 7 (4.3.1. SYNERGY OF DELTA REWARDS AND ADAPTIVE), p. 5 (4. Experiments), p. 7 (4.3.1. SYNERGY OF DELTA REWARDS AND ADAPTIVE) |
| Primary metric/result | As shown in Table 1, LAGEA achieves a strong performance improvement of 5.3% over baselines, with an average success rate of 80% on hidden-fixed ... | numeric claim only at cited anchor | p. 6 (4. Experiments) |

- Numeric sentences retained from the body:
- no numeric body cue

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 1. Overview of LAGEA framework. (a) After each rollout, key-frame selection identifies causal moments and computes per-step weights ˆwt; a VLM queried on ... | p. 3 (Figure/Table caption) |
| body limitation/failure cue | This accelerated learning is driven by the dense, corrective signals from our feedback mechanism, which fosters a more effective exploration process compared to the ... | p. 6 (4.1.2. RESULTS ON FETCH TASKS) |
| body limitation/failure cue | Alignment enables control-relevant geometry: (a) success/failure logit margin increases over training, (b) policy success accelerates, and (c) BCE/InfoNCE objectives co-train the shared space for ... | p. 8 (4.3.1. SYNERGY OF DELTA REWARDS AND ADAPTIVE) |
| body limitation/failure cue | Figure 9. Schema for structured feedback returned by the VLM Example structured feedback is shown for two Meta-World tasks - button-press-topdown-v2 and door-open-v2 - ... | p. 19 (Figure/Table caption) |
| body limitation/failure cue | Figure 11. Success case with structured feedback for door-open-v2-goal-observable task. high confidence, and suggested fix=(n/a). In button-press-topdown-v2, success is attributed to a secure grasp ... | p. 20 (Figure/Table caption) |
| body limitation/failure cue | Figure 13. Failure case with structured feedback for door-open-v2-goal-observable task. K. Ablation To quantify the contribution of each component in LAGEA, we run controlled ... | p. 21 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Implementation details are available in Appendix F. | p. 5 (4. Experiments) |
| LAGEA leverages Qwen-2.5-VL-3B for generating structured feedback, encoded with GPT-2. | p. 5 (4. Experiments) |
| Average success rate across five random seeds. | p. 6 (4. Experiments) |
| Average success rate (STD) across three different seeds; higher is better. | p. 6 (4. Experiments) |
| Natural-language feedback accelerates convergence: across eight Meta-World tasks, LAGEA reaches high success in far fewer steps than FuRL and SAC, which plateau late or ... | p. 7 (4.1.2. RESULTS ON FETCH TASKS) |
| 0.0M 0.2M 0.4M 0.6M 0.8M 1.0M Environment Steps 400 200 0 200 400 VLM Reward VLM Reward Signal Over Training 0.0M 0.2M 0.4M 0.6M ... | p. 7 (4.1.2. RESULTS ON FETCH TASKS) |
| Average performance of Freeform vs Structured Feedback across three different seeds. | p. 8 (4.3.3. IMPACT OF STRUCTURED FEEDBACK) |
| Comparison among randomly sampled, uniformly sampled, and LaGEA sampled keyframes for five Meta-World observable tasks on three random seeds. | p. 8 (4.3.1. SYNERGY OF DELTA REWARDS AND ADAPTIVE) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 1. Overview of LAGEA framework. (a) After each rollout, key-frame selection identifies causal moments and computes per-step weights ˆwt; a VLM queried on those ...
- **p. 6 / 4.1.2. RESULTS ON FETCH TASKS - extractive PDF cue:** This accelerated learning is driven by the dense, corrective signals from our feedback mechanism, which fosters a more effective exploration process compared to the slower, ...
- **p. 8 / 4.3.1. SYNERGY OF DELTA REWARDS AND ADAPTIVE - extractive PDF cue:** Alignment enables control-relevant geometry: (a) success/failure logit margin increases over training, (b) policy success accelerates, and (c) BCE/InfoNCE objectives co-train the shared space for LAGEA.
- **p. 19 / Figure/Table caption - extractive PDF cue:** Figure 9. Schema for structured feedback returned by the VLM Example structured feedback is shown for two Meta-World tasks - button-press-topdown-v2 and door-open-v2 - with ...
- **p. 20 / Figure/Table caption - extractive PDF cue:** Figure 11. Success case with structured feedback for door-open-v2-goal-observable task. high confidence, and suggested fix=(n/a). In button-press-topdown-v2, success is attributed to a secure grasp followed ...
- **p. 21 / Figure/Table caption - extractive PDF cue:** Figure 13. Failure case with structured feedback for door-open-v2-goal-observable task. K. Ablation To quantify the contribution of each component in LAGEA, we run controlled ablations ...

- **PDF anchors reviewed:** datasets p. 5 (4. Experiments), p. 5 (4. Experiments), p. 7 (4.1.2. RESULTS ON FETCH TASKS), p. 8 (4.3.1. SYNERGY OF DELTA REWARDS AND ADAPTIVE), p. 6 (4. Experiments), p. 6 (4.1.2. RESULTS ON FETCH TASKS), metrics p. 15 (Figure/Table caption), p. 7 (4.1.2. RESULTS ON FETCH TASKS), p. 6 (4. Experiments), p. 8 (4.3.1. SYNERGY OF DELTA REWARDS AND ADAPTIVE), p. 6 (4.1.2. RESULTS ON FETCH TASKS), p. 7 (4.1.2. RESULTS ON FETCH TASKS), baselines p. 6 (4.1.2. RESULTS ON FETCH TASKS), p. 7 (4.3.1. SYNERGY OF DELTA REWARDS AND ADAPTIVE), p. 8 (4.3.3. IMPACT OF STRUCTURED FEEDBACK), p. 5 (4. Experiments), p. 5 (4. Experiments), p. 6 (4. Experiments), results p. 15 (Figure/Table caption), p. 6 (4. Experiments), p. 6 (4. Experiments), p. 7 (4.3.1. SYNERGY OF DELTA REWARDS AND ADAPTIVE), p. 5 (4. Experiments), p. 7 (4.3.1. SYNERGY OF DELTA REWARDS AND ADAPTIVE).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
