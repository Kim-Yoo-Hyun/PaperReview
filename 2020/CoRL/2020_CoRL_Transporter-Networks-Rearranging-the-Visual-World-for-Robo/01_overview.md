# Transporter Networks: Rearranging the Visual World for Robotic Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (23 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2010.14406.
> PDF retrieval source: https://arxiv.org/pdf/2010.14406. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2020 / CoRL
- Authors: not duplicated here when not verified in the registry source
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: REFERENCE
- Tags: Robotics, Vision-Language-Action, equivariance, Imitation Learning
- Official paper: https://arxiv.org/abs/2010.14406
- Full-text retrieval: https://arxiv.org/pdf/2010.14406
- Code/Project: https://github.com/google-research/ravens
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (23 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Manipulation, contact, tactile, and dexterity의 manipulation 문제를 이해하기 위해 읽는다. 본문은 This naturally leads us to ask: is there structure that we can incorporate into our end-to-end models to improve their learning efficiency, without imposing any of the limitations or burdens of explicit ...를 문제로 두고, Transporter Networks decompose the problem into (i) picking and (ii) pick-conditioned placing: fpick(ot)→Tpick fplace(ot,Tpick)→Tplace We present a solution to both with Transporter Networks - but in this work, our primary contribution ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / 1 Introduction - extractive body cue:** End-to-end models that map directly from pixels to actions hold the capacity to learn complex manipulation skills, but are known to require copious amounts of ...
- **p. 1 / 1 Introduction - extractive body cue:** Integrating object-centric assumptions - e.g., object keypoints [3, 4, 5, 6], embeddings [7, 8], or dense descriptors [9, 10, 11] - has been shown to ...
- **p. 1 / 1 Introduction - extractive body cue:** However, these representations often impose data collection burdens (i.e., configuring scenes with specific singulated objects) and still struggle to address challenging scenarios with unseen classes ...
- **p. 1 / 1 Introduction - extractive body cue:** This naturally leads us to ask: is there structure that we can incorporate into our end-to-end models to improve their learning efficiency, without imposing any ...
- **p. 1 / 1 Introduction - extractive body cue:** In this work, we propose the Transporter Network, a simple end-to-end model architecture that preserves spatial structure for vision-based manipulation, without object-centric assumptions: • Manipulation ...
- **p. 1 / 1 Introduction - extractive body cue:** Prior end-to-end models [1, 2] often use convolutional architectures with raw images, in which valuable spatial information can be lost to perspective distortions.
- **p. 2 / 1 Introduction - extractive body cue:** They do not require any prior knowledge of the objects to be manipulated - they rely only on information contained within partial RGB-D data from ...

## Core Idea

- **p. 3 / 3 Method - extractive body cue:** Transporter Networks decompose the problem into (i) picking and (ii) pick-conditioned placing: fpick(ot)→Tpick fplace(ot,Tpick)→Tplace We present a solution to both with Transporter Networks - but ...
- **p. 1 / 1 Introduction - extractive body cue:** Our method uses 3D reconstruction to project visual data onto a spatiallyconsistent representation as input, with which it is able to better exploit equivariance [13, ...
- **p. 1 / 1 Introduction - extractive body cue:** In this work, we propose the Transporter Network, a simple end-to-end model architecture that preserves spatial structure for vision-based manipulation, without object-centric assumptions: • Manipulation ...
- **p. 2 / 1 Introduction - extractive body cue:** We propose a simple model architecture that learns to attend to a local region and predict its spatial displacement, while retaining the spatial structure of ...
- **p. 4 / 3 Method - extractive body cue:** Our method preserves rotation and translation equivariance for efficient learning.
- **p. 5 / 3 Method - extractive body cue:** Placing: Our placing model is a two-stream feed-forward FCN that takes as input the visual observation ot ∈RH×W×4 and outputs two dense feature maps: query ...
- **p. 5 / 3 Method - extractive body cue:** Picking: Our picking model is a single feed-forward FCN that takes as input the visual observation ot∈RH×W×4 and outputs dense pixel-wise values that correlate with ...
- **p. 4 / 3 Method - extractive body cue:** Spatially consistent visual representations enable us to perform visuo-spatial transporting, in which dense pixel-wise features from a partial crop ot[Tpick] centered on Tpick are rigidly ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Picking: Our picking model is a single feed-forward FCN that takes as input the visual observation ot∈RH×W×4 and outputs dense pixel-wise values that correlate with picking success: Vpick∈RH×W = softmax(Qpick((u,v)/ot)). | RGB-D/point cloud, object state와 contact/task observation | p. 5 (3 Method), p. 5 (3 Method) |
| State/latent | Picking, model, single, feed-forward, FCN, takes, input, visual, observation, outputs, dense, pixel-wise | object geometry, affordance, contact mode 또는 end-effector state | p. 5 (3 Method), p. 5 (3 Method), p. 2 (3 Method) |
| Output/action | Placing: Our placing model is a two-stream feed-forward FCN that takes as input the visual observation ot ∈RH×W×4 and outputs two dense feature maps: query features ψ(ot)∈RH×W×d and key features φ(ot)∈RH×W×d, where ... | grasp, pose, force 또는 end-effector trajectory | p. 5 (3 Method), p. 2 (3 Method), p. 1 (1 Introduction) |
| Objective/outcome | 8-stride was chosen to balance between maximizing receptive field coverage per pixel prediction, while minimizing loss of resolution in the latent mid-level features of the network. | task completion, contact success, pose/force error와 generalization | p. 5 (3 Method), p. 6 (3 Method), p. 6 (3 Method) |

## Main Claims and Actual Contribution

- **p. 3 / 3 Method - extractive body cue:** Transporter Networks decompose the problem into (i) picking and (ii) pick-conditioned placing: fpick(ot)→Tpick fplace(ot,Tpick)→Tplace We present a solution to both with Transporter Networks - but ...
- **p. 1 / 1 Introduction - extractive body cue:** Our method uses 3D reconstruction to project visual data onto a spatiallyconsistent representation as input, with which it is able to better exploit equivariance [13, ...
- **p. 1 / 1 Introduction - extractive body cue:** In this work, we propose the Transporter Network, a simple end-to-end model architecture that preserves spatial structure for vision-based manipulation, without object-centric assumptions: • Manipulation ...
- **p. 2 / 1 Introduction - extractive body cue:** We propose a simple model architecture that learns to attend to a local region and predict its spatial displacement, while retaining the spatial structure of ...
- **p. 4 / 3 Method - extractive body cue:** Our method preserves rotation and translation equivariance for efficient learning.
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2. Baseline comparisons. Task success rate (mean %) vs. # of demonstration episodes (1, 10, 100, or 1000) used in training. Generalizing to Unseen ...
- **p. 6 / 4 Results - extractive body cue:** We report results with the models that have achieved highest validation performance during training, averaged over 100 unseen test runs for each task.
- **p. 6 / 4 Results - extractive body cue:** Our method does not require 3 cameras - having more cameras only improves visual coverage.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (Figure/Table caption), p. 6 (4 Results) |
| Embodiment/environment | Ravens, our simulated benchmark learning environment built with PyBullet [44], consists of a Universal Robot UR5e with a suction gripper overlooking a 0.5×1m tabletop workspace, with 3 simulated 640x480 RGB-D cameras pointing ... | hardware/simulator version and reset protocol | p. 6 (4 Results), p. 7 (4 Results) |
| Dataset/benchmark | 2 shows sample efficiency of baselines trained from stochastic demonstrations for each task, and evaluated on unseen test settings, with random rotations and translations of objects (including target zones). | role, split, size and leakage | p. 6 (4 Results), p. 7 (4 Results), p. 7 (4 Results), p. 6 (4 Results) |
| Metric | Task success rate (mean %) vs. # of demonstration episodes (1, 10, 100, or 1000) used in training. | definition, denominator, direction and uncertainty | p. 7 (4 Results), p. 6 (4 Results), p. 6 (4 Results) |
| Baseline/ablation | Table 6. Ablative comparisons. Task success rate (mean %) vs. # of demonstration episodes (1, 10, 100, or 1000) used in training. 6.12 Training Convergence We train Transporter Networks with Adam [53], ... | fair input/data/compute/action matching | p. 20 (Figure/Table caption), p. 6 (Figure/Table caption), p. 6 (4 Results) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 5 Conclusion - extractive body cue:** In terms of its current limitations: it is sensitive to camera-robot calibration, and it remains unclear how to integrate torque/force actions with spatial action spaces.
- **p. 6 / 4 Results - extractive body cue:** Performance is evaluated with a metric from 0 (failure) to 100 (success).
- **p. 19 / Figure/Table caption - extractive body cue:** Figure 9. Depictions of the generalization ability of different models on the simplified translation-only block-insertion task. Each episode is visualized as a mark on the ...
- **p. 7 / 4 Results - extractive body cue:** For example, when a stack of blocks falls over, they can re-build the stack of blocks as if they had just started the task.
- **p. 6 / 4 Results - extractive body cue:** Our method does not require 3 cameras - having more cameras only improves visual coverage.
- **p. 7 / 4 Results - extractive body cue:** We hypothesize that equivariance to rotations and translations enable them to learn these recovery behaviors even with little data on multi-step tasks (see Tab.

## Why Read It

Manipulation, contact, tactile, and dexterity의 manipulation 문제를 이해하기 위해 읽는다. 본문은 This naturally leads us to ask: is there structure that we can incorporate into our end-to-end models to improve their learning efficiency, without imposing any of the limitations or burdens of explicit ...를 문제로 두고, Transporter Networks decompose the problem into (i) picking and (ii) pick-conditioned placing: fpick(ot)→Tpick fplace(ot,Tpick)→Tplace We present a solution to both with Transporter Networks - but in this work, our primary contribution ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 5 (3 Method), p. 5 (3 Method) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
