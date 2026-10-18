# Flashcards: A/B Testing & Product Experiments

## Purpose and Basic Concepts

- What is an A/B test? == A controlled experiment that randomly assigns units to variants and compares predefined outcomes to estimate the effect of a change.
- What are the control and treatment groups? == The control receives the reference experience; the treatment receives the change being evaluated.
- What kinds of changes can be evaluated with an A/B test? == Product changes such as a checkout flow, ranking algorithm, email, or price, provided assignment and outcome measurement support a valid comparison.
- Why is a before-and-after comparison weaker than a randomized A/B test? == Seasonality, user mix, marketing, and other changes can explain a time-based difference; concurrent randomization helps separate these from the treatment effect.
- How does an A/B test differ from a canary release? == An A/B test primarily estimates a change's effect; a canary release primarily limits rollout risk. A canary is not automatically a valid randomized experiment.
- How does an A/B test differ from usability testing? == An A/B test measures outcome differences across assigned groups; usability testing observes how people interact with a product to uncover problems and explanations.
- What is an A/A test? == An experiment assigning users to equivalent experiences to check the assignment, measurement, and analysis pipeline.
- Should a valid A/A test always be non-significant? == No; a calibrated test can still produce false positives at its stated rate. Repeated anomalies are a reason to investigate.

## Hypotheses and Success Criteria

- What should an experiment hypothesis specify? == The target population, proposed change, expected mechanism, and measurable outcome, including the expected direction when justified.
- What is a primary metric? == The main outcome used for the prespecified experiment decision, such as purchases per eligible user.
- Why choose a primary metric before running the experiment? == It prevents selecting whichever metric happens to improve and keeps the decision aligned with the original goal.
- What is a guardrail metric? == An outcome that should not deteriorate beyond an acceptable threshold, such as errors, latency, cancellations, or user complaints.
- What is a diagnostic metric? == A supporting measure used to understand mechanisms, such as button clicks or funnel steps, rather than automatically deciding whether to ship.
- Why can optimizing click-through rate harm the product? == More clicks may come from confusion or clickbait without improving task completion, purchases, or long-term satisfaction.
- What is a practical significance threshold? == The smallest benefit or largest harm that matters for the business or users, defined separately from a statistical significance cutoff.
- What belongs in an experiment plan? == Hypothesis, eligibility, randomization unit, variants, metrics, sample-size assumptions, duration, analysis method, stopping rules, and rollout criteria.

## Assignment and Exposure

- What is the randomization unit? == The entity assigned to a variant, such as a user, household, organization, or geographic region.
- How should the randomization unit be chosen? == Match it to the experience and likely spillovers; use larger units when users influence one another, while accounting for reduced statistical efficiency.
- What is sticky assignment? == Keeping an eligible unit in the same variant throughout the experiment, rather than randomly changing its experience on each visit.
- Why is request-level randomization risky for a multi-step user flow? == One person may see both variants, causing inconsistent experiences, carryover, and correlated observations.
- How can deterministic hashing support random assignment? == Hash a stable unit ID with an experiment-specific salt and map the result into allocation buckets, using a well-distributed hash and stable configuration.
- Why use an experiment-specific salt for bucketing? == It avoids unintentionally assigning the same users to the same arms across unrelated experiments.
- Assignment versus exposure? == Assignment selects a variant; exposure means the unit actually encounters the relevant experience. Both can matter for instrumentation and interpretation.
- Why define experiment eligibility before treatment can affect it? == Selecting users based on treatment-influenced behavior can make the comparison groups systematically different.
- Why can cross-device use complicate a user-level experiment? == One person may receive different assignments under separate device IDs; stable identity can reduce contamination but must respect privacy constraints.

## Metrics and Instrumentation

- What must an experiment event identify? == Enough information to connect a valid event to its unit, experiment, variant, event time, and outcome, using privacy-appropriate identifiers.
- What is a conversion rate in an experiment? == The proportion of eligible units meeting a specified conversion definition within a defined observation window.
- Why must a conversion metric define its denominator? == Conversions per visitor, session, or exposed user answer different questions and can move differently under the same treatment.
- Why define an outcome observation window? == Users need comparable time to produce an outcome; late entrants otherwise have less opportunity to convert or return.
- What is a delayed outcome? == A result observed only after time has passed, such as 30-day retention, a refund, or subscription renewal.
- Why can an aggregate metric hide harm? == Improvements in a large segment can mask regressions in a smaller segment, such as a device type or accessibility group.
- What should be checked before interpreting experiment outcomes? == Assignment integrity, event completeness, duplicate events, sample ratios, eligibility filters, metric definitions, and exposure timing.
- Why should variant-specific event names and logging paths be reviewed carefully? == Different instrumentation can create an apparent effect that is actually a measurement difference.

## Sample Size, Duration, and Monitoring

