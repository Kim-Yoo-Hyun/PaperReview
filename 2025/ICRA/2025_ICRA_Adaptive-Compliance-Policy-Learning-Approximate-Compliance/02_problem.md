# Problem — Adaptive Compliance Policy: Learning Approximate Compliance for Diffusion Guided Control

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-25 · 저자판 PDF 3–6쪽, §III–IV, Tables I–II 확인. [서지·게재 상태](https://api.crossref.org/works/10.1109/ICRA55743.2025.11128452)

## 문제와 검증 범위

접촉 작업에서는 같은 위치를 지나더라도 물체에 가해야 할 힘이 달라진다. 사람이 시연한 위치·힘으로부터 로봇의 목표 운동과 접촉 방향 강성을 함께 학습할 수 있는지 묻는다.

실물에서 물체 뒤집기와 꽃병 닦기를 시험했다. 뒤집기 Table I의 다섯 조건, 방법당 총 100회에서 ACP는 96회, 균일 강성의 compliant policy는 23회 성공했다. 꽃병 닦기는 Table II에 따로 보고했다. [원문 및 평가 절](https://arxiv.org/pdf/2410.09309v2#page=4)
