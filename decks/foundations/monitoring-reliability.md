# Flashcards: Monitoring & Reliability

## Monitoring and Observability

- What is monitoring? == Collecting and checking signals about a system to understand its condition and detect known problems.
- What is observability in software operations? == The ability to understand a system's internal behavior from its emitted signals, including when investigating problems not anticipated in advance.
- What is telemetry? == Data emitted by a system about its behavior, such as logs, metrics, traces, and events.
- What is a dashboard? == A visual collection of signals used to inspect system behavior; it is useful only if the measures and context support decisions.
- What is a health check? == A small automated probe of a component's defined operating condition, such as readiness to receive traffic; its result is only as meaningful as what it checks.
- Why is an application process being alive not enough to prove the service is healthy? == It may still reject requests, produce incorrect results, or be unable to reach a critical dependency.
- What is black-box monitoring? == Checking a system from the outside, such as calling a public endpoint and verifying the response.
- What is white-box monitoring? == Using internal signals such as queue depth, memory usage, and application error counters to understand behavior.

## Logs, Metrics, and Traces

- What is a log? == A timestamped record of an event, often including severity and contextual fields.
- What is structured logging? == Writing log fields in a machine-readable format, such as JSON, so they can be searched and aggregated reliably.
- What is a log level? == A severity category such as debug, info, warning, or error, used to filter and prioritize log events.
- What is a metric? == A numerical measurement recorded over time, usually with dimensions describing the component or operation.
- What is a counter metric? == A cumulative count that normally increases and can reset when a process restarts, such as total requests handled.
- What is a gauge metric? == A value that can increase or decrease, such as active connections or current memory usage.
- What is a histogram metric? == A summary of observations across value ranges, useful for distributions such as request latency or payload size.
- What is a distributed trace? == A record of related operations across a request or workflow, showing their timing and relationships across components.
- What is a span? == One timed operation within a trace, such as a database query or service call, with context and attributes.
- What is a correlation ID? == An identifier carried across related operations so their logs or other records can be connected.
- When are metrics more useful than individual logs? == When detecting aggregate trends or conditions, such as a rising error rate across millions of requests.
- When are traces especially useful? == When locating which dependency or operation caused a particular request to be slow or fail.
- Why should logs and traces avoid secrets and unnecessary personal data? == Telemetry is often copied widely and retained, creating privacy and security risks beyond the original application.

## Useful Service Signals

- What are the four golden signals commonly used in service monitoring? == Latency, traffic, errors, and saturation.
- What is latency? == The time taken to complete a defined operation, measured between explicitly chosen start and end points.
- What is throughput? == The amount of work completed per unit of time, such as successful requests per second.
- What is an error rate? == The proportion of relevant operations classified as failures over a defined window, using an explicit denominator and failure definition.
- What is saturation? == How close a resource is to its effective capacity, often visible through queued work or waiting time.
- Why can average latency hide a serious problem? == A small fraction of very slow requests can badly affect users while the average remains acceptable.
- What does p99 request latency describe? == The latency at or below which approximately 99% of the measured requests fall; about 1% are slower.
- Why should you not simply average p99 values from several servers? == Percentiles are not additive; combine the underlying distribution data or appropriate histogram counts before computing a service-wide percentile.
- Why monitor latency separately for successes and failures? == Fast failures can make overall latency look better while the actual user experience gets worse.
- What is the RED method? == Monitor Rate, Errors, and Duration for request-driven services.
- What is the USE method? == Examine Utilization, Saturation, and Errors for each resource, such as CPU, memory, or storage.
- What is high metric cardinality? == A large number of distinct label combinations, creating many time series and increasing storage and query costs.
- Why are request IDs poor labels for aggregate metrics? == Each request creates another distinct label value; store such detail in logs or traces instead.

## Reliability Targets

