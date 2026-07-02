# Method

- Year/Venue: 2025 / ICRA
- Category: Benchmarks and Datasets
- Tags: VLA, 3D Vision, Benchmark
- Paper link: ./2025/ICRA/2025_ICRA_IRef-VLA-A-Benchmark-for-Interactive-Referential-Grounding/paper.pdf
- Code/Project: not identified from venue audit
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- — With the recent rise of large language models, vision-language models, and other general foundation models, there is growing potential for multimodal, multi-task robotics that can operate in ...
- One such application is indoor navigation using natural language instructions.
- However, despite recent progress, this problem remains challenging due to the 3D spatial reasoning and semantic understanding required.

## 원리적 동기
- However, despite recent progress, this problem remains challenging due to the 3D spatial reasoning and semantic understanding required.
- IRef-VLA is the largest real-world dataset for the referential grounding task, consisting of over 11.5K scanned 3D rooms from existing datasets, 7.6M heuristically generated semantic relations, and 4.7M ...
- — With the recent rise of large language models, vision-language models, and other general foundation models, there is growing potential for multimodal, multi-task robotics that can operate in ...

## 핵심 방법론
- MVT 3D-VisTA Train Checkpoint Sr3D Nr3D Overall Overall ScanNet Baseline (Sr3D, reported) 64.5% - - - Baseline (Sr3D, reproduced) 59% 31.8% 29.0% 17.2% IRef-VLA-ScanNet 50.0% 29.7% 56.0% 26.7% ...
- Number of statements per relation type from each dataset processed TABLE I S UMMARY OF SEMANTIC RELATIONSHIP TYPES IN IR EF -VLA Relation Above Below Definition Target is ...
- The dominant three colors were obtained for each object based on the point cloud and a color clustering algorithm.
- To provide extra navigation targets, each scan was also processed to generate the horizontally traversable free space.
- Separate traversable regions in a room are combined into sub-regions, for which spatial relations with other objects in the scene are generated to create unambiguous references to these ...
