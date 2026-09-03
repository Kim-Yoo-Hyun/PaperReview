# Method - Transporter Networks: Rearranging the Visual World for Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (23 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2010.14406; PDF retrieval source: https://arxiv.org/pdf/2010.14406. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 5 (3 Method), p. 5 (3 Method), p. 4 (3 Method), p. 4 (3 Method), p. 6 (3 Method), p. 6 (3 Method)): Placing: Our placing model is a two-stream feed-forward FCN that takes as input the visual observation ot ∈RH×W×4 and outputs two dense feature maps: query features ψ(ot)∈RH×W×d and key features ...

## Method Body Digest

- **p. 5 / 3 Method - extractive body cue:** Placing: Our placing model is a two-stream feed-forward FCN that takes as input the visual observation ot ∈RH×W×4 and outputs two dense feature maps: query ...
- **p. 5 / 3 Method - extractive body cue:** Picking: Our picking model is a single feed-forward FCN that takes as input the visual observation ot∈RH×W×4 and outputs dense pixel-wise values that correlate with ...
- **p. 4 / 3 Method - extractive body cue:** Spatially consistent visual representations enable us to perform visuo-spatial transporting, in which dense pixel-wise features from a partial crop ot[Tpick] centered on Tpick are rigidly ...
- **p. 4 / 3 Method - extractive body cue:** We formulate this as a template matching problem, using cross-correlation with dense feature embeddings ψ(·) and φ(·) from two deep models: Qplace(τ/ot,Tpick)=ψ(ot[Tpick])∗φ(ot)[τ], Tplace=argmax {τi} Qplace(τi/ot,Tpick) ...
- **p. 6 / 3 Method - extractive body cue:** Our training loss is simply the cross-entropy between these one-hot pixel maps and the outputs of the picking and placing models: L=-EYpick[logVpick]-EYplace[logVplace].
- **p. 6 / 3 Method - extractive body cue:** For SE(3) models involving regression, we use a Huber loss on each regression channel.
- **p. 3 / 3 Method - extractive body cue:** As in prior works [31, 32, 33], Transporter Networks use fully convolutional networks (FCNs, commonly used in vision for image segmentation tasks [34]) to model ...
- **p. 5 / 3 Method - extractive body cue:** 8-stride was chosen to balance between maximizing receptive field coverage per pixel prediction, while minimizing loss of resolution in the latent mid-level features of the ...

## Design Rationale

