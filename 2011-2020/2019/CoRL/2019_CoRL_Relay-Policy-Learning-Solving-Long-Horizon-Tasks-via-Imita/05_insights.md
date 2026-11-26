# Insights — Relay Policy Learning: Solving Long-Horizon Tasks via Imitation and Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (13 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v100/gupta20a.html; PDF retrieval source: https://arxiv.org/pdf/1910.11956. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1 Introduction - extractive body cue:** Lastly, and most importantly, since our method ensures that every low-level trajectory is goal-conditioned (allowing for a simple reward specification) and of the same, limited ...
- **p. 2 / 1 Introduction - extractive body cue:** Second, our method does not require any explicit form of skill segmentation or subgoal definition, which otherwise would need to be learned or explicitly provided.
- **p. 3 / 3 Preliminaries - extractive body cue:** Our approach consists of two phases: relay imitation learning (RIL), followed by relay reinforcement fine-tuning (RRF) described in Sec.
- **p. 1 / Abstract - extractive body cue:** We present relay policy learning, a method for imitation and reinforcement learning that can solve multi-stage, long-horizon robotic tasks.
- **p. 1 / Abstract - extractive body cue:** We demonstrate the effectiveness of our method on a number of multi-stage, long-horizon manipulation tasks in a challenging kitchen simulation environment.
- **p. 3 / 3 Preliminaries - extractive body cue:** This architecture consists of a high-level goal-setting policy and a low-level subgoal-conditioned policy, which together generate an environment action for a given state.
- **p. 3 / 3 Preliminaries - extractive body cue:** Unstructured Demos Relay Imitation Learning Relay Reinforcement Fine-tuning Env Reward Action Subgoal Relay Data Relabeling High level Low level Figure 2: Relay policy learning: the ...
- **Contribution anchor:** p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (3 Preliminaries), p. 1 (Abstract), p. 1 (Abstract), p. 3 (3 Preliminaries)

### Strongest assumption and failure boundary

