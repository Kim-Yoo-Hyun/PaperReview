# Evaluation - Efficient Reinforcement Learning by Guiding World Models with Non-Curated Data

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (35 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://iclr.cc/virtual/2026/poster/10007436; PDF retrieval source: https://arxiv.org/pdf/2502.19544. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 20 (Figure/Table caption), p. 9 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 21 (Figure/Table caption), p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS)): Figure 15: Comparison of DreamerV3 under different model size configurations. NCRL consis- tently outperforms both variants. A.6 PERFORMANCE ON CHALLENGING METAWORLD TASKS In Sec. I, although NCRL solves most MetaWorld ...

## Evaluation Body Digest

- **p. 8 / 4 EXPERIMENTS - extractive PDF cue:** I show comparison results on 22 locomotion and 50 robotic manipulation tasks with pixel inputs from DMControl and Meta-World benchmarks.
- **p. 7 / 4 EXPERIMENTS - extractive PDF cue:** Dataset Our dataset consists of data from two benchmarks: DMControl and Meta-World, visualized in Sec.
- **p. 7 / 4 EXPERIMENTS - extractive PDF cue:** As the unsupervised RL agents are trained to maximize the agent's curiosity rather than a specific reward signal, the dataset for DMControl does not contain ...
- **p. 8 / 4 EXPERIMENTS - extractive PDF cue:** We train an RL agent to control an Ant robot from DMControl to complete a series of tasks incrementally.
- **p. 9 / 4 EXPERIMENTS - extractive PDF cue:** NCRL demonstrates the effectiveness of using execution guidance over uncertainty-based reward labeling on challenging robotic manipulation tasks.
- **p. 9 / 4 EXPERIMENTS - extractive PDF cue:** Setup & Baselines We set our continual adaptation experiment based on the Quadruped robot from DMControl.
- **p. 10 / 4 EXPERIMENTS - extractive PDF cue:** We use the Quadruped Walk task as a representative task for the investigation.
- **p. 10 / 4 EXPERIMENTS - extractive PDF cue:** Fine-tuning the full world model yields the best performance on the tested task.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** uncertain robot state와 safe/unsafe operating region.
- **Input boundary:** observation, uncertainty/risk estimate와 task command.
- **Output/decision under evaluation:** shielded, recovery 또는 safe action.
- **Primary target:** task return과 violation/failure probability.
- **Detected evaluation headings:** 4 EXPERIMENTS (p. 6); A MORE RESULTS (p. 18).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 15: Comparison of DreamerV3 under different model size configurations. NCRL consis- tently outperforms both variants. A.6 PERFORMANCE ON CHALLENGING METAWORLD TASKS In Sec. ... | p. 20 (Figure/Table caption) |
| 4 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | Results Figure 5 shows NCRL significantly outperforms PackNet, enabling adaptation within 100 trials per task. | p. 9 (4 EXPERIMENTS) |
| 4 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | With 150k online samples, NCRL achieves higher aggregate scores compared to DrQ-v2 and DreamerV3, matching their performance obtained with 3.3-6.7× more samples (500k for ... | p. 8 (4 EXPERIMENTS) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 16: Improved success rate on MetaWorld tasks as the training budget increases. B THEORETICAL ANALYSIS In this section, we give a theoretical analysis ... | p. 21 (Figure/Table caption) |
| 4 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | Despite the baselines having access to better-structured data, NCRL still significantly outperforms all baselines across the tested tasks. | p. 7 (4 EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 8 / 4 EXPERIMENTS - extractive PDF cue:** I show comparison results on 22 locomotion and 50 robotic manipulation tasks with pixel inputs from DMControl and Meta-World benchmarks.
- **p. 7 / 4 EXPERIMENTS - extractive PDF cue:** Dataset Our dataset consists of data from two benchmarks: DMControl and Meta-World, visualized in Sec.
- **p. 7 / 4 EXPERIMENTS - extractive PDF cue:** As the unsupervised RL agents are trained to maximize the agent's curiosity rather than a specific reward signal, the dataset for DMControl does not contain ...
- **p. 8 / 4 EXPERIMENTS - extractive PDF cue:** We train an RL agent to control an Ant robot from DMControl to complete a series of tasks incrementally.
- **p. 9 / 4 EXPERIMENTS - extractive PDF cue:** NCRL demonstrates the effectiveness of using execution guidance over uncertainty-based reward labeling on challenging robotic manipulation tasks.
- **p. 9 / 4 EXPERIMENTS - extractive PDF cue:** Setup & Baselines We set our continual adaptation experiment based on the Quadruped robot from DMControl.
- **p. 10 / 4 EXPERIMENTS - extractive PDF cue:** We use the Quadruped Walk task as a representative task for the investigation.
- **p. 10 / 4 EXPERIMENTS - extractive PDF cue:** Fine-tuning the full world model yields the best performance on the tested task.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 1: Overview of NCRL (Non-curated offline data for efficient RL). NCRL leverages non- curated offline data-reward-free, mixed-quality, and multi-embodiment-to enable efficient RL. It uses ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Table 1: Comparison with different policy learning methods that leverage offline data. Offline RL Off2On RL RLPD MT Offline RL NCRL (ours) Reward-free offline data ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 2: Visualization of Distribution Mismatch. Left: At the early stage of fine-tuning, there is a distribution shift between offline data used for world model ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 3: Left: Quantitative comparison across 72 diverse tasks from Meta-World (Yu et al., 2020) and DMControl (Tassa et al., 2018) with the same sample ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 4: Comparison with other world model pre-training methods. NCRL outperforms state- of-the-art model-based methods without relying on techniques used in iVideoGPT, such as reward ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 5: NCRL enables fast task adaptation. We train an RL agent to control an Ant robot from DMControl to complete a series of tasks ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Figure 6: Ablation study on key components. "P" represents world model pre-training, "ER" means experience rehearsal, and "G" represents execution guidance. The combination of a ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Figure 7: Comparison of execution guidance versus uncertainty-based reward labeling. NCRL demonstrates the effectiveness of using execution guidance over uncertainty-based reward label- ing on challenging ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | I show comparison results on 22 locomotion and 50 robotic manipulation tasks with pixel inputs from DMControl and Meta-World benchmarks. | embodiment, simulator version and control stack | p. 8 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS) |
| Task/environment | Dataset Our dataset consists of data from two benchmarks: DMControl and Meta-World, visualized in Sec. | reset, timeout, object/scene variation | p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS) |
| Observation/sensor | observation, uncertainty/risk estimate와 task command | calibration, preprocessing, privileged input | p. 1 (1 INTRODUCTION), p. 2 (3. Train) |
| Output/decision | shielded, recovery 또는 safe action | action frame, controller and termination | p. 2 (3. Train), p. 3 (3. Train) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Steps (1e3) 0 50 100 Success Rate (%) Button Press TW. | definition/direction/unit from same section | p. 8 (4 EXPERIMENTS) |
| Steps (1e3) 0 50 100 Success Rate (%) Plate Slide 0 50 100 Env. | definition/direction/unit from same section | p. 8 (4 EXPERIMENTS) |
| Figure 15: Comparison of DreamerV3 under different model size configurations. NCRL consis- tently outperforms both variants. A.6 PERFORMANCE ON CHALLENGING METAWORLD TASKS In Sec. ... | definition/direction/unit from same section | p. 20 (Figure/Table caption) |
| Steps (1e3) 0 50 100 Normalized Score Stick Pull Base (P+ER) +G (ours) +OTS Figure 7: Comparison of execution guidance versus uncertainty-based reward labeling. | definition/direction/unit from same section | p. 9 (4 EXPERIMENTS) |
| Figure 16: Improved success rate on MetaWorld tasks as the training budget increases. B THEORETICAL ANALYSIS In this section, we give a theoretical analysis ... | definition/direction/unit from same section | p. 21 (Figure/Table caption) |
| Table 3: Success rate of Meta-World benchmark with pixel inputs. Tasks DreamerV3 @ 1M DrQ-v2 @ 1M DreamerV3 @ 150k | definition/direction/unit from same section | p. 28 (Figure/Table caption) |
| UDS shows only slightly better performance on Walker Run compared to R3M and JSRL-BC, demonstrating the ineffectiveness of zero-reward labeling. | definition/direction/unit from same section | p. 7 (4 EXPERIMENTS) |
| 4.1 NCRL IMPROVES SAMPLE EFFICIENCY ACROSS DIVERSE TASKS Comparison with Methods that Leverage Offline Data We compare NCRL against several state-of-the-art methods that leverage ... | definition/direction/unit from same section | p. 7 (4 EXPERIMENTS) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Our method outperforms all compared baselines by a large margin. | comparison identity and matched condition | p. 7 (4 EXPERIMENTS) |
| 4.1 NCRL IMPROVES SAMPLE EFFICIENCY ACROSS DIVERSE TASKS Comparison with Methods that Leverage Offline Data We compare NCRL against several state-of-the-art methods that leverage ... | comparison identity and matched condition | p. 7 (4 EXPERIMENTS) |
| NCRL significantly outperforms the widely used baseline PackNet by properly leveraging non-curated offline data. | comparison identity and matched condition | p. 8 (4 EXPERIMENTS) |
| Figure 3: Left: Quantitative comparison across 72 diverse tasks from Meta-World (Yu et al., 2020) and DMControl (Tassa et al., 2018) with the same ... | comparison identity and matched condition | p. 6 (Figure/Table caption) |
| Figure 7: Comparison of execution guidance versus uncertainty-based reward labeling. NCRL demonstrates the effectiveness of using execution guidance over uncertainty-based reward label- ing on ... | comparison identity and matched condition | p. 9 (Figure/Table caption) |
| NCRL outperforms stateof-the-art model-based methods without relying on techniques used in iVideoGPT, such as reward shaping and demonstration-based replay buffer initialization. | comparison identity and matched condition | p. 8 (4 EXPERIMENTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| 7, our method outperforms the variant using OTS on hard exploration tasks, Assembly and Stick Pull, by a large margin, showing the effectiveness of ... | component/input/data sensitivity | p. 10 (4 EXPERIMENTS) |
| 4.3 ABLATIONS Role of Each Component We now analyze each component's contribution using the same set of tasks from Sec. | component/input/data sensitivity | p. 9 (4 EXPERIMENTS) |
| Steps (1e3) 0 50 100 Normalized Score Stick Pull DreamerV3 +P +P+ER +P+ER+G (ours) Figure 6: Ablation study on key components. "P" represents world ... | component/input/data sensitivity | p. 9 (4 EXPERIMENTS) |
| Figure 13: Ablation study on the role of each component. "P" represents world model pretraining, "ER" means experience rehearsal, and "G" represents execution guidance. ... | component/input/data sensitivity | p. 20 (Figure/Table caption) |
| Figure 1: Overview of NCRL (Non-curated offline data for efficient RL). NCRL leverages non- curated offline data-reward-free, mixed-quality, and multi-embodiment-to enable efficient RL. It ... | component/input/data sensitivity | p. 2 (Figure/Table caption) |
| We further conduct detailed ablation studies to evaluate our method. | component/input/data sensitivity | p. 7 (4 EXPERIMENTS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To summarize, our contributions are: C1 We propose a more realistic setting for leveraging offline data that consists of reward-free and mixed-quality multi-embodiment data. | Figure 15: Comparison of DreamerV3 under different model size configurations. NCRL consis- tently outperforms both variants. A.6 PERFORMANCE ON CHALLENGING METAWORLD TASKS In Sec. ... | PDF body cue; verify exact table/figure and matched conditions | p. 20 (Figure/Table caption), p. 9 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 21 (Figure/Table caption), p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS) |
| Primary metric/result | Results Figure 5 shows NCRL significantly outperforms PackNet, enabling adaptation within 100 trials per task. | numeric claim only at cited anchor | p. 9 (4 EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 7 / 4 EXPERIMENTS - extractive PDF cue:** As the unsupervised RL agents are trained to maximize the agent's curiosity rather than a specific reward signal, the dataset for DMControl does not contain ...
- **p. 7 / 4 EXPERIMENTS - extractive PDF cue:** For example, on Quadruped Walk, NCRL benefits from exploratory offline data, enabling pixel-based control within just 100 trials.
- **p. 9 / 4 EXPERIMENTS - extractive PDF cue:** Results Figure 5 shows NCRL significantly outperforms PackNet, enabling adaptation within 100 trials per task.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | We show that naive fine-tuning of world models fails to accelerate RL training due to distributional shift and propose two techniques - experience rehearsal ... | p. 10 (5 CONCLUSION) |
| body limitation/failure cue | R3M fails to improve sample efficiency on most tasks, consistent with findings in Hansen et al. | p. 7 (4 EXPERIMENTS) |
| body limitation/failure cue | As the compared baselines cannot handle multi-embodiment data like NCRL, we preprocess the offline data to only include task-relevant trajectories for them. | p. 7 (4 EXPERIMENTS) |
| body limitation/failure cue | 6, world model pre-training shows promising results when the offline data consists of diverse trajectories, such as data collected by exploratory agents (Walker Run), ... | p. 9 (4 EXPERIMENTS) |
| body limitation/failure cue | Figure 9: Comparison with Diffusion Policy. NCRL can effectively handle non-curated offline data while the imitation learning baseline fails. A.2 COMPARISON WITH IVIDEOGPT Comparison ... | p. 18 (Figure/Table caption) |
| body limitation/failure cue | Figure 11: Comparison with model-based approaches for leveraging offline data. 500 retrieved trajectories. Our method achieves consistently high precision. For the Door Open task, ... | p. 19 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Steps (1e3) 0 20 40 60 Normalized Score Walker Run 0 200 400 Env. | p. 9 (4 EXPERIMENTS) |
| Specifically, the agent sequentially learns stand, walk, run, jump, roll, and roll fast tasks with 300K environment steps per task. | p. 9 (4 EXPERIMENTS) |
| We use three random seeds for each task. | p. 7 (4 EXPERIMENTS) |
| We enhance the original implementation with reward ensembles. | p. 7 (4 EXPERIMENTS) |
| Steps (1e3) 0 50 100 Success Rate (%) Button Press TW. | p. 8 (4 EXPERIMENTS) |
| Steps (1e3) 0 50 100 Success Rate (%) Plate Slide 0 50 100 Env. | p. 8 (4 EXPERIMENTS) |
| 8, the encoder, decoder, and latent dynamics play important roles during fine-tuning. | p. 10 (4 EXPERIMENTS) |
| While pre-training visual encoders (Schwarzer et al., 2021; Nair et al., 2022; Parisi et al., 2022; Xiao et al., 2022; Yang & Nachum, 2021; ... | p. 1 (1 INTRODUCTION) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 10 / 5 CONCLUSION - extractive PDF cue:** We show that naive fine-tuning of world models fails to accelerate RL training due to distributional shift and propose two techniques - experience rehearsal and ...
- **p. 7 / 4 EXPERIMENTS - extractive PDF cue:** R3M fails to improve sample efficiency on most tasks, consistent with findings in Hansen et al.
- **p. 7 / 4 EXPERIMENTS - extractive PDF cue:** As the compared baselines cannot handle multi-embodiment data like NCRL, we preprocess the offline data to only include task-relevant trajectories for them.
- **p. 9 / 4 EXPERIMENTS - extractive PDF cue:** 6, world model pre-training shows promising results when the offline data consists of diverse trajectories, such as data collected by exploratory agents (Walker Run), while ...
- **p. 18 / Figure/Table caption - extractive PDF cue:** Figure 9: Comparison with Diffusion Policy. NCRL can effectively handle non-curated offline data while the imitation learning baseline fails. A.2 COMPARISON WITH IVIDEOGPT Comparison in ...
- **p. 19 / Figure/Table caption - extractive PDF cue:** Figure 11: Comparison with model-based approaches for leveraging offline data. 500 retrieved trajectories. Our method achieves consistently high precision. For the Door Open task, some ...

- **PDF anchors reviewed:** datasets p. 8 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), metrics p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 20 (Figure/Table caption), p. 9 (4 EXPERIMENTS), p. 21 (Figure/Table caption), p. 28 (Figure/Table caption), baselines p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 6 (Figure/Table caption), p. 9 (Figure/Table caption), p. 8 (4 EXPERIMENTS), results p. 20 (Figure/Table caption), p. 9 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 21 (Figure/Table caption), p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
