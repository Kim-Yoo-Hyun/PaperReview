# Exploring the Limits of Combinatorial Generalization in Embodied Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

RoboCombine은 단계 순서에 맞는 성공과 단계 간 전환을 측정한다. HSE는 계획·전환·행동을 나누며 PRTI는 개별 기술의 시작 상태를 확장한다.

공개 저장소의 19개 조합 과제와 세 트랙을 확인했다. 초록에 보고된 PRTI 비교는 정답 전환 시각을 준 조건이다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2610.15425) · [저자 project/code](https://github.com/AutoLab-SAI-SJTU/RoboCombine). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 각 트랙의 정답 신호, 단계별 분모, 자세 초기화 비용은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

첫 조작 이후 실패를 해석할 때 하위 지시와 인계 자세를 통제한 직접 선행으로 참조한다.

### Dependency and Evolution

LADDER의 단계 수별 평가와 함께 보면 지시 분할과 앞 단계가 남긴 물리 상태의 영향을 구별할 수 있다.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

같은 두 기술에서 정답 전환과 동일 정책을 고정하고 앞 단계가 남긴 자세와 표준 시작 자세를 대조한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

다음 지시와 전환 시각을 고정했을 때 인계 자세 분포를 바꾸는 것만으로 순서 성공이 달라지는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
