# CoRe-VLA: Preserving Cross-View Coordination in VLAs under Camera Shifts

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

Point-cloud reprojection과 render 복원, execution alignment로 training view를 복구한다.

5 real-robot task, LIBERO-100와 LIBERO-Plus를 보고한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2609.37150) · 저자 프로젝트·코드 주소 미확인. 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 intrinsic/extrinsic 접근, depth 정렬, asynchronous 비용은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

D1 camera-shift 보정의 직접 NEXT baseline이다. Conditional Routing CoRE-VLA와 별도 identity다.

### Dependency and Evolution

SpatialVLA/PointVLA의 3D 표현과 camera CoRe-VLA의 input-view restoration을 구분하고 MoManipVLA의 geometry/control interface와 연결한다.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

Known-transform comparator와 같은 관측으로 변환을 추정하는 baseline을 분리한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

카메라 변환을 모를 때도 기존 복원 접근이 충분한가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
