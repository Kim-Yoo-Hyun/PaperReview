# Scaling up Memory for Robotic Control via Experience Retrieval

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract/project 기반 — 본문 수동 확인 필요.
> Source audit: 2026-11-02 공식 서지·abstract 및 저자 소개 확인. 실제 정독·코드 실행을 뜻하지 않는다.

## Target Problem and Bottleneck

긴 관측 이력을 모두 처리하는 비용과 무차별 subsampling의 정보 손실을 함께 다룬다.

## Changed Formulation

[방법](./03_method.md)의 입력과 학습/배포 개입을 구분해 선행과 비교한다. 단순 성공률 향상보다 어떤 정보가 언제 추가되는지가 비교의 기준이다.

## Assumptions to Verify — Researcher Interpretation

선택 supervision·실패 후 이력 분포·최근 frame 예산. 공식 proceedings는 Qwen 7B, project는 3B로 표기하므로 backbone 크기는 version 확인 필요.

이는 본문에서 확인할 질문이며 논문이 직접 인정한 실패 목록이 아니다.

## Position in the Robotics Loop

이력 keyframe·현재 관측·task → 상위 언어 지시 → π0.5 하위 조작 정책. Episode 내 기억과 외부 시연 bank는 다른 정보원이다.

정확한 sensor·state·action frame 및 controller 경계는 본문 확인 전 확정하지 않는다.

근거: [공식 paper/abstract](https://proceedings.iclr.cc/paper_files/paper/2026/hash/9da515b1ad19d032a7398f00f5ff9b0c-Abstract-Conference.html) · [저자 project](https://jen-pan.github.io/memer/).
