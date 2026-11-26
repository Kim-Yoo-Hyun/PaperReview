# AWAC: Accelerating Online Reinforcement Learning with Offline Datasets

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2020 / arXiv
- Authors: Ashvin Nair, Abhishek Gupta, Murtaza Dalal, Sergey Levine
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: offline-to-online, reinforcement-learning, advantage-weighting, manipulation
- Aliases: AWAC
- Official paper: https://arxiv.org/abs/2006.09359
- Venue verification: https://arxiv.org/abs/2006.09359
- Code/Project: https://awacrl.github.io/
- Code: https://github.com/vitchyr/rlkit
- Source audit: 2026-11-12: 공식 publication/초록 또는 저자 source 확인. 저자 project·arXiv v6 확인. OpenReview forum은 browser challenge로 본문 접근 실패했고 공식 acceptance를 확인하지 못해 arXiv 2020으로 등록한다. Project의 code 링크는 식별했으나 해당 경로 직접 fetch는 실패했다. 초록·지정 project 범위이며 전체 정독·코드 실행·사용자 reading 완료를 뜻하지 않는다. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

AWAC는 이미 수집된 최적·비최적 궤적으로 로봇 정책을 초기화하고 새 환경 상호작용을 같은 학습에 더해 성능을 개선한다. [PDF 1쪽](https://arxiv.org/pdf/2006.09359v6#page=1)

## Core Idea and Contribution

- 오프폴리시 비평가가 추정한 어드밴티지로 자료 속 행동의 우도에 가중치를 주어 별도 행동 정책 밀도 모델 없이 행위자를 갱신한다. [PDF 4쪽](https://arxiv.org/pdf/2006.09359v6#page=4) · [PDF 5쪽](https://arxiv.org/pdf/2006.09359v6#page=5)
- 실물 서랍 열기, 밸브 회전, 다지 손 조작에서 기존 자료와 온라인 경험을 함께 썼을 때의 학습 곡선을 비교했다. [PDF 7쪽](https://arxiv.org/pdf/2006.09359v6#page=7) · [PDF 8쪽](https://arxiv.org/pdf/2006.09359v6#page=8)

## Observation–State–Action Interface

Offline transition·online replay → critic → 가중 행동 모방 → 실제 행동 수집.

## Evaluation Scope and Claim Boundary

시뮬레이션과 실제 다지 손·서랍 열기·밸브 조작을 평가한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2006.09359) · [저자 project/code](https://awacrl.github.io/) · [공식 code](https://github.com/vitchyr/rlkit/tree/master/examples/awac). 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

RL 이득이 성공 선택이나 weighted imitation으로 설명되는지 비교할 핵심 baseline이다.

## Verification Boundary

본문에서 확인할 항목: advantage scale·weight clipping·replay 비율·새 데이터 수집 비용. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.

## 공개 자료

- 코드 · AWAC 장점 가중 행위자 및 비평가 학습 · rlkit/torch/sac/awac_trainer.py [배포 파일](https://raw.githubusercontent.com/vitchyr/rlkit/ac45a9db24b89d97369bef302487273bcc3e3d84/rlkit/torch/sac/awac_trainer.py)
