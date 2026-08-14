# Problem

> Evidence maturity: `UNREAD`. 아래 내용은 source cue와 사전 구조화이며, 정독 전에는 paper-supported conclusion으로 인용하지 않는다.

- Year/Venue: 2020 / RA-L
- Category: World Models, Safety, and Recovery
- Tags: Robotics, safe reinforcement learning, recovery policy, real robot
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://sites.google.com/berkeley.edu/recovery-rl/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## 왜 문제인가
- —Safety remains a central obstacle preventing widespread use of RL in the real world: learning new tasks in uncertain environments requires extensive exploration, but safety requires limiting exploration.
- We propose Recovery RL, an algorithm which navigates this tradeoff by (1) leveraging offline data to learn about constraint violating zones before policy learning and (2) separating the ...
- We evaluate Recovery RL on 6 simulation domains, including two contact-rich manipulation tasks and an imagebased navigation task, and an image-based obstacle avoidance task on a physical robot.

## 해결하려는 문제
- We propose Recovery RL, an algorithm which navigates this tradeoff by (1) leveraging offline data to learn about constraint violating zones before policy learning and (2) separating the ...
- Results suggest that Recovery RL trades off constraint violations and task successes 2 - 20 times more efficiently in simulation domains and 3 times more efficiently in physical ...
- We compare Recovery RL to 5 prior safe RL methods which jointly optimize for task performance and safety via constrained optimization or reward shaping and find that Recovery ...

## 선행 연구 / 배경 단서
- UNVERIFIED — full text의 해당 section을 정독한 뒤 근거와 위치를 기록한다.
