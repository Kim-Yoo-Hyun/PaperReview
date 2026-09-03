# Problem - Latent Action Pretraining from Videos

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (27 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.iclr.cc/paper_files/paper/2025/hash/45d74e190008c7bff2845ffc8e3facd3-Abstract-Conference.html; PDF retrieval source: https://proceedings.iclr.cc/paper_files/paper/2025/hash/45d74e190008c7bff2845ffc8e3facd3-Abstract-Conference.html. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION)): However, it is challenging to learn from internet video data for two major challenges: first, much of the raw data on the web lacks explicit action labels; second, the data ...

## PDF Body Digest

- **p. 1 / ABSTRACT - extractive body cue:** We introduce Latent Action Pretraining, the first unsupervised method for pretraining Vision-Language-Action (VLA) models without ground-truth robot action labels.
- **p. 1 / ABSTRACT - extractive body cue:** Existing Vision-Language-Action models require action labels typically collected by human teleoperators during pretraining, which significantly limits possible data sources and scale.
- **p. 1 / ABSTRACT - extractive body cue:** In this work, we propose a method to learn from internet-scale videos that do not have robot action labels.
- **p. 1 / ABSTRACT - extractive body cue:** We first train an action quantization model leveraging VQ-VAE-based objective to learn discrete latent actions between image frames, then pretrain a latent VLA model to ...
- **p. 1 / ABSTRACT - extractive body cue:** Experimental results demonstrate that our method significantly outperforms existing techniques that train robot manipulation policies from large-scale videos.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** However, it is challenging to learn from internet video data for two major challenges: first, much of the raw data on the web lacks explicit ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** However, diverse real-world robot datasets mostly require human teleoperation, which makes scaling difficult.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, it is challenging to learn from internet video data for two major challenges: first, much of the raw data on the ... | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | Then, we do action pretraining by using a pretrained VLM to predict the zt given the language instruction of a video clip ... | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF body |
| State / latent | Then, action, pretraining, pretrained, VLM, predict, given, language, instruction, video | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | Since, latent, pretraining, does, rely, ground, truth, actions | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: Then, action, pretraining, pretrained, VLM, predict, given, language, instruction, video | p. 4 (2. Latent Pretraining), p. 2 (1 INTRODUCTION), p. 4 (2. Latent Pretraining) |
| Decision / output variable | action, pose, option or chunk a; body terms: Vision-Language-Action, Models, VLA, robotics, Brohan, Kim, trained, aligning | p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Objective / loss / cost | policy/action modeling objective; cue terms: Latent, Action, Quantization, first, learn, discrete, actions, fully | p. 3 (2. Latent Pretraining), p. 3 (2. Latent Pretraining), p. 4 (2. Latent Pretraining), p. 4 (2. Latent Pretraining) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (2. Latent Pretraining), p. 4 (2. Latent Pretraining), p. 4 (2. Latent Pretraining) |
| Success / guarantee | instruction-conditioned task success | p. 6 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / 1 INTRODUCTION - extractive body cue:** However, diverse real-world robot datasets mostly require human teleoperation, which makes scaling difficult.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** We measure performance on diverse manipulation videos, including existing robot video datasets (without utilizing ground-truth actions) and human manipulation datasets.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Analogous to Byte Pair Encoding (Sennrich et al., 2016) used for language modeling, this can be seen as learning to tokenize atomic actions without requiring ...

## What the Paper Changes

PDF body contribution framing (p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 4 (2. Latent Pretraining)): Vision-Language-Action Models (VLA) for robotics (Brohan et al., 2023; Kim et al., 2024) are trained by aligning large language models with vision encoders, and then finetuning it on on diverse ...

- **p. 1 / 1 INTRODUCTION - extractive body cue:** Latent Action Pretraining consists of two models that are learned sequentially, followed by a finetuning stage to map the latent actions to real robot actions.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** We expect that our method opens up the potential for building foundation models for robotics by pretraining on much larger web-scale video data.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Furthermore, on real-world manipulation tasks, our method leads to a new monolithic VLA model, outperforming OPENVLA, the current state-of-the-art model Vision Language Action (VLA) model ...
- **p. 4 / 2. Latent Pretraining - extractive body cue:** The VQ-VAE objective enables the latent action zt to be discrete tokens (codebooks), making it easy for VLMs to predict zt.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 25 | Figure 17: Success and Failure Cases of UNIPI. (Top) Given the instruction of ‘move the green block away ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | We observe that most failures of LAPA are due to early grasping. | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | Like before, UNIPI is constrained by its diffusion model's planning limitations, while VPT performs strongly, even surpassing ACTIONVLA ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 10 | 6 LIMITATIONS AND CONCLUSION In this paper, we introduce Latent Action Pretraining, a scalable pretraining method for building ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 4 (2. Latent Pretraining), p. 2 (1 INTRODUCTION), p. 4 (2. Latent Pretraining), p. 1 (1 INTRODUCTION). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), interface p. 4 (2. Latent Pretraining), p. 2 (1 INTRODUCTION), p. 4 (2. Latent Pretraining), p. 1 (1 INTRODUCTION), objective p. 3 (2. Latent Pretraining), p. 3 (2. Latent Pretraining), p. 4 (2. Latent Pretraining), p. 4 (2. Latent Pretraining).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (27 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** However, it is challenging to learn from internet video data for two major challenges: first, much of the raw data on the web lacks explicit action labels; second, the data ... (p. 1, 1 INTRODUCTION).
- **Formulation-changing contribution:** Vision-Language-Action Models (VLA) for robotics (Brohan et al., 2023; Kim et al., 2024) are trained by aligning large language models with vision encoders, and then finetuning it on on diverse ... (p. 1, 1 INTRODUCTION).
- **Assumption/failure evidence:** We observe that most failures of LAPA are due to early grasping. (p. 7, 4 EXPERIMENTS).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
