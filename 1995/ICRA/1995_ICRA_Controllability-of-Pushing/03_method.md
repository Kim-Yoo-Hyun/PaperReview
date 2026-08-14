# Method

- Year/Venue: 1995 / ICRA
- Category: Robotics Foundations: Contact and Whole-Body Control
- Tags: Robotics, contact-rich manipulation, pushing, controllability
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: not released
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Brief Method
- For the case of line contact, we find a set of pushing directions that keep the object fixed to the pusher, and we use these pushing directions to ...

## 원리적 동기
- For the quasi-static pushing problem, we are only concerned with force and velocity directions, not their magnitudes.
- If the object is too large to be grasped or too heavy to be carried, however, this approach fails.
- For the case of line contact, we find a set of pushing directions that keep the object fixed to the pusher, and we use these pushing directions to ...

## 핵심 방법론
- A robotic manipulator is often required to move an object from one place to another.
- An obvious solution is to equip the manipulator with a gripper and adopt the pick-and-place approach.
- By designing the grasp to resist all forces that could reasonably act on the object during the motion, grasp planning and path planning can be decoupled.
- If the object is too large to be grasped or too heavy to be carried, however, this approach fails.
- It underutilizes the resources available to the robot, as it considers only the control forces that can be statically applied at the gripper.
