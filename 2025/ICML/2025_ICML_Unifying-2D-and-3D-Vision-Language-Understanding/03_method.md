# Method

- Year/Venue: 2025 / ICML Poster
- Category: 3D Vision-Language Grounding
- Tags: Vision-Language Model, 3D Vision
- Paper link: ./2025/ICML/2025_ICML_Unifying-2D-and-3D-Vision-Language-Understanding/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- We introduce UniVLG, a unified architecture for 2D and 3D vision-language understanding that bridges the gap between existing 2D-centric models and the rich 3D sensory data available in ...
- We propose a novel language-conditioned mask decoder shared across 2D and 3D modalities to ground objects effectively in both RGB and RGBD images, outperforming box-based approaches.
- We present results for two model versions: one trained solely on 3D data (UniVLG-3D-only) and the other trained jointly on both 2D and 3D datasets (UniVLG).

## 원리적 동기
- The key limitation, however, is dataset availability: while 2D datasets are vast and well-curated, 3D datasets remain scarce and expensive to annotate (Dai et al., 2017; Yeshwanth et ...
- Given these challenges, is scaling 3D training data the only viable path to bridging this gap, or are there alternative strategies for making 3D models more effective?
- We introduce UniVLG, a unified architecture for 2D and 3D vision-language understanding that bridges the gap between existing 2D-centric models and the rich 3D sensory data available in ...

## 핵심 방법론
- We present results for two model versions: one trained solely on 3D data (UniVLG-3D-only) and the other trained jointly on both 2D and 3D datasets (UniVLG).
- For the Det setup, a predicted bounding box is considered correct if its intersection over union (IoU) with the ground truth box is higher than a predetermined threshold ...
- For example, 3D-VisTA (Zhu et al., 2023b) trains on the previously mentioned 3D datasets that we use but also includes 3RScan (1500 scenes) (Wald et al., 2019), Objaverse ...
- Evaluation Metrics: We use the standard top-1 accuracy
- Despite our best efforts, we could not manage to re-train PQ3D with sensor point clouds due to their use of multiple backbones, and multi-stage training strategies.
