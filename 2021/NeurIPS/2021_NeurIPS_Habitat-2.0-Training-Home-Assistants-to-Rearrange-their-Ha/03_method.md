# Method - Habitat 2.0: Training Home Assistants to Rearrange their Habitat

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (16 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.neurips.cc/paper_files/paper/2021/hash/021bbc7ee20b71134d53e20206bd6feb-Abstract.html; PDF retrieval source: https://proceedings.neurips.cc/paper_files/paper/2021/file/021bbc7ee20b71134d53e20206bd6feb-Paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 1 (Abstract), p. 2 (1 Introduction), p. 7 (8 GPUs), p. 7 (8 GPUs), p. 2 (1 Introduction), p. 6 (8 GPUs)): We introduce Habitat 2.0 (H2.0), a simulation platform for training virtual robots in interactive 3D environments and complex physics-enabled scenarios.

## Method Body Digest

- **p. 1 / Abstract - extractive body cue:** We introduce Habitat 2.0 (H2.0), a simulation platform for training virtual robots in interactive 3D environments and complex physics-enabled scenarios.
- **p. 2 / 1 Introduction - extractive body cue:** H2.0 by design and choice does not support non-rigid dynamics (deformables, fluids, films, cloths, ropes), physical state transformations (cutting, drilling, welding, melting), audio or tactile ...
- **p. 7 / 8 GPUs - extractive body cue:** MonolithicRL: a ‘sensors-to-actions' policy trained end-to-end with reinforcement learning (RL).
- **p. 7 / 8 GPUs - extractive body cue:** At every step, it outputs the desired change in end-effector position (δx, δy, δz); the desired end-effector position is fed into an inverse kinematics solver ...
- **p. 2 / 1 Introduction - extractive body cue:** The benefit of this focus is that we were able to design and optimize H2.0 to be exceedingly fast - simulating a Fetch robot interacting ...
- **p. 6 / 8 GPUs - extractive body cue:** 242 ±2 177 ±3 224 ±3 2223 ±3 814 ±2 941 ±2 7192 ±55 3965 ±30 4829 ±50 Table 2: Benchmarking H2.0 performance: simulation steps ...
- **p. 8 / 8 GPUs - extractive body cue:** The controller was described in ‘Action Space' above and is consistent with MonolithicRL.
- **p. 8 / 8 GPUs - extractive body cue:** However, the performance drop of SPA (and qualitative results) suggest that the unseen receptacles (shelf, armchair, tv stand) may be objectively more difficult to pick ...

## Design Rationale

- **p. 2 / 1 Introduction - extractive body cue:** To support this long-term research agenda, we present: • ReplicaCAD: an artist-authored fully-interactive recreation of ‘FRL-apartment' spaces from the Replica dataset [2] consisting of 111 ...
- **p. 1 / Abstract - extractive body cue:** We introduce Habitat 2.0 (H2.0), a simulation platform for training virtual robots in interactive 3D environments and complex physics-enabled scenarios.
- **p. 1 / Abstract - extractive body cue:** Specifically, we present: (i) ReplicaCAD: an artist-authored, annotated, reconfigurable 3D dataset of apartments (matching real spaces) with articulated objects (e.g. cabinets and drawers that can ...

## Source Evidence Cues

- **p. 1 / Abstract - extractive body cue:** We introduce Habitat 2.0 (H2.0), a simulation platform for training virtual robots in interactive 3D environments and complex physics-enabled scenarios.
- **p. 2 / 1 Introduction - extractive body cue:** H2.0 by design and choice does not support non-rigid dynamics (deformables, fluids, films, cloths, ropes), physical state transformations (cutting, drilling, welding, melting), audio or tactile ...
- **p. 7 / 8 GPUs - extractive body cue:** MonolithicRL: a ‘sensors-to-actions' policy trained end-to-end with reinforcement learning (RL).
- **p. 7 / 8 GPUs - extractive body cue:** At every step, it outputs the desired change in end-effector position (δx, δy, δz); the desired end-effector position is fed into an inverse kinematics solver ...
- **p. 2 / 1 Introduction - extractive body cue:** The benefit of this focus is that we were able to design and optimize H2.0 to be exceedingly fast - simulating a Fetch robot interacting ...
- **p. 6 / 8 GPUs - extractive body cue:** 242 ±2 177 ±3 224 ±3 2223 ±3 814 ±2 941 ±2 7192 ±55 3965 ±30 4829 ±50 Table 2: Benchmarking H2.0 performance: simulation steps ...
- **p. 8 / 8 GPUs - extractive body cue:** The controller was described in ‘Action Space' above and is consistent with MonolithicRL.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Task / interface definition | method 비교에 필요한 task·state·action contract를 고정한다 | environment, embodiment, task variation, split | episode, instruction, observation/action schema와 reset rule을 정의 | benchmark episodes | We introduce Habitat 2.0 (H2.0), a simulation platform for training virtual robots in interactive 3D environments and complex physics-enabled scenarios. | p. 1 (Abstract), p. 2 (1 Introduction) |
| Baseline harness | 같은 protocol로 method와 baseline을 실행한다 | episode와 method interface | baseline, ablation, seed, checkpoint와 rollout budget을 통제 | comparable trajectories/scores | H2.0 by design and choice does not support non-rigid dynamics (deformables, fluids, films, cloths, ropes), physical state transformations (cutting, drilling, welding, melting), ... | p. 2 (1 Introduction), p. 7 (8 GPUs) |
| Metric / failure reporting | success 외에 generalization과 failure를 측정한다 | trajectory, log, task outcome | score aggregation, failure taxonomy, efficiency와 reproducibility audit을 적용 | comparison matrix | MonolithicRL: a ‘sensors-to-actions' policy trained end-to-end with reinforcement learning (RL). | p. 7 (8 GPUs), p. 7 (8 GPUs) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 8 / 8 GPUs - extractive body cue:** However, the performance drop of SPA (and qualitative results) suggest that the unseen receptacles (shelf, armchair, tv stand) may be objectively more difficult to pick ...
- **p. 3 / 1 Introduction - extractive body cue:** However, crafting a combined reward function and learning scheme that elicits chaining of such skills for the long-horizon HAB tasks remained out of our reach.
- **p. 2 / 1 Introduction - extractive body cue:** The benefit of this focus is that we were able to design and optimize H2.0 to be exceedingly fast - simulating a Fetch robot interacting ...
- **p. 2 / 1 Introduction - extractive body cue:** We aim to advance the entire ‘research stack' for developing such embodied agents in simulation - (1) data: curating house-scale interactive 3D assets (e.g. kitchens ...
- **p. 6 / 8 GPUs - extractive body cue:** H2.0 single-process with optimizations on is ⇠1200% faster than iGibson (1191 vs 100 SPS).
- **p. 6 / 8 GPUs - extractive body cue:** In contrast, H2.0 single-process with all optimizations turned off is 240% faster (242 vs 100 SPS).
- **Formal bridge:** standardized episode e and interface -> method trajectory/action -> benchmark score and failure cost -> comparable score and protocol validity.
- **Equation/algorithm anchors:** p. 8 (8 GPUs), p. 7 (8 GPUs).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | MonolithicRL, sensors-to-actions, policy, trained, end-to-end, reinforcement, learning, supplementary, analyze, different, sensor, input, modalities, Appendix | standardized observation, action, task state와 evaluation split | body cue; exact tensor/frame verify |
| State/latent | MonolithicRL, sensors-to-actions, policy, trained, end-to-end, reinforcement, learning, supplementary, analyze, different | benchmark state/goal와 method decision | body cue; notation verify |
| Action/output | support, long-term, research, agenda, present, ReplicaCAD, artist-authored, fully-interactive, recreation, FRL-apartment | policy/controller trajectory 또는 measured result | body cue; unit/decoder verify |
| Objective/constraint | However, performance, drop, SPA, qualitative, suggest, unseen, receptacles, shelf, armchair | benchmark score and failure cost | equation anchor required |

## Observation–State–Action Interface

- **p. 7 / 8 GPUs - extractive body cue:** MonolithicRL: a ‘sensors-to-actions' policy trained end-to-end with reinforcement learning (RL).
- **p. 8 / 8 GPUs - extractive body cue:** In the supplementary we also analyze different sensor input modalities (Appendix F.1), the surprising success of "blind" policies (Appendix F.2), the effect of different camera ...
- **p. 7 / 8 GPUs - extractive body cue:** At every step, it outputs the desired change in end-effector position (δx, δy, δz); the desired end-effector position is fed into an inverse kinematics solver ...
- **p. 2 / 1 Introduction - extractive body cue:** The robot operates entirely from onboard sensing - head- and arm-mounted RGB-D cameras, proprioceptive joint-position sensors (for the arm), and egomotion sensors (for the mobile ...
- **p. 2 / 1 Introduction - extractive body cue:** H2.0 by design and choice does not support non-rigid dynamics (deformables, fluids, films, cloths, ropes), physical state transformations (cutting, drilling, welding, melting), audio or tactile ...
- **p. 3 / 1 Introduction - extractive body cue:** Specifically, once the end-effector reaches 15cm (or closer) to an object, a discrete grasp action becomes available that, if executed, snaps the object into its ...
- **p. 6 / 8 GPUs - extractive body cue:** 242 ±2 177 ±3 224 ±3 2223 ±3 814 ±2 941 ±2 7192 ±55 3965 ±30 4829 ±50 Table 2: Benchmarking H2.0 performance: simulation steps ...
- **Normalized interface:** observation=standardized observation, action, task state와 evaluation split; state=benchmark state/goal와 method decision; output/action=policy/controller trajectory 또는 measured result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | benchmark episode/task horizon과 method rollout horizon을 명시해야 한다. | Specifically, we present: (i) ReplicaCAD: an artist-authored, annotated, reconfigurable 3D dataset of apartments (matching real spaces) with articulated objects (e.g. cabinets and ... | episode/sequence/action-chunk boundary |
| Rate / latency | benchmark step/control rate, reset and evaluation throughput을 분리한다. | Thus, our agent predicts the current action at not from the current observations ot but from an observation from 1 timestep ago ... | Hz/fps, inference time and control rate |
| Memory | episode logs, seed/split metadata와 method state/history. | not recovered | window and reset |
| Compute | environment throughput, policy inference와 evaluation parallelism이 결정한다. | This is a fairly standard experimental configuration in robotics (with 30 FPS cameras and 120 Hz control). | hardware, batch and throughput |

## Training vs Inference

- **p. 1 / Abstract - extractive body cue:** We introduce Habitat 2.0 (H2.0), a simulation platform for training virtual robots in interactive 3D environments and complex physics-enabled scenarios.
- **p. 7 / 8 GPUs - extractive body cue:** MonolithicRL: a ‘sensors-to-actions' policy trained end-to-end with reinforcement learning (RL).
- **p. 2 / 1 Introduction - extractive body cue:** Training and testing such robots in hardware directly is slow, expensive, and difficult to reproduce.
- **p. 7 / 8 GPUs - extractive body cue:** The visual input is encoded using a CNN, concatenated with embeddings of proprioceptive-sensing and goal coordinates, and fed to a recurrent actor-critic network, trained with ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** introduce, Habitat, simulation, platform, training, virtual, robots, interactive, environments, complex, physics-enabled, scenarios, design, choice, does, support, non-rigid, dynamics, deformables, fluids.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Task / interface definition | 242 ±2 177 ±3 224 ±3 2223 ±3 814 ±2 941 ±2 7192 ±55 3965 ±30 4829 ±50 Table 2: Benchmarking H2.0 ... | p. 6 (8 GPUs), p. 6 (8 GPUs) |
| Baseline harness | In the more complex task of PrepareGroceries (Figure 5b), TP+SRL outperforms TP+SPA both with and without oracle navigation due to the perception ... | p. 10 (8 GPUs), p. 8 (8 GPUs) |
| Metric / failure reporting | Figure 5: Success rates for Home Assistant Benchmark tasks. Due to the difficulty of full HAB tasks, we analyze performance as completing ... | p. 10 (Figure/Table caption), p. 6 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 8 / 8 GPUs - extractive body cue:** In the supplementary we also analyze different sensor input modalities (Appendix F.1), the surprising success of "blind" policies (Appendix F.2), the effect of different camera ...
- **p. 6 / 8 GPUs - extractive body cue:** The ablations for H2.0 (denoted by ‘- render opts', ‘-physics opts', and ‘-all opts.') show that principles followed in our system design lead to significant ...
- **p. 7 / 8 GPUs - extractive body cue:** The task for the robot is to pick up a target object with center-of-mass coordinates s0 2 R3 (provided in robot's coordinate system) as efficiently ...
- **p. 8 / 8 GPUs - extractive body cue:** PrepareGroceries: Remove 2 objects from the fridge to the counters and place one object back in the fridge (see Fig.
- **p. 9 / 8 GPUs - extractive body cue:** Crafting an SPA pipeline for opening/closing unknown articulated containers is an open unsolved problem in robotics - involving detecting and tracking articulation [66, 67] without ...
- **p. 10 / 8 GPUs - extractive body cue:** Sense-plan-act variants scale poorly to increasing task complexity.
- **p. 10 / 8 GPUs - extractive body cue:** In the more complex task of PrepareGroceries (Figure 5b), TP+SRL outperforms TP+SPA both with and without oracle navigation due to the perception challenge of the ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 1 (Abstract), p. 2 (1 Introduction), p. 7 (8 GPUs), p. 7 (8 GPUs), p. 2 (1 Introduction), p. 6 (8 GPUs), objective p. 8 (8 GPUs), p. 3 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 6 (8 GPUs), p. 6 (8 GPUs), temporal p. 1 (Abstract), p. 5 (2 Related Work), p. 6 (2 Related Work), p. 1 (Abstract), p. 2 (1 Introduction), p. 2 (1 Introduction).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
