# ClevrSkills: Compositional Language And Visual Reasoning in Robotics

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2024 / NeurIPS
- Authors: Sanjay Haresh, Daniel Dijkman, Apratim Bhattacharyya, Roland Memisevic
- Category: Benchmarks and Datasets
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: Robotics, compositional-reasoning, Benchmark, multimodal-instructions
- Aliases: ClevrSkills
- Official paper: https://proceedings.neurips.cc/paper_files/paper/2024/hash/439539557e9ba0d04055773ff1f3241c-Abstract-Datasets_and_Benchmarks_Track.html
- Venue verification: https://proceedings.neurips.cc/paper_files/paper/2024/hash/439539557e9ba0d04055773ff1f3241c-Abstract-Datasets_and_Benchmarks_Track.html
- Code/Project: https://github.com/Qualcomm-AI-research/ClevrSkills
- Code: https://github.com/Qualcomm-AI-research/ClevrSkills
- Source audit: 2026-11-01 공식 서지/abstract·project/code 소개 확인. NeurIPS 2024 Datasets and Benchmarks 공식 proceedings 확인. 신규 노트는 보수적으로 abstract/project 범위이며, 기존 SET의 지정 본문/code 감사는 별도 source ledger를 따른다. 정독·native 실행을 뜻하지 않는다. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

ClevrSkills는 배운 기초 동작을 새로운 순서나 조합으로 재사용하는 조작 정책의 능력을 평가한다. [PDF 1쪽](https://proceedings.neurips.cc/paper_files/paper/2024/file/439539557e9ba0d04055773ff1f3241c-Paper-Datasets_and_Benchmarks_Track.pdf#page=1)

## Core Idea and Contribution

- ManiSkill2에서 시각·언어 지시, 전문가 궤적, 세 단계의 조합 난도를 갖춘 시뮬레이션 과제를 구성했다. [PDF 3쪽](https://proceedings.neurips.cc/paper_files/paper/2024/file/439539557e9ba0d04055773ff1f3241c-Paper-Datasets_and_Benchmarks_Track.pdf#page=3) · [PDF 4쪽](https://proceedings.neurips.cc/paper_files/paper/2024/file/439539557e9ba0d04055773ff1f3241c-Paper-Datasets_and_Benchmarks_Track.pdf#page=4) · [PDF 5쪽](https://proceedings.neurips.cc/paper_files/paper/2024/file/439539557e9ba0d04055773ff1f3241c-Paper-Datasets_and_Benchmarks_Track.pdf#page=5)
- 모방 정책을 학습한 뒤 익숙한 과제와 보지 못한 조합에 평가해 개별 동작을 배우고도 새 조합에서 실패하는 조건을 보였다. [PDF 8쪽](https://proceedings.neurips.cc/paper_files/paper/2024/file/439539557e9ba0d04055773ff1f3241c-Paper-Datasets_and_Benchmarks_Track.pdf#page=8) · [PDF 9쪽](https://proceedings.neurips.cc/paper_files/paper/2024/file/439539557e9ba0d04055773ff1f3241c-Paper-Datasets_and_Benchmarks_Track.pdf#page=9)

## Observation–State–Action Interface

언어·시각 task prompt와 로봇 관측 → 조작 정책 → simulator predicate 평가. Dataset annotation과 정책에 허용되는 입력을 구분해야 한다.

## Evaluation Scope and Claim Boundary

기초 조작에서 복합 과제로 이어지는 세 수준의 curriculum에서 VLM 기반 baseline을 평가한다. 이 등록에서는 정확한 trial 수·성공률을 새로 확정하지 않는다.

근거: [공식 paper/abstract](https://proceedings.neurips.cc/paper_files/paper/2024/hash/439539557e9ba0d04055773ff1f3241c-Abstract-Datasets_and_Benchmarks_Track.html) · [저자 project/code](https://github.com/Qualcomm-AI-research/ClevrSkills). 문장에 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

VIMA·VLABench와 함께 집합/수량 후보의 기존 조합 task와 평가 predicate를 이해할 NEXT benchmark다. 여러 물체 처리·나열 표현 자체를 새 기여로 삼지 않도록 등록한다.

## Verification Boundary

task 생성의 정답 정보와 자동 입력, 부분집합 허용 범위, release/contact predicate, 조합 split의 학습 support을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
