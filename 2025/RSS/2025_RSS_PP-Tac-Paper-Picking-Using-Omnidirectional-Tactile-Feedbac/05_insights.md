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

- **Closed-loop position:** `tactile image/force, vision과 proprioceptive history → contact geometry, force state 또는 latent dynamics → grasp/contact action, force command 또는 object motion`.
- 이 논문의 재사용 가능한 지점은 2) Diffusion Policy Training: Train a policy fon this dataset t0 infer motions from tactile feedback and proprioceptive states, ensuring generalization to real-world robotic systems,를 trajectory with compliant finger control via tactile feedback; (3) Model based force tracking": combines the PP-Tac-lerived hand trajectory with compliant finger control via tactile feedback; (4) Non-disturbance: grasp using our dextero ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 contact geometry, force state 또는 latent dynamics가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 As shown in the "Non-disturbance" baseline in Section VI-C, removing data disturbance led to a notable performance drop across all experiments, often resulting in complete failure when grasping stiff objects, such as ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: To address this, we propose a visionindependent tactile-based approach. ‘The core idea leverages tactile feedback to maintain contact conditions (as defined in Section IV), facilitating the creation of a buckling region for ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `Manipulation, contact, tactile, and dexterity`; tags: `Robotics, tactile sensing, dexterous manipulation, deformable objects, force control, slip detection`.
- **Reading predecessor in the generated track queue:** V-HOP: Visuo-Haptic 6D Object Pose Tracking (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** GeoDEx: A Unified Geometric Framework for Tactile Dexterous and Extrinsic Manipulation under Force Uncertainty (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** As shown in the "Non-disturbance" baseline in Section VI-C, removing data disturbance led to a notable performance drop across all experiments, often resulting in complete failure when grasping stiff objects, such as ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: of the proposed algorithms on a physical robotic system, Both the hardware design and code for the PP-Tac system are publicly released to support further research and. community development,.
3. Compare against the body-reported baseline or a matched simpler baseline: Fig. 9: Experiment results. Evaluations were conducted to quantify the success rate of grasping four different flat objects (paper. plastic bag, ‘loth, and paper bag) across four terrain setups (plane, slope, book ....
4. Report the body metric and its denominator/aggregation: Fig. 9: Experiment results. Evaluations were conducted to quantify the success rate of grasping four different flat objects (paper. plastic bag, ‘loth, and paper bag) across four terrain setups (plane, slope, book ....
5. Re-run the body-reported ablation/failure condition: Last, ablation studies are conducted to examine the influence of parameters, and the necessary training steps (Section VI-E)..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 6 (A. Implementation Details), p. 6 (B. PP-Tac Policy), p. 9 (B. Depth Reconstruction of VBTS); the primary result is directionally consistent at p. 9 (Figure/Table caption), p. 6 (VI. EXPERIMENTS), p. 4 (Figure/Table caption); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 address, visionindependent, tactile-based mechanism이 Fig. 9: Experiment results. Evaluations were conducted to quantify the success rate of grasping four different ... 대비 Fig. 9: Experiment results. Evaluations were conducted to quantify the success rate of grasping four different flat objects ...을 개선하고, As shown in the "Non-disturbance" baseline in Section VI-C, removing data disturbance led to a notable ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
