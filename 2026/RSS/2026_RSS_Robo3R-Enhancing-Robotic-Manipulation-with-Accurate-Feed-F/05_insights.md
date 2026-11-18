# Robo3R: Enhancing Robotic Manipulation with Accurate Feed-Forward 3D Reconstruction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

RGB와 robot state에서 local geometry·camera pose를 추정하고 robot frame의 metric geometry로 정렬한다.

Robo3R-4M 합성 데이터로 학습하고 imitation·sim-to-real·grasp synthesis·collision-free planning의 downstream 효과를 평가한다.

근거: [공식 paper/abstract](https://roboticsproceedings.org/rss22/p056.html) · [저자 project/code](https://yangsizhe.github.io/robo3r/). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 Robot state privilege·similarity transform·훈련 물체 중복·latency은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

TASK-GEOMETRY가 일반 재구성 정확도 개선의 반복인지 판단할 직접 비교다.

### Dependency and Evolution

DUSt3R/VGGT의 reconstruction 표현과 Robo3R의 robot-frame geometry를 구별한다.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

같은 policy와 RGB에서 local shape·scale·extrinsic 오류를 독립적으로 주입한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

전체 geometry 오차보다 접촉 영역의 task tolerance가 행동 성공을 더 잘 예측하는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
