# Problem — OneTwoVLA: A Unified Vision-Language-Action Model with Adaptive Reasoning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-25 · §3.1, Algorithm 1, §4, Appendix F (hardware) 검토. [방법·평가 원문](https://arxiv.org/html/2505.11917) · [저자 코드](https://github.com/Fanqi-Lin/OneTwoVLA)

## 문제와 검증 범위

긴 작업 중 언제 현재 동작을 계속하고 언제 다시 추론할지를 결정해야 한다. 일정 주기로 외부 VLM에 계획을 요청하면 이 시점을 정책이 배우기 어렵다.

실물 장기 조작, 실패 감지·복구, 일반화 과제를 시험했다. Fig. 6의 장기 작업 비교는 과제당 20회이며 동일 데이터로 조정한 π0와 외부 계획기를 쓰는 비교군을 포함한다. [원문 및 평가 절](https://arxiv.org/html/2505.11917)
