# Method — Adaptive Compliance Policy: Learning Approximate Compliance for Diffusion Guided Control

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-25 · 저자판 PDF 3–6쪽, §III–IV, Tables I–II 확인. [서지·게재 상태](https://api.crossref.org/works/10.1109/ICRA55743.2025.11128452)

## 관측과 출력

RGB, 말단 자세와 힘 이력을 입력받아 참조 행동과 가변 강성을 복원할 표현을 출력한다. 실험에서 순응성은 3차원 병진에 적용한다. 언어 지시는 사용하지 않는다.

## 학습·실행 방법

시연에서 기준 위치·힘과 가상 평형점을 구성하고 주 접촉력 방향의 강성을 근사한다. 시각·힘 이력을 조건으로 한 확산 정책이 출력한 목표를 하위 순응 제어기가 추종한다.

- §III에서 Diffusion Policy의 조건부 행동 헤드를 재사용하고 출력에 가변 순응성 표현을 더한다. [pr-0019 · 원문](https://arxiv.org/pdf/2410.09309v2#page=4)
