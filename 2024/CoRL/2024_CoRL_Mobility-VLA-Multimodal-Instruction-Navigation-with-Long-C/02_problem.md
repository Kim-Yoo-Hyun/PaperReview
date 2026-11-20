# Mobility VLA: Multimodal Instruction Navigation with Long-Context VLMs and Topological Graphs

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

언어·이미지 지시를 이전 tour 영상과 연결해 실제 장소로 이동해야 한다.

## Bottleneck and Changed Formulation

장문맥 VLM의 goal-frame 선택과 topological graph 기반 하위 navigation을 결합한다.

## System and Robotics Loop

tour video·multimodal instruction → goal frame → graph/low-level policy → 이동 action.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

tour/graph 구축 비용, goal 후보 접근, online 관측과 planner timing.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

기록된 tour를 제공한 실환경의 multimodal instruction navigation을 평가한다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.mlr.press/v270/xu25b.html). Exact objective, constraints, success definition은 본문 수동 확인 필요.
