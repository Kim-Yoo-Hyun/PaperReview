# OGBench: Benchmarking Offline Goal-Conditioned RL

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

다양한 goal-conditioned environment/dataset와 reference algorithm 구현을 제공하여 능력별 차이를 드러낸다.

ICLR abstract는 8종 환경, 85 datasets 및 6 reference algorithm을 보고한다. Task/split별 정확한 성공 정의는 본문 확인 필요.

근거: [공식 paper/abstract](https://proceedings.iclr.cc/paper_files/paper/2025/hash/ecd92623ac899357312aaa8915853699-Abstract-Conference.html) · [저자 project/code](https://github.com/seohongpark/ogbench). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 Goal sampling, reward relabeling, split/dataset 품질과 성공률 aggregation은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

Benchmark. Stitching·장기 horizon·pixel input 등의 능력을 구분하는 기준이다. FQL/Q-chunking/DQC 결과를 이해하는 prerequisite이며 LIBERO/CALVIN과 평가 목적을 구분한다. Language-conditioned real-robot benchmark는 아니다.

### Dependency and Evolution

IQL/CQL → OGBench → FQL/Q-chunking/DQC; LIBERO와 평가 목적 구분.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

동일 data budget으로 FQL/IQL 계열을 manipulation 및 maze task에서 비교하고 능력별 점수를 분리한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

Aggregate score가 같은 두 알고리즘도 stitching과 장기 horizon 조건에서 다른 순위를 보이는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
