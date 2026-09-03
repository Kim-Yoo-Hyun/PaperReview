# Insights — Mobile ALOHA: Learning Bimanual Mobile Manipulation using Low-Cost Whole-Body Teleoperation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (20 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2401.02117; PDF retrieval source: https://arxiv.org/pdf/2401.02117. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1. Introduction - extractive body cue:** On the hardware front, we present Mobile ALOHA, a low-cost and whole-body teleoperation system for collecting bimanual mobile manipulation data.
- **p. 2 / 1. Introduction - extractive body cue:** The main contribution of this paper is a system for learning complex mobile bimanual manipulation tasks.
- **p. 1 / 1. Introduction - extractive body cue:** Imitation learning from human-provided demonstrations is a promising tool for developing generalist robots, as it allows people to teach arbitrary skills to robots.
- **p. 4 / 3. Mobile ALOHA Hardware - extractive body cue:** Connecting the operator to the mobile manipulator directly also enables coarse haptic feedback when the robot collides with objects.
- **p. 1 / Abstract - extractive body cue:** In this work, we develop a system for imitating mobile manipulation tasks that are bimanual and require whole-body control.
- **p. 5 / 3. Mobile ALOHA Hardware - extractive body cue:** The training objective for a mobile manipulation policy πm for a task m is E(oi,aiarms,ai base)∼Dm mobile  L(ai arms, ai base, πm(oi))  + ...
- **p. 2 / 1. Introduction - extractive body cue:** While many recent works demonstrate that highly expressive policy classes such as diffusion models and transformers can perform well on fine-grained, multi-modal manipulation tasks, it ...
- **Contribution anchor:** p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 4 (3. Mobile ALOHA Hardware), p. 1 (Abstract), p. 5 (3. Mobile ALOHA Hardware)

### Strongest assumption and failure boundary

