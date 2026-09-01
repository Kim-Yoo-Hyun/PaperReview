# Problem - Scaling Proprioceptive-Visual Learning with Heterogeneous Pre-trained Transformers

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (24 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://papers.nips.cc/paper_files/paper/2024/hash/e0f393e7980a24fd12fa6f15adfa25fb-Abstract-Conference.html; PDF retrieval source: https://arxiv.org/pdf/2409.20537. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1 Introduction), p. 2 (1 Introduction), p. 6 (1 Introduction), p. 6 (1 Introduction), p. 8 (1 Introduction)): Recent progress in open-source large-scale data collection [14, 75] has made this path possible, but the heterogeneity (such as varying robot hardware and different environments) present in large-scale robotic data ...

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** One of the roadblocks for training generalist robotic models today is heterogeneity.
- **p. 1 / Abstract - extractive body cue:** Previous robot learning methods often collect data to train with one specific embodiment for one task, which is expensive and prone to overfitting.
- **p. 1 / Abstract - extractive body cue:** This work studies the problem of learning policy representations through heterogeneous pretraining on robot data across different embodiments and tasks at scale.
- **p. 1 / Abstract - extractive body cue:** We propose Heterogeneous Pre-trained Transformers (HPT), which pre-train a large, shareable trunk of a policy neural network to learn a task and embodiment agnostic shared ...
- **p. 1 / Abstract - extractive body cue:** This general architecture aligns the specific proprioception and vision inputs from distinct embodiments to a short sequence of tokens and then processes such tokens to ...
- **p. 1 / 1 Introduction - extractive body cue:** Recent progress in open-source large-scale data collection [14, 75] has made this path possible, but the heterogeneity (such as varying robot hardware and different environments) ...
- **p. 2 / 1 Introduction - extractive body cue:** The heterogeneity in robotics presents a distinct challenge: different robots are physically different embodiments1 of hardware acting in different environments.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Recent progress in open-source large-scale data collection [14, 75] has made this path possible, but the heterogeneity (such as varying robot hardware ... | multi-robot demonstration/dataset ecosystem | body wording is the source claim |
| Observation / input | We reinitialize the head and stem parameters with embodiment-specific input and output dimensions (such as different proprioception and action dimensions), and freeze ... | multi-view observation, language/task label과 action trajectory | exact sensor/frame/preprocessing from PDF |
| State / latent | reinitialize, head, stem, parameters, embodiment-specific, input, output, dimensions, different, proprioception | shared representation, embodiment/task identity와 data distribution | notation and tensor shape require body check |
| Output / action | MLP, takes, input, pooled, feature, trunk, outputs, normalized | dataset sample 또는 learned policy action | exact unit/frame/decoder require body check |
| Target outcome | cross-domain transfer and task performance | coverage, cross-embodiment transfer, data efficiency와 task success | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | trajectory D with task/embodiment metadata; body terms: reinitialize, head, stem, parameters, embodiment-specific, input, output, dimensions, different, proprioception | p. 6 (1 Introduction), p. 4 (1 Introduction), p. 5 (1 Introduction) |
| Decision / output variable | normalized sample or downstream action; body terms: introduce, Heterogeneous, Pre-trained, Transformers, HPT, family, architecture, designed | p. 2 (1 Introduction), p. 2 (1 Introduction), p. 5 (1 Introduction) |
| Objective / loss / cost | coverage/data efficiency/transfer objective; cue terms: Since, human, datasets, contain, proprioception, action, information, hand | p. 17 (A.1 Dataset Details) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 17 (A.1 Dataset Details) |
| Success / guarantee | cross-domain transfer and task performance | p. 10 (Figure/Table caption), p. 9 (Figure/Table caption), p. 7 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1 Introduction - extractive body cue:** The heterogeneity in robotics presents a distinct challenge: different robots are physically different embodiments1 of hardware acting in different environments.
- **p. 6 / 1 Introduction - extractive body cue:** Strictly increasing data while keeping others bottlenecked (HPT-S 6
- **p. 6 / 1 Introduction - extractive body cue:** Admittedly, there are several caveats to this metric including the closed-loop performance gap and the task success rate gap.
- **p. 8 / 1 Introduction - extractive body cue:** For the human datasets that lack proprioception and action information, we use poses and 2D positions as surrogates for the supervised policy learning objectives.

## What the Paper Changes

PDF contribution framing (p. 2 (1 Introduction), p. 2 (1 Introduction), p. 5 (1 Introduction), p. 4 (1 Introduction), p. 5 (1 Introduction)): We introduce Heterogeneous Pre-trained Transformers (HPT), a family of architecture designed to scalably learn from data across heterogeneous embodiments.

- **p. 2 / 1 Introduction - extractive body cue:** In this work, we propose to address this issue by aligning the proprioception and vision information from different embodiments to a shared "language" of policies ...
- **p. 5 / 1 Introduction - extractive body cue:** This is used as the input sequence to the trunk that we introduce below.
- **p. 4 / 1 Introduction - extractive body cue:** These tokenizers map heterogeneous inputs from different embodiments to a fixed number of tokens with fixed dimensions, which enables the trunk to treat them in ...
- **p. 5 / 1 Introduction - extractive body cue:** We show illustrations of dataset mixtures (each color is a distinct embodiment) from different domains including real robot teleop [14], deployed robots [38], simulations, and ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 10 | See Appendix §C for some failure modes. | reported limitation/failure wording; scope must be verified |
| body cue at p. 23 | Figure 18: Ablation Study on HPT Stem. We ablate the pre-training performance for (a) proprioception, (b) vision stems, ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 23 | Figure 19: (a) Initial Condition Overlay. We visualize different rollout initial conditions during test times. (b) Failure Cases ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 10 | We hope this perspective will inspire future work in handling the heterogeneous nature of robotic data for robotic ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

robot_data writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 6 (1 Introduction), p. 4 (1 Introduction), p. 5 (1 Introduction), p. 5 (1 Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1 Introduction), p. 2 (1 Introduction), p. 6 (1 Introduction), p. 6 (1 Introduction), p. 8 (1 Introduction), interface p. 6 (1 Introduction), p. 4 (1 Introduction), p. 5 (1 Introduction), p. 5 (1 Introduction), objective p. 17 (A.1 Dataset Details).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
