# Method

- Year/Venue: 2025 / ICCV
- Category: 3D Vision-Language Grounding
- Tags: 3D Vision
- Paper link: ./2025/ICCV/2025_ICCV_ViewSRD-3D-Visual-Grounding-via-Structured-Multi-View-Deco/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- To tackle these challenges, we propose ViewSRD, a framework that formulates 3D visual grounding as a structured multi-view decomposition process.
- Our SRD module is inherently model-agnostic, operating independently of the training process by focusing exclusively on decoupling complex multi-anchor queries into simpler single-anchor queries.
- This decoupling mechanism reduces ambiguity in multi-anchor descriptions, enhances target grounding, and serves as a model-independent preprocessing step, ensuring seamless compatibility with various 3DVG methods to improve performance ...

## 원리적 동기
- To tackle these challenges, we propose ViewSRD, a framework that formulates 3D visual grounding as a structured multi-view decomposition process.
- However, existing methods struggle with disentangling targets from anchors in complex multi-anchor queries and resolving inconsistencies in spatial descriptions caused by perspective variations.
- To tackle these challenges, we propose ViewSRD, a framework that formulates 3D visual grounding as a structured multi-view decomposition process.

## 핵심 방법론
- Our SRD module is inherently model-agnostic, operating independently of the training process by focusing exclusively on decoupling complex multi-anchor queries into simpler single-anchor queries.
- This decoupling mechanism reduces ambiguity in multi-anchor descriptions, enhances target grounding, and serves as a model-independent preprocessing step, ensuring seamless compatibility with various 3DVG methods to improve performance ...
- 3DVG-Transformer LanguageRefer TransRefer3D SAT MVT ViewRefer MiKASA CoT3DRef ViewSRD (ours) Sr3D Overall Easy Hard View Dep.
