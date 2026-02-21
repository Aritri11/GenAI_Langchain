Why GPT / proprietary APIs are a problem?


• Need for credit cards, recurring cost, rate limits, data going to vendor servers, student constraints.
• Rise of mature open‑source LLMs
• LLaMA, Mistral, DeepSeek, Qwen, GLM, etc., released as downloadable weights and architectures via platforms like Hugging Face.


What is an LLM (foundation view)?


• Large neural network with many layers, fundamentally just a collection of numbers (weights and biases) that store all learned knowledge.


Proprietary vs open‑source models


• Proprietary models
• Fully owned/controlled by a company, hidden architecture/weights/data, only usable via UI or API, usually paywalled for full capabilities (Gemini, GPT, etc.).
• Open‑source models
• Public weights, architecture, sometimes training data; can be downloaded and run locally, fine‑tuned, customized, and used without per‑token API cost.
• Why open‑source is hard to use directly
• Raw checkpoints, storage and VRAM management, quantization/compatibility, manual setup for inference, lots of friction despite being “free.”


What Ollama is and why it exists


• Purpose of Ollama
• A local tool/runtime that lets you download, run, and manage open‑source LLMs on your own machine, hiding storage/VRAM/config complexity.
• Conceptual analogy
• Ollama is like WhatsApp for open‑source models: you only focus on sending/receiving messages; it handles all low‑level transport and plumbing.
• Key benefits
• Privacy and data control: prompts never leave your machine; can run fully offline after download.
• Low latency and offline access: local inference once weights are downloaded.
• Cost predictability: pay only for electricity/hardware, no API subscription.
• Simple install and setup: one installer, then single‑line commands to pull/run models.
• Pre‑built model library: curated, quantized variants of LLaMA, Mistral, Qwen, DeepSeek, etc., in multiple sizes and capabilities (vision, tools, embeddings, thinking, cloud‑ready).
• Vendor‑lock‑in free: you control models and usage; no external terms beyond original model license.


Hardware and system requirements


• Supported OS
• macOS, Windows, Linux.
• Recommended minimum hardware
• 8 GB RAM or more for smoother experience; mid‑range modern CPU (e.g., i5 13th gen or better recommended).
• Storage considerations
• Models stored locally; e.g., Qwen 3 (2B) ≈ 2 GB, 8B ≈ 6+ GB; need enough disk for multiple models.
• GPU
• Optional but improves speed and smoothness; CPU‑only still works.


Using Ollama via CLI (command line)


1. Basic model management
• Pull model: ollama pull <model-name> (e.g., ollama pull mistral:8b). Ollama fetches all required files and stores them in the right place automatically.
• List local models: ollama list or ollama ls shows all downloaded models and sizes.
• Delete model: ollama rm <model-name> removes local files to free disk.
2. Running models interactively
• Start a model: ollama run <model-name> loads weights from disk into working memory (RAM/VRAM) and opens an interactive REPL where you can send prompts.
• Example queries: factual questions, definitions, etc.; works even if you disconnect from the internet.
• Exiting: use /bye to leave the model session.
3. Using models with images in CLI
• Some models have vision capability (e.g., gamma:3 in video). They can take image paths with prompts (e.g., “summarize the image”).
• If you use a text‑only model for an image, it will fail because it lacks vision capability.
4. Introspection and tuning from CLI
• /show subcommands inside ollama run:
• /show info – architecture, parameters, context length, quantization, capabilities (completion, tools, vision, thinking).
• /show parameters – current decoding parameters set for the session.
• /show system – current system prompt/instruction, if any.
• /set subcommands:
• /set parameter <name> <value> – adjust temperature, top‑p, etc., on the fly.
• /set system <instruction> – define a new system prompt (e.g., “you are a helpful assistant”).
• Positioning of CLI usage
• Mainly for local experimentation and testing: quick system prompt and parameter iterations before wiring into full apps via code.


Using Ollama from Python (Ollama library)


