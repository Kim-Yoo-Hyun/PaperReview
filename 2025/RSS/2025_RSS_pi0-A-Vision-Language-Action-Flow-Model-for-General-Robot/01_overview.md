# π0: A Vision-Language-Action Flow Model for General Robot Control

> Evidence maturity: `UNREAD`. 아래 내용은 source cue와 사전 구조화이며, 정독 전에는 paper-supported conclusion으로 인용하지 않는다.

- Year/Venue: 2025 / RSS
- Category: VLA and Generalist Robot Policies
- Tags: Robotics, VLA, Flow Matching, generalist policy, cross-embodiment, dexterous manipulation
- Official paper: https://www.roboticsproceedings.org/rss21/p010.html
- Official PDF: https://www.roboticsproceedings.org/rss21/p010.pdf
- Code/Project: https://www.pi.website/research/pi0
- Source audit: official abstract/proceedings reviewed on 2026-08-12; full text manual review required for exact implementation and numeric claims.

## Why This Paper Is Here

π0.5와 FAST를 이해하기 위한 flow-matching VLA predecessor.

## Problem

다양한 robot embodiment와 dexterous task를 하나의 generalist policy로 다루면서 web-scale semantic prior를 continuous robot action으로 연결해야 한다.

## Core Idea

- Pretrained VLM 위에 flow-matching action expert를 결합한다.
- Single-arm, dual-arm, mobile manipulator의 다양한 data로 공동 학습한다.
- 직접 prompting, high-level VLM instruction, downstream fine-tuning을 하나의 generalist policy setting에서 다룬다.

## Observation / State / Action Interface

이미지·language·proprioception을 받아 연속 action chunk를 flow-matching 과정으로 생성한다. 실제 controller의 action convention과 rate는 embodiment별 adapter가 담당한다.

## Evaluation Scope

- 공식 RSS abstract는 laundry folding, table cleaning, box assembly 등 다양한 dexterous task와 여러 robot platform을 보고한다.
- Direct prompting, language following과 new-skill fine-tuning을 구분해 비교해야 한다.

## Limitations to Verify

- Cross-embodiment 성능이 data balance와 embodiment adapter 중 어디서 오는지 분리하기 어렵다.
- Action chunk 중 contact disturbance에 대한 고주파 feedback과 recovery는 별도 검증이 필요하다.

## Reading Lineage

`Flow Matching + pretrained VLM → π0 → FAST / π0.5`
