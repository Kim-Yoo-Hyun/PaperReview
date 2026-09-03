# Efficient Reinforcement Learning by Guiding World Models with Non-Curated Data

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (35 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://iclr.cc/virtual/2026/poster/10007436.
> PDF retrieval source: https://arxiv.org/pdf/2502.19544. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICLR
- Authors: not duplicated here when not verified in the registry source
- Primary track: World models, safety, uncertainty, and recovery
- Tier: REFERENCE
- Tags: Robotics, Reinforcement Learning, world model, non-curated data
- Official paper: https://iclr.cc/virtual/2026/poster/10007436
- Full-text retrieval: https://arxiv.org/pdf/2502.19544
- Code/Project: https://aidanscannell.com/publications/efficient-rl-by-guiding-generalist-world-models-with-non-curated-data/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (35 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

World models, safety, uncertainty, and recovery의 safety 문제를 이해하기 위해 읽는다. 본문은 While pre-training visual encoders (Schwarzer et al., 2021; Nair et al., 2022; Parisi et al., 2022; Xiao et al., 2022; Yang & Nachum, 2021; Shang et al., 2024) is a common approach ...를 문제로 두고, To summarize, our contributions are: C1 We propose a more realistic setting for leveraging offline data that consists of reward-free and mixed-quality multi-embodiment data.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** Leveraging offline data is a promising way to improve the sample efficiency of online reinforcement learning (RL).
- **p. 1 / ABSTRACT - extractive body cue:** This paper expands the pool of usable data for offline-to-online RL by leveraging abundant non-curated data that is reward-free, of mixed quality, and collected across ...
- **p. 1 / ABSTRACT - extractive body cue:** Although learning a world model appears promising for utilizing such data, we find that naive finetuning fails to accelerate RL training on many tasks.
- **p. 1 / ABSTRACT - extractive body cue:** Through careful investigation, we attribute this failure to the distributional shift between offline and online data during fine-tuning.
- **p. 1 / ABSTRACT - extractive body cue:** To address this issue and effectively use the offline data, we propose two techniques: i) experience rehearsal and ii) execution guidance.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** While pre-training visual encoders (Schwarzer et al., 2021; Nair et al., 2022; Parisi et al., 2022; Xiao et al., 2022; Yang & Nachum, 2021; Shang ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** However, prior work has explored world model training primarily in settings with known rewards (Lu et al., 2023; Rafailov et al., 2023; Hansen et al., ...

## Core Idea

- **p. 2 / 3. Train - extractive body cue:** To summarize, our contributions are: C1 We propose a more realistic setting for leveraging offline data that consists of reward-free and mixed-quality multi-embodiment data.
- **p. 1 / ABSTRACT - extractive body cue:** To address this issue and effectively use the offline data, we propose two techniques: i) experience rehearsal and ii) execution guidance.
- **p. 1 / ABSTRACT - extractive body cue:** Under limited sample budgets, our method achieves nearly twice the aggregate score of learning-from-scratch baselines across 72 visuomotor tasks spanning 6 embodiments.
- **p. 2 / 3. Train - extractive body cue:** To this end, we propose a pipeline named Non-curated offline data for efficient RL (NCRL).
- **p. 3 / 3. Train - extractive body cue:** C3 We propose two techniques, experience rehearsal and execution guidance, to mitigate the distributional gap and encourage exploration during RL fine-tuning.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** While pre-training visual encoders (Schwarzer et al., 2021; Nair et al., 2022; Parisi et al., 2022; Xiao et al., 2022; Yang & Nachum, 2021; Shang ...
- **p. 2 / 3. Train - extractive body cue:** Building on these insights, we propose using non-curated offline data in both pre-training and fine-tuning stages, in contrast to previous methods that only consider the ...
- **p. 2 / 3. Train - extractive body cue:** It uses this data to pretrain a task-agnostic world model, and then, during fine-tuning, to reduce distributional shift and guide exploration through experience rehearsal and ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | While pre-training visual encoders (Schwarzer et al., 2021; Nair et al., 2022; Parisi et al., 2022; Xiao et al., 2022; Yang & Nachum, 2021; Shang et al., 2024) is a common approach ... | observation, uncertainty/risk estimate와 task command | p. 1 (1 INTRODUCTION), p. 2 (3. Train) |
| State/latent | While, pre-training, visual, encoders, Schwarzer, Nair, Parisi, Xiao, Yang, Nachum, Shang, common | safe set, recovery state 또는 constraint margin | p. 1 (1 INTRODUCTION), p. 2 (3. Train), p. 2 (3. Train) |
| Output/action | Guidance Policy Enc Dec Enc Dec Enc Dec Figure 1: Overview of NCRL (Non-curated offline data for efficient RL). | shielded, recovery 또는 safe action | p. 2 (3. Train), p. 2 (3. Train), p. 1 (1 INTRODUCTION) |
| Objective/outcome | For instance, leveraging offline datasets for new robotic manipulation tasks requires retrospectively annotating image-based data with rewards. | task return과 violation/failure probability | p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (3. Train) |

## Main Claims and Actual Contribution

- **p. 2 / 3. Train - extractive body cue:** To summarize, our contributions are: C1 We propose a more realistic setting for leveraging offline data that consists of reward-free and mixed-quality multi-embodiment data.
- **p. 1 / ABSTRACT - extractive body cue:** To address this issue and effectively use the offline data, we propose two techniques: i) experience rehearsal and ii) execution guidance.
- **p. 1 / ABSTRACT - extractive body cue:** Under limited sample budgets, our method achieves nearly twice the aggregate score of learning-from-scratch baselines across 72 visuomotor tasks spanning 6 embodiments.
- **p. 2 / 3. Train - extractive body cue:** To this end, we propose a pipeline named Non-curated offline data for efficient RL (NCRL).
- **p. 3 / 3. Train - extractive body cue:** C3 We propose two techniques, experience rehearsal and execution guidance, to mitigate the distributional gap and encourage exploration during RL fine-tuning.
- **p. 20 / Figure/Table caption - extractive body cue:** Figure 15: Comparison of DreamerV3 under different model size configurations. NCRL consis- tently outperforms both variants. A.6 PERFORMANCE ON CHALLENGING METAWORLD TASKS In Sec. I, ...
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** Results Figure 5 shows NCRL significantly outperforms PackNet, enabling adaptation within 100 trials per task.
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** With 150k online samples, NCRL achieves higher aggregate scores compared to DrQ-v2 and DreamerV3, matching their performance obtained with 3.3-6.7× more samples (500k for DMControl, ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 20 (Figure/Table caption), p. 9 (4 EXPERIMENTS) |
| Embodiment/environment | I show comparison results on 22 locomotion and 50 robotic manipulation tasks with pixel inputs from DMControl and Meta-World benchmarks. | hardware/simulator version and reset protocol | p. 8 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS) |
| Dataset/benchmark | As the unsupervised RL agents are trained to maximize the agent's curiosity rather than a specific reward signal, the dataset for DMControl does not contain expert trajectories for a specific task (e.g., ... | role, split, size and leakage | p. 8 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS) |
| Metric | Steps (1e3) 0 50 100 Success Rate (%) Button Press TW. | definition, denominator, direction and uncertainty | p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 20 (Figure/Table caption) |
| Baseline/ablation | Our method outperforms all compared baselines by a large margin. | fair input/data/compute/action matching | p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 10 / 5 CONCLUSION - extractive body cue:** We show that naive fine-tuning of world models fails to accelerate RL training due to distributional shift and propose two techniques - experience rehearsal and ...
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** R3M fails to improve sample efficiency on most tasks, consistent with findings in Hansen et al.
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** As the compared baselines cannot handle multi-embodiment data like NCRL, we preprocess the offline data to only include task-relevant trajectories for them.
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** 6, world model pre-training shows promising results when the offline data consists of diverse trajectories, such as data collected by exploratory agents (Walker Run), while ...
- **p. 18 / Figure/Table caption - extractive body cue:** Figure 9: Comparison with Diffusion Policy. NCRL can effectively handle non-curated offline data while the imitation learning baseline fails. A.2 COMPARISON WITH IVIDEOGPT Comparison in ...
- **p. 19 / Figure/Table caption - extractive body cue:** Figure 11: Comparison with model-based approaches for leveraging offline data. 500 retrieved trajectories. Our method achieves consistently high precision. For the Door Open task, some ...
- **p. 20 / Figure/Table caption - extractive body cue:** Figure 14: Comparison with injecting different ratios of task-irrelevant offline data. Our method remains robust even as the quality of the retrieved data degrades. A.5 ...

## Why Read It

World models, safety, uncertainty, and recovery의 safety 문제를 이해하기 위해 읽는다. 본문은 While pre-training visual encoders (Schwarzer et al., 2021; Nair et al., 2022; Parisi et al., 2022; Xiao et al., 2022; Yang & Nachum, 2021; Shang et al., 2024) is a common approach ...를 문제로 두고, To summarize, our contributions are: C1 We propose a more realistic setting for leveraging offline data that consists of reward-free and mixed-quality multi-embodiment data.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (3. Train), p. 2 (3. Train), p. 1 (ABSTRACT), p. 3 (3. Train) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
