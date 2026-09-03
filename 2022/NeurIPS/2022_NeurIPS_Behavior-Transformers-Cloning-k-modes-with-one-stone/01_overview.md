# Behavior Transformers: Cloning k modes with one stone

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.neurips.cc/paper_files/paper/2022/hash/90d17e882adbdda42349db6f50123817-Abstract-Conference.html.
> PDF retrieval source: https://proceedings.neurips.cc/paper_files/paper/2022/hash/90d17e882adbdda42349db6f50123817-Abstract-Conference.html. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2022 / NeurIPS
- Authors: not duplicated here when not verified in the registry source
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: Robotics, Imitation Learning, Transformer, multimodal actions
- Official paper: https://proceedings.neurips.cc/paper_files/paper/2022/hash/90d17e882adbdda42349db6f50123817-Abstract-Conference.html
- Full-text retrieval: https://proceedings.neurips.cc/paper_files/paper/2022/hash/90d17e882adbdda42349db6f50123817-Abstract-Conference.html
- Code/Project: https://mahis.life/bet/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

RL, IL, offline learning, and robot data의 il 문제를 이해하기 위해 읽는다. 본문은 However, unlike previous efforts similar to Mixture Density Networks (MDN) to do so, whose limitations have been explored in Florence et al.를 문제로 두고, In this work, we present Behavior Transformers (BeT), a new method for learning behaviors from rich, distributionally multi-modal data.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** While behavior learning has made impressive progress in recent times, it lags behind computer vision and natural language processing due to its inability to leverage ...
- **p. 1 / Abstract - extractive body cue:** Human behaviors have wide variance, multiple modes, and human demonstrations typically do not come with reward labels.
- **p. 1 / Abstract - extractive body cue:** These properties limit the applicability of current methods in Offline RL and Behavioral Cloning to learn from large, pre-collected datasets.
- **p. 1 / Abstract - extractive body cue:** In this work, we present Behavior Transformer (BeT), a new technique to model unlabeled demonstration data with multiple modes.
- **p. 1 / Abstract - extractive body cue:** BeT retrofits standard transformer architectures with action discretization coupled with a multi-task action correction inspired by offset prediction in object detection.
- **p. 3 / 1 Introduction - extractive body cue:** However, unlike previous efforts similar to Mixture Density Networks (MDN) to do so, whose limitations have been explored in Florence et al.
- **p. 3 / 1 Introduction - extractive body cue:** Limitations of traditional MSEbased BC: While MSE-based BC has been able to solve a variety of tasks [9, 77], it assumes that the data distribution ...

## Core Idea

