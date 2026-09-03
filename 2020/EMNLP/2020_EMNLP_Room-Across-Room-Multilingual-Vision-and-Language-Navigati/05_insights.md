# Insights — Room-Across-Room: Multilingual Vision-and-Language Navigation with Dense Spatiotemporal Grounding

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (21 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://aclanthology.org/2020.emnlp-main.356/; PDF retrieval source: https://aclanthology.org/2020.emnlp-main.356.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / 1 Introduction - extractive body cue:** We introduce Room-across-Room (RxR), a VLN dataset that addresses gaps in existing ones by (1) ∗First two.
- **p. 1 / Abstract - extractive body cue:** We introduce Room-Across-Room (RxR), a new Vision-and-Language Navigation (VLN) dataset.
- **p. 2 / 1 Introduction - extractive body cue:** In addition to verifying instruction quality, this allows us to collect a play-by-play account of how a human interpreted the instructions, represented as a pose ...
- **p. 2 / 1 Introduction - extractive body cue:** Guide and Follower pose traces provide dense spatiotemporal alignments between instructions, visual percepts and actions - and both perspectives are useful for agent training.
- **p. 1 / 1 Introduction - extractive body cue:** We provide monolingual and multilingual baseline experiments using a variant of the Reinforced Cross-Modal Matching agent (Wang et al., 2019).
- **p. 1 / Abstract - extractive body cue:** We also provide results for a model that learns from synchronized pose traces by focusing only on portions of the panorama attended to in human ...
- **p. 2 / 1 Introduction - extractive body cue:** This especially matters for VLN, as different languages encode spatial and temporal information in idiosyncratic ways-e.g., how contact/support relationships are expressed (Munnich et al., 2001), ...
- **Contribution anchor:** p. 1 (1 Introduction), p. 1 (Abstract), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (1 Introduction), p. 1 (Abstract)

### Strongest assumption and failure boundary

- **p. 3 / 1 Introduction - extractive body cue:** High variance in path length, such that agents cannot simply exploit a strong length prior.
- **p. 3 / 1 Introduction - extractive body cue:** Paths may approach their goal indirectly, so agents cannot simply go straight to the goal.
- **p. 5 / 1 Introduction - extractive body cue:** If the second Follower also fails, then the path is reenqueued to generate another Guide and Follower annotation.
- **p. 2 / 1 Introduction - extractive body cue:** The dominance of high resource languages is a pervasive problem as it is unclear that research findings generalize to other languages (Bender, 2009).
- **p. 1 / 1 Introduction - extractive body cue:** We introduce Room-across-Room (RxR), a VLN dataset that addresses gaps in existing ones by (1) ∗First two.
- **p. 8 / 5 Experiments - extractive body cue:** Although RxR and R2R share the same underlying environments, we note that RxR →R2R cannot exploit R2R's
- **p. 8 / 5 Experiments - extractive body cue:** This is consistent with results in multilingual machine translation (MT) and automatic speech recognition (ASR) where adding more languages can also lead to degradation for ...
- **Boundary to test:** Although RxR and R2R share the same underlying environments, we note that RxR →R2R cannot exploit R2R's

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | We introduce Room-across-Room (RxR), a VLN dataset that addresses gaps in existing ones by (1) ∗First two.
| Reported outcome | Applying the same approach to textual attention did not improve performance. | p. 8 (5 Experiments), p. 9 (5 Experiments) |
| Failure/limitation | Although RxR and R2R share the same underlying environments, we note that RxR →R2R cannot exploit R2R's | p. 8 (5 Experiments), p. 8 (5 Experiments) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `standardized observation, action, task state와 evaluation split → benchmark state/goal와 method decision → policy/controller trajectory 또는 measured result`.
- 이 논문의 재사용 가능한 지점은 Guide and Follower pose traces provide dense spatiotemporal alignments between instructions, visual percepts and actions - and both perspectives are useful for agent training.를 The output of the Guide task is an audio file, a tokenized, timestamped, manually-transcribed instruction, and a pose trace (a series of timestamped 6-DOF camera poses).로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 benchmark state/goal와 method decision가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Although RxR and R2R share the same underlying environments, we note that RxR →R2R cannot exploit R2R's에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: We introduce Room-across-Room (RxR), a VLN dataset that addresses gaps in existing ones by (1) ∗First two.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `Robotics-enabling 3D perception`; tags: `Vision-Language Navigation, Navigation, grounding, Benchmark`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Although RxR and R2R share the same underlying environments, we note that RxR →R2R cannot exploit R2R's; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Monolingual Results Table 5 provides results on the val-unseen split for several training settings, as well as human performance from Follower annotations..
3. Compare against the body-reported baseline or a matched simpler baseline: 1 and 2), monolingual outperforms multilingual (exp..
4. Report the body metric and its denominator/aggregation: Table 4: Simple baselines on val-unseen paths. RxR proves more difficult than R2R overall, and less amenable to agents that tend to go straight (baselines 2 and 3). Note: Baseline 3 partly ....
5. Re-run the body-reported ablation/failure condition: 7) is trained without data augmentation from model-generated instructions (Fried et al., 2018; Tan et al., 2019) and with hyperparameters tuned for RxR..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 2 (1 Introduction), p. 1 (1 Introduction), p. 1 (Abstract); the primary result is directionally consistent at p. 8 (5 Experiments), p. 9 (5 Experiments), p. 8 (Figure/Table caption); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 introduce, Room-across-Room, RxR mechanism이 1 and 2), monolingual outperforms multilingual (exp. 대비 Table 4: Simple baselines on val-unseen paths. RxR proves more difficult than R2R overall, and less amenable to ...을 개선하고, Although RxR and R2R share the same underlying environments, we note that RxR →R2R cannot exploit ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
