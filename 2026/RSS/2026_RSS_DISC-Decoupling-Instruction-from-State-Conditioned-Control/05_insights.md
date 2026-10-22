# DISC: Decoupling Instruction from State-Conditioned Control via Policy Generation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

Instruction-only hypernetwork가 task-specific visuomotor policy의 파라미터를 생성한다.

LIBERO-90, Meta-World 및 동일 visual context의 실제 로봇 비교를 보고한다.

근거: [공식 paper/abstract](https://www.roboticsproceedings.org/rss22/p147.html) · [저자 project/code](https://github.com/ReNginx/DISC). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 generated parameter 수, training budget, 동일 장면 통제은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

OpenVLA 이후 language-conditioned 행동 여부를 확인할 직접 비교군이므로 NEXT다.

### Dependency and Evolution

RT-1/OpenVLA의 language-conditioned policy → DISC의 instruction-to-weights 방식; Hi Robot의 계층적 task 분해와 비교한다.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

장면을 고정하고 목표 지시만 바꾸는 paired evaluation을 한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

같은 scene의 서로 다른 지시에서 행동 차이가 유지되는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
