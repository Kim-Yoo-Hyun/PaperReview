# Insights

## 이 논문에서 가져갈 핵심 개념
- 핵심 방법 단서: Frames FVD↓ LPIPS↓ SSIM↑ PSNR↑ RPE↓ RVE↓ DFoT (Song et al., 2025) REPA (Yu et al., 2024a) VideoREPA (Zhang et al., 2025c) Geometry Forcing (ours) Geometry Forcing (ours) ...

## 내 연구 방향에서 어떻게 활용할 수 있나
- 위 paper-specific cue를 논문 claim으로만 두지 말고, 3D Vision + Robotics에서 representation, memory, planning 설계 원리로 재사용한다.
- Diffusion/generative prior를 sparse observation completion, 3D scene/object generation, action trajectory proposal에 사용할 수 있다.
- 생성 모델의 prior는 부족한 geometry나 demonstration을 보완하지만, physical feasibility와 metric correctness를 별도 제약으로 확인해야 한다.

## 이 논문이 끝난 지점
- visual/shape generation 품질 이후에도 geometry correctness, controllability, physical plausibility, robot execution 가능성은 남는다.

## 다음 연구 질문
- 2D/3D diffusion prior가 실제 3D reconstruction이나 planning에서 metric error를 줄이는가, 아니면 plausible hallucination을 늘리는가?
- language-conditioned generation 결과를 robot execution constraint로 어떻게 검증하고 거를 수 있는가?
- generated scene/action 후보의 uncertainty를 downstream planner에 어떻게 전달할 수 있는가?

## 실험으로 확인할 방향
- 논문 내 evaluation 단서: 자동 추출에서 명확한 dataset 단서 없음 / accuracy, mAP, PSNR, SSIM, LPIPS
- 내 연구 확장 benchmark 후보: ShapeNet, Objaverse, ScanNet, RLBench
- 내 연구 확장 metric 후보: Chamfer, F-score, CLIP score, success rate
- 검증 초점: generation fidelity, geometric validity, physical feasibility, downstream task utility를 함께 확인한다.

## 주의할 점
- 이 파일의 활용 방향은 논문 claim이 아니라, 위 paper-specific cue를 3D Vision + Robotics 연구 방향으로 확장한 survey-level 해석이다.
- 논문 내 explicit limitation/future cue가 부족한 경우, 후속 질문은 method scope와 evaluation scope의 빈틈에서 도출했다.

## 근거가 되는 논문 단서
- Method cue: Frames FVD↓ LPIPS↓ SSIM↑ PSNR↑ RPE↓ RVE↓ DFoT (Song et al., 2025) REPA (Yu et al., 2024a) VideoREPA (Zhang et al., 2025c) Geometry Forcing (ours) Geometry Forcing (ours) ...
