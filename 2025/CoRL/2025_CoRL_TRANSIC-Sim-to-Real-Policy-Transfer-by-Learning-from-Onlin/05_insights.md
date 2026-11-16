# TRANSIC: Sim-to-Real Policy Transfer by Learning from Online Correction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

사람의 online correction으로 residual policy를 학습해 simulation 정책과 결합한다.

가구 조립 등 실로봇 접촉 조작의 sim-to-real 전이를 보고한다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v270/jiang25a.html) · [저자 project/code](https://transic-robot.github.io/) · [공식 code](https://github.com/transic-robot/transic). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 개입 시점/시간 비용, residual 제어 권한, correction과 평가 분할은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

새 RL/VLA 적응 기여를 주장하기 전에 인간 개입·residual 학습으로 설명되는 이득을 대조한다.

### Dependency and Evolution

Residual RL·SERL → TRANSIC; HIL-SERL과 intervention 방식 비교.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

base policy·개입 횟수·관측을 고정하고 residual과 단순 finetuning을 비교한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

같은 correction 예산에서 residual 결합이 전체 policy finetuning보다 안정적인가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
