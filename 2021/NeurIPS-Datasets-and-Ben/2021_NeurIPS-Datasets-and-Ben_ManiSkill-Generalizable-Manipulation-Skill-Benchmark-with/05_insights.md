# Insights — ManiSkill: Generalizable Manipulation Skill Benchmark with Large-Scale Demonstrations

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (24 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://datasets-benchmarks-proceedings.neurips.cc/paper_files/paper/2021/hash/eda80a3d5b344bc40f3bc04f65b7a357-Abstract-round2.html; PDF retrieval source: https://arxiv.org/pdf/2107.14483.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / Abstract - extractive body cue:** Here we propose SAPIEN Manipulation Skill Benchmark (ManiSkill) to benchmark manipulation skills over diverse objects in a full-physics simulator.
- **p. 3 / Abstract - extractive body cue:** Here we introduce the key features of the benchmark.
- **p. 3 / Abstract - extractive body cue:** Additionally, we present and evaluate 3D neural network-based policy learning baselines.
- **p. 4 / Abstract - extractive body cue:** To summarize, here are the key contributions of ManiSkill Benchmark. • The topology and geometry variation of our data allow our benchmark to compare objectlevel ...
- **p. 2 / Abstract - extractive body cue:** On the other hand, [10, 11, 12, 13, 14, 15, 16, 17] can propose novel grasp poses on novel objects based on visual inputs.
- **p. 5 / Abstract - extractive body cue:** Here, s ∈S is an environment state that consists of robot states (e.g. joint angles of the robot) and object states (e.g. object pose and ...
- **p. 8 / Abstract - extractive body cue:** The global features from the PointNets are then fed into a Transformer [76], after which a final attention pooling layer extracts the final representations and ...
- **Contribution anchor:** p. 1 (Abstract), p. 3 (Abstract), p. 3 (Abstract), p. 4 (Abstract), p. 2 (Abstract), p. 5 (Abstract)

### Strongest assumption and failure boundary

- **p. 1 / Abstract - extractive body cue:** However, 3D assets in existing benchmarks mostly lack the diversity of 3D shapes that align with real-world intra-class complexity in topology and geometry.
- **p. 2 / Abstract - extractive body cue:** Several benchmarks or environments, including robosuite [28], RLBench [31], and MetaWorld [30], feature a wide range of tasks; however, they possess a common problem: lacking ...
- **p. 2 / Abstract - extractive body cue:** Despite the quantity of existing environments, most of them lack the ability to benchmark object-level generalizability within categories, and lack inclusion for different methodologies in ...
- **p. 1 / Abstract - extractive body cue:** Tasks are carefully chosen to cover distinct types of manipulation challenges.
- **p. 3 / Abstract - extractive body cue:** Second, ManiSkill focuses on 4 object-centric manipulation tasks that exemplify household manipulation skills with different types of object motions, thereby posing challenges to distinct aspects ...
- **p. 9 / Abstract - extractive body cue:** It is worth noting that our experiment results should not discourage benchmark users to include failure trajectories and find better usage of offline RL methods, ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4: RGB-D (RGB/Depth) and point cloud observations in ManiSkill. Left two images: RGB-D image from one of the three cameras mounted on the robot. ...
- **Boundary to test:** It is worth noting that our experiment results should not discourage benchmark users to include failure trajectories and find better usage of offline RL methods, especially those interested in the No External ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Here we propose SAPIEN Manipulation Skill Benchmark (ManiSkill) to benchmark manipulation skills over diverse objects in a full-physics simulator. | p. 1 (Abstract), p. 3 (Abstract) |
| Reported outcome | We adopted pointcloud observation mode and designed point cloud-based vision architectures as our feature extractor since previous work [46] has achieved significant performance improvements by using point clouds instead of RGB-D images. | p. 8 (Abstract), p. 9 (Abstract) |
| Failure/limitation | It is worth noting that our experiment results should not discourage benchmark users to include failure trajectories and find better usage of offline RL methods, especially those interested in the No External ... | p. 9 (Abstract), p. 6 (Figure/Table caption) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `standardized observation, action, task state와 evaluation split → benchmark state/goal와 method decision → policy/controller trajectory 또는 measured result`.
- 이 논문의 재사용 가능한 지점은 In pointcloud and rgbd modes, the object states in s are replaced by the corresponding point cloud / RGB-D visual observations captured from a panoramic camera mounted on a robot. state mode ...를 2 ManiSkill Benchmark The goal of building ManiSkill benchmark can be best described as facilitating learning generalizable manipulation skills from 3D visual inputs with demonstrations. "Manipulation" involves low-level physical intera ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 benchmark state/goal와 method decision가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 It is worth noting that our experiment results should not discourage benchmark users to include failure trajectories and find better usage of offline RL methods, especially those interested in the No External ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Here we propose SAPIEN Manipulation Skill Benchmark (ManiSkill) to benchmark manipulation skills over diverse objects in a full-physics simulator.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `Manipulation, contact, tactile, and dexterity`; tags: `Robotics, Benchmark, Dataset, manipulation, simulation`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** It is worth noting that our experiment results should not discourage benchmark users to include failure trajectories and find better usage of offline RL methods, especially those interested in the No External ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: We plan to process more objects from the PartNet-Mobility dataset [62] and add them to our ManiSkill assets; 2) While the four tasks currently provided in ManiSkill exemplify distinct manipulation challenges, they ....
3. Compare against the body-reported baseline or a matched simpler baseline: Therefore, we designed several baselines and open-sourced their implementations here to encourage future explorations in the field..
4. Report the body metric and its denominator/aggregation: Table 5: The success rates of SAC [60] agents on OpenCabinetDrawer trained from scratch with 106 time-steps on different numbers of cabinets. The SAC agents are trained in the state mode using ....
5. Re-run the body-reported ablation/failure condition: While network architectures and algorithms play an important role in the performance, learning manipulation skills from demonstrations is challenging without a large number of trajectories, even in one single environment..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 5 (Abstract), p. 8 (Abstract), p. 7 (Abstract); the primary result is directionally consistent at p. 8 (Abstract), p. 9 (Abstract), p. 8 (Figure/Table caption); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 Here, SAPIEN, Manipulation mechanism이 Therefore, we designed several baselines and open-sourced their implementations here to encourage future explorations in the ... 대비 Table 5: The success rates of SAC [60] agents on OpenCabinetDrawer trained from scratch with 106 time-steps on ...을 개선하고, It is worth noting that our experiment results should not discourage benchmark users to include failure ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
