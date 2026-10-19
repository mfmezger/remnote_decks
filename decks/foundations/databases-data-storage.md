# Flashcards: Databases & Data Storage

## Data Models

- What is a database? == An organized collection of data managed so it can be stored, queried, and updated according to defined rules.
- What is a database management system (DBMS)? == Software that manages databases, including storage, queries, access control, and concurrency.
- What is a relational database? == A database organized around relations, commonly represented as tables with rows, columns, and constraints.
- What is SQL? == Structured Query Language, used to define, query, and modify relational data; individual database systems support different dialects and extensions.
- What does NoSQL mean? == A broad category of database approaches such as document, key-value, wide-column, and graph models; it does not imply no schema or no transactions.
- What is a document database? == A database that stores records as structured documents, often allowing nested fields and flexible shapes.
- What is a key-value store? == A store that retrieves values by keys, commonly optimized for direct lookups rather than arbitrary relational joins.
- What is a graph database? == A database representing entities and relationships as nodes and edges, with operations designed for traversing those relationships.
- What is an object store? == Storage for objects addressed by keys, typically suitable for files or blobs with metadata rather than relational queries and multi-row transactions.
- How should a data store be selected? == Start from access patterns, consistency requirements, data relationships, scale, and operational needs rather than choosing only by popularity.

## Tables, Keys, and Constraints

- What is a database schema? == The defined structure and rules for data, such as tables, column types, relationships, and constraints; some systems also use schema to mean a namespace.
- What is a primary key? == A column or set of columns that uniquely identifies each row and cannot be null.
- What is a foreign key? == A constraint requiring referenced values to correspond to an allowed row in another or the same table, subject to configured null and update/delete behavior.
- What is a unique constraint? == A rule preventing duplicate values or value combinations; how nulls interact with uniqueness depends on the database and configuration.
- What does a NOT NULL constraint do? == Requires a column to contain a value rather than SQL NULL.
- What is a CHECK constraint? == A condition the database enforces on row values, such as a quantity being nonnegative, with details depending on SQL null semantics and the database.
- What does NULL represent in SQL? == A missing, unknown, or inapplicable value, distinct from zero or an empty string.
- Why use IS NULL rather than equals NULL in a SQL filter? == Ordinary comparisons with NULL evaluate to unknown, not true; IS NULL explicitly tests for a null value.
- What is referential integrity? == The validity of relationships between records, such as an order referencing an existing customer.
- Why enforce critical invariants in the database as well as application code? == Concurrent writes or other clients can bypass application checks; database constraints protect the shared data boundary.

## Queries and Joins

- What are CRUD operations? == Create, Read, Update, and Delete: the basic operations for managing stored records.
- What does a SELECT query do? == Retrieves data, potentially applying filters, joins, grouping, calculations, and ordering.
- WHERE versus HAVING? == WHERE filters rows before grouping; HAVING filters groups after aggregation.
- What does GROUP BY do? == Groups rows by specified values so aggregate functions such as COUNT or SUM can be computed per group.
- What is an INNER JOIN? == A join that returns combinations of rows satisfying the join condition, excluding rows without a match.
- What is a LEFT JOIN? == A join that keeps all left-side rows and fills right-side columns with NULL when no matching right-side row exists.
- Why can a WHERE filter on the right table change a LEFT JOIN's behavior? == A condition that rejects NULL also removes unmatched rows, potentially turning the result into the equivalent of an inner join.
- Why can a join produce more rows than either input table? == A row can match multiple rows on the other side; many-to-many matches multiply combinations.
- What is the difference between COUNT(*) and COUNT(column)? == COUNT(*) counts rows, while COUNT(column) counts rows where that column is not NULL.
- Does a SQL result have a guaranteed order without ORDER BY? == No; apparent ordering can change with the query plan, data layout, or execution conditions.
- What is SQL injection? == Untrusted input is interpreted as SQL syntax, allowing an attacker to alter a query's meaning.
- How do parameterized queries reduce SQL injection risk? == They pass data values separately from SQL structure; dynamic identifiers or sort clauses still need controlled construction.

## Indexes and Query Performance

- What is a database index? == An additional data structure that helps locate rows or satisfy ordering without scanning all stored data.
- What is the main trade-off of adding an index? == Reads can become faster, but the index uses storage and must be maintained during inserts, updates, and deletes.
- What is a full table scan? == Reading the table's rows to find matching data; it can be appropriate for small tables or queries needing much of the table.
- What is a composite index? == An index on multiple columns, whose order affects which filters and sort orders it can support efficiently.
- Why does column order matter in a typical composite B-tree index? == The index is ordered by its leading columns first, so queries constraining those columns are usually easier to narrow efficiently; exact capabilities depend on the engine.
- What is a query execution plan? == The operations the database chooses to run a query, such as scans, joins, sorts, and index lookups.
- What is EXPLAIN used for? == Inspecting a query's planned execution so performance problems can be investigated rather than guessed.
- Why use care with EXPLAIN ANALYZE or equivalent commands? == They execute the query to collect actual measurements, which can be expensive or cause writes if the statement modifies data.
- What is the N+1 query problem? == Loading a collection with one query and then issuing another query per item, creating excessive round trips.
- What is a connection pool? == A bounded set of reusable database connections, reducing connection setup cost and controlling concurrent database access.
- Why can an oversized connection pool hurt performance? == Too many concurrent queries can increase contention, memory use, and queueing rather than increase useful throughput.

