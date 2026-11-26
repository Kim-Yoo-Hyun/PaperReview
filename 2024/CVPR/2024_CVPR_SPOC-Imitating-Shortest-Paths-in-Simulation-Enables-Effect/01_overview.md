# SPOC: Imitating Shortest Paths in Simulation Enables Effective Navigation and Manipulation in the Real World

> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-25 · §4–7, Appendix (zero-shot real-world transfer and Table 9) 검토. [방법·평가 원문](https://arxiv.org/html/2312.02976) · [저자 코드](https://github.com/allenai/spoc-robot-training)

- Year/Venue: 2024 / CVPR
- Authors: Kiana Ehsani, Tanmay Gupta, Rose Hendrix, Jordi Salvador, Luca Weihs, Kuo-Hao Zeng, Kunal Pratap Singh, Yejin Kim, Winson Han, Alvaro Herrasti, Ranjay Krishna, Dustin Schwenk, Eli VanderBilt, Aniruddha Kembhavi
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: REFERENCE
- Tags: VLA, mobile manipulation, discrete actions, simulation, sim-to-real
- Official paper: https://openaccess.thecvf.com/content/CVPR2024/html/Ehsani_SPOC_Imitating_Shortest_Paths_in_Simulation_Enables_Effective_Navigation_and_CVPR_2024_paper.html
- Code/Project: https://spoc-robot.github.io/

## 연구 질문과 기여

언어로 지정한 물체를 찾아 집을 때 로봇이 베이스를 움직일지, 팔을 뻗을지, 하위 과제를 끝낼지를 하나의 정책이 선택할 수 있는지 묻는다.

시뮬레이터의 최단 경로와 조작 휴리스틱으로 시연을 생성한다. 두 RGB 카메라와 언어 목표를 인코딩한 뒤 인과적 Transformer가 과거 관측·행동을 보고 다음 이산 행동을 선택한다.

## 정책 출력

20개 선택지에 베이스 전진·후진·회전, 팔 이동, 그리퍼 회전, 집기·놓기, 하위 과제 완료·종료가 포함된다. 한 스텝에는 한 행동을 택한다. 실물 Stretch의 마지막 집기는 Detic·FastSAM 기반 휴리스틱이 보조한다. [방법 원문](https://arxiv.org/html/2312.02976)

## 평가 범위

CHORES의 탐색·집기·가져오기와 실물 Stretch 전이를 평가했다. 실물 Table 9는 물체에 접근해 집기 요청까지 도달한 정책 성공과 실제 집기를 포함한 성공을 따로 보고한다. [원문 및 평가 절](https://arxiv.org/html/2312.02976)

## 선정 근거

π0.5의 연속 베이스·양팔 공동 제어와 비교할 수 있는 이산 행동 선행이다. 같은 행동 어휘로 순서를 선택하는 능력과 여러 축을 동시에 움직이는 능력의 차이가 드러난다.
