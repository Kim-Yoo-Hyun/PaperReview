# ActMem-VLA: Action-History Memory with Dual-Expert Denoising for Long-Horizon Vision-Language-Action Policies

> Evidence maturity: `FULL_TEXT_CHECKED`. 요약과 기여를 아래 쪽수에서 확인했다.

- Year/Venue: 2026 / arXiv
- Authors: Yaxin Zhao, Dianye Huang, Chenwei Wang, Chenguang Yang, Zhongliang Jiang
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, memory, action-history, long-horizon
- Aliases: ActMem-VLA
- Official paper: https://arxiv.org/abs/2609.37307
- Venue verification: https://arxiv.org/abs/2609.37307
- Code/Project: not identified
- Code: not_identified
- Full-text retrieval: https://arxiv.org/pdf/2609.37307v2
- Source audit: 2026-11-24에 요약과 핵심 기여 두 개를 원문과 대조했다. 평가 조건은 04_evaluation.md에 쪽수와 함께 기록했다.

## Problem and Importance

ActMem-VLA는 비슷하게 보이는 장면에서 작업 단계를 구분하기 위해 실행한 행동 이력을 인코딩하고, 동결된 VLA의 초기 잡음 제거 단계를 유도한다. [PDF 1쪽](https://arxiv.org/pdf/2609.37307v2#page=1) · [PDF 3쪽](https://arxiv.org/pdf/2609.37307v2#page=3)

## Core Idea and Contribution

- Mamba 기억과 경량 행동 전문가만 학습해 초기 잡음 제거를 맡기고, 남은 단계에서 기존 행동 전문가가 세부 움직임을 다듬는다. [PDF 3쪽](https://arxiv.org/pdf/2609.37307v2#page=3) · [PDF 4쪽](https://arxiv.org/pdf/2609.37307v2#page=4)
- LIBERO-Mem의 시연 길이로 정한 과제별 스텝 제한을 적용한 10개 과제에서 평균 성공률은 80.8%였고 π0.5는 65.2%, MemoryVLA는 49.5%였다. 과제별 우위는 달랐다. [PDF 4쪽](https://arxiv.org/pdf/2609.37307v2#page=4) · [PDF 5쪽](https://arxiv.org/pdf/2609.37307v2#page=5)

## Observation–State–Action Interface

실행 행동 이력·현재 맥락 → memory/PAE → frozen AE의 행동 refinement.

## Evaluation Scope and Claim Boundary

LIBERO-Mem 평균 80.8%는 과제별 시연 길이로 정한 스텝 제한을 적용한 결과다. 공통 600스텝 제한의 결과는 그림 3, 과제별 제한은 그림 4에 실렸다. [PDF 4쪽](https://arxiv.org/pdf/2609.37307v2#page=4) · [PDF 5쪽](https://arxiv.org/pdf/2609.37307v2#page=5)

근거: [공식 paper/abstract](https://arxiv.org/abs/2609.37307).

## Why This Paper Is Here — Researcher Interpretation

행동 이력 memory의 강한 비교 자료이며 결과 기반 기억이라는 질문의 기존 대안을 구체화한다.

## Verification Boundary

본문에서 확인할 항목: memory reset·실제 실행 이력의 정의·효과 피드백 접근권·분할과 예산. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
