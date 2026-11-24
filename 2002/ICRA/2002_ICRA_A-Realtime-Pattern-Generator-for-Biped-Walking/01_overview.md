# A Realtime Pattern Generator for Biped Walking

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (7 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://api.crossref.org/works/10.1109/ROBOT.2002.1013335.
> PDF retrieval source: https://www.cs.cmu.edu/~cga/legs/kuff1e.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2002 / ICRA
- Authors: S. Kajita, F. Kanehiro, K. Kaneko, K. Fujiwara, K. Yokoi, H. Hirukawa
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: REFERENCE
- Tags: Robotics, humanoid, bipedal locomotion, 3D linear inverted pendulum, real-time control
- Official paper: https://api.crossref.org/works/10.1109/ROBOT.2002.1013335
- Full-text retrieval: https://www.cs.cmu.edu/~cga/legs/kuff1e.pdf
- Code/Project: not identified
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (7 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 한 줄 요약과 핵심 기여 두 개를 각 문장에 인용한 판본의 원문에서 확인했다.

## Why This Paper Is Here

3차원 선형 역진자 모드는 이족 로봇의 질량중심 운동을 평면에 구속해 실시간으로 보행 패턴을 생성한다. [PDF 1쪽](https://www.cs.cmu.edu/~cga/legs/kuff1e.pdf#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** For realtime walking control of a biped robot, we analyze the dynamics of a three-dimensional inverted pendulum whose motions are constrained onto an arbitrarily defined ...
- **p. 1 / Abstract - extractive body cue:** This analysis leads us a simple linear dynamics, the Three-Dimensional Linear Inverted Pendulum Mode (3D-LIPM).
- **p. 1 / Abstract - extractive body cue:** Geometric nature of trajectories under the 3D-LIPM is discussed, and an algorithm for walking pattern generation is presented.
- **p. 1 / Abstract - extractive body cue:** Experimental results of realtime walking control of a 12 d.o.f. biped robot HRP-2L using an input device such as a game pad are also shown.
- **p. 1 / 1 Introduction - extractive body cue:** Research on humanoid robots and biped locomotion is currently one of the most exciting topics in the field of robotics and there exist many ongoing ...
- **p. 4 / 1 Introduction - extractive body cue:** 3.2 Pattern generation along a local axis Now the problem becomes a control of the motion along X or Y -axis for each step.

## Core Idea

- **p. 1 / 1 Introduction - extractive body cue:** It allows a separate controller design for the sagittal (x-z) and the lateral (y-z) motions and simplifies a walking pattern generation a great deal.
- **p. 1 / 1 Introduction - extractive body cue:** In this paper, we take the standpoint of the second approach, and introduce a new modeling which represents the dynamics of a robot with limited ...
- **p. 2 / 1 Introduction - extractive body cue:** Let (τr, τp, f) be the actuator torque and force associated with the state variables (θr, θp, r).
- **p. 3 / 1 Introduction - extractive body cue:** Therefore, the 3D-LIPM with zero input torque can be considered as a dynamics under the central force field.
- **p. 3 / 1 Introduction - extractive body cue:** Since the 3DLIPM is a dynamics under the central force field, the motion along Y ′ and X′ is also governed by the identical equations ...
- **p. 1 / 1 Introduction - extractive body cue:** Therefore, it mainly relies on the accuracy of the model data [3, 5, 10, 14].
- **p. 2 / 1 Introduction - extractive body cue:** (11) Therefore, we have the same dynamics of Eq.
- **p. 4 / 1 Introduction - extractive body cue:** The initial body state (x(n) i , v(n) i ) and the final body state (x(n) f , v(n) f ) have the relationship given ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Let (τr, τp, f) be the actuator torque and force associated with the state variables (θr, θp, r). | proprioception, reference pose/motion, visual or language command | p. 2 (1 Introduction), p. 3 (1 Introduction) |
| State/latent | Let, actuator, torque, force, associated, state, variables, Therefore, D-LIPM, zero, input, considered | whole-body pose, balance/contact state와 skill/mode | p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction) |
| Output/action | Therefore, the 3D-LIPM with zero input torque can be considered as a dynamics under the central force field. | joint/whole-body action, motion target 또는 task trajectory | p. 3 (1 Introduction), p. 3 (1 Introduction), p. 1 (1 Introduction) |
| Objective/outcome | 2 Derivation of 3D Linear Inverted Pendulum Mode 2.1 Motion equation of a 3D inverted pendulum When a biped robot is supporting its body on one leg, its dominant dynamics can be ... | tracking, balance, skill/task success와 recovery | p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction) |

## Main Claims and Actual Contribution

- 평면 구속 아래 3차원 역진자의 수평 운동이 단순한 선형식이 되는 조건과 궤적의 기하를 유도한다. [PDF 2쪽](https://www.cs.cmu.edu/~cga/legs/kuff1e.pdf#page=2) · [PDF 3쪽](https://www.cs.cmu.edu/~cga/legs/kuff1e.pdf#page=3)
- 사용자의 이동 방향 입력으로 발 디딜 위치와 보행을 갱신하는 과정을 HRP-2L에서 확인한다. [PDF 6쪽](https://www.cs.cmu.edu/~cga/legs/kuff1e.pdf#page=6) · [PDF 7쪽](https://www.cs.cmu.edu/~cga/legs/kuff1e.pdf#page=7)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 6 (4 Experiments), p. 6 (4 Experiments) |
| Embodiment/environment | of realtime bipped walking 4.1 Biped robot HRP-2L The biped robot HRP-2L, which is the leg module for HRP-21, is used for the experiments. | hardware/simulator version and reset protocol | p. 5 (4 Experiments), p. 5 (4 Experiments) |
| Dataset/benchmark | The realtime walk generation was tested on a 12 d.o.f. biped robot HRP-2L with the game pad interface, and a dynamically stable walk was successfully performed. | role, split, size and leakage | p. 5 (4 Experiments), p. 5 (4 Experiments), p. 6 (4 Experiments), p. 6 (4 Experiments) |
| Metric | In order to reduce the error between the desired ZMP trajectory and the actual ZMP, the horizontal position of the torso is adjusted. | definition, denominator, direction and uncertainty | p. 6 (4 Experiments), p. 5 (4 Experiments), p. 6 (4 Experiments) |
| Baseline/ablation | not recovered | fair input/data/compute/action matching | 본문 anchor 없음 |

## Explicit Limitations and Failure Boundary

- **p. 6 / 4 Experiments - extractive body cue:** Although we assume an ideal robot, which can step towards any direction at all time, in the former section, HRP-2L has the limit of joint ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1 Introduction), p. 4 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction)이다.
