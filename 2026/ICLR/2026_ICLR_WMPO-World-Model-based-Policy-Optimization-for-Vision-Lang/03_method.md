# Method - WMPO: World Model-based Policy Optimization for Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://iclr.cc/virtual/2026/poster/10007263; PDF retrieval source: https://arxiv.org/pdf/2511.09515. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 2 (1 Introduction), p. 4 (1. Imagined Trajectory Generation), p. 5 (1. Imagined Trajectory Generation), p. 1 (Abstract), p. 2 (1 Introduction), p. 1 (Body text (section boundary not confidently recovered))): First, to mitigate the state-distribution mismatch between expert demonstrations and policy rollouts, we introduce policy behavior alignment, finetuning the world model with behavioral data collected by the policy itself.

## Method Body Digest

- **p. 2 / 1 Introduction - extractive body cue:** First, to mitigate the state-distribution mismatch between expert demonstrations and policy rollouts, we introduce policy behavior alignment, finetuning the world model with behavioral data collected ...
- **p. 4 / 1. Imagined Trajectory Generation - extractive body cue:** The overall training procedure consists of three components: (1) Imagined Trajectory Generation, where policy model πθold and world model pϕ interact alternately to generate a ...
- **p. 5 / 1. Imagined Trajectory Generation - extractive body cue:** Thus, each imagined trajectory in the world model is represented as a labeled pair (τ, y), which is then used for policy optimization.
- **p. 1 / Abstract - extractive body cue:** We introduce World-Model-based Policy Optimization (WMPO), a principled framework for onpolicy VLA RL without interacting with the real environment.
- **p. 2 / 1 Introduction - extractive body cue:** To this end, we propose World Model-based Policy Optimization (WMPO), as illustrated in Fig.
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** WMPO: World Model-based Policy Optimization for Vision-Language-Action Models Fangqi Zhu1,2, Zhengyang Yan1, Zicong Hong1, Quanxin Shou1, Xiao Ma2,∗, Song Guo1,∗ 1Hong Kong University of Science ...
- **p. 5 / 1. Imagined Trajectory Generation - extractive body cue:** 3.3 Reward Model A key requirement for scalable policy optimization in the world model is automatically judging whether an imagined trajectory indicates task success.
- **p. 4 / 1. Imagined Trajectory Generation - extractive body cue:** Our objective is to train a policy πθ(a / s) such that the predicted cumulative return of the imagined trajectories will be maximized max θ ...

## Design Rationale

- **p. 2 / 1 Introduction - extractive body cue:** To this end, we propose World Model-based Policy Optimization (WMPO), as illustrated in Fig.
- **p. 2 / 1 Introduction - extractive body cue:** First, to mitigate the state-distribution mismatch between expert demonstrations and policy rollouts, we introduce policy behavior alignment, finetuning the world model with behavioral data collected ...
- **p. 1 / Abstract - extractive body cue:** We introduce World-Model-based Policy Optimization (WMPO), a principled framework for onpolicy VLA RL without interacting with the real environment.

## Source Evidence Cues

