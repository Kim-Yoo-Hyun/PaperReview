# Insights — HumanPlus: Humanoid Shadowing and Imitation from Humans

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=WnSl42M9Z4; PDF retrieval source: https://arxiv.org/pdf/2406.10454. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1. Introduction - extractive body cue:** In this paper, we present a full-stack system for humanoids to learn motion and autonomous skills from human data.
- **p. 3 / 1. Introduction - extractive body cue:** Core to this system is both (1) a real-time shadowing system that allows human operators to whole-body control humanoids using a single RGB camera and ...
- **p. 3 / 1. Introduction - extractive body cue:** Using forward dynamics prediction on image features, our method shows improved performance by regularizing on image feature spaces and preventing the vision-based skill policy from ...
- **p. 4 / 4. Human Body and Hand Data - extractive body cue:** Each of the humanoid hip and shoulder joints consists of 3 orthogonal revolute joints, so can be viewed as one spherical joints.
- **p. 5 / 5. Shadowing of Human Motion - extractive body cue:** The humanoid target pose consists of target forward and lateral velocities, target roll and pitch, target yaw velocity and target joint angles, and is retargeted ...
- **p. 2 / 1. Introduction - extractive body cue:** We leverage this dataset by first retargeting human poses to humanoid poses and then training a task-agnostic low-level policy called Humanoid Shadowing Transformer conditioning on ...
- **p. 7 / 6. Imitation of Human Skills - extractive body cue:** In this work, we modify the Action Chunking Transformer [104] by removing its encoder-decoder architecture to develop a decoder-only Humanoid Imitation Transformer (HIT) for skill ...
- **Contribution anchor:** p. 2 (1. Introduction), p. 3 (1. Introduction), p. 3 (1. Introduction), p. 4 (4. Human Body and Hand Data), p. 5 (5. Shadowing of Human Motion), p. 2 (1. Introduction)

### Strongest assumption and failure boundary

