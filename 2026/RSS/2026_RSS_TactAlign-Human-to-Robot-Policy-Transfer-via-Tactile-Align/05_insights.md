# Insights — TactAlign: Human-to-Robot Policy Transfer via Tactile Alignment

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (16 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://roboticsconference.org/program/papers/6/; PDF retrieval source: https://roboticsconference.org/program/papers/6/. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 3 / III. METHODOLOGY - extractive body cue:** Our method consists of two stages: self-supervised representation learning and cross-embodiment alignment via pseudo-pairs.
- **p. 2 / I. INTRODUCTION - extractive body cue:** The core contributions of our work are: • We propose TactAlign, a method for aligning crosssensor tactile data from unpaired demonstrations of the same task.
- **p. 2 / I. INTRODUCTION - extractive body cue:** TactAlign leverages rectified flow with noisy pseudo-pairs to learn a latent mapping that enables H2R policy transfer between humans and robots equipped with heterogeneous tactile ...
- **p. 4 / III. METHODOLOGY - extractive body cue:** Second: We propose incorporating pseudo-pairs into rectified flow to guide the velocity field toward desired correspondences between the source and target distributions.
- **p. 1 / I. INTRODUCTION - extractive body cue:** In contrast, our proposed method enables tactile transfer from unpaired datasets of the same task without requiring such pairing assumptions.
- **p. 3 / III. METHODOLOGY - extractive body cue:** We use a learnable length-1 query between the encoder and decoder to produce a fixed-dimensional latent representation via cross-attention pooling.
- **p. 3 / III. METHODOLOGY - extractive body cue:** A learnable length 1 query is implemented between the encoder and decoder to output a fixeddimensional latent representations after the cross-attention module.
- **Contribution anchor:** p. 3 (III. METHODOLOGY), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 4 (III. METHODOLOGY), p. 1 (I. INTRODUCTION), p. 3 (III. METHODOLOGY)

### Strongest assumption and failure boundary

- **p. 1 / I. INTRODUCTION - extractive body cue:** This strict pairing can be prohibitively difficult to maintain during contact-rich interactions involving sliding contact or dynamic object motion necessary for general manipulation.
- **p. 1 / I. INTRODUCTION - extractive body cue:** While effective, many of these approaches assume identical tactile sensors or little to no embodiment gap, which simplifies transfer but limits applicability across diverse robot ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** However, existing methods primarily focus on static contact scenarios [30, 29, 11, 10] and coarse semanticlevel alignment objectives [10, 51], leaving their effectiveness for continuous ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Moreover, these approaches often rely on paired supervision or labels, limiting scalability across heterogeneous sensors and robots.
- **p. 8 / V. LIMITATION - extractive body cue:** Moreover, tactile alignment alone does not address visual discrepancies between human and robot embodiments.
- **p. 8 / V. LIMITATION - extractive body cue:** Incorporating vision and other modalities into a unified multi-modal policy is also an important direction for future work.
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3: Red and blue indicate two subsets of the source distribution. The left side of each of the three panels shows the provided training ...
- **Boundary to test:** Moreover, tactile alignment alone does not address visual discrepancies between human and robot embodiments.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Our method consists of two stages: self-supervised representation learning and cross-embodiment alignment via pseudo-pairs. | p. 3 (III. METHODOLOGY), p. 2 (I. INTRODUCTION) |
| Reported outcome | Fig. 8: Lid Closing Task. With randomized grasps, the policy uses touch to perform search, alignment, and closing between the lid and the bottle. We show human data improves generalization to unseen ... | p. 7 (Figure/Table caption), p. 5 (IV. EXPERIMENTS AND RESULTS) |
| Failure/limitation | Moreover, tactile alignment alone does not address visual discrepancies between human and robot embodiments. | p. 8 (V. LIMITATION), p. 8 (V. LIMITATION) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `tactile image/force, vision과 proprioceptive history → contact geometry, force state 또는 latent dynamics → grasp/contact action, force command 또는 object motion`.
- 이 논문의 재사용 가능한 지점은 However, most existing human-to-robot (H2R) approaches omit tactile feedback entirely and instead focus on transferring more readily available observations such as egocentric vision or state-action pairs in configuration space.를 Problem Statement Our goal is to learn a latent-space mapping that transfers human tactile observations to robot tactile observations.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 contact geometry, force state 또는 latent dynamics가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Moreover, tactile alignment alone does not address visual discrepancies between human and robot embodiments.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Our method consists of two stages: self-supervised representation learning and cross-embodiment alignment via pseudo-pairs.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `Manipulation, contact, tactile, and dexterity`; tags: `Robotics, tactile, cross-embodiment, human-to-robot transfer, contact-rich manipulation, dexterity, representation alignment`.
- **Reading predecessor in the generated track queue:** Tabero: Learning Gentle Manipulation with Closed-Loop Force Feedback from Vision, Touch, and Language (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** DexterityGen: Foundation Controller for Unprecedented Dexterity (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Moreover, tactile alignment alone does not address visual discrepancies between human and robot embodiments.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: The dataset includes 1,472 robot force samples (24:1 train:test split) and 1,527 human force samples used only for evaluation..
3. Compare against the body-reported baseline or a matched simpler baseline: Fig. 10: ℓ1 force prediction error (mean ± std) along each axis, averaged over five evaluations. G →R evaluates force prediction on the robot using human tactile signals, with (blue) and without ....
4. Report the body metric and its denominator/aggregation: Fig. 10: ℓ1 force prediction error (mean ± std) along each axis, averaged over five evaluations. G →R evaluates force prediction on the robot using human tactile signals, with (blue) and without ....
5. Re-run the body-reported ablation/failure condition: Fig. 6: Pivoting Task. The task begins in a non-contact state and transitions to pivoting upon contact detection via tactile feedback, with the goal of maintaining contact without dropping the object. Top: ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 3 (III. METHODOLOGY), p. 3 (III. METHODOLOGY), p. 2 (III. METHODOLOGY); the primary result is directionally consistent at p. 7 (Figure/Table caption), p. 5 (IV. EXPERIMENTS AND RESULTS); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 consists, stages, self-supervised mechanism이 Fig. 10: ℓ1 force prediction error (mean ± std) along each axis, averaged over five evaluations. ... 대비 Fig. 10: ℓ1 force prediction error (mean ± std) along each axis, averaged over five evaluations. G →R ...을 개선하고, Moreover, tactile alignment alone does not address visual discrepancies between human and robot embodiments. 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
