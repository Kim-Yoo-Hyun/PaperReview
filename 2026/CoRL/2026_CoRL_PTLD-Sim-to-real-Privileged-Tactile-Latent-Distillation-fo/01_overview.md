# PTLD: Sim-to-real Privileged Tactile Latent Distillation for Dexterous Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-19 · 서지·초록과 링크한 방법·비교 절을 확인했다. 논문 전체 정독과 실험 재현은 미확인이다.

- Year/Venue: 2026 / CoRL
- Authors: Rosy Chen, Mustafa Mukadam, Michael Kaess, Tingfan Wu, Francois R Hogan, Jitendra Malik, Akash Sharma
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: NEXT
- Tags: sim-to-real, tactile sensing, policy distillation
- Official paper: https://arxiv.org/abs/2603.04531
- Code/Project: https://akashsharma02.github.io/ptld-website/

## 연구 질문과 기여

실제 로봇에서만 얻을 수 있는 특권 센서 신호로 촉각 상태 추정기를 증류한다.

보조 관측이 가능한 교사와 촉각 학생의 학습·배포 입력을 분리한다. 시뮬레이션에서 학습한 손안 조작 정책을 실제 회전과 목표 자세 재정렬에서 시험한다.

## 평가 범위

실제 손안 회전·자세 재정렬에서 고유수용감각만 사용하는 정책과 비교했다. [원문 및 평가 절](https://arxiv.org/pdf/2603.04531#page=6)

## 선정 근거

실물의 특권 관측을 학습 때만 사용해 촉각 상태 추정기를 증류하는 전이 기준이다.
