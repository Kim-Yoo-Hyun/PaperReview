# Behavior-Skill: A Fine-Grained Benchmark for Evaluating Vision-Language-Action Policies in Long-Horizon Tasks

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / arXiv
- Authors: Chunyun Ma, Lun Luo, Xingjian Luo, Xiexing Feng, Hang Zhang, Wei Liu, Feng Qiao, Yaonan Wang, Huimin Lu, Xieyuanli Chen
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: Robotics, VLA, Benchmark, mobile-manipulation, skill-evaluation
- Aliases: Behavior-Skill
- Official paper: https://arxiv.org/abs/2608.30536
- Venue verification: https://arxiv.org/abs/2608.30536
- Code/Project: https://github.com/nubot-nudt/Behavior-Skill
- Code: https://github.com/nubot-nudt/Behavior-Skill
- Source audit: 2026-10-28 공식 서지/abstract·저자 project/code 소개 확인. 신규 표준 노트는 abstract 기반이다. 기존 HANDOFF 지정 구간 검토는 별도 source ledger에 있으며 전체 정독·payload·실행 검증을 뜻하지 않는다. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

Behavior-Skill은 긴 가사 작업의 전체 성공률에 가려지는 기술별 병목을 볼 수 있도록 중간 상태에서 정책을 평가한다. [PDF 1쪽](https://arxiv.org/pdf/2608.30536v1#page=1)

## Core Idea and Contribution

- 시연을 기술별 구간으로 나누고 각 구간의 시작 상태와 성공 기준을 저장해 지정한 중간 상태에서 반복 평가할 수 있게 했다. [PDF 2쪽](https://arxiv.org/pdf/2608.30536v1#page=2) · [PDF 3쪽](https://arxiv.org/pdf/2608.30536v1#page=3) · [PDF 4쪽](https://arxiv.org/pdf/2608.30536v1#page=4)
- 기술 단위 측정과 전체 궤적 평가를 비교하고 접촉이 필요한 동작에서 범용 정책의 실패가 집중되는 조건을 분석했다. [PDF 2쪽](https://arxiv.org/pdf/2608.30536v1#page=2) · [PDF 6쪽](https://arxiv.org/pdf/2608.30536v1#page=6)

## Observation–State–Action Interface

Skill instruction와 복원된 시작 상태의 관측 → VLA action → skill 성공 판단 및 trajectory/skill 단위 지표.

## Evaluation Scope and Claim Boundary

50개 household task의 시연으로 구성한 benchmark에서 π0.5와 GR00T 등 정책을 평가한다. 복원된 유효 시작 상태의 개별 능력은 이전 정책이 실제 도달한 상태에서의 연결 실행 성능과 구분한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2608.30536) · [저자 project/code](https://github.com/nubot-nudt/Behavior-Skill). 문장에 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

현재 HANDOFF P0의 직접적인 benchmark/source prerequisite다. 전체 task 성공률과 독립 skill 능력의 차이를 읽을 NEXT로 추가하되 preprint status를 유지한다.

## Verification Boundary

공개 release와 논문 정책 쌍의 일치, 시연 reset과 continuation의 차이, 학습/평가 instance 분리, normalizer와 controller·queue·종료 정의을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