5. Setup
• Install library: pip install ollama.
• Import: import ollama.
6. Text generation with generate
• ollama.generate(model="llama3.2:1b", prompt="Why does the moon glow?") returns a dict with fields like model, created_at, timings, and response (text completion).
• Access text via response["response"].
• stream=True streams tokens chunk‑by‑chunk (iterate over chunks and print).
7. Parameters and system prompt in code
• system="You are a funny assistant" – injects system instruction.
• options={...} – tuning decoding: temperature, top_k, top_p, min_p, stop tokens, etc., matching documented API parameters.
8. Sending images from Python
• Convert image(s) to base64 (using base64 module) and pass via images=[<base64-strings>] in generate.
• Example tasks: caption single image, generate story from multiple images.
9. Limitations of generate
• Stateless: one prompt → one response, no conversation history or context awareness.
10. Chat‑style conversations with chat
• Use ollama.chat with messages=[{"role": "user"/"assistant"/"system", "content": "..."}] to maintain full conversation history and context.
• chat supports tool calling (via tools parameter) unlike generate.
11. Other Python helper methods
• ollama.list() – list local models programmatically.
• ollama.pull(model="..."), ollama.delete(model="..."), ollama.show(model="...") – code equivalents of CLI commands.


Tool calling: concepts and implementation


12. What tool calling is
• Method that allows an LLM to use external tools/systems to perform tasks it cannot do itself (e.g., database access, live weather, today’s news).
• Extends capabilities beyond static training data and knowledge cutoff by delegating to Python functions.
13. Why LLMs need tools
• LLM limitations: knowledge cutoff, no direct internet/DB access, cannot execute actions by themselves.
• Tools = Python functions containing code to do real work (DB query, API call, computation, etc.).
14. General tool‑calling flow (conceptual)
• Step 1: Define tools (Python functions) for each external capability.
• Step 2: Define tool schema (JSON description) listing each function: name, description, parameters (names, types, required, descriptions).
• Step 3: Call the LLM with your prompt + tools schema.
• If LLM can answer directly, it does.
• If not, it reads tool schema, chooses a tool, and decides parameter values by parsing the user prompt.
• Step 4: LLM returns a JSON object describing which tool to call and with what arguments.
• Step 5: Your code executes the Python function with those arguments and collects the result.
• Step 6: Call the LLM again with the full message history: original user prompt, assistant’s tool‑call message, tool result; LLM then produces the final natural‑language answer.
15. Ollama‑specific details
• Only models with “tools” capability in Ollama’s model card can perform tool calls (e.g., specific Qwen / Gamma variants).
• Tool calling is only available via chat API (tools parameter); generate does not support tools.
16. End‑to‑end example used in video
• Scenario: electronics shop.
• Dummy “inventory” DB (dict): products with quantity and base_price.
• Tool 1: check_inventory(product_name) – looks up product, returns availability, stock, and base price.
• Tool 2: calculate_loyalty_discount(base_price, years_as_customer) – computes loyalty discount capped at 30%, returns final price.
• Tool schema:
• JSON definitions for both tools including parameter types and descriptions.
• Conversation messages list:
• Start with {"role": "user", "content": "I want to buy an iPhone, can you check stock?"} stored in messages.
• First ollama.chat(...) call:
• model="qwen3:8b" (with tools capability), messages=messages, tools=<schema>.
• LLM responds with an assistant message whose tool_calls field indicates which function to call and with what argument (e.g., {"name": "check_inventory", "arguments": {"product_name": "iPhone"}}).
• Host code logic:
• Extract tool name and arguments from response.
• Map tool name to actual Python function and call it.
• Append tool result back into messages with role="tool" plus the result payload.
• Second ollama.chat(...) call:
• Same model, updated messages including user → assistant (tool call) → tool (result).
• LLM now returns human‑friendly answer like “The iPhone is out of stock” or “5 laptops available at price X.”
• Example prompts:
• Check stock for laptop vs iPhone.
• Compute final price for a 5‑year loyal customer buying a laptop (LLM decides to call both tools in order).


Model Files and customizing behavior


• Problem: general‑purpose LLM vs specialized behavior
• Base LLM can do everything (code, Shakespeare, etc.), but production apps often need specialized personas: polite support bot, harsh code reviewer, Gen‑Z casual bot, etc.
• Two approaches:
• Heavyweight: design new architecture and fully train/fine‑tune – expensive.
• Lightweight (what Ollama exposes via Model Files): keep base LLM weights, but wrap them with a specific instruction template and parameters to create a “specialized” variant.
• Conceptual mechanism:
• Take a general‑purpose model as “brain.”
• Prepare an instruction file describing how it should behave (tone, role, constraints, response style).
• Combine them into a new named model via Ollama’s Model File, without changing underlying weights.
• Intuition example:
• Bright student already knows math; you just teach a shortcut method. Knowledge is unchanged; only the way they apply it changes.



