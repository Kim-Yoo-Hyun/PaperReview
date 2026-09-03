# Problem - VQ-VLA: Improving Vision-Language-Action Models via Scaling Vector-Quantized Action Tokenizers

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Wang_VQ-VLA_Improving_Vision-Language-Action_Models_via_Scaling_Vector-Quantized_Action_Tokenizers_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Wang_VQ-VLA_Improving_Vision-Language-Action_Models_via_Scaling_Vector-Quantized_Action_Tokenizers_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction)): In this paper, we delve deeper into the potential of action tokenization, with a specific emphasis on its scalability and accuracy.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** In this paper, we introduce an innovative vector quantization based action tokenizer built upon the largest-scale action trajectory dataset to date, leveraging over 100 times ...
- **p. 1 / Abstract - extractive body cue:** This extensive dataset enables our tokenizer to capture rich spatiotemporal dynamics, resulting in a model that not only accelerates inference but also generates smoother and ...
- **p. 1 / Abstract - extractive body cue:** Once trained, the tokenizer can be seamlessly adapted to a wide range of downstream tasks in a zero-shot manner, from short-horizon reactive behaviors to long-horizon ...
- **p. 1 / Abstract - extractive body cue:** A key finding of our work is that the domain gap between synthetic and real action trajectories is marginal, allowing us to effectively utilize a ...
- **p. 1 / Abstract - extractive body cue:** To validate our approach, we conducted extensive experiments in both simulated environments and on real robotic platforms.
- **p. 1 / 1. Introduction - extractive body cue:** In this paper, we delve deeper into the potential of action tokenization, with a specific emphasis on its scalability and accuracy.
- **p. 2 / 1. Introduction - extractive body cue:** In summary, our contributions are as follows: • We propose a general convolutional residual VQ-VAEbased framework for action tokenizers. • We demonstrate that action tokenizers ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | In this paper, we delve deeper into the potential of action tokenization, with a specific emphasis on its scalability and accuracy. | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | The method frames action prediction as a vision-language task, mapping input observation images and natural language instructions to discrete robot action sequences. | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF body |
| State / latent | frames, action, prediction, vision-language, task, mapping, input, observation, images, natural | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | low-frequency, high-frequency, temporal, patterns, input, actions, improving, ability | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: frames, action, prediction, vision-language, task, mapping, input, observation, images, natural | p. 2 (3. Methods), p. 3 (3. Methods), p. 4 (3.3. Training Residual VQ-VAE) |
| Decision / output variable | action, pose, option or chunk a; body terms: summary, contributions, follows, general, convolutional, residual, VQ-VAEbased, framework | p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction) |
| Objective / loss / cost | policy/action modeling objective; cue terms: train, framework, minimize, total, loss, weighted, combination, reconstruction | p. 3 (3.2. Action Tokenizer via Residual VQ-VAE), p. 3 (3. Methods), p. 4 (3.4. Integrating Residual VQ-VAE as Action Tok), p. 4 (3.4. Integrating Residual VQ-VAE as Action Tok), p. 2 (3. Methods) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (3.4. Integrating Residual VQ-VAE as Action Tok), p. 2 (3. Methods), p. 2 (3. Methods) |
| Success / guarantee | instruction-conditioned task success | p. 6 (4.2.2. Performance on Short-Horizon Tasks), p. 6 (4.2.3. Performance on Long-Horizon Tasks), p. 5 (4.1.2. Effectiveness of Conv Residual VQ-VAE) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. Introduction - extractive body cue:** In this paper, we delve deeper into the potential of action tokenization, with a specific emphasis on its scalability and accuracy.

## What the Paper Changes

PDF body contribution framing (p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.3. Training Residual VQ-VAE)): In summary, our contributions are as follows: • We propose a general convolutional residual VQ-VAEbased framework for action tokenizers. • We demonstrate that action tokenizers can be effectively scaled by ...

- **p. 1 / 1. Introduction - extractive body cue:** Specifically, we propose a convolutional residual VQVAE [5, 28, 52] framework for training action tokenizers.
- **p. 1 / 1. Introduction - extractive body cue:** To effectively train the model, we propose a progressive training strategy: Initially, we train the tokenizer on realworld robotic datasets, such as OpenX-Embodiment [34], which ...
- **p. 2 / 1. Introduction - extractive body cue:** Compared to previous approaches that typically rely on training with single-task datasets, our method expands the tokenizer training dataset by more than 100 times, effectively ...
- **p. 3 / 3.3. Training Residual VQ-VAE - extractive body cue:** To improve the encoder's ability to process temporal and spatial information, we introduced two types of embeddings before the action sequences are passed into the ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | Despite these promising results, there still remain some limitations and opportunities for future work. | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | 4) Flip the pot upright: We set a flipped pot on the platform, the robot need to flip ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | Although real-world data may contain noise, the inclusion of Open X-Embodiment data as a real-world dataset expands the ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | In contrast, the VQO+L+M model successfully opened the drawer in all test cases, demonstrating its robustness and reliability ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 2 (3. Methods), p. 3 (3. Methods), p. 4 (3.3. Training Residual VQ-VAE), p. 3 (3.2. Action Tokenizer via Residual VQ-VAE). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (1. Introduction), interface p. 2 (3. Methods), p. 3 (3. Methods), p. 4 (3.3. Training Residual VQ-VAE), p. 3 (3.2. Action Tokenizer via Residual VQ-VAE), objective p. 3 (3.2. Action Tokenizer via Residual VQ-VAE), p. 3 (3. Methods), p. 4 (3.4. Integrating Residual VQ-VAE as Action Tok), p. 4 (3.4. Integrating Residual VQ-VAE as Action Tok), p. 2 (3. Methods).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
