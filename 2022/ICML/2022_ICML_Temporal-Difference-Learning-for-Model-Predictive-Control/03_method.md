# Method - Temporal Difference Learning for Model Predictive Control

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (20 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2203.04955; PDF retrieval source: https://arxiv.org/pdf/2203.04955. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 4 (4. Task-Oriented Latent Dynamics Model), p. 5 (4. Task-Oriented Latent Dynamics Model), p. 4 (4. Task-Oriented Latent Dynamics Model), p. 3 (3. TD-Learning for Model Predictive Control), p. 3 (3. TD-Learning for Model Predictive Control), p. 5 (4. Task-Oriented Latent Dynamics Model)): Our proposed TOLD consists of five learned components hθ, dθ, Rθ, Qθ, πθ that predict the following quantities: Representation: zt = hθ(st) Latent dynamics: zt+1 = dθ(zt, at) Reward: ˆrt ...

## Method Body Digest

- **p. 4 / 4. Task-Oriented Latent Dynamics Model - extractive body cue:** Our proposed TOLD consists of five learned components hθ, dθ, Rθ, Qθ, πθ that predict the following quantities: Representation: zt = hθ(st) Latent dynamics: zt+1 ...
- **p. 5 / 4. Task-Oriented Latent Dynamics Model - extractive body cue:** Instead, we propose to regularize TOLD with a latent state consistency loss (shown in Equation 10) that forces a future latent state prediction zt+1 = ...
- **p. 4 / 4. Task-Oriented Latent Dynamics Model - extractive body cue:** During training, we minimize a temporally weighted objective J (θ; Γ) = t+H X i=t λi-tL(θ; Γi) , (7) where Γ ∼B is a trajectory ...
- **p. 3 / 3. TD-Learning for Model Predictive Control - extractive body cue:** (2015)) control for planning (denoted Πθ), learned models dθ, Rθ of the (latent) dynamics and reward signal, respectively, a terminal state-action value function Qθ, and ...
- **p. 3 / 3. TD-Learning for Model Predictive Control - extractive body cue:** We plan at Algorithm 1 TD-MPC (inference) Require: θ : learned network parameters µ0, σ0: initial parameters for N N, Nπ: num sample/policy trajectories st, ...
- **p. 5 / 4. Task-Oriented Latent Dynamics Model - extractive body cue:** We use an exponential moving average θ-of the online network parameters θ for computing the value target (Lillicrap et al., 2016), and similarly also use ...
- **p. 5 / 4. Task-Oriented Latent Dynamics Model - extractive body cue:** The TD-objective in Equation 9 requires estimating the quantity maxat Qθ-(zt, at), which is extremely costly to compute using planning (Lowrey et al., 2019).
- **p. 5 / 4. Task-Oriented Latent Dynamics Model - extractive body cue:** Therefore, we instead learn a policy πθ that maximizes Qθ by minimizing the objective Jπ(θ; Γ) = - t+H X i=t λi-tQθ(zi, πθ(sg(zi))) , (11) ...

## Design Rationale

- **p. 1 / 1. Introduction - extractive body cue:** (Top) We present a framework for MPC using a task-oriented latent dynamics model and value function learned jointly by temporal difference learning.
- **p. 1 / 1. Introduction - extractive body cue:** (Bottom) Episode return of our method, SAC, and MPC with a ground-truth simulator on challenging, highdimensional Humanoid and Dog tasks (Tassa et al., 2018).
- **p. 2 / 1. Introduction - extractive body cue:** Lastly, we propose a modality-agnostic prediction loss in latent space that enforces temporal consistency in the learned representation without explicit state or image prediction.

## Source Evidence Cues

