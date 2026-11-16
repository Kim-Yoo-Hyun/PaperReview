# Diagnosing Compositional Generalization in Sequential Robot Tasks

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

지시 marginal·지시 조합·context–action 변화를 분리하고, 데이터 coverage와 단계별 정책을 비교한다.

Pick-and-place, 후속 버튼 조작, 의존적인 두 단계 조작에서 coverage와 분해를 비교한다. 저자 공개 code는 개선된 pipeline이라 release 결과와 논문 결과가 다를 수 있다고 명시한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2607.29687) · [저자 project/code](https://yixiaowang7.github.io/Diagnosing_Compositional_Generalization_Robot_Page/) · [공식 code](https://github.com/YixiaoWang7/Diagnosing_Compositional_Generalization_Robot). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 v1/v2 차이, 단계별 정책의 입력과 전환 신호, 종속 지시의 정보 병목, demonstration 예산, 공개 release와 논문 설정의 차이은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

DataMIL·ReMix의 데이터 선택 흐름과 SET의 단순 분해를 연결할 instruction-coverage 선행이다. 분해 자체를 신규 기여로 주장하지 않고 학습 support를 따질 NEXT로 등록한다.

### Dependency and Evolution

Imitation learning의 데이터 구성 → 지시 공간 coverage → 조합 평가라는 비교 경로다. Spa-Bench의 실제 공간 진단과 별도로 읽는다..

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

논문의 coverage split과 공개 release 차이를 먼저 확인하고 동일 demonstration 예산·정보 조건을 고정한다. 현재 SET의 D/R 비교를 이 논문의 재현이라고 부르지 않는다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

복합 지시를 분해한 이득이 다음 단계에 필요한 문맥을 잃거나 학습 coverage가 달라진 효과와 구별되는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
