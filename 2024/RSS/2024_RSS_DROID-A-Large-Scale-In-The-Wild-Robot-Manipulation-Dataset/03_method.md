# Method - DROID: A Large-Scale In-The-Wild Robot Manipulation Dataset

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (26 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2403.12945; PDF retrieval source: https://arxiv.org/pdf/2403.12945. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 6 (IV. DROID DATASET ANALYSIS), p. 4 (III. DROID DATA COLLECTION SETUP), p. 4 (III. DROID DATA COLLECTION SETUP), p. 1 (Abstract), p. 1 (13 Institutions), p. 2 (I. INTRODUCTION)): We use the point of first gripper closing in every episode as a proxy for interactions in the dataset and visualize the 3D location of these interaction points for different ...

## Method Body Digest

- **p. 6 / IV. DROID DATASET ANALYSIS - extractive body cue:** We use the point of first gripper closing in every episode as a proxy for interactions in the dataset and visualize the 3D location of ...
- **p. 4 / III. DROID DATA COLLECTION SETUP - extractive body cue:** We use the Polymetis controller [33] and record actions both in robot joint space and in end-effector space at a control frequency of 15Hz.
- **p. 4 / III. DROID DATA COLLECTION SETUP - extractive body cue:** For each trajectory, we record the output of all RGB cameras, relevant low level state information from the robot, equivalent robot control commands from various ...
- **p. 1 / Abstract - extractive body cue:** In this work, we introduce DROID (Distributed Robot Interaction Dataset), a diverse robot manipulation dataset with arXiv:2403.12945v2 [cs.RO] 22 Apr 2025
- **p. 1 / 13 Institutions - extractive body cue:** 1: We introduce DROID (Distributed Robot Interaction Dataset), an "in-the-wild" robot manipulation dataset with 76k trajectories or 350 hours of interaction data, collected across 564 ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** However, creating such datasets is challenging: in contrast to vision or language data, training manipulation policies typically requires robot manipulation data with recorded observations and ...
- **p. 3 / III. DROID DATA COLLECTION SETUP - extractive body cue:** In this work, we introduce DROID (Distributed Robot Interaction Dataset), an open-source robot manipulation dataset that provides for very high diversity and variability of scenes, ...
- **p. 4 / III. DROID DATA COLLECTION SETUP - extractive body cue:** We use the same hardware setup across all 13 institutions to streamline data collection while maximizing portability and flexibility.

## Design Rationale

- **p. 2 / I. INTRODUCTION - extractive body cue:** In this work, we introduce DROID (Distributed Robot Interaction Dataset), a robot manipulation dataset of unprecedented diversity (see Fig.
- **p. 1 / 13 Institutions - extractive body cue:** 1: We introduce DROID (Distributed Robot Interaction Dataset), an "in-the-wild" robot manipulation dataset with 76k trajectories or 350 hours of interaction data, collected across 564 ...
- **p. 3 / III. DROID DATA COLLECTION SETUP - extractive body cue:** In this section, we introduce our hardware setup and the data collection protocol.

## Source Evidence Cues

- **p. 6 / IV. DROID DATASET ANALYSIS - extractive body cue:** We use the point of first gripper closing in every episode as a proxy for interactions in the dataset and visualize the 3D location of ...
- **p. 4 / III. DROID DATA COLLECTION SETUP - extractive body cue:** We use the Polymetis controller [33] and record actions both in robot joint space and in end-effector space at a control frequency of 15Hz.
- **p. 4 / III. DROID DATA COLLECTION SETUP - extractive body cue:** For each trajectory, we record the output of all RGB cameras, relevant low level state information from the robot, equivalent robot control commands from various ...
- **p. 1 / Abstract - extractive body cue:** In this work, we introduce DROID (Distributed Robot Interaction Dataset), a diverse robot manipulation dataset with arXiv:2403.12945v2 [cs.RO] 22 Apr 2025
- **p. 1 / 13 Institutions - extractive body cue:** 1: We introduce DROID (Distributed Robot Interaction Dataset), an "in-the-wild" robot manipulation dataset with 76k trajectories or 350 hours of interaction data, collected across 564 ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** However, creating such datasets is challenging: in contrast to vision or language data, training manipulation policies typically requires robot manipulation data with recorded observations and ...
- **p. 3 / III. DROID DATA COLLECTION SETUP - extractive body cue:** In this work, we introduce DROID (Distributed Robot Interaction Dataset), an open-source robot manipulation dataset that provides for very high diversity and variability of scenes, ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Data schema / normalization | heterogeneous robot trajectory를 공통 sample로 만든다 | observation, action, task와 embodiment metadata | sensor/action schema alignment, filtering, normalization을 수행 | shared dataset representation | We use the point of first gripper closing in every episode as a proxy for interactions in the dataset and visualize the ... | p. 6 (IV. DROID DATASET ANALYSIS), p. 4 (III. DROID DATA COLLECTION SETUP) |
| Coverage / augmentation | task·embodiment·failure variation을 확장한다 | dataset과 metadata | retargeting, relabeling, synthetic/teleoperation augmentation 또는 sampling을 적용 | expanded data support | We use the Polymetis controller [33] and record actions both in robot joint space and in end-effector space at a control frequency ... | p. 4 (III. DROID DATA COLLECTION SETUP), p. 4 (III. DROID DATA COLLECTION SETUP) |
| Downstream learning interface | 정규화된 data를 policy/representation이 사용한다 | shared observations/actions | pretraining, BC, action-token 또는 representation learning을 수행 | checkpoint/policy action | For each trajectory, we record the output of all RGB cameras, relevant low level state information from the robot, equivalent robot control ... | p. 4 (III. DROID DATA COLLECTION SETUP), p. 1 (Abstract) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / III. DROID DATA COLLECTION SETUP - extractive body cue:** We use the same hardware setup across all 13 institutions to streamline data collection while maximizing portability and flexibility.
- **p. 4 / III. DROID DATA COLLECTION SETUP - extractive body cue:** When designing the collection protocol for DROID, we focused on the following objectives: (1) preventing common data collection mistakes like "camera cannot see robot" or ...
- **p. 3 / III. DROID DATA COLLECTION SETUP - extractive body cue:** 2), a hardware platform for data collection that is shared between all institutions, allowing us to quickly set up new data collection units and roll ...
- **Formal bridge:** trajectory D with task/embodiment metadata -> normalized sample or downstream action -> coverage/data efficiency/transfer objective -> cross-domain transfer and task performance.
- **Equation/algorithm anchors:** p. 4 (III. DROID DATA COLLECTION SETUP), p. 3 (III. DROID DATA COLLECTION SETUP).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | trajectory, record, output, RGB, cameras, relevant, level, state, information, robot, equivalent, control, commands, various | multi-view observation, language/task label과 action trajectory | body cue; exact tensor/frame verify |
| State/latent | trajectory, record, output, RGB, cameras, relevant, level, state, information, robot | shared representation, embodiment/task identity와 data distribution | body cue; notation verify |
| Action/output | introduce, DROID, Distributed, Robot, Interaction, Dataset, manipulation, unprecedented, diversity, Fig | dataset sample 또는 learned policy action | body cue; unit/decoder verify |
| Objective/constraint | same, hardware, setup, across, institutions, streamline, data, collection, while, maximizing | coverage/data efficiency/transfer objective | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / III. DROID DATA COLLECTION SETUP - extractive body cue:** For each trajectory, we record the output of all RGB cameras, relevant low level state information from the robot, equivalent robot control commands from various ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** However, creating such datasets is challenging: in contrast to vision or language data, training manipulation policies typically requires robot manipulation data with recorded observations and ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** In experiments across 6 tasks and 4 locations, from labs to offices and real households, we find that DROID boosts policy performance, robustness and generalizability ...
- **p. 3 / Dataset - extractive body cue:** Additionally, recent works suggest that diffusion denoising models [22] are a powerful parametrization for multimodal action output distributions that combine expressivity with scalability [7, 16, ...
- **p. 1 / 13 Institutions - extractive body cue:** Each DROID episode contains three synchronized RGB camera streams, camera calibration, depth information, and natural language instructions.
- **p. 4 / III. DROID DATA COLLECTION SETUP - extractive body cue:** We record image observations with three synchronized stereo camera streams: two exterior Zed 2 cameras, table-mounted on adjustable tripods to quickly adapt to a new ...
- **p. 5 / IV. DROID DATASET ANALYSIS - extractive body cue:** For each dataset, we run our analysis using one randomly sampled third-person camera frame per episode and the provided language instruction annotations.
- **Normalized interface:** observation=multi-view observation, language/task label과 action trajectory; state=shared representation, embodiment/task identity와 data distribution; output/action=dataset sample 또는 learned policy action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | trajectory demonstration horizon; training sample window와 deployment task horizon을 분리한다. | In line with prior work [7], we train the diffusion policy to generate 16-step action sequences, and during rollouts, step 8 actions ... | episode/sequence/action-chunk boundary |
| Rate / latency | data recording/action sampling rate와 policy inference/control rate를 분리한다. | The waffle maker position is randomized between episodes. | Hz/fps, inference time and control rate |
| Memory | trajectory, embodiment/task metadata와 dataset index. | not recovered | window and reset |
| Compute | data decoding, normalization/augmentation과 downstream training budget이 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 2 / I. INTRODUCTION - extractive body cue:** However, creating such datasets is challenging: in contrast to vision or language data, training manipulation policies typically requires robot manipulation data with recorded observations and ...
- **p. 3 / III. DROID DATA COLLECTION SETUP - extractive body cue:** This includes the full dataset under CC-BY 4.0 license, an interactive dataset visualizer, code for training generalizable policies on DROID, pre-trained policy checkpoints, and a ...
- **p. 7 / V. EXPERIMENTS - extractive body cue:** We first downsample the camera observations to a resolution of 128 × 128 and use a ResNet-50 visual encoder pre-trained on ImageNet [11] to encode ...
- **p. 8 / V. EXPERIMENTS - extractive body cue:** Similarly, in the multi-step Cook Lentils task, baselines tend to fail after two or sometimes just one step, while co-training with DROID is the only ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** point, first, gripper, closing, every, episode, proxy, interactions, dataset, visualize, location, interaction, points, different, datasets, Fig, Polymetis, controller, record, actions.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Data schema / normalization | Overall, we find that DROID significantly increases diversity in tasks, objects, scenes, viewpoints and interaction locations over existing large scale robot manipulation ... | p. 5 (IV. DROID DATASET ANALYSIS), p. 3 (Dataset) |
| Coverage / augmentation | One of the unique benefits of DROID compared to existing robot datasets is its amount of scene diversity. | p. 8 (V. EXPERIMENTS), p. 8 (V. EXPERIMENTS) |
| Downstream learning interface | Fig. 8: Does DROID Improve Policy Performance and Robustness? We find that across all our evaluation tasks, co-training with DROID significantly improves ... | p. 9 (Figure/Table caption), p. 7 (V. EXPERIMENTS) |

## Failure and Ablation Link

- **p. 6 / IV. DROID DATASET ANALYSIS - extractive body cue:** We then use GPT4 to de-duplicate the verbs, i.e., remove synonyms and typos.
- **p. 7 / V. EXPERIMENTS - extractive body cue:** The out of distribution variant consists of toasting novel objects.
- **p. 7 / V. EXPERIMENTS - extractive body cue:** The out of distribution variant involves placing a distractor plate on the table.
- **p. 8 / V. EXPERIMENTS - extractive body cue:** Cook Lentils: The robot needs to remove the pan lid, pick up and pour lentils into the pan, and turn on the stove(add distractor objects).
- **p. 8 / V. EXPERIMENTS - extractive body cue:** We remove the Language Table dataset [35], equivalent to 5% of the Octo training mix, due to its repetitive scene layouts and tasks, and its ...
- **p. 16 / Figure/Table caption - extractive body cue:** Fig. 11: DROID data collection GUI. Top left: Screen for entering feasible tasks for the current scene. Tasks can either be selected from a list ...
- **p. 17 / Figure/Table caption - extractive body cue:** Fig. 12: Qualitative examples of scenes in DROID. We use GPT-4V to categorize scenes into 9 scene types. DROID contains robot manipulation demonstrations in a ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 6 (IV. DROID DATASET ANALYSIS), p. 4 (III. DROID DATA COLLECTION SETUP), p. 4 (III. DROID DATA COLLECTION SETUP), p. 1 (Abstract), p. 1 (13 Institutions), p. 2 (I. INTRODUCTION), objective p. 4 (III. DROID DATA COLLECTION SETUP), p. 4 (III. DROID DATA COLLECTION SETUP), p. 3 (III. DROID DATA COLLECTION SETUP), temporal p. 7 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 8 (V. EXPERIMENTS), p. 8 (V. EXPERIMENTS), p. 5 (IV. DROID DATASET ANALYSIS), p. 1 (13 Institutions).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
