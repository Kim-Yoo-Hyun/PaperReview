# Actions as Language: Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

자연어로 low-level action을 표현하고 parameter-efficient adaptation을 사용한다.

Robot manipulation과 VQA 능력 보존을 함께 보고한다.

근거: [공식 paper/abstract](https://proceedings.iclr.cc/paper_files/paper/2026/hash/7a0f8055c838df8e62329a76c7c6403d-Abstract-Conference.html). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 action decoding, LoRA 범위, VQA/robot split과 robot controller은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

의미 능력 보존이라는 넓은 방향의 직접 선행이며 action interface 비교에도 필요하다.

### Dependency and Evolution

RT-2·OpenVLA → language action interface → LAP.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

같은 데이터·backbone으로 VQA 보존과 instruction-conditioned 성공률을 따로 측정한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

VQA 보존이 지시 변화에 대한 행동 성능도 예측하는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
