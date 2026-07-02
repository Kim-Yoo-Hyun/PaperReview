# Method

- Year/Venue: 2025 / NeurIPS Poster
- Category: Vision-Language-Action and Robot Manipulation
- Tags: Vision-Language Model, Robotics, 3D Vision
- Paper link: ./2025/NeurIPS/2025_NeurIPS_ViSPLA-Visual-Iterative-Self-Prompting-for-Language-Guided/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- Project Website We propose ViSPLA, a novel iterative self-prompting framework for language-guided 3D affordance detection that incorporates differential geometric feedback for progressive mask refinement.
- While existing approaches model this as a direct mapping fθ : (P, L) 7→ M, we introduce an iterative refinement process, as already described in section 1: Mt ...
- To further enhance precision and coherence, we introduce Implicit Neural Affordance Fields, which define continuous probabilistic regions over the 3D surface without additional supervision.

## 원리적 동기
- This approach addresses several critical challenges in the field: (1) Existing single-pass inference methods lack the ability to iteratively refine predictions, often leading to suboptimal segmentation, especially on ...
- Formally, we can represent the affordance detection problem as a mapping function fθ : (P) 7→ A, where P ∈ RN ×3 denotes a point cloud with N ...
- Project Website We propose ViSPLA, a novel iterative self-prompting framework for language-guided 3D affordance detection that incorporates differential geometric feedback for progressive mask refinement.

## 핵심 방법론
- We propose ViSPLA, a novel iterative self-prompting framework for language-guided 3D affordance detection that incorporates differential geometric feedback for progressive mask refinement.
- While existing approaches model this as a direct mapping fθ : (P, L) 7→ M, we introduce an iterative refinement process, as already described in section 1: Mt ...
- Unlike previous methods that rely on single-pass inference, our approach employs a recurrent self-prompting mechanism that leverages the intrinsic geometric properties of predicted affordance masks to guide subsequent ...
- 3.2 Preliminaries: Language-guided Affordance Detection Backbone We build upon the 3D-AffordanceLLM architecture, adopting it as our backbone, which comprises a pre-trained point encoder fPE , a point cloud ...
- ViSPLA consists of three main components: (1) a language-guided affordance detection backbone based on 3D-AffordanceLLM, (2) a differential geometry-based self-prompting module, and (3) an iterative affordance refinement module, ...
