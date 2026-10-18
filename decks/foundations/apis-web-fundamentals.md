# Flashcards: APIs & Web Fundamentals

## Clients, Servers, and Addresses

- What is an API? == An application programming interface: a defined way for software components to interact, including operations, inputs, outputs, and behavior.
- What is a client-server interaction? == A client initiates a request for a capability or resource, and a server handles it and returns a response.
- What is an API endpoint? == An exposed interaction point, commonly identified in an HTTP API by a method and URL path, such as GET /users/42.
- What is a URL? == A uniform resource locator identifying how and where to access a resource, including components such as scheme, host, path, and optional query.
- What does DNS do? == Resolves domain names to information such as IP addresses, allowing clients to locate services by name.
- What is a port in networking? == A numbered transport endpoint used to distinguish services on a host, such as port 443 commonly used for HTTPS.
- What is the difference between a path parameter and a query parameter? == A path parameter is part of the resource path, such as /users/42; a query parameter follows ?, such as ?page=2, and often controls filtering or options.
- Is a URL fragment sent to the HTTP server as part of the request target? == No; the part after # is handled by the client, for example to navigate within a page.

## HTTP Requests and Responses

- What is HTTP? == The Hypertext Transfer Protocol, an application-layer protocol defining request and response semantics for exchanging resources and related information.
- What is HTTPS? == HTTP protected by TLS, providing encryption in transit, integrity protection, and usually server authentication.
- Does HTTPS prove that a website or API is trustworthy? == No; it protects the connection to the authenticated domain, not the honesty or correctness of the service.
- What are the main parts of an HTTP request? == A method and target, headers carrying metadata, and an optional body carrying content.
- What are the main parts of an HTTP response? == A status code, headers carrying metadata, and an optional body carrying content.
- What is an HTTP header? == A named metadata field describing the request, response, representation, or handling rules.
- What does the Content-Type header describe? == The media type of the message body, such as application/json.
- What does the Accept request header describe? == The response media types the client can handle or prefers.
- What is JSON? == A text data format supporting objects, arrays, strings, numbers, booleans, and null; it does not natively define dates or binary data.
- Why must API input be validated even when it is valid JSON? == Correct JSON syntax does not guarantee required fields, acceptable values, valid business rules, or authorization.

## Methods and Idempotency

- What is GET intended for? == Retrieving a resource representation without requesting a change to server state.
- What is POST commonly used for? == Submitting content for processing, such as creating a server-identified resource or triggering an action; its exact behavior depends on the endpoint.
- What is PUT intended for? == Creating or replacing the state of a resource at the target URI with the supplied representation.
- What is PATCH intended for? == Applying a partial modification to a resource using a defined patch format or API contract.
- What is DELETE intended for? == Removing the association between a target URI and its current functionality or resource representation, according to the API contract.
- What is HEAD used for? == Requesting the headers that a corresponding GET would return, without transferring the response body.
- What does it mean for an HTTP method to be safe? == Its defined semantics are essentially read-only from the client's perspective; incidental effects such as access logging can still occur.
- What does idempotent mean for an HTTP operation? == Repeating the same request has the same intended server-side effect as making it once.
- Which common HTTP methods are idempotent by their defined semantics? == GET, HEAD, OPTIONS, PUT, and DELETE; POST and PATCH are not guaranteed to be idempotent.
- Can repeated DELETE requests return different status codes and still be idempotent? == Yes; deleting once may succeed and a later request may report not found, while the intended final state remains the same.
- Can a PATCH operation be idempotent? == Yes; setting a field to a fixed value can be idempotent, while incrementing a counter is generally not.
- What is an idempotency key? == A client-provided identifier that lets a server recognize retries of the same logical operation and avoid repeating its effects, subject to the API's scope and retention rules.

## Status Codes

- What do the HTTP status-code families mean? == 1xx informational, 2xx successful, 3xx redirection, 4xx client-request problems, and 5xx server-side failures.
- What does HTTP 200 OK mean? == The request succeeded; the response content and exact meaning depend on the method and endpoint.
- What does HTTP 201 Created mean? == The request succeeded and created one or more resources; a Location header can identify the primary new resource.
- What does HTTP 202 Accepted mean? == The request was accepted for processing but processing is not complete, so it does not guarantee eventual success.
- What does HTTP 204 No Content mean? == The request succeeded and the response has no message body.
- What does HTTP 400 Bad Request indicate? == The server cannot or will not process the request because of a perceived client error, such as malformed input.
- HTTP 401 versus 403? == 401 means valid authentication credentials are missing or unacceptable; 403 means the server refuses access, often despite knowing the caller's identity.
- What does HTTP 404 Not Found mean? == The target resource was not found or the server is not willing to disclose that it exists.
- What does HTTP 409 Conflict mean? == The request conflicts with the current state of the target resource, such as a version conflict.
- What does HTTP 429 Too Many Requests mean? == The caller has exceeded a rate limit; the response may indicate when to try again.
- HTTP 500 versus 502 versus 503 versus 504? == 500 is an unexpected server error; 502 is an invalid upstream response at a gateway; 503 is temporary unavailability; 504 is an upstream timeout at a gateway.
- Does receiving HTTP 200 prove a business operation succeeded? == Not necessarily; success semantics depend on the API contract, and a poorly designed API may encode business failures only in the body.

