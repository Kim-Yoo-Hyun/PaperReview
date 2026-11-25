# Method - Robotic World Model: A Neural Network Simulator for Robust Policy Optimization in Robotics

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (21 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2501.10100; PDF retrieval source: https://arxiv.org/pdf/2501.10100. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> DOC-QA1 (2026-10-23): 제어문자·깨진 추출 구간과 직접 연결된 표 항목을 PDF 페이지 이미지와 대조했다. 확인 범위·원문 URL·페이지·수정 이력은 [대조 기록](../../../work/sources/pdf_note_review_2026-10-23.json)에 있다. 노트 전체의 정독이나 모든 기존 주장에 대한 재검증을 뜻하지 않으며 reading status는 유지한다.

## Method in One Sentence

PDF body method statement (p. 6 (3 Approach), p. 4 (3 Approach), p. 4 (3 Approach), p. 5 (3 Approach), p. 5 (3 Approach), p. 6 (3 Approach)): Algorithm 1 Policy optimization with RWM 1: Initialize policy πθ, world model pϕ, and replay buffer D 2: for learning iterations = 1, 2, . . . do 3: Collect ...

## Method Body Digest

- **p. 6 / 3 Approach - extractive body cue:** Algorithm 1 Policy optimization with RWM 1: Initialize policy πθ, world model pϕ, and replay buffer D 2: for learning iterations = 1, 2, . ...
- **p. 4 / 3 Approach - extractive body cue:** The input to the world model consists of a sequence of observation-action pairs spanning M historical steps.
- **p. 4 / 3 Approach - extractive body cue:** World models [14] approximate the environment dynamics and facilitate policy optimization by enabling simulated environment interactions in imagination [16].
- **p. 5 / 3 Approach - extractive body cue:** The approach combines model-based imagination with model-free RL to achieve efficient and robust policy optimization, as outlined in Algorithm 1.
- **p. 5 / 3 Approach - extractive body cue:** Imagination agents are initialized from samples in D and simulate trajectories using the world model for T steps, enabling policy updates through a reinforcement learning ...
- **p. 6 / 3 Approach - extractive body cue:** 3 7: Update πθ using PPO or another reinforcement learning algorithm 8: end for While PPO is known for its strong performance in robotic tasks, ...
- **p. 19 / A.4.3 Collision Handling and Model Pretraining - extractive body cue:** As an alternative, we warm up the model using data from a suboptimal policy, which significantly stabilizes training.
- **p. 4 / 3 Approach - extractive body cue:** The agent seeks to learn a policy πθ : O →A that maximizes the expected discounted return Eπθ hP t≥0 γtrt i , where rt ...

## Design Rationale

- **p. 2 / 1 Introduction - extractive body cue:** Our contributions are summarized as follows: (i) We introduce a novel network architecture and training framework that enables the learning of reliable world models capable ...
- **p. 2 / 1 Introduction - extractive body cue:** In this work, we present a novel approach for learning world models that emphasizes robustness and accuracy over long-horizon predictions.
- **p. 4 / 3 Approach - extractive body cue:** To address this gap, we propose Robotic World Model (RWM), a novel framework for learning robust world models in partially observable and dynamically complex environments.

## Source Evidence Cues

- **p. 6 / 3 Approach - extractive body cue:** Algorithm 1 Policy optimization with RWM 1: Initialize policy πθ, world model pϕ, and replay buffer D 2: for learning iterations = 1, 2, . ...
- **p. 4 / 3 Approach - extractive body cue:** The input to the world model consists of a sequence of observation-action pairs spanning M historical steps.
- **p. 4 / 3 Approach - extractive body cue:** World models [14] approximate the environment dynamics and facilitate policy optimization by enabling simulated environment interactions in imagination [16].
- **p. 5 / 3 Approach - extractive body cue:** The approach combines model-based imagination with model-free RL to achieve efficient and robust policy optimization, as outlined in Algorithm 1.
- **p. 5 / 3 Approach - extractive body cue:** Imagination agents are initialized from samples in D and simulate trajectories using the world model for T steps, enabling policy updates through a reinforcement learning ...
- **p. 6 / 3 Approach - extractive body cue:** 3 7: Update πθ using PPO or another reinforcement learning algorithm 8: end for While PPO is known for its strong performance in robotic tasks, ...
- **p. 19 / A.4.3 Collision Handling and Model Pretraining - extractive body cue:** As an alternative, we warm up the model using data from a suboptimal policy, which significantly stabilizes training.
- **Detected method headings:** 3 Approach (p. 4); A.2 Network Architecture (p. 16); A.4.3 Collision Handling and Model Pretraining (p. 19)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Physics state / interface | robot·environment state를 simulator contract로 표현한다 | geometry, dynamics, contact, control input | rigid-body/contact/differentiable state를 구성 | simulator state | Algorithm 1 Policy optimization with RWM 1: Initialize policy πθ, world model pϕ, and replay buffer D 2: for learning iterations = ... | p. 6 (3 Approach), p. 4 (3 Approach) |
| Rollout / model query | candidate action의 consequence를 계산한다 | state와 action | physics step, learned dynamics, parallel 또는 differentiable rollout을 수행 | trajectory/reward/prediction | The input to the world model consists of a sequence of observation-action pairs spanning M historical steps. | p. 4 (3 Approach), p. 4 (3 Approach) |
| Learning / transfer handoff | simulation result를 policy 또는 real deployment로 전달한다 | rollout과 task objective | gradient, replay, randomization, calibration 또는 transfer adaptation을 적용 | policy/controller/data | World models [14] approximate the environment dynamics and facilitate policy optimization by enabling simulated environment interactions in imagination [16]. | p. 4 (3 Approach), p. 5 (3 Approach) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 3 Approach - extractive body cue:** The agent seeks to learn a policy πθ : O →A that maximizes the expected discounted return Eπθ hP t≥0 γtrt i , where rt ...
- **p. 19 / A.4.3 Collision Handling and Model Pretraining - extractive body cue:** First, the online dataset is extremely limited, as it is generated by only a single environment, akin to real-world constraints.
- **원문 대조:** N-step rollout에서 관측 예측 오차 L_o와 privileged-information 예측 오차 L_c를 합하고, horizon k에 따라 α^k로 가중한 뒤 1/N로 평균한다. 접촉 등의 privileged information은 추가 학습 목표로 사용된다. ([PDF p. 4](https://arxiv.org/pdf/2501.10100#page=4), §3.2 Self-supervised Autoregressive Training, Eq. (2)).
- **p. 5 / 3 Approach - extractive body cue:** To improve gradient propagation through autoregressive predictions, we apply reparameterization tricks to enable effective end-to-end optimization.
- **p. 19 / A.4.3 Collision Handling and Model Pretraining - extractive body cue:** During policy optimization, MBPO-PPO treats these termination predictions as episode-ending events in imagination rollouts, affecting PPO's return computation and state values.
- **p. 5 / 3 Approach - extractive body cue:** Rewards are computed from imagined observations and privileged information.
- **Formal bridge:** sim state s_t and parameters δ -> sim action/rollout -> physics/model/planning objective -> fidelity, throughput and downstream task utility.
- **Equation/algorithm anchors:** p. 4 (3 Approach), p. 4 (3 Approach), p. 5 (3 Approach), p. 19 (A.4.3 Collision Handling and Model Pretraining), p. 5 (3 Approach), p. 6 (3 Approach).

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Reinforcement, Learning, World, Models, formulate, problem, modeling, environment, Partially, Observable, Markov, Decision, Process, POMDP | simulated state, geometry, contact와 control input | body cue; exact tensor/frame verify |
| State/latent | Reinforcement, Learning, World, Models, formulate, problem, modeling, environment, Partially, Observable | dynamics/contact state 또는 learned simulator representation | body cue; notation verify |
| Action/output | contributions, summarized, follows, introduce, novel, network, architecture, training, framework, enables | simulation step, trajectory 또는 environment query | body cue; unit/decoder verify |
| Objective/constraint | agent, seeks, learn, policy, maximizes, expected, discounted, return, where, reward | physics/model/planning objective | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 3 Approach - extractive body cue:** 3.1 Reinforcement Learning and World Models We formulate the problem by modeling the environment as a Partially Observable Markov Decision Process (POMDP) [40], defined by ...
- **p. 4 / 3 Approach - extractive body cue:** The input to the world model consists of a sequence of observation-action pairs spanning M historical steps.
- **p. 5 / 3 Approach - extractive body cue:** During imagination, the actions are generated recursively by the policy πθ conditioned on the observations predicted by the world model pϕ, which is further conditioned ...
- **p. 6 / 3 Approach - extractive body cue:** Algorithm 1 Policy optimization with RWM 1: Initialize policy πθ, world model pϕ, and replay buffer D 2: for learning iterations = 1, 2, . ...
- **p. 1 / 1 Introduction - extractive body cue:** While model-free RL algorithms such as Proximal Policy Optimization (PPO) [2] and Soft Actor-Critic (SAC) [1] have demonstrated impressive results in simulation, their high interaction ...
- **p. 19 / A.4.3 Collision Handling and Model Pretraining - extractive body cue:** During policy optimization, MBPO-PPO treats these termination predictions as episode-ending events in imagination rollouts, affecting PPO's return computation and state values.
- **p. 5 / 3 Approach - extractive body cue:** Imagination agents are initialized from samples in D and simulate trajectories using the world model for T steps, enabling policy updates through a reinforcement learning ...
- **Normalized interface:** observation=simulated state, geometry, contact와 control input; state=dynamics/contact state 또는 learned simulator representation; output/action=simulation step, trajectory 또는 environment query.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | simulator step, rollout length와 task episode horizon을 분리한다. | The control frequency of the robot is at 50 Hz. | episode/sequence/action-chunk boundary |
| Rate / latency | simulation step rate와 learned policy/control rate를 별도로 기록한다. | The model is trained with history horizon M = 32 and forecast horizon N = 8. | Hz/fps, inference time and control rate |
| Memory | sim state, contact state와 rollout/replay buffer. | The model is trained with history horizon M = 32 and forecast horizon N = 8. | window and reset |
| Compute | physics solver, parallel environments와 differentiable rollout cost가 결정한다. | The control frequency of the robot is at 50 Hz. | hardware, batch and throughput |

## Training vs Inference

- **p. 6 / 3 Approach - extractive body cue:** Algorithm 1 Policy optimization with RWM 1: Initialize policy πθ, world model pϕ, and replay buffer D 2: for learning iterations = 1, 2, . ...
- **p. 6 / 3 Approach - extractive body cue:** 3 7: Update πθ using PPO or another reinforcement learning algorithm 8: end for While PPO is known for its strong performance in robotic tasks, ...
- **p. 19 / A.4.3 Collision Handling and Model Pretraining - extractive body cue:** As an alternative, we warm up the model using data from a suboptimal policy, which significantly stabilizes training.
- **p. 19 / A.4.3 Collision Handling and Model Pretraining - extractive body cue:** Training the world model entirely from scratch on such data would lead to severe overfitting and long training times.
- **p. 8 / 4 Experiments - extractive body cue:** The policy is trained using estimated rewards computed from predicted observations by RWM.
- **p. 8 / 4 Experiments - extractive body cue:** 4.4 Policy Learning and Hardware Transfer Using MBPO-PPO, we train a goal-conditioned velocity tracking policy for ANYmal D and Unitree G1 leveraging RWM.

## Method-Specific Formal Details

- **Body-defined terms:** Algorithm, Policy, optimization, RWM, Initialize, world, model, replay, buffer, learning, iterations, Collect, observation-action, pairs, interacting, environment, Update, autoregressive, training, data.
- **Relevant PDF headings:** 3 Approach (p. 4); A.2 Network Architecture (p. 16); A.4.3 Collision Handling and Model Pretraining (p. 19).

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Physics state / interface | The experiments are designed to assess the accuracy and robustness of RWM, evaluate its architectural and training design choices, and demonstrate its ... | p. 6 (4 Experiments), p. 9 (4 Experiments) |
| Rollout / model query | Figure 4: Autoregressive trajectory prediction errors across diverse robotic environments and network architectures. RWM trained with autoregressive training (RWM-AR) consistently outperforms baseline ... | p. 8 (Figure/Table caption), p. 7 (4 Experiments) |
| Learning / transfer handoff | A.4.1 reveals that, while extending both M and N improves accuracy, practical considerations of computational cost necessitate careful tuning of these hyperparameters ... | p. 6 (4 Experiments), p. 8 (4 Experiments) |

## Failure and Ablation Link

- **p. 9 / 4 Experiments - extractive body cue:** In addition, the need for additional interaction with the environment to fine-tune the world model highlights areas for further refinement.
- **p. 9 / 4 Experiments - extractive body cue:** In contrast, SHAC fails to converge, producing unstable behaviors that degrade both policy and model quality.
- **p. 9 / 4 Experiments - extractive body cue:** 5 Limitations The policy learned with RWM and MBPO-PPO surpasses existing MBRL methods in both robustness and generalization.
- **p. 10 / 6 Conclusion - extractive body cue:** In this work, we present RWM, a robust and scalable framework for learning world models tailored to complex robotic tasks.
- **p. 10 / 6 Conclusion - extractive body cue:** The results highlight RWM 's potential to enable adaptive, robust, and high-performing robotic systems, setting a foundation for broader adoption of model-based approaches in real-world ...
- **p. 7 / 4 Experiments - extractive body cue:** Grey curves represent the MLP baseline, which exhibits significantly higher error accumulation and reduced robustness to noise.
- **p. 7 / 4 Experiments - extractive body cue:** To assess the robustness of RWM, we analyze its performance under Gaussian noise perturbations applied to both observations and actions.

## Reproduction Checklist

[공통 검토 기준](../../../research/READING_STATUS.md#note-checks)

## Verification Questions

- **Evidence anchors reviewed:** method p. 6 (3 Approach), p. 4 (3 Approach), p. 4 (3 Approach), p. 5 (3 Approach), p. 5 (3 Approach), p. 6 (3 Approach), objective p. 4 (3 Approach), p. 19 (A.4.3 Collision Handling and Model Pretraining), p. 4 (3 Approach), p. 5 (3 Approach), p. 19 (A.4.3 Collision Handling and Model Pretraining), p. 5 (3 Approach), temporal p. 6 (4 Experiments), p. 6 (4 Experiments), p. 8 (4 Experiments), p. 4 (3 Approach), p. 4 (3 Approach), p. 5 (3 Approach).
