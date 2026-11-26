# Method — Bi-VLA: Bilateral Control-Based Imitation Learning via Vision-Language Fusion for Action Generation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-25 · §III, §IV, Tables II–IV 검토. [방법·평가 원문](https://arxiv.org/html/2509.18865)

## 관측과 출력

다섯 관절의 leader 각도·각속도·토크를 함께 예측해 한 시점당 15개 참조값을 낸다. 4채널 양방향 제어기가 참조를 follower의 전류 명령으로 변환한다.

## 학습·실행 방법

천장·그리퍼 RGB와 언어를 FiLM으로 결합하고 follower 관절 상태와 함께 Transformer CVAE에 넣는다. SigLIP와 DistilBERT를 사용한 변형을 비교한다.
