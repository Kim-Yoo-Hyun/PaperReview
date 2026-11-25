# TidyBot++: An Open-Source Holonomic Mobile Manipulator for Robot Learning

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2024 / CoRL
- Authors: Jimmy Wu, William Chong, Robert Holmberg, Aaditya Prasad, Yihuai Gao, Oussama Khatib, Shuran Song, Szymon Rusinkiewicz, Jeannette Bohg
- Category: Locomotion, Whole-Body, and Mobile Manipulation
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: NEXT
- Tags: Robotics, mobile manipulation, teleoperation, holonomic-base
- Aliases: TidyBot++, TidyBot2
- Official paper: https://proceedings.mlr.press/v270/wu25a.html
- Venue verification: https://proceedings.mlr.press/v270/wu25a.html
- Conference edition: 2024 · https://proceedings.mlr.press/v270/
- Code/Project: https://tidybot2.github.io/
- Code: https://github.com/jimmyyhwu/tidybot2
- Source audit: 2026-10-25 공식 abstract/서지정보 및 명시된 저자 링크 확인. 이번 노트는 abstract 기반이며 본문 전체·코드 실행·payload는 미검증이다. CoRL 개최 2024, PMLR 출판 2025. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

TidyBot++는 좁은 실내에서도 어느 방향으로든 이동하며 여러 로봇팔과 함께 쓸 수 있도록 설계한 모바일 조작 플랫폼이다. [PDF 1쪽](https://raw.githubusercontent.com/mlresearch/v270/d9fe509ba390176a5fd650178a381a0a7b2d4f64/assets/wu25a/wu25a.pdf#page=1)

## Core Idea and Contribution

- 능동 캐스터로 평면 병진과 회전을 제어하는 베이스를 만들고 로봇팔 장착과 스마트폰 원격조작 방식을 공개했다. [PDF 3쪽](https://raw.githubusercontent.com/mlresearch/v270/d9fe509ba390176a5fd650178a381a0a7b2d4f64/assets/wu25a/wu25a.pdf#page=3) · [PDF 4쪽](https://raw.githubusercontent.com/mlresearch/v270/d9fe509ba390176a5fd650178a381a0a7b2d4f64/assets/wu25a/wu25a.pdf#page=4) · [PDF 5쪽](https://raw.githubusercontent.com/mlresearch/v270/d9fe509ba390176a5fd650178a381a0a7b2d4f64/assets/wu25a/wu25a.pdf#page=5)
- 실내 작업에서 이동과 팔 조작을 결합해 원격 시연을 수집하고 그 자료로 학습한 정책의 실행을 평가했다. [PDF 6쪽](https://raw.githubusercontent.com/mlresearch/v270/d9fe509ba390176a5fd650178a381a0a7b2d4f64/assets/wu25a/wu25a.pdf#page=6) · [PDF 7쪽](https://raw.githubusercontent.com/mlresearch/v270/d9fe509ba390176a5fd650178a381a0a7b2d4f64/assets/wu25a/wu25a.pdf#page=7)

## Observation–State–Action Interface

사람 teleoperation → base/arm demonstration → mobile manipulation policy.

## Evaluation Scope and Claim Boundary

실로봇 가정 과제에서 수집한 시연으로 학습한 정책을 평가한다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v270/wu25a.html) · [저자 project/code](https://github.com/jimmyyhwu/tidybot2). 문장에 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

다양한 로봇 연구에서 policy 성능과 base의 운동학적 자유도 차이를 구분할 플랫폼 기준이다.

## Verification Boundary

arm 지원 범위와 실제 검증 조합, base/arm 제어 주기, 비용·teleoperation protocol을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.

## 원문 대조

전방향 이동 기저와 휴대전화 원격조작으로 실물 시연을 수집했다. 확인한 다운로드용 시연과 정책은 sim-v1 예제다. [방법과 평가](https://raw.githubusercontent.com/mlresearch/v270/d9fe509ba390176a5fd650178a381a0a7b2d4f64/assets/wu25a/wu25a.pdf#page=7)

## 공개 자료

- 코드 — 모바일 매니퓰레이터의 이동 기저 제어 · base_controller.py [배포 파일](https://raw.githubusercontent.com/jimmyyhwu/tidybot2/c8dd23819f9cced476124a4b88538e6863ef53f7/base_controller.py)
- 가중치 — sim-v1 행동 정책 · epoch-0500-train_loss-0.001.ckpt [배포 파일](https://www.dropbox.com/scl/fi/tpmnl1lh2tljxsnq3nnr9/epoch-0500-train_loss-0.001.ckpt?rlkey=44ou4zfhu2de5hjse3v670qos&dl=1")
- 데이터 — sim-v1 시뮬레이션 시연 · sim-v1.hdf5 [배포 파일](https://www.dropbox.com/scl/fi/0lhco1tfoi7dxyjcsz1ok/sim-v1.hdf5?rlkey=4wyspmcr9xymvsy2s22t6girv&dl=1")
