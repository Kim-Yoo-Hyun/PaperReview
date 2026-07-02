# Method

- Year/Venue: 2024 / CVPR
- Category: 3D Large Multimodal Models
- Tags: LLM, 3D Vision, sensor fusion
- Paper link: ./2024/CVPR/2024_CVPR_MultiPLY-A-Multisensory-Object-Centric-Embodied-Large-Lang/paper.pdf
- Code/Project: not identified from primary page
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- To usher in the study of this area, we propose MultiPLY, a multisensory embodied large language model that could incorporate multisensory interactive data, including visual, audio, tactile, and ...
- Likewise, we propose to represent the environment as an abstracted object-centric representation.
- MultiPLY In this section, we introduce the MultiPLY framework.

## 원리적 동기
- Existing multi-modal large language models (e.g., LLaVA , Flamingo , BLIP-2 , PaLM-E ) excel at num
- Current multi-modal large language models, however, passively absorb sensory data as inputs, lacking the capacity to actively interact with the objects in the 3D environment and dynamically collect ...
- To usher in the study of this area, we propose MultiPLY, a multisensory embodied large language model that could incorporate multisensory interactive data, including visual, audio, tactile, and ...

## 핵심 방법론
- Likewise, we propose to represent the environment as an abstracted object-centric representation.
- MultiPLY In this section, we introduce the MultiPLY framework.
- We use concept graphs powered with a CLIP encoder to first encode the objects in the observed images, and fuse the outputs in images to 3D by multi-view ...
- The object is chosen by the attention between the language features (i.e., the last hidden state of the LLM of the SELECT token), and the CLIP visual features ...
- It selects the object with the maximum attention score.
