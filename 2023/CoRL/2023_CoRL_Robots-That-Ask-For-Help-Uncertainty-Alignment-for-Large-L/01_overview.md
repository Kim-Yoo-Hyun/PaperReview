# Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (24 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2307.01928.
> PDF retrieval source: https://arxiv.org/pdf/2307.01928. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2023 / CoRL
- Authors: not duplicated here when not verified in the registry source
- Primary track: World models, safety, uncertainty, and recovery
- Tier: REFERENCE
- Tags: Robotics, LLM planning, uncertainty, conformal prediction, human intervention
- Official paper: https://arxiv.org/abs/2307.01928
- Full-text retrieval: https://arxiv.org/pdf/2307.01928
- Code/Project: https://robot-help.github.io/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (24 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

World models, safety, uncertainty, and recovery의 safety 문제를 이해하기 위해 읽는다. 본문은 However, one of the major challenges with current LLMs is their tendency to hallucinate, i.e., to confidently generate outputs that are plausible but incorrect and untethered from reality.를 문제로 두고, Here, we present a novel extension of CP to multi-step settings that tackles this challenge.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Large language models (LLMs) exhibit a wide range of promising capabilities - from step-by-step planning to commonsense reasoning - that may provide utility for robots, ...
- **p. 1 / Abstract - extractive body cue:** In this work, we present KNOWNO, which is a framework for measuring and aligning the uncertainty of LLM-based planners such that they know when they ...
- **p. 1 / Abstract - extractive body cue:** KNOWNO builds on the theory of conformal prediction to provide statistical guarantees on task completion while minimizing human help in complex multi-step planning settings.
- **p. 1 / Abstract - extractive body cue:** Experiments across a variety of simulated and real robot setups that involve tasks with different modes of ambiguity (e.g., from spatial to numeric uncertainties, from ...
- **p. 1 / Abstract - extractive body cue:** KNOWNO can be used with LLMs out of the box without modelfinetuning, and suggests a promising lightweight approach to modeling uncertainty that can complement and ...
- **p. 1 / 1 Introduction - extractive body cue:** However, one of the major challenges with current LLMs is their tendency to hallucinate, i.e., to confidently generate outputs that are plausible but incorrect and ...
- **p. 5 / 1 Introduction - extractive body cue:** However, the original CP formulation cannot be applied here since the context xt between steps are dependent; moreover, the robot's actions at step t influence ...

## Core Idea

- **p. 5 / 1 Introduction - extractive body cue:** Here, we present a novel extension of CP to multi-step settings that tackles this challenge.
- **p. 2 / 1 Introduction - extractive body cue:** We propose KNOWNO- Know When You Don't Know - a framework for aligning the uncertainty of LLM-based planners utilizing the theory of conformal prediction (CP) ...
- **p. 4 / 1 Introduction - extractive body cue:** We introduce CP below, and then present the different practical settings we consider (possibly involving multiple planning steps and/or multiple correct plans per step).
- **p. 5 / 1 Introduction - extractive body cue:** Suppose that each data point consists of a sequence of augmented context x = (˜x0,˜x1,...,˜xT-1) and true labels y = (y0,y1,...,yT-1), where T is the ...
- **p. 6 / 1 Introduction - extractive body cue:** We extend our method and confidence guarantees to this setting for both single- and multi-step problems in Section A3 and Section A4.
- **p. 2 / 1 Introduction - extractive body cue:** Language model planners can generate step-by-step robot plans, where each step y is composed of variable-length sequences of symbols (σ1,σ2,...,σk), e.g., text tokens as input ...
- **p. 3 / 1 Introduction - extractive body cue:** The environment e can be formulated as a partially observable Markov decision process (POMDP): at any given state st at time t, given a user ...
- **p. 3 / 1 Introduction - extractive body cue:** Our policy π is composed of four parts (Fig.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The environment e can be formulated as a partially observable Markov decision process (POMDP): at any given state st at time t, given a user instruction ℓ, the robot executes an action ... | observation, uncertainty/risk estimate와 task command | p. 3 (1 Introduction), p. 2 (1 Introduction) |
| State/latent | environment, formulated, partially, observable, Markov, decision, process, POMDP, given, state, time, user | safe set, recovery state 또는 constraint margin | p. 3 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction) |
| Output/action | Language model planners can generate step-by-step robot plans, where each step y is composed of variable-length sequences of symbols (σ1,σ2,...,σk), e.g., text tokens as input to a language-conditioned policy [1] (see Fig. | shielded, recovery 또는 safe action | p. 2 (1 Introduction), p. 3 (1 Introduction), p. 1 (1 Introduction) |
| Objective/outcome | This eliminates plans that the LLM considers unlikely and reduces the problem of next-step prediction down to a single next-token prediction - aligning with LLM log-likelihood loss functions and LLM training data ... | task return과 violation/failure probability | p. 3 (1 Introduction), p. 1 (Abstract), p. 2 (1 Introduction) |

## Main Claims and Actual Contribution

- **p. 5 / 1 Introduction - extractive body cue:** Here, we present a novel extension of CP to multi-step settings that tackles this challenge.
- **p. 2 / 1 Introduction - extractive body cue:** We propose KNOWNO- Know When You Don't Know - a framework for aligning the uncertainty of LLM-based planners utilizing the theory of conformal prediction (CP) ...
- **p. 4 / 1 Introduction - extractive body cue:** We introduce CP below, and then present the different practical settings we consider (possibly involving multiple planning steps and/or multiple correct plans per step).
- **p. 5 / 1 Introduction - extractive body cue:** Suppose that each data point consists of a sequence of augmented context x = (˜x0,˜x1,...,˜xT-1) and true labels y = (y0,y1,...,yT-1), where T is the ...
- **p. 6 / 1 Introduction - extractive body cue:** We extend our method and confidence guarantees to this setting for both single- and multi-step problems in Section A3 and Section A4.
- **p. 8 / 4 Experiments - extractive body cue:** Nonetheless, KnowNo still achieves 1-ϵ target success rate, as the coverage guarantee from CP makes no assumption about the LLM confidences (e.g., calibrated or accurate) ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: KNOWNO uses Conformal Prediction (CP) to align the uncertainty of LLM planners. Given a language instruction, an LLM generates possible next steps and ...
- **p. 7 / 4 Experiments - extractive body cue:** KNOWNO achieves target task success rate consistently.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 8 (4 Experiments), p. 2 (Figure/Table caption) |
| Embodiment/environment | In future deployment, we envision that a robot can interact with an end-user (e.g., in a home) to collect a dataset through interactions with the human; the human can provide their true ... | hardware/simulator version and reset protocol | p. 6 (4 Experiments), p. 7 (4 Experiments) |
| Dataset/benchmark | A robot arm is asked to rearrange objects on a table in the PyBullet simulator [17] (Fig. | role, split, size and leakage | p. 6 (4 Experiments), p. 7 (4 Experiments), p. 6 (4 Experiments), p. 8 (4 Experiments) |
| Metric | 4 we vary the target error rate ϵ and show the curves of task success rate vs. prediction set size and human help rate averaged over the three settings. | definition, denominator, direction and uncertainty | p. 7 (4 Experiments), p. 8 (4 Experiments), p. 6 (4 Experiments) |
| Baseline/ablation | Figure 1: KNOWNO uses Conformal Prediction (CP) to align the uncertainty of LLM planners. Given a language instruction, an LLM generates possible next steps and its confidences (scores) in these options. CP ... | fair input/data/compute/action matching | p. 2 (Figure/Table caption), p. 6 (4 Experiments), p. 6 (4 Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 9 / 6 Discussion - extractive body cue:** Limitations and future work: The primary limitation of our work is that the task completion guarantee assumes environments (objects) are fully grounded in the text ...
- **p. 9 / 6 Discussion - extractive body cue:** Another limitation is that, for the task guarantee to hold, the human needs to faithfully provide help when the robot needs it.
- **p. 7 / 4 Experiments - extractive body cue:** First, we investigate whether KNOWNO and the baselines achieve a given target task success rate consistently in the three settings - we set the failure ...
- **p. 6 / 4 Experiments - extractive body cue:** Note that the ϵ level is not used in Prompt Set or Binary, and so the user cannot explicitly control the task success rate.
- **p. 7 / 4 Experiments - extractive body cue:** Simple Set and Ensemble Set cannot achieve coverage consistently.
- **p. 8 / 4 Experiments - extractive body cue:** Target success guarantee from KnowNo is robust to varying LLM choice.
- **p. 8 / 4 Experiments - extractive body cue:** Can you dispose of it?"), and ones that potentially involve unsafe actions (e.g., "place the bowl in the microwave."; there is a plastic bowl and ...

## Why Read It

World models, safety, uncertainty, and recovery의 safety 문제를 이해하기 위해 읽는다. 본문은 However, one of the major challenges with current LLMs is their tendency to hallucinate, i.e., to confidently generate outputs that are plausible but incorrect and untethered from reality.를 문제로 두고, Here, we present a novel extension of CP to multi-step settings that tackles this challenge.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1 Introduction), p. 5 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 4 (1 Introduction), p. 2 (1 Introduction) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
