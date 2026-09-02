# Diffusion Meets DAgger: Supercharging Eye-in-hand Imitation Learning

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (14 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://www.roboticsproceedings.org/rss20/p048.html.
> PDF retrieval source: https://arxiv.org/pdf/2402.17768.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / RSS
- Authors: not duplicated here when not verified in the registry source
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: Robotics, Imitation Learning, DAgger, diffusion model, compounding error, eye-in-hand
- Official paper: https://www.roboticsproceedings.org/rss20/p048.html
- Full-text retrieval: https://arxiv.org/pdf/2402.17768.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-02 (14 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

RL, IL, offline learning, and robot data의 il 문제를 이해하기 위해 읽는다. 본문은 1: Eye-in-hand Imitation learning with DMD: A common failure mode in an imitation learning setting is the problem of poor generalization due to compounding execution errors at test time as shown in ...를 문제로 두고, We present experiments that evaluate the aforementioned design choices in developing a data creation framework to supercharge eye-in-hand imitation learning.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** A common failure mode for policies trained with imitation is compounding execution errors at test time.
- **p. 1 / Abstract - extractive body cue:** When the learned policy encounters states that are not present in the expert demonstrations, the policy fails, leading to degenerate behavior.
- **p. 1 / Abstract - extractive body cue:** The Dataset Aggregation, or DAgger approach to this problem simply collects more data to cover these failure states.
- **p. 1 / Abstract - extractive body cue:** However, in practice, this is often prohibitively expensive.
- **p. 1 / Abstract - extractive body cue:** In this work, we propose Diffusion Meets DAgger (DMD), a method that reaps the benefits of DAgger but without the cost, for eye-in-hand imitation learning ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** However, DAgger [56] is challenging to put into practice: it requires an expert operator to supervise the robot during execution and guide it to recover ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Computing action labels for these samples present yet another challenge (Figure 5).

## Core Idea

- **p. 2 / I. INTRODUCTION - extractive body cue:** We present experiments that evaluate the aforementioned design choices in developing a data creation framework to supercharge eye-in-hand imitation learning.
- **p. 2 / I. INTRODUCTION - extractive body cue:** Across all tasks, we see a sizeable improvement over vanilla behavior cloning, demonstrating the effectiveness of our framework Diffusion Meets DAgger (DMD).
- **p. 3 / III. APPROACH - extractive body cue:** To address this issue, as shown in Figure 2, our approach generates an augmented dataset ˜D and trains the policy jointly on ˜D ∪D.
- **p. 3 / III. APPROACH - extractive body cue:** 2: DMD System Overview: Our system operates in three stages. a) A diffusion model is trained, using task and play data, to synthesize novel views ...
- **p. 4 / III. APPROACH - extractive body cue:** Finetuning with around 50 trajectories leads to realistic novel view synthesis for our tasks as shown in Figure 7.
- **p. 3 / III. APPROACH - extractive body cue:** 3: DMD Architecture: We use the architecture introduced in [81], a U-Net diffusion model with blocks composed of convolution, self-attention, and cross attention layers.
- **p. 3 / III. APPROACH - extractive body cue:** We use action labels in the trajectory τ to compute the action label ˜at for this perturbed view.
- **p. 4 / III. APPROACH - extractive body cue:** We use structure from motion (SfM) algorithms [8, 15, 23, 59, 60, 69] to extract poses for the images in the trajectory τ.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Purple-outlined images are diffusion-generated augmenting samples. c) The original task data and augmenting dataset are combined for policy learning. views from a wrist camera, and the actions at are the relative end-effector ... | observation history와 expert trajectory/action | p. 3 (III. APPROACH), p. 1 (I. INTRODUCTION) |
| State/latent | Purple-outlined, images, diffusion-generated, augmenting, samples, original, task, data, dataset, combined, policy, learning | behavior policy와 temporal action context | p. 3 (III. APPROACH), p. 1 (I. INTRODUCTION), p. 2 (III. APPROACH) |
| Output/action | In this paper, we pursue an alternate paradigm: automatically generating observations and action labels for out-of-distribution states. | predicted action 또는 action chunk | p. 1 (I. INTRODUCTION), p. 2 (III. APPROACH), p. 1 (I. INTRODUCTION) |
| Objective/outcome | This gives the final training objective of: L = //ϵ -ϵθ(xb t, E(Ia), aTb, t)// where xb 0 = E(Ib). | imitation error, task success, robustness와 compounding error | p. 3 (III. APPROACH), p. 4 (III. APPROACH) |

