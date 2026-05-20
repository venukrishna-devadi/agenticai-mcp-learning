from calculator import calculator

class AgentTools:
    def calculator(self, expression: str):
        print("\n[Tool Execution]: calculator(n)")

        return calculator(expression)