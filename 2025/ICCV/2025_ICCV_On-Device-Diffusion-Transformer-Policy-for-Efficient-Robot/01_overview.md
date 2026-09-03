# On-Device Diffusion Transformer Policy for Efficient Robot Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Wu_On-Device_Diffusion_Transformer_Policy_for_Efficient_Robot_Manipulation_ICCV_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Wu_On-Device_Diffusion_Transformer_Policy_for_Efficient_Robot_Manipulation_ICCV_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: Robotics, Diffusion
- Official paper: https://openaccess.thecvf.com/content/ICCV2025/html/Wu_On-Device_Diffusion_Transformer_Policy_for_Efficient_Robot_Manipulation_ICCV_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/ICCV2025/papers/Wu_On-Device_Diffusion_Transformer_Policy_for_Efficient_Robot_Manipulation_ICCV_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 However, this endeavor presents multifaceted challenges: 1) Diffusion Policies require multiple denoising steps, which slows down the generation process; 2) the standard architectures [8, 36, 37] involve billions of parameters, leading ...를 문제로 두고, In this work, we introduce a novel framework named LightDP for Diffusion Policies that enables models to achieve real-time generation on mobile devices.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Diffusion Policies have significantly advanced robotic manipulation tasks via imitation learning, but their application on resource-constrained mobile platforms remains challenging due to computational inefficiency and ...
- **p. 1 / Abstract - extractive body cue:** In this paper, we propose LightDP, a novel framework specifically designed to accelerate Diffusion Policies for real-time deployment on mobile devices.
- **p. 1 / Abstract - extractive body cue:** LightDP addresses the computational bottleneck through two core strategies: network compression of the denoising modules and reduction of the required sampling steps.
- **p. 1 / Abstract - extractive body cue:** We first conduct an extensive computational analysis on existing Diffusion Policy architectures, identifying the denoising network as the primary contributor to latency.
- **p. 1 / Abstract - extractive body cue:** To overcome performance degradation typically associated with conventional pruning methods, we introduce a unified pruning and retraining pipeline, optimizing the model's postpruning recoverability explicitly.
- **p. 1 / 1. Introduction - extractive body cue:** However, this endeavor presents multifaceted challenges: 1) Diffusion Policies require multiple denoising steps, which slows down the generation process; 2) the standard architectures [8, 36, ...
- **p. 1 / 1. Introduction - extractive body cue:** Through the comprehensive component evaluation, we observe that the denoiser is the major bottleneck for Diffusion Policies (as shown in Table 1).

## Core Idea

- **p. 1 / 1. Introduction - extractive body cue:** In this work, we introduce a novel framework named LightDP for Diffusion Policies that enables models to achieve real-time generation on mobile devices.
- **p. 2 / 1. Introduction - extractive body cue:** Our contributions are summarized as follows: • We present a novel framework for Diffusion Policies to obtain the efficient diffusion transformer that achieves real-time action ...
- **p. 5 / 4.3. Prune the Model by Learning - extractive body cue:** In the left figure, we present the consistency distillation pipeline adopted in our method.
- **p. 5 / 4.3. Prune the Model by Learning - extractive body cue:** In the right figure, we present the prune by learning technique used in our method, where a set of Bernoulli variables (gate score) is learned ...
- **p. 4 / 4.3. Prune the Model by Learning - extractive body cue:** To address this issue, we propose to use a single-stage pruning method [10], where the mask M and weight ˆϕ are jointly optimized to minimize ...
- **p. 3 / 4.1. Problem Formulation - extractive body cue:** A diffusion policy πϕ(a/o, g) is trained to imitate the expert's behavior by maximizing the log-likelihood of the action a Diffusion Transformer Observation Encoder x4 ...
- **p. 4 / 4.3. Prune the Model by Learning - extractive body cue:** To address this, a common approach is a two-stage pruning process: first determine the mask M (by minimizing the loss L with a given criterion), ...
- **p. 5 / 4.3. Prune the Model by Learning - extractive body cue:** Then, two noised actions at and at+k are fed into the Student Model fϕ and the Target Model fϕ⋆to calculate the consistency loss.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | A diffusion policy πϕ(a/o, g) is trained to imitate the expert's behavior by maximizing the log-likelihood of the action a Diffusion Transformer Observation Encoder x4 action Vision Encoder FFN MHCA Transformer Block ... | image/video, language instruction, proprioception과 history | p. 3 (4.1. Problem Formulation), p. 3 (4.1. Problem Formulation) |
| State/latent | diffusion, policy, trained, imitate, expert, behavior, maximizing, log-likelihood, action, Transformer, Observation, Encoder | language-grounded task state와 action-policy context | p. 3 (4.1. Problem Formulation), p. 3 (4.1. Problem Formulation), p. 5 (4.3. Prune the Model by Learning) |
| Output/action | Given the demonstration T , a trajectory τ ∈T is a sequence of observation o and robot action a, denoted as τ = {(o1, a1), ..., (oNτ , aNτ )}. | continuous action, pose 또는 action chunk | p. 3 (4.1. Problem Formulation), p. 5 (4.3. Prune the Model by Learning), p. 4 (4.3. Prune the Model by Learning) |
| Objective/outcome | To address this issue, we propose to use a single-stage pruning method [10], where the mask M and weight ˆϕ are jointly optimized to minimize the loss L after pruning. | instruction following, task success, generalization과 latency | p. 4 (4.3. Prune the Model by Learning), p. 4 (4.3. Prune the Model by Learning), p. 3 (4.1. Problem Formulation) |

## Main Claims and Actual Contribution

- **p. 1 / 1. Introduction - extractive body cue:** In this work, we introduce a novel framework named LightDP for Diffusion Policies that enables models to achieve real-time generation on mobile devices.
- **p. 2 / 1. Introduction - extractive body cue:** Our contributions are summarized as follows: • We present a novel framework for Diffusion Policies to obtain the efficient diffusion transformer that achieves real-time action ...
- **p. 5 / 4.3. Prune the Model by Learning - extractive body cue:** In the left figure, we present the consistency distillation pipeline adopted in our method.
- **p. 5 / 4.3. Prune the Model by Learning - extractive body cue:** In the right figure, we present the prune by learning technique used in our method, where a set of Bernoulli variables (gate score) is learned ...
- **p. 4 / 4.3. Prune the Model by Learning - extractive body cue:** To address this issue, we propose to use a single-stage pruning method [10], where the mask M and weight ˆϕ are jointly optimized to minimize ...
- **p. 6 / 5.3. Evaluation on DiffusionPolicy Transformer - extractive body cue:** The results show that through our method, the pruned model can achieve a comparable success rate with the vanilla model.
- **p. 6 / 5.3. Evaluation on DiffusionPolicy Transformer - extractive body cue:** Especially, we find a 2-layer diffusion transformer can achieve a success rate with 0.724, which is quite close to the original 14078
- **p. 7 / 5.4. Evaluation on MDT-V - extractive body cue:** Similarly, in the D→D scenario, all models register lower performance, with the most compressed model suffering from a steep decline in both success rate and ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 6 (5.3. Evaluation on DiffusionPolicy Transformer), p. 6 (5.3. Evaluation on DiffusionPolicy Transformer) |
| Embodiment/environment | The benchmark dataset is split into four manipulation environments, A, B, C, and D. | hardware/simulator version and reset protocol | p. 6 (5.1. Benchmarks and Evaluation Metrics), p. 8 (5.6. Qualitative Results) |
| Dataset/benchmark | The benchmark comprises 130 tasks across 4 suites: LIBERO-Spatial, LIBEROObject, LIBERO-Goal, LIBERO-100. | role, split, size and leakage | p. 6 (5.1. Benchmarks and Evaluation Metrics), p. 8 (5.6. Qualitative Results), p. 6 (5.1. Benchmarks and Evaluation Metrics), p. 7 (5.4. Evaluation on MDT-V) |
| Metric | And we follow the evaluation protocol adopted in Diffusion Policy [8] to evaluate the success rate of the manipulation task. • CALVIN [30] is a simulation benchmark for measuring the performance of ... | definition, denominator, direction and uncertainty | p. 6 (5.1. Benchmarks and Evaluation Metrics), p. 7 (5.4. Evaluation on MDT-V), p. 6 (5.3. Evaluation on DiffusionPolicy Transformer) |
| Baseline/ablation | Table 2. Performance comparison of LightDP compressed models with varying depth and inference steps. All models are trained on the same Push-T dataset for 3K epochs. DP-T⋆refers to the baseline model evaluated ... | fair input/data/compute/action matching | p. 7 (Figure/Table caption), p. 5 (5. Experiments), p. 5 (5. Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 7 / 5.6. Qualitative Results - extractive body cue:** In the Push-T task, the pruned model successfully pushed the T-shaped block into the goal zone, without any failure in the manipu14079
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 2. The training pipeline of our proposed LightDP. In the left figure, we present the consistency distillation pipeline adopted in our method. The Student ...
- **p. 6 / 5.2. Implementation Details - extractive body cue:** Our consistency distillation is applied to the model's x0 prediction (predicting the denoised action), following common practice, and we start the EMA decay rate at ...

## Why Read It

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 However, this endeavor presents multifaceted challenges: 1) Diffusion Policies require multiple denoising steps, which slows down the generation process; 2) the standard architectures [8, 36, 37] involve billions of parameters, leading ...를 문제로 두고, In this work, we introduce a novel framework named LightDP for Diffusion Policies that enables models to achieve real-time generation on mobile devices.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 1 (1. Introduction), p. 3 (4.1. Problem Formulation), p. 4 (4.3. Prune the Model by Learning), p. 5 (4.3. Prune the Model by Learning), p. 5 (4.3. Prune the Model by Learning) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
