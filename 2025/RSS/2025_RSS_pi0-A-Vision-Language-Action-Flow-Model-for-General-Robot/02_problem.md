# Problem — π0: A Vision-Language-Action Flow Model for General Robot Control

> Evidence maturity: `UNREAD`. 아래 내용은 source cue와 사전 구조화이며, 정독 전에는 paper-supported conclusion으로 인용하지 않는다.

- Year/Venue: 2025 / RSS
- Category: VLA and Generalist Robot Policies
- Tags: Robotics, VLA, Flow Matching, generalist policy, cross-embodiment, dexterous manipulation
- Official paper: https://www.roboticsproceedings.org/rss21/p010.html
- Official PDF: https://www.roboticsproceedings.org/rss21/p010.pdf
- Code/Project: https://www.pi.website/research/pi0
- Source audit: official abstract/proceedings reviewed on 2026-08-12; full text manual review required for exact implementation and numeric claims.

## Target Problem

다양한 robot embodiment와 dexterous task를 하나의 generalist policy로 다루면서 web-scale semantic prior를 continuous robot action으로 연결해야 한다.

## Core Assumptions

- 대규모 heterogeneous robot data의 action space를 공통 policy interface로 정렬할 수 있다.
- 저주파 semantic backbone과 action expert의 분리가 task에 필요한 control bandwidth를 제공한다.

## Closed-Loop Position

이 논문은 현재 robotics loop에서 `Flow Matching + pretrained VLM → π0 → FAST / π0.5` 연결을 담당한다. 실제 정독 시 observation/state/action/control 중 어느 interface를 고정하고 어느 부분을 학습하는지 확인한다.

## Falsification Question

Cross-embodiment 성능이 data balance와 embodiment adapter 중 어디서 오는지 분리하기 어렵다.
