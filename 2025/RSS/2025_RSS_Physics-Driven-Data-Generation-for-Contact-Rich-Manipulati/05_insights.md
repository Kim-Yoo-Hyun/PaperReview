# Insights — Physics-Driven Data Generation for Contact-Rich Manipulation via Trajectory Optimization

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (14 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p053.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p053.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 4 / IV. AUTOMATED DATA GENERATION - extractive body cue:** In this section, we present our method for automatically generating large quantities of physically feasible trajectories for contact-rich manipulation tasks across a range of objects, ...
- **p. 3 / C. Trajectory Optimization for Contact-Rich Tasks - extractive body cue:** We present a Virtual Reality (VR)-based data collection pipeline designed for intuitive and efficient collection of hu- ‘man demonstrations across multiple robot embodiments. ‘The pipeline ...
- **p. 1 / Abstract - extractive body cue:** We present a low-cost data generation pipeline that integrates physics-based. simulation, human demonstrations, and model-based planning to efficiently generate large- ‘sale, high-quality datasets for contact-rich ...
- **p. 1 / body section boundary not confidently recovered - extractive body cue:** Leveraging trajectory optimization, our framework automatically generates thousands of ‘dynamically feasible contactrich trajectories across a range of embodiments and physical parameters from only 24 human ...
- **p. 2 / 1. IyTRODUCTION - extractive body cue:** 1) We present an intuitive, embodiment-flexible demonstration interface based on virtual reality and physics simulation, enabling fast data collection for dexterous contact-rich manipulation.
- **p. 3 / C. Trajectory Optimization for Contact-Rich Tasks - extractive body cue:** While these approaches search over the parameters of a neural network policy and potentially optimize 4 more global objective, we leverage trajectory optimization as a ...
- **p. 7 / B. Demonstration-Guided Trajectory Optimization - extractive body cue:** ‘The iiwa and Panda arms differ in contact geometry, velocity limits, and joint constraints, all of which are explicitly modeled within the trajectory optimization framework ...
- **Contribution anchor:** p. 4 (IV. AUTOMATED DATA GENERATION), p. 3 (C. Trajectory Optimization for Contact-Rich Tasks), p. 1 (Abstract), p. 1 (body section boundary not confidently recovered), p. 2 (1. IyTRODUCTION), p. 3 (C. Trajectory Optimization for Contact-Rich Tasks)

### Strongest assumption and failure boundary

