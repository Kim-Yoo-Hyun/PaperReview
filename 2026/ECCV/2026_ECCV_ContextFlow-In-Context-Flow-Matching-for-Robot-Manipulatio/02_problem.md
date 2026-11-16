# ContextFlow: In-Context Flow Matching for Robot Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

새 과제 적응을 위해 정책을 반복 fine-tuning하는 비용을 줄일 필요가 있다.

## Bottleneck and Changed Formulation

시연의 시각·proprioception·행동을 압축하는 perceiver와 in-context 조건부 flow matching을 결합한다.

## System and Robotics Loop

현재 관측과 demonstration context → continuous action flow; 새 context로 행동을 조건화한다.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

context 길이·선정 비용, 미관측 task 정의, bimanual action 정규화.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

LIBERO의 미관측 구성과 실제 단일팔·양팔 조작을 평가한다.

## Evidence Anchor

[공식 paper/abstract](https://link.springer.com/chapter/10.1007/978-3-032-37531-5_16) · [저자 project/code](https://dingjiansw101.github.io/contextflow-page/) · [공식 code](https://github.com/dingjiansw101/ContextFlow). Exact objective, constraints, success definition은 본문 수동 확인 필요.
