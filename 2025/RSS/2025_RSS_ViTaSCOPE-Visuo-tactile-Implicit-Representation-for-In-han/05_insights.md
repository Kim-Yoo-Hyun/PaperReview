# Insights — ViTaSCOPE: Visuo-tactile Implicit Representation for In-hand Pose and Extrinsic Contact Estimation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-19 · 서지·초록과 링크한 방법·비교 절을 확인했다. 논문 전체 정독과 실험 재현은 미확인이다.

## Paper-supported conclusion

암묵적 형상 표현을 도구 표면과 접촉 위치에 공유한다. 센서의 전단 변형과 부분 관측을 이용해 자세와 외부 접촉을 복원한다. [원문 및 평가 절](https://arxiv.org/pdf/2506.12239#page=7)

## Researcher interpretation

손안 물체의 자세와 물체가 환경에 닿는 위치를 함께 추정하는 접촉 상태 기준이다.

- GelSight 계열 광학 촉각 센서를 실물 그리퍼의 도구 접촉 관측에 사용한다. 실기 설정 및 p.2 관련 연구. 센서 결합 관계다. [pr-0848 · 원문](https://arxiv.org/pdf/2506.12239#page=6)

## 최소 비교 실험

같은 가림 조건에서 자세 오차가 외부 접촉 위치 오차로 얼마나 전달되는지 측정한다.
