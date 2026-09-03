# Method - Unified Video Action Model

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (13 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p074.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p074.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 4 (C. Decoupled Video and Action Diffusions), p. 4 (C. Decoupled Video and Action Diffusions), p. 5 (C. Decoupled Video and Action Diffusions), p. 5 (C. Decoupled Video and Action Diffusions), p. 8 (VII. UVA As A FORWARD DYNAMICS MODEL), p. 8 (VII. UVA As A FORWARD DYNAMICS MODEL)): Previous video generation-based policy learning methods rely on hierarchically generating videos first and then predicting actions, leading to slow speed and accumulated errors. ‘To address this, we propose decoupling video ...

## Method Body Digest

- **p. 4 / C. Decoupled Video and Action Diffusions - extractive body cue:** Previous video generation-based policy learning methods rely on hierarchically generating videos first and then predicting actions, leading to slow speed and accumulated errors. ‘To address ...
- **p. 4 / C. Decoupled Video and Action Diffusions - extractive body cue:** Instead of training the model solely on the task of predicting future observations and actions based on historical data, we propose a masked training approach ...
- **p. 5 / C. Decoupled Video and Action Diffusions - extractive body cue:** This masked training strategy enables the model to perform a diverse range of functions, including acting as a robot policy, video ‘model, forward and inverse ...
- **p. 5 / C. Decoupled Video and Action Diffusions - extractive body cue:** For instance, when given only image ‘observations, the model can function as an inverse dynamics ‘model to generate action labels from videos.
- **p. 8 / VII. UVA As A FORWARD DYNAMICS MODEL - extractive body cue:** it to guide the behavior of a pretrained policy model, such as the DP-C.
- **p. 8 / VII. UVA As A FORWARD DYNAMICS MODEL - extractive body cue:** Our model can perform forward dynamics predictions O41 = fiorars(O;, Ax).
- **p. 4 / C. Decoupled Video and Action Diffusions - extractive body cue:** Similarly, the video diffusion loss is defined as
- **p. 5 / V. UVA As PoLicy - extractive body cue:** For realworld tasks, fo minimize evaluation bias, all evaluations use public benchmarks with released datasets-no additional training data were collected,

## Design Rationale

- **p. 1 / 1. Iyrropucrion - extractive body cue:** ‘To address these limitations, we propose UVA, « Unified Video and Action Mode! designed to simultaneously model videos and actions - capturing the underlying interactions ...
- **p. 2 / 1. Iyrropucrion - extractive body cue:** At inference, this decoupling allows the system to bypass video generation entirely, directly utilizing the latent representation for fast action prediction, This design enables real-time ...
- **p. 1 / 1. Iyrropucrion - extractive body cue:** We propose the following three design choices to achieve this:

## Source Evidence Cues

