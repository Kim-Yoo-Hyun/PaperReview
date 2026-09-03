# Octo: An Open-Source Generalist Robot Policy

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2405.12213.
> PDF retrieval source: https://arxiv.org/pdf/2405.12213. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / RSS
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: CORE
- Tags: Robotics, generalist policy, Imitation Learning
- Official paper: https://arxiv.org/abs/2405.12213
- Full-text retrieval: https://arxiv.org/pdf/2405.12213
- Code/Project: https://octo-models.github.io/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 Training a unified control policy in robotics presents unique challenges, requiring handling different robot embodiments, sensor setups, action spaces, task specifications, environments, and compute budgets.를 문제로 두고, In principle, collected ∗Lead authors, ordered alphabetically, see Section A for list of contributions.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Large policies pretrained on diverse robot datasets have the potential to transform robotic learning: instead of training new policies from scratch, such generalist robot policies ...
- **p. 1 / Abstract - extractive body cue:** However, to be widely applicable across a range of robotic learning scenarios, environments, and tasks, such policies need to handle diverse sensors and action spaces, ...
- **p. 1 / Abstract - extractive body cue:** In this work, we aim to lay the groundwork for developing open-source, widely applicable, generalist policies for robotic manipulation.
- **p. 1 / Abstract - extractive body cue:** As a first step, we introduce Octo, a large transformer-based policy trained on 800k trajectories from the Open X-Embodiment dataset, the largest robot manipulation dataset ...
- **p. 1 / Abstract - extractive body cue:** It can be instructed via language commands or goal images and can be effectively finetuned to robot setups with new sensory inputs and action spaces ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Training a unified control policy in robotics presents unique challenges, requiring handling different robot embodiments, sensor setups, action spaces, task specifications, environments, and compute budgets.
- **p. 2 / I. INTRODUCTION - extractive body cue:** Although these models represent significant steps toward a true "general-purpose robot model," they have been limited in multiple important aspects: they typically constrain downstream users ...

## Core Idea

- **p. 1 / I. INTRODUCTION - extractive body cue:** In principle, collected ∗Lead authors, ordered alphabetically, see Section A for list of contributions.
- **p. 2 / I. INTRODUCTION - extractive body cue:** Our primary contribution is Octo, a transformer-based policy pretrained on the largest robot manipulation dataset to date: 800k robot demonstrations from the Open X-Embodiment dataset ...
- **p. 3 / III. THE OCTO MODEL - extractive body cue:** It consists of three key parts: input tokenizers that transform
- **p. 4 / III. THE OCTO MODEL - extractive body cue:** This modular design enables us to add and remove observations or tasks during finetuning (see below).
- **p. 5 / III. THE OCTO MODEL - extractive body cue:** This enables our model to learn control mostly from self-supervised visual observations and reduces the burden on language annotation, similar to prior work on multi-context ...
- **p. 4 / III. THE OCTO MODEL - extractive body cue:** We use the t5-base (111M) model [74]. • Image observations and goals are passed through a shallow convolution stack, then split into a sequence of ...
- **p. 5 / III. THE OCTO MODEL - extractive body cue:** Training objective We use a conditional diffusion decoding head to predict continuous, multi-modal action distributions [34, 17].
- **p. 5 / III. THE OCTO MODEL - extractive body cue:** We use the same diffusion training objective during finetuning and update the full model, a recipe which outperformed those that freeze subsets of the pretrained ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | It also supports natural language instructions, goal images, observation histories, and multi-modal, chunked action prediction via diffusion decoding [17]. | image/video, language instruction, proprioception과 history | p. 3 (III. THE OCTO MODEL), p. 2 (I. INTRODUCTION) |
| State/latent | supports, natural, language, instructions, goal, images, observation, histories, multi-modal, chunked, action, prediction | language-grounded task state와 action-policy context | p. 3 (III. THE OCTO MODEL), p. 2 (I. INTRODUCTION), p. 4 (III. THE OCTO MODEL) |
| Output/action | The core of our model is a transformer architecture that maps arbitrary input tokens (created from observations and tasks) to output tokens (then decoded into actions), which can be trained on a ... | continuous action, pose 또는 action chunk | p. 2 (I. INTRODUCTION), p. 4 (III. THE OCTO MODEL), p. 3 (III. THE OCTO MODEL) |
| Objective/outcome | We use the AdamW optimizer [51] with an inverse square root decay learning rate schedule [97], with weight decay of 0.1 and gradient clipping of 1.0. | instruction following, task success, generalization과 latency | p. 5 (III. THE OCTO MODEL), p. 5 (III. THE OCTO MODEL), p. 3 (III. THE OCTO MODEL) |

## Main Claims and Actual Contribution

