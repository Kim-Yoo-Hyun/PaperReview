# Method - Learning to Be Uncertain: Pre-training World Models with Horizon-Calibrated Uncertainty

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (21 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://iclr.cc/virtual/2026/poster/10007319; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/245358. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> DOC-QA1 (2026-10-23): 제어문자·깨진 추출 구간과 직접 연결된 표 항목을 PDF 페이지 이미지와 대조했다. 확인 범위·원문 URL·페이지·수정 이력은 [대조 기록](../../../work/sources/pdf_note_review_2026-10-23.json)에 있다. 노트 전체의 정독이나 모든 기존 주장에 대한 재검증을 뜻하지 않으며 reading status는 유지한다.

## Method in One Sentence

- **원문 대조:** 각 dynamics ensemble head는 현재 latent state와 temporal embedding을 조건으로 미래 latent state의 Gaussian mean·isotropic variance를 출력한다. Head별 분포 예측과, head mean 사이 disagreement를 키우는 HCU 항은 별도 요소다. ([PDF p. 5](https://proceedings.iclr.cc/paper_files/paper/2026/file/ad222e6e38e26e3f00d85829b9e02f43-Paper-Conference.pdf#page=5), §4.1, Eq. (1)).

## Method Body Digest

- **원문 대조:** 각 dynamics ensemble head는 현재 latent state와 temporal embedding을 조건으로 미래 latent state의 Gaussian mean·isotropic variance를 출력한다. Head별 분포 예측과, head mean 사이 disagreement를 키우는 HCU 항은 별도 요소다. ([PDF p. 5](https://proceedings.iclr.cc/paper_files/paper/2026/file/ad222e6e38e26e3f00d85829b9e02f43-Paper-Conference.pdf#page=5), §4.1, Eq. (1)).
- **p. 5 / 4 METHODOLOGY - extractive body cue:** In the pre-training phase, we introduce a variable-horizon prediction task, where an ensemble of dynamics models learns to forecast future states over randomly sampled time ...
- **p. 6 / 4 METHODOLOGY - extractive body cue:** The composite latent state [ˆst; ˜st] then drives policy optimization, with an auxiliary reward predictor Rθ trained on task-specific rewards to guide imagination-based planning.
- **p. 6 / 4 METHODOLOGY - extractive body cue:** The pre-trained stream-unmodified from pre-training-receives only temporal embeddings and generates latent states ˆst that capture action-agnostic environmental dynamics.
- **p. 4 / 4 METHODOLOGY - extractive body cue:** 2: (1) uncertaintyaware pre-training on action-free video, followed by (2) efficient fine-tuning for downstream con4
- **p. 7 / 4 METHODOLOGY - extractive body cue:** The overall algorithm is in appendix B, and full architectural details appear in appendix C.1.
- **p. 7 / 4 METHODOLOGY - extractive body cue:** Solid curves represent the mean evaluation return across four random seeds, and shaded regions denote the 95% confidence interval. exploiting task-specific action knowledge from the ...
- **p. 5 / 4 METHODOLOGY - extractive body cue:** To dynamically balance predictive accuracy against uncertainty representation, we formulate a dual optimization objective: Ltotal = Lpred + λLHCU (4) Here, λ serves as an ...

## Design Rationale

- **p. 2 / 1 INTRODUCTION - extractive body cue:** We propose a novel framework using variable-horizon prediction and introduce the Horizon-Calibrated Uncertainty (HCU) loss to learn the relationship between time and predictive uncertainty explicitly.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Instead of single-step prediction, our method trains a probabilistic ensemble to forecast states across variable, randomly sampled time horizons.
- **p. 4 / 4 METHODOLOGY - extractive body cue:** Our methodology is structured around a two-phase framework as shown in fig.

## Source Evidence Cues

- **원문 대조:** 각 dynamics ensemble head는 현재 latent state와 temporal embedding을 조건으로 미래 latent state의 Gaussian mean·isotropic variance를 출력한다. Head별 분포 예측과, head mean 사이 disagreement를 키우는 HCU 항은 별도 요소다. ([PDF p. 5](https://proceedings.iclr.cc/paper_files/paper/2026/file/ad222e6e38e26e3f00d85829b9e02f43-Paper-Conference.pdf#page=5), §4.1, Eq. (1)).
- **p. 5 / 4 METHODOLOGY - extractive body cue:** In the pre-training phase, we introduce a variable-horizon prediction task, where an ensemble of dynamics models learns to forecast future states over randomly sampled time ...
- **p. 6 / 4 METHODOLOGY - extractive body cue:** The composite latent state [ˆst; ˜st] then drives policy optimization, with an auxiliary reward predictor Rθ trained on task-specific rewards to guide imagination-based planning.
- **p. 6 / 4 METHODOLOGY - extractive body cue:** The pre-trained stream-unmodified from pre-training-receives only temporal embeddings and generates latent states ˆst that capture action-agnostic environmental dynamics.
- **p. 4 / 4 METHODOLOGY - extractive body cue:** 2: (1) uncertaintyaware pre-training on action-free video, followed by (2) efficient fine-tuning for downstream con4
- **p. 7 / 4 METHODOLOGY - extractive body cue:** The overall algorithm is in appendix B, and full architectural details appear in appendix C.1.
- **p. 7 / 4 METHODOLOGY - extractive body cue:** Solid curves represent the mean evaluation return across four random seeds, and shaded regions denote the 95% confidence interval. exploiting task-specific action knowledge from the ...
- **Detected method headings:** 4 METHODOLOGY (p. 4); C MODEL DETAILS (p. 15); C.1 MODEL ARCHITECTURE (p. 15)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Risk / failure representation | unsafe state와 uncertainty를 계산한다 | observation, nominal command, history | barrier, risk model, failure classifier, uncertainty 또는 safe set을 추정 | risk/margin/failure state | Formally, each ensemble head outputs the Gaussian parameters for the future latent state: p(i) θ (st+k / st, ∆te k) = N ... | p. 5 (4 METHODOLOGY), p. 5 (4 METHODOLOGY) |
| Filtering / recovery | nominal command를 안전 command로 바꾼다 | nominal action과 safety constraint | QP shield, backup policy, correction, stop 또는 recovery plan을 선택 | safe/recovery action | In the pre-training phase, we introduce a variable-horizon prediction task, where an ensemble of dynamics models learns to forecast future states over ... | p. 5 (4 METHODOLOGY), p. 6 (4 METHODOLOGY) |
| Monitoring / re-entry | 실행 결과를 다시 risk decision에 반영한다 | executed action과 next observation | threshold, update, replan, abort 또는 return-to-task를 수행 | continue/correct/abort state | The composite latent state [ˆst; ˜st] then drives policy optimization, with an auxiliary reward predictor Rθ trained on task-specific rewards to guide ... | p. 6 (4 METHODOLOGY), p. 6 (4 METHODOLOGY) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 4 METHODOLOGY - extractive body cue:** To dynamically balance predictive accuracy against uncertainty representation, we formulate a dual optimization objective: Ltotal = Lpred + λLHCU (4) Here, λ serves as an ...
- **p. 5 / 4 METHODOLOGY - extractive body cue:** We optimize model parameters by minimizing a combined objective.
- **p. 6 / 4 METHODOLOGY - extractive body cue:** The composite latent state [ˆst; ˜st] then drives policy optimization, with an auxiliary reward predictor Rθ trained on task-specific rewards to guide imagination-based planning.
- **p. 6 / 4 METHODOLOGY - extractive body cue:** More critically, this design is tightly coupled with the Horizon-Calibrated Uncertainty (HCU) loss: the embedding serves as a direct conditioning signal for the expected degree ...
- **p. 7 / 4 METHODOLOGY - extractive body cue:** Solid curves represent the mean evaluation return across four random seeds, and shaded regions denote the 95% confidence interval. exploiting task-specific action knowledge from the ...
- **Formal bridge:** state/history and risk h(s) -> filtered/recovery action u_safe -> task utility subject to safety constraint -> low violation/failure probability with useful intervention.
- **Equation/algorithm anchors:** p. 5 (4 METHODOLOGY), p. 5 (4 METHODOLOGY), p. 6 (4 METHODOLOGY).

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Formally, ensemble, head, outputs, Gaussian, parameters, future, latent, state, ensure, effective, extraction, observational, information | observation, uncertainty/risk estimate와 task command | body cue; exact tensor/frame verify |
| State/latent | Formally, ensemble, head, outputs, Gaussian, parameters, future, latent, state, ensure | safe set, recovery state 또는 constraint margin | body cue; notation verify |
| Action/output | novel, framework, variable-horizon, prediction, introduce, Horizon-Calibrated, Uncertainty, HCU, loss, learn | shielded, recovery 또는 safe action | body cue; unit/decoder verify |
| Objective/constraint | dynamically, balance, predictive, accuracy, against, uncertainty, representation, formulate, dual, optimization | task utility subject to safety constraint | equation anchor required |

## Observation–State–Action Interface

- **원문 대조:** 각 dynamics ensemble head는 현재 latent state와 temporal embedding을 조건으로 미래 latent state의 Gaussian mean·isotropic variance를 출력한다. Head별 분포 예측과, head mean 사이 disagreement를 키우는 HCU 항은 별도 요소다. ([PDF p. 5](https://proceedings.iclr.cc/paper_files/paper/2026/file/ad222e6e38e26e3f00d85829b9e02f43-Paper-Conference.pdf#page=5), §4.1, Eq. (1)).
- **p. 4 / 3 PRELIMINARIES - extractive body cue:** It consists of three core components: (i) a representation model zt ∼qϕ(zt/zt-1, ot) that encodes the current observation ot into a latent state zt, (ii) ...
- **p. 5 / 4 METHODOLOGY - extractive body cue:** However, video data inherently lacks explicit action labels and permits multiple plausible futures from identical states.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** A promising frontier is to pre-train these models on large, action-free video datasets (Seo et al., 2022), allowing them to build a foundational understanding of ...
- **p. 4 / 3 PRELIMINARIES - extractive body cue:** This new model layer produces a task-specific state st conditioned on both the agent's action at-1 and the underlying action-free state zt.
- **p. 6 / 4 METHODOLOGY - extractive body cue:** The pre-trained stream-unmodified from pre-training-receives only temporal embeddings and generates latent states ˆst that capture action-agnostic environmental dynamics.
- **p. 6 / 4 METHODOLOGY - extractive body cue:** The composite latent state [ˆst; ˜st] then drives policy optimization, with an auxiliary reward predictor Rθ trained on task-specific rewards to guide imagination-based planning.
- **Normalized interface:** observation=observation, uncertainty/risk estimate와 task command; state=safe set, recovery state 또는 constraint margin; output/action=shielded, recovery 또는 safe action.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | 현재 command의 one-step safety 또는 recovery trajectory horizon; exact lookahead 확인 필요. | 4.2 VARIABLE-HORIZON PREDICTION AND RELATIVE TEMPORAL EMBEDDING Conventional video-based world models predominantly focus on single-step next-frame prediction, neglecting the inherent multi-scale temporal ... | episode/sequence/action-chunk boundary |
| Rate / latency | nominal policy와 safety monitor/filter의 runtime rate를 별도로 기록한다. | This relative encoding strategy provides two critical advantages: it inherently normalizes temporal relationships across videos of varying lengths by representing k as ... | Hz/fps, inference time and control rate |
| Memory | risk score, recent trajectory/history와 recovery state. | not recovered | window and reset |
| Compute | risk inference, barrier/QP solve 또는 backup policy selection이 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 4 METHODOLOGY - extractive body cue:** In the pre-training phase, we introduce a variable-horizon prediction task, where an ensemble of dynamics models learns to forecast future states over randomly sampled time ...
- **p. 6 / 4 METHODOLOGY - extractive body cue:** The composite latent state [ˆst; ˜st] then drives policy optimization, with an auxiliary reward predictor Rθ trained on task-specific rewards to guide imagination-based planning.
- **p. 6 / 4 METHODOLOGY - extractive body cue:** The pre-trained stream-unmodified from pre-training-receives only temporal embeddings and generates latent states ˆst that capture action-agnostic environmental dynamics.
- **p. 4 / 4 METHODOLOGY - extractive body cue:** 2: (1) uncertaintyaware pre-training on action-free video, followed by (2) efficient fine-tuning for downstream con4
- **p. 7 / 4 METHODOLOGY - extractive body cue:** Solid curves represent the mean evaluation return across four random seeds, and shaded regions denote the 95% confidence interval. exploiting task-specific action knowledge from the ...
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** The somewhat larger performance variance of HAUWM on tasks like Dial Turn is an expected trade-off of our ensemble-based architecture, which, while enabling superior average ...

## Method-Specific Formal Details

- **Body-defined terms:** Formally, ensemble, head, outputs, Gaussian, parameters, future, latent, state, ensure, effective, extraction, observational, information, employ, widely, encoderdecoder, architecture, Dreamer, style.
- **Relevant PDF headings:** 4 METHODOLOGY (p. 4); C MODEL DETAILS (p. 15); C.1 MODEL ARCHITECTURE (p. 15).

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Risk / failure representation | 5.1 EXPERIMENTAL SETUP Benchmark Environments. | p. 7 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS) |
| Filtering / recovery | Performance (RQ1): Does HAUWM lead to improved sample efficiency and final performance on downstream RL tasks compared to state-of-the-art methods? | p. 7 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS) |
| Monitoring / re-entry | In the imitation learning setting, HAUWM achieves stateof-the-art performance, outperforming baselines in several tasks and performing competitively in Drawer Close. | p. 9 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS) |

## Failure and Ablation Link

- **p. 8 / 5 EXPERIMENTS - extractive body cue:** First, to verify the necessity of our core contribution, we trained a variant without the Horizon-Calibrated Uncertainty loss (w/o HCU).
- **p. 7 / 5 EXPERIMENTS - extractive body cue:** Ablation (RQ2): What are the relative contributions of the core components of HAUWM?
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** We conduct a series of ablation studies to dissect the contributions of HAUWM's key components and validate our design choices, and record results in table ...
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** Furthermore, HAUWM shows strong performance in the offline RL, where learning from a fixed dataset without online interaction is required.
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** For additional ablation studies examining the scaling function k and the number of ensemble dynamics heads M, refer to the appendix E.4 and appendix E.5.
- **p. 21 / Figure/Table caption - extractive body cue:** Table 6: Ablation on ensemble size M. Performance peaks at M = 7, confirming that moderate ensemble diversity yields the best downstream control performance. Number ...
- **p. 21 / Figure/Table caption - extractive body cue:** Table 5: Ablation on the scaling function in the HCU loss (eq. (3)). Linear scaling achieves the best performance and training stability across all tasks. ...

## Reproduction Checklist

[공통 검토 기준](../../../research/READING_STATUS.md#note-checks)

## Verification Questions

- **Evidence anchors reviewed:** method p. 5 (4 METHODOLOGY), p. 5 (4 METHODOLOGY), p. 6 (4 METHODOLOGY), p. 6 (4 METHODOLOGY), p. 4 (4 METHODOLOGY), p. 7 (4 METHODOLOGY), objective p. 5 (4 METHODOLOGY), p. 5 (4 METHODOLOGY), p. 6 (4 METHODOLOGY), p. 6 (4 METHODOLOGY), p. 7 (4 METHODOLOGY), temporal p. 6 (4 METHODOLOGY), p. 6 (4 METHODOLOGY), p. 5 (4 METHODOLOGY), p. 5 (4 METHODOLOGY), p. 9 (5 EXPERIMENTS), p. 1 (ABSTRACT).
