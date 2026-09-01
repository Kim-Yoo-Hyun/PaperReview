# Problem - Instruction-Augmented Long-Horizon Planning: Embedding Grounding Mechanisms in Embodied Mobile Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (9 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://ojs.aaai.org/index.php/AAAI/article/view/33610; PDF retrieval source: https://ojs.aaai.org/index.php/AAAI/article/view/33610. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 7 (Problem Formulation), p. 5 (Problem Formulation), p. 6 (Problem Formulation), p. 7 (Problem Formulation), p. 3 (Problem Formulation)): Planning failures occur when the planner fails to generate the correct action sequence.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Enabling humanoid robots to perform long-horizon mobile manipulation planning in real-world environments based on embodied perception and comprehension abilities has been a longstanding challenge.
- **p. 1 / Abstract - extractive body cue:** With the recent rise of large language models (LLMs), there has been a notable increase in the development of LLM-based planners.
- **p. 1 / Abstract - extractive body cue:** These approaches either utilize human-provided textual representations of the real world or heavily depend on prompt engineering to extract such representations, lacking the capability to ...
- **p. 1 / Abstract - extractive body cue:** To address these limitations, we present the Instruction-Augmented Long-Horizon Planning (IALP) system, a novel framework that employs LLMs to generate feasible and optimal actions based ...
- **p. 1 / Abstract - extractive body cue:** Distinct from prior works, our approach augments user instructions into PDDL problems by leveraging both the abstract reasoning capabilities of LLMs and grounding mechanisms.
- **p. 7 / Problem Formulation - extractive body cue:** Planning failures occur when the planner fails to generate the correct action sequence.
- **p. 5 / Problem Formulation - extractive body cue:** We exclude any grasps that cannot be reached in the current state by computing a grasp reachability index for each candidate grasp.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Planning failures occur when the planner fails to generate the correct action sequence. | mobile base와 one/two-arm manipulation environment | body wording is the source claim |
| Observation / input | It captures the utility of the action sequence at:H with respect to satisfying the instruction i on current state st. | egocentric RGB-D, language/task goal, base-arm proprioception | exact sensor/frame/preprocessing from PDF |
| State / latent | captures, utility, action, sequence, respect, satisfying, instruction, current, state, later | map/object/contact state와 base-arm coordination decision | notation and tensor shape require body check |
| Output / action | Given, PDDL, problem, specific, task, domain, user, instruction | base motion plus arm/gripper action | exact unit/frame/decoder require body check |
| Target outcome | task completion and recovery | long-horizon task success, reachability, collision과 recovery | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | base-arm-object state and language/task goal; body terms: captures, utility, action, sequence, respect, satisfying, instruction, current, state, later | p. 3 (Problem Formulation), p. 3 (Problem Formulation), p. 5 (Problem Formulation) |
| Decision / output variable | base plus arm/gripper action; body terms: library, consists, four, promptable, predicates, addressed, through, prompt | p. 3 (Problem Formulation), p. 3 (Problem Formulation), p. 5 (Problem Formulation) |
| Objective / loss / cost | long-horizon task utility under reachability/contact constraints; cue terms: later, term, Equation, represents, probability, action, sequence, achieve | p. 3 (Problem Formulation), p. 3 (Problem Formulation), p. 5 (Problem Formulation), p. 5 (Problem Formulation) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (Problem Formulation), p. 5 (Problem Formulation), p. 4 (Problem Formulation) |
| Success / guarantee | task completion and recovery | p. 7 (Problem Formulation), p. 7 (Problem Formulation), p. 3 (Problem Formulation) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 5 / Problem Formulation - extractive body cue:** We exclude any grasps that cannot be reached in the current state by computing a grasp reachability index for each candidate grasp.
- **p. 6 / Problem Formulation - extractive body cue:** Given the instruction, "Pick the paper box on the wooden table and place it on the black table," and with the 2D and 3D images ...
- **p. 7 / Problem Formulation - extractive body cue:** For the system without feasibility feedback (labeled as IALP w/o Feasibility Feedback), it encounters difficulty in generating feasible actions due to the removal of feasibility ...
- **p. 3 / Problem Formulation - extractive body cue:** If even one skill fails, then the entire action sequence fails.

## What the Paper Changes

PDF contribution framing (p. 3 (Problem Formulation), p. 3 (Problem Formulation), p. 5 (Problem Formulation), p. 7 (Problem Formulation), p. 7 (Problem Formulation)): This library consists of four promptable predicates that can be addressed through prompt engineering based on the reasoning ability of state-of-the-art LLMs, such as holding and on, and six predicates ...

- **p. 3 / Problem Formulation - extractive body cue:** 2, we propose the InstructionAugmented Long-Horizon Planning (IALP) system to inPromptable on, in, holding, opened Grounding Mechanism at, find, graspable, placeable, detected, reachable Table 1: ...
- **p. 5 / Problem Formulation - extractive body cue:** We introduce six feasibility predicates, comprising two navigation predicates and four manipulation predicates, to maximize the feasibility score Sfb thereby increasing the likelihood that the ...
- **p. 7 / Problem Formulation - extractive body cue:** These results demonstrate that our method can accomplish these tasks within a reasonable time.
- **p. 7 / Problem Formulation - extractive body cue:** Conclusion We propose IALP, a framework that leverages promptable and grounding mechanism-based predicates to construct an informative PDDL problem to represent task-relevant information of the ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 7 | Planning failures occur when the planner fails to generate the correct action sequence. | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | All instances of predicate-checking failures were systematically aggregated and classified into three categories: planning, promptable, and grounding mechanisms ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 3 | If even one skill fails, then the entire action sequence fails. | reported limitation/failure wording; scope must be verified |
| body cue at p. 4 | For instance, a robot cannot move toward a blue jacket if it cannot identify a 14693 | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

mobile_manipulation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 3 (Problem Formulation), p. 3 (Problem Formulation), p. 5 (Problem Formulation), p. 6 (Problem Formulation). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 7 (Problem Formulation), p. 5 (Problem Formulation), p. 6 (Problem Formulation), p. 7 (Problem Formulation), p. 3 (Problem Formulation), interface p. 3 (Problem Formulation), p. 3 (Problem Formulation), p. 5 (Problem Formulation), p. 6 (Problem Formulation), objective p. 3 (Problem Formulation), p. 3 (Problem Formulation), p. 5 (Problem Formulation), p. 5 (Problem Formulation).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
