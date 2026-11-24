# STAFF: Speculative Coreset Selection for Task-Specific Fine-tuning

> Evidence maturity: `FULL_TEXT_CHECKED`. 요약과 기여를 아래 쪽수에서 확인했다.

- Year/Venue: 2025 / ICLR
- Authors: Xiaoyu Zhang, Juan Zhai, Shiqing Ma, Chao Shen, Tianlin Li, Weipeng Jiang, Yang Liu
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: REFERENCE
- Tags: Robotics, evaluation, data-selection
- Aliases:
- Official paper: https://proceedings.iclr.cc/paper_files/paper/2025/hash/412360d2dd428c26f34918c8d682cf7e-Abstract-Conference.html
- Venue verification: https://proceedings.iclr.cc/paper_files/paper/2025/hash/412360d2dd428c26f34918c8d682cf7e-Abstract-Conference.html
- Code/Project: not identified
- Code: not_identified
- Full-text retrieval: https://proceedings.iclr.cc/paper_files/paper/2025/file/412360d2dd428c26f34918c8d682cf7e-Paper-Conference.pdf
- Source audit: 2026-11-24에 요약과 핵심 기여 두 개를 원문과 대조했다.

## Problem and Importance

STAFF는 대규모 언어 모델의 미세조정 자료를 고를 때 같은 계열의 소형 모델로 후보를 먼저 채점해 선별 비용을 줄인다. [PDF 1쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/412360d2dd428c26f34918c8d682cf7e-Paper-Conference.pdf#page=1) · [PDF 5쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/412360d2dd428c26f34918c8d682cf7e-Paper-Conference.pdf#page=5)

## Core Idea and Contribution

- 소형 모델의 점수를 구간별로 나눈 뒤 대상 모델로 일부 표본을 검산해 중요한 구간에 선별 예산을 더 배분한다. [PDF 4쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/412360d2dd428c26f34918c8d682cf7e-Paper-Conference.pdf#page=4) · [PDF 5쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/412360d2dd428c26f34918c8d682cf7e-Paper-Conference.pdf#page=5) · [PDF 6쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/412360d2dd428c26f34918c8d682cf7e-Paper-Conference.pdf#page=6)
- 언어 과제에서 남길 자료 비율을 바꿔 미세조정 후 품질과 코어셋을 고르는 데 드는 시간을 각각 측정했다. [PDF 7쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/412360d2dd428c26f34918c8d682cf7e-Paper-Conference.pdf#page=7) · [PDF 8쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/412360d2dd428c26f34918c8d682cf7e-Paper-Conference.pdf#page=8)

## Observation–State–Action Interface

LLM 학습 예제 → proxy score·target verification → coreset; robot action interface는 아니다.

## Evaluation Scope and Claim Boundary

LLM fine-tuning 평가이며 VLA의 closed-loop 성공을 검증한 논문은 아니다.

근거: [공식 paper/abstract](https://proceedings.iclr.cc/paper_files/paper/2025/hash/412360d2dd428c26f34918c8d682cf7e-Abstract-Conference.html).

## Why This Paper Is Here — Researcher Interpretation

Proxy scoring과 target 확인 자체를 새 VLA 기여로 재주장하지 않게 하는 GAP-N1의 직접 선행이다.

## Verification Boundary

LLM에서 VLA로의 적용 한계, target verification 비용을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
