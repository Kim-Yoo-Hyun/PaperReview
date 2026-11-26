# HumanVLA: Towards Vision-Language Directed Object Rearrangement by Physical Humanoid

> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-25 · §3–4, Appendix A–B (state/action spaces and distillation) 검토. [방법·평가 원문](https://arxiv.org/html/2406.19972)

- Year/Venue: 2024 / NeurIPS
- Authors: Xinyu Xu, Yizheng Zhang, Yong-Lu Li, Lei Han, Cewu Lu
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: REFERENCE
- Tags: VLA, whole-body control, object rearrangement, policy distillation, simulation
- Official paper: https://proceedings.neurips.cc/paper_files/paper/2024/hash/215aeb07b5996c969c0123c3c6ee8f54-Abstract-Conference.html
- Code/Project: https://github.com/AllenXuuu/HumanVLA

## 연구 질문과 기여

물체 위치·목표·내비게이션 waypoint를 아는 시뮬레이터 교사의 전신 행동을, 1인칭 영상과 언어를 받는 정책으로 옮길 수 있는지 묻는다.

목표 조건 RL과 adversarial motion prior로 상태 기반 교사를 학습한다. DAgger로 교사 행동을 모방하고, 훈련용 active rendering으로 물체를 바라보는 시선을 가르친다.

## 정책 출력

학생은 1인칭 시각·언어와 로봇 고유수용 상태로 전신 28개 관절의 PD 목표를 30 Hz로 낸다. 관절 PD가 torque를 계산하고 교사의 waypoint·물체 정답은 배포 경로에서 빠진다. [방법 원문](https://arxiv.org/html/2406.19972)

## 평가 범위

Isaac Gym에서 15개 강체로 구성한 휴머노이드가 물체로 걸어가 운반하고 재배치하는 과제를 평가했다. 본문은 배치 성공 및 거리 오차를 보고한다. 실물 휴머노이드 전이는 여기서 평가하지 않았다. [원문 및 평가 절](https://arxiv.org/html/2406.19972)

## 선정 근거

기존 WholeBodyVLA와 달리 보행 명령을 받아 균형을 잡는 별도 RL 정책이 배포 경로에 없다. 전신 관절 인터페이스에 대한 시뮬레이션 근거를 제공한다.
