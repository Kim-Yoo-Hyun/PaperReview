# StreamVLN: Streaming Vision-and-Language Navigation via SlowFast Context Modeling

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

긴 navigation video history를 처리하면서 action generation의 latency와 context 크기를 제한하는 문제다.

## Bottleneck and Changed Formulation

Fast streaming dialogue context와 slow-updating memory를 결합하고 3D-aware token pruning으로 history를 압축한다.

## System and Robotics Loop

Interleaved vision/language/action stream → bounded context memory → navigation action.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

3D pruning에 필요한 입력, KV-cache 갱신, 실제 sensor/controller 지연.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

저자 공식 project는 VLN-CE benchmark와 여러 실제 환경의 장기 navigation을 설명한다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2507.05240) · [저자 project/code](https://streamvln.github.io/). Exact objective, constraints, success definition은 본문 수동 확인 필요.
