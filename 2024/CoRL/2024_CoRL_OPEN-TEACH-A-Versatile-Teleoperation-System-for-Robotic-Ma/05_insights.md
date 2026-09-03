# Insights — OPEN TEACH: A Versatile Teleoperation System for Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (20 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v270/iyer25a.html; PDF retrieval source: https://arxiv.org/pdf/2403.07870. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / I. INTRODUCTION - extractive body cue:** The contributions of this work is summarized as follows: 1) We present OPEN TEACH, an open-source system for plug-and-play teleoperation framework suitable for collecting demonstrations ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** In this work, we present OPEN TEACH, an open-source framework for robot teleoperation that supports a variety of robots, including bimanual and multi-finger manipulation, all ...
- **p. 4 / IV. OPEN TEACH - extractive body cue:** In this section, we provide details about the VR-based teleoperation setup and the system design that enables data collection using this framework.
- **p. 4 / IV. OPEN TEACH - extractive body cue:** We observe that OPEN TEACH is the only framework that enables controlling multiple arms, hands, and mobile manipulators, is calibration-free, and is completely open-source.
- **p. 5 / IV. OPEN TEACH - extractive body cue:** The high frame rate streaming enables reactive control by the user, while widgets for visualizing the robot's camera view help the user focus on fine-grained ...
- **p. 3 / III. BACKGROUND ON IMITATION LEARNING - extractive body cue:** For both of these methods, the first phase involves obtaining a non-parametric base-policy πb : Z →A with encoded representations z ∈Z and actions a ...
- **p. 3 / III. BACKGROUND ON IMITATION LEARNING - extractive body cue:** Behavior Cloning Given a dataset of expert rollouts for a desired task in the form of observation and action pairs D == {(o, a)} ⊂O ...
- **Contribution anchor:** p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 4 (IV. OPEN TEACH), p. 4 (IV. OPEN TEACH), p. 5 (IV. OPEN TEACH), p. 3 (III. BACKGROUND ON IMITATION LEARNING)

### Strongest assumption and failure boundary

