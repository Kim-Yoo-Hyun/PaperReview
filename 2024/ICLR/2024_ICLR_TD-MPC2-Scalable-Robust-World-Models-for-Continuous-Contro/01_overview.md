# TD-MPC2: Scalable, Robust World Models for Continuous Control

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (31 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2310.16828.
> PDF retrieval source: https://arxiv.org/pdf/2310.16828. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / ICLR
- Authors: not duplicated here when not verified in the registry source
- Primary track: World models, safety, uncertainty, and recovery
- Tier: CORE
- Tags: Robotics, world model, continuous control, model predictive control
- Official paper: https://arxiv.org/abs/2310.16828
- Full-text retrieval: https://arxiv.org/pdf/2310.16828
- Code/Project: https://www.nicklashansen.com/td-mpc2/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (31 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

World models, safety, uncertainty, and recovery의 safety 문제를 이해하기 위해 읽는다. 본문은 However, accurately predicting raw future observations (e.g., images or proprioceptive features) over long time horizons is a difficult problem, and does not necessarily lead to effective control (Lambert et al., 2020).를 문제로 두고, In this work, we present TDMPC2: a significant step towards achieving this goal.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** TD-MPC is a model-based reinforcement learning (RL) algorithm that performs local trajectory optimization in the latent space of a learned implicit (decoderfree) world model.
- **p. 1 / ABSTRACT - extractive body cue:** In this work, we present TD-MPC2: a series of improvements upon the TD-MPC algorithm.
- **p. 1 / ABSTRACT - extractive body cue:** We demonstrate that TD-MPC2 improves significantly over baselines across 104 online RL tasks spanning 4 diverse task domains, achieving consistently strong results with a single ...
- **p. 1 / ABSTRACT - extractive body cue:** We further show that agent capabilities increase with model and data size, and successfully train a single 317M parameter agent to perform 80 tasks across ...
- **p. 1 / ABSTRACT - extractive body cue:** We conclude with an account of lessons, opportunities, and risks associated with large TD-MPC2 agents.
- **p. 3 / 2 BACKGROUND - extractive body cue:** However, accurately predicting raw future observations (e.g., images or proprioceptive features) over long time horizons is a difficult problem, and does not necessarily lead to ...
- **p. 5 / 2 BACKGROUND - extractive body cue:** However, in the general case where domain knowledge cannot be assumed, we may instead choose to learn the task embeddings (and, implicitly, task relations) from ...

## Core Idea

- **p. 2 / 1 INTRODUCTION - extractive body cue:** In this work, we present TDMPC2: a significant step towards achieving this goal.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Our algorithmic contributions, which have been key to achieving this milestone, are two-fold: (1) improved algorithmic robustness by revisiting core design choices, and (2) careful ...
- **p. 1 / ABSTRACT - extractive body cue:** In this work, we present TD-MPC2: a series of improvements upon the TD-MPC algorithm.
- **p. 3 / 2 BACKGROUND - extractive body cue:** We introduce the TD-MPC2 algorithm in the following, and provide a full list of algorithmic improvements in Appendix A.
- **p. 3 / 2 BACKGROUND - extractive body cue:** Specifically, we propose a series of improvements to the TD-MPC algorithm, which have been key to achieving strong algorithmic robustness (can use the same hyperparameters ...
- **p. 3 / 2 BACKGROUND - extractive body cue:** The TD-MPC2 architecture is shown in Figure 3 and consists of five components: Encoder z = h(s, e) ▷Maps observations to their latent representations Latent ...
- **p. 1 / ABSTRACT - extractive body cue:** TD-MPC is a model-based reinforcement learning (RL) algorithm that performs local trajectory optimization in the latent space of a learned implicit (decoderfree) world model.
- **p. 5 / 2 BACKGROUND - extractive body cue:** To do so, we zero-pad all model inputs and outputs to their largest respective dimensions, and mask out invalid action dimensions in predictions made by ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The TD-MPC2 architecture is shown in Figure 3 and consists of five components: Encoder z = h(s, e) ▷Maps observations to their latent representations Latent dynamics z′ = d(z, a, e) ▷Models ... | observation, uncertainty/risk estimate와 task command | p. 3 (2 BACKGROUND), p. 5 (2 BACKGROUND) |
| State/latent | TD-MPC2, architecture, Figure, consists, five, components, Encoder, Maps, observations, latent, representations, dynamics | safe set, recovery state 또는 constraint margin | p. 3 (2 BACKGROUND), p. 5 (2 BACKGROUND), p. 2 (1 INTRODUCTION) |
| Output/action | To do so, we zero-pad all model inputs and outputs to their largest respective dimensions, and mask out invalid action dimensions in predictions made by the policy prior p during both training ... | shielded, recovery 또는 safe action | p. 5 (2 BACKGROUND), p. 2 (1 INTRODUCTION), p. 2 (2 BACKGROUND) |
| Objective/outcome | The h, d, R, Q components are jointly optimized to minimize the objective L (θ) .= E (s,a,r,s′)0:H∼B   H X t=0 λt   ∥z′ t -sg(h(s′ t))∥2 2 / ... | task return과 violation/failure probability | p. 4 (2 BACKGROUND), p. 3 (2 BACKGROUND), p. 5 (2 BACKGROUND) |

## Main Claims and Actual Contribution

- **p. 2 / 1 INTRODUCTION - extractive body cue:** In this work, we present TDMPC2: a significant step towards achieving this goal.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Our algorithmic contributions, which have been key to achieving this milestone, are two-fold: (1) improved algorithmic robustness by revisiting core design choices, and (2) careful ...
- **p. 1 / ABSTRACT - extractive body cue:** In this work, we present TD-MPC2: a series of improvements upon the TD-MPC algorithm.
- **p. 3 / 2 BACKGROUND - extractive body cue:** We introduce the TD-MPC2 algorithm in the following, and provide a full list of algorithmic improvements in Appendix A.
- **p. 3 / 2 BACKGROUND - extractive body cue:** Specifically, we propose a series of improvements to the TD-MPC algorithm, which have been key to achieving strong algorithmic robustness (can use the same hyperparameters ...
- **p. 22 / Figure/Table caption - extractive body cue:** Figure 13. Single-task Meta-World results. Success rate (%) as a function of environment steps. TD-MPC2 performance is comparable to existing methods on easy tasks, while ...
- **p. 23 / Figure/Table caption - extractive body cue:** Figure 16. Single-task MyoSuite results. Success rate (%) as a function of environment steps. This task domain includes high-dimensional contact-rich musculoskeletal motor control (A ∈R39) ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 4. Single-task RL. Episode return (DMControl) and success rate (others) as a function of environment steps across 104 continuous control tasks spanning 4 diverse ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 22 (Figure/Table caption), p. 23 (Figure/Table caption) |
| Embodiment/environment | However, TD-MPC2 can be readily applied to tasks with other input 120k environment steps corresponds to 20 episodes in DMControl and 100 episodes in Meta-World. | hardware/simulator version and reset protocol | p. 8 (4.1 RESULTS), p. 6 (4 EXPERIMENTS) |
| Dataset/benchmark | (Left) Normalized score as a function of model size on the two 80-task and 30-task datasets. | role, split, size and leakage | p. 8 (4.1 RESULTS), p. 6 (4 EXPERIMENTS), p. 7 (4.1 RESULTS), p. 7 (4.1 RESULTS) |
| Metric | To summarize agent performance with a single metric, we produce a normalized score that is an average of all individual task success rates (Meta-World) and episode returns normalized to the [0, 100] ... | definition, denominator, direction and uncertainty | p. 7 (4.1 RESULTS), p. 5 (Figure/Table caption), p. 6 (4 EXPERIMENTS) |
| Baseline/ablation | TD-MPC2 outperforms baselines by a large margin on these tasks, despite using the same hyperparameters across all tasks. | fair input/data/compute/action matching | p. 6 (4.1 RESULTS), p. 6 (4 EXPERIMENTS), p. 9 (4.1 RESULTS) |

## Explicit Limitations and Failure Boundary

- **p. 9 / 4.1 RESULTS - extractive body cue:** While we are excited by the potential of generalist world models, several challenges remain: (i) misspecification of task rewards can lead to unintended outcomes (Clark ...
- **p. 22 / Figure/Table caption - extractive body cue:** Figure 13. Single-task Meta-World results. Success rate (%) as a function of environment steps. TD-MPC2 performance is comparable to existing methods on easy tasks, while ...
- **p. 7 / 4.1 RESULTS - extractive body cue:** Notably, performance does not appear to have saturated for our largest models (317M parameters) on either dataset, and we can thus expect results to continue ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 2. Tasks. TD-MPC2 performs 104 diverse tasks from (left to right) DMControl (Tassa et al., 2018), Meta-World (Yu et al., 2019), ManiSkill2 (Gu et ...
- **p. 7 / 4.1 RESULTS - extractive body cue:** While our work mainly focuses on the scaling and robustness of world models, we also explore the efficacy of finetuning pretrained world models for few-shot ...
- **p. 8 / 4.1 RESULTS - extractive body cue:** We observe that all of our proposed improvements contribute meaningfully to the robustness and strong performance of TD-MPC2 in both single-task RL and multi-task RL.
- **p. 9 / 4.1 RESULTS - extractive body cue:** We firmly believe that improving algorithmic robustness will continue to have profound impact on the field.

## Why Read It

World models, safety, uncertainty, and recovery의 safety 문제를 이해하기 위해 읽는다. 본문은 However, accurately predicting raw future observations (e.g., images or proprioceptive features) over long time horizons is a difficult problem, and does not necessarily lead to effective control (Lambert et al., 2020).를 문제로 두고, In this work, we present TDMPC2: a significant step towards achieving this goal.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 3 (2 BACKGROUND), p. 5 (2 BACKGROUND), p. 5 (2 BACKGROUND), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (2 BACKGROUND) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (31 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** However, accurately predicting raw future observations (e.g., images or proprioceptive features) over long time horizons is a difficult problem, and does not necessarily lead to effective control (Lambert et al., ... (p. 3, 2 BACKGROUND).
- **Actual contribution:** In this work, we present TDMPC2: a significant step towards achieving this goal. (p. 2, 1 INTRODUCTION).
- **Evaluation boundary:** Figure 16. Single-task MyoSuite results. Success rate (%) as a function of environment steps. This task domain includes high-dimensional contact-rich musculoskeletal motor control (A ∈R39) with a physiologically accurate robot ... (p. 23, Figure/Table caption).
- **Explicit failure boundary:** While we are excited by the potential of generalist world models, several challenges remain: (i) misspecification of task rewards can lead to unintended outcomes (Clark & Amodei, 2016) that may ... (p. 9, 4.1 RESULTS).
