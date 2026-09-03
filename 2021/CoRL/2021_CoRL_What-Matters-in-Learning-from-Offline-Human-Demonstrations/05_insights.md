# Insights — What Matters in Learning from Offline Human Demonstrations for Robot Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (13 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v164/mandlekar22a.html; PDF retrieval source: https://proceedings.mlr.press/v164/mandlekar22a/mandlekar22a.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 3 / Dataset - extractive body cue:** We present success rates averaged over 3 seeds for each method across the low-dim Machine-Generated (MG), Proficient-Human (PH), and Multi-Human (MH) datasets.
- **p. 2 / 1 Introduction - extractive body cue:** We find that history-dependent models can be extremely effective in learning from single and multi-human datasets while state-of-the-art batch RL algorithms struggle to learn from ...
- **p. 3 / Dataset - extractive body cue:** Unlike traditional supervised learning, where model selection can be achieved by using the model with the lowest validation loss [21], offline policy learning often suffers ...
- **p. 4 / Dataset - extractive body cue:** We collected these datasets by first training a state-of-the-art RL algorithm [30] on the Lift and Can task, taking agent checkpoints that are saved regularly ...
- **p. 3 / Dataset - extractive body cue:** In our study, we explore how agent design decisions affect policy performances, including the choice of agent architecture, agent observation space, and hyperparameter choices per ...
- **p. 1 / Abstract - extractive body cue:** Based on the study, we derive a series of lessons including the sensitivity to different algorithmic design choices, the dependence on the quality of the ...
- **p. 2 / 1 Introduction - extractive body cue:** Differences from classic supervised learning, such as a mismatch between training and evaluation objectives (task success rate), can make selecting a final policy challenging [21, ...
- **Contribution anchor:** p. 3 (Dataset), p. 2 (1 Introduction), p. 3 (Dataset), p. 4 (Dataset), p. 3 (Dataset), p. 1 (Abstract)

### Strongest assumption and failure boundary

- **p. 2 / 1 Introduction - extractive body cue:** Unfortunately, a lack of suitable benchmark and human datasets have made studying this setting difficult.
- **p. 2 / 1 Introduction - extractive body cue:** Studying these challenges in the context of robot manipulation and human-provided datasets could be a stepping stone to closing the gap between robot and human ...
- **p. 1 / 1 Introduction - extractive body cue:** What has inhibited the use of large human-provided datasets to address this gap?
- **p. 1 / 1 Introduction - extractive body cue:** Despite these advances, the offline learning paradigm has not been nearly as disruptive in robotics as in other disciplines - there is a large gap ...
- **p. 4 / Dataset - extractive body cue:** We present success rates averaged over 3 seeds for each method across different subsets of the Multi-Human datasets, corresponding to mixtures of demonstrations from "Better", ...
- **p. 6 / 4 Experiments - extractive body cue:** There is a strong expectation for batch RL algorithms to be able to distinguish between actions leading to successful placement and actions leading to task ...
- **p. 6 / 4 Experiments - extractive body cue:** The final row of Table 2 shows additional results on a diagnostic dataset termed Can-Paired, where a single operator collected 2 demonstrations for each of ...
- **Boundary to test:** We present success rates averaged over 3 seeds for each method across different subsets of the Multi-Human datasets, corresponding to mixtures of demonstrations from "Better", "Adequate", and "Worse" human operators, and finally ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | We present success rates averaged over 3 seeds for each method across the low-dim Machine-Generated (MG), Proficient-Human (PH), and Multi-Human (MH) datasets. | p. 3 (Dataset), p. 2 (1 Introduction) |
| Reported outcome | Unlike traditional supervised learning, where model selection can be achieved by using the model with the lowest validation loss [21], offline policy learning often suffers from the fact that the training objective ... | p. 3 (Dataset), p. 6 (4 Experiments) |
| Failure/limitation | We present success rates averaged over 3 seeds for each method across different subsets of the Multi-Human datasets, corresponding to mixtures of demonstrations from "Better", "Adequate", and "Worse" human operators, and finally ... | p. 4 (Dataset), p. 6 (4 Experiments) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Paper-specific interface:** Both include end-effector poses and gripper finger positions, and only differ in whether ground-truth object information is used (low-dim) or whether that information is replaced by the available camera observations ... (p. 4, Dataset).
- **Paper-specific mechanism:** Differences from classic supervised learning, such as a mismatch between training and evaluation objectives (task success rate), can make selecting a final policy challenging [21, 22], especially in real-world settings ... (p. 2, 1 Introduction).
- **Evidence boundary:** the reported outcome is Table 2: Results on Suboptimal Human Data. We present success rates averaged over 3 seeds for each method across different subsets of the Multi-Human datasets, corresponding to mixtures of demonstrations ... (p. 4, Figure/Table caption); the relevant task/metric cue is We first note that less complex tasks (Lift, Can) can yield proficient policies (75%-100% success rate) using a small fraction of the data (20%). (p. 7, 4 Experiments). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** We present success rates averaged over 3 seeds for each method across different subsets of the Multi-Human datasets, corresponding to mixtures of demonstrations from "Better", "Adequate", and "Worse" human operators, ... (p. 4, Dataset).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `CORE` in `RL, IL, offline learning, and robot data`; tags: `Robotics, Imitation Learning, offline learning, robot dataset, Benchmark, robomimic`.
- **Reading predecessor in the generated track queue:** Domain Randomization for Transferring Deep Neural Networks from Simulation to the Real World (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Implicit Behavioral Cloning (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** We present success rates averaged over 3 seeds for each method across different subsets of the Multi-Human datasets, corresponding to mixtures of demonstrations from "Better", "Adequate", and "Worse" human operators, and finally ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: Both include end-effector poses and gripper finger positions, and only differ in whether ground-truth object information is used (low-dim) or whether that information is replaced by the available camera observations ... (p. 4, Dataset); preserve the objective/update rule: Unlike traditional supervised learning, where model selection can be achieved by using the model with the lowest validation loss [21], offline policy learning often suffers from the fact that the ... (p. 3, Dataset).
2. Use the paper-reported task/data/environment cue: We further show that important design decisions made through our study in simulation directly translate to effective policy learning on real world tasks and datasets. (p. 3, Dataset).
3. Compare against the reported or matched baseline: Interestingly, results are lower for MH datasets compared to PH datasets, even though the MH datasets contain 100 more demos (300 demos vs. (p. 5, 4 Experiments).
4. Report the body metric with its denominator and aggregation: We first note that less complex tasks (Lift, Can) can yield proficient policies (75%-100% success rate) using a small fraction of the data (20%). (p. 7, 4 Experiments).
5. Re-run the reported ablation or stress/failure condition: 4.3 Effect of Observation Space (C5) Learning from image observations can match low-dim agent performance. (p. 6, 4 Experiments); if none is reported, design one around: We present success rates averaged over 3 seeds for each method across different subsets of the Multi-Human datasets, corresponding to mixtures of demonstrations from "Better", "Adequate", and "Worse" human operators, ... (p. 4, Dataset).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 2 (1 Introduction), p. 2 (1 Introduction), match the reported outcome at p. 4 (Figure/Table caption), p. 5 (Figure/Table caption), p. 6 (Figure/Table caption), and measure the boundary at p. 4 (Dataset), p. 6 (4 Experiments).

## Falsifiable research question

Under the paper's stated interface (Both include end-effector poses and gripper finger positions, and only differ in whether ground-truth object information is used (low-dim) or whether that ...), does the paper-specific mechanism (Differences from classic supervised learning, such as a mismatch between training and evaluation objectives (task success rate), can make selecting a final ...) retain the reported evaluation outcome (We first note that less complex tasks (Lift, Can) can yield proficient policies (75%-100% success rate) using a ...) when tested against the paper's strongest explicit boundary (We present success rates averaged over 3 seeds for each method across different subsets of the Multi-Human datasets, ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (We first note that less complex tasks (Lift, Can) can yield proficient policies (75%-100% success rate) using a ...) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (13 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** Differences from classic supervised learning, such as a mismatch between training and evaluation objectives (task success rate), can make selecting a final policy challenging [21, 22], especially in real-world settings ... (p. 2, 1 Introduction).
- **Paper-supported outcome:** Table 2: Results on Suboptimal Human Data. We present success rates averaged over 3 seeds for each method across different subsets of the Multi-Human datasets, corresponding to mixtures of demonstrations ... (p. 4, Figure/Table caption).
- **Strongest explicit boundary:** We present success rates averaged over 3 seeds for each method across different subsets of the Multi-Human datasets, corresponding to mixtures of demonstrations from "Better", "Adequate", and "Worse" human operators, ... (p. 4, Dataset).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
