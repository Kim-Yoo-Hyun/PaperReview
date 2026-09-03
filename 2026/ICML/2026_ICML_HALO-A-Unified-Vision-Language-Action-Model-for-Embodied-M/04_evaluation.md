# Evaluation - HALO: A Unified Vision-Language-Action Model for Embodied Multimodal Chain-of-Thought Reasoning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=lduY9csXqw; PDF retrieval source: https://openreview.net/pdf/f0a4b4b3d1775cb04d6e602c68bf3c4914033562.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (4.5. Real-World Results), p. 6 (4. Experiments), p. 7 (4.2. Simulation Results), p. 7 (4.2. Simulation Results), p. 8 (4.3. Ablation Study), p. 6 (Figure/Table caption)): While the baselines suffer noticeable performance degradation in the presence of visual distractions, lighting and background variations, and novel objects, HALO remains robust and achieves the highest success rates across ...

## Evaluation Body Digest

- **p. 7 / 4.1. Experiment Settings - extractive body cue:** The simulation dataset contains 2,500 expert demonstrations (50 per task) collected in clean environments, while the real-world dataset consists of 320 demonstrations (80 per task).
- **p. 7 / 4.2. Simulation Results - extractive body cue:** We conduct simulation experiments on RoboTwin 2.0 (Chen et al., 2025c), a comprehensive benchmark comprising 50 challenging manipulation tasks.
- **p. 6 / 4. Experiments - extractive body cue:** Our study focuses on: (i) whether the proposed unified VLA architecture with EM-CoT improves overall performance and generalization; (ii) whether HALO can generate informative EM-CoT ...
- **p. 8 / 4.5. Real-World Results - extractive body cue:** We further evaluate HALO on a real-world Cobot Mobile ALOHA platform on four long-horizon manipulation tasks, including tool-use sweeping, bimanual cup nesting, inter-arm screwdriver handover, ...
- **p. 16 / C. Training Implementation - extractive body cue:** Complete Result on RoboTwin2.0 Benchmark See Table 5 for complete result on RoboTwin 2.0 benchmark.
- **p. 16 / C. Training Implementation - extractive body cue:** Details on Real-World Experiment Our real-world experiments are all conducted with COBOT Magic, a robot using the Mobile ALOHA system design (Fu et al., 2024) ...
- **p. 8 / 4.5. Real-World Results - extractive body cue:** These tasks require multi-step planning, semantic grounding, and coordinated dual-arm control skills, making them valuable for evaluating the effectiveness of EM-CoT reasoning in real-world settings.
- **p. 8 / 4.5. Real-World Results - extractive body cue:** While the baselines suffer noticeable performance degradation in the presence of visual distractions, lighting and background variations, and novel objects, HALO remains robust and achieves ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 4. Experiments (p. 6); 4.1. Experiment Settings (p. 7); 4.2. Simulation Results (p. 7); 4.4. Qualitative Results of EM-CoT (p. 8); 4.5. Real-World Results (p. 8); C. Training Implementation (p. 16).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4.5. Real-World Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | While the baselines suffer noticeable performance degradation in the presence of visual distractions, lighting and background variations, and novel objects, HALO remains robust and ... | p. 8 (4.5. Real-World Results) |
| 4. Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our study focuses on: (i) whether the proposed unified VLA architecture with EM-CoT improves overall performance and generalization; (ii) whether HALO can generate informative ... | p. 6 (4. Experiments) |
| 4.2. Simulation Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | On fine-grained tasks such as "Blocks Ranking Size" and "Stamp Seal," HALO achieves a multi-fold increase in success rates compared to baselines, demonstrating its ... | p. 7 (4.2. Simulation Results) |
| 4.2. Simulation Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | While π0 and RDT-1B exhibit some degree of robustness, they plateau at significantly lower performance levels, whereas HALO continues to improve as it incorporates ... | p. 7 (4.2. Simulation Results) |
| 4.3. Ablation Study | EMPIRICAL / REAL-ROBOT OR HARDWARE | Combining both reasoning modalities in HALO achieves the highest accuracy, particularly on hard tasks. | p. 8 (4.3. Ablation Study) |

## Dataset / Benchmark Role