- **p. 2 / 1. Introduction - extractive body cue:** This problem is further exacerbated by the lack of off-the-shelf and integrated hardware platforms.
- **p. 2 / 1. Introduction - extractive body cue:** Traditional approaches, such as decoupling the problem into perception, planning and tracking, and separate modularization of control for arms and legs [10, 10, 23, 40], ...
- **p. 3 / 1. Introduction - extractive body cue:** Shadowing provides an efficient data collection pipeline for diverse real-world tasks, bypassing the sim-to-real gap of RGB perception.
- **p. 8 / Figure/Table caption - extractive body cue:** Table 4: Robustness Evaluation. Our low-level policy (Ours) can withstand large disturbance forces, has a shorter recovery time, and enables more whole-body skills than the ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 3: Teleop Comparisons & User Studies. We report averaged completion time for 6 participants on 2 tasks. target poses while saving energy and avoiding ...
- **p. 10 / 9. Experiments on Imitation - extractive body cue:** Throughout the development of our system, we encountered several limitations.
- **p. 10 / 9. Experiments on Imitation - extractive body cue:** It fails the Wear a Shoe and Walk task completely, where depth perception is crucial.
- **Boundary to test:** Table 4: Robustness Evaluation. Our low-level policy (Ours) can withstand large disturbance forces, has a shorter recovery time, and enables more whole-body skills than the manufacturer controller (H1 Default). Kinesthetic Teaching ALOH ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | In this paper, we present a full-stack system for humanoids to learn motion and autonomous skills from human data. | p. 2 (1. Introduction), p. 3 (1. Introduction) |
| Reported outcome | Our HIT achieves higher success rates than other baselines across all tasks. | p. 10 (9. Experiments on Imitation), p. 9 (Figure/Table caption) |
| Failure/limitation | Table 4: Robustness Evaluation. Our low-level policy (Ours) can withstand large disturbance forces, has a shorter recovery time, and enables more whole-body skills than the manufacturer controller (H1 Default). Kinesthetic Teaching ALOH ... | p. 8 (Figure/Table caption), p. 7 (Figure/Table caption) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Paper-specific interface:** The complex dynamics and high-dimensional state and action spaces of humanoids pose difficulties in both perception and control. (p. 2, 1. Introduction).
- **Paper-specific mechanism:** In this paper, we present a full-stack system for humanoids to learn motion and autonomous skills from human data. (p. 2, 1. Introduction).
- **Evidence boundary:** the reported outcome is Shown in Table 5, we compare our imitation learning method Humanoid Imitation Transformer with three baseline methods: HIT policies with monocular inputs (Monocular), ACT [104], and Open-loop trajectory replay, across ... (p. 10, 9. Experiments on Imitation); the relevant task/metric cue is In contrast, our system has the lowest timeto-completion, has the highest success rate of stable standing, and is the only method that can be used for whole-body teleoperation, solving the ... (p. 10, 8.1. Comparisons with Other Teleoperation). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** It fails the Wear a Shoe and Walk task completely, where depth perception is crucial. (p. 10, 9. Experiments on Imitation).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `Locomotion, whole-body, mobile manipulation, and humanoids`; tags: `Robotics, humanoid, human-to-humanoid, Imitation Learning, teleoperation`.
- **Reading predecessor in the generated track queue:** Walk These Ways: Tuning Robot Control for Generalization with Multiplicity of Behavior (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** ASAP: Aligning Simulation and Real-World Physics for Learning Agile Humanoid Whole-Body Skills (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Table 4: Robustness Evaluation. Our low-level policy (Ours) can withstand large disturbance forces, has a shorter recovery time, and enables more whole-body skills than the manufacturer controller (H1 Default). Kinesthetic Teaching ALOH ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: The complex dynamics and high-dimensional state and action spaces of humanoids pose difficulties in both perception and control. (p. 2, 1. Introduction); preserve the objective/update rule: Typically, learning-based low-level policies are designed to be task-specific due to time-consuming reward engineering [19, 68], enabling the humanoid hardware to demonstrate only one skill at a time, such as ... (p. 2, 1. Introduction).
2. Use the paper-reported task/data/environment cue: The participants are tasked to perform the Rearrange Objects task and its variant, Rearrange Lower Objects, where an object is placed on a lower table of height 0.55m, requiring the ... (p. 9, 8.1. Comparisons with Other Teleoperation).
3. Compare against the reported or matched baseline: Overall HIT (Ours) outperforms others. (p. 9, 8. Experiments on Shadowing).
4. Report the body metric with its denominator and aggregation: In contrast, our system has the lowest timeto-completion, has the highest success rate of stable standing, and is the only method that can be used for whole-body teleoperation, solving the ... (p. 10, 8.1. Comparisons with Other Teleoperation).
5. Re-run the reported ablation or stress/failure condition: The participants are tasked to perform the Rearrange Objects task and its variant, Rearrange Lower Objects, where an object is placed on a lower table of height 0.55m, requiring the ... (p. 9, 8.1. Comparisons with Other Teleoperation); if none is reported, design one around: It fails the Wear a Shoe and Walk task completely, where depth perception is crucial. (p. 10, 9. Experiments on Imitation).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 2 (1. Introduction), p. 3 (1. Introduction), match the reported outcome at p. 10 (9. Experiments on Imitation), p. 9 (8.1. Comparisons with Other Teleoperation), p. 9 (8.1. Comparisons with Other Teleoperation), and measure the boundary at p. 10 (9. Experiments on Imitation), p. 10 (9. Experiments on Imitation).

## Falsifiable research question

Under the paper's stated interface (The complex dynamics and high-dimensional state and action spaces of humanoids pose difficulties in both perception and control.), does the paper-specific mechanism (In this paper, we present a full-stack system for humanoids to learn motion and autonomous skills from human data.) retain the reported evaluation outcome (In contrast, our system has the lowest timeto-completion, has the highest success rate of stable standing, and is ...) when tested against the paper's strongest explicit boundary (It fails the Wear a Shoe and Walk task completely, where depth perception is crucial.)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (In contrast, our system has the lowest timeto-completion, has the highest success rate of stable standing, and is ...) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (17 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** In this paper, we present a full-stack system for humanoids to learn motion and autonomous skills from human data. (p. 2, 1. Introduction).
- **Paper-supported outcome:** Shown in Table 5, we compare our imitation learning method Humanoid Imitation Transformer with three baseline methods: HIT policies with monocular inputs (Monocular), ACT [104], and Open-loop trajectory replay, across ... (p. 10, 9. Experiments on Imitation).
- **Strongest explicit boundary:** It fails the Wear a Shoe and Walk task completely, where depth perception is crucial. (p. 10, 9. Experiments on Imitation).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
