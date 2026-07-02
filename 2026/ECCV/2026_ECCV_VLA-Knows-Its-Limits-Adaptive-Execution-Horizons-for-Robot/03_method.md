# Method

- Year/Venue: 2026 / ECCV
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, Robotics
- Paper link: ./2026/ECCV/2026_ECCV_VLA-Knows-Its-Limits-Adaptive-Execution-Horizons-for-Robot/paper.pdf
- Code/Project: https://hatchetproject.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- To uncover the reasons, we analyze the cross- and self-attention weights in flow-based VLAs and reveal two key phenomena: (i) intrachunk actions attend invariantly to vision–language tokens, limiting ...
- Motivated by these insights, we interpret action self-attention weights as a proxy for the model’s predictive limit and propose AutoHorizon, the first test-time method that dynamically estimates the ...

## 원리적 동기
- Action chunking has recently emerged as a standard practice in flow-based Vision-Language-Action (VLA) models.
- However, the effect and choice of the execution horizon—the number of actions to be executed from each predicted chunk—remains underexplored.
- To uncover the reasons, we analyze the cross- and self-attention weights in flow-based VLAs and reveal two key phenomena: (i) intrachunk actions attend invariantly to vision–language tokens, limiting ...

## 핵심 방법론
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
