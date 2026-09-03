# Method - Extreme Parkour with Legged Robots

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2309.14341; PDF retrieval source: https://arxiv.org/pdf/2309.14341. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 6 (3 Method), p. 5 (3 Method), p. 5 (3 Method), p. 6 (3 Method), p. 4 (3 Method), p. 4 (3 Method)): 3.2 Reinforcement Learning from Scandots (Phase 1) We use the above rewards to learn a policy using model-free RL [33] in simulation.

## Method Body Digest

- **p. 6 / 3 Method - extractive body cue:** 3.2 Reinforcement Learning from Scandots (Phase 1) We use the above rewards to learn a policy using model-free RL [33] in simulation.
- **p. 5 / 3 Method - extractive body cue:** We use Regularized Online Adaptation (ROA)[9] to train an estimator to recover environmental information from the history of observations.
- **p. 5 / 3 Method - extractive body cue:** In this paper, we use ROA for adaptation and two-phase training for the vision backbone but introduce key modifications for the challenging task of extreme ...
- **p. 6 / 3 Method - extractive body cue:** We use supervised learning to obtain a deployable policy which automatically estimates these quantities.
- **p. 4 / 3 Method - extractive body cue:** To train adaptive motor policies, recent approaches use two-phase student teacher training [18, 25, 36, 8].
- **p. 4 / 3 Method - extractive body cue:** We wish to train a single neural network that goes directly from raw depth and onboard sensing to joint angle commands.
- **p. 5 / 3 Method - extractive body cue:** While the above reward is sufficient for diverse parkour behavior, for challenging obstacles the robot tends to step close to the edge to minimize energy ...
- **p. 2 / 3 Method - extractive body cue:** 4 3.1 Unified Reward for Extreme Parkour . . . . . . . . . . . . . . . . . . ...

## Design Rationale

- **p. 3 / 1 Introduction - extractive body cue:** To allow the robot to adjust itself as per the obstacle type at deployment, we propose a novel dual distillation method.
- **p. 3 / 1 Introduction - extractive body cue:** Below, we summarize the main contributions: • A novel dual distillation method for distilling both agile motor commands and rapidly fluctuating heading directions from depth ...
- **p. 5 / 3 Method - extractive body cue:** We present a simple, unified reward formulation from which diverse behaviors emerge automatically and are perfectly adapted to the terrain geometry.

## Source Evidence Cues

