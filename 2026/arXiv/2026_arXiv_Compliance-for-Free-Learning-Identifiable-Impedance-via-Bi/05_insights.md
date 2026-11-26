# Insights — Compliance for Free: Learning Identifiable Impedance via Bilateral Teleoperation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-25 · §III-F/G, §IV, Table II 검토. [방법·평가 원문](https://arxiv.org/html/2609.19976)

## Paper-supported conclusion

양방향 시연의 leader 자세로 의도한 평형점을 따로 기록하고, 관측으로 식별할 수 있는 축·시점에 강성 레이블을 만든다. SmolVLA의 공유 표현 위에서 평형 자세에 flow matching, 로그 강성에 마스킹한 Huber 손실을 쓴다. [원문 및 평가 절](https://arxiv.org/html/2609.19976)

## Researcher interpretation

CompVLA와 출력은 비슷하지만 강성 정답을 어떻게 얻는지가 다르다. 시연의 측정 가능성이 학습한 접촉력 차이로 이어지는지 추적할 수 있다.

- SmolVLA의 시각언어 백본을 고정하고 행동 전문가를 강성 출력에 맞게 학습한다. §III-F. [pr-0915 · 원문](https://arxiv.org/html/2609.19976)

## 최소 비교 실험

같은 닦기 궤적과 힘 추정기에서 출력 강성을 지시 간 교환하고, 지워진 면적과 접촉력 RMS가 어느 지시를 따르는지 측정한다.

## 검증 질문

한 팔·한 닦기 과제에서 나타난 지시별 힘 차이가 다른 표면 또는 다른 추정기의 영점에서도 유지되는지는 확인이 필요하다.
