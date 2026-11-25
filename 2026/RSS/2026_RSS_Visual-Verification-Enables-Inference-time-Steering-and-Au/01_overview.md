# Visual Verification Enables Inference-time Steering and Autonomous Policy Improvement

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / RSS
- Authors: Mingtong Zhang, Dhruv Shah
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, verification, test-time-compute, self-improvement
- Aliases: VERITAS
- Official paper: https://roboticsproceedings.org/rss22/p079.html
- Venue verification: https://roboticsproceedings.org/rss22/p079.html
- Code/Project: https://veritas-improvement.github.io/
- Code: https://github.com/princeton-prism/veritas
- Source audit: 2026-11-07–08: official metadata/abstract 및 저자 project/repository 공개 범위 확인.  본문 전체 정독·코드 실행·독립 성능 검증 아님. 사용자 reading status UNREAD 유지. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

VERITAS는 범용 정책의 행동 후보를 실행 전 시각 정보로 검증해 행동을 선택하고 그 실행 자료로 정책을 추가 학습한다. [PDF 1쪽](https://roboticsproceedings.org/rss22/p079.pdf#page=1)

## Core Idea and Contribution

- 사전학습 정책이 제안한 여러 행동 묶음을 시각 검증기로 비교해 별도의 정책 갱신 없이 실행할 행동을 선택한다. [PDF 4쪽](https://roboticsproceedings.org/rss22/p079.pdf#page=4) · [PDF 5쪽](https://roboticsproceedings.org/rss22/p079.pdf#page=5)
- 시각 검증을 거쳐 성공한 자율 실행으로 정책을 오프라인 미세조정하고 추가 전문가 시연을 이용한 비교 조건과 성능을 평가했다. [PDF 6쪽](https://roboticsproceedings.org/rss22/p079.pdf#page=6) · [PDF 7쪽](https://roboticsproceedings.org/rss22/p079.pdf#page=7)

## Observation–State–Action Interface

기존 정책의 행동 후보 → gradient-free 시각 검증 → 실행·재학습 데이터.

## Evaluation Scope and Claim Boundary

SIMPLER와 실제 DROID setup에서 steering 및 offline 개선을 평가한다.

근거: [공식 paper/abstract](https://roboticsproceedings.org/rss22/p079.html). 문장에 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

RL 자체의 기여를 주장할 때 반드시 비교할 자율 데이터 선택·모방 대안이다.

## Verification Boundary

verifier 오류와 성공 판정의 독립성, fine-tuning objective, 인간 개입의 집계 범위을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.

## 공개 자료

- 코드 — 행동 후보를 선택하는 시각 검증기 · src/agent/veritas_verifier/veritas_verifier.py [배포 파일](https://raw.githubusercontent.com/princeton-prism/veritas/88962258bf1dd961b894b87ed0527d9bb4197cb8/src/agent/veritas_verifier/veritas_verifier.py)

## 판본과 출처

저자 프로젝트. [공식 페이지](https://veritas-improvement.github.io/)
