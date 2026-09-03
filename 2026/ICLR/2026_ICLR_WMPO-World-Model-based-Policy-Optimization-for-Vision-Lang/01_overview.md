# WMPO: World Model-based Policy Optimization for Vision-Language-Action Models

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://iclr.cc/virtual/2026/poster/10007263.
> PDF retrieval source: https://arxiv.org/pdf/2511.09515. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICLR
- Authors: not duplicated here when not verified in the registry source
- Primary track: World models, safety, uncertainty, and recovery
- Tier: NEXT
- Tags: Robotics, world model, policy optimization, model predictive control
- Official paper: https://iclr.cc/virtual/2026/poster/10007263
- Full-text retrieval: https://arxiv.org/pdf/2511.09515
- Code/Project: https://wm-po.github.io/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

World models, safety, uncertainty, and recovery의 safety 문제를 이해하기 위해 읽는다. 본문은 Nevertheless, integrating these models with existing VLAs remains a challenge.를 문제로 두고, To this end, we propose World Model-based Policy Optimization (WMPO), as illustrated in Fig.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Vision-Language-Action (VLA) models have shown strong potential for general-purpose robotic manipulation, but their reliance on expert demonstrations limits their ability to learn from failures and ...
- **p. 1 / Abstract - extractive body cue:** Reinforcement learning (RL) addresses these through self-improving interactions with the physical environment, but suffers from high sample complexity on real robots.
- **p. 1 / Abstract - extractive body cue:** We introduce World-Model-based Policy Optimization (WMPO), a principled framework for onpolicy VLA RL without interacting with the real environment.
- **p. 1 / Abstract - extractive body cue:** In contrast to widely used latent world models, WMPO focuses on pixel-based predictions that align the "imagined" trajectories with the VLA features pretrained with web-scale ...
- **p. 1 / Abstract - extractive body cue:** Crucially, WMPO enables the policy to perform on-policy GRPO that provides stronger performance than the often-used off-policy methods.
- **p. 2 / 1 Introduction - extractive body cue:** Nevertheless, integrating these models with existing VLAs remains a challenge.
- **p. 1 / 1 Introduction - extractive body cue:** This self-improvement process can lead to policies that are more robust and capable of recovering from failure.

## Core Idea

- **p. 2 / 1 Introduction - extractive body cue:** To this end, we propose World Model-based Policy Optimization (WMPO), as illustrated in Fig.
- **p. 2 / 1 Introduction - extractive body cue:** First, to mitigate the state-distribution mismatch between expert demonstrations and policy rollouts, we introduce policy behavior alignment, finetuning the world model with behavioral data collected ...
- **p. 1 / Abstract - extractive body cue:** We introduce World-Model-based Policy Optimization (WMPO), a principled framework for onpolicy VLA RL without interacting with the real environment.
- **p. 4 / 1. Imagined Trajectory Generation - extractive body cue:** The overall training procedure consists of three components: (1) Imagined Trajectory Generation, where policy model πθold and world model pϕ interact alternately to generate a ...
- **p. 5 / 1. Imagined Trajectory Generation - extractive body cue:** To mitigate this issue, we introduce a noisy-frame conditioning technique: during training, conditional frames Ii-m:i are perturbed with diffusion noise at 50/1000 steps rather than ...
- **p. 5 / 1. Imagined Trajectory Generation - extractive body cue:** Thus, each imagined trajectory in the world model is represented as a labeled pair (τ, y), which is then used for policy optimization.
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** WMPO: World Model-based Policy Optimization for Vision-Language-Action Models Fangqi Zhu1,2, Zhengyang Yan1, Zicong Hong1, Quanxin Shou1, Xiao Ma2,∗, Song Guo1,∗ 1Hong Kong University of Science ...
- **p. 5 / 1. Imagined Trajectory Generation - extractive body cue:** 3.3 Reward Model A key requirement for scalable policy optimization in the world model is automatically judging whether an imagined trajectory indicates task success.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Given c initial frames I0:c, the policy πθ takes the most recent m frames and language instruction g as input and predicts an action chunk 1 , i.e., ai:i+K ∼πθ(Ii-m:i, g). | observation, uncertainty/risk estimate와 task command | p. 5 (1. Imagined Trajectory Generation), p. 4 (3. Policy Update) |
| State/latent | Given, initial, frames, policy, takes, most, recent, language, instruction, input, predicts, action | safe set, recovery state 또는 constraint margin | p. 5 (1. Imagined Trajectory Generation), p. 4 (3. Policy Update), p. 5 (1. Imagined Trajectory Generation) |
| Output/action | Initial State Language Instruction 𝑠0 𝑔 𝜋𝜃 Policy Model Update መ𝐴𝑖 መ𝐴1 መ𝐴𝐺 | shielded, recovery 또는 safe action | p. 4 (3. Policy Update), p. 5 (1. Imagined Trajectory Generation), p. 1 (1 Introduction) |
| Objective/outcome | Our objective is to train a policy πθ(a / s) such that the predicted cumulative return of the imagined trajectories will be maximized max θ Eτ∼πθ,pϕ [Rψ(τ)] . | task return과 violation/failure probability | p. 4 (1. Imagined Trajectory Generation), p. 6 (1. Imagined Trajectory Generation), p. 4 (1. Imagined Trajectory Generation) |

