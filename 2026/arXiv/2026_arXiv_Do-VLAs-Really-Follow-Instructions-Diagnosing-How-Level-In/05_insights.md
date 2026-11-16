# Do VLAs Really Follow Instructions? Diagnosing How-Level Instruction Following in Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

How-level 지시의 효과를 진단하고 segment-level 지시 보강을 비교하며, 지시에만 주어진 조건을 성공 정의에 포함하는 SIMPLER-IN을 제안한다.

보강된 지시에 대한 행동 반응이 늘어도 작업 성공이 일관되게 높아지지는 않으며, 까다롭거나 분포 밖의 지시에 일반화가 제한된다고 보고한다. SIMPLER-IN의 상세 task·split·trial은 본문 확인 대상이다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2610.21251) · [저자 project/code](https://github.com/sangwu99/how-level-vla-Arxiv). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 SIMPLER-IN 조건별 성공 정의와 중립 문장 대조, 지시 보강 학습의 정보·데이터 통제, OOD 범위, 평가 코드와 checkpoint 일치은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

현재 제약 유지·철회 후보에서 지시 반응, 목표 성공, 제약 준수를 분리할 직접 진단 선행이다. 평가 정의 자체를 새 기여로 과장하지 않기 위한 NEXT이며 preprint로 둔다.

### Dependency and Evolution

Hi Robot의 상위 지시 해석 ↔ How-level의 하위 행동 준수 진단; ReSteer의 중간 전환 ↔ 지시 내용의 준수.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

같은 상태의 목표만 지시·제약 포함 지시·의미 동일 재진술을 구분해 기록한다. 자동 의미 갱신과 물리적 수행 실패를 분리하며 아직 정책 실행은 하지 않았다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

명시적인 최초 지시와 부분 수정 뒤 재구성한 지시를 같은 표현으로 맞춰도 의미 갱신 오류가 추가 행동 실패를 설명하는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
