# PolicyTrim: Boosting Intrinsic Policy Efficiency of Vision-Language-Action Models

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (27 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2606.22540.
> PDF retrieval source: https://arxiv.org/pdf/2606.22540. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ECCV
- Authors: Xianghui Wang, Feng Chen, Wenbo Zhang, Hua Yan, Zixuan Wang, Changsheng Li, Yinjie Lei
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, Vision-Language Model
- Official paper: https://arxiv.org/abs/2606.22540
- Full-text retrieval: https://arxiv.org/pdf/2606.22540
- Code/Project: https://inceptionwang.github.io/PolicyTrim/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (27 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 한 줄 요약과 핵심 기여 두 개를 각 문장에 인용한 판본의 원문에서 확인했다.

## Why This Paper Is Here

PolicyTrim은 VLA를 강화학습으로 후학습해 한 번에 믿고 실행할 행동 구간을 늘리고 과제를 마치는 데 필요한 동작 수를 줄인다. [PDF 1쪽](https://arxiv.org/pdf/2606.22540v3#page=1)

## Problem and Motivation

- **p. 1 / 1 Introduction - extractive body cue:** Vision-Language-Action (VLA) models integrate visual perception, language understanding, and action generation into a single end-to-end framework, establishing a scalable paradigm for general-purpose robotic manipulation [2-4,10-12,19, ...
- **p. 3 / X. Wang et al - extractive body cue:** The main contributions of this work are summarized as follows: - We identify policy efficiency as a critical yet overlooked deployment bottleneck for VLA models ...
- **p. 4 / X. Wang et al - extractive body cue:** However, existing GRPO approaches for VLAs universally rely on binary success rewards [6, 14, 21, 28], which create two fundamental limitations.
- **p. 2 / X. Wang et al - extractive body cue:** However, the policy efficiency bottleneck of the models is largely unexplored, governed by the effective executable length of predicted action chunks and the total physical ...
- **p. 1 / Body text (section not recovered) - extractive body cue:** Vision-Language-Action (VLA) models provide a unified paradigm for robotic manipulation, yet their real-world deployment is often bottlenecked by execution efficiency.
- **p. 2 / X. Wang et al - extractive body cue:** Consequently, intrinsic policy efficiency remains the primary bottleneck for deployed VLA systems.

## Core Idea

- **p. 3 / X. Wang et al - extractive body cue:** The main contributions of this work are summarized as follows: - We identify policy efficiency as a critical yet overlooked deployment bottleneck for VLA models ...
- **p. 5 / 3 Method - extractive body cue:** We propose a two-stage posttraining framework that extends the executable action horizon per inference and reduces the number of steps required to complete a task ...
- **p. 1 / Body text (section not recovered) - extractive body cue:** Ultimately, our framework delivers up to a 5.83× end-to-end deployment speedup without compromising task success rates.
- **p. 3 / X. Wang et al - extractive body cue:** PolicyTrim 3 In this paper, we propose PolicyTrim, a two-stage RL-based post-training framework that enhances the policy efficiency of VLA models through reliable chunk extension ...
- **p. 5 / 3 Method - extractive body cue:** At an arbitrary decision step t, the policy πθ processes the current visual observation ot and language instruction l to predict a sequence of future ...
- **p. 15 / 2.48 Method - extractive body cue:** Moreover, prediction errors accumulate along action chunks due to distribution shift, causing the policy to take redundant corrective actions that further inflate the total execution ...
- **p. 15 / 2.48 Method - extractive body cue:** While compute-centric methods reduce per-step inference latency, PolicyTrim targets the total number of forward inference calls, a dimension existing acceleration techniques leave entirely unaddressed.
- **p. 21 / B Implementation Details - extractive body cue:** We applied group-relative reward normalization and updated the policy directly from rollout returns, without a critic

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | At an arbitrary decision step t, the policy πθ processes the current visual observation ot and language instruction l to predict a sequence of future actions at:t+H in parallel, where H denotes ... | image/video, language instruction, proprioception과 history | p. 5 (3 Method), p. 4 (X. Wang et al) |
| State/latent | arbitrary, decision, step, policy, processes, current, visual, observation, language, instruction, predict, sequence | language-grounded task state와 action-policy context | p. 5 (3 Method), p. 4 (X. Wang et al), p. 1 (Body text (section not recovered)) |
| Output/action | Visual token pruning [16,24,43] and action tokenization compression [32,47] reduce input and output overhead respectively. | continuous action, pose 또는 action chunk | p. 4 (X. Wang et al), p. 1 (Body text (section not recovered)), p. 15 (2.48 Method) |
| Objective/outcome | 2, the framework decouples this enhancement objective into two progressive learning stages targeting | instruction following, task success, generalization과 latency | p. 5 (3 Method), p. 15 (2.48 Method), p. 21 (B Implementation Details) |

## Main Claims and Actual Contribution

- 실행 구간을 늘려도 성공하는 경우와 더 적은 동작으로 성공하는 경우를 보상에 반영하고 재현하기 어려운 단축 경로를 억제한다. [PDF 1쪽](https://arxiv.org/pdf/2606.22540v3#page=1) · [PDF 5쪽](https://arxiv.org/pdf/2606.22540v3#page=5) · [PDF 6쪽](https://arxiv.org/pdf/2606.22540v3#page=6) · [PDF 7쪽](https://arxiv.org/pdf/2606.22540v3#page=7)
- 여러 정책에서 성공률, 실제 동작 수, 정책 호출 수를 나누어 측정해 행동 청크 사용 효율을 비교했다. [PDF 10쪽](https://arxiv.org/pdf/2606.22540v3#page=10) · [PDF 11쪽](https://arxiv.org/pdf/2606.22540v3#page=11) · [PDF 12쪽](https://arxiv.org/pdf/2606.22540v3#page=12)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 9 (4 Experiment), p. 12 (Figure/Table caption) |
| Embodiment/environment | We evaluate on three diverse benchmarks including LIBERO [25], ManiSkill [41], Meta-World [30] and further validate its sim-to-real transfer on a physical robot platform. | hardware/simulator version and reset protocol | p. 9 (4 Experiment), p. 9 (4 Experiment) |
| Dataset/benchmark | We evaluate on three diverse benchmarks including LIBERO [25], ManiSkill [41], Meta-World [30] and further validate its sim-to-real transfer on a physical robot platform. | role, split, size and leakage | p. 9 (4 Experiment), p. 9 (4 Experiment) |
| Metric | Fig. 1: Intrinsic policy inefficiency in deployed VLA models manifests along two di- mensions. (a) Repeated rollouts on identical tasks reveal substantial variance in step counts, indicating concise execution paths exist but ... | definition, denominator, direction and uncertainty | p. 2 (Figure/Table caption), p. 9 (4 Experiment), p. 25 (Figure/Table caption) |
| Baseline/ablation | Fig. 3: Qualitative comparison on randomly sampled LIBERO tasks. Under identi- cal configurations, the baseline incurs redundant physical actions, whereas PolicyTrim achieves task completion in roughly half the steps. divergence among t ... | fair input/data/compute/action matching | p. 11 (Figure/Table caption), p. 23 (Figure/Table caption), p. 26 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 27 / Figure/Table caption - extractive body cue:** Fig. 7: Failure case without group-anchored stability regularization. The pol- icy approaches the bowl with insufficient clearance, causing a collision and task failure. In this ...
- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 1: Intrinsic policy inefficiency in deployed VLA models manifests along two di- mensions. (a) Repeated rollouts on identical tasks reveal substantial variance in step ...
- **p. 25 / Figure/Table caption - extractive body cue:** Fig. 6: Real-world execution visualization on the FlipMug task. C.5 Robustness under Visual Perturbations We further evaluate PolicyTrim under visual distribution shifts in simulation. Specifically, ...
- **p. 25 / Figure/Table caption - extractive body cue:** Table 10: Simulation robustness results on LIBERO-Spatial under visual perturba- tions. We report SR / Step, where SR is success rate in % and Step ...
- **p. 26 / Figure/Table caption - extractive body cue:** Table 11: Horizon-sweep baseline for π0.5. Fixed larger horizons degrade success rate, while PolicyTrim learns to extend the reliable horizon through RL post-training.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 3 (X. Wang et al), p. 4 (X. Wang et al), p. 2 (X. Wang et al), p. 1 (Body text (section not recovered)), p. 5 (3 Method)이다.