- **p. 3 / 3 Method - extractive body cue:** Transporter Networks decompose the problem into (i) picking and (ii) pick-conditioned placing: fpick(ot)→Tpick fplace(ot,Tpick)→Tplace We present a solution to both with Transporter Networks - but ...
- **p. 1 / 1 Introduction - extractive body cue:** Our method uses 3D reconstruction to project visual data onto a spatiallyconsistent representation as input, with which it is able to better exploit equivariance [13, ...
- **p. 1 / 1 Introduction - extractive body cue:** In this work, we propose the Transporter Network, a simple end-to-end model architecture that preserves spatial structure for vision-based manipulation, without object-centric assumptions: • Manipulation ...

## Source Evidence Cues

- **p. 5 / 3 Method - extractive body cue:** Placing: Our placing model is a two-stream feed-forward FCN that takes as input the visual observation ot ∈RH×W×4 and outputs two dense feature maps: query ...
- **p. 5 / 3 Method - extractive body cue:** Picking: Our picking model is a single feed-forward FCN that takes as input the visual observation ot∈RH×W×4 and outputs dense pixel-wise values that correlate with ...
- **p. 4 / 3 Method - extractive body cue:** Spatially consistent visual representations enable us to perform visuo-spatial transporting, in which dense pixel-wise features from a partial crop ot[Tpick] centered on Tpick are rigidly ...
- **p. 4 / 3 Method - extractive body cue:** We formulate this as a template matching problem, using cross-correlation with dense feature embeddings ψ(·) and φ(·) from two deep models: Qplace(τ/ot,Tpick)=ψ(ot[Tpick])∗φ(ot)[τ], Tplace=argmax {τi} Qplace(τi/ot,Tpick) ...
- **p. 6 / 3 Method - extractive body cue:** Our training loss is simply the cross-entropy between these one-hot pixel maps and the outputs of the picking and placing models: L=-EYpick[logVpick]-EYplace[logVplace].
- **p. 6 / 3 Method - extractive body cue:** For SE(3) models involving regression, we use a Huber loss on each regression channel.
- **p. 3 / 3 Method - extractive body cue:** As in prior works [31, 32, 33], Transporter Networks use fully convolutional networks (FCNs, commonly used in vision for image segmentation tasks [34]) to model ...
- **Detected method headings:** 3 Method (p. 2)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / affordance state | object와 contact-relevant scene을 표현한다 | RGB-D, point cloud, object/task observation | pose, affordance, grasp/contact graph 또는 SE(3) descriptor를 구성 | object/contact state | Placing: Our placing model is a two-stream feed-forward FCN that takes as input the visual observation ot ∈RH×W×4 and outputs two dense ... | p. 5 (3 Method), p. 5 (3 Method) |
| Grasp / trajectory generation | goal을 feasible manipulation candidate로 바꾼다 | geometry/contact state와 task goal | grasp sampling, pose planning, trajectory optimization 또는 policy decoding을 적용 | grasp, pose, force 또는 trajectory | Picking: Our picking model is a single feed-forward FCN that takes as input the visual observation ot∈RH×W×4 and outputs dense pixel-wise values ... | p. 5 (3 Method), p. 4 (3 Method) |
| Contact execution / correction | interaction outcome으로 action을 닫힌 loop로 수정한다 | candidate와 visual/force/tactile feedback | tracking, regrasp, correction, termination 또는 recovery를 수행 | next action/task state | Spatially consistent visual representations enable us to perform visuo-spatial transporting, in which dense pixel-wise features from a partial crop ot[Tpick] centered on ... | p. 4 (3 Method), p. 4 (3 Method) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3 Method - extractive body cue:** 8-stride was chosen to balance between maximizing receptive field coverage per pixel prediction, while minimizing loss of resolution in the latent mid-level features of the ...
- **p. 6 / 3 Method - extractive body cue:** While we only have labels for a single pixel per dense probability map, gradients are passed to all other pixels via image-wide softmax.
- **p. 6 / 3 Method - extractive body cue:** Our training loss is simply the cross-entropy between these one-hot pixel maps and the outputs of the picking and placing models: L=-EYpick[logVpick]-EYplace[logVplace].
- **p. 3 / 3 Method - extractive body cue:** As in prior works [31, 32, 33], Transporter Networks use fully convolutional networks (FCNs, commonly used in vision for image segmentation tasks [34]) to model ...
- **p. 4 / 3 Method - extractive body cue:** We formulate this as a template matching problem, using cross-correlation with dense feature embeddings ψ(·) and φ(·) from two deep models: Qplace(τ/ot,Tpick)=ψ(ot[Tpick])∗φ(ot)[τ], Tplace=argmax {τi} Qplace(τi/ot,Tpick) ...
- **p. 5 / 3 Method - extractive body cue:** Note that this operation can be made fast if implemented with highly optimized matrix multiplication (where the crop is 5
- **Formal bridge:** object geometry/contact state -> grasp/pose/force/trajectory -> task/contact/pose objective -> completion, contact success and robustness.
- **Equation/algorithm anchors:** p. 3 (3 Method), p. 4 (3 Method), p. 5 (3 Method), p. 5 (3 Method), p. 6 (3 Method), p. 6 (3 Method).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Picking, model, single, feed-forward, FCN, takes, input, visual, observation, outputs, dense, pixel-wise, values, correlate | RGB-D/point cloud, object state와 contact/task observation | body cue; exact tensor/frame verify |
| State/latent | Picking, model, single, feed-forward, FCN, takes, input, visual, observation, outputs | object geometry, affordance, contact mode 또는 end-effector state | body cue; notation verify |
| Action/output | Transporter, Networks, decompose, problem, picking, pick-conditioned, placing, fpick, Tpick, fplace | grasp, pose, force 또는 end-effector trajectory | body cue; unit/decoder verify |
| Objective/constraint | stride, chosen, balance, between, maximizing, receptive, field, coverage, pixel, prediction | task/contact/pose objective | equation anchor required |

## Observation–State–Action Interface

- **p. 5 / 3 Method - extractive body cue:** Picking: Our picking model is a single feed-forward FCN that takes as input the visual observation ot∈RH×W×4 and outputs dense pixel-wise values that correlate with ...
- **p. 5 / 3 Method - extractive body cue:** Placing: Our placing model is a two-stream feed-forward FCN that takes as input the visual observation ot ∈RH×W×4 and outputs two dense feature maps: query ...
- **p. 2 / 3 Method - extractive body cue:** Consider the problem of learning pick-and-place actions at with a robot from visual observations ot: f(ot)→at=(Tpick,Tplace)∈A where Tpick is the pose of the end effector ...
- **p. 1 / 1 Introduction - extractive body cue:** In our experiments, Transporter Networks exhibit superior sample efficiency on a number of tabletop manipulation tasks that involve changing the state of the robot's environment ...
- **p. 4 / 3 Method - extractive body cue:** In the planar SE(2) case, we discretize the space of SO(2) rotations into k bins, then rotate the input visual observation ot for each bin. ...
- **p. 6 / 3 Method - extractive body cue:** 3.3 Training: Learning from Demonstrations We assume access to a dataset D = {ζ1,ζ2,...,ζn} of n expert demonstrations, where each trajectory ζi = {(o0,a0),(o1,a1),...} is ...
- **p. 6 / 3 Method - extractive body cue:** During training, we uniformly sample observation-action pairs from the dataset D, from which each action at can be unpacked into two training labels: Tpick and ...
- **Normalized interface:** observation=RGB-D/point cloud, object state와 contact/task observation; state=object geometry, affordance, contact mode 또는 end-effector state; output/action=grasp, pose, force 또는 end-effector trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | grasp/pose proposal에서 contact episode까지의 task horizon; trajectory chunk 여부 확인 필요. | Our visual observation ot is a projection of the scene (e.g., reconstructed from RGB-D images), defined on a regular grid of pixels ... | episode/sequence/action-chunk boundary |
| Rate / latency | perception/planning rate와 low-level contact control rate가 분리된다. | In this work, we consider tasks that can be completed by a sequence of two-pose motion primitives. | Hz/fps, inference time and control rate |
| Memory | object/contact state, current pose와 tactile/force history; exact window 확인 필요. | Extending Transporter Networks with memory to handle non-Markovian tasks would be interesting future work. | window and reset |
| Compute | point/pose encoding, candidate sampling/optimization과 collision/contact checking이 결정한다. | Total inference time (with both picking and placing models) amounts to 200ms on an Nvidia GTX 2080 GPU. | hardware, batch and throughput |

## Training vs Inference

- **p. 6 / 3 Method - extractive body cue:** Our training loss is simply the cross-entropy between these one-hot pixel maps and the outputs of the picking and placing models: L=-EYpick[logVpick]-EYplace[logVplace].
- **p. 6 / 3 Method - extractive body cue:** Total inference time (with both picking and placing models) amounts to 200ms on an Nvidia GTX 2080 GPU.
- **p. 6 / 3 Method - extractive body cue:** Validation performance generally converges after a few hours of training on a single commodity GPU.
- **p. 8 / 4 Results - extractive body cue:** Despite COVID-19 lockdowns preventing physical access, we were still able to perform real experiments using our Unitybased [46] UI that enables people to remotely teleoperate ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Placing, model, two-stream, feed-forward, FCN, takes, input, visual, observation, outputs, dense, feature, maps, query, features, where, dimensionality, Picking, single, pixel-wise.
- **Relevant PDF headings:** 3 Method (p. 2).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / affordance state | Ravens, our simulated benchmark learning environment built with PyBullet [44], consists of a Universal Robot UR5e with a suction gripper overlooking a ... | p. 6 (4 Results), p. 7 (4 Results) |
| Grasp / trajectory generation | Table 6. Ablative comparisons. Task success rate (mean %) vs. # of demonstration episodes (1, 10, 100, or 1000) used in training. ... | p. 20 (Figure/Table caption), p. 6 (Figure/Table caption) |
| Contact execution / correction | Table 2. Baseline comparisons. Task success rate (mean %) vs. # of demonstration episodes (1, 10, 100, or 1000) used in training. ... | p. 7 (Figure/Table caption), p. 6 (4 Results) |

## Failure and Ablation Link

- **p. 4 / Figure/Table caption - extractive body cue:** Figure 4. In this 6-DoF variant of the task presented in Fig. 3, the fixture location varies as well in the out-of-plane rotations (rx, ry), ...
- **p. 6 / 4 Results - extractive body cue:** In this work, we do not use simulation for sim-to-real transfer - rather only as a means to provide a consistent and controlled environment for ...
- **p. 6 / 4 Results - extractive body cue:** Some tasks include multi-modality and permutations - for example, in stacking, a successful 6-block pyramid is invariant to the permutation of blocks within each row, ...
- **p. 7 / 4 Results - extractive body cue:** In our variant of the kit assembly task with unseen objects (shown in Fig.
- **p. 7 / 4 Results - extractive body cue:** We investigate two variants of experts in this setting: (a) one that provides deterministic demonstrations where Tpick, Tplace are fixed relative to the block and ...
- **p. 8 / 4 Results - extractive body cue:** Since it learns pick-conditioned placing, it can also stack plates with varying initial predicted pick locations from only 10 demonstrations on a real robot (bottom ...
- **p. 13 / Figure/Table caption - extractive body cue:** Figure 7. In Towers of Hanoi (a), the task is to sequentially pick-and-place 3 disks from the first peg to the third peg without placing ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 5 (3 Method), p. 5 (3 Method), p. 4 (3 Method), p. 4 (3 Method), p. 6 (3 Method), p. 6 (3 Method), objective p. 5 (3 Method), p. 6 (3 Method), p. 6 (3 Method), p. 3 (3 Method), p. 4 (3 Method), p. 5 (3 Method), temporal p. 3 (3 Method), p. 3 (3 Method), p. 5 (3 Method), p. 5 (3 Method), p. 6 (3 Method), p. 7 (4 Results).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
