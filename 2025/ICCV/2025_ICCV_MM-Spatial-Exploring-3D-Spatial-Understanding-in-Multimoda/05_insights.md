# Insights — MM-Spatial: Exploring 3D Spatial Understanding in Multimodal LLMs

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (6 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Daxberger_MM-Spatial_Exploring_3D_Spatial_Understanding_in_Multimodal_LLMs_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Daxberger_MM-Spatial_Exploring_3D_Spatial_Understanding_in_Multimodal_LLMs_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 5 / Model - extractive body cue:** Comparison with SOTA models on text-rich benchmarks.
- **p. 5 / Model - extractive body cue:** Comparison with SOTA models on knowledge and general benchmarks.
- **p. 6 / Model - extractive body cue:** We study how the improvement from using vision (i.e., comparing a vision-evaluated model vs. a blind-evaluated model) changes after applying the blind filtering strategy outlined ...
- **p. 6 / Model - extractive body cue:** Our results confirm that after applying our filtering strategy, 1) blind models perform substantially worse, and 2) vision improvements (i.e., the delta between vision and ...
- **Contribution anchor:** p. 5 (Model), p. 5 (Model), p. 6 (Model), p. 6 (Model)

### Strongest assumption and failure boundary

- **p. 1 / Body text (section not recovered) - extractive body cue:** We consider the spatial relationships left vs. right and in front vs. behind between two objects, as determined from the current camera pose / viewpoint:2 ...
- **p. 1 / Body text (section not recovered) - extractive body cue:** We leave a more comprehensive study of how to benefit 3D grounding with CoT for future work.
- **p. 1 / Body text (section not recovered) - extractive body cue:** We also did preliminary experiments with 3D Grounding samples, but found that performance does not improve / even slightly regresses there, so we did not ...
- **Boundary to test:** We leave a more comprehensive study of how to benefit 3D grounding with CoT for future work.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Comparison with SOTA models on text-rich benchmarks. | p. 5 (Model), p. 5 (Model) |
| Reported outcome | Table 7. Data Mixture Ratio Results. Comparison of different data mixture ratios - both (Rel)ative to the General category (as in MM1.5), and (Eff)ective when considering the dataset sizes - on aggregated ... | p. 4 (Figure/Table caption), p. 2 (Body text (section not recovered)) |
| Failure/limitation | We leave a more comprehensive study of how to benefit 3D grounding with CoT for future work. | p. 1 (Body text (section not recovered)), p. 1 (Body text (section not recovered)) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `RGB-D, image set, point cloud, depth와 camera pose → geometry, map, object/relationship state → point map, pose, scene graph, affordance 또는 query result`.
- 이 논문의 재사용 가능한 지점은 This highlights the effectiveness of our blind filtering procedure in ensuring that our CA-VQA benchmark becomes more reliant on vision input (i.e., less susceptible to a strong language prior).를 This is in contrast to some of the tasks from the other spatial understanding benchmarks we consider (CV-Bench and SpatialRGPT-Bench), where we found that blind models can perform very strongly and even ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 geometry, map, object/relationship state가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 We leave a more comprehensive study of how to benefit 3D grounding with CoT for future work.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Comparison with SOTA models on text-rich benchmarks.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `ARCHIVE` in `Robotics-enabling 3D perception`; tags: `3D Vision`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** We leave a more comprehensive study of how to benefit 3D grounding with CoT for future work.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Comparison of different data mixture ratios - both (Rel)ative to the General category (as in MM1.5), and (Eff)ective when considering the dataset sizes - on aggregated metrics across the different benchmark categories..
3. Compare against the body-reported baseline or a matched simpler baseline: Results on Further Benchmark Categories We here present a more detailed analysis of MM-Spatial compared with SOTA baselines across the different benchmark categories..
4. Report the body metric and its denominator/aggregation: Our experiments reveal the accuracy of the resulting depth estimates. • Tool-use..
5. Re-run the body-reported ablation/failure condition: Investigating the effect of adding a new model capability is particularly relevant for models with limited capacity, such as the 3B model we consider..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 5 (Model), p. 5 (Model), p. 6 (Model); the primary result is directionally consistent at p. 4 (Figure/Table caption), p. 2 (Body text (section not recovered)), p. 6 (Model); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 Comparison, SOTA, models mechanism이 Results on Further Benchmark Categories We here present a more detailed analysis of MM-Spatial compared with ... 대비 Our experiments reveal the accuracy of the resulting depth estimates. • Tool-use.을 개선하고, We leave a more comprehensive study of how to benefit 3D grounding with CoT for future ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
