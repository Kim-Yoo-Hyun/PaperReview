# Problem

- Year/Venue: 2026 / CVPR
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, Chain-of-Thought, Planning
- Paper link: ./2026/CVPR/2026_CVPR_ACoT-VLA-Action-Chain-of-Thought-for-Vision-Language-Actio/paper.pdf
- Code/Project: not identified from primary page
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- Sub-tasks Vision-Language-Action models have emerged as essential generalist robot policies for diverse manipulation tasks, conventionally relying on directly translating multimodal inputs into actions via Vision-Language Model embeddings.
- Recent advancements have introduced explicit intermediary reasoning—such as sub-task prediction (language) or goal image synthesis (vision)—to guide action generation.
- However, these intermediate reasoning are often indirect and inherently limited in their capacity to convey the full, granular information required for precise action execution.

## 해결하려는 문제
- In this paper, we propose ACoT-VLA, a novel architecture that materializes the ACoT paradigm.
- Extensive experiments in real-world and simulation environments demonstrate the superiority of our proposed method.
- We introduce Action Chain-of-Thought (ACoT), a paradigm where the reasoning process itself is formulated as a structured sequence of coarse action intents that guide the final policy.

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
