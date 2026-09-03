# Insights — Bring My Cup! Personalizing Vision-Language-Action Models with Visual Attentive Prompting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (48 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=fm6Z3wfTae; PDF retrieval source: https://arxiv.org/pdf/2512.20014.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 3 / 1. Introduction - extractive body cue:** Our main contributions are as follows: • Personal Object Manipulation: We introduce a personalization task for VLAs where the policy must manipulate user-specific objects among ...
- **p. 2 / 1. Introduction - extractive body cue:** We propose Visual Attentive Prompting (VAP), a training-free framework that injects instance-awareness into frozen VLAs by intervening only on their inputs.
- **p. 4 / 3.1. Problem Formulation - extractive body cue:** While exact gradientbased optimization would be computationally prohibitive, we propose VAP as a zero-shot approximation.
- **p. 4 / 3.1. Problem Formulation - extractive body cue:** The category is known, but the specific instance is novel and unseen during training, and at test time the robot encounters o amidst visually similar ...
- **p. 4 / 3.1. Problem Formulation - extractive body cue:** We consider a pre-trained VLA policy πVLA(a / x, ℓ) mapping observation x = (I, s) and instruction ℓto action a, where I = {I(v)}V ...
- **Contribution anchor:** p. 3 (1. Introduction), p. 2 (1. Introduction), p. 4 (3.1. Problem Formulation), p. 4 (3.1. Problem Formulation), p. 4 (3.1. Problem Formulation)

### Strongest assumption and failure boundary

- **p. 2 / 1. Introduction - extractive body cue:** To bridge this semantic gap, we formulate the challenge of manipulating personal objects.
- **p. 2 / 1. Introduction - extractive body cue:** In each benchmark, one object is replaced by a user-specific instance, same-category distractors are added, and the policy must ground the correct instance from a ...
- **p. 3 / 1. Introduction - extractive body cue:** Ablations confirm that neither component alone reliably closes the gap between semantic commands and instance-level control.
- **p. 4 / 3.1. Problem Formulation - extractive body cue:** Reference images are the primary signal in this regime: detailed verbal descriptions cannot reliably distinguish two same-category instances, while a few photographs carry the discriminative ...
- **p. 1 / 1. Introduction - extractive body cue:** By training on large-scale robot datasets (Open XEmbodiment Collaboration et al., 2023), these models achieve strong generalization to generic instructions (e.g., "pick up the cup").
- **p. 42 / Figure/Table caption - extractive body cue:** Figure 23. Case 3 (correct prompt): correct instance highlighted but manipulation fails. The mask prompt consistently highlights the intended personal object in all relevant views, ...
- **p. 25 / Figure/Table caption - extractive body cue:** Figure 9. Soft Prompt: relatively consistent localization yet failed execution. Across the rollout, the token-patch similarity heatmaps remain largely concentrated near the intended personal object, ...
- **Boundary to test:** Figure 23. Case 3 (correct prompt): correct instance highlighted but manipulation fails. The mask prompt consistently highlights the intended personal object in all relevant views, and the robot approaches the prompted object, ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Our main contributions are as follows: • Personal Object Manipulation: We introduce a personalization task for VLAs where the policy must manipulate user-specific objects among visually similar distractors using only a few ... | p. 3 (1. Introduction), p. 2 (1. Introduction) |
| Reported outcome | VAP improves average SR from 18.8% to 58.8%, significantly outperforming soft/hard prompts which remain in the 27.5-31.2% range. | p. 8 (5.4. Results on Real-world Benchmark), p. 7 (5.1. Experimental Setup) |
| Failure/limitation | Figure 23. Case 3 (correct prompt): correct instance highlighted but manipulation fails. The mask prompt consistently highlights the intended personal object in all relevant views, and the robot approaches the prompted object, ... | p. 42 (Figure/Table caption), p. 25 (Figure/Table caption) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `image/video, language instruction, proprioception과 history → language-grounded task state와 action-policy context → continuous action, pose 또는 action chunk`.
- 이 논문의 재사용 가능한 지점은 We consider a pre-trained VLA policy πVLA(a / x, ℓ) mapping observation x = (I, s) and instruction ℓto action a, where I = {I(v)}V v=1 denotes multi-view RGB images from V ...를 Our main contributions are as follows: • Personal Object Manipulation: We introduce a personalization task for VLAs where the policy must manipulate user-specific objects among visually similar distractors using only a few ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 language-grounded task state와 action-policy context가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Figure 23. Case 3 (correct prompt): correct instance highlighted but manipulation fails. The mask prompt consistently highlights the intended personal object in all relevant views, and the robot approaches the prompted object, ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Our main contributions are as follows: • Personal Object Manipulation: We introduce a personalization task for VLAs where the policy must manipulate user-specific objects among visually similar distractors using only a few ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `VLA and generalist robot policies`; tags: `VLA, Vision-Language Model, Robotics`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Figure 23. Case 3 (correct prompt): correct instance highlighted but manipulation fails. The mask prompt consistently highlights the intended personal object in all relevant views, and the robot approaches the prompted object, ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Spanning both selection and pick-and-place tasks, this benchmark rigorously evaluates whether VAP can reliably identify and manipulate userspecified objects on physical hardware..
3. Compare against the body-reported baseline or a matched simpler baseline: VAP outperforms other baselines across all scenarios..
4. Report the body metric and its denominator/aggregation: Table 18. Controlled occlusion sweep on Personalized-SIMPLER. We vary the number of consecutive frames during which the target is fully occluded and report tracking accuracy and task success rate. The spatio-temporal tracker ....
5. Re-run the body-reported ablation/failure condition: Table 14. Ablation of instruction rewriting on single-view Personalized-SIMPLER. "Mask-only" removes rewriting, while "Rewrite- only" removes the visual highlight but keeps the same tint-color rewrite template, serving as a negative con ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 4 (3.1. Problem Formulation), p. 4 (3.1. Problem Formulation); the primary result is directionally consistent at p. 8 (5.4. Results on Real-world Benchmark), p. 7 (5.1. Experimental Setup), p. 8 (5.2. Baselines); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 main, contributions, follows mechanism이 VAP outperforms other baselines across all scenarios. 대비 Table 18. Controlled occlusion sweep on Personalized-SIMPLER. We vary the number of consecutive frames during which the target ...을 개선하고, Figure 23. Case 3 (correct prompt): correct instance highlighted but manipulation fails. The mask prompt consistently ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
