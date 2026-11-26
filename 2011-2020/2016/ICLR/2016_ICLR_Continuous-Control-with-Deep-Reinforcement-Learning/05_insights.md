# Insights — Continuous Control with Deep Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (14 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1509.02971; PDF retrieval source: https://arxiv.org/pdf/1509.02971. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

> DOC-QA1 (2026-10-23): 제어문자·깨진 추출 구간과 직접 연결된 표 항목을 PDF 페이지 이미지와 대조했다. 확인 범위·원문 URL·페이지·수정 이력은 [대조 기록](../../../../work/sources/pdf_note_review_2026-10-23.json)에 있다. 노트 전체의 정독이나 모든 기존 주장에 대한 재검증을 뜻하지 않으며 reading status는 유지한다.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / 1 INTRODUCTION - extractive body cue:** In this work we present a model-free, off-policy actor-critic algorithm using deep function approximators that can learn policies in high-dimensional, continuous action spaces.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** In order to evaluate our method we constructed a variety of challenging physical control problems that involve complex multi-joint movements, unstable and rich contact dynamics, ...
- **p. 1 / ABSTRACT - extractive body cue:** We present an actor-critic, model-free algorithm based on the deterministic policy gradient that can operate over continuous action spaces.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** However, as we show below, a naive application of this actor-critic method with neural function approximators is unstable for challenging problems.
- **p. 3 / 2 BACKGROUND - extractive body cue:** Our contribution here is to provide modifications to DPG, inspired by the success of DQN, which allow it to use neural network function approximators to ...
- **p. 4 / 2 BACKGROUND - extractive body cue:** In the low-dimensional case, we used batch normalization on the state input and all layers of the µ network and all layers of the Q ...
- **p. 2 / 2 BACKGROUND - extractive body cue:** We model it as a Markov decision process with a state space S, action space A = IRN, an initial state distribution p(s1), transition dynamics ...
- **Contribution anchor:** p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (ABSTRACT), p. 2 (1 INTRODUCTION), p. 3 (2 BACKGROUND), p. 4 (2 BACKGROUND)

### Strongest assumption and failure boundary

