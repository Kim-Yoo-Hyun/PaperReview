# Method

- Year/Venue: 2020 / CoRL
- Category: Equivariance, Diffusion, and 3D Action
- Tags: Robotics, Vision-Language Action, equivariance, Imitation Learning
- Paper link: ./2020/CoRL/2020_CoRL_Transporter-Networks-Rearranging-the-Visual-World-for-Robo/paper.pdf
- Code/Project: https://github.com/google-research/ravens
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- In this work, we propose the Transporter Network, a simple model architecture that rearranges deep features to infer spatial displacements from visual input – which can parameterize robot ...
- We validate our methods with hardware in the real world.
- Our method can represent complex multi-modal policy distributions and generalizes to multi-step sequential tasks, as well as 6DoF pick-and-place.

## 원리적 동기
- It is sample efficient in learning complex vision-based manipulation tasks: inserting blocks into fixtures (a), sequential pick-and-place in Towers of Hanoi (c), assembling kits with unseen objects (d), ...
- Our method can represent complex multi-modal policy distributions and generalizes to multi-step sequential tasks, as well as 6DoF pick-and-place.
- In this work, we propose the Transporter Network, a simple model architecture that rearranges deep features to infer spatial displacements from visual input – which can parameterize robot ...

## 핵심 방법론
- Consider the problem of learning pick-and-place actions at with a robot from visual observations ot: f(ot)→at =(Tpick,Tplace)∈A where Tpick is the pose of the end effector used to ...
- Both poses can be defined in SE(2) or SE(3), depending on the task and degrees of freedom available to the
