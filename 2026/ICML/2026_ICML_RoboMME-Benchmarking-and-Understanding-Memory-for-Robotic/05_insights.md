# RoboMME: Benchmarking and Understanding Memory for Robotic Generalist Policies

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

Temporal·spatial·object·procedural memory task와 여러 memory-augmented VLA를 비교한다.

16 manipulation task와 14 memory variant를 보고하며 memory 효용은 task에 의존한다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v306/dai26c.html) · [저자 project/code](https://robomme.github.io/) · [공식 code](https://github.com/RoboMME/robomme_benchmark). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 task dictionary와 goal/evaluator, history cutoff, raw ID와 split은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

현재 GAP-N1–N3의 직접 benchmark이며 memory 필요성과 단순 정보 누설을 구분하는 기준이다.

### Dependency and Evolution

π0.5 → RoboMME → 관측/목표를 맞춘 proxy 데이터 전이 진단.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

먼저 3개 planned fixture의 native 관측·goal 일치를 확인한다. 기존 N3-A 계약 PASS는 native 재현이 아니다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

이 노트의 paper 재현은 미실행이다. 저장소의 별도 [GAP-N3-A 계약 검사](https://github.com/Kim-Yoo-Hyun/PaperReview/blob/8303fdd74fedbd456c0ab94230bde5cfd64c40ba/work/experiments/proxy_observation_contract/README.md)는 source/합성 17/17 PASS이며 RoboMME native 재현이 아니다. [N3-B 환경 설정](https://github.com/Kim-Yoo-Hyun/PaperReview/blob/8303fdd74fedbd456c0ab94230bde5cfd64c40ba/work/experiments/proxy_observation_contract/README.md#native-environment)과 실제 관측 일치 검증이 남아 있다.

### Research Gap and Falsifiable Question

Policy가 보는 history를 동일하게 유지할 때 selector의 cue 누락이 subset 효용을 바꾸는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
