# Simple Masked Training Strategies Yield Control Policies That Are Robust to Sensor Failure

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2024 / CoRL
- Authors: Skand Skand, Bikram Pandit, Chanho Kim, Li Fuxin, Stefan Lee
- Conference year: 2024; proceedings publication year: 2025. [PMLR volume 270](https://proceedings.mlr.press/v270/)의 개최일과 출판일을 구분한다.
- Category: World Models, Safety, and Recovery
- Primary track: World models, safety, uncertainty, and recovery
- Tier: NEXT
- Tags: Robotics, evaluation, robustness
- Aliases:
- Official paper: https://proceedings.mlr.press/v270/skand25a.html
- Venue verification: https://proceedings.mlr.press/v270/skand25a.html
- Conference edition: 2024 · https://proceedings.mlr.press/v270/
- Code/Project: https://pvskand.github.io/projects/RME
- Code: project_only
- Source audit: 2026-10-25 공식 abstract와 publication metadata 및 명시된 project/code 공개 링크 확인. 본문 정독·코드 실행·payload 검증은 이번 등록 범위 밖이다. CoRL 개최 2024, PMLR 출판 2025를 분리한다. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

이 연구는 학습 중 일부 센서 입력을 가려 실제 센서가 빠진 뒤에도 제어를 계속할 수 있는 강화학습 정책을 만든다. [PDF 1쪽](https://raw.githubusercontent.com/mlresearch/v270/d9fe509ba390176a5fd650178a381a0a7b2d4f64/assets/skand25a/skand25a.pdf#page=1)

## Core Idea and Contribution

- 다중 센서 인코더가 이용 가능한 관측을 알 수 있게 하고 훈련 중 센서 모달리티의 일부를 무작위로 제거한다. [PDF 3쪽](https://raw.githubusercontent.com/mlresearch/v270/d9fe509ba390176a5fd650178a381a0a7b2d4f64/assets/skand25a/skand25a.pdf#page=3) · [PDF 5쪽](https://raw.githubusercontent.com/mlresearch/v270/d9fe509ba390176a5fd650178a381a0a7b2d4f64/assets/skand25a/skand25a.pdf#page=5)
- 양발 보행과 조작에서 고유수용감각·시각 고장을 시험하고 실제 Cassie의 보행 명령 추종도 평가했다. [PDF 6쪽](https://raw.githubusercontent.com/mlresearch/v270/d9fe509ba390176a5fd650178a381a0a7b2d4f64/assets/skand25a/skand25a.pdf#page=6) · [PDF 8쪽](https://raw.githubusercontent.com/mlresearch/v270/d9fe509ba390176a5fd650178a381a0a7b2d4f64/assets/skand25a/skand25a.pdf#page=8)

## Observation–State–Action Interface

가용 sensor와 결손 처리 표현 → RL control policy.

## Evaluation Scope and Claim Boundary

Locomotion과 manipulation, simulation과 실로봇의 sensor failure를 평가한다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v270/skand25a.html) · [저자 project/code](https://pvskand.github.io/projects/RME). 문장에 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

새 multimodal VLA adaptation 전에 대조할 단순 sensor-dropout 기준이다.

## Verification Boundary

결손 종류·지속 시간·학습 노출, proprio와 image mask 차이을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
