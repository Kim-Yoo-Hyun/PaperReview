# Method

> Evidence maturity: `UNREAD`. 아래 내용은 source cue와 사전 구조화이며, 정독 전에는 paper-supported conclusion으로 인용하지 않는다.

- Year/Venue: 2023 / CoRL
- Category: VLA and Generalist Robot Policies
- Tags: VLA, Vision-Language Model, Robotics
- Paper link: ./2023/CoRL/2023_CoRL_RT-2-Vision-Language-Action-Models-Transfer-Web-Knowledge/paper.pdf
- Code/Project: https://robotics-transformer2.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- We develop a protocol that allows us to run RT-2 models on robots by deploying them in a multi-TPU cloud service and querying this service over the network.
- During co-fine-tuning we balance the ratios of robot and web data in each training batch by increasing the sampling weight on the robot dataset.

## 원리적 동기
- visual concepts from web scale data and low level robot actions during fine-tuning, instead of just robot actions.
- During co-fine-tuning we balance the ratios of robot and web data in each training batch by increasing the sampling weight on the robot dataset.
- We develop a protocol that allows us to run RT-2 models on robots by deploying them in a multi-TPU cloud service and querying this service over the network.

## 핵심 방법론
- UNVERIFIED — full text의 해당 section을 정독한 뒤 근거와 위치를 기록한다.
