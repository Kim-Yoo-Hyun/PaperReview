# Problem - WMPO: World Model-based Policy Optimization for Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://iclr.cc/virtual/2026/poster/10007263; PDF retrieval source: https://arxiv.org/pdf/2511.09515. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction)): Nevertheless, integrating these models with existing VLAs remains a challenge.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Vision-Language-Action (VLA) models have shown strong potential for general-purpose robotic manipulation, but their reliance on expert demonstrations limits their ability to learn from failures and ...
- **p. 1 / Abstract - extractive body cue:** Reinforcement learning (RL) addresses these through self-improving interactions with the physical environment, but suffers from high sample complexity on real robots.
- **p. 1 / Abstract - extractive body cue:** We introduce World-Model-based Policy Optimization (WMPO), a principled framework for onpolicy VLA RL without interacting with the real environment.
- **p. 1 / Abstract - extractive body cue:** In contrast to widely used latent world models, WMPO focuses on pixel-based predictions that align the "imagined" trajectories with the VLA features pretrained with web-scale ...
- **p. 1 / Abstract - extractive body cue:** Crucially, WMPO enables the policy to perform on-policy GRPO that provides stronger performance than the often-used off-policy methods.
- **p. 2 / 1 Introduction - extractive body cue:** Nevertheless, integrating these models with existing VLAs remains a challenge.
- **p. 1 / 1 Introduction - extractive body cue:** This self-improvement process can lead to policies that are more robust and capable of recovering from failure.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Nevertheless, integrating these models with existing VLAs remains a challenge. | uncertain robot state와 safe/unsafe operating region | body wording is the source claim |
| Observation / input | Given c initial frames I0:c, the policy πθ takes the most recent m frames and language instruction g as input and predicts ... | observation, uncertainty/risk estimate와 task command | exact sensor/frame/preprocessing from PDF body |
| State / latent | Given, initial, frames, policy, takes, most, recent, language, instruction, input | safe set, recovery state 또는 constraint margin | notation and tensor shape require body check |
| Output / action | address, mismatch, fine-tune, world, model, real, rollout, trajectories | shielded, recovery 또는 safe action | exact unit/frame/decoder require body check |
| Target outcome | low violation/failure probability with useful intervention | task return과 violation/failure probability | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | state/history and risk h(s); body terms: Given, initial, frames, policy, takes, most, recent, language, instruction, input | p. 5 (1. Imagined Trajectory Generation), p. 4 (3. Policy Update), p. 5 (1. Imagined Trajectory Generation) |
| Decision / output variable | filtered/recovery action u_safe; body terms: World, Model-based, Policy, Optimization, WMPO, illustrated, Fig, First | p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (Abstract) |
| Objective / loss / cost | task utility subject to safety constraint; cue terms: objective, train, policy, predicted, cumulative, return, imagined, trajectories | p. 4 (1. Imagined Trajectory Generation), p. 6 (1. Imagined Trajectory Generation), p. 5 (1. Imagined Trajectory Generation), p. 6 (1. Imagined Trajectory Generation), p. 3 (1 Introduction), p. 4 (3. Policy Update) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (1. Imagined Trajectory Generation), p. 6 (1. Imagined Trajectory Generation), p. 5 (1. Imagined Trajectory Generation) |
| Success / guarantee | low violation/failure probability with useful intervention | p. 8 (4 Experiments), p. 7 (4 Experiments), p. 7 (4 Experiments) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / 1 Introduction - extractive body cue:** This self-improvement process can lead to policies that are more robust and capable of recovering from failure.
- **p. 2 / 1 Introduction - extractive body cue:** Second, short-horizon prediction makes it difficult to define accurate rewards and is prone to reward hacking.
- **p. 3 / 1 Introduction - extractive body cue:** We further demonstrate WMPO's strong generalization compared to offline RL methods, as well as its capacity for lifelong learning through alternating updates between the VLA ...

## What the Paper Changes

PDF body contribution framing (p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (Abstract), p. 4 (1. Imagined Trajectory Generation), p. 5 (1. Imagined Trajectory Generation)): To this end, we propose World Model-based Policy Optimization (WMPO), as illustrated in Fig.

- **p. 2 / 1 Introduction - extractive body cue:** First, to mitigate the state-distribution mismatch between expert demonstrations and policy rollouts, we introduce policy behavior alignment, finetuning the world model with behavioral data collected ...
- **p. 1 / Abstract - extractive body cue:** We introduce World-Model-based Policy Optimization (WMPO), a principled framework for onpolicy VLA RL without interacting with the real environment.
- **p. 4 / 1. Imagined Trajectory Generation - extractive body cue:** The overall training procedure consists of three components: (1) Imagined Trajectory Generation, where policy model πθold and world model pϕ interact alternately to generate a ...
- **p. 5 / 1. Imagined Trajectory Generation - extractive body cue:** To mitigate this issue, we introduce a noisy-frame conditioning technique: during training, conditional frames Ii-m:i are perturbed with diffusion noise at 50/1000 steps rather than ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | The baseline policy, trained only on expert demonstrations, has never observed collisions during training; it continues to push ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 10 | 6, demonstrate that WMPO achieves stable and substantial improvements over both baselines, whereas DPO fails to improve iteratively ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | This is because WMPO discourages stuck behaviors, which often result in failures due to timeouts. | reported limitation/failure wording; scope must be verified |
| body cue at p. 10 | 7, more cases including failure could be found in Appendix C), to validate the effectiveness of WMPO. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

safety writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 5 (1. Imagined Trajectory Generation), p. 4 (3. Policy Update), p. 5 (1. Imagined Trajectory Generation), p. 1 (1 Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), interface p. 5 (1. Imagined Trajectory Generation), p. 4 (3. Policy Update), p. 5 (1. Imagined Trajectory Generation), p. 1 (1 Introduction), objective p. 4 (1. Imagined Trajectory Generation), p. 6 (1. Imagined Trajectory Generation), p. 5 (1. Imagined Trajectory Generation), p. 6 (1. Imagined Trajectory Generation), p. 3 (1 Introduction), p. 4 (3. Policy Update).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (16 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** Nevertheless, integrating these models with existing VLAs remains a challenge. (p. 2, 1 Introduction).
- **Formulation-changing contribution:** To this end, we propose World Model-based Policy Optimization (WMPO), as illustrated in Fig. (p. 2, 1 Introduction).
- **Assumption/failure evidence:** In contrast, Fig 9 shows a failure case where the model does not correctly predict a failed trajectory. (p. 15, C Real World Cases).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
