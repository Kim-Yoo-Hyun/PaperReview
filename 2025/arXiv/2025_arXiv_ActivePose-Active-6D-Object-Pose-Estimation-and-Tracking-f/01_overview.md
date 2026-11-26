# ActivePose: Active 6D Object Pose Estimation and Tracking for Robotic Manipulation

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2025 / arXiv
- Authors: Sheng Liu, Zhe Li, Weiheng Wang, Han Sun, Heng Zhang, Hongpeng Chen, Yusen Qin, Arash Ajoudani, Yizhao Wang
- Category: Robotics-Enabling 3D Perception
- Primary track: Robotics-enabling 3D perception
- Tier: NEXT
- Tags: active perception, 6D pose, VLM, next-best-view
- Aliases: ActivePose
- Official paper: https://arxiv.org/abs/2509.11364
- Venue verification: https://arxiv.org/abs/2509.11364
- Code/Project: not identified
- Code: not_identified
- 방법·평가 확인 (2026-11-25): [원문 3, 4, 5, 6, 7쪽](https://arxiv.org/pdf/2509.11364v2#page=3) · [다축 분류와 공개 범위](../../../work/sources/batches/core_next_10.yaml)
- Source audit: 2026-11-18: 공식 초록·bibliographic record와 연결된 저자 자료 확인. Abstract 기반 등록이며 본문 전체·실험 재현은 미확인. 현재 abstract는 2026-03-07 v2; 최초 공개 연도 2025 유지. 이전 N1의 v1 지정 절 검토와 같은 본문으로 취급하지 않는다. 공식 conference/journal acceptance 확인을 확보하지 못해 preprint 유지. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

ActivePose는 새 물체 자세가 모호할 때 카메라를 능동적으로 옮기고, 조작 도중에는 물체가 보이도록 시점을 제어해 자세 추적을 유지한다. [PDF 1쪽](https://arxiv.org/pdf/2509.11364v2#page=1)

## Core Idea and Contribution

- CAD 렌더링과 FoundationPose 자세 가설의 엔트로피로 시점 예시를 구성하고, 시각언어 모델의 모호성 점수와 결합해 도달 가능한 다음 시점을 선택한다. [PDF 3쪽](https://arxiv.org/pdf/2509.11364v2#page=3) · [PDF 4쪽](https://arxiv.org/pdf/2509.11364v2#page=4)
- 카메라 궤적을 출력하는 확산 정책을 시연으로 학습하고, 실제 물체 이동·가림에서의 추적 및 핀 삽입 결과를 초기 자세 추정과 구분해 평가했다. [PDF 5쪽](https://arxiv.org/pdf/2509.11364v2#page=5) · [PDF 6쪽](https://arxiv.org/pdf/2509.11364v2#page=6) · [PDF 7쪽](https://arxiv.org/pdf/2509.11364v2#page=7)

## Observation–State–Action Interface

RGB 관측·CAD 기반 가상 시점 → ambiguity score·NBV·pose tracking으로 이어진다.

## Evaluation Scope and Claim Boundary

공식 초록은 로봇 조작을 위한 active pose estimation/tracking을 다룬다. Task별 성공률과 camera 이동 비용은 본문 확인 필요다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2509.11364). 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

Pose estimation+active perception 조합이 이미 구현됐음을 보여 주는 직접 선행이다.

## Verification Boundary

VLM score calibration·CAD render 조건·물리 camera 비용·task success 기준을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
