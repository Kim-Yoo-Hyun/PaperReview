# Adaptive Action Chunking at Inference-time for Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

Action entropy를 이용해 추론 중 실행할 chunk 길이를 조정한다.

Simulation과 real-robot manipulation 비교를 보고한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2604.04161) · [저자 project/code](https://lance-lot.github.io/adaptive-chunking.github.io/). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 entropy 추정 sample 수, 최소 이동량, sensor/inference timing은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

E2의 adaptive horizon 주장에 대한 직접 baseline이다.

### Dependency and Evolution

ACT·Diffusion Policy → RTC → AAC.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

고정/적응 horizon을 동일 wall-clock·관측 예산·controller에서 비교한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

추가 sampling·관측 비용을 맞춘 뒤에도 적응형 horizon 이득이 남는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
