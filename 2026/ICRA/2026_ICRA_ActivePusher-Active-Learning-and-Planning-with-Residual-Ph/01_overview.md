# ActivePusher: Active Learning and Planning with Residual Physics for Nonprehensile Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-26 서지와 IEEE 서지와 학회 원문 PDF 3–8쪽의 능동 수집·실물 실험 대조. Full-text scope의 수치·조건만 기록했다.

- Year/Venue: 2026 / ICRA
- Authors: Zhuoyun Zhong, Seyedali Golestaneh, Constantinos Chamzas
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: REFERENCE
- Tags: nonprehensile manipulation, active learning, residual dynamics, contact, Planning
- Official paper: https://ieeexplore.ieee.org/abstract/document/11696785
- Code/Project: https://github.com/elpis-lab/ActivePusher

## 연구 질문과 기여

접촉 물리의 오차가 클 때 밀기 모델의 학습에 어떤 실제 상호작용을 사용해야 할지가 문제다.

공칭 물리 모델의 예측 오차를 잔차로 학습하고, 예측 불확실성을 기준으로 새 상호작용을 고른다. 보정 동역학과 불확실성을 이용해 접촉을 포함한 경로를 계획한다.

## 평가 범위

MuJoCo와 실물 밀기 실험에서 예측, 데이터 획득 전략 및 계획 성공을 비교했다. 물체와 경로는 PDF 6–7쪽에 있다. [원문 및 평가 절](https://events.infovaya.com/uploads/documents/pdfviewer/7c/40/222074-4101.pdf#page=7)

## 선정 근거

밀기에서 동역학 보정과 능동 재수집을 함께 적용하는 비교 기준으로, 로봇팔과 시뮬레이션에서 비교할 수 있다.
