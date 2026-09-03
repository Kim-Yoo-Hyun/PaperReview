# Problem - Inner Monologue: Embodied Reasoning through Planning with Language Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (25 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v205/huang23c.html; PDF retrieval source: https://arxiv.org/pdf/2207.05608. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (1 Introduction), p. 2 (1 Introduction), p. 1 (1 Introduction)): While conventionally these challenges have been approached from the perspective of planning (e.g., TAMP [1]) or hierarchical learning (e.g., HRL [2]), effective high-level reasoning about complex tasks also requires semantic ...

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Recent works have shown how the reasoning capabilities of Large Language Models (LLMs) can be applied to domains beyond natural language processing, such as planning ...
- **p. 1 / Abstract - extractive body cue:** These embodied problems require an agent to understand many semantic aspects of the world: the repertoire of skills available, how these skills influence the world, ...
- **p. 1 / Abstract - extractive body cue:** LLMs planning in embodied environments need to consider not just what skills to do, but also how and when to do them - answers that ...
- **p. 1 / Abstract - extractive body cue:** In this work, we investigate to what extent LLMs used in such embodied contexts can reason over sources of feedback provided through natural language, without ...
- **p. 1 / Abstract - extractive body cue:** We propose that by leveraging environment feedback, LLMs are able to form an inner monologue that allows them to more richly process and plan in ...
- **p. 1 / 1 Introduction - extractive body cue:** While conventionally these challenges have been approached from the perspective of planning (e.g., TAMP [1]) or hierarchical learning (e.g., HRL [2]), effective high-level reasoning about ...
- **p. 2 / 1 Introduction - extractive body cue:** Notably, we show that it can efficiently retry under observed stochastic failure, replan under systematic infeasibility, or request human feedback for ambiguous queries, resulting in ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | While conventionally these challenges have been approached from the perspective of planning (e.g., TAMP [1]) or hierarchical learning (e.g., HRL [2]), effective ... | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | As a demonstration of the versatility of LLMs and grounded closed-loop feedback, we additionally show several surprising capabilities emerging from the inner ... | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF body |
| State / latent | demonstration, versatility, LLMs, grounded, closed-loop, feedback, additionally, several, surprising, capabilities | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | input, model, consists, initial, image, observation, final, after | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: demonstration, versatility, LLMs, grounded, closed-loop, feedback, additionally, several, surprising, capabilities | p. 2 (1 Introduction), p. 15 (A.1 Inner Monologue for Simulated Tabletop Rearrangement), p. 17 (A.2 Inner Monologue for Real-World Tabletop Rearrangement) |
| Decision / output variable | action, pose, option or chunk a; body terms: Inspired, human, thought, process, inner, monologue, natural, framework | p. 1 (1 Introduction), p. 2 (1 Introduction), p. 17 (A.2 Inner Monologue for Real-World Tabletop Rearrangement) |
| Objective / loss / cost | policy/action modeling objective; cue terms: model, trained, binary, cross, entropy, loss, respect, ground | p. 17 (A.2 Inner Monologue for Real-World Tabletop Rearrangement), p. 17 (A.2 Inner Monologue for Real-World Tabletop Rearrangement), p. 18 (A.2 Inner Monologue for Real-World Tabletop Rearrangement), p. 18 (A.2 Inner Monologue for Real-World Tabletop Rearrangement) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 15 (A.1 Inner Monologue for Simulated Tabletop Rearrangement), p. 16 (A.2 Inner Monologue for Real-World Tabletop Rearrangement), p. 18 (A.2 Inner Monologue for Real-World Tabletop Rearrangement) |
| Success / guarantee | instruction-conditioned task success | p. 6 (Figure/Table caption), p. 6 (Figure/Table caption), p. 7 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1 Introduction - extractive body cue:** Notably, we show that it can efficiently retry under observed stochastic failure, replan under systematic infeasibility, or request human feedback for ambiguous queries, resulting in ...
- **p. 1 / 1 Introduction - extractive body cue:** While prior work has investigated using language models as planners [20, 21] or incorporating.

## What the Paper Changes

PDF body contribution framing (p. 1 (1 Introduction), p. 2 (1 Introduction), p. 17 (A.2 Inner Monologue for Real-World Tabletop Rearrangement), p. 2 (1 Introduction), p. 1 (1 Introduction)): Inspired by the human thought process, we propose that such an inner monologue is a natural framework for incorporating feedback for LLMs.

- **p. 2 / 1 Introduction - extractive body cue:** Robot Success Detector Scene Descriptor (b) (c) (a) Human Figure 1: Inner Monologue enables grounded closed-loop feedback for robot planning with large language models by ...
- **p. 17 / A.2 Inner Monologue for Real-World Tabletop Rearrangement - extractive body cue:** The input to the model consists of: (1) o0, the initial image observation, (2) of, the final image observation after the policy chose to terminate ...
- **p. 2 / 1 Introduction - extractive body cue:** Notably, we show that it can efficiently retry under observed stochastic failure, replan under systematic infeasibility, or request human feedback for ambiguous queries, resulting in ...
- **p. 1 / 1 Introduction - extractive body cue:** We observe that similarly to recent work [19], natural language provides a universal and interpretable interface for such grounding of model communication and allows them ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 9 | Table 5. As for failure modes, Inner Monologue may fail due to several sources of errors: (1) success ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | Table 3: Averaged success rate across 120 evaluations on several task families in our real-world mobile manipulation environment. ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | Table 1: Success rates for various methods, averaged across 50 episodes in Ravens-based environment with test-time disturbances. CLIPort ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | Figure 4: Failure causes on 120 evaluations. When disturbances are added (red), only the Inner Mono- logue variants ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 2 (1 Introduction), p. 15 (A.1 Inner Monologue for Simulated Tabletop Rearrangement), p. 17 (A.2 Inner Monologue for Real-World Tabletop Rearrangement), p. 16 (A.2 Inner Monologue for Real-World Tabletop Rearrangement). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (1 Introduction), p. 2 (1 Introduction), p. 1 (1 Introduction), interface p. 2 (1 Introduction), p. 15 (A.1 Inner Monologue for Simulated Tabletop Rearrangement), p. 17 (A.2 Inner Monologue for Real-World Tabletop Rearrangement), p. 16 (A.2 Inner Monologue for Real-World Tabletop Rearrangement), objective p. 17 (A.2 Inner Monologue for Real-World Tabletop Rearrangement), p. 17 (A.2 Inner Monologue for Real-World Tabletop Rearrangement), p. 18 (A.2 Inner Monologue for Real-World Tabletop Rearrangement), p. 18 (A.2 Inner Monologue for Real-World Tabletop Rearrangement).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (25 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** While conventionally these challenges have been approached from the perspective of planning (e.g., TAMP [1]) or hierarchical learning (e.g., HRL [2]), effective high-level reasoning about complex tasks also requires semantic ... (p. 1, 1 Introduction).
- **Formulation-changing contribution:** Inspired by the human thought process, we propose that such an inner monologue is a natural framework for incorporating feedback for LLMs. (p. 1, 1 Introduction).
- **Assumption/failure evidence:** Notably, we show that it can efficiently retry under observed stochastic failure, replan under systematic infeasibility, or request human feedback for ambiguous queries, resulting in significantly improved performance in dynamical ... (p. 2, 1 Introduction).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
