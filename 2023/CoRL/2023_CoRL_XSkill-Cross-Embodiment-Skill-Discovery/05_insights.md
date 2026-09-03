# Insights — XSkill: Cross Embodiment Skill Discovery

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (20 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v229/xu23a.html; PDF retrieval source: https://arxiv.org/pdf/2307.09955. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1 Introduction - extractive body cue:** Together with the new cross-embodiment dataset in simulation and the real world, we hope to inspire future exploration in this area. • Introducing the first ...
- **p. 1 / 1 Introduction - extractive body cue:** We refer to the task as "Cross-Embodiment Skill Discovery" and introduce our method 7th Conference on Robot Learning (CoRL 2023), Atlanta, USA.
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

- **Paper-specific interface:** In the Compose phase, the algorithm takes as input a single human prompt video τ h prompt for a new task that requires an unseen composition of skills to complete. (p. 3, 3 Approach).
- **Paper-specific mechanism:** Together with the new cross-embodiment dataset in simulation and the real world, we hope to inspire future exploration in this area. • Introducing the first attempt toward this task XSkill ... (p. 2, 1 Introduction).
- **Evidence boundary:** the reported outcome is During the inference, the robot must complete an unseen composition of subtasks after viewing a prompt video from the sphere agent demonstration. • Realworld Kitchen: is a new benchmark we ... (p. 6, 4 Evaluation); the relevant task/metric cue is The performance of XSkill and all baseline methods is evaluated based on both subtask completion and order of completion. (p. 6, 4 Evaluation). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** However, directly following the skill sequence ˜z for execution often results in a fragile system that is sensitive to unexpected failures or speed mismatch. (p. 5, B P).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `VLA and generalist robot policies`; tags: `Robotics, cross-embodiment, skill discovery, human video, Imitation Learning, Diffusion`.
- **Reading predecessor in the generated track queue:** SayPlan: Grounding Large Language Models using 3D Scene Graphs for Scalable Robot Task Planning (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Scaling Proprioceptive-Visual Learning with Heterogeneous Pre-trained Transformers (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Figure 2: XSkill Discover: At each training iteration, a batch of video are sampled from the same embodiment dataset. Each video vt i is augmented into two versions and encoded using temporal ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: In the Compose phase, the algorithm takes as input a single human prompt video τ h prompt for a new task that requires an unseen composition of skills to complete. (p. 3, 3 Approach); preserve the objective/update rule: Both ftemporal and fprototype are trained jointly to minimize the CorssEntropy loss between the predicted pij and target qij skill prototypes distributions: Lprototype = (p. 4, 3 Approach).
2. Use the paper-reported task/data/environment cue: We test XSkill on both simulated and real-world environments: • Franka Kitchen: is a simulated kitchen environment [71] that includes 7 sub-tasks and is accompanied by 580 robot demonstration trajectories. (p. 6, 4 Evaluation).
3. Compare against the reported or matched baseline: 1 & 2) on unseen tasks with cross-embodiment prompts in simulated and real-world environments, which outperforms all baselines. (p. 7, 4 Evaluation).
4. Report the body metric with its denominator and aggregation: The performance of XSkill and all baseline methods is evaluated based on both subtask completion and order of completion. (p. 6, 4 Evaluation).
5. Re-run the reported ablation or stress/failure condition: The ablation study on K, time contrastive loss, and more implementation details can be found in the supplementary material. (p. 6, 4 Evaluation); if none is reported, design one around: However, directly following the skill sequence ˜z for execution often results in a fragile system that is sensitive to unexpected failures or speed mismatch. (p. 5, B P).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 2 (1 Introduction), p. 1 (1 Introduction), match the reported outcome at p. 6 (4 Evaluation), p. 7 (4 Evaluation), p. 7 (4 Evaluation), and measure the boundary at p. 5 (B P), p. 2 (1 Introduction).

## Falsifiable research question

Under the paper's stated interface (In the Compose phase, the algorithm takes as input a single human prompt video τ h prompt for a new task that ...), does the paper-specific mechanism (Together with the new cross-embodiment dataset in simulation and the real world, we hope to inspire future exploration in this area. • ...) retain the reported evaluation outcome (The performance of XSkill and all baseline methods is evaluated based on both subtask completion and order of ...) when tested against the paper's strongest explicit boundary (However, directly following the skill sequence ˜z for execution often results in a fragile system that is sensitive ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (The performance of XSkill and all baseline methods is evaluated based on both subtask completion and order of ...) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (20 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** Together with the new cross-embodiment dataset in simulation and the real world, we hope to inspire future exploration in this area. • Introducing the first attempt toward this task XSkill ... (p. 2, 1 Introduction).
- **Paper-supported outcome:** During the inference, the robot must complete an unseen composition of subtasks after viewing a prompt video from the sphere agent demonstration. • Realworld Kitchen: is a new benchmark we ... (p. 6, 4 Evaluation).
- **Strongest explicit boundary:** However, directly following the skill sequence ˜z for execution often results in a fragile system that is sensitive to unexpected failures or speed mismatch. (p. 5, B P).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
