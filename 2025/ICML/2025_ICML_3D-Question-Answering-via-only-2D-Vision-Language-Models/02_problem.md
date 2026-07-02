# Problem

- Year/Venue: 2025 / ICML Poster
- Category: 3D Large Multimodal Models
- Tags: Vision-Language Model, 3D Vision
- Paper link: ./2025/ICML/2025_ICML_3D-Question-Answering-via-only-2D-Vision-Language-Models/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- Tokenization <2D Views> <Question> What is the black couch facing? a1.

## 해결하려는 문제
- We evaluate cdViews on the widely-used ScanQA and SQA benchmarks, demonstrating that it achieves state-of-the-art performance in 3D-QA while relying solely on 2D models without fine-tuning.
- We propose cdViews, a novel approach to automatically selecting critical and diverse Views for 3D-QA. cdViews consists of two key components: viewSelector prioritizing critical views based on their ...
- All of these methods require computationally intensive 3D-language alignment using point cloud data for spatial reasoning. a4 is our method that leverages pre-trained LVLMs operating solely on 2D ...

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
