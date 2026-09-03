# LangWBC: Language-Directed Humanoid Whole-Body Control via End-to-End Learning

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; tesseract OCR fallback; title-token overlap first two pages=1.0); canonical paper source: https://www.roboticsproceedings.org/rss21/p065.html.
> PDF retrieval source: https://www.roboticsproceedings.org/rss21/p065.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / RSS
- Authors: not duplicated here when not verified in the registry source
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: NEXT
- Tags: Robotics, humanoid, whole-body control, language-conditioned control, policy distillation
- Official paper: https://www.roboticsproceedings.org/rss21/p065.html
- Full-text retrieval: https://www.roboticsproceedings.org/rss21/p065.pdf
- Code/Project: https://langwbc.github.io/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (15 pages; tesseract OCR fallback; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Locomotion, whole-body, mobile manipulation, and humanoids의 humanoid 문제를 이해하기 위해 읽는다. 본문은 However, transferring these controllers to real-world hardware faces challenges due to the sim-to-real gap.를 문제로 두고, Furthermore, our framework enables smooth transitions between motion clips and generates novel motions through interpolation, demonstrating generalization beyond the training data를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** General-purpose humanoid robots are expected 10 interact intuitively with humans, enabling seamless integration into daily life.
- **p. 1 / Abstract - extractive body cue:** Natural language provides the most accessible ‘medium for this purpose.
- **p. 1 / Abstract - extractive body cue:** However, translating language into humanoid whole-body motion remains a si primarily due to the gap between fand physical actions.
- **p. 1 / Abstract - extractive body cue:** In this work, we present an end-to-end, language-directed policy for real-world humanoid whole-body ‘control.
- **p. 1 / Abstract - extractive body cue:** Our approach combines reinforcement learning with policy distillation, allowing a single neural network to interpret inguage commands and execute corresponding. physical acions directly.
- **p. 2 / A. Learning-based Humanoid Whole-body Control - extractive body cue:** However, transferring these controllers to real-world hardware faces challenges due to the sim-to-real gap.
- **p. 4 / A. Motion-Tracking Teacher Policy - extractive body cue:** We categorize the motions into two levels of difficulty:

## Core Idea

