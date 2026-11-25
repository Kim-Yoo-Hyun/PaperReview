# Learning Visuotactile Estimation and Control for Non-prehensile Manipulation under Occlusions

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. 아래에 인용한 원문 절·표의 평가 조건을 대조했다.
> Source audit: 2026-11-25 원문 방법·평가 대조.

## 평가 조건

추정기는 말단 자세·힘과 불완전한 물체 자세 관측을 이용한다. 참 상태를 받는 학습용 정책과 추정 상태·불확실성을 받는 실행 정책을 구별한다. [PDF 4쪽](https://raw.githubusercontent.com/mlresearch/v270/d9fe509ba390176a5fd650178a381a0a7b2d4f64/assets/ferrandis25a/ferrandis25a.pdf#page=4)

실물 KUKA iiwa의 손목 카메라로 AprilTag를 추적하고 손목 힘·토크 센서로 접촉을 관측했다. 자연 시야 가림에서는 19/20회, 인위적으로 5초 가린 조건에서는 10/10회, 전체 가림에서는 7/10회 성공했다(§6). [PDF 8쪽](https://raw.githubusercontent.com/mlresearch/v270/d9fe509ba390176a5fd650178a381a0a7b2d4f64/assets/ferrandis25a/ferrandis25a.pdf#page=8)

## Proposed Evaluation — Researcher Interpretation

동일 estimator에서 uncertainty 입력만 제거하고 occlusion 조건별 제어 실패를 비교한다.

이 실험은 실행하지 않았으며, 수치나 결론을 미리 부여하지 않는다.
