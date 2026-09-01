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

- **Closed-loop position:** `observation history와 expert trajectory/action → behavior policy와 temporal action context → predicted action 또는 action chunk`.
- 이 논문의 재사용 가능한 지점은 7: end while 8: Distill fine-tuned policies into a single multi-goal policy Algorithm 2 Relay data relabeling for RIL low level Require: Demonstrations D = {τ0, τ1, ...τN} 1: for n = ...를 This architecture consists of a high-level goal-setting policy and a low-level subgoal-conditioned policy, which together generate an environment action for a given state.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 behavior policy와 temporal action context가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Figure 9: Visualization of successful learned behavior for moving kettle, turning top knob, sliding the slider and opening the hinge cabinet D.2 Failure Cases에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Lastly, and most importantly, since our method ensures that every low-level trajectory is goal-conditioned (allowing for a simple reward specification) and of the same, limited length, it is very amenable to reinforcement ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `RL, IL, offline learning, and robot data`; tags: `Robotics, Imitation Learning, Reinforcement Learning, long-horizon manipulation`.
- **Reading predecessor in the generated track queue:** Learning Latent Plans from Play (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** RLBench: The Robot Learning Benchmark & Learning Environment (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Figure 9: Visualization of successful learned behavior for moving kettle, turning top knob, sliding the slider and opening the hinge cabinet D.2 Failure Cases; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: The environment consists of a 9 DoF positioncontrolled Franka robot interacting with a kitchen scene that includes an openable microwave, four turnable oven burners, an oven light switch, a freely movable kettle, ....
3. Compare against the body-reported baseline or a matched simpler baseline: Figure 5: Comparison of the RPL algorithm with a number of baselines averaged over 17 compound goals and 2 (baseline methods) or 3 (our approach) random seeds. Fine-tuning with all three variants ....
4. Report the body metric and its denominator/aggregation: Performing reinforcement fine-tuning individually on 17 different compound goals seen in the demonstrations, we observe a significant improvement in the average success rate and stepwise completion scores over all the baselines when ....
5. Re-run the body-reported ablation/failure condition: We experiment with three variants of the fine-tuning update in our experimental evaluation: IRIL-RPL (fine-tuning with Eqn 2, 3 and iterative relay data relabeling to incorporate off-policy data as described above), DAPG-RPL ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 3 (3 Preliminaries), p. 3 (3 Preliminaries), p. 4 (3 Preliminaries); the primary result is directionally consistent at p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 8 (3 Preliminaries); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 Lastly, most, importantly mechanism이 Figure 5: Comparison of the RPL algorithm with a number of baselines averaged over 17 compound ... 대비 Performing reinforcement fine-tuning individually on 17 different compound goals seen in the demonstrations, we observe a significant improvement ...을 개선하고, Figure 9: Visualization of successful learned behavior for moving kettle, turning top knob, sliding the slider ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
