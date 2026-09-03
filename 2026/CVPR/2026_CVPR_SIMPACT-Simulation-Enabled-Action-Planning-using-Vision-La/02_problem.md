# Problem - SIMPACT: Simulation-Enabled Action Planning using Vision-Language Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Liu_SIMPACT_Simulation-Enabled_Action_Planning_using_Vision-Language_Models_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_SIMPACT_Simulation-Enabled_Action_Planning_using_Vision-Language_Models_CVPR_2026_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction)): However, despite their remarkable commonsense and semantic reasoning capabilities, VLMs lack a grounded understanding of physical dynamics.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Vision-Language Models (VLMs) exhibit remarkable common-sense and semantic reasoning capabilities.
- **p. 1 / Abstract - extractive body cue:** However, they lack a grounded understanding of physical dynamics.
- **p. 1 / Abstract - extractive body cue:** This limitation arises from training VLMs on static internet-scale visual-language data that contain no causal interactions or action-conditioned changes.
- **p. 1 / Abstract - extractive body cue:** Consequently, it remains challenging to leverage VLMs for fine-grained robotic manipulation tasks that require physical understanding, reasoning, and corresponding action planning.
- **p. 1 / Abstract - extractive body cue:** To overcome this, we present SIMPACT, a test-time, SIMulation-enabled ACTion Planning framework that equips VLMs with physical reasoning through simulation-in-the-loop world modeling, without requiring any ...
- **p. 2 / 1. Introduction - extractive body cue:** Lacking physical understanding, VLMs often propose plans that appear reasonable in language but fail during execution.
- **p. 2 / 1. Introduction - extractive body cue:** To address this limitation, we propose a framework that augments VLMs with physical simulation rollouts as contextual feedback, enabling test-time physical reasoning for action planning.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, despite their remarkable commonsense and semantic reasoning capabilities, VLMs lack a grounded understanding of physical dynamics. | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | Our framework enables zero-shot robotic manipulation action generation from a single RGB-D image input I0 and natural language instruction `task and outputs ... | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF body |
| State / latent | framework, enables, zero-shot, robotic, manipulation, action, generation, single, RGB-D, image | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | planner, takes, input, initial, RGB-D, observation, simulator, state | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: framework, enables, zero-shot, robotic, manipulation, action, generation, single, RGB-D, image | p. 3 (3. Method), p. 5 (3.2. Action Planning via Simulation-enabled VLM), p. 4 (3.2. Action Planning via Simulation-enabled VLM) |
| Decision / output variable | action, pose, option or chunk a; body terms: summary, makes, following, contributions, introduce, test-time, zero-shot, framework | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Method) |
| Objective / loss / cost | policy/action modeling objective; cue terms: VLM, determines, action, sequence, achieves, task, objective, executed | p. 5 (3.2. Action Planning via Simulation-enabled VLM), p. 5 (3.2. Action Planning via Simulation-enabled VLM) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (3. Method), p. 4 (3.2. Action Planning via Simulation-enabled VLM), p. 4 (3.2. Action Planning via Simulation-enabled VLM) |
| Success / guarantee | instruction-conditioned task success | p. 8 (4.3. Ablation study), p. 6 (4.1. Experimental Setup), p. 6 (4.1. Experimental Setup) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Introduction - extractive body cue:** Lacking physical understanding, VLMs often propose plans that appear reasonable in language but fail during execution.
- **p. 2 / 1. Introduction - extractive body cue:** To address this limitation, we propose a framework that augments VLMs with physical simulation rollouts as contextual feedback, enabling test-time physical reasoning for action planning.

## What the Paper Changes

PDF body contribution framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Method), p. 4 (3.1. Simulation Construction), p. 3 (3.1. Simulation Construction)): In summary, this paper makes the following contributions: • We introduce a test-time, zero-shot framework enabling VLMs to plan physics-aware embodied actions; • We present a pipeline for automatically generating ...

- **p. 2 / 1. Introduction - extractive body cue:** By augmenting VLMs with physical simulation, our framework enables them to anticipate action consequences, evaluate predicted outcomes, and iteratively adjust their decisions at test time, ...
- **p. 3 / 3. Method - extractive body cue:** Our framework enables zero-shot robotic manipulation action generation from a single RGB-D image input I0 and natural language instruction `task and outputs robot action sequence ...
- **p. 4 / 3.1. Simulation Construction - extractive body cue:** Our method first instantiates a physics simulator given the real-world scene.
- **p. 3 / 3.1. Simulation Construction - extractive body cue:** Our approach employs a physics-based simulator to predict the consequences of actions for manipulation planning.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | Planning failures occur when the robot fails to generate a feasible action sequence even after multiple rounds of ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Failures are categorized as perception, planning, or execution. successful action sequence is particularly challenging. | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | We show representative failures from baseline methods that lack simulationenabled reasoning. | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | However, they struggle with tasks that require precise action planning, where small errors, such as pushing the wrong ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 3 (3. Method), p. 5 (3.2. Action Planning via Simulation-enabled VLM), p. 4 (3.2. Action Planning via Simulation-enabled VLM), p. 3 (3.1. Simulation Construction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), interface p. 3 (3. Method), p. 5 (3.2. Action Planning via Simulation-enabled VLM), p. 4 (3.2. Action Planning via Simulation-enabled VLM), p. 3 (3.1. Simulation Construction), objective p. 5 (3.2. Action Planning via Simulation-enabled VLM), p. 5 (3.2. Action Planning via Simulation-enabled VLM).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (12 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** However, despite their remarkable commonsense and semantic reasoning capabilities, VLMs lack a grounded understanding of physical dynamics. (p. 1, 1. Introduction).
- **Formulation-changing contribution:** In summary, this paper makes the following contributions: • We introduce a test-time, zero-shot framework enabling VLMs to plan physics-aware embodied actions; • We present a pipeline for automatically generating ... (p. 2, 1. Introduction).
- **Assumption/failure evidence:** However, they struggle with tasks that require precise action planning, where small errors, such as pushing the wrong part of an object (in non-toppling push) or squeezing an incorrect region ... (p. 7, 4.2. Results).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
