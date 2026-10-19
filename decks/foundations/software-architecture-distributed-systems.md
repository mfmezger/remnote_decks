# Flashcards: Software Architecture & Distributed Systems

## Boundaries and Trade-Offs

- What is software architecture? == The important structural choices, boundaries, and interactions of a system, together with the constraints and trade-offs behind them.
- What is a component? == A part of a system with a defined responsibility and interface, such as a module, library, or service.
- What is separation of concerns? == Dividing responsibilities so that unrelated concerns can be understood and changed with limited interference.
- What is coupling? == The degree to which components depend on one another; tighter coupling makes changes more likely to spread across boundaries.
- What is cohesion? == How closely the responsibilities within a component belong together; high cohesion usually makes the component easier to understand.
- What is an interface? == A contract describing how another component can interact with a capability without needing to know its implementation details.
- What is an abstraction? == A simplified view that exposes relevant behavior while hiding details; a useful abstraction matches real needs rather than adding indirection for its own sake.
- What is an architecture decision record (ADR)? == A short document recording a significant decision, its context, alternatives, and consequences.

## Monoliths and Services

- What is a monolith? == An application deployed as a single unit, which may still contain well-separated internal modules.
- What is a modular monolith? == A single deployable application with explicit internal boundaries between cohesive modules.
- What are microservices? == An architecture of separately deployable services organized around bounded responsibilities and communicating over explicit interfaces.
- What is a common advantage of a monolith for a small system? == Simpler development, testing, deployment, and local transactions without many network boundaries.
- What is a common advantage of microservices? == Teams can deploy and scale suitable service boundaries independently when contracts, ownership, and operations support that independence.
- What costs do microservices introduce? == Network failures, distributed data consistency, observability, deployment coordination, and interface-versioning complexity.
- What is a distributed monolith? == A system split across services that still require coordinated changes or deployments, gaining network complexity without much independence.
- Why should service boundaries not be chosen only around database tables? == Business workflows and ownership often span tables; table-based services can create excessive coupling and chatty interactions.
- What is the difference between a library and a service? == A library runs within its caller's process; a service runs independently and is accessed across a process or network boundary.

## Communication and Messaging

- What is synchronous communication? == The caller waits for a response before continuing the dependent work, coupling progress to the callee's availability and latency.
- What is asynchronous communication? == The sender can continue without waiting for the receiver to finish, often through messages, queues, or events.
- What is a message queue? == A buffer that stores work until consumers can process it, helping separate production from consumption rates.
- What is a message broker? == Infrastructure that receives, routes, and often stores messages between producers and consumers.
- What is publish-subscribe messaging? == Producers publish to a topic and multiple subscriptions can receive the same event, unlike one shared work queue where consumers typically compete for jobs.
- Command versus event? == A command requests that something happen; an event records that something has happened.
- What is an acknowledgment in message processing? == A consumer's signal that a message has been handled according to the broker's protocol, allowing it to be removed or its position committed.
- What is at-most-once delivery? == A message is delivered zero or one times; avoiding redelivery means failures can lose work.
- What is at-least-once delivery? == Messages can be redelivered to avoid losing work, so consumers must handle duplicates.
- Why is exactly-once processing a claim that needs a clear scope? == A broker may guarantee a specific delivery or transaction boundary, while external effects such as payments still require coordination or idempotency.
- What is a dead-letter queue? == A destination for messages that could not be processed under the retry policy, enabling investigation or controlled reprocessing.
- Why is a dead-letter queue not a complete error-handling strategy? == Failed work still needs ownership, monitoring, diagnosis, and a safe recovery or discard decision.
- What is backpressure? == Signaling or enforcing that producers slow down when consumers cannot keep up, rather than allowing unbounded queued work.

## Scaling and Traffic Management

- What is vertical scaling? == Increasing the capacity of one machine or instance, such as adding CPU or memory.
- What is horizontal scaling? == Adding more instances and distributing work among them.
- Why is adding instances not guaranteed to increase throughput proportionally? == Shared bottlenecks, coordination, contention, and uneven work distribution can limit the gain.
- What is a load balancer? == A component that distributes incoming traffic across suitable backend instances.
- What is a reverse proxy? == A server that accepts client requests on behalf of backend servers and forwards them, often handling routing, TLS, or caching.
- What is service discovery? == Finding the current network locations of service instances as they start, stop, or move.
- What is a stateless application instance? == An instance that does not rely on its own local durable conversational state between requests; shared state may still exist in databases or other services.
- Why are stateless instances often easier to scale horizontally? == Requests can be routed to different instances without requiring a particular instance's local session state.
- What is a bottleneck? == The resource or stage that limits overall performance; improving unrelated components may have little effect until it is addressed.

