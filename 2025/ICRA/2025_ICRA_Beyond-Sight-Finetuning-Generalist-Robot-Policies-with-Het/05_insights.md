# Beyond Sight: Finetuning Generalist Robot Policies with Heterogeneous Sensors via Language Grounding

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

Language grounding과 multimodal contrastive·language generation loss로 새 sensor 의미를 연결한다.

Diffusion generalist와 VLA의 실세계 manipulation 및 cross-modal prompting을 보고한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2501.04693) · [저자 project/code](https://fuse-model.github.io/) · [공식 code](https://github.com/fuse-model/FuSe). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 센서 동기화, 모달별 annotation 비용, 입력 결손과 추가 정보의 구별은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

새 sensor 결합을 연구할 때 naive finetuning·masked training과 함께 대조할 직접 기준이다.

### Dependency and Evolution

Generalist policy → FuSe → task-relevant multisensory VLA.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

같은 데이터로 naive finetuning·masked training·FuSe를 가림 조건별 비교한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

동일 정보량과 예산에서 language grounding 이득이 단순 modality dropout 이후에도 남는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
