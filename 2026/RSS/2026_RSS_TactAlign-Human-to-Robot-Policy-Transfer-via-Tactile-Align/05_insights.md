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

- **Paper-specific interface:** We use f g i , pg i and f r j , pr j to denote the tactile observation and pose of a single fingertip at independent time indices ... (p. 3, III. METHODOLOGY).
- **Paper-specific mechanism:** The core contributions of our work are: • We propose TactAlign, a method for aligning crosssensor tactile data from unpaired demonstrations of the same task. (p. 2, I. INTRODUCTION).
- **Evidence boundary:** the reported outcome is The dataset includes 1,472 robot force samples (24:1 train:test split) and 1,527 human force samples used only for evaluation. (p. 5, IV. EXPERIMENTS AND RESULTS); the relevant task/metric cue is Successful execution therefore depends on detecting contact onset and reasoning about contact throughout the task as in Fig. (p. 5, IV. EXPERIMENTS AND RESULTS). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** Without alignment, the success rate is also 0%, with failures primarily arising from jamming, from which the policy cannot recover, often leading to complete unscrewing of the light bulb. (p. 7, 8. The pivoting and insertion).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `Manipulation, contact, tactile, and dexterity`; tags: `Robotics, tactile, cross-embodiment, human-to-robot transfer, contact-rich manipulation, dexterity, representation alignment`.
- **Reading predecessor in the generated track queue:** Tabero: Learning Gentle Manipulation with Closed-Loop Force Feedback from Vision, Touch, and Language (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** DexterityGen: Foundation Controller for Unprecedented Dexterity (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Moreover, tactile alignment alone does not address visual discrepancies between human and robot embodiments.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: We use f g i , pg i and f r j , pr j to denote the tactile observation and pose of a single fingertip at independent time indices ... (p. 3, III. METHODOLOGY); preserve the objective/update rule: In step2, we aggregate the learned latents from both domains to construct pseudo-pairs (h∗, r∗), and learn a velocity field vθ that transports the glove latent distribution to the robot ... (p. 3, III. METHODOLOGY).
2. Use the paper-reported task/data/environment cue: The dataset includes 1,472 robot force samples (24:1 train:test split) and 1,527 human force samples used only for evaluation. (p. 5, IV. EXPERIMENTS AND RESULTS).
3. Compare against the reported or matched baseline: Successful execution therefore depends on detecting contact onset and reasoning about contact throughout the task as in Fig. (p. 5, IV. EXPERIMENTS AND RESULTS).
4. Report the body metric with its denominator and aggregation: Successful execution therefore depends on detecting contact onset and reasoning about contact throughout the task as in Fig. (p. 5, IV. EXPERIMENTS AND RESULTS).
5. Re-run the reported ablation or stress/failure condition: Successful execution therefore depends on detecting contact onset and reasoning about contact throughout the task as in Fig. (p. 5, IV. EXPERIMENTS AND RESULTS); if none is reported, design one around: Without alignment, the success rate is also 0%, with failures primarily arising from jamming, from which the policy cannot recover, often leading to complete unscrewing of the light bulb. (p. 7, 8. The pivoting and insertion).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), match the reported outcome at p. 5 (IV. EXPERIMENTS AND RESULTS), p. 8 (Figure/Table caption), p. 7 (Figure/Table caption), and measure the boundary at p. 7 (8. The pivoting and insertion), p. 8 (V. LIMITATION).

## Falsifiable research question

Under the paper's stated interface (We use f g i , pg i and f r j , pr j to denote the tactile observation and pose ...), does the paper-specific mechanism (The core contributions of our work are: • We propose TactAlign, a method for aligning crosssensor tactile data from unpaired demonstrations of ...) retain the reported evaluation outcome (Successful execution therefore depends on detecting contact onset and reasoning about contact throughout the task as in Fig.) when tested against the paper's strongest explicit boundary (Without alignment, the success rate is also 0%, with failures primarily arising from jamming, from which the policy ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (Successful execution therefore depends on detecting contact onset and reasoning about contact throughout the task as in Fig.) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (16 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** The core contributions of our work are: • We propose TactAlign, a method for aligning crosssensor tactile data from unpaired demonstrations of the same task. (p. 2, I. INTRODUCTION).
- **Paper-supported outcome:** The dataset includes 1,472 robot force samples (24:1 train:test split) and 1,527 human force samples used only for evaluation. (p. 5, IV. EXPERIMENTS AND RESULTS).
- **Strongest explicit boundary:** Without alignment, the success rate is also 0%, with failures primarily arising from jamming, from which the policy cannot recover, often leading to complete unscrewing of the light bulb. (p. 7, 8. The pivoting and insertion).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
