# Problem

- Year/Venue: 2025 / NeurIPS Oral
- Category: Navigation and Embodied AI
- Tags: Vision-Language Model, 3D Vision, Navigation
- Paper link: ./2025/NeurIPS/2025_NeurIPS_Dynam3D-Dynamic-Layered-3D-Tokens-Empower-VLM-for-Vision-a/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- We propose Dynam3D to alleviate the limitations mentioned above.
- Despite these recent advances, several limitations still remain: 1) Video-based models struggle to capture spatial geometry and semantics in large-scale 3D environments.
- A 3D instance merging discriminator aligns 2D instances with existing 3D instances based on geometry and semantics to enable dynamic updates of 3D instance representations.

## 해결하려는 문제
- By leveraging large-scale 3D-language pretraining and task-specific adaptation, our Dynam3D sets new state-of-the-art performance on VLN benchmarks including R2R-CE, REVERIE-CE and NavRAG-CE under monocular settings.
- To address these limitations, we propose Dynam3D, a dynamic layered 3D representation model that leverages language-aligned, generalizable, and hierarchical 3D representations as visual input to train 3D-VLM in ...
- Furthermore, experiments for pre-exploration, lifelong memory, and real-world robot validate the effectiveness of practical deployment.

## 선행 연구 / 배경 단서
- We propose Dynam3D to alleviate the limitations mentioned above.
- In summary, our main contributions include: • We propose Dynam3D, a multi-level patch-instance-zone 3D representation model that performs online 3D instance and zone-level encoding and real-time hierarchical updates ...
- Despite these recent advances, several limitations still remain: 1) Video-based models struggle to capture spatial geometry and semantics in large-scale 3D environments.
