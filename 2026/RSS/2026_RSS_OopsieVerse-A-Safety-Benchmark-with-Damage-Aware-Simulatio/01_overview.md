# OopsieVerse: A Safety Benchmark with Damage-Aware Simulation for Robot Manipulation

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / RSS
- Authors: Arnav Balaji, Arpit Bahety, Sriniket Ambatipudi, Daniel Lam, Junhong Xu, Roberto Martín-Martín
- Category: World Models, Safety, and Recovery
- Primary track: World models, safety, uncertainty, and recovery
- Tier: NEXT
- Tags: damage-aware, safety, Benchmark
- Aliases: OopsieVerse
- Official paper: https://www.roboticsproceedings.org/rss22/p098.html
- Venue verification: https://www.roboticsproceedings.org/rss22/p098.html
- Code/Project: https://robin-lab.cs.utexas.edu/oopsieverse/
- Code: https://github.com/UT-Austin-RobIn/oopsieverse
- Source audit: 2026-10-19: 공식 paper abstract 및 저자 project/code README 확인; abstract 기반 — 본문 수동 확인 필요. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

OopsieVerse는 가사 로봇이 일을 끝냈는지와 그 과정에서 물체나 환경에 손상을 일으켰는지를 분리해 측정한다. [PDF 1쪽](https://www.roboticsproceedings.org/rss22/p098.pdf#page=1)

## Core Idea and Contribution

- DamageSim은 접촉력·온도 변화·액체 상호작용을 손상 신호로 바꾸고 이를 보상이나 종료 조건에 반영한다. [PDF 2쪽](https://www.roboticsproceedings.org/rss22/p098.pdf#page=2) · [PDF 3쪽](https://www.roboticsproceedings.org/rss22/p098.pdf#page=3)
- 서로 다른 물리 엔진의 가사 환경에 손상 측정을 적용해 시연 수집, 정책 학습, VLA의 안전한 작업 완료를 평가했다. [PDF 5쪽](https://www.roboticsproceedings.org/rss22/p098.pdf#page=5) · [PDF 8쪽](https://www.roboticsproceedings.org/rss22/p098.pdf#page=8)

## Observation–State–Action Interface

Physical simulator state/signal → damage observation/reward/termination → IL/RL 및 VLA evaluation.

## Evaluation Scope and Claim Boundary

RSS abstract는 OmniGibson과 RoboCasa 구현, safer demonstration, damage-conditioned IL/RL, VLA safety 및 sim-to-real use case를 설명한다.

근거: [공식 paper/abstract](https://www.roboticsproceedings.org/rss22/p098.html) · [저자 project/code](https://robin-lab.cs.utexas.edu/oopsieverse/). 문장에 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

Benchmark. Task success와 물리적 damage를 분리하고 damage-aware IL/RL 및 VLA 평가를 지원한다. 기존 safety/recovery 흐름에 contact·thermal·fluid damage라는 구체적인 평가 축을 보충한다.

## Verification Boundary

Damage threshold/단위, simulator fidelity, user preference와 real-world damage validation을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.

## 원문과 공개 자료

- 코드 — DamageSim과 손상을 측정하는 조작 환경 · damagesim/core/damageable_env.py [배포 파일](https://raw.githubusercontent.com/UT-Austin-RobIn/oopsieverse/a739f99e94f32c3229ae6932299e2e0e8c065480/damagesim/core/damageable_env.py)
- 데이터 — 서랍 열기 벤치마크 장면의 초기 상태 · oopsiebench/envs/behavior1k/init_states/open_drawer.pkl [배포 파일](https://raw.githubusercontent.com/UT-Austin-RobIn/oopsieverse/a739f99e94f32c3229ae6932299e2e0e8c065480/oopsiebench/envs/behavior1k/init_states/open_drawer.pkl)
