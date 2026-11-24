# WoCoCo: Learning Whole-Body Humanoid Control with Sequential Contacts

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.mlr.press/v270/zhang25a.html.
> PDF retrieval source: https://arxiv.org/pdf/2406.06005. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / CoRL
- Authors: Chong Zhang, Wenli Xiao, Tairan He, Guanya Shi
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: REFERENCE
- Tags: Robotics, humanoid, whole-body control, sequential contacts, Reinforcement Learning
- Official paper: https://proceedings.mlr.press/v270/zhang25a.html
- Full-text retrieval: https://arxiv.org/pdf/2406.06005
- Code/Project: https://lecar-lab.github.io/wococo/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 한 줄 요약과 핵심 기여 두 개를 각 문장에 인용한 판본의 원문에서 확인했다.

## Why This Paper Is Here

WoCoCo는 접촉 순서가 정해진 휴머노이드 과제를 접촉 단계들로 분해해 전신 강화학습 정책을 훈련한다. [PDF 1쪽](https://raw.githubusercontent.com/mlresearch/v270/d9fe509ba390176a5fd650178a381a0a7b2d4f64/assets/zhang25a/zhang25a.pdf#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Humanoid activities involving sequential contacts are crucial for complex robotic interactions and operations in the real world and are traditionally solved by model-based motion planning, ...
- **p. 1 / Abstract - extractive body cue:** Although model-free reinforcement learning (RL) has become a powerful tool for versatile and robust whole-body humanoid control, it still requires tedious task-specific tuning and state ...
- **p. 1 / Abstract - extractive body cue:** In this work, we propose WoCoCo (Whole-Body Control with Sequential Contacts), a unified framework to learn whole-body humanoid control with sequential contacts by naturally decomposing ...
- **p. 1 / Abstract - extractive body cue:** Such decomposition facilitates simple and general policy learning pipelines through task-agnostic reward and sim-to-real designs, requiring only one or two task-related terms to be specified ...
- **p. 1 / Abstract - extractive body cue:** We demonstrated that endto-end RL-based controllers trained with WoCoCo enable four challenging wholebody humanoid tasks involving diverse contact sequences in the real world without any ...
- **p. 8 / 1 Introduction - extractive body cue:** 6 Limitation and Future Works One limitation of our work is the lacking knowledge of when the controller will fail.
- **p. 5 / 1 Introduction - extractive body cue:** However, model mismatch and perturbations such as uneven terrains pose significant challenges to these controllers, for which RL can be a promising solution [13, 22].

## Core Idea

- **p. 3 / 1 Introduction - extractive body cue:** In Section 4, we show how our framework, WoCoCo, can be applied to a variety of challenging dynamic tasks with flexible definitions and representations of ...
- **p. 5 / 1 Introduction - extractive body cue:** 4 Case Studies In this section, we show how our framework, WoCoCo, can be applied to various challenging tasks with different contact sequences.
- **p. 3 / 1 Introduction - extractive body cue:** In this paper, we study tasks where contact stages are predefined (e.g., heuristically designed), and our method can seamlessly be integrated with high-level contact planners ...
- **p. 2 / 1 Introduction - extractive body cue:** To better facilitate exploration, we propose a task-agnostic curiosity reward term.
- **p. 4 / 1 Introduction - extractive body cue:** Instead, we propose to use count-based curiosity rewards via random neural network (NN) based hash, inspired by Tang et al.
- **p. 3 / 1 Introduction - extractive body cue:** To develop RL-based controllers for these tasks, we formulate the policy learning problem as an extended Markov Decision Process (MDP) M = ⟨S, A, T ...
- **p. 6 / 1 Introduction - extractive body cue:** Lower Row: We transfer the policy to the real world, testing jumps with double-foot contacts at different heights and a "hug" posture. provided current and ...
- **p. 1 / 1 Introduction - extractive body cue:** Provided specific contact plans, the typical solution is to employ model-based motion planning or trajectory optimization to generate whole-body references for tracking [2, 3, 4].

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | [28, 40], we stack 3 control steps of previous joint states and actions, and append them to the policy observations to enhance the robustness by temporal memory. | proprioception, reference pose/motion, visual or language command | p. 5 (1 Introduction), p. 3 (1 Introduction) |
| State/latent | stack, control, steps, previous, joint, states, actions, append, them, policy, observations, enhance | whole-body pose, balance/contact state와 skill/mode | p. 5 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction) |
| Output/action | To develop RL-based controllers for these tasks, we formulate the policy learning problem as an extended Markov Decision Process (MDP) M = ⟨S, A, T , R, γ, Gcon, Gtask⟩of state st ... | joint/whole-body action, motion target 또는 task trajectory | p. 3 (1 Introduction), p. 3 (1 Introduction), p. 8 (1 Introduction) |
| Objective/outcome | The objective is to maximize the expected return E [P t γtrt] by finding an optimal policy at = π∗(st/gcon i:I , gtask i:I ). | tracking, balance, skill/task success와 recovery | p. 3 (1 Introduction), p. 2 (1 Introduction), p. 6 (1 Introduction) |

