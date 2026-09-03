# Insights — VLA Knows Its Limits: Adaptive Execution Horizons for Robot Policies

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2602.21445; PDF retrieval source: https://arxiv.org/pdf/2602.21445. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1. Introduction - extractive body cue:** (2) Building on these insights, we propose AutoHorizon, a novel attention-guided strategy that dynamically estimates the execution horizon for each action chunk, allowing the policy ...
- **p. 2 / 1. Introduction - extractive body cue:** Specifically, we introduce a bidirectional soft-pointer mechanism that locates the first turning points where the attention mass ceases to advance and begins to plateau.
- **p. 3 / 3.1. Preliminary - extractive body cue:** Building on these insights, we introduce an efficient strategy for execution 3
- **p. 5 / 3.4. AutoHorizon - extractive body cue:** Motivated by the above analysis, we propose leveraging attention weights as a proxy to estimate the execution horizon for each action chunk.
- **p. 5 / 3.4. AutoHorizon - extractive body cue:** To this end, we introduce AutoHorizon-a dataadaptive approach that estimates execution horizons directly from the model's intrinsic attention dynamics.
- **p. 6 / 3.4. AutoHorizon - extractive body cue:** Intuitively, St[i, j] quantifies how strongly the i-th query action attends to the j-th key action, revealing how far the model effectively "looks ahead." Our ...
- **p. 5 / 3.3. VLA Knows Its Limits - extractive body cue:** We infer that, due to the strong vision-language pretraining of the backbone model, most linguistic semantics are already embedded within the visual representations during action ...
- **Contribution anchor:** p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Preliminary), p. 5 (3.4. AutoHorizon), p. 5 (3.4. AutoHorizon), p. 6 (3.4. AutoHorizon)

### Strongest assumption and failure boundary

- **p. 1 / 1. Introduction - extractive body cue:** 1, varying the execution horizon leads to substantial performance fluctuations-ranging from consistent successes to frequent failures.
- **p. 1 / 1. Introduction - extractive body cue:** Prior works [3, 8, 12, 24, 39] typically set a fixed execu1.
- **p. 2 / 1. Introduction - extractive body cue:** (3) Extensive experiments on simulated and real-world robot manipulation tasks demonstrate that our method generalizes across different flow-based policies, incurs negligible computational overhead, and outperforms ...
- **p. 3 / 3.1. Preliminary - extractive body cue:** Here, the parameter p ∈N specifies the prediction horizon, i.e., the temporal window over which the model forecasts future actions conditioned on the current perceptual-linguistic ...
- **p. 7 / 4.2. Simulation Results - extractive body cue:** Most estimated horizons fall within moderately low values-favoring reactivity-while occasional larger horizons facilitate faster task 7
- **p. 7 / 4.1. Experimental Settings - extractive body cue:** For all experiments, we report both the mean and standard deviation to ensure fair comparison and robust evaluation.
- **p. 8 / 4.3. Real-World Results - extractive body cue:** Object positions and orientations are randomized across trials to ensure robustness and generalization.
- **Boundary to test:** Most estimated horizons fall within moderately low values-favoring reactivity-while occasional larger horizons facilitate faster task 7

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | (2) Building on these insights, we propose AutoHorizon, a novel attention-guided strategy that dynamically estimates the execution horizon for each action chunk, allowing the policy to adapt to varying perceptual conditions. | p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Reported outcome | 8, and find that AutoHorizon consistently achieves higher success rates. | p. 8 (4.2. Simulation Results), p. 13 (Figure/Table caption) |
| Failure/limitation | Most estimated horizons fall within moderately low values-favoring reactivity-while occasional larger horizons facilitate faster task 7 | p. 7 (4.2. Simulation Results), p. 7 (4.1. Experimental Settings) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `image/video, language instruction, proprioception과 history → language-grounded task state와 action-policy context → continuous action, pose 또는 action chunk`.
- 이 논문의 재사용 가능한 지점은 Denote the pretrained diffusion-/flow-based VisionLanguage-Action (VLA) model as π(At/ot, c), where ot represents the input visual observations at time step t, and c denotes the corresponding language command.를 During execution, the agent typically performs the first e actions from the predicted chunk before re-sampling new input observations and generating the next action chunk, where e ∈N defines the execution horizon.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 language-grounded task state와 action-policy context가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Most estimated horizons fall within moderately low values-favoring reactivity-while occasional larger horizons facilitate faster task 7에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: (2) Building on these insights, we propose AutoHorizon, a novel attention-guided strategy that dynamically estimates the execution horizon for each action chunk, allowing the policy to adapt to varying perceptual conditions.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `VLA and generalist robot policies`; tags: `VLA, Robotics`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Most estimated horizons fall within moderately low values-favoring reactivity-while occasional larger horizons facilitate faster task 7; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Our experiments leverage two benchmark datasets: the LIBERO dataset [20], which offers a diverse suite of single-arm manipulation tasks, and the RoboTwin dataset [7, 23], which focuses on bimanual coordination tasks..
3. Compare against the body-reported baseline or a matched simpler baseline: Compared with the strong Static Oracle+ baseline, it always achieves comparable or even superior results, demonstrating robustness to hyperparameter choices..
4. Report the body metric and its denominator/aggregation: 8, and find that AutoHorizon consistently achieves higher success rates..
5. Re-run the body-reported ablation/failure condition: Task Suite LIB-Spatial LIB-Object LIB-Goal LIB-10 Static Oracle e = 1 92.7 ± 0.9 94.7 ± 3.4 82.7 ± 0.9 74.7 ± 3.4 e = 2 96.0 ± 1.6 95.3 ± 3.8 ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 6 (3.4. AutoHorizon), p. 5 (3.4. AutoHorizon), p. 5 (3.3. VLA Knows Its Limits); the primary result is directionally consistent at p. 8 (4.2. Simulation Results), p. 13 (Figure/Table caption), p. 7 (4.2. Simulation Results); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 Building, insights, AutoHorizon mechanism이 Compared with the strong Static Oracle+ baseline, it always achieves comparable or even superior results, demonstrating ... 대비 8, and find that AutoHorizon consistently achieves higher success rates.을 개선하고, Most estimated horizons fall within moderately low values-favoring reactivity-while occasional larger horizons facilitate faster task 7 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
