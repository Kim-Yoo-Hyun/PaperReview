# Problem - Perceiver-Actor: A Multi-Task Transformer for Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (28 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2209.05451; PDF retrieval source: https://arxiv.org/pdf/2209.05451. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction)): Can we still bring the power of Transformers to 6-DoF manipulation with the right problem formulation?

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Transformers have revolutionized vision and natural language processing with their ability to scale with large datasets.
- **p. 1 / Abstract - extractive body cue:** But in robotic manipulation, data is both limited and expensive.
- **p. 1 / Abstract - extractive body cue:** Can manipulation still benefit from Transformers with the right problem formulation?
- **p. 1 / Abstract - extractive body cue:** We investigate this question with PERACT, a language-conditioned behavior-cloning agent for multi-task 6-DoF manipulation.
- **p. 1 / Abstract - extractive body cue:** PERACT encodes language goals and RGB-D voxel observations with a Perceiver Transformer [1], and outputs discretized actions by "detecting the next best voxel action".
- **p. 1 / 1 Introduction - extractive body cue:** Thus, while Transformers may be domain agnostic, they still require the right problem formulation to be data efficient.
- **p. 2 / 1 Introduction - extractive body cue:** In summary, our contributions are as follows: • A novel problem formulation for perceiving, acting, and specifying goals with Transformers. • An efficient action-centric framework ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Can we still bring the power of Transformers to 6-DoF manipulation with the right problem formulation? | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | PERACT encodes language goals and RGB-D voxel observations with a Perceiver Transformer [1], and outputs discretized actions by "detecting the next best ... | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF body |
| State / latent | PERACT, encodes, language, goals, RGB-D, voxel, observations, Perceiver, Transformer, outputs | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | Unlike, frameworks, operate, images, voxelized, observation, action, space | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: PERACT, encodes, language, goals, RGB-D, voxel, observations, Perceiver, Transformer, outputs | p. 1 (Abstract), p. 2 (1 Introduction), p. 1 (Abstract) |
| Decision / output variable | action, pose, option or chunk a; body terms: summary, contributions, follows, novel, problem, formulation, perceiving, acting | p. 2 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction) |
| Objective / loss / cost | policy/action modeling objective; cue terms: not stated or recoverable in the selected PDF body | no optimization/equation sentence selected |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | 본문 anchor 없음 |
| Success / guarantee | instruction-conditioned task success | p. 7 (Figure/Table caption), p. 24 (Figure/Table caption), p. 7 (4 Results) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / 1 Introduction - extractive body cue:** Thus, while Transformers may be domain agnostic, they still require the right problem formulation to be data efficient.
- **p. 2 / 1 Introduction - extractive body cue:** In summary, our contributions are as follows: • A novel problem formulation for perceiving, acting, and specifying goals with Transformers. • An efficient action-centric framework ...
- **p. 2 / 1 Introduction - extractive body cue:** This voxel-based formulation provides a strong structural prior with several benefits: a natural method for fusing multi-view observations, learning robust action-centric3 representations [18, 19], and ...

## What the Paper Changes

PDF body contribution framing (p. 2 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction)): In summary, our contributions are as follows: • A novel problem formulation for perceiving, acting, and specifying goals with Transformers. • An efficient action-centric framework for grounding language in 6-DoF ...

- **p. 1 / 1 Introduction - extractive body cue:** To this end, we present PERACT (short for PERCEIVER-ACTOR), a language-conditioned BC agent that can learn to imitate a wide variety of 6-DoF manipulation tasks ...
- **p. 2 / 1 Introduction - extractive body cue:** We also demonstrate our approach with a Franka Panda on 7 real-world tasks (k-o; only 5 shown) with a multi-task agent trained with just 53 ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 6 | Evaluations are scored either 0 for failures or 100 for complete successes. | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | Each evaluation episode is scored either a 0 for failure or 100 for succces. | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | These are very high-precision tasks where being off by a few centimeters or degrees could lead to unrecoverable ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | The most common failures involved predicting incorrect gripper open actions, which often lead the agent into unseen states. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 1 (Abstract), p. 2 (1 Introduction), p. 1 (Abstract), p. 2 (1 Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), interface p. 1 (Abstract), p. 2 (1 Introduction), p. 1 (Abstract), p. 2 (1 Introduction), objective no optimization/equation sentence selected.
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (28 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** Can we still bring the power of Transformers to 6-DoF manipulation with the right problem formulation? (p. 1, 1 Introduction).
- **Formulation-changing contribution:** In summary, our contributions are as follows: • A novel problem formulation for perceiving, acting, and specifying goals with Transformers. • An efficient action-centric framework for grounding language in 6-DoF ... (p. 2, 1 Introduction).
- **Assumption/failure evidence:** The most common failures involved predicting incorrect gripper open actions, which often lead the agent into unseen states. (p. 8, 4 Results).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
