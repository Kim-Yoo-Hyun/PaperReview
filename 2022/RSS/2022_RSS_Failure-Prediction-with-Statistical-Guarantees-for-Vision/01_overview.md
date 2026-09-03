# Failure Prediction with Statistical Guarantees for Vision-Based Robot Control

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2202.05894.
> PDF retrieval source: https://arxiv.org/pdf/2202.05894. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2022 / RSS
- Authors: not duplicated here when not verified in the registry source
- Primary track: World models, safety, uncertainty, and recovery
- Tier: REFERENCE
- Tags: Robotics, failure prediction, vision-based control, statistical guarantees, safe deployment
- Official paper: https://arxiv.org/abs/2202.05894
- Full-text retrieval: https://arxiv.org/pdf/2202.05894
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

World models, safety, uncertainty, and recovery의 safety 문제를 이해하기 위해 읽는다. 본문은 Given access to a black-box control policy (e.g., one with neural network components), our goal is to train a failure predictor for this policy.를 문제로 두고, Our primary contribution is to develop an approach for learning a failure predictor with guaranteed bounds on error rates, given a black-box control policy that operates on a robotic system with high-dimensional ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** We are motivated by the problem of performing failure prediction for safety-critical robotic systems with highdimensional sensor observations (e.g., vision).
- **p. 1 / Abstract - extractive body cue:** Given access to a black-box control policy (e.g., in the form of a neural network) and a dataset of training environments, we present an approach ...
- **p. 1 / Abstract - extractive body cue:** In order to achieve this, we utilize techniques from Probably Approximately Correct (PAC)-Bayes generalization theory.
- **p. 1 / Abstract - extractive body cue:** In addition, we present novel class-conditional bounds that allow us to trade-off the relative rates of false-positive vs. false-negative errors.
- **p. 1 / Abstract - extractive body cue:** We propose algorithms that train failure predictors (that take as input the history of sensor observations) by minimizing our theoretical error bounds.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Given access to a black-box control policy (e.g., one with neural network components), our goal is to train a failure predictor for this policy.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Our primary contribution is to develop an approach for learning a failure predictor with guaranteed bounds on error rates, given a black-box control policy that ...

## Core Idea

- **p. 1 / I. INTRODUCTION - extractive body cue:** Our primary contribution is to develop an approach for learning a failure predictor with guaranteed bounds on error rates, given a black-box control policy that ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** box policy for training purposes, we present a reduction of the failure prediction problem (which involves non-i.i.d. data in the form of sensor observations) to ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** In addition, we develop novel classconditional bounds that allow us to trade-off the relative rates of false negative vs. false positive errors.
- **p. 3 / III. PROBLEM FORMULATION - extractive body cue:** Below we present the two optimization problems corresponding to misclassification error and classconditional misclassification error: inf DF E E∼DE E f∼DF  C(rf(E, π))  ...
- **p. 3 / III. PROBLEM FORMULATION - extractive body cue:** To evaluate the performance of the failure predictor, we introduce the error of applying the predictor f in an environment E where a policy π ...
- **p. 3 / III. PROBLEM FORMULATION - extractive body cue:** Let rf : E × Π →X T × YT denote the function that ‘rolls out' the system with the given policy and the predictor ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | We consider a deterministic, black-box task policy π : O →A that maps (potentially a history of) observations to a control input. | observation, uncertainty/risk estimate와 task command | p. 3 (III. PROBLEM FORMULATION), p. 1 (I. INTRODUCTION) |
| State/latent | consider, deterministic, black-box, task, policy, maps, potentially, history, observations, control, input, primary | safe set, recovery state 또는 constraint margin | p. 3 (III. PROBLEM FORMULATION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| Output/action | Our primary contribution is to develop an approach for learning a failure predictor with guaranteed bounds on error rates, given a black-box control policy that operates on a robotic system with high-dimensional ... | shielded, recovery 또는 safe action | p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION) |
| Objective/outcome | Our goal is to use the training environments S to learn failure predictors that minimize the errors and provably generalize to unseen environments drawn from the distribution DE. | task return과 violation/failure probability | p. 3 (III. PROBLEM FORMULATION), p. 3 (III. PROBLEM FORMULATION), p. 2 (III. PROBLEM FORMULATION) |

## Main Claims and Actual Contribution

