# Insights — Habitat 2.0: Training Home Assistants to Rearrange their Habitat

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (16 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.neurips.cc/paper_files/paper/2021/hash/021bbc7ee20b71134d53e20206bd6feb-Abstract.html; PDF retrieval source: https://proceedings.neurips.cc/paper_files/paper/2021/file/021bbc7ee20b71134d53e20206bd6feb-Paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1 Introduction - extractive body cue:** To support this long-term research agenda, we present: • ReplicaCAD: an artist-authored fully-interactive recreation of ‘FRL-apartment' spaces from the Replica dataset [2] consisting of 111 ...
- **p. 1 / Abstract - extractive body cue:** We introduce Habitat 2.0 (H2.0), a simulation platform for training virtual robots in interactive 3D environments and complex physics-enabled scenarios.
- **p. 1 / Abstract - extractive body cue:** Specifically, we present: (i) ReplicaCAD: an artist-authored, annotated, reconfigurable 3D dataset of apartments (matching real spaces) with articulated objects (e.g. cabinets and drawers that can ...
- **p. 2 / 1 Introduction - extractive body cue:** Developing such embodied intelligent systems is a goal of deep scientific and societal value.
- **p. 3 / 1 Introduction - extractive body cue:** H2.0 is free, open-sourced under the MIT license, and under active development.
- **p. 2 / 1 Introduction - extractive body cue:** H2.0 by design and choice does not support non-rigid dynamics (deformables, fluids, films, cloths, ropes), physical state transformations (cutting, drilling, welding, melting), audio or tactile ...
- **p. 7 / 8 GPUs - extractive body cue:** MonolithicRL: a ‘sensors-to-actions' policy trained end-to-end with reinforcement learning (RL).
- **Contribution anchor:** p. 2 (1 Introduction), p. 1 (Abstract), p. 1 (Abstract), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 2 (1 Introduction)

### Strongest assumption and failure boundary

- **p. 2 / 1 Introduction - extractive body cue:** Training and testing such robots in hardware directly is slow, expensive, and difficult to reproduce.
- **p. 3 / 1 Introduction - extractive body cue:** Hierarchy cuts both ways: However, a hierarchy with independent skills suffers from ‘hand-off problems' where a succeeding skill isn't set up for success by the ...
- **p. 2 / 1 Introduction - extractive body cue:** As we will show, they also directly translate to training-time speed-up and accuracy improvements from training agents (for object rearrangement tasks) on more experience. • ...
- **p. 3 / 1 Introduction - extractive body cue:** We conduct a systematic study of two distinct techniques - monolithic ‘sensors-to-actions' policies trained with reinforcement learning (RL) at scale, and classical senseplan-act pipelines (SPA) ...
- **p. 10 / 8 GPUs - extractive body cue:** We make the following observations (See Appendix I for skill learning curves and SPA failure statistics): 1.
- **p. 7 / 8 GPUs - extractive body cue:** The agent fails if the accumulated contact force experienced by the arm/body exceeds a threshold of 5k Newtons.
- **p. 7 / 8 GPUs - extractive body cue:** If the scalar is negative and the gripper is currently holding an object, then the object currently held in the gripper is released and simulated ...
- **Boundary to test:** We make the following observations (See Appendix I for skill learning curves and SPA failure statistics): 1.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | To support this long-term research agenda, we present: • ReplicaCAD: an artist-authored fully-interactive recreation of ‘FRL-apartment' spaces from the Replica dataset [2] consisting of 111 unique layouts of a single apartment backgroun ... | p. 2 (1 Introduction), p. 1 (Abstract) |
| Reported outcome | Figure 5: Success rates for Home Assistant Benchmark tasks. Due to the difficulty of full HAB tasks, we analyze performance as completing a part of the overall task. For the TP methods ... | p. 10 (Figure/Table caption), p. 6 (Figure/Table caption) |
| Failure/limitation | We make the following observations (See Appendix I for skill learning curves and SPA failure statistics): 1. | p. 10 (8 GPUs), p. 7 (8 GPUs) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `standardized observation, action, task state와 evaluation split → benchmark state/goal와 method decision → policy/controller trajectory 또는 measured result`.
- 이 논문의 재사용 가능한 지점은 MonolithicRL: a ‘sensors-to-actions' policy trained end-to-end with reinforcement learning (RL).를 In the supplementary we also analyze different sensor input modalities (Appendix F.1), the surprising success of "blind" policies (Appendix F.2), the effect of different camera placements (Appendix F.3), different action spaces (Appendi ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 benchmark state/goal와 method decision가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 We make the following observations (See Appendix I for skill learning curves and SPA failure statistics): 1.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: To support this long-term research agenda, we present: • ReplicaCAD: an artist-authored fully-interactive recreation of ‘FRL-apartment' spaces from the Replica dataset [2] consisting of 111 unique layouts of a single apartment backgroun ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `Locomotion, whole-body, mobile manipulation, and humanoids`; tags: `Robotics, simulation, mobile manipulation, Benchmark, physics, long-horizon tasks`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** We make the following observations (See Appendix I for skill learning curves and SPA failure statistics): 1.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: 242 ±2 177 ±3 224 ±3 2223 ±3 814 ±2 941 ±2 7192 ±55 3965 ±30 4829 ±50 Table 2: Benchmarking H2.0 performance: simulation steps per second (higher better) over 10 runs ....
3. Compare against the body-reported baseline or a matched simpler baseline: In the more complex task of PrepareGroceries (Figure 5b), TP+SRL outperforms TP+SPA both with and without oracle navigation due to the perception challenge of the tight and cluttered fridge..
4. Report the body metric and its denominator/aggregation: Figure 5: Success rates for Home Assistant Benchmark tasks. Due to the difficulty of full HAB tasks, we analyze performance as completing a part of the overall task. For the TP methods ....
5. Re-run the body-reported ablation/failure condition: In the supplementary we also analyze different sensor input modalities (Appendix F.1), the surprising success of "blind" policies (Appendix F.2), the effect of different camera placements (Appendix F.3), different action spaces (Appendi ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 1 (Abstract), p. 2 (1 Introduction), p. 7 (8 GPUs); the primary result is directionally consistent at p. 10 (Figure/Table caption), p. 6 (Figure/Table caption), p. 8 (Figure/Table caption); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 support, long-term, research mechanism이 In the more complex task of PrepareGroceries (Figure 5b), TP+SRL outperforms TP+SPA both with and without ... 대비 Figure 5: Success rates for Home Assistant Benchmark tasks. Due to the difficulty of full HAB tasks, we ...을 개선하고, We make the following observations (See Appendix I for skill learning curves and SPA failure statistics): ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
