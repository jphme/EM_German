# German Benchmarks

Based on the `big-refactor` branch of the [Eleuther LLM Evaluation Harness](https://github.com/EleutherAI/lm-evaluation-harness/tree/big-refactor).

After installation these benchmarks can be run with

```python
from lm_eval.tasks import include_task_folder
from lm_eval import evaluator

include_task_folder('.')

results = evaluator.simple_evaluate(
    model='hf-auto',
    model_args='pretrained=jphme/em_german_7b_v01',
    tasks=['wikitext_de','ger_micro_bench','belebele_ger'],
    #limit=5,
    write_out=False,
    log_samples=False,
)
```

I will add example results of the EM models soon.