- **p. 1 / 1 INTRODUCTION - extractive body cue:** However, this has many limitations, most notably the curse of dimensionality: the number of actions increases exponentially with the number of degrees of freedom.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Such large action spaces are difficult to explore efficiently, and thus successfully training DQN-like networks in this context is likely intractable.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Prior to DQN, it was generally believed that learning value functions using large, non-linear function approximators was difficult and unstable.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** A key feature of the approach is its simplicity: it requires only a straightforward actor-critic architecture and learning algorithm with very few "moving parts", making ...
- **p. 3 / 2 BACKGROUND - extractive body cue:** However, such approximators appear essential in order to learn and generalize on large state spaces.
- **p. 12 / Figure/Table caption - extractive body cue:** Table 2: Dimensionality of the MuJoCo tasks: the dimensionality of the underlying physics model dim(s), number of action dimensions dim(a) and observation dimensions dim(o). task ...
- **p. 8 / 6 CONCLUSION - extractive body cue:** The work combines insights from recent advances in deep learning and reinforcement learning, resulting in an algorithm that robustly solves challenging problems across a variety ...
- **Boundary to test:** Table 2: Dimensionality of the MuJoCo tasks: the dimensionality of the underlying physics model dim(s), number of action dimensions dim(a) and observation dimensions dim(o). task name Brief Description blockworld1 Agent is required ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | In this work we present a model-free, off-policy actor-critic algorithm using deep function approximators that can learn policies in high-dimensional, continuous action spaces. | p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Reported outcome | Table 1: Performance after training across all environments for at most 2.5 million steps. We report both the average and best observed (across 5 runs). All scores, except Torcs, are normalized so ... | p. 7 (Figure/Table caption), p. 5 (4 RESULTS) |
| Failure/limitation | Table 2: Dimensionality of the MuJoCo tasks: the dimensionality of the underlying physics model dim(s), number of action dimensions dim(a) and observation dimensions dim(o). task name Brief Description blockworld1 Agent is required ... | p. 12 (Figure/Table caption), p. 8 (6 CONCLUSION) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Paper-specific interface:** Recently, significant progress has been made by combining advances in deep learning for sensory processing (Krizhevsky et al., 2012) with reinforcement learning, resulting in the "Deep Q Network" (DQN) algorithm ... (p. 1, 1 INTRODUCTION).
- **Paper-specific mechanism:** In this work we present a model-free, off-policy actor-critic algorithm using deep function approximators that can learn policies in high-dimensional, continuous action spaces. (p. 1, 1 INTRODUCTION).
- **Evidence boundary:** the reported outcome is Table 1: Performance after training across all environments for at most 2.5 million steps. We report both the average and best observed (across 5 runs). All scores, except Torcs, are ... (p. 7, Figure/Table caption); the relevant task/metric cue is Cart Pendulum Swing-up Cartpole Swing-up Fixed Reacher Blockworld Gripper Puck Shooting Monoped Balancing Moving Gripper Cheetah Million Steps 0 1 1 0 1 1 0 0 1 1 0 0 ... (p. 6, 4 RESULTS). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** On both low-dimensional and from pixels, some replicas were able to learn reasonable policies that are able to complete a circuit around the track though other replicas failed to learn ... (p. 6, 4 RESULTS).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `RL, IL, offline learning, and robot data`; tags: `Robotics, Reinforcement Learning, continuous control, actor-critic`.
- **Reading predecessor in the generated track queue:** DrEureka: Language Model Guided Sim-To-Real Transfer (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Addressing Function Approximation Error in Actor-Critic Methods (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Table 2: Dimensionality of the MuJoCo tasks: the dimensionality of the underlying physics model dim(s), number of action dimensions dim(a) and observation dimensions dim(o). task name Brief Description blockworld1 Agent is required ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. **재현 계획의 원문 근거:** Background의 critic loss는 Q(s_t,a_t)와 Bellman target y_t 사이 squared error의 기대값이다. 실제 DDPG에서는 별도 target actor/critic과 soft update를 사용하므로, p. 3의 배경식을 최종 target-network 구현식으로 그대로 옮기지 않는다. ([PDF p. 3](https://arxiv.org/pdf/1509.02971#page=3), §2 Background, Eqs. (4)–(5); §3 p. 4). 실제 재현은 이 문헌 대조에서 수행하지 않았다.
2. Use the paper-reported task/data/environment cue: In all tasks, we ran experiments using both a low-dimensional state description (such as joint angles and positions) and high-dimensional renderings of the environment. (p. 5, 4 RESULTS).
3. Compare against the reported or matched baseline: We normalized the scores using two baselines. (p. 5, 4 RESULTS).
4. Report the body metric with its denominator and aggregation: Cart Pendulum Swing-up Cartpole Swing-up Fixed Reacher Blockworld Gripper Puck Shooting Monoped Balancing Moving Gripper Cheetah Million Steps 0 1 1 0 1 1 0 0 1 1 0 0 ... (p. 6, 4 RESULTS).
5. Re-run the reported ablation or stress/failure condition: We evaluated the policy periodically during training by testing it without exploration noise. (p. 5, 4 RESULTS); if none is reported, design one around: On both low-dimensional and from pixels, some replicas were able to learn reasonable policies that are able to complete a circuit around the track though other replicas failed to learn ... (p. 6, 4 RESULTS).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), match the reported outcome at p. 7 (Figure/Table caption), p. 5 (4 RESULTS), p. 5 (4 RESULTS), and measure the boundary at p. 6 (4 RESULTS), p. 9 (6 CONCLUSION).

## Falsifiable research question

Under the paper's stated interface (Recently, significant progress has been made by combining advances in deep learning for sensory processing (Krizhevsky et al., 2012) with reinforcement learning, ...), does the paper-specific mechanism (In this work we present a model-free, off-policy actor-critic algorithm using deep function approximators that can learn policies in high-dimensional, continuous action ...) retain the reported evaluation outcome (Cart Pendulum Swing-up Cartpole Swing-up Fixed Reacher Blockworld Gripper Puck Shooting Monoped Balancing Moving Gripper Cheetah Million Steps ...) when tested against the paper's strongest explicit boundary (On both low-dimensional and from pixels, some replicas were able to learn reasonable policies that are able to ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (Cart Pendulum Swing-up Cartpole Swing-up Fixed Reacher Blockworld Gripper Puck Shooting Monoped Balancing Moving Gripper Cheetah Million Steps ...) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (14 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** In this work we present a model-free, off-policy actor-critic algorithm using deep function approximators that can learn policies in high-dimensional, continuous action spaces. (p. 1, 1 INTRODUCTION).
- **Paper-supported outcome:** Table 1: Performance after training across all environments for at most 2.5 million steps. We report both the average and best observed (across 5 runs). All scores, except Torcs, are ... (p. 7, Figure/Table caption).
- **Strongest explicit boundary:** On both low-dimensional and from pixels, some replicas were able to learn reasonable policies that are able to complete a circuit around the track though other replicas failed to learn ... (p. 6, 4 RESULTS).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
