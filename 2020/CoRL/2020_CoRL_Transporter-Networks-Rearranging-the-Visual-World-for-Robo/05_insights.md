# Insights — Transporter Networks: Rearranging the Visual World for Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (23 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2010.14406; PDF retrieval source: https://arxiv.org/pdf/2010.14406. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 3 / 3 Method - extractive body cue:** Transporter Networks decompose the problem into (i) picking and (ii) pick-conditioned placing: fpick(ot)→Tpick fplace(ot,Tpick)→Tplace We present a solution to both with Transporter Networks - but ...
- **p. 1 / 1 Introduction - extractive body cue:** Our method uses 3D reconstruction to project visual data onto a spatiallyconsistent representation as input, with which it is able to better exploit equivariance [13, ...
- **p. 1 / 1 Introduction - extractive body cue:** In this work, we propose the Transporter Network, a simple end-to-end model architecture that preserves spatial structure for vision-based manipulation, without object-centric assumptions: • Manipulation ...
- **p. 2 / 1 Introduction - extractive body cue:** We propose a simple model architecture that learns to attend to a local region and predict its spatial displacement, while retaining the spatial structure of ...
- **p. 4 / 3 Method - extractive body cue:** Our method preserves rotation and translation equivariance for efficient learning.
- **p. 5 / 3 Method - extractive body cue:** Placing: Our placing model is a two-stream feed-forward FCN that takes as input the visual observation ot ∈RH×W×4 and outputs two dense feature maps: query ...
- **p. 5 / 3 Method - extractive body cue:** Picking: Our picking model is a single feed-forward FCN that takes as input the visual observation ot∈RH×W×4 and outputs dense pixel-wise values that correlate with ...
- **Contribution anchor:** p. 3 (3 Method), p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 4 (3 Method), p. 5 (3 Method)

### Strongest assumption and failure boundary

- **p. 1 / 1 Introduction - extractive body cue:** This naturally leads us to ask: is there structure that we can incorporate into our end-to-end models to improve their learning efficiency, without imposing any ...
- **p. 1 / 1 Introduction - extractive body cue:** Prior end-to-end models [1, 2] often use convolutional architectures with raw images, in which valuable spatial information can be lost to perspective distortions.
- **p. 2 / 1 Introduction - extractive body cue:** They do not require any prior knowledge of the objects to be manipulated - they rely only on information contained within partial RGB-D data from ...
- **p. 2 / 1 Introduction - extractive body cue:** On 10 unique tabletop manipulation tasks, Transporter Networks trained from scratch are capable of achieving greater than 90% success on most tasks with objects in ...
- **p. 8 / 5 Conclusion - extractive body cue:** In terms of its current limitations: it is sensitive to camera-robot calibration, and it remains unclear how to integrate torque/force actions with spatial action spaces.
- **p. 6 / 4 Results - extractive body cue:** Performance is evaluated with a metric from 0 (failure) to 100 (success).
- **p. 19 / Figure/Table caption - extractive body cue:** Figure 9. Depictions of the generalization ability of different models on the simplified translation-only block-insertion task. Each episode is visualized as a mark on the ...
- **Boundary to test:** In terms of its current limitations: it is sensitive to camera-robot calibration, and it remains unclear how to integrate torque/force actions with spatial action spaces.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Transporter Networks decompose the problem into (i) picking and (ii) pick-conditioned placing: fpick(ot)→Tpick fplace(ot,Tpick)→Tplace We present a solution to both with Transporter Networks - but in this work, our primary contribution ... | p. 3 (3 Method), p. 1 (1 Introduction) |
| Reported outcome | Table 2. Baseline comparisons. Task success rate (mean %) vs. # of demonstration episodes (1, 10, 100, or 1000) used in training. Generalizing to Unseen Objects. Three of our benchmark tasks involve ... | p. 7 (Figure/Table caption), p. 6 (4 Results) |
| Failure/limitation | In terms of its current limitations: it is sensitive to camera-robot calibration, and it remains unclear how to integrate torque/force actions with spatial action spaces. | p. 8 (5 Conclusion), p. 6 (4 Results) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `RGB-D/point cloud, object state와 contact/task observation → object geometry, affordance, contact mode 또는 end-effector state → grasp, pose, force 또는 end-effector trajectory`.
- 이 논문의 재사용 가능한 지점은 Picking: Our picking model is a single feed-forward FCN that takes as input the visual observation ot∈RH×W×4 and outputs dense pixel-wise values that correlate with picking success: Vpick∈RH×W = softmax(Qpick((u,v)/ot)).를 Placing: Our placing model is a two-stream feed-forward FCN that takes as input the visual observation ot ∈RH×W×4 and outputs two dense feature maps: query features ψ(ot)∈RH×W×d and key features φ(ot)∈RH×W×d, where ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 object geometry, affordance, contact mode 또는 end-effector state가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 In terms of its current limitations: it is sensitive to camera-robot calibration, and it remains unclear how to integrate torque/force actions with spatial action spaces.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Transporter Networks decompose the problem into (i) picking and (ii) pick-conditioned placing: fpick(ot)→Tpick fplace(ot,Tpick)→Tplace We present a solution to both with Transporter Networks - but in this work, our primary contribution ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `Manipulation, contact, tactile, and dexterity`; tags: `Robotics, Vision-Language-Action, equivariance, Imitation Learning`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** In terms of its current limitations: it is sensitive to camera-robot calibration, and it remains unclear how to integrate torque/force actions with spatial action spaces.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Ravens, our simulated benchmark learning environment built with PyBullet [44], consists of a Universal Robot UR5e with a suction gripper overlooking a 0.5×1m tabletop workspace, with 3 simulated 640x480 RGB-D cameras pointing ....
3. Compare against the body-reported baseline or a matched simpler baseline: Table 6. Ablative comparisons. Task success rate (mean %) vs. # of demonstration episodes (1, 10, 100, or 1000) used in training. 6.12 Training Convergence We train Transporter Networks with Adam [53], ....
4. Report the body metric and its denominator/aggregation: Task success rate (mean %) vs. # of demonstration episodes (1, 10, 100, or 1000) used in training..
5. Re-run the body-reported ablation/failure condition: Figure 4. In this 6-DoF variant of the task presented in Fig. 3, the fixture location varies as well in the out-of-plane rotations (rx, ry), and height (z). Transporter Networks can address ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 5 (3 Method), p. 5 (3 Method), p. 4 (3 Method); the primary result is directionally consistent at p. 7 (Figure/Table caption), p. 6 (4 Results), p. 6 (4 Results); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 Transporter, Networks, decompose mechanism이 Table 6. Ablative comparisons. Task success rate (mean %) vs. # of demonstration episodes (1, 10, ... 대비 Task success rate (mean %) vs. # of demonstration episodes (1, 10, 100, or 1000) used in training.을 개선하고, In terms of its current limitations: it is sensitive to camera-robot calibration, and it remains unclear ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
