# Method

- Year/Venue: 2021 / ICRA
- Category: Manipulation, Contact, and Dexterity
- Tags: Robotics, deformable object, cable manipulation, cloth manipulation, goal-conditioned learning, vision-based control
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://sites.google.com/view/berkeley-deformable/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Brief Method
- We propose embedding goal-conditioning into Transporter Networks, a recently proposed model architecture for learning robotic manipulation that rearranges deep features to infer displacements that can represent pick and ...
- In this work, we propose a new suite of benchmark tasks, called DeformableRavens, to test manipulation of cables, fabrics, and bags spanning 1D, 2D, and 3D deformables.
- For several tasks in the benchmark, we propose to tackle them using novel goal-conditioned va GT-State MLP GT-State MLP 2-Step Transporter cable-ring-notarget GT-State MLP GT-State MLP 2-Step Transporter ...

## 원리적 동기
- — Rearranging and manipulating deformable objects such as cables, fabrics, and bags is a long-standing challenge in robotic manipulation.
- I NTRODUCTION Manipulating deformable objects is a long-standing challenge in robotics with a wide range of real-world applications.
- We propose embedding goal-conditioning into Transporter Networks, a recently proposed model architecture for learning robotic manipulation that rearranges deep features to infer displacements that can represent pick and ...

## 핵심 방법론
- GT-State MLP GT-State MLP 2-Step Transporter cable-ring-notarget GT-State MLP GT-State MLP 2-Step Transporter 1 10 100 1000 1 10 100 1000 1 10 100 1000 1 10 100 ...
- On bagalone-open, Transporter attains performance of 61.7% and 63.3% with 100 and 1000 demos, which is comparable to the scripted demonstrator performance of 60.2% (1000 successes out of ...
- Similarly, on bag-items-1 and bag-items-2, the best raw performance numbers (with
