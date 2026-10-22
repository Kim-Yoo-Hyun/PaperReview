# OopsieVerse: A Safety Benchmark with Damage-Aware Simulation for Robot Manipulation

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / RSS
- Category: World Models, Safety, and Recovery
- Primary track: World models, safety, uncertainty, and recovery
- Tier: NEXT
- Tags: damage-aware, safety, Benchmark
- Aliases: OopsieVerse
- Official paper: https://www.roboticsproceedings.org/rss22/p098.html
- Venue verification: https://www.roboticsproceedings.org/rss22/p098.html
- Code/Project: https://robin-lab.cs.utexas.edu/oopsieverse/
- Code: https://github.com/UT-Austin-RobIn/oopsieverse
- Source audit: 2026-10-19: 공식 paper abstract 및 저자 project/code README 확인; abstract 기반 — 본문 수동 확인 필요.

## Problem and Importance

Household manipulation의 task success만으로는 robot·물체·환경의 손상을 평가할 수 없다.

## Core Idea and Contribution

Contact/thermal/fluid signal을 damage로 변환하는 DamageSim과 damage-aware household task benchmark를 제공한다.

## Observation–State–Action Interface

Physical simulator state/signal → damage observation/reward/termination → IL/RL 및 VLA evaluation.

## Evaluation Scope and Claim Boundary

RSS abstract는 OmniGibson과 RoboCasa 구현, safer demonstration, damage-conditioned IL/RL, VLA safety 및 sim-to-real use case를 설명한다.

근거: [공식 paper/abstract](https://www.roboticsproceedings.org/rss22/p098.html) · [저자 project/code](https://robin-lab.cs.utexas.edu/oopsieverse/). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

Benchmark. Task success와 물리적 damage를 분리하고 damage-aware IL/RL 및 VLA 평가를 지원한다. 기존 safety/recovery 흐름에 contact·thermal·fluid damage라는 구체적인 평가 축을 보충한다.

## Verification Boundary

Damage threshold/단위, simulator fidelity, user preference와 real-world damage validation을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
