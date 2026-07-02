# Method

- Year/Venue: 2026 / CVPR
- Category: Language-Embedded NeRF and Gaussian Fields
- Tags: Gaussian Splatting, 4D, referring segmentation
- Paper link: ./2026/CVPR/2026_CVPR_ST4R-Splat-Spatio-Temporal-Referring-Segmentation-in-4D-Ga/paper.pdf
- Code/Project: not identified from primary page
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- We introduce Spatio-Temporal Referring Segmentation in 4D Gaussian Splatting (STRS-4DGS), a novel task aiming to jointly identify and segment a target instance across space and time given a ...
- To tackle this, we propose ST4R-Splat, the first framework for STRS-4DGS.
- To provide rich spatio-temporal semantic supervision, we develop an automatic, MLLM-based captioning pipeline that generates decoupled spatial and temporal textual descriptions.

## 원리적 동기
- While existing methods focus on static 3D referring segmentation or openvocabulary 4D querying, they struggle to ground complex spatio-temporal referring expressions in explicit 4D reconstructions.
- However, these representations are primarily optimized for geometric fidelity and novel view synthesis, inherently lacking support for se- zha@cis.pku.edu.cn mantic reasoning and language-based scene understanding.
- We introduce Spatio-Temporal Referring Segmentation in 4D Gaussian Splatting (STRS-4DGS), a novel task aiming to jointly identify and segment a target instance across space and time given a ...

## 핵심 방법론
- americano chicken cookie espresso choco keyboard Average ReferSplat 4DLangSplat 36.97 35.70 38.65 52.26 28.47 46.55 37.41 32.55 50.61 32.32 20.39 61.00 35.42 43.40 Ours 80.51 83.57 69.48 69.65 ...
- Quantitative comparisons on the HyperNeRF dataset.
- We report (a) time-agnostic referring querying (mIoU in %) and (b) timesensitive referring querying (Acc and vIoU in %).
- Best results are highlighted in bold.
- For time-agnostic referring queries, Fig.
