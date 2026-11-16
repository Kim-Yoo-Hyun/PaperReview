# Ψ₀: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Source audit: 2026-11-16: RSS metadata·공식 project/code 및 arXiv v1 §III–IV, Appendix IX–X의 지정 내용 확인. RSS 최종본문 전체 대조·사용자 정독·실험을 의미하지 않는다.
> Canonical metadata: [01_overview.md](./01_overview.md).

## Paper-supported Conclusion

단계별 표현/행동 학습과 humanoid 데이터 recipe가 실물 이동 조작에 유효하다는 저자 비교 결과다. 평가 범위와 보조 개입은 [04_evaluation](./04_evaluation.md)을 따른다. [원문](https://arxiv.org/html/2603.12263v1).

## Researcher Interpretation

- 새로 비교할 축은 데이터 품질·표현·학습 단계이며, RL 제어기를 연결한 것 자체가 새 연구 공백은 아니다.
- 강한 가정은 task-space 정렬과 하위 controller competence다. 동일 관측에서도 지시 선택 실패와 실행 불가능성을 구별해야 한다.
- π₀/flow 정책·FAST를 출발점으로 EgoDex/HE 데이터와 AMO/SONIC 제어를 함께 읽는다. 이는 읽기 연결이며 모두 직접 인용 계보라는 뜻은 아니다.

## Minimal Reproduction and Falsifiable Question

고정 데이터·action interface·controller·물리 시간에서 VLM freeze/unfreeze와 supervised/RL update를 비교한다. 질문: reward update가 지시별 행동 구별을 유지하면서 실패 복구를 개선하는가? 데이터량·controller 변경만으로 이득이 설명되면 독립 학습 기여를 주장하지 않는다.

이 비교는 제안이며 미실행이다. 기존 UNIFIED/LANGRET 후보의 gate·우선순위는 유지한다. 공개 checkpoint마다 학습 recipe가 달라 우선 버전 동등성을 확인해야 한다.
