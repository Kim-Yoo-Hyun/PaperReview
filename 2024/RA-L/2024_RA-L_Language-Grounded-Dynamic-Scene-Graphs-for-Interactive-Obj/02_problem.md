# Problem - Language-Grounded Dynamic Scene Graphs for Interactive Object Search with Mobile Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2403.08605; PDF retrieval source: https://arxiv.org/pdf/2403.08605. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION)): To address these challenges, we propose grounding LLMs in dynamically built scene graphs.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** To fully leverage the capabilities of mobile manipulation robots, it is imperative that they are able to autonomously execute long-horizon tasks in large unexplored environments.
- **p. 1 / Abstract - extractive body cue:** While large language models (LLMs) have shown emergent reasoning skills on arbitrary tasks, existing work primarily concentrates on explored environments, typically focusing on either navigation ...
- **p. 1 / Abstract - extractive body cue:** In this work, we propose MoMa-LLM, a novel approach that grounds language models within structured representations derived from openvocabulary scene graphs, dynamically updated as the ...
- **p. 1 / Abstract - extractive body cue:** We tightly interleave these representations with an object-centric action space.
- **p. 1 / Abstract - extractive body cue:** Given object detections, the resulting approach is zero-shot, open-vocabulary, and readily extendable to a spectrum of mobile manipulation and household robotic tasks.
- **p. 1 / I. INTRODUCTION - extractive body cue:** To address these challenges, we propose grounding LLMs in dynamically built scene graphs.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Furthermore, the presence of interactive scenes and articulated objects introduces a multitude of potential states and failure cases.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | To address these challenges, we propose grounding LLMs in dynamically built scene graphs. | mobile base와 one/two-arm manipulation environment | body wording is the source claim |
| Observation / input | We rely on a simple success state to the action history, stating "success", "failure", or "invalid argument" in case the output of ... | egocentric RGB-D, language/task goal, base-arm proprioception | exact sensor/frame/preprocessing from PDF body |
| State / latent | rely, simple, success, state, action, history, stating, failure, invalid, argument | map/object/contact state와 base-arm coordination decision | notation and tensor shape require body check |
| Output / action | Scene, Graph, MoMa-LLM-policy, operates, attributed, holds, different, abstraction | base motion plus arm/gripper action | exact unit/frame/decoder require body check |
| Target outcome | task completion and recovery | long-horizon task success, reachability, collision과 recovery | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | base-arm-object state and language/task goal; body terms: rely, simple, success, state, action, history, stating, failure, invalid, argument | p. 5 (IV. MOMA-LLM), p. 5 (IV. MOMA-LLM), p. 3 (IV. MOMA-LLM) |
| Decision / output variable | base plus arm/gripper action; body terms: address, challenges, grounding, LLMs, dynamically, built, scene, graphs | p. 1 (I. INTRODUCTION), p. 1 (2 Toyota Motor Europe (TME)), p. 3 (IV. MOMA-LLM) |
| Objective / loss / cost | long-horizon task utility under reachability/contact constraints; cue terms: Objects, then, assigned, room, label, node, minimizes, object | p. 1 (Abstract), p. 3 (IV. MOMA-LLM), p. 4 (IV. MOMA-LLM), p. 4 (IV. MOMA-LLM), p. 5 (IV. MOMA-LLM), p. 5 (IV. MOMA-LLM) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (IV. MOMA-LLM), p. 5 (IV. MOMA-LLM), p. 5 (IV. MOMA-LLM) |
| Success / guarantee | task completion and recovery | p. 7 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / I. INTRODUCTION - extractive body cue:** Furthermore, the presence of interactive scenes and articulated objects introduces a multitude of potential states and failure cases.

## What the Paper Changes

PDF body contribution framing (p. 1 (I. INTRODUCTION), p. 1 (2 Toyota Motor Europe (TME)), p. 3 (IV. MOMA-LLM), p. 4 (IV. MOMA-LLM), p. 4 (IV. MOMA-LLM)): To address these challenges, we propose grounding LLMs in dynamically built scene graphs.

- **p. 1 / 2 Toyota Motor Europe (TME) - extractive body cue:** Furthermore, we introduce a novel evaluation paradigm for object search tasks, employing full efficiency curves to remove the dependency on arbitrary time budgets inherent in ...
- **p. 3 / IV. MOMA-LLM - extractive body cue:** To address the challenges of interactive open-vocabulary household tasks, we propose MoMa-LLM, which intertwines high-level reasoning with scalable dynamic scene representations.
- **p. 4 / IV. MOMA-LLM - extractive body cue:** It consists of the path on the Voronoi graph GV, and the Euclidean distances d from the Voronoi nodes no and nvp to the object ...
- **p. 4 / IV. MOMA-LLM - extractive body cue:** It consists of the following high-level actions: navigate(room_name, object_name): Navigation to an object in a room via an A∗planner in the explored BEV-map Bt, inflated ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 7 | Furthermore, the agent was able to react to the (unseen) subpolicy failures, such as re-trying to open a ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | The two failures stemmed from irrecoverable failures of the subpolicies, in particular, collisions of the base during navigation ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | Object interactions, distance travelled and infeasible actions averaged over all episodes, including early terminated failures. | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | This metric does not take into account the costs of object interactions. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

mobile_manipulation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 5 (IV. MOMA-LLM), p. 5 (IV. MOMA-LLM), p. 3 (IV. MOMA-LLM), p. 4 (IV. MOMA-LLM). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), interface p. 5 (IV. MOMA-LLM), p. 5 (IV. MOMA-LLM), p. 3 (IV. MOMA-LLM), p. 4 (IV. MOMA-LLM), objective p. 1 (Abstract), p. 3 (IV. MOMA-LLM), p. 4 (IV. MOMA-LLM), p. 4 (IV. MOMA-LLM), p. 5 (IV. MOMA-LLM), p. 5 (IV. MOMA-LLM).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (17 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** To address these challenges, we propose grounding LLMs in dynamically built scene graphs. (p. 1, I. INTRODUCTION).
- **Formulation-changing contribution:** To address these challenges, we propose grounding LLMs in dynamically built scene graphs. (p. 1, I. INTRODUCTION).
- **Assumption/failure evidence:** Furthermore, the agent was able to react to the (unseen) subpolicy failures, such as re-trying to open a drawer when the gripper slipped off the handle. (p. 7, V. EXPERIMENTS).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
