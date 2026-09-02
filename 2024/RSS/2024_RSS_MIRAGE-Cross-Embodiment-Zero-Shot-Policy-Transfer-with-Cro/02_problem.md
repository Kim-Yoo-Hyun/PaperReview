# Problem - MIRAGE: Cross-Embodiment Zero-Shot Policy Transfer with Cross-Painting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (16 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss20/p069.html; PDF retrieval source: https://www.roboticsproceedings.org/rss20/p069.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (I. INTRODUCTION), p. 4 (4) We assume that the background and lighting conditions), p. 3 (III. PROBLEM STATEMENT), p. 3 (III. PROBLEM STATEMENT)): This poses several challenges, as outlined in prior work [108], stemming from variations in kinematic configuration, control scheme, camera viewpoint, and end-effector morphology.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** The ability to reuse collected data and transfer trained policies between robots could alleviate the burden of additional data collection and training.
- **p. 1 / Abstract - extractive body cue:** While existing approaches such as pretraining plus finetuning and co-training show promise, they do not generalize to robots unseen in training.
- **p. 1 / Abstract - extractive body cue:** Focusing on common robot arms with similar workspaces and 2-jaw grippers, we investigate the feasibility of zero-shot transfer.
- **p. 1 / Abstract - extractive body cue:** Through simulation studies on 8 manipulation tasks, we find that state-based Cartesian control policies can successfully zero-shot transfer to a target robot after accounting for ...
- **p. 1 / Abstract - extractive body cue:** To address robot visual disparities for vision-based policies, we introduce Mirage, which uses "cross-painting"-masking out the unseen target robot and inpainting the seen source robot-during ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** This poses several challenges, as outlined in prior work [108], stemming from variations in kinematic configuration, control scheme, camera viewpoint, and end-effector morphology.
- **p. 4 / 4) We assume that the background and lighting conditions - extractive body cue:** This allows us to separate any challenges that arise due to changes in the background environment and focus on the impact of visual differences between ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | This poses several challenges, as outlined in prior work [108], stemming from variations in kinematic configuration, control scheme, camera viewpoint, and end-effector ... | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | Given a source policy action aS t+1 = πS(sS t , oS t ), we would like to transform it into a ... | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF body |
| State / latent | Given, source, policy, action, would, like, transform, target, takes, inputs | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | Prior, found, aligning, action, observation, spaces, facilitate, policy | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: Given, source, policy, action, would, like, transform, target, takes, inputs | p. 4 (4) We assume that the background and lighting conditions), p. 4 (4) We assume that the background and lighting conditions), p. 3 (III. PROBLEM STATEMENT) |
| Decision / output variable | action, pose, option or chunk a; body terms: summarize, contributions, address, robot, visual, disparities, vision-based, policies | p. 2 (I. INTRODUCTION), p. 1 (Abstract), p. 2 (I. INTRODUCTION) |
| Objective / loss / cost | policy/action modeling objective; cue terms: Focusing, common, robot, arms, similar, workspaces, grippers, investigate | no optimization/equation sentence selected |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 1 (Abstract) |
| Success / guarantee | instruction-conditioned task success | p. 4 (IV. STATE-BASED TRANSFER EXPERIMENTS), p. 5 (IV. STATE-BASED TRANSFER EXPERIMENTS), p. 5 (IV. STATE-BASED TRANSFER EXPERIMENTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 4 / 4) We assume that the background and lighting conditions - extractive body cue:** This allows us to separate any challenges that arise due to changes in the background environment and focus on the impact of visual differences between ...
- **p. 3 / III. PROBLEM STATEMENT - extractive body cue:** Mirage leverages the following assumptions and design choices to reduce the gap between robots and enable zero-shot transfer:
- **p. 3 / III. PROBLEM STATEMENT - extractive body cue:** Prior work [108] has found aligning the action and observation spaces can facilitate policy transfer.

## What the Paper Changes

PDF body contribution framing (p. 2 (I. INTRODUCTION), p. 1 (Abstract), p. 2 (I. INTRODUCTION), p. 3 (1) We assume knowledge of the two robots' coordinate), p. 3 (1) We assume knowledge of the two robots' coordinate)): To summarize, our key contributions are:

- **p. 1 / Abstract - extractive body cue:** To address robot visual disparities for vision-based policies, we introduce Mirage, which uses "cross-painting"-masking out the unseen target robot and inpainting the seen source robot-during ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Through extensive experiments on 9 manipulation tasks in both simulation and real across 6 different robot and gripper setups, we show that Mirage, despite its ...
- **p. 3 / 1) We assume knowledge of the two robots' coordinate - extractive body cue:** This allows us to render robots in a camera pose that is within the distribution of the training image poses.
- **p. 3 / 1) We assume knowledge of the two robots' coordinate - extractive body cue:** This allows us to transfer between robots with different numbers of joints and compensate for alternate gripper shapes across embodiments.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 5 | Less robust source policies leave little room for error, while more robust ones tend to retry even if ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | On the other hand, the failure modes we observe on the different robots or grippers are all very ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 10 | Fig. 6: (a) An example of camera calibration error resulting in failure to mask all of the target ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | We see that there is a significant drop in performance, indicating that the difference in the forward dynamics ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 4 (4) We assume that the background and lighting conditions), p. 4 (4) We assume that the background and lighting conditions), p. 3 (III. PROBLEM STATEMENT), p. 7 (2) Can Mirage successfully zero-shot transfer trained vision). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (I. INTRODUCTION), p. 4 (4) We assume that the background and lighting conditions), p. 3 (III. PROBLEM STATEMENT), p. 3 (III. PROBLEM STATEMENT), interface p. 4 (4) We assume that the background and lighting conditions), p. 4 (4) We assume that the background and lighting conditions), p. 3 (III. PROBLEM STATEMENT), p. 7 (2) Can Mirage successfully zero-shot transfer trained vision), objective no optimization/equation sentence selected.
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
