# Insights — Adaptive Compliance Policy: Learning Approximate Compliance for Diffusion Guided Control

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-25 · 저자판 PDF 3–6쪽, §III–IV, Tables I–II 확인. [서지·게재 상태](https://api.crossref.org/works/10.1109/ICRA55743.2025.11128452)

## Paper-supported conclusion

시연에서 기준 위치·힘과 가상 평형점을 구성하고 주 접촉력 방향의 강성을 근사한다. 시각·힘 이력을 조건으로 한 확산 정책이 출력한 목표를 하위 순응 제어기가 추종한다. [원문 및 평가 절](https://arxiv.org/pdf/2410.09309v2#page=4)

## Researcher interpretation

VLA가 목표 강성을 정하는 연구의 비교 기준이다. 같은 시연에서 운동을 모방하는 것과 접촉 방향의 강성을 선택하는 것의 차이를 점검할 수 있다.

- §III에서 Diffusion Policy의 조건부 행동 헤드를 재사용하고 출력에 가변 순응성 표현을 더한다. [pr-0019 · 원문](https://arxiv.org/pdf/2410.09309v2#page=4)

## 최소 비교 실험

동일한 시연과 하위 제어기를 사용해 정책의 목표 궤적을 고정하고 강성만 상수 또는 예측값으로 바꾼다. 물체별 성공률과 최대 접촉력을 함께 비교한다.