- **p. 4 / 4. Task-Oriented Latent Dynamics Model - extractive body cue:** Our proposed TOLD consists of five learned components hθ, dθ, Rθ, Qθ, πθ that predict the following quantities: Representation: zt = hθ(st) Latent dynamics: zt+1 ...
- **p. 5 / 4. Task-Oriented Latent Dynamics Model - extractive body cue:** Instead, we propose to regularize TOLD with a latent state consistency loss (shown in Equation 10) that forces a future latent state prediction zt+1 = ...
- **p. 4 / 4. Task-Oriented Latent Dynamics Model - extractive body cue:** During training, we minimize a temporally weighted objective J (θ; Γ) = t+H X i=t λi-tL(θ; Γi) , (7) where Γ ∼B is a trajectory ...
- **p. 3 / 3. TD-Learning for Model Predictive Control - extractive body cue:** (2015)) control for planning (denoted Πθ), learned models dθ, Rθ of the (latent) dynamics and reward signal, respectively, a terminal state-action value function Qθ, and ...
- **p. 3 / 3. TD-Learning for Model Predictive Control - extractive body cue:** We plan at Algorithm 1 TD-MPC (inference) Require: θ : learned network parameters µ0, σ0: initial parameters for N N, Nπ: num sample/policy trajectories st, ...
- **p. 5 / 4. Task-Oriented Latent Dynamics Model - extractive body cue:** We use an exponential moving average θ-of the online network parameters θ for computing the value target (Lillicrap et al., 2016), and similarly also use ...
- **Detected method headings:** 3. TD-Learning for Model Predictive Control (p. 3); 4. Task-Oriented Latent Dynamics Model (p. 4)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Risk / failure representation | unsafe state와 uncertainty를 계산한다 | observation, nominal command, history | barrier, risk model, failure classifier, uncertainty 또는 safe set을 추정 | risk/margin/failure state | Our proposed TOLD consists of five learned components hθ, dθ, Rθ, Qθ, πθ that predict the following quantities: Representation: zt = hθ(st) ... | p. 4 (4. Task-Oriented Latent Dynamics Model), p. 5 (4. Task-Oriented Latent Dynamics Model) |
| Filtering / recovery | nominal command를 안전 command로 바꾼다 | nominal action과 safety constraint | QP shield, backup policy, correction, stop 또는 recovery plan을 선택 | safe/recovery action | Instead, we propose to regularize TOLD with a latent state consistency loss (shown in Equation 10) that forces a future latent state ... | p. 5 (4. Task-Oriented Latent Dynamics Model), p. 4 (4. Task-Oriented Latent Dynamics Model) |
| Monitoring / re-entry | 실행 결과를 다시 risk decision에 반영한다 | executed action과 next observation | threshold, update, replan, abort 또는 return-to-task를 수행 | continue/correct/abort state | During training, we minimize a temporally weighted objective J (θ; Γ) = t+H X i=t λi-tL(θ; Γi) , (7) where Γ ∼B ... | p. 4 (4. Task-Oriented Latent Dynamics Model), p. 3 (3. TD-Learning for Model Predictive Control) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 4. Task-Oriented Latent Dynamics Model - extractive body cue:** During training, we minimize a temporally weighted objective J (θ; Γ) = t+H X i=t λi-tL(θ; Γi) , (7) where Γ ∼B is a trajectory ...
- **p. 5 / 4. Task-Oriented Latent Dynamics Model - extractive body cue:** The TD-objective in Equation 9 requires estimating the quantity maxat Qθ-(zt, at), which is extremely costly to compute using planning (Lowrey et al., 2019).
- **p. 5 / 4. Task-Oriented Latent Dynamics Model - extractive body cue:** Therefore, we instead learn a policy πθ that maximizes Qθ by minimizing the objective Jπ(θ; Γ) = - t+H X i=t λi-tQθ(zi, πθ(sg(zi))) , (11) ...
- **p. 3 / 3. TD-Learning for Model Predictive Control - extractive body cue:** H from N(µj-1, (σj-1)2I) 4: Sample Nπ traj. of length H using πθ, dθ // Estimate trajectory returns φΓ using dθ, Rθ, Qθ, starting from ...
- **p. 4 / 4. Task-Oriented Latent Dynamics Model - extractive body cue:** Then, TOLD recurrently predicts the following latent states z1, z2, . . . , zH, as well as a value ˆq, reward ˆr, and action ...
- **p. 3 / 3. TD-Learning for Model Predictive Control - extractive body cue:** (2015)) control for planning (denoted Πθ), learned models dθ, Rθ of the (latent) dynamics and reward signal, respectively, a terminal state-action value function Qθ, and ...
- **Formal bridge:** state/history and risk h(s) -> filtered/recovery action u_safe -> task utility subject to safety constraint -> low violation/failure probability with useful intervention.
- **Equation/algorithm anchors:** p. 4 (4. Task-Oriented Latent Dynamics Model), p. 5 (4. Task-Oriented Latent Dynamics Model), p. 5 (4. Task-Oriented Latent Dynamics Model), p. 3 (3. TD-Learning for Model Predictive Control), p. 3 (3. TD-Learning for Model Predictive Control), p. 4 (4. Task-Oriented Latent Dynamics Model).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | control, planning, denoted, learned, models, latent, dynamics, reward, signal, respectively, terminal, state-action, value, function | observation, uncertainty/risk estimate와 task command | body cue; exact tensor/frame verify |
| State/latent | control, planning, denoted, learned, models, latent, dynamics, reward, signal, respectively | safe set, recovery state 또는 constraint margin | body cue; notation verify |
| Action/output | Top, present, framework, MPC, task-oriented, latent, dynamics, model, value, function | shielded, recovery 또는 safe action | body cue; unit/decoder verify |
| Objective/constraint | During, training, minimize, temporally, weighted, objective, i-tL, where, trajectory, sampled | task utility subject to safety constraint | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 3. TD-Learning for Model Predictive Control - extractive body cue:** (2015)) control for planning (denoted Πθ), learned models dθ, Rθ of the (latent) dynamics and reward signal, respectively, a terminal state-action value function Qθ, and ...
- **p. 3 / 3. TD-Learning for Model Predictive Control - extractive body cue:** H from N(µj-1, (σj-1)2I) 4: Sample Nπ traj. of length H using πθ, dθ // Estimate trajectory returns φΓ using dθ, Rθ, Qθ, starting from ...
- **p. 5 / 4. Task-Oriented Latent Dynamics Model - extractive body cue:** Instead, we propose to regularize TOLD with a latent state consistency loss (shown in Equation 10) that forces a future latent state prediction zt+1 = ...
- **p. 2 / 2. Preliminaries - extractive body cue:** We aim to learn a parameterized mapping Πθ : S 7→A with parameters θ such that discounted return EΓ∼Πθ[P∞ t=1 γtrt], rt ∼R(·/st, at) is ...
- **p. 2 / 2. Preliminaries - extractive body cue:** Model-free TD-learning algorithms aim to estimate an optimal state-action value function Q∗: S × A 7→ R using a parametric value function Qθ(s, a) ≈ ...
- **p. 4 / 4. Task-Oriented Latent Dynamics Model - extractive body cue:** Our proposed TOLD consists of five learned components hθ, dθ, Rθ, Qθ, πθ that predict the following quantities: Representation: zt = hθ(st) Latent dynamics: zt+1 ...
- **p. 5 / 4. Task-Oriented Latent Dynamics Model - extractive body cue:** This is in contrast to prior work on model-based learning that learn a model by state or video prediction, entirely decoupled from policy and/or value ...
- **Normalized interface:** observation=observation, uncertainty/risk estimate와 task command; state=safe set, recovery state 또는 constraint margin; output/action=shielded, recovery 또는 safe action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | 현재 command의 one-step safety 또는 recovery trajectory horizon; exact lookahead 확인 필요. | Secondly, we back-propagate gradients from the reward and TD-objective through multiple rollout steps of the model, improving reward and value predictions over ... | episode/sequence/action-chunk boundary |
| Rate / latency | nominal policy와 safety monitor/filter의 runtime rate를 별도로 기록한다. | (2018)) and Algorithm 2 TOLD (training) Require: θ, θ-: randomly initialized network parameters η, τ, λ, B: learning rate, coefficients, buffer 1: ... | Hz/fps, inference time and control rate |
| Memory | risk score, recent trajectory/history와 recovery state. | not recovered | window and reset |
| Compute | risk inference, barrier/QP solve 또는 backup policy selection이 latency를 결정한다. | TD-Learning for MPC 0 250 500 750 1000 Episode return Average 0 100 200 300 400 Acrobot Swingup 0 250 500 750 ... | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / 4. Task-Oriented Latent Dynamics Model - extractive body cue:** During training, we minimize a temporally weighted objective J (θ; Γ) = t+H X i=t λi-tL(θ; Γi) , (7) where Γ ∼B is a trajectory ...
- **p. 3 / 3. TD-Learning for Model Predictive Control - extractive body cue:** We plan at Algorithm 1 TD-MPC (inference) Require: θ : learned network parameters µ0, σ0: initial parameters for N N, Nπ: num sample/policy trajectories st, ...
- **p. 5 / 4. Task-Oriented Latent Dynamics Model - extractive body cue:** We use an exponential moving average θ-of the online network parameters θ for computing the value target (Lillicrap et al., 2016), and similarly also use ...
- **p. 5 / 5. Experiments - extractive body cue:** (2018)) and Algorithm 2 TOLD (training) Require: θ, θ-: randomly initialized network parameters η, τ, λ, B: learning rate, coefficients, buffer 1: while not tired ...
- **p. 9 / 5. Experiments - extractive body cue:** We provide additional experiments on inference times in Appendix H.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** TOLD, consists, five, learned, components, predict, following, quantities, Representation, Latent, dynamics, Reward, Value, Policy, Given, observation, observed, time, network, encodes.
- **Relevant PDF headings:** 3. TD-Learning for Model Predictive Control (p. 3); 4. Task-Oriented Latent Dynamics Model (p. 4).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Risk / failure representation | TD-Learning for MPC 0 250 500 750 1000 Episode return Average 0 100 200 300 400 Acrobot Swingup 0 250 500 750 ... | p. 6 (5. Experiments), p. 7 (5. Experiments) |
| Filtering / recovery | Figure 4. Learning from pixels. Return of our method (TD-MPC) and state-of-the-art algorithms on 12 challenging image-based DMControl tasks. We follow prior ... | p. 7 (Figure/Table caption), p. 8 (5. Experiments) |
| Monitoring / re-entry | Figure 14. Individual Meta-World tasks. Success rate of our method (TD-MPC) and SAC on diverse manipulation tasks from Meta- World (Yu et ... | p. 19 (Figure/Table caption), p. 17 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 6 / 5. Experiments - extractive body cue:** We consider: (i) our method implemented using a state predictor (hθ being the identity function), (ii) our method implemented without the latent consistency loss from ...
- **p. 6 / 5. Experiments - extractive body cue:** All three methods learn a model using a reconstruction loss, and select actions using either MPC or a learned policy. -MuZero (Schrittwieser et al., 2020) ...
- **p. 8 / 5. Experiments - extractive body cue:** However, we also observe that we can reduce the planning cost during inference by 50% (compared to during training) without a drop in performance by ...
- **p. 12 / Figure/Table caption - extractive body cue:** Figure 7. Model generalization. Return of our method under three different settings: (Rand. init) TD-MPC trained from scratch on the two Run tasks; (Finetune) TD-MPC ...
- **p. 15 / Figure/Table caption - extractive body cue:** Figure 10. Latent dynamics objective. Return of our method (TD-MPC) using different latent dynamics objectives in addition to reward and value prediction. 15 state-based continuous ...
- **p. 5 / 5. Experiments - extractive body cue:** All components are deterministic and implemented using MLPs.
- **p. 13 / Figure/Table caption - extractive body cue:** Table 3. Comparison to prior work. We compare key components of TD-MPC to prior model-based and model-free approaches. Model objective describes which objective is used ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (4. Task-Oriented Latent Dynamics Model), p. 5 (4. Task-Oriented Latent Dynamics Model), p. 4 (4. Task-Oriented Latent Dynamics Model), p. 3 (3. TD-Learning for Model Predictive Control), p. 3 (3. TD-Learning for Model Predictive Control), p. 5 (4. Task-Oriented Latent Dynamics Model), objective p. 4 (4. Task-Oriented Latent Dynamics Model), p. 5 (4. Task-Oriented Latent Dynamics Model), p. 5 (4. Task-Oriented Latent Dynamics Model), p. 3 (3. TD-Learning for Model Predictive Control), p. 4 (4. Task-Oriented Latent Dynamics Model), p. 3 (3. TD-Learning for Model Predictive Control), temporal p. 2 (1. Introduction), p. 5 (5. Experiments), p. 6 (5. Experiments), p. 8 (5. Experiments), p. 8 (5. Experiments), p. 3 (3. TD-Learning for Model Predictive Control).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
