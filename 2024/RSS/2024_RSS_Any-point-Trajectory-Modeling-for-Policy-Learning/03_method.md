# Method - Any-point Trajectory Modeling for Policy Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss20/p092.html; PDF retrieval source: https://www.roboticsproceedings.org/rss20/p092.html. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 3 (IV. METHOD), p. 3 (IV. METHOD), p. 4 (IV. METHOD), p. 4 (IV. METHOD), p. 5 (IV. METHOD), p. 5 (IV. METHOD)): To model the tracks, we propose a track transformer and illustrate the architecture in Figure 2 (a). a) Self-supervised Track Annotation.: Initially, we generate point trajectories from action-free videos for ...

## Method Body Digest

- **p. 3 / IV. METHOD - extractive body cue:** To model the tracks, we propose a track transformer and illustrate the architecture in Figure 2 (a). a) Self-supervised Track Annotation.: Initially, we generate point ...
- **p. 3 / IV. METHOD - extractive body cue:** As illustrated in Figure 2, ATM is a two-stage framework: first learn to predict future point trajectories in a video frame as the pre-training with ...
- **p. 4 / IV. METHOD - extractive body cue:** Track-guided Policy Learning After training a track transformer to predict future tracks based on observations, we can then learn policies guided by these predicted trajectories. ...
- **p. 4 / IV. METHOD - extractive body cue:** Action-labeled Demos (b) Stage 2: Track-guided Policy Learning (a) Stage 1: Any-point Trajectory Modeling action Track-guided Policy 𝜋 Track Transformer Language Instruction Off-the-shelf Tracker Fig.
- **p. 5 / IV. METHOD - extractive body cue:** Note that, the weights of our policy model are randomly initialized rather than copied from the pretrained Track Transformer like other video-pretraining methods [33, 28], ...
- **p. 5 / IV. METHOD - extractive body cue:** Given the current observation and the predicted tracks from the frozen pre-trained track transformer, we train a track-guided policy from a limited demonstration dataset.
- **p. 5 / IV. METHOD - extractive body cue:** Our track-guided policy is trained with MSE loss.
- **p. 3 / III. PRELIMINARY - extractive body cue:** To begin with, we denote the action-free video dataset as To = {(τ (i) o , ℓ(i))}No i=1, where ℓ(i) is the language instruction for ...

## Design Rationale

- **p. 2 / I. INTRODUCTION - extractive body cue:** We summarize our main contributions below: 1) We propose an Any-point Trajectory Model, a simple and novel framework that bridges video pre-training to policy learning, ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Additionally, we demonstrate that our method facilitates effective transfer learning from human videos and videos of a robot with a different morphology.
- **p. 3 / IV. METHOD - extractive body cue:** To model the tracks, we propose a track transformer and illustrate the architecture in Figure 2 (a). a) Self-supervised Track Annotation.: Initially, we generate point ...

## Source Evidence Cues

