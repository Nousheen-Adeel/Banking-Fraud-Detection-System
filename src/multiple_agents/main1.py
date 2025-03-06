from crewai.flow import Flow, start
from multiple_agents.crews.dev_crew.fraud_detection_crew import FraudDetectionCrew


class FraudDetectionFlow(Flow):
    """Flow for fraud detection crew"""
    @start()
    def run_fraud_detection_crew(self):
        output = FraudDetectionCrew().crew().kickoff(  
            inputs={
                "problem": "Develop a Python-based fraud detection system for banking transactions and phishing attack prevention."
            }
        )
        return output.raw

def kickoff():
    fraud_flow = FraudDetectionFlow()
    result = fraud_flow.kickoff()
    print(result)
