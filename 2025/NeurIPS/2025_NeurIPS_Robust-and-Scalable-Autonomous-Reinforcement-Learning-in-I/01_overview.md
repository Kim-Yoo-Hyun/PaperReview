# Robust and Scalable Autonomous Reinforcement Learning in Irreversible Environments

> Evidence maturity: `FULL_TEXT_CHECKED`. 아래에 쪽수를 붙인 문장을 원문과 대조했다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2025 / NeurIPS
- Authors: Sang-Hyun Lee
- Category: Robotics Foundations: Robot Learning
- Primary track: RL, IL, offline learning, and robot data
- Tier: REFERENCE
- Tags: RL, evaluation, learning-foundation
- Aliases: RSA
- Official paper: https://proceedings.neurips.cc/paper_files/paper/2025/hash/56d748a1d7128158681280be7668e0d3-Abstract-Conference.html
- Full-text retrieval: https://proceedings.neurips.cc/paper_files/paper/2025/file/56d748a1d7128158681280be7668e0d3-Paper-Conference.pdf
- Venue verification: https://proceedings.neurips.cc/paper_files/paper/2025/hash/56d748a1d7128158681280be7668e0d3-Abstract-Conference.html
- Code/Project: not identified
- Code: not_identified
- Source audit: 2026-11-24에 한 줄 요약과 핵심 기여 두 개를 아래 PDF 쪽수에 대조했다.

## Problem and Importance

RSA는 되돌리기 어려운 상태가 있는 환경에서 과제 정책과 복귀 정책을 함께 학습하며 진행도에 따라 시작·목표 상태를 선택한다. [PDF 1쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/56d748a1d7128158681280be7668e0d3-Paper-Conference.pdf#page=1)

## Core Idea and Contribution

- 정책이 배울 여지가 있는 상태로 커리큘럼을 구성하고 행동 기록으로 복귀하기 어려운 상태를 식별한다. [PDF 4쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/56d748a1d7128158681280be7668e0d3-Paper-Conference.pdf#page=4) · [PDF 5쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/56d748a1d7128158681280be7668e0d3-Paper-Conference.pdf#page=5) · [PDF 6쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/56d748a1d7128158681280be7668e0d3-Paper-Conference.pdf#page=6)
- 이동·조작 시뮬레이션에서 성공과 외부 재설정을 비교하고 상태 선정과 비가역성 탐지의 효과를 분리해 평가했다. [PDF 7쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/56d748a1d7128158681280be7668e0d3-Paper-Conference.pdf#page=7) · [PDF 8쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/56d748a1d7128158681280be7668e0d3-Paper-Conference.pdf#page=8) · [PDF 9쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/56d748a1d7128158681280be7668e0d3-Paper-Conference.pdf#page=9)

## Observation–State–Action Interface

Forward/reset 경험 → informative state 선택·위험 회피.

## Evaluation Scope and Claim Boundary

가역/비가역 환경에서 성능과 manual reset 감소를 보고한다.

근거: [공식 paper/abstract](https://proceedings.neurips.cc/paper_files/paper/2025/hash/56d748a1d7128158681280be7668e0d3-Abstract-Conference.html). 추가 수치와 실패 조건은 해당 실험의 표·설정을 확인해야 한다.

## Why This Paper Is Here — Researcher Interpretation

C5/D3의 비가역성·reset 질문에 필요한 RL 선행이다.

## Verification Boundary

irreversibility 정의, behavior encoding, task-specific 정보, reset 비용을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
