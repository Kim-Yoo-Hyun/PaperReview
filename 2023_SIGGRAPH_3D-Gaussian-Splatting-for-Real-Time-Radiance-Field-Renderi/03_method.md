# Method

## Brief Method
핵심은 foundation model feature와 3D 구조를 정렬하여 downstream task별 supervision 의존도를 줄이는 것이다.

## Abstract Method Cue
We introduce three key elements that allow us to achieve state-of-the-art visual quality while maintaining competitive training times and importantly allow high-quality real-time (>= ...

## 원리적 동기
- 3D 구조는 물체 간 거리, pose, occlusion, affordance를 제공한다.
- Vision-language/LLM prior는 open vocabulary와 commonsense를 제공한다.
- 두 표현을 alignment하면 annotation-heavy 3D supervision 없이도 더 넓은 task로 확장할 수 있다.

## 핵심 방법론
- Task family: core 3D geometry and scene representation learning
- Representation: Gaussian Splatting, 3D reconstruction
- Training/optimization: paper-specific; PDF의 method section에서 loss, supervision, inference pipeline 확인 필요.
- Deployment assumption: sensor calibration, scene reconstruction quality, and action feasibility are likely critical when moved to real robots.
