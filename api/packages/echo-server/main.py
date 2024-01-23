from echo_server import agent_executor

if __name__ == "__main__":
    original_query = "What do you know about Vertex John?"
    followup_query = "email"
    chat_history = [
        (
            "What do you know about vertex email John?",
            "I found multiple emails named John. Could you please specify "
            "which one you are interested in? Here are some options:"
            "\n\n1. john@me.com\n2. john@lt.com",
        )
    ]
    print(agent_executor.invoke({"input": original_query}))
    print(
        agent_executor.invoke({"input": followup_query, "chat_history": chat_history})
    )
