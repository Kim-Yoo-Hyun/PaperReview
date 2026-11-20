# Method - Relay Policy Learning: Solving Long-Horizon Tasks via Imitation and Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v100/gupta20a.html; PDF retrieval source: https://arxiv.org/pdf/1910.11956. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 3 (3 Preliminaries), p. 3 (3 Preliminaries), p. 4 (3 Preliminaries), p. 4 (3 Preliminaries), p. 6 (3 Preliminaries), p. 5 (3 Preliminaries)): This architecture consists of a high-level goal-setting policy and a low-level subgoal-conditioned policy, which together generate an environment action for a given state.

## Method Body Digest

- **p. 3 / 3 Preliminaries - extractive body cue:** This architecture consists of a high-level goal-setting policy and a low-level subgoal-conditioned policy, which together generate an environment action for a given state.
- **p. 3 / 3 Preliminaries - extractive body cue:** Unstructured Demos Relay Imitation Learning Relay Reinforcement Fine-tuning Env Reward Action Subgoal Relay Data Relabeling High level Low level Figure 2: Relay policy learning: the ...
- **p. 4 / 3 Preliminaries - extractive body cue:** 7: end while 8: Distill fine-tuned policies into a single multi-goal policy Algorithm 2 Relay data relabeling for RIL low level Require: Demonstrations D = ...
- **p. 4 / 3 Preliminaries - extractive body cue:** RIL assumes access to the pool of demonstrations consisting of N trajectories D = {τ i, τ j, τ k, ...}, where each trajectory consists ...
- **p. 6 / 3 Preliminaries - extractive body cue:** To circumvent these challenges, we use RPL to fine-tune on a number of different high level goals individually, and then distill all of the learned ...
- **p. 5 / 3 Preliminaries - extractive body cue:** We then generate state-goal-action tuples for Dh, via relay data relabeling within the high-level window being considered, as described in Algorithm 2, 3.
- **p. 5 / 3 Preliminaries - extractive body cue:** First, we choose a window size Wl and generate state-goalaction tuples for Dl, (s, sl g, a) by goal-relabeling within a sliding window along the ...
- **p. 5 / 3 Preliminaries - extractive body cue:** For the high-level policy, given a high-level goal-reaching reward function rh(st, gt, sh g), we can optimize it by running a similar goal-conditioned policy gradient ...

## Design Rationale

- **p. 2 / 1 Introduction - extractive body cue:** Lastly, and most importantly, since our method ensures that every low-level trajectory is goal-conditioned (allowing for a simple reward specification) and of the same, limited ...
- **p. 2 / 1 Introduction - extractive body cue:** Second, our method does not require any explicit form of skill segmentation or subgoal definition, which otherwise would need to be learned or explicitly provided.
- **p. 3 / 3 Preliminaries - extractive body cue:** Our approach consists of two phases: relay imitation learning (RIL), followed by relay reinforcement fine-tuning (RRF) described in Sec.

## Source Evidence Cues

