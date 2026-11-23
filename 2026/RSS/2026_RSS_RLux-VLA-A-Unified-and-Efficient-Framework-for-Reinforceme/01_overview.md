# RLinf-VLA: A Unified and Efficient Framework for Reinforcement Learning of Vision-Language-Action Models

> Evidence maturity: `ABSTRACT_CHECKED`. 개요 전반은 초록 수준이며, 아래 요약과 두 기여에는 확인한 본문 위치를 표시했다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / RSS
- Authors: Hongzhi Zang, Mingjie Wei, Si Xu, Yongji Wu, Zhen Guo, Yuanqing Wang, Hao Lin, Peihong Wang, Hua Yuan, Yixian Zhang, Liangzhi Shi, Yuqing Xie, Zhexuan Xu, Zhihao Liu, Kang Chen, Wenhao Tang, Quanlu Zhang, Weinan Zhang, Chao Yu, Yu Wang
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA-RL, simulator, resource-allocation
- Aliases: RLux-VLA, RLinf-VLA
- Official paper: https://www.roboticsproceedings.org/rss22/p089.html
- Venue verification: https://www.roboticsproceedings.org/rss22/p089.html
- Code/Project: https://github.com/RLinf/RLinf/blob/main/docs/source-zh/rst_source/resources/release_v0.3.rst
- Code: https://github.com/RLinf/RLinf
- Source audit: 2026-11-23 요약과 핵심 기여 두 개를 원문 본문에 대조했다. 나머지 세부 분석은 기존 초록·공식 자료에 근거한다.

2026-11-06: RSS 2026 공식 title을 RLinf-VLA로 정정. arXiv/DOI·paper_id·기존 folder 유지; 이전 RLux-VLA는 검색 alias이며 공식 title로 사용하지 않는다.

## Problem and Importance

RLinf-VLA는 여러 VLA·강화학습 알고리즘·시뮬레이터를 같은 인터페이스로 연결해 정책 성능과 학습 효율을 비교하는 플랫폼이다. [PDF 1쪽](https://www.roboticsproceedings.org/rss22/p089.pdf#page=1)

## Core Idea and Contribution

- 렌더링·추론·학습의 자원 배분을 나누거나 중첩하는 파이프라인을 설계했다. [PDF 3쪽](https://www.roboticsproceedings.org/rss22/p089.pdf#page=3) · [PDF 4쪽](https://www.roboticsproceedings.org/rss22/p089.pdf#page=4)
- LIBERO·ManiSkill·RoboTwin의 성공률을 보고하고 자원 배치에 따른 학습 처리량을 측정했다. [PDF 6쪽](https://www.roboticsproceedings.org/rss22/p089.pdf#page=6) · [PDF 8쪽](https://www.roboticsproceedings.org/rss22/p089.pdf#page=8)

## Observation–State–Action Interface

Simulator observation/reward → VLA rollout → training worker; resource allocation과 policy interface를 분리한다.

## Evaluation Scope and Claim Boundary

RSS abstract는 LIBERO, ManiSkill, RoboTwin simulation에서 training efficiency와 policy 성능을 비교한다.

근거: [공식 paper/abstract](https://www.roboticsproceedings.org/rss22/p089.html) · [저자 project/code](https://github.com/RLinf/RLinf/blob/main/docs/source-zh/rst_source/resources/release_v0.3.rst). 그 밖의 수치, 기준선의 비교 조건, 실패 범위는 별도 대조가 필요하다.

## Why This Paper Is Here — Researcher Interpretation

Current trend / system. 여러 VLA·RL 알고리즘·시뮬레이터를 비교할 공통 interface와 resource allocation을 제공한다. SimpleVLA-RL 및 ConRFT 실험을 설계할 때 algorithm 효과와 시스템 throughput을 분리하는 데 유용하다. 공식 RSS title은 RLinf-VLA다.

## Verification Boundary

Model별 action interface, GPU utilization 산정, asynchronous policy lag을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
