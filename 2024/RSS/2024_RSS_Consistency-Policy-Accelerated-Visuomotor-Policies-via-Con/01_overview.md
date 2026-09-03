# Consistency Policy: Accelerated Visuomotor Policies via Consistency Distillation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://www.roboticsproceedings.org/rss20/p071.html.
> PDF retrieval source: https://www.roboticsproceedings.org/rss20/p071.html. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / RSS
- Authors: not duplicated here when not verified in the registry source
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: Robotics, visuomotor policy, diffusion policy, consistency distillation, low latency, real-time control
- Official paper: https://www.roboticsproceedings.org/rss20/p071.html
- Full-text retrieval: https://www.roboticsproceedings.org/rss20/p071.html
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

RL, IL, offline learning, and robot data의 robot_data 문제를 이해하기 위해 읽는다. 본문은 1: Both Diffusion and Consistency Policy work by sampling random actions and denoising them into predictions of actions. xt denotes the current action distribution at a time t ∈[0, T], where larger ...를 문제로 두고, Overall, we demonstrate that inference speed of our approach is on average about an order of magnitude faster than the fastest baseline (see Table I) and maintains similar or higher success rates ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Many robotic systems, such as mobile manipulators or quadrotors, cannot be equipped with high-end GPUs due to space, weight, and power constraints.
- **p. 1 / Abstract - extractive body cue:** These constraints prevent these systems from leveraging recent developments in visuomotor policy architectures that require high-end GPUs to achieve fast policy inference.
- **p. 1 / Abstract - extractive body cue:** In this paper, we propose Consistency Policy, a faster and similarly powerful alternative to Diffusion Policy for learning visuomotor robot control.
- **p. 1 / Abstract - extractive body cue:** By virtue of its fast inference speed, Consistency Policy can enable low latency decision making in resource-constrained robotic setups.
- **p. 1 / Abstract - extractive body cue:** A Consistency Policy is distilled from a pretrained Diffusion Policy by enforcing selfconsistency along the Diffusion Policy's learned trajectories.
- **p. 1 / I. INTRODUCTION - extractive body cue:** 1: Both Diffusion and Consistency Policy work by sampling random actions and denoising them into predictions of actions. xt denotes the current action distribution at ...

## Core Idea

- **p. 2 / I. INTRODUCTION - extractive body cue:** Overall, we demonstrate that inference speed of our approach is on average about an order of magnitude faster than the fastest baseline (see Table I) ...
- **p. 4 / 2) Student Model (Consistency Policy) - extractive body cue:** Single-step inference from our trained Consistency Policy works as follows: sample the initial position z ∼N(0, I), compute x = gθ(z, T, 0; o) where ...
- **p. 4 / 2) Student Model (Consistency Policy) - extractive body cue:** [14] propose a training objective to distill a teacher model sϕ(xt, t; o) into a student model gθ(xt, t, s; o) and achieve state of ...
- **p. 3 / 1) Teacher Model (EDM) - extractive body cue:** A trained EDM model takes as input the current position xt and time t along a PFODE, as well as the conditioning o, and is ...
- **p. 5 / 2) Student Model (Consistency Policy) - extractive body cue:** For our student model, we use the same architecture except with expanded FiLM blocks to accomodate conditioning on the stop timestep, s.
- **p. 3 / III. CONSISTENCY POLICY - extractive body cue:** We then describe how to train a Consistency Policy, which requires training a teacher Diffusion Policy and then distilling this teacher model into a Consistency ...
- **p. 5 / 2) Student Model (Consistency Policy) - extractive body cue:** To this end, we also maintain the 1D Convolutional UNet architecture from Diffusion Policy for our teacher model.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The figure shows distributions of predicted action sequences (indicated by the sequences of red to green dots) at different stages of the respective generation process. a) Diffusion Policy denoises an action sequence ... | multi-view observation, language/task label과 action trajectory | p. 1 (I. INTRODUCTION), p. 4 (2) Student Model (Consistency Policy)) |
| State/latent | figure, distributions, predicted, action, sequences, indicated, green, dots, different, stages, respective, generation | shared representation, embodiment/task identity와 data distribution | p. 1 (I. INTRODUCTION), p. 4 (2) Student Model (Consistency Policy)), p. 3 (III. CONSISTENCY POLICY) |
| Output/action | Single-step inference from our trained Consistency Policy works as follows: sample the initial position z ∼N(0, I), compute x = gθ(z, T, 0; o) where T is the max timestep we use ... | dataset sample 또는 learned policy action | p. 4 (2) Student Model (Consistency Policy)), p. 3 (III. CONSISTENCY POLICY), p. 1 (I. INTRODUCTION) |
| Objective/outcome | Following [13], we optimize the Denoising Score Matching (DSM) loss to train the EDM model: LDSM(θ) = Et,x0,xt/x0[d(x0, sϕ (xt, t; o))] (3) The DSM objective takes a sampled point along a ... | coverage, cross-embodiment transfer, data efficiency와 task success | p. 3 (1) Teacher Model (EDM)), p. 4 (2) Student Model (Consistency Policy)), p. 4 (2) Student Model (Consistency Policy)) |