- **p. 2 / 4) We achieve high success rates in zero-shot hardware - extractive body cue:** data collection [31, 32], reducing cognitive load, physical strain, and user frustration compared to traditional techniques like kinesthetic teaching or 3D mouse control (33). ‘These ...
- **p. 1 / 1. IyTRODUCTION - extractive body cue:** However, the significant embodiment gap and limited action labeling make this data difficult 10 transfer effectively to robot policies.
- **p. 1 / 1. IyTRODUCTION - extractive body cue:** However, collecting real-world, contact-rich manipulation data through teleoperation is, challenging due to the need for precise multi-contact interactions, which are difficult to achieve in practice ...
- **p. 2 / B. Data Augmentation - extractive body cue:** To address these challenges, significant effort has been devoted to automating the data generation process through data augmentation techniques.
- **p. 3 / C. Trajectory Optimization for Contact-Rich Tasks - extractive body cue:** To tackle these challenges, researchers have explored various trajectory optimization for- ‘ulations for multi-contact interactions.
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 11: Policy failure and recovery on hardware. The baseline policy frequently (a) gets stuck on the box surface when small deviations from the demonstration ...
- **p. 7 / B. Demonstration-Guided Trajectory Optimization - extractive body cue:** Simply transforming the end-effector pose in an object-centric manner as in MimicGen disregards the contact between the rest of the robot and the object, and ...
- **Boundary to test:** Fig. 11: Policy failure and recovery on hardware. The baseline policy frequently (a) gets stuck on the box surface when small deviations from the demonstration trajectories occur, and (b) struggles to recover ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | In this section, we present our method for automatically generating large quantities of physically feasible trajectories for contact-rich manipulation tasks across a range of objects, initial conditions, and embodiments from only a ... | p. 4 (IV. AUTOMATED DATA GENERATION), p. 3 (C. Trajectory Optimization for Contact-Rich Tasks) |
| Reported outcome | In contrast, policies trained on the expanded dataset generated by our pipeline demonstrate a higher likelihood of re-establishing contact with the object after initial misses, resulting in significantly improved success rates up ... | p. 8 (A. Policy Evaluation in Simulation), p. 8 (A. Policy Evaluation in Simulation) |
| Failure/limitation | Fig. 11: Policy failure and recovery on hardware. The baseline policy frequently (a) gets stuck on the box surface when small deviations from the demonstration trajectories occur, and (b) struggles to recover ... | p. 9 (Figure/Table caption), p. 7 (B. Demonstration-Guided Trajectory Optimization) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Paper-specific interface:** The necessary frequent contact mode switches and high-dimensional action space pose great challenges for traditional model-based planners, while the precise contact interactions require fine-grained control actions (p. 6, B. Demonstration-Guided Trajectory Optimization).
- **Paper-specific mechanism:** In this section, we present our method for automatically generating large quantities of physically feasible trajectories for contact-rich manipulation tasks across a range of objects, initial conditions, and embodiments from ... (p. 4, IV. AUTOMATED DATA GENERATION).
- **Evidence boundary:** the reported outcome is In contrast, policies trained on the expanded dataset generated by our pipeline demonstrate a higher likelihood of re-establishing contact with the object after initial misses, resulting in significantly improved success ... (p. 8, A. Policy Evaluation in Simulation); the relevant task/metric cue is We evaluate the performance by conducting 48 policy rollouts for each embodiment in simulation and record the success rates in Fig. (p. 7, A. Policy Evaluation in Simulation). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** Second, although our method demonstrates strong performance in the vicinity of the demonstration due to trajectory optimization, the learned policies struggle to recover from states far outside the demonstrated regions, ... (p. 10, B. Policy Evaluation on Hardware).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `Manipulation, contact, tactile, and dexterity`; tags: `Robotics, contact-rich manipulation, trajectory optimization, synthetic data`.
- **Reading predecessor in the generated track queue:** Towards Tight Convex Relaxations for Contact-Rich Manipulation (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Complementarity-Free Multi-Contact Modeling and Optimization for Dexterous Manipulation (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Fig. 11: Policy failure and recovery on hardware. The baseline policy frequently (a) gets stuck on the box surface when small deviations from the demonstration trajectories occur, and (b) struggles to recover ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: The necessary frequent contact mode switches and high-dimensional action space pose great challenges for traditional model-based planners, while the precise contact interactions require fine-grained control actions (p. 6, B. Demonstration-Guided Trajectory Optimization); preserve the objective/update rule: Contact-Implicit Trajectory Optimization Existing works based on contact-implicit trajectory optimization (CITO) [22, 21] have sought to formulate the combinatorial problem into 4 smooth optimization problem by using complementarity con ... (p. 3, C. Trajectory Optimization for Contact-Rich Tasks).
2. Use the paper-reported task/data/environment cue: We illustrate our framework's capability to efficiently produce diverse, high-quality contactich datasets for training behavior cloning policies across multiple robotic platforms, including the floating Allegro hand and the bimanual Pan ... (p. 7, VI. BEHAVIOR CLONING EXPERIMENTS).
3. Compare against the reported or matched baseline: The baseline behavior cloning policy trained on the original (p. 8, A. Policy Evaluation in Simulation).
4. Report the body metric with its denominator and aggregation: We evaluate the performance by conducting 48 policy rollouts for each embodiment in simulation and record the success rates in Fig. (p. 7, A. Policy Evaluation in Simulation).
5. Re-run the reported ablation or stress/failure condition: These factors together present significant challenges for traditional model-based planners without guidance. (p. 8, A. Policy Evaluation in Simulation); if none is reported, design one around: Second, although our method demonstrates strong performance in the vicinity of the demonstration due to trajectory optimization, the learned policies struggle to recover from states far outside the demonstrated regions, ... (p. 10, B. Policy Evaluation on Hardware).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 4 (IV. AUTOMATED DATA GENERATION), p. 1 (Abstract), match the reported outcome at p. 8 (A. Policy Evaluation in Simulation), p. 8 (A. Policy Evaluation in Simulation), p. 7 (A. Policy Evaluation in Simulation), and measure the boundary at p. 10 (B. Policy Evaluation on Hardware), p. 9 (B. Policy Evaluation on Hardware).

## Falsifiable research question

Under the paper's stated interface (The necessary frequent contact mode switches and high-dimensional action space pose great challenges for traditional model-based planners, while the precise contact interactions ...), does the paper-specific mechanism (In this section, we present our method for automatically generating large quantities of physically feasible trajectories for contact-rich manipulation tasks across a ...) retain the reported evaluation outcome (We evaluate the performance by conducting 48 policy rollouts for each embodiment in simulation and record the success ...) when tested against the paper's strongest explicit boundary (Second, although our method demonstrates strong performance in the vicinity of the demonstration due to trajectory optimization, the ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (We evaluate the performance by conducting 48 policy rollouts for each embodiment in simulation and record the success ...) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (14 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** In this section, we present our method for automatically generating large quantities of physically feasible trajectories for contact-rich manipulation tasks across a range of objects, initial conditions, and embodiments from ... (p. 4, IV. AUTOMATED DATA GENERATION).
- **Paper-supported outcome:** In contrast, policies trained on the expanded dataset generated by our pipeline demonstrate a higher likelihood of re-establishing contact with the object after initial misses, resulting in significantly improved success ... (p. 8, A. Policy Evaluation in Simulation).
- **Strongest explicit boundary:** Second, although our method demonstrates strong performance in the vicinity of the demonstration due to trajectory optimization, the learned policies struggle to recover from states far outside the demonstrated regions, ... (p. 10, B. Policy Evaluation on Hardware).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
