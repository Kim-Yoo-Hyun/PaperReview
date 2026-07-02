# Method

- Year/Venue: 2026 / ICML
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, Vision-Language Model, Robotics, Diffusion
- Paper link: ./2026/ICML/2026_ICML_Discrete-Diffusion-VLA-Bringing-Discrete-Diffusion-to-Acti/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- Instead, we present Discrete Diffusion VLA that discretizes action chunks and models them with discrete diffusion pattern retaining progressive refinement inside the unified transformer backbone.
- On out-of-distribution tests of LIBERO-Goal, our method exhibits only 0.8% language degradation versus 8.0% of parallel decoding, and 20.4% vision degradation versus 29.0% for continuous diffusion, demonstrating well ...
- However, prevailing VLAs either generate actions autoregressively in a fixed left-to-right order with poor performance or attach separate diffusion heads outside the backbone that fragments information pathways and ...

## 원리적 동기
- Continuous diffusion over action chunks (left) versus discrete token decoders: AR (sequential), BERT-style (parallel), and our discrete diffusion with re-masking.
- Diffusion AR Action Chunk Sequential BERT Discrete Iterative Diffusion Refine Parallel Action Chunk Gen.
- Instead, we present Discrete Diffusion VLA that discretizes action chunks and models them with discrete diffusion pattern retaining progressive refinement inside the unified transformer backbone.

## 핵심 방법론
- Out-of-distribution performance on LIBERO-Spatial Method Original Lang Aug Vision Aug OpenVLA-OFT (Discrete) 96.2% 94.6% (↓1.6%) 95.0% (↓1.2%) OpenVLA-OFT (Diffusion) 96.9% 94.3% (↓2.6%) 91.1% (↓5.8%) 97.6% 96.2% (↓1.4%) 96.0% ...
- This joint evaluation directly tests whether our unified architecture preserves VLM priors while achieving strong action decoding.
- Tables 2 and 3 reveal a key advantage of our unified architecture in preserving visionlanguage capabilities under distribution shift.
- Meanwhile, bidirectional attention over action chunks and confidence-based decoding order yield consistent gains over AR decoding as shown above.
- Original Lang Aug Vision Aug OpenVLA-OFT (Discrete) 95.6% 87.6% (↓8.0%) 73.0% (↓22.6%) OpenVLA-OFT (Diffusion) 96.0% 93.6% (↓2.4%) 67.0% (↓29.0%) OpenVLA-OFT (L1) 97.9% 94.7% (↓3.2%) 74.7% (↓23.2%) Discrete Diffusion ...
