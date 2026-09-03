# SINGER: An Onboard Generalist Vision-Language Navigation Policy for Drones

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (9 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_3.html.
> PDF retrieval source: https://arxiv.org/pdf/2509.18610. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICRA
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: Vision-Language Model, Navigation
- Official paper: https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_3.html
- Full-text retrieval: https://arxiv.org/pdf/2509.18610
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (9 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 [8] introduces FiGS, a high-fidelity Gaussian-Splatting-based drone simulator to narrow the sim-to-real gap for stronger real-world transfer; however, FiGS lacks the semantic knowledge required for open-world drone navigation, limiting ...를 문제로 두고, We summarize our contributions as follows: • We introduce a high-fidelity drone simulator for efficient imitation learning in language-specified drone navigation problems built on language embedded Gaussian Splatting. • We design a ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Large vision-language models have driven remarkable progress in open-vocabulary robot policies, e.g., generalist robot manipulation policies, that enable robots to complete complex tasks specified in ...
- **p. 1 / Abstract - extractive body cue:** Despite these successes, open-vocabulary autonomous drone navigation remains an unsolved challenge due to the scarcity of largescale demonstrations, real-time control demands of drones for stabilization, ...
- **p. 1 / Abstract - extractive body cue:** In this work, we present SINGER for language-guided autonomous drone navigation in the open world using only onboard sensing and compute.
- **p. 1 / Abstract - extractive body cue:** To train robust, open-vocabulary navigation policies, SINGER leverages three central components: (i) a photorealistic language-embedded flight simulator with minimal sim-to-real gap using Gaussian Splatting for ...
- **p. 1 / Abstract - extractive body cue:** Through extensive hardware flight experiments, we demonstrate superior zero-shot sim-to-real transfer of our policy to unseen environments and unseen language-conditioned goal objects.
- **p. 2 / I. INTRODUCTION - extractive body cue:** [8] introduces FiGS, a high-fidelity Gaussian-Splatting-based drone simulator to narrow the sim-to-real gap for stronger real-world transfer; however, FiGS lacks the semantic knowledge required for ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** To address the data scarcity challenge, prior work [6], [7] trains visuomotor policies for drone navigation in simulation, but the effectiveness of the resulting policies ...

## Core Idea

- **p. 2 / I. INTRODUCTION - extractive body cue:** We summarize our contributions as follows: • We introduce a high-fidelity drone simulator for efficient imitation learning in language-specified drone navigation problems built on language ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** In this paper, we introduce SINGER (Semantic In-situ Navigation and Guidance for Embodied Robots), a pipeline for training language-conditioned drone navigation policies addressing the aforementioned ...
- **p. 5 / V. SINGER POLICY ARCHITECTURE AND TRAINING - extractive body cue:** The twostage training procedure prescribed in [8] is used to first train a history network to predict time-varying system parameters in a latent vector by ...
- **p. 5 / V. SINGER POLICY ARCHITECTURE AND TRAINING - extractive body cue:** The deep learned policy architecture is adopted from the SV-Net described in [8], with an additional image preprocessing step appended to the feature extractor network.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | In this work, we ask the question: "Can we train a visionlanguage drone navigation policy to reach previously unseen goal objects in a previously unseen environment using only on board sensing and ... | camera/depth stream, pose, map와 language goal | p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| State/latent | question, train, visionlanguage, drone, navigation, policy, reach, previously, unseen, goal, objects, environment | robot pose, free-space/semantic map와 local goal | p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| Output/action | At deployment, we inference CLIPSeg [11] to produce open-vocabulary semantic images of the environment as conditioning inputs, processed by an end-to-end visuomotor drone policy for low-level drone commands. | collision-free trajectory 또는 velocity command | p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION) |
| Objective/outcome | This full network is trained with a loss on the expert demonstrator's motor commands over the 2s trajectory chunks. | goal reach, safety, localization error와 replanning latency | p. 5 (V. SINGER POLICY ARCHITECTURE AND TRAINING) |

## Main Claims and Actual Contribution

- **p. 2 / I. INTRODUCTION - extractive body cue:** We summarize our contributions as follows: • We introduce a high-fidelity drone simulator for efficient imitation learning in language-specified drone navigation problems built on language ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** In this paper, we introduce SINGER (Semantic In-situ Navigation and Guidance for Embodied Robots), a pipeline for training language-conditioned drone navigation policies addressing the aforementioned ...
- **p. 7 / VI. EXPERIMENTS - extractive body cue:** The overall success rate of the policy insimulation is also comparable to the results in hardware.
- **p. 7 / VI. EXPERIMENTS - extractive body cue:** We include SINGER's results under the same conditions as a testament to its ability to outperform the baseline.
- **p. 5 / VI. EXPERIMENTS - extractive body cue:** We evaluate the performance of the SINGER in drone experiments to evaluate its generalization and robustness capabilities in simulation within a 3DGS environment and in ...
- **p. 6 / VI. EXPERIMENTS - extractive body cue:** The policy is evaluated on successful flight towards the queried object without collisions.
- **p. 6 / VI. EXPERIMENTS - extractive body cue:** Finally, the hardest scenario is designed to evaluate policy performance in a unseen environment and on unseen semantic queries.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (VI. EXPERIMENTS), p. 7 (VI. EXPERIMENTS) |
| Embodiment/environment | Baseline and SINGER On Hardware We evaluate the real-world performance of SINGER against a baseline in six hardware experiments with five trials each, corresponding to three semantic queries with two initial locations ... | hardware/simulator version and reset protocol | p. 6 (VI. EXPERIMENTS), p. 5 (VI. EXPERIMENTS) |
| Dataset/benchmark | When deployed in hardware in the hardest evaluation scenario (three unseen semantic queries in an unseen deployment environment) SINGER performs the best overall, keeping all semantic queries in view during flight and ... | role, split, size and leakage | p. 6 (VI. EXPERIMENTS), p. 5 (VI. EXPERIMENTS), p. 6 (VI. EXPERIMENTS), p. 7 (VI. EXPERIMENTS) |
| Metric | The overall success rate of the policy insimulation is also comparable to the results in hardware. | definition, denominator, direction and uncertainty | p. 7 (VI. EXPERIMENTS), p. 6 (VI. EXPERIMENTS), p. 5 (VI. EXPERIMENTS) |
| Baseline/ablation | The baseline fails to track the correct semantic query 16.67% of the time (5/30), demonstrating the limited semantic scene understanding of the baseline compared to SINGER. | fair input/data/compute/action matching | p. 6 (VI. EXPERIMENTS), p. 7 (VI. EXPERIMENTS), p. 7 (VI. EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 6 / VI. EXPERIMENTS - extractive body cue:** SINGER performs the best at this experiment difficulty, reaching the goal region 73% of the time, and reaching sub-meter proximity 92.7% of the time with ...
- **p. 7 / VI. EXPERIMENTS - extractive body cue:** This results in one more failure case (6/30) vs. the baseline at (5/30) due to tracking the incorrect semantic query, as the drone cannot maintain ...
- **p. 7 / VI. EXPERIMENTS - extractive body cue:** Crosshatching direction on unsuccessful trials denotes the reason for failure, where collisions are counted while the policy has the query in-view, while query-not-in-view describes cases ...
- **p. 6 / VI. EXPERIMENTS - extractive body cue:** The policy is evaluated on successful flight towards the queried object without collisions.
- **p. 5 / VI. EXPERIMENTS - extractive body cue:** We evaluate the performance of the SINGER in drone experiments to evaluate its generalization and robustness capabilities in simulation within a 3DGS environment and in ...

## Why Read It

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 [8] introduces FiGS, a high-fidelity Gaussian-Splatting-based drone simulator to narrow the sim-to-real gap for stronger real-world transfer; however, FiGS lacks the semantic knowledge required for open-world drone navigation, limiting ...를 문제로 두고, We summarize our contributions as follows: • We introduce a high-fidelity drone simulator for efficient imitation learning in language-specified drone navigation problems built on language embedded Gaussian Splatting. • We design a ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 5 (V. SINGER POLICY ARCHITECTURE AND TRAINING), p. 5 (V. SINGER POLICY ARCHITECTURE AND TRAINING) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
