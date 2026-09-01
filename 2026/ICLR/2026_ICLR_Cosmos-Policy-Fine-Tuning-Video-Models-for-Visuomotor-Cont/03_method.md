# Method - Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (22 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://iclr.cc/virtual/2026/poster/10006732; PDF retrieval source: https://arxiv.org/pdf/2601.16163. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 17 (A.2.2 LIBERO TRAINING DETAILS), p. 21 (A.4.2 COSMOS POLICY INFERENCE LATENCY), p. 16 (A.2.1 COSMOS POLICY NOISE DISTRIBUTION), p. 17 (A.2.2 LIBERO TRAINING DETAILS), p. 16 (A.2.1 COSMOS POLICY NOISE DISTRIBUTION), p. 15 (A.1 LATENT INJECTION IMPLEMENTATION DETAILS)): (Note that these are single-step training losses given varying σ (noise levels) as input, rather than losses on generations from the multi-step diffusion sampling used during policy inference.) The magnitudes ...

## Method Body Digest

- **p. 17 / A.2.2 LIBERO TRAINING DETAILS - extractive PDF cue:** (Note that these are single-step training losses given varying σ (noise levels) as input, rather than losses on generations from the multi-step diffusion sampling used ...
- **p. 21 / A.4.2 COSMOS POLICY INFERENCE LATENCY - extractive PDF cue:** Cosmos Policy first generates N candidate action chunks with 10 denoising steps each, then generates an ensemble of 3 future state predictions per action proposal ...
- **p. 16 / A.2.1 COSMOS POLICY NOISE DISTRIBUTION - extractive PDF cue:** This higher lower bound empirically improves prediction accuracy at inference time for actions, future states, and values, as measured by lower L1 loss on training ...
- **p. 17 / A.2.2 LIBERO TRAINING DETAILS - extractive PDF cue:** After 40K gradient steps, the policy's action L1 training loss is 0.012, future proprio L1 training loss is 0.007, future wrist image latent L1 training ...
- **p. 16 / A.2.1 COSMOS POLICY NOISE DISTRIBUTION - extractive PDF cue:** Therefore, to ensure that current timestep observations and future timestep observations have similarly structured latent representations, we place them after the blank first latent frame ...
- **p. 15 / A.1 LATENT INJECTION IMPLEMENTATION DETAILS - extractive PDF cue:** We first normalize each action dimension to [-1, +1], and then flatten the array into a (K × dact) vector.
- **p. 22 / A.4.2 COSMOS POLICY INFERENCE LATENCY - extractive PDF cue:** (4) Adding to the prior ablation, we ablate both the future state and value targets when training the policy, thus training a barebones policy that ...
- **p. 17 / A.2.4 ALOHA TRAINING DETAILS - extractive PDF cue:** We train for this seemingly large number of gradient steps across all methods because we observe that training loss continues to decrease and task execution ...

## Design Rationale

- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** We evaluate our method in two modes: first as a direct policy (without planning) and then with model-based planning using the future state and value ...
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** This search process produces trajectories that are more likely to succeed at the task Our main contribution is the Cosmos Policy approach for fine-tuning pretrained ...
- **p. 4 / 3 PRELIMINARIES - extractive PDF cue:** Rather than designing new model components or making architectural modifications as done in prior works, we propose to encode additional modalities as new latent frames ...

## Source Evidence Cues

- **p. 17 / A.2.2 LIBERO TRAINING DETAILS - extractive PDF cue:** (Note that these are single-step training losses given varying σ (noise levels) as input, rather than losses on generations from the multi-step diffusion sampling used ...
- **p. 21 / A.4.2 COSMOS POLICY INFERENCE LATENCY - extractive PDF cue:** Cosmos Policy first generates N candidate action chunks with 10 denoising steps each, then generates an ensemble of 3 future state predictions per action proposal ...
- **p. 16 / A.2.1 COSMOS POLICY NOISE DISTRIBUTION - extractive PDF cue:** This higher lower bound empirically improves prediction accuracy at inference time for actions, future states, and values, as measured by lower L1 loss on training ...
- **p. 17 / A.2.2 LIBERO TRAINING DETAILS - extractive PDF cue:** After 40K gradient steps, the policy's action L1 training loss is 0.012, future proprio L1 training loss is 0.007, future wrist image latent L1 training ...
- **p. 16 / A.2.1 COSMOS POLICY NOISE DISTRIBUTION - extractive PDF cue:** Therefore, to ensure that current timestep observations and future timestep observations have similarly structured latent representations, we place them after the blank first latent frame ...
- **p. 15 / A.1 LATENT INJECTION IMPLEMENTATION DETAILS - extractive PDF cue:** We first normalize each action dimension to [-1, +1], and then flatten the array into a (K × dact) vector.
- **p. 22 / A.4.2 COSMOS POLICY INFERENCE LATENCY - extractive PDF cue:** (4) Adding to the prior ablation, we ablate both the future state and value targets when training the policy, thus training a barebones policy that ...
- **Detected method headings:** A.2.1 COSMOS POLICY NOISE DISTRIBUTION (p. 15); A.3.1 GENERAL COSMOS POLICY EVALUATION DETAILS (p. 17); A.4.2 COSMOS POLICY INFERENCE LATENCY (p. 21)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Risk / failure representation | unsafe state와 uncertainty를 계산한다 | observation, nominal command, history | barrier, risk model, failure classifier, uncertainty 또는 safe set을 추정 | risk/margin/failure state | (Note that these are single-step training losses given varying σ (noise levels) as input, rather than losses on generations from the multi-step ... | p. 17 (A.2.2 LIBERO TRAINING DETAILS), p. 21 (A.4.2 COSMOS POLICY INFERENCE LATENCY) |
| Filtering / recovery | nominal command를 안전 command로 바꾼다 | nominal action과 safety constraint | QP shield, backup policy, correction, stop 또는 recovery plan을 선택 | safe/recovery action | Cosmos Policy first generates N candidate action chunks with 10 denoising steps each, then generates an ensemble of 3 future state predictions ... | p. 21 (A.4.2 COSMOS POLICY INFERENCE LATENCY), p. 16 (A.2.1 COSMOS POLICY NOISE DISTRIBUTION) |
| Monitoring / re-entry | 실행 결과를 다시 risk decision에 반영한다 | executed action과 next observation | threshold, update, replan, abort 또는 return-to-task를 수행 | continue/correct/abort state | This higher lower bound empirically improves prediction accuracy at inference time for actions, future states, and values, as measured by lower L1 ... | p. 16 (A.2.1 COSMOS POLICY NOISE DISTRIBUTION), p. 17 (A.2.2 LIBERO TRAINING DETAILS) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 17 / A.2.2 LIBERO TRAINING DETAILS - extractive PDF cue:** After 40K gradient steps, the policy's action L1 training loss is 0.012, future proprio L1 training loss is 0.007, future wrist image latent L1 training ...
- **p. 17 / A.2.4 ALOHA TRAINING DETAILS - extractive PDF cue:** We train for this seemingly large number of gradient steps across all methods because we observe that training loss continues to decrease and task execution ...
- **p. 16 / A.2.1 COSMOS POLICY NOISE DISTRIBUTION - extractive PDF cue:** This higher lower bound empirically improves prediction accuracy at inference time for actions, future states, and values, as measured by lower L1 loss on training ...
- **p. 22 / A.4.2 COSMOS POLICY INFERENCE LATENCY - extractive PDF cue:** Top: We ablate individual components of the joint objectives training scheme and auxiliary supervision discussed in Section 4.2 and visualized in Figure 12.
- **p. 15 / A.2.1 COSMOS POLICY NOISE DISTRIBUTION - extractive PDF cue:** For action generation, we observe that the low weight on higher noise levels causes inaccurate action predictions during sampling.
- **p. 16 / A.2.1 COSMOS POLICY NOISE DISTRIBUTION - extractive PDF cue:** We find this empirically improves action prediction accuracy and overall success rate.
- **Formal bridge:** state/history and risk h(s) -> filtered/recovery action u_safe -> task utility subject to safety constraint -> low violation/failure probability with useful intervention.
- **Equation/algorithm anchors:** p. 17 (A.2.4 ALOHA TRAINING DETAILS), p. 17 (A.2.2 LIBERO TRAINING DETAILS), p. 16 (A.2.1 COSMOS POLICY NOISE DISTRIBUTION), p. 22 (A.4.2 COSMOS POLICY INFERENCE LATENCY).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | does, support, robot, proprioception, input, actions, state, values, output, multiple, camera, views-all, desired, required | observation, uncertainty/risk estimate와 task command | body cue; exact tensor/frame verify |
| State/latent | does, support, robot, proprioception, input, actions, state, values, output, multiple | safe set, recovery state 또는 constraint margin | body cue; notation verify |
| Action/output | evaluate, modes, first, direct, policy, without, planning, then, model-based, future | shielded, recovery 또는 safe action | body cue; unit/decoder verify |
| Objective/constraint | After, gradient, steps, policy, action, training, loss, future, proprio, wrist | task utility subject to safety constraint | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 3 PRELIMINARIES - extractive PDF cue:** It does not support robot proprioception as input, robot actions or state values as output, nor multiple camera views-all of which are desired or required ...
- **p. 4 / 3 PRELIMINARIES - extractive PDF cue:** 4 COSMOS POLICY: ADAPTING VIDEO MODEL FOR CONTROL & PLANNING In this section, we discuss how to adapt Cosmos-Predict2 into a unified model that predicts ...
- **p. 17 / A.2.2 LIBERO TRAINING DETAILS - extractive PDF cue:** (Note that these are single-step training losses given varying σ (noise levels) as input, rather than losses on generations from the multi-step diffusion sampling used ...
- **p. 5 / 3 PRELIMINARIES - extractive PDF cue:** sequence contains 11 latent frames: (1) a blank placeholder,* (2) robot proprioception (e.g., endeffector pose or joint angles), (3) wrist camera image, (4) first third-person ...
- **p. 5 / 3 PRELIMINARIES - extractive PDF cue:** The choice of the input mask determines whether the value function represents the state value V (s′) or state-action value Q(s, a); we compare these ...
- **p. 6 / 3 PRELIMINARIES - extractive PDF cue:** Cosmos Policy can successfully execute real-world robotic control tasks that require long-horizon, high-precision manipulation and have high action multimodality. while the latter two outputs can ...
- **p. 6 / 3 PRELIMINARIES - extractive PDF cue:** 4.3 PLANNING WITH COSMOS POLICY'S WORLD MODEL AND VALUE FUNCTION Cosmos Policy can be deployed as (1) a direct policy without planning or (2) a ...
- **Normalized interface:** observation=observation, uncertainty/risk estimate와 task command; state=safe set, recovery state 또는 constraint margin; output/action=shielded, recovery 또는 safe action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | 현재 command의 one-step safety 또는 recovery trajectory horizon; exact lookahead 확인 필요. | We frame robotic manipulation tasks as finite-horizon Markov decision processes (MDPs) defined by the tuple ⟨S, A, T, R, H⟩, where S ... | episode/sequence/action-chunk boundary |
| Rate / latency | nominal policy와 safety monitor/filter의 runtime rate를 별도로 기록한다. | We ensure fair comparison between methods by using the same fixed set of initial states for each method. §Diffusion Policy is an ... | Hz/fps, inference time and control rate |
| Memory | risk score, recent trajectory/history와 recovery state. | In other words, we do not use input history nor predict future frames across multiple subsequent timesteps. | window and reset |
| Compute | risk inference, barrier/QP solve 또는 backup policy selection이 latency를 결정한다. | Finally, for the significantly smaller Diffusion Policy, which only contains approximately 150M parameters (as opposed to 2-7B for the other methods), we ... | hardware, batch and throughput |

## Training vs Inference

- **p. 17 / A.2.2 LIBERO TRAINING DETAILS - extractive PDF cue:** (Note that these are single-step training losses given varying σ (noise levels) as input, rather than losses on generations from the multi-step diffusion sampling used ...
- **p. 16 / A.2.1 COSMOS POLICY NOISE DISTRIBUTION - extractive PDF cue:** This higher lower bound empirically improves prediction accuracy at inference time for actions, future states, and values, as measured by lower L1 loss on training ...
- **p. 17 / A.2.2 LIBERO TRAINING DETAILS - extractive PDF cue:** After 40K gradient steps, the policy's action L1 training loss is 0.012, future proprio L1 training loss is 0.007, future wrist image latent L1 training ...
- **p. 22 / A.4.2 COSMOS POLICY INFERENCE LATENCY - extractive PDF cue:** (4) Adding to the prior ablation, we ablate both the future state and value targets when training the policy, thus training a barebones policy that ...
- **p. 17 / A.2.4 ALOHA TRAINING DETAILS - extractive PDF cue:** Finally, for the significantly smaller Diffusion Policy, which only contains approximately 150M parameters (as opposed to 2-7B for the other methods), we train from scratch ...
- **p. 22 / A.4.2 COSMOS POLICY INFERENCE LATENCY - extractive PDF cue:** Each version of the policy is trained with the exact same training hyperparameters and compute as the original Cosmos Policy in RoboCasa, and evaluated across ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Note, single-step, training, losses, given, varying, noise, levels, input, rather, generations, multi-step, diffusion, sampling, during, policy, inference, magnitudes, imply, model.
- **Relevant PDF headings:** A.2.1 COSMOS POLICY NOISE DISTRIBUTION (p. 15); A.3.1 GENERAL COSMOS POLICY EVALUATION DETAILS (p. 17); A.4.2 COSMOS POLICY INFERENCE LATENCY (p. 21).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Risk / failure representation | The LIBERO benchmark (Liu et al., 2024) consists of a variety of environments and tasks featuring a single Franka Emika Panda robot ... | p. 7 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS) |
| Filtering / recovery | Our method achieves highest performance overall, even outperforming fine-tuned state-of-the-art vision-language-action (VLA) models. | p. 8 (5 EXPERIMENTS), p. 8 (Figure/Table caption) |
| Monitoring / re-entry | Table 1: LIBERO simulation benchmark results. Success rates (SR) across four LIBERO benchmark task suites (Liu et al., 2024). Cosmos Policy success ... | p. 8 (Figure/Table caption), p. 8 (5 EXPERIMENTS) |

## Failure and Ablation Link

- **p. 20 / Figure/Table caption - extractive PDF cue:** Table 4: Cosmos Policy ablations in LIBERO. Here we report the results of two independent ablations: (1) In Section 4.2, we discussed that Cosmos Policy's ...
- **p. 20 / A.4.1 ADDITIONAL ABLATION EXPERIMENTS - extractive PDF cue:** To further study the effects of individual components of the Cosmos Policy design, as well as the joint training objectives discussed in Section 4.2, we ...
- **p. 10 / 5 EXPERIMENTS - extractive PDF cue:** We find that the model-based variant (V (s′)) leads to highest overall performance. pares different variants of planning, such as directly learning a Q-value function ...
- **p. 10 / 5 EXPERIMENTS - extractive PDF cue:** The V (s′) variant requires a world model to predict the future state before the value can be estimated, while the Q(s, a) variant enables ...
- **p. 22 / Figure/Table caption - extractive PDF cue:** Table 5: Cosmos Policy ablations and additional experiments in RoboCasa. Top: We ablate individual components of the joint objectives training scheme and auxiliary supervision discussed ...
- **p. 8 / 5 EXPERIMENTS - extractive PDF cue:** We answer Q1 by comparing Cosmos Policy as a direct policy (without planning) with state-of-the-art imitation learning policies and assessing their relative effectiveness.
- **p. 8 / 5 EXPERIMENTS - extractive PDF cue:** We answer Q2 by ablating various components of Cosmos Policy and analyzing the resulting effects on task performance.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 17 (A.2.2 LIBERO TRAINING DETAILS), p. 21 (A.4.2 COSMOS POLICY INFERENCE LATENCY), p. 16 (A.2.1 COSMOS POLICY NOISE DISTRIBUTION), p. 17 (A.2.2 LIBERO TRAINING DETAILS), p. 16 (A.2.1 COSMOS POLICY NOISE DISTRIBUTION), p. 15 (A.1 LATENT INJECTION IMPLEMENTATION DETAILS), objective p. 17 (A.2.2 LIBERO TRAINING DETAILS), p. 17 (A.2.4 ALOHA TRAINING DETAILS), p. 16 (A.2.1 COSMOS POLICY NOISE DISTRIBUTION), p. 22 (A.4.2 COSMOS POLICY INFERENCE LATENCY), p. 15 (A.2.1 COSMOS POLICY NOISE DISTRIBUTION), p. 16 (A.2.1 COSMOS POLICY NOISE DISTRIBUTION), temporal p. 3 (3 PRELIMINARIES), p. 7 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), p. 15 (A.1 LATENT INJECTION IMPLEMENTATION DETAILS), p. 3 (3 PRELIMINARIES), p. 5 (3 PRELIMINARIES).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
