# TactileStep: Sole Tactile Learning for Regulating Foot–Terrain Interaction in Humanoid Locomotion

> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-26 서지와 CoRL 공식 채택·Spotlight S7과 저자판 PDF 3–9쪽의 학습·실물 표 3 대조. Full-text scope의 수치·조건만 기록했다.

- Year/Venue: 2026 / CoRL
- Authors: Zizhuo Wang, Ming-Ju Lee, Shaoting Zhu, Haozhe Lou, Hang Zhao, Yiming Li
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: REFERENCE
- Tags: humanoid, locomotion, tactile sensing, sim-to-real, Reinforcement Learning
- Official paper: https://arxiv.org/abs/2609.28959
- Code/Project: https://tactilestep.github.io/

## 연구 질문과 기여

과제 성공률로는 착지 충격과 불안정한 발 지지를 비교하기 어렵다.

발 접촉을 압력 배열로 바꾸는 모의 센서를 구성하고 실물 깔창과 같은 접촉 특징을 정책이 읽게 한다. 접지 위상별 보상은 착지 충격과 지지 상태를 따로 조절한다.

## 평가 범위

시뮬레이션과 Unitree G1에서 착지력, 충격 소음, 접촉 면적, 이동 성능을 평가했다. 실물 결과는 표 3에 있다. [원문 및 평가 절](https://arxiv.org/pdf/2609.28959#page=9)

## 선정 근거

G1 실험에 발 접촉 품질과 균형 회복을 별도 지표로 넣는 근거다.