## Main Claims and Actual Contribution

- 예정한 접촉이 이루어지는지를 이용해 단계 전이를 정의하고 여러 과제에서 공통 보상 항을 재사용한다. [PDF 3쪽](https://raw.githubusercontent.com/mlresearch/v270/d9fe509ba390176a5fd650178a381a0a7b2d4f64/assets/zhang25a/zhang25a.pdf#page=3) · [PDF 4쪽](https://raw.githubusercontent.com/mlresearch/v270/d9fe509ba390176a5fd650178a381a0a7b2d4f64/assets/zhang25a/zhang25a.pdf#page=4)
- 점프·상자 운반·박수와 발 구르기·등반에서 학습된 접촉 순서와 실물 동작 수행을 평가한다. [PDF 6쪽](https://raw.githubusercontent.com/mlresearch/v270/d9fe509ba390176a5fd650178a381a0a7b2d4f64/assets/zhang25a/zhang25a.pdf#page=6) · [PDF 7쪽](https://raw.githubusercontent.com/mlresearch/v270/d9fe509ba390176a5fd650178a381a0a7b2d4f64/assets/zhang25a/zhang25a.pdf#page=7)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 6 (Figure/Table caption), p. 6 (1 Introduction) |
| Embodiment/environment | Left Middle Right Figure 4: Learned dancing motions in simulation and the real-world. | hardware/simulator version and reset protocol | p. 7 (1 Introduction), p. 7 (1 Introduction) |
| Dataset/benchmark | By altering the destinations, we make the robot generate ball trajectories forming "WoCoCo". | role, split, size and leakage | p. 7 (1 Introduction), p. 7 (1 Introduction), p. 8 (1 Introduction), p. 8 (1 Introduction) |
| Metric | Figure 4: Learned dancing motions in simulation and the real-world. Black bounding boxes indicate the foot contact goals and the hand task goals. Reward. There are two task-related rewards, one encourageing spreading ... | definition, denominator, direction and uncertainty | p. 7 (Figure/Table caption), p. 2 (Figure/Table caption), p. 6 (1 Introduction) |
| Baseline/ablation | Figure 6: We train the dinosaur robot to push the ball towards destinations with different end effec- tors. By altering the destinations, we make the robot generate ball trajectories forming "WoCoCo". 5 ... | fair input/data/compute/action matching | p. 8 (Figure/Table caption), p. 8 (1 Introduction), p. 6 (1 Introduction) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 1 Introduction - extractive body cue:** 6 Limitation and Future Works One limitation of our work is the lacking knowledge of when the controller will fail.
- **p. 8 / 1 Introduction - extractive body cue:** Therefore, we may explore failure predictors [56] and other safety assessment methods in the future [57].
- **p. 7 / 1 Introduction - extractive body cue:** The contact goal requires foot contact with the ground in their corresponding bounding boxes (predefined in the world frame), plus hand self-collision if the move ...
- **p. 5 / 1 Introduction - extractive body cue:** [44] use RL to learn double-foot jumping in the 3D space, yet their method does not support continuous jumps, relies on a motion reference, and ...
- **p. 5 / 1 Introduction - extractive body cue:** 2, demonstrating the humanoid's capability to perform versatile continuous jumping while tracking upper body postures, and robustness against perturbations such as unseen gravels.
- **p. 6 / 1 Introduction - extractive body cue:** It can also recover after stepping on a belt tied to itself, showcasing robustness.
- **p. 6 / 1 Introduction - extractive body cue:** By defining the contact sequence solely on the hands, we leverage RL to achieve robust locomotion while simplifying the whole task.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 8 (1 Introduction), p. 5 (1 Introduction), p. 2 (1 Introduction), p. 4 (1 Introduction), p. 3 (1 Introduction)이다.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (18 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** However, model mismatch and perturbations such as uneven terrains pose significant challenges to these controllers, for which RL can be a promising solution [13, 22]. (p. 5, 1 Introduction).
- **Actual contribution:** In Section 4, we show how our framework, WoCoCo, can be applied to a variety of challenging dynamic tasks with flexible definitions and representations of contact and task goals. (p. 3, 1 Introduction).
- **Evaluation boundary:** Figure 4: Learned dancing motions in simulation and the real-world. Black bounding boxes indicate the foot contact goals and the hand task goals. Reward. There are two task-related rewards, one ... (p. 7, Figure/Table caption).
- **Explicit failure boundary:** 6 Limitation and Future Works One limitation of our work is the lacking knowledge of when the controller will fail. (p. 8, 1 Introduction).
