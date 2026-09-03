# Insights — Planning-oriented Autonomous Driving

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (24 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2212.10156; PDF retrieval source: https://arxiv.org/pdf/2212.10156. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 4 / 2. Methodology - extractive body cue:** To address this, we present OccFormer to incorporate both scene-level and agent-level semantics in two aspects: (1) a dense scene feature acquires agent-level features via ...
- **p. 2 / 1. Introduction - extractive body cue:** (b) we present UniAD, a comprehensive end-to-end system that leverages a wide span of tasks.
- **p. 2 / 1. Introduction - extractive body cue:** Through extensive ablations, we verify the superiority of our method over previous state-of-the-arts in all aspects.
- **p. 3 / 2. Methodology - extractive body cue:** Prediction: Motion Forecasting Recent studies have proven the effectiveness of transformer structure on the motion task [43,44,63,69,70,84,99], inspired by which we propose MotionFormer in the ...
- **p. 3 / 2. Methodology - extractive body cue:** Besides queries encoding other agents surrounding the ego-vehicle, we introduce one particular ego-vehicle query in the query set to explicitly model the self-driving vehicle itself, ...
- **p. 5 / 2. Methodology - extractive body cue:** Detailedly, F t ds is passed through a self-attention layer to model responses between distant grids, then a crossattention layer models interactions between agent features ...
- **p. 5 / 2. Methodology - extractive body cue:** To further conserve training memory, each block follows a downsample-upsample manner with an attention module in between to conduct pixel-agent interaction at 1/8 downscaled feature, ...
- **Contribution anchor:** p. 4 (2. Methodology), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (2. Methodology), p. 3 (2. Methodology), p. 5 (2. Methodology)

### Strongest assumption and failure boundary

- **p. 1 / 1. Introduction - extractive body cue:** Although such a design simplifies the R&D difficulty across teams, it bares the risk of information loss across modules, error accumulation and feature misalignment due ...
- **p. 2 / 1. Introduction - extractive body cue:** The choice and priority of preceding tasks should be determined in favor of planning.
- **p. 24 / Figure/Table caption - extractive body cue:** Figure 14. Failure cases 2. In this case, the planner is over-cautious about the incoming vehicle in the narrow street. The dark environment is one ...
- **p. 24 / Figure/Table caption - extractive body cue:** Figure 13. Failure cases 1. Here we present a long-tail scenario, where a large trailer with a white container occupies the entire road. We can ...
- **p. 7 / 3.3. Qualitative Results - extractive body cue:** Besides, we analyze that failure cases of UniAD are mainly under some long-tail scenarios such as large trucks and trailers, shown in the Supplementary as ...
- **p. 6 / 3.1. Joint Results - extractive body cue:** In Exp.1012, only when the two tasks are introduced simultaneously (Exp.12), both metrics of the planning L2 and collision rate achieve the best results, compared ...
- **p. 7 / 3.3. Qualitative Results - extractive body cue:** UniAD achieves the lowest L2 error and collision rate in all time intervals and even outperforms LiDAR-based methods (†) in most cases, verifying the safety ...
- **Boundary to test:** Figure 14. Failure cases 2. In this case, the planner is over-cautious about the incoming vehicle in the narrow street. The dark environment is one critical type of long-tail scenarios in autonomous ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | To address this, we present OccFormer to incorporate both scene-level and agent-level semantics in two aspects: (1) a dense scene feature acquires agent-level features via an exquisitely designed attention module when unrolling ... | p. 4 (2. Methodology), p. 2 (1. Introduction) |
| Reported outcome | UniAD achieves the lowest L2 error and collision rate in all time intervals and even outperforms LiDAR-based methods (†) in most cases, verifying the safety of our system. | p. 7 (3.3. Qualitative Results), p. 6 (Figure/Table caption) |
| Failure/limitation | Figure 14. Failure cases 2. In this case, the planner is over-cautious about the incoming vehicle in the narrow street. The dark environment is one critical type of long-tail scenarios in autonomous ... | p. 24 (Figure/Table caption), p. 24 (Figure/Table caption) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `RGB-D, image set, point cloud, depth와 camera pose → geometry, map, object/relationship state → point map, pose, scene graph, affordance 또는 query result`.
- 이 논문의 재사용 가능한 지점은 MapFormer also has N stacked layers whose output results of each layer are all supervised, while only the updated queries QM in the last layer are forwarded to MotionFormer for agent-map interaction.를 Similar to [8], TrackFormer contains N layers and the final output state QA provides knowledge of Na valid agents for downstream prediction tasks.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 geometry, map, object/relationship state가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Figure 14. Failure cases 2. In this case, the planner is over-cautious about the incoming vehicle in the narrow street. The dark environment is one critical type of long-tail scenarios in autonomous ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: To address this, we present OccFormer to incorporate both scene-level and agent-level semantics in two aspects: (1) a dense scene feature acquires agent-level features via an exquisitely designed attention module when unrolling ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `Planning and control`; tags: `Planning, sensor fusion, 3D perception`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Figure 14. Failure cases 2. In this case, the planner is over-cautious about the incoming vehicle in the narrow street. The dark environment is one critical type of long-tail scenarios in autonomous ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: We conduct experiments on the challenging nuScenes dataset [6]..
3. Compare against the body-reported baseline or a matched simpler baseline: The first row (ID-0) serves as a vanilla multi-task baseline with separate task heads for comparison..
4. Report the body metric and its denominator/aggregation: UniAD achieves the lowest L2 error and collision rate in all time intervals and even outperforms LiDAR-based methods (†) in most cases, verifying the safety of our system..
5. Re-run the body-reported ablation/failure condition: We conduct extensive ablations as shown in Table 2 to prove the effectiveness and necessity of preceding tasks in the end-to-end pipeline..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 5 (2. Methodology), p. 5 (2. Methodology), p. 2 (2. Methodology); the primary result is directionally consistent at p. 7 (3.3. Qualitative Results), p. 6 (Figure/Table caption), p. 6 (3.2. Modular Results); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 address, present, OccFormer mechanism이 The first row (ID-0) serves as a vanilla multi-task baseline with separate task heads for comparison. 대비 UniAD achieves the lowest L2 error and collision rate in all time intervals and even outperforms LiDAR-based methods ...을 개선하고, Figure 14. Failure cases 2. In this case, the planner is over-cautious about the incoming vehicle ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
