# Safe Whole-Body Loco-Manipulation via Combined Model and Learning-based Control

> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-26 서지와 ICRA 서지와 MERL 저자 게재본 PDF 4–9쪽의 제어기·실물 평가 대조. Full-text scope의 수치·조건만 기록했다.

- Year/Venue: 2026 / ICRA
- Authors: Alexander Schperberg, Yeping Wang, Stefano Di Cairano
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: REFERENCE
- Tags: force control, admittance control, whole-body control, Reinforcement Learning, reference governor
- Official paper: https://www.merl.com/publications/TR2026-072
- Code/Project: not identified

## 연구 질문과 기여

걷는 중 말단에 힘이 걸리면 다리 속도 추종과 팔의 순응을 같이 조절해야 한다.

손목의 힘·토크를 어드미턴스로 말단 속도에 매핑하고 다리 RL과 팔 제어에 배분한다. Reference Governor가 기준 속도를 허용 범위로 조정한다.

## 평가 범위

6자유도 팔을 단 Unitree Go2의 시뮬레이션과 실물에서 힘 추종과 상호작용을 검증했다. [원문 및 평가 절](https://www.merl.com/publications/docs/TR2026-072.pdf#page=8)

## 선정 근거

G1의 전신 제어 실험에서 학습형 새 방법의 이득을 보기 전에 사용할 힘 반응과 제약 기준이다.
