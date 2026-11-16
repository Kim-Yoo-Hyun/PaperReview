# DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

소수 인간 시연을 재사용해 시뮬레이션의 양팔 dexterous trajectory를 생성한다.

양팔 조작 simulation과 real2sim2real 사례를 제시한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2410.24185) · [저자 project/code](https://dexmimicgen.github.io/) · [공식 code](https://github.com/NVlabs/dexmimicgen). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 object-state/segmentation 접근, source-target task 대응, 생성 실패 및 sim-to-real 비용은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

여러 embodiment의 데이터를 늘릴 때 실제 시연과 합성 trajectory의 역할을 비교할 자산이다.

### Dependency and Evolution

MimicGen → DexMimicGen; RoboMIND·OXE와 데이터 생성 조건 비교.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

원본 시연 수를 고정하고 reset 다양성과 양팔 동기화 조건별 실패를 분리한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

시연 수보다 생성 가능한 coordination·contact coverage가 전이를 제한하는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
