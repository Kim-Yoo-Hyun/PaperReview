# ContactBench 1.0: A Benchmark for Everyday Contact-Rich Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

접촉 skill taxonomy와 제작 가능한 물체·대응 simulation asset을 제공한다.

36개 reference task 중 6개에서 vision-only와 visual-tactile 정책을 비교한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2610.24512) · [저자 project/code](https://jingyi-xiang.github.io/contactbench/) · [공식 code](https://github.com/Michaelwyx/contactbench-sim). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 task별 success 판정, asset version, 정책용 reset/step와 scripted helper 분리은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

접촉 일반화 질문을 구체적인 물리 변화와 재현 자산으로 정의할 benchmark다.

### Dependency and Evolution

π₀.₅·Diffusion Policy 및 촉각 정책의 접촉 평가를 연결한다..

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

한 task의 nominal/변형 asset에서 force-rule·motion-only·joint-gain 조건을 비교한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

촉각 추가보다 접촉 행동 학습과 gain 적응이 물리 변화에 효과적인가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
