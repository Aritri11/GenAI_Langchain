Runnable = any component that can take input, do something, and return output.


RunnableSequence:


Runs components step-by-step in order.


Output of one → input of the next.


RunnableParallel:


Runs multiple runnables at the same time and returns all outputs.


RunnableBranch (Conditional Runnable):


Routes execution based on conditions.


RunnableLambda:


Wraps a Python function as a runnable.


RunnablePassthrough:


Passes input forward unchanged.