- **p. 2 / 1. Introduction - extractive body cue:** (1) We lack accessible, plug-and-play hardware for whole-body teleoperation.
- **p. 2 / 1. Introduction - extractive body cue:** We seek to tackle the challenges of applying imitation learning to bimanual mobile manipulation in this paper.
- **p. 10 / 8. User Studies - extractive body cue:** Despite Mobile ALOHA's simplicity and performance, there are still limitations that we hope to address in future works.
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2: Hardware Details. Left: Mobile ALOHA has two wrist cameras and one top camera, with onboard power and compute. Middle: The teleoperation setup can ...
- **p. 8 / 6.1. Co-training Improves Performance - extractive body cue:** In all of these cases, compounding errors appear to be the main source of failure, either from the stochasticity of robot base velocity control or ...
- **p. 9 / 6.1. Co-training Improves Performance - extractive body cue:** The main failure modes are imprecise grasping on Lift Glass and Wipe as well as jerky motion when switching between chunks.
- **p. 8 / 6.1. Co-training Improves Performance - extractive body cue:** The only task that falls below 80% success is Cook Shrimp (40%), which is a 75-second long-horizon task for which we only collected 20 demonstrations.
- **Boundary to test:** Despite Mobile ALOHA's simplicity and performance, there are still limitations that we hope to address in future works.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | On the hardware front, we present Mobile ALOHA, a low-cost and whole-body teleoperation system for collecting bimanual mobile manipulation data. | p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Reported outcome | Co-training improves the whole-task success rate in 5 out of the 7 tasks, with a boost of 45%, 20%, 80%, 95% and 80% respectively. | p. 8 (6.1. Co-training Improves Performance), p. 7 (Figure/Table caption) |
| Failure/limitation | Despite Mobile ALOHA's simplicity and performance, there are still limitations that we hope to address in future works. | p. 10 (8. User Studies), p. 3 (Figure/Table caption) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Paper-specific interface:** While many recent works demonstrate that highly expressive policy classes such as diffusion models and transformers can perform well on fine-grained, multi-modal manipulation tasks, it is largely unclear whether the ... (p. 2, 1. Introduction).
- **Paper-specific mechanism:** The main contribution of this paper is a system for learning complex mobile bimanual manipulation tasks. (p. 2, 1. Introduction).
- **Evidence boundary:** the reported outcome is Table 1: Co-training improves ACT performance. Across 7 challenging mobile manipulation tasks, co-training with static ALOHA dataset consistently improve the success rate (%) of ACT. It is particularly important for ... (p. 7, Figure/Table caption); the relevant task/metric cue is Co-training improves the whole-task success rate in 5 out of the 7 tasks, with a boost of 45%, 20%, 80%, 95% and 80% respectively. (p. 8, 6.1. Co-training Improves Performance). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** In all of these cases, compounding errors appear to be the main source of failure, either from the stochasticity of robot base velocity control or from rich contacts such as ... (p. 8, 6.1. Co-training Improves Performance).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `CORE` in `Locomotion, whole-body, mobile manipulation, and humanoids`; tags: `Robotics, mobile manipulation, bimanual manipulation, teleoperation`.
- **Reading predecessor in the generated track queue:** OmniH2O: Universal and Dexterous Human-to-Humanoid Whole-Body Teleoperation and Learning (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Perpetual Humanoid Control for Real-time Simulated Avatars (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Despite Mobile ALOHA's simplicity and performance, there are still limitations that we hope to address in future works.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: While many recent works demonstrate that highly expressive policy classes such as diffusion models and transformers can perform well on fine-grained, multi-modal manipulation tasks, it is largely unclear whether the ... (p. 2, 1. Introduction); preserve the objective/update rule: The training objective for a mobile manipulation policy πm for a task m is E(oi,aiarms,ai base)∼Dm mobile  L(ai arms, ai base, πm(oi))  + E(oi,aiarms)∼Dstatic  L(ai arms, [0, ... (p. 5, 3. Mobile ALOHA Hardware).
2. Use the paper-reported task/data/environment cue: For example in the case of Lift Glass and Wipe sub-task, the #Attempts equals the number of success from the previous subtask Grasp Towel, as the robot could fail and ... (p. 8, 6.1. Co-training Improves Performance).
3. Compare against the reported or matched baseline: We start with ACT [104], the method introduced with ALOHA, and train it on all 7 tasks with and without co-training. (p. 8, 6.1. Co-training Improves Performance).
4. Report the body metric with its denominator and aggregation: Co-training improves the whole-task success rate in 5 out of the 7 tasks, with a boost of 45%, 20%, 80%, 95% and 80% respectively. (p. 8, 6.1. Co-training Improves Performance).
5. Re-run the reported ablation or stress/failure condition: We start with ACT [104], the method introduced with ALOHA, and train it on all 7 tasks with and without co-training. (p. 8, 6.1. Co-training Improves Performance); if none is reported, design one around: In all of these cases, compounding errors appear to be the main source of failure, either from the stochasticity of robot base velocity control or from rich contacts such as ... (p. 8, 6.1. Co-training Improves Performance).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 2 (1. Introduction), p. 2 (1. Introduction), match the reported outcome at p. 7 (Figure/Table caption), p. 8 (6.1. Co-training Improves Performance), p. 9 (6.1. Co-training Improves Performance), and measure the boundary at p. 8 (6.1. Co-training Improves Performance), p. 9 (6.1. Co-training Improves Performance).

## Falsifiable research question

Under the paper's stated interface (While many recent works demonstrate that highly expressive policy classes such as diffusion models and transformers can perform well on fine-grained, multi-modal ...), does the paper-specific mechanism (The main contribution of this paper is a system for learning complex mobile bimanual manipulation tasks.) retain the reported evaluation outcome (Co-training improves the whole-task success rate in 5 out of the 7 tasks, with a boost of 45%, ...) when tested against the paper's strongest explicit boundary (In all of these cases, compounding errors appear to be the main source of failure, either from the ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (Co-training improves the whole-task success rate in 5 out of the 7 tasks, with a boost of 45%, ...) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (20 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** The main contribution of this paper is a system for learning complex mobile bimanual manipulation tasks. (p. 2, 1. Introduction).
- **Paper-supported outcome:** Table 1: Co-training improves ACT performance. Across 7 challenging mobile manipulation tasks, co-training with static ALOHA dataset consistently improve the success rate (%) of ACT. It is particularly important for ... (p. 7, Figure/Table caption).
- **Strongest explicit boundary:** In all of these cases, compounding errors appear to be the main source of failure, either from the stochasticity of robot base velocity control or from rich contacts such as ... (p. 8, 6.1. Co-training Improves Performance).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
