# Evaluation - Transporter Networks: Rearranging the Visual World for Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (23 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2010.14406; PDF retrieval source: https://arxiv.org/pdf/2010.14406. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (Figure/Table caption), p. 6 (4 Results), p. 6 (4 Results), p. 7 (4 Results), p. 8 (4 Results), p. 20 (Figure/Table caption)): Table 2. Baseline comparisons. Task success rate (mean %) vs. # of demonstration episodes (1, 10, 100, or 1000) used in training. Generalizing to Unseen Objects. Three of our benchmark ...

## Evaluation Body Digest

- **p. 6 / 4 Results - extractive PDF cue:** Ravens, our simulated benchmark learning environment built with PyBullet [44], consists of a Universal Robot UR5e with a suction gripper overlooking a 0.5×1m tabletop workspace, ...
- **p. 7 / 4 Results - extractive PDF cue:** Three of our benchmark tasks involve generalizing to unseen objects (see Tab.
- **p. 7 / 4 Results - extractive PDF cue:** 2 shows sample efficiency of baselines trained from stochastic demonstrations for each task, and evaluated on unseen test settings, with random rotations and translations of ...
- **p. 6 / 4 Results - extractive PDF cue:** In simulation, we benchmark on 10 discrete-time tabletop manipulation tasks, some which require closed-loop visual feedback for multi-step sequencing.
- **p. 8 / 4 Results - extractive PDF cue:** Since it learns pick-conditioned placing, it can also stack plates with varying initial predicted pick locations from only 10 demonstrations on a real robot (bottom ...
- **p. 8 / 4 Results - extractive PDF cue:** Transporter Networks test performance on real robots with human demonstration data.
- **p. 7 / 4 Results - extractive PDF cue:** Task success rate (mean %) vs. # of demonstration episodes (1, 10, 100, or 1000) used in training.
- **p. 6 / 4 Results - extractive PDF cue:** Performance is evaluated with a metric from 0 (failure) to 100 (success).

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** rigid/articulated object와 robot manipulator contact scene.
- **Input boundary:** RGB-D/point cloud, object state와 contact/task observation.
- **Output/decision under evaluation:** grasp, pose, force 또는 end-effector trajectory.
- **Primary target:** task completion, contact success, pose/force error와 generalization.
- **Detected evaluation headings:** 4 Results (p. 6).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 2. Baseline comparisons. Task success rate (mean %) vs. # of demonstration episodes (1, 10, 100, or 1000) used in training. Generalizing to ... | p. 7 (Figure/Table caption) |
| 4 Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | We report results with the models that have achieved highest validation performance during training, averaged over 100 unseen test runs for each task. | p. 6 (4 Results) |
| 4 Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our method does not require 3 cameras - having more cameras only improves visual coverage. | p. 6 (4 Results) |
| 4 Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | In general, Transporter Networks achieve orders of magnitude more sample efficiency than the image-based alternatives, and also provides better sample efficiency than multi-layer perceptrons ... | p. 7 (4 Results) |
| 4 Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | On this more challenging task, our model demonstrates considerably better sample efficiency than the image-based baselines achieved on the strictly-easier 3DoF-only block-insertion task (Tab. | p. 8 (4 Results) |

## Dataset / Benchmark Role

- **p. 6 / 4 Results - extractive PDF cue:** Ravens, our simulated benchmark learning environment built with PyBullet [44], consists of a Universal Robot UR5e with a suction gripper overlooking a 0.5×1m tabletop workspace, ...
- **p. 7 / 4 Results - extractive PDF cue:** Three of our benchmark tasks involve generalizing to unseen objects (see Tab.
- **p. 7 / 4 Results - extractive PDF cue:** 2 shows sample efficiency of baselines trained from stochastic demonstrations for each task, and evaluated on unseen test settings, with random rotations and translations of ...
- **p. 6 / 4 Results - extractive PDF cue:** In simulation, we benchmark on 10 discrete-time tabletop manipulation tasks, some which require closed-loop visual feedback for multi-step sequencing.
- **p. 8 / 4 Results - extractive PDF cue:** Since it learns pick-conditioned placing, it can also stack plates with varying initial predicted pick locations from only 10 demonstrations on a real robot (bottom ...
- **p. 8 / 4 Results - extractive PDF cue:** Transporter Networks test performance on real robots with human demonstration data.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 1. A Transporter Network is a simple model architecture that attends to a local region and predicts its spatial displacement (b) from visual input ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2. Simple planar pick-and-place task where (i) there is a distri- bution of successful pick poses, and (ii) for each successful pick pose, there ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 3. In this setting (a) where the task is to pick up the red block with an immobilizing grasp (e.g., suction) and place it ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 4. In this 6-DoF variant of the task presented in Fig. 3, the fixture location varies as well in the out-of-plane rotations (rx, ry), ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 1. Each task in Ravens is characterized by a unique set of attributes. We use behavior cloning simulation experiments to compare with baselines. In ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 2. Baseline comparisons. Task success rate (mean %) vs. # of demonstration episodes (1, 10, 100, or 1000) used in training. Generalizing to Unseen ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 3. Simplified 2DoF (no rotation) block-insertion is harder to learn with demonstrations from a stochastic oracle than a deterministic one. Sample Complexity in Simplified ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 5. Transporter Networks can predict the desired spatial displacements of piles of small objects (left), which informs how to push them towards a target ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Ravens, our simulated benchmark learning environment built with PyBullet [44], consists of a Universal Robot UR5e with a suction gripper overlooking a 0.5×1m tabletop ... | embodiment, simulator version and control stack | p. 6 (4 Results), p. 7 (4 Results) |
| Task/environment | Three of our benchmark tasks involve generalizing to unseen objects (see Tab. | reset, timeout, object/scene variation | p. 7 (4 Results), p. 7 (4 Results) |
| Observation/sensor | RGB-D/point cloud, object state와 contact/task observation | calibration, preprocessing, privileged input | p. 5 (3 Method), p. 5 (3 Method) |
| Output/decision | grasp, pose, force 또는 end-effector trajectory | action frame, controller and termination | p. 2 (3 Method), p. 1 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Task success rate (mean %) vs. # of demonstration episodes (1, 10, 100, or 1000) used in training. | definition/direction/unit from same section | p. 7 (4 Results) |
| Performance is evaluated with a metric from 0 (failure) to 100 (success). | definition/direction/unit from same section | p. 6 (4 Results) |
| We report results with the models that have achieved highest validation performance during training, averaged over 100 unseen test runs for each task. | definition/direction/unit from same section | p. 6 (4 Results) |
| Consider a simplified translation-only block-insertion task illustrated in Fig. | definition/direction/unit from same section | p. 7 (4 Results) |
| Transporter Networks test performance on real robots with human demonstration data. | definition/direction/unit from same section | p. 8 (4 Results) |
| For kit assembly, the robot uses a suction gripper and an industrial Photoneo PhoXi camera (for high resolution and accurate IR-depth). | definition/direction/unit from same section | p. 8 (4 Results) |
| Figure 3. In this setting (a) where the task is to pick up the red block with an immobilizing grasp (e.g., suction) and place ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| Figure 7. In Towers of Hanoi (a), the task is to sequentially pick-and-place 3 disks from the first peg to the third peg without ... | definition/direction/unit from same section | p. 13 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Table 6. Ablative comparisons. Task success rate (mean %) vs. # of demonstration episodes (1, 10, 100, or 1000) used in training. 6.12 Training ... | comparison identity and matched condition | p. 20 (Figure/Table caption) |
| Table 1. Each task in Ravens is characterized by a unique set of attributes. We use behavior cloning simulation experiments to compare with baselines. ... | comparison identity and matched condition | p. 6 (Figure/Table caption) |
| Each task comes with a scripted oracle that provides expert demonstrations by randomly sampling the distribution of successful Tpick and Tplace - samples of ... | comparison identity and matched condition | p. 6 (4 Results) |
| Simplified 2DoF (no rotation) block-insertion is harder to learn with demonstrations from a stochastic oracle than a deterministic one. | comparison identity and matched condition | p. 7 (4 Results) |
| The benchmark is difficult - most baselines, while capable of over-fitting to the demonstration training set, generalize poorly with only 1,000 demonstrations. | comparison identity and matched condition | p. 7 (4 Results) |
| Most baselines perform well with deterministic demonstrations, but begin to struggle with stochastic ones. | comparison identity and matched condition | p. 8 (4 Results) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 4. In this 6-DoF variant of the task presented in Fig. 3, the fixture location varies as well in the out-of-plane rotations (rx, ... | component/input/data sensitivity | p. 4 (Figure/Table caption) |
| In this work, we do not use simulation for sim-to-real transfer - rather only as a means to provide a consistent and controlled environment ... | component/input/data sensitivity | p. 6 (4 Results) |
| Some tasks include multi-modality and permutations - for example, in stacking, a successful 6-block pyramid is invariant to the permutation of blocks within each ... | component/input/data sensitivity | p. 6 (4 Results) |
| In our variant of the kit assembly task with unseen objects (shown in Fig. | component/input/data sensitivity | p. 7 (4 Results) |
| We investigate two variants of experts in this setting: (a) one that provides deterministic demonstrations where Tpick, Tplace are fixed relative to the block ... | component/input/data sensitivity | p. 7 (4 Results) |
| Since it learns pick-conditioned placing, it can also stack plates with varying initial predicted pick locations from only 10 demonstrations on a real robot ... | component/input/data sensitivity | p. 8 (4 Results) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Transporter Networks decompose the problem into (i) picking and (ii) pick-conditioned placing: fpick(ot)→Tpick fplace(ot,Tpick)→Tplace We present a solution to both with Transporter Networks - ... | Table 2. Baseline comparisons. Task success rate (mean %) vs. # of demonstration episodes (1, 10, 100, or 1000) used in training. Generalizing to ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (Figure/Table caption), p. 6 (4 Results), p. 6 (4 Results), p. 7 (4 Results), p. 8 (4 Results), p. 20 (Figure/Table caption) |
| Primary metric/result | We report results with the models that have achieved highest validation performance during training, averaged over 100 unseen test runs for each task. | numeric claim only at cited anchor | p. 6 (4 Results) |

- Numeric sentences retained from the body:
- **p. 6 / 4 Results - extractive PDF cue:** Ravens, our simulated benchmark learning environment built with PyBullet [44], consists of a Universal Robot UR5e with a suction gripper overlooking a 0.5×1m tabletop workspace, ...
- **p. 5 / 3 Method - extractive PDF cue:** 3.2 Network Architecture Observation Space: For tabletop manipulation, our visual observation ot is an orthographic top-down view of a 0.5×1m tabletop workspace, generated in simulation ...
- **p. 5 / 3 Method - extractive PDF cue:** The top-down image ot has a pixel resolution of 160×320 - each pixel represents a 3.125×3.125mm vertical column of 3D space in the workspace.
- **p. 6 / 3 Method - extractive PDF cue:** Total inference time (with both picking and placing models) amounts to 200ms on an Nvidia GTX 2080 GPU.
- **p. 6 / 3 Method - extractive PDF cue:** 4), we evaluate Transporter Networks in their ability to learn from n = 1, 10, 100, or 1,000 demonstrations per task.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | In terms of its current limitations: it is sensitive to camera-robot calibration, and it remains unclear how to integrate torque/force actions with spatial action ... | p. 8 (5 Conclusion) |
| body limitation/failure cue | Performance is evaluated with a metric from 0 (failure) to 100 (success). | p. 6 (4 Results) |
| body limitation/failure cue | Figure 9. Depictions of the generalization ability of different models on the simplified translation-only block-insertion task. Each episode is visualized as a mark on ... | p. 19 (Figure/Table caption) |
| body limitation/failure cue | For example, when a stack of blocks falls over, they can re-build the stack of blocks as if they had just started the task. | p. 7 (4 Results) |
| body limitation/failure cue | Our method does not require 3 cameras - having more cameras only improves visual coverage. | p. 6 (4 Results) |
| body limitation/failure cue | We hypothesize that equivariance to rotations and translations enable them to learn these recovery behaviors even with little data on multi-step tasks (see Tab. | p. 7 (4 Results) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Total inference time (with both picking and placing models) amounts to 200ms on an Nvidia GTX 2080 GPU. | p. 6 (3 Method) |
| Rotations of the crop around the pick are used to decode the best placing rotation. | p. 4 (3 Method) |
| Our placing model shares a similar hourglass encoder decoder architecture as the picking model: each stream is an 8-stride 43-layer ResNet, but without non-linear ... | p. 5 (3 Method) |
| Our picking model is an hourglass encoder decoder architecture: a 43-layer residual network (ResNet) [41] with 12 residual blocks and 8-stride (3 2-stride convolutions ... | p. 5 (3 Method) |
| Validation performance generally converges after a few hours of training on a single commodity GPU. | p. 6 (3 Method) |
| For kit assembly, the robot uses a suction gripper and an industrial Photoneo PhoXi camera (for high resolution and accurate IR-depth). | p. 8 (4 Results) |
| Despite COVID-19 lockdowns preventing physical access, we were still able to perform real experiments using our Unitybased [46] UI that enables people to remotely ... | p. 8 (4 Results) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 5 Conclusion - extractive PDF cue:** In terms of its current limitations: it is sensitive to camera-robot calibration, and it remains unclear how to integrate torque/force actions with spatial action spaces.
- **p. 6 / 4 Results - extractive PDF cue:** Performance is evaluated with a metric from 0 (failure) to 100 (success).
- **p. 19 / Figure/Table caption - extractive PDF cue:** Figure 9. Depictions of the generalization ability of different models on the simplified translation-only block-insertion task. Each episode is visualized as a mark on the ...
- **p. 7 / 4 Results - extractive PDF cue:** For example, when a stack of blocks falls over, they can re-build the stack of blocks as if they had just started the task.
- **p. 6 / 4 Results - extractive PDF cue:** Our method does not require 3 cameras - having more cameras only improves visual coverage.
- **p. 7 / 4 Results - extractive PDF cue:** We hypothesize that equivariance to rotations and translations enable them to learn these recovery behaviors even with little data on multi-step tasks (see Tab.

- **PDF anchors reviewed:** datasets p. 6 (4 Results), p. 7 (4 Results), p. 7 (4 Results), p. 6 (4 Results), p. 8 (4 Results), p. 8 (4 Results), metrics p. 7 (4 Results), p. 6 (4 Results), p. 6 (4 Results), p. 7 (4 Results), p. 8 (4 Results), p. 8 (4 Results), baselines p. 20 (Figure/Table caption), p. 6 (Figure/Table caption), p. 6 (4 Results), p. 7 (4 Results), p. 7 (4 Results), p. 8 (4 Results), results p. 7 (Figure/Table caption), p. 6 (4 Results), p. 6 (4 Results), p. 7 (4 Results), p. 8 (4 Results), p. 20 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