## Caching

- What is a cache? == A store of reusable results or copies intended to reduce latency, computation, or load on another system.
- What is a cache hit versus a cache miss? == A hit finds a usable entry; a miss requires obtaining the result from another source or recomputing it.
- What is a cache's time to live (TTL)? == The period after which an entry is considered expired; it limits lifetime but does not guarantee the value stays current before expiry.
- What is cache invalidation? == Removing or updating cached entries when they should no longer be used, such as after underlying data changes.
- What is the cache-aside pattern? == The application checks the cache, reads the source on a miss, and populates the cache; writes need a suitable invalidation or update strategy.
- What is a cache stampede? == Many requests simultaneously recompute or reload the same missing or expired entry, causing a load spike.
- How can cache stampedes be reduced? == Coalesce concurrent refreshes, spread expiration times with jitter, or serve bounded stale data during refresh when acceptable.
- Why must cache keys include relevant user or tenant context? == Otherwise a cached response can be reused for the wrong caller, causing incorrect results or data leakage.
- What is the trade-off of serving stale cache entries? == It can improve availability and latency while sacrificing freshness; whether that is acceptable depends on the data and business operation.

## Failures and Resilience Patterns

- What is a partial failure in a distributed system? == Some components or communication paths fail while others continue working, leaving different parts with different observations.
- What does a network timeout prove about a remote operation? == Only that a response was not received in time; the operation may have failed, still be running, or already succeeded.
- Why set an end-to-end deadline rather than only unrelated per-call timeouts? == It limits the total time spent across dependencies and retries so the complete operation stays within its budget.
- What is exponential backoff? == Increasing the wait between retry attempts, usually up to a cap, to reduce pressure during failure or overload.
- Why add jitter to retry delays? == Random variation prevents many clients from retrying simultaneously in synchronized bursts.
- What is a retry storm? == Retries amplify traffic against an already struggling dependency, potentially causing wider failure.
- What is a retry budget? == A limit on retry volume or attempts so recovery efforts do not consume excessive capacity or exceed the request deadline.
- What is a circuit breaker? == A mechanism that temporarily rejects calls to a failing dependency, then allows controlled trial calls before restoring normal traffic.
- What are the common circuit-breaker states? == Closed allows calls, open rejects them, and half-open allows limited probes to test recovery.
- What is the bulkhead pattern? == Isolating capacity or resources between workloads so one failure or overload does not consume everything.
- What is load shedding? == Deliberately rejecting or dropping lower-priority or excess work to preserve useful service under overload.
- What is a fallback? == An alternative behavior used when the preferred path fails, such as returning cached data or disabling a nonessential feature.
- Why can an untested fallback worsen an outage? == It may return incorrect results or send a sudden load spike to another system that cannot handle it.

## Distributed State and Coordination

- What is replication? == Maintaining copies of data or state on multiple nodes for availability, durability, or read scaling, depending on the design.
- Replication versus sharding? == Replication copies the same data; sharding divides different data across nodes. A system can use both.
- What is eventual consistency? == If updates stop and communication continues, replicas eventually converge; reads before convergence may return older or different values.
- What is linearizability? == A consistency guarantee under which each operation appears to take effect atomically between its invocation and response, respecting real-time order.
- What does the CAP theorem constrain? == During a network partition, a distributed shared-data system cannot guarantee both linearizable consistency and availability of every request to a non-failing node.
- Why is CAP not simply a permanent choice of any two out of three properties? == Network partitions are failures the system must handle; the consistency-versus-availability trade-off becomes unavoidable during those partitions.
- What is a leader in a replicated system? == A node responsible for coordinating a role such as accepting ordered writes; leader election and failover need safeguards against conflicting leaders.
- What is split brain? == Multiple nodes act as the authoritative leader at the same time without safe coordination, potentially accepting conflicting updates.
- What is distributed consensus? == A protocol by which nodes agree on a value or ordered decisions despite specified failure conditions, under explicit assumptions.
- What is a saga? == A sequence of local transactions across services with compensating actions to address failures instead of one global database transaction.
- Why is a compensating action not always a perfect rollback? == External effects may be irreversible or visible, such as an email already sent; compensation is a new business action, not erasing history.
- What is the transactional outbox pattern? == Store a business update and an event record in one local database transaction, then publish the event asynchronously to avoid losing the event between a database commit and message send.
- Does the transactional outbox eliminate duplicate event delivery? == No; publishing and retries can still produce duplicates, so downstream processing commonly needs idempotency.
