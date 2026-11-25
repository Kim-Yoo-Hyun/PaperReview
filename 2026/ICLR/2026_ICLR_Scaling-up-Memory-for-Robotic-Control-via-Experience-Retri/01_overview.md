# Scaling up Memory for Robotic Control via Experience Retrieval

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / ICLR
- Authors: Ajay Sridhar, Jennifer Pan, Satvik Sharma, Chelsea Finn
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, episodic-memory, hierarchical-control, long-horizon
- Aliases: MemER, MemER: Scaling Up Memory for Robot Control via Experience Retrieval
- Official paper: https://proceedings.iclr.cc/paper_files/paper/2026/hash/9da515b1ad19d032a7398f00f5ff9b0c-Abstract-Conference.html
- Venue verification: https://proceedings.iclr.cc/paper_files/paper/2026/hash/9da515b1ad19d032a7398f00f5ff9b0c-Abstract-Conference.html
- Code/Project: https://jen-pan.github.io/memer/
- Code: https://github.com/memer-policy/memer
- Source audit: 2026-11-02 공식 proceedings/publisher의 서지·abstract와 저자 project/code 소개를 확인했다. 노트는 abstract/project 기반이며 본문 정독·native 실행을 뜻하지 않는다. 사용자 읽기 상태는 UNREAD 유지. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

MemER는 수분에 걸친 조작에서 현재 지시 수행에 필요한 과거 장면을 찾고 최근 장면과 함께 다음 행동을 정한다. [PDF 1쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/9da515b1ad19d032a7398f00f5ff9b0c-Paper-Conference.pdf#page=1)

## Core Idea and Contribution

- 상위 정책이 핵심 프레임을 골라 과거의 중요한 장면을 보존하고, 최근 관측과 함께 해석해 하위 조작 정책에 지시를 전달한다. [PDF 3쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/9da515b1ad19d032a7398f00f5ff9b0c-Paper-Conference.pdf#page=3) · [PDF 4쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/9da515b1ad19d032a7398f00f5ff9b0c-Paper-Conference.pdf#page=4)
- 세 가지 실제 장시간 과제에서 핵심 장면 검색과 최근 관측의 역할을 평가하고 기억을 제거한 조건과 비교했다. [PDF 6쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/9da515b1ad19d032a7398f00f5ff9b0c-Paper-Conference.pdf#page=6) · [PDF 8쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/9da515b1ad19d032a7398f00f5ff9b0c-Paper-Conference.pdf#page=8)

## Observation–State–Action Interface

이력 keyframe·현재 관측·task → 상위 언어 지시 → π0.5 하위 조작 정책. Episode 내 기억과 외부 시연 bank는 다른 정보원이다.

## Evaluation Scope

수분 동안의 기억이 필요한 실제 로봇 조작 과제 3개에서 비교한다. 프로젝트의 object search·counting·dust-and-replace는 task 설명이며 독립 재현 결과가 아니다.

근거: [공식 paper/abstract](https://proceedings.iclr.cc/paper_files/paper/2026/hash/9da515b1ad19d032a7398f00f5ff9b0c-Abstract-Conference.html) · [저자 project](https://jen-pan.github.io/memer/).

## Why This Paper Is Here — Researcher Interpretation

MemoryVLA와 계층 정책의 관계를 구체화하는 NEXT다. 외부 시연 검색과 실행 중 기억을 구분하고 SET의 counting 선행을 보완한다.

범위와 수치의 미확인 항목은 [평가 노트](./04_evaluation.md)에, 제안하는 반증 질문은 [insights](./05_insights.md)에 둔다.

## 공개 자료

- 코드 — 장기 실물 과제의 핵심 프레임 기억 · memer_eval/memory.py [배포 파일](https://raw.githubusercontent.com/memer-policy/memer/fb6dbd0e37a8dd76c965ff3f1344f9b448b61911/memer_eval/memory.py)
- 가중치·학습 파라미터 — 먼지 닦기용 상위 기억 정책 Qwen3-VL · model-00001-of-00002.safetensors [배포 파일](https://huggingface.co/ajaysri/memer-dusting-qwen3vl-4b-step-1500/resolve/d7db9739abecb62d16dac532ddf244a56951c817/model-00001-of-00002.safetensors)
- 데이터 — 먼지 닦기 기술 주석이 있는 훈련 시연 · data/chunk-000/file-000.parquet [배포 파일](https://huggingface.co/datasets/ajaysri/dusting_train_50_v3_subtasks_rgb/resolve/392dfd68e81b0e2e6e451ba252a1a8597bb215d5/data/chunk-000/file-000.parquet)

## 판본과 출처

게재본이 사용한 상위 모델은 Qwen2.5-VL-7B-Instruct다. 현재 공개된 먼지 닦기용 상위 모델은 Qwen3-VL-4B다. [원문](https://proceedings.iclr.cc/paper_files/paper/2026/file/9da515b1ad19d032a7398f00f5ff9b0c-Paper-Conference.pdf)
