# Method - What Matters for Batch Online Reinforcement Learning in Robotics?

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://iclr.cc/virtual/2026/poster/10006859; PDF retrieval source: https://arxiv.org/pdf/2505.08078. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 2 (1 Introduction), p. 8 (3 Preliminaries), p. 5 (3 Preliminaries), p. 7 (3 Preliminaries), p. 7 (3 Preliminaries), p. 8 (3 Preliminaries)): Based on these observations, we propose a general recipe for effective batch online RL: train an expressive IL policy as the actor, train a Q-function on the autonomous data, and ...

## Method Body Digest

- **p. 2 / 1 Introduction - extractive PDF cue:** Based on these observations, we propose a general recipe for effective batch online RL: train an expressive IL policy as the actor, train a Q-function ...
- **p. 8 / 3 Preliminaries - extractive PDF cue:** This is in contrast to batch online RL, where to leverage diversity of the online data, the initial model needs to have captured enough of ...
- **p. 5 / 3 Preliminaries - extractive PDF cue:** For all of the algorithm classes, we use a diffusion-based policy as the default.
- **p. 7 / 3 Preliminaries - extractive PDF cue:** For the expressive policy class, we use implicit policy extraction as analyzed in Section 4.2.
- **p. 7 / 3 Preliminaries - extractive PDF cue:** For Gaussian policies, since the action distribution is less expressive, we use explicit policy extraction.
- **p. 8 / 3 Preliminaries - extractive PDF cue:** This instantiation recovers the IDQL algorithm [26] for one iteration of batch online RL, though the recipe defines a category of methods and can be ...
- **p. 4 / 3 Preliminaries - extractive PDF cue:** The policy can then be recovered from the Q-function and value function via a policy extraction step.
- **p. 3 / 3 Preliminaries - extractive PDF cue:** As in traditional RL, the objective is to find a policy π that maximizes the expected sum of discounted rewards Eτ∼pπ(τ)[P t γtr(st, at)] where ...

## Design Rationale

- **p. 2 / 1 Introduction - extractive PDF cue:** On top of the recipe, we propose a simple practical addition to induce even more diversity and achieve better sample efficiency: applying a small amount ...
- **p. 2 / 1 Introduction - extractive PDF cue:** Based on these observations, we propose a general recipe for effective batch online RL: train an expressive IL policy as the actor, train a Q-function ...
- **p. 5 / 3 Preliminaries - extractive PDF cue:** In Figure 3, we present the average normalized returns over iterations of batch online RL for each algorithm class on our six tasks.

## Source Evidence Cues

