# TACTIC: Tactile and Vision Conditioned Contact-Centric Control for Whole-Arm Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-26 서지와 RSS 게재본 PDF 3–9쪽의 모델·MPC 및 실험 대조. Full-text scope의 수치·조건만 기록했다.

- Year/Venue: 2026 / RSS
- Authors: Rishabh Madan, Angchen Xie, Samantha Saak, Andres Blanco, Dohyeok Lee, Sarah Grace Brown, Yunting Yan, Mark Zolotas, Jose Barreiros, Tapomayukh Bhattacharjee
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: REFERENCE
- Tags: whole-arm manipulation, tactile sensing, RGB-D, model predictive control, force control
- Official paper: https://roboticsproceedings.org/rss22/p060.html
- Code/Project: https://emprise.cs.cornell.edu/tactic/

## 연구 질문과 기여

팔 여러 링크의 접촉이 생기고 끊기면 말단의 자세만으로 각 접촉력을 예측하기 어렵다.

행동 조건부 잠재 동역학에 접촉 Jacobian을 결합한다. 표본 기반 MPC는 접촉력을 바꿀 수 있는 방향으로 행동을 샘플링하고 목표 진행과 힘 조절을 함께 평가한다.

## 평가 범위

모의 실험에서 모델 기반·모델 자유 기준과 예측기 변형을 비교하고, 실물 Kinova Gen3에서는 다중 접촉이 포함된 보조 팔 움직임을 평가했다. [원문 및 평가 절](https://roboticsproceedings.org/rss22/p060.pdf#page=8)

## 선정 근거

말단 센서가 놓치는 팔 링크 접촉을 제어에 사용하는 직접 비교 기준이다.
