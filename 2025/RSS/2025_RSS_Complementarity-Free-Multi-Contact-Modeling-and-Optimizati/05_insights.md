# Insights — Complementarity-Free Multi-Contact Modeling and Optimization for Dexterous Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (18 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p111.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p111.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / Abstract - extractive body cue:** Our method consistently achieves state-of-the ) a 96.5% average success rate across all objects
- **p. 1 / body section boundary not confidently recovered - extractive body cue:** 1: We propose a complementarty-free multi-contact model that a various challenging dexterous manipulation tasks, including fingertip in-air manipulation (cols.
- **p. 2 / Abstract - extractive body cue:** Our method sets a new benchmark for model-based contact-rich dexterous manipulation: « Highly versatile dexterity: 96.5% average success rate across all objects and environments « ...
- **p. 5 / B. New Complementarty-Free Multi-Contact Model - extractive body cue:** To circumvent the dual complementarity in (13), we propose ‘new contact model based on Lemma 1.
- **p. 2 / A. Rigid Body Multi-contact Models - extractive body cue:** (62, 33] developed penalty-based contact models.
- **p. 2 / A. Rigid Body Multi-contact Models - extractive body cue:** First, closed-form contact constraint resolution: our model builds on optimization-based contact dynamics (6, 39}, but instead of solving the primal [6, 39] or dual programs ...
- **p. 2 / A. Rigid Body Multi-contact Models - extractive body cue:** 1) Nonconvex Complementarity Contact Models: Rigid body contact dynamics is traditionally formulated using complermentarity models [S1, 49, 52]: it enforces no interpenetration and no contact ...
- **Contribution anchor:** p. 1 (Abstract), p. 1 (body section boundary not confidently recovered), p. 2 (Abstract), p. 5 (B. New Complementarty-Free Multi-Contact Model), p. 2 (A. Rigid Body Multi-contact Models), p. 2 (A. Rigid Body Multi-contact Models)

### Strongest assumption and failure boundary