- **p. 2 / 1 Introduction - extractive PDF cue:** Based on these observations, we propose a general recipe for effective batch online RL: train an expressive IL policy as the actor, train a Q-function ...
- **p. 8 / 3 Preliminaries - extractive PDF cue:** This is in contrast to batch online RL, where to leverage diversity of the online data, the initial model needs to have captured enough of ...
- **p. 5 / 3 Preliminaries - extractive PDF cue:** For all of the algorithm classes, we use a diffusion-based policy as the default.
- **p. 7 / 3 Preliminaries - extractive PDF cue:** For the expressive policy class, we use implicit policy extraction as analyzed in Section 4.2.
- **p. 7 / 3 Preliminaries - extractive PDF cue:** For Gaussian policies, since the action distribution is less expressive, we use explicit policy extraction.
- **p. 8 / 3 Preliminaries - extractive PDF cue:** This instantiation recovers the IDQL algorithm [26] for one iteration of batch online RL, though the recipe defines a category of methods and can be ...
- **p. 4 / 3 Preliminaries - extractive PDF cue:** The policy can then be recovered from the Q-function and value function via a policy extraction step.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Data schema / normalization | heterogeneous robot trajectory를 공통 sample로 만든다 | observation, action, task와 embodiment metadata | sensor/action schema alignment, filtering, normalization을 수행 | shared dataset representation | Based on these observations, we propose a general recipe for effective batch online RL: train an expressive IL policy as the actor, ... | p. 2 (1 Introduction), p. 8 (3 Preliminaries) |
| Coverage / augmentation | task·embodiment·failure variation을 확장한다 | dataset과 metadata | retargeting, relabeling, synthetic/teleoperation augmentation 또는 sampling을 적용 | expanded data support | This is in contrast to batch online RL, where to leverage diversity of the online data, the initial model needs to have ... | p. 8 (3 Preliminaries), p. 5 (3 Preliminaries) |
| Downstream learning interface | 정규화된 data를 policy/representation이 사용한다 | shared observations/actions | pretraining, BC, action-token 또는 representation learning을 수행 | checkpoint/policy action | For all of the algorithm classes, we use a diffusion-based policy as the default. | p. 5 (3 Preliminaries), p. 7 (3 Preliminaries) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / 3 Preliminaries - extractive PDF cue:** As in traditional RL, the objective is to find a policy π that maximizes the expected sum of discounted rewards Eτ∼pπ(τ)[P t γtr(st, at)] where ...
- **p. 4 / 3 Preliminaries - extractive PDF cue:** To do so, it aims to minimize the following objectives for learning a parameterized Q-function Qϕ (with target Q-function Qϕ′) and value function Vψ: LQ(ϕ) ...
- **p. 6 / 3 Preliminaries - extractive PDF cue:** This is done through maximizing a RL objective and an IL objective offline to learn the policy.
- **p. 7 / 3 Preliminaries - extractive PDF cue:** Both use supervised IL objectives and the value function objectives from IQL.
- **p. 4 / 3 Preliminaries - extractive PDF cue:** Imitation learning is often formulated as behavior cloning, which uses supervised learning to learn a policy πθ parameterized by θ to maximize the log-likelihood of ...
- **p. 6 / 3 Preliminaries - extractive PDF cue:** In contrast to a separate policy extraction step that explicitly extracts a policy to maximize Q-values, an alternative for policy extraction is to optimize for ...
- **Formal bridge:** trajectory D with task/embodiment metadata -> normalized sample or downstream action -> coverage/data efficiency/transfer objective -> cross-domain transfer and task performance.
- **Equation/algorithm anchors:** p. 3 (3 Preliminaries), p. 4 (3 Preliminaries), p. 4 (3 Preliminaries), p. 6 (3 Preliminaries), p. 7 (3 Preliminaries), p. 8 (3 Preliminaries).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | observations, general, recipe, effective, batch, online, train, expressive, policy, actor, Q-function, autonomous, data, perform | multi-view observation, language/task label과 action trajectory | body cue; exact tensor/frame verify |
| State/latent | observations, general, recipe, effective, batch, online, train, expressive, policy, actor | shared representation, embodiment/task identity와 data distribution | body cue; notation verify |
| Action/output | recipe, simple, practical, addition, induce, even, more, diversity, achieve, better | dataset sample 또는 learned policy action | body cue; unit/decoder verify |
| Objective/constraint | traditional, objective, find, policy, maximizes, expected, discounted, rewards, where, gives | coverage/data efficiency/transfer objective | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1 Introduction - extractive PDF cue:** Based on these observations, we propose a general recipe for effective batch online RL: train an expressive IL policy as the actor, train a Q-function ...
- **p. 6 / 3 Preliminaries - extractive PDF cue:** Intuitively, this makes sense because value-based RL methods can use the Q-function to determine which states and actions are desirable even in failure trajectories, thus ...
- **p. 8 / 3 Preliminaries - extractive PDF cue:** We use RGB images and robot proprioceptive state (joint and end-effector positions) as input, and use a ResNet-18 [32] as the vision backbone.
- **p. 3 / 3 Preliminaries - extractive PDF cue:** S denotes the state space and A denotes the action space. r(s, a) is the reward function mapping from state and action pairs to rewards, ...
- **p. 4 / 3 Preliminaries - extractive PDF cue:** The policy can then be recovered from the Q-function and value function via a policy extraction step.
- **p. 4 / 3 Preliminaries - extractive PDF cue:** As in IQL, we consider Advantage-Weighted Regression (AWR) [16] as a canonical example of a policy extraction method.
- **p. 5 / 3 Preliminaries - extractive PDF cue:** We examine policy extraction choices individually in more detail in Section 4.2 and policy expressivity in Section 4.3.
- **Normalized interface:** observation=multi-view observation, language/task label과 action trajectory; state=shared representation, embodiment/task identity와 data distribution; output/action=dataset sample 또는 learned policy action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | trajectory demonstration horizon; training sample window와 deployment task horizon을 분리한다. | N do Di ←Collect M rollouts with Rollout(πi-1, Qi-1) Qi ←UpdateValue(∪iDi) πi ←UpdatePolicy(∪iDi) end Algorithm 1: Framework of Batch Online RL We ... | episode/sequence/action-chunk boundary |
| Rate / latency | data recording/action sampling rate와 policy inference/control rate를 분리한다. | On top of the recipe, we propose a simple practical addition to induce even more diversity and achieve better sample efficiency: applying ... | Hz/fps, inference time and control rate |
| Memory | trajectory, embodiment/task metadata와 dataset index. | not recovered | window and reset |
| Compute | data decoding, normalization/augmentation과 downstream training budget이 결정한다. | We run N=10 to 20 iterations of batch online RL with M=200 rollouts per iteration. | hardware, batch and throughput |

