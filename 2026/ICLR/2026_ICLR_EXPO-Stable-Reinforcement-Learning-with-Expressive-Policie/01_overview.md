# EXPO: Stable Reinforcement Learning with Expressive Policies

> Evidence maturity: `FULL_TEXT_CHECKED` — 지정 절만 확인한 기록이며 전체 정독·실험 재현을 뜻하지 않는다.

- Year/Venue: 2026 / ICLR
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: reinforcement-learning, expressive-policy, residual-policy, value-selection
- Aliases: EXPO
- Official paper: https://proceedings.iclr.cc/paper_files/paper/2026/hash/d56a652ad743308b24b6c4d0e6411dd7-Abstract-Conference.html
- Venue verification: https://proceedings.iclr.cc/paper_files/paper/2026/hash/d56a652ad743308b24b6c4d0e6411dd7-Abstract-Conference.html
- Code/Project: https://github.com/pd-perry/EXPO
- Code: https://github.com/pd-perry/EXPO
- Source audit: 2026-11-03 공식 venue/서지 재확인; 기존 GAP-VRL 검토의 지정 본문 §4 / Algorithm 1; expo_learner.py selected update paths를 반영. 선택 절 검토이며 전체 논문 정독·native 실행은 아님. 공개 code를 읽었지만 실행하지 않았다. Co-adaptation 결과를 독립 base release 교체 후 동결 editor의 전이 근거로 확대하지 않는다. 사용자 읽기 상태는 UNREAD 유지.

## Problem and Importance

표현력이 큰 imitation 정책을 online RL로 개선할 때 안정적인 최적화와 탐색을 확보하는 문제다.

## Core Idea and Contribution

Expressive base의 imitation 업데이트와 Gaussian edit 정책의 Q 기반 업데이트를 결합하고, base/edit 행동을 value로 선택한다.

## Observation–State–Action Interface

관측 → base 행동 및 수정 행동 → Q 선택 → 환경. Rollout 선택과 TD target에서의 선택 역할을 함께 확인해야 한다.

## Evaluation Scope and Limitations

공식 proceedings의 online RL 비교와 공개 구현을 확인했다. 현재 registry 노트는 학습 경로에 초점을 두며 개별 점수·독립 재현 결과를 제시하지 않는다.

공개 code를 읽었지만 실행하지 않았다. Co-adaptation 결과를 독립 base release 교체 후 동결 editor의 전이 근거로 확대하지 않는다.

근거: [지정 본문](https://arxiv.org/html/2507.07986v3) — §4 / Algorithm 1; expo_learner.py selected update paths. Code 검토 revision: `bbd571306b413e05d5d4b01a6efa20352c2b891a`; 실행하지 않았다.

## Why This Paper Is Here — Researcher Interpretation

Residual/editor와 value 선택을 결합한 강한 직접 baseline이다. Q 선택·base 모방·editor RL이라는 조합 자체의 신규성 주장을 막는 NEXT다.
