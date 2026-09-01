# Evaluation - SemanticVLA: Towards Semantic Reasoning over Action Memorization via Synergistic Explicit Trace and Latent Action Planning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Ni_SemanticVLA_Towards_Semantic_Reasoning_over_Action_Memorization_via_Synergistic_Explicit_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Ni_SemanticVLA_Towards_Semantic_Reasoning_over_Action_Memorization_via_Synergistic_Explicit_CVPR_2026_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (4.1. Simulation Benchmarks), p. 6 (4.1. Simulation Benchmarks), p. 7 (4.3. Instruction Variance Robustness), p. 8 (4.4. Explicit Trace-Guided Latent Action Learning), p. 8 (Figure/Table caption), p. 1 (Figure/Table caption)): As shown in Table 1, SemanticVLA achieves 97.0% average success rate, outperforming strong baselines across task categories.

## Evaluation Body Digest

- **p. 5 / 4. Experiments - extractive PDF cue:** Our experiments validate three core properties: Effectiveness (Section 4.1, 4.2) competitive task success rates on simulation benchmarks and real-world deployments; Robustness (Section 4.3) stable performance ...
- **p. 6 / 4.1. Simulation Benchmarks - extractive PDF cue:** We evaluate on the WidowX manipulation suite, training on Bridge dataset demonstrations and testing across four tasks with controlled visual variations over 24 episodes each.
- **p. 6 / 4.2. Real-world Robotics Evaluation - extractive PDF cue:** We further conduct real-world experiments using a Franka Research 3 robot arm with Franka hand and two Intel RealSense D435 cameras.
- **p. 7 / 4.3. Instruction Variance Robustness - extractive PDF cue:** The evaluation settings include paraphrased variants with appearance-based references such as "orange object" instead of "carrot", negation phrases like "not the towel", and commonsense cues ...
- **p. 8 / 4.5. Latent Tokens Stabilize Trace Execution - extractive PDF cue:** We evaluate on real-world Franka manipulation under three generalization axes: visual shifts, task variations, and language rephrasing.
- **p. 8 / 4.5. Latent Tokens Stabilize Trace Execution - extractive PDF cue:** Real-world generalization evaluations under visual perturbation, instruction rephrasing, and task variation. tent action planning achieves 48% on language rephrasing compared to MolmoAct's 33%, directly validating ...
- **p. 7 / 4.3. Instruction Variance Robustness - extractive PDF cue:** Performance on LIBERO and SimplerEnv benchmarks under instruction variations.
- **p. 8 / 4.4. Explicit Trace-Guided Latent Action Learning - extractive PDF cue:** Solid lines: success rate (right yaxis); Dashed lines: latent prediction accuracy (left y-axis). training.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 4. Experiments (p. 5); 4.1. Simulation Benchmarks (p. 6); 4.2. Real-world Robotics Evaluation (p. 6).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.1. Simulation Benchmarks | EMPIRICAL / REAL-ROBOT OR HARDWARE | As shown in Table 1, SemanticVLA achieves 97.0% average success rate, outperforming strong baselines across task categories. | p. 6 (4.1. Simulation Benchmarks) |
| 4.1. Simulation Benchmarks | EMPIRICAL / REAL-ROBOT OR HARDWARE | SemanticVLA achieves 65.1% average success rate, outperforming competitive baselines and demonstrating effective transfer of trace-guided spatial understanding across manipulation primitives. | p. 6 (4.1. Simulation Benchmarks) |
| 4.3. Instruction Variance Robustness | EMPIRICAL / REAL-ROBOT OR HARDWARE | Dashed bars: success rates with original instructions; Solid bars: rephrased instructions with similar task semantics. across perturbations, only 9.4% on LIBERO and significantly outperforming ... | p. 7 (4.3. Instruction Variance Robustness) |
| 4.4. Explicit Trace-Guided Latent Action Learning | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our tokens achieve substantially higher accuracy and success rates, with gaps exceeding 12%, demonstrating that trace supervision during pretraining imbues latent embeddings with richer ... | p. 8 (4.4. Explicit Trace-Guided Latent Action Learning) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 6. The analysis of latent learning. Training curves on LIBERO instruction rephrasing. Solid lines: success rate (right y- axis); Dashed lines: latent prediction ... | p. 8 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 5 / 4. Experiments - extractive PDF cue:** Our experiments validate three core properties: Effectiveness (Section 4.1, 4.2) competitive task success rates on simulation benchmarks and real-world deployments; Robustness (Section 4.3) stable performance ...
- **p. 6 / 4.1. Simulation Benchmarks - extractive PDF cue:** We evaluate on the WidowX manipulation suite, training on Bridge dataset demonstrations and testing across four tasks with controlled visual variations over 24 episodes each.
- **p. 6 / 4.2. Real-world Robotics Evaluation - extractive PDF cue:** We further conduct real-world experiments using a Franka Research 3 robot arm with Franka hand and two Intel RealSense D435 cameras.
- **p. 7 / 4.3. Instruction Variance Robustness - extractive PDF cue:** The evaluation settings include paraphrased variants with appearance-based references such as "orange object" instead of "carrot", negation phrases like "not the towel", and commonsense cues ...
- **p. 8 / 4.5. Latent Tokens Stabilize Trace Execution - extractive PDF cue:** We evaluate on real-world Franka manipulation under three generalization axes: visual shifts, task variations, and language rephrasing.
- **p. 8 / 4.5. Latent Tokens Stabilize Trace Execution - extractive PDF cue:** Real-world generalization evaluations under visual perturbation, instruction rephrasing, and task variation. tent action planning achieves 48% on language rephrasing compared to MolmoAct's 33%, directly validating ...
- **p. 7 / 4.3. Instruction Variance Robustness - extractive PDF cue:** Performance on LIBERO and SimplerEnv benchmarks under instruction variations.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. SemanticVLA Overview. Current VLA models struggle with instruction variations and reasoning-intensive tasks, often mem- orizing patterns rather than understanding semantics. We introduce a ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2. Semantic Latent Action Tokenizer. Two-stage archi- tecture for trace-guided latent tokens. Stage 1 learns geometric patterns from traces. Stage 2 grounds them in ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 3. SemanticVLA Architecture Overview. Our dual-path framework synergistically combines explicit trace reasoning and implicit latent action planning. The VLM processes visual observations and language ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 1. Performance comparison on LIBERO and SimplerEnv. Underlined scores show best results excluding SemanticVLA. Models LIBERO (Franka) benchmark WidowX benchmark in SimplerEnv Spatial Objects ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 4. Real-world robot experiments. We evaluate SemanticVLA on long-horizon compositional tasks (food preparing and desktop sorting) and reasoning-intensive tasks (math calculation and word spelling), ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 2. Success rate evaluation in real robot experiments in long-horizon and reasoning scenarios. Models Long-horizon tasks Reasoning tasks Avg Food Preparing
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 5. Instruction Rephrasing Robustness. Performance on LIBERO and SimplerEnv benchmarks under instruction vari- ations. Dashed bars: success rates with original instructions; Solid bars: rephrased ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 6. The analysis of latent learning. Training curves on LIBERO instruction rephrasing. Solid lines: success rate (right y- axis); Dashed lines: latent prediction accuracy ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Our experiments validate three core properties: Effectiveness (Section 4.1, 4.2) competitive task success rates on simulation benchmarks and real-world deployments; Robustness (Section 4.3) stable ... | embodiment, simulator version and control stack | p. 5 (4. Experiments), p. 6 (4.1. Simulation Benchmarks) |
| Task/environment | We evaluate on the WidowX manipulation suite, training on Bridge dataset demonstrations and testing across four tasks with controlled visual variations over 24 episodes ... | reset, timeout, object/scene variation | p. 6 (4.1. Simulation Benchmarks), p. 6 (4.2. Real-world Robotics Evaluation) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 5 (3.3. Flow Matching Action Decoding), p. 5 (3.3. Flow Matching Action Decoding) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 4 (3.2. VLM Co-training with Trace and Latent Action), p. 4 (3.1. Semantic Latent Action Tokenizer) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Solid lines: success rate (right yaxis); Dashed lines: latent prediction accuracy (left y-axis). training. | definition/direction/unit from same section | p. 8 (4.4. Explicit Trace-Guided Latent Action Learning) |
| Our tokens achieve substantially higher accuracy and success rates, with gaps exceeding 12%, demonstrating that trace supervision during pretraining imbues latent embeddings with richer ... | definition/direction/unit from same section | p. 8 (4.4. Explicit Trace-Guided Latent Action Learning) |
| Our experiments validate three core properties: Effectiveness (Section 4.1, 4.2) competitive task success rates on simulation benchmarks and real-world deployments; Robustness (Section 4.3) stable ... | definition/direction/unit from same section | p. 5 (4. Experiments) |
| Figure 5. Instruction Rephrasing Robustness. Performance on LIBERO and SimplerEnv benchmarks under instruction vari- ations. Dashed bars: success rates with original instructions; Solid bars: ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Figure 1. SemanticVLA Overview. Current VLA models struggle with instruction variations and reasoning-intensive tasks, often mem- orizing patterns rather than understanding semantics. We introduce ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| As shown in Table 1, SemanticVLA achieves 97.0% average success rate, outperforming strong baselines across task categories. | definition/direction/unit from same section | p. 6 (4.1. Simulation Benchmarks) |
| SemanticVLA achieves 65.1% average success rate, outperforming competitive baselines and demonstrating effective transfer of trace-guided spatial understanding across manipulation primitives. | definition/direction/unit from same section | p. 6 (4.1. Simulation Benchmarks) |
| Success rate evaluation in real robot experiments in long-horizon and reasoning scenarios. | definition/direction/unit from same section | p. 7 (4.2. Real-world Robotics Evaluation) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| As shown in Table 1, SemanticVLA achieves 97.0% average success rate, outperforming strong baselines across task categories. | comparison identity and matched condition | p. 6 (4.1. Simulation Benchmarks) |
| SemanticVLA achieves 65.1% average success rate, outperforming competitive baselines and demonstrating effective transfer of trace-guided spatial understanding across manipulation primitives. | comparison identity and matched condition | p. 6 (4.1. Simulation Benchmarks) |
| Dashed bars: success rates with original instructions; Solid bars: rephrased instructions with similar task semantics. across perturbations, only 9.4% on LIBERO and significantly outperforming ... | comparison identity and matched condition | p. 7 (4.3. Instruction Variance Robustness) |
| As shown in Figure 7, SemanticVLA substantially outperforms all baselines across all generalization types. | comparison identity and matched condition | p. 8 (4.5. Latent Tokens Stabilize Trace Execution) |
| Baselines show substantial brittleness under rephrasing, with OpenVLA degrading by 18.4% and UniVLA by 23.9%. | comparison identity and matched condition | p. 7 (4.3. Instruction Variance Robustness) |
| We compare against trace-only baselines including TraceVLA with visual overlay, HAMSTER with direct trace conditioning, and MolmoAct with trace reasoning plus raw action tokens. | comparison identity and matched condition | p. 8 (4.5. Latent Tokens Stabilize Trace Execution) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| More critically, to isolate the effect of trace-guided pretraining, we conduct a controlled ablation comparing our latent tokens against UniVLA's-both trained without explicit trace ... | component/input/data sensitivity | p. 8 (4.4. Explicit Trace-Guided Latent Action Learning) |
| To validate that trace guidance produces semanticallygrounded latent tokens beyond architectural benefits, we conduct ablations on LIBERO instruction rephrasing with three variants: SemanticVLA with ... | component/input/data sensitivity | p. 7 (4.4. Explicit Trace-Guided Latent Action Learning) |
| Our ablation without laVisual 58 14 Task Language Success Rate (%) 56 53 29 35 51 11 30 33 48 8 27 29 46 ... | component/input/data sensitivity | p. 8 (4.5. Latent Tokens Stabilize Trace Execution) |
| We evaluate two complementary categories with 20 rollouts per task across 5 variants that vary objects, positions and scene layouts. | component/input/data sensitivity | p. 6 (4.2. Real-world Robotics Evaluation) |
| The evaluation settings include paraphrased variants with appearance-based references such as "orange object" instead of "carrot", negation phrases like "not the towel", and commonsense ... | component/input/data sensitivity | p. 7 (4.3. Instruction Variance Robustness) |
| Our trace-guided latent pretraining provides explicit spatial semantics beyond UniVLA and VQ-VLA, whose latents lack geometric scaffolding and rely solely on visual reconstruction or ... | component/input/data sensitivity | p. 6 (4.1. Simulation Benchmarks) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our approach consists of three stages: (1) Semantic Latent Token Pretraining (Sec. | As shown in Table 1, SemanticVLA achieves 97.0% average success rate, outperforming strong baselines across task categories. | PDF body cue; verify exact table/figure and matched conditions | p. 6 (4.1. Simulation Benchmarks), p. 6 (4.1. Simulation Benchmarks), p. 7 (4.3. Instruction Variance Robustness), p. 8 (4.4. Explicit Trace-Guided Latent Action Learning), p. 8 (Figure/Table caption), p. 1 (Figure/Table caption) |
| Primary metric/result | SemanticVLA achieves 65.1% average success rate, outperforming competitive baselines and demonstrating effective transfer of trace-guided spatial understanding across manipulation primitives. | numeric claim only at cited anchor | p. 6 (4.1. Simulation Benchmarks) |

- Numeric sentences retained from the body:
- **p. 6 / 4.1. Simulation Benchmarks - extractive PDF cue:** Following established protocols [27], we finetune independently per suite on 16 H200 GPUs for 30K steps with batch size 128 and action chunk size 12, ...
- **p. 6 / 4.1. Simulation Benchmarks - extractive PDF cue:** We evaluate on the WidowX manipulation suite, training on Bridge dataset demonstrations and testing across four tasks with controlled visual variations over 24 episodes each.
- **p. 6 / 4.2. Real-world Robotics Evaluation - extractive PDF cue:** We further conduct real-world experiments using a Franka Research 3 robot arm with Franka hand and two Intel RealSense D435 cameras.
- **p. 6 / 4.2. Real-world Robotics Evaluation - extractive PDF cue:** The model runs on a single NVIDIA RTX 3090 GPU achieving realtime control.
- **p. 6 / 4.2. Real-world Robotics Evaluation - extractive PDF cue:** We evaluate two complementary categories with 20 rollouts per task across 5 variants that vary objects, positions and scene layouts.
- **p. 8 / 4.4. Explicit Trace-Guided Latent Action Learning - extractive PDF cue:** 5 10 15 20 25 30 Training Steps (k) 40 50 60 70 80 90 100 Latent Token Prediction Accuracy (%) SemanticVLA (SR) w/o Trace ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 1. SemanticVLA Overview. Current VLA models struggle with instruction variations and reasoning-intensive tasks, often mem- orizing patterns rather than understanding semantics. We introduce ... | p. 1 (Figure/Table caption) |
| body limitation/failure cue | We believe this synergistic fusion of explicit trace and latent action tokens pathways provides a promising and principled approach to designing more effective VLA ... | p. 8 (5. Conclusion) |
| body limitation/failure cue | Our experiments validate three core properties: Effectiveness (Section 4.1, 4.2) competitive task success rates on simulation benchmarks and real-world deployments; Robustness (Section 4.3) stable ... | p. 5 (4. Experiments) |
| body limitation/failure cue | Figure 3. SemanticVLA Architecture Overview. Our dual-path framework synergistically combines explicit trace reasoning and implicit latent action planning. The VLM processes visual observations and ... | p. 5 (Figure/Table caption) |
| body limitation/failure cue | SimplerEnv [32] probes cross-domain robustness through visual appearance shifts on short-horizon WidowX tasks. | p. 6 (4.1. Simulation Benchmarks) |
| body limitation/failure cue | Reasoningenhanced approaches such as ThinkAct, MolmoAct, and Magma substantially outperform direct action prediction models including OpenVLA and RT-1-X, confirming the importance of structured reasoning ... | p. 6 (4.1. Simulation Benchmarks) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Following established protocols [27], we finetune independently per suite on 16 H200 GPUs for 30K steps with batch size 128 and action chunk size ... | p. 6 (4.1. Simulation Benchmarks) |
| In Stage 1, we pretrain the semantic latent action tokenizer on TraceX-240K for 50K steps with batch size 512, learning clean geometric primitives without ... | p. 5 (3.4. Training Recipe) |
| In Stage 2, we co-train the VLM to jointly predict trace coordinates and latent action tokens on the same dataset for 100K steps with ... | p. 5 (3.4. Training Recipe) |
| To enable latent action prediction, we augment the VLM vocabulary with special tokens {ACT_1, ..., ACT_K} indexing into the pretrained codebook from Section 3.1. | p. 4 (3.2. VLM Co-training with Trace and Latent Action) |
| Trace provides explicit spatial targets that guide the VLM's spatial reasoning, while latent tokens encode visuallygrounded primitives that fuse geometric patterns with scene-specific observations. | p. 4 (3.2. VLM Co-training with Trace and Latent Action) |
| The model runs on a single NVIDIA RTX 3090 GPU achieving realtime control. | p. 6 (4.2. Real-world Robotics Evaluation) |
| Compared to MolmoAct which expands vocabulary with raw action tokens, our latent interface maintains modality separation and enables stable decoding through the flow matching ... | p. 7 (4.2. Real-world Robotics Evaluation) |
| The geometric scaffolding from trace sequences acts as a strong inductive bias, filtering task-irrelevant variations and forcing the codebook to capture true manipulation semantics. | p. 8 (4.4. Explicit Trace-Guided Latent Action Learning) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. SemanticVLA Overview. Current VLA models struggle with instruction variations and reasoning-intensive tasks, often mem- orizing patterns rather than understanding semantics. We introduce a ...
- **p. 8 / 5. Conclusion - extractive PDF cue:** We believe this synergistic fusion of explicit trace and latent action tokens pathways provides a promising and principled approach to designing more effective VLA architectures ...
- **p. 5 / 4. Experiments - extractive PDF cue:** Our experiments validate three core properties: Effectiveness (Section 4.1, 4.2) competitive task success rates on simulation benchmarks and real-world deployments; Robustness (Section 4.3) stable performance ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 3. SemanticVLA Architecture Overview. Our dual-path framework synergistically combines explicit trace reasoning and implicit latent action planning. The VLM processes visual observations and language ...
- **p. 6 / 4.1. Simulation Benchmarks - extractive PDF cue:** SimplerEnv [32] probes cross-domain robustness through visual appearance shifts on short-horizon WidowX tasks.
- **p. 6 / 4.1. Simulation Benchmarks - extractive PDF cue:** Reasoningenhanced approaches such as ThinkAct, MolmoAct, and Magma substantially outperform direct action prediction models including OpenVLA and RT-1-X, confirming the importance of structured reasoning for ...

- **PDF anchors reviewed:** datasets p. 5 (4. Experiments), p. 6 (4.1. Simulation Benchmarks), p. 6 (4.2. Real-world Robotics Evaluation), p. 7 (4.3. Instruction Variance Robustness), p. 8 (4.5. Latent Tokens Stabilize Trace Execution), p. 8 (4.5. Latent Tokens Stabilize Trace Execution), metrics p. 8 (4.4. Explicit Trace-Guided Latent Action Learning), p. 8 (4.4. Explicit Trace-Guided Latent Action Learning), p. 5 (4. Experiments), p. 7 (Figure/Table caption), p. 1 (Figure/Table caption), p. 6 (4.1. Simulation Benchmarks), baselines p. 6 (4.1. Simulation Benchmarks), p. 6 (4.1. Simulation Benchmarks), p. 7 (4.3. Instruction Variance Robustness), p. 8 (4.5. Latent Tokens Stabilize Trace Execution), p. 7 (4.3. Instruction Variance Robustness), p. 8 (4.5. Latent Tokens Stabilize Trace Execution), results p. 6 (4.1. Simulation Benchmarks), p. 6 (4.1. Simulation Benchmarks), p. 7 (4.3. Instruction Variance Robustness), p. 8 (4.4. Explicit Trace-Guided Latent Action Learning), p. 8 (Figure/Table caption), p. 1 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
