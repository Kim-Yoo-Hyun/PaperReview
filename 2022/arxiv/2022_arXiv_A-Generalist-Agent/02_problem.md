# Problem - A Generalist Agent

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (42 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2205.06175; PDF retrieval source: https://arxiv.org/abs/2205.06175. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 7 (1 Introduction), p. 10 (1 Introduction), p. 14 (1 Introduction), p. 8 (1 Introduction), p. 9 (1 Introduction)): There are two challenges in this benchmark: Skill Mastery (where the agent is provided data from the 5 test object triplets it is later tested on) and Skill Generalization (where ...

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Inspired by progress in large-scale language modeling, we apply a similar approach towards building a single generalist agent beyond the realm of text outputs.
- **p. 1 / Abstract - extractive body cue:** The agent, which we refer to as Gato, works as a multi-modal, multi-task, multi-embodiment generalist policy.
- **p. 1 / Abstract - extractive body cue:** The same network with the same weights can play Atari, caption images, chat, stack blocks with a real robot arm and much more, deciding based ...
- **p. 1 / Abstract - extractive body cue:** In this report we describe the model and the data, and document the current capabilities of Gato.
- **p. 1 / Abstract - extractive body cue:** A man surfing in the ocean as the sun sets G G What is the capital of France?
- **p. 7 / 1 Introduction - extractive body cue:** There are two challenges in this benchmark: Skill Mastery (where the agent is provided data from the 5 test object triplets it is later tested ...
- **p. 10 / 1 Introduction - extractive body cue:** Agent Group 1 Group 2 Group 3 Group 4 Group 5 Average Gato 24.5% 33% 50.5% 76.5% 66.5% 50.2% BC-IMP (Lee et al., 2021) 23% ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | There are two challenges in this benchmark: Skill Mastery (where the agent is provided data from the 5 test object triplets it ... | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | 2.2 Embedding input tokens and setting output targets After tokenization and sequencing, we apply a parameterized embedding function f(·; θe) to each ... | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF body |
| State / latent | Embedding, input, tokens, setting, output, targets, After, tokenization, sequencing, apply | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | cute, Images, questions, Text, proprioception, continuous, actions, Atari | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: Embedding, input, tokens, setting, output, targets, After, tokenization, sequencing, apply | p. 3 (1 Introduction), p. 3 (1 Introduction), p. 2 (Abstract) |
| Decision / output variable | action, pose, option or chunk a; body terms: During, evaluation, agent, prompted, successful, demonstration, desired, task | p. 4 (1 Introduction), p. 6 (1 Introduction), p. 6 (1 Introduction) |
| Objective / loss / cost | policy/action modeling objective; cue terms: Masking, loss, function, applied, only, target, outputs, text | p. 2 (Abstract), p. 3 (1 Introduction), p. 4 (1 Introduction), p. 4 (1 Introduction), p. 6 (1 Introduction) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (1 Introduction), p. 5 (1 Introduction), p. 8 (1 Introduction) |
| Success / guarantee | instruction-conditioned task success | p. 12 (Figure/Table caption), p. 14 (1 Introduction), p. 14 (1 Introduction) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 10 / 1 Introduction - extractive body cue:** Agent Group 1 Group 2 Group 3 Group 4 Group 5 Average Gato 24.5% 33% 50.5% 76.5% 66.5% 50.2% BC-IMP (Lee et al., 2021) 23% ...
- **p. 14 / 1 Introduction - extractive body cue:** Agent Group 1 Group 2 Group 3 Group 4 Group 5 Average Gato 58% 57.6% 78.5% 89 % 95.1% 75.6% BC-IMP (Lee et al., 2021) ...
- **p. 8 / 1 Introduction - extractive body cue:** For the most difficult task, called BossLevel, Gato scores 75%.
- **p. 9 / 1 Introduction - extractive body cue:** A man in a blue suit with a white bow tie and black shoes.

## What the Paper Changes

PDF body contribution framing (p. 4 (1 Introduction), p. 6 (1 Introduction), p. 6 (1 Introduction), p. 7 (1 Introduction), p. 8 (1 Introduction)): During evaluation, the agent can be prompted using a successful demonstration of the desired task, which we do by default in all control results that we present here.

- **p. 6 / 1 Introduction - extractive body cue:** ALIGN (Jia et al., 2021) consists of 1.8B images and their alternative text (alt-text) annotations.
- **p. 6 / 1 Introduction - extractive body cue:** LTIP (Long Text & Image Pairs), consists of 312 million images with captions (Alayrac et al., 2022).
- **p. 7 / 1 Introduction - extractive body cue:** The environment consists of a Sawyer robot arm with 3-DoF cartesian velocity control, an additional DoF for velocity, and a discrete gripper action.
- **p. 8 / 1 Introduction - extractive body cue:** While the single-task online RL agents which generated the data still outperform Gato, this may be overcome by adding capacity or using offline RL training ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 16 | Figure 13: Embedding visualization. T-SNE visualization of embeddings from different tasks. A large part of the vision-language embeddings ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 18 | 8 Limitations and Future work 8.1 RL data collection Gato is a data-driven approach, as it is derived ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 18 | This limitation underscores the need for a careful design and a deployment process that incorporates multiple disciplines and ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 19 | Context-length is therefore a current limitation of our architecture, mainly due to the quadratic scaling of self-attention. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 3 (1 Introduction), p. 3 (1 Introduction), p. 2 (Abstract), p. 5 (1 Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 7 (1 Introduction), p. 10 (1 Introduction), p. 14 (1 Introduction), p. 8 (1 Introduction), p. 9 (1 Introduction), interface p. 3 (1 Introduction), p. 3 (1 Introduction), p. 2 (Abstract), p. 5 (1 Introduction), objective p. 2 (Abstract), p. 3 (1 Introduction), p. 4 (1 Introduction), p. 4 (1 Introduction), p. 6 (1 Introduction).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (42 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** There are two challenges in this benchmark: Skill Mastery (where the agent is provided data from the 5 test object triplets it is later tested on) and Skill Generalization (where ... (p. 7, 1 Introduction).
- **Formulation-changing contribution:** During evaluation, the agent can be prompted using a successful demonstration of the desired task, which we do by default in all control results that we present here. (p. 4, 1 Introduction).
- **Assumption/failure evidence:** After this point (at 5000), performance degrades slightly but does not drop far below the expert's performance. (p. 12, 1 Introduction).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
