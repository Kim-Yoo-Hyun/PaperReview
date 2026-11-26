# Insights — SPOC: Imitating Shortest Paths in Simulation Enables Effective Navigation and Manipulation in the Real World

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-25 · §4–7, Appendix (zero-shot real-world transfer and Table 9) 검토. [방법·평가 원문](https://arxiv.org/html/2312.02976) · [저자 코드](https://github.com/allenai/spoc-robot-training)

## Paper-supported conclusion

시뮬레이터의 최단 경로와 조작 휴리스틱으로 시연을 생성한다. 두 RGB 카메라와 언어 목표를 인코딩한 뒤 인과적 Transformer가 과거 관측·행동을 보고 다음 이산 행동을 선택한다. [원문 및 평가 절](https://arxiv.org/html/2312.02976)

## Researcher interpretation

π0.5의 연속 베이스·양팔 공동 제어와 비교할 수 있는 이산 행동 선행이다. 같은 행동 어휘로 순서를 선택하는 능력과 여러 축을 동시에 움직이는 능력의 차이가 드러난다.

## 최소 비교 실험

같은 배치에서 정책의 집기 호출률과 호출 뒤 파지 성공률을 따로 집계한다. 베이스와 팔을 한 번에 한 축만 움직이는 제약도 함께 기록한다.

## 검증 질문

실물에서 집기 직전 접근과 마지막 파지를 따로 평가해야 학습된 정책과 집기 휴리스틱의 효과를 귀속할 수 있다.
