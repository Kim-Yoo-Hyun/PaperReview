# RoboFollow: Unveiling the Instruction Following Mirage in Embodied Agents

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

같은 scene의 여러 지시 등으로 instruction following을 단계별 평가한다.

Simulation benchmark와 제한된 실제 검증을 보고한다.

근거: [공식 paper/abstract](https://openreview.net/forum?id=A9AQjk3dAt) · [저자 project/code](https://github.com/AutoLab-SAI-SJTU/RoboFollow). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 scene entropy, evaluator oracle, task infeasibility, real-robot coverage은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

C2/D3의 instruction switch와 성공 지표를 검증할 핵심 benchmark다.

### Dependency and Evolution

LIBERO·instruction diagnostics → RoboFollow.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

동일 scene·task 능력에서 지시만 바꿔 순응·실행 성공을 별도 측정한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

기본 skill competence를 통제한 뒤에도 지시 변화 실패가 남는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
