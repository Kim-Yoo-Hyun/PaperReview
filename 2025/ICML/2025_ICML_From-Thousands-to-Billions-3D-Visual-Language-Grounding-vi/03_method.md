# Method

- Year/Venue: 2025 / ICML Poster
- Category: 3D Vision-Language Grounding
- Tags: Vision-Language Model, 3D Vision
- Paper link: ./2025/ICML/2025_ICML_From-Thousands-to-Billions-3D-Visual-Language-Grounding-vi/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- This rendersupervised formulation enables end-to-end training of complete encoder-decoder architectures and is inherently model-agnostic.
- Loss Ablation Existing pretraining pipelines primarily focus on the encoder (Zhu et al., 2023b; Banani et al., 2021), whereas the render-supervised formulation can pretrain the entire architecture in ...
- We introduce LIFT-GS, a practical distillation technique that overcomes this limitation by using differentiable rendering to bridge 3D and 2D supervision.

## 원리적 동기
- We introduce LIFT-GS, a practical distillation technique that overcomes this limitation by using differentiable rendering to bridge 3D and 2D supervision.
- This six-order-of-magnitude gap in data availability severely limits the capabilities of current 3D grounding systems, creating one of the most significant challenges in embodied AI.
- This rendersupervised formulation enables end-to-end training of complete encoder-decoder architectures and is inherently model-agnostic.

## 핵심 방법론
- Loss Ablation Existing pretraining pipelines primarily focus on the encoder (Zhu et al., 2023b; Banani et al., 2021), whereas the render-supervised formulation can pretrain the entire architecture in ...
- For these evaluations, we use a model pretrained only on ScanNet as the baseline.
- Moreover, LIFT-GS substantially outperforms PonderV2† (47.5% vs 45.4% Acc@0.25), underscoring the impact of multimodal decoder architectures enabled by the LIFT-GS render-supervised formulation. boxes from the SOTA object detector ...
- Compare to SOTA pretraining methods We compare
- Because PQ3D uses multiple backbones and a multi-stage training pipeline, we were not able to reproduce PQ3D on the sensor point cloud setting.
