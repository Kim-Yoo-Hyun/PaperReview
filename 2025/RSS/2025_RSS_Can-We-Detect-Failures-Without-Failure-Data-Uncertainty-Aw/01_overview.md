# Can We Detect Failures Without Failure Data? Uncertainty-Aware Runtime Failure Detection for Imitation Learning Policies

- Year/Venue: 2025 / RSS
- Category: World Models, Safety, and Recovery
- Tags: Robotics, failure detection, uncertainty, conformal prediction, Imitation Learning, runtime monitoring
- Official paper: https://www.roboticsproceedings.org/rss21/p073.html
- Official PDF: https://www.roboticsproceedings.org/rss21/p073.pdf
- Code/Project: https://cxu-tri.github.io/FAIL-Detect-Website/
- Source audit: official abstract/proceedings reviewed on 2026-08-12; full text manual review required for exact implementation and numeric claims.

## Why This Paper Is Here

Known failure data 없이 runtime policy failure를 탐지하는 SAFE 이전/병렬의 직접 비교점.

## Problem

실제 deployment failure는 다양하고 사전에 수집하기 어려워 failure-supervised detector의 확장성이 낮다.

## Core Idea

- Policy input/output을 failure와 상관된 scalar signal로 distill한다.
- Sequential OOD detection으로 failure onset을 찾는다.
- Conformal prediction으로 uncertainty를 calibration하고 learned flow-based density signal도 비교한다.

## Observation / State / Action Interface

기존 imitation policy를 바꾸지 않는 modular runtime monitor이며 출력은 시간별 failure score와 alarm이다.

## Evaluation Scope

- 공식 RSS abstract는 다양한 robot manipulation task에서 learned/post-hoc signal과 failure-detection baseline을 비교한다고 보고한다.
- Accuracy뿐 아니라 detection delay와 false alarm을 함께 기록해야 한다.

## Limitations to Verify

- Failure detection이 recovery action 선택까지 해결하지 않는다.
- Conformal guarantee가 sequential distribution shift와 closed-loop intervention 뒤에도 그대로 유지되는지 확인해야 한다.

## Reading Lineage

`Policy uncertainty / OOD detection → FAIL-Detect / SAFE → typed recovery`
