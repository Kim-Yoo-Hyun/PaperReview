# Problem - Do As I Can, Not As I Say: Grounding Language in Robotic Affordances

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (34 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2204.01691; PDF retrieval source: https://arxiv.org/pdf/2204.01691. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (1 Introduction), p. 2 (1 Introduction), p. 11 (5.1 Results), p. 3 (2 Preliminaries), p. 7 (5.1 Results)): With prompt engineering, a LLM may be capable of splitting the high-level instruction into sub-tasks, but it cannot do so without the context of what the robot is capable of ...

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Large language models can encode a wealth of semantic knowledge about the world.
- **p. 1 / Abstract - extractive body cue:** Such knowledge could be extremely useful to robots aiming to act upon high-level, temporally extended instructions expressed in natural language.
- **p. 1 / Abstract - extractive body cue:** However, a significant weakness of language models is that they lack real-world experience, which makes it difficult to leverage them for decision making within a ...
- **p. 1 / Abstract - extractive body cue:** For example, asking a language model to describe how to clean a spill might result in a reasonable narrative, but it may not be applicable ...
- **p. 1 / Abstract - extractive body cue:** We propose to provide real-world grounding by means of pretrained skills, which are used to constrain the model to propose natural language actions that are ...
- **p. 2 / 1 Introduction - extractive body cue:** With prompt engineering, a LLM may be capable of splitting the high-level instruction into sub-tasks, but it cannot do so without the context of what ...
- **p. 2 / 1 Introduction - extractive body cue:** This question poses a major challenge.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | With prompt engineering, a LLM may be capable of splitting the high-level instruction into sub-tasks, but it cannot do so without the ... | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | The goal of TD methods is to learn state or state-action value functions (Q-function) Qπ(s, a), which represents the discounted sum of ... | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF body |
| State / latent | goal, methods, learn, state, state-action, value, functions, Q-function, represents, discounted | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | Algorithm, SayCan, Given, high, level, instruction, state, skills | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: goal, methods, learn, state, state-action, value, functions, Q-function, represents, discounted | p. 3 (2 Preliminaries), p. 3 (2 Preliminaries), p. 5 (2 Preliminaries) |
| Decision / output variable | action, pose, option or chunk a; body terms: evaluate, number, real-world, robotic, tasks, where, need, grounding | p. 1 (Abstract), p. 2 (1 Introduction), p. 1 (Abstract) |
| Objective / loss / cost | policy/action modeling objective; cue terms: leverage, intuition, setup, express, affordances, value, functions, sparse | p. 3 (2 Preliminaries) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (2 Preliminaries), p. 2 (2 Preliminaries), p. 5 (2 Preliminaries) |
| Success / guarantee | instruction-conditioned task success | p. 9 (Figure/Table caption), p. 33 (Figure/Table caption), p. 9 (5.1 Results) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1 Introduction - extractive body cue:** This question poses a major challenge.
- **p. 11 / 5.1 Results - extractive body cue:** As presented herein, SayCan only receives environmental feedback through value functions at the current decision step, meaning if a skill fails or the environment changes, ...
- **p. 3 / 2 Preliminaries - extractive body cue:** Assuming that a skill that succeeds makes progress on i with probability p(ℓπ/i) (i.e., its probability of being the right skill), and a skill that ...
- **p. 7 / 5.1 Results - extractive body cue:** Appendix E.6 shows additional rollouts with complex decisions, embodiment grounding, and long-horizon tasks in Figures 14-17 as well as failures in Figure 16.

## What the Paper Changes

PDF body contribution framing (p. 1 (Abstract), p. 2 (1 Introduction), p. 1 (Abstract), p. 4 (2 Preliminaries), p. 6 (2 Preliminaries)): We evaluate our method on a number of real-world robotic tasks, where we show the need for real-world grounding and that this approach is capable of completing long-horizon, abstract, natural ...

- **p. 2 / 1 Introduction - extractive body cue:** Our method, SayCan, extracts and leverages the knowledge within LLMs in physically-grounded tasks.
- **p. 1 / Abstract - extractive body cue:** We propose to provide real-world grounding by means of pretrained skills, which are used to constrain the model to propose natural language actions that are ...
- **p. 4 / 2 Preliminaries - extractive body cue:** With this approach, we are able to effectively extract knowledge from the language model, but it leaves a major issue: while the decoding of the ...
- **p. 6 / 2 Preliminaries - extractive body cue:** We test our method in two environments: a real office kitchen and a mock environment mirroring the kitchen, which is also the environment in which ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 12 | Future work that extends the repertoire of skills and improves their robustness would mitigate this limitation. | reported limitation/failure wording; scope must be verified |
| body cue at p. 12 | 8 Conclusions, Limitations and Future Work We presented SayCan, a method that enables leveraging and grounding the rich ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | Appendix E.6 shows additional rollouts with complex decisions, embodiment grounding, and long-horizon tasks in Figures 14-17 as well ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Overall, 65% of the errors were LLM failures and 35% were affordance failures. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 3 (2 Preliminaries), p. 3 (2 Preliminaries), p. 5 (2 Preliminaries), p. 6 (2 Preliminaries). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1 Introduction), p. 2 (1 Introduction), p. 11 (5.1 Results), p. 3 (2 Preliminaries), p. 7 (5.1 Results), interface p. 3 (2 Preliminaries), p. 3 (2 Preliminaries), p. 5 (2 Preliminaries), p. 6 (2 Preliminaries), objective p. 3 (2 Preliminaries).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
