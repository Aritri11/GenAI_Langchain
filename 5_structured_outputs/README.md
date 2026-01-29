1. TypedDict – when to use
Use TypedDict when:
You want a lightweight way to define the output structure (field names and basic types) with minimal boilerplate.
You already trust the model reasonably (prototyping, demos, internal tools) and do not need strict runtime validation.
​You are fine getting back a plain Python dict rather than a richer object.
​
Typical use:
Quick experiments, simple scripts, notebooks, or when you just need fields like summary, sentiment, pros, cons and will do any extra checks yourself in code.

2. Pydantic – when to use
Use Pydantic models when:
You need strong data validation and type safety (production APIs, user‑facing systems, or anything that writes to databases).
You want automatic checks (wrong type, missing required field, invalid enum etc.) to raise errors instead of silently accepting bad LLM output.
You like working with rich model objects (methods, defaults, validators) rather than plain dicts.

Typical use:
Production pipelines, FastAPI/other web services, or critical workflows where incorrect structure or types from the LLM are not acceptable.

3. JSON Schema – when to use
Use JSON schema when:
You need a model‑agnostic, language‑independent schema (for example, exposing the schema to other services, or matching an existing API/database contract).
​You are integrating with systems that already expect JSON schema (frontends, other microservices, validation libraries).
​You want the LLM to output raw JSON that conforms to a schema, without tying yourself to Python‑only constructs.
​

Typical use:
Cross‑language systems, external integrations, or when your “source of truth” for structure is a JSON schema used beyond just the LangChain code.
​

Very short rule of thumb
TypedDict → simple, fast, minimal, mostly for trusted/prototyping scenarios.
Pydantic → strict validation and robustness, preferred for production and APIs.

JSON schema → interoperable schema for cross‑service or cross‑language integration.
