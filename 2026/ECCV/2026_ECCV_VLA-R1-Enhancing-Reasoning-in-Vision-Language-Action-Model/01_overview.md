# VLA-R1: Enhancing Reasoning in Vision-Language-Action Models

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / ECCV
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: RLVR, GRPO, affordance, trajectory-reasoning
- Aliases: VLA-R1, VLA-CoT-13K
- Official paper: https://arxiv.org/abs/2510.01623
- Venue verification: https://eccv.ecva.net/Conferences/2026/AcceptedPapers
- Code/Project: https://gigaai-research.github.io/VLA-R1/
- Code: https://github.com/GigaAI-research/VLA-R1
- Source audit: 2026-11-07–08: official metadata/abstract 및 저자 project/repository 공개 범위 확인. Region/trajectory 출력 뒤 downstream control을 쓰므로 직접 motor-action RL과 동일시하지 않는다. 본문 전체 정독·코드 실행·독립 성능 검증 아님. 사용자 reading status UNREAD 유지.

## Problem and Importance

Action 생성만 감독하면 affordance·기하 관계를 고려하는 명시적 추론이 약할 수 있다.

## Core Idea and Contribution

CoT 데이터와 region alignment·trajectory consistency·format reward를 사용한 GRPO 후학습을 결합한다.

## Observation–State–Action Interface

시각·지시 → affordance region·trajectory와 reasoning → downstream robot control. 직접 joint action 최적화와 구분한다.

## Evaluation Scope and Claim Boundary

In/out-of-domain, simulation과 실로봇 평가를 보고한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2510.01623) · [저자 project/code](https://gigaai-research.github.io/VLA-R1/) · [공식 code](https://github.com/GigaAI-research/VLA-R1). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

VLA의 RL이 환경 return이 아닌 검증 가능한 중간 출력 보상일 때의 직접 비교 기준이다.

## Verification Boundary

annotation 접근, downstream controller의 역할, execution feedback 사용 범위을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
