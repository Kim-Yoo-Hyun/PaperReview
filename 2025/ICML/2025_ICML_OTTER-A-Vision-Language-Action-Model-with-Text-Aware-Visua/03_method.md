# Method

- Year/Venue: 2025 / ICML Poster
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, Vision-Language Model, Robotics
- Paper link: ./2025/ICML/2025_ICML_OTTER-A-Vision-Language-Action-Model-with-Text-Aware-Visua/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- We propose OTTER, a novel VLA architecture that leverages these existing alignments through explicit, text-aware visual feature extraction.
- More details about model training and architectures are in Appendix B.
- As OpenVLA has many tokens per timestep, its context length cannot be extended and we use its default context length.

## 원리적 동기
- We propose OTTER, a novel VLA architecture that leverages these existing alignments through explicit, text-aware visual feature extraction.
- This approach requires the policy network to connect the vision and language information and conduct precise robot control, which often presents significant challenges, especially in unseen environments.
- We propose OTTER, a novel VLA architecture that leverages these existing alignments through explicit, text-aware visual feature extraction.

## 핵심 방법론
- More details about model training and architectures are in Appendix B.
- As OpenVLA has many tokens per timestep, its context length cannot be extended and we use its default context length.
- We hypothesize this is because it’s challenging for the direct feature passing architectures to learn generalizable vision-language connections on a small robotic dataset, while OTTER can utilize the ...
- Direct Feature Passing OTTER (DFP-OTTER): a variant of OTTER where the text tokens, vision tokens are passed to an attention pooling layer separately to obtain independent tokens, which ...
- Training Tasks Unseen Tasks - 61% ± 5.3% 15% ± 3.4% 17% ± 2.9% 30% ± 3.9% 29% ± 3.7% 26% ± 4.0% 40% ± 4.0% 57% ± ...
