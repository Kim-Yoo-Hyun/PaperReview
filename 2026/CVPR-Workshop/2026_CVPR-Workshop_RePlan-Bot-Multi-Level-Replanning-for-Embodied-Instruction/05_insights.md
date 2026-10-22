# RePlan-Bot: Multi-Level Replanning for Embodied Instruction Following

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

고수준 계획 감사와 탐색·저수준 보정을 연결한다.

ALFRED instruction following 평가를 보고한다.

근거: [공식 paper/abstract](https://openaccess.thecvf.com/content/CVPR2026W/GRAIL-V/html/Gong_RePlan-Bot_Multi-Level_Replanning_for_Embodied_Instruction_Following_CVPRW_2026_paper.html). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 ALFRED predicate, oracle map 접근, action executor, VLA와의 차이은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

D3의 multi-level replanning이 이미 존재하는 workshop 비교군이다.

### Dependency and Evolution

Language planning·ALFRED → RePlan-Bot.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

Plan 수정과 action 보정을 분리하고 task success·개입 비용을 비교한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

같은 실행기와 도구에서 새로운 switching 기준의 이득이 남는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
