# Reactive Diffusion Policy: Slow-Fast Visual-Tactile Policy Learning for Contact-Rich Manipulation

- Year/Venue: 2025 / RSS
- Category: Manipulation, Contact, and Dexterity
- Tags: Robotics, Diffusion, tactile sensing, contact-rich manipulation, slow-fast control, Imitation Learning
- Official paper: https://www.roboticsproceedings.org/rss21/p052.html
- Official PDF: https://www.roboticsproceedings.org/rss21/p052.pdf
- Code/Project: https://reactive-diffusion-policy.github.io/
- Source audit: official abstract/proceedings reviewed on 2026-08-12; full text manual review required for exact implementation and numeric claims.

## Why This Paper Is Here

Diffusion action chunk와 high-frequency tactile feedback을 직접 연결하는 G-01의 필수 baseline.

## Problem

Visual imitation policy의 긴 action chunk는 complex trajectory를 표현하지만 chunk 실행 중 contact 변화에 즉시 반응하기 어렵다.

## Core Idea

- TactAR teleoperation으로 실시간 tactile feedback이 포함된 demonstration을 수집한다.
- 저주파 latent diffusion policy가 high-level action chunk를 예측한다.
- 고주파 asymmetric tokenizer가 tactile feedback을 이용해 chunk 내부 action을 수정한다.

## Observation / State / Action Interface

Vision은 느린 latent plan에, tactile signal은 빠른 closed-loop correction에 들어가는 dual-rate policy다.

## Evaluation Scope

- 공식 RSS abstract는 3개 contact-rich task와 서로 다른 tactile/force sensor 적용을 보고한다.
- Success 외에 reaction time, contact force와 sensor transfer를 확인해야 한다.

## Limitations to Verify

- Task와 sensor 수가 제한적이며 safety guarantee를 직접 제공하지 않는다.
- VLA semantic planner나 hybrid force-position controller와의 결합은 별도 문제다.

## Reading Lineage

`Diffusion Policy → Reactive Diffusion Policy → tactile/force-aware VLA executor`
