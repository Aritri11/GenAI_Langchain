Simple Chain
The most basic chain:
One input → One LLM call → One output


Sequential Chain
Multiple chains executed one after another, where the output of one becomes the input of the next.
Input → Chain 1 → Chain 2 → Chain 3 → Final Output


Conditional Chain
A chain that chooses different paths based on conditions.
It’s like if-else logic for LLM workflows.
Input → Decision Step → Route to Different Chains


Parallel Chain
Multiple chains run at the same time, and their outputs are combined.
Input → Chain A ┐
               ├→ Combine Results → Output
        → Chain B ┘




