- Why calculate sample size before an A/B test? == To assess whether available traffic can detect a decision-relevant effect with the chosen error rate and power.
- Which inputs matter for sizing a conversion-rate experiment? == Baseline conversion, target detectable change, alpha, power, allocation ratio, and any clustering or repeated-measure structure.
- Why is a 50/50 allocation often statistically efficient? == With similar outcome variances and costs, balanced groups minimize the variance of the treatment-control difference for a fixed total sample.
- Why might an experiment use less than 50% treatment traffic? == To limit exposure risk or capacity demands, accepting that the same precision may require more total traffic or time.
- Why is reaching the planned sample count not always enough? == The experiment may still need full business cycles, sufficient outcome follow-up, or time for temporary novelty effects to settle.
- Should every A/B test run for exactly two weeks? == No; duration depends on traffic, effect size, business cycles, outcome delays, and the prespecified analysis design.
- Can you monitor an experiment before its planned end? == Yes, especially for safety and data quality; repeatedly declaring efficacy from ordinary fixed-horizon p-values requires statistical correction.
- What is a valid way to allow early efficacy stopping? == Prespecify a sequential design with appropriate stopping boundaries or another method valid under the intended monitoring rule.
- When can an experiment be stopped immediately without claiming a measured benefit? == When serious harm, outages, privacy issues, or broken data collection make continued exposure unacceptable.

## Data Quality and Analysis

- What is sample ratio mismatch (SRM)? == An observed allocation across variants that is statistically inconsistent with the configured randomization proportions.
- What can cause SRM? == Assignment bugs, redirects, uneven logging loss, identity problems, or analysis filters that remove one variant's users more often.
- What should you do when SRM is detected? == Investigate and resolve the cause before trusting outcome comparisons; simply reweighting group counts does not generally repair the underlying bias.
- What is an intention-to-treat analysis? == Comparing units by their original assigned group, including those who did not fully use the treatment, with appropriate handling of missing outcomes.
- Why can comparing only users who used a new feature be biased? == Feature usage is self-selected and can be affected by treatment, so users in the compared groups may no longer be comparable.
- What is absolute lift for a conversion metric? == Treatment conversion minus control conversion; a rise from 10% to 11% is +1 percentage point.
- What is relative lift for a conversion metric? == (Treatment conversion - control conversion) / control conversion; a rise from 10% to 11% is +10% relative lift.
- Why report an uncertainty interval alongside lift? == A point estimate alone does not show whether plausible effects include meaningful benefit, negligible change, or meaningful harm.
- Why must uncertainty calculations respect the randomization unit? == Outcomes within a user or cluster may be correlated; treating every event as an independent randomized unit can understate uncertainty.
- What is CUPED in online experimentation? == A variance-reduction method using predictive pre-treatment covariates to adjust outcomes, potentially improving precision without changing random assignment.

## Common Pitfalls

- What is a novelty effect? == A temporary response to a new experience that may fade as users become familiar with it.
- What is a carryover effect? == An earlier treatment continues to affect later behavior, making later exposures or crossover periods harder to interpret.
- What is experiment contamination? == Units receive or are influenced by another group's treatment, weakening the intended separation between variants.
- How can network effects break a simple user-level A/B test? == Treated users can influence control users, so the comparison no longer isolates independent treatment experiences.
- What is an interaction between experiments? == The effect of one change depends on whether another change is also active; independent assignment alone does not make such interactions disappear.
- Why is post-hoc segment hunting risky? == Searching many segments and reporting only favorable ones creates multiple-testing and selection problems; treat findings as exploratory or use planned corrections.
- Does significance in one subgroup and non-significance in another prove their effects differ? == No; test the difference between subgroup effects directly, with appropriate uncertainty and multiplicity handling.
- Why can changing a metric definition midway invalidate a planned analysis? == It changes the outcome being tested after data have influenced decisions; document the change and consider a new confirmatory experiment.

## Decisions and Follow-Up

- Does a statistically significant positive primary metric automatically justify shipping? == No; consider effect size, guardrails, implementation cost, data quality, and whether the result matches the target population and use case.
- What does an inconclusive experiment mean? == The data do not support a sufficiently clear decision under the planned criteria; it does not automatically mean the variants are equivalent.
- How should you handle an inconclusive result? == Report the estimate and interval, assess remaining uncertainty, and decide whether to stop, redesign, or collect more data using a valid analysis plan.
- What is a long-term holdout? == A group kept on a reference experience longer to estimate persistent effects that short experiments may miss.
- What should an experiment report include? == Hypothesis, design, dates, population, sample sizes, data-quality checks, effect estimates with uncertainty, guardrails, limitations, and the decision.
- Why continue monitoring after an experiment winner is rolled out? == Full rollout can change load, user composition, and interactions, while rare or delayed harms may not have appeared during the experiment.