## Transactions and ACID

- What is a database transaction? == A group of operations treated as a unit according to the database's transaction guarantees.
- What does COMMIT do? == Successfully ends a transaction and makes its changes committed according to the database's durability and visibility rules.
- What does ROLLBACK do? == Aborts a transaction and undoes its uncommitted transactional changes; it does not undo unrelated external effects such as sent emails.
- What does ACID stand for? == Atomicity, Consistency, Isolation, and Durability.
- What is atomicity? == A transaction's changes are applied as a whole or not at all, within the transaction's supported scope.
- What is consistency in ACID? == A valid transaction preserves the defined data invariants; the database enforces declared constraints, while application logic must encode other business rules correctly.
- What is isolation? == Rules controlling how concurrent transactions can observe and interfere with one another.
- What is durability? == Once a commit is acknowledged, its changes survive the failures covered by the database's durability configuration and guarantees.
- Does ACID consistency mean every replica always returns the latest value? == No; ACID consistency concerns data invariants, while replica consistency concerns the visibility and ordering of updates across copies.
- What is a write-ahead log (WAL)? == A log of changes written before corresponding data pages are persisted, enabling recovery and supporting durability in systems that use it.

## Concurrency and Isolation Levels

- What is a dirty read? == Reading data written by another transaction before that transaction commits.
- What is a non-repeatable read? == Reading the same row twice in a transaction and seeing different committed values because another transaction changed it.
- What is a phantom read? == Repeating a query within a transaction and seeing a changed set of matching rows due to another transaction's changes.
- What does read committed isolation generally prevent? == Dirty reads; repeated statements may still observe different committed data, with details depending on the engine.
- What is repeatable read intended to provide? == Protection against changes to previously read data within a transaction; guarantees for ranges and other anomalies vary by database implementation.
- What is serializable isolation? == A guarantee that committed concurrent transactions have results equivalent to some serial execution; transactions may need to abort and retry to maintain it.
- What is a lost update? == One update unintentionally overwrites another, often because both writers used the same stale starting value.
- What is optimistic concurrency control? == Perform work assuming conflicts are uncommon, then check a version or other condition before committing and retry or reject if it changed.
- What is pessimistic concurrency control? == Acquire locks or similar restrictions to prevent conflicting operations while work is in progress.
- What is a deadlock? == Transactions wait on one another in a cycle, so none can proceed without intervention such as aborting one transaction.
- Why keep transactions short? == Long transactions can hold locks or old snapshots, increase contention, and delay cleanup or other work.

## Data Modeling and Evolution

- What is normalization? == Organizing relational data to reduce avoidable duplication and update anomalies, often by separating facts according to their dependencies.
- What is denormalization? == Deliberately storing redundant or precombined data to improve some reads, at the cost of storage and more complex consistency maintenance.
- What is an update anomaly? == Duplicated facts become inconsistent because only some copies are changed, such as conflicting customer addresses in separate order rows.
- Why should large data backfills often run in bounded batches? == They can otherwise hold resources for too long, overload the database, or make failure recovery difficult.
- What is a soft delete? == Marking a record as deleted without immediately removing it physically, which requires queries and retention policies to handle that state correctly.
- Why is soft deletion not necessarily sufficient for a privacy deletion request? == The data may remain in tables, indexes, replicas, logs, or backups; deletion requirements must cover applicable storage and retention behavior.

## Replication, Backups, and Workloads

- What is a read replica? == A copy that can serve reads from replicated data, potentially reducing load on the primary but possibly lagging behind it.
- What is replication lag? == The delay between a change at one node and its availability on a replica.
- How can replica lag affect a read immediately after a write? == The user may read an older value if the read is routed to a replica that has not applied the write yet.
- What is sharding in a database? == Splitting data across nodes by a partitioning key, requiring attention to distribution, cross-shard queries, and transactions.
- What is a hot shard? == A partition receiving disproportionate traffic or data, limiting performance despite spare capacity elsewhere.
- Backup versus replication? == Backups preserve recoverable historical copies; replication maintains live copies and can quickly propagate accidental deletion or corruption.
- What is point-in-time recovery? == Restoring a database to a chosen time using a base backup and the required sequence of logs or changes.
- Why should database restores be tested? == Backup files, credentials, logs, or procedures may be incomplete or unusable; a restore drill verifies recovery in practice.
- OLTP versus OLAP? == Online transaction processing handles operational reads and writes, while online analytical processing handles larger aggregations and analytical queries, often using different storage and execution designs.
- Row-oriented versus column-oriented storage? == Row storage groups fields of each record and often suits transactional access; column storage groups values of each field and often suits scans and aggregations over selected columns.
