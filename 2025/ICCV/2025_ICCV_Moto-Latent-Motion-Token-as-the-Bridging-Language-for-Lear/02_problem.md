# Problem - Moto: Latent Motion Token as the Bridging Language for Learning Robot Manipulation from Videos

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Chen_Moto_Latent_Motion_Token_as_the_Bridging_Language_for_Learning_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Chen_Moto_Latent_Motion_Token_as_the_Bridging_Language_for_Learning_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (1. Introduction), p. 2 (1. Introduction)): The main challenge is finding an appropriate representation for autoregressive pre-training on video data that effectively captures prior knowledge for robot manipulation.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Recent developments in Large Language Models (LLMs) pre-trained on extensive corpora have shown significant success in various natural language processing (NLP) tasks with minimal fine-tuning.
- **p. 1 / Abstract - extractive body cue:** This success offers new promise for robotics, which has long been constrained by the high cost of action-labeled data.
- **p. 1 / Abstract - extractive body cue:** We ask: given the abundant video data containing interaction-related knowledge available as a rich "corpus", can a similar generative pretraining approach be effectively applied to ...
- **p. 1 / Abstract - extractive body cue:** The key challenge is to identify an effective representation for autoregressive pre-training that benefits robot manipulation tasks.
- **p. 1 / Abstract - extractive body cue:** Inspired by the way humans learn new skills through observing dynamic environments, we propose that effective robotic learning should emphasize motion-related knowledge, which is closely ...
- **p. 2 / 1. Introduction - extractive body cue:** The main challenge is finding an appropriate representation for autoregressive pre-training on video data that effectively captures prior knowledge for robot manipulation.
- **p. 2 / 1. Introduction - extractive body cue:** These learned priors are subsequently transferred to enhance robot manipulation performance through a co-fine-tuning strategy.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | The main challenge is finding an appropriate representation for autoregressive pre-training on video data that effectively captures prior knowledge for robot manipulation. | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | An MLP-based action head projects the output hidden state of each action query token into the real robot action space. | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF body |
| State / latent | MLP-based, action, head, projects, output, hidden, state, query, token, real | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | Additionally, prepend, text, features, instruction, visual, initial, video | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: MLP-based, action, head, projects, output, hidden, state, query, token, real | p. 4 (3.4. Co-fine-tuning for Robot Manipulation), p. 2 (1. Introduction), p. 4 (3.3. Motion Token Autoregressive Pre-training) |
| Decision / output variable | action, pose, option or chunk a; body terms: summary, contributions, below, Introduction, Latent, Motion, Tokens, model | p. 2 (1. Introduction), p. 3 (3.1. Overview), p. 4 (3.4. Co-fine-tuning for Robot Manipulation) |
| Objective / loss / cost | policy/action modeling objective; cue terms: total, action, loss, Laction, defined, math, mathcal, Delta | p. 4 (3.2. Latent Motion Tokenizer), p. 4 (3.4. Co-fine-tuning for Robot Manipulation) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (3.4. Co-fine-tuning for Robot Manipulation), p. 4 (3.3. Motion Token Autoregressive Pre-training) |
| Success / guarantee | instruction-conditioned task success | p. 7 (5.3. Moto-GPT as an Effective Robot Policy), p. 7 (5.3. Moto-GPT as an Effective Robot Policy), p. 8 (5.3. Moto-GPT as an Effective Robot Policy) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Introduction - extractive body cue:** These learned priors are subsequently transferred to enhance robot manipulation performance through a co-fine-tuning strategy.

## What the Paper Changes

PDF body contribution framing (p. 2 (1. Introduction), p. 3 (3.1. Overview), p. 4 (3.4. Co-fine-tuning for Robot Manipulation), p. 2 (1. Introduction)): In summary, our contributions are as below: • Introduction of Latent Motion Tokens, which model visual motions between video frames in an unsupervised manner, serving as a bridging "language" for ...

- **p. 3 / 3.1. Overview - extractive body cue:** 2, Moto consists of three stages: 1) unsupervised training of the Latent Motion Tokenizer, 2) pre-training of the generative model MotoGPT, and 3) co-fine-tuning for ...
- **p. 4 / 3.4. Co-fine-tuning for Robot Manipulation - extractive body cue:** To address this, during fine-tuning, we introduce special action query tokens into Moto-GPT's input, enabling the generation of real robot actions through a flexible action ...
- **p. 2 / 1. Introduction - extractive body cue:** The performance can be further boosted with human video pre-training, highlighting the potential of our approach in transferring motion knowledge learned from Internet-scale videos to ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 6 | 7, clearly differentiate successful trajectories from failures and random attempts. | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | The top-k token prediction accuracy and the visualization of predicted video trajectories 20 40 60 80 Sequence Step ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Future work will improve model architectures and incorporate more diverse human videos to tackle complex manipulation tasks. | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | This further demonstrates the robustness of MotoGPT in real-world deployment. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 4 (3.4. Co-fine-tuning for Robot Manipulation), p. 2 (1. Introduction), p. 4 (3.3. Motion Token Autoregressive Pre-training), p. 3 (3.1. Overview). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1. Introduction), p. 2 (1. Introduction), interface p. 4 (3.4. Co-fine-tuning for Robot Manipulation), p. 2 (1. Introduction), p. 4 (3.3. Motion Token Autoregressive Pre-training), p. 3 (3.1. Overview), objective p. 4 (3.2. Latent Motion Tokenizer), p. 4 (3.4. Co-fine-tuning for Robot Manipulation).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
