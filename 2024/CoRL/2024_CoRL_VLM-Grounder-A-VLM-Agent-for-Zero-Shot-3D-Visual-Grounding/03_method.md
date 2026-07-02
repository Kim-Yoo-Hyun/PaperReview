# Method

- Year/Venue: 2024 / CoRL
- Category: 3D Vision-Language Grounding
- Tags: 3D visual grounding, VLM, zero-shot
- Paper link: ./2024/CoRL/2024_CoRL_VLM-Grounder-A-VLM-Agent-for-Zero-Shot-3D-Visual-Grounding/paper.pdf
- Code/Project: https://github.com/InternRobotics/VLM-Grounder
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- To explore this, we propose a Visual-Retrieval Benchmark.
- PC Acc@0.25 Acc@0.5 Acc@0.25 Acc@0.5 Acc@0.25 Acc@0.5 ScanRefer TGNN InstanceRefer 3DVG-Transformer BUTD-DETR é é é é é é é é é é 37.3 34.3 40.2 47.6 52.2 24.3 ...
- In this work, we present VLM-Grounder, a novel framework using vision-language models (VLMs) for zero-shot 3D visual grounding based solely on 2D images.

## 원리적 동기
- However, estimating a 3D bounding box from a single image can be problematic due to limited field-of-view and inaccurate depth information.
- However, existing visual grounding datasets are scarce and limited to a pre-defined vocabulary, challenging the development of general models for open-world applications.
- To explore this, we propose a Visual-Retrieval Benchmark.

## 핵심 방법론
- To explore this, we propose a Visual-Retrieval Benchmark.
- PC Acc@0.25 Acc@0.5 Acc@0.25 Acc@0.5 Acc@0.25 Acc@0.5 ScanRefer TGNN InstanceRefer 3DVG-Transformer BUTD-DETR é é é é é é é é é é 37.3 34.3 40.2 47.6 52.2 24.3 ...
- Without model training, VLM-Grounder’s overall performance also competes with supervised learning methods like InstanceRefer (38.8%) and 3DVG-Transformer (40.8%).
- We use the top five layouts and observe how accuracy varies with the number of images sent to GPT-4V in one request.
