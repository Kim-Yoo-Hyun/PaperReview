# Method

- Year/Venue: 2023 / NeurIPS
- Category: Benchmarks and Datasets
- Tags: Robotics, Imitation Learning, Benchmark
- Paper link: ./2023/NeurIPS/2023_NeurIPS_Benchmarking-Knowledge-Transfer-for-Lifelong-Robot-Learnin/paper.pdf
- Code/Project: https://libero-project.github.io/main.html
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- Our extensive experiments present several insightful or even unexpected discoveries: sequential finetuning outperforms existing lifelong learning methods in forward transfer, no single visual encoder architecture excels at all ...
- Specifically, LIBERO highlights five key research topics in LLDM: 1) how to efficiently transfer declarative knowledge, procedural knowledge, or the mixture of both; 2) how to design effective ...
- To advance research in LLDM, we introduce LIBERO, a novel benchmark of lifelong learning for robot manipulation.

## 원리적 동기
- Consider a scenario where a robot, initially trained to retrieve juice from a fridge, fails ∗
- Our extensive experiments present several insightful or even unexpected discoveries: sequential finetuning outperforms existing lifelong learning methods in forward transfer, no single visual encoder architecture excels at all ...
- Our extensive experiments present several insightful or even unexpected discoveries: sequential finetuning outperforms existing lifelong learning methods in forward transfer, no single visual encoder architecture excels at all ...

## 핵심 방법론
- A longstanding goal in machine learning is to develop a generalist agent that can perform a wide range of tasks.
- While multitask learning is one approach, it is computationally demanding and not adaptable to ongoing changes.
- Lifelong learning , however, offers a practical solution by amortizing the learning process over the agent’s lifespan.
- Its goal is to leverage prior knowledge to facilitate learning new tasks (forward transfer) and use the newly acquired knowledge to enhance performance on prior tasks (backward transfer).
- The main body of the lifelong learning literature has focused on how agents transfer declarative knowledge in visual or language tasks, which pertains to declarative knowledge about entities ...
