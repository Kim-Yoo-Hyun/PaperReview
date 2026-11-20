# ActiveMimic: Egocentric Video Pretraining with Active Perception

> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-19 · 서지·초록과 링크한 방법·비교 절을 확인했다. 논문 전체 정독과 실험 재현은 미확인이다.

- Year/Venue: 2026 / CoRL
- Authors: Xingyao Lin, Guojin Zhong, Tianyi Lu, Ziyi Ye, Yichen Zhu, Zuxuan Wu, Yu-Gang Jiang
- Primary track: Robotics-enabling 3D perception
- Tier: NEXT
- Tags: active perception, egocentric video, Imitation Learning
- Official paper: https://arxiv.org/abs/2606.06194
- Code/Project: https://activemimic.github.io/

## 연구 질문과 기여

사람의 1인칭 영상에서 카메라와 손목 궤적을 복원해 관측과 조작을 함께 사전학습한다.

움직이는 카메라의 궤적을 배울 행동으로 취급한다. 로봇에 적응한 후 능동 관측이 필요한 실제 조작 과제에서 비교한다.

## 평가 범위

실물 능동 조작에서 사람 영상과 로봇 시연을 사용하는 사전학습 기준선을 비교했다. [원문 및 평가 절](https://arxiv.org/pdf/2606.06194#page=7)

## 선정 근거

사람의 머리 움직임을 관측 행동으로 학습하고 실제 로봇으로 전이하는 직접 선행이다.
