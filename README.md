# RemNote Decks

English-language flashcards for software engineering, statistics, and AI. Each Markdown file is a standalone deck using RemNote's `Question == Answer` format.

## Organization

- [`decks/foundations/`](decks/foundations/): everyday software-engineering concepts, from smoke tests to Git and databases.
- [`decks/statistics/`](decks/statistics/): statistical reasoning, product experiments, and ML evaluation metrics.
- [`decks/ai/`](decks/ai/): LLM internals, applications, evaluation, and operations.

## Deck Index

### Software Engineering Foundations

| Deck | Topics | Cards |
| --- | --- | ---: |
| [Software Testing & QA](decks/foundations/software-testing-qa.md) | Smoke and regression tests, test levels, mocks, coverage, performance testing | 71 |
| [Deployment & Releases](decks/foundations/deployment-releases.md) | CI/CD, environments, canaries, blue-green deployments, feature flags, rollback | 67 |
| [Monitoring & Reliability](decks/foundations/monitoring-reliability.md) | Logs, metrics, traces, SLI/SLO/SLA, alerts, incidents, recovery | 76 |
| [APIs & Web Fundamentals](decks/foundations/apis-web-fundamentals.md) | HTTP, JSON, status codes, REST, authentication, OAuth, webhooks, idempotency | 77 |
| [Software Architecture & Distributed Systems](decks/foundations/software-architecture-distributed-systems.md) | Monoliths, services, queues, caching, scaling, retries, distributed state | 74 |
| [Databases & Data Storage](decks/foundations/databases-data-storage.md) | SQL/NoSQL, joins, indexes, ACID, isolation, migrations, replication, backups | 80 |
| [Git & Collaboration](decks/foundations/git-collaboration.md) | Commits, branches, pull requests, merge/rebase, conflicts, revert/reset | 81 |

### Statistics and Experiments

| Deck | Topics | Cards |
| --- | --- | ---: |
| [Statistics & Experiment Design](decks/statistics/statistics-experiment-design.md) | Probability, confidence intervals, hypothesis tests, power, bootstrap, causality | 87 |
| [A/B Testing & Product Experiments](decks/statistics/ab-testing-experiments.md) | Assignment, metrics, instrumentation, duration, SRM, analysis, ship decisions | 66 |
| [ML Evaluation Metrics](decks/statistics/metrics.md) | Classification, regression, ranking, generative models, evaluation methodology | 109 |

**Scope:** Statistics & Experiment Design teaches the methods and their interpretation. A/B Testing & Product Experiments applies those ideas to running trustworthy product experiments. ML Evaluation Metrics focuses on measuring model performance.

### AI and LLMs

| Deck | Topics | Cards |
| --- | --- | ---: |
| [Transformer & LLM Internals](decks/ai/transformer-internals.md) | Attention, architectures, tokenization, training objectives, scaling | 93 |
| [Retrieval-Augmented Generation](decks/ai/rag.md) | Chunking, embeddings, retrieval, reranking, grounding, evaluation | 93 |
| [Agents & Tool Use](decks/ai/agents-tool-use.md) | Planning, tool calling, structured outputs, MCP, memory, permissions | 86 |
| [Fine-Tuning & Alignment](decks/ai/fine-tuning-alignment.md) | SFT, LoRA/QLoRA, preference learning, RLHF, reasoning | 97 |
| [LLM Inference & Serving](decks/ai/inference-serving.md) | KV cache, batching, quantization, parallelism, latency, cost | 89 |
| [LLM Evals](decks/ai/llm-evals.md) | Evaluation datasets, judges, benchmarks, regression checks | 90 |
| [LLMOps & Observability](decks/ai/llmops-observability.md) | OpenTelemetry, tracing, production metrics, prompt management | 81 |
| [LLM Security](decks/ai/llm-security.md) | Prompt injection, leakage, poisoning, guardrails, red teaming | 91 |

## Suggested Starting Points

- **Everyday engineering vocabulary:** Testing → Git → APIs → Databases → Architecture → Deployment → Monitoring.
- **Understanding experiments:** Statistics & Experiment Design → A/B Testing & Product Experiments.
- **Measuring AI systems:** ML Evaluation Metrics → LLM Evals, then the relevant application deck.

You can study decks independently. Each concept has one home deck; other decks only add cards that look at it from a different angle (for example, GQA is defined in Transformer & LLM Internals, while LLM Inference & Serving asks why it speeds up decoding).

## Using the Decks in RemNote

1. Open a deck's raw Markdown source rather than copying a rendered table or the index above.
2. Copy the deck text into a RemNote document, or use RemNote's import feature for the supported text/Markdown format.
3. Check that the question and answer sides of a few cards were recognized correctly before importing the rest of your collection.

Example source:

```markdown
# Flashcards: Example

## Testing

- What is a smoke test? == A short check that critical functionality works well enough for further testing or use.
```

RemNote recognizes `==` or `>>` as the separator for a basic forward flashcard. See the official [text-import guide](https://help.remnote.com/en/articles/9252072-how-to-import-flashcards-from-text). These files follow that syntax; an in-app import is not part of the repository checks.

## Adding or Editing Cards

- Put each deck in the most relevant existing category; create a new category only when needed.
- Use lowercase, hyphen-separated filenames and a single `# Flashcards: ...` title.
- Group related cards under `##` headings.
- Keep each card on one line: `- Question? == Answer.`
- Prefer one learning target per card; include comparison and application questions as well as definitions.
- State important assumptions and limitations rather than teaching misleading absolutes.
- Keep cards understandable without relying on their order in a study session.
- Before adding a card, search the other decks; don't repeat a question that already has a home deck.
- Use `×` for multiplication, never the letter `x`.
- Update the index and card count when adding or changing a deck.
- Run `python3 scripts/check_decks.py` to check card format, duplicate questions across decks, and the README card counts.

## Visual Cards (Pilot)

[`pilot/visual-pilot.md`](pilot/visual-pilot.md) tests image and LaTeX cards before they go into the decks. RemNote's Markdown import resolves relative image paths only inside a zip file, so import the pilot as a zip instead of pasting it:

```sh
cd pilot && zip -r ../remnote-visual-pilot.zip visual-pilot.md images
```

The images are generated by [`scripts/make_images.py`](scripts/make_images.py): `uv run scripts/make_images.py`.

## Selected References

- [MDN: HTTP idempotency](https://developer.mozilla.org/en-US/docs/Glossary/Idempotent)
- [MDN: Cross-Origin Resource Sharing](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS)
- [Microsoft Research: Diagnosing Sample Ratio Mismatch in A/B Testing](https://www.microsoft.com/en-us/research/articles/diagnosing-sample-ratio-mismatch-in-a-b-testing/)
- [Microsoft Research: Patterns of Trustworthy Experimentation — During-Experiment Stage](https://www.microsoft.com/en-us/research/articles/patterns-of-trustworthy-experimentation-during-experiment-stage/)
