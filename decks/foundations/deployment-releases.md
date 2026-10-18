# Flashcards: Deployment & Releases

## From Code to a Running System

- What is a build? == The process of turning source code and dependencies into a usable artifact, such as an executable, package, or container image.
- What is a build artifact? == A versioned output of a build that can be tested, stored, and deployed.
- What is a deployment? == Installing or updating a version of software in an environment where it can run.
- What is a release? == Making functionality available to its intended users; a release can happen separately from deployment through feature flags or routing.
- Deployment versus release? == Deployment changes what software is running; release changes what functionality users can access.
- What is a rollback? == Returning to a previous working version or configuration after a problematic change.
- What is a roll-forward fix? == Deploying a new corrective change rather than restoring the previous version.
- What is a hotfix? == An urgent change intended to resolve a production problem, usually through an expedited but still controlled delivery process.

## Environments and Configuration

- What is a development environment? == An environment used to implement and try changes, often on a developer's machine or in an isolated workspace.
- What is a staging environment? == A pre-production environment used to validate changes under conditions resembling production.
- What is the production environment? == The environment serving real users or business workloads, where failures can have direct consequences.
- Why can a change work in staging but fail in production? == Differences in traffic, data, configuration, permissions, dependencies, or infrastructure can expose untested conditions.
- What is environment parity? == Keeping important aspects of environments similar enough to reduce surprises, without requiring identical scale or real production data.
- Why should production secrets not be committed to Git? == Repository history and copies can expose them widely; use a secret-management mechanism with access control and rotation.
- What is configuration drift? == Untracked differences between the intended system configuration and the actual running configuration.
- Why validate configuration before starting a service? == Missing or invalid settings should cause an explicit early failure instead of unexpected behavior during user requests.

## Continuous Integration and Delivery

- What is continuous integration (CI)? == Frequently integrating small changes into a shared codebase and automatically checking that they build and pass relevant tests.
- What is a CI pipeline? == An automated sequence of jobs such as formatting checks, tests, security scans, and artifact builds triggered by repository events.
- What is continuous delivery? == Keeping changes in a tested, deployable state so production deployment can happen on demand, potentially with manual approval.
- What is continuous deployment? == Automatically deploying changes to production after they pass the required pipeline checks, without a routine manual release gate.
- Continuous delivery versus continuous deployment? == Delivery makes production deployment reliably available on demand; deployment automates that final step as well.
- What is a pipeline stage or job? == A named set of automated actions, such as unit tests or image publishing, with its own inputs, execution conditions, and result.
- Why should pipeline failures block promotion when they represent required checks? == Promoting despite a failed gate bypasses the evidence the team relies on to judge the change safe.
- Why build once and promote the same artifact across environments? == It ensures production receives the exact artifact already tested, instead of a rebuild with potentially different dependencies or outputs.
- What is an immutable artifact reference? == An identifier tied to exact artifact content, such as a container digest, rather than a mutable label that can point somewhere else later.
- Why keep a deployment record linking version, configuration, and time? == It makes incidents traceable to the actual change and supports reproducible rollbacks and audits.

## Packaging and Infrastructure

- What is a container image? == A packaged filesystem and metadata used to start containers, usually containing the application and its runtime dependencies.
- What is a container? == A running isolated process environment created from an image, typically sharing the host's operating-system kernel.
- Container versus virtual machine? == A container usually isolates processes using a shared host kernel; a virtual machine runs a separate guest operating system on virtualized hardware.
- Does using containers eliminate environment differences? == No; host architecture, runtime configuration, permissions, networking, and external services can still differ.
- What is infrastructure as code (IaC)? == Defining infrastructure in version-controlled configuration or code so changes can be reviewed and applied repeatably.
- What is a declarative infrastructure configuration? == A description of the desired state that a tool attempts to reconcile with the actual state.
- What is an idempotent deployment operation? == Repeating it with the same intended configuration does not keep introducing additional changes beyond that desired state.
- What is a deployment manifest? == A configuration describing how an application should run, such as its image, resources, replicas, and environment settings.

## Rollout Strategies

