# Can We Detect Failures Without Failure Data? Uncertainty-Aware Runtime Failure Detection for Imitation Learning Policies

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (20 pages; tesseract OCR fallback; title-token overlap first two pages=1.0); canonical paper source: https://www.roboticsproceedings.org/rss21/p073.html.
> PDF retrieval source: https://www.roboticsproceedings.org/rss21/p073.pdf. Reading tracker status/evidence was not changed.

- Year/Venue: 2025 / RSS
- Authors: not duplicated here when not verified in the registry source
- Primary track: World models, safety, uncertainty, and recovery
- Tier: NEXT
- Tags: Robotics, failure detection, uncertainty, conformal prediction, Imitation Learning, runtime monitoring
- Official paper: https://www.roboticsproceedings.org/rss21/p073.html
- Full-text retrieval: https://www.roboticsproceedings.org/rss21/p073.pdf
- Code/Project: https://cxu-tri.github.io/FAIL-Detect-Website/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-02 (20 pages; tesseract OCR fallback; title-token overlap first two pages=1.0)

## Why This Paper Is Here

World models, safety, uncertainty, and recovery의 safety 문제를 이해하기 위해 읽는다. 본문은 Detecting failures in robotic manipulation tasks poses several challenges.를 문제로 두고, Aside from being performant, our method enables faster inference than prior work [1], which requires sampling, ‘multiple robot actions during inference.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Recent years have witnessed impressive robotic ‘manipulation systems driven by advances
- **p. 1 / Abstract - extractive body cue:** fand generative modeling, such as approaches.
- **p. 1 / Abstract - extractive body cue:** As robot policy performance increases, so does the complexity and time horizon of achievable tasks,
- **p. 1 / Abstract - extractive body cue:** ing unexpected and diverse failure modes that are difficult to predict a priori.
- **p. 1 / Abstract - extractive body cue:** To enable trustworthy policy' deployment in safety-critical human environments, reliable runtime failure detection becomes important during policy inference.
- **p. 1 / 1. INTRODUCTION - extractive body cue:** Detecting failures in robotic manipulation tasks poses several challenges.
- **p. 1 / 1. INTRODUCTION - extractive body cue:** This poses significant challenges since collecting and annotating a comprehensive set of failure examples is often time-consuming, expensive, and even infeasible in many real-world scenarios.

## Core Idea

- **p. 1 / 1. INTRODUCTION - extractive body cue:** Aside from being performant, our method enables faster inference than prior work [1], which requires sampling, ‘multiple robot actions during inference.
- **p. 2 / 1. INTRODUCTION - extractive body cue:** ur contributions are as follows, We present FAIL-Detect, ‘4 modular two stage uncertainty-aware runtime failure detec~ tion framework for generative imitation learning-based robotic ‘manipulation, First, ...
- **p. 1 / 1. INTRODUCTION - extractive body cue:** A key novelty of our method is the ability to learn failure detection signals without access 10 failure data.
- **p. 3 / 1. INTRODUCTION - extractive body cue:** STAC does not require failure data, consists ofa score ‘computed post-hoc from a batch of predicted actions and a cconstant-time CP threshold to flag failures, ...
- **p. 2 / 1. INTRODUCTION - extractive body cue:** We show that FAIL-Detect identifies failures accurately and quickly on diverse robotic manipulation tasks, both in simulation and on robot hardware, outperforming SOTA failure detection ...
- **p. 3 / III. PROBLEM FORMULATION - extractive body cue:** Let g(Ar / Or) denote the generator, where O, represents the environment observation (e.g. image features and robot states) at time f, and g is ...
- **p. 3 / III. PROBLEM FORMULATION - extractive body cue:** The first A' <H actions Ave, sje are executed, after which the robot re-plans by generating a new sequence of HY actions attime t+-11'.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | In the first stage, we extract scalar signals from policy inputs and/or outputs (e-g., robot states, visual features, generated future actions) that are discriminative between successes and failures during policy inference. | observation, uncertainty/risk estimate와 task command | p. 1 (1. INTRODUCTION), p. 3 (III. PROBLEM FORMULATION) |
| State/latent | first, stage, extract, scalar, signals, policy, inputs, and/or, outputs, robot, states, visual | safe set, recovery state 또는 constraint margin | p. 1 (1. INTRODUCTION), p. 3 (III. PROBLEM FORMULATION), p. 1 (1. INTRODUCTION) |
| Output/action | Let g(Ar / Or) denote the generator, where O, represents the environment observation (e.g. image features and robot states) at time f, and g is a stochastic predictor of a sequence of ... | shielded, recovery 또는 safe action | p. 3 (III. PROBLEM FORMULATION), p. 1 (1. INTRODUCTION), p. 3 (III. PROBLEM FORMULATION) |
| Objective/outcome | task return과 violation/failure probability | task return과 violation/failure probability | 본문 anchor 없음 |

