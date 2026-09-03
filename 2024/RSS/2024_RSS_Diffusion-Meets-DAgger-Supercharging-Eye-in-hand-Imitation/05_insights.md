# Insights — Diffusion Meets DAgger: Supercharging Eye-in-hand Imitation Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (14 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss20/p048.html; PDF retrieval source: https://arxiv.org/pdf/2402.17768.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / I. INTRODUCTION - extractive body cue:** We present experiments that evaluate the aforementioned design choices in developing a data creation framework to supercharge eye-in-hand imitation learning.
- **p. 2 / I. INTRODUCTION - extractive body cue:** Across all tasks, we see a sizeable improvement over vanilla behavior cloning, demonstrating the effectiveness of our framework Diffusion Meets DAgger (DMD).
- **p. 3 / III. APPROACH - extractive body cue:** To address this issue, as shown in Figure 2, our approach generates an augmented dataset ˜D and trains the policy jointly on ˜D ∪D.
- **p. 3 / III. APPROACH - extractive body cue:** 2: DMD System Overview: Our system operates in three stages. a) A diffusion model is trained, using task and play data, to synthesize novel views ...
- **p. 4 / III. APPROACH - extractive body cue:** Finetuning with around 50 trajectories leads to realistic novel view synthesis for our tasks as shown in Figure 7.
- **p. 3 / III. APPROACH - extractive body cue:** 3: DMD Architecture: We use the architecture introduced in [81], a U-Net diffusion model with blocks composed of convolution, self-attention, and cross attention layers.
- **p. 3 / III. APPROACH - extractive body cue:** We use action labels in the trajectory τ to compute the action label ˜at for this perturbed view.
- **Contribution anchor:** p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (III. APPROACH), p. 3 (III. APPROACH), p. 4 (III. APPROACH), p. 3 (III. APPROACH)

### Strongest assumption and failure boundary

