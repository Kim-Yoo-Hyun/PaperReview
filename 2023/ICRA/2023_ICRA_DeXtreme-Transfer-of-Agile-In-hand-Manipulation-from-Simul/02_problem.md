# Problem - DeXtreme: Transfer of Agile In-hand Manipulation from Simulation to Reality

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (28 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://research.nvidia.com/publication/2023-06_dextreme-transfer-agile-hand-manipulation-simulation-reality; PDF retrieval source: https://research.nvidia.com/publication/2023-06_dextreme-transfer-agile-hand-manipulation-simulation-reality. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 3 (1 Introduction), p. 3 (1 Introduction)): However, due to the complexity of their training architecture, and the sui generis nature of their work on sim-to-real transfer, reproducing and building upon their success has proven to be ...

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Recent work has demonstrated the ability of deep reinforcement learning (RL) algorithms to learn complex robotic behaviours in simulation, including in the domain of multi-fingered ...
- **p. 1 / Abstract - extractive body cue:** However, such models can be challenging to transfer to the real world due to the gap between simulation and reality.
- **p. 1 / Abstract - extractive body cue:** In this paper, we present our techniques to train a) a policy that can perform robust dexterous manipulation on an anthropomorphic robot hand and b) ...
- **p. 1 / Abstract - extractive body cue:** Our policies are trained to adapt to a wide range of conditions in simulation.
- **p. 1 / Abstract - extractive body cue:** Consequently, our vision-based policies significantly outperform the best vision policies in the literature on the same reorientation task and are competitive with policies that are ...
- **p. 3 / 1 Introduction - extractive body cue:** However, due to the complexity of their training architecture, and the sui generis nature of their work on sim-to-real transfer, reproducing and building upon their ...
- **p. 3 / 1 Introduction - extractive body cue:** While the NLP and computer vision communities have reproduced and extended the successes of large-scale models like GPT-3 [3] and DALL-E [4, 5] respectively, similar ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, due to the complexity of their training architecture, and the sui generis nature of their work on sim-to-real transfer, reproducing and ... | rigid/articulated object와 robot manipulator contact scene | body wording is the source claim |
| Observation / input | Input Dimensionality Actor Critic Object position with noise 3D ✓ ✓ Object orientation with noise 4D (quaternion) ✓ ✓ Target position 3D ... | RGB-D/point cloud, object state와 contact/task observation | exact sensor/frame/preprocessing from PDF body |
| State / latent | Input, Dimensionality, Actor, Critic, Object, position, noise, orientation, quaternion, Target | object geometry, affordance, contact mode 또는 end-effector state | notation and tensor shape require body check |
| Output / action | best, policy, Long, Short-Term, Memory, LSTM, network, taking | grasp, pose, force 또는 end-effector trajectory | exact unit/frame/decoder require body check |
| Target outcome | completion, contact success and robustness | task completion, contact success, pose/force error와 generalization | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | object geometry/contact state; body terms: Input, Dimensionality, Actor, Critic, Object, position, noise, orientation, quaternion, Target | p. 6 (2 Method), p. 4 (2 Method), p. 6 (2 Method) |
| Decision / output variable | grasp/pose/force/trajectory; body terms: Task, performing, object, reorientation, anthropomorphic, hand, Hardware, setup | p. 3 (2 Method), p. 4 (2 Method), p. 7 (2 Method) |
| Objective / loss / cost | task/contact/pose objective; cue terms: Policy, Learning, Formulation, task, manipulating, cube, desired, orientation | p. 8 (2 Method), p. 6 (2 Method), p. 9 (2 Method), p. 10 (2 Method), p. 16 (Method) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 6 (2 Method), p. 4 (2 Method), p. 7 (2 Method) |
| Success / guarantee | completion, contact success and robustness | p. 15 (3 Results), p. 13 (Figure/Table caption), p. 15 (3 Results) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 3 / 1 Introduction - extractive body cue:** While the NLP and computer vision communities have reproduced and extended the successes of large-scale models like GPT-3 [3] and DALL-E [4, 5] respectively, similar ...

## What the Paper Changes

PDF body contribution framing (p. 3 (2 Method), p. 4 (2 Method), p. 7 (2 Method), p. 2 (1 Introduction), p. 3 (1 Introduction)): 2.1 Task We propose a method for performing object reorientation on an anthropomorphic hand.

- **p. 4 / 2 Method - extractive body cue:** 2.2 Hardware Our hardware setup (see Fig 2) consists of an Allegro Hand rigidly mounted at the wrist.
- **p. 7 / 2 Method - extractive body cue:** To help overcome this, we introduce various kinds of randomisations [15] into the simulated environment as listed in Table 3.
- **p. 2 / 1 Introduction - extractive body cue:** Multi-fingered robotic hands offer an exciting platform to develop and enable human-level dexterity.
- **p. 3 / 1 Introduction - extractive body cue:** We seek to provide a much broader segment of the research community with access to a novel state-of-the-art in-hand manipulation system in hopes of catalyzing ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | Figure 4: Parameter range adjustments, pi_lo and pi_hi, with ADR based on the performance of policy at the ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 18 | However, these often fail to reproduce the agile dexterity present in human hands, as the limitations of such ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 17 | These approaches work well while an object maintains no-slip 10While extrinsics change with different camera configurations, the intrinsics ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 18 | 5 Limitations Despite our best efforts, the gap between simulations and the real world is still noticeable. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

manipulation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 6 (2 Method), p. 4 (2 Method), p. 6 (2 Method), p. 10 (2 Method). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 3 (1 Introduction), p. 3 (1 Introduction), interface p. 6 (2 Method), p. 4 (2 Method), p. 6 (2 Method), p. 10 (2 Method), objective p. 8 (2 Method), p. 6 (2 Method), p. 9 (2 Method), p. 10 (2 Method), p. 16 (Method).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (28 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** However, due to the complexity of their training architecture, and the sui generis nature of their work on sim-to-real transfer, reproducing and building upon their success has proven to be ... (p. 3, 1 Introduction).
- **Formulation-changing contribution:** 2.1 Task We propose a method for performing object reorientation on an anthropomorphic hand. (p. 3, 2 Method).
- **Assumption/failure evidence:** However, we did not observe this as a significant limitation for our experiments, and our policies nevertheless achieved rollouts with high consecutive successes in the real world. (p. 10, 2 Method).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
