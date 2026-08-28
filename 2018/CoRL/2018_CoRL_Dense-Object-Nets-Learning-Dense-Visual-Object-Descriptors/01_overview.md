# Dense Object Nets: Learning Dense Visual Object Descriptors By and For Robotic Manipulation

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2018 / CoRL
- Category: Robotics-Enabling 3D Perception
- Tags: Robotics, manipulation, Dense Descriptors, representation learning
- Official paper: https://proceedings.mlr.press/v87/florence18a.html
- Code/Project: https://dense-object-nets.github.io/
- Source audit: official proceedings abstract and project page checked; training/evaluation details remain UNVERIFIED.

## Why This Paper Is Here

object-centric dense correspondence를 manipulation control에 연결한 대표 representation-learning foundation이다.

## Problem

texture·view 변화에도 물체 표면의 task-relevant point correspondence를 얻는다.

## Core Idea

self-supervised multi-view RGB-D data로 pixel-level dense descriptors를 학습하고 correspondence 기반 manipulation을 수행한다.

## Interface

camera observation을 object surface descriptor/correspondence로 변환해 grasping·manipulation target을 제공한다.

## Evaluation Scope

real-robot manipulation과 correspondence 품질이 평가되며 exact objects/tasks는 정독 후 확정한다.
