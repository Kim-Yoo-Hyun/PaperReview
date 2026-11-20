# A Systematic Study of Data Modalities and Strategies for Co-training Large Behavior Models for Robot Manipulation

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue
- Authors: Fanqi Lin, Kushal Arora, Jean Mercat, Haruki Nishimura, Paarth Shah, Chen Xu, Mengchao Zhang, Mark Zolotas, Maya Angeles, Owen Pfannenstiehl, Andrew Beaulieu, Jose Barreiros
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: VLA, co-training, robot-data, generalization
- Aliases:
- Official paper: https://roboticsproceedings.org/rss22/p007.html
- Venue verification: https://roboticsproceedings.org/rss22/p007.html
- Code/Project: https://co-training-lbm.github.io/
- Code: project_only
- Source audit: 2026-11-02 공식 proceedings/publisher의 서지·abstract와 저자 project/code 소개를 확인했다. 노트는 abstract/project 기반이며 본문 정독·native 실행을 뜻하지 않는다. 사용자 읽기 상태는 UNREAD 유지.

## Problem and Importance

이종 데이터의 종류와 섞는 학습 단계가 로봇 일반화에 어떤 차이를 만드는지 체계적으로 검토한다.

## Core Idea and Contribution

vision-language 자료·robot 언어 annotation·다른 embodiment 데이터·human video·이산 action token을 여러 co-training 전략으로 비교한다.

## Observation–State–Action Interface

여러 modality의 supervision → 공통 VLA 학습 → 목표 로봇 조작. Test-time context 교체와 training-data 혼합은 구분한다.

## Evaluation Scope

공식 abstract는 89개 정책을 simulation과 실제 로봇에서 평가했다고 보고한다. 모든 modality가 유익하다는 결론은 아니며 이산 action-token 변형의 이득은 해당 비교에서 유의하지 않았다.

근거: [공식 paper/abstract](https://roboticsproceedings.org/rss22/p007.html) · [저자 project](https://co-training-lbm.github.io/).

## Why This Paper Is Here — Researcher Interpretation

Open X-Embodiment·DataMIL·ReMix 이후 데이터 양과 종류의 효과를 분리하는 NEXT 실증 기준이다. 새로운 아키텍처보다 데이터 구성이라는 단순 대안을 먼저 검토하게 한다.

범위와 수치의 미확인 항목은 [평가 노트](./04_evaluation.md)에, 제안하는 반증 질문은 [insights](./05_insights.md)에 둔다.
