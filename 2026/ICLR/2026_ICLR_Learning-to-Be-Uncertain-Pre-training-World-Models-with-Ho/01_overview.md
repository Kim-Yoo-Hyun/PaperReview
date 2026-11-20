# Learning to Be Uncertain: Pre-training World Models with Horizon-Calibrated Uncertainty

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (21 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://iclr.cc/virtual/2026/poster/10007319.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/245358. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICLR
- Authors: Shenghua Wan, Le Gan, De-Chuan Zhan
- Primary track: World models, safety, uncertainty, and recovery
- Tier: REFERENCE
- Tags: Robotics, world model, uncertainty, long-horizon prediction, model-based reinforcement learning
- Official paper: https://iclr.cc/virtual/2026/poster/10007319
- Full-text retrieval: https://proceedings.iclr.cc/paper_files/paper/2026/file/ad222e6e38e26e3f00d85829b9e02f43-Paper-Conference.pdf
- Code/Project: https://iclr.cc/virtual/2026/poster/10007319
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (21 pages; PyMuPDF text; title-token overlap first two pages=1.0)

> DOC-QA1 (2026-10-23): 제어문자·깨진 추출 구간과 직접 연결된 표 항목을 PDF 페이지 이미지와 대조했다. 확인 범위·원문 URL·페이지·수정 이력은 [대조 기록](../../../work/sources/pdf_note_review_2026-10-23.json)에 있다. 노트 전체의 정독이나 모든 기존 주장에 대한 재검증을 뜻하지 않으며 reading status는 유지한다.

## Why This Paper Is Here

World models, safety, uncertainty, and recovery의 safety 문제를 이해하기 위해 읽는다. 본문은 1 (b), where standard RSSM-based baselines (APV and ContextWM), even when equipped with ensemble heads, exhibit artificially low and nearly flat predictive uncertainty that fails to grow with the prediction horizon, in ...를 문제로 두고, We propose a novel framework using variable-horizon prediction and introduce the Horizon-Calibrated Uncertainty (HCU) loss to learn the relationship between time and predictive uncertainty explicitly.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** Pre-training world models on large, action-free video datasets offers a promising path toward generalist agents, but a fundamental flaw undermines this paradigm.
- **p. 1 / ABSTRACT - extractive body cue:** Prevailing methods train models to predict a single, deterministic future, an objective that is ill-posed for inherently stochastic environments where actions are unknown.
- **p. 1 / ABSTRACT - extractive body cue:** We contend that a world model should instead learn a structured, probabilistic representation of the future where predictive uncertainty correctly scales with the temporal horizon.
- **p. 1 / ABSTRACT - extractive body cue:** To achieve this, we introduce a pre-training framework, Horizon-cAlibrated Uncertainty World Model (HAUWM), built on a probabilistic ensemble that predicts frames at randomly sampled future ...
- **p. 1 / ABSTRACT - extractive body cue:** The core of our method is a Horizon-Calibrated Uncertainty (HCU) loss, which explicitly shapes the latent space by encouraging predictive variance to grow as the ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** 1 (b), where standard RSSM-based baselines (APV and ContextWM), even when equipped with ensemble heads, exhibit artificially low and nearly flat predictive uncertainty that fails ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** However, a critical flaw undermines current approaches.

## Core Idea

- **p. 2 / 1 INTRODUCTION - extractive body cue:** We propose a novel framework using variable-horizon prediction and introduce the Horizon-Calibrated Uncertainty (HCU) loss to learn the relationship between time and predictive uncertainty explicitly.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Instead of single-step prediction, our method trains a probabilistic ensemble to forecast states across variable, randomly sampled time horizons.
- **p. 4 / 4 METHODOLOGY - extractive body cue:** Our methodology is structured around a two-phase framework as shown in fig.
- **p. 5 / 4 METHODOLOGY - extractive body cue:** To explicitly preserve future-state diversity, we introduce a Horizon-Calibrated Uncertainty (HCU) loss.
- **p. 5 / 4 METHODOLOGY - extractive body cue:** In the pre-training phase, we introduce a variable-horizon prediction task, where an ensemble of dynamics models learns to forecast future states over randomly sampled time ...
- **원문 대조:** 각 dynamics ensemble head는 현재 latent state와 temporal embedding을 조건으로 미래 latent state의 Gaussian mean·isotropic variance를 출력한다. Head별 분포 예측과, head mean 사이 disagreement를 키우는 HCU 항은 별도 요소다. ([PDF p. 5](https://proceedings.iclr.cc/paper_files/paper/2026/file/ad222e6e38e26e3f00d85829b9e02f43-Paper-Conference.pdf#page=5), §4.1, Eq. (1)).
- **p. 6 / 4 METHODOLOGY - extractive body cue:** The composite latent state [ˆst; ˜st] then drives policy optimization, with an auxiliary reward predictor Rθ trained on task-specific rewards to guide imagination-based planning.
- **p. 6 / 4 METHODOLOGY - extractive body cue:** The pre-trained stream-unmodified from pre-training-receives only temporal embeddings and generates latent states ˆst that capture action-agnostic environmental dynamics.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Latent transition output | 원문 대조: 각 dynamics ensemble head는 현재 latent state와 temporal embedding을 조건으로 미래 latent state의 Gaussian mean·isotropic variance를 출력한다. Head별 분포 예측과, head mean 사이 disagreement를 키우는 HCU 항은 별도 요소다. ([PDF p. 5](https://proceedings.iclr.cc/paper_files/paper/2026/file/ad222e6e38e26e3f00d85829b9e02f43-Paper-Conference.pdf#page=5), §4.1, Eq. (1)) | 현재 state·temporal embedding → Gaussian parameter | [PDF p. 5](https://proceedings.iclr.cc/paper_files/paper/2026/file/ad222e6e38e26e3f00d85829b9e02f43-Paper-Conference.pdf#page=5), §4.1, Eq. (1) |
| State/latent | Formally, ensemble, head, outputs, Gaussian, parameters, future, latent, state, ensure, effective, extraction | safe set, recovery state 또는 constraint margin | p. 5 (4 METHODOLOGY), p. 4 (3 PRELIMINARIES), p. 5 (4 METHODOLOGY) |
| Output/action | It consists of three core components: (i) a representation model zt ∼qϕ(zt/zt-1, ot) that encodes the current observation ot into a latent state zt, (ii) a latent transition model ˆzt ∼pϕ(ˆzt/zt-1) that ... | shielded, recovery 또는 safe action | p. 4 (3 PRELIMINARIES), p. 5 (4 METHODOLOGY), p. 1 (1 INTRODUCTION) |
| Objective/outcome | To dynamically balance predictive accuracy against uncertainty representation, we formulate a dual optimization objective: Ltotal = Lpred + λLHCU (4) Here, λ serves as an adaptive counterweight that maintains the essential tension ... | task return과 violation/failure probability | p. 5 (4 METHODOLOGY), p. 5 (4 METHODOLOGY), p. 6 (4 METHODOLOGY) |

## Main Claims and Actual Contribution

- **p. 2 / 1 INTRODUCTION - extractive body cue:** We propose a novel framework using variable-horizon prediction and introduce the Horizon-Calibrated Uncertainty (HCU) loss to learn the relationship between time and predictive uncertainty explicitly.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Instead of single-step prediction, our method trains a probabilistic ensemble to forecast states across variable, randomly sampled time horizons.
- **p. 4 / 4 METHODOLOGY - extractive body cue:** Our methodology is structured around a two-phase framework as shown in fig.
- **p. 5 / 4 METHODOLOGY - extractive body cue:** To explicitly preserve future-state diversity, we introduce a Horizon-Calibrated Uncertainty (HCU) loss.
- **p. 5 / 4 METHODOLOGY - extractive body cue:** In the pre-training phase, we introduce a variable-horizon prediction task, where an ensemble of dynamics models learns to forecast future states over randomly sampled time ...
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** In the imitation learning setting, HAUWM achieves stateof-the-art performance, outperforming baselines in several tasks and performing competitively in Drawer Close.
- **p. 7 / 5 EXPERIMENTS - extractive body cue:** Performance (RQ1): Does HAUWM lead to improved sample efficiency and final performance on downstream RL tasks compared to state-of-the-art methods?
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** 3, our method, HAUWM, achieves state-of-the-art sample efficiency and final performance on the majority of the tested benchmarks.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 9 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS) |
| Embodiment/environment | 5.1 EXPERIMENTAL SETUP Benchmark Environments. | hardware/simulator version and reset protocol | p. 7 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS) |
| Dataset/benchmark | Therefore, we fine-tune our pre-trained model using established algorithms for imitation learning (IL) and offline RL on several benchmark tasks, with standard VMAIL (Rafailov et al., 2021b) and LOMPO (Rafailov et al., ... | role, split, size and leakage | p. 7 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS) |
| Metric | Table 2: Performance of HAUWM and baselines on diverse downstream learning paradigms, includ- ing imitation and offline RL. All scores are normalized returns, reported as the mean and standard deviation across 10 ... | definition, denominator, direction and uncertainty | p. 10 (Figure/Table caption), p. 8 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS) |
| Baseline/ablation | Performance (RQ1): Does HAUWM lead to improved sample efficiency and final performance on downstream RL tasks compared to state-of-the-art methods? | fair input/data/compute/action matching | p. 7 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 7 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 6 / 4 METHODOLOGY - extractive body cue:** To maintain compatibility with this stream's original design, we condition it on relative temporal embeddings ∆te k=1 (as defined in Section 4.2), injecting a Gaussian ...
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** This led to significant performance degradation, particularly on the DMC benchmark, confirming that explicitly modeling structured temporal uncertainty is critical for learning robust dynamics representations.
- **p. 7 / 5 EXPERIMENTS - extractive body cue:** Robustness (RQ4): Can our pre-training world model generalize to diverse downstream learning paradigms?
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** We attribute this strong performance to our core contribution: by pre-training a model that explicitly represents temporal uncertainty, the agent builds a more robust and ...
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** This suggests that the structured uncertainty learned during pre-training provides a robust foundation for mimicking experts, where understanding plausible future states is crucial.
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** Therefore, we fine-tune our pre-trained model using established algorithms for imitation learning (IL) and offline RL on several benchmark tasks, with standard VMAIL (Rafailov et ...

## Why Read It

World models, safety, uncertainty, and recovery의 safety 문제를 이해하기 위해 읽는다. 본문은 1 (b), where standard RSSM-based baselines (APV and ContextWM), even when equipped with ensemble heads, exhibit artificially low and nearly flat predictive uncertainty that fails to grow with the prediction horizon, in ...를 문제로 두고, We propose a novel framework using variable-horizon prediction and introduce the Horizon-Calibrated Uncertainty (HCU) loss to learn the relationship between time and predictive uncertainty explicitly.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 4 (3 PRELIMINARIES), p. 4 (3 PRELIMINARIES), p. 5 (4 METHODOLOGY) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
