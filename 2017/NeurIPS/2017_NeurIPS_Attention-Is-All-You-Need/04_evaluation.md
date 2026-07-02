# Evaluation

- Year/Venue: 2017 / NeurIPS
- Category: Foundations: Transformer and Language Models
- Tags: LLM, Transformer, representation
- Paper link: ./2017/NeurIPS/2017_NeurIPS_Attention-Is-All-You-Need/paper.pdf
- Code/Project: https://github.com/tensorflow/tensor2tensor
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- WMT 2014

## Metrics
- BLEU
- accuracy

## Evaluation Protocol and Results
- On the WMT 2014 English-to-French translation task, our big model achieves a BLEU score of 41.0, outperforming all of the previously published single models, at less than 1/4 ...
- 6.1 Machine Translation On the WMT 2014 English-to-German translation task, the big transformer model (Transformer (big) in Table 2) outperforms the best previously reported models (including ensembles) by ...
- 6.2 Model Variations To evaluate the importance of different components of the Transformer, we varied our base model in different ways, measuring the change in performance on English-to-German ...
- On the WMT 2014 English-to-French translation task, our big model achieves a BLEU score of 41.0, outperforming all of the previously published single models, at less than 1/4 ...
- Our model achieves 28.4 BLEU on the WMT 2014 Englishto-German translation task, improving over the existing best results, including ensembles, by over 2 BLEU.

## Baselines
- On the WMT 2014 English-to-French translation task, our big model achieves a BLEU score of 41.0, outperforming all of the previously published single models, at less than 1/4 ...
- Even our base model surpasses all previously published models and ensembles, at a fraction of the training cost of any of the competitive models.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
