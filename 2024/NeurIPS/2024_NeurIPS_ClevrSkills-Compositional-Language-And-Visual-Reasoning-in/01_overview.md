# ClevrSkills: Compositional Language And Visual Reasoning in Robotics

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
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
- Source audit: 2026-11-01 공식 서지/abstract·project/code 소개 확인. NeurIPS 2024 Datasets and Benchmarks 공식 proceedings 확인. 신규 노트는 보수적으로 abstract/project 범위이며, 기존 SET의 지정 본문/code 감사는 별도 source ledger를 따른다. 정독·native 실행을 뜻하지 않는다.

## Problem and Importance

익힌 기본 조작 기술을 새로운 복합 지시로 조합할 수 있는지 평가한다.

## Core Idea and Contribution

ManiSkill2 기반 환경과 demonstration dataset, 단계별 조합 과제로 언어·시각 지시 이행을 비교한다.

## Observation–State–Action Interface

언어·시각 task prompt와 로봇 관측 → 조작 정책 → simulator predicate 평가. Dataset annotation과 정책에 허용되는 입력을 구분해야 한다.

## Evaluation Scope and Claim Boundary

기초 조작에서 복합 과제로 이어지는 세 수준의 curriculum에서 VLM 기반 baseline을 평가한다. 이 등록에서는 정확한 trial 수·성공률을 새로 확정하지 않는다.

근거: [공식 paper/abstract](https://proceedings.neurips.cc/paper_files/paper/2024/hash/439539557e9ba0d04055773ff1f3241c-Abstract-Datasets_and_Benchmarks_Track.html) · [저자 project/code](https://github.com/Qualcomm-AI-research/ClevrSkills). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

VIMA·VLABench와 함께 집합/수량 후보의 기존 조합 task와 평가 predicate를 이해할 NEXT benchmark다. 여러 물체 처리·나열 표현 자체를 새 기여로 삼지 않도록 등록한다.

## Verification Boundary

task 생성의 정답 정보와 자동 입력, 부분집합 허용 범위, release/contact predicate, 조합 split의 학습 support을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
