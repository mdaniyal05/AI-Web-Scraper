from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from templates.llm_template import template

model = OllamaLLM(model="llama3.1")


def parse_with_llama3(content_chunks, parse_description):
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model

    parsed_results = []

    for i, chunk in enumerate(content_chunks, start=1):
        response = chain.invoke(
            {"content": chunk, "parse_description": parse_description})

        print(f"Parsed batch {i} of {len(content_chunks)}")

        parsed_results.append(response)

    return "\n".join(parsed_results)
