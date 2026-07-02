# Method

- Year/Venue: 2026 / ICML
- Category: Vision-Language-Action and Robot Manipulation
- Tags: Vision-Language Model, Robotics
- Paper link: ./2026/ICML/2026_ICML_RoboOmni-Actions-Are-Just-Another-Modality-for-Vision-Lang/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- To address this, we introduce RoboOmni, a unified multi-modal next-token prediction framework.
- At the core of our method is Multi-Token Action Prediction (MTAP), which integrates action chunking directly into the discrete tokenizer.
- Our controlled comparisons isolate the benefits of the RoboOmni architecture.

## 원리적 동기
- However, a critical challenge has emerged: while built upon highly capable VLMs, many current VLA implementations struggle to retain the broad generalization abilities inherent in their parent models.
- However, unified discrete frameworks lag behind decoupled continuous designs due to limitations in action chunking and temporal modeling.
- To address this, we introduce RoboOmni, a unified multi-modal next-token prediction framework.

## 핵심 방법론
- Our controlled comparisons isolate the benefits of the RoboOmni architecture.
- Notably, our discrete-token approach also outperforms π0 -FAST (61.9%), further confirming that our unified architecture effectively bridges the gap