- **p. 6 / 3 Method - extractive body cue:** 3.2 Reinforcement Learning from Scandots (Phase 1) We use the above rewards to learn a policy using model-free RL [33] in simulation.
- **p. 5 / 3 Method - extractive body cue:** We use Regularized Online Adaptation (ROA)[9] to train an estimator to recover environmental information from the history of observations.
- **p. 5 / 3 Method - extractive body cue:** In this paper, we use ROA for adaptation and two-phase training for the vision backbone but introduce key modifications for the challenging task of extreme ...
- **p. 6 / 3 Method - extractive body cue:** We use supervised learning to obtain a deployable policy which automatically estimates these quantities.
- **p. 4 / 3 Method - extractive body cue:** To train adaptive motor policies, recent approaches use two-phase student teacher training [18, 25, 36, 8].
- **p. 4 / 3 Method - extractive body cue:** We wish to train a single neural network that goes directly from raw depth and onboard sensing to joint angle commands.
- **Detected method headings:** 3 Method (p. 2); 3 Method (p. 4)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Command / terrain state | body state와 terrain/task context를 표현한다 | proprioception, terrain/perception, velocity command | history encoder, reference, terrain latent 또는 behavior mode를 구성 | locomotion context | 3.2 Reinforcement Learning from Scandots (Phase 1) We use the above rewards to learn a policy using model-free RL [33] in simulation. | p. 6 (3 Method), p. 5 (3 Method) |
| Whole-body policy / controller | context에서 joint target 또는 torque를 만든다 | context, body state, contact | RL policy, reference tracking, inverse dynamics 또는 whole-body control을 적용 | joint action/torque | We use Regularized Online Adaptation (ROA)[9] to train an estimator to recover environmental information from the history of observations. | p. 5 (3 Method), p. 5 (3 Method) |
| Adaptation / recovery | disturbance와 contact mismatch에 대응한다 | new observation/history와 failure signal | latent adaptation, foothold change, recovery 또는 replan을 수행 | updated command | In this paper, we use ROA for adaptation and two-phase training for the vision backbone but introduce key modifications for the challenging ... | p. 5 (3 Method), p. 6 (3 Method) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3 Method - extractive body cue:** While the above reward is sufficient for diverse parkour behavior, for challenging obstacles the robot tends to step close to the edge to minimize energy ...
- **p. 2 / 3 Method - extractive body cue:** 4 3.1 Unified Reward for Extreme Parkour . . . . . . . . . . . . . . . . . . ...
- **p. 5 / 3 Method - extractive body cue:** This is done to prevent the robot from exploiting the reward and learning the unintended behavior of turning around the obstacle.
- **p. 6 / 3 Method - extractive body cue:** The rewards defined above typically lead to a gait that uses all four legs.
- **p. 6 / 3 Method - extractive body cue:** 3.2 Reinforcement Learning from Scandots (Phase 1) We use the above rewards to learn a policy using model-free RL [33] in simulation.
- **p. 4 / 3 Method - extractive body cue:** Later works [9] introduce regularized online adaptation (ROA) to collapse this into a single phase.
- **Formal bridge:** body/proprioceptive/terrain state -> joint action/torque/footstep -> return, tracking or stability objective -> progress, balance and terrain robustness.
- **Equation/algorithm anchors:** p. 5 (3 Method).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | result, deployment, policy, only, outputs, agile, motor, commands, rapidly, adjusts, heading, directions, input, depth | proprioception, terrain/perception observation과 velocity command | body cue; exact tensor/frame verify |
| State/latent | result, deployment, policy, only, outputs, agile, motor, commands, rapidly, adjusts | body/contact state, foothold 또는 behavior mode | body cue; notation verify |
| Action/output | allow, robot, adjust, itself, obstacle, type, deployment, novel, dual, distillation | joint target, torque, footstep 또는 locomotion action | body cue; unit/decoder verify |
| Objective/constraint | While, above, reward, sufficient, diverse, parkour, behavior, challenging, obstacles, robot | return, tracking or stability objective | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 1 Introduction - extractive body cue:** As a result at deployment, the policy not only outputs agile motor commands but also rapidly adjusts heading directions all from input depth image.
- **p. 6 / 3 Method - extractive body cue:** This policy takes as input, the proprioception x, scandots m, target heading ˆd, walking flag W and commanded speed vcmd.
- **p. 6 / 3 Method - extractive body cue:** For exteroception, similar to the RMA architecture in [2] we replace the scandots input to the base policy with a convnet-GRU pipeline that accepts depth.
- **p. 5 / 3 Method - extractive body cue:** Action Deepcopy Supervise Phase 1 Phase 2 Scandots Proprioception ?
- **p. 5 / 3 Method - extractive body cue:** In phase 2, we distill from scandots into a policy that operates from onboard depth and automatically decides its heading (yaw) direction conditioned on the ...
- **p. 3 / 1 Introduction - extractive body cue:** A single neural network is trained via RL in simulation to directly output motor commands from pixels [2, 43, 23].
- **p. 4 / 3 Method - extractive body cue:** We wish to train a single neural network that goes directly from raw depth and onboard sensing to joint angle commands.
- **Normalized interface:** observation=proprioception, terrain/perception observation과 velocity command; state=body/contact state, foothold 또는 behavior mode; output/action=joint target, torque, footstep 또는 locomotion action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | gait/skill episode horizon과 short-horizon body control이 계층적으로 분리된다. | We use Regularized Online Adaptation (ROA)[9] to train an estimator to recover environmental information from the history of observations. | episode/sequence/action-chunk boundary |
| Rate / latency | high-level command, policy rate와 low-level torque rate를 구분; exact rate 확인 필요. | Later works [9] introduce regularized online adaptation (ROA) to collapse this into a single phase. | Hz/fps, inference time and control rate |
| Memory | proprioceptive history, terrain latent와 contact/body state. | We use Regularized Online Adaptation (ROA)[9] to train an estimator to recover environmental information from the history of observations. | window and reset |
| Compute | policy inference, adaptation encoder와 whole-body/control solve가 latency를 결정한다. | Each method is run for 5 trials on each terrain for each difficulty and the success rate is recorded (Fig. | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 3 Method - extractive body cue:** We use Regularized Online Adaptation (ROA)[9] to train an estimator to recover environmental information from the history of observations.
- **p. 5 / 3 Method - extractive body cue:** In this paper, we use ROA for adaptation and two-phase training for the vision backbone but introduce key modifications for the challenging task of extreme ...
- **p. 4 / 3 Method - extractive body cue:** To train adaptive motor policies, recent approaches use two-phase student teacher training [18, 25, 36, 8].
- **p. 4 / 3 Method - extractive body cue:** We wish to train a single neural network that goes directly from raw depth and onboard sensing to joint angle commands.
- **p. 6 / 3 Method - extractive body cue:** W is sampled randomly in {0,1} at training time and controlled via remote at deployment time.
- **p. 7 / 4 Results - extractive body cue:** The deployable policy can be trained on a single 3090 GPU in less than 20 hours.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Reinforcement, Learning, Scandots, Phase, above, rewards, learn, policy, model-free, simulation, Regularized, Online, Adaptation, ROA, train, estimator, recover, environmental, information, history.
- **Relevant PDF headings:** 3 Method (p. 2); 3 Method (p. 4).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Command / terrain state | Starred is recent concurrent work [47]. baseline comparison in simulation since it is infeasible to provide human joystick commands and provide real-world ... | p. 9 (4 Results), p. 7 (4 Results) |
| Whole-body policy / controller | We find that our method outperforms the baselines in terms of both metrics. | p. 8 (4 Results), p. 9 (4 Results) |
| Adaptation / recovery | In addition, its feet clearance also helps it to achieve some performance with noisy measurements. | p. 8 (4 Results), p. 8 (4 Results) |

## Failure and Ablation Link

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: Extreme Parkour: Low-cost robot with imprecise actuation can perform precise athletic behaviors directly from a high-dimensional image without any explicit mapping and planning. ...
- **p. 8 / 4 Results - extractive body cue:** 2 with velocity tracking in base frame used in [2]. • No feet clearance penalty (NoClear): Removes the penalization for stepping near the edges defined ...
- **p. 8 / 4 Results - extractive body cue:** Due to the robustness of the handstand policy, our robot is able to descend stairs in a handstand pose without vision and stabilize against the ...
- **p. 9 / 4 Results - extractive body cue:** NoClear is trained without feet edge penalty and therefore steps very close to the edge which is unstable and often falls.
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 7: For each terrain, we run 5 trials and record the number of successes. We find that ours has 20-80% higher success rate on ...
- **p. 8 / 4 Results - extractive body cue:** Noisy is able to get some performance but has very large variance since it can rely on collisions with its legs to sense terrain geometry ...
- **p. 9 / 4 Results - extractive body cue:** These sudden adjustments are out-ofdistribution for the policy and it cannot adapt fast enough, causing it to fail.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 6 (3 Method), p. 5 (3 Method), p. 5 (3 Method), p. 6 (3 Method), p. 4 (3 Method), p. 4 (3 Method), objective p. 5 (3 Method), p. 2 (3 Method), p. 5 (3 Method), p. 6 (3 Method), p. 6 (3 Method), p. 4 (3 Method), temporal p. 5 (3 Method), p. 4 (3 Method), p. 4 (3 Method), p. 5 (3 Method), p. 6 (3 Method), p. 6 (3 Method).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (12 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** For exteroception, similar to the RMA architecture in [2] we replace the scandots input to the base policy with a convnet-GRU pipeline that accepts depth. (p. 6, 3 Method).
- **Objective/update evidence:** 4 3.1 Unified Reward for Extreme Parkour . . . . . . . . . . . . . . . . . . . . . . . ... (p. 2, 3 Method).
- **Temporal/runtime evidence:** To train the vision backbone, a similar teacher-student framework is employed [2, 43, 23] where a teacher trained with privileged scandots information is distilled to a 4 (p. 4, 3 Method).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
