# Method - MOPO: Model-based Offline Policy Optimization

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2005.13239; PDF retrieval source: https://arxiv.org/pdf/2005.13239. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 4 (3 Preliminaries), p. 4 (3 Preliminaries), p. 7 (3 Preliminaries), p. 1 (Abstract), p. 2 (1 Introduction), p. 6 (3 Preliminaries)): 4 MOPO: Model-Based Offline Policy Optimization Unlike model-free methods, our goal is to design an offline model-based reinforcement learning algorithm that can take actions that are not strictly within the ...

## Method Body Digest

- **p. 4 / 3 Preliminaries - extractive body cue:** 4 MOPO: Model-Based Offline Policy Optimization Unlike model-free methods, our goal is to design an offline model-based reinforcement learning algorithm that can take actions that ...
- **p. 4 / 3 Preliminaries - extractive body cue:** Then we maximize the conservative estimation of the return by an off-the-shelf reinforcement learning algorithm, which gives MOPO, a generic model-based off-policy algorithm (Section 4.2).
- **p. 7 / 3 Preliminaries - extractive body cue:** Following MBPO, we model the dynamics using a neural network that outputs a Gaussian distribution over the next state and reward3: bTθ,φ(st+1, r/st, at) = ...
- **p. 1 / Abstract - extractive body cue:** Our algorithm, Model-based Offline Policy Optimization (MOPO), outperforms standard model-based RL algorithms and prior state-of-the-art model-free offline RL algorithms on existing offline RL benchmarks and ...
- **p. 2 / 1 Introduction - extractive body cue:** We empirically compare this approach, model-based offline policy optimization (MOPO), to both MBPO and existing state-of-the-art model-free offline RL algorithms.
- **p. 6 / 3 Preliminaries - extractive body cue:** Algorithm 1 Framework for Model-based Offline Policy Optimization (MOPO) with Reward Penalty Require: Dynamics model bT with admissible error estimator u(s, a); constant λ.
- **p. 1 / Abstract - extractive body cue:** Instead, we propose to modify the existing model-based RL methods by applying them with rewards artificially penalized by the uncertainty of the dynamics.
- **p. 4 / 3 Preliminaries - extractive body cue:** Moreover, equation (2) suggests that a policy that obtains high reward in the estimated MDP while also minimizing Gπ c M will obtain high reward ...

## Design Rationale

- **p. 2 / 1 Introduction - extractive body cue:** The primary contribution of this work is an offline model-based RL algorithm that optimizes a policy in an uncertainty-penalized MDP, where the reward function is ...
- **p. 1 / Abstract - extractive body cue:** Instead, we propose to modify the existing model-based RL methods by applying them with rewards artificially penalized by the uncertainty of the dynamics.
- **p. 5 / 3 Preliminaries - extractive body cue:** We will analyze our framework under the assumption that we have access to an oracle uncertainty quantification module that provides an upper bound on the ...

## Source Evidence Cues