- **p. 7 / 4.1. Experiment Settings - extractive body cue:** The simulation dataset contains 2,500 expert demonstrations (50 per task) collected in clean environments, while the real-world dataset consists of 320 demonstrations (80 per task).
- **p. 7 / 4.2. Simulation Results - extractive body cue:** We conduct simulation experiments on RoboTwin 2.0 (Chen et al., 2025c), a comprehensive benchmark comprising 50 challenging manipulation tasks.
- **p. 6 / 4. Experiments - extractive body cue:** Our study focuses on: (i) whether the proposed unified VLA architecture with EM-CoT improves overall performance and generalization; (ii) whether HALO can generate informative EM-CoT ...
- **p. 8 / 4.5. Real-World Results - extractive body cue:** We further evaluate HALO on a real-world Cobot Mobile ALOHA platform on four long-horizon manipulation tasks, including tool-use sweeping, bimanual cup nesting, inter-arm screwdriver handover, ...
- **p. 16 / C. Training Implementation - extractive body cue:** Complete Result on RoboTwin2.0 Benchmark See Table 5 for complete result on RoboTwin 2.0 benchmark.
- **p. 16 / C. Training Implementation - extractive body cue:** Details on Real-World Experiment Our real-world experiments are all conducted with COBOT Magic, a robot using the Mobile ALOHA system design (Fu et al., 2024) ...
- **p. 8 / 4.5. Real-World Results - extractive body cue:** These tasks require multi-step planning, semantic grounding, and coordinated dual-arm control skills, making them valuable for evaluating the effectiveness of EM-CoT reasoning in real-world settings.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1. HALO first performs textual reasoning and task planning, then predicts visual subgoals for fine-grained guidance, and finally generates actions conditioned on EM-CoT. This ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 2. Overview of EM-CoT Data Synthesis Pipeline. The pipeline converts raw robotic trajectories into EM-CoT data in three phases: (1) action primitives are extracted ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3. Attention Masking Strategy for EM-CoT. (1) Spa- tial and semantic tokens utilize bidirectional attention within frames. (2) Noise tokens attend bidirectionally to each ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 4. Overview of dataset recipe. HALO training involves two stages: Stage 1 pre-trains on general VQA, visual generation, and action prediction to build foundation ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Quantitative results in simulation on RoboTwin 2.0. Each task is evaluated 100 times under the Easy (Clean) and Hard (Domain- randomized) settings, and ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2. Ablation studies on training recipe and EM-CoT. Panel A: training recipe ablation (V/T/A denote visual generation, textual VQA, and action prediction data. Note ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5. Qualitative Analysis of the EM-CoT. We highlight (i) accurate textual reasoning and subgoal image generation in the clean setting, and (ii) robust EM-CoT ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 6. Real-World Task Settings. (a) Basic Setting: Four tasks, including tool-use sweeping, bimanual cup nesting, inter- arm screwdriver handover, and placing an object into ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The simulation dataset contains 2,500 expert demonstrations (50 per task) collected in clean environments, while the real-world dataset consists of 320 demonstrations (80 per ... | embodiment, simulator version and control stack | p. 7 (4.1. Experiment Settings), p. 7 (4.2. Simulation Results) |
| Task/environment | We conduct simulation experiments on RoboTwin 2.0 (Chen et al., 2025c), a comprehensive benchmark comprising 50 challenging manipulation tasks. | reset, timeout, object/scene variation | p. 7 (4.2. Simulation Results), p. 6 (4. Experiments) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 3 (3.1. Problem Formulation), p. 3 (3.1. Problem Formulation) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 5 (3.3. EM-CoT Data Pipeline), p. 2 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| While the baselines suffer noticeable performance degradation in the presence of visual distractions, lighting and background variations, and novel objects, HALO remains robust and ... | definition/direction/unit from same section | p. 8 (4.5. Real-World Results) |
| The average success rate of HALO reaches 80.46% on Easy tasks and 26.44% on Hard tasks, surpassing baseline policy π0 by 34.1% and 10.1%, ... | definition/direction/unit from same section | p. 7 (4.2. Simulation Results) |
| In contrast, traditional reactive policies such as Diffusion Policy struggle significantly in randomized environments, with success rates dropping to near-zero (0.6%) in Hard settings. | definition/direction/unit from same section | p. 7 (4.2. Simulation Results) |
| Table 1. Quantitative results in simulation on RoboTwin 2.0. Each task is evaluated 100 times under the Easy (Clean) and Hard (Domain- randomized) settings, ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| Figure 7. Quantitative results of real-world experiments on both the basic setting and the generalization setting. Each task is evaluated over 50 trials, and ... | definition/direction/unit from same section | p. 9 (Figure/Table caption) |
| Combining both reasoning modalities in HALO achieves the highest accuracy, particularly on hard tasks. | definition/direction/unit from same section | p. 8 (4.3. Ablation Study) |
| Our study focuses on: (i) whether the proposed unified VLA architecture with EM-CoT improves overall performance and generalization; (ii) whether HALO can generate informative ... | definition/direction/unit from same section | p. 6 (4. Experiments) |
| Configuration Pre-training Fine-tuning Base Architecture Qwen2.5-1.5B × 3 Experts Total Parameters ≈4.5B Optimizer AdamW Learning Rate 1 × 10-4 5 × 10-5 Learning Rate ... | definition/direction/unit from same section | p. 16 (C. Training Implementation) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| It can be observed that HALO consistently outperforms all competitive baselines across both Easy and Hard settings. | comparison identity and matched condition | p. 7 (4.2. Simulation Results) |
| On fine-grained tasks such as "Blocks Ranking Size" and "Stamp Seal," HALO achieves a multi-fold increase in success rates compared to baselines, demonstrating its ... | comparison identity and matched condition | p. 7 (4.2. Simulation Results) |
| As shown in Figure 7, HALO consistently outperforms the baseline policies π0 and π0.5 under both the basic and generalization settings. | comparison identity and matched condition | p. 8 (4.5. Real-World Results) |
| Our study focuses on: (i) whether the proposed unified VLA architecture with EM-CoT improves overall performance and generalization; (ii) whether HALO can generate informative ... | comparison identity and matched condition | p. 6 (4. Experiments) |
| While the baselines suffer noticeable performance degradation in the presence of visual distractions, lighting and background variations, and novel objects, HALO remains robust and ... | comparison identity and matched condition | p. 8 (4.5. Real-World Results) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We perform ablation studies to validate the effectiveness of HALO's mechanism design, including the versatile pre-training and the EM-CoT-augmented Fine-tuning. | component/input/data sensitivity | p. 7 (4.3. Ablation Study) |
| Baseline results are taken directly from the official RoboTwin 2.0 leaderboard.1 To isolate the contribution of EM-CoT, we further include a variant of our ... | component/input/data sensitivity | p. 7 (4.2. Simulation Results) |
| Notably, without any pre-training (w/o V+T+A), the model's performance falls to a complete 0% on hard tasks, demonstrating that pre-training is an absolutely foundational ... | component/input/data sensitivity | p. 8 (4.3. Ablation Study) |
| As shown in Panel B, both visual subgoal images and textual reasoning are crucial components for EM-CoT, removing either component degrades performance. | component/input/data sensitivity | p. 8 (4.3. Ablation Study) |
| Figure 4. Overview of dataset recipe. HALO training involves two stages: Stage 1 pre-trains on general VQA, visual generation, and action prediction to build ... | component/input/data sensitivity | p. 5 (Figure/Table caption) |
| In this section, we provide details on pre-training and fine-tuning of HALO. | component/input/data sensitivity | p. 16 (C. Training Implementation) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To address this, we propose HALO, a unified VLA model that enables embodied multimodal chain-of-thought (EM-CoT) reasoning. | While the baselines suffer noticeable performance degradation in the presence of visual distractions, lighting and background variations, and novel objects, HALO remains robust and ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (4.5. Real-World Results), p. 6 (4. Experiments), p. 7 (4.2. Simulation Results), p. 7 (4.2. Simulation Results), p. 8 (4.3. Ablation Study), p. 6 (Figure/Table caption) |
| Primary metric/result | Our study focuses on: (i) whether the proposed unified VLA architecture with EM-CoT improves overall performance and generalization; (ii) whether HALO can generate informative ... | numeric claim only at cited anchor | p. 6 (4. Experiments) |

- Numeric sentences retained from the body:
- **p. 7 / 4.2. Simulation Results - extractive body cue:** Besides, even without the explicit reasoning chain, HALO-w/o EM-CoT already surpasses the strongest baseline (π0) by a substantial margin of +28.92 points on average for ...
- **p. 16 / C. Training Implementation - extractive body cue:** ("Put lemon into drawer") We collect 80 trajectories for each task, and process them through our automated pipeline to yield the EM-CoT data.
- **p. 6 / 3.4. Training Recipe - extractive body cue:** Each task is evaluated 100 times under the Easy (Clean) and Hard (Domainrandomized) settings, and the average success rate across 50 tasks is reported.
- **p. 16 / C. Training Implementation - extractive body cue:** ("Put lemon into drawer") We collect 80 trajectories for each task, and process them through our automated pipeline to yield the EM-CoT data.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Notably, without any pre-training (w/o V+T+A), the model's performance falls to a complete 0% on hard tasks, demonstrating that pre-training is an absolutely foundational ... | p. 8 (4.3. Ablation Study) |
| body limitation/failure cue | Particularly, the consistent huge relative performance gap (i.e., 73.5% and 62.0%) between HALO and π0 especially on Hard tasks indicates that HALO can also ... | p. 7 (4.2. Simulation Results) |
| body limitation/failure cue | While the baselines suffer noticeable performance degradation in the presence of visual distractions, lighting and background variations, and novel objects, HALO remains robust and ... | p. 8 (4.5. Real-World Results) |
| body limitation/failure cue | Figure 3. Attention Masking Strategy for EM-CoT. (1) Spa- tial and semantic tokens utilize bidirectional attention within frames. (2) Noise tokens attend bidirectionally to ... | p. 5 (Figure/Table caption) |
| body limitation/failure cue | These results underscore the effectiveness and robustness of HALO for complex robotic manipulation. | p. 7 (4.2. Simulation Results) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Configuration Pre-training Fine-tuning Base Architecture Qwen2.5-1.5B × 3 Experts Total Parameters ≈4.5B Optimizer AdamW Learning Rate 1 × 10-4 5 × 10-5 Learning Rate ... | p. 16 (C. Training Implementation) |
| Please refer to Appendix C for implementation details. | p. 6 (3.4. Training Recipe) |
| Using these datasets, HALO is fine-tuned for 110k steps in simulation and 80k steps in real-world experiments. | p. 7 (4.1. Experiment Settings) |
| During pre-training, following (Deng et al., 2025), training samples are concatenated to a maximum sequence length of 27k tokens, and Flex Attention (Dong et ... | p. 7 (4.1. Experiment Settings) |
| We illustrate the detailed hyperparameters in Table 4. | p. 16 (C. Training Implementation) |
| To project heterogeneous data into a unified representation space, we employ modality-specific encoders. | p. 4 (3.2. Unified Architecture) |
| See Appendix B for more details on this pipeline, including the pseudo code and tailored prompt used in each phase. | p. 4 (3.3. EM-CoT Data Pipeline) |
| Proprio: Robot Trajectory Data Task Instruction: Observations: Compute Position red block, green block, and blue block in a left-to-right sequence, forming a row. | p. 5 (3.3. EM-CoT Data Pipeline) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 4.3. Ablation Study - extractive body cue:** Notably, without any pre-training (w/o V+T+A), the model's performance falls to a complete 0% on hard tasks, demonstrating that pre-training is an absolutely foundational requirement ...
- **p. 7 / 4.2. Simulation Results - extractive body cue:** Particularly, the consistent huge relative performance gap (i.e., 73.5% and 62.0%) between HALO and π0 especially on Hard tasks indicates that HALO can also handle ...
- **p. 8 / 4.5. Real-World Results - extractive body cue:** While the baselines suffer noticeable performance degradation in the presence of visual distractions, lighting and background variations, and novel objects, HALO remains robust and achieves ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3. Attention Masking Strategy for EM-CoT. (1) Spa- tial and semantic tokens utilize bidirectional attention within frames. (2) Noise tokens attend bidirectionally to each ...
- **p. 7 / 4.2. Simulation Results - extractive body cue:** These results underscore the effectiveness and robustness of HALO for complex robotic manipulation.

- **Evidence anchors reviewed:** datasets p. 7 (4.1. Experiment Settings), p. 7 (4.2. Simulation Results), p. 6 (4. Experiments), p. 8 (4.5. Real-World Results), p. 16 (C. Training Implementation), p. 16 (C. Training Implementation), metrics p. 8 (4.5. Real-World Results), p. 7 (4.2. Simulation Results), p. 7 (4.2. Simulation Results), p. 6 (Figure/Table caption), p. 9 (Figure/Table caption), p. 8 (4.3. Ablation Study), baselines p. 7 (4.2. Simulation Results), p. 7 (4.2. Simulation Results), p. 8 (4.5. Real-World Results), p. 6 (4. Experiments), p. 8 (4.5. Real-World Results), results p. 8 (4.5. Real-World Results), p. 6 (4. Experiments), p. 7 (4.2. Simulation Results), p. 7 (4.2. Simulation Results), p. 8 (4.3. Ablation Study), p. 6 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
