# Insights — Efficient Reinforcement Learning by Guiding World Models with Non-Curated Data

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (35 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://iclr.cc/virtual/2026/poster/10007436; PDF retrieval source: https://arxiv.org/pdf/2502.19544. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 3. Train - extractive body cue:** To summarize, our contributions are: C1 We propose a more realistic setting for leveraging offline data that consists of reward-free and mixed-quality multi-embodiment data.
- **p. 1 / ABSTRACT - extractive body cue:** To address this issue and effectively use the offline data, we propose two techniques: i) experience rehearsal and ii) execution guidance.
- **p. 1 / ABSTRACT - extractive body cue:** Under limited sample budgets, our method achieves nearly twice the aggregate score of learning-from-scratch baselines across 72 visuomotor tasks spanning 6 embodiments.
- **p. 2 / 3. Train - extractive body cue:** To this end, we propose a pipeline named Non-curated offline data for efficient RL (NCRL).
- **p. 3 / 3. Train - extractive body cue:** C3 We propose two techniques, experience rehearsal and execution guidance, to mitigate the distributional gap and encourage exploration during RL fine-tuning.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** While pre-training visual encoders (Schwarzer et al., 2021; Nair et al., 2022; Parisi et al., 2022; Xiao et al., 2022; Yang & Nachum, 2021; Shang ...
- **p. 2 / 3. Train - extractive body cue:** Building on these insights, we propose using non-curated offline data in both pre-training and fine-tuning stages, in contrast to previous methods that only consider the ...
- **Contribution anchor:** p. 2 (3. Train), p. 1 (ABSTRACT), p. 1 (ABSTRACT), p. 2 (3. Train), p. 3 (3. Train), p. 1 (1 INTRODUCTION)

### Strongest assumption and failure boundary

- **p. 1 / 1 INTRODUCTION - extractive body cue:** While pre-training visual encoders (Schwarzer et al., 2021; Nair et al., 2022; Parisi et al., 2022; Xiao et al., 2022; Yang & Nachum, 2021; Shang ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** However, prior work has explored world model training primarily in settings with known rewards (Lu et al., 2023; Rafailov et al., 2023; Hansen et al., ...
- **p. 10 / 5 CONCLUSION - extractive body cue:** We show that naive fine-tuning of world models fails to accelerate RL training due to distributional shift and propose two techniques - experience rehearsal and ...
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** R3M fails to improve sample efficiency on most tasks, consistent with findings in Hansen et al.
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** As the compared baselines cannot handle multi-embodiment data like NCRL, we preprocess the offline data to only include task-relevant trajectories for them.
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** 6, world model pre-training shows promising results when the offline data consists of diverse trajectories, such as data collected by exploratory agents (Walker Run), while ...
- **p. 18 / Figure/Table caption - extractive body cue:** Figure 9: Comparison with Diffusion Policy. NCRL can effectively handle non-curated offline data while the imitation learning baseline fails. A.2 COMPARISON WITH IVIDEOGPT Comparison in ...
- **Boundary to test:** We show that naive fine-tuning of world models fails to accelerate RL training due to distributional shift and propose two techniques - experience rehearsal and execution guidance - to mitigate this issue.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | To summarize, our contributions are: C1 We propose a more realistic setting for leveraging offline data that consists of reward-free and mixed-quality multi-embodiment data. | p. 2 (3. Train), p. 1 (ABSTRACT) |
| Reported outcome | Figure 15: Comparison of DreamerV3 under different model size configurations. NCRL consis- tently outperforms both variants. A.6 PERFORMANCE ON CHALLENGING METAWORLD TASKS In Sec. I, although NCRL solves most MetaWorld tasks with ... | p. 20 (Figure/Table caption), p. 9 (4 EXPERIMENTS) |
| Failure/limitation | We show that naive fine-tuning of world models fails to accelerate RL training due to distributional shift and propose two techniques - experience rehearsal and execution guidance - to mitigate this issue. | p. 10 (5 CONCLUSION), p. 7 (4 EXPERIMENTS) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `observation, uncertainty/risk estimate와 task command → safe set, recovery state 또는 constraint margin → shielded, recovery 또는 safe action`.
- 이 논문의 재사용 가능한 지점은 While pre-training visual encoders (Schwarzer et al., 2021; Nair et al., 2022; Parisi et al., 2022; Xiao et al., 2022; Yang & Nachum, 2021; Shang et al., 2024) is a common approach ...를 Guidance Policy Enc Dec Enc Dec Enc Dec Figure 1: Overview of NCRL (Non-curated offline data for efficient RL).로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 safe set, recovery state 또는 constraint margin가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 We show that naive fine-tuning of world models fails to accelerate RL training due to distributional shift and propose two techniques - experience rehearsal and execution guidance - to mitigate this issue.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: To summarize, our contributions are: C1 We propose a more realistic setting for leveraging offline data that consists of reward-free and mixed-quality multi-embodiment data.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `World models, safety, uncertainty, and recovery`; tags: `Robotics, Reinforcement Learning, world model, non-curated data`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** We show that naive fine-tuning of world models fails to accelerate RL training due to distributional shift and propose two techniques - experience rehearsal and execution guidance - to mitigate this issue.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: I show comparison results on 22 locomotion and 50 robotic manipulation tasks with pixel inputs from DMControl and Meta-World benchmarks..
3. Compare against the body-reported baseline or a matched simpler baseline: Our method outperforms all compared baselines by a large margin..
4. Report the body metric and its denominator/aggregation: Steps (1e3) 0 50 100 Success Rate (%) Button Press TW..
5. Re-run the body-reported ablation/failure condition: 7, our method outperforms the variant using OTS on hard exploration tasks, Assembly and Stick Pull, by a large margin, showing the effectiveness of using execution guidance..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 1 (1 INTRODUCTION), p. 2 (3. Train), p. 2 (3. Train); the primary result is directionally consistent at p. 20 (Figure/Table caption), p. 9 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 summarize, contributions, more mechanism이 Our method outperforms all compared baselines by a large margin. 대비 Steps (1e3) 0 50 100 Success Rate (%) Button Press TW.을 개선하고, We show that naive fine-tuning of world models fails to accelerate RL training due to distributional ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
