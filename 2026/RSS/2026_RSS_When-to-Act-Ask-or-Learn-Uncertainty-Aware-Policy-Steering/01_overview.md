# When to Act, Ask, or Learn: Uncertainty-Aware Policy Steering

> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-26 서지와 RSS 게재본 PDF 2–8쪽에서 의사결정과 배포 결과 대조. Full-text scope의 수치·조건만 기록했다.

- Year/Venue: 2026 / RSS
- Authors: Jessie Yuan, Yilin Wu, Andrea Bajcsy
- Primary track: World models, safety, uncertainty, and recovery
- Tier: REFERENCE
- Tags: conformal prediction, uncertainty estimation, policy steering, human intervention, residual learning
- Official paper: https://roboticsproceedings.org/rss22/p142.html
- Code/Project: https://jessie-yuan.github.io/ups/
- Code: https://github.com/CMU-IntentLab/uncertainty_aware_policy_steering

## 연구 질문과 기여

언어 지시의 모호함과 기본 정책이 행동을 생성하지 못하는 상황에는 서로 다른 피드백이 필요하다.

VLM의 평가와 정책의 행동 후보에 conformal prediction을 적용한다. 실행, 지시 확인 질문, 행동 개입 요청을 구분하고, 수집한 개입으로 잔차를 학습한다.

## 평가 범위

모의·실물 집기와 배치를 통해 모호함과 실행 불능을 각각 평가하고, 미보정 기준 및 개입 방식과 비교했다. [원문 및 평가 절](https://roboticsproceedings.org/rss22/p142.pdf#page=8)

## 선정 근거

실패 원인에 따라 재관측, 사용자 질문, 수정 시연에 예산을 나누는 연구에서 직접 비교할 수 있다.
