# Problem - PILCO: A Model-Based and Data-Efficient Approach to Policy Search

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://icml.cc/2011/papers/323_icmlpaper.pdf; PDF retrieval source: https://www.deisenroth.cc/publication/deisenroth-2011-c/. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (Abstract), p. 1 (Abstract), p. 2 (2.1. Dynamics Model Learning)): Pilco reduces model bias, one of the key problems of model-based reinforcement learning, in a principled way.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** In this paper, we introduce pilco, a practical, data-efficient model-based policy search method.
- **p. 1 / Abstract - extractive body cue:** Pilco reduces model bias, one of the key problems of model-based reinforcement learning, in a principled way.
- **p. 1 / Abstract - extractive body cue:** By learning a probabilistic dynamics model and explicitly incorporating model uncertainty into long-term planning, pilco can cope with very little data and facilitates learning from ...
- **p. 1 / Abstract - extractive body cue:** Policy evaluation is performed in closed form using state-ofthe-art approximate inference.
- **p. 1 / Abstract - extractive body cue:** Furthermore, policy gradients are computed analytically for policy improvement.
- **p. 2 / 2.1. Dynamics Model Learning - extractive body cue:** (5) Throughout this paper, we consider a prior mean function m ≡0 and the squared exponential (SE) kernel k with automatic relevance determination.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Pilco reduces model bias, one of the key problems of model-based reinforcement learning, in a principled way. | 실물 카트폴과 모의 외발 로봇의 제어 학습 | body wording is the source claim |
| Observation / input | Policy evaluation is performed in closed form using state-ofthe-art approximate inference. | 상태·행동·관측된 다음 상태 | exact sensor/frame/preprocessing from PDF body |
| State / latent | Policy, evaluation, performed, closed, form, state-ofthe-art, approximate, inference, PILCO, Model-Based | 가우시안 과정 동역학과 미래 상태 분포 | notation and tensor shape require body check |
| Output / action | Furthermore, policy, gradients, computed, analytically, improvement, following, detail | 기대 장기 비용으로 갱신한 피드백 정책 | exact unit/frame/decoder require body check |
| Target outcome | cross-domain transfer and task performance | 상호작용 시간과 제어 목표 달성 | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | 상태·행동·관측된 다음 상태; body terms: Policy, evaluation, performed, closed, form, state-ofthe-art, approximate, inference, PILCO, Model-Based | p. 1 (Abstract), p. 3 (2.1. Dynamics Model Learning), p. 1 (Abstract) |
| Decision / output variable | 기대 장기 비용으로 갱신한 피드백 정책; body terms: introduce, pilco, practical, data-efficient, model-based, policy, search, evaluation | p. 1 (Abstract) |
| Objective / loss / cost | 상호작용 시간과 제어 목표 달성; cue terms: Analytic, derivatives, allow, standard, gradient-based, non-convex, optimization, methods | p. 2 (2. Model-based Indirect Policy Search), p. 4 (2.3. Analytic Gradients for Policy Improvement), p. 5 (2.3. Analytic Gradients for Policy Improvement), p. 5 (2.3. Analytic Gradients for Policy Improvement) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 2 (2.1. Dynamics Model Learning), p. 4 (2.2.2. Covariance Matrix of the Prediction), p. 5 (2.3. Analytic Gradients for Policy Improvement) |
| Success / guarantee | cross-domain transfer and task performance | p. 6 (3.3. Unicycle Riding), p. 6 (3.3. Unicycle Riding), p. 3 (2.2. Policy Evaluation) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / Abstract - extractive body cue:** By learning a probabilistic dynamics model and explicitly incorporating model uncertainty into long-term planning, pilco can cope with very little data and facilitates learning from ...
- **p. 2 / 2.1. Dynamics Model Learning - extractive body cue:** (5) Throughout this paper, we consider a prior mean function m ≡0 and the squared exponential (SE) kernel k with automatic relevance determination.

## What the Paper Changes

PDF body contribution framing (p. 1 (Abstract)): In this paper, we introduce pilco, a practical, data-efficient model-based policy search method.

- additional contribution PDF body cue not selected; no claim inferred

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 7 | Hence, pilco's unprecedented data efficiency cannot solely be attributed to any kind of reward shaping. | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | Trial-and-error learning leads to some limitations in the discovered policy: Pilco is not an optimal control method; it ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | The goal was to ride the unicycle, i.e., to prevent it from falling. | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | After 1.2 s, either the unicycle had fallen or the learned controller had managed to balance it very ... | reported limitation/failure wording; scope must be verified |

## Position in the Robotics Loop

상태·행동·관측된 다음 상태 → 가우시안 과정 동역학과 미래 상태 분포 → 기대 장기 비용으로 갱신한 피드백 정책. [원문 근거](./01_overview.md#observation-state-and-output-interface)

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (Abstract), p. 1 (Abstract), p. 2 (2.1. Dynamics Model Learning), interface p. 1 (Abstract), p. 3 (2.1. Dynamics Model Learning), p. 1 (Abstract), p. 2 (2. Model-based Indirect Policy Search), objective p. 2 (2. Model-based Indirect Policy Search), p. 4 (2.3. Analytic Gradients for Policy Improvement), p. 5 (2.3. Analytic Gradients for Policy Improvement), p. 5 (2.3. Analytic Gradients for Policy Improvement).

[공통 검토 기준](../../../../research/READING_STATUS.md#note-checks)

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (8 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** Pilco reduces model bias, one of the key problems of model-based reinforcement learning, in a principled way. (p. 1, Abstract).
- **Formulation-changing contribution:** In this paper, we introduce pilco, a practical, data-efficient model-based policy search method. (p. 1, Abstract).
- **Assumption/failure evidence:** Trial-and-error learning leads to some limitations in the discovered policy: Pilco is not an optimal control method; it merely finds a solution for the task. (p. 7, 4. Discussion and Conclusion).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