- **p. 2 / Abstract - extractive body cue:** (III) Fewer hyperparameters: the proposed model has fewer parameters, making it easy to tune, and it also supports model auto-tuning using any learning framework ‘The ...
- **p. 1 / Abstract - extractive body cue:** This introduces computational challenges in both learning of contact dynamics [42] and combinatorics optimization of contact modes [14, 41.
- **p. 1 / Abstract - extractive body cue:** A primary challenge for model-based methods is the non-smooth and hybrid nature of contact-rich dynamics - smooth motions are frequently interrupted by discrete contact events ...
- **p. 2 / A. Rigid Body Multi-contact Models - extractive body cue:** Since the NCPs cannot be interpreted as the KKT conditions of a convex program, they are challenging to solve.
- **p. 3 / C. Reinforcement Learning for Dexterous Manipulation - extractive body cue:** Our proposed method aims to bridge this gap and even surpass state-of-the-art RL in suecess rate and manipulation accuracy.
- **p. 9 / B. MPC Setting and Results - extractive body cue:** [1p Peargal] $0.02 tm), 1-(dhggecd™)? < 0.015, is deemed a failure if the object does not satisfy (33) within the maximum MPC rollout length 11 ...
- **p. 15 / Figure/Table caption - extractive body cue:** Fig. 17: An failure case for stick reorientation,
- **Boundary to test:** [1p Peargal] $0.02 tm), 1-(dhggecd™)? < 0.015, is deemed a failure if the object does not satisfy (33) within the maximum MPC rollout length 11 = 2000.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Our method consistently achieves state-of-the ) a 96.5% average success rate across all objects | p. 1 (Abstract), p. 1 (body section boundary not confidently recovered) |
| Reported outcome | (1) The proposed complementarity-free MPC consistently outperforms Implicit MPC (ie., MPC with complementarity model) across various manipulation tasks in terms of success | p. 10 (B. MPC Setting and Results), p. 10 (B. MPC Setting and Results) |
| Failure/limitation | [1p Peargal] $0.02 tm), 1-(dhggecd™)? < 0.015, is deemed a failure if the object does not satisfy (33) within the maximum MPC rollout length 11 = 2000. | p. 9 (B. MPC Setting and Results), p. 15 (Figure/Table caption) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Paper-specific interface:** For simplicity, we model a manipulation system using the quasi-dynamic formulation (34, 14, 1, 41], which primarily captures the positional displacement of a contact-rich system in relation to contact interactions ... (p. 3, A. Optimization-based Quasi-Dynamic Contact Model).
- **Paper-specific mechanism:** Our method consistently achieves state-of-the ) a 96.5% average success rate across all objects (p. 1, Abstract).
- **Evidence boundary:** the reported outcome is For each object, we conduct 20 trials with different random inital and target poses. ‘The results are in Table IV, where we quantify the manipulation accuracy by (p. 9, B. MPC Setting and Results); the relevant task/metric cue is the manipulation accuracy is evaluated using (p. 9, B. MPC Setting and Results). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** [1p Peargal] $0.02 tm), 1-(dhggecd™)? < 0.015, is deemed a failure if the object does not satisfy (33) within the maximum MPC rollout length 11 = 2000. (p. 9, B. MPC Setting and Results).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `Manipulation, contact, tactile, and dexterity`; tags: `Robotics, contact-rich manipulation, multi-contact, trajectory optimization`.
- **Reading predecessor in the generated track queue:** Physics-Driven Data Generation for Contact-Rich Manipulation via Trajectory Optimization (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** SoftGym: Benchmarking Deep Reinforcement Learning for Deformable Object Manipulation (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** [1p Peargal] $0.02 tm), 1-(dhggecd™)? < 0.015, is deemed a failure if the object does not satisfy (33) within the maximum MPC rollout length 11 = 2000.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: For simplicity, we model a manipulation system using the quasi-dynamic formulation (34, 14, 1, 41], which primarily captures the positional displacement of a contact-rich system in relation to contact interactions ... (p. 3, A. Optimization-based Quasi-Dynamic Contact Model); preserve the objective/update rule: The time-stepping equation of the quasi-dynamic model is (p. 3, A. Optimization-based Quasi-Dynamic Contact Model).
2. Use the paper-reported task/data/environment cue: ABLE Il: The model setting for all objects and tasks. (p. 9, B. MPC Setting and Results).
3. Compare against the reported or matched baseline: Without ground support, the three fingertips (p. 10, B. MPC Setting and Results).
4. Report the body metric with its denominator and aggregation: the manipulation accuracy is evaluated using (p. 9, B. MPC Setting and Results).
5. Re-run the reported ablation or stress/failure condition: Without ground support, the three fingertips (p. 10, B. MPC Setting and Results); if none is reported, design one around: [1p Peargal] $0.02 tm), 1-(dhggecd™)? < 0.015, is deemed a failure if the object does not satisfy (33) within the maximum MPC rollout length 11 = 2000. (p. 9, B. MPC Setting and Results).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 1 (Abstract), p. 1 (Body text (section boundary not confidently recovered)), match the reported outcome at p. 9 (B. MPC Setting and Results), p. 12 (Figure/Table caption), p. 9 (B. MPC Setting and Results), and measure the boundary at p. 9 (B. MPC Setting and Results), p. 13 (A. TriFinger inchand Manipulation).

## Falsifiable research question

Under the paper's stated interface (For simplicity, we model a manipulation system using the quasi-dynamic formulation (34, 14, 1, 41], which primarily captures the positional displacement of ...), does the paper-specific mechanism (Our method consistently achieves state-of-the ) a 96.5% average success rate across all objects) retain the reported evaluation outcome (the manipulation accuracy is evaluated using) when tested against the paper's strongest explicit boundary ([1p Peargal] $0.02 tm), 1-(dhggecd™)? < 0.015, is deemed a failure if the object does not satisfy (33) ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (the manipulation accuracy is evaluated using) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (18 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** Our method consistently achieves state-of-the ) a 96.5% average success rate across all objects (p. 1, Abstract).
- **Paper-supported outcome:** For each object, we conduct 20 trials with different random inital and target poses. ‘The results are in Table IV, where we quantify the manipulation accuracy by (p. 9, B. MPC Setting and Results).
- **Strongest explicit boundary:** [1p Peargal] $0.02 tm), 1-(dhggecd™)? < 0.015, is deemed a failure if the object does not satisfy (33) within the maximum MPC rollout length 11 = 2000. (p. 9, B. MPC Setting and Results).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
