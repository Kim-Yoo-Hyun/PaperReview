# Relative Entropy Policy Search

> Evidence maturity: `FULL_TEXT_CHECKED`. 요약과 기여를 아래 쪽수에서 확인했다.

- Year/Venue: 2010 / AAAI
- Authors: Jan Peters, Katharina Mülling, Yasemin Altün
- 저자 판본: 학회 서지에는 Katharina Mulling, Yasemin Altun로 실려 있다. [PDF 1쪽](https://cdn.aaai.org/ojs/7727/7727-13-11257-1-2-20201228.pdf#page=1) · [학회 서지](https://ojs.aaai.org/index.php/AAAI/article/view/7727)
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: REFERENCE
- Tags: reinforcement-learning, policy-search, KL-divergence, information-constraint
- Aliases: REPS
- Official paper: https://ojs.aaai.org/index.php/AAAI/article/view/7727
- Venue verification: https://ojs.aaai.org/index.php/AAAI/article/view/7727
- Code/Project:
- Code: not_identified
- Full-text retrieval: https://cdn.aaai.org/ojs/7727/7727-13-11257-1-2-20201228.pdf
- Source audit: 2026-11-24에 요약과 핵심 기여 두 개를 원문과 대조했다.

## Problem and Importance

REPS는 정책을 개선할 때 새 상태·행동 분포가 표본 분포에서 벗어나는 정도를 상대 엔트로피로 제한한다. [PDF 1쪽](https://cdn.aaai.org/ojs/7727/7727-13-11257-1-2-20201228.pdf#page=1) · [PDF 2쪽](https://cdn.aaai.org/ojs/7727/7727-13-11257-1-2-20201228.pdf#page=2)

## Core Idea and Contribution

- 기대 보상 개선에 분포 보존 제약을 둔 최적화 문제에서 쌍대 문제와 표본 가중치를 유도해 정책을 갱신한다. [PDF 2쪽](https://cdn.aaai.org/ojs/7727/7727-13-11257-1-2-20201228.pdf#page=2) · [PDF 3쪽](https://cdn.aaai.org/ojs/7727/7727-13-11257-1-2-20201228.pdf#page=3)
- 소규모 제어 예제와 시뮬레이션 로봇 탁구에서 상태에 따라 타구 동작 프리미티브를 선택하는 정책을 평가했다. [PDF 4쪽](https://cdn.aaai.org/ojs/7727/7727-13-11257-1-2-20201228.pdf#page=4) · [PDF 5쪽](https://cdn.aaai.org/ojs/7727/7727-13-11257-1-2-20201228.pdf#page=5) · [PDF 6쪽](https://cdn.aaai.org/ojs/7727/7727-13-11257-1-2-20201228.pdf#page=6)

## Observation–State–Action Interface

정책 분포·return → 정보 제약 최적화 → 새 정책 분포.

## Evaluation Scope and Claim Boundary

소규모 MDP, Mountain Car와 모의 로봇 탁구에서 평가했다. 탁구 실험에서는 타구 성공 보상으로 동작 프리미티브를 선택했다.

근거: [공식 paper/abstract](https://ojs.aaai.org/index.php/AAAI/article/view/7727).

## 검색 태그 근거

새 상태·행동 분포가 표본을 수집한 분포에서 벗어나는 정도를 상대 엔트로피로 제한한다. Mountain Car와 모의 로봇 탁구에서 시험했으며, 탁구에서는 상태에 따라 타구 프리미티브를 선택했다. [원문 2쪽](https://cdn.aaai.org/ojs/7727/7727-13-11257-1-2-20201228.pdf#page=2) · [원문 5쪽](https://cdn.aaai.org/ojs/7727/7727-13-11257-1-2-20201228.pdf#page=5)

## Why This Paper Is Here — Researcher Interpretation

TRPO·MPO·KL 제약의 개념 계보를 보완할 원전이며 현재 공통 정독은 GAE/PPO를 우선한다.

## Verification Boundary

본문에서 확인할 항목: KL 방향·분포 제약·sample 추정·실제 행동 변화. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
