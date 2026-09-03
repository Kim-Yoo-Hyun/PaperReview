# Relay Policy Learning: Solving Long-Horizon Tasks via Imitation and Reinforcement Learning

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.mlr.press/v100/gupta20a.html.
> PDF retrieval source: https://arxiv.org/pdf/1910.11956. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2020 / CoRL
- Authors: not duplicated here when not verified in the registry source
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: Robotics, Imitation Learning, Reinforcement Learning, long-horizon manipulation
- Official paper: https://proceedings.mlr.press/v100/gupta20a.html
- Full-text retrieval: https://arxiv.org/pdf/1910.11956
- Code/Project: https://relay-policy-learning.github.io/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

RL, IL, offline learning, and robot data의 il 문제를 이해하기 위해 읽는다. 본문은 However, HRL methods have traditionally struggled due to various practical challenges such as exploration [5], skill segmentation [6] and reward definition [7].를 문제로 두고, Lastly, and most importantly, since our method ensures that every low-level trajectory is goal-conditioned (allowing for a simple reward specification) and of the same, limited length, it is very amenable to reinforcement ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** We present relay policy learning, a method for imitation and reinforcement learning that can solve multi-stage, long-horizon robotic tasks.
- **p. 1 / Abstract - extractive body cue:** This general and universally-applicable, two-phase approach consists of an imitation learning stage that produces goal-conditioned hierarchical policies, and a reinforcement learning phase that finetunes these ...
- **p. 1 / Abstract - extractive body cue:** Our method, while not necessarily perfect at imitation learning, is very amenable to further improvement via environment interaction, allowing it to scale to challenging longhorizon ...
- **p. 1 / Abstract - extractive body cue:** We simplify the long-horizon policy learning problem by using a novel data-relabeling algorithm for learning goal-conditioned hierarchical policies, where the low-level only acts for a ...
- **p. 1 / Abstract - extractive body cue:** While we rely on demonstration data to bootstrap policy learning, we do not assume access to demonstrations of every specific tasks that is being solved, ...
- **p. 1 / 1 Introduction - extractive body cue:** However, HRL methods have traditionally struggled due to various practical challenges such as exploration [5], skill segmentation [6] and reward definition [7].
- **p. 5 / 3 Preliminaries - extractive body cue:** Reinforcement learning provides a solution to this challenge, by enabling continuous improvement of the learned policy directly from experience.

## Core Idea

- **p. 2 / 1 Introduction - extractive body cue:** Lastly, and most importantly, since our method ensures that every low-level trajectory is goal-conditioned (allowing for a simple reward specification) and of the same, limited ...
- **p. 2 / 1 Introduction - extractive body cue:** Second, our method does not require any explicit form of skill segmentation or subgoal definition, which otherwise would need to be learned or explicitly provided.
- **p. 3 / 3 Preliminaries - extractive body cue:** Our approach consists of two phases: relay imitation learning (RIL), followed by relay reinforcement fine-tuning (RRF) described in Sec.
- **p. 1 / Abstract - extractive body cue:** We present relay policy learning, a method for imitation and reinforcement learning that can solve multi-stage, long-horizon robotic tasks.
- **p. 1 / Abstract - extractive body cue:** We demonstrate the effectiveness of our method on a number of multi-stage, long-horizon manipulation tasks in a challenging kitchen simulation environment.
- **p. 3 / 3 Preliminaries - extractive body cue:** This architecture consists of a high-level goal-setting policy and a low-level subgoal-conditioned policy, which together generate an environment action for a given state.
- **p. 3 / 3 Preliminaries - extractive body cue:** Unstructured Demos Relay Imitation Learning Relay Reinforcement Fine-tuning Env Reward Action Subgoal Relay Data Relabeling High level Low level Figure 2: Relay policy learning: the ...
- **p. 4 / 3 Preliminaries - extractive body cue:** 7: end while 8: Distill fine-tuned policies into a single multi-goal policy Algorithm 2 Relay data relabeling for RIL low level Require: Demonstrations D = ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | 7: end while 8: Distill fine-tuned policies into a single multi-goal policy Algorithm 2 Relay data relabeling for RIL low level Require: Demonstrations D = {τ0, τ1, ...τN} 1: for n = ... | observation history와 expert trajectory/action | p. 4 (3 Preliminaries), p. 3 (3 Preliminaries) |
| State/latent | while, Distill, fine-tuned, policies, single, multi-goal, policy, Algorithm, Relay, data, relabeling, RIL | behavior policy와 temporal action context | p. 4 (3 Preliminaries), p. 3 (3 Preliminaries), p. 5 (3 Preliminaries) |
| Output/action | This architecture consists of a high-level goal-setting policy and a low-level subgoal-conditioned policy, which together generate an environment action for a given state. | predicted action 또는 action chunk | p. 3 (3 Preliminaries), p. 5 (3 Preliminaries), p. 5 (3 Preliminaries) |
| Objective/outcome | For the high-level policy, given a high-level goal-reaching reward function rh(st, gt, sh g), we can optimize it by running a similar goal-conditioned policy gradient optimization to maximize the sum of high-level ... | imitation error, task success, robustness와 compounding error | p. 5 (3 Preliminaries), p. 5 (3 Preliminaries), p. 3 (3 Preliminaries) |

