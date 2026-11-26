# Insights — When to Act, Ask, or Learn: Uncertainty-Aware Policy Steering

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-26 서지와 RSS 게재본 PDF 2–8쪽에서 의사결정과 배포 결과 대조. Full-text scope의 수치·조건만 기록했다.

## Paper-supported conclusion

VLM의 평가와 정책의 행동 후보에 conformal prediction을 적용한다. 실행, 지시 확인 질문, 행동 개입 요청을 구분하고, 수집한 개입으로 잔차를 학습한다. [원문 및 평가 절](https://roboticsproceedings.org/rss22/p142.pdf#page=8)

## Researcher interpretation

실패 원인에 따라 재관측, 사용자 질문, 수정 시연에 예산을 나누는 연구에서 직접 비교할 수 있다.

- KnowNo의 언어 수준 불확실성 처리와 제안 선택지를 비교한다. [pr-0706 · 원문](https://roboticsproceedings.org/rss22/p142.pdf#page=3)
- 실험의 저수준 행동 후보를 내는 기준선으로 Diffusion Policy를 사용한다. [pr-0019 · 원문](https://roboticsproceedings.org/rss22/p142.pdf#page=6)

## 최소 비교 실험

같은 상태에서 목표만 모호하게 만든 경우와 정책의 유효 후보를 없앤 경우를 분리해 개입 선택 오류를 비교한다.
