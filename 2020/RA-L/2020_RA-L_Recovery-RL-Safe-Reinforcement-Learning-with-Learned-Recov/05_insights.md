# Insights — Recovery RL: Safe Reinforcement Learning with Learned Recovery Zones

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2010.15920; PDF retrieval source: https://arxiv.org/pdf/2010.15920. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / I. INTRODUCTION - extractive body cue:** Thus, endowing RL agents with the ability to satisfy constraints during learning not only enables robots to interact safely, but also allows them to more ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** We present Recovery RL, a new algorithm for safe robotic RL.
- **p. 1 / I. INTRODUCTION - extractive body cue:** If it tips over the carton, then not only can this possibly break the carton and create a mess, but it also requires laborious human ...
- **p. 3 / III. PROBLEM STATEMENT - extractive body cue:** We present an algorithm to optimize equation (III.1) by utilizing a pair of policies, a task policy πtask, which is trained to maximize Rπ over ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Separating the task and recovery policies makes it easier to balance task performance and safety, and allows using off-the-shelf RL algorithms for both.
- **p. 5 / IV. RECOVERY RL - extractive body cue:** [8] to plan over a learned stochastic dynamics model, while for tasks with visual observations, we use a VAE based latent dynamics model.
- **p. 1 / Abstract - extractive body cue:** We propose Recovery RL, an algorithm which navigates this tradeoff by (1) leveraging offline data to learn about constraint violating zones before policy learning and ...
- **Contribution anchor:** p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 3 (III. PROBLEM STATEMENT), p. 2 (I. INTRODUCTION), p. 5 (IV. RECOVERY RL)

### Strongest assumption and failure boundary

