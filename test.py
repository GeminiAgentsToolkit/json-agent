from json_agent import create_agent


if __name__ == "__main__":
    agent = create_agent(model_name="gemini-1.5-flash", debug=True)
    # read file "test.yaml" to string variable
    with open("test.yaml", "r") as f:
        file_content = f.read()
        print(agent.send_message(f"please convert to json: {file_content}"))