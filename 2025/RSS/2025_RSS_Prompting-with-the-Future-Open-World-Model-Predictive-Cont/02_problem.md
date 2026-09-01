# Problem - Prompting with the Future: Open-World Model Predictive Control with Interactive Digital Twins

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (11 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p145.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p145.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 3 (III. PROBLEM FORMULATION)): We do not assume access to task-specific training data, in-context ‘examples, or hard-coded motion primitives as used in prior work (20, 27, 13, 25].

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Open-world robotic manipulation requires robots to perform novel tasks described by free-form language in unsteuctured settings.
- **p. 1 / Abstract - extractive body cue:** While vision-language models (VLMs) offer strong, high-level semantic reasoning, they lack the fine-grained physical insight needed for precise low-level control.
- **p. 1 / Abstract - extractive body cue:** To address this gap, we introduce Prompting with the Future (PWTE), a model predictive control framework that augments VLM-based policies With explicit physics modeling.
- **p. 1 / Abstract - extractive body cue:** PWTF builds an interactive digital {win of the workspace from a quick handheld video scan, enabling prediction of future states under candidate action sequences.
- **p. 1 / Abstract - extractive body cue:** [n= stead of asking the VLM to predict actions or results by reasoning ‘dynamics, the framework simulates diverse possible outcomes, renders them as visual prompts ...
- **p. 3 / III. PROBLEM FORMULATION - extractive body cue:** We do not assume access to task-specific training data, in-context ‘examples, or hard-coded motion primitives as used in prior work (20, 27, 13, 25].
- **p. 5 / C. Motion Planning via Simulation-Informed Prompting - extractive body cue:** To validate the effectiveness of our framework, in this section, we design eight real-world manipulation tasks that require 6 DoF control, semantic understanding, and diverse ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | We do not assume access to task-specific training data, in-context ‘examples, or hard-coded motion primitives as used in prior work (20, 27, ... | uncertain robot state와 safe/unsafe operating region | body wording is the source claim |
| Observation / input | We consider a tabletop setting with ‘one robotic arm. ‘The framework's input consists of a natural language instruction { specifying the task, ... | observation, uncertainty/risk estimate와 task command | exact sensor/frame/preprocessing from PDF |
| State / latent | consider, tabletop, setting, robotic, framework, input, consists, natural, language, instruction | safe set, recovery state 또는 constraint margin | notation and tensor shape require body check |
| Output / action | step, interactive, digital, twin, simulates, future, states, candidate | shielded, recovery 또는 safe action | exact unit/frame/decoder require body check |
| Target outcome | low violation/failure probability with useful intervention | task return과 violation/failure probability | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | state/history and risk h(s); body terms: consider, tabletop, setting, robotic, framework, input, consists, natural, language, instruction | p. 3 (III. PROBLEM FORMULATION), p. 4 (A. Construction of Interactive Digital Twins), p. 4 (A. Construction of Interactive Digital Twins) |
| Decision / output variable | filtered/recovery action u_safe; body terms: validate, effectiveness, framework, section, design, eight, real-world, manipulation | p. 5 (C. Motion Planning via Simulation-Informed Prompting), p. 3 (III. PROBLEM FORMULATION), p. 3 (A. Construction of Interactive Digital Twins) |
| Objective / loss / cost | task utility subject to safety constraint; cue terms: decomposition, localizes, optimization, objective, improving, sample, efficiency, enhancing | p. 4 (C. Motion Planning via Simulation-Informed Prompting), p. 5 (C. Motion Planning via Simulation-Informed Prompting), p. 5 (C. Motion Planning via Simulation-Informed Prompting) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (III. PROBLEM FORMULATION), p. 5 (C. Motion Planning via Simulation-Informed Prompting), p. 4 (C. Motion Planning via Simulation-Informed Prompting) |
| Success / guarantee | low violation/failure probability with useful intervention | p. 5 (A. Experimental setup), p. 5 (B. Quantitative results), p. 8 (B. Quantitative results) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 3 / III. PROBLEM FORMULATION - extractive body cue:** We do not assume access to task-specific training data, in-context ‘examples, or hard-coded motion primitives as used in prior work (20, 27, 13, 25].

## What the Paper Changes

PDF contribution framing (p. 5 (C. Motion Planning via Simulation-Informed Prompting), p. 3 (III. PROBLEM FORMULATION), p. 3 (A. Construction of Interactive Digital Twins), p. 4 (A. Construction of Interactive Digital Twins), p. 4 (A. Construction of Interactive Digital Twins)): To validate the effectiveness of our framework, in this section, we design eight real-world manipulation tasks that require 6 DoF control, semantic understanding, and diverse ‘manipulation skills, We compare our ...

- **p. 3 / III. PROBLEM FORMULATION - extractive body cue:** Central o our framework is a pre-trained vision-language model (VLM). ‘The model processes an ordered sequence of interleaved text and RGB images and returns a ...
- **p. 3 / A. Construction of Interactive Digital Twins - extractive body cue:** Unlike prior work, which often focuses solely on static reconstruction [40, 24), our method produces dynamic, actionconditioned digital twins by combining mesh-based physical modeling with ...
- **p. 4 / A. Construction of Interactive Digital Twins - extractive body cue:** Given a free-form instrition, our framework first performs high-level planning by generating structured subtasks from multi-view observations.
- **p. 4 / A. Construction of Interactive Digital Twins - extractive body cue:** ‘Through this construction pipeline, we obtain an interactive digital twin where the mesh representation provides physical structure, the Gaussian splatting enables efficient and realistic rendering, ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 5 | A task is considered a failure if the robot causes imeversible results or if the maximum step budget ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | Since Voxposer and MOKA rely on ‘open-vocabulary detectors to detect objects before manipula tion, they fail when the ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | The failure cases can be categorized into four groups: | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Our main failure cases can be divided into four categories. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

safety writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 3 (III. PROBLEM FORMULATION), p. 4 (A. Construction of Interactive Digital Twins), p. 4 (A. Construction of Interactive Digital Twins), p. 5 (C. Motion Planning via Simulation-Informed Prompting). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 3 (III. PROBLEM FORMULATION), interface p. 3 (III. PROBLEM FORMULATION), p. 4 (A. Construction of Interactive Digital Twins), p. 4 (A. Construction of Interactive Digital Twins), p. 5 (C. Motion Planning via Simulation-Informed Prompting), objective p. 4 (C. Motion Planning via Simulation-Informed Prompting), p. 5 (C. Motion Planning via Simulation-Informed Prompting), p. 5 (C. Motion Planning via Simulation-Informed Prompting).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
