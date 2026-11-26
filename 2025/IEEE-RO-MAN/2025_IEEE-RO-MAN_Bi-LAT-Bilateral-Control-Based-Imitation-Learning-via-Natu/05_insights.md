# Insights — Bi-LAT: Bilateral Control-Based Imitation Learning via Natural Language and Action Chunking with Transformers

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-25 · §III-D/E, §IV–V, Tables I–II 검토. [방법·평가 원문](https://arxiv.org/html/2504.01301)

## Paper-supported conclusion

ResNet-18 영상 특징, 언어 임베딩, follower 관절 상태를 조건으로 ACT 계열 Transformer CVAE가 미래 leader 관절각·각속도·토크 청크를 회귀한다. 양방향 원격조작 시연이 세 변수의 교사 신호를 제공한다. [원문 및 평가 절](https://arxiv.org/html/2504.01301)

## Researcher interpretation

ACT의 청크에 관절 토크를 실제 실행 참조로 담은 비교점이다. 종이컵과 스펀지의 힘 수식어가 바꾼 행동을 접촉 구간에서 확인할 수 있다.

## 최소 비교 실험

같은 컵, 같은 시연, 같은 양방향 제어 이득에서 토크 참조만 두 지시 사이에 바꾼다. 집기 성공과 변형량이 함께 달라지는지 확인한다.

## 검증 질문

언어가 바꾼 토크가 실행 결과에 얼마나 기여했는지는 위치·속도 참조까지 맞춘 토크 채널 절제로 검증할 수 있다.
