# Method - A Minimalist Approach to Offline Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2106.06860; PDF retrieval source: https://arxiv.org/pdf/2106.06860. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 4 (3 Background), p. 4 (3 Background), p. 1 (Abstract), p. 1 (1 Introduction), p. 6 (3 Background), p. 3 (3 Background)): Most offline RL algorithms are built explicitly on top of an existing off-policy deep RL algorithm, such as TD3 [Fujimoto et al., 2018] or SAC [Haarnoja et al., 2018], but ...

## Method Body Digest

- **p. 4 / 3 Background - extractive body cue:** Most offline RL algorithms are built explicitly on top of an existing off-policy deep RL algorithm, such as TD3 [Fujimoto et al., 2018] or SAC ...
- **p. 4 / 3 Background - extractive body cue:** CQL Fisher-BRC TD3+BC [Kumar et al., 2020] [Kostrikov et al., 2021] (Ours) Algorithmic Adjustments Add regularizer to critic† Train a generative model†‡ Add a BC ...
- **p. 1 / Abstract - extractive body cue:** Due to errors in value estimation from out-of-distribution actions, most offline RL algorithms take the approach of constraining or regularizing the policy with the actions ...
- **p. 1 / 1 Introduction - extractive body cue:** While most off-policy RL algorithms are applicable in the offline setting, they tend to under-perform due to "extrapolation error": an error in policy evaluation, where ...
- **p. 6 / 3 Background - extractive body cue:** Let si be the ith feature of the state s, let µi σi be the mean and standard deviation, respectively, of the ith feature across ...
- **p. 3 / 3 Background - extractive body cue:** Consequently, algorithms have taken the approach of constraining or regularizing the policy to stay near to the actions in the dataset [Levine et al., 2020].
- **p. 5 / 3 Background - extractive body cue:** On top of the architecture changes, for CQL this is largely due to the costs of logsumexp over multiple sampled actions, and for Fisher-BRC, the ...
- **p. 3 / 3 Background - extractive body cue:** The objective of an RL agent is to maximize the expected discounted return Eπ[P∞ t=0 γtrt+1], which is the expected cumulative sum of rewards when ...

## Design Rationale

- **p. 1 / 1 Introduction - extractive body cue:** Consequently, offline RL enables the use of previously logged data or leveraging an expert, such as a human operator, without any of the risk associated ...
- **p. 2 / 1 Introduction - extractive body cue:** The surprising effectiveness of our minimalist approach suggests that in the context of offline RL, simpler approaches have been left underexplored in favor of more ...
- **p. 3 / 3 Background - extractive body cue:** We believe these challenges highlight the importance of minimalist approaches, where performance can be easily attributed to algorithmic contributions, rather than entangled with the specifics ...

## Source Evidence Cues

