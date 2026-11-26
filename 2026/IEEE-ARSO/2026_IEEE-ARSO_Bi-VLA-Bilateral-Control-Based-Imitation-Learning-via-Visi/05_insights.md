# Insights — Bi-VLA: Bilateral Control-Based Imitation Learning via Vision-Language Fusion for Action Generation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-25 · §III, §IV, Tables II–IV 검토. [방법·평가 원문](https://arxiv.org/html/2509.18865)

## Paper-supported conclusion

천장·그리퍼 RGB와 언어를 FiLM으로 결합하고 follower 관절 상태와 함께 Transformer CVAE에 넣는다. SigLIP와 DistilBERT를 사용한 변형을 비교한다. [원문 및 평가 절](https://arxiv.org/html/2509.18865)

## Researcher interpretation

Bi-LAT의 운동·토크 인터페이스에서 시각과 언어의 결합 방식을 바꿨다. 단순히 토크를 학습 보조량으로 예측한 연구와 구별할 직접 선행이다.

## 최소 비교 실험

초기 영상을 고정하고 목적지 지시만 바꾼 뒤, 선택한 목적지와 놓기 단계의 성공을 각각 집계한다.

## 검증 질문

새 출발지와 목적지 조합에서 언어 분기 오류와 내려놓을 때의 접촉 오류를 따로 측정하면 두 개선을 구별할 수 있다.
