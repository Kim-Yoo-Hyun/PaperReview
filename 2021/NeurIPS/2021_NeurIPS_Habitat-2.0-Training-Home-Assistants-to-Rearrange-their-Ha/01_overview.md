# Habitat 2.0: Training Home Assistants to Rearrange their Habitat

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (16 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.neurips.cc/paper_files/paper/2021/hash/021bbc7ee20b71134d53e20206bd6feb-Abstract.html.
> PDF retrieval source: https://proceedings.neurips.cc/paper_files/paper/2021/file/021bbc7ee20b71134d53e20206bd6feb-Paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2021 / NeurIPS
- Authors: not duplicated here when not verified in the registry source
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: REFERENCE
- Tags: Robotics, simulation, mobile manipulation, Benchmark, physics, long-horizon tasks
- Official paper: https://proceedings.neurips.cc/paper_files/paper/2021/hash/021bbc7ee20b71134d53e20206bd6feb-Abstract.html
- Full-text retrieval: https://proceedings.neurips.cc/paper_files/paper/2021/file/021bbc7ee20b71134d53e20206bd6feb-Paper.pdf
- Code/Project: https://aihabitat.org/
- Paper type: benchmark_or_dataset
- Source audit: full-text PDF body checked on 2026-09-02 (16 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Locomotion, whole-body, mobile manipulation, and humanoids의 benchmark 문제를 이해하기 위해 읽는다. 본문은 Training and testing such robots in hardware directly is slow, expensive, and difficult to reproduce.를 문제로 두고, To support this long-term research agenda, we present: • ReplicaCAD: an artist-authored fully-interactive recreation of ‘FRL-apartment' spaces from the Replica dataset [2] consisting of 111 unique layouts of a single apartment backgroun ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** We introduce Habitat 2.0 (H2.0), a simulation platform for training virtual robots in interactive 3D environments and complex physics-enabled scenarios.
- **p. 1 / Abstract - extractive body cue:** We make comprehensive contributions to all levels of the embodied AI stack - data, simulation, and benchmark tasks.
- **p. 1 / Abstract - extractive body cue:** Specifically, we present: (i) ReplicaCAD: an artist-authored, annotated, reconfigurable 3D dataset of apartments (matching real spaces) with articulated objects (e.g. cabinets and drawers that can ...
- **p. 1 / Abstract - extractive body cue:** These large-scale engineering contributions allow us to systematically compare deep reinforcement learning (RL) at scale and classical sense-plan-act (SPA) pipelines in long-horizon structured tasks, with ...
- **p. 1 / Abstract - extractive body cue:** We find that (1) flat RL policies struggle on HAB compared to hierarchical ones; (2) a hierarchy with independent skills suffers from ‘hand-off problems', and ...
- **p. 2 / 1 Introduction - extractive body cue:** Training and testing such robots in hardware directly is slow, expensive, and difficult to reproduce.
- **p. 3 / 1 Introduction - extractive body cue:** Hierarchy cuts both ways: However, a hierarchy with independent skills suffers from ‘hand-off problems' where a succeeding skill isn't set up for success by the ...

## Core Idea

- **p. 2 / 1 Introduction - extractive body cue:** To support this long-term research agenda, we present: • ReplicaCAD: an artist-authored fully-interactive recreation of ‘FRL-apartment' spaces from the Replica dataset [2] consisting of 111 ...
- **p. 1 / Abstract - extractive body cue:** We introduce Habitat 2.0 (H2.0), a simulation platform for training virtual robots in interactive 3D environments and complex physics-enabled scenarios.
- **p. 1 / Abstract - extractive body cue:** Specifically, we present: (i) ReplicaCAD: an artist-authored, annotated, reconfigurable 3D dataset of apartments (matching real spaces) with articulated objects (e.g. cabinets and drawers that can ...
- **p. 2 / 1 Introduction - extractive body cue:** Developing such embodied intelligent systems is a goal of deep scientific and societal value.
- **p. 3 / 1 Introduction - extractive body cue:** H2.0 is free, open-sourced under the MIT license, and under active development.
- **p. 2 / 1 Introduction - extractive body cue:** H2.0 by design and choice does not support non-rigid dynamics (deformables, fluids, films, cloths, ropes), physical state transformations (cutting, drilling, welding, melting), audio or tactile ...
- **p. 7 / 8 GPUs - extractive body cue:** MonolithicRL: a ‘sensors-to-actions' policy trained end-to-end with reinforcement learning (RL).
- **p. 7 / 8 GPUs - extractive body cue:** At every step, it outputs the desired change in end-effector position (δx, δy, δz); the desired end-effector position is fed into an inverse kinematics solver ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | MonolithicRL: a ‘sensors-to-actions' policy trained end-to-end with reinforcement learning (RL). | standardized observation, action, task state와 evaluation split | p. 7 (8 GPUs), p. 8 (8 GPUs) |
| State/latent | MonolithicRL, sensors-to-actions, policy, trained, end-to-end, reinforcement, learning, supplementary, analyze, different, sensor, input | benchmark state/goal와 method decision | p. 7 (8 GPUs), p. 8 (8 GPUs), p. 7 (8 GPUs) |
| Output/action | In the supplementary we also analyze different sensor input modalities (Appendix F.1), the surprising success of "blind" policies (Appendix F.2), the effect of different camera placements (Appendix F.3), different action spaces (Appendi ... | policy/controller trajectory 또는 measured result | p. 8 (8 GPUs), p. 7 (8 GPUs), p. 2 (1 Introduction) |
| Objective/outcome | However, the performance drop of SPA (and qualitative results) suggest that the unseen receptacles (shelf, armchair, tv stand) may be objectively more difficult to pick up objects from since the shelf and ... | success metric, robustness, generalization과 reproducibility | p. 8 (8 GPUs), p. 3 (1 Introduction), p. 2 (1 Introduction) |

## Main Claims and Actual Contribution

- **p. 2 / 1 Introduction - extractive body cue:** To support this long-term research agenda, we present: • ReplicaCAD: an artist-authored fully-interactive recreation of ‘FRL-apartment' spaces from the Replica dataset [2] consisting of 111 ...
- **p. 1 / Abstract - extractive body cue:** We introduce Habitat 2.0 (H2.0), a simulation platform for training virtual robots in interactive 3D environments and complex physics-enabled scenarios.
- **p. 1 / Abstract - extractive body cue:** Specifically, we present: (i) ReplicaCAD: an artist-authored, annotated, reconfigurable 3D dataset of apartments (matching real spaces) with articulated objects (e.g. cabinets and drawers that can ...
- **p. 2 / 1 Introduction - extractive body cue:** Developing such embodied intelligent systems is a goal of deep scientific and societal value.
- **p. 3 / 1 Introduction - extractive body cue:** H2.0 is free, open-sourced under the MIT license, and under active development.
- **p. 10 / Figure/Table caption - extractive body cue:** Figure 5: Success rates for Home Assistant Benchmark tasks. Due to the difficulty of full HAB tasks, we analyze performance as completing a part of ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 2: Benchmarking H2.0 performance: simulation steps per second (higher better) over 10 runs and a 95% confidence-interval In Idle, the agent is executing random ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 3: Pick generalization analysis: success rates with mean and standard error on 600 episodes (and across 3 seeds for MonolithicRL). Systematic Generalization. With H2.0 ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | BENCHMARK / DATASET | do not infer unreported downstream behavior | p. 10 (Figure/Table caption), p. 6 (Figure/Table caption) |
| Embodiment/environment | 242 ±2 177 ±3 224 ±3 2223 ±3 814 ±2 941 ±2 7192 ±55 3965 ±30 4829 ±50 Table 2: Benchmarking H2.0 performance: simulation steps per second (higher better) over 10 runs ... | hardware/simulator version and reset protocol | p. 6 (8 GPUs), p. 6 (8 GPUs) |
| Dataset/benchmark | 6 Home Assistant Benchmark (HAB) We now describe our benchmark of common household assistive robotic tasks. | role, split, size and leakage | p. 6 (8 GPUs), p. 6 (8 GPUs), p. 8 (8 GPUs), p. 7 (8 GPUs) |
| Metric | Figure 5: Success rates for Home Assistant Benchmark tasks. Due to the difficulty of full HAB tasks, we analyze performance as completing a part of the overall task. For the TP methods ... | definition, denominator, direction and uncertainty | p. 10 (Figure/Table caption), p. 8 (8 GPUs), p. 10 (8 GPUs) |
| Baseline/ablation | In the more complex task of PrepareGroceries (Figure 5b), TP+SRL outperforms TP+SPA both with and without oracle navigation due to the perception challenge of the tight and cluttered fridge. | fair input/data/compute/action matching | p. 10 (8 GPUs), p. 8 (8 GPUs), p. 8 (8 GPUs) |

## Explicit Limitations and Failure Boundary

- **p. 10 / 8 GPUs - extractive body cue:** We make the following observations (See Appendix I for skill learning curves and SPA failure statistics): 1.
- **p. 7 / 8 GPUs - extractive body cue:** The agent fails if the accumulated contact force experienced by the arm/body exceeds a threshold of 5k Newtons.
- **p. 7 / 8 GPUs - extractive body cue:** If the scalar is negative and the gripper is currently holding an object, then the object currently held in the gripper is released and simulated ...
- **p. 8 / 8 GPUs - extractive body cue:** We cannot make any such claims for SPA.
- **p. 8 / 8 GPUs - extractive body cue:** SensePlanAct (SPA) pipeline: Sensing consists of constructing an accumulative 3D point-cloud of the scene from depth sensors, which is then used for collision queries.
- **p. 9 / 8 GPUs - extractive body cue:** The agent is evaluated on unseen layouts and configurations of objects, and so cannot simply memorize.
- **p. 10 / 8 GPUs - extractive body cue:** 7 Societal Impacts, Limitations, and Conclusion ReplicaCAD was modeled upon apartments in one country (USA).

## Why Read It

Locomotion, whole-body, mobile manipulation, and humanoids의 benchmark 문제를 이해하기 위해 읽는다. 본문은 Training and testing such robots in hardware directly is slow, expensive, and difficult to reproduce.를 문제로 두고, To support this long-term research agenda, we present: • ReplicaCAD: an artist-authored fully-interactive recreation of ‘FRL-apartment' spaces from the Replica dataset [2] consisting of 111 unique layouts of a single apartment backgroun ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 Introduction), p. 3 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 1 (Abstract), p. 2 (1 Introduction) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
