# PaCo-VLA: Passivity-Shielded Compliance Prior for Contact-Rich Vision-Language-Action Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-25 · §IV-A–C, §V-A–D, Table I 및 배포 파라미터 검토. [방법·평가 원문](https://arxiv.org/html/2606.00515)

- Year/Venue: 2026 / arXiv
- Authors: Haofan Cao, Zhaoyang Li, Zhichao You
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: REFERENCE
- Tags: VLA, admittance control, passivity, variable compliance, contact-rich manipulation
- Official paper: https://arxiv.org/abs/2606.00515
- Code/Project: not identified

## 연구 질문과 기여

접촉 중 지시가 바뀌거나 관측이 오래되었을 때 질량·감쇠·강성의 급격한 변화는 에너지를 주입할 수 있다. 어느 물체를 어떤 단계에서 다룰지와 현재 접촉에서 적용 가능한 순응성을 함께 다뤄야 한다.

고정된 시각언어행동 백본의 RGB·언어 표현에서 학습한 융합 모듈이 목표 물체, 작업 단계, 복구 단서, 유효성 및 대각 어드미턴스 파라미터를 함께 예측한다. 별도 passivity shield가 파라미터를 투영하고 에너지 탱크와 힘 한계로 현재 적용할 값을 정한다.

## 정책 출력

모델은 각 축의 가상 질량·감쇠·강성 (M̂, D̂, K̂)을 별도의 값으로 제안한다. 단계 선택은 공용 운동 primitive를 정한다. 배포 설정에서 정책 제안 50 Hz, 순응 제어·안전 투영 250 Hz다. 배포되는 최종 파라미터와 모터 명령에는 이 투영·제어가 개입한다. [방법 원문](https://arxiv.org/html/2606.00515)

## 평가 범위

시뮬레이션의 커넥터·닦기와 실물 AUBO-i5의 접촉 작업을 평가했다. Table I의 합성 시험은 조건당 1,000개 파라미터 제안이며 수동성 여유 위반은 전체 투영에서 0%, 해당 투영을 제거하면 50.5%였다. 이는 실물 성공률과 구별되는 검증이다. [원문 및 평가 절](https://arxiv.org/html/2606.00515)

## 선정 근거

CompVLA에서 강성으로부터 계산되는 감쇠와 달리 VLA가 감쇠를 직접 제안하는 사례다. 강성·감쇠의 학습, 외부 제어기의 안전 투영, 최종 운동 명령을 따로 측정할 수 있다.
