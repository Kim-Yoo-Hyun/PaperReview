# Method

## Brief Method
핵심은 pretrained VLM/LLM 또는 3D representation을 policy/action space에 결합해 language-conditioned manipulation을 더 일반화 가능하게 만드는 것이다.

## Abstract Method Cue
In this paper, we introduce a method that incorporates explicit visual chain-of-thought (CoT) reasoning into vision-language-action models (VLAs) by predicting future image frames autoregressively ...

## 원리적 동기
- 3D 구조는 물체 간 거리, pose, occlusion, affordance를 제공한다.
- Vision-language/LLM prior는 open vocabulary와 commonsense를 제공한다.
- 두 표현을 alignment하면 annotation-heavy 3D supervision 없이도 더 넓은 task로 확장할 수 있다.

## 핵심 방법론
- Task family: robot manipulation and vision-language-action control
- Representation: VLA
- Training/optimization: paper-specific; PDF의 method section에서 loss, supervision, inference pipeline 확인 필요.
- Deployment assumption: sensor calibration, scene reconstruction quality, and action feasibility are likely critical when moved to real robots.