- **p. 2 / 1 Introduction - extractive body cue:** First, to mitigate the state-distribution mismatch between expert demonstrations and policy rollouts, we introduce policy behavior alignment, finetuning the world model with behavioral data collected ...
- **p. 4 / 1. Imagined Trajectory Generation - extractive body cue:** The overall training procedure consists of three components: (1) Imagined Trajectory Generation, where policy model πθold and world model pϕ interact alternately to generate a ...
- **p. 5 / 1. Imagined Trajectory Generation - extractive body cue:** Thus, each imagined trajectory in the world model is represented as a labeled pair (τ, y), which is then used for policy optimization.
- **p. 1 / Abstract - extractive body cue:** We introduce World-Model-based Policy Optimization (WMPO), a principled framework for onpolicy VLA RL without interacting with the real environment.
- **p. 2 / 1 Introduction - extractive body cue:** To this end, we propose World Model-based Policy Optimization (WMPO), as illustrated in Fig.
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** WMPO: World Model-based Policy Optimization for Vision-Language-Action Models Fangqi Zhu1,2, Zhengyang Yan1, Zicong Hong1, Quanxin Shou1, Xiao Ma2,∗, Song Guo1,∗ 1Hong Kong University of Science ...
- **p. 5 / 1. Imagined Trajectory Generation - extractive body cue:** 3.3 Reward Model A key requirement for scalable policy optimization in the world model is automatically judging whether an imagined trajectory indicates task success.
- **Detected method headings:** 3. Policy Update (p. 4)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Risk / failure representation | unsafe state와 uncertainty를 계산한다 | observation, nominal command, history | barrier, risk model, failure classifier, uncertainty 또는 safe set을 추정 | risk/margin/failure state | First, to mitigate the state-distribution mismatch between expert demonstrations and policy rollouts, we introduce policy behavior alignment, finetuning the world model with ... | p. 2 (1 Introduction), p. 4 (1. Imagined Trajectory Generation) |
| Filtering / recovery | nominal command를 안전 command로 바꾼다 | nominal action과 safety constraint | QP shield, backup policy, correction, stop 또는 recovery plan을 선택 | safe/recovery action | The overall training procedure consists of three components: (1) Imagined Trajectory Generation, where policy model πθold and world model pϕ interact alternately ... | p. 4 (1. Imagined Trajectory Generation), p. 5 (1. Imagined Trajectory Generation) |
| Monitoring / re-entry | 실행 결과를 다시 risk decision에 반영한다 | executed action과 next observation | threshold, update, replan, abort 또는 return-to-task를 수행 | continue/correct/abort state | Thus, each imagined trajectory in the world model is represented as a labeled pair (τ, y), which is then used for policy ... | p. 5 (1. Imagined Trajectory Generation), p. 1 (Abstract) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 1. Imagined Trajectory Generation - extractive body cue:** Our objective is to train a policy πθ(a / s) such that the predicted cumulative return of the imagined trajectories will be maximized max θ ...
- **p. 6 / 1. Imagined Trajectory Generation - extractive body cue:** The reward model, implemented as a VideoMAE [39] encoder with a linear head, is trained with binary cross-entropy loss.
- **p. 4 / 1. Imagined Trajectory Generation - extractive body cue:** The overall training procedure consists of three components: (1) Imagined Trajectory Generation, where policy model πθold and world model pϕ interact alternately to generate a ...
- **p. 5 / 1. Imagined Trajectory Generation - extractive body cue:** 3.3 Reward Model A key requirement for scalable policy optimization in the world model is automatically judging whether an imagined trajectory indicates task success.
- **p. 6 / 1. Imagined Trajectory Generation - extractive body cue:** We adopt Group Relative Policy Optimization (GRPO) as the policy optimization algorithm, since it provides stable and scalable training in settings with sparse rewards.
- **p. 5 / 1. Imagined Trajectory Generation - extractive body cue:** Let xi denote the feature representation at frame i; the update rule within each transformer block is given as: xi = xi + (1 + ...
- **Formal bridge:** state/history and risk h(s) -> filtered/recovery action u_safe -> task utility subject to safety constraint -> low violation/failure probability with useful intervention.
- **Equation/algorithm anchors:** p. 4 (1. Imagined Trajectory Generation), p. 6 (1. Imagined Trajectory Generation), p. 5 (1. Imagined Trajectory Generation), p. 6 (1. Imagined Trajectory Generation), p. 3 (1 Introduction), p. 4 (3. Policy Update).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Given, initial, frames, policy, takes, most, recent, language, instruction, input, predicts, action, chunk, Ii-m | observation, uncertainty/risk estimate와 task command | body cue; exact tensor/frame verify |
| State/latent | Given, initial, frames, policy, takes, most, recent, language, instruction, input | safe set, recovery state 또는 constraint margin | body cue; notation verify |
| Action/output | World, Model-based, Policy, Optimization, WMPO, illustrated, Fig, First, mitigate, state-distribution | shielded, recovery 또는 safe action | body cue; unit/decoder verify |
| Objective/constraint | objective, train, policy, predicted, cumulative, return, imagined, trajectories, will, maximized | task utility subject to safety constraint | equation anchor required |

## Observation–State–Action Interface

- **p. 5 / 1. Imagined Trajectory Generation - extractive body cue:** Given c initial frames I0:c, the policy πθ takes the most recent m frames and language instruction g as input and predicts an action chunk ...
- **p. 4 / 3. Policy Update - extractive body cue:** Initial State Language Instruction 𝑠0 𝑔 𝜋𝜃 Policy Model Update መ𝐴𝑖 መ𝐴1 መ𝐴𝐺
- **p. 5 / 1. Imagined Trajectory Generation - extractive body cue:** To address this mismatch, we fine-tune the world model on real rollout trajectories collected from the policy itself, thereby adapting it to the downstream (state, ...
- **p. 1 / 1 Introduction - extractive body cue:** Vision-Language-Action (VLA) models [1-3] have emerged as a promising paradigm for general-purpose robotic manipulation, enabling robots to follow natural language instructions in complex, unstructured environments.
- **p. 4 / 1. Imagined Trajectory Generation - extractive body cue:** S = I × G, where I denotes the image observation space, i.e., image sequences I0:K, and G denotes the language instruction space.
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** WMPO: World Model-based Policy Optimization for Vision-Language-Action Models Fangqi Zhu1,2, Zhengyang Yan1, Zicong Hong1, Quanxin Shou1, Xiao Ma2,∗, Song Guo1,∗ 1Hong Kong University of Science ...
- **p. 2 / 1 Introduction - extractive body cue:** First, to mitigate the state-distribution mismatch between expert demonstrations and policy rollouts, we introduce policy behavior alignment, finetuning the world model with behavioral data collected ...
- **Normalized interface:** observation=observation, uncertainty/risk estimate와 task command; state=safe set, recovery state 또는 constraint margin; output/action=shielded, recovery 또는 safe action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | 현재 command의 one-step safety 또는 recovery trajectory horizon; exact lookahead 확인 필요. | While this design supports long-horizon rollouts, it also introduces challenges such as visual distortion and action-frame misalignment. | episode/sequence/action-chunk boundary |
| Rate / latency | nominal policy와 safety monitor/filter의 runtime rate를 별도로 기록한다. | These trajectories are further used to fine-tune a world model, which predicts the next K = 8 frames given c = 4 ... | Hz/fps, inference time and control rate |
| Memory | risk score, recent trajectory/history와 recovery state. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | risk inference, barrier/QP solve 또는 backup policy selection이 latency를 결정한다. | These trajectories are further used to fine-tune a world model, which predicts the next K = 8 frames given c = 4 ... | hardware, batch and throughput |

## Training vs Inference

- **p. 2 / 1 Introduction - extractive body cue:** First, to mitigate the state-distribution mismatch between expert demonstrations and policy rollouts, we introduce policy behavior alignment, finetuning the world model with behavioral data collected ...
- **p. 4 / 1. Imagined Trajectory Generation - extractive body cue:** The overall training procedure consists of three components: (1) Imagined Trajectory Generation, where policy model πθold and world model pϕ interact alternately to generate a ...
- **p. 7 / 4 Experiments - extractive body cue:** 4.1 Experiment Settings Implementation Details In this work, we fine-tune OpenVLA-OFT [24] via imitation learning on target manipulation tasks as our base policy.
- **p. 5 / 1. Imagined Trajectory Generation - extractive body cue:** When applying the imagined trajectory to VLA optimization, we decode the images back into pixel space to better leverage the pretrained knowledge, rather than retraining ...
- **p. 5 / 1. Imagined Trajectory Generation - extractive body cue:** To mitigate this issue, we introduce a noisy-frame conditioning technique: during training, conditional frames Ii-m:i are perturbed with diffusion noise at 50/1000 steps rather than ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** First, mitigate, state-distribution, mismatch, between, expert, demonstrations, policy, rollouts, introduce, behavior, alignment, finetuning, world, model, behavioral, data, collected, itself, overall.
- **Relevant PDF headings:** 3. Policy Update (p. 4).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Risk / failure representation | We conduct extensive experiments to evaluate the effectiveness of WMPO, focusing on the following questions: (1) can WMPO outperform online and offline ... | p. 6 (4 Experiments), p. 9 (4 Experiments) |
| Filtering / recovery | Results show that WMPO consistently outperforms both GRPO and DPO baselines under different budgets. | p. 7 (4 Experiments), p. 8 (4 Experiments) |
| Monitoring / re-entry | We conduct extensive experiments to evaluate the effectiveness of WMPO, focusing on the following questions: (1) can WMPO outperform online and offline ... | p. 6 (4 Experiments), p. 10 (4 Experiments) |

## Failure and Ablation Link

- **p. 7 / 4 Experiments - extractive body cue:** These trajectories are further used to fine-tune a world model, which predicts the next K = 8 frames given c = 4 conditioning frames and ...
- **p. 7 / 4 Experiments - extractive body cue:** 4.1 Experiment Settings Implementation Details In this work, we fine-tune OpenVLA-OFT [24] via imitation learning on target manipulation tasks as our base policy.
- **p. 10 / 4 Experiments - extractive body cue:** Using the Cobot Mobile ALOHA platform, we collect 200 high-quality expert demonstrations to fine-tune the OpenVLA-OFT model as the base policy.
- **p. 10 / 4 Experiments - extractive body cue:** We then deploy this policy to collect an additional 128 trajectories, which are used to further fine-tune the world model and optimize the policy within ...
- **p. 8 / 4 Experiments - extractive body cue:** The baseline policy, trained only on expert demonstrations, has never observed collisions during training; it continues to push the square against the stick until the ...
- **p. 10 / 4 Experiments - extractive body cue:** 6, demonstrate that WMPO achieves stable and substantial improvements over both baselines, whereas DPO fails to improve iteratively due to unstable training.
- **p. 8 / 4 Experiments - extractive body cue:** This is because WMPO discourages stuck behaviors, which often result in failures due to timeouts.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 2 (1 Introduction), p. 4 (1. Imagined Trajectory Generation), p. 5 (1. Imagined Trajectory Generation), p. 1 (Abstract), p. 2 (1 Introduction), p. 1 (Body text (section boundary not confidently recovered)), objective p. 4 (1. Imagined Trajectory Generation), p. 6 (1. Imagined Trajectory Generation), p. 4 (1. Imagined Trajectory Generation), p. 5 (1. Imagined Trajectory Generation), p. 6 (1. Imagined Trajectory Generation), p. 5 (1. Imagined Trajectory Generation), temporal p. 2 (1 Introduction), p. 7 (4 Experiments), p. 5 (1. Imagined Trajectory Generation), p. 6 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (16 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** We adopt Group Relative Policy Optimization (GRPO) as the policy optimization algorithm, since it provides stable and scalable training in settings with sparse rewards. (p. 6, 1. Imagined Trajectory Generation).
- **Objective/update evidence:** The overall training procedure consists of three components: (1) Imagined Trajectory Generation, where policy model πθold and world model pϕ interact alternately to generate a full imagined trajectory; (2) Trajectory ... (p. 4, 1. Imagined Trajectory Generation).
- **Temporal/runtime evidence:** These trajectories are further used to fine-tune a world model, which predicts the next K = 8 frames given c = 4 conditioning frames and one action chunk. (p. 7, 4 Experiments).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
