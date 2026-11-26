# Bi-LAT: Bilateral Control-Based Imitation Learning via Natural Language and Action Chunking with Transformers

> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-25 · §III-D/E, §IV–V, Tables I–II 검토. [방법·평가 원문](https://arxiv.org/html/2504.01301)

- Year/Venue: 2025 / IEEE RO-MAN
- Authors: Takumi Kobayashi, Masato Kobayashi, Thanpimon Buamanee, Yuki Uranishi
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: REFERENCE
- Tags: VLA, bilateral control, joint torque, joint velocity, bimanual manipulation
- Official paper: https://ieeexplore.ieee.org/document/11217852
- Code/Project: https://mertcookimg.github.io/bi-lat/

## 연구 질문과 기여

컵을 집는 경로가 같아도 ‘부드럽게’와 ‘세게’는 다른 관절 토크를 요구한다. 위치 시연만으로는 이 차이를 재생하기 어렵다.

ResNet-18 영상 특징, 언어 임베딩, follower 관절 상태를 조건으로 ACT 계열 Transformer CVAE가 미래 leader 관절각·각속도·토크 청크를 회귀한다. 양방향 원격조작 시연이 세 변수의 교사 신호를 제공한다.

## 정책 출력

영상·언어·follower의 (q, q̇, τ)에서 leader의 (q*, q̇*, τ*)를 예측한다. 배포 시 양방향 제어식이 이 예측과 follower 상태를 결합해 모터 전류를 계산한다. 1 kHz는 양방향 제어 루프의 주기다. [방법 원문](https://arxiv.org/html/2504.01301)

## 평가 범위

OpenManipulator-X 단팔의 종이컵 쌓기와 ALPHA-α 양팔의 스펀지 비틀기를 실물에서 시험했다. 단계별 성공과 물체를 잡거나 비트는 동안의 토크 분포를 비교했다. [원문 및 평가 절](https://arxiv.org/html/2504.01301)

## 선정 근거

ACT의 청크에 관절 토크를 실제 실행 참조로 담은 비교점이다. 종이컵과 스펀지의 힘 수식어가 바꾼 행동을 접촉 구간에서 확인할 수 있다.
