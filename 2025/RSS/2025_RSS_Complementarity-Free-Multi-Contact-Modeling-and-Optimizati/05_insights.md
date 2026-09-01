# Insights — Complementarity-Free Multi-Contact Modeling and Optimization for Dexterous Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (18 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p111.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p111.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / Abstract - extractive body cue:** Our method consistently achieves state-of-the ) a 96.5% average success rate across all objects
- **p. 1 / Front matter - extractive body cue:** 1: We propose a complementarty-free multi-contact model that a various challenging dexterous manipulation tasks, including fingertip in-air manipulation (cols.
- **p. 2 / Abstract - extractive body cue:** Our method sets a new benchmark for model-based contact-rich dexterous manipulation: « Highly versatile dexterity: 96.5% average success rate across all objects and environments « ...
- **p. 5 / B. New Complementarty-Free Multi-Contact Model - extractive body cue:** To circumvent the dual complementarity in (13), we propose ‘new contact model based on Lemma 1.
- **p. 2 / A. Rigid Body Multi-contact Models - extractive body cue:** (62, 33] developed penalty-based contact models.
- **p. 2 / A. Rigid Body Multi-contact Models - extractive body cue:** First, closed-form contact constraint resolution: our model builds on optimization-based contact dynamics (6, 39}, but instead of solving the primal [6, 39] or dual programs ...
- **p. 2 / A. Rigid Body Multi-contact Models - extractive body cue:** 1) Nonconvex Complementarity Contact Models: Rigid body contact dynamics is traditionally formulated using complermentarity models [S1, 49, 52]: it enforces no interpenetration and no contact ...
- **Contribution anchor:** p. 1 (Abstract), p. 1 (Front matter), p. 2 (Abstract), p. 5 (B. New Complementarty-Free Multi-Contact Model), p. 2 (A. Rigid Body Multi-contact Models), p. 2 (A. Rigid Body Multi-contact Models)

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
| Mechanism/contribution | Our method consistently achieves state-of-the ) a 96.5% average success rate across all objects | p. 1 (Abstract), p. 1 (Front matter) |
| Reported outcome | (1) The proposed complementarity-free MPC consistently outperforms Implicit MPC (ie., MPC with complementarity model) across various manipulation tasks in terms of success | p. 10 (B. MPC Setting and Results), p. 10 (B. MPC Setting and Results) |
| Failure/limitation | [1p Peargal] $0.02 tm), 1-(dhggecd™)? < 0.015, is deemed a failure if the object does not satisfy (33) within the maximum MPC rollout length 11 = 2000. | p. 9 (B. MPC Setting and Results), p. 15 (Figure/Table caption) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `RGB-D/point cloud, object state와 contact/task observation → object geometry, affordance, contact mode 또는 end-effector state → grasp, pose, force 또는 end-effector trajectory`.
- 이 논문의 재사용 가능한 지점은 This implementation creates « closed-loop control effect on the real system, ie., feedback from system state qf to control input 1 (qi를 In a manipulation system, the MPC policy is implemented in a receding horizon fashion, by repeatedly solving (8) at the real system state qf encountered at the policy rollout step & and ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 object geometry, affordance, contact mode 또는 end-effector state가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 [1p Peargal] $0.02 tm), 1-(dhggecd™)? < 0.015, is deemed a failure if the object does not satisfy (33) within the maximum MPC rollout length 11 = 2000.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Our method consistently achieves state-of-the ) a 96.5% average success rate across all objects
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `Manipulation, contact, tactile, and dexterity`; tags: `Robotics, contact-rich manipulation, multi-contact, trajectory optimization`.
- **Reading predecessor in the generated track queue:** Physics-Driven Data Generation for Contact-Rich Manipulation via Trajectory Optimization (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** SoftGym: Benchmarking Deep Reinforcement Learning for Deformable Object Manipulation (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** [1p Peargal] $0.02 tm), 1-(dhggecd™)? < 0.015, is deemed a failure if the object does not satisfy (33) within the maximum MPC rollout length 11 = 2000.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: ABLE Il: The model setting for all objects and tasks..
3. Compare against the body-reported baseline or a matched simpler baseline: (1) The proposed complementarity-free MPC consistently outperforms Implicit MPC (ie., MPC with complementarity model) across various manipulation tasks in terms of success.
4. Report the body metric and its denominator/aggregation: Fig. 12: Results of the TiiFinger in-hand manipulation for various objects. For each object on the x-axis, the upper panel shows the success rate across 20 trials based on criterion (49). The ....
5. Re-run the body-reported ablation/failure condition: Without ground support, the three fingertips.
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 2 (A. Rigid Body Multi-contact Models), p. 2 (A. Rigid Body Multi-contact Models), p. 5 (B. New Complementarty-Free Multi-Contact Model); the primary result is directionally consistent at p. 10 (B. MPC Setting and Results), p. 10 (B. MPC Setting and Results), p. 12 (Figure/Table caption); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 consistently, achieves, state-of-the mechanism이 (1) The proposed complementarity-free MPC consistently outperforms Implicit MPC (ie., MPC with complementarity model) across various ... 대비 Fig. 12: Results of the TiiFinger in-hand manipulation for various objects. For each object on the x-axis, the ...을 개선하고, [1p Peargal] $0.02 tm), 1-(dhggecd™)? < 0.015, is deemed a failure if the object does not ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
