# Scaling Robot Policy Evaluation via Discrete Diffusion World Model

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

Action을 unified token으로 다루는 discrete diffusion과 keyframe memory·progress 출력을 결합한다.

LIBERO·RoboTwin 및 real-robot task 기반 평가를 보고한다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v306/li26hi.html) · [저자 project/code](https://dworldeval.github.io/). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 성공 평가기 독립성, 실패 데이터, final/preprint 차이은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

World-model 평가를 연구할 때 시각 품질과 행동별 순위 신뢰도를 구분할 직접 비교군이다.

### Dependency and Evolution

WorldEval/Ctrl-World → dWorldEval → native outcome과의 ranking 진단.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

동일 초기 관측에서 후보별 predicted/native 결과를 맞춰 false positive와 순위 오류를 센다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

같은 상태의 후보 행동 순위가 out-of-distribution action에서도 native 결과와 일치하는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
