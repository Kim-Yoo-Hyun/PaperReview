# Problem — SPOC: Imitating Shortest Paths in Simulation Enables Effective Navigation and Manipulation in the Real World

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-25 · §4–7, Appendix (zero-shot real-world transfer and Table 9) 검토. [방법·평가 원문](https://arxiv.org/html/2312.02976) · [저자 코드](https://github.com/allenai/spoc-robot-training)

## 문제와 검증 범위

언어로 지정한 물체를 찾아 집을 때 로봇이 베이스를 움직일지, 팔을 뻗을지, 하위 과제를 끝낼지를 하나의 정책이 선택할 수 있는지 묻는다.

CHORES의 탐색·집기·가져오기와 실물 Stretch 전이를 평가했다. 실물 Table 9는 물체에 접근해 집기 요청까지 도달한 정책 성공과 실제 집기를 포함한 성공을 따로 보고한다. [원문 및 평가 절](https://arxiv.org/html/2312.02976)
