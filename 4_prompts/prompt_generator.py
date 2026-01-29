from langchain_core.prompts import PromptTemplate

#template
template= PromptTemplate(template="""Please summarize the research paper titled "{paper_input}" with the following specifications:
Explanation style: {style_input}
Explanation length: {length_input}
1. Problem Statement
2. Motivation and Background
3. Methodology
4. Key Results
5. Contributions
6. Limitations (if mentioned)
7. Future Work (if mentioned)

Rules:
- Be concise but informative
- Do not add information not present in the paper
- Use bullet points where appropriate
- Maintain an academic tone""",
                         input_variables=['paper_input', 'style_input', 'length_input'])

template.save('template.json')
