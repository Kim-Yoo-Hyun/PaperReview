# AC2-VLA: Action-Context-Aware Adaptive Computation in Vision-Language-Action Models for Efficient Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED` — 초록·명시한 project 근거. 전체 본문·구현 정독 및 사용자 읽기 완료가 아니다.

## Paper-supported conclusion

영상·지시·이전 행동 context로 cache 재사용·token pruning·layer 실행을 조절하고 action-guided distillation으로 학습한다.

Robotic manipulation benchmark에서 계산량·속도와 성공을 비교한다. 초록만으로 real-robot trial 조건은 확정하지 않는다.

근거: [공식 paper/abstract](https://ijcai.org/proceedings/2026/228). 초록의 주장 범위이며 독립 재현 결과가 아니다.

## Researcher interpretation

### Why This Matters

RL 기반 시간 적응과 비교할 학습된 계산 절감 baseline이며 지연·feedback·성능의 비용 분리를 돕는다.

### Dependency and Evolution

OpenVLA/CogACT·추론 가속 → AC2-VLA → real-time RL의 강한 비-RL 계산 대안.

이는 개념적 읽기 연결이며 직접 citation 또는 검증된 derivation을 뜻하지 않는다.

### Assumptions and Failure Questions

관측 age·cache invalidation·학습 추가 비용·FLOPs와 실측 latency.

논문이 실제 보고한 failure case로 간주하지 않는다.

### Minimal Comparison

같은 hardware·관측 age에서 dense·adaptive compute·real-time RL의 성공/지연을 비교한다.

### Falsifiable Question

계산 절감의 이득은 실제 wall-clock feedback을 맞추면 RL 시간 적응과 어떻게 달라지는가?

같은 정보·데이터·계산 조건에서 단순 대안이 차이를 설명하면 해당 확장 가설을 수정한다. 공식 초록과 metadata 수준의 정리다. 구체적 실험 조건·수치·본문 한계는 추가 확인이 필요하다.
