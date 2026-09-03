# Problem - A Minimalist Approach to Offline Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2106.06860; PDF retrieval source: https://arxiv.org/pdf/2106.06860. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 3 (3 Background), p. 4 (3 Background), p. 3 (3 Background), p. 5 (3 Background), p. 6 (3 Background)): One challenge for offline RL is the problem of extrapolation error [Fujimoto et al., 2019b], which is generalization error in the approximate value function, induced by selecting actions not contained ...

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Offline reinforcement learning (RL) defines the task of learning from a fixed batch of data.
- **p. 1 / Abstract - extractive body cue:** Due to errors in value estimation from out-of-distribution actions, most offline RL algorithms take the approach of constraining or regularizing the policy with the actions ...
- **p. 1 / Abstract - extractive body cue:** Built on pre-existing RL algorithms, modifications to make an RL algorithm work offline comes at the cost of additional complexity.
- **p. 1 / Abstract - extractive body cue:** Offline RL algorithms introduce new hyperparameters and often leverage secondary components such as generative models, while adjusting the underlying RL algorithm.
- **p. 1 / Abstract - extractive body cue:** In this paper we aim to make a deep RL algorithm work while making minimal changes.
- **p. 3 / 3 Background - extractive body cue:** One challenge for offline RL is the problem of extrapolation error [Fujimoto et al., 2019b], which is generalization error in the approximate value function, induced ...
- **p. 4 / 3 Background - extractive body cue:** However, in the offline setting, where we cannot interact with the environment, making additional adjustments to the underlying algorithm should be considered as more costly ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | One challenge for offline RL is the problem of extrapolation error [Fujimoto et al., 2019b], which is generalization error in the approximate ... | offline robot transition/trajectory dataset과 deployment MDP | body wording is the source claim |
| Observation / input | While most off-policy RL algorithms are applicable in the offline setting, they tend to under-perform due to "extrapolation error": an error in ... | dataset state/observation, action, reward와 return-to-go | exact sensor/frame/preprocessing from PDF body |
| State / latent | While, most, off-policy, algorithms, applicable, offline, setting, they, tend, under-perform | Q/value 또는 sequence-policy state | notation and tensor shape require body check |
| Output / action | turn, affects, policy, improvement, where, agents, learn, prefer | dataset-supported action sequence | exact unit/frame/decoder require body check |
| Target outcome | offline return and deployment safety | offline policy value, OOD safety와 closed-loop success | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | dataset transition (s,a,r,s′); body terms: While, most, off-policy, algorithms, applicable, offline, setting, they, tend, under-perform | p. 1 (1 Introduction), p. 3 (3 Background), p. 1 (1 Introduction) |
| Decision / output variable | dataset-supported policy action; body terms: Consequently, offline, enables, previously, logged, data, leveraging, expert | p. 1 (1 Introduction), p. 2 (1 Introduction), p. 3 (3 Background) |
| Objective / loss / cost | offline value with OOD control; cue terms: objective, agent, maximize, expected, discounted, return, cumulative, rewards | p. 2 (1 Introduction), p. 4 (3 Background), p. 6 (3 Background), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 3 (3 Background) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 7 (3 Background), p. 3 (3 Background), p. 1 (1 Introduction) |
| Success / guarantee | offline return and deployment safety | p. 7 (Figure/Table caption), p. 17 (Figure/Table caption), p. 18 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 4 / 3 Background - extractive body cue:** However, in the offline setting, where we cannot interact with the environment, making additional adjustments to the underlying algorithm should be considered as more costly ...
- **p. 3 / 3 Background - extractive body cue:** 4 Challenges in Offline RL In this section, we identify key open challenges in offline RL through analyzing and evaluating prior algorithms.
- **p. 5 / 3 Background - extractive body cue:** In analyzing the final trained policies of prior offline algorithms, we learned of a tangential, and open, challenge in the form of instability.
- **p. 6 / 3 Background - extractive body cue:** While we could not solve this challenge sufficiently within the scope of this work, the fact that this is reproducible even in the minimalistic variant ...

## What the Paper Changes

PDF body contribution framing (p. 1 (1 Introduction), p. 2 (1 Introduction), p. 3 (3 Background), p. 4 (3 Background), p. 6 (3 Background)): Consequently, offline RL enables the use of previously logged data or leveraging an expert, such as a human operator, without any of the risk associated with an untrained RL agent.

- **p. 2 / 1 Introduction - extractive body cue:** The surprising effectiveness of our minimalist approach suggests that in the context of offline RL, simpler approaches have been left underexplored in favor of more ...
- **p. 3 / 3 Background - extractive body cue:** We believe these challenges highlight the importance of minimalist approaches, where performance can be easily attributed to algorithmic contributions, rather than entangled with the specifics ...
- **p. 4 / 3 Background - extractive body cue:** If additional changes are necessary, then it suggests the algorithmic contributions alone are insufficient.
- **p. 6 / 3 Background - extractive body cue:** As discussed in Section 4 a minimalist approach has a variety of benefits, such as reducing the number of hyperparameters to tune, increasing scalability by ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 9 | Finally, we believe the sheer simplicity of our approach highlights a possible overemphasis on algorithmic complexity made by ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | Additionally, we highlight existing open challenges in offline RL research, including not only the extra implementation, computation, and ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Table 3: Run time comparison of training each offline RL algorithm (does not include evaluation costs). (Left) Breakdown ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 19 | Figure 8: Benchmarking wall-clock training time of DT and TD3+BC over 1 million steps. Does not include evaluation ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

offline_rl writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 1 (1 Introduction), p. 3 (3 Background), p. 1 (1 Introduction), p. 2 (1 Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 3 (3 Background), p. 4 (3 Background), p. 3 (3 Background), p. 5 (3 Background), p. 6 (3 Background), interface p. 1 (1 Introduction), p. 3 (3 Background), p. 1 (1 Introduction), p. 2 (1 Introduction), objective p. 2 (1 Introduction), p. 4 (3 Background), p. 6 (3 Background), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 3 (3 Background).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (19 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** One challenge for offline RL is the problem of extrapolation error [Fujimoto et al., 2019b], which is generalization error in the approximate value function, induced by selecting actions not contained ... (p. 3, 3 Background).
- **Formulation-changing contribution:** Consequently, offline RL enables the use of previously logged data or leveraging an expert, such as a human operator, without any of the risk associated with an untrained RL agent. (p. 1, 1 Introduction).
- **Assumption/failure evidence:** We use the hyperparameters defined in the CQL paper rather than the default settings in the CQL GitHub as we found those settings performed poorly. † denotes hyperparameters which deviate ... (p. 15, B Experimental Details).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
