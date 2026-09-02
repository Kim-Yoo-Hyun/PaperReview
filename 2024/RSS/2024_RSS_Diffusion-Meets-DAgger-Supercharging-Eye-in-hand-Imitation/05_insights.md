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

- **Closed-loop position:** `observation history와 expert trajectory/action → behavior policy와 temporal action context → predicted action 또는 action chunk`.
- 이 논문의 재사용 가능한 지점은 Purple-outlined images are diffusion-generated augmenting samples. c) The original task data and augmenting dataset are combined for policy learning. views from a wrist camera, and the actions at are the relative end-effector ...를 In this paper, we pursue an alternate paradigm: automatically generating observations and action labels for out-of-distribution states.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 behavior policy와 temporal action context가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 A common failure case for BC is that as the robot rotates the cup with coffee beans, it does not move the cup closer to the receiving cup; the blue cup then ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: We present experiments that evaluate the aforementioned design choices in developing a data creation framework to supercharge eye-in-hand imitation learning.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `RL, IL, offline learning, and robot data`; tags: `Robotics, Imitation Learning, DAgger, diffusion model, compounding error, eye-in-hand`.
- **Reading predecessor in the generated track queue:** Efficient Online Reinforcement Learning with Offline Data (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Consistency Policy: Accelerated Visuomotor Policies via Consistency Distillation (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** A common failure case for BC is that as the robot rotates the cup with coffee beans, it does not move the cup closer to the receiving cup; the blue cup then ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Finally, we test whether DMD improves generalization to novel objects and environment when provided with a diverse task dataset, as described in Section IV-E..
3. Compare against the body-reported baseline or a matched simpler baseline: Actions are executed on the robot by commanding the robot to go 1cm in the predicted direction. d) Baselines: We use vanilla behavior cloning on the expert data as the baseline as ....
4. Report the body metric and its denominator/aggregation: This advantage results in higher task performance: DMD achieves a 100% success rate, while SPARTN [86] achieves only 50%..
5. Re-run the body-reported ablation/failure condition: We modified VIME's [78] grabber mount for Franka, allowing the robot to reach end-effector poses without reaching joint limits. spaces (pouring, hanging a shirt), generalization to new objects (stacking), precision in reaching ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 3 (III. APPROACH), p. 3 (III. APPROACH), p. 4 (III. APPROACH); the primary result is directionally consistent at p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 6 (IV. EXPERIMENTS); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 present, experiments, evaluate mechanism이 Actions are executed on the robot by commanding the robot to go 1cm in the predicted ... 대비 This advantage results in higher task performance: DMD achieves a 100% success rate, while SPARTN [86] achieves only ...을 개선하고, A common failure case for BC is that as the robot rotates the cup with coffee ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
