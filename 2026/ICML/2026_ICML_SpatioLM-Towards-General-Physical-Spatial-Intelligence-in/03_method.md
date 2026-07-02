# Method

- Year/Venue: 2026 / ICML Spotlight
- Category: 3D Large Multimodal Models
- Tags: Vision-Language Model, 3D Vision
- Paper link: ./2026/ICML/2026_ICML_SpatioLM-Towards-General-Physical-Spatial-Intelligence-in/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- To this end, we propose a parameter-efficient Spatio-vision Language Models (SpatioLM), that enhances spa MD-S MD-M DA-2K DR Proprietary Models (API) GPT-5.2* (OpenAI, 2025) Gemini-2.5-flash* (Comanici et al., ...
- The overall training objective is a weighted sum of a language modeling loss and mixed geometric losses.
- Unified Task Formulation We consider two configurations: • SpatioLMSenseNovaSI-8B : InternVL3 architecture, initialized from SenseNovaSI-8B (Cai et al., 2025b).

## 원리적 동기
- Most existing solutions introduce extra 3D prior inputs or external spatial encoders, which increase complexity and degrade the underlying VLMs’ general-purpose capabilities after spatial fine-tuning.
- To this end, we propose a parameter-efficient Spatio-vision Language Models (SpatioLM), that enhances spa MD-S MD-M DA-2K DR Proprietary Models (API) GPT-5.2* (OpenAI, 2025) Gemini-2.5-flash* (Comanici et al., ...

## 핵심 방법론
- The overall training objective is a weighted sum of a language modeling loss and mixed geometric losses.
- Unified Task Formulation We consider two configurations: • SpatioLMSenseNovaSI-8B : InternVL3 architecture, initialized from SenseNovaSI-8B (Cai et al., 2025b).
- To systematically enhance the spatial intelligence of SpatioLM, we construct a comprehensive training corpus that unifies low-level spatial perception with high-level spatial understanding, spanning diverse indoor and outdoor ...
- SpatioLM frames diverse spatial tasks as conditional language modeling, using prompt design to specify tasks and next-token prediction in the vocabulary space. • SpatioLMInternVL3.5-8B : InternVL3.5 architecture, initialized ...
- Visual Spatial Reasoning Training Data.
