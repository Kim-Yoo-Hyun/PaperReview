# Method

- Year/Venue: 2025 / NeurIPS
- Category: World Models, Safety, and Recovery
- Tags: Robotics, VLA, failure detection, conformal prediction, uncertainty
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://vla-safe.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Brief Method
- In this paper, we introduce the multitask failure detection problem and propose SAFE, a failure detector for generalist robot policies such as VLAs.
- We use uppert as the failure flag threshold δt , and more details about functional CP can be found in Appendix.
- For fMLP , we use an MLP g(·) to project et into a single scalar for each P timestep t independently and accumulate the outputs as the failure ...

## 원리적 동기
- In this paper, we focus on the multitask failure detection problem.
- To tackle this problem, we study the internal features of VLAs and find that they capture high-level knowledge about task success and failure.
- In this paper, we introduce the multitask failure detection problem and propose SAFE, a failure detector for generalist robot policies such as VLAs.

## 핵심 방법론
- We use uppert as the failure flag threshold δt , and more details about functional CP can be found in Appendix.
- For fMLP , we use an MLP g(·) to project et into a single scalar for each P timestep t independently and accumulate the outputs as the failure ...
- For fLSTM , we use an LSTM model to sequentially process the input stream of VLA’s features e0:t and project the hidden state vector of LSTM into a ...
- Calibrate failure detection threshold and deploy Action: 𝑨𝑡 SAFE-MLP 𝑠1 Decoder 𝑠ǁ1 𝒆𝑡 MLP MLP MLP MLP 𝒆1 𝒆2 𝒆3 𝒆𝑇 SAFE-LSTM 𝑠1 𝑠2 𝑠3 𝑠𝑇 LSTM LSTM ...
