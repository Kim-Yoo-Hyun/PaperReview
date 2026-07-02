# Method

- Year/Venue: 2024 / CVPR
- Category: 3D Large Multimodal Models
- Tags: LLM, 3D Vision, Planning
- Paper link: ./2024/CVPR/2024_CVPR_LL3DA-Visual-Interactive-Instruction-Tuning-for-Omni-3D-Un/paper.pdf
- Code/Project: https://github.com/Open3DA/LL3DA
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- In this paper, we present LL3DA, a Large Language 3D Assistant that takes point cloud as direct input and respond to both textual- 1.
- To examine whether our method could distinguish different tasks given the textual instructions and visual prompts introduced in Sec.
- The first row is our baseline method that directly generates the captions based on visual prompts without any textual instructions, and the second row is our method that ...

## 원리적 동기
- Existing works seek help from multi-view images, and project 2D features to 3D space as 3D scene representations.
- Prior works have made initial success addressing various 3D vision and language tasks.
- In this paper, we present LL3DA, a Large Language 3D Assistant that takes point cloud as direct input and respond to both textual- 1.

## 핵심 방법론
- To examine whether our method could distinguish different tasks given the textual instructions and visual prompts introduced in Sec.
- The first row is our baseline method that directly generates the captions based on visual prompts without any textual instructions, and the second row is our method that ...
- There is also an interesting observation that although we did not differentiate between the two datasets for 3D-DC, and the training Instructions ✓ C@0.5↑ 60.20 62.84 B-4@0.5↑ 34.79 ...
- We listed two ways of encoding visual prompts, (a) adopting a unified transformer to aggregate features from all kinds of interactions, and (b) directly concatenate the visual prompts ...
- Answer Type Method ScanQA Clip-Guided Multi-CLIP 3D-VLP 3D-VisTA 3D-LLM∗ LL3DA (Ours) CLS GEN Large Language Model Multi-Modal Transformer Textual Instructions (a) Early Fusion (ours) R↑ 33.33 34.51 35.70 ...