## Main Claims and Actual Contribution

- **p. 2 / 1 Introduction - extractive body cue:** Lastly, and most importantly, since our method ensures that every low-level trajectory is goal-conditioned (allowing for a simple reward specification) and of the same, limited ...
- **p. 2 / 1 Introduction - extractive body cue:** Second, our method does not require any explicit form of skill segmentation or subgoal definition, which otherwise would need to be learned or explicitly provided.
- **p. 3 / 3 Preliminaries - extractive body cue:** Our approach consists of two phases: relay imitation learning (RIL), followed by relay reinforcement fine-tuning (RRF) described in Sec.
- **p. 1 / Abstract - extractive body cue:** We present relay policy learning, a method for imitation and reinforcement learning that can solve multi-stage, long-horizon robotic tasks.
- **p. 1 / Abstract - extractive body cue:** We demonstrate the effectiveness of our method on a number of multi-stage, long-horizon manipulation tasks in a challenging kitchen simulation environment.
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1: Comparison of RIL to goal-conditioned behavior cloning with and without relabeling in terms success and step-completion rate averaged across 17 tasks. RIL outperforms ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5: Comparison of the RPL algorithm with a number of baselines averaged over 17 compound goals and 2 (baseline methods) or 3 (our approach) ...
- **p. 8 / 3 Preliminaries - extractive body cue:** While the success rate drops slightly, this gives us a single multi-task policy that can achieve multiple temporally-extended goals (Fig 5).

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | SYSTEM / EVALUATION SCOPE UNRESOLVED | do not infer unreported downstream behavior | p. 7 (Figure/Table caption), p. 8 (Figure/Table caption) |
| Embodiment/environment | The environment consists of a 9 DoF positioncontrolled Franka robot interacting with a kitchen scene that includes an openable microwave, four turnable oven burners, an oven light switch, a freely movable kettle, ... | hardware/simulator version and reset protocol | p. 6 (3 Preliminaries), p. 4 (3 Preliminaries) |
| Dataset/benchmark | We construct the low-level dataset by iterating through the pool of demonstrations and relabeling them using our relay data relabelling algorithm. | role, split, size and leakage | p. 6 (3 Preliminaries), p. 4 (3 Preliminaries), p. 5 (3 Preliminaries), p. 5 (3 Preliminaries) |
| Metric | Performing reinforcement fine-tuning individually on 17 different compound goals seen in the demonstrations, we observe a significant improvement in the average success rate and stepwise completion scores over all the baselines when ... | definition, denominator, direction and uncertainty | p. 7 (3 Preliminaries), p. 7 (3 Preliminaries), p. 8 (Figure/Table caption) |
| Baseline/ablation | Figure 5: Comparison of the RPL algorithm with a number of baselines averaged over 17 compound goals and 2 (baseline methods) or 3 (our approach) random seeds. Fine-tuning with all three variants ... | fair input/data/compute/action matching | p. 8 (Figure/Table caption), p. 8 (3 Preliminaries), p. 7 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 13 / Figure/Table caption - extractive body cue:** Figure 9: Visualization of successful learned behavior for moving kettle, turning top knob, sliding the slider and opening the hinge cabinet D.2 Failure Cases
- **p. 6 / 3 Preliminaries - extractive body cue:** While these trajectories did not necessarily reach the goals that were originally commanded, and therefore cannot be considered optimal for those goals, they do end ...
- **p. 13 / Figure/Table caption - extractive body cue:** Figure 10: Visualization of failing learned behavior for moving kettle, turning the bottom knob, moving the slider and turning on the oven light 13

## Why Read It

RL, IL, offline learning, and robot data의 il 문제를 이해하기 위해 읽는다. 본문은 However, HRL methods have traditionally struggled due to various practical challenges such as exploration [5], skill segmentation [6] and reward definition [7].를 문제로 두고, Lastly, and most importantly, since our method ensures that every low-level trajectory is goal-conditioned (allowing for a simple reward specification) and of the same, limited length, it is very amenable to reinforcement ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1 Introduction), p. 5 (3 Preliminaries), p. 6 (3 Preliminaries), p. 6 (3 Preliminaries), p. 7 (3 Preliminaries), p. 3 (3 Preliminaries) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (13 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** However, HRL methods have traditionally struggled due to various practical challenges such as exploration [5], skill segmentation [6] and reward definition [7]. (p. 1, 1 Introduction).
- **Actual contribution:** Second, our method does not require any explicit form of skill segmentation or subgoal definition, which otherwise would need to be learned or explicitly provided. (p. 2, 1 Introduction).
- **Evaluation boundary:** Figure 5: Comparison of the RPL algorithm with a number of baselines averaged over 17 compound goals and 2 (baseline methods) or 3 (our approach) random seeds. Fine-tuning with all ... (p. 8, Figure/Table caption).
- **Explicit failure boundary:** While these trajectories did not necessarily reach the goals that were originally commanded, and therefore cannot be considered optimal for those goals, they do end up reaching the actual states ... (p. 6, 3 Preliminaries).