- **p. 3 / 3 Preliminaries - extractive body cue:** This architecture consists of a high-level goal-setting policy and a low-level subgoal-conditioned policy, which together generate an environment action for a given state.
- **p. 3 / 3 Preliminaries - extractive body cue:** Unstructured Demos Relay Imitation Learning Relay Reinforcement Fine-tuning Env Reward Action Subgoal Relay Data Relabeling High level Low level Figure 2: Relay policy learning: the ...
- **p. 4 / 3 Preliminaries - extractive body cue:** 7: end while 8: Distill fine-tuned policies into a single multi-goal policy Algorithm 2 Relay data relabeling for RIL low level Require: Demonstrations D = ...
- **p. 4 / 3 Preliminaries - extractive body cue:** RIL assumes access to the pool of demonstrations consisting of N trajectories D = {τ i, τ j, τ k, ...}, where each trajectory consists ...
- **p. 6 / 3 Preliminaries - extractive body cue:** To circumvent these challenges, we use RPL to fine-tune on a number of different high level goals individually, and then distill all of the learned ...
- **p. 5 / 3 Preliminaries - extractive body cue:** We then generate state-goal-action tuples for Dh, via relay data relabeling within the high-level window being considered, as described in Algorithm 2, 3.
- **p. 5 / 3 Preliminaries - extractive body cue:** First, we choose a window size Wl and generate state-goalaction tuples for Dl, (s, sl g, a) by goal-relabeling within a sliding window along the ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Demonstration representation | expert trajectory를 training pair/context로 정렬한다 | observation history, goal, expert action | temporal alignment, relabeling 또는 latent context construction을 수행 | training sample/context | This architecture consists of a high-level goal-setting policy and a low-level subgoal-conditioned policy, which together generate an environment action for a given ... | p. 3 (3 Preliminaries), p. 3 (3 Preliminaries) |
| Policy fitting | expert action distribution을 학습한다 | context와 action target | behavior cloning, adversarial, sequence, diffusion 또는 flow objective를 최적화 | policy/action distribution | Unstructured Demos Relay Imitation Learning Relay Reinforcement Fine-tuning Env Reward Action Subgoal Relay Data Relabeling High level Low level Figure 2: Relay ... | p. 3 (3 Preliminaries), p. 4 (3 Preliminaries) |
| Closed-loop rollout | distribution shift와 recovery를 확인한다 | current observation/history | action/chunk을 실행하고 feedback으로 다음 prediction을 갱신 | trajectory/failure signal | 7: end while 8: Distill fine-tuned policies into a single multi-goal policy Algorithm 2 Relay data relabeling for RIL low level Require: ... | p. 4 (3 Preliminaries), p. 4 (3 Preliminaries) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3 Preliminaries - extractive body cue:** For the high-level policy, given a high-level goal-reaching reward function rh(st, gt, sh g), we can optimize it by running a similar goal-conditioned policy gradient ...
- **p. 5 / 3 Preliminaries - extractive body cue:** Given a low-level goal-reaching reward function rl(st, at, sl g), we can optimize the low-level policy by simply augmenting the state of the agent with ...
- **p. 3 / 3 Preliminaries - extractive body cue:** The goal of RL is to find a policy π(a/s) that maximizes expected reward over trajectories induced by the policy: Eπ[PT t=0 γtri(st, at)].
- **p. 3 / 3 Preliminaries - extractive body cue:** To extend RL to multiple tasks, a goal-conditioned formulation ( [17]) can be used to learn a policy π(a/s, sg) which maximizes the expected reward ...
- **p. 4 / 3 Preliminaries - extractive body cue:** 4.3), and add to Dl, Dh 6: Update the policy via policy gradient update using Eqn 2, 3.
- **p. 1 / 1 Introduction - extractive body cue:** However, HRL methods have traditionally struggled due to various practical challenges such as exploration [5], skill segmentation [6] and reward definition [7].
- **Formal bridge:** observation history o_{t−H:t} -> expert-like action/chunk a_{t:t+H} -> imitation or action-distribution loss -> closed-loop task success and robustness.
- **Equation/algorithm anchors:** p. 4 (3 Preliminaries), p. 5 (3 Preliminaries), p. 3 (3 Preliminaries), p. 5 (3 Preliminaries), p. 6 (3 Preliminaries), p. 6 (3 Preliminaries).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | while, Distill, fine-tuned, policies, single, multi-goal, policy, Algorithm, Relay, data, relabeling, RIL, level, Require | observation history와 expert trajectory/action | body cue; exact tensor/frame verify |
| State/latent | while, Distill, fine-tuned, policies, single, multi-goal, policy, Algorithm, Relay, data | behavior policy와 temporal action context | body cue; notation verify |
| Action/output | Lastly, most, importantly, since, ensures, every, low-level, trajectory, goal-conditioned, allowing | predicted action 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | high-level, policy, given, goal-reaching, reward, function, optimize, running, similar, goal-conditioned | imitation or action-distribution loss | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 3 Preliminaries - extractive body cue:** 7: end while 8: Distill fine-tuned policies into a single multi-goal policy Algorithm 2 Relay data relabeling for RIL low level Require: Demonstrations D = ...
- **p. 3 / 3 Preliminaries - extractive body cue:** This architecture consists of a high-level goal-setting policy and a low-level subgoal-conditioned policy, which together generate an environment action for a given state.
- **p. 5 / 3 Preliminaries - extractive body cue:** However, the actions at the high level are subgoal states that are provided to the low-level policy, so they must be chosen as states along ...
- **p. 5 / 3 Preliminaries - extractive body cue:** We also label all states st+1, ...., st+Wh along a valid trajectory as potential high-level goals that are reached from state st by the high ...
- **p. 3 / 3 Preliminaries - extractive body cue:** Goal-conditioned reinforcement learning: We define M = (S, A, P, r) to be a finite-horizon Markov decision process (MDP), where S and A are state ...
- **p. 4 / 3 Preliminaries - extractive body cue:** This provides temporal abstraction, since the high level policy operates at a coarser resolution than the low-level policy.
- **p. 6 / 3 Preliminaries - extractive body cue:** While these trajectories did not necessarily reach the goals that were originally commanded, and therefore cannot be considered optimal for those goals, they do end ...
- **Normalized interface:** observation=observation history와 expert trajectory/action; state=behavior policy와 temporal action context; output/action=predicted action 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single-step 또는 action chunk/trajectory horizon; exact chunk length는 exact value was not selected from the PDF body. | Env Env Env Env Env Env Env High level goal Figure 3: Relay policy architecture: A high level goal setter πθ takes ... | episode/sequence/action-chunk boundary |
| Rate / latency | training inference와 deployed control tick을 분리; action chunk면 receding execution 여부 확인. | For the subsequent H steps, the goal produced by πh θ is kept fixed, while πl θ generates an action at at ... | Hz/fps, inference time and control rate |
| Memory | current observation, temporal history 또는 recurrent/sequence context. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | backbone/decoder inference, sampling steps와 action horizon이 latency를 결정한다. | not stated or recoverable in the selected PDF body | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / 3 Preliminaries - extractive body cue:** Unstructured Demos Relay Imitation Learning Relay Reinforcement Fine-tuning Env Reward Action Subgoal Relay Data Relabeling High level Low level Figure 2: Relay policy learning: the ...
- **p. 4 / 3 Preliminaries - extractive body cue:** 7: end while 8: Distill fine-tuned policies into a single multi-goal policy Algorithm 2 Relay data relabeling for RIL low level Require: Demonstrations D = ...
- **p. 6 / 3 Preliminaries - extractive body cue:** To circumvent these challenges, we use RPL to fine-tune on a number of different high level goals individually, and then distill all of the learned ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** architecture, consists, high-level, goal-setting, policy, low-level, subgoal-conditioned, together, generate, environment, action, given, state, Unstructured, Demos, Relay, Imitation, Learning, Reinforcement, Fine-tuning.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Demonstration representation | The environment consists of a 9 DoF positioncontrolled Franka robot interacting with a kitchen scene that includes an openable microwave, four turnable ... | p. 6 (3 Preliminaries), p. 4 (3 Preliminaries) |
| Policy fitting | Figure 5: Comparison of the RPL algorithm with a number of baselines averaged over 17 compound goals and 2 (baseline methods) or ... | p. 8 (Figure/Table caption), p. 8 (3 Preliminaries) |
| Closed-loop rollout | Table 1: Comparison of RIL to goal-conditioned behavior cloning with and without relabeling in terms success and step-completion rate averaged across 17 ... | p. 7 (Figure/Table caption), p. 8 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 6 / 3 Preliminaries - extractive body cue:** We experiment with three variants of the fine-tuning update in our experimental evaluation: IRIL-RPL (fine-tuning with Eqn 2, 3 and iterative relay data relabeling to ...
- **p. 7 / 3 Preliminaries - extractive body cue:** Each goal has different elements manipulated, requiring multiple stages to solve: (a) microwave, kettle, light, slider, (b) kettle, burner, slider, cabinet, (c) burner, top burner, ...
- **p. 8 / 3 Preliminaries - extractive body cue:** The RPL method also outperforms the pre-train-low-level baseline, which we hypothesize is because we are not able to search very effectively in the goal space ...
- **p. 7 / 3 Preliminaries - extractive body cue:** Performing reinforcement fine-tuning individually on 17 different compound goals seen in the demonstrations, we observe a significant improvement in the average success rate and stepwise ...
- **p. 8 / 3 Preliminaries - extractive body cue:** Fine-tuning with all three variants of our method outperforms fine-tuning using flat policies.
- **p. 4 / 3 Preliminaries - extractive body cue:** [22]) D, corresponding to demonstrations of meaningful activities provided by the user, without any particular task in mind, e.g. opening cabinet doors, playing with different ...
- **p. 5 / 3 Preliminaries - extractive body cue:** (1) This procedure gives us an initialization for both the low-level and the high-level policies, without the requirement for any explicit goal labeling from a ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (3 Preliminaries), p. 3 (3 Preliminaries), p. 4 (3 Preliminaries), p. 4 (3 Preliminaries), p. 6 (3 Preliminaries), p. 5 (3 Preliminaries), objective p. 5 (3 Preliminaries), p. 5 (3 Preliminaries), p. 3 (3 Preliminaries), p. 3 (3 Preliminaries), p. 4 (3 Preliminaries), p. 1 (1 Introduction), temporal p. 4 (3 Preliminaries), p. 4 (3 Preliminaries), p. 5 (3 Preliminaries), p. 1 (1 Introduction), p. 1 (Abstract), p. 2 (2 Related Work).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (13 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** 7: end while 8: Distill fine-tuned policies into a single multi-goal policy Algorithm 2 Relay data relabeling for RIL low level Require: Demonstrations D = {τ0, τ1, ...τN} 1: for ... (p. 4, 3 Preliminaries).
- **Objective/update evidence:** For the high-level policy, given a high-level goal-reaching reward function rh(st, gt, sh g), we can optimize it by running a similar goal-conditioned policy gradient optimization to maximize the sum ... (p. 5, 3 Preliminaries).
- **Temporal/runtime evidence:** We simplify the long-horizon policy learning problem by using a novel data-relabeling algorithm for learning goal-conditioned hierarchical policies, where the low-level only acts for a fixed number of steps, regardless ... (p. 1, Abstract).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
