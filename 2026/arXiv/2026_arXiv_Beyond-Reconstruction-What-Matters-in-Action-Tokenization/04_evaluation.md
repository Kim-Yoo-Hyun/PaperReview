# Evaluation — Beyond Reconstruction: What Matters in Action Tokenization for Robot Policies?

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 지정 본문 절만 확인; 전체 정독·재현 아님.

## Paper-Supported Evaluation Scope

22개 tokenizer 설정과 Robomimic·LIBERO·RoboTwin, VLA·실제 로봇 평가를 보고한다. Appendix C.3은 tokenization 없는 flow policy까지 horizon 대조에 포함한다.

## Interpretation Boundary

일반 reconstruction/control 불일치와 horizon 효과는 이미 다룬다. Code soon으로 표기되어 실행 검증되지 않았다. 저자 NeurIPS 표기는 exact 공식 listing을 확인하지 못해 arXiv 유지.

## Reproduction Status

이번 작업의 정책 실행·학습은 0회다. 위에서 명시하지 않은 dataset 크기·split·trial·hardware·metric·baseline 수치는 미기록이며 논문 자체의 미보고를 뜻하지 않는다. Resource 자동 연결은 cue_only다.

근거: [확인한 원문](https://arxiv.org/pdf/2610.09170v1), §1, §4, §6, Appendix B.2/C.3.