- **p. 1 / I. INTRODUCTION - extractive body cue:** 1: Eye-in-hand Imitation learning with DMD: A common failure mode in an imitation learning setting is the problem of poor generalization due to compounding execution ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** However, DAgger [56] is challenging to put into practice: it requires an expert operator to supervise the robot during execution and guide it to recover ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Computing action labels for these samples present yet another challenge (Figure 5).
- **p. 9 / 24 Demo - extractive body cue:** A common failure case for BC is that as the robot rotates the cup with coffee beans, it does not move the cup closer to ...
- **p. 8 / 24 Demo - extractive body cue:** See videos on project website for failure modes.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** [86] seek to imitate, it fails when the gripper manipulates the scene, as in our tasks.
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** It c) NeRF Grabber-Mask ˜It Cannot generate in-hand apple Grabber needs to be paste in Move Forward Move Backward a) NeRF No-Mask ˜It Cannot generate ...
- **Boundary to test:** A common failure case for BC is that as the robot rotates the cup with coffee beans, it does not move the cup closer to the receiving cup; the blue cup then ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | We present experiments that evaluate the aforementioned design choices in developing a data creation framework to supercharge eye-in-hand imitation learning. | p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| Reported outcome | Fig. 9: Diffusion vs NeRF We visualize perturbed samples generated using DMD and NeRF with different masking strategies. The top row shows images generated for a forward movement relative to It; the ... | p. 7 (Figure/Table caption), p. 8 (Figure/Table caption) |
| Failure/limitation | A common failure case for BC is that as the robot rotates the cup with coffee beans, it does not move the cup closer to the receiving cup; the blue cup then ... | p. 9 (24 Demo), p. 1 (Figure/Table caption) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Paper-specific interface:** Purple-outlined images are diffusion-generated augmenting samples. c) The original task data and augmenting dataset are combined for policy learning. views from a wrist camera, and the actions at are the ... (p. 3, III. APPROACH).
- **Paper-specific mechanism:** We present experiments that evaluate the aforementioned design choices in developing a data creation framework to supercharge eye-in-hand imitation learning. (p. 2, I. INTRODUCTION).
- **Evidence boundary:** the reported outcome is Fig. 9: Diffusion vs NeRF We visualize perturbed samples generated using DMD and NeRF with different masking strategies. The top row shows images generated for a forward movement relative to ... (p. 7, Figure/Table caption); the relevant task/metric cue is This advantage results in higher task performance: DMD achieves a 100% success rate, while SPARTN [86] achieves only 50%. (p. 7, IV. EXPERIMENTS). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** A common failure case for BC is that as the robot rotates the cup with coffee beans, it does not move the cup closer to the receiving cup; the blue ... (p. 9, 24 Demo).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `RL, IL, offline learning, and robot data`; tags: `Robotics, Imitation Learning, DAgger, diffusion model, compounding error, eye-in-hand`.
- **Reading predecessor in the generated track queue:** Efficient Online Reinforcement Learning with Offline Data (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Consistency Policy: Accelerated Visuomotor Policies via Consistency Distillation (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** A common failure case for BC is that as the robot rotates the cup with coffee beans, it does not move the cup closer to the receiving cup; the blue cup then ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: Purple-outlined images are diffusion-generated augmenting samples. c) The original task data and augmenting dataset are combined for policy learning. views from a wrist camera, and the actions at are the ... (p. 3, III. APPROACH); preserve the objective/update rule: This gives the final training objective of: L = //ϵ -ϵθ(xb t, E(Ia), aTb, t)// where xb 0 = E(Ib). (p. 3, III. APPROACH).
2. Use the paper-reported task/data/environment cue: Finally, we test whether DMD improves generalization to novel objects and environment when provided with a diverse task dataset, as described in Section IV-E. (p. 5, IV. EXPERIMENTS).
3. Compare against the reported or matched baseline: On the pushing task, we present visual comparisons to NeRF-based synthesis approach SPARTN [86] in Section IV-A2 and in-depth quantitative analysis (ablation of design choices, offline evaluations) in Section IV-A3. (p. 5, IV. EXPERIMENTS).
4. Report the body metric with its denominator and aggregation: This advantage results in higher task performance: DMD achieves a 100% success rate, while SPARTN [86] achieves only 50%. (p. 7, IV. EXPERIMENTS).
5. Re-run the reported ablation or stress/failure condition: On the pushing task, we present visual comparisons to NeRF-based synthesis approach SPARTN [86] in Section IV-A2 and in-depth quantitative analysis (ablation of design choices, offline evaluations) in Section IV-A3. (p. 5, IV. EXPERIMENTS); if none is reported, design one around: A common failure case for BC is that as the robot rotates the cup with coffee beans, it does not move the cup closer to the receiving cup; the blue ... (p. 9, 24 Demo).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), match the reported outcome at p. 7 (Figure/Table caption), p. 6 (Figure/Table caption), p. 5 (IV. EXPERIMENTS), and measure the boundary at p. 9 (24 Demo), p. 10 (24 Demo).

## Falsifiable research question

Under the paper's stated interface (Purple-outlined images are diffusion-generated augmenting samples. c) The original task data and augmenting dataset are combined for policy learning. views from a ...), does the paper-specific mechanism (We present experiments that evaluate the aforementioned design choices in developing a data creation framework to supercharge eye-in-hand imitation learning.) retain the reported evaluation outcome (This advantage results in higher task performance: DMD achieves a 100% success rate, while SPARTN [86] achieves only ...) when tested against the paper's strongest explicit boundary (A common failure case for BC is that as the robot rotates the cup with coffee beans, it ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (This advantage results in higher task performance: DMD achieves a 100% success rate, while SPARTN [86] achieves only ...) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (14 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** We present experiments that evaluate the aforementioned design choices in developing a data creation framework to supercharge eye-in-hand imitation learning. (p. 2, I. INTRODUCTION).
- **Paper-supported outcome:** Fig. 9: Diffusion vs NeRF We visualize perturbed samples generated using DMD and NeRF with different masking strategies. The top row shows images generated for a forward movement relative to ... (p. 7, Figure/Table caption).
- **Strongest explicit boundary:** A common failure case for BC is that as the robot rotates the cup with coffee beans, it does not move the cup closer to the receiving cup; the blue ... (p. 9, 24 Demo).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
