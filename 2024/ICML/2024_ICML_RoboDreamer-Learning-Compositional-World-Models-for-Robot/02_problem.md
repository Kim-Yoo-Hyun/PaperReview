# Problem

- Year/Venue: 2024 / ICML
- Category: World Models, Safety, and Recovery
- Tags: Robotics, world model, video prediction, language planning, compositional generalization
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://robodreamer.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## 왜 문제인가
- When existing text-to-video models (AVDC (Ko et al., 2023)) are given unusual combinations of language instructions, they are unable to synthesize videos that align accurately with these descriptions.

## 해결하려는 문제
- Our approach can successfully synthesize video plans on unseen goals in the RT-X, enables successful robot execution in simulation, and substantially outperforms monolithic baseline approaches to video generation.
- To resolve this issue, we introduce RoboDreamer, an innovative approach for learning a compositional world model by factorizing the video generation.
- However, one major issue in such models is generalization – models are limited to synthesizing videos subject to language instructions similar to those seen at training time.

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
