# Method

## Brief Method
핵심은 2D/3D visual tokens, point/scene representation, language model을 정렬해 공간 질의와 embodied reasoning을 한 모델에서 처리하는 것이다.

## Abstract Method Cue
In this paper, we propose a system that leverages Vision-Language Models (VLMs), like GPT-4V, to intelligently search the design action space to arrive at ...

## 원리적 동기
- 3D 구조는 물체 간 거리, pose, occlusion, affordance를 제공한다.
- Vision-language/LLM prior는 open vocabulary와 commonsense를 제공한다.
- 두 표현을 alignment하면 annotation-heavy 3D supervision 없이도 더 넓은 task로 확장할 수 있다.

## 핵심 방법론
- Task family: 3D vision-language spatial reasoning
- Representation: 3D Vision, Graph Reasoning
- Training/optimization: paper-specific; PDF의 method section에서 loss, supervision, inference pipeline 확인 필요.
- Deployment assumption: sensor calibration, scene reconstruction quality, and action feasibility are likely critical when moved to real robots.