## API Styles and Contracts

- What is REST? == An architectural style for distributed systems based on constraints including a uniform interface, stateless interactions, and cacheability; it is not simply another name for JSON over HTTP.
- What is a resource in a REST-style API? == A concept identified by a URI, such as an order or user, whose representations can be transferred and manipulated through defined interactions.
- What does stateless interaction mean in REST? == Each request contains the information needed to understand it rather than relying on hidden conversational state from prior requests; servers can still store resource data.
- What is RPC? == Remote procedure call: interacting with another process by invoking named operations with parameters, as if calling functions across a boundary.
- What is GraphQL? == An API query language and execution model in which clients select fields from a typed schema; it also supports mutations and subscriptions.
- What is an OpenAPI description? == A machine-readable description of an HTTP API's operations, inputs, responses, and related details, usable for documentation and tooling.
- What is a backward-compatible API change? == A change that existing supported clients can continue to use correctly without modification; compatibility depends on actual client expectations.
- Why can adding a response field still break some clients? == Strict decoders or clients that assume an exact object shape may reject it, so additive changes are safe only under a compatible contract.
- What is pagination? == Returning a large result set in bounded pieces rather than in one response.
- Offset pagination versus cursor pagination? == Offset pagination skips a number of rows; cursor pagination continues from a position in a defined ordering and can behave better under large or changing datasets.

## Authentication and Browser Security

- Authentication versus authorization? == Authentication establishes who or what the caller is; authorization decides which actions that caller may perform.
- What is an API key? == A credential identifying or granting access to an API consumer, often a project or application; it is not necessarily proof of an end user's identity.
- What is a bearer token? == A credential that grants its associated access to whoever possesses it, so disclosure can allow impersonation until it expires or is revoked.
- What is OAuth 2.0 primarily for? == Delegated authorization: allowing a client to obtain limited access to protected resources without sharing the resource owner's password with that client.
- What does OpenID Connect add to OAuth 2.0? == An identity layer for user authentication, including ID tokens and standardized identity-related behavior.
- What is a JWT? == A JSON Web Token carrying claims in a compact format; it may be signed or encrypted, but a common signed JWT is not confidential.
- Why is decoding a JWT not enough to trust it? == The receiver must validate the intended token type, signature or protection, issuer, audience, expiration, and other applicable claims.
- What is a cookie? == A value stored by a browser and sent with matching requests according to domain, path, and security rules, often used to carry a session identifier.
- What does the HttpOnly cookie attribute do? == Prevents browser scripts from reading the cookie directly; it does not by itself stop malicious scripts from making authenticated requests.
- What is CORS? == Cross-Origin Resource Sharing: browser-enforced rules and response headers controlling whether scripts can access responses from another origin.
- Does CORS replace authentication or protect an API from non-browser callers? == No; scripts outside the browser and other clients are not constrained by the browser's CORS checks.
- What is a CORS preflight request? == An OPTIONS request a browser sends before certain cross-origin requests to check whether the intended method and headers are permitted.
- What is CSRF? == Cross-site request forgery: causing a victim's browser to send an unwanted authenticated request using credentials it attaches automatically, such as cookies.
- What is XSS? == Cross-site scripting: executing attacker-controlled script in a trusted site's browser context, potentially exposing data or performing actions as the user.

## Reliable API Interactions

- What is a webhook? == An HTTP callback sent by one system to another when an event occurs, reducing the need for repeated polling.
- How should a webhook receiver handle authenticity and duplicate delivery? == Verify the provider's authentication or signature scheme, apply relevant replay checks, and process events idempotently using stable event IDs.
- What is polling? == Repeatedly asking a server whether data or an operation's status has changed.
- What is a WebSocket? == A persistent bidirectional connection allowing client and server to exchange messages without a separate HTTP request for every message.
- What are Server-Sent Events (SSE)? == A server-to-client event stream over HTTP, commonly used for live updates when bidirectional messaging is unnecessary.
- Why should API calls have explicit timeouts? == A missing response must not tie up resources indefinitely; timeout values should fit the overall operation's time budget.
- What is a rate limit? == A bound on request volume or resource consumption over a period, used to protect capacity and allocate access fairly.
- What does a Retry-After header communicate? == A delay in seconds or an HTTP date indicating when a follow-up request may be appropriate.
- Why can retrying a timed-out payment request be dangerous? == The server may have completed the payment before the response was lost; use idempotency support or reconcile the operation before repeating its effect.
- What is an ETag? == An identifier for a particular resource representation, usable for cache validation or conditional operations such as preventing lost updates.
- What does an HTTP 304 Not Modified response mean? == A conditional GET or HEAD request can reuse the stored representation; the response does not send a new representation body.
