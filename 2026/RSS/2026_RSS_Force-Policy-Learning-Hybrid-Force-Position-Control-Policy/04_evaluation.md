# Force Policy: Learning Hybrid Force-Position Control Policy under Interaction Frame for Contact-Rich Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. 아래에 인용한 원문 절·표의 평가 조건을 대조했다.
> Source audit: 2026-11-25 원문 방법·평가 대조.

## 평가 조건

그림 3의 전역 정책은 5 Hz로 시각 특징과 행동을 생성한다. 50 Hz의 국소 정책은 손목 영상·말단 자세·힘/토크 이력을 이용해 힘을 제어할 축과 위치를 제어할 축, 목표 힘을 정한다. [PDF 5쪽](https://roboticsproceedings.org/rss22/p128.pdf#page=5)

Flexiv Rizon 4와 손목 6축 힘·토크 센서로 상자 뒤집기, 전기차 충전기 삽입, 스티커 제거를 시험했다(그림 4). [PDF 6쪽](https://roboticsproceedings.org/rss22/p128.pdf#page=6)

표 II의 성공률은 단계별 누적 성공이며 마지막 단계까지 완료해야 과제 성공이다. [PDF 7쪽](https://roboticsproceedings.org/rss22/p128.pdf#page=7)

저자가 설명한 상호작용 좌표계의 범위는 안정된 접촉이다. 공개 체크포인트와 시연의 확인 범위는 상자 뒤집기 과제다. [PDF 8쪽](https://roboticsproceedings.org/rss22/p128.pdf#page=8)

## Proposed Evaluation — Researcher Interpretation

관측과 controller를 맞춘 후 접촉 검출, frame 추정, force regulation의 실패를 각각 계측한다.

이 실험은 실행하지 않았으며, 수치나 결론을 미리 부여하지 않는다.
