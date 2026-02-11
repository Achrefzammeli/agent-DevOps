from agent.agent import ask_agent

def main():
    print("🤖 Agent DevOps - mode CLI")
    print("Tape une erreur technique (ou 'exit')\n")

    while True:
        user_input = input(">>> ").strip()

        if user_input.lower() == "exit":
            print("👋 Fin de session.")
            break

        if not user_input:
            print("⚠️ Veuillez entrer une erreur technique valide.\n")
            continue

        response = ask_agent(user_input)

        print("\n--- Réponse de l'agent ---")
        print(response)
        print("-------------------------\n")

if __name__ == "__main__":
    main()
