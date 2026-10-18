# Flashcards: Software Testing & QA

## Testing Fundamentals

- What is software testing? == Evaluating software to find defects and gather evidence that it meets expectations; passing tests does not prove the absence of all defects.
- What is quality assurance (QA)? == Activities that help prevent and detect quality problems across development, including process improvements, reviews, and testing.
- What is a test case? == A defined situation with inputs or setup, an action, and an expected result that can be checked.
- What is an assertion in a test? == A check that an observed result or condition matches an expectation; a failed assertion makes the test fail.
- What is a test suite? == A collection of tests run together, often grouped by component, purpose, or execution cost.
- What is a test oracle? == A source of expected behavior used to decide whether a result is correct, such as a specification, invariant, or trusted implementation.
- What is the Arrange-Act-Assert pattern? == Set up the test conditions, perform the action under test, then check the result.
- What makes a test useful as documentation? == It clearly names the expected behavior and shows a small, understandable example without requiring hidden context.

## Smoke, Sanity, and Regression Tests

- What is a smoke test? == A short, broad check that critical functionality works well enough for further testing or use, such as starting the app and completing a basic request.
- When are smoke tests commonly run? == After a build or deployment, before spending time on deeper checks or exposing more traffic.
- What is an example of a web application's smoke test? == Start the deployed app, load a key page, and perform a safe representative action such as signing in with a test account.
- Does a passing smoke test mean a release is bug-free? == No; it only provides evidence that the basic paths checked by the smoke suite work.
- What is a regression test? == A test that checks whether a change has broken behavior that should still work.
- Smoke test versus regression test? == Smoke describes a small breadth-first check of critical functionality; regression describes the purpose of detecting broken existing behavior. A test can be both.
- What is a sanity test? == A commonly used term for a focused check after a small change to see whether the affected behavior is plausible; team definitions vary.
- What is the difference between retesting a fix and regression testing? == Retesting checks that the reported defect is fixed; regression testing checks that existing behavior has not been broken elsewhere.

## Test Levels and Boundaries

- What is a unit test? == A focused test of a small unit of behavior, such as a function or component, usually with controlled dependencies.
- What is an integration test? == A test that checks whether components work correctly together, such as application code interacting with a real database.
- What is an end-to-end (E2E) test? == A test of a complete user or business flow through the relevant system components, such as placing an order through the UI.
- Unit test versus integration test? == A unit test isolates a small behavior; an integration test checks a boundary between components. The exact boundary depends on the project.
- What is a system test? == A test of the integrated system against its requirements, without necessarily including every external system in a full business journey.
- What is user acceptance testing (UAT)? == Validation by users or business representatives that the system supports agreed needs and acceptance criteria.
- What is a contract test? == A check that a service or component follows an agreed interaction contract, such as required response fields and their meanings.
- Why are contract tests useful between services? == They can detect incompatible interface changes without requiring every service to run together in a full E2E environment.
- What is the test pyramid? == A guideline favoring many fast, focused tests and fewer expensive broad tests; the appropriate mix depends on architecture and risk.
- Why not rely only on E2E tests? == They are often slower, harder to diagnose, and more sensitive to environment failures than focused tests.

## Test Doubles

- What is a test double? == A replacement for a real dependency used to control conditions or observe interactions during a test.
- What is a stub? == A test double that returns configured responses, such as a payment provider that always returns a declined result.
- What is a mock? == A test double used to verify interactions, such as whether an email sender was called with the expected recipient; framework terminology varies.
- What is a fake? == A simplified working implementation, such as an in-memory repository, that is useful for tests but not equivalent to the full production system.
- What is a spy? == A test double or wrapper that records how it was called so interactions can be checked afterward.
- What is a dummy object? == A placeholder passed to satisfy an interface or argument list but not used in the behavior being tested.
- What is the risk of excessive mocking? == Tests can become tightly coupled to implementation details and pass even when the real components cannot work together.
- Why can an in-memory database fake miss production bugs? == It may differ in SQL behavior, constraints, transaction isolation, concurrency, or supported data types.

## Choosing Test Cases