- **p. 4 / C. Decoupled Video and Action Diffusions - extractive body cue:** Previous video generation-based policy learning methods rely on hierarchically generating videos first and then predicting actions, leading to slow speed and accumulated errors. ‘To address ...
- **p. 4 / C. Decoupled Video and Action Diffusions - extractive body cue:** Instead of training the model solely on the task of predicting future observations and actions based on historical data, we propose a masked training approach ...
- **p. 5 / C. Decoupled Video and Action Diffusions - extractive body cue:** This masked training strategy enables the model to perform a diverse range of functions, including acting as a robot policy, video ‘model, forward and inverse ...
- **p. 5 / C. Decoupled Video and Action Diffusions - extractive body cue:** For instance, when given only image ‘observations, the model can function as an inverse dynamics ‘model to generate action labels from videos.
- **p. 8 / VII. UVA As A FORWARD DYNAMICS MODEL - extractive body cue:** it to guide the behavior of a pretrained policy model, such as the DP-C.
- **p. 8 / VII. UVA As A FORWARD DYNAMICS MODEL - extractive body cue:** Our model can perform forward dynamics predictions O41 = fiorars(O;, Ax).
- **Detected method headings:** V. UVA As PoLicy (p. 5); VII. UVA As A FORWARD DYNAMICS MODEL (p. 8)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Risk / failure representation | unsafe state와 uncertainty를 계산한다 | observation, nominal command, history | barrier, risk model, failure classifier, uncertainty 또는 safe set을 추정 | risk/margin/failure state | Previous video generation-based policy learning methods rely on hierarchically generating videos first and then predicting actions, leading to slow speed and accumulated ... | p. 4 (C. Decoupled Video and Action Diffusions), p. 4 (C. Decoupled Video and Action Diffusions) |
| Filtering / recovery | nominal command를 안전 command로 바꾼다 | nominal action과 safety constraint | QP shield, backup policy, correction, stop 또는 recovery plan을 선택 | safe/recovery action | Instead of training the model solely on the task of predicting future observations and actions based on historical data, we propose a ... | p. 4 (C. Decoupled Video and Action Diffusions), p. 5 (C. Decoupled Video and Action Diffusions) |
| Monitoring / re-entry | 실행 결과를 다시 risk decision에 반영한다 | executed action과 next observation | threshold, update, replan, abort 또는 return-to-task를 수행 | continue/correct/abort state | This masked training strategy enables the model to perform a diverse range of functions, including acting as a robot policy, video ‘model, ... | p. 5 (C. Decoupled Video and Action Diffusions), p. 5 (C. Decoupled Video and Action Diffusions) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / C. Decoupled Video and Action Diffusions - extractive body cue:** Masked Training with Flexible Objectives
- **p. 4 / C. Decoupled Video and Action Diffusions - extractive body cue:** Similarly, the video diffusion loss is defined as
- **p. 5 / V. UVA As PoLicy - extractive body cue:** For realworld tasks, fo minimize evaluation bias, all evaluations use public benchmarks with released datasets-no additional training data were collected,
- **p. 5 / C. Decoupled Video and Action Diffusions - extractive body cue:** Unused components are masked and replaced with a learned mask token. ‘The action loss and video loss are selectively applied to supervise the model depending ...
- **Formal bridge:** state/history and risk h(s) -> filtered/recovery action u_safe -> task utility subject to safety constraint -> low violation/failure probability with useful intervention.
- **Equation/algorithm anchors:** p. 4 (C. Decoupled Video and Action Diffusions), p. 4 (C. Decoupled Video and Action Diffusions), p. 5 (C. Decoupled Video and Action Diffusions).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Mask, Training, Flexibility, ability, predict, videos, actions, through, unified, representations, further, unlocks, potential, perform | observation, uncertainty/risk estimate와 task command | body cue; exact tensor/frame verify |
| State/latent | Mask, Training, Flexibility, ability, predict, videos, actions, through, unified, representations | safe set, recovery state 또는 constraint margin | body cue; notation verify |
| Action/output | address, limitations, UVA, Unified, Video, Action, Mode, designed, simultaneously, model | shielded, recovery 또는 safe action | body cue; unit/decoder verify |
| Objective/constraint | Masked, Training, Flexible, Objectives, Similarly, video, diffusion, loss, defined, realworld | task utility subject to safety constraint | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1. Iyrropucrion - extractive body cue:** 3) Mask Training for Flexibility: The ability to predict both videos and actions through unified representations further unlocks the potential to perform a diverse set ...
- **p. 3 / 1. Iyrropucrion - extractive body cue:** Problem Statement: Given a sequence of image observations {Ocners---sOr} and action chunks {Ar-n,.-..Aea}e where his the history horizon, our goal is to predict the future ...
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** (b) By leveraging masked taining, UVA supports flexible input-output ‘combinations for actions and videos.
- **p. 2 / 1. Iyrropucrion - extractive body cue:** In [24], a video diffusion model is fine-tuned ‘on robotics tasks, with the latent representations from the pre~ dicted videos serving as inputs to a ...
- **p. 3 / 1. Iyrropucrion - extractive body cue:** We first introduce the model with complete video and action inputs and outputs (SIII-A-SII-C).
- **p. 4 / C. Decoupled Video and Action Diffusions - extractive body cue:** Previous video generation-based policy learning methods rely on hierarchically generating videos first and then predicting actions, leading to slow speed and accumulated errors. ‘To address ...
- **p. 5 / C. Decoupled Video and Action Diffusions - extractive body cue:** For instance, when given only image ‘observations, the model can function as an inverse dynamics ‘model to generate action labels from videos.
- **Normalized interface:** observation=observation, uncertainty/risk estimate와 task command; state=safe set, recovery state 또는 constraint margin; output/action=shielded, recovery 또는 safe action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | 현재 command의 one-step safety 또는 recovery trajectory horizon; exact lookahead 확인 필요. | Latents from /h different time steps are then temporally concatenated with latent representations from other time steps to produce a NV x ... | episode/sequence/action-chunk boundary |
| Rate / latency | nominal policy와 safety monitor/filter의 runtime rate를 별도로 기록한다. | Problem Statement: Given a sequence of image observations {Ocners---sOr} and action chunks {Ar-n,.-..Aea}e where his the history horizon, our goal is to ... | Hz/fps, inference time and control rate |
| Memory | risk score, recent trajectory/history와 recovery state. | Problem Statement: Given a sequence of image observations {Ocners---sOr} and action chunks {Ar-n,.-..Aea}e where his the history horizon, our goal is to ... | window and reset |
| Compute | risk inference, barrier/QP solve 또는 backup policy selection이 latency를 결정한다. | For DPC and DP-T, we follow their original implementations and also perform denoising over 100 steps. | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / C. Decoupled Video and Action Diffusions - extractive body cue:** Previous video generation-based policy learning methods rely on hierarchically generating videos first and then predicting actions, leading to slow speed and accumulated errors. ‘To address ...
- **p. 4 / C. Decoupled Video and Action Diffusions - extractive body cue:** Instead of training the model solely on the task of predicting future observations and actions based on historical data, we propose a masked training approach ...
- **p. 5 / C. Decoupled Video and Action Diffusions - extractive body cue:** This masked training strategy enables the model to perform a diverse range of functions, including acting as a robot policy, video ‘model, forward and inverse ...
- **p. 8 / VII. UVA As A FORWARD DYNAMICS MODEL - extractive body cue:** it to guide the behavior of a pretrained policy model, such as the DP-C.
- **p. 5 / A. Simulation Benchmarks - extractive body cue:** OpenVLA infers fone action ata time, so itis run 8 times to match the inference time for 8 executed actions.
- **p. 4 / C. Decoupled Video and Action Diffusions - extractive body cue:** This design preserves the generative strengths of diffusion models while significantly reducing inference time.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Previous, video, generation-based, policy, learning, methods, rely, hierarchically, generating, videos, first, then, predicting, actions, leading, slow, speed, accumulated, errors, address.
- **Relevant PDF headings:** V. UVA As PoLicy (p. 5); VII. UVA As A FORWARD DYNAMICS MODEL (p. 8).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Risk / failure representation | Trained on a diverse dataset spanning multiple robot embodiments and tasks, xo demonstrates. strong zero-shot and fine-tuned performance. | p. 6 (B. Real-world Benchmarks), p. 5 (B. Real-world Benchmarks) |
| Filtering / recovery | This evaluation aims to compare ‘our method with a strong baseline in prior works by replicating 4 similar evaluation setup. | p. 7 (B. Real-world Benchmarks), p. 6 (B. Real-world Benchmarks) |
| Monitoring / re-entry | For example, with changes in goal color, UniPi achieves a success rate of 40%, UVA achieves 64%, while OpenVLA only reaches 32%. | p. 8 (B. Real-world Benchmarks), p. 8 (B. Real-world Benchmarks) |

