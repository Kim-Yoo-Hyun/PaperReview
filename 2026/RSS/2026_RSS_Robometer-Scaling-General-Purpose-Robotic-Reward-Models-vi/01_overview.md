# Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue
- Authors: Anthony Liang, Yigit Korkmaz, Jiahui Zhang, Minyoung Hwang, Abrar Anwar, Sidhant Kaushik, Aditya Shah, Alex S. Huang, Luke Zettlemoyer, Dieter Fox, Yu Xiang, Anqi Li, Andreea Bobu, Abhishek Gupta, Stephen Tu, Erdem Biyik, Jesse Zhang
- Category: World Models, Safety, and Recovery
- Primary track: World models, safety, uncertainty, and recovery
- Tier: NEXT
- Tags: reward-learning, robot-learning, evaluation
- Aliases:
- Official paper: https://www.roboticsproceedings.org/rss22/p140.html
- Venue verification: https://www.roboticsproceedings.org/rss22/p140.html
- Code/Project: https://robometer.github.io/
- Code: https://github.com/robometer/robometer
- Source audit: 2026-10-22 공식 abstract/arXiv abstract와 publication metadata 확인. 새 5개 note는 abstract 수준의 분석이며 상세 본문·코드 감사는 기존 buildup dossier의 명시 범위만 따른다.

## Problem and Importance

성공·실패를 포함한 이질적 robot trajectory에서 범용 reward를 학습한다.

## Core Idea and Contribution

Progress supervision과 trajectory comparison을 결합한다.

## Observation–State–Action Interface

영상 trajectory·비교 정보 → progress/reward.

## Evaluation Scope and Claim Boundary

대규모 multi-robot 자료와 downstream 실제 robot RL을 보고한다.

근거: [공식 paper/abstract](https://www.roboticsproceedings.org/rss22/p140.html) · [저자 project/code](https://robometer.github.io/). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

C4/C6의 reward·progress·평가 신호를 비교할 핵심 최신 baseline이다.

## Verification Boundary

policy version chronology, failure labels, reward training 중복, calibration을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
