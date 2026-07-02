# Method

- Year/Venue: 2026 / CVPR
- Category: Benchmarks and Datasets
- Tags: Visual-Language Grounding, Benchmark, Robotics
- Paper link: ./2026/CVPR/2026_CVPR_RealVLG-R1-A-Large-Scale-Real-World-Visual-Language-Ground/paper.pdf
- Code/Project: not identified from primary page
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- To address these limitations, we propose the RealVLG framework, which integrates the RealVLG11B dataset and the RealVLG-R1 model to unify real-world visual-language grounding and grasping tasks.
- This comprehensive and integrated methodology establishes a unified, quantifiable standard for comparing model architectures across visual-language grounding and grasping tasks.
- The GSPO variant attains slightly lower geometric scores (mIoU=29.2%) but exhibits higher training stability and fully structured outputs (Rv =100%).

## 원리적 동기
- Existing VLG approaches focus on coarse-grained, object-level localization, while traditional robotic grasping methods rely predominantly on geometric cues and lack language guidance, which limits their applicability in language-driven ...
- To address these limitations, we propose the RealVLG framework, which integrates the RealVLG11B dataset and the RealVLG-R1 model to unify real-world visual-language grounding and grasping tasks.
- To address these limitations, we propose the RealVLG framework, which integrates the RealVLG11B dataset and the RealVLG-R1 model to unify real-world visual-language grounding and grasping tasks.

## 핵심 방법론
- This comprehensive and integrated methodology establishes a unified, quantifiable standard for comparing model architectures across visual-language grounding and grasping tasks.
- The GSPO variant attains slightly lower geometric scores (mIoU=29.2%) but exhibits higher training stability and fully structured outputs (Rv =100%).
- Following the data split in Table 2, both RealVLG-R1 and Qwen2.5-VL+SFT were fine-tuned for 10 epochs using only 10% of the training set.
