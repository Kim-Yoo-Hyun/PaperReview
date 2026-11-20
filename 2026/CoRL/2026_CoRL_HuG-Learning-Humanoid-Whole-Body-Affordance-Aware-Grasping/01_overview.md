# HuG: Learning Humanoid Whole-Body Affordance-Aware Grasping with Active Perception

> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-19 · 서지·초록과 링크한 방법·비교 절을 확인했다. 논문 전체 정독과 실험 재현은 미확인이다.

- Year/Venue: 2026 / CoRL
- Authors: Xuanbin Peng, Lai Wei, Yuze Zhai, Qingyuan Yu, Keyi Wang, Jianglong Ye, Xiaolong Wang
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: NEXT
- Tags: humanoid, active perception, whole-body grasping
- Official paper: https://arxiv.org/abs/2611.01659
- Code/Project: https://xuanbinpeng.com/hug

## 연구 질문과 기여

휴머노이드가 관측 위치와 파지를 선택할 때 실제 전신 제어기가 유지할 수 있는 자세를 학습한다.

전신 동역학 검사로 기구학적으로 가능한 파지 후보를 다시 선별한다. 선반의 여러 높이에서 실물 파지, 분포 밖 높이에서 시뮬레이션 전이를 구분해 평가한다.

## 평가 범위

다단 선반의 실제 파지와 훈련 범위 밖 높이에 대한 시뮬레이션 결과를 구분한다. [원문 및 평가 절](https://arxiv.org/pdf/2611.01659#page=8)

## 선정 근거

카메라 탐색과 파지 가능성 판단에 전신 균형 제약을 결합한 실기 휴머노이드 기준이다.
