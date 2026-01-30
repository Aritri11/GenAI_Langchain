Output parsers turn LLM text into Python-friendly data, but they only work as well as the model’s ability to follow structure.

1️. StrOutputParser

Returns plain text

No structure or validation

Most reliable with any model

from langchain_core.output_parsers import StrOutputParser

2️. PydanticOutputParser

Converts output into a Pydantic model

Enforces schema and validation

Strict — fails if output is not valid JSON

from langchain.output_parsers import PydanticOutputParser

3️. JSON Parsing (implicit)

Parses JSON-like output

Less strict than Pydantic

Still unreliable with HF models