- **p. 2 / I. INTRODUCTION - extractive body cue:** The challenge of easy-to-use teleoperation devices is more apparent in dexterous manipulation problems [24, 47, 3, 4], owing to the high dimensional action space.
- **p. 2 / I. INTRODUCTION - extractive body cue:** Recently proposed exoskeleton-based teleoperation frameworks like ALOHA [67], GELLO [61], and AirExo [14] attempt to alleviate this problem by having the human teleoperator directly control ...
- **p. 3 / III. BACKGROUND ON IMITATION LEARNING - extractive body cue:** Following this convention, the objective of BC is to find the value θ that maximizes the probability of the observed data. θ∗= argmax θ Y ...
- **p. 8 / VI. LIMITATIONS AND DISCUSSION - extractive body cue:** However, we recognize a few limitations in this work: (a) OPEN TEACH relies on the accuracy of the in-built hand pose detection in the VR ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 3: The demonstration collection process as viewed from within the VR application. Shown here is one task being performed for each real-world setup. High ...
- **Boundary to test:** However, we recognize a few limitations in this work: (a) OPEN TEACH relies on the accuracy of the in-built hand pose detection in the VR headset.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | The contributions of this work is summarized as follows: 1) We present OPEN TEACH, an open-source system for plug-and-play teleoperation framework suitable for collecting demonstrations across different robot morphologies in both simula ... | p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| Reported outcome | Overall, the learned policies achieve an average success rate of 86% across all tasks and robot morphologies. | p. 6 (4) How intuitive is the system for new users?), p. 6 (4) How intuitive is the system for new users?) |
| Failure/limitation | However, we recognize a few limitations in this work: (a) OPEN TEACH relies on the accuracy of the in-built hand pose detection in the VR headset. | p. 8 (VI. LIMITATIONS AND DISCUSSION), p. 5 (Figure/Table caption) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Paper-specific interface:** Human-to-Robot Retargeting Hardware Network Server Hand Pose Detection Pose Detection Wrist Pose Detection Camera Stream Visual Feedback Oculus Passthrough Fig. (p. 4, III. BACKGROUND ON IMITATION LEARNING).
- **Paper-specific mechanism:** The contributions of this work is summarized as follows: 1) We present OPEN TEACH, an open-source system for plug-and-play teleoperation framework suitable for collecting demonstrations across different robot morphologies in ... (p. 2, I. INTRODUCTION).
- **Evidence boundary:** the reported outcome is Robot Setup Task Number of Demos Success Rate Franka-Allegro Open Box 3 9/10 Grasp Sponge 6 7/10 Pick Up Tea Sachet 4 7/10 Grasp Object and Twist 6 8/10 Allegro ... (p. 8, 4) How intuitive is the system for new users?); the relevant task/metric cue is Overall, the learned policies achieve an average success rate of 86% across all tasks and robot morphologies. (p. 6, 4) How intuitive is the system for new users?). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** However, we recognize a few limitations in this work: (a) OPEN TEACH relies on the accuracy of the in-built hand pose detection in the VR headset. (p. 8, VI. LIMITATIONS AND DISCUSSION).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `Manipulation, contact, tactile, and dexterity`; tags: `Robotics, teleoperation, cross-embodiment, dexterous manipulation, bimanual manipulation, data collection`.
- **Reading predecessor in the generated track queue:** Octopi: Object Property Reasoning with Large Tactile-Language Models (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** end of this track queue (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** However, we recognize a few limitations in this work: (a) OPEN TEACH relies on the accuracy of the in-built hand pose detection in the VR headset.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: Human-to-Robot Retargeting Hardware Network Server Hand Pose Detection Pose Detection Wrist Pose Detection Camera Stream Visual Feedback Oculus Passthrough Fig. (p. 4, III. BACKGROUND ON IMITATION LEARNING); preserve the objective/update rule: The aforementioned devices are cost-effective and easy to set up. (p. 2, I. INTRODUCTION).
2. Use the paper-reported task/data/environment cue: Our experiments and tasks are designed to answer the following questions: 1) How versatile is OPEN TEACH across a range of robotics setups? (p. 6, V. EXPERIMENTAL EVALUATION).
3. Compare against the reported or matched baseline: On these tasks, OPEN TEACH demonstrates a higher success rate along with significantly reduced median time to complete tasks compared to the other baselines. (p. 8, 4) How intuitive is the system for new users?).
4. Report the body metric with its denominator and aggregation: Overall, the learned policies achieve an average success rate of 86% across all tasks and robot morphologies. (p. 6, 4) How intuitive is the system for new users?).
5. Re-run the reported ablation or stress/failure condition: Each setup is a combination of a variant of a robot arm with either an Allegro Hand or a 2-fingered gripper. (p. 6, 4) How intuitive is the system for new users?); if none is reported, design one around: However, we recognize a few limitations in this work: (a) OPEN TEACH relies on the accuracy of the in-built hand pose detection in the VR headset. (p. 8, VI. LIMITATIONS AND DISCUSSION).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), match the reported outcome at p. 8 (4) How intuitive is the system for new users?), p. 6 (V. EXPERIMENTAL EVALUATION), p. 5 (Figure/Table caption), and measure the boundary at p. 8 (VI. LIMITATIONS AND DISCUSSION), p. 8 (4) How intuitive is the system for new users?).

## Falsifiable research question

Under the paper's stated interface (Human-to-Robot Retargeting Hardware Network Server Hand Pose Detection Pose Detection Wrist Pose Detection Camera Stream Visual Feedback Oculus Passthrough Fig.), does the paper-specific mechanism (The contributions of this work is summarized as follows: 1) We present OPEN TEACH, an open-source system for plug-and-play teleoperation framework suitable ...) retain the reported evaluation outcome (Overall, the learned policies achieve an average success rate of 86% across all tasks and robot morphologies.) when tested against the paper's strongest explicit boundary (However, we recognize a few limitations in this work: (a) OPEN TEACH relies on the accuracy of the ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (Overall, the learned policies achieve an average success rate of 86% across all tasks and robot morphologies.) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (20 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** The contributions of this work is summarized as follows: 1) We present OPEN TEACH, an open-source system for plug-and-play teleoperation framework suitable for collecting demonstrations across different robot morphologies in ... (p. 2, I. INTRODUCTION).
- **Paper-supported outcome:** Robot Setup Task Number of Demos Success Rate Franka-Allegro Open Box 3 9/10 Grasp Sponge 6 7/10 Pick Up Tea Sachet 4 7/10 Grasp Object and Twist 6 8/10 Allegro ... (p. 8, 4) How intuitive is the system for new users?).
- **Strongest explicit boundary:** However, we recognize a few limitations in this work: (a) OPEN TEACH relies on the accuracy of the in-built hand pose detection in the VR headset. (p. 8, VI. LIMITATIONS AND DISCUSSION).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
