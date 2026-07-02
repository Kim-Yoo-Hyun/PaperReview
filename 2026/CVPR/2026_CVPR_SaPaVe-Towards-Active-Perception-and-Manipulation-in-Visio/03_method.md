# Method

- Year/Venue: 2026 / CVPR
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, active perception, Robotics
- Paper link: ./2026/CVPR/2026_CVPR_SaPaVe-Towards-Active-Perception-and-Manipulation-in-Visio/paper.pdf
- Code/Project: not identified from primary page
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- We compare our method against several strong baselines: (1) In the first experiment, we compare our model with current powerful VLM, including the general models (e.g., Qwen2.5-VL-72B , ...
- To this end, we propose SaPaVe, an end-to-end framework that jointly learns these capabilities in a data-efficient manner.
- To support this, we introduce ActiveViewPose-200K, comprising 200k image-language-camera movement pairs for semantic camera movement learning, and a 3D geometry-aware module that improves execution robustness under dynamic viewpoints.

## 원리적 동기
- Existing methods struggle to unify semantic-driven perception actively with robust, viewpoint-invariant execution accordingly.
- We compare our method against several strong baselines: (1) In the first experiment, we compare our model with current powerful VLM, including the general models (e.g., Qwen2.5-VL-72B , ...

## 핵심 방법론
- We compare our method against several strong baselines: (1) In the first experiment, we compare our model with current powerful VLM, including the general models (e.g., Qwen2.5-VL-72B , ...
- We use our model but keep the head camera fixed. (b) Fixed Camera + Wrist Camera: We again use our model with a fixed head camera and introduce ...
- We report the success rate (%) compare to different camera configurations with the same architecture.
- 4.3)? (3) Compared to existing VLA models, how does our model architecture enhance active manipulation capabilities (Sec.
- This is because the generalist VLMs struggle to translate abstract instructions into precise camera poses, whereas our specialized training yields a much more accurate and robust perception policy.
