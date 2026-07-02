# Method

- Year/Venue: 2023 / ICCV
- Category: 3D Large Multimodal Models
- Tags: 3D Vision-Language, alignment, Transformer
- Paper link: ./2023/ICCV/2023_ICCV_3D-VisTA-Pre-trained-Transformer-for-3D-Vision-and-Text-Al/paper.pdf
- Code/Project: https://3d-vista.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- In this paper, we propose 3D-VisTA, a pre-trained Transformer for 3D Vision and Text Alignment that can be easily adapted to various downstream tasks.
- 3D-VisTA In this section, we introduce 3D-VisTA, a simple and unified Transformer for aligning 3D scenes and text.
- Then the text and 3D object tokens CA ✓ ✓ ✓ ✓ ✓ × Architecture 2D MV LC ✓ ✓ ✓ ✓ × × × Table 2: The ...

## 원리적 동기
- ScanScribe contains 2,995 RGBD scans for 1,185 unique indoor scenes originating from ScanNet and 3R-Scan datasets, along with paired 278K scene descriptions generated from existing 3D-VL tasks, templates, ...
- In this paper, we propose 3D-VisTA, a pre-trained Transformer for 3D Vision and Text Alignment that can be easily adapted to various downstream tasks.

## 핵심 방법론
- 3D-VisTA In this section, we introduce 3D-VisTA, a simple and unified Transformer for aligning 3D scenes and text.
- Then the text and 3D object tokens CA ✓ ✓ ✓ ✓ ✓ × Architecture 2D MV LC ✓ ✓ ✓ ✓ × × × Table 2: The ...
- Our final pre-training objective is obtained by simply adding the losses of the proxy tasks above: Lpre-train = LMLM + LMOM + LSTM (5) Notably, the proposed pre-training ...
- Position Multi-modal fusion Masked language modeling 3D dense captioning 3D situated reasoning 3D question answering 3D visual grounding Masked object modeling Figure 2: The model architecture of our ...
- We follow the BERT pre-training to perform MLM: (1) 15% of the text tokens are randomly chosen; (2) 80% of the time: replace these tokens with [MASK]; (2) ...
