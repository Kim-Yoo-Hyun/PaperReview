# Instruction-Augmented Long-Horizon Planning: Embedding Grounding Mechanisms in Embodied Mobile Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (9 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://ojs.aaai.org/index.php/AAAI/article/view/33610.
> PDF retrieval source: https://ojs.aaai.org/index.php/AAAI/article/view/33610. Reading tracker status/evidence was not changed.

- Year/Venue: 2025 / AAAI
- Authors: not duplicated here when not verified in the registry source
- Primary track: Planning and control
- Tier: NEXT
- Tags: Robotics, task and motion planning, PDDL, mobile manipulation, long-horizon, language grounding, real-world
- Official paper: https://ojs.aaai.org/index.php/AAAI/article/view/33610
- Full-text retrieval: https://ojs.aaai.org/index.php/AAAI/article/view/33610
- Code/Project: not identified
- Paper type: system
- Source audit: full-text PDF body checked on 2026-09-02 (9 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Planning and control의 mobile_manipulation 문제를 이해하기 위해 읽는다. 본문은 Planning failures occur when the planner fails to generate the correct action sequence.를 문제로 두고, This library consists of four promptable predicates that can be addressed through prompt engineering based on the reasoning ability of state-of-the-art LLMs, such as holding and on, and six predicates determined by ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Enabling humanoid robots to perform long-horizon mobile manipulation planning in real-world environments based on embodied perception and comprehension abilities has been a longstanding challenge.
- **p. 1 / Abstract - extractive body cue:** With the recent rise of large language models (LLMs), there has been a notable increase in the development of LLM-based planners.
- **p. 1 / Abstract - extractive body cue:** These approaches either utilize human-provided textual representations of the real world or heavily depend on prompt engineering to extract such representations, lacking the capability to ...
- **p. 1 / Abstract - extractive body cue:** To address these limitations, we present the Instruction-Augmented Long-Horizon Planning (IALP) system, a novel framework that employs LLMs to generate feasible and optimal actions based ...
- **p. 1 / Abstract - extractive body cue:** Distinct from prior works, our approach augments user instructions into PDDL problems by leveraging both the abstract reasoning capabilities of LLMs and grounding mechanisms.
- **p. 7 / Problem Formulation - extractive body cue:** Planning failures occur when the planner fails to generate the correct action sequence.
- **p. 5 / Problem Formulation - extractive body cue:** We exclude any grasps that cannot be reached in the current state by computing a grasp reachability index for each candidate grasp.

## Core Idea

- **p. 3 / Problem Formulation - extractive body cue:** This library consists of four promptable predicates that can be addressed through prompt engineering based on the reasoning ability of state-of-the-art LLMs, such as holding ...
- **p. 3 / Problem Formulation - extractive body cue:** 2, we propose the InstructionAugmented Long-Horizon Planning (IALP) system to inPromptable on, in, holding, opened Grounding Mechanism at, find, graspable, placeable, detected, reachable Table 1: ...
- **p. 5 / Problem Formulation - extractive body cue:** We introduce six feasibility predicates, comprising two navigation predicates and four manipulation predicates, to maximize the feasibility score Sfb thereby increasing the likelihood that the ...
- **p. 7 / Problem Formulation - extractive body cue:** These results demonstrate that our method can accomplish these tasks within a reasonable time.
- **p. 7 / Problem Formulation - extractive body cue:** Conclusion We propose IALP, a framework that leverages promptable and grounding mechanism-based predicates to construct an informative PDDL problem to represent task-relevant information of the ...
- **p. 5 / Problem Formulation - extractive body cue:** Given the PDDL problem P of a specific task, domain D, and user instruction i, we first query the LLM planner to generate K candidates ...
- **p. 4 / Problem Formulation - extractive body cue:** Then, the robot executes the actions generated and selected by the LLM planner based on the constructed PDDL problem.
- **p. 4 / Problem Formulation - extractive body cue:** First, the feasibility of executing the action at at state st, such as whether the object to be manipulated can be grasped.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | It captures the utility of the action sequence at:H with respect to satisfying the instruction i on current state st. | egocentric RGB-D, language/task goal, base-arm proprioception | p. 3 (Problem Formulation), p. 3 (Problem Formulation) |
| State/latent | captures, utility, action, sequence, respect, satisfying, instruction, current, state, later, term, Equation | map/object/contact state와 base-arm coordination decision | p. 3 (Problem Formulation), p. 3 (Problem Formulation), p. 5 (Problem Formulation) |
| Output/action | The later term of Equation 1 represents the probability that the action sequence at:H achieve rewards rt:H when executed from the state st, which is conditionally independent of the instruction i. | base motion plus arm/gripper action | p. 3 (Problem Formulation), p. 5 (Problem Formulation), p. 6 (Problem Formulation) |
| Objective/outcome | The later term of Equation 1 represents the probability that the action sequence at:H achieve rewards rt:H when executed from the state st, which is conditionally independent of the instruction i. | long-horizon task success, reachability, collision과 recovery | p. 3 (Problem Formulation), p. 3 (Problem Formulation), p. 4 (Problem Formulation) |

## Main Claims and Actual Contribution

- **p. 3 / Problem Formulation - extractive body cue:** This library consists of four promptable predicates that can be addressed through prompt engineering based on the reasoning ability of state-of-the-art LLMs, such as holding ...
- **p. 3 / Problem Formulation - extractive body cue:** 2, we propose the InstructionAugmented Long-Horizon Planning (IALP) system to inPromptable on, in, holding, opened Grounding Mechanism at, find, graspable, placeable, detected, reachable Table 1: ...
- **p. 5 / Problem Formulation - extractive body cue:** We introduce six feasibility predicates, comprising two navigation predicates and four manipulation predicates, to maximize the feasibility score Sfb thereby increasing the likelihood that the ...
- **p. 7 / Problem Formulation - extractive body cue:** These results demonstrate that our method can accomplish these tasks within a reasonable time.
- **p. 7 / Problem Formulation - extractive body cue:** Conclusion We propose IALP, a framework that leverages promptable and grounding mechanism-based predicates to construct an informative PDDL problem to represent task-relevant information of the ...
- **p. 7 / Problem Formulation - extractive body cue:** The results indicate that IALP achieves a success rate of over 80% in all long-term tasks.
- **p. 7 / Problem Formulation - extractive body cue:** As a result, the success rate is substantially lower than that of other configurations.
- **p. 3 / Problem Formulation - extractive body cue:** The Planning Objective The objective is to find a sequence of actions {a1, · · · , aH}, denoted as a1:H, that can achieve the ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (Problem Formulation), p. 7 (Problem Formulation) |
| Embodiment/environment | While 15 errors out of 100 may appear insignificant, they represent a considerable workload in real-world hardware experiments compared with numerical simulations due to factors such as hardware issues, noise, and physical ... | hardware/simulator version and reset protocol | p. 7 (Problem Formulation), p. 3 (Problem Formulation) |
| Dataset/benchmark | Discussion To investigate the types of failure cases in real-world experiments, we conducted 20 trials for each task within a realworld environment and recorded all occurring errors. | role, split, size and leakage | p. 7 (Problem Formulation), p. 3 (Problem Formulation), p. 7 (Problem Formulation), p. 5 (Problem Formulation) |
| Metric | As a result, the success rate is substantially lower than that of other configurations. | definition, denominator, direction and uncertainty | p. 7 (Problem Formulation), p. 7 (Problem Formulation), p. 3 (Problem Formulation) |
| Baseline/ablation | Figure 6: The success rate of IALP compared with that of IALP without feasibility feedback and without optimal se- lection, respectively. list the actions and PDDL problems generated for the other four ... | fair input/data/compute/action matching | p. 7 (Figure/Table caption), p. 3 (Problem Formulation), p. 7 (Problem Formulation) |

## Explicit Limitations and Failure Boundary

- **p. 7 / Problem Formulation - extractive body cue:** Planning failures occur when the planner fails to generate the correct action sequence.
- **p. 7 / Problem Formulation - extractive body cue:** All instances of predicate-checking failures were systematically aggregated and classified into three categories: planning, promptable, and grounding mechanisms failures.
- **p. 3 / Problem Formulation - extractive body cue:** If even one skill fails, then the entire action sequence fails.
- **p. 4 / Problem Formulation - extractive body cue:** For instance, a robot cannot move toward a blue jacket if it cannot identify a 14693
- **p. 4 / Problem Formulation - extractive body cue:** The entire action sequence a1:H fails, denoted by Sfb = 0, if at least one action fails, i.e., rt = 0, ∃t ∈{1 : H}.
- **p. 5 / Problem Formulation - extractive body cue:** We exclude any grasps that cannot be reached in the current state by computing a grasp reachability index for each candidate grasp.
- **p. 5 / Problem Formulation - extractive body cue:** When there's a feasible path, navigation errors can still cause the action to fail.

## Why Read It

Planning and control의 mobile_manipulation 문제를 이해하기 위해 읽는다. 본문은 Planning failures occur when the planner fails to generate the correct action sequence.를 문제로 두고, This library consists of four promptable predicates that can be addressed through prompt engineering based on the reasoning ability of state-of-the-art LLMs, such as holding and on, and six predicates determined by ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 7 (Problem Formulation), p. 5 (Problem Formulation), p. 6 (Problem Formulation), p. 7 (Problem Formulation), p. 3 (Problem Formulation), p. 5 (Problem Formulation) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
