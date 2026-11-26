# Method — When to Act, Ask, or Learn: Uncertainty-Aware Policy Steering

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-26 서지와 RSS 게재본 PDF 2–8쪽에서 의사결정과 배포 결과 대조. Full-text scope의 수치·조건만 기록했다.

## 관측과 출력

지시와 관측, 동결한 확산 정책의 행동 후보를 받아 삼중 선택지 중 하나를 출력한다.

## 학습·실행 방법

VLM의 평가와 정책의 행동 후보에 conformal prediction을 적용한다. 실행, 지시 확인 질문, 행동 개입 요청을 구분하고, 수집한 개입으로 잔차를 학습한다.

- KnowNo의 언어 수준 불확실성 처리와 제안 선택지를 비교한다. [pr-0706 · 원문](https://roboticsproceedings.org/rss22/p142.pdf#page=3)
- 실험의 저수준 행동 후보를 내는 기준선으로 Diffusion Policy를 사용한다. [pr-0019 · 원문](https://roboticsproceedings.org/rss22/p142.pdf#page=6)
