# Method - Scaffolding Dexterous Manipulation with Vision-Language Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (29 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=PdRf0O7baQ; PDF retrieval source: https://arxiv.org/pdf/2506.19212.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 5 (2. Plan Generation 𝜏), p. 5 (2. Plan Generation 𝜏), p. 6 (2. Plan Generation 𝜏), p. 6 (2. Plan Generation 𝜏), p. 2 (1 Introduction), p. 2 (1 Introduction)): 3D Proj. b) Inference 𝑥(1) board 𝑥(2) apple 𝑤1 wrist Environment (with keypoint tracking) Generate a motion trajectory for <task> with keypoints. 𝑥1:𝑇 1 𝑥1:𝑇 2 ෥𝑤1:𝑇 Action (𝑤𝑡+ Δ𝑤𝑡, ...

## Method Body Digest

- **p. 5 / 2. Plan Generation 𝜏 - extractive body cue:** 3D Proj. b) Inference 𝑥(1) board 𝑥(2) apple 𝑤1 wrist Environment (with keypoint tracking) Generate a motion trajectory for <task> with keypoints. 𝑥1:𝑇 1 𝑥1:𝑇 ...
- **p. 5 / 2. Plan Generation 𝜏 - extractive body cue:** In this section, we describe how we use the plan τ to further guide the learning and exploration of πl through the reward function, policy ...
- **p. 6 / 2. Plan Generation 𝜏 - extractive body cue:** Instead, we use ˜w1:T in the policy parameterization itself.
- **p. 6 / 2. Plan Generation 𝜏 - extractive body cue:** To further guide learning, we introduce a curriculum: the initial threshold δinit is linearly annealed to δinit/2 over the course of training.
- **p. 2 / 1 Introduction - extractive body cue:** Then, provided the initial keypoints and hand pose, the VLM generates the associated 3D trajectories for both object and hand motions to define the supervision ...
- **p. 2 / 1 Introduction - extractive body cue:** By controlling the robot's hands and fingers, the low-level policy learns to effectively track the trajectory and complete the desired task.
- **p. 1 / Abstract - extractive body cue:** Subsequently, we train a low-level residual RL policy in simulation to track these coarse trajectories or "scaffolds" with high fidelity.
- **p. 2 / 1 Introduction - extractive body cue:** So long as these motions generally encapsulate the desired behavior, RL can optimize per-timestep offsets and finger motions to maximize the tracking reward, ultimately surpassing ...

## Design Rationale

- **p. 1 / Abstract - extractive body cue:** Moreover, we showcase that our method transfers to realworld robotic hands without any human demonstrations or handcrafted rewards.
- **p. 2 / 1 Introduction - extractive body cue:** Building upon this insight, we introduce a framework for learning manipulation policies for dexterous robot hands with VLM-generated motion plans and residual RL.
- **p. 2 / 1 Introduction - extractive body cue:** Across 8 tasks, our method achieves close performance in both success rate and generalization to handcrafted, oracle plans despite requiring no manual reward engineering.

## Source Evidence Cues

