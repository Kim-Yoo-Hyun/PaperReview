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
- **p. 1 / Front matter - extractive body cue:** Leveraging trajectory optimization, our framework automatically generates thousands of ‘dynamically feasible contactrich trajectories across a range of embodiments and physical parameters from only 24 human ...
- **p. 2 / 1. IyTRODUCTION - extractive body cue:** 1) We present an intuitive, embodiment-flexible demonstration interface based on virtual reality and physics simulation, enabling fast data collection for dexterous contact-rich manipulation.
- **p. 3 / C. Trajectory Optimization for Contact-Rich Tasks - extractive body cue:** While these approaches search over the parameters of a neural network policy and potentially optimize 4 more global objective, we leverage trajectory optimization as a ...
- **p. 7 / B. Demonstration-Guided Trajectory Optimization - extractive body cue:** ‘The iiwa and Panda arms differ in contact geometry, velocity limits, and joint constraints, all of which are explicitly modeled within the trajectory optimization framework ...
- **Contribution anchor:** p. 4 (IV. AUTOMATED DATA GENERATION), p. 3 (C. Trajectory Optimization for Contact-Rich Tasks), p. 1 (Abstract), p. 1 (Front matter), p. 2 (1. IyTRODUCTION), p. 3 (C. Trajectory Optimization for Contact-Rich Tasks)

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

- **Closed-loop position:** `RGB-D/point cloud, object state와 contact/task observation → object geometry, affordance, contact mode 또는 end-effector state → grasp, pose, force 또는 end-effector trajectory`.
- 이 논문의 재사용 가능한 지점은 We train UNet-based diffusion policies [25] for all tasks, The action space is the robot configuration (joint angles, and additional floating base coordinates for the Allegro hand), while the observation space is ...를 [62] extend the path integral formulation to handle state-input constraints and validate the approach on quadruped stabilization on hardware.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 object geometry, affordance, contact mode 또는 end-effector state가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Fig. 11: Policy failure and recovery on hardware. The baseline policy frequently (a) gets stuck on the box surface when small deviations from the demonstration trajectories occur, and (b) struggles to recover ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: In this section, we present our method for automatically generating large quantities of physically feasible trajectories for contact-rich manipulation tasks across a range of objects, initial conditions, and embodiments from only a ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `Manipulation, contact, tactile, and dexterity`; tags: `Robotics, contact-rich manipulation, trajectory optimization, synthetic data`.
- **Reading predecessor in the generated track queue:** Towards Tight Convex Relaxations for Contact-Rich Manipulation (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Complementarity-Free Multi-Contact Modeling and Optimization for Dexterous Manipulation (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Fig. 11: Policy failure and recovery on hardware. The baseline policy frequently (a) gets stuck on the box surface when small deviations from the demonstration trajectories occur, and (b) struggles to recover ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: We illustrate our framework's capability to efficiently produce diverse, high-quality contactich datasets for training behavior cloning policies across multiple robotic platforms, including the floating Allegro hand and the bimanual Pan ....
3. Compare against the body-reported baseline or a matched simpler baseline: The baseline behavior cloning policy trained on the original.
4. Report the body metric and its denominator/aggregation: We evaluate the performance by conducting 48 policy rollouts for each embodiment in simulation and record the success rates in Fig..
5. Re-run the body-reported ablation/failure condition: These factors together present significant challenges for traditional model-based planners without guidance..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 3 (C. Trajectory Optimization for Contact-Rich Tasks), p. 7 (B. Demonstration-Guided Trajectory Optimization), p. 3 (C. Trajectory Optimization for Contact-Rich Tasks); the primary result is directionally consistent at p. 8 (A. Policy Evaluation in Simulation), p. 8 (A. Policy Evaluation in Simulation), p. 7 (A. Policy Evaluation in Simulation); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 section, present, automatically mechanism이 The baseline behavior cloning policy trained on the original 대비 We evaluate the performance by conducting 48 policy rollouts for each embodiment in simulation and record the success ...을 개선하고, Fig. 11: Policy failure and recovery on hardware. The baseline policy frequently (a) gets stuck on ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
