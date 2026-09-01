# Contact-Invariant Optimization for Hand Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://homes.cs.washington.edu/~zoran/behavior-discovery.html.
> PDF retrieval source: https://homes.cs.washington.edu/~zoran/behavior-discovery.pdf. Reading tracker status/evidence was not changed.

- Year/Venue: 2014 / SIGGRAPH
- Authors: not duplicated here when not verified in the registry source
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: CORE
- Tags: Robotics, contact-rich manipulation, trajectory optimization, contact invariant
- Official paper: https://homes.cs.washington.edu/~zoran/behavior-discovery.html
- Full-text retrieval: https://homes.cs.washington.edu/~zoran/behavior-discovery.pdf
- Code/Project: not identified
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-02 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Manipulation, contact, tactile, and dexterity의 manipulation 문제를 이해하기 위해 읽는다. 본문은 In complex behaviors and in complex environments, however, it is difficult to know in advance what these contact sets should be and how they should change from one phase to the next.를 문제로 두고, At the core of our framework is the contact-invariant optimization (CIO) method we introduce here.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** We present a motion synthesis framework capable of producing a wide variety of important human behaviors that have rarely been studied, including getting up from ...
- **p. 1 / Abstract - extractive body cue:** Our framework is not specific to humans, but applies to characters of arbitrary morphology and limb configuration.
- **p. 1 / Abstract - extractive body cue:** The approach is fully automatic and does not require domain knowledge specific to each behavior.
- **p. 1 / Abstract - extractive body cue:** It also does not require pre-existing examples or motion capture data.
- **p. 1 / Abstract - extractive body cue:** At the core of our framework is the contact-invariant optimization (CIO) method we introduce here.
- **p. 2 / 1 Introduction - extractive body cue:** In complex behaviors and in complex environments, however, it is difficult to know in advance what these contact sets should be and how they should ...
- **p. 1 / 1 Introduction - extractive body cue:** Automated synthesis of complex human behaviors is one of the long-standing grand challenges in computer graphics, that would also have an impact on robotics, biomechanics, ...

## Core Idea

- **p. 1 / Abstract - extractive body cue:** At the core of our framework is the contact-invariant optimization (CIO) method we introduce here.
- **p. 1 / 1 Introduction - extractive body cue:** In this paper we present a step towards a more general yet fully automated framework for behavior synthesis, capable of produc
- **p. 2 / 1 Introduction - extractive body cue:** The important difference is that the domain to which our method is tailored is much larger, and includes any behavior of any articulated character where ...
- **p. 2 / 1 Introduction - extractive body cue:** Intuitively, CIO is a way of reshaping a highly discontinuous and local-minima-prone search space of movements and contacts, into a slightly larger but much better-behaved ...
- **p. 1 / 1 Introduction - extractive body cue:** These algorithms are successful because they exploit domain-specific knowledge: state machines synchronized to the relatively simple and stereotypical pattern of foot-ground contacts, reduced models based ...
- **p. 2 / 1 Introduction - extractive body cue:** These auxiliary variables affect not only the cost function but also the dynamics (by enabling and disabling contact forces), and are optimized together with the ...
- **p. 2 / 1 Introduction - extractive body cue:** Additional innovations include a continuation scheme allowing helper forces at the potential contacts rather than the torso, as well as a feature-based model of physics ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Instead, movement details and complexity should emerge from an automated procedure whose only inputs are intuitive high-level goals that are easy to specify. | RGB-D/point cloud, object state와 contact/task observation | p. 1 (1 Introduction), p. 1 (1 Introduction) |
| State/latent | Instead, movement, details, complexity, should, emerge, automated, procedure, whose, only, inputs, intuitive | object geometry, affordance, contact mode 또는 end-effector state | p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction) |
| Output/action | After three decades of intensive research, we now have algorithms that can make simulated humanoids walk robustly and realistically in response to high-level interactive inputs such as desired body velocity and orientation. | grasp, pose, force 또는 end-effector trajectory | p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Objective/outcome | These auxiliary variables affect not only the cost function but also the dynamics (by enabling and disabling contact forces), and are optimized together with the movement trajectory. | task completion, contact success, pose/force error와 generalization | p. 1 (Abstract), p. 1 (1 Introduction), p. 2 (1 Introduction) |

## Main Claims and Actual Contribution

- **p. 1 / Abstract - extractive body cue:** At the core of our framework is the contact-invariant optimization (CIO) method we introduce here.
- **p. 1 / 1 Introduction - extractive body cue:** In this paper we present a step towards a more general yet fully automated framework for behavior synthesis, capable of produc
- **p. 2 / 1 Introduction - extractive body cue:** The important difference is that the domain to which our method is tailored is much larger, and includes any behavior of any articulated character where ...
- **p. 2 / 1 Introduction - extractive body cue:** Intuitively, CIO is a way of reshaping a highly discontinuous and local-minima-prone search space of movements and contacts, into a slightly larger but much better-behaved ...
- **p. 6 / 5 Results - extractive body cue:** Because contacts can be made with the surfaces of other characters, the task is achieved by one character climbing on top of the other.
- **p. 6 / 5 Results - extractive body cue:** Two characters also cooperate to achieve tasks impossible for one, such as ℓpos for one of the characters specifying a target location above character's height.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 6 (5 Results), p. 6 (5 Results) |
| Embodiment/environment | Tasks similar to ℓpos and ℓdir are used to specify final position and orientation of the object. | hardware/simulator version and reset protocol | p. 6 (5 Results), p. 6 (5 Results) |
| Dataset/benchmark | Tasks similar to ℓpos and ℓdir are used to specify final position and orientation of the object. | role, split, size and leakage | p. 6 (5 Results), p. 6 (5 Results) |
| Metric | The optimization was successful in getting up, walking and climbing scenarios, with strategies appropriate for each morphology. | definition, denominator, direction and uncertainty | p. 6 (5 Results), p. 6 (5 Results), p. 8 (Figure/Table caption) |
| Baseline/ablation | For example, animal trot pattern of contacts (moving front leg and opposite hind leg together) emerges for quadruped walking without explicitly being specified. | fair input/data/compute/action matching | p. 6 (5 Results), p. 6 (5 Results), p. 6 (5 Results) |

## Explicit Limitations and Failure Boundary

- **p. 6 / 5 Results - extractive body cue:** One way to remove this limitation is to simply increase the number of potential contacts and cover the entire body with sufficient density.
- **p. 6 / 5 Results - extractive body cue:** These limitations may be removed by using full-body inverse dynamics to calculate the character's joint torques, and penalizing the torques or some related quantity.
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 2: Simplified Character Model. The features used in our character description with collision capsule geometry overlaid. YIN, K., COROS, S., BEAUDOIN, P., AND VAN ...
- **p. 5 / 2 Related Work - extractive body cue:** Exactly the same continuation scheme was successful in all of the diverse behaviors we studied, and so our method does not need behavior-specific adjustments.
- **p. 5 / 2 Related Work - extractive body cue:** The solution obtained at the end of each phase is perturbed with small zero-mean Gaussian noise (to break any symmetries) and used to initialize the ...

## Why Read It

Manipulation, contact, tactile, and dexterity의 manipulation 문제를 이해하기 위해 읽는다. 본문은 In complex behaviors and in complex environments, however, it is difficult to know in advance what these contact sets should be and how they should change from one phase to the next.를 문제로 두고, At the core of our framework is the contact-invariant optimization (CIO) method we introduce here.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 Introduction), p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 1 (1 Introduction), p. 1 (Abstract) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
