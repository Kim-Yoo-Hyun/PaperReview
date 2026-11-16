# PhysTwin: Physics-Informed Reconstruction and Simulation of Deformable Objects from Videos

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

물리 simulation·geometry·Gaussian rendering을 결합해 상호작용 영상에서 역모델링한다.

변형체 재구성·미래 예측·새 상호작용과 model-based robot planning 사례를 보고한다.

근거: [공식 paper/abstract](https://openaccess.thecvf.com/content/ICCV2025/html/Jiang_PhysTwin_Physics-Informed_Reconstruction_and_Simulation_of_Deformable_Objects_from_Videos_ICCV_2025_paper.html) · [저자 project/code](https://jianghanxiao.github.io/phystwin-web/) · [공식 code](https://github.com/Jianghanxiao/PhysTwin). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 material/boundary 식별성, interaction 데이터 접근, planning 평가와 reconstruction의 분리은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

3D 외관 재구성과 행동에 유용한 물성 모델을 구별할 직접 연결 연구다.

### Dependency and Evolution

Gaussian scene representation·AdaptiGraph → PhysTwin; GAP-DE의 물성/경계 조건 비교.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

동일 관측 적합도의 여러 모델을 새 interaction으로 구분하고 planning regret을 비교한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

영상 재현 오차가 비슷한 모델들이 새 접촉 행동의 최적 선택에서도 일치하는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
