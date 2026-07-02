# Method

- Year/Venue: 2024 / ECCV
- Category: 3D Large Multimodal Models
- Tags: Vision-Language Model, 3D Vision, Graph Reasoning
- Paper link: ./2024/ECCV/2024_ECCV_BlenderAlchemy-Editing-3D-Graphics-with-Vision-Language-Mo/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- In this paper, we propose a system that leverages Vision-Language Models (VLMs), like GPT-4V, to intelligently search the design action space to arrive at an answer that can ...

## 원리적 동기
- Moreover, slightly different design goals may require completely different sequences, making automation difficult.
- In this paper, we propose a system that leverages Vision-Language Models (VLMs), like GPT-4V, to intelligently search the design action space to arrive at an answer that can ...

## 핵심 방법론
- The goal of our system is to perform edits within the Blender 3D graphic design environment through iteratively refining programs that define a sequence of edits in Blender.
- This requires us to (1) decompose the input initial Blender input into a combination of programs and a “base” Blender state (Section 3.1) and (2) develop a procedure ...
- 3.1 Representation of the Blender Visual State The state of the initial Blender design environment can be decomposed into (1) (2) (k) an “base” Blender state Sbase and ...
- We set each initial program (i) p0 to be a program that concerns a single part of the 3D graphical design (1) workflow – for instance, p0 is ...
- The decomposition of Sinit into Sbase and p10 ...pk0 can be done using techniques like the
