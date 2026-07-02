# ConceptFusion: Open-set Multimodal 3D Mapping

- Year/Venue: 2023 / RSS
- Category: Open-Vocabulary 3D Mapping
- Tags: sensor fusion, open-vocabulary, SLAM, Robotics
- Paper link: ./2023/RSS/2023_RSS_ConceptFusion-Open-set-Multimodal-3D-Mapping/paper.pdf
- Code/Project: https://concept-fusion.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Most existing approaches that integrate semantic concepts with 3D maps largely remain confined to the closed-set setting: they can only reason about a finite set of concepts, pre-defined ...

## Core Idea
- C ONCLUSION We presented ConceptFusion as an effective solution to the open-set multimodal 3D mapping problem.
- The zero-shot nature of our method enables reasoning over a significantly broad range of concepts; leveraging off-the-shelf foundation features for open-set perception.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- This enables effective zero-shot spatial reasoning, not needing any additional training or finetuning, and retains long-tailed concepts better than supervised approaches, outperforming them by more than 40% margin ...
- We demonstrate that pixel-aligned open-set features can be fused into 3D maps via traditional SLAM and multi-view fusion approaches.
- We showcase new avenues for blending foundation models with 3D open-set multimodal mapping.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- This enables effective zero-shot spatial reasoning, not needing any additional training or finetuning, and retains long-tailed concepts better than supervised approaches, outperforming them by more than 40% margin ...
- Most existing approaches that integrate semantic concepts with 3D maps largely remain confined to the closed-set setting: they can only reason about a finite set of concepts, pre-defined ...
- Most of these advancements have relied on a closed-set of concepts, a fixed set of labels available at training time.

## Abstract Cue
- —Building 3D maps of the environment is central to robot navigation, planning, and interaction with objects in a scene.