- **p. 1 / 1 Introduction - extractive body cue:** However, HRL methods have traditionally struggled due to various practical challenges such as exploration [5], skill segmentation [6] and reward definition [7].
- **p. 5 / 3 Preliminaries - extractive body cue:** Reinforcement learning provides a solution to this challenge, by enabling continuous improvement of the learned policy directly from experience.
- **p. 6 / 3 Preliminaries - extractive body cue:** This allows us to learn a single policy capable of achieving multiple high level goals, without dealing with the challenges of multi-task optimization.
- **p. 6 / 3 Preliminaries - extractive body cue:** [33], it is often difficult to learn multiple tasks together with on-policy policy gradient methods, because of high variance and conflicting gradients.
- **p. 7 / 3 Preliminaries - extractive body cue:** The last baseline is representative of a class of HIL algorithms [23, 24, 26], which are difficult to fine-tune because it is not clear how ...
- **p. 13 / Figure/Table caption - extractive body cue:** Figure 9: Visualization of successful learned behavior for moving kettle, turning top knob, sliding the slider and opening the hinge cabinet D.2 Failure Cases
- **p. 6 / 3 Preliminaries - extractive body cue:** While these trajectories did not necessarily reach the goals that were originally commanded, and therefore cannot be considered optimal for those goals, they do end ...
- **Boundary to test:** Figure 9: Visualization of successful learned behavior for moving kettle, turning top knob, sliding the slider and opening the hinge cabinet D.2 Failure Cases

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Lastly, and most importantly, since our method ensures that every low-level trajectory is goal-conditioned (allowing for a simple reward specification) and of the same, limited length, it is very amenable to reinforcement ... | p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Reported outcome | Table 1: Comparison of RIL to goal-conditioned behavior cloning with and without relabeling in terms success and step-completion rate averaged across 17 tasks. RIL outperforms the non-hierarchical methods 5.2 Relay Reinforcement Fine-tu ... | p. 7 (Figure/Table caption), p. 8 (Figure/Table caption) |
| Failure/limitation | Figure 9: Visualization of successful learned behavior for moving kettle, turning top knob, sliding the slider and opening the hinge cabinet D.2 Failure Cases | p. 13 (Figure/Table caption), p. 6 (3 Preliminaries) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Paper-specific interface:** Goal-conditioned reinforcement learning: We define M = (S, A, P, r) to be a finite-horizon Markov decision process (MDP), where S and A are state and action spaces, P(st+1 / ... (p. 3, 3 Preliminaries).
- **Paper-specific mechanism:** Second, our method does not require any explicit form of skill segmentation or subgoal definition, which otherwise would need to be learned or explicitly provided. (p. 2, 1 Introduction).
- **Evidence boundary:** the reported outcome is Figure 5: Comparison of the RPL algorithm with a number of baselines averaged over 17 compound goals and 2 (baseline methods) or 3 (our approach) random seeds. Fine-tuning with all ... (p. 8, Figure/Table caption); the relevant task/metric cue is Performing reinforcement fine-tuning individually on 17 different compound goals seen in the demonstrations, we observe a significant improvement in the average success rate and stepwise completion scores over all the ... (p. 7, 3 Preliminaries). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** While these trajectories did not necessarily reach the goals that were originally commanded, and therefore cannot be considered optimal for those goals, they do end up reaching the actual states ... (p. 6, 3 Preliminaries).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `RL, IL, offline learning, and robot data`; tags: `Robotics, Imitation Learning, Reinforcement Learning, long-horizon manipulation`.
- **Reading predecessor in the generated track queue:** Learning Latent Plans from Play (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** RLBench: The Robot Learning Benchmark & Learning Environment (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Figure 9: Visualization of successful learned behavior for moving kettle, turning top knob, sliding the slider and opening the hinge cabinet D.2 Failure Cases; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: Goal-conditioned reinforcement learning: We define M = (S, A, P, r) to be a finite-horizon Markov decision process (MDP), where S and A are state and action spaces, P(st+1 / ... (p. 3, 3 Preliminaries); preserve the objective/update rule: For the high-level policy, given a high-level goal-reaching reward function rh(st, gt, sh g), we can optimize it by running a similar goal-conditioned policy gradient optimization to maximize the sum ... (p. 5, 3 Preliminaries).
2. Use the paper-reported task/data/environment cue: The environment consists of a 9 DoF positioncontrolled Franka robot interacting with a kitchen scene that includes an openable microwave, four turnable oven burners, an oven light switch, a freely ... (p. 6, 3 Preliminaries).
3. Compare against the reported or matched baseline: Figure 5: Comparison of the RPL algorithm with a number of baselines averaged over 17 compound goals and 2 (baseline methods) or 3 (our approach) random seeds. Fine-tuning with all ... (p. 8, Figure/Table caption).
4. Report the body metric with its denominator and aggregation: Performing reinforcement fine-tuning individually on 17 different compound goals seen in the demonstrations, we observe a significant improvement in the average success rate and stepwise completion scores over all the ... (p. 7, 3 Preliminaries).
5. Re-run the reported ablation or stress/failure condition: We experiment with three variants of the fine-tuning update in our experimental evaluation: IRIL-RPL (fine-tuning with Eqn 2, 3 and iterative relay data relabeling to incorporate off-policy data as described ... (p. 6, 3 Preliminaries); if none is reported, design one around: While these trajectories did not necessarily reach the goals that were originally commanded, and therefore cannot be considered optimal for those goals, they do end up reaching the actual states ... (p. 6, 3 Preliminaries).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 2 (1 Introduction), p. 2 (1 Introduction), match the reported outcome at p. 8 (Figure/Table caption), p. 7 (Figure/Table caption), p. 6 (3 Preliminaries), and measure the boundary at p. 6 (3 Preliminaries), p. 12 (C Oracle Baseline Details).

## Falsifiable research question

Under the paper's stated interface (Goal-conditioned reinforcement learning: We define M = (S, A, P, r) to be a finite-horizon Markov decision process (MDP), where S and ...), does the paper-specific mechanism (Second, our method does not require any explicit form of skill segmentation or subgoal definition, which otherwise would need to be learned ...) retain the reported evaluation outcome (Performing reinforcement fine-tuning individually on 17 different compound goals seen in the demonstrations, we observe a significant improvement ...) when tested against the paper's strongest explicit boundary (While these trajectories did not necessarily reach the goals that were originally commanded, and therefore cannot be considered ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (Performing reinforcement fine-tuning individually on 17 different compound goals seen in the demonstrations, we observe a significant improvement ...) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (13 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** Second, our method does not require any explicit form of skill segmentation or subgoal definition, which otherwise would need to be learned or explicitly provided. (p. 2, 1 Introduction).
- **Paper-supported outcome:** Figure 5: Comparison of the RPL algorithm with a number of baselines averaged over 17 compound goals and 2 (baseline methods) or 3 (our approach) random seeds. Fine-tuning with all ... (p. 8, Figure/Table caption).
- **Strongest explicit boundary:** While these trajectories did not necessarily reach the goals that were originally commanded, and therefore cannot be considered optimal for those goals, they do end up reaching the actual states ... (p. 6, 3 Preliminaries).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
