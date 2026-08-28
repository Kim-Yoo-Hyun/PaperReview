# Problem — DIGIT: A Novel Design for a Low-Cost Compact High-Resolution Tactile Sensor with Application to In-Hand Manipulation

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2020 / IEEE Robotics and Automation Letters
- Category: Manipulation, Contact, and Dexterity
- Tags: Robotics, tactile sensing, dexterous manipulation, contact
- Official paper: https://doi.org/10.1109/LRA.2020.2977257
- Code/Project: https://digit.ml/
- Source audit: publisher metadata, abstract, and official project page checked; hardware details remain UNVERIFIED.

## Target Problem and Assumptions

multi-finger/in-hand manipulation에 탑재 가능한 작고 저렴한 고해상도 tactile sensor가 필요하다.

## Closed-Loop Position

finger contact image stream을 tactile perception/policy input으로 제공한다.

## Audit Questions

정독 시 가정이 실제 robot dynamics, partial observability, contact와 distribution shift에서 유지되는지 확인한다.