## Main Claims and Actual Contribution

- **p. 1 / 1. INTRODUCTION - extractive body cue:** Aside from being performant, our method enables faster inference than prior work [1], which requires sampling, ‘multiple robot actions during inference.
- **p. 2 / 1. INTRODUCTION - extractive body cue:** ur contributions are as follows, We present FAIL-Detect, ‘4 modular two stage uncertainty-aware runtime failure detec~ tion framework for generative imitation learning-based robotic ‘manipulation, First, ...
- **p. 1 / 1. INTRODUCTION - extractive body cue:** A key novelty of our method is the ability to learn failure detection signals without access 10 failure data.
- **p. 3 / 1. INTRODUCTION - extractive body cue:** STAC does not require failure data, consists ofa score ‘computed post-hoc from a batch of predicted actions and a cconstant-time CP threshold to flag failures, ...
- **p. 2 / 1. INTRODUCTION - extractive body cue:** We show that FAIL-Detect identifies failures accurately and quickly on diverse robotic manipulation tasks, both in simulation and on robot hardware, outperforming SOTA failure detection ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 5: Quantitative results for the robot hardware experiments across two tasks with policies trained using FM and DP. We consider two different ways to ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 4: Quantitative failure detection results for simulation tasks on FM policy (best, second) third); results with TPR and TNR are in Fig. 11 ‘and ...
- **p. 7 / V. EXPERIMENTS - extractive body cue:** We omit comparison against ensembles [31], a popular OOD detection technique, die to RND having shown improved performance ‘over ensembles in prior work {13} and ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (Figure/Table caption), p. 6 (Figure/Table caption) |
| Embodiment/environment | significantly fewer rollouts in the robot hardware tasks (i.e., 50 rollouts) compared to the simulation tasks (i.e., 2000 rollouts) | hardware/simulator version and reset protocol | p. 7 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS) |
| Dataset/benchmark | In the robot hardware experiments, we consider two tasks on a bimanual Franka Emika Panda robot station that are significantly more challenging: FoldRedTowel and CleanUpSpill (see Fig. | role, split, size and leakage | p. 7 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS) |
| Metric | Fig. 4: Quantitative failure detection results for simulation tasks on FM policy (best, second) third); results with TPR and TNR are in Fig. 11 ‘and results on DP are in Fig. 12. ... | definition, denominator, direction and uncertainty | p. 6 (Figure/Table caption), p. 5 (Figure/Table caption), p. 6 (V. EXPERIMENTS) |
| Baseline/ablation | Fig. 5: Quantitative results for the robot hardware experiments across two tasks with policies trained using FM and DP. We consider two different ways to compute the CP band: "setting-lependent" using successful ... | fair input/data/compute/action matching | p. 7 (Figure/Table caption), p. 6 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 3: Robot hardware experiment scenarios. (Top row) FoldRedTowel with Disturbance: In (b), the human pulls the towel from the position in (a) towards the ...
- **p. 7 / C. Do failure detections align with human intuition? - extractive body cue:** This performance shows the capacity of failure-free failure detection methods to robustly identify failures across many scenarios.
- **p. 3 / IV. FAILURE DETECTION FRAMEWORK - extractive body cue:** 2) Calibrate time-varying thresholds 1, based on a CP band. ‘The final decision D(r:8) = 1(Dry(Ar.Or:6) > me) raises a failure flag if the sealar ...
- **p. 7 / C. Do failure detections align with human intuition? - extractive body cue:** How performant is failure detection without failure data?
- **p. 8 / C. Do failure detections align with human intuition? - extractive body cue:** and higher failure/suecess separation.
- **p. 8 / C. Do failure detections align with human intuition? - extractive body cue:** What is the impact of leamed vs. post-hoc scores on failure detection?
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 7: Physical interpretation of logy, the most successful and robust learned score method. Failed trajectory scores are in red and successful ones are in ...

## Why Read It

World models, safety, uncertainty, and recovery의 safety 문제를 이해하기 위해 읽는다. 본문은 Detecting failures in robotic manipulation tasks poses several challenges.를 문제로 두고, Aside from being performant, our method enables faster inference than prior work [1], which requires sampling, ‘multiple robot actions during inference.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. INTRODUCTION), p. 1 (1. INTRODUCTION), p. 3 (1. INTRODUCTION), p. 3 (III. PROBLEM FORMULATION), p. 2 (1. INTRODUCTION), p. 3 (III. PROBLEM FORMULATION) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
