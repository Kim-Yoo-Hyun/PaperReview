# Method - Efficient Reinforcement Learning by Guiding World Models with Non-Curated Data

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (35 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://iclr.cc/virtual/2026/poster/10007436; PDF retrieval source: https://arxiv.org/pdf/2502.19544. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 1 (1 INTRODUCTION), p. 2 (3. Train), p. 2 (3. Train), p. 1 (ABSTRACT), p. 3 (3. Train), p. 3 (3. Train)): While pre-training visual encoders (Schwarzer et al., 2021; Nair et al., 2022; Parisi et al., 2022; Xiao et al., 2022; Yang & Nachum, 2021; Shang et al., 2024) is a ...

## Method Body Digest

- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** While pre-training visual encoders (Schwarzer et al., 2021; Nair et al., 2022; Parisi et al., 2022; Xiao et al., 2022; Yang & Nachum, 2021; Shang ...
- **p. 2 / 3. Train - extractive PDF cue:** Building on these insights, we propose using non-curated offline data in both pre-training and fine-tuning stages, in contrast to previous methods that only consider the ...
- **p. 2 / 3. Train - extractive PDF cue:** It uses this data to pretrain a task-agnostic world model, and then, during fine-tuning, to reduce distributional shift and guide exploration through experience rehearsal and ...
- **p. 1 / ABSTRACT - extractive PDF cue:** Although learning a world model appears promising for utilizing such data, we find that naive finetuning fails to accelerate RL training on many tasks.
- **p. 3 / 3. Train - extractive PDF cue:** Offline RL Off2On RL RLPD MT Offline RL NCRL (ours) Reward-free offline data ✗ ✗ ✗ ✗ ✓ Non-expert offline data ✓ ✓ ✓ ✓ ...
- **p. 3 / 3. Train - extractive PDF cue:** Published as a conference paper at ICLR 2026 Table 1: Comparison with different policy learning methods that leverage offline data.
- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** For instance, leveraging offline datasets for new robotic manipulation tasks requires retrospectively annotating image-based data with rewards.
- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** We instead propose expanding the pool of usable offline data by utilizing abundant non-curated data that is reward-free, of mixed quality, and collected across multiple ...

## Design Rationale

- **p. 2 / 3. Train - extractive PDF cue:** To summarize, our contributions are: C1 We propose a more realistic setting for leveraging offline data that consists of reward-free and mixed-quality multi-embodiment data.
- **p. 1 / ABSTRACT - extractive PDF cue:** To address this issue and effectively use the offline data, we propose two techniques: i) experience rehearsal and ii) execution guidance.
- **p. 1 / ABSTRACT - extractive PDF cue:** Under limited sample budgets, our method achieves nearly twice the aggregate score of learning-from-scratch baselines across 72 visuomotor tasks spanning 6 embodiments.

## Source Evidence Cues

- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** While pre-training visual encoders (Schwarzer et al., 2021; Nair et al., 2022; Parisi et al., 2022; Xiao et al., 2022; Yang & Nachum, 2021; Shang ...
- **p. 2 / 3. Train - extractive PDF cue:** Building on these insights, we propose using non-curated offline data in both pre-training and fine-tuning stages, in contrast to previous methods that only consider the ...
- **p. 2 / 3. Train - extractive PDF cue:** It uses this data to pretrain a task-agnostic world model, and then, during fine-tuning, to reduce distributional shift and guide exploration through experience rehearsal and ...
- **p. 1 / ABSTRACT - extractive PDF cue:** Although learning a world model appears promising for utilizing such data, we find that naive finetuning fails to accelerate RL training on many tasks.
- **p. 3 / 3. Train - extractive PDF cue:** Offline RL Off2On RL RLPD MT Offline RL NCRL (ours) Reward-free offline data ✗ ✗ ✗ ✗ ✓ Non-expert offline data ✓ ✓ ✓ ✓ ...
- **p. 3 / 3. Train - extractive PDF cue:** Published as a conference paper at ICLR 2026 Table 1: Comparison with different policy learning methods that leverage offline data.
- **Detected method headings:** A.5 MODEL SIZE OF DREAMERV3 (p. 20)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Risk / failure representation | unsafe state와 uncertainty를 계산한다 | observation, nominal command, history | barrier, risk model, failure classifier, uncertainty 또는 safe set을 추정 | risk/margin/failure state | While pre-training visual encoders (Schwarzer et al., 2021; Nair et al., 2022; Parisi et al., 2022; Xiao et al., 2022; Yang & ... | p. 1 (1 INTRODUCTION), p. 2 (3. Train) |
| Filtering / recovery | nominal command를 안전 command로 바꾼다 | nominal action과 safety constraint | QP shield, backup policy, correction, stop 또는 recovery plan을 선택 | safe/recovery action | Building on these insights, we propose using non-curated offline data in both pre-training and fine-tuning stages, in contrast to previous methods that ... | p. 2 (3. Train), p. 2 (3. Train) |
| Monitoring / re-entry | 실행 결과를 다시 risk decision에 반영한다 | executed action과 next observation | threshold, update, replan, abort 또는 return-to-task를 수행 | continue/correct/abort state | It uses this data to pretrain a task-agnostic world model, and then, during fine-tuning, to reduce distributional shift and guide exploration through ... | p. 2 (3. Train), p. 1 (ABSTRACT) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** For instance, leveraging offline datasets for new robotic manipulation tasks requires retrospectively annotating image-based data with rewards.
- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** We instead propose expanding the pool of usable offline data by utilizing abundant non-curated data that is reward-free, of mixed quality, and collected across multiple ...
- **p. 2 / 3. Train - extractive PDF cue:** NCRL leverages noncurated offline data-reward-free, mixed-quality, and multi-embodiment-to enable efficient RL.
- **p. 2 / 3. Train - extractive PDF cue:** In the pre-training stage, NCRL learns a task-agnostic world model from non-curated offline data that is reward-free, mix-quality and task-agnostic.
- **p. 3 / 3. Train - extractive PDF cue:** Offline RL Off2On RL RLPD MT Offline RL NCRL (ours) Reward-free offline data ✗ ✗ ✗ ✗ ✓ Non-expert offline data ✓ ✓ ✓ ✓ ...
- **Formal bridge:** state/history and risk h(s) -> filtered/recovery action u_safe -> task utility subject to safety constraint -> low violation/failure probability with useful intervention.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | While, pre-training, visual, encoders, Schwarzer, Nair, Parisi, Xiao, Yang, Nachum, Shang, common, utilize, non-curated | observation, uncertainty/risk estimate와 task command | body cue; exact tensor/frame verify |
| State/latent | While, pre-training, visual, encoders, Schwarzer, Nair, Parisi, Xiao, Yang, Nachum | safe set, recovery state 또는 constraint margin | body cue; notation verify |
| Action/output | summarize, contributions, more, realistic, setting, leveraging, offline, data, consists, reward-free | shielded, recovery 또는 safe action | body cue; unit/decoder verify |
| Objective/constraint | instance, leveraging, offline, datasets, robotic, manipulation, tasks, requires, retrospectively, annotating | task utility subject to safety constraint | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** While pre-training visual encoders (Schwarzer et al., 2021; Nair et al., 2022; Parisi et al., 2022; Xiao et al., 2022; Yang & Nachum, 2021; Shang ...
- **p. 2 / 3. Train - extractive PDF cue:** Guidance Policy Enc Dec Enc Dec Enc Dec Figure 1: Overview of NCRL (Non-curated offline data for efficient RL).
- **p. 2 / 3. Train - extractive PDF cue:** On representative challenging tasks, NCRL outperforms baselines that leverage offline data as well as state-of-the-art methods using pre-trained world models by a significant margin.
- **p. 3 / 3. Train - extractive PDF cue:** Published as a conference paper at ICLR 2026 Table 1: Comparison with different policy learning methods that leverage offline data.
- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** Leveraging offline data offers a promising way to improve the sample efficiency of reinforcement learning (RL).
- **p. 3 / 3. Train - extractive PDF cue:** C3 We propose two techniques, experience rehearsal and execution guidance, to mitigate the distributional gap and encourage exploration during RL fine-tuning.
- **Normalized interface:** observation=observation, uncertainty/risk estimate와 task command; state=safe set, recovery state 또는 constraint margin; output/action=shielded, recovery 또는 safe action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | 현재 command의 one-step safety 또는 recovery trajectory horizon; exact lookahead 확인 필요. | UDS and ExPLORe reuse offline data by labeling it with zero rewards and UCB rewards, respectively, and concatenating it with online data ... | episode/sequence/action-chunk boundary |
| Rate / latency | nominal policy와 safety monitor/filter의 runtime rate를 별도로 기록한다. | (iv) JSRL-BC (Uchendu et al., 2023), which collects online data using a mixture of the training policy and a behavior-cloned prior policy ... | Hz/fps, inference time and control rate |
| Memory | risk score, recent trajectory/history와 recovery state. | not recovered | window and reset |
| Compute | risk inference, barrier/QP solve 또는 backup policy selection이 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** While pre-training visual encoders (Schwarzer et al., 2021; Nair et al., 2022; Parisi et al., 2022; Xiao et al., 2022; Yang & Nachum, 2021; Shang ...
- **p. 2 / 3. Train - extractive PDF cue:** Building on these insights, we propose using non-curated offline data in both pre-training and fine-tuning stages, in contrast to previous methods that only consider the ...
- **p. 2 / 3. Train - extractive PDF cue:** It uses this data to pretrain a task-agnostic world model, and then, during fine-tuning, to reduce distributional shift and guide exploration through experience rehearsal and ...
- **p. 1 / ABSTRACT - extractive PDF cue:** Although learning a world model appears promising for utilizing such data, we find that naive finetuning fails to accelerate RL training on many tasks.
- **p. 3 / 3. Train - extractive PDF cue:** Offline RL Off2On RL RLPD MT Offline RL NCRL (ours) Reward-free offline data ✗ ✗ ✗ ✗ ✓ Non-expert offline data ✓ ✓ ✓ ✓ ...
- **p. 10 / 4 EXPERIMENTS - extractive PDF cue:** 8, the encoder, decoder, and latent dynamics play important roles during fine-tuning.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** While, pre-training, visual, encoders, Schwarzer, Nair, Parisi, Xiao, Yang, Nachum, Shang, common, utilize, non-curated, offline, datasets, fails, fully, leverage, rich.
- **Relevant PDF headings:** A.5 MODEL SIZE OF DREAMERV3 (p. 20).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Risk / failure representation | I show comparison results on 22 locomotion and 50 robotic manipulation tasks with pixel inputs from DMControl and Meta-World benchmarks. | p. 8 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS) |
| Filtering / recovery | Our method outperforms all compared baselines by a large margin. | p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS) |
| Monitoring / re-entry | Figure 15: Comparison of DreamerV3 under different model size configurations. NCRL consis- tently outperforms both variants. A.6 PERFORMANCE ON CHALLENGING METAWORLD TASKS ... | p. 20 (Figure/Table caption), p. 9 (4 EXPERIMENTS) |

## Failure and Ablation Link

- **p. 10 / 4 EXPERIMENTS - extractive PDF cue:** 7, our method outperforms the variant using OTS on hard exploration tasks, Assembly and Stick Pull, by a large margin, showing the effectiveness of using ...
- **p. 9 / 4 EXPERIMENTS - extractive PDF cue:** 4.3 ABLATIONS Role of Each Component We now analyze each component's contribution using the same set of tasks from Sec.
- **p. 9 / 4 EXPERIMENTS - extractive PDF cue:** Steps (1e3) 0 50 100 Normalized Score Stick Pull DreamerV3 +P +P+ER +P+ER+G (ours) Figure 6: Ablation study on key components. "P" represents world model ...
- **p. 20 / Figure/Table caption - extractive PDF cue:** Figure 13: Ablation study on the role of each component. "P" represents world model pretraining, "ER" means experience rehearsal, and "G" represents execution guidance. Together ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 1: Overview of NCRL (Non-curated offline data for efficient RL). NCRL leverages non- curated offline data-reward-free, mixed-quality, and multi-embodiment-to enable efficient RL. It uses ...
- **p. 7 / 4 EXPERIMENTS - extractive PDF cue:** We further conduct detailed ablation studies to evaluate our method.
- **p. 7 / 4 EXPERIMENTS - extractive PDF cue:** For DMControl, we include 10k trajectories covering 5 embodiments collected by unsupervised RL agents (Rajeswar et al., 2023; Pathak et al., 2017), trained via curiosity ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 1 (1 INTRODUCTION), p. 2 (3. Train), p. 2 (3. Train), p. 1 (ABSTRACT), p. 3 (3. Train), p. 3 (3. Train), objective p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (3. Train), p. 2 (3. Train), p. 3 (3. Train), temporal p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