- **p. 1 / I. INTRODUCTION - extractive body cue:** Our primary contribution is to develop an approach for learning a failure predictor with guaranteed bounds on error rates, given a black-box control policy that ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** box policy for training purposes, we present a reduction of the failure prediction problem (which involves non-i.i.d. data in the form of sensor observations) to ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** In addition, we develop novel classconditional bounds that allow us to trade-off the relative rates of false negative vs. false positive errors.
- **p. 3 / III. PROBLEM FORMULATION - extractive body cue:** Below we present the two optimization problems corresponding to misclassification error and classconditional misclassification error: inf DF E E∼DE E f∼DF  C(rf(E, π))  ...
- **p. 3 / III. PROBLEM FORMULATION - extractive body cue:** To evaluate the performance of the failure predictor, we introduce the error of applying the predictor f in an environment E where a policy π ...
- **p. 8 / V. EXPERIMENTAL RESULTS - extractive body cue:** In order to evaluate the failure predictor on policies with different task success rates, we choose three different policies saved at different epochs during training.
- **p. 7 / V. EXPERIMENTAL RESULTS - extractive body cue:** We aim to examine the improvement in safety of the policy with the addition of the failure predictor; thus, we test in settings that are ...
- **p. 8 / V. EXPERIMENTAL RESULTS - extractive body cue:** 5 in the drone example, we achieve strong bounds on conditional misclassification Fig.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 8 (V. EXPERIMENTAL RESULTS), p. 7 (V. EXPERIMENTAL RESULTS) |
| Embodiment/environment | In order to create different environments for the robot, we obtained 50 mugs of diverse geometries from the ShapeNet dataset [49]. | hardware/simulator version and reset protocol | p. 8 (V. EXPERIMENTAL RESULTS), p. 6 (V. EXPERIMENTAL RESULTS) |
| Dataset/benchmark | We train the failure predictor in simulation and apply it on a hardware platform with a Parrot Swing drone (Fig. | role, split, size and leakage | p. 8 (V. EXPERIMENTAL RESULTS), p. 6 (V. EXPERIMENTAL RESULTS), p. 6 (V. EXPERIMENTAL RESULTS), p. 7 (V. EXPERIMENTAL RESULTS) |
| Metric | In order to evaluate the failure predictor on policies with different task success rates, we choose three different policies saved at different epochs during training. | definition, denominator, direction and uncertainty | p. 8 (V. EXPERIMENTAL RESULTS), p. 6 (Figure/Table caption), p. 6 (V. EXPERIMENTAL RESULTS) |
| Baseline/ablation | Across all three settings, we achieve tight guarantees on failure prediction compared to the true expected failure rate of the policies. | fair input/data/compute/action matching | p. 8 (V. EXPERIMENTAL RESULTS), p. 7 (V. EXPERIMENTAL RESULTS), p. 7 (V. EXPERIMENTAL RESULTS) |

## Explicit Limitations and Failure Boundary

- **p. 5 / IV. FAILURE PREDICTION WITH GUARANTEED ERROR - extractive body cue:** Bound on Class-Conditional Misclassification Error The example above shows that minimizing the total misclassification error can fail to perform well when the relative importance of ...
- **p. 6 / IV. FAILURE PREDICTION WITH GUARANTEED ERROR - extractive body cue:** Thus, if the policy designer has access to a single training dataset to learn a failure predictor, conformal prediction does not guarantee that the expected ...
- **p. 7 / V. EXPERIMENTAL RESULTS - extractive body cue:** We note TABLE II RESULTS FOR FAILURE PREDICTION ON NAVIGATION TASK Setting Standard Occluded Obstacle True Expected Failure (Sim) 0.253 0.514 Misclassification Bound 0.128 0.154 ...
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1. We train a failure predictor which guarantees (with high probability) detection of a failure ahead of time. A policy is tasked with avoiding ...
- **p. 8 / V. EXPERIMENTAL RESULTS - extractive body cue:** Since the gripper does not reach the mug in the first two out of five steps of the rollout, we only train the failure predictor ...
- **p. 3 / IV. FAILURE PREDICTION WITH GUARANTEED ERROR - extractive body cue:** BOUNDS Our approach for learning failure predictors with guaranteed error bounds relies on a reduction to results from the PACBayes generalization theory from supervised learning; ...
- **p. 4 / IV. FAILURE PREDICTION WITH GUARANTEED ERROR - extractive body cue:** Continuum of optimal predictors (red) for varying class population ratios (successes and failures).

## Why Read It

World models, safety, uncertainty, and recovery의 safety 문제를 이해하기 위해 읽는다. 본문은 Given access to a black-box control policy (e.g., one with neural network components), our goal is to train a failure predictor for this policy.를 문제로 두고, Our primary contribution is to develop an approach for learning a failure predictor with guaranteed bounds on error rates, given a black-box control policy that operates on a robotic system with high-dimensional ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (III. PROBLEM FORMULATION), p. 2 (I. INTRODUCTION), p. 3 (III. PROBLEM FORMULATION), p. 3 (III. PROBLEM FORMULATION) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