## Main Claims and Actual Contribution

- **p. 2 / 1 Introduction - extractive body cue:** To this end, we propose World Model-based Policy Optimization (WMPO), as illustrated in Fig.
- **p. 2 / 1 Introduction - extractive body cue:** First, to mitigate the state-distribution mismatch between expert demonstrations and policy rollouts, we introduce policy behavior alignment, finetuning the world model with behavioral data collected ...
- **p. 1 / Abstract - extractive body cue:** We introduce World-Model-based Policy Optimization (WMPO), a principled framework for onpolicy VLA RL without interacting with the real environment.
- **p. 4 / 1. Imagined Trajectory Generation - extractive body cue:** The overall training procedure consists of three components: (1) Imagined Trajectory Generation, where policy model πθold and world model pϕ interact alternately to generate a ...
- **p. 5 / 1. Imagined Trajectory Generation - extractive body cue:** To mitigate this issue, we introduce a noisy-frame conditioning technique: during training, conditional frames Ii-m:i are perturbed with diffusion noise at 50/1000 steps rather than ...
- **p. 6 / 4 Experiments - extractive body cue:** We conduct extensive experiments to evaluate the effectiveness of WMPO, focusing on the following questions: (1) can WMPO outperform online and offline RL in simulation ...
- **p. 10 / 4 Experiments - extractive body cue:** The results show that the base policy, DPO, and WMPO achieve success rates of 53%, 60%, and 70%, respectively, demonstrating the effectiveness of WMPO on ...
- **p. 9 / 4 Experiments - extractive body cue:** DPO attains modest improvements in the in-distribution setting compared to the base policy, but its performance degrades significantly under background and texture changes, suggesting reliance ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 6 (4 Experiments), p. 10 (4 Experiments) |
| Embodiment/environment | We conduct extensive experiments to evaluate the effectiveness of WMPO, focusing on the following questions: (1) can WMPO outperform online and offline RL in simulation environments; (2) how does the behavior of ... | hardware/simulator version and reset protocol | p. 6 (4 Experiments), p. 9 (4 Experiments) |
| Dataset/benchmark | The top row shows the real-world trajectory of the base policy executed in the real world, while the bottom row depicts the corresponding imagined trajectory starting from the same initial state within ... | role, split, size and leakage | p. 6 (4 Experiments), p. 9 (4 Experiments), p. 9 (4 Experiments), p. 10 (4 Experiments) |
| Metric | Furthermore, we evaluate the reward model and find that it achieves an F1 score above 0.95 across all tasks, reliably distinguishing success from failure and effectively mitigating reward hacking. | definition, denominator, direction and uncertainty | p. 8 (4 Experiments), p. 7 (4 Experiments), p. 7 (4 Experiments) |
| Baseline/ablation | Results show that WMPO consistently outperforms both GRPO and DPO baselines under different budgets. | fair input/data/compute/action matching | p. 7 (4 Experiments), p. 8 (4 Experiments), p. 6 (4 Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 4 Experiments - extractive body cue:** The baseline policy, trained only on expert demonstrations, has never observed collisions during training; it continues to push the square against the stick until the ...
- **p. 10 / 4 Experiments - extractive body cue:** 6, demonstrate that WMPO achieves stable and substantial improvements over both baselines, whereas DPO fails to improve iteratively due to unstable training.
- **p. 8 / 4 Experiments - extractive body cue:** This is because WMPO discourages stuck behaviors, which often result in failures due to timeouts.
- **p. 10 / 4 Experiments - extractive body cue:** 7, more cases including failure could be found in Appendix C), to validate the effectiveness of WMPO.
- **p. 7 / 4 Experiments - extractive body cue:** Collision Self-correction Continue moving down WMPO Base Policy … … Figure 3 Behavior analysis of the Square task (inserting the square into the stick) shows ...
- **p. 9 / 4 Experiments - extractive body cue:** DPO attains modest improvements in the in-distribution setting compared to the base policy, but its performance degrades significantly under background and texture changes, suggesting reliance ...

## Why Read It

World models, safety, uncertainty, and recovery의 safety 문제를 이해하기 위해 읽는다. 본문은 Nevertheless, integrating these models with existing VLAs remains a challenge.를 문제로 두고, To this end, we propose World Model-based Policy Optimization (WMPO), as illustrated in Fig.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 2 (1 Introduction), p. 4 (1. Imagined Trajectory Generation) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (16 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** Nevertheless, integrating these models with existing VLAs remains a challenge. (p. 2, 1 Introduction).
- **Actual contribution:** To this end, we propose World Model-based Policy Optimization (WMPO), as illustrated in Fig. (p. 2, 1 Introduction).
- **Evaluation boundary:** 0 128 256 Rollout Budget 45 50 55 60 65 Success Rate (%) Base Policy DPO WMPO Figure 6 Lifelong learning results of WMPO and baselines. (p. 9, 4 Experiments).
- **Explicit failure boundary:** In contrast, Fig 9 shows a failure case where the model does not correctly predict a failed trajectory. (p. 15, C Real World Cases).
