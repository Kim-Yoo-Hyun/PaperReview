# Problem

- Year/Venue: 2022 / SIGGRAPH
- Category: Foundations: 3D Scene Representations
- Tags: NeRF, 3D Vision, representation, efficiency
- Paper link: ./2022/SIGGRAPH/2022_SIGGRAPH_Instant-Neural-Graphics-Primitives-with-a-Multiresolution/paper.pdf
- Code/Project: https://nvlabs.github.io/instant-ngp/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- Unlike prior work, no structural updates to the data structure are needed at any point during training. • Efficiency: our hash table lookups are O (1) and do ...
- However, such data structures rely on heuristics and structural modifications (such as pruning, splitting, or merging) that may complicate the training process, limit the method to a specific ...
- The hash tables thus automatically prioritize the sparse areas with the most important fine scale detail.

## 해결하려는 문제
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## 선행 연구 / 배경 단서
- Unlike prior work, no structural updates to the data structure are needed at any point during training. • Efficiency: our hash table lookups are O (1) and do ...
- However, such data structures rely on heuristics and structural modifications (such as pruning, splitting, or merging) that may complicate the training process, limit the method to a specific ...
- The hash tables thus automatically prioritize the sparse areas with the most important fine scale detail.
