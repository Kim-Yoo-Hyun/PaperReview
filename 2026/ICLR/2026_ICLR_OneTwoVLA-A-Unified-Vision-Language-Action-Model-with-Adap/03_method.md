# Method — OneTwoVLA: A Unified Vision-Language-Action Model with Adaptive Reasoning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-25 · §3.1, Algorithm 1, §4, Appendix F (hardware) 검토. [방법·평가 원문](https://arxiv.org/html/2505.11917) · [저자 코드](https://github.com/Fanqi-Lin/OneTwoVLA)

## 관측과 출력

다중 카메라, 지시, 직전 추론과 참조 영상에서 모드를 고른다. 실물 단팔은 끝단 자세와 그리퍼 폭 7차원, 양팔은 14차원이다. 양팔 플랫폼의 베이스와 리프트는 평가에 쓰지 않았다.

## 학습·실행 방법

같은 모델이 [BOR]와 [BOA] 중 하나를 먼저 생성한다. 전자에서는 텍스트로 계획·상태를 갱신하고 후자에서는 π0의 flow-matching 전문가로 행동 청크를 낸다.

- π0를 기본 VLA로 사용하고 연속 행동 전문가의 flow-matching 손실을 계승한다. §3.1. [pr-0746 · 원문](https://arxiv.org/html/2505.11917)
