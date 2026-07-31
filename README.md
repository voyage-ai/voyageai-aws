# voyageai-aws

Notebooks and sample payloads for deploying VoyageAI models via AWS SageMaker.

> [!WARNING]
> **`deploy_voyage_model_package_sagemaker.ipynb` is deprecated.** It covers the older model catalogue (the voyage-3 and voyage-2 families, `rerank-2`) and does not receive new models. Use **`deploy_mongodb_voyage_model_package_sagemaker.ipynb`** for all current deployments.

## Docs

- https://www.mongodb.com/docs/voyageai/management/aws-marketplace/
- https://docs.voyageai.com/docs/aws-marketplace-mongodb-voyage

## Model support

Models available through `deploy_mongodb_voyage_model_package_sagemaker.ipynb`.

| Model | Real-time endpoint | Batch transform |
|---|---|---|
| voyage-4 | Yes | Yes |
| voyage-4-lite | Yes | Yes |
| voyage-4-large | Yes | No (1) |
| voyage-3.5, voyage-3.5-lite | Yes | Yes |
| voyage-3-large, voyage-code-3 | Yes | Yes |
| voyage-context-3 | Yes | Yes |
| voyage-context-4 | Yes | No (1) |
| voyage-multimodal-3.5, voyage-multimodal-3 | Yes | Yes |
| rerank-2.5, rerank-2.5-lite | Yes | No (2) |

1. Requires a GPU family AWS does not offer for [batch transform jobs](https://docs.aws.amazon.com/sagemaker/latest/dg/batch-transform.html) (G7e class or above). Real-time endpoints only until AWS extends batch transform hardware support.
2. Reranking scores candidates against a query at request time, so it is a real-time operation. Batch transform is not offered for rerankers.

### Batch transform configuration

Batch transform jobs must use `BatchStrategy="SingleRecord"` with `SplitType="Line"` and JSON Lines input (`application/jsonlines`), one complete request per line. `MultiRecord` batching, other split types, and other content types such as CSV are not supported. See [CreateTransformJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTransformJob.html) and [TransformInput](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TransformInput.html) for the full set of AWS options.

## Development

Linting/formatting is handled by [pre-commit](https://pre-commit.com/):

```
pip install pre-commit
pre-commit install
```

Hooks then run automatically on `git commit`. To run them manually against all files:

```
pre-commit run --all-files
```
