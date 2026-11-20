# KineDex: Learning Tactile-Informed Visuomotor Policies via Kinesthetic Teaching for Dexterous Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-19 · 서지·초록과 링크한 방법·비교 절을 확인했다. 논문 전체 정독과 실험 재현은 미확인이다.

- Year/Venue: 2025 / CoRL
- Authors: Di Zhang, Chengbo Yuan, Chuan Wen, Hai Zhang, Junqiao Zhao, Yang Gao
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: NEXT
- Tags: kinesthetic teaching, tactile sensing, dexterous manipulation
- Official paper: https://proceedings.mlr.press/v305/zhang25l.html
- Code/Project: https://dinomini00.github.io/KineDex/

## 연구 질문과 기여

촉각을 장착한 로봇 손에 직접 동작을 가르쳐 목표 자세와 힘을 함께 학습한다.

직접 교시 중 시각·촉각·접촉력에 대응하는 행동을 수집한다. 확산 정책이 자세와 힘 명령을 예측해 접촉 조작을 실행한다.

## 평가 범위

실물 손의 접촉 조작에서 힘 제어·촉각 관측 등 구성요소를 제거해 비교했다. [원문 및 평가 절](https://raw.githubusercontent.com/mlresearch/v305/main/assets/zhang25l/zhang25l.pdf#page=6)

## 선정 근거

접촉력 시연을 수집하고 힘을 제어하는 정책까지 연결하는 촉각 모방학습의 기준이다.
