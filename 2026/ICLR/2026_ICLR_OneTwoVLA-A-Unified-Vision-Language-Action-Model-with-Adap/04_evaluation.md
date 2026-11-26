# Evaluation — OneTwoVLA: A Unified Vision-Language-Action Model with Adaptive Reasoning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-25 · §3.1, Algorithm 1, §4, Appendix F (hardware) 검토. [방법·평가 원문](https://arxiv.org/html/2505.11917) · [저자 코드](https://github.com/Fanqi-Lin/OneTwoVLA)

## 평가 조건

실물 장기 조작, 실패 감지·복구, 일반화 과제를 시험했다. Fig. 6의 장기 작업 비교는 과제당 20회이며 동일 데이터로 조정한 π0와 외부 계획기를 쓰는 비교군을 포함한다. [원문 및 평가 절](https://arxiv.org/html/2505.11917)

## 해석할 때 확인할 조건

추론 호출 빈도를 맞췄을 때도 사건에 맞춘 모드 전환이 긴 작업의 실패 후 복구에 이득을 주는지 따로 비교할 수 있다.
