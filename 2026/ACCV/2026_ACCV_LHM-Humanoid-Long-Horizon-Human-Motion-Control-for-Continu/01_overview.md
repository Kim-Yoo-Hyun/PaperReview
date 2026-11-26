# LHM-Humanoid: Long-Horizon Human Motion Control for Continuous Object Transport in Cluttered Scenes

> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-25 · §3.1–3.3, §4.2–4.3, Tables 1 and 3; ACCV 2026 programme 검토. [방법·평가 원문](https://arxiv.org/html/2508.16943)

- Year/Venue: 2026 / ACCV
- Authors: Haozhuo Zhang, Jingkai Sun, Michele Caprio, Angelo Cangelosi, Jian Tang, Shanghang Zhang, Qiang Zhang, Wei Pan
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: REFERENCE
- Tags: VLA, whole-body control, loco-manipulation, policy distillation, simulation
- Official paper: https://openreview.net/forum?id=ZJKDHOC5r7
- Code/Project: https://haozhuo-zhang.github.io/LHM-Humanoid/

## 연구 질문과 기여

첫 물체를 내려놓은 뒤 생긴 불안정한 자세가 다음 물체로의 이동과 집기를 방해한다. 초기화 없이 두 운반 작업을 이어가는 조건을 다룬다.

첫 물체를 놓고 물러나는 교사와 그 상태에서 다음 과업을 시작하는 교사를 RL로 학습해 하나의 정책으로 증류한다. 이 정책의 스텝별 행동을 다시 1인칭 RGB·언어 학생에게 DAgger로 가르친다.

## 정책 출력

시각언어 버전은 현재 배치 목표를 지정하는 언어와 1인칭 RGB에서 모의 휴머노이드의 전신 행동을 출력한다. 연속 지시는 외부에서 주어지며 공개 본문의 해당 절은 모터 전류나 직접 토크 차원을 명시하지 않는다. [방법 원문](https://arxiv.org/html/2508.16943)

## 평가 범위

Isaac Gym의 연속 운반 실험이다. Table 3에서 시각언어 학생의 두 과제 전체 성공률은 63.7%, 가장 높은 비교군은 40.7%다. Table 1의 privileged 정책 수치와 구별한다. [원문 및 평가 절](https://arxiv.org/html/2508.16943)

## 선정 근거

HumanVLA의 단일 재배치에서 다음 운반을 시작할 수 있는 자세까지 연구 단위를 넓힌 비교점이다. 실물 전신 제어나 자율적인 언어 하위 목표 생성을 입증하는 자료로 확대하지 않는다.