- **p. 4 / 3 Background - extractive body cue:** Most offline RL algorithms are built explicitly on top of an existing off-policy deep RL algorithm, such as TD3 [Fujimoto et al., 2018] or SAC ...
- **p. 4 / 3 Background - extractive body cue:** CQL Fisher-BRC TD3+BC [Kumar et al., 2020] [Kostrikov et al., 2021] (Ours) Algorithmic Adjustments Add regularizer to critic† Train a generative model†‡ Add a BC ...
- **p. 1 / Abstract - extractive body cue:** Due to errors in value estimation from out-of-distribution actions, most offline RL algorithms take the approach of constraining or regularizing the policy with the actions ...
- **p. 1 / 1 Introduction - extractive body cue:** While most off-policy RL algorithms are applicable in the offline setting, they tend to under-perform due to "extrapolation error": an error in policy evaluation, where ...
- **p. 6 / 3 Background - extractive body cue:** Let si be the ith feature of the state s, let µi σi be the mean and standard deviation, respectively, of the ith feature across ...
- **p. 3 / 3 Background - extractive body cue:** Consequently, algorithms have taken the approach of constraining or regularizing the policy to stay near to the actions in the dataset [Levine et al., 2020].
- **p. 5 / 3 Background - extractive body cue:** On top of the architecture changes, for CQL this is largely due to the costs of logsumexp over multiple sampled actions, and for Fisher-BRC, the ...
- **Detected method headings:** C.2 State Feature Normalization with Other Algorithms (p. 17)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Fixed-data support | 온라인 탐색 없이 transition/action 분포를 정의한다 | offline trajectories와 metadata | dataset support, behavior distribution과 task return을 정리 | training batch/support | Most offline RL algorithms are built explicitly on top of an existing off-policy deep RL algorithm, such as TD3 [Fujimoto et al., ... | p. 4 (3 Background), p. 4 (3 Background) |
| Value / uncertainty update | dataset 밖 action의 과대추정을 억제한다 | batch transition과 value parameters | conservative, implicit, uncertainty 또는 behavior-regularized update를 수행 | Q/V/uncertainty estimate | CQL Fisher-BRC TD3+BC [Kumar et al., 2020] [Kostrikov et al., 2021] (Ours) Algorithmic Adjustments Add regularizer to critic† Train a generative model†‡ ... | p. 4 (3 Background), p. 1 (Abstract) |
| Policy extraction / deployment | 학습된 value를 실행 action으로 변환한다 | value와 behavior support | argmax, advantage weighting, sequence decoding 또는 constraint filtering을 적용 | dataset-supported action | Due to errors in value estimation from out-of-distribution actions, most offline RL algorithms take the approach of constraining or regularizing the policy ... | p. 1 (Abstract), p. 1 (1 Introduction) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / 3 Background - extractive body cue:** The objective of an RL agent is to maximize the expected discounted return Eπ[P∞ t=0 γtrt+1], which is the expected cumulative sum of rewards when ...
- **p. 4 / 3 Background - extractive body cue:** CQL Fisher-BRC TD3+BC [Kumar et al., 2020] [Kostrikov et al., 2021] (Ours) Algorithmic Adjustments Add regularizer to critic† Train a generative model†‡ Add a BC ...
- **p. 6 / 3 Background - extractive body cue:** While the choice of λ in Equation (3) is ultimately just a hyperparameter, we observe that the balance between RL (in maximizing Q) and imitation ...
- **p. 7 / 3 Background - extractive body cue:** TD3+BC achieves effectively the same performances as the state-of-the-art Fisher-BRC, despite being much simpler to implement and tune and more than halving the computation cost. ...
- **p. 3 / 3 Background - extractive body cue:** We measure this objective by a value function, which measures the expected discounted return after taking the action a in state s: Qπ(s, a) = ...
- **p. 1 / 1 Introduction - extractive body cue:** The solution class for this problem revolves around the idea that the learned policy should be kept close to the data-generating process (or behavior policy), ...
- **Formal bridge:** dataset transition (s,a,r,s′) -> dataset-supported policy action -> offline value with OOD control -> offline return and deployment safety.
- **Equation/algorithm anchors:** p. 2 (1 Introduction), p. 4 (3 Background), p. 6 (3 Background), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 3 (3 Background).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | While, most, off-policy, algorithms, applicable, offline, setting, they, tend, under-perform, extrapolation, error, policy, evaluation | dataset state/observation, action, reward와 return-to-go | body cue; exact tensor/frame verify |
| State/latent | While, most, off-policy, algorithms, applicable, offline, setting, they, tend, under-perform | Q/value 또는 sequence-policy state | body cue; notation verify |
| Action/output | Consequently, offline, enables, previously, logged, data, leveraging, expert, human, operator | dataset-supported action sequence | body cue; unit/decoder verify |
| Objective/constraint | objective, agent, maximize, expected, discounted, return, cumulative, rewards, when, following | offline value with OOD control | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / 1 Introduction - extractive body cue:** While most off-policy RL algorithms are applicable in the offline setting, they tend to under-perform due to "extrapolation error": an error in policy evaluation, where ...
- **p. 3 / 3 Background - extractive body cue:** The behavior of an RL agent is determined by a policy π which maps states to actions (deterministic policy), or states to a probability distribution ...
- **p. 1 / 1 Introduction - extractive body cue:** This in turn affects policy improvement, where agents learn to prefer out-of-distribution actions whose value has been overestimated, resulting in poor performance [Fujimoto et al., ...
- **p. 2 / 1 Introduction - extractive body cue:** Additionally, we remark that normalizing the states over the dataset, such that they have mean 0 and standard deviation 1, improves the stability of the ...
- **p. 2 / 1 Introduction - extractive body cue:** We find that we can match the performance of state-of-the-art offline RL algorithms with a single adjustment to the policy update step of the TD3 ...
- **p. 3 / 3 Background - extractive body cue:** Consequently, algorithms have taken the approach of constraining or regularizing the policy to stay near to the actions in the dataset [Levine et al., 2020].
- **p. 4 / 3 Background - extractive body cue:** On top of algorithmic changes, CQL also adds a pre-training phase where the actor is only trained with imitation learning and selects the max action ...
- **Normalized interface:** observation=dataset state/observation, action, reward와 return-to-go; state=Q/value 또는 sequence-policy state; output/action=dataset-supported action sequence.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | offline trajectory/discounted return horizon; deployment horizon과 분리한다. | We train each algorithm for 1 million time steps and evaluate every 5000 time steps. | episode/sequence/action-chunk boundary |
| Rate / latency | training은 batch update, inference는 environment control tick; exact values 확인 필요. | We evaluate run time of training each of the offline RL algorithms for 1 million time steps, using the author-provoided implementations. | Hz/fps, inference time and control rate |
| Memory | fixed dataset, value/policy parameters와 optional context/history. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | dataset size, conservative/value update와 sequence/action decoding이 비용을 결정한다. | Each evaluation consists of 10 episodes. | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / 3 Background - extractive body cue:** Most offline RL algorithms are built explicitly on top of an existing off-policy deep RL algorithm, such as TD3 [Fujimoto et al., 2018] or SAC ...
- **p. 4 / 3 Background - extractive body cue:** CQL Fisher-BRC TD3+BC [Kumar et al., 2020] [Kostrikov et al., 2021] (Ours) Algorithmic Adjustments Add regularizer to critic† Train a generative model†‡ Add a BC ...
- **p. 1 / Abstract - extractive body cue:** Due to errors in value estimation from out-of-distribution actions, most offline RL algorithms take the approach of constraining or regularizing the policy with the actions ...
- **p. 3 / 3 Background - extractive body cue:** Consequently, algorithms have taken the approach of constraining or regularizing the policy to stay near to the actions in the dataset [Levine et al., 2020].
- **p. 5 / 3 Background - extractive body cue:** On top of the architecture changes, for CQL this is largely due to the costs of logsumexp over multiple sampled actions, and for Fisher-BRC, the ...
- **p. 4 / 3 Background - extractive body cue:** CQL Fisher-BRC TD3+BC [Kumar et al., 2020] [Kostrikov et al., 2021] (Ours) Algorithmic Adjustments Add regularizer to critic† Train a generative model†‡ Add a BC ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Most, offline, algorithms, built, explicitly, existing, off-policy, deep, algorithm, TD3, Fujimoto, SAC, Haarnoja, then, further, modify, underlying, non-algorithmic, implementation, changes.
- **Relevant PDF headings:** C.2 State Feature Normalization with Other Algorithms (p. 17).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Fixed-data support | We evaluate our proposed approach on the D4RL benchmark of OpenAI gym MuJoCo tasks [Todorov et al., 2012, Brockman et al., 2016, ... | p. 7 (6 Experiments), p. 7 (6 Experiments) |
| Value / uncertainty update | Our offline RL baselines include two state-of-the-art algorithms, CQL [Kumar et al., 2020] and Fisher-BRC [Kostrikov et al., 2021], as well as ... | p. 7 (6 Experiments), p. 8 (Figure/Table caption) |
| Policy extraction / deployment | Table 3: Run time comparison of training each offline RL algorithm (does not include evaluation costs). (Left) Breakdown of the cost of ... | p. 8 (Figure/Table caption), p. 7 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 9 / Figure/Table caption - extractive body cue:** Figure 5: Percent difference of the performance of an ablation of our proposed approach, compared to the full algorithm. TD3+λ+BC+Norm refers to the complete algorithm, ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 3: Run time comparison of training each offline RL algorithm (does not include evaluation costs). (Left) Breakdown of the cost of the added implementation ...
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 6: Percent difference of the performance of an ablation over α, compared to the full algorithm. Recall the form of the sole hyperparameter λ ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3: Percent difference of the worst evaluation during the last 10 evaluations. This measures the deviations in performance over a period of time. HC ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 1: Percent difference of performance of offline RL algorithms and their simplified versions which remove implementation adjustments to their underlying algorithm. HC = HalfCheetah, ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 4: Learning curves comparing the performance of TD3+BC against offline RL baselines in the D4RL datasets. Curves are averaged over 5 seeds, with the ...
- **p. 19 / Figure/Table caption - extractive body cue:** Figure 8: Benchmarking wall-clock training time of DT and TD3+BC over 1 million steps. Does not include evaluation costs. We remark that the DT was ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (3 Background), p. 4 (3 Background), p. 1 (Abstract), p. 1 (1 Introduction), p. 6 (3 Background), p. 3 (3 Background), objective p. 3 (3 Background), p. 4 (3 Background), p. 6 (3 Background), p. 7 (3 Background), p. 3 (3 Background), p. 1 (1 Introduction), temporal p. 7 (6 Experiments), p. 8 (120 HalfCheetah-Medium-Expert), p. 7 (6 Experiments), p. 5 (3 Background), p. 5 (3 Background), p. 1 (Abstract).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (19 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** Due to errors in value estimation from out-of-distribution actions, most offline RL algorithms take the approach of constraining or regularizing the policy with the actions contained in the dataset. (p. 1, Abstract).
- **Objective/update evidence:** TD3's policy π is updated with the deterministic policy gradient [Silver et al., 2014]: π = argmax π E(s,a)∼D[Q(s, π(s))]. (p. 2, 1 Introduction).
- **Temporal/runtime evidence:** Each evaluation consists of 10 episodes. (p. 7, 6 Experiments).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
