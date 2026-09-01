# Method - Ctrl-World: A Controllable Generative World Model for Robot Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://iclr.cc/virtual/2026/poster/10011332; PDF retrieval source: https://arxiv.org/pdf/2510.10125. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 4 (1 INTRODUCTION), p. 5 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION)): Specifically, robot observation ot = [I1 t , . . . , In t , qt] includes n camera views [I1 t , . . . , In t ] ...

## Method Body Digest

- **p. 3 / 1 INTRODUCTION - extractive body cue:** Specifically, robot observation ot = [I1 t , . . . , In t , qt] includes n camera views [I1 t , . . ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** In this paper, we introduce Ctrl-World, a Controllable, multi-view generative world model designed for policy-in-the-loop interaction, enabling multi-step rollouts entirely within imagination space, as illustrated ...
- **p. 4 / 1 INTRODUCTION - extractive body cue:** Published as a conference paper at ICLR 2026 Spatial Transformer Temporal Transformer (𝑩×𝑷, 𝑻, 𝑪) (𝑩×𝑻, 𝑷, 𝑪) Timeline Spatial Tokens History Poses + Action ...
- **p. 5 / 1 INTRODUCTION - extractive body cue:** 1: for i = 0 to M do 2: τ = [oi 0] 3: for j = 0 to N do 4: Current observation: ot ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Some works leverage video prediction models to synthesize robotic trajectories with fake action labels, and these synthetic trajectories can then be used for policy learning ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** To enable multi-step interaction with the policy in imagination space, W must generate future multi-view observations: ot+1, ..., ot+H ∼W(·/ot, At) (2) Then the final ...
- **p. 4 / 1 INTRODUCTION - extractive body cue:** Then this action-conditioned world model is fine-tuned with diffusion loss (Ho et al., 2020; Karras et al., 2022).
- **p. 2 / 1 INTRODUCTION - extractive body cue:** A complementary line of research integrates future-prediction objectives into generalist policies via co-training (Zhao et al., 2025; Li et al., 2025a; Zhu et al., 2025; ...

## Design Rationale

- **p. 2 / 1 INTRODUCTION - extractive body cue:** In this paper, we introduce Ctrl-World, a Controllable, multi-view generative world model designed for policy-in-the-loop interaction, enabling multi-step rollouts entirely within imagination space, as illustrated ...
- **p. 1 / ABSTRACT - extractive body cue:** We show that our method can accurately rank policy performance without real-world robot rollouts.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** Building on early works (Finn & Levine, 2017; Ebert et al., 2018; Xie et al., 2019; Dasari et al., 2019; Yang et al., 2023; Wu ...

## Source Evidence Cues

- **p. 3 / 1 INTRODUCTION - extractive body cue:** Specifically, robot observation ot = [I1 t , . . . , In t , qt] includes n camera views [I1 t , . . ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** In this paper, we introduce Ctrl-World, a Controllable, multi-view generative world model designed for policy-in-the-loop interaction, enabling multi-step rollouts entirely within imagination space, as illustrated ...
- **p. 4 / 1 INTRODUCTION - extractive body cue:** Published as a conference paper at ICLR 2026 Spatial Transformer Temporal Transformer (𝑩×𝑷, 𝑻, 𝑪) (𝑩×𝑻, 𝑷, 𝑪) Timeline Spatial Tokens History Poses + Action ...
- **p. 5 / 1 INTRODUCTION - extractive body cue:** 1: for i = 0 to M do 2: τ = [oi 0] 3: for j = 0 to N do 4: Current observation: ot ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Some works leverage video prediction models to synthesize robotic trajectories with fake action labels, and these synthetic trajectories can then be used for policy learning ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** To enable multi-step interaction with the policy in imagination space, W must generate future multi-view observations: ot+1, ..., ot+H ∼W(·/ot, At) (2) Then the final ...
- **p. 4 / 1 INTRODUCTION - extractive body cue:** Then this action-conditioned world model is fine-tuned with diffusion loss (Ho et al., 2020; Karras et al., 2022).
- **Detected method headings:** A MORE DETAILS FOR WORLD MODEL LEARNING (p. 16); B MORE DETAILS FOR POLICY EVALUATION (p. 16); C MORE DETAILS FOR POLICY IMPROVEMENT (p. 18)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Risk / failure representation | unsafe state와 uncertainty를 계산한다 | observation, nominal command, history | barrier, risk model, failure classifier, uncertainty 또는 safe set을 추정 | risk/margin/failure state | Specifically, robot observation ot = [I1 t , . . . , In t , qt] includes n camera views [I1 t ... | p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Filtering / recovery | nominal command를 안전 command로 바꾼다 | nominal action과 safety constraint | QP shield, backup policy, correction, stop 또는 recovery plan을 선택 | safe/recovery action | In this paper, we introduce Ctrl-World, a Controllable, multi-view generative world model designed for policy-in-the-loop interaction, enabling multi-step rollouts entirely within imagination ... | p. 2 (1 INTRODUCTION), p. 4 (1 INTRODUCTION) |
| Monitoring / re-entry | 실행 결과를 다시 risk decision에 반영한다 | executed action과 next observation | threshold, update, replan, abort 또는 return-to-task를 수행 | continue/correct/abort state | Published as a conference paper at ICLR 2026 Spatial Transformer Temporal Transformer (𝑩×𝑷, 𝑻, 𝑪) (𝑩×𝑻, 𝑷, 𝑪) Timeline Spatial Tokens History ... | p. 4 (1 INTRODUCTION), p. 5 (1 INTRODUCTION) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 2 / 1 INTRODUCTION - extractive body cue:** A complementary line of research integrates future-prediction objectives into generalist policies via co-training (Zhao et al., 2025; Li et al., 2025a; Zhu et al., 2025; ...
- **p. 1 / ABSTRACT - extractive body cue:** Both of these processes are slow, costly, and difficult to scale.
- **p. 4 / 1 INTRODUCTION - extractive body cue:** Then this action-conditioned world model is fine-tuned with diffusion loss (Ho et al., 2020; Karras et al., 2022).
- **p. 4 / 1 INTRODUCTION - extractive body cue:** While recent works (Du et al., 2023) explore the use of Vision-Language Models as general-purpose reward models, we leave such extensions to future work.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** (2) Frame-level action conditioning tightly aligns visual dynamics with control signals, ensuring that generated rollouts reflect the causal effect of each action.
- **Formal bridge:** state/history and risk h(s) -> filtered/recovery action u_safe -> task utility subject to safety constraint -> low violation/failure probability with useful intervention.
- **Equation/algorithm anchors:** p. 2 (1 INTRODUCTION), p. 4 (1 INTRODUCTION), p. 4 (1 INTRODUCTION).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Specifically, robot, observation, includes, camera, views, pose, policy, outputs, H-step, action, chunk, given, instruction | observation, uncertainty/risk estimate와 task command | body cue; exact tensor/frame verify |
| State/latent | Specifically, robot, observation, includes, camera, views, pose, policy, outputs, H-step | safe set, recovery state 또는 constraint margin | body cue; notation verify |
| Action/output | introduce, Ctrl-World, Controllable, multi-view, generative, world, model, designed, policy-in-the-loop, interaction | shielded, recovery 또는 safe action | body cue; unit/decoder verify |
| Objective/constraint | complementary, line, research, integrates, future-prediction, objectives, generalist, policies, co-training, Zhao | task utility subject to safety constraint | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 1 INTRODUCTION - extractive body cue:** Specifically, robot observation ot = [I1 t , . . . , In t , qt] includes n camera views [I1 t , . . ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** A modern generalist policy π typically maps multi-view observations and language instructions into a sequence of actions (Zhao et al., 2023; Black et al., 2025).
- **p. 5 / 1 INTRODUCTION - extractive body cue:** Specifically, we can (i) rephrase the instructions, since VLA policies tend to be steerable, exhibiting different behaviors in response to different instructions; or (ii) reset ...
- **p. 4 / 1 INTRODUCTION - extractive body cue:** To enable full controllability, we additionally condition the model on the action sequence [at+1:t+H] output by the policy.
- **p. 4 / 1 INTRODUCTION - extractive body cue:** Given an initial observation o0 and instruction l, a policy π together with the world model W can generate a synthetic trajectory τ.
- **p. 5 / 1 INTRODUCTION - extractive body cue:** 11: end for 12: Finetune πθ with Lθ = Eot,at:t+H∼Ds∥πθ(ot, l) -at:t+H∥2. initial observations and instructions, policy behavior tends to be highly deterministic.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Unlike these works, we leverage video generation to perform action-conditioned prediction, which enables using the model for both policy evaluation and policy improvement.
- **Normalized interface:** observation=observation, uncertainty/risk estimate와 task command; state=safe set, recovery state 또는 constraint margin; output/action=shielded, recovery 또는 safe action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | 현재 command의 one-step safety 또는 recovery trajectory horizon; exact lookahead 확인 필요. | During rollouts, the world model receives 15-step action chunks (corresponding to 1 s) and autoregressively predicts the next frames for 10 steps, ... | episode/sequence/action-chunk boundary |
| Rate / latency | nominal policy와 safety monitor/filter의 runtime rate를 별도로 기록한다. | Published as a conference paper at ICLR 2026 Cam 1 Generalist Policy Cam 2 Cam 3 … World Model Pred 1 Pred ... | Hz/fps, inference time and control rate |
| Memory | risk score, recent trajectory/history와 recovery state. | Published as a conference paper at ICLR 2026 Cam 1 Generalist Policy Cam 2 Cam 3 … World Model Pred 1 Pred ... | window and reset |
| Compute | risk inference, barrier/QP solve 또는 backup policy selection이 latency를 결정한다. | During rollouts, the world model receives 15-step action chunks (corresponding to 1 s) and autoregressively predicts the next frames for 10 steps, ... | hardware, batch and throughput |

## Training vs Inference

- **p. 2 / 1 INTRODUCTION - extractive body cue:** In this paper, we introduce Ctrl-World, a Controllable, multi-view generative world model designed for policy-in-the-loop interaction, enabling multi-step rollouts entirely within imagination space, as illustrated ...
- **p. 4 / 1 INTRODUCTION - extractive body cue:** Published as a conference paper at ICLR 2026 Spatial Transformer Temporal Transformer (𝑩×𝑷, 𝑻, 𝑪) (𝑩×𝑻, 𝑷, 𝑪) Timeline Spatial Tokens History Poses + Action ...
- **p. 5 / 1 INTRODUCTION - extractive body cue:** 1: for i = 0 to M do 2: τ = [oi 0] 3: for j = 0 to N do 4: Current observation: ot ...
- **p. 4 / 1 INTRODUCTION - extractive body cue:** Then this action-conditioned world model is fine-tuned with diffusion loss (Ho et al., 2020; Karras et al., 2022).
- **p. 5 / 5 EXPERIMENTS - extractive body cue:** We train the model on 2×8 H100 GPUs, with a total batch size of 64.
- **p. 6 / 5 EXPERIMENTS - extractive body cue:** During rollouts, the world model receives 15-step action chunks (corresponding to 1 s) and autoregressively predicts the next frames for 10 steps, producing 10 s-long ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Specifically, robot, observation, includes, camera, views, pose, policy, outputs, H-step, action, chunk, given, instruction, goal, world, model, predict, outcomes, executing.
- **Relevant PDF headings:** A MORE DETAILS FOR WORLD MODEL LEARNING (p. 16); B MORE DETAILS FOR POLICY EVALUATION (p. 16); C MORE DETAILS FOR POLICY IMPROVEMENT (p. 18).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Risk / failure representation | The DROID dataset (Khazatsky et al., 2024) contains 95,599 diverse trajectories collected from 564 scenes, providing dense coverage of the workspace. | p. 5 (5 EXPERIMENTS), p. 5 (5 EXPERIMENTS) |
| Filtering / recovery | Consistent with observations from prior work (Quevedo et al., 2025; Zhu et al., 2024), we also find that these baselines struggle to ... | p. 6 (5 EXPERIMENTS), p. 5 (5 EXPERIMENTS) |
| Monitoring / re-entry | Spatial Shape Towel-Dir Novel-Obj Average 0.0 0.2 0.4 0.6 0.8 1.0 Success rate 0.29 0.44 0.57 0.25 0.39 0.88 0.91 0.80 0.75 ... | p. 9 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS) |

## Failure and Ablation Link

- **p. 7 / 5 EXPERIMENTS - extractive body cue:** Published as a conference paper at ICLR 2026 Z axis -6 cm Z axis -6 cm Close Gripper Z axis +6 cm X axis -3 ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4: Controllability of Ctrl-World and ablations. Different action sequences can produce distinct rollouts in Ctrl-World with centimeter-level precision. Removing memory leads to blurry predictions ...
- **p. 6 / 5 EXPERIMENTS - extractive body cue:** Evaluated Camera Method Computation-based Model-based PSNR ↑ SSIM ↑ LPIPS ↓ FID ↓ FVD ↓ Third-view Camera Ctrl-World 23.56 0.828 0.091 25.00 97.4 Ctrl-World w/o ...
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** Ablations on memory components and frame-level conditions are in Table 2, which confirm the importance of each component.
- **p. 6 / Figure/Table caption - extractive body cue:** Table 2: Ablations on key components in Ctrl-World. Removing memory mechanisms, frame-level action conditioning or multi-view joint predictions all lead to a performance drop. 2025) ...
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** We now evaluate whether Ctrl-World can be used to generate synthetic post-training data for improving VLA models without real-world data.
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: Ctrl-World is designed for policy-in-the-loop rollouts with generalist robot policies. It generates joint multi-view predictions (including wrist views), enforces fine-grained action control via ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 4 (1 INTRODUCTION), p. 5 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), objective p. 2 (1 INTRODUCTION), p. 1 (ABSTRACT), p. 4 (1 INTRODUCTION), p. 4 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), temporal p. 6 (5 EXPERIMENTS), p. 2 (1 INTRODUCTION), p. 5 (5 EXPERIMENTS), p. 6 (5 EXPERIMENTS), p. 4 (1 INTRODUCTION), p. 1 (ABSTRACT).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
