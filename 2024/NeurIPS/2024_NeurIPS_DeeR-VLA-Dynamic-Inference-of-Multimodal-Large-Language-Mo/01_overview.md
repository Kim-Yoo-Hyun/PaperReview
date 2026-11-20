# DeeR-VLA: Dynamic Inference of Multimodal Large Language Models for Efficient Robot Execution

> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-19 · 서지·초록과 링크한 방법·비교 절을 확인했다. 논문 전체 정독과 실험 재현은 미확인이다.

- Year/Venue: 2024 / NeurIPS
- Authors: Yang Yue, Yulin Wang, Bingyi Kang, Yizeng Han, Shenzhi Wang, Shiji Song, Jiashi Feng, Gao Huang
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, early exit, inference efficiency
- Official paper: https://proceedings.neurips.cc/paper_files/paper/2024/hash/67b0e7c7c2a5780aeefe3b79caac106e-Abstract-Conference.html
- Code/Project: https://github.com/yueyang130/DeeR-VLA

## 연구 질문과 기여

로봇 정책이 관측마다 다른 깊이에서 추론을 종료하도록 학습한다.

여러 중간 층에서 행동을 출력한다. 평균 계산량과 순간 지연·메모리 요구에 맞춰 종료 조건을 조정한다.

## 평가 범위

CALVIN 장기 지시 조작에서 작업 성능, 연산량과 메모리를 함께 비교했다. [원문 및 평가 절](https://proceedings.neurips.cc/paper_files/paper/2024/file/67b0e7c7c2a5780aeefe3b79caac106e-Paper-Conference.pdf#page=8)

## 선정 근거

계산 예산에 따라 같은 VLA의 실행 깊이를 바꾸는 비교 기준이다.
