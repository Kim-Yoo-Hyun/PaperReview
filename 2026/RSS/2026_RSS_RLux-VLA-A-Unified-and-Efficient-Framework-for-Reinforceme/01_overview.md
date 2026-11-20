# RLinf-VLA: A Unified and Efficient Framework for Reinforcement Learning of Vision-Language-Action Models

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue
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
- Source audit: 2026-10-19: 공식 paper abstract 및 저자 project/code README 확인; abstract 기반 — 본문 수동 확인 필요.

2026-11-06: RSS 2026 공식 title을 RLinf-VLA로 정정. arXiv/DOI·paper_id·기존 folder 유지; 이전 RLux-VLA는 검색 alias이며 공식 title로 사용하지 않는다.

## Problem and Importance

VLA RL 구현이 model·algorithm·simulator마다 분리되어 공정한 비교와 효율적인 scaling이 어려운 문제다.

## Core Idea and Contribution

VLA/RL/simulator 공통 interface와 rendering·inference·training 자원 할당 구조를 제공한다.

## Observation–State–Action Interface

Simulator observation/reward → VLA rollout → training worker; resource allocation과 policy interface를 분리한다.

## Evaluation Scope and Claim Boundary

RSS abstract는 LIBERO, ManiSkill, RoboTwin simulation에서 training efficiency와 policy 성능을 비교한다.

근거: [공식 paper/abstract](https://www.roboticsproceedings.org/rss22/p089.html) · [저자 project/code](https://github.com/RLinf/RLinf/blob/main/docs/source-zh/rst_source/resources/release_v0.3.rst). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

Current trend / system. 여러 VLA·RL 알고리즘·시뮬레이터를 비교할 공통 interface와 resource allocation을 제공한다. SimpleVLA-RL 및 ConRFT 실험을 설계할 때 algorithm 효과와 시스템 throughput을 분리하는 데 유용하다. 공식 RSS title은 RLinf-VLA다.

## Verification Boundary

Model별 action interface, GPU utilization 산정, asynchronous policy lag을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