- **p. 2 / 1. Iyrropucrion - extractive body cue:** Furthermore, our framework enables smooth transitions between motion clips and generates novel motions through interpolation, demonstrating generalization beyond the training data
- **p. 2 / 1. Iyrropucrion - extractive body cue:** ‘+ Our method enables the generation of diverse motions, smooth transitions, and adaptability to a wide range of textual inputs, including the synthesis of novel ...
- **p. 1 / Abstract - extractive body cue:** In this work, we present an end-to-end, language-directed policy for real-world humanoid whole-body ‘control.
- **p. 1 / 1. Iyrropucrion - extractive body cue:** In this work, we introduce LangWBC, a framework that addresses these dual challenges through a single end-to-end
- **p. 3 / B. Generative Action Modeling - extractive body cue:** enables robust real-world deployment but also generates novel, unseen motions while generalizing to similar text commands.
- **p. 5 / B. Language-Directed Student Policy - extractive body cue:** The decoder then takes the sampled latent vector =: along with the latest state observation to output the action We use an MLP with layer ...
- **p. 3 / B. Generative Action Modeling - extractive body cue:** Then, «stdent policy, leveraging a CVAE architecture, jointly models high-level linguistic insretions and low-level physical actions of the teacher policy ina unified Intent space, During ...
- **p. 4 / A. Motion-Tracking Teacher Policy - extractive body cue:** ‘The teacher policy is trained using Proximal Policy Optimization (PPO) [33] to minimize the discrepancy between the robot's movements and the reference motions. ‘To encourage ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | ‘To enable the robot to interpret and act on natural language commands, we design a CVAE-based student policy that encodes textual instructions and physical actions into a unified latent space, using only ... | proprioception, reference pose/motion, visual or language command | p. 4 (B. Language-Directed Student Policy), p. 4 (B. Language-Directed Student Policy) |
| State/latent | enable, robot, interpret, natural, language, commands, design, CVAE-based, student, policy, encodes, textual | whole-body pose, balance/contact state와 skill/mode | p. 4 (B. Language-Directed Student Policy), p. 4 (B. Language-Directed Student Policy), p. 5 (B. Language-Directed Student Policy) |
| Output/action | We input a sequence of historical observations and actions, sampled at 10 Hz over a 2-second window, yielding a 20-step trajectory of input-output pars. | joint/whole-body action, motion target 또는 task trajectory | p. 4 (B. Language-Directed Student Policy), p. 5 (B. Language-Directed Student Policy), p. 3 (III. MerHops) |
| Objective/outcome | ‘The teacher policy is trained using Proximal Policy Optimization (PPO) [33] to minimize the discrepancy between the robot's movements and the reference motions. ‘To encourage symmetry inthe learned policy, we also incorporate ... | tracking, balance, skill/task success와 recovery | p. 4 (A. Motion-Tracking Teacher Policy), p. 3 (A. Motion-Tracking Teacher Policy), p. 3 (A. Motion-Tracking Teacher Policy) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Iyrropucrion - extractive body cue:** Furthermore, our framework enables smooth transitions between motion clips and generates novel motions through interpolation, demonstrating generalization beyond the training data
- **p. 2 / 1. Iyrropucrion - extractive body cue:** ‘+ Our method enables the generation of diverse motions, smooth transitions, and adaptability to a wide range of textual inputs, including the synthesis of novel ...
- **p. 1 / Abstract - extractive body cue:** In this work, we present an end-to-end, language-directed policy for real-world humanoid whole-body ‘control.
- **p. 1 / 1. Iyrropucrion - extractive body cue:** In this work, we introduce LangWBC, a framework that addresses these dual challenges through a single end-to-end
- **p. 3 / B. Generative Action Modeling - extractive body cue:** enables robust real-world deployment but also generates novel, unseen motions while generalizing to similar text commands.
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 9. Latent Space Interpolation: CLIP+CVAE ys. CLIP. Alone ‘Comparison of motion quality when iterpolting between forward and side- ‘ways walking. The CLIPSCVAE model (let) ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | SYSTEM / EVALUATION SCOPE UNRESOLVED | do not infer unreported downstream behavior | p. 9 (Figure/Table caption) |
| Embodiment/environment | We conduct extensive experiments to evaluate our framework for language-directed humanoid whole-body control with 4 Unitree GI humanoid robot. | hardware/simulator version and reset protocol | p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Dataset/benchmark | This allows for better generalization to unseen commands, smoother motion interpolation, and more coherent transitions between behaviors. | role, split, size and leakage | p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 6 (B. Latent Space Analysis), p. 7 (B. Latent Space Analysis) |
| Metric | We begin with an overview and demonstrate diverse motions enabled by our approach. | definition, denominator, direction and uncertainty | p. 5 (IV. EXPERIMENTS), p. 5 (Figure/Table caption), p. 7 (B. Latent Space Analysis) |
| Baseline/ablation | Fig. 9. Latent Space Interpolation: CLIP+CVAE ys. CLIP. Alone ‘Comparison of motion quality when iterpolting between forward and side- ‘ways walking. The CLIPSCVAE model (let) produces smooth and coherent iagonal walking, while ... | fair input/data/compute/action matching | p. 9 (Figure/Table caption), p. 5 (IV. EXPERIMENTS), p. 5 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 3. Robustness to External Disturbances. The humanoid robot demonstrates robust stability while executing a hand-waving motion under exteal perturbations. When subjected to kicks (top ...
- **p. 9 / C. Generalization to Unseen Texts - extractive body cue:** ietepolating between walking (Command 1) and side stepping (Command 2) predoces walking the side, a whole-body masion that does not exist i the
- **p. 7 / C. Generalization to Unseen Texts - extractive body cue:** We find the poticy performs forward motion in a consistent speed and style despite phrasing differences like "move" vs. "walk." demonstrating robustness to linguistic variation
- **p. 7 / C. Generalization to Unseen Texts - extractive body cue:** CLIP encoder handles minor linguistic variations well, it produces significantly different encodings for out-of-distribution commands, which the MLP policy struggles to generalize from.
- **p. 8 / C. Generalization to Unseen Texts - extractive body cue:** Moreover, the robot's movement stays agile and stable, demonstrating the framework's robustness to unseen latent codes,
- **p. 8 / C. Generalization to Unseen Texts - extractive body cue:** ‘dynamics of humanoid motion, achieving smooth and coherent transitions ~ such as running, stopping, and switching to limb ‘movements - within a single policy, without ...
- **p. 9 / C. Generalization to Unseen Texts - extractive body cue:** The quantitative results, summarized in Table Il, indicate that our full framework outperforms all ablation baselines, ‘confirming the contribution of each proposed component to efficient ...

## Why Read It

Locomotion, whole-body, mobile manipulation, and humanoids의 humanoid 문제를 이해하기 위해 읽는다. 본문은 However, transferring these controllers to real-world hardware faces challenges due to the sim-to-real gap.를 문제로 두고, Furthermore, our framework enables smooth transitions between motion clips and generates novel motions through interpolation, demonstrating generalization beyond the training data를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (A. Learning-based Humanoid Whole-body Control), p. 1 (1. Iyrropucrion), p. 1 (Abstract), p. 4 (A. Motion-Tracking Teacher Policy), p. 2 (B. Generative Action Modeling), p. 5 (B. Language-Directed Student Policy) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (15 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** While prior works on language-directed real-world humanoid control have shown success by decoupling the problem into kinematic motion generation and whole-body tracking control [34, 10, 25], this hierarchical approach has ... (p. 1, 1. Iyrropucrion).
- **Actual contribution:** Furthermore, our framework enables smooth transitions between motion clips and generates novel motions through interpolation, demonstrating generalization beyond the training data (p. 2, 1. Iyrropucrion).
- **Evaluation boundary:** We conduct extensive experiments to evaluate our framework for language-directed humanoid whole-body control with 4 Unitree GI humanoid robot. (p. 5, IV. EXPERIMENTS).
- **Explicit failure boundary:** CLIP encoder handles minor linguistic variations well, it produces significantly different encodings for out-of-distribution commands, which the MLP policy struggles to generalize from. (p. 7, C. Generalization to Unseen Texts).
