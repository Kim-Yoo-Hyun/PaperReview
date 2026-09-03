# Insights — S3E: A Multi-Robot Multimodal Dataset for Collaborative SLAM

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2210.13723; PDF retrieval source: https://arxiv.org/pdf/2210.13723. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / C OLLABORATIVE Simultaneous Localization and Map - extractive body cue:** In this paper, we introduce four trajectory prototypes designed to meet these principles and evaluate the adaptability of C-SLAM methodologies across diverse closure strategies in ...
- **p. 1 / Abstract - extractive body cue:** Addressing this gap, we introduce S3E, an expansive multimodal dataset.
- **p. 2 / 3 UGVs - extractive body cue:** In conclusion, our work makes several key contributions to the field: ∙We have created a cutting-edge C-SLAM dataset using three ground robots, each equipped with ...
- **p. 3 / III. S3E DATASET - extractive body cue:** This includes the sensor types, their resolution, measurement range, accuracy, and any other pertinent technical details that define their contribution to the SLAM system's performance.
- **p. 2 / 3 UGVs - extractive body cue:** In the right part, our mobile platforms are available in two versions, each designed for different operational requirements.
- **p. 1 / C OLLABORATIVE Simultaneous Localization and Map - extractive body cue:** To fill this gap and enhance C-SLAM research, we introduce S3E dataset, offering a multimodal perspective with a variety of cooperative trajectory patterns in both ...
- **p. 3 / III. S3E DATASET - extractive body cue:** For synchronization across agents, we address two distinct scenarios: ∙In outdoor settings with access to Global Navigation Satellite System (GNSS) signals, we use GNSS time ...
- **Contribution anchor:** p. 1 (C OLLABORATIVE Simultaneous Localization and Map), p. 1 (Abstract), p. 2 (3 UGVs), p. 3 (III. S3E DATASET), p. 2 (3 UGVs), p. 1 (C OLLABORATIVE Simultaneous Localization and Map)

### Strongest assumption and failure boundary

- **p. 1 / Abstract - extractive body cue:** Despite this interest, the scalability and diversity of existing datasets for collaborative trajectories remain limited, especially in scenarios with constrained perspectives where the generalization capabilities ...
- **p. 1 / Abstract - extractive body cue:** Addressing this gap, we introduce S3E, an expansive multimodal dataset.
- **p. 4 / III. S3E DATASET - extractive body cue:** Playground: Open spaces with fewer obstructions challenge feature extraction and optimization.
- **p. 4 / III. S3E DATASET - extractive body cue:** Teaching Building and Tunnel: Poor lighting and similar geometric structures challenge robustness in maintaining
- **p. 2 / 3 UGVs - extractive body cue:** This dataset is the first to incorporate UWB relative distance measurements, providing a new research dimension. ∙To assess C-SLAM's performance in environments with limited overlap, ...
- **p. 6 / III. S3E DATASET - extractive body cue:** If inter-loop closures detection fails, we mark it "Failed".
- **p. 7 / VI. CONCLUSION - extractive body cue:** Our experiments using this dataset have highlighted the improved robustness of C-SLAM systems, especially in handling inter-loop closures.
- **Boundary to test:** If inter-loop closures detection fails, we mark it "Failed".

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | In this paper, we introduce four trajectory prototypes designed to meet these principles and evaluate the adaptability of C-SLAM methodologies across diverse closure strategies in multi-robot operations. | p. 1 (C OLLABORATIVE Simultaneous Localization and Map), p. 1 (Abstract) |
| Reported outcome | However, in areas with limited overlap, reducing drift remained a challenge. - The incorporation of UWB measurements in CoLRIO significantly improved localization robustness and accuracy, as demonstrated in Table VII, showcasing the ... | p. 7 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS) |
| Failure/limitation | If inter-loop closures detection fails, we mark it "Failed". | p. 6 (III. S3E DATASET), p. 7 (VI. CONCLUSION) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `standardized observation, action, task state와 evaluation split → benchmark state/goal와 method decision → policy/controller trajectory 또는 measured result`.
- 이 논문의 재사용 가능한 지점은 These sequences feature meticulously synchronized and spatially calibrated data streams, including 360-degree LiDAR point cloud, high-resolution stereo imagery, high-frequency inertial measurement units (IMU), and Ultrawideband (UWB) re ...를 2) Communication Constraints: Robots are typically limited to sharing information within close proximity, necessitating trajectory designs that maintain a reasonable interaction distance for effective communication.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 benchmark state/goal와 method decision가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 If inter-loop closures detection fails, we mark it "Failed".에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: In this paper, we introduce four trajectory prototypes designed to meet these principles and evaluate the adaptability of C-SLAM methodologies across diverse closure strategies in multi-robot operations.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `Robotics-enabling 3D perception`; tags: `Robotics`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** If inter-loop closures detection fails, we mark it "Failed".; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: The dataset features two mobile robot platform versions: ∙S3Ev1.0: Designed for indoor use with a compact design for exceptional maneuverability in tight spaces. ∙S3Ev2.0: Enhanced with a wider frame to accommodate a ....
3. Compare against the body-reported baseline or a matched simpler baseline: For most of the baselines, we only modify the intrinsic and extrinsic of the sensors and use the left camera for evaluation..
4. Report the body metric and its denominator/aggregation: The results, summarized in Table V and Table VI , reveal the absolute trajectory error (ATE) for both single-agent and collaborative SLAM (C-SLAM) systems in outdoor and indoor environments without UWB measurement. ....
5. Re-run the body-reported ablation/failure condition: The results, summarized in Table V and Table VI , reveal the absolute trajectory error (ATE) for both single-agent and collaborative SLAM (C-SLAM) systems in outdoor and indoor environments without UWB measurement. ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 1 (C OLLABORATIVE Simultaneous Localization and Map), p. 1 (C OLLABORATIVE Simultaneous Localization and Map), p. 3 (III. S3E DATASET); the primary result is directionally consistent at p. 7 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 3 (III. S3E DATASET); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 introduce, four, trajectory mechanism이 For most of the baselines, we only modify the intrinsic and extrinsic of the sensors and ... 대비 The results, summarized in Table V and Table VI , reveal the absolute trajectory error (ATE) for both ...을 개선하고, If inter-loop closures detection fails, we mark it "Failed". 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
