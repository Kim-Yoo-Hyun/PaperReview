# Method — SPOC: Imitating Shortest Paths in Simulation Enables Effective Navigation and Manipulation in the Real World

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-25 · §4–7, Appendix (zero-shot real-world transfer and Table 9) 검토. [방법·평가 원문](https://arxiv.org/html/2312.02976) · [저자 코드](https://github.com/allenai/spoc-robot-training)

## 관측과 출력

20개 선택지에 베이스 전진·후진·회전, 팔 이동, 그리퍼 회전, 집기·놓기, 하위 과제 완료·종료가 포함된다. 한 스텝에는 한 행동을 택한다. 실물 Stretch의 마지막 집기는 Detic·FastSAM 기반 휴리스틱이 보조한다.

## 학습·실행 방법

시뮬레이터의 최단 경로와 조작 휴리스틱으로 시연을 생성한다. 두 RGB 카메라와 언어 목표를 인코딩한 뒤 인과적 Transformer가 과거 관측·행동을 보고 다음 이산 행동을 선택한다.
