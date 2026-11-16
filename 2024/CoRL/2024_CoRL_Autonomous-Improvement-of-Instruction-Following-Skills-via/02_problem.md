# Autonomous Improvement of Instruction Following Skills via Foundation Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

로봇이 자율 수집한 비최적 경험을 사람의 추가 언어 주석 없이 instruction-following 개선에 활용해야 한다.

## Bottleneck and Changed Formulation

VLM으로 의미 있는 경험의 수집·평가를 돕고 언어 조건 이미지 목표 생성과 goal-reaching 정책을 분리하여 자율 데이터로 학습한다.

## System and Robotics Loop

언어 → image subgoal → goal-conditioned robot action. 학습 데이터 수집/평가와 배포 정책의 역할을 분리한다.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

수집 scene과 평가 scene의 분리, 데이터 release의 실제 접근성, 의미 이해와 운동 능력 개선의 기여, 서로 다른 정책 정보량.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

공식 abstract는 새로운 실세계 환경의 정책 개선과 5개 tabletop 환경에서 수집한 25K trajectory 데이터 공개를 설명한다. Project는 9개 평가 scene을 설명하므로 두 숫자의 분모를 합치지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://proceedings.mlr.press/v270/zhou25b.html) · [저자 project/code](https://soar-autonomous-improvement.github.io/) · [공식 code](https://github.com/soar-autonomous-improvement/code-release). Exact objective, constraints, success definition은 본문 수동 확인 필요.
