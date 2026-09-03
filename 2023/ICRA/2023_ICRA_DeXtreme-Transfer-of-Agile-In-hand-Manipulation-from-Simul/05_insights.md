# Insights — DeXtreme: Transfer of Agile In-hand Manipulation from Simulation to Reality

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (28 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://research.nvidia.com/publication/2023-06_dextreme-transfer-agile-hand-manipulation-simulation-reality; PDF retrieval source: https://research.nvidia.com/publication/2023-06_dextreme-transfer-agile-hand-manipulation-simulation-reality. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 3 / 2 Method - extractive body cue:** 2.1 Task We propose a method for performing object reorientation on an anthropomorphic hand.
- **p. 4 / 2 Method - extractive body cue:** 2.2 Hardware Our hardware setup (see Fig 2) consists of an Allegro Hand rigidly mounted at the wrist.
- **p. 7 / 2 Method - extractive body cue:** To help overcome this, we introduce various kinds of randomisations [15] into the simulated environment as listed in Table 3.
- **p. 2 / 1 Introduction - extractive body cue:** Multi-fingered robotic hands offer an exciting platform to develop and enable human-level dexterity.
- **p. 3 / 1 Introduction - extractive body cue:** We seek to provide a much broader segment of the research community with access to a novel state-of-the-art in-hand manipulation system in hopes of catalyzing ...
- **p. 4 / 2 Method - extractive body cue:** We use Proximal Policy Optimisation (PPO) [9] to learn a parametric stochastic policy πθ (actor), mapping from observations o ∈O to actions a ∈A.
- **p. 10 / 2 Method - extractive body cue:** To account for unmodelled dynamics, we use a Random Network Adversary (RNA, see below).
- **Contribution anchor:** p. 3 (2 Method), p. 4 (2 Method), p. 7 (2 Method), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 4 (2 Method)

### Strongest assumption and failure boundary

- **p. 3 / 1 Introduction - extractive body cue:** However, due to the complexity of their training architecture, and the sui generis nature of their work on sim-to-real transfer, reproducing and building upon their ...
- **p. 3 / 1 Introduction - extractive body cue:** While the NLP and computer vision communities have reproduced and extended the successes of large-scale models like GPT-3 [3] and DALL-E [4, 5] respectively, similar ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 4: Parameter range adjustments, pi_lo and pi_hi, with ADR based on the performance of policy at the boundaries Qi_lo and Qi_hi with respect to ...
- **p. 18 / 4 Related work - extractive body cue:** However, these often fail to reproduce the agile dexterity present in human hands, as the limitations of such a sequential approach to control place corresponding ...
- **p. 17 / 4 Related work - extractive body cue:** These approaches work well while an object maintains no-slip 10While extrinsics change with different camera configurations, the intrinsics remain the same.
- **p. 18 / 4 Related work - extractive body cue:** 5 Limitations Despite our best efforts, the gap between simulations and the real world is still noticeable.
- **p. 17 / Method - extractive body cue:** We suspect that this is because, despite the extreme levels of randomisation we do, there is a "null space" of possible policies which perform similarly ...
- **Boundary to test:** Figure 4: Parameter range adjustments, pi_lo and pi_hi, with ADR based on the performance of policy at the boundaries Qi_lo and Qi_hi with respect to the thresholds tl and th. If the ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | 2.1 Task We propose a method for performing object reorientation on an anthropomorphic hand. | p. 3 (2 Method), p. 4 (2 Method) |
| Reported outcome | We demonstrate performance which significantly improves upon the best vision policies 8Although [8] focused on the Rubik's cube, they also trained for block reorientation (pp. | p. 14 (3 Results), p. 14 (3 Results) |
| Failure/limitation | Figure 4: Parameter range adjustments, pi_lo and pi_hi, with ADR based on the performance of policy at the boundaries Qi_lo and Qi_hi with respect to the thresholds tl and th. If the ... | p. 8 (Figure/Table caption), p. 18 (4 Related work) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Paper-specific interface:** The slow turnaround time involved in repairing the hardware motivated us to do it ourselves regularly during the experiments, but it was only a temporary solution. • Since we do ... (p. 17, Method).
- **Paper-specific mechanism:** 2.1 Task We propose a method for performing object reorientation on an anthropomorphic hand. (p. 3, 2 Method).
- **Evidence boundary:** the reported outcome is Table 7: The results of running different models on the real robot. We run 10 trials per policy [1] to benchmark the average consecutive successes. Individual rows within each experiment ... (p. 14, Figure/Table caption); the relevant task/metric cue is This also lets us separate the drop in performance due to LSTM instability from pose estimation errors in the real world. (p. 15, 3 Results). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** However, we did not observe this as a significant limitation for our experiments, and our policies nevertheless achieved rollouts with high consecutive successes in the real world. (p. 10, 2 Method).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `Manipulation, contact, tactile, and dexterity`; tags: `Robotics, dexterous manipulation, sim-to-real, Reinforcement Learning, NVIDIA`.
- **Reading predecessor in the generated track queue:** DIGIT: A Novel Design for a Low-Cost Compact High-Resolution Tactile Sensor with Application to In-Hand Manipulation (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Control-Limited Differential Dynamic Programming (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Figure 4: Parameter range adjustments, pi_lo and pi_hi, with ADR based on the performance of policy at the boundaries Qi_lo and Qi_hi with respect to the thresholds tl and th. If the ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: The slow turnaround time involved in repairing the hardware motivated us to do it ourselves regularly during the experiments, but it was only a temporary solution. • Since we do ... (p. 17, Method); preserve the objective/update rule: 2.3 Policy Learning with RL RL Formulation: The task of manipulating the cube to the desired orientation is modelled as a sequential decision making problem where the agent interacts with ... (p. 4, 2 Method).
2. Use the paper-reported task/data/environment cue: We believe such inter-day variations are important to benchmark in robotics [20] and have endeavoured to highlight this specifically in this challenging task. (p. 14, 3 Results).
3. Compare against the reported or matched baseline: Our ablation studies in Section 3.2 do test the strength of the pose estimator for manipulation in the real world. (p. 13, Experiment).
4. Report the body metric with its denominator and aggregation: This also lets us separate the drop in performance due to LSTM instability from pose estimation errors in the real world. (p. 15, 3 Results).
5. Re-run the reported ablation or stress/failure condition: Our ablation studies in Section 3.2 do test the strength of the pose estimator for manipulation in the real world. (p. 13, Experiment); if none is reported, design one around: However, we did not observe this as a significant limitation for our experiments, and our policies nevertheless achieved rollouts with high consecutive successes in the real world. (p. 10, 2 Method).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 3 (2 Method), p. 3 (1 Introduction), match the reported outcome at p. 14 (Figure/Table caption), p. 15 (3 Results), p. 13 (Experiment), and measure the boundary at p. 10 (2 Method), p. 8 (2 Method).

## Falsifiable research question

Under the paper's stated interface (The slow turnaround time involved in repairing the hardware motivated us to do it ourselves regularly during the experiments, but it was ...), does the paper-specific mechanism (2.1 Task We propose a method for performing object reorientation on an anthropomorphic hand.) retain the reported evaluation outcome (This also lets us separate the drop in performance due to LSTM instability from pose estimation errors in ...) when tested against the paper's strongest explicit boundary (However, we did not observe this as a significant limitation for our experiments, and our policies nevertheless achieved ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (This also lets us separate the drop in performance due to LSTM instability from pose estimation errors in ...) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (28 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** 2.1 Task We propose a method for performing object reorientation on an anthropomorphic hand. (p. 3, 2 Method).
- **Paper-supported outcome:** Table 7: The results of running different models on the real robot. We run 10 trials per policy [1] to benchmark the average consecutive successes. Individual rows within each experiment ... (p. 14, Figure/Table caption).
- **Strongest explicit boundary:** However, we did not observe this as a significant limitation for our experiments, and our policies nevertheless achieved rollouts with high consecutive successes in the real world. (p. 10, 2 Method).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
