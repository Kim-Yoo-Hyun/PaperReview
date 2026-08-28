# Impedance Control: An Approach to Manipulation: Part I—Theory

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 1985 / Journal of Dynamic Systems, Measurement, and Control
- Category: Robotics Foundations: Contact and Whole-Body Control
- Tags: Robotics, Impedance Control, contact, manipulation
- Official paper: https://doi.org/10.1115/1.3140702
- Code/Project: not identified
- Source audit: publisher metadata and abstract checked; stability derivations remain UNVERIFIED.

## Why This Paper Is Here

로봇-환경 상호작용을 단순 위치 오차가 아니라 desired mechanical impedance로 설계하는 핵심 contact-control foundation이다.

## Problem

uncertain environment와 접촉할 때 motion 또는 force 하나만 직접 추종해서는 robust interaction을 만들기 어렵다는 문제를 다룬다.

## Core Idea

motion과 interaction force 사이의 목표 동적 관계를 inertia-damping-stiffness 형태로 설계한다.

## Interface

pose/velocity와 external wrench feedback을 actuation으로 매핑하는 low-level interaction-control 계층이다.

## Evaluation Scope

Part I은 이론 정립이 중심이며 구현·하드웨어 범위는 후속 part와 함께 확인해야 한다.
