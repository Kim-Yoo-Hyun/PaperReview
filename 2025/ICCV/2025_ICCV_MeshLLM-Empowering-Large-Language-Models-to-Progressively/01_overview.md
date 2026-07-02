# MeshLLM: Empowering Large Language Models to Progressively Understand and Generate 3D Mesh

- Year/Venue: 2025 / ICCV
- Category: 3D Large Multimodal Models
- Tags: 3D Vision
- Paper link: ./2025/ICCV/2025_ICCV_MeshLLM-Empowering-Large-Language-Models-to-Progressively/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Our approach addresses key limtext-serialized Default: #CAE9F3 itations in existing methods, including the limited dataset scale when catering to LLMs’ token length and the loss of 3D structural ...
- With the rapid development of virtual reality and robotic interaction, equipping LLMs with 3D perception and spatial reasoning capabilities has become a pressing challenge.
- Against this backdrop, existing research has attempted to integrate LLMs with 3D data .

## Core Idea
- Furthermore, we propose inferring face connectivity from vertices and local mesh assembly training strategies, significantly enhancing the LLMs’ ability to capture mesh topology and spatial structures.
- Building on the constructed dataset, we propose a structured training paradigm that models meshes hierarchically from vertices to faces and mesh assembly, enabling LLMs to effectively perceive the ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Experiments show that MeshLLM outperforms the state-of-the-art LLaMA-Mesh in both mesh generation quality and shape understanding, highlighting its great potential in processing text-serialized 3D meshes.
- In recent years, large language models (LLMs), exemplified by the GPT series, have achieved groundbreaking advancements.
- While these methods have demonstrated a sword a sword 31k Full Mesh 1500k training LLaMA-Mesh Primitive-Mesh v f assembly Mesh LLM text-mesh alignment training Figure 2.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Experiments show that MeshLLM outperforms the state-of-the-art LLaMA-Mesh in both mesh generation quality and shape understanding, highlighting its great potential in processing text-serialized 3D meshes.
- Furthermore, we propose inferring face connectivity from vertices and local mesh assembly training strategies, significantly enhancing the LLMs’ ability to capture mesh topology and spatial structures.
- While these methods have demonstrated a sword a sword 31k Full Mesh 1500k training LLaMA-Mesh Primitive-Mesh v f assembly Mesh LLM text-mesh alignment training Figure 2.

## Abstract Cue
- Introduction We present MeshLLM, a novel framework that leverages large language models (LLMs) to understand and generate All mesh 3D meshes.
