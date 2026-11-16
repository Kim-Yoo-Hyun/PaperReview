# ContactBench 1.0: A Benchmark for Everyday Contact-Rich Robotic Manipulation

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / arXiv
- Category: Manipulation, Contact, and Dexterity
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: NEXT
- Tags: Benchmark, tactile, contact, robot-data
- Aliases: ContactBench 1.0
- Official paper: https://arxiv.org/abs/2610.24512
- Venue verification: https://arxiv.org/abs/2610.24512
- Code/Project: https://jingyi-xiang.github.io/contactbench/
- Code: https://github.com/Michaelwyx/contactbench-sim
- Source audit: 2026-11-09: official abstract/project 및 metadata 확인. v2 abstract/project·simulation repository 공개 확인. Asset 공개를 완성된 RL environment 또는 학습 성공 증거로 간주하지 않는다. 새 5-note는 abstract 기반이며 전체 본문/실행/사용자 정독을 뜻하지 않는다.

## Problem and Importance

접촉 기술의 다양성과 실험실 간 재현 가능한 평가가 부족하다.

## Core Idea and Contribution

접촉 skill taxonomy와 제작 가능한 물체·대응 simulation asset을 제공한다.

## Observation–State–Action Interface

물체·task variation → 실제/시뮬레이션 접촉 과제.

## Evaluation Scope and Claim Boundary

36개 reference task 중 6개에서 vision-only와 visual-tactile 정책을 비교한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2610.24512) · [저자 project/code](https://jingyi-xiang.github.io/contactbench/) · [공식 code](https://github.com/Michaelwyx/contactbench-sim). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

접촉 일반화 질문을 구체적인 물리 변화와 재현 자산으로 정의할 benchmark다.

## Verification Boundary

task별 success 판정, asset version, 정책용 reset/step와 scripted helper 분리을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