- What is a recreate deployment? == Stop the old version and then start the new one, which is simple but can cause downtime.
- What is a rolling deployment? == Gradually replace old instances with new ones while keeping some instances available to serve traffic.
- What is a key compatibility requirement during a rolling deployment? == Old and new instances must safely coexist, including their API contracts, shared data formats, and database usage.
- What is blue-green deployment? == Maintain two environments, prepare the new version in the inactive one, then switch traffic from the old environment to the new one.
- What is a trade-off of blue-green deployment? == It can enable a fast traffic switch and fallback but requires extra capacity and careful handling of shared state and data changes.
- What is a canary release? == Expose a new version to a limited portion of traffic or users, evaluate it, and expand exposure or roll back.
- What should be monitored during a canary? == Relevant error rates, latency, resource use, and business or correctness signals, compared with a suitable baseline.
- Why is a canary not automatically an A/B test? == Its traffic may not be randomized or representative, and its purpose and analysis often focus on operational safety rather than causal effect estimation.
- What is a shadow deployment? == Send copies of real requests to a candidate version while the established version continues producing user-visible responses.
- Why must shadow traffic be isolated from side effects? == Duplicate requests could otherwise charge users, send messages, or modify production data a second time.
- Why do shadow results not fully predict real-user outcomes? == Users do not act on the shadow responses, so downstream behavior and feedback effects are absent.

## Feature Flags

- What is a feature flag? == A runtime-controlled switch that changes which behavior is enabled without necessarily deploying new code.
- How can feature flags separate deployment from release? == Deploy the implementation disabled, then enable it for selected users or everyone when ready.
- What is a kill switch? == A control that quickly disables a risky feature or behavior when problems occur.
- What is a percentage rollout? == Enabling a feature for a configured share of eligible users or traffic, usually with stable assignment for user-facing experiences.
- What is a risk of long-lived feature flags? == They multiply possible code paths and can become confusing technical debt if ownership and cleanup are neglected.
- What should a feature flag have besides a name? == An owner, purpose, safe default, intended lifetime, and a plan for removal or permanent management.
- Can a feature flag undo data changes already made? == Not necessarily; disabling a code path does not reverse writes, external actions, or incompatible schema changes.

## Health Checks and Safe Shutdown

- What is a startup probe? == A check that allows an application time to initialize before normal liveness or readiness handling takes over.
- What is a liveness check? == A check that the process is functioning enough that restarting it may be an appropriate response to failure.
- What is a readiness check? == A check that an instance is currently able to receive its intended traffic; failure should remove it from routing rather than necessarily restart it.
- Why should a temporary database outage not automatically fail every instance's liveness check? == Restarting all instances rarely repairs the database and can create a restart storm that worsens recovery.
- What is graceful shutdown? == Stop accepting new work, allow in-flight work to finish within a limit, and release resources before terminating.
- What is connection draining? == Removing an instance from new traffic while giving existing connections or requests time to complete.
- Why run smoke tests after deployment? == They check critical behavior in the actual target environment, where configuration or routing errors may differ from CI.

## Migrations and Recovery

- What is a database migration? == A versioned change to a database schema or its data, coordinated with the application versions that use it.
- What is the expand-and-contract migration pattern? == First add a compatible structure, migrate readers and writers or data, then remove the old structure after it is no longer needed.
- Why can renaming a database column in one step break a rolling deployment? == Older instances may still query the old name while newer instances expect the new one.
- Why can rolling back application code fail after a schema migration? == The old code may not understand the new schema or data, and destructive migrations may not be reversible.
- Why is a backup alone not a complete rollback plan? == Restoring can take time, lose recent writes, and affect other users or services; recovery steps and consequences must be understood and tested.
- What is a deployment gate? == A required check or approval before moving a change to the next environment or rollout stage.
- What should be decided before a risky production rollout? == Success and failure criteria, observation time, responsible people, and a tested rollback or roll-forward path.
- What are release notes for? == Communicating user-visible changes, known issues, and migration requirements for a specific release.
- What does semantic versioning express for a declared public API? == MAJOR for incompatible API changes, MINOR for backward-compatible functionality, and PATCH for backward-compatible fixes; 0.x versions signal initial development.
