# Problem - AgiBot World Colosseo: A Large-scale Manipulation Platform for Scalable and Intelligent Embodied Systems

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (9 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://opendrivelab.com/AgiBot-World/; PDF retrieval source: https://arxiv.org/pdf/2503.06669. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION)): While significant progress has been made in general-purpose foundational models for natural language processing [1] and computer vision [2], robotics lags behind due to the difficulty of (high-quality) data collection.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** We explore how scalable robot data can address real-world challenges for generalized robotic manipulation.
- **p. 1 / Abstract - extractive body cue:** Introducing AgiBot World, a large-scale platform comprising over 1 million trajectories across 217 tasks in five deployment scenarios, we achieve an order-of-magnitude increase in data ...
- **p. 1 / Abstract - extractive body cue:** Accelerated by a standardized collection pipeline with human-in-the-loop verification, AgiBot World guarantees high-quality and diverse data distribution.
- **p. 1 / Abstract - extractive body cue:** It is extensible from grippers to dexterous hands and visuo-tactile sensors for fine-grained skill acquisition.
- **p. 1 / Abstract - extractive body cue:** Building on top of data, we introduce Genie Operator-1 (GO-1), a novel generalist policy that leverages latent action representations to maximize data utilization, demonstrating predictable ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** While significant progress has been made in general-purpose foundational models for natural language processing [1] and computer vision [2], robotics lags behind due to the ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Yet for the open-set real-world setting, tasks spanning from fine-grained object interaction, mobile manipulation to collaborative tasks, remains a formidable challenge [5].

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | While significant progress has been made in general-purpose foundational models for natural language processing [1] and computer vision [2], robotics lags behind ... | high-DoF humanoid whole-body dynamics와 contacts | body wording is the source claim |
| Observation / input | Following our dataset, to address the limitations of previous robot foundation models that heavily rely on indomain robot datasets, we present Genie ... | proprioception, reference pose/motion, visual or language command | exact sensor/frame/preprocessing from PDF body |
| State / latent | Following, dataset, address, limitations, previous, robot, foundation, models, heavily, rely | whole-body pose, balance/contact state와 skill/mode | notation and tensor shape require body check |
| Output / action | Yet, open-set, real-world, setting, tasks, spanning, fine-grained, object | joint/whole-body action, motion target 또는 task trajectory | exact unit/frame/decoder require body check |
| Target outcome | motion/task success and recovery | tracking, balance, skill/task success와 recovery | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | whole-body pose/contact/reference state; body terms: Following, dataset, address, limitations, previous, robot, foundation, models, heavily, rely | p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION) |
| Decision / output variable | joint/whole-body action; body terms: Following, dataset, address, limitations, previous, robot, foundation, models | p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| Objective / loss / cost | tracking/balance/task objective; cue terms: GO1, fine-tuning, conducted, learning, rate, batch, size, optimization | no optimization/equation sentence selected |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 7 (2) Implementation Details) |
| Success / guarantee | motion/task success and recovery | p. 7 (Figure/Table caption), p. 6 (1) Evaluation Tasks), p. 7 (2) Implementation Details) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / I. INTRODUCTION - extractive body cue:** Yet for the open-set real-world setting, tasks spanning from fine-grained object interaction, mobile manipulation to collaborative tasks, remains a formidable challenge [5].
- **p. 2 / I. INTRODUCTION - extractive body cue:** These findings underscore the dataset's efficacy in bridging the gap between controlled laboratory environments and real-world robotic applications.
- **p. 2 / I. INTRODUCTION - extractive body cue:** To achieve generalpurpose robotic intelligence, it is essential to develop datasets that scale in size and diversity while capturing real-world variability, supported by general-purpose humanoid ...

## What the Paper Changes

PDF body contribution framing (p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION)): Following our dataset, to address the limitations of previous robot foundation models that heavily rely on indomain robot datasets, we present Genie Operator-1 (GO1), a novel generalist policy that utilizes ...

- **p. 2 / I. INTRODUCTION - extractive body cue:** 2) We propose GO-1, a robot foundation policy using latent action representations to unlock web-scale pre-training on web data.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 3 | Notably, to expand data applicability and potential, we include imperfect data (i.e., failure recovery data with annotated error ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 3 | Hand Failure Recovery Human-inthe-loop Collection RoboNet [11] 162k n/a 10 ✗ ✗ Single ✗ ✗ ✗ scripted BridgeData ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 4 | These trajectories, referred to as failure recovery data, constitute approximately one percent of the dataset. | reported limitation/failure wording; scope must be verified |
| body cue at p. 4 | Teleoperator Training Data Collection Data Upload Data Processing Quality Check Failure Recovery Annotation Data Delivery Data Discard No: ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

humanoid writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 7 (2) Implementation Details). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), interface p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 7 (2) Implementation Details), objective no optimization/equation sentence selected.
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (9 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** Yet for the open-set real-world setting, tasks spanning from fine-grained object interaction, mobile manipulation to collaborative tasks, remains a formidable challenge [5]. (p. 1, I. INTRODUCTION).
- **Formulation-changing contribution:** Following our dataset, to address the limitations of previous robot foundation models that heavily rely on indomain robot datasets, we present Genie Operator-1 (GO1), a novel generalist policy that utilizes ... (p. 2, I. INTRODUCTION).
- **Assumption/failure evidence:** Teleoperator Training Data Collection Data Upload Data Processing Quality Check Failure Recovery Annotation Data Delivery Data Discard No: Discard Edge-side Cloud-side Task Succeed Failed No Yes Validity Varification Model Training ... (p. 4, Dataset).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