- **p. 5 / 2. Plan Generation 𝜏 - extractive body cue:** 3D Proj. b) Inference 𝑥(1) board 𝑥(2) apple 𝑤1 wrist Environment (with keypoint tracking) Generate a motion trajectory for <task> with keypoints. 𝑥1:𝑇 1 𝑥1:𝑇 ...
- **p. 5 / 2. Plan Generation 𝜏 - extractive body cue:** In this section, we describe how we use the plan τ to further guide the learning and exploration of πl through the reward function, policy ...
- **p. 6 / 2. Plan Generation 𝜏 - extractive body cue:** Instead, we use ˜w1:T in the policy parameterization itself.
- **p. 6 / 2. Plan Generation 𝜏 - extractive body cue:** To further guide learning, we introduce a curriculum: the initial threshold δinit is linearly annealed to δinit/2 over the course of training.
- **p. 2 / 1 Introduction - extractive body cue:** Then, provided the initial keypoints and hand pose, the VLM generates the associated 3D trajectories for both object and hand motions to define the supervision ...
- **p. 2 / 1 Introduction - extractive body cue:** By controlling the robot's hands and fingers, the low-level policy learns to effectively track the trajectory and complete the desired task.
- **p. 1 / Abstract - extractive body cue:** Subsequently, we train a low-level residual RL policy in simulation to track these coarse trajectories or "scaffolds" with high fidelity.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | 3D Proj. b) Inference 𝑥(1) board 𝑥(2) apple 𝑤1 wrist Environment (with keypoint tracking) Generate a motion trajectory for <task> with keypoints. ... | p. 5 (2. Plan Generation 𝜏), p. 5 (2. Plan Generation 𝜏) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | In this section, we describe how we use the plan τ to further guide the learning and exploration of πl through the ... | p. 5 (2. Plan Generation 𝜏), p. 6 (2. Plan Generation 𝜏) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | Instead, we use ˜w1:T in the policy parameterization itself. | p. 6 (2. Plan Generation 𝜏), p. 6 (2. Plan Generation 𝜏) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 2 / 1 Introduction - extractive body cue:** So long as these motions generally encapsulate the desired behavior, RL can optimize per-timestep offsets and finger motions to maximize the tracking reward, ultimately surpassing ...
- **p. 5 / 2. Plan Generation 𝜏 - extractive body cue:** Naïvely, πl is optimized to maximize the expected cumulative reward provided plans sampled from πh, maxπl Eτ∼πh(·/oh 1 )Eol 1:T ∼πl(·/τ)[∑︁T t=1 rτ(ol t)] where ...
- **p. 1 / 1 Introduction - extractive body cue:** However, using RL simply shifts the burden from data collection to reward design.
- **p. 1 / Abstract - extractive body cue:** Moreover, we showcase that our method transfers to realworld robotic hands without any human demonstrations or handcrafted rewards.
- **p. 2 / 1 Introduction - extractive body cue:** Standard RL approaches for dexterous manipulation necessitate hand-crafting complex, task-specific reward functions.
- **p. 5 / 2. Plan Generation 𝜏 - extractive body cue:** Standard RL based approaches for dexterous manipulation often require complex, hand-crafted reward functions.
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 5 (2. Plan Generation 𝜏), p. 6 (2. Plan Generation 𝜏), p. 6 (2. Plan Generation 𝜏).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Proj, Inference, board, apple, wrist, Environment, keypoint, tracking, Generate, motion, trajectory, task, keypoints, Action | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | Proj, Inference, board, apple, wrist, Environment, keypoint, tracking, Generate, motion | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | Moreover, showcase, transfers, realworld, robotic, hands, without, human, demonstrations, handcrafted | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | long, motions, generally, encapsulate, desired, behavior, optimize, per-timestep, offsets, finger | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 5 / 2. Plan Generation 𝜏 - extractive body cue:** 3D Proj. b) Inference 𝑥(1) board 𝑥(2) apple 𝑤1 wrist Environment (with keypoint tracking) Generate a motion trajectory for <task> with keypoints. 𝑥1:𝑇 1 𝑥1:𝑇 ...
- **p. 5 / 2. Plan Generation 𝜏 - extractive body cue:** We learn πl using residual reinforcement learning [16, 26], which we formalize through a "plan" conditioned MDP on top of the low-level observation space Ol ...
- **p. 2 / 1 Introduction - extractive body cue:** A large amount of this complexity arises from the need to guide exploration; with large action spaces, dexterous hands need to be coaxed towards the ...
- **p. 6 / 2. Plan Generation 𝜏 - extractive body cue:** Specifically, the learned low-level policy πl θ predicts offsets ∆w to the wrist plan ˜wt instead of absolute actions wtarg.
- **p. 6 / 2. Plan Generation 𝜏 - extractive body cue:** This residual approach uses the world knowledge encoded by the VLM plan to guide exploration of the low-level policy to relevant parts of the state ...
- **p. 2 / 1 Introduction - extractive body cue:** Given a natural language instruction (e.g., "hammer once" Fig.
- **p. 1 / Abstract - extractive body cue:** Subsequently, we train a low-level residual RL policy in simulation to track these coarse trajectories or "scaffolds" with high fidelity.
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | So long as these motions generally encapsulate the desired behavior, RL can optimize per-timestep offsets and finger motions to maximize the tracking ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | We run 20 trials for each configuration for a total of 2000 evaluation episodes and average results across three seeds. | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not recovered | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | We run 20 trials for each configuration for a total of 2000 evaluation episodes and average results across three seeds. | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 2. Plan Generation 𝜏 - extractive body cue:** 3D Proj. b) Inference 𝑥(1) board 𝑥(2) apple 𝑤1 wrist Environment (with keypoint tracking) Generate a motion trajectory for <task> with keypoints. 𝑥1:𝑇 1 𝑥1:𝑇 ...
- **p. 6 / 2. Plan Generation 𝜏 - extractive body cue:** To further guide learning, we introduce a curriculum: the initial threshold δinit is linearly annealed to δinit/2 over the course of training.
- **p. 2 / 1 Introduction - extractive body cue:** Then, provided the initial keypoints and hand pose, the VLM generates the associated 3D trajectories for both object and hand motions to define the supervision ...
- **p. 1 / Abstract - extractive body cue:** Subsequently, we train a low-level residual RL policy in simulation to track these coarse trajectories or "scaffolds" with high fidelity.
- **p. 1 / 1 Introduction - extractive body cue:** The prevailing approach for training generalist policies - imitation learning from demonstrations [5, 49] - has achieved limited success with robot hands, primarily due to ...
- **p. 6 / 2. Plan Generation 𝜏 - extractive body cue:** Further training details and hyperparameters are in Section A.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Proj, Inference, board, apple, wrist, Environment, keypoint, tracking, Generate, motion, trajectory, task, keypoints, Action, Residual, Policy, PPO, Reward, Plan, Optional.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | The low-level policy is trained entirely in simulation using a digital twin of the real-world environment, and then executed in the real-world, ... | p. 9 (4 Experiments), p. 9 (4 Experiments) |
| Action / skill decoding | Figure 3: A depiction of the eight tasks used for evaluation. Each task belongs to one of four overarching categories. Methods Given ... | p. 7 (Figure/Table caption), p. 7 (4 Experiments) |
| Receding execution / feedback | Figure 5: (Left) The performance of our method as we iteratively refine the high-level policy πh by providing successful plans τ in-context. ... | p. 8 (Figure/Table caption), p. 23 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 23 / Figure/Table caption - extractive body cue:** Figure 11: Effect of Gaussian noise on VLM predictions in the simulation task suite. Success rate (in %) is averaged across three seeds; uncertainty indicates ...
- **p. 9 / 4 Experiments - extractive body cue:** (Right) Ablation of VLM components.
- **p. 7 / 4 Experiments - extractive body cue:** Thus, we mainly focus our experiments on comparison with a variety of oracles and ablations: • Iterative Keypoint Rewards (IKER): We implement Iterative Keypoint Rewards ...
- **p. 7 / 4 Experiments - extractive body cue:** We compare against additional reinforcement learning and imitation learning baselines and additionally ablate adding systematic noise into VLM predictions in Section E We evaluate two ...
- **p. 9 / 4 Experiments - extractive body cue:** To ablate the impact of using a VLM for keypoint detection and plan generation, we replace each component with an oracle in Fig.
- **p. 8 / 4 Experiments - extractive body cue:** To comprehensively evaluate the failure modes of our pipeline across all tasks, we present a Sankey diagram in Fig.
- **p. 8 / 4 Experiments - extractive body cue:** Our analysis reveals that the most significant failure mode is incomplete trajectory tracking, occurring in 26% of the rollouts.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 5 (2. Plan Generation 𝜏), p. 5 (2. Plan Generation 𝜏), p. 6 (2. Plan Generation 𝜏), p. 6 (2. Plan Generation 𝜏), p. 2 (1 Introduction), p. 2 (1 Introduction), objective p. 2 (1 Introduction), p. 5 (2. Plan Generation 𝜏), p. 1 (1 Introduction), p. 1 (Abstract), p. 2 (1 Introduction), p. 5 (2. Plan Generation 𝜏), temporal p. 2 (1 Introduction), p. 7 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments), p. 9 (4 Experiments), p. 9 (4 Experiments).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
