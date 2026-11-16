# LIBERO-Plus: A Progressive Robustness Benchmark for Visual-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

배치·camera·robot 초기 상태·언어·조명·배경·sensor noise를 통제한 점진 평가를 구성한다.

다수 VLA의 simulation robustness를 비교한다. 수치·정확한 난도 split은 본문 확인 필요.

근거: [공식 paper/abstract](https://openaccess.thecvf.com/content/CVPR2026/html/Fei_LIBERO-Plus_A_Progressive_Robustness_Benchmark_for_Visual-Language-Action_Models_CVPR_2026_paper.html) · [저자 project/code](https://github.com/sylvestf/LIBERO-plus). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 난도 선정에 쓰인 model, perturbation validity, test contamination은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

기본 성공률과 일반화 성능을 구분하는 현재 VLA 평가의 직접 기준이다.

### Dependency and Evolution

LIBERO → LIBERO-Plus → task validity를 확인한 강건성 비교.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

동일 checkpoint로 원본/변형 task를 paired 비교하고 reachability와 성공 판정을 감사한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

Perturbation 후에도 행동 가능한 task라는 조건을 통제하면 실패 패턴이 유지되는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
