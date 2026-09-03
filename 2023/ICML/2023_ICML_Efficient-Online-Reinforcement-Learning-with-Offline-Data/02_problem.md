# Problem - Efficient Online Reinforcement Learning with Offline Data

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v202/ball23a.html; PDF retrieval source: https://proceedings.mlr.press/v202/ball23a/ball23a.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Preliminaries)): While the individual ingredients of RLPD are refreshingly simple modifications on existing RL components, we show that their combination delivers state-of-the-art performance on a number of popular online RL with ...

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Sample efficiency and exploration remain major challenges in online reinforcement learning (RL).
- **p. 1 / Abstract - extractive body cue:** A powerful approach that can be applied to address these issues is the inclusion of offline data, such as prior trajectories from a human expert ...
- **p. 1 / Abstract - extractive body cue:** Previous methods have relied on extensive modifications and additional complexity to ensure the effective use of this data.
- **p. 1 / Abstract - extractive body cue:** Instead, we ask: can we simply apply existing off-policy methods to leverage offline data when learning online?
- **p. 1 / Abstract - extractive body cue:** In this work, we demonstrate that the answer is yes; however, a set of minimal but important changes to existing off-policy RL algorithms are required ...
- **p. 2 / 1. Introduction - extractive body cue:** While the individual ingredients of RLPD are refreshingly simple modifications on existing RL components, we show that their combination delivers state-of-the-art performance on a number ...
- **p. 1 / 1. Introduction - extractive body cue:** Here we show the difficult D4RL AntMaze domain (10 seeds, 1 std. shaded), averaged over all 6 tasks.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | While the individual ingredients of RLPD are refreshingly simple modifications on existing RL components, we show that their combination delivers state-of-the-art performance ... | offline robot transition/trajectory dataset과 deployment MDP | body wording is the source claim |
| Observation / input | This in turn does not discourage the policy from exploring unknown and potentially valuable regions of the state-action space. | dataset state/observation, action, reward와 return-to-go | exact sensor/frame/preprocessing from PDF body |
| State / latent | turn, does, discourage, policy, exploring, unknown, potentially, valuable, regions, state-action | Q/value 또는 sequence-policy state | notation and tensor shape require body check |
| Output / action | property, offline, datasets, they, usually, provide, complete, state-action | dataset-supported action sequence | exact unit/frame/decoder require body check |
| Target outcome | offline return and deployment safety | offline policy value, OOD safety와 closed-loop success | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | dataset transition (s,a,r,s′); body terms: turn, does, discourage, policy, exploring, unknown, potentially, valuable, regions, state-action | p. 4 (4. Online RL with Offline Data), p. 5 (4.4. Per-Environment Design Choices), p. 3 (3. Preliminaries) |
| Decision / output variable | dataset-supported policy action; body terms: First, simple, mechanism, incorporating, prior, data, present, off-policy | p. 3 (4. Online RL with Offline Data), p. 3 (4. Online RL with Offline Data), p. 1 (1. Introduction) |
| Objective / loss / cost | offline value with OOD control; cue terms: Determine, number, Critic, targets, subset, Initialize, empty, replay | p. 5 (4.4. Per-Environment Design Choices), p. 5 (4.4. Per-Environment Design Choices), p. 1 (1. Introduction), p. 3 (4. Online RL with Offline Data), p. 4 (4.4. Per-Environment Design Choices), p. 2 (1. Introduction) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (4.4. Per-Environment Design Choices), p. 2 (1. Introduction), p. 8 (2 Layers) |
| Success / guarantee | offline return and deployment safety | p. 17 (Figure/Table caption), p. 8 (Figure/Table caption), p. 7 (5.1. RLPD Analysis and Ablation Study) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. Introduction - extractive body cue:** Here we show the difficult D4RL AntMaze domain (10 seeds, 1 std. shaded), averaged over all 6 tasks.
- **p. 1 / 1. Introduction - extractive body cue:** In real-world problems, however, we are often confronted with scenarios where samples are expensive, and furthermore, rewards are sparse, often exacerbated by high dimensional state ...
- **p. 2 / 1. Introduction - extractive body cue:** Thus far however, such methods have seen limited success in this problem setting.
- **p. 3 / 3. Preliminaries - extractive body cue:** Due to this lack of on-policy coverage, methods using function approximation may over-extrapolate values when learning on this data, leading to a pronounced effect on ...

## What the Paper Changes

PDF body contribution framing (p. 3 (4. Online RL with Offline Data), p. 3 (4. Online RL with Offline Data), p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction)): First, we propose a simple mechanism for incorporating the prior data.

- **p. 3 / 4. Online RL with Offline Data - extractive body cue:** To this end, we present an approach based on off-policy model-free RL, without pre-training or explicit constraints, which we call RLPD (Reinforcement Learning with Prior ...
- **p. 1 / 1. Introduction - extractive body cue:** Here we show the difficult D4RL AntMaze domain (10 seeds, 1 std. shaded), averaged over all 6 tasks.
- **p. 1 / 1. Introduction - extractive body cue:** Our approach, RLPD, extends standard off-policy RL and achieves reliable state-of-the-art online performance on a number of tasks using offline data.
- **p. 2 / 1. Introduction - extractive body cue:** We show that online off-policy RL algorithms can be remarkably effective at learning with offline data.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | Figure 10. Symmetric sampling improves sample efficiency and reduces variance across seeds, and does not work by simply ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Figure 9. In general, critic ensembling provides the best perfor- mance. Dropout performs worse in sparse reward tasks. ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

offline_rl writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 4 (4. Online RL with Offline Data), p. 5 (4.4. Per-Environment Design Choices), p. 3 (3. Preliminaries), p. 3 (3. Preliminaries). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Preliminaries), interface p. 4 (4. Online RL with Offline Data), p. 5 (4.4. Per-Environment Design Choices), p. 3 (3. Preliminaries), p. 3 (3. Preliminaries), objective p. 5 (4.4. Per-Environment Design Choices), p. 5 (4.4. Per-Environment Design Choices), p. 1 (1. Introduction), p. 3 (4. Online RL with Offline Data), p. 4 (4.4. Per-Environment Design Choices), p. 2 (1. Introduction).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (18 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** In real-world problems, however, we are often confronted with scenarios where samples are expensive, and furthermore, rewards are sparse, often exacerbated by high dimensional state and action spaces. (p. 1, 1. Introduction).
- **Formulation-changing contribution:** Here we show the difficult D4RL AntMaze domain (10 seeds, 1 std. shaded), averaged over all 6 tasks. (p. 1, 1. Introduction).
- **Assumption/failure evidence:** To this end, we show that Layer Normalization (LayerNorm) (Ba et al., 2016) can bound the extrapolation of networks but, crucially, does not explicitly constrain the policy to remain close ... (p. 4, 4. Online RL with Offline Data).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
