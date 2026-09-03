# Problem - Robot Fine-Tuning Made Easy: Pre-Training Rewards and Policies for Autonomous Real-World Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://ieeexplore.ieee.org/document/10610421/; PDF retrieval source: https://arxiv.org/pdf/2310.15145. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 3 (III. PRELIMINARIES), p. 3 (III. PRELIMINARIES)): However, numerous challenges arise when using this recipe in practice.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** The pre-train and fine-tune paradigm in machine learning has had dramatic success in a wide range of domains because the use of existing data or ...
- **p. 1 / Abstract - extractive body cue:** We aim to enable this paradigm in robotic reinforcement learning, allowing a robot to learn a new task with little human effort by leveraging data ...
- **p. 1 / Abstract - extractive body cue:** However, reinforcement learning often requires significant human effort in the form of manual reward specification or environment resets, even if the policy is pre-trained.
- **p. 1 / Abstract - extractive body cue:** We introduce ROBOFUME, a reset-free fine-tuning system that pre-trains a multi-task manipulation policy from diverse datasets of prior experiences and self-improves online to learn a ...
- **p. 1 / Abstract - extractive body cue:** Our insights are to utilize calibrated offline reinforcement learning techniques to ensure efficient online finetuning of a pre-trained policy in the presence of distribution shifts ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** However, numerous challenges arise when using this recipe in practice.
- **p. 2 / I. INTRODUCTION - extractive body cue:** In the pre-training phase, we assume access to a diverse prior dataset, a few task demonstrations and reset demonstrations of the target task, and a ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, numerous challenges arise when using this recipe in practice. | offline robot transition/trajectory dataset과 deployment MDP | body wording is the source claim |
| Observation / input | The policy then takes as inputs a concatenation of the encoded image observation ϕ(simg), task representation z, and proprioceptive information sp, processes ... | dataset state/observation, action, reward와 return-to-go | exact sensor/frame/preprocessing from PDF body |
| State / latent | policy, then, takes, inputs, concatenation, encoded, image, observation, simg, task | Q/value 또는 sequence-policy state | notation and tensor shape require body check |
| Output / action | failure, states, consist, entirely, image, observations, correspond, unsuccessful | dataset-supported action sequence | exact unit/frame/decoder require body check |
| Target outcome | offline return and deployment safety | offline policy value, OOD safety와 closed-loop success | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | dataset transition (s,a,r,s′); body terms: policy, then, takes, inputs, concatenation, encoded, image, observation, simg, task | p. 3 (IV. ROBOFUME), p. 4 (IV. ROBOFUME), p. 3 (III. PRELIMINARIES) |
| Decision / output variable | dataset-supported policy action; body terms: assumes, access, prior, dataset, Dprior, consists, demonstrations, different | p. 3 (III. PRELIMINARIES), p. 1 (Body text (section boundary not confidently recovered)), p. 1 (Abstract) |
| Objective / loss / cost | offline value with OOD control; cue terms: VLM, outputs, sparse, binary, reward, returning, success, token | p. 3 (IV. ROBOFUME), p. 3 (IV. ROBOFUME), p. 1 (Body text (section boundary not confidently recovered)), p. 4 (IV. ROBOFUME), p. 4 (IV. ROBOFUME) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 1 (Body text (section boundary not confidently recovered)), p. 1 (Abstract), p. 2 (I. INTRODUCTION) |
| Success / guarantee | offline return and deployment safety | p. 5 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / I. INTRODUCTION - extractive body cue:** In the pre-training phase, we assume access to a diverse prior dataset, a few task demonstrations and reset demonstrations of the target task, and a ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** This causes non-trivial distribution shifts between pre-training and online fine-tuning data, which makes effectively fine-tuning a robot policy difficult.
- **p. 3 / III. PRELIMINARIES - extractive body cue:** The failure states D/ consist entirely of image observations that correspond to unsuccessful states and are collected to aid with the VLM reward learning.
- **p. 3 / III. PRELIMINARIES - extractive body cue:** To facilitate learning on the downstream task, we also assume the availability of a small set of target task demos Df, target task reset demos ...

## What the Paper Changes

PDF body contribution framing (p. 3 (III. PRELIMINARIES), p. 1 (Body text (section boundary not confidently recovered)), p. 1 (Abstract), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION)): Our method assumes access to a prior dataset Dprior = ∪N j=1Dj = ∪N j=1{(sj i, aj i, s′j i )}K i=1, which consists of demonstrations of N different tasks ...

- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** 1: We propose a system that enables autonomous and efficient real-world robot learning.
- **p. 1 / Abstract - extractive body cue:** In a diverse set of five real robot manipulation tasks, we show that our method can incorporate data from an existing robot dataset collected at ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** We evaluate our framework by pre-training it on the Bridge dataset [19] and testing it on a diverse set of real-world downstream tasks: cloth folding, ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** We perform more quantitative experiments in a simulation setup, where we illustrate that our method outperforms imitation learning and offline RL methods that either do ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 5 | All tasks use 50 forward and 50 backward demos for the target task, and fewer than 20 combined ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | We provide 10 forward and reset demonstrations for each task, 30 failure demos, and 10 demos each for ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | We find that in the Vase simulated task, VIP fails to obtain good behaviors. | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | Integrating this work with new VLM models that can exhibit robust zero-shot performance on unseen manipulation tasks and ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

offline_rl writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 3 (IV. ROBOFUME), p. 4 (IV. ROBOFUME), p. 3 (III. PRELIMINARIES), p. 4 (IV. ROBOFUME). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 3 (III. PRELIMINARIES), p. 3 (III. PRELIMINARIES), interface p. 3 (IV. ROBOFUME), p. 4 (IV. ROBOFUME), p. 3 (III. PRELIMINARIES), p. 4 (IV. ROBOFUME), objective p. 3 (IV. ROBOFUME), p. 3 (IV. ROBOFUME), p. 1 (Body text (section boundary not confidently recovered)), p. 4 (IV. ROBOFUME), p. 4 (IV. ROBOFUME).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (8 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** However, numerous challenges arise when using this recipe in practice. (p. 1, I. INTRODUCTION).
- **Formulation-changing contribution:** We evaluate our framework by pre-training it on the Bridge dataset [19] and testing it on a diverse set of real-world downstream tasks: cloth folding, cloth covering, sponge pickand-place, placing ... (p. 2, I. INTRODUCTION).
- **Assumption/failure evidence:** All tasks use 50 forward and 50 backward demos for the target task, and fewer than 20 combined trajectories of failures. (p. 5, V. EXPERIMENTS).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
