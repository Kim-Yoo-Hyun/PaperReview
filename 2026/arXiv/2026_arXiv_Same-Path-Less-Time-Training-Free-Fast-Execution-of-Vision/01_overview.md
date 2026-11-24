# Same Path, Less Time: Training-Free Fast Execution of Vision-Language-Action Models under Inference Latency

> Evidence maturity: `FULL_TEXT_CHECKED`. 요약과 기여를 아래 쪽수에서 확인했다.

- Year/Venue: 2026 / arXiv
- Authors: Fuyi Chen
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, latency, action-chunking, control-frequency
- Aliases: Path-preserving Time Scaling, PTS
- Official paper: https://arxiv.org/abs/2611.01390
- Venue verification: https://arxiv.org/abs/2611.01390
- Code/Project: not identified
- Code: not_identified
- Full-text retrieval: https://arxiv.org/pdf/2611.01390v1
- Source audit: 2026-11-24에 요약과 핵심 기여 두 개를 원문과 대조했다. 평가 조건은 04_evaluation.md에 쪽수와 함께 기록했다.

## Problem and Importance

PTS는 동결된 행동 청크 정책을 실행할 때 새 추론이 끝날 때까지 이동한 양과 경로를 따라가는 속도를 함께 고려해 추론 지연을 보상한다. [PDF 1쪽](https://arxiv.org/pdf/2611.01390v1#page=1) · [PDF 4쪽](https://arxiv.org/pdf/2611.01390v1#page=4)

## Core Idea and Contribution

- 새 청크에는 추론 중 진행한 위치에서 진입하고, 그리퍼가 움직이는 구간과 구동기의 동작 범위에 따라 팔의 가속 배율을 제한한다. [PDF 4쪽](https://arxiv.org/pdf/2611.01390v1#page=4) · [PDF 5쪽](https://arxiv.org/pdf/2611.01390v1#page=5) · [PDF 6쪽](https://arxiv.org/pdf/2611.01390v1#page=6)
- LIBERO에서 지연을 주입해 π0.5와 SmolVLA의 처리량과 성공률을 비교하고, 이동 표적을 포함하는 LIBERO-Dynamic에서는 비동기 등속 실행과 비슷한 처리량을 관찰했다. [PDF 7쪽](https://arxiv.org/pdf/2611.01390v1#page=7) · [PDF 10쪽](https://arxiv.org/pdf/2611.01390v1#page=10) · [PDF 11쪽](https://arxiv.org/pdf/2611.01390v1#page=11)

## Observation–State–Action Interface

고정 VLA 행동 chunk·추론 지연 → 경로/진행도 정렬 → 속도 조절된 실행 명령.

## Evaluation Scope and Claim Boundary

표 1의 처리량은 추론 대기 시간을 포함한 제어 1,000스텝당 성공 횟수다. π0.5는 4개 과제군, SmolVLA는 2개 과제군에서 비교했다. [PDF 7쪽](https://arxiv.org/pdf/2611.01390v1#page=7) · [PDF 8쪽](https://arxiv.org/pdf/2611.01390v1#page=8)

근거: [공식 paper/abstract](https://arxiv.org/abs/2611.01390).

## Why This Paper Is Here — Researcher Interpretation

제어 주기 학습 전에 넘어야 할 학습 없는 실행 대안이며 예비 timing 질문의 비교 자료다.

## Verification Boundary

본문에서 확인할 항목: 실제 지연과 주입 지연·동작 제한·gripper 동기화·실제 로봇 전이. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
