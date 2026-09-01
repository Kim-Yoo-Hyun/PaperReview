# Method - WorldGym: World Model as An Environment for Policy Evaluation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (25 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://iclr.cc/virtual/2026/poster/10008029; PDF retrieval source: https://arxiv.org/pdf/2506.00613. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 3 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 1 (ABSTRACT), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 5 (1 INTRODUCTION)): First, the world model is initialized with an initial observation o0, which is then passed as input to a policy π which produces a chunk of actions apred.

## Method Body Digest

- **p. 3 / 1 INTRODUCTION - extractive body cue:** First, the world model is initialized with an initial observation o0, which is then passed as input to a policy π which produces a chunk ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** 3.1 BUILDING THE WORLD MODEL First, we describe the architecture and key implementation details, followed by our proposed inference scheme for policy rollouts.
- **p. 1 / ABSTRACT - extractive body cue:** We propose a world-model-based policy evaluation environment (WorldGym), an autoregressive, action-conditioned video generation model which serves as a proxy to real world environments.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Inspired by this observation, we propose a world-model-based policy evaluation environment (WorldGym), as shown in Figure 1.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** We consider a multi-task, finite-horizon, partially observable Markov Decision Process (POMDP) (Puterman, 2014; Kaelbling et al., 1995), specified by M = (S, A, O, G, ...
- **p. 5 / 1 INTRODUCTION - extractive body cue:** We then assess whether relative policy performance is preserved, comparing different versions, sizes, and training stages of the same models (Section 4.2).
- **p. 4 / 1 INTRODUCTION - extractive body cue:** We propose setting the horizon equal to the policy's action chunk size, /apred/.
- **p. 1 / ABSTRACT - extractive body cue:** Policies are evaluated via Monte Carlo rollouts in the world model, with a vision-language model providing rewards.

## Design Rationale

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Key contributions of this paper include: • We propose to use video world model to evaluate robot policies across different robot morphologies, and perform a ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Inspired by this observation, we propose a world-model-based policy evaluation environment (WorldGym), as shown in Figure 1.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** To ensure the world model is fully controllable by robot actions, we propose to randomly drop out actions for entire video clips, and use classifier-free ...

## Source Evidence Cues

- **p. 3 / 1 INTRODUCTION - extractive body cue:** First, the world model is initialized with an initial observation o0, which is then passed as input to a policy π which produces a chunk ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** 3.1 BUILDING THE WORLD MODEL First, we describe the architecture and key implementation details, followed by our proposed inference scheme for policy rollouts.
- **p. 1 / ABSTRACT - extractive body cue:** We propose a world-model-based policy evaluation environment (WorldGym), an autoregressive, action-conditioned video generation model which serves as a proxy to real world environments.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Inspired by this observation, we propose a world-model-based policy evaluation environment (WorldGym), as shown in Figure 1.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** We consider a multi-task, finite-horizon, partially observable Markov Decision Process (POMDP) (Puterman, 2014; Kaelbling et al., 1995), specified by M = (S, A, O, G, ...
- **p. 5 / 1 INTRODUCTION - extractive body cue:** We then assess whether relative policy performance is preserved, comparing different versions, sizes, and training stages of the same models (Section 4.2).
- **p. 4 / 1 INTRODUCTION - extractive body cue:** We propose setting the horizon equal to the policy's action chunk size, /apred/.
- **Detected method headings:** C ARCHITECTURE AND TRAINING DETAILS OF VIDEO BASED POLICY (p. 19); C.1 VALIDATION VISUALIZATION OF LANGUAGE CONDITIONED VIDEO GENERATION MODEL (p. 19)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Risk / failure representation | unsafe state와 uncertainty를 계산한다 | observation, nominal command, history | barrier, risk model, failure classifier, uncertainty 또는 safe set을 추정 | risk/margin/failure state | First, the world model is initialized with an initial observation o0, which is then passed as input to a policy π which ... | p. 3 (1 INTRODUCTION), p. 3 (1 INTRODUCTION) |
| Filtering / recovery | nominal command를 안전 command로 바꾼다 | nominal action과 safety constraint | QP shield, backup policy, correction, stop 또는 recovery plan을 선택 | safe/recovery action | 3.1 BUILDING THE WORLD MODEL First, we describe the architecture and key implementation details, followed by our proposed inference scheme for policy ... | p. 3 (1 INTRODUCTION), p. 1 (ABSTRACT) |
| Monitoring / re-entry | 실행 결과를 다시 risk decision에 반영한다 | executed action과 next observation | threshold, update, replan, abort 또는 return-to-task를 수행 | continue/correct/abort state | We propose a world-model-based policy evaluation environment (WorldGym), an autoregressive, action-conditioned video generation model which serves as a proxy to real world ... | p. 1 (ABSTRACT), p. 2 (1 INTRODUCTION) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 1 / ABSTRACT - extractive body cue:** Policies are evaluated via Monte Carlo rollouts in the world model, with a vision-language model providing rewards.
- **p. 1 / ABSTRACT - extractive body cue:** Evaluating robot control policies is difficult: real-world testing is costly, and handcrafted simulators require manual effort to improve in realism and generality.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** We consider the sparse reward setting 2
- **p. 2 / 1 INTRODUCTION - extractive body cue:** WorldGym then passes the generated rollout to a VLM which provides rewards.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** The value of a policy π can be defined as the total expected future reward: ρ(π) =E[R(sH, g)/s0, g ∼G, at ∼π(st, g), st+1 ∼T(st, ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** As a result, learning a world model can benefit from diverse data from different tasks and environments with different state spaces, goals, and reward functions.
- **Formal bridge:** state/history and risk h(s) -> filtered/recovery action u_safe -> task utility subject to safety constraint -> low violation/failure probability with useful intervention.
- **Equation/algorithm anchors:** p. 4 (1 INTRODUCTION).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | First, world, model, initialized, initial, observation, then, passed, input, policy, produces, chunk, actions, apred | observation, uncertainty/risk estimate와 task command | body cue; exact tensor/frame verify |
| State/latent | First, world, model, initialized, initial, observation, then, passed, input, policy | safe set, recovery state 또는 constraint margin | body cue; notation verify |
| Action/output | Key, contributions, include, video, world, model, evaluate, robot, policies, across | shielded, recovery 또는 safe action | body cue; unit/decoder verify |
| Objective/constraint | Policies, evaluated, Monte, Carlo, rollouts, world, model, vision-language, providing, rewards | task utility subject to safety constraint | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 1 INTRODUCTION - extractive body cue:** First, the world model is initialized with an initial observation o0, which is then passed as input to a policy π which produces a chunk ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** This makes it possible to learn a single world model that, in principle, can be used as an interactive environment to evaluate any policies on ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** A policy π interacts with the environment for a goal starting from an initial state g, s0 ∼G, producing a distribution π(·/st, g) over A ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** Motivated by characteristics of a real-robot system such as image based observations, high control frequencies, diverse offline data from different tasks/environments, and the lack of ...
- **p. 1 / ABSTRACT - extractive body cue:** We propose a world-model-based policy evaluation environment (WorldGym), an autoregressive, action-conditioned video generation model which serves as a proxy to real world environments.
- **p. 7 / 1 INTRODUCTION - extractive body cue:** 4.3 OUT-OF-DISTRIBUTION INPUTS In this section, use WorldGym to explore policies' performance on both OOD input images and OOD language instructions.
- **p. 8 / 1 INTRODUCTION - extractive body cue:** Starting from a set of initial frames from the tasks listed in Table 5, we modify each task's language instruction, e.g. changing the target object ...
- **Normalized interface:** observation=observation, uncertainty/risk estimate와 task command; state=safe set, recovery state 또는 constraint margin; output/action=shielded, recovery 또는 safe action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | 현재 command의 one-step safety 또는 recovery trajectory horizon; exact lookahead 확인 필요. | Key contributions of this paper include: • We propose to use video world model to evaluate robot policies across different robot morphologies, ... | episode/sequence/action-chunk boundary |
| Rate / latency | nominal policy와 safety monitor/filter의 runtime rate를 별도로 기록한다. | To enable efficient rollouts of policies which predict different-length action chunks, WorldGym aligns its diffusion horizon length with policies' chunk sizes at ... | Hz/fps, inference time and control rate |
| Memory | risk score, recent trajectory/history와 recovery state. | not recovered | window and reset |
| Compute | risk inference, barrier/QP solve 또는 backup policy selection이 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / 1 INTRODUCTION - extractive body cue:** 3.1 BUILDING THE WORLD MODEL First, we describe the architecture and key implementation details, followed by our proposed inference scheme for policy rollouts.
- **p. 5 / 1 INTRODUCTION - extractive body cue:** We then assess whether relative policy performance is preserved, comparing different versions, sizes, and training stages of the same models (Section 4.2).
- **p. 6 / 1 INTRODUCTION - extractive body cue:** 0 5k 10k 20k 40k 60k Checkpoint (training steps) 0 5 10 15 20 25 30 35 Success Rate (%) Mean Success Rate Across Checkpoints ...
- **p. 7 / 1 INTRODUCTION - extractive body cue:** To examine whether WorldGym provides meaningful signals for policy training, hyperparameter tuning, and checkpoint selections, we train two robot policies from scratch.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To enable efficient rollouts of policies which predict different-length action chunks, WorldGym aligns its diffusion horizon length with policies' chunk sizes at inference time.
- **p. 4 / 1 INTRODUCTION - extractive body cue:** By virtue of being trained with Diffusion Forcing, as well as our usage of a causal temporal attention mask, we can flexibly control how many ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** First, world, model, initialized, initial, observation, then, passed, input, policy, produces, chunk, actions, apred, BUILDING, describe, architecture, implementation, details, followed.
- **Relevant PDF headings:** C ARCHITECTURE AND TRAINING DETAILS OF VIDEO BASED POLICY (p. 19); C.1 VALIDATION VISUALIZATION OF LANGUAGE CONDITIONED VIDEO GENERATION MODEL (p. 19).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Risk / failure representation | We suspect that OpenVLA consistently outperforms Octo and RT-1-X on OOD language tasks due to its strong VLM backbone and richer robot ... | p. 8 (1 INTRODUCTION), p. 8 (1 INTRODUCTION) |
| Filtering / recovery | We suspect that OpenVLA consistently outperforms Octo and RT-1-X on OOD language tasks due to its strong VLM backbone and richer robot ... | p. 8 (1 INTRODUCTION), p. 22 (Figure/Table caption) |
| Monitoring / re-entry | Table 3: Performance of VLM as reward (mean and standard error across 4 runs) on videos from RT-1 (Brohan et al., 2022) ... | p. 17 (Figure/Table caption), p. 6 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 9 / 1 INTRODUCTION - extractive body cue:** RT-1-X Octo OpenVLA 0 10 20 30 40 50 60 70 Success Rate (%) 15.6% 23.8% 67.4% 7.6% 4.1% 39.4% Effect of OOD Distractors on ...
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 13: Effect of OOD Distractors. We use an image editing model to add distractor objects to the Bridge evaluation suite, finding that RT-1- X ...
- **p. 8 / 1 INTRODUCTION - extractive body cue:** Additionally, even without access to an image editing model, we demonstrate that WorldGym can be used to evaluate policies' performance on OOD language instructions.
- **p. 8 / 1 INTRODUCTION - extractive body cue:** Future research could be prioritized to address these issues, all without spending extra effort to set up additional experiments in the real world or within ...
- **p. 25 / Figure/Table caption - extractive body cue:** Table 8: Dataset ablation. Larger training dataset improves all three metrics comparing generated videos and ground-truth validation videos. ↑means higher the better. Subset (Bridge V1) ...
- **p. 8 / 1 INTRODUCTION - extractive body cue:** Pick Carrot Pick Carrot Pick Carrot Pick Cat Pick Cat Pick Taylor Swift Pick Square Figure 10: OOD: Failure modes.
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 10: OOD: Failure modes. Left: We add a laptop to the scene, which displays an image of a carrot. In 15% of trials, OpenVLA ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 3 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 1 (ABSTRACT), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 5 (1 INTRODUCTION), objective p. 1 (ABSTRACT), p. 1 (ABSTRACT), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), temporal p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 4 (1 INTRODUCTION), p. 4 (1 INTRODUCTION), p. 9 (5 RELATED WORK).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
