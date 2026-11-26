# Method — Bi-LAT: Bilateral Control-Based Imitation Learning via Natural Language and Action Chunking with Transformers

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-25 · §III-D/E, §IV–V, Tables I–II 검토. [방법·평가 원문](https://arxiv.org/html/2504.01301)

## 관측과 출력

영상·언어·follower의 (q, q̇, τ)에서 leader의 (q*, q̇*, τ*)를 예측한다. 배포 시 양방향 제어식이 이 예측과 follower 상태를 결합해 모터 전류를 계산한다. 1 kHz는 양방향 제어 루프의 주기다.

## 학습·실행 방법

ResNet-18 영상 특징, 언어 임베딩, follower 관절 상태를 조건으로 ACT 계열 Transformer CVAE가 미래 leader 관절각·각속도·토크 청크를 회귀한다. 양방향 원격조작 시연이 세 변수의 교사 신호를 제공한다.