- What is service reliability? == The ability to provide the intended service consistently under defined conditions over time, including correctness and timely responses.
- What is availability? == The proportion of time or valid operations for which a service is usable, according to a stated definition.
- What is uptime? == Time during which a system is considered operational; it may differ from user-visible availability if checks are too shallow.
- What is a service level indicator (SLI)? == A measurement of service behavior from a defined perspective, such as the fraction of valid requests that succeed within a latency threshold.
- What is a service level objective (SLO)? == A target for an SLI over a defined period, such as 99.9% successful requests over 30 days.
- What is a service level agreement (SLA)? == An agreement defining service commitments and consequences for missing them, such as contractual service credits.
- SLI versus SLO versus SLA? == The SLI is the measurement, the SLO is the target, and the SLA is the agreement with consequences.
- Why is an SLO usually stricter than the corresponding SLA? == It leaves a safety margin, so the team is alerted and can react before contractual consequences apply.
- What is an error budget? == The amount of unreliability allowed by an SLO; a 99.9% good-event target permits 0.1% bad events over the measurement window.
- What is an error-budget policy? == An agreed response to budget consumption, such as slowing risky releases or prioritizing reliability improvements.
- How much downtime does 99.9% time-based availability allow over exactly 30 days? == 43.2 minutes, because 0.001 × 30 × 24 × 60 = 43.2; request-based SLOs do not translate directly into downtime.
- What is an error-budget burn rate? == The observed bad-event rate divided by the allowed bad-event rate; a value of 10 consumes budget ten times as fast as the sustainable rate at the same traffic level.
- What is multi-window burn-rate alerting? == Alerting only when the burn rate is high over both a long window (e.g. 1 h) and a short one (e.g. 5 min): the long window ignores blips, the short one lets the alert clear soon after recovery.
- Why define reliability targets around user journeys? == Infrastructure health alone can miss failures in the tasks users actually need to complete.

## Alerts and On-Call Work

- What is an alert? == An automated notification that a condition may require attention or action.
- What makes an alert actionable? == It identifies a meaningful problem, reaches an appropriate owner, and suggests a response that can improve the situation.
- What is alert fatigue? == Reduced attention and slower response caused by too many noisy, redundant, or unimportant notifications.
- When should an alert page someone rather than create a ticket? == When a timely human response is required to prevent or limit significant harm; nonurgent work can usually wait in a queue.
- Symptom-based versus cause-based alerting? == Symptom alerts detect user-visible problems; cause alerts detect internal conditions that may explain or predict them.
- Why can sustained SLO violations be better paging signals than a brief CPU spike? == They reflect actual or imminent service harm, while a short resource spike may be harmless.
- What is alert deduplication or grouping? == Combining related notifications so one underlying incident does not overwhelm responders with many separate pages.
- What is a runbook? == A practical guide for diagnosing and handling a recurring operational situation, including safe steps and escalation paths.
- What should an alert message include? == The affected service, observed problem, time and severity, relevant context, and links to a runbook or investigation view.

## Incident Response

- What is an incident? == An unplanned event that disrupts service or threatens its expected reliability, security, or data integrity.
- What is incident severity? == A classification of impact and urgency used to coordinate response; the exact levels are organization-specific.
- What is mitigation during an incident? == Reducing immediate harm, such as disabling a feature or shifting traffic, even before the underlying cause is fully understood.
- Mitigation versus root-cause correction? == Mitigation restores acceptable service quickly; corrective work addresses contributing causes to reduce recurrence.
- What is an incident commander? == The person coordinating priorities, roles, and communication during an incident so responders can work effectively.
- Why maintain an incident timeline? == It records symptoms, decisions, and changes, supporting coordination and later analysis without relying on memory.
- What is a blameless postmortem? == An analysis of what happened and why, focused on system conditions and improvements rather than assigning personal blame.
- What makes a postmortem action item useful? == It addresses a concrete risk and has an owner, a verifiable outcome, and a realistic follow-up date.
- Why should the abbreviation MTTR be defined explicitly? == It can mean mean time to repair, recover, restore, or resolve; comparisons are misleading unless the start and end events match.

## Resilience and Recovery

- What is resilience? == The ability to tolerate disruption and recover while preserving as much useful service as possible.
- What is redundancy? == Having additional components or copies so one failure need not stop the service.
- What is a single point of failure? == A component whose failure alone can make the relevant service unavailable.
- Why does redundancy not guarantee reliability? == Replicas can share failure causes such as a region, configuration error, credential, or corrupted data.
- What is graceful degradation? == Continuing to provide reduced but useful functionality when part of the system fails.
- What is a recovery time objective (RTO)? == The target maximum time to restore a service after a disruption.
- What is a recovery point objective (RPO)? == The target maximum amount of data loss expressed as time, such as losing at most the last 15 minutes of writes.
- What is a synthetic check? == An automated simulated user action run periodically to test a defined service path from a known location or environment.
- Synthetic monitoring versus real-user monitoring? == Synthetic checks use controlled test traffic; real-user monitoring observes actual user experiences, which are broader but less controlled.
- What is chaos engineering? == Controlled experiments that introduce failures to test resilience, with a clear hypothesis, limited impact, monitoring, and stop conditions.
