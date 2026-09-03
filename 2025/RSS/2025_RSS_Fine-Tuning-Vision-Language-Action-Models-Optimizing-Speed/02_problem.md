# Problem - Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (24 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p017.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p017.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 3 (A. VIA Fine-Tuning Design Decisions), p. 2 (1. Iyrropucrion), p. 3 (A. VIA Fine-Tuning Design Decisions), p. 4 (B. Implementing Alternative Design Components), p. 1 (1. Iyrropucrion)): Existing approaches that fine-tune VLAs using the base ‘model's autoregressive training recipe face two key limitations: slow inference speed (3-5 Hz) unsuitable for high-frequency control, and unreliable task execution on ...

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Recent vision-language-action models (VLAS) build ‘upon pretrained vision-language model and leverage diverse robot datasets to demonstrate strong task execution, language following ability, and semantic generalization.
- **p. 1 / Abstract - extractive body cue:** Despite these successes, VLAS struggle with novel robot setups and require fine= tuning to achieve good performance, yet how to most effectively fine-tune them is ...
- **p. 1 / Abstract - extractive body cue:** In this work, we study key VLA adaptation design choices such as different action decoding schemes, action representations,
- **p. 1 / Abstract - extractive body cue:** ‘decoding, action chunking, a conti and a simple L1 regression-based lea ference efficiency, policy performance, and flex inthe rodel's input-output opecicatios.
- **p. 1 / Abstract - extractive body cue:** We propose OpenVLA™ OFT, an instantiation of this sels a new state of the art on the L wation benchmark, significantly boosting OpenVLA's average success ...
- **p. 3 / A. VIA Fine-Tuning Design Decisions - extractive body cue:** Existing approaches that fine-tune VLAs using the base ‘model's autoregressive training recipe face two key limitations: slow inference speed (3-5 Hz) unsuitable for high-frequency control, ...
- **p. 2 / 1. Iyrropucrion - extractive body cue:** We address this gap by exploring VLA adaptation design decisions for fast inference and reliable task execution on a real-world bimanual ‘manipulator with a 25 ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Existing approaches that fine-tune VLAs using the base ‘model's autoregressive training recipe face two key limitations: slow inference speed (3-5 Hz) unsuitable ... | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | ‘decoding, action chunking, a conti and a simple L1 regression-based lea ference efficiency, policy performance, and flex inthe rodel's input-output opecicatios. | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF body |
| State / latent | decoding, action, chunking, conti, simple, regression-based, ference, efficiency, policy, performance | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | Building, insights, introduce, OpenVLA-OFT, instantiation, Optimized, Fine-Tuning, OFT | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: decoding, action, chunking, conti, simple, regression-based, ference, efficiency, policy, performance | p. 1 (Abstract), p. 7 (3) LI regression objective), p. 1 (1. Iyrropucrion) |
| Decision / output variable | action, pose, option or chunk a; body terms: next, section, present, parallel, generation, scheme, enables, efficient | p. 3 (1. Iyrropucrion), p. 1 (Abstract), p. 1 (1. Iyrropucrion) |
| Objective / loss / cost | policy/action modeling objective; cue terms: maintain, same, convergence, criterion, LIBERO, experiments, training, until | p. 15 (C. Feature-wise Linear Modulation (FILM) Implementation), p. 8 (3) LI regression objective), p. 14 (B. Implementation Details), p. 15 (C. Feature-wise Linear Modulation (FILM) Implementation) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 14 (B. Implementation Details), p. 14 (C. Feature-wise Linear Modulation (FILM) Implementation), p. 15 (C. Feature-wise Linear Modulation (FILM) Implementation) |
| Success / guarantee | instruction-conditioned task success | p. 9 (C. ALOHA Task Performance Results), p. 8 (C. ALOHA Task Performance Results), p. 9 (C. ALOHA Task Performance Results) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Iyrropucrion - extractive body cue:** We address this gap by exploring VLA adaptation design decisions for fast inference and reliable task execution on a real-world bimanual ‘manipulator with a 25 ...
- **p. 3 / A. VIA Fine-Tuning Design Decisions - extractive body cue:** To address these challenges, we investigate three key design components for VLA fine-tuning:
- **p. 4 / B. Implementing Alternative Design Components - extractive body cue:** Challenges with language following, When deploying on the ALOHA robot setup with multiple viewpoints including from wrist-mounted cameras, we observe that policies can struggle with ...
- **p. 1 / 1. Iyrropucrion - extractive body cue:** Prior work has begun exploring VLA adaptation strategies, with Kim et al.

## What the Paper Changes

PDF body contribution framing (p. 3 (1. Iyrropucrion), p. 1 (Abstract), p. 1 (1. Iyrropucrion), p. 14 (B. Implementation Details), p. 2 (1. Iyrropucrion)): In the next section, ‘we present a parallel generation scheme that enables efficient action chunking.

- **p. 1 / Abstract - extractive body cue:** We propose OpenVLA™ OFT, an instantiation of this sels a new state of the art on the L wation benchmark, significantly boosting OpenVLA's average success ...
- **p. 1 / 1. Iyrropucrion - extractive body cue:** Building on these insights, we introduce OpenVLA-OFT: an instantiation of an Optimized Fine-Tuning (OFT) recipe that integrates parallel decoding and action chunking, continuous action representations, ...
- **p. 14 / B. Implementation Details - extractive body cue:** LI regression: The MLP action head consists of 4 layers with ReLU activation, mapping final Llama-2 decoder layer hidden states directly to continuous actions.
- **p. 2 / 1. Iyrropucrion - extractive body cue:** With 25-timestep action ‘chunks, OpenVLA-OFT+ achieves 43% faster throughput than base OpenVLA, demonstrating that our new fine-tuning recipe ‘enables real-time robot control with strong task ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 9 | On the other hand, zy demonstrates more robust execution ‘with smoother motions and better reactivity to feedback, often ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | As visualized in Figure 6, it often fails to correct mistakes in the "scoop X into | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Among VLAs, we observe distinct charac teristics: RDT-IB achieves good language following through its "Alternating Condition Injection" scheme ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | Top In some cases, RDT-IB fails 10 respond to missed howl placement, coatiauing 10 pour iagredieats into empey ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 1 (Abstract), p. 7 (3) LI regression objective), p. 1 (1. Iyrropucrion), p. 4 (B. Implementing Alternative Design Components). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 3 (A. VIA Fine-Tuning Design Decisions), p. 2 (1. Iyrropucrion), p. 3 (A. VIA Fine-Tuning Design Decisions), p. 4 (B. Implementing Alternative Design Components), p. 1 (1. Iyrropucrion), interface p. 1 (Abstract), p. 7 (3) LI regression objective), p. 1 (1. Iyrropucrion), p. 4 (B. Implementing Alternative Design Components), objective p. 15 (C. Feature-wise Linear Modulation (FILM) Implementation), p. 8 (3) LI regression objective), p. 14 (B. Implementation Details), p. 15 (C. Feature-wise Linear Modulation (FILM) Implementation).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (24 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** To address these challenges, we investigate three key design components for VLA fine-tuning: (p. 3, A. VIA Fine-Tuning Design Decisions).
- **Formulation-changing contribution:** In the next section, ‘we present a parallel generation scheme that enables efficient action chunking. (p. 3, 1. Iyrropucrion).
- **Assumption/failure evidence:** As visualized in Figure 6, it often fails to correct mistakes in the "scoop X into (p. 8, C. ALOHA Task Performance Results).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