- **p. 4 / 3 Preliminaries - extractive body cue:** 4 MOPO: Model-Based Offline Policy Optimization Unlike model-free methods, our goal is to design an offline model-based reinforcement learning algorithm that can take actions that ...
- **p. 4 / 3 Preliminaries - extractive body cue:** Then we maximize the conservative estimation of the return by an off-the-shelf reinforcement learning algorithm, which gives MOPO, a generic model-based off-policy algorithm (Section 4.2).
- **p. 7 / 3 Preliminaries - extractive body cue:** Following MBPO, we model the dynamics using a neural network that outputs a Gaussian distribution over the next state and reward3: bTθ,φ(st+1, r/st, at) = ...
- **p. 1 / Abstract - extractive body cue:** Our algorithm, Model-based Offline Policy Optimization (MOPO), outperforms standard model-based RL algorithms and prior state-of-the-art model-free offline RL algorithms on existing offline RL benchmarks and ...
- **p. 2 / 1 Introduction - extractive body cue:** We empirically compare this approach, model-based offline policy optimization (MOPO), to both MBPO and existing state-of-the-art model-free offline RL algorithms.
- **p. 6 / 3 Preliminaries - extractive body cue:** Algorithm 1 Framework for Model-based Offline Policy Optimization (MOPO) with Reward Penalty Require: Dynamics model bT with admissible error estimator u(s, a); constant λ.
- **p. 1 / Abstract - extractive body cue:** Instead, we propose to modify the existing model-based RL methods by applying them with rewards artificially penalized by the uncertainty of the dynamics.
- **Detected method headings:** C MOPO Practical Algorithm Outline (p. 16); Method (p. 18)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Fixed-data support | 온라인 탐색 없이 transition/action 분포를 정의한다 | offline trajectories와 metadata | dataset support, behavior distribution과 task return을 정리 | training batch/support | 4 MOPO: Model-Based Offline Policy Optimization Unlike model-free methods, our goal is to design an offline model-based reinforcement learning algorithm that can ... | p. 4 (3 Preliminaries), p. 4 (3 Preliminaries) |
| Value / uncertainty update | dataset 밖 action의 과대추정을 억제한다 | batch transition과 value parameters | conservative, implicit, uncertainty 또는 behavior-regularized update를 수행 | Q/V/uncertainty estimate | Then we maximize the conservative estimation of the return by an off-the-shelf reinforcement learning algorithm, which gives MOPO, a generic model-based off-policy ... | p. 4 (3 Preliminaries), p. 7 (3 Preliminaries) |
| Policy extraction / deployment | 학습된 value를 실행 action으로 변환한다 | value와 behavior support | argmax, advantage weighting, sequence decoding 또는 constraint filtering을 적용 | dataset-supported action | Following MBPO, we model the dynamics using a neural network that outputs a Gaussian distribution over the next state and reward3: bTθ,φ(st+1, ... | p. 7 (3 Preliminaries), p. 1 (Abstract) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 3 Preliminaries - extractive body cue:** Moreover, equation (2) suggests that a policy that obtains high reward in the estimated MDP while also minimizing Gπ c M will obtain high reward ...
- **p. 6 / 3 Preliminaries - extractive body cue:** Second, by varying the choice of δ to maximize the RHS of Equation (11), we trade off the risk and the return.
- **p. 3 / 3 Preliminaries - extractive body cue:** The goal in RL is to optimize a policy π(a / s) that maximizes the expected discounted return ηM(π) := E π,T,µ0 [P∞ t=0 γtr(st, ...
- **p. 5 / 3 Preliminaries - extractive body cue:** We observe that f M is conservative in that the return under it bounds from below the true return: ηM(π) ≥ ¯E (s,a)∼ρπ b T ...
- **p. 1 / Abstract - extractive body cue:** We theoretically show that the algorithm maximizes a lower bound of the policy's return under the true MDP.
- **p. 2 / 1 Introduction - extractive body cue:** The primary contribution of this work is an offline model-based RL algorithm that optimizes a policy in an uncertainty-penalized MDP, where the reward function is ...
- **Formal bridge:** dataset transition (s,a,r,s′) -> dataset-supported policy action -> offline value with OOD control -> offline return and deployment safety.
- **Equation/algorithm anchors:** p. 2 (1 Introduction), p. 4 (3 Preliminaries), p. 4 (3 Preliminaries), p. 5 (3 Preliminaries), p. 5 (3 Preliminaries), p. 6 (3 Preliminaries).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | MOPO, Model-Based, Offline, Policy, Optimization, Unlike, model-free, methods, goal, design, reinforcement, learning, algorithm, take | dataset state/observation, action, reward와 return-to-go | body cue; exact tensor/frame verify |
| State/latent | MOPO, Model-Based, Offline, Policy, Optimization, Unlike, model-free, methods, goal, design | Q/value 또는 sequence-policy state | body cue; notation verify |
| Action/output | primary, contribution, offline, model-based, algorithm, optimizes, policy, uncertainty-penalized, MDP, where | dataset-supported action sequence | body cue; unit/decoder verify |
| Objective/constraint | Moreover, equation, suggests, policy, obtains, high, reward, estimated, MDP, while | offline value with OOD control | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 3 Preliminaries - extractive body cue:** 4 MOPO: Model-Based Offline Policy Optimization Unlike model-free methods, our goal is to design an offline model-based reinforcement learning algorithm that can take actions that ...
- **p. 2 / 1 Introduction - extractive body cue:** We argue that it is important for an offline RL algorithm to be equipped with the ability to leave the data support to learn a ...
- **p. 3 / 3 Preliminaries - extractive body cue:** Let Pπ b T ,t(s) denote the probability of being in state s at time step t if actions are sampled according to π and ...
- **p. 3 / 3 Preliminaries - extractive body cue:** We consider the standard Markov decision process (MDP) M = (S, A, T, r, µ0, γ), where S and A denote the state space and ...
- **p. 6 / 3 Preliminaries - extractive body cue:** Equation (11) tells us that the learned policy ˆπ can be as good as any policy π with ϵu(π) ≤δ, or in other words, any ...
- **p. 7 / 3 Preliminaries - extractive body cue:** Following MBPO, we model the dynamics using a neural network that outputs a Gaussian distribution over the next state and reward3: bTθ,φ(st+1, r/st, at) = ...
- **p. 1 / Abstract - extractive body cue:** However, it is also challenging, due to the distributional shift between the offline training data and those states visited by the learned policy.
- **Normalized interface:** observation=dataset state/observation, action, reward와 return-to-go; state=Q/value 또는 sequence-policy state; output/action=dataset-supported action sequence.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | offline trajectory/discounted return horizon; deployment horizon과 분리한다. | The datasets in this benchmark have been generated as follows: random: roll out a randomly initialized policy for 1M steps. medium: partially ... | episode/sequence/action-chunk boundary |
| Rate / latency | training은 batch update, inference는 environment control tick; exact values 확인 필요. | Let Pπ b T ,t(s) denote the probability of being in state s at time step t if actions are sampled according ... | Hz/fps, inference time and control rate |
| Memory | fixed dataset, value/policy parameters와 optional context/history. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | dataset size, conservative/value update와 sequence/action decoding이 비용을 결정한다. | not stated or recoverable in the selected PDF body | hardware, batch and throughput |

## Training vs Inference

- **p. 8 / 5 Experiments - extractive body cue:** Concretely, we train SAC for 1M steps and use the entire training replay buffer as the trajectories for the batch data.
- **p. 8 / 5 Experiments - extractive body cue:** Each number is the normalized score proposed in [18] of the policy at the last iteration of training, averaged over 6 random seeds, ± standard ...
- **p. 9 / 5 Experiments - extractive body cue:** In halfcheetah-jump, the agent is asked to run while jumping as high as possible given an training offline dataset of halfcheetah running.
- **p. 1 / 1 Introduction - extractive body cue:** Reinforcement learning (RL) methods, in contrast, struggle to scale to many real-world applications, e.g., autonomous driving [74] and healthcare [22], because they rely on costly ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** MOPO, Model-Based, Offline, Policy, Optimization, Unlike, model-free, methods, goal, design, reinforcement, learning, algorithm, take, actions, strictly, within, support, behavioral, distribution.
- **Relevant PDF headings:** C MOPO Practical Algorithm Outline (p. 16); Method (p. 18).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Fixed-data support | 5.1 Evaluation on the D4RL benchmark To answer question (1), we evaluate our method on a large subset of datasets in the ... | p. 7 (5 Experiments), p. 8 (5 Experiments) |
| Value / uncertainty update | We compare against several baselines, including the current state-of-the-art model-free offline RL algorithms. | p. 7 (5 Experiments), p. 8 (5 Experiments) |
| Policy extraction / deployment | Table 2: Average returns halfcheetah-jump and ant-angle that require out-of-distribution policy. The MOPO results are averaged over 6 random seeds, ± standard ... | p. 9 (Figure/Table caption), p. 18 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 7 / 5 Experiments - extractive body cue:** To answer question (3), we conduct a complete ablation study to analyze the effect of each module in MOPO in Appendix D.
- **p. 18 / Figure/Table caption - extractive body cue:** Table 3: Ablation study on two D4RL tasks halfcheetah-mixed and walker2d-mixed and two out-of- distribution tasks halfcheetah-jump and ant-angle. We use average returns where the ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: Comparison between vanilla model-based RL (MBPO [29]) with or without model ensembles and vanilla model-free RL (SAC [27]) on two offline RL tasks: ...
- **p. 7 / 5 Experiments - extractive body cue:** (3) How does each component in MOPO affect performance?
- **p. 9 / 6 Conclusion - extractive body cue:** However, uncertainty estimation does not explain the entire difference nor does it explain why model-free methods cannot also enjoy the benefits of uncertainty estimation.
- **p. 9 / 6 Conclusion - extractive body cue:** Our work opens up a number of questions and directions for future work.
- **p. 8 / 5 Experiments - extractive body cue:** In particular, model-free offline RL cannot outperform the best trajectory in the batch dataset, whereas MOPO exceeds the batch max by a significant margin.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (3 Preliminaries), p. 4 (3 Preliminaries), p. 7 (3 Preliminaries), p. 1 (Abstract), p. 2 (1 Introduction), p. 6 (3 Preliminaries), objective p. 4 (3 Preliminaries), p. 6 (3 Preliminaries), p. 3 (3 Preliminaries), p. 5 (3 Preliminaries), p. 1 (Abstract), p. 2 (1 Introduction), temporal p. 8 (5 Experiments), p. 3 (3 Preliminaries), p. 8 (5 Experiments), p. 9 (5 Experiments), p. 3 (3 Preliminaries), p. 1 (1 Introduction).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (19 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** 4 MOPO: Model-Based Offline Policy Optimization Unlike model-free methods, our goal is to design an offline model-based reinforcement learning algorithm that can take actions that are not strictly within the ... (p. 4, 3 Preliminaries).
- **Objective/update evidence:** The primary contribution of this work is an offline model-based RL algorithm that optimizes a policy in an uncertainty-penalized MDP, where the reward function is penalized by an estimate of ... (p. 2, 1 Introduction).
- **Temporal/runtime evidence:** Concretely, we train SAC for 1M steps and use the entire training replay buffer as the trajectories for the batch data. (p. 8, 5 Experiments).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
