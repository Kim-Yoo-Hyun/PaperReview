# LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization

> Evidence maturity: `FULL_TEXT_CHECKED`. 요약과 기여를 아래 쪽수에서 확인했다.

- Year/Venue: 2025 / arXiv
- Authors: Xueyang Zhou, Yangming Xu, Guiyao Tie, Yongchao Chen, Guowen Zhang, Duanfeng Chu, Pan Zhou, Lichao Sun
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, Benchmark, generalization
- Aliases:
- Official paper: https://arxiv.org/abs/2510.03827
- Venue verification: https://arxiv.org/abs/2510.03827
- Code/Project: https://github.com/Zxy-MLlab/LIBERO-PRO
- Code: https://github.com/Zxy-MLlab/LIBERO-PRO
- Full-text retrieval: https://arxiv.org/pdf/2510.03827v2
- Source audit: 2026-11-24에 요약과 핵심 기여 두 개를 원문과 대조했다. 평가 조건은 04_evaluation.md에 쪽수와 함께 기록했다.

## Problem and Importance

LIBERO-PRO는 기존 LIBERO에서 학습한 조작 정책의 성공이 물체·배치·지시·환경이 바뀌어도 유지되는지 검사한다. [PDF 1쪽](https://arxiv.org/pdf/2510.03827v2#page=1) · [PDF 6쪽](https://arxiv.org/pdf/2510.03827v2#page=6)

## Core Idea and Contribution

- 목표 물체를 바꾸거나 지시를 교란하는 진단 사례와, 물체·배치·지시·과제·환경을 나눠 바꾸는 벤치마크를 제시했다. [PDF 3쪽](https://arxiv.org/pdf/2510.03827v2#page=3) · [PDF 4쪽](https://arxiv.org/pdf/2510.03827v2#page=4) · [PDF 6쪽](https://arxiv.org/pdf/2510.03827v2#page=6)
- OpenVLA, π0, π0.5에서 교란 종류와 과제군에 따라 성공률 저하가 달랐고, 위치와 과제 변화에서 큰 하락을 관찰했다. [PDF 7쪽](https://arxiv.org/pdf/2510.03827v2#page=7) · [PDF 8쪽](https://arxiv.org/pdf/2510.03827v2#page=8)

## Observation–State–Action Interface

변형 task/지시 → VLA → 실행 결과.

## Evaluation Scope and Claim Boundary

그림 6은 교란을 다섯 종류로 나누며 작업 목표를 바꾸는 교란은 조합에서 제외한다. 그림 7의 성공률은 모델·교란·과제군별로 달라서 초록의 0.0%를 전체 평균으로 인용할 수 없다. [PDF 6쪽](https://arxiv.org/pdf/2510.03827v2#page=6) · [PDF 7쪽](https://arxiv.org/pdf/2510.03827v2#page=7) · [PDF 8쪽](https://arxiv.org/pdf/2510.03827v2#page=8)

근거: [공식 paper/abstract](https://arxiv.org/abs/2510.03827) · [저자 project/code](https://github.com/Zxy-MLlab/LIBERO-PRO).

## Why This Paper Is Here — Researcher Interpretation

지시 교란 평가와 구현된 task의 유효성을 함께 점검할 비교 benchmark다.

## Verification Boundary

변경된 목표의 타당성, 언어 교란의 의미, v1/v2 차이을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
