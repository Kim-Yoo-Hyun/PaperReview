# Method - Diffusion Meets DAgger: Supercharging Eye-in-hand Imitation Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (14 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss20/p048.html; PDF retrieval source: https://arxiv.org/pdf/2402.17768.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 3 (III. APPROACH), p. 3 (III. APPROACH), p. 4 (III. APPROACH), p. 4 (III. APPROACH), p. 2 (III. APPROACH), p. 2 (III. APPROACH)): 3: DMD Architecture: We use the architecture introduced in [81], a U-Net diffusion model with blocks composed of convolution, self-attention, and cross attention layers.

## Method Body Digest

- **p. 3 / III. APPROACH - extractive body cue:** 3: DMD Architecture: We use the architecture introduced in [81], a U-Net diffusion model with blocks composed of convolution, self-attention, and cross attention layers.
- **p. 3 / III. APPROACH - extractive body cue:** We use action labels in the trajectory τ to compute the action label ˜at for this perturbed view.
- **p. 4 / III. APPROACH - extractive body cue:** We use structure from motion (SfM) algorithms [8, 15, 23, 59, 60, 69] to extract poses for the images in the trajectory τ.
- **p. 4 / III. APPROACH - extractive body cue:** 2) Labeling Generated Images: For each image ˜It = f(It, ∆p) generated from an original image It, we use It+k as the target for generating ...
- **p. 2 / III. APPROACH - extractive body cue:** Policy π is trained using supervised learning to regress action at from images It.
- **p. 2 / III. APPROACH - extractive body cue:** Overview Given task data D, imitation learning learns a task policy π.
- **p. 3 / III. APPROACH - extractive body cue:** This gives the final training objective of: L = //ϵ -ϵθ(xb t, E(Ia), aTb, t)// where xb 0 = E(Ib).
- **p. 4 / III. APPROACH - extractive body cue:** This causes conflicting supervision, as the computed action does not make progress toward completing the task.

## Design Rationale

- **p. 2 / I. INTRODUCTION - extractive body cue:** We present experiments that evaluate the aforementioned design choices in developing a data creation framework to supercharge eye-in-hand imitation learning.
- **p. 2 / I. INTRODUCTION - extractive body cue:** Across all tasks, we see a sizeable improvement over vanilla behavior cloning, demonstrating the effectiveness of our framework Diffusion Meets DAgger (DMD).
- **p. 3 / III. APPROACH - extractive body cue:** To address this issue, as shown in Figure 2, our approach generates an augmented dataset ˜D and trains the policy jointly on ˜D ∪D.

## Source Evidence Cues