- **p. 1 / I. INTRODUCTION - extractive body cue:** However, when deploying RL agents in the real world, unconstrained exploration can result in highly suboptimal behaviors which can damage the robot, break surroundings objects, ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** While these approaches are appealing for their generality and simplicity, there are two key aspects which make them difficult to use in practice.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Most prior work in safe RL integrates constraint satisfaction into the task objective to ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** We evaluate Recovery RL on an imagebased obstacle avoidance task on a physical robot and find that it trades off constraint violations and task successes ...
- **p. 3 / III. PROBLEM STATEMENT - extractive body cue:** Setting εrisk = 0 as well results in a robust optimal control problem.
- **p. 6 / V. EXPERIMENTS - extractive body cue:** In all navigation tasks, we find that Recovery RL significantly outperforms prior methods with both model-free and model-based recovery policies, while for the object extraction ...
- **p. 7 / V. EXPERIMENTS - extractive body cue:** We hypothesize that the model-based recovery mechanism is better able to compensate for approximation errors in ˆQπ φ,risk, resulting in a more robust recovery policy.
- **Boundary to test:** In all navigation tasks, we find that Recovery RL significantly outperforms prior methods with both model-free and model-based recovery policies, while for the object extraction environments, Recovery RL with a model-based recovery ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Thus, endowing RL agents with the ability to satisfy constraints during learning not only enables robots to interact safely, but also allows them to more efficiently learn in the real world. | p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| Reported outcome | Results suggest that Recovery RL with both model-free and modelbased recovery mechanisms significantly outperform prior algorithms across all 3 2D pointmass navigation environments | p. 6 (V. EXPERIMENTS), p. 6 (Figure/Table caption) |
| Failure/limitation | In all navigation tasks, we find that Recovery RL significantly outperforms prior methods with both model-free and model-based recovery policies, while for the object extraction environments, Recovery RL with a model-based recovery ... | p. 6 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Paper-specific interface:** Safe exploration poses a tradeoff: learning new skills through environmental interaction requires exploring a wide range of possible behaviors, but learning safely forces the agent to restrict exploration to constraint ... (p. 1, I. INTRODUCTION).
- **Paper-specific mechanism:** Thus, endowing RL agents with the ability to satisfy constraints during learning not only enables robots to interact safely, but also allows them to more efficiently learn in the real ... (p. 1, I. INTRODUCTION).
- **Evidence boundary:** the reported outcome is Figure 9: Simulation Experiments Cumulative Violations: We plot the cumulative constraint violations for each algorithm in each simulation domain, with results averaged over 10 runs for all algorithms. We observe ... (p. 12, Figure/Table caption); the relevant task/metric cue is We do not report reward per episode, as episodes terminate on task completion or constraint violation. (p. 5, V. EXPERIMENTS). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** We then study the sensitivity of Recovery RL to the number of offline transitions used to pretrain πrec and ˆQπ φ,risk (right) and find that Recovery RL performs well even ... (p. 7, V. EXPERIMENTS).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `CORE` in `World models, safety, uncertainty, and recovery`; tags: `Robotics, safe reinforcement learning, recovery policy, real robot`.
- **Reading predecessor in the generated track queue:** Control Barrier Function Based Quadratic Programs for Safety Critical Systems (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** DreamGen: Unlocking Generalization in Robot Learning through Video World Models (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** In all navigation tasks, we find that Recovery RL significantly outperforms prior methods with both model-free and model-based recovery policies, while for the object extraction environments, Recovery RL with a model-based recovery ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: Safe exploration poses a tradeoff: learning new skills through environmental interaction requires exploring a wide range of possible behaviors, but learning safely forces the agent to restrict exploration to constraint ... (p. 1, I. INTRODUCTION); preserve the objective/update rule: We propose Recovery RL, an algorithm which navigates this tradeoff by (1) leveraging offline data to learn about constraint violating zones before policy learning and (2) separating the goals of ... (p. 1, Abstract).
2. Use the paper-reported task/data/environment cue: Domains: We evaluate Recovery RL on a set of 6 simulation domains (Figure 3) and an image-based obstacle avoidance task on a physical robot (Figure 6). (p. 5, V. EXPERIMENTS).
3. Compare against the reported or matched baseline: Recovery RL and all comparisons which have a safety critic are given the same offline dataset Doffline. (p. 5, V. EXPERIMENTS).
4. Report the body metric with its denominator and aggregation: We do not report reward per episode, as episodes terminate on task completion or constraint violation. (p. 5, V. EXPERIMENTS).
5. Re-run the reported ablation or stress/failure condition: Ablations: We ablate different components of Recovery RL and study the sensitivity of Recovery RL to the number of transitions in Doffline for the Object Extraction domain in Figure 7. (p. 7, V. EXPERIMENTS); if none is reported, design one around: We then study the sensitivity of Recovery RL to the number of offline transitions used to pretrain πrec and ˆQπ φ,risk (right) and find that Recovery RL performs well even ... (p. 7, V. EXPERIMENTS).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), match the reported outcome at p. 12 (Figure/Table caption), p. 13 (Figure/Table caption), p. 6 (V. EXPERIMENTS), and measure the boundary at p. 7 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS).

## Falsifiable research question

Under the paper's stated interface (Safe exploration poses a tradeoff: learning new skills through environmental interaction requires exploring a wide range of possible behaviors, but learning safely ...), does the paper-specific mechanism (Thus, endowing RL agents with the ability to satisfy constraints during learning not only enables robots to interact safely, but also allows ...) retain the reported evaluation outcome (We do not report reward per episode, as episodes terminate on task completion or constraint violation.) when tested against the paper's strongest explicit boundary (We then study the sensitivity of Recovery RL to the number of offline transitions used to pretrain πrec ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (We do not report reward per episode, as episodes terminate on task completion or constraint violation.) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (15 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** Thus, endowing RL agents with the ability to satisfy constraints during learning not only enables robots to interact safely, but also allows them to more efficiently learn in the real ... (p. 1, I. INTRODUCTION).
- **Paper-supported outcome:** Figure 9: Simulation Experiments Cumulative Violations: We plot the cumulative constraint violations for each algorithm in each simulation domain, with results averaged over 10 runs for all algorithms. We observe ... (p. 12, Figure/Table caption).
- **Strongest explicit boundary:** We then study the sensitivity of Recovery RL to the number of offline transitions used to pretrain πrec and ˆQπ φ,risk (right) and find that Recovery RL performs well even ... (p. 7, V. EXPERIMENTS).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
