# Insights — XSkill: Cross Embodiment Skill Discovery

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (20 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v229/xu23a.html; PDF retrieval source: https://arxiv.org/pdf/2307.09955. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1 Introduction - extractive body cue:** Together with the new cross-embodiment dataset in simulation and the real world, we hope to inspire future exploration in this area. • Introducing the first ...
- **p. 1 / 1 Introduction - extractive body cue:** We refer to the task as "Cross-Embodiment Skill Discovery" and introduce our method 7th Conference on Robot Learning (CoRL 2023), Atlanta, USA. arXiv:2307.09955v2 [cs.RO] 28 ...
- **p. 2 / 1 Introduction - extractive body cue:** To encourage across-embodiment alignment, we introduce a set of learnable skill prototypes through feature clustering.
- **p. 3 / 3 Approach - extractive body cue:** The XSkill framework consists of three phases: Discover §3.1, Transfer §3.2, and Compose §3.3 that uses three different data sources.
- **p. 1 / 1 Introduction - extractive body cue:** 3) Compose, performing novel compositions of the learned skills to accomplish new tasks.
- **p. 3 / 3 Approach - extractive body cue:** From this video prompt, the algorithm first identifies the order of skills used in the prompt and then composes the skills using the learned policy ...
- **p. 4 / 3 Approach - extractive body cue:** Then, we extract the skill representation zij = ftemporal(vij) from each video clip with a temporal skill encoder consisting of a vision backbone and a ...
- **Contribution anchor:** p. 2 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 3 (3 Approach), p. 1 (1 Introduction), p. 3 (3 Approach)

### Strongest assumption and failure boundary

- **p. 2 / 1 Introduction - extractive body cue:** With the proposed skill alignment transformer, the algorithm can robustly align skills in the human video to the robot visual observation, despite the embodiment difference ...
- **p. 2 / 1 Introduction - extractive body cue:** Meanwhile, our approach differs from existing work on single-embodiment skill discovery [7, 8, 9], which solely relies on on-robot demonstration data.
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2: XSkill Discover: At each training iteration, a batch of video are sampled from the same embodiment dataset. Each video vt i is augmented ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 6: Execution on a novel task and robustness to perturbation. (a) XSkill analyzes a human video of a novel task, identifying skills for each ...
- **Boundary to test:** Figure 2: XSkill Discover: At each training iteration, a batch of video are sampled from the same embodiment dataset. Each video vt i is augmented into two versions and encoded using temporal ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Together with the new cross-embodiment dataset in simulation and the real world, we hope to inspire future exploration in this area. • Introducing the first attempt toward this task XSkill that consists ... | p. 2 (1 Introduction), p. 1 (1 Introduction) |
| Reported outcome | [XSkill] achieves 70.2% and 60% success (Tab. | p. 7 (4 Evaluation), p. 7 (4 Evaluation) |
| Failure/limitation | Figure 2: XSkill Discover: At each training iteration, a batch of video are sampled from the same embodiment dataset. Each video vt i is augmented into two versions and encoded using temporal ... | p. 3 (Figure/Table caption), p. 8 (Figure/Table caption) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `observation history와 expert trajectory/action → behavior policy와 temporal action context → predicted action 또는 action chunk`.
- 이 논문의 재사용 가능한 지점은 In the transfer phase, the algorithm uses the robot teleoperation dataset Dr to learn the skill-conditioned visuomotor policy P(a/s, z), where z ∈Z and s includes both robot proprioception and visual observation ...를 From this video prompt, the algorithm first identifies the order of skills used in the prompt and then composes the skills using the learned policy P(a/s, z).로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 behavior policy와 temporal action context가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Figure 2: XSkill Discover: At each training iteration, a batch of video are sampled from the same embodiment dataset. Each video vt i is augmented into two versions and encoded using temporal ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Together with the new cross-embodiment dataset in simulation and the real world, we hope to inspire future exploration in this area. • Introducing the first attempt toward this task XSkill that consists ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `VLA and generalist robot policies`; tags: `Robotics, cross-embodiment, skill discovery, human video, Imitation Learning, Diffusion`.
- **Reading predecessor in the generated track queue:** SayPlan: Grounding Large Language Models using 3D Scene Graphs for Scalable Robot Task Planning (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Scaling Proprioceptive-Visual Learning with Heterogeneous Pre-trained Transformers (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Figure 2: XSkill Discover: At each training iteration, a batch of video are sampled from the same embodiment dataset. Each video vt i is augmented into two versions and encoded using temporal ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: During the inference, the robot must complete an unseen composition of subtasks after viewing a prompt video from the sphere agent demonstration. • Realworld Kitchen: is a new benchmark we introduce to ....
3. Compare against the body-reported baseline or a matched simpler baseline: 1 & 2) on unseen tasks with cross-embodiment prompts in simulated and real-world environments, which outperforms all baselines..
4. Report the body metric and its denominator/aggregation: The performance of XSkill and all baseline methods is evaluated based on both subtask completion and order of completion..
5. Re-run the body-reported ablation/failure condition: The ablation study on K, time contrastive loss, and more implementation details can be found in the supplementary material..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 3 (3 Approach), p. 4 (3 Approach), p. 3 (3 Approach); the primary result is directionally consistent at p. 7 (4 Evaluation), p. 7 (4 Evaluation), p. 5 (Figure/Table caption); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 Together, cross-embodiment, dataset mechanism이 1 & 2) on unseen tasks with cross-embodiment prompts in simulated and real-world environments, which outperforms ... 대비 The performance of XSkill and all baseline methods is evaluated based on both subtask completion and order of ...을 개선하고, Figure 2: XSkill Discover: At each training iteration, a batch of video are sampled from the ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