- **p. 3 / IV. METHOD - extractive body cue:** To model the tracks, we propose a track transformer and illustrate the architecture in Figure 2 (a). a) Self-supervised Track Annotation.: Initially, we generate point ...
- **p. 3 / IV. METHOD - extractive body cue:** As illustrated in Figure 2, ATM is a two-stage framework: first learn to predict future point trajectories in a video frame as the pre-training with ...
- **p. 4 / IV. METHOD - extractive body cue:** Track-guided Policy Learning After training a track transformer to predict future tracks based on observations, we can then learn policies guided by these predicted trajectories. ...
- **p. 4 / IV. METHOD - extractive body cue:** Action-labeled Demos (b) Stage 2: Track-guided Policy Learning (a) Stage 1: Any-point Trajectory Modeling action Track-guided Policy 𝜋 Track Transformer Language Instruction Off-the-shelf Tracker Fig.
- **p. 5 / IV. METHOD - extractive body cue:** Note that, the weights of our policy model are randomly initialized rather than copied from the pretrained Track Transformer like other video-pretraining methods [33, 28], ...
- **p. 5 / IV. METHOD - extractive body cue:** Given the current observation and the predicted tracks from the frozen pre-trained track transformer, we train a track-guided policy from a limited demonstration dataset.
- **Detected method headings:** IV. METHOD (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Demonstration representation | expert trajectory를 training pair/context로 정렬한다 | observation history, goal, expert action | temporal alignment, relabeling 또는 latent context construction을 수행 | training sample/context | To model the tracks, we propose a track transformer and illustrate the architecture in Figure 2 (a). a) Self-supervised Track Annotation.: Initially, ... | p. 3 (IV. METHOD), p. 3 (IV. METHOD) |
| Policy fitting | expert action distribution을 학습한다 | context와 action target | behavior cloning, adversarial, sequence, diffusion 또는 flow objective를 최적화 | policy/action distribution | As illustrated in Figure 2, ATM is a two-stage framework: first learn to predict future point trajectories in a video frame as ... | p. 3 (IV. METHOD), p. 4 (IV. METHOD) |
| Closed-loop rollout | distribution shift와 recovery를 확인한다 | current observation/history | action/chunk을 실행하고 feedback으로 다음 prediction을 갱신 | trajectory/failure signal | Track-guided Policy Learning After training a track transformer to predict future tracks based on observations, we can then learn policies guided by ... | p. 4 (IV. METHOD), p. 4 (IV. METHOD) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / IV. METHOD - extractive body cue:** Our track-guided policy is trained with MSE loss.
- **Formal bridge:** observation history o_{t−H:t} -> expert-like action/chunk a_{t:t+H} -> imitation or action-distribution loss -> closed-loop task success and robustness.
- **Equation/algorithm anchors:** p. 5 (IV. METHOD).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | begin, denote, action-free, video, dataset, where, language, instruction, episode, denotes, observation-only, trajectory, consisting, camera | observation history와 expert trajectory/action | body cue; exact tensor/frame verify |
| State/latent | begin, denote, action-free, video, dataset, where, language, instruction, episode, denotes | behavior policy와 temporal action context | body cue; notation verify |
| Action/output | summarize, main, contributions, below, Any-point, Trajectory, Model, simple, novel, framework | predicted action 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | track-guided, policy, trained, MSE, loss | imitation or action-distribution loss | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / III. PRELIMINARY - extractive body cue:** To begin with, we denote the action-free video dataset as To = {(τ (i) o , ℓ(i))}No i=1, where ℓ(i) is the language instruction for ...
- **p. 4 / IV. METHOD - extractive body cue:** ATM is permutation invariant to the input set of points, and we also find ATM to be robust to the distribution of the points, allowing ...
- **p. 4 / IV. METHOD - extractive body cue:** Action-labeled Demos (b) Stage 2: Track-guided Policy Learning (a) Stage 1: Any-point Trajectory Modeling action Track-guided Policy 𝜋 Track Transformer Language Instruction Off-the-shelf Tracker Fig.
- **p. 3 / IV. METHOD - extractive body cue:** More formally, given an image observation ot at timestep t, any set of 2D query points on the image frame pt = {pt,k}K k=1, and ...
- **p. 5 / IV. METHOD - extractive body cue:** Surprisingly, as the tracks already provide the finegrained subgoals, we find that the policy no longer needs language instruction at this stage as task specification.
- **p. 2 / I. INTRODUCTION - extractive body cue:** However, the lack of action labels makes utilization of video data in policy learning difficult.
- **p. 2 / I. INTRODUCTION - extractive body cue:** Previous works have addressed this by using self-supervised objectives for video pre-training to learn a feature representation of the observation for policy learning [43, 33, ...
- **Normalized interface:** observation=observation history와 expert trajectory/action; state=behavior policy와 temporal action context; output/action=predicted action 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single-step 또는 action chunk/trajectory horizon; exact chunk length는 exact value was not selected from the PDF body. | For each video, we randomly sample a time step ¯t and then randomly sample points on this frame and generate their tracks ... | episode/sequence/action-chunk boundary |
| Rate / latency | training inference와 deployed control tick을 분리; action chunk면 receding execution 여부 확인. | Formally, given a sequence of images from a video o1, ..., oT , any one of the time steps ¯t ∈[1, T], ... | Hz/fps, inference time and control rate |
| Memory | current observation, temporal history 또는 recurrent/sequence context. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | backbone/decoder inference, sampling steps와 action horizon이 latency를 결정한다. | not stated or recoverable in the selected PDF body | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / IV. METHOD - extractive body cue:** To model the tracks, we propose a track transformer and illustrate the architecture in Figure 2 (a). a) Self-supervised Track Annotation.: Initially, we generate point ...
- **p. 3 / IV. METHOD - extractive body cue:** As illustrated in Figure 2, ATM is a two-stage framework: first learn to predict future point trajectories in a video frame as the pre-training with ...
- **p. 4 / IV. METHOD - extractive body cue:** Track-guided Policy Learning After training a track transformer to predict future tracks based on observations, we can then learn policies guided by these predicted trajectories. ...
- **p. 5 / IV. METHOD - extractive body cue:** Note that, the weights of our policy model are randomly initialized rather than copied from the pretrained Track Transformer like other video-pretraining methods [33, 28], ...
- **p. 5 / IV. METHOD - extractive body cue:** Given the current observation and the predicted tracks from the frozen pre-trained track transformer, we train a track-guided policy from a limited demonstration dataset.
- **p. 4 / IV. METHOD - extractive body cue:** For the language instruction, we use a pre-trained BERT [9] encoder.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** model, tracks, track, transformer, illustrate, architecture, Figure, Self-supervised, Annotation, Initially, generate, point, trajectories, action-free, videos, trajectory, modeling, pre-training, illustrated, ATM.
- **Relevant PDF headings:** IV. METHOD (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Demonstration representation | All methods are trained on 10 action-labeled demonstration trajectories and 50 action-free video demonstration trajectories of the robot for each task, amounting ... | p. 5 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS) |
| Policy fitting | Fig. 4: We compare with state-of-the-art video pre-training methods on language-conditioned manipulation tasks in the LIBERO benchmark [27]. (a) Visualization of the ... | p. 6 (Figure/Table caption), p. 2 (2) Through extensive experiments on simulated bench) |
| Closed-loop rollout | Fig. 6: We implement ATM Diffusion Policy by adding the predicted future trajectories as additional conditioning and show consistent improvement over the ... | p. 7 (Figure/Table caption), p. 9 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 5 / V. EXPERIMENTS - extractive body cue:** Finally, we present ablation results in Sec.
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 9: Success rate of our policy trained with 4%, 10% and 20% action-labeled demos. Our policy trained with only 4% demos performs comparably to ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 7: Learning robotic skills from human videos for three tasks. We collect 100 videos of a human performing the tasks directly and 10 teleoperation ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 8: Cross-morphology skill transfer for a pick-and-place task. Here, we collect 160 action-free videos of a Franka arm and 10 action-labeled demonstrations from a ...
- **p. 5 / V. EXPERIMENTS - extractive body cue:** We perform experiments to answer the following questions: • How does ATM compare with state-of-the-art video pretraining and behaviour cloning baselines for learning from action-free ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 2: Overview of our framework. (a) In the first stage, given an action-free video dataset, we first sample 2D points on one video frame ...
- **p. 7 / 1) BC denotes the vanilla behavioral cloning which trains - extractive body cue:** Please see our video for failure cases of a video prediction model.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (IV. METHOD), p. 3 (IV. METHOD), p. 4 (IV. METHOD), p. 4 (IV. METHOD), p. 5 (IV. METHOD), p. 5 (IV. METHOD), objective p. 5 (IV. METHOD), temporal p. 3 (IV. METHOD), p. 3 (III. PRELIMINARY), p. 2 (I. INTRODUCTION), p. 7 (1) BC denotes the vanilla behavioral cloning which trains), p. 2 (I. INTRODUCTION), p. 4 (IV. METHOD).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (13 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** To model the tracks, we propose a track transformer and illustrate the architecture in Figure 2 (a). a) Self-supervised Track Annotation.: Initially, we generate point trajectories from action-free videos for ... (p. 3, IV. METHOD).
- **Objective/update evidence:** Our track-guided policy is trained with MSE loss. (p. 5, IV. METHOD).
- **Temporal/runtime evidence:** For each video, we randomly sample a time step ¯t and then randomly sample points on this frame and generate their tracks by running the tracker. (p. 3, IV. METHOD).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