## Training vs Inference

- **p. 2 / 1 Introduction - extractive PDF cue:** Based on these observations, we propose a general recipe for effective batch online RL: train an expressive IL policy as the actor, train a Q-function ...
- **p. 8 / 3 Preliminaries - extractive PDF cue:** This is in contrast to batch online RL, where to leverage diversity of the online data, the initial model needs to have captured enough of ...
- **p. 8 / 3 Preliminaries - extractive PDF cue:** This instantiation recovers the IDQL algorithm [26] for one iteration of batch online RL, though the recipe defines a category of methods and can be ...
- **p. 6 / 3 Preliminaries - extractive PDF cue:** Returns are averaged over 3 seeds and 100 evaluation trials at each iteration. more diverse trajectories after batch online RL.
- **p. 4 / 3 Preliminaries - extractive PDF cue:** We run N=10 to 20 iterations of batch online RL with M=200 rollouts per iteration.
- **p. 7 / 3 Preliminaries - extractive PDF cue:** To control for the advantages of the implicit policy extraction method in batch online RL that we observed in Section 4.2, we additionally run a ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** observations, general, recipe, effective, batch, online, train, expressive, policy, actor, Q-function, autonomous, data, perform, implicit, extraction, rollouts, contrast, where, leverage.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Data schema / normalization | Based on our results, in Section 5 we present a recipe for batch online RL, and demonstrate the practicality of the recipe ... | p. 5 (3 Preliminaries), p. 8 (3 Preliminaries) |
| Coverage / augmentation | Figure 11: Normalized returns of value-based RL compared with IL, filtered-IL, and temporally- correlated noise at different data scales, shown for each ... | p. 13 (Figure/Table caption), p. 5 (3 Preliminaries) |
| Downstream learning interface | Figure 3: Normalized returns of different algorithm classes over multiple iterations of improvement. Value-based RL significantly outperforms IL and filtered-IL. Runs are ... | p. 5 (Figure/Table caption), p. 7 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 6 / 3 Preliminaries - extractive PDF cue:** We separate policy extraction into two distinct categories, explicit policy extraction and implicit policy extraction, to analyze the effect of extraction method on performance.
- **p. 8 / 3 Preliminaries - extractive PDF cue:** However, it does not improve data scaling because the correlated noise has the effect of increasing the distribution the policy learns, but this increase in ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 8: Normalized re- turns of value-based RL with and without temporally corre- lated noise at different data scales, averaged over all tasks. Improving diversity ...
- **p. 9 / 6 Discussion - extractive PDF cue:** Batch online RL provides a paradigm for just that-enabling policies to leverage their own rollouts for self-improvement without the complications of online RL.
- **p. 9 / 6 Discussion - extractive PDF cue:** For researchers, we bring to attention open questions for future work to optimize each component of the recipe further.
- **p. 9 / 6 Discussion - extractive PDF cue:** Our work presents a general recipe on batch online RL, though it does have a number of limitations.
- **p. 9 / 6 Discussion - extractive PDF cue:** 7 Limitations In this work, we empirically analyze the key axes that affect performance in batch online RL, demonstrating that the general recipe of value-based ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 2 (1 Introduction), p. 8 (3 Preliminaries), p. 5 (3 Preliminaries), p. 7 (3 Preliminaries), p. 7 (3 Preliminaries), p. 8 (3 Preliminaries), objective p. 3 (3 Preliminaries), p. 4 (3 Preliminaries), p. 6 (3 Preliminaries), p. 7 (3 Preliminaries), p. 4 (3 Preliminaries), p. 6 (3 Preliminaries), temporal p. 3 (3 Preliminaries), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (3 Preliminaries), p. 4 (3 Preliminaries), p. 4 (3 Preliminaries).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
