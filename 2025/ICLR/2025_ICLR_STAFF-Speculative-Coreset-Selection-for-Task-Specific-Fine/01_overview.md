# STAFF: Speculative Coreset Selection for Task-Specific Fine-tuning

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue
- Authors: Xiaoyu Zhang, Juan Zhai, Shiqing Ma, Chao Shen, Tianlin Li, Weipeng Jiang, Yang Liu
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: REFERENCE
- Tags: Robotics, evaluation, data-selection
- Aliases:
- Official paper: https://proceedings.iclr.cc/paper_files/paper/2025/hash/412360d2dd428c26f34918c8d682cf7e-Abstract-Conference.html
- Venue verification: https://proceedings.iclr.cc/paper_files/paper/2025/hash/412360d2dd428c26f34918c8d682cf7e-Abstract-Conference.html
- Code/Project: not identified
- Code: not_identified
- Source audit: 2026-10-25 공식 abstract와 publication metadata 및 명시된 project/code 공개 링크 확인. 본문 정독·코드 실행·payload 검증은 이번 등록 범위 밖이다.

## Problem and Importance

큰 target model에서 coreset 점수를 직접 계산하는 비용이 크다.

## Core Idea and Contribution

동일 family의 작은 model로 점수를 추정하고 target에서 확인해 선택 예산과 coverage를 조정한다.

## Observation–State–Action Interface

LLM 학습 예제 → proxy score·target verification → coreset; robot action interface는 아니다.

## Evaluation Scope and Claim Boundary

LLM fine-tuning 평가이며 VLA의 closed-loop 성공을 검증한 논문은 아니다.

근거: [공식 paper/abstract](https://proceedings.iclr.cc/paper_files/paper/2025/hash/412360d2dd428c26f34918c8d682cf7e-Abstract-Conference.html). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

Proxy scoring과 target 확인 자체를 새 VLA 기여로 재주장하지 않게 하는 GAP-N1의 직접 선행이다.

## Verification Boundary

LLM에서 VLA로의 적용 한계, target verification 비용을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