- **p. 2 / 1 Introduction - extractive body cue:** In this work, we present Behavior Transformers (BeT), a new method for learning behaviors from rich, distributionally multi-modal data.
- **p. 4 / 1 Introduction - extractive body cue:** To address this, we propose a new factoring of the action prediction task by dividing each action in two parts: a categorical variable denoting an ...
- **p. 1 / Abstract - extractive body cue:** In this work, we present Behavior Transformer (BeT), a new technique to model unlabeled demonstration data with multiple modes.
- **p. 1 / 1 Introduction - extractive body cue:** This is in stark contrast to vision and language tasks, where pretrained models and data-driven priors are the norm [19, 11, 32, 6], which allows ...
- **p. 2 / 1 Introduction - extractive body cue:** This allows us to model high-dimensional, continuous multi-modal action distributions as categorical distributions without learning complicated generative models [42, 20].
- **p. 4 / 1 Introduction - extractive body cue:** We use a transformer decoder model, namely minGPT [11], with minor modifications, as our backbone.
- **p. 3 / 1 Introduction - extractive body cue:** To operationalize these two features in a single behavior model, we make use of transformers since (a) they are effective in utilizing prior observational history, ...
- **p. 4 / 1 Introduction - extractive body cue:** (C) Rollouts from BeT in test time, where it first chooses a bin and then picks the corresponding offset to reconstruct a continuous action. distributions ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | 2 Behavior Transformers Given a dataset of continuous observation and action pairs D ⌘{(o, a)} ⇢O ⇥A that contains behaviors we are interested in, our goal is to learn a behavior policy ... | observation history와 expert trajectory/action | p. 3 (1 Introduction), p. 5 (1 Introduction) |
| State/latent | Behavior, Transformers, Given, dataset, continuous, observation, action, pairs, contains, behaviors, interested, goal | behavior policy와 temporal action context | p. 3 (1 Introduction), p. 5 (1 Introduction), p. 1 (1 Introduction) |
| Output/action | For each observation oi in the sequence, the head produces a k ⇥dim(A) matrix with k proposed residual action vectors, ⇣ ha(j) i i ⌘k j=1 = (hˆa(1) i i, hˆa(2) i ... | predicted action 또는 action chunk | p. 5 (1 Introduction), p. 1 (1 Introduction), p. 3 (1 Introduction) |
| Objective/outcome | Following this convention, our objective is to find the parameter ✓that maximizes the probability of the observed data ✓⇤:= arg max ✓ Y t P(at / ot; ✓) (1) When the model ... | imitation error, task success, robustness와 compounding error | p. 3 (1 Introduction), p. 4 (1 Introduction), p. 4 (1 Introduction) |

## Main Claims and Actual Contribution

- **p. 2 / 1 Introduction - extractive body cue:** In this work, we present Behavior Transformers (BeT), a new method for learning behaviors from rich, distributionally multi-modal data.
- **p. 4 / 1 Introduction - extractive body cue:** To address this, we propose a new factoring of the action prediction task by dividing each action in two parts: a categorical variable denoting an ...
- **p. 1 / Abstract - extractive body cue:** In this work, we present Behavior Transformer (BeT), a new technique to model unlabeled demonstration data with multiple modes.
- **p. 1 / 1 Introduction - extractive body cue:** This is in stark contrast to vision and language tasks, where pretrained models and data-driven priors are the norm [19, 11, 32, 6], which allows ...
- **p. 2 / 1 Introduction - extractive body cue:** This allows us to model high-dimensional, continuous multi-modal action distributions as categorical distributions without learning complicated generative models [42, 20].
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: Unconditional rollouts from BeT models trained from multi-modal demonstartions on the CARLA, Block push, and Franka Kitchen environments. Due to the multi-modal architecture ...
- **p. 6 / 3 Experiments - extractive body cue:** We see that BeT outperforms all other methods in all environments except CARLA, where it is narrowly outperformed by LWR.
- **p. 6 / 3 Experiments - extractive body cue:** While IBC is slower than explicit BC models because of their sampling requirements, they have been shown to learn well on multi-modal data, and outperform ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 2 (Figure/Table caption), p. 6 (3 Experiments) |
| Embodiment/environment | 3.1 Environments and datasets We experiment with five broad environments. | hardware/simulator version and reset protocol | p. 5 (3 Experiments), p. 5 (3 Experiments) |
| Dataset/benchmark | We use the relay policy learning dataset with 566 demonstrations collected by human participants wearing VR headsets. | role, split, size and leakage | p. 5 (3 Experiments), p. 5 (3 Experiments), p. 6 (3 Experiments), p. 6 (3 Experiments) |
| Metric | Reward is normalized with respect to the best performing model. | definition, denominator, direction and uncertainty | p. 9 (3 Experiments), p. 8 (3 Experiments), p. 5 (3 Experiments) |
| Baseline/ablation | Figure 5: Comparison between an RBC model and two BeT models, trained with and without historical context on a dataset with three distinct modes. BeT with history is better able to capture ... | fair input/data/compute/action matching | p. 8 (Figure/Table caption), p. 6 (3 Experiments), p. 6 (3 Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 6 / 3 Experiments - extractive body cue:** Since the models are all behavioral cloning algorithms, they share the failure mode of failing once the observations go out of distribution (OOD).
- **p. 6 / 3 Experiments - extractive body cue:** On the other hand, we observe that BeT's primary failure mode is not realizing a block has not completely entered the target yet, while other ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2: Comparison between a regular MSE-based BC model and a BeT models that can capture multi-modal distributions. The MSE-BC model takes 0 action to ...
- **p. 8 / 3 Experiments - extractive body cue:** We see that they may perform well sometimes but overall still fall short of our k-means binning approach.
- **p. 9 / 4 Related Work - extractive body cue:** BeT falls under the second category, as it is a behavior cloning model.
- **p. 8 / 3 Experiments - extractive body cue:** We see in Table 2 that in CARLA and Block push, BeT covers all the modes of the demonstration data, even in the few cases ...

## Why Read It

RL, IL, offline learning, and robot data의 il 문제를 이해하기 위해 읽는다. 본문은 However, unlike previous efforts similar to Mixture Density Networks (MDN) to do so, whose limitations have been explored in Florence et al.를 문제로 두고, In this work, we present Behavior Transformers (BeT), a new method for learning behaviors from rich, distributionally multi-modal data.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 3 (1 Introduction), p. 3 (1 Introduction), p. 5 (1 Introduction), p. 1 (1 Introduction), p. 1 (1 Introduction), p. 4 (1 Introduction) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (14 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** However, unlike previous efforts similar to Mixture Density Networks (MDN) to do so, whose limitations have been explored in Florence et al. (p. 3, 1 Introduction).
- **Actual contribution:** In this work, we present Behavior Transformers (BeT), a new method for learning behaviors from rich, distributionally multi-modal data. (p. 2, 1 Introduction).
- **Evaluation boundary:** Figure 5: Comparison between an RBC model and two BeT models, trained with and without historical context on a dataset with three distinct modes. BeT with history is better able ... (p. 8, Figure/Table caption).
- **Explicit failure boundary:** Since the models are all behavioral cloning algorithms, they share the failure mode of failing once the observations go out of distribution (OOD). (p. 6, 3 Experiments).
