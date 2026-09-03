# Insights — Extreme Parkour with Legged Robots

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2309.14341; PDF retrieval source: https://arxiv.org/pdf/2309.14341. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 3 / 1 Introduction - extractive body cue:** To allow the robot to adjust itself as per the obstacle type at deployment, we propose a novel dual distillation method.
- **p. 3 / 1 Introduction - extractive body cue:** Below, we summarize the main contributions: • A novel dual distillation method for distilling both agile motor commands and rapidly fluctuating heading directions from depth ...
- **p. 5 / 3 Method - extractive body cue:** We present a simple, unified reward formulation from which diverse behaviors emerge automatically and are perfectly adapted to the terrain geometry.
- **p. 6 / 3 Method - extractive body cue:** To overcome this issue, we propose to use a mixture of teacher and student (MTS).
- **p. 6 / 3 Method - extractive body cue:** To explore this diversity, we introduce a term to track a desired forward vector using the same inner product design principle, which can be controlled ...
- **p. 6 / 3 Method - extractive body cue:** 3.2 Reinforcement Learning from Scandots (Phase 1) We use the above rewards to learn a policy using model-free RL [33] in simulation.
- **p. 5 / 3 Method - extractive body cue:** We use Regularized Online Adaptation (ROA)[9] to train an estimator to recover environmental information from the history of observations.
- **Contribution anchor:** p. 3 (1 Introduction), p. 3 (1 Introduction), p. 5 (3 Method), p. 6 (3 Method), p. 6 (3 Method), p. 6 (3 Method)

### Strongest assumption and failure boundary

- **p. 3 / 1 Introduction - extractive body cue:** However, low cost poses a new challenge for parkour which is not as prominent in prior walking works.
- **p. 3 / 1 Introduction - extractive body cue:** All these challenges are not feasible with such an approach.
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 7: For each terrain, we run 5 trials and record the number of successes. We find that ours has 20-80% higher success rate on ...
- **p. 8 / 4 Results - extractive body cue:** Noisy is able to get some performance but has very large variance since it can rely on collisions with its legs to sense terrain geometry ...
- **p. 9 / 4 Results - extractive body cue:** These sudden adjustments are out-ofdistribution for the policy and it cannot adapt fast enough, causing it to fail.
- **p. 8 / 4 Results - extractive body cue:** NoClear achieves slightly higher performance but it places feet close to the obstacle edges which is unstable in the real world.
- **Boundary to test:** Figure 7: For each terrain, we run 5 trials and record the number of successes. We find that ours has 20-80% higher success rate on the most difficult instance of each terrain. ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | To allow the robot to adjust itself as per the obstacle type at deployment, we propose a novel dual distillation method. | p. 3 (1 Introduction), p. 3 (1 Introduction) |
| Reported outcome | In addition, its feet clearance also helps it to achieve some performance with noisy measurements. | p. 8 (4 Results), p. 8 (4 Results) |
| Failure/limitation | Figure 7: For each terrain, we run 5 trials and record the number of successes. We find that ours has 20-80% higher success rate on the most difficult instance of each terrain. ... | p. 9 (Figure/Table caption), p. 8 (4 Results) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Paper-specific interface:** As a result at deployment, the policy not only outputs agile motor commands but also rapidly adjusts heading directions all from input depth image. (p. 3, 1 Introduction).
- **Paper-specific mechanism:** Below, we summarize the main contributions: • A novel dual distillation method for distilling both agile motor commands and rapidly fluctuating heading directions from depth images. • A simple yet ... (p. 3, 1 Introduction).
- **Evidence boundary:** the reported outcome is Figure 7: For each terrain, we run 5 trials and record the number of successes. We find that ours has 20-80% higher success rate on the most difficult instance of ... (p. 9, Figure/Table caption); the relevant task/metric cue is First, we test our reward design and overall pipeline (Tab. (p. 8, 4 Results). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** It sometimes succeeds on hurdles and gaps but fails when the human has to provide sudden direction changes which are out-of-distribution. (p. 9, 4 Results).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `Locomotion, whole-body, mobile manipulation, and humanoids`; tags: `Robotics, quadruped locomotion, parkour, Reinforcement Learning`.
- **Reading predecessor in the generated track queue:** Learning Quadrupedal Locomotion over Challenging Terrain (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Walk These Ways: Tuning Robot Control for Generalization with Multiplicity of Behavior (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Figure 7: For each terrain, we run 5 trials and record the number of successes. We find that ours has 20-80% higher success rate on the most difficult instance of each terrain. ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: As a result at deployment, the policy not only outputs agile motor commands but also rapidly adjusts heading directions all from input depth image. (p. 3, 1 Introduction); preserve the objective/update rule: 4 3.1 Unified Reward for Extreme Parkour . . . . . . . . . . . . . . . . . . . . . . . ... (p. 2, 3 Method).
2. Use the paper-reported task/data/environment cue: Starred is recent concurrent work [47]. baseline comparison in simulation since it is infeasible to provide human joystick commands and provide real-world comparisons instead. (p. 9, 4 Results).
3. Compare against the reported or matched baseline: We find that our method outperforms the baselines in terms of both metrics. (p. 8, 4 Results).
4. Report the body metric with its denominator and aggregation: First, we test our reward design and overall pipeline (Tab. (p. 8, 4 Results).
5. Re-run the reported ablation or stress/failure condition: 2 with velocity tracking in base frame used in [2]. • No feet clearance penalty (NoClear): Removes the penalization for stepping near the edges defined in Eq. (p. 8, 4 Results); if none is reported, design one around: It sometimes succeeds on hurdles and gaps but fails when the human has to provide sudden direction changes which are out-of-distribution. (p. 9, 4 Results).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 3 (1 Introduction), p. 3 (1 Introduction), match the reported outcome at p. 9 (Figure/Table caption), p. 7 (4 Results), p. 8 (4 Results), and measure the boundary at p. 9 (4 Results), p. 8 (4 Results).

## Falsifiable research question

Under the paper's stated interface (As a result at deployment, the policy not only outputs agile motor commands but also rapidly adjusts heading directions all from input ...), does the paper-specific mechanism (Below, we summarize the main contributions: • A novel dual distillation method for distilling both agile motor commands and rapidly fluctuating heading ...) retain the reported evaluation outcome (First, we test our reward design and overall pipeline (Tab.) when tested against the paper's strongest explicit boundary (It sometimes succeeds on hurdles and gaps but fails when the human has to provide sudden direction changes ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (First, we test our reward design and overall pipeline (Tab.) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (12 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** Below, we summarize the main contributions: • A novel dual distillation method for distilling both agile motor commands and rapidly fluctuating heading directions from depth images. • A simple yet ... (p. 3, 1 Introduction).
- **Paper-supported outcome:** Figure 7: For each terrain, we run 5 trials and record the number of successes. We find that ours has 20-80% higher success rate on the most difficult instance of ... (p. 9, Figure/Table caption).
- **Strongest explicit boundary:** It sometimes succeeds on hurdles and gaps but fails when the human has to provide sudden direction changes which are out-of-distribution. (p. 9, 4 Results).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
