# Method

- Year/Venue: 2024 / RSS
- Category: Manipulation, Contact, and Dexterity
- Tags: Robotics, contact-rich manipulation, convex relaxation, trajectory optimization
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://www.roboticsproceedings.org/rss20/p132.html
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Brief Method
- This highlights a key advantage of our approach: by reasoning on a global level, our method (empirically) always finds a solution, without relying on an initial guess.
- — We present a novel method for global motion planning of robotic systems that interact with the environment through contacts.
- C ONCLUSION AND F UTURE W ORK In this work, we present a framework for planning nearglobally optimal trajectories for contact-rich systems.

## 원리적 동기
- Approaches that blend the discrete and continuous components often do so locally (around a given trajectory) and are unable to reason about the global problem; or rely on ...
- We formulate the motion-planning problem as a shortest-path problem in a graph of convex sets, where a path in the graph corresponds to a contact sequence and a ...
- This highlights a key advantage of our approach: by reasoning on a global level, our method (empirically) always finds a solution, without relying on an initial guess.

## 핵심 방법론
- This highlights a key advantage of our approach: by reasoning on a global level, our method (empirically) always finds a solution, without relying on an initial guess.
- C ONCLUSION AND F UTURE W ORK In this work, we present a framework for planning nearglobally optimal trajectories for contact-rich systems.
- With a cost function that is specifically tuned to optimize the baseline’s performance, our method finds a solution in 100% of the instances for both slider geometries.
- While these problems can certainly be addressed by e.g. finer trajectory discretization, velocity constraints, or tuning, these issues are naturally handled in our method, which guarantees that the ...
- We are currently working on applying our method to more complex contact tasks.
