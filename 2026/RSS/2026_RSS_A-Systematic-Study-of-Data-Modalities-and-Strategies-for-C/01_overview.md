# A Systematic Study of Data Modalities and Strategies for Co-training Large Behavior Models for Robot Manipulation

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / RSS
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
- Source audit: 2026-11-02 공식 proceedings/publisher의 서지·abstract와 저자 project/code 소개를 확인했다. 노트는 abstract/project 기반이며 본문 정독·native 실행을 뜻하지 않는다. 사용자 읽기 상태는 UNREAD 유지. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

이 연구는 대규모 조작 정책에서 로봇 행동 이외의 감독 신호를 함께 학습할 때 어떤 데이터가 실제 성능에 기여하는지 비교한다. [PDF 1쪽](https://roboticsproceedings.org/rss22/p007.pdf#page=1)

## Core Idea and Contribution

- 일반 시각언어 자료, 로봇 영상의 세밀한 문장, 다른 로봇의 궤적, 사람 영상, 이산화한 행동을 통제된 공동학습 설정에서 대조했다. [PDF 2쪽](https://roboticsproceedings.org/rss22/p007.pdf#page=2) · [PDF 3쪽](https://roboticsproceedings.org/rss22/p007.pdf#page=3) · [PDF 4쪽](https://roboticsproceedings.org/rss22/p007.pdf#page=4)
- 실물·시뮬레이션 비교에서 시각언어·다른 로봇 자료의 이득을 보고했고, 시험한 설정에서 이산 행동 공동학습의 유의한 이득은 확인하지 못했다. [PDF 6쪽](https://roboticsproceedings.org/rss22/p007.pdf#page=6) · [PDF 7쪽](https://roboticsproceedings.org/rss22/p007.pdf#page=7) · [PDF 8쪽](https://roboticsproceedings.org/rss22/p007.pdf#page=8) · [PDF 9쪽](https://roboticsproceedings.org/rss22/p007.pdf#page=9)

## Observation–State–Action Interface

여러 modality의 supervision → 공통 VLA 학습 → 목표 로봇 조작. Test-time context 교체와 training-data 혼합은 구분한다.

## Evaluation Scope

공식 abstract는 89개 정책을 simulation과 실제 로봇에서 평가했다고 보고한다. 모든 modality가 유익하다는 결론은 아니며 이산 action-token 변형의 이득은 해당 비교에서 유의하지 않았다.

근거: [공식 paper/abstract](https://roboticsproceedings.org/rss22/p007.html) · [저자 project](https://co-training-lbm.github.io/).

## Why This Paper Is Here — Researcher Interpretation

Open X-Embodiment·DataMIL·ReMix 이후 데이터 양과 종류의 효과를 분리하는 NEXT 실증 기준이다. 새로운 아키텍처보다 데이터 구성이라는 단순 대안을 먼저 검토하게 한다.

범위와 수치의 미확인 항목은 [평가 노트](./04_evaluation.md)에, 제안하는 반증 질문은 [insights](./05_insights.md)에 둔다.
