# Insights — GeoDEx: A Unified Geometric Framework for Tactile Dexterous and Extrinsic Manipulation under Force Uncertainty

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (12 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p057.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p057.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / Abstract - extractive body cue:** Through various experimental results, we show that while relying on direct inaccurate and noisy force readings from tactile sensors results in unstable or failed manipulation, ...
- **p. 2 / B. Utilizing Tactile Readings - extractive body cue:** Our framework consists of three major components as shown in Fig.1: a force planner that generates robust plans for
- **p. 1 / Abstract - extractive body cue:** In this paper, we introduce GeoDEx, a unified estimation, planning, and control framework using geometric primitives such a plane, cone and ellipsoid, which enables dexterous ...
- **p. 2 / B. Utilizing Tactile Readings - extractive body cue:** We will end by describing the control architecture of our framework.
- **p. 3 / B. Force Estimation - extractive body cue:** Our projection allows changes to normal force magnitude and practically gives similar results as we will show in the experimental section,
- **p. 2 / B. Utilizing Tactile Readings - extractive body cue:** In this section, we will first define the necessary concepts for our theoretical framework, and then use these concepts to address the problems of how ...
- **p. 5 / B. Force Estimation - extractive body cue:** We use MwoCo to simulate the arm, hand, and objects' kinematics, dynamics, and contact interactions.
- **Contribution anchor:** p. 1 (Abstract), p. 2 (B. Utilizing Tactile Readings), p. 1 (Abstract), p. 2 (B. Utilizing Tactile Readings), p. 3 (B. Force Estimation), p. 2 (B. Utilizing Tactile Readings)

### Strongest assumption and failure boundary

- **p. 1 / 1. Iyrropucrion - extractive body cue:** While force sensors can provide accurate force readings, physical limitations associated with ‘embedding the sensors into the robotic hands, as well as lack of high-resolution ...
- **p. 1 / Abstract - extractive body cue:** However, accuracy of the measured forces is not ‘on a par with those of the force sensors due to the potential bration challenges and noise.
- **p. 2 / B. Utilizing Tactile Readings - extractive body cue:** Most Of the existing works focus on contact force and position planning and validate the method in simulation only [23, 25, 26], [27] performed hardware ...
- **p. 3 / B. Utilizing Tactile Readings - extractive body cue:** When extrinsic contacts are present, we can also assume there is a virtual sensor attached to the contact point that can measure force in the ...
- **p. 2 / B. Utilizing Tactile Readings - extractive body cue:** In this section, we will first define the necessary concepts for our theoretical framework, and then use these concepts to address the problems of how ...
- **p. 10 / V. Discussion - extractive body cue:** For these failure cases, the main element at fault was the saturation of the tactile sensors of one or more fingertips.
- **p. 10 / V. Discussion - extractive body cue:** We can use this contact location, along with the object parameters to compute the ‘optimal force needed to grasp the object in force equilibrium, such ...
- **Boundary to test:** For these failure cases, the main element at fault was the saturation of the tactile sensors of one or more fingertips.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Through various experimental results, we show that while relying on direct inaccurate and noisy force readings from tactile sensors results in unstable or failed manipulation, our method enables successful grasping and extrinsic ... | p. 1 (Abstract), p. 2 (B. Utilizing Tactile Readings) |
| Reported outcome | According to the results, we can see an improvement | p. 7 (B. Simulation Results), p. 8 (C. Hardware Results) |
| Failure/limitation | For these failure cases, the main element at fault was the saturation of the tactile sensors of one or more fingertips. | p. 10 (V. Discussion), p. 10 (V. Discussion) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Paper-specific interface:** We use the error © between the desired forces and the ‘observations at each contact point along with the fingrtp's Jacobian J to compute direction of motion ofthe fingertips as (p. 5, B. Force Estimation).
- **Paper-specific mechanism:** Through various experimental results, we show that while relying on direct inaccurate and noisy force readings from tactile sensors results in unstable or failed manipulation, our method enables successful grasping ... (p. 1, Abstract).
- **Evidence boundary:** the reported outcome is The success rate along with the mean and standard ‘deviation ofthe force error at the contact points for the success and failure cases is presented in table Ill, We can ... (p. 8, C. Hardware Results); the relevant task/metric cue is ‘TABLE IMI: Success rate for wrench and cylinder grasp experiments with the mean and sid of the force error of the grasps when it was successful and when it failed (p. 8, C. Hardware Results). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** Through various experimental results, we show that while relying on direct inaccurate and noisy force readings from tactile sensors results in unstable or failed manipulation, our method enables successful grasping ... (p. 1, Abstract).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `Manipulation, contact, tactile, and dexterity`; tags: `Robotics, tactile sensing, force uncertainty, dexterous manipulation, extrinsic manipulation, geometric planning`.
- **Reading predecessor in the generated track queue:** PP-Tac: Paper Picking Using Omnidirectional Tactile Feedback in Dexterous Robotic Hands (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Demonstrating REASSEMBLE: A Multimodal Dataset for Contact-rich Robotic Assembly and Disassembly (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** For these failure cases, the main element at fault was the saturation of the tactile sensors of one or more fingertips.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: We use the error © between the desired forces and the ‘observations at each contact point along with the fingrtp's Jacobian J to compute direction of motion ofthe fingertips as (p. 5, B. Force Estimation); preserve the objective/update rule: Forces on FE-plane satisfy linear force equilibrium constraints: (p. 2, B. Utilizing Tactile Readings).
2. Use the paper-reported task/data/environment cue: The simulation uses the same values as the hardware for the hand joints' PD gains. (p. 6, B. Simulation Results).
3. Compare against the reported or matched baseline: We compared the controller when using the estimated force values against the raw measurements, with the results shown in Fig. (p. 6, B. Simulation Results).
4. Report the body metric with its denominator and aggregation: ‘TABLE IMI: Success rate for wrench and cylinder grasp experiments with the mean and sid of the force error of the grasps when it was successful and when it failed (p. 8, C. Hardware Results).
5. Re-run the reported ablation or stress/failure condition: 1) without over-pressuring it (following constraint in eq. (p. 7, C. Hardware Results); if none is reported, design one around: Through various experimental results, we show that while relying on direct inaccurate and noisy force readings from tactile sensors results in unstable or failed manipulation, our method enables successful grasping ... (p. 1, Abstract).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 1 (Abstract), p. 1 (Abstract), match the reported outcome at p. 8 (C. Hardware Results), p. 8 (C. Hardware Results), p. 6 (B. Simulation Results), and measure the boundary at p. 1 (Abstract), p. 9 (C. Hardware Results).

## Falsifiable research question

Under the paper's stated interface (We use the error © between the desired forces and the ‘observations at each contact point along with the fingrtp's Jacobian J ...), does the paper-specific mechanism (Through various experimental results, we show that while relying on direct inaccurate and noisy force readings from tactile sensors results in unstable ...) retain the reported evaluation outcome (‘TABLE IMI: Success rate for wrench and cylinder grasp experiments with the mean and sid of the force ...) when tested against the paper's strongest explicit boundary (Through various experimental results, we show that while relying on direct inaccurate and noisy force readings from tactile ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (‘TABLE IMI: Success rate for wrench and cylinder grasp experiments with the mean and sid of the force ...) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (12 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** Through various experimental results, we show that while relying on direct inaccurate and noisy force readings from tactile sensors results in unstable or failed manipulation, our method enables successful grasping ... (p. 1, Abstract).
- **Paper-supported outcome:** The success rate along with the mean and standard ‘deviation ofthe force error at the contact points for the success and failure cases is presented in table Ill, We can ... (p. 8, C. Hardware Results).
- **Strongest explicit boundary:** Through various experimental results, we show that while relying on direct inaccurate and noisy force readings from tactile sensors results in unstable or failed manipulation, our method enables successful grasping ... (p. 1, Abstract).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