- What is a happy-path test? == A test of the expected successful flow with valid inputs and normal operating conditions.
- What is a negative test? == A test that checks behavior under invalid inputs, rejected operations, or failures, such as denying access without permission.
- What is an edge case? == An unusual or extreme condition that may expose assumptions, such as an empty collection, a very large value, or a leap day.
- What is boundary-value analysis? == Testing values at and around limits, such as just below, at, and just above a minimum age.
- What is equivalence partitioning? == Grouping inputs expected to behave similarly and selecting representative examples from each group.
- What is a parameterized test? == One test definition executed with multiple input and expected-output combinations.
- What is property-based testing? == Generating many inputs and checking general properties, such as sorting preserving the input elements and producing ordered output.
- What is fuzz testing? == Feeding many generated or mutated inputs to a system to expose crashes, security flaws, or unexpected behavior.
- What is a snapshot or golden-file test? == Comparing current output with a stored expected output; updates require review so regressions are not accepted blindly.
- Why are snapshot tests alone insufficient for correctness? == They detect changes, not whether the stored or new behavior is actually correct.

## Reliability and Isolation

- What is a flaky test? == A test that sometimes passes and sometimes fails without relevant changes to the code, inputs, or intended conditions.
- What commonly causes flaky tests? == Timing assumptions, shared state, uncontrolled randomness, real network dependencies, race conditions, and unstable test data.
- Why is repeatedly rerunning a flaky test not a real fix? == It hides unreliable evidence and can mask genuine failures; investigate the cause and stabilize the test.
- What is test isolation? == Tests do not depend on other tests' execution order or leftover state and can run independently.
- What is a test fixture? == Reusable setup data or resources that place a test in a known starting state, often paired with cleanup.
- Why should tests clean up resources even when they fail? == Leftover files, database rows, or processes can affect later tests and make failures difficult to reproduce.
- Why avoid fixed sleeps in asynchronous tests when possible? == They can be both slow and unreliable; wait for a specific observable condition with a bounded timeout instead.
- How can tests involving time be made deterministic? == Inject or control the clock so the test does not depend on the wall clock, time zone, or a real waiting period.
- Why record a random seed when a generated test fails? == It can help reproduce the failing input sequence, though environment and generator versions may also matter.

## Coverage and Test Quality

- What is code coverage? == A measurement of which parts of code were executed by tests, such as lines or branches.
- What is branch coverage? == The proportion of decision outcomes exercised by tests, such as both the true and false paths of an if statement.
- Does 100% line coverage guarantee good tests? == No; tests may execute code without checking meaningful outcomes or exploring important input combinations.
- What is mutation testing? == Deliberately making small changes to code and checking whether the test suite detects them.
- What can a surviving mutation indicate? == A missing or weak assertion, an untested behavior, or a mutation equivalent to the original program.
- Why should tests usually assert observable behavior instead of internal implementation details? == Behavior-focused tests allow harmless refactoring while still detecting meaningful regressions.
- What is a false positive in a test suite? == A reported failure even though the behavior being checked is acceptable, for example due to an unstable test environment.
- What is a false negative in a test suite? == A passing result despite a real defect, for example because the assertion does not cover the broken behavior.

## Performance, Security, and Workflow

- What is a load test? == A test of behavior under an expected or specified workload, measuring factors such as latency, errors, and throughput.
- What is a stress test? == A test that pushes beyond normal capacity to identify limits, failure behavior, and recovery characteristics.
- What is a soak test? == A sustained workload test used to reveal problems that emerge over time, such as memory leaks or resource exhaustion.
- What is a security test? == A check for weaknesses that could violate confidentiality, integrity, or availability, such as broken authorization or injection vulnerabilities.
- What is exploratory testing? == Learning about the system, designing tests, and executing them interactively to investigate risks and unexpected behavior.
- What is test-driven development (TDD)? == Write a failing test for a small behavior, implement enough to pass it, then refactor while keeping tests passing.
- Why add a regression test when fixing a bug? == It demonstrates the failure before the fix and helps prevent the same bug from returning.
- What should a CI test failure provide? == A clear failure message and enough relevant logs or artifacts to reproduce and diagnose it, without leaking secrets.
- What is risk-based testing? == Prioritizing test effort according to the likelihood and impact of failures rather than treating all functionality as equally important.
- How is an A/B test different from a software correctness test? == An A/B test estimates the effect of a product change on outcomes; a correctness test checks whether specified behavior works as expected.
