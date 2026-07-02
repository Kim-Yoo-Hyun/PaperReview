# Method

- Year/Venue: 2026 / ICML
- Category: Navigation and Embodied AI
- Tags: Navigation, Reinforcement Learning
- Paper link: ./2026/ICML/2026_ICML_Plan-in-Sandbox-Navigate-in-Open-Worlds-Learning-Physics-G/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- These sub-goals are subsequently executed by • We introduce a novel Generative Experience-Driven Learning paradigm to address the severe data scarcity and real-world transfer challenges in embodied navigation. ...
- To this end, we propose Sandbox-Abstracted Grounded Experience (SAGE), a framework that enables agents to learn within a physics-grounded semantic abstraction rather than a photorealistic simulation, mimicking the ...
- To mitigate this issue, we propose an Asymmetric Adaptive Clipping (AAC) strategy.

## 원리적 동기
- Although the research community has turned to Reinforcement Learning (RL) to facilitate policy adaptation (Zeng et al., 2024; Choi et al., 2024; Wang & Huang, 2025) from highlevel ...
- Problem Formulation We formulate the learning problem via three core components: (1) a physics-grounded semantic sandbox S, which provides an environment ES ; (2) an unknown target task ...
- These sub-goals are subsequently executed by • We introduce a novel Generative Experience-Driven Learning paradigm to address the severe data scarcity and real-world transfer challenges in embodied navigation. ...

## 핵심 방법론
- This confirms that our approach effectively mitigates the dependency on massive datasets, paving a scalable avenue for enhancing navigation policies by integrating abundant, low-cost sandbox tasks.
- Training via Genesis and Evolution (+G.&E.) boosts A-EQA SR† by 6.29% over the zero-shot baseline, Sparse Observation vs.
- An optimally relaxed bound (ϵexp = 1.0) balances this, enabling rapid experience absorption without policy collapse, achieving a peak SR† of 53.21% and SPL† of 37.07% at 150 ...
