# Method — PaCo-VLA: Passivity-Shielded Compliance Prior for Contact-Rich Vision-Language-Action Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-25 · §IV-A–C, §V-A–D, Table I 및 배포 파라미터 검토. [방법·평가 원문](https://arxiv.org/html/2606.00515)

## 관측과 출력

모델은 각 축의 가상 질량·감쇠·강성 (M̂, D̂, K̂)을 별도의 값으로 제안한다. 단계 선택은 공용 운동 primitive를 정한다. 배포 설정에서 정책 제안 50 Hz, 순응 제어·안전 투영 250 Hz다. 배포되는 최종 파라미터와 모터 명령에는 이 투영·제어가 개입한다.

## 학습·실행 방법

고정된 시각언어행동 백본의 RGB·언어 표현에서 학습한 융합 모듈이 목표 물체, 작업 단계, 복구 단서, 유효성 및 대각 어드미턴스 파라미터를 함께 예측한다. 별도 passivity shield가 파라미터를 투영하고 에너지 탱크와 힘 한계로 현재 적용할 값을 정한다.
