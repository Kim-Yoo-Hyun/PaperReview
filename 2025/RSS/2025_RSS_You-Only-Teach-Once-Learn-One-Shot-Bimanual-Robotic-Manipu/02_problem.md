# Problem - You Only Teach Once: Learn One-Shot Bimanual Robotic Manipulation from Video Demonstrations

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (22 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p149.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p149.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 4 (A. Problem Formulation)): Next, we present how to obtain sufficient training demonstrations proliferated from only a single-shot human teaching and how to improve existing diffusion-based imitation policies for addressing the bimanual manipulation problem.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Bimanual robotic manipulat challenge of embodied intelligence duc
- **p. 1 / Abstract - extractive body cue:** dual-arm spatialtemporal coordination and high-dimensional
- **p. 1 / Abstract - extractive body cue:** ies or direct teleoperation to alleviate or circumvent these i sues, often making them lack simplicity, versatility and scalability Differently, we believe that the most ...
- **p. 1 / Abstract - extractive body cue:** ach Once), which can extract and then inject patterns of bimanual actions from as few as a single binocular observation of hand movements, and teach ...
- **p. 1 / Abstract - extractive body cue:** Furthermore, based on keyframes= based motion trajectories, we devise as fe if training demonstrations
- **p. 4 / A. Problem Formulation - extractive body cue:** Next, we present how to obtain sufficient training demonstrations proliferated from only a single-shot human teaching and how to improve existing diffusion-based imitation policies for ...
- **p. 4 / B. Hand Motion Extraction and Injection - extractive body cue:** As an altemative, we propose to project all 3D points {f!"°}/_, onto the 2D image, nd then lft these points to 3D by applying the ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Next, we present how to obtain sufficient training demonstrations proliferated from only a single-shot human teaching and how to improve existing diffusion-based ... | demonstration으로 정의된 robot task distribution | body wording is the source claim |
| Observation / input | For all our bimanual tasks, the observation horizon is set to 1, so we only use the initial state observation of the ... | observation history와 expert trajectory/action | exact sensor/frame/preprocessing from PDF |
| State / latent | bimanual, tasks, observation, horizon, only, initial, state, left, network, inputs | behavior policy와 temporal action context | notation and tensor shape require body check |
| Output / action | mainly, consider, bimanual, robot, manipula, tion, tasks, where | predicted action 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | closed-loop task success and robustness | imitation error, task success, robustness와 compounding error | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | observation history o_{t−H:t}; body terms: bimanual, tasks, observation, horizon, only, initial, state, left, network, inputs | p. 17 (A. Implementation Details of Our BiDP), p. 4 (A. Problem Formulation), p. 4 (A. Problem Formulation) |
| Decision / output variable | expert-like action/chunk a_{t:t+H}; body terms: altemative, project, points, onto, image, then, applying, stereo | p. 4 (B. Hand Motion Extraction and Injection), p. 4 (A. Problem Formulation), p. 17 (A. Implementation Details of Our BiDP) |
| Objective / loss / cost | imitation or action-distribution loss; cue terms: learning, objective, simply, concluded, maximum, likelihood, observation-conditioned, imitation | p. 4 (A. Problem Formulation) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (A. Problem Formulation), p. 17 (A. Implementation Details of Our BiDP), p. 17 (A. Implementation Details of Our BiDP) |
| Success / guarantee | closed-loop task success and robustness | p. 9 (B. Results Comparison), p. 9 (B. Results Comparison), p. 10 (B. Results Comparison) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 4 / A. Problem Formulation - extractive body cue:** Next, we present how to obtain sufficient training demonstrations proliferated from only a single-shot human teaching and how to improve existing diffusion-based imitation policies for ...

## What the Paper Changes

PDF contribution framing (p. 4 (B. Hand Motion Extraction and Injection), p. 4 (A. Problem Formulation), p. 17 (A. Implementation Details of Our BiDP), p. 5 (B. Hand Motion Extraction and Injection), p. 17 (A. Implementation Details of Our BiDP)): As an altemative, we propose to project all 3D points {f!"°}/_, onto the 2D image, nd then lft these points to 3D by applying the stereo matching algorithm {92}.

- **p. 4 / A. Problem Formulation - extractive body cue:** Next, we present how to obtain sufficient training demonstrations proliferated from only a single-shot human teaching and how to improve existing diffusion-based imitation policies for ...
- **p. 17 / A. Implementation Details of Our BiDP - extractive body cue:** 1) Spaces of observation and action: We adopt a 13 ‘dimensional proprioception vector and a 7-dimensional action, space for each robot arm, respectively. ‘The proprioception ...
- **p. 5 / B. Hand Motion Extraction and Injection - extractive body cue:** In the following, we show that the extracted fine-grained keyframes-based motion actions A along with the corresponding motion mask C will continue to play a ...
- **p. 17 / A. Implementation Details of Our BiDP - extractive body cue:** This core design relies on the stil rapidly developing capabilities of vision foundation models (VEMs).

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 11 | In short, these limitations highlight the need for further innovations to enhance robustness, generalization, and scalability in bimanual ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 11 | tation: Although YOTO has achieved impressive performance on various long-horizon bimanual manipulation tasks, we conclude that it has ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 21 | Fig. 15: From top to bottom, we have examples of failed cases in all five tasks during evaluation, ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | Firstly, when directly applying advanced 3D hand mesh reconstruction methods (ei ther HaMeR [67] or WiLoR [71)) the ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

il writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 17 (A. Implementation Details of Our BiDP), p. 4 (A. Problem Formulation), p. 4 (A. Problem Formulation), p. 17 (A. Implementation Details of Our BiDP). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 4 (A. Problem Formulation), interface p. 17 (A. Implementation Details of Our BiDP), p. 4 (A. Problem Formulation), p. 4 (A. Problem Formulation), p. 17 (A. Implementation Details of Our BiDP), objective p. 4 (A. Problem Formulation).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
