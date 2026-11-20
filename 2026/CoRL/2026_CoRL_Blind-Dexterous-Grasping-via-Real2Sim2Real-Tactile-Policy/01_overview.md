# Blind Dexterous Grasping via Real2Sim2Real Tactile Policy Learning

> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-19 · 서지·초록과 링크한 방법·비교 절을 확인했다. 논문 전체 정독과 실험 재현은 미확인이다.

- Year/Venue: 2026 / CoRL
- Authors: Shengcheng Luo, Xiyan Huang, Zhe Xu, Wanlin Li, Ziyuan Jiao, Chenxi Xiao
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: NEXT
- Tags: dexterous grasping, tactile sensing, real-to-sim
- Official paper: https://arxiv.org/abs/2606.11767
- Code/Project: http://Dex-Blind-Grasp.github.io

## 연구 질문과 기여

시각 없이 촉각으로 파지하도록 시뮬레이터의 접촉 이벤트를 보정하고 RL 전문가를 증류한다.

기하를 아는 시뮬레이션 전문가들의 성공 궤적을 수집한다. 실물에서는 촉각·로봇 상태를 관측하는 확산 정책을 배포한다.

## 평가 범위

촉각을 장착한 실물 LEAP Hand에서 학습에 사용한 물체와 새 물체를 나눠 파지를 평가했다. [원문 및 평가 절](https://arxiv.org/pdf/2606.11767#page=6)

## 선정 근거

시각이 없는 다지 파지에서 촉각 접촉 보정과 RL 전문가 증류를 검토할 기준이다.
