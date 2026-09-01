# Method - Cross-Embodiment Offline Reinforcement Learning for Heterogeneous Robot Datasets

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (22 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://iclr.cc/virtual/2026/poster/10010454; PDF retrieval source: https://arxiv.org/pdf/2602.18025. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 4 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 5 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 1 (ABSTRACT), p. 2 (1 INTRODUCTION)): Specifically, we encode each action with an action encoder to obtain a latent action vector, which we then concatenate with the latent representation of the URMA encoder.

## Method Body Digest

- **p. 4 / 1 INTRODUCTION - extractive PDF cue:** Specifically, we encode each action with an action encoder to obtain a latent action vector, which we then concatenate with the latent representation of the ...
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** For example, implicit Q-learning (IQL) (Kostrikov et al., 2021) first fits a state value function Vψ(s) via expectile regression to capture an upper expectile of ...
- **p. 5 / 1 INTRODUCTION - extractive PDF cue:** We pre-train via offline RL on a dataset excluding one robot, then finetune that robot with pre-trained networks, comparing it to a model trained without ...
- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** This trend has also begun to influence robotics, where scaling transformer-based architectures and training them on large, heterogeneous robot datasets have produced "robot foundation models" ...
- **p. 1 / ABSTRACT - extractive PDF cue:** To mitigate this, we introduce an embodiment-based grouping strategy in which robots are clustered by morphological similarity and the model is updated with a group ...
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** To mitigate these conflicts, we propose a simple, static grouping strategy that represents each robot as a morphology graph and clusters robots by graph-based distances; ...
- **p. 3 / 1 INTRODUCTION - extractive PDF cue:** To fill this gap, we introduce the new benchmark that systematically combines offline RL with cross-embodiment learning, analyze the interactions between these paradigms, and propose ...
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** 2 RELATED WORKS 2.1 OFFLINE RL Offline RL aims to learn a policy that maximizes cumulative reward using only a static dataset of environment interactions ...

## Design Rationale

- **p. 4 / 1 INTRODUCTION - extractive PDF cue:** 3.3 NETWORK ARCHITECTURE In this section, we present our approach to cross-embodiment learning in an offline RL setting.
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** To address this, we propose a novel group-task update strategy based on robot embodiment information.
- **p. 5 / 1 INTRODUCTION - extractive PDF cue:** To address this issue, we propose a novel mitigation strategy that groups robots according to their embodiment, thus reducing gradient conflicts.

## Source Evidence Cues

- **p. 4 / 1 INTRODUCTION - extractive PDF cue:** Specifically, we encode each action with an action encoder to obtain a latent action vector, which we then concatenate with the latent representation of the ...
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** For example, implicit Q-learning (IQL) (Kostrikov et al., 2021) first fits a state value function Vψ(s) via expectile regression to capture an upper expectile of ...
- **p. 5 / 1 INTRODUCTION - extractive PDF cue:** We pre-train via offline RL on a dataset excluding one robot, then finetune that robot with pre-trained networks, comparing it to a model trained without ...
- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** This trend has also begun to influence robotics, where scaling transformer-based architectures and training them on large, heterogeneous robot datasets have produced "robot foundation models" ...
- **p. 1 / ABSTRACT - extractive PDF cue:** To mitigate this, we introduce an embodiment-based grouping strategy in which robots are clustered by morphological similarity and the model is updated with a group ...
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** To mitigate these conflicts, we propose a simple, static grouping strategy that represents each robot as a morphology graph and clusters robots by graph-based distances; ...
- **p. 3 / 1 INTRODUCTION - extractive PDF cue:** To fill this gap, we introduce the new benchmark that systematically combines offline RL with cross-embodiment learning, analyze the interactions between these paradigms, and propose ...
- **Detected method headings:** A USE OF LARGE LANGUAGE MODELS (LLMS) (p. 12)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Fixed-data support | 온라인 탐색 없이 transition/action 분포를 정의한다 | offline trajectories와 metadata | dataset support, behavior distribution과 task return을 정리 | training batch/support | Specifically, we encode each action with an action encoder to obtain a latent action vector, which we then concatenate with the latent ... | p. 4 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Value / uncertainty update | dataset 밖 action의 과대추정을 억제한다 | batch transition과 value parameters | conservative, implicit, uncertainty 또는 behavior-regularized update를 수행 | Q/V/uncertainty estimate | For example, implicit Q-learning (IQL) (Kostrikov et al., 2021) first fits a state value function Vψ(s) via expectile regression to capture an ... | p. 2 (1 INTRODUCTION), p. 5 (1 INTRODUCTION) |
| Policy extraction / deployment | 학습된 value를 실행 action으로 변환한다 | value와 behavior support | argmax, advantage weighting, sequence decoding 또는 constraint filtering을 적용 | dataset-supported action | We pre-train via offline RL on a dataset excluding one robot, then finetune that robot with pre-trained networks, comparing it to a ... | p. 5 (1 INTRODUCTION), p. 1 (1 INTRODUCTION) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** 2 RELATED WORKS 2.1 OFFLINE RL Offline RL aims to learn a policy that maximizes cumulative reward using only a static dataset of environment interactions ...
- **p. 3 / 1 INTRODUCTION - extractive PDF cue:** Unlike the standard multi-task RL setting, where a single robot embodiment solves multiple tasks with different rewards or goals, here multiple robot embodiments solve a ...
- **p. 5 / 1 INTRODUCTION - extractive PDF cue:** These findings indicate that effective crossembodiment learning requires methods that minimize negative transfer while maximizing positive transfer.
- **p. 8 / 1 INTRODUCTION - extractive PDF cue:** 5.3 EMBODIMENT-GROUPED OFFLINE RL UPDATE Algorithm 1 Embodiment-Grouped Offline RL Require: Robot groups {G1, . . . , GM}, dataset D Ensure: Policy θπ; critics/targets ...
- **p. 1 / ABSTRACT - extractive PDF cue:** To mitigate this, we introduce an embodiment-based grouping strategy in which robots are clustered by morphological similarity and the model is updated with a group ...
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** To mitigate these conflicts, we propose a simple, static grouping strategy that represents each robot as a morphology graph and clusters robots by graph-based distances; ...
- **Formal bridge:** dataset transition (s,a,r,s′) -> dataset-supported policy action -> offline value with OOD control -> offline return and deployment safety.
- **Equation/algorithm anchors:** p. 7 (1 INTRODUCTION), p. 1 (ABSTRACT), p. 2 (1 INTRODUCTION), p. 6 (1 INTRODUCTION), p. 7 (1 INTRODUCTION), p. 8 (1 INTRODUCTION).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | EXPERIMENTAL, SETUP, PROBLEM, SETTING, study, multi-embodiment, offline, where, single, policy, must, control, multiple, robot | dataset state/observation, action, reward와 return-to-go | body cue; exact tensor/frame verify |
| State/latent | EXPERIMENTAL, SETUP, PROBLEM, SETTING, study, multi-embodiment, offline, where, single, policy | Q/value 또는 sequence-policy state | body cue; notation verify |
| Action/output | NETWORK, ARCHITECTURE, section, present, cross-embodiment, learning, offline, setting, address, novel | dataset-supported action sequence | body cue; unit/decoder verify |
| Objective/constraint | RELATED, WORKS, OFFLINE, aims, learn, policy, maximizes, cumulative, reward, only | offline value with OOD control | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 1 INTRODUCTION - extractive PDF cue:** 3 EXPERIMENTAL SETUP 3.1 PROBLEM SETTING We study multi-embodiment offline RL, where a single policy must control multiple robot morphologies under a common state-action interface.
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** Finally, the policy πϕ(a / s) is extracted via advantage-weighted BC, avoiding any need to evaluate out-of-distribution actions.
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** 2 RELATED WORKS 2.1 OFFLINE RL Offline RL aims to learn a policy that maximizes cumulative reward using only a static dataset of environment interactions ...
- **p. 3 / 1 INTRODUCTION - extractive PDF cue:** In this way, the same policy πθ(a / s, f morph(τ)) can generalize across embodiments by conditioning on these universal state features.
- **p. 4 / 1 INTRODUCTION - extractive PDF cue:** The central challenge is to train a single network across robots whose state and action dimensions differ.
- **p. 4 / 1 INTRODUCTION - extractive PDF cue:** To facilitate offline RL, we further extend URMA by introducing a state-action value function (Q-function).
- **p. 6 / 1 INTRODUCTION - extractive PDF cue:** (1) in which Q(s, a) denotes the learned state-action value function and V (s) denotes the learned state value function.
- **Normalized interface:** observation=dataset state/observation, action, reward와 return-to-go; state=Q/value 또는 sequence-policy state; output/action=dataset-supported action sequence.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | offline trajectory/discounted return horizon; deployment horizon과 분리한다. | During training, we record the tuple (st, at, st+1, rt, dt) at each time step to capture the state, action, next state, ... | episode/sequence/action-chunk boundary |
| Rate / latency | training은 batch update, inference는 environment control tick; exact values 확인 필요. | Preprint 0 5 10 Update steps ×103 0 15 30 45 60 Eval/Episode Return (a) Badger 0 5 10 15 20 25 ... | Hz/fps, inference time and control rate |
| Memory | fixed dataset, value/policy parameters와 optional context/history. | not recovered | window and reset |
| Compute | dataset size, conservative/value update와 sequence/action decoding이 비용을 결정한다. | IQL performance across datasets (mean ± standard error over 5 seeds). | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 1 INTRODUCTION - extractive PDF cue:** We pre-train via offline RL on a dataset excluding one robot, then finetune that robot with pre-trained networks, comparing it to a model trained without ...
- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** This trend has also begun to influence robotics, where scaling transformer-based architectures and training them on large, heterogeneous robot datasets have produced "robot foundation models" ...
- **p. 10 / 1 INTRODUCTION - extractive PDF cue:** 5, the wall-clock training time grows substantially with M.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Specifically, encode, action, encoder, obtain, latent, vector, then, concatenate, representation, URMA, example, implicit, Q-learning, IQL, Kostrikov, first, fits, state, value.
- **Relevant PDF headings:** A USE OF LARGE LANGUAGE MODELS (LLMS) (p. 12).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Fixed-data support | Preprint (a) Embodiment-based similarity matrix (b) Average gradient cosine similarity matrix (c) Embodiment-based similarity vs. mean gradient cosine similarity Figure 3: (a) ... | p. 7 (1 INTRODUCTION), p. 8 (1 INTRODUCTION) |
| Value / uncertainty update | Compared to the IQL cross-embodiment baseline, the average improvement in the Suboptimal datasets 70% is 7.15% for PCGrad, 18.33% for SEL and ... | p. 9 (1 INTRODUCTION), p. 10 (1 INTRODUCTION) |
| Policy extraction / deployment | From the table, EG achieves the most stable and substantial improvement on the 70% Suboptimal Forward dataset (+14.41, +38.34%). | p. 9 (1 INTRODUCTION), p. 8 (1 INTRODUCTION) |

## Failure and Ablation Link

- **p. 10 / 1 INTRODUCTION - extractive PDF cue:** (ii) Sensitivity to the group count M We evaluate the effect of the number of Embodiment Grouping clusters M by sweeping M over {1, 2, ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 1: Comparison of learning curves between cross-embodiment pre-trained networks and net- works trained without cross-embodiment pre-training for Badger, Unitree G1, and Cassie. "leave-one-out" experiment. ...
- **p. 10 / 1 INTRODUCTION - extractive PDF cue:** To remove this effect, we also run a compute-normalized comparison in which, for the IQL baseline, we multiply the total number of optimizer steps K ...
- **p. 8 / 1 INTRODUCTION - extractive PDF cue:** Finally, to assess the effect of our embodiment-based grouping strategy across different learning backbones, we report Embodiment Grouping (EG) counterparts of BC, TD3+BC, and IQL.
- **p. 8 / 1 INTRODUCTION - extractive PDF cue:** We denote these variants as BC+EG, TD3+BC+EG, and IQL+EG (ours), respectively.
- **p. 9 / 1 INTRODUCTION - extractive PDF cue:** The variant that combines IQL with Embodiment Grouping achieves the best average performance.
- **p. 9 / 1 INTRODUCTION - extractive PDF cue:** 6.2 ABLATIONS & COMPUTE-NORMALIZED ANALYSIS This section disentangles design choices in Embodiment Grouping (EG) and the impact of compute.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 4 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 5 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 1 (ABSTRACT), p. 2 (1 INTRODUCTION), objective p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 5 (1 INTRODUCTION), p. 8 (1 INTRODUCTION), p. 1 (ABSTRACT), p. 2 (1 INTRODUCTION), temporal p. 3 (1 INTRODUCTION), p. 5 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 4 (1 INTRODUCTION), p. 8 (1 INTRODUCTION).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