- **p. 3 / III. APPROACH - extractive body cue:** 3: DMD Architecture: We use the architecture introduced in [81], a U-Net diffusion model with blocks composed of convolution, self-attention, and cross attention layers.
- **p. 3 / III. APPROACH - extractive body cue:** We use action labels in the trajectory τ to compute the action label ˜at for this perturbed view.
- **p. 4 / III. APPROACH - extractive body cue:** We use structure from motion (SfM) algorithms [8, 15, 23, 59, 60, 69] to extract poses for the images in the trajectory τ.
- **p. 4 / III. APPROACH - extractive body cue:** 2) Labeling Generated Images: For each image ˜It = f(It, ∆p) generated from an original image It, we use It+k as the target for generating ...
- **p. 2 / III. APPROACH - extractive body cue:** Policy π is trained using supervised learning to regress action at from images It.
- **p. 2 / III. APPROACH - extractive body cue:** Overview Given task data D, imitation learning learns a task policy π.
- **Detected method headings:** III. APPROACH (p. 2)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Demonstration representation | expert trajectory를 training pair/context로 정렬한다 | observation history, goal, expert action | temporal alignment, relabeling 또는 latent context construction을 수행 | training sample/context | 3: DMD Architecture: We use the architecture introduced in [81], a U-Net diffusion model with blocks composed of convolution, self-attention, and cross ... | p. 3 (III. APPROACH), p. 3 (III. APPROACH) |
| Policy fitting | expert action distribution을 학습한다 | context와 action target | behavior cloning, adversarial, sequence, diffusion 또는 flow objective를 최적화 | policy/action distribution | We use action labels in the trajectory τ to compute the action label ˜at for this perturbed view. | p. 3 (III. APPROACH), p. 4 (III. APPROACH) |
| Closed-loop rollout | distribution shift와 recovery를 확인한다 | current observation/history | action/chunk을 실행하고 feedback으로 다음 prediction을 갱신 | trajectory/failure signal | We use structure from motion (SfM) algorithms [8, 15, 23, 59, 60, 69] to extract poses for the images in the trajectory ... | p. 4 (III. APPROACH), p. 4 (III. APPROACH) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / III. APPROACH - extractive body cue:** This gives the final training objective of: L = //ϵ -ϵθ(xb t, E(Ia), aTb, t)// where xb 0 = E(Ib).
- **p. 4 / III. APPROACH - extractive body cue:** This causes conflicting supervision, as the computed action does not make progress toward completing the task.
- **Formal bridge:** observation history o_{t−H:t} -> expert-like action/chunk a_{t:t+H} -> imitation or action-distribution loss -> closed-loop task success and robustness.
- **Equation/algorithm anchors:** p. 3 (III. APPROACH).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Purple-outlined, images, diffusion-generated, augmenting, samples, original, task, data, dataset, combined, policy, learning, views, wrist | observation history와 expert trajectory/action | body cue; exact tensor/frame verify |
| State/latent | Purple-outlined, images, diffusion-generated, augmenting, samples, original, task, data, dataset, combined | behavior policy와 temporal action context | body cue; notation verify |
| Action/output | present, experiments, evaluate, aforementioned, design, choices, developing, data, creation, framework | predicted action 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | gives, final, training, objective, aTb, where, causes, conflicting, supervision, computed | imitation or action-distribution loss | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / III. APPROACH - extractive body cue:** Purple-outlined images are diffusion-generated augmenting samples. c) The original task data and augmenting dataset are combined for policy learning. views from a wrist camera, and ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this paper, we pursue an alternate paradigm: automatically generating observations and action labels for out-of-distribution states.
- **p. 2 / III. APPROACH - extractive body cue:** Policy π is trained using supervised learning to regress action at from images It.
- **p. 1 / I. INTRODUCTION - extractive body cue:** We target imitation learning problems in the context of eyein-hand setups (i.e. setups where images come from a camera b) Current Practice (Dataset Aggregation) c) ...
- **p. 2 / III. APPROACH - extractive body cue:** The task data comprises a set of trajectories τi, each consisting of a sequence of image action pairs, (It, at).
- **p. 3 / III. APPROACH - extractive body cue:** The design of the conditional diffusion model is described in Section III-B, and the procedure for sampling augmenting images and computing action labels is detailed ...
- **p. 4 / III. APPROACH - extractive body cue:** The action label for ˜It is simply the action that conveys the agent from the pose depicted in ˜It to the pose in It+k.
- **Normalized interface:** observation=observation history와 expert trajectory/action; state=behavior policy와 temporal action context; output/action=predicted action 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single-step 또는 action chunk/trajectory horizon; exact chunk length는 exact value not recovered from the selected body cues. | Specifically, we learn a function f(It, ∆p) that synthesizes the observation ˜It at a small perturbation ∆p to the trajectory at time ... | episode/sequence/action-chunk boundary |
| Rate / latency | training inference와 deployed control tick을 분리; action chunk면 receding execution 여부 확인. | Purple-outlined images are diffusion-generated augmenting samples. c) The original task data and augmenting dataset are combined for policy learning. views from a ... | Hz/fps, inference time and control rate |
| Memory | current observation, temporal history 또는 recurrent/sequence context. | not recovered | window and reset |
| Compute | backbone/decoder inference, sampling steps와 action horizon이 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 2 / III. APPROACH - extractive body cue:** Policy π is trained using supervised learning to regress action at from images It.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** The policy is trained by L1 regression to the (unit length) actions using the Adam optimizer with a learning rate of 1e-4.
- **p. 4 / III. APPROACH - extractive body cue:** The pre-trained VQ-GAN codebooks is kept fixed.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** DMD, Architecture, introduced, U-Net, diffusion, model, blocks, composed, convolution, self-attention, cross, attention, layers, action, labels, trajectory, compute, label, perturbed, view.
- **Relevant PDF headings:** III. APPROACH (p. 2).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Demonstration representation | Finally, we test whether DMD improves generalization to novel objects and environment when provided with a diverse task dataset, as described in ... | p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Policy fitting | Actions are executed on the robot by commanding the robot to go 1cm in the predicted direction. d) Baselines: We use vanilla ... | p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |
| Closed-loop rollout | Fig. 9: Diffusion vs NeRF We visualize perturbed samples generated using DMD and NeRF with different masking strategies. The top row shows ... | p. 7 (Figure/Table caption), p. 8 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 5 / IV. EXPERIMENTS - extractive body cue:** We modified VIME's [78] grabber mount for Franka, allowing the robot to reach end-effector poses without reaching joint limits. spaces (pouring, hanging a shirt), generalization ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** 8: Effect of Using Different Future Frames for Labeling Augmenting Images: We experiment with using different future frame It+k for labeling the diffusion-generated images.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** On the pushing task, we present visual comparisons to NeRF-based synthesis approach SPARTN [86] in Section IV-A2 and in-depth quantitative analysis (ablation of design choices, ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** In contrast, images synthesized using our diffusion model move the camera as desired without creating any artifacts.
- **p. 9 / 24 Demo - extractive body cue:** A common failure case for BC is that as the robot rotates the cup with coffee beans, it does not move the cup closer to ...
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: Eye-in-hand Imitation learning with DMD: A common failure mode in an imitation learning setting is the problem of poor generalization due to compounding ...
- **p. 8 / 24 Demo - extractive body cue:** See videos on project website for failure modes.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (III. APPROACH), p. 3 (III. APPROACH), p. 4 (III. APPROACH), p. 4 (III. APPROACH), p. 2 (III. APPROACH), p. 2 (III. APPROACH), objective p. 3 (III. APPROACH), p. 4 (III. APPROACH), temporal p. 1 (I. INTRODUCTION), p. 3 (III. APPROACH), p. 4 (III. APPROACH), p. 4 (III. APPROACH), p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
