# Scaling up Memory for Robotic Control via Experience Retrieval

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue
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
- Source audit: 2026-11-02 공식 proceedings/publisher의 서지·abstract와 저자 project/code 소개를 확인했다. 노트는 abstract/project 기반이며 본문 정독·native 실행을 뜻하지 않는다. 사용자 읽기 상태는 UNREAD 유지.

## Problem and Importance

긴 관측 이력을 모두 처리하는 비용과 무차별 subsampling의 정보 손실을 함께 다룬다.

## Core Idea and Contribution

상위 정책이 과거의 중요한 keyframe을 선택·추적하고 최근 관측과 함께 하위 정책용 지시를 만든다.

## Observation–State–Action Interface

이력 keyframe·현재 관측·task → 상위 언어 지시 → π0.5 하위 조작 정책. Episode 내 기억과 외부 시연 bank는 다른 정보원이다.

## Evaluation Scope

수분 동안의 기억이 필요한 실제 로봇 조작 과제 3개에서 비교한다. 프로젝트의 object search·counting·dust-and-replace는 task 설명이며 독립 재현 결과가 아니다.

근거: [공식 paper/abstract](https://proceedings.iclr.cc/paper_files/paper/2026/hash/9da515b1ad19d032a7398f00f5ff9b0c-Abstract-Conference.html) · [저자 project](https://jen-pan.github.io/memer/).

## Why This Paper Is Here — Researcher Interpretation

MemoryVLA와 계층 정책의 관계를 구체화하는 NEXT다. 외부 시연 검색과 실행 중 기억을 구분하고 SET의 counting 선행을 보완한다.

범위와 수치의 미확인 항목은 [평가 노트](./04_evaluation.md)에, 제안하는 반증 질문은 [insights](./05_insights.md)에 둔다.