## Main Claims and Actual Contribution

- **p. 2 / I. INTRODUCTION - extractive body cue:** We present experiments that evaluate the aforementioned design choices in developing a data creation framework to supercharge eye-in-hand imitation learning.
- **p. 2 / I. INTRODUCTION - extractive body cue:** Across all tasks, we see a sizeable improvement over vanilla behavior cloning, demonstrating the effectiveness of our framework Diffusion Meets DAgger (DMD).
- **p. 3 / III. APPROACH - extractive body cue:** To address this issue, as shown in Figure 2, our approach generates an augmented dataset ˜D and trains the policy jointly on ˜D ∪D.
- **p. 3 / III. APPROACH - extractive body cue:** 2: DMD System Overview: Our system operates in three stages. a) A diffusion model is trained, using task and play data, to synthesize novel views ...
- **p. 4 / III. APPROACH - extractive body cue:** Finetuning with around 50 trajectories leads to realistic novel view synthesis for our tasks as shown in Figure 7.
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 9: Diffusion vs NeRF We visualize perturbed samples generated using DMD and NeRF with different masking strategies. The top row shows images generated for ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 10: Comparison of BC, SPARTN, and DMD for Staying on Course. We show the trajectories executed by BC, SPARTN [86], and DMD over several ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** Adding ˜D generated by diffusion models improve performance on top of other augmentation techniques.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 7 (Figure/Table caption), p. 8 (Figure/Table caption) |
| Embodiment/environment | Finally, we test whether DMD improves generalization to novel objects and environment when provided with a diverse task dataset, as described in Section IV-E. | hardware/simulator version and reset protocol | p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Dataset/benchmark | (b) As shown in Figure 9, our diffusion model synthesizes higher quality images than NeRFs, especially when scenes undergo deformations. | role, split, size and leakage | p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |
| Metric | This advantage results in higher task performance: DMD achieves a 100% success rate, while SPARTN [86] achieves only 50%. | definition, denominator, direction and uncertainty | p. 7 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 8 (Figure/Table caption) |
| Baseline/ablation | Actions are executed on the robot by commanding the robot to go 1cm in the predicted direction. d) Baselines: We use vanilla behavior cloning on the expert data as the baseline as ... | fair input/data/compute/action matching | p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 9 / 24 Demo - extractive body cue:** A common failure case for BC is that as the robot rotates the cup with coffee beans, it does not move the cup closer to ...
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: Eye-in-hand Imitation learning with DMD: A common failure mode in an imitation learning setting is the problem of poor generalization due to compounding ...
- **p. 8 / 24 Demo - extractive body cue:** See videos on project website for failure modes.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** [86] seek to imitate, it fails when the gripper manipulates the scene, as in our tasks.
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** It c) NeRF Grabber-Mask ˜It Cannot generate in-hand apple Grabber needs to be paste in Move Forward Move Backward a) NeRF No-Mask ˜It Cannot generate ...
- **p. 8 / 24 Demo - extractive body cue:** BC often fails to lift the tall cups above the box and pushes the box forward continuously.
- **p. 9 / 24 Demo - extractive body cue:** 2) Online Validation: DMD succeeds 80% of the time while BC fails completely.

## Why Read It

RL, IL, offline learning, and robot data의 il 문제를 이해하기 위해 읽는다. 본문은 1: Eye-in-hand Imitation learning with DMD: A common failure mode in an imitation learning setting is the problem of poor generalization due to compounding execution errors at test time as shown in ...를 문제로 두고, We present experiments that evaluate the aforementioned design choices in developing a data creation framework to supercharge eye-in-hand imitation learning.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (III. APPROACH), p. 3 (III. APPROACH), p. 4 (III. APPROACH) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
