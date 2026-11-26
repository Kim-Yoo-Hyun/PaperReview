# Insights — PaCo-VLA: Passivity-Shielded Compliance Prior for Contact-Rich Vision-Language-Action Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-25 · §IV-A–C, §V-A–D, Table I 및 배포 파라미터 검토. [방법·평가 원문](https://arxiv.org/html/2606.00515)

## Paper-supported conclusion

고정된 시각언어행동 백본의 RGB·언어 표현에서 학습한 융합 모듈이 목표 물체, 작업 단계, 복구 단서, 유효성 및 대각 어드미턴스 파라미터를 함께 예측한다. 별도 passivity shield가 파라미터를 투영하고 에너지 탱크와 힘 한계로 현재 적용할 값을 정한다. [원문 및 평가 절](https://arxiv.org/html/2606.00515)

## Researcher interpretation

CompVLA에서 강성으로부터 계산되는 감쇠와 달리 VLA가 감쇠를 직접 제안하는 사례다. 강성·감쇠의 학습, 외부 제어기의 안전 투영, 최종 운동 명령을 따로 측정할 수 있다.

## 최소 비교 실험

저자 설정의 짝지은 닦기 조건에서 정책의 제안 감쇠, 투영 뒤 감쇠, 힘 추종 오차와 복구 횟수를 기록한다. 고정 감쇠를 쓰는 동일한 shield와 비교한다.

## 검증 질문

같은 물체·기하·초기 접촉을 유지한 채 재질 지시만 바꾸면 제안 감쇠와 실제 적용 감쇠가 모두 달라지는가?