## Main Claims and Actual Contribution

- **p. 2 / I. INTRODUCTION - extractive body cue:** Overall, we demonstrate that inference speed of our approach is on average about an order of magnitude faster than the fastest baseline (see Table I) ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** This divergence can be explained by stochasticity on an easy task: if the first CP generation is already earning .98 success rate, subsequent chaining steps ...
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** Results: Table IV shows how the baseline DDiM-variant of Diffusion Policy achieves similar average success rates as our method on the Rubbish Clean Up and ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** On Robomimic Can, single-step CP actually outperforms 3-step CP and registers a marginal improvement over DDPM.
- **p. 8 / IV. EXPERIMENTS - extractive body cue:** Trash Clean Up Plug Insertion Microwave Success Inference Success Inference Success Rate Rate Time (ms) Rate Time (ms) DDiM 0.8 ± .13 192 0.6 ± ...
- **p. 8 / IV. EXPERIMENTS - extractive body cue:** We suggest that any user wishing to improve performance on a difficult task begin by trying subdivided discretized time and only attempt further hyperparameter tuning ...
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Doing so allows us to directly compare the generation speed and success rates of the baselines versus our own.
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** For success rates, we average over 10 trials for the first and third tasks while we average over 20 trials for the second task.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SIMULATION | do not infer unreported downstream behavior | p. 6 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS) |
| Embodiment/environment | 1) Robomimic: From the robomimic [17] benchmark suite, we evaluate our method on the Lift, Can, Square and Tool Hang tasks, which compromise all the single-robot tasks in Robomimic. | hardware/simulator version and reset protocol | p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Dataset/benchmark | Policy NFE Lift Can Square ToolHang Push-T DDPM 27 1.00 .97 ± .01 .93 ± .02 .79 ± .03 .87 ± .03 DDiM 9 1.00 .82 ± .03 .85 ± .03 .14 ... | role, split, size and leakage | p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |
| Metric | Metrics: The key metric we report in the Robomimic experiments is the average success rate earned by a particular policy network on the given task, along with the standard error of this ... | definition, denominator, direction and uncertainty | p. 6 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 8 (IV. EXPERIMENTS) |
| Baseline/ablation | Thus, we construct an optimistically strong baseline by assuming these speedups can be realized without degrading performance from the standard sequential samplers. | fair input/data/compute/action matching | p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 9 / V. LIMITATIONS - extractive body cue:** In future work, we will explore how we can potentially re-introduce multimodality to Consistency Policy through more complex sampling schemes.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** Single-step CP often falls in between DDPM and DDiM in terms of success rate, especially on the harder tasks such as Square and Tool Hang, ...
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** More discussion about the mobile task in particular is present in Limitations see Sec.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** Note that we are optimistic in assuming that speeding up the baseline DDPM and DDiM Policies [6] with ParaDiGMS [27] does not result in a ...
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: Both Diffusion and Consistency Policy work by sampling random actions and denoising them into predictions of actions. xt denotes the current action distribution ...
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** ParaDiGMS's experiments do not show any degradation in performance when using parallel sampling, but they do assume access to sufficient compute.
- **p. 8 / IV. EXPERIMENTS - extractive body cue:** [14] proposed the non-adjacent CTM objective that enforces consistency between any points t and u denoised down to any s < u < t.

## Why Read It

RL, IL, offline learning, and robot data의 robot_data 문제를 이해하기 위해 읽는다. 본문은 1: Both Diffusion and Consistency Policy work by sampling random actions and denoising them into predictions of actions. xt denotes the current action distribution at a time t ∈[0, T], where larger ...를 문제로 두고, Overall, we demonstrate that inference speed of our approach is on average about an order of magnitude faster than the fastest baseline (see Table I) and maintains similar or higher success rates ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (I. INTRODUCTION), p. 4 (2) Student Model (Consistency Policy)), p. 4 (2) Student Model (Consistency Policy)), p. 3 (1) Teacher Model (EDM)), p. 5 (2) Student Model (Consistency Policy)), p. 3 (III. CONSISTENCY POLICY) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (11 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** However, Consistency Policy still performs well on the Push-T task, suggesting that this lack of multi-modality is not hurting us on the standard evaluation tasks used by related work. (p. 9, V. LIMITATIONS).
- **Actual contribution:** Overall, we demonstrate that inference speed of our approach is on average about an order of magnitude faster than the fastest baseline (see Table I) and maintains similar or higher ... (p. 2, I. INTRODUCTION).
- **Evaluation boundary:** Policy NFE Lift Can Square ToolHang Push-T DDPM 27 1.00 .97 ± .01 .93 ± .02 .79 ± .03 .87 ± .03 DDiM 9 1.00 .82 ± .03 .85 ± ... (p. 6, IV. EXPERIMENTS).
- **Explicit failure boundary:** Differentiating with respect to every operation could lead to unstable training and slow or even failed convergence. (p. 4, 2) Student Model (Consistency Policy)).