- **p. 1 / I. INTRODUCTION - extractive body cue:** In principle, collected ∗Lead authors, ordered alphabetically, see Section A for list of contributions.
- **p. 2 / I. INTRODUCTION - extractive body cue:** Our primary contribution is Octo, a transformer-based policy pretrained on the largest robot manipulation dataset to date: 800k robot demonstrations from the Open X-Embodiment dataset ...
- **p. 3 / III. THE OCTO MODEL - extractive body cue:** It consists of three key parts: input tokenizers that transform
- **p. 4 / III. THE OCTO MODEL - extractive body cue:** This modular design enables us to add and remove observations or tasks during finetuning (see below).
- **p. 5 / III. THE OCTO MODEL - extractive body cue:** This enables our model to learn control mostly from self-supervised visual observations and reduces the burden on language annotation, similar to prior work on multi-context ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 6: Model Scaling. The performance of Octo improves with larger model sizes on both UR5 and WidowX tasks. Success rates are averaged over 10 ...
- **p. 7 / 1) Can Octo control multiple robot embodiments and solve - extractive body cue:** We evaluated our model on the WidowX tasks using goal image conditioning and found that it achieved a 25% higher success rate than when evaluated ...
- **p. 7 / 1) Can Octo control multiple robot embodiments and solve - extractive body cue:** While the Octo model achieves high success on novel objects, zero-shot performance slightly degrades in a new scene, and high degradation for novel behaviors like ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | SYSTEM / EVALUATION SCOPE UNRESOLVED | do not infer unreported downstream behavior | p. 8 (Figure/Table caption), p. 7 (1) Can Octo control multiple robot embodiments and solve) |
| Embodiment/environment | We evaluate Octo's capabilities to control robots in environments from the pretraining data out-of-the-box and to efficiently finetune to new tasks and environments with small target domain datasets. | hardware/simulator version and reset protocol | p. 6 (1) Can Octo control multiple robot embodiments and solve), p. 7 (1) Can Octo control multiple robot embodiments and solve) |
| Dataset/benchmark | In the BridgeV2 domain, we performed a fine-grained analysis of the zero-shot capabilities in Table VII; measuring performance on setups seen in the dataset, and for novel environments, scenes, and skills. | role, split, size and leakage | p. 6 (1) Can Octo control multiple robot embodiments and solve), p. 7 (1) Can Octo control multiple robot embodiments and solve), p. 7 (1) Can Octo control multiple robot embodiments and solve), p. 5 (III. THE OCTO MODEL) |
| Metric | Fig. 6: Model Scaling. The performance of Octo improves with larger model sizes on both UR5 and WidowX tasks. Success rates are averaged over 10 trials on one language-conditioned task per robot. ... | definition, denominator, direction and uncertainty | p. 8 (Figure/Table caption), p. 6 (1) Can Octo control multiple robot embodiments and solve), p. 7 (1) Can Octo control multiple robot embodiments and solve) |
| Baseline/ablation | On average across the six evaluation setups (detailed in Appendix F), Octo outperforms the next best baseline by 52%. | fair input/data/compute/action matching | p. 7 (1) Can Octo control multiple robot embodiments and solve), p. 5 (III. THE OCTO MODEL), p. 5 (III. THE OCTO MODEL) |

## Explicit Limitations and Failure Boundary

- **p. 7 / 1) Can Octo control multiple robot embodiments and solve - extractive body cue:** While the Octo model achieves high success on novel objects, zero-shot performance slightly degrades in a new scene, and high degradation for novel behaviors like ...
- **p. 5 / III. THE OCTO MODEL - extractive body cue:** Finally, we zero-pad any missing camera channels and align the gripper action spaces between the datasets such that a gripper command of +1 means "the ...
- **p. 5 / III. THE OCTO MODEL - extractive body cue:** (1) The hyperparameters α, γ, and σ correspond to the noise schedule: we use the standard cosine schedule from [66].

## Why Read It

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 Training a unified control policy in robotics presents unique challenges, requiring handling different robot embodiments, sensor setups, action spaces, task specifications, environments, and compute budgets.를 문제로 두고, In principle, collected ∗Lead authors, ordered alphabetically, see Section A for list of contributions.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 4 (III. THE OCTO MODEL), p. 5 (III. THE OCTO MODEL), p. 5 (III. THE OCTO MODEL) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (17 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** Training a unified control policy in robotics presents unique challenges, requiring handling different robot embodiments, sensor setups, action spaces, task specifications, environments, and compute budgets. (p. 2, I. INTRODUCTION).
- **Actual contribution:** In principle, collected ∗Lead authors, ordered alphabetically, see Section A for list of contributions. (p. 1, I. INTRODUCTION).
- **Evaluation boundary:** Fig. 6: Model Scaling. The performance of Octo improves with larger model sizes on both UR5 and WidowX tasks. Success rates are averaged over 10 trials on one language-conditioned task ... (p. 8, Figure/Table caption).
- **Explicit failure boundary:** Although these models represent significant steps toward a true "general-purpose robot model," they have been limited in multiple important aspects: they typically constrain downstream users to a pre-defined and often ... (p. 2, I. INTRODUCTION).
