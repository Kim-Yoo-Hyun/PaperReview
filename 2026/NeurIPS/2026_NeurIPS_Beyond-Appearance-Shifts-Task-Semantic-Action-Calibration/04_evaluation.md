# Evaluation — Beyond Appearance Shifts: Task-Semantic Action Calibration for VLA Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 지정 본문 절만 확인; 전체 정독·재현 아님.

## Paper-Supported Evaluation Scope

LIBERO와 실제 로봇에서 clean/control 및 changed-task 결과를 분리한다. Table 7의 easy swaps 800회에서 New 548, Old 0, Other 252를 보고한다. Table 13은 destination·relation·order 변경도 평가한다.

## Interpretation Boundary

Break 열은 옛 목표 성공률이므로 낮다고 새 목표 성공이 아니다. Margin 분리만으로 물리적 성공이 보장되지 않는다. 최종 proceedings와 읽은 v1의 동일성·공개 구현은 미확인.

## Reproduction Status

이번 작업의 정책 실행·학습은 0회다. 위에서 명시하지 않은 dataset 크기·split·trial·hardware·metric·baseline 수치는 미기록이며 논문 자체의 미보고를 뜻하지 않는다. Resource 자동 연결은 cue_only다.

근거: [확인한 원문](https://arxiv.org/html/2609.23650v1), §3–4, §5.1–5.3, Tables 6–7, Appendix A.2.1.
