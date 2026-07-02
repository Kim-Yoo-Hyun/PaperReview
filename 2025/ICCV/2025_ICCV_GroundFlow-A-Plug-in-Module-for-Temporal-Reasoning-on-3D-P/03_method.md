# Method

- Year/Venue: 2025 / ICCV
- Category: 3D Vision-Language Grounding
- Tags: 3D Vision
- Paper link: ./2025/ICCV/2025_ICCV_GroundFlow-A-Plug-in-Module-for-Temporal-Reasoning-on-3D-P/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- To fill this gap, we propose GroundFlow — a plug-in module for temporal reasoning on 3D point cloud sequential grounding.
- In summary, we make the following contributions: • We propose the GroundFlow module with a recurrent framework, which can be integrated into previous 3DVG baselines and introduce important ...
- In addition, we propose GroundFlow module, which can be built on top of the existing 3DVG methods to perform temporal fusion with previous step embeddings, improving the comprehension ...

## 원리적 동기
- Effectively retrieving relevant previous information is essential for solving this problem, yet current visual grounding methods lack a design for temporal fusion.
- Due to the lack of an effective module for collecting related historical information, state-of-theart 3DVG methods face significant challenges in adapting to the SG3D task.
- To fill this gap, we propose GroundFlow — a plug-in module for temporal reasoning on 3D point cloud sequential grounding.

## 핵심 방법론
- GPT4 + PointNet++ (Zero-shot) LEO (3DLLM) 3D-VisTA 3D-VisTA+ GroundFlow MiKASA MiKASA + GroundFlow PQ3D PQ3D + GroundFlow Vil3DRel Vil3DRel + GroundFlow ScanNet s-acc t-acc 42.6 10.9 61.2 25.7 ...
- Comparisons on SG3D benchmark across five datasets.
- The values for the metrics s-acc (step accuracy) and t-acc (task accuracy) are expressed as percentages (%).
- The methods with our proposed modules are highlighted in orange and the numbers in bold represent the best performance in given dataset and metrics.
- Comparison on SG3D Benchmark Comparison with 3DVG methods.
