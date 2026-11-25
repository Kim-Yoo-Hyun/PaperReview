# MP1: MeanFlow Tames Policy Learning in 1-step for Robotic Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://ojs.aaai.org/index.php/AAAI/article/view/38919.
> PDF retrieval source: https://ojs.aaai.org/index.php/AAAI/article/view/38919. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / AAAI
- Authors: Juyi Sheng, Ziyi Wang, Peiming Li, Mengyuan Liu
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: Robotics, Imitation Learning, 3D point cloud, Flow Matching, action policy, inference efficiency, real-world manipulation
- Official paper: https://ojs.aaai.org/index.php/AAAI/article/view/38919
- Full-text retrieval: https://ojs.aaai.org/index.php/AAAI/article/view/38919
- Code/Project: https://github.com/LogSSim/MP1
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

MP1은 3D 점군에서 조건화한 평균 흐름을 학습해 신경망을 한 번 호출해 로봇 행동 궤적을 생성한다. [PDF 1쪽](https://ojs.aaai.org/index.php/AAAI/article/download/38919/42881#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** In robot manipulation, robot learning has become a prevailing approach.
- **p. 1 / Abstract - extractive body cue:** However, generative models within this field face a fundamental trade-off between the slow, iterative sampling of diffusion models and the architectural constraints of faster Flow-based ...
- **p. 1 / Abstract - extractive body cue:** To address these limitations, we introduce MP1, which pairs 3D point-cloud inputs with the MeanFlow paradigm to generate action trajectories in one network function evaluation ...
- **p. 1 / Abstract - extractive body cue:** By directly learning the interval-averaged velocity via the "MeanFlow Identity", our policy avoids any additional consistency constraints.
- **p. 1 / Abstract - extractive body cue:** This formulation eliminates numerical ODE-solver errors during inference, yielding more precise trajectories.
- **p. 2 / Abstract - extractive body cue:** However, diffusion still faces challenges related to inference time.
- **p. 2 / Abstract - extractive body cue:** However, 2D inputs often lack depth information, which limits the accuracy in completing tasks.

## Core Idea

- **p. 2 / Abstract - extractive body cue:** Our contributions are as follows: • We introduce MP1, the first MeanFlow-based robot learning framework.
- **p. 1 / Abstract - extractive body cue:** We validate our method on the Adroit and Meta-World benchmarks, as well as in real-world scenarios.
- **p. 1 / Abstract - extractive body cue:** To address these limitations, we introduce MP1, which pairs 3D point-cloud inputs with the MeanFlow paradigm to generate action trajectories in one network function evaluation ...
- **p. 2 / Abstract - extractive body cue:** We present the first adaptation of the MeanFlow (Geng et al.
- **p. 3 / Abstract - extractive body cue:** To address these challenges, we propose the MP1 (Fig.
- **p. 1 / Abstract - extractive body cue:** Because subtle scene-context variations are critical for robot learning, especially in few-shot learning, we introduce a lightweight Dispersive Loss that repels state embeddings during training, ...
- **p. 4 / Abstract - extractive body cue:** This can lead to a form of "feature collapse", where the policy network maps distinct environmental states that demand fundamentally different actions to nearly identical ...
- **p. 3 / Abstract - extractive body cue:** MP1: One-Step Trajectory Generation In the context of robot learning, the policy's task is to map a sequence of observations, including 3D point clouds P ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | MP1: One-Step Trajectory Generation In the context of robot learning, the policy's task is to map a sequence of observations, including 3D point clouds P and robotic states S, to a future ... | observation history와 expert trajectory/action | p. 3 (Abstract), p. 3 (Abstract) |
| State/latent | MP1, One-Step, Trajectory, Generation, context, robot, learning, policy, task, sequence, observations, including | behavior policy와 temporal action context | p. 3 (Abstract), p. 3 (Abstract), p. 4 (Abstract) |
| Output/action | The MP1 takes the historical observation point cloud and the robot's state as inputs. | predicted action 또는 action chunk | p. 3 (Abstract), p. 4 (Abstract), p. 4 (Abstract) |
| Objective/outcome | However, generative models within this field face a fundamental trade-off between the slow, iterative sampling of diffusion models and the architectural constraints of faster Flow-based methods, which often rely on explicit consistency ... | imitation error, task success, robustness와 compounding error | p. 1 (Abstract), p. 4 (Abstract), p. 4 (Abstract) |

## Main Claims and Actual Contribution

- MeanFlow의 구간 평균 속도를 직접 학습하고 비슷한 장면의 상태 표현을 구분하는 보조 손실을 추가한다. [PDF 1쪽](https://ojs.aaai.org/index.php/AAAI/article/download/38919/42881#page=1) · [PDF 3쪽](https://ojs.aaai.org/index.php/AAAI/article/download/38919/42881#page=3)
- Adroit·Meta-World와 실제 조작에서 성공률과 실행 시간을 측정해 여러 단계가 필요한 생성 정책과 비교했다. [PDF 6쪽](https://ojs.aaai.org/index.php/AAAI/article/download/38919/42881#page=6) · [PDF 7쪽](https://ojs.aaai.org/index.php/AAAI/article/download/38919/42881#page=7)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 5 (Figure/Table caption), p. 6 (Abstract) |
| Embodiment/environment | Conditioning on 3D point-cloud features, it learns effectively from a handful of demonstrations, yet delivers one-step sampling with SOTA success rates and millisecond-level inference latency. • We incorporate a lightweight Dispersive L ... | hardware/simulator version and reset protocol | p. 2 (Abstract), p. 7 (Abstract) |
| Dataset/benchmark | 3, we present the performance of MP1 and Flowpolicy on the hammer task in the simulation environment, as well as the experimental results for the hammer task in the real-world environment. | role, split, size and leakage | p. 2 (Abstract), p. 7 (Abstract), p. 7 (Abstract), p. 3 (Abstract) |
| Metric | Figure 4: Success rate curves of different methods on multi- ple Meta-World tasks. We compare the performance of MP1, FlowPolicy, and DP3 on four tasks. The x-axis represents training steps, and the ... | definition, denominator, direction and uncertainty | p. 6 (Figure/Table caption), p. 7 (Abstract), p. 7 (Abstract) |
| Baseline/ablation | MP1 is capable of one-step inference and, compared to state-of-the-art (SOTA) methods, improves the average success rate by 7.3% (Tab. | fair input/data/compute/action matching | p. 2 (Abstract), p. 5 (Figure/Table caption), p. 1 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 4 / Abstract - extractive body cue:** MP1 FlowPolicy Adroit: Hammer (FlowPolicy: 15.3ms/ MP1:7.1ms) Real-world: Hammer (FlowPolicy: 22.3s/ MP1:18.6s) failure success Figure 3: Qualitative comparison of the proposed MP1 and the previous ...
- **p. 2 / Abstract - extractive body cue:** 3D Input Robot Learning To overcome the limitations of 2D inputs, 3D inputs have gained prominence.
- **p. 2 / Abstract - extractive body cue:** However, a purely regression-based objective fails to impose explicit regularization on the policy's internal feature space (Wang and He 2025).
- **p. 4 / Abstract - extractive body cue:** Moreover, our method successfully completes the real-world hammer task, whereas FlowPolicy fails. estimate of the total derivative, with a stop-gradient sg(·) to ensure stability: utgt ...
- **p. 7 / Abstract - extractive body cue:** Conclusion In this paper, we address the limitations of existing Diffusion-based and Flow-based approaches by introducing MeanFlow into robot learning.
- **p. 3 / Abstract - extractive body cue:** Unlike Diffusion-based methods, our approach does not require multi-step denoising; distinct from existing Flowbased approaches, the MP1 does not rely on ODE solvers, consistency constraints, ...
- **p. 3 / Abstract - extractive body cue:** After passing through the MeanFlow, the model computes regression loss (Lcfg) between the mean velocity generated from the initial noise and the target velocity.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (Abstract), p. 1 (Abstract), p. 3 (Abstract)이다.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (8 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** However, diffusion still faces challenges related to inference time. (p. 2, Abstract).
- **Actual contribution:** Our contributions are as follows: • We introduce MP1, the first MeanFlow-based robot learning framework. (p. 2, Abstract).
- **Evaluation boundary:** Figure 6: Real-world setup. Real-world Experimental Results In Fig. 3, we present the performance of MP1 and Flowpol- icy on the hammer task in the simulation environment, as well as ... (p. 7, Figure/Table caption).
- **Explicit failure boundary:** However, a purely regression-based objective fails to impose explicit regularization on the policy's internal feature space (Wang and He 2025). (p. 2, Abstract).

## 원문과 공개 자료

- 코드 — 평균 흐름 행동 정책과 평가 · MP1/eval.py [배포 파일](https://raw.githubusercontent.com/LogSSim/MP1/e1e9e8fc60da9137b699ad4544d34fcb0222e624/MP1/eval.py)
