# EXPO: Stable Reinforcement Learning with Expressive Policies

> Evidence maturity: `FULL_TEXT_CHECKED` — 지정 절만 확인한 기록이며 전체 정독·실험 재현을 뜻하지 않는다.

- Year/Venue: 2026 / ICLR
- Authors: Perry Dong, Qiyang Li, Dorsa Sadigh, Chelsea Finn
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: Reinforcement Learning, expressive-policy, residual-policy, value-selection
- Aliases: EXPO
- Official paper: https://iclr.cc/virtual/2026/poster/10008723
- Venue verification: https://proceedings.iclr.cc/paper_files/paper/2026/hash/d56a652ad743308b24b6c4d0e6411dd7-Abstract-Conference.html
- Code/Project: https://github.com/pd-perry/EXPO
- Code: https://github.com/pd-perry/EXPO
- Source audit: 2026-11-03 공식 venue/서지 재확인; 기존 GAP-VRL 검토의 지정 본문 §4 / Algorithm 1; expo_learner.py selected update paths를 반영. 선택 절 검토이며 전체 논문 정독·native 실행은 아님. 공개 code를 읽었지만 실행하지 않았다. Co-adaptation 결과를 독립 base release 교체 후 동결 editor의 전이 근거로 확대하지 않는다. 사용자 읽기 상태는 UNREAD 유지. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

EXPO는 모방학습 정책이 제시한 행동을 작은 확률적 정책이 수정하고 두 후보의 가치를 비교해 온라인 강화학습을 수행한다. [PDF 1쪽](https://arxiv.org/pdf/2507.07986v3#page=1)

## Core Idea and Contribution

- 편집 정책을 기본 정책과 별도로 두고 원래 행동과 편집한 행동 중 더 높은 가치를 내는 것을 실행과 가치 학습에 활용한다. [PDF 3쪽](https://arxiv.org/pdf/2507.07986v3#page=3) · [PDF 4쪽](https://arxiv.org/pdf/2507.07986v3#page=4) · [PDF 5쪽](https://arxiv.org/pdf/2507.07986v3#page=5)
- 시연 자료로 초기화한 뒤 환경에서 개선하는 설정에서 여러 행동 분포를 표현하는 정책을 강화학습 기준선과 비교했다. [PDF 6쪽](https://arxiv.org/pdf/2507.07986v3#page=6) · [PDF 7쪽](https://arxiv.org/pdf/2507.07986v3#page=7) · [PDF 8쪽](https://arxiv.org/pdf/2507.07986v3#page=8)

## Observation–State–Action Interface

관측 → base 행동 및 수정 행동 → Q 선택 → 환경. Rollout 선택과 TD target에서의 선택 역할을 함께 확인해야 한다.

## Evaluation Scope and Limitations

공식 proceedings의 online RL 비교와 공개 구현을 확인했다. 현재 registry 노트는 학습 경로에 초점을 두며 개별 점수·독립 재현 결과를 제시하지 않는다.

공개 code를 읽었지만 실행하지 않았다. Co-adaptation 결과를 독립 base release 교체 후 동결 editor의 전이 근거로 확대하지 않는다.

근거: [지정 본문](https://arxiv.org/html/2507.07986v3) — §4 / Algorithm 1; expo_learner.py selected update paths. Code 검토 revision: `bbd571306b413e05d5d4b01a6efa20352c2b891a`; 실행하지 않았다.

## Why This Paper Is Here — Researcher Interpretation

Residual/editor와 value 선택을 결합한 강한 직접 baseline이다. Q 선택·base 모방·editor RL이라는 조합 자체의 신규성 주장을 막는 NEXT다.

## 공개 자료

- 코드 — 행동 후보의 가치 비교와 편집 정책 학습 · expo/agents/sac/expo_learner.py [배포 파일](https://raw.githubusercontent.com/pd-perry/EXPO/bbd571306b413e05d5d4b01a6efa20352c2b891a/expo/agents/sac/expo_learner.py)
- 데이터 — EXPO가 재배포한 MimicGen 조작 자료 · expo_mmgdatasets.zip [배포 파일](https://drive.google.com/file/d/1qemTmLkEkE17dFN6A2BJvVYLJBtLbN67/view)
