# Insights — PP-Tac: Paper Picking Using Omnidirectional Tactile Feedback in Dexterous Robotic Hands

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (14 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p056.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p056.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 5 / V. POLICY LEARNING FOR PAPER-PICKING - extractive body cue:** To address this, we propose a visionindependent tactile-based approach. ‘The core idea leverages tactile feedback to maintain contact conditions (as defined in Section IV), facilitating ...
- **p. 6 / A. Implementation Details - extractive body cue:** Thus, the entire inference process consists of 10 steps.
- **p. 5 / IV. PROBLEM STATEMENT - extractive body cue:** In practice, our approach solved this problem by adopting a Iearing-based policy rather than a model-based optimization paradigm.
- **p. 8 / B. Depth Reconstruction of VBTS - extractive body cue:** These evaluations showcase the robustness and adaptability of our approach,
- **p. 4 / IV. PROBLEM STATEMENT - extractive body cue:** This research introduces a novel approach to tackle the paper picking problem that was previously unexplored.
- **p. 6 / A. Implementation Details - extractive body cue:** Our diffusion policy is implemented as a fourlayer Transformer encoder with a latent dimension of 512 and four attention heads.
- **p. 6 / B. PP-Tac Policy - extractive body cue:** Such an overparameterized input allows the network to extract more robust and expressive latent features for the diffusion policy.
- **Contribution anchor:** p. 5 (V. POLICY LEARNING FOR PAPER-PICKING), p. 6 (A. Implementation Details), p. 5 (IV. PROBLEM STATEMENT), p. 8 (B. Depth Reconstruction of VBTS), p. 4 (IV. PROBLEM STATEMENT), p. 6 (A. Implementation Details)

### Strongest assumption and failure boundary

- **p. 4 / IV. PROBLEM STATEMENT - extractive body cue:** Next, we aim to address the challenge of grasping thin, deformable paper-like objects from flat surfaces.
- **p. 4 / IV. PROBLEM STATEMENT - extractive body cue:** Although creases or irregularities in the ‘material can sometimes provide grasping points, a particularly challenging scenario arises when the object is extremely flat and lacks ...
- **p. 5 / IV. PROBLEM STATEMENT - extractive body cue:** One challenge is determining the control inputs for all finger joints and the hand pose (i.e. the end-effector pose of the manipulator).
- **p. 5 / IV. PROBLEM STATEMENT - extractive body cue:** In practice, our approach solved this problem by adopting a Iearing-based policy rather than a model-based optimization paradigm.
- **p. 9 / B. Depth Reconstruction of VBTS - extractive body cue:** As shown in the "Non-disturbance" baseline in Section VI-C, removing data disturbance led to a notable performance drop across all experiments, often resulting in complete ...
- **p. 6 / VI. EXPERIMENTS - extractive body cue:** We also compare our system with various manipulators to highlight its advantages and limitations (Section VI-D).
- **p. 6 / A. Grasp Motion Dataset Synthesis - extractive body cue:** After filtering out collision-prone sequences, we obtained a dataset of 500,000 grasp samples, ‘each consisting of Naxa ~ 100 frames.
- **Boundary to test:** As shown in the "Non-disturbance" baseline in Section VI-C, removing data disturbance led to a notable performance drop across all experiments, often resulting in complete failure when grasping stiff objects, such as ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | To address this, we propose a visionindependent tactile-based approach. ‘The core idea leverages tactile feedback to maintain contact conditions (as defined in Section IV), facilitating the creation of a buckling region for ... | p. 5 (V. POLICY LEARNING FOR PAPER-PICKING), p. 6 (A. Implementation Details) |
| Reported outcome | Fig. 9: Experiment results. Evaluations were conducted to quantify the success rate of grasping four different flat objects (paper. plastic bag, ‘loth, and paper bag) across four terrain setups (plane, slope, book ... | p. 9 (Figure/Table caption), p. 6 (VI. EXPERIMENTS) |
| Failure/limitation | As shown in the "Non-disturbance" baseline in Section VI-C, removing data disturbance led to a notable performance drop across all experiments, often resulting in complete failure when grasping stiff objects, such as ... | p. 9 (B. Depth Reconstruction of VBTS), p. 6 (VI. EXPERIMENTS) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Paper-specific interface:** One challenge is determining the control inputs for all finger joints and the hand pose (i.e. the end-effector pose of the manipulator). (p. 5, IV. PROBLEM STATEMENT).
- **Paper-specific mechanism:** Despite recent advances in robotic Robots are increasingly popular as assistive agents in evhardware and embodied Al, existing systems continue to struggle eryday life, particularly within household environments (3) with ... (p. 1, Abstract).
- **Evidence boundary:** the reported outcome is Fig. 9: Experiment results. Evaluations were conducted to quantify the success rate of grasping four different flat objects (paper. plastic bag, ‘loth, and paper bag) across four terrain setups (plane, ... (p. 9, Figure/Table caption); the relevant task/metric cue is Next, we show the quantitative and qualitative results of the depth reconstruction of our VBTS (Section VI-B). (p. 6, VI. EXPERIMENTS). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** However, vision-based methods often struggle in real-world DOM tasks due to variability in object appearance, unknown physical properties, visual occlusions [25, 6], and inconsistent lighting conditions [48, 22) ‘These limitations ... (p. 2, A. Deformable Object Manipulation).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `Manipulation, contact, tactile, and dexterity`; tags: `Robotics, tactile sensing, dexterous manipulation, deformable objects, force control, slip detection`.
- **Reading predecessor in the generated track queue:** V-HOP: Visuo-Haptic 6D Object Pose Tracking (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** GeoDEx: A Unified Geometric Framework for Tactile Dexterous and Extrinsic Manipulation under Force Uncertainty (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** As shown in the "Non-disturbance" baseline in Section VI-C, removing data disturbance led to a notable performance drop across all experiments, often resulting in complete failure when grasping stiff objects, such as ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: One challenge is determining the control inputs for all finger joints and the hand pose (i.e. the end-effector pose of the manipulator). (p. 5, IV. PROBLEM STATEMENT); preserve the objective/update rule: We implement this through the PPTac policy, developed in two stages: 1) Trajectory Optimization: Generate a dataset of grasping motions using trajectory ‘optimization. (p. 5, V. POLICY LEARNING FOR PAPER-PICKING).
2. Use the paper-reported task/data/environment cue: of the proposed algorithms on a physical robotic system, Both the hardware design and code for the PP-Tac system are publicly released to support further research and. community development, (p. 2, 4) We provide a full implementation and systematic evaluation).
3. Compare against the reported or matched baseline: Then, we per form systematic comparisons of our system on different flat ‘materials and supporting terrains (Section VI-C). (p. 6, VI. EXPERIMENTS).
4. Report the body metric with its denominator and aggregation: Next, we show the quantitative and qualitative results of the depth reconstruction of our VBTS (Section VI-B). (p. 6, VI. EXPERIMENTS).
5. Re-run the reported ablation or stress/failure condition: Last, ablation studies are conducted to examine the influence of parameters, and the necessary training steps (Section VI-E). (p. 6, VI. EXPERIMENTS); if none is reported, design one around: However, vision-based methods often struggle in real-world DOM tasks due to variability in object appearance, unknown physical properties, visual occlusions [25, 6], and inconsistent lighting conditions [48, 22) ‘These limitations ... (p. 2, A. Deformable Object Manipulation).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 1 (Abstract), p. 4 (IV. PROBLEM STATEMENT), match the reported outcome at p. 9 (Figure/Table caption), p. 6 (VI. EXPERIMENTS), p. 2 (4) We provide a full implementation and systematic evaluation), and measure the boundary at p. 2 (A. Deformable Object Manipulation), p. 6 (VI. EXPERIMENTS).

## Falsifiable research question

Under the paper's stated interface (One challenge is determining the control inputs for all finger joints and the hand pose (i.e. the end-effector pose of the manipulator).), does the paper-specific mechanism (Despite recent advances in robotic Robots are increasingly popular as assistive agents in evhardware and embodied Al, existing systems continue to struggle ...) retain the reported evaluation outcome (Next, we show the quantitative and qualitative results of the depth reconstruction of our VBTS (Section VI-B).) when tested against the paper's strongest explicit boundary (However, vision-based methods often struggle in real-world DOM tasks due to variability in object appearance, unknown physical properties, ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (Next, we show the quantitative and qualitative results of the depth reconstruction of our VBTS (Section VI-B).) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (14 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** Despite recent advances in robotic Robots are increasingly popular as assistive agents in evhardware and embodied Al, existing systems continue to struggle eryday life, particularly within household environments (3) with ... (p. 1, Abstract).
- **Paper-supported outcome:** Fig. 9: Experiment results. Evaluations were conducted to quantify the success rate of grasping four different flat objects (paper. plastic bag, ‘loth, and paper bag) across four terrain setups (plane, ... (p. 9, Figure/Table caption).
- **Strongest explicit boundary:** However, vision-based methods often struggle in real-world DOM tasks due to variability in object appearance, unknown physical properties, visual occlusions [25, 6], and inconsistent lighting conditions [48, 22) ‘These limitations ... (p. 2, A. Deformable Object Manipulation).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
