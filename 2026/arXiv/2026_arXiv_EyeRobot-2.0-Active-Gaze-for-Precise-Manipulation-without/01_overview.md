# EyeRobot 2.0: Active Gaze for Precise Manipulation without Wrist Cameras

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue
- Authors: Kush Hari, Justin Kerr, Nidhya Shivakumar, Samarth Mahapatra, Carmelo Sferrazza, Jiahui Lei, Jitendra Malik, C. Karen Liu, Ken Goldberg, Angjoo Kanazawa
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: active perception, bimanual manipulation, Reinforcement Learning, Imitation Learning
- Aliases:
- Official paper: https://arxiv.org/abs/2610.03710
- Venue verification: https://arxiv.org/abs/2610.03710
- Code/Project: https://eyerobot2.github.io/
- Code: project_only
- Source audit: 2026-10-22 공식 abstract/arXiv abstract와 publication metadata 확인. 새 5개 note는 abstract 수준의 분석이며 상세 본문·코드 감사는 기존 buildup dossier의 명시 범위만 따른다.

## Problem and Importance

Wrist camera 없이 정밀 manipulation을 위한 gaze를 구성한다.

## Core Idea and Contribution

Stereo fixation 기반 표현과 gaze/행동 제어를 연결한다.

## Observation–State–Action Interface

Stereo 시선·관측 → fixation-relative 표현 → manipulation.

## Evaluation Scope and Claim Boundary

Simulation 및 실제 bimanual manipulation을 보고한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2610.03710) · [저자 project/code](https://eyerobot2.github.io/). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

C1의 시선 조절과 action-relevant 관측에 대한 직접 REFERENCE다.

## Verification Boundary

물리/가상 gaze 경계, stereo calibration, RL/BC supervision, robot 범위을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
