# Problem - Efficient Reinforcement Learning by Guiding World Models with Non-Curated Data

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (35 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://iclr.cc/virtual/2026/poster/10007436; PDF retrieval source: https://arxiv.org/pdf/2502.19544. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION)): While pre-training visual encoders (Schwarzer et al., 2021; Nair et al., 2022; Parisi et al., 2022; Xiao et al., 2022; Yang & Nachum, 2021; Shang et al., 2024) is a ...

## PDF Body Digest

- **p. 1 / ABSTRACT - extractive PDF cue:** Leveraging offline data is a promising way to improve the sample efficiency of online reinforcement learning (RL).
- **p. 1 / ABSTRACT - extractive PDF cue:** This paper expands the pool of usable data for offline-to-online RL by leveraging abundant non-curated data that is reward-free, of mixed quality, and collected across ...
- **p. 1 / ABSTRACT - extractive PDF cue:** Although learning a world model appears promising for utilizing such data, we find that naive finetuning fails to accelerate RL training on many tasks.
- **p. 1 / ABSTRACT - extractive PDF cue:** Through careful investigation, we attribute this failure to the distributional shift between offline and online data during fine-tuning.
- **p. 1 / ABSTRACT - extractive PDF cue:** To address this issue and effectively use the offline data, we propose two techniques: i) experience rehearsal and ii) execution guidance.
- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** While pre-training visual encoders (Schwarzer et al., 2021; Nair et al., 2022; Parisi et al., 2022; Xiao et al., 2022; Yang & Nachum, 2021; Shang ...
- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** However, prior work has explored world model training primarily in settings with known rewards (Lu et al., 2023; Rafailov et al., 2023; Hansen et al., ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | While pre-training visual encoders (Schwarzer et al., 2021; Nair et al., 2022; Parisi et al., 2022; Xiao et al., 2022; Yang & ... | uncertain robot state와 safe/unsafe operating region | body wording is the source claim |
| Observation / input | While pre-training visual encoders (Schwarzer et al., 2021; Nair et al., 2022; Parisi et al., 2022; Xiao et al., 2022; Yang & ... | observation, uncertainty/risk estimate와 task command | exact sensor/frame/preprocessing from PDF |
| State / latent | While, pre-training, visual, encoders, Schwarzer, Nair, Parisi, Xiao, Yang, Nachum | safe set, recovery state 또는 constraint margin | notation and tensor shape require body check |
| Output / action | representative, challenging, tasks, NCRL, outperforms, baselines, leverage, offline | shielded, recovery 또는 safe action | exact unit/frame/decoder require body check |
| Target outcome | low violation/failure probability with useful intervention | task return과 violation/failure probability | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | state/history and risk h(s); body terms: While, pre-training, visual, encoders, Schwarzer, Nair, Parisi, Xiao, Yang, Nachum | p. 1 (1 INTRODUCTION), p. 2 (3. Train), p. 2 (3. Train) |
| Decision / output variable | filtered/recovery action u_safe; body terms: summarize, contributions, more, realistic, setting, leveraging, offline, data | p. 2 (3. Train), p. 1 (ABSTRACT), p. 1 (ABSTRACT) |
| Objective / loss / cost | task utility subject to safety constraint; cue terms: instance, leveraging, offline, datasets, robotic, manipulation, tasks, requires | no optimization/equation sentence selected |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 2 (3. Train), p. 2 (3. Train), p. 3 (3. Train) |
| Success / guarantee | low violation/failure probability with useful intervention | p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 20 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** However, prior work has explored world model training primarily in settings with known rewards (Lu et al., 2023; Rafailov et al., 2023; Hansen et al., ...

## What the Paper Changes

PDF contribution framing (p. 2 (3. Train), p. 1 (ABSTRACT), p. 1 (ABSTRACT), p. 2 (3. Train), p. 3 (3. Train)): To summarize, our contributions are: C1 We propose a more realistic setting for leveraging offline data that consists of reward-free and mixed-quality multi-embodiment data.

- **p. 1 / ABSTRACT - extractive PDF cue:** To address this issue and effectively use the offline data, we propose two techniques: i) experience rehearsal and ii) execution guidance.
- **p. 1 / ABSTRACT - extractive PDF cue:** Under limited sample budgets, our method achieves nearly twice the aggregate score of learning-from-scratch baselines across 72 visuomotor tasks spanning 6 embodiments.
- **p. 2 / 3. Train - extractive PDF cue:** To this end, we propose a pipeline named Non-curated offline data for efficient RL (NCRL).
- **p. 3 / 3. Train - extractive PDF cue:** C3 We propose two techniques, experience rehearsal and execution guidance, to mitigate the distributional gap and encourage exploration during RL fine-tuning.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 10 | We show that naive fine-tuning of world models fails to accelerate RL training due to distributional shift and ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | R3M fails to improve sample efficiency on most tasks, consistent with findings in Hansen et al. | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | As the compared baselines cannot handle multi-embodiment data like NCRL, we preprocess the offline data to only include ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | 6, world model pre-training shows promising results when the offline data consists of diverse trajectories, such as data ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

safety writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 1 (1 INTRODUCTION), p. 2 (3. Train), p. 2 (3. Train), p. 3 (3. Train). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), interface p. 1 (1 INTRODUCTION), p. 2 (3. Train), p. 2 (3. Train), p. 3 (3. Train), objective no optimization/equation sentence selected.
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
