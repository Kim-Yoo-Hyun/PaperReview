# Joint-Aligned Latent Action: Towards Scalable VLA Pretraining in the Wild

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

역동역학과 실제 행동에 함께 정렬한 latent action을 학습한다.

사람 동작 및 simulation·실제 robot manipulation 전이를 평가한다.

근거: [공식 paper/abstract](https://openaccess.thecvf.com/content/CVPR2026/html/Luo_Joint-Aligned_Latent_Action_Towards_Scalable_VLA_Pretraining_in_the_Wild_CVPR_2026_paper.html) · [저자 project/code](https://research.beingbeyond.com/jala) · [공식 code](https://github.com/BeingBeyond/JALA). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 실제 action label 요구량, 인간 손과 robot action 대응, 비정형 영상 split은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

Unified VLA-RL의 action representation 기여를 판단할 사전학습 비교 기준이다.

### Dependency and Evolution

LAPA·VPT·latent-action VLA와 사람 영상에서 행동 정보를 얻는 방식을 비교한다..

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

동일 영상·로봇 데이터에서 역동역학만, 행동 정렬만, 공동 정렬을 비교한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

RL에 유리한 latent가 단순 reconstruction 품질보다 action alignment로 설명되는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
