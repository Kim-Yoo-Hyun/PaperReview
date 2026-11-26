# OneTwoVLA: A Unified Vision-Language-Action Model with Adaptive Reasoning

> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-25 · §3.1, Algorithm 1, §4, Appendix F (hardware) 검토. [방법·평가 원문](https://arxiv.org/html/2505.11917) · [저자 코드](https://github.com/Fanqi-Lin/OneTwoVLA)

- Year/Venue: 2026 / ICLR
- Authors: Fanqi Lin, Ruiqian Nai, Yingdong Hu, Jiacheng You, Junming Zhao, Yang Gao
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, mode switching, task decomposition, Flow Matching, long-horizon manipulation
- Official paper: https://proceedings.iclr.cc/paper_files/paper/2026/hash/ebfabf372037aaa4a8d92c9b457ece3e-Abstract-Conference.html
- Code/Project: https://one-two-vla.github.io/

## 연구 질문과 기여

긴 작업 중 언제 현재 동작을 계속하고 언제 다시 추론할지를 결정해야 한다. 일정 주기로 외부 VLM에 계획을 요청하면 이 시점을 정책이 배우기 어렵다.

같은 모델이 [BOR]와 [BOA] 중 하나를 먼저 생성한다. 전자에서는 텍스트로 계획·상태를 갱신하고 후자에서는 π0의 flow-matching 전문가로 행동 청크를 낸다.

## 정책 출력

다중 카메라, 지시, 직전 추론과 참조 영상에서 모드를 고른다. 실물 단팔은 끝단 자세와 그리퍼 폭 7차원, 양팔은 14차원이다. 양팔 플랫폼의 베이스와 리프트는 평가에 쓰지 않았다. [방법 원문](https://arxiv.org/html/2505.11917)

## 평가 범위

실물 장기 조작, 실패 감지·복구, 일반화 과제를 시험했다. Fig. 6의 장기 작업 비교는 과제당 20회이며 동일 데이터로 조정한 π0와 외부 계획기를 쓰는 비교군을 포함한다. [원문 및 평가 절](https://arxiv.org/html/2505.11917)

## 선정 근거

상위 추론과 연속 행동 전문가가 한 정책 안에서 모드를 교대하는 사례다. π0.5의 하위 지시 재예측과 달리 추론할 시점 자체가 학습 대상이다.