## Failure and Ablation Link

- **p. 8 / B. Real-world Benchmarks - extractive body cue:** This highlights the better potential of UVA for tasks that require reasoning over extended temporal contexts, Effect of Joint Video-Action Modeling: We evaluate this by ...
- **p. 5 / B. Real-world Benchmarks - extractive body cue:** Training Data: We use two publicly available datasets introduced by [11] and [29] without collecting any additional training data.
- **p. 6 / B. Real-world Benchmarks - extractive body cue:** + UVA-action is an ablation of UVA, where the video generation part is excluded, and the model is trained solely as a policy model.
- **p. 7 / B. Real-world Benchmarks - extractive body cue:** Its visual understanding could be enhanced by training on additional video data without action labels.
- **p. 7 / B. Real-world Benchmarks - extractive body cue:** We noticed that the dataset contains extensive recovery data from the moments of failure to correct the policy. ‘This data is particularly useful for models ...
- **p. 6 / B. Real-world Benchmarks - extractive body cue:** Trained on a diverse dataset spanning multiple robot embodiments and tasks, xo demonstrates. strong zero-shot and fine-tuned performance.
- **p. 10 / IX. Discussion - extractive body cue:** Limitation and Future Work: One limitation of our frame- ‘work is that it does not currently leverage large amounts of actionless video data, which could ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (C. Decoupled Video and Action Diffusions), p. 4 (C. Decoupled Video and Action Diffusions), p. 5 (C. Decoupled Video and Action Diffusions), p. 5 (C. Decoupled Video and Action Diffusions), p. 8 (VII. UVA As A FORWARD DYNAMICS MODEL), p. 8 (VII. UVA As A FORWARD DYNAMICS MODEL), objective p. 4 (C. Decoupled Video and Action Diffusions), p. 4 (C. Decoupled Video and Action Diffusions), p. 5 (V. UVA As PoLicy), p. 5 (C. Decoupled Video and Action Diffusions), temporal p. 4 (B. Masked Autoencoder for Observation Prediction), p. 3 (1. Iyrropucrion), p. 4 (C. Decoupled Video and Action Diffusions), p. 3 (1. Iyrropucrion), p. 7 (B. Real-world Benchmarks), p. 7 (B. Real-world Benchmarks).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (13 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** 3) Mask Training for Flexibility: The ability to predict both videos and actions through unified representations further unlocks the potential to perform a diverse set of functions using masked training, ... (p. 2, 1. Iyrropucrion).
- **Objective/update evidence:** Masked Training with Flexible Objectives (p. 4, C. Decoupled Video and Action Diffusions).
- **Temporal/runtime evidence:** Problem Statement: Given a sequence of image observations {Ocners---sOr} and action chunks {Ar-n,.-..Aea}e where his the history horizon, our goal is to predict the future actions {Ay,...,As.,*-1} and observations {Opcis..-,Orsne}s ... (p. 3, 1. Iyrropucrion).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
