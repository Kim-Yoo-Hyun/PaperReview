# WoCoCo: Learning Whole-Body Humanoid Control with Sequential Contacts

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=Czs2xH9114.
> PDF retrieval source: https://arxiv.org/pdf/2406.06005. Reading tracker status/evidence was not changed.

- Year/Venue: 2024 / CoRL
- Authors: not duplicated here when not verified in the registry source
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: NEXT
- Tags: Robotics, humanoid, whole-body control, sequential contacts, Reinforcement Learning
- Official paper: https://openreview.net/forum?id=Czs2xH9114
- Full-text retrieval: https://arxiv.org/pdf/2406.06005
- Code/Project: https://wococo-humanoid.github.io/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-02 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Locomotion, whole-body, mobile manipulation, and humanoids의 humanoid 문제를 이해하기 위해 읽는다. 본문은 6 Limitation and Future Works One limitation of our work is the lacking knowledge of when the controller will fail.를 문제로 두고, In Section 4, we show how our framework, WoCoCo, can be applied to a variety of challenging dynamic tasks with flexible definitions and representations of contact and task goals.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

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

- **p. 3 / 1 Introduction - extractive body cue:** In Section 4, we show how our framework, WoCoCo, can be applied to a variety of challenging dynamic tasks with flexible definitions and representations of ...
- **p. 5 / 1 Introduction - extractive body cue:** 4 Case Studies In this section, we show how our framework, WoCoCo, can be applied to various challenging tasks with different contact sequences.
- **p. 3 / 1 Introduction - extractive body cue:** In this paper, we study tasks where contact stages are predefined (e.g., heuristically designed), and our method can seamlessly be integrated with high-level contact planners ...
- **p. 2 / 1 Introduction - extractive body cue:** To better facilitate exploration, we propose a task-agnostic curiosity reward term.
- **p. 4 / 1 Introduction - extractive body cue:** Instead, we propose to use count-based curiosity rewards via random neural network (NN) based hash, inspired by Tang et al.
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3: Learned whole-body box loco-manipulation behaviors in the real world. Results. As shown in Fig. 3, the humanoid can efficiently turn, transition seamlessly between ...
- **p. 6 / 1 Introduction - extractive body cue:** By defining the contact sequence solely on the hands, we leverage RL to achieve robust locomotion while simplifying the whole task.
- **p. 8 / 1 Introduction - extractive body cue:** In comparison, our curiosity rewards achieves effective exploration without overfitting specific behaviors.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

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

Locomotion, whole-body, mobile manipulation, and humanoids의 humanoid 문제를 이해하기 위해 읽는다. 본문은 6 Limitation and Future Works One limitation of our work is the lacking knowledge of when the controller will fail.를 문제로 두고, In Section 4, we show how our framework, WoCoCo, can be applied to a variety of challenging dynamic tasks with flexible definitions and representations of contact and task goals.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 8 (1 Introduction), p. 5 (1 Introduction), p. 2 (1 Introduction), p. 4 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
