# voyageai-aws

Notebooks and sample payloads for deploying VoyageAI models via AWS SageMaker.

## Docs

- https://www.mongodb.com/docs/voyageai/management/aws-marketplace/
- https://docs.voyageai.com/docs/aws-marketplace-mongodb-voyage

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
