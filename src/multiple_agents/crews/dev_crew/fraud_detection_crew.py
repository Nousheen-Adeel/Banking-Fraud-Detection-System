from crewai import Agent, Crew, Task
from crewai.project import CrewBase, agent, crew, task
import pandas as pd
import logging


@CrewBase
class FraudDetectionCrew:
    """Fraud Detection and Phishing Prevention Crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    def __init__(self):
        # Initialize logging
        logging.basicConfig(filename="logs/fraud_detection.log", level=logging.INFO)

    @agent
    def junior_python_developer(self) -> Agent:
        config = self.agents_config["junior_python_developer"].copy()
        config.pop('id', None)  # Remove id field before creating Agent
        return Agent(
            config=config,
        )

    @agent
    def senior_python_developer(self) -> Agent:
        config = self.agents_config["senior_python_developer"].copy()
        config.pop('id', None)  # Remove id field before creating Agent
        return Agent(
            config=config,
        )

    @task
    def develop_fraud_detection_model(self) -> Task:
        return Task(
            config=self.tasks_config["develop_fraud_detection_model"],
        )

    @task
    def review_security_measures(self) -> Task:
        return Task(
            config=self.tasks_config["review_security_measures"],
        )

    def load_transaction_data(self):
        """Loads transaction data from CSV"""
        try:
            df = pd.read_csv("src/multiple_agents/data/transactions.csv")
            return df
        except Exception as e:
            logging.error(f"Error loading transaction data: {e}")
            return None

    def detect_fraud(self):
        """Simple fraud detection logic using transaction dataset"""
        df = self.load_transaction_data()
        if df is not None:
            fraud_cases = df[df["is_fraud"] == 1]
            logging.info(f"Fraud cases detected: \n{fraud_cases}")
            return fraud_cases
        return "No fraud data available."

    def detect_phishing(self):
        """Simple phishing detection using phishing email dataset"""
        try:
            df = pd.read_csv("src/multiple_agents/data/phishing_emails.csv")
            phishing_cases = df[df["label"] == "Phishing"]
            logging.info(f"Phishing emails detected: \n{phishing_cases}")
            return phishing_cases
        except Exception as e:
            logging.error(f"Error loading phishing email data: {e}")
            return "No phishing data available."

    @crew
    def crew(self) -> Crew:
        """Creates the Fraud Detection and Security Crew"""

        junior_dev = self.junior_python_developer()
        senior_dev = self.senior_python_developer()

        fraud_task = Task(
            description="Analyze banking transactions and flag suspicious ones as fraud.",
            expected_output="Identified fraudulent transactions in a structured report.",
            agent=junior_dev
        )

        security_task = Task(
            description="Enhance security measures and ensure fraud detection model accuracy.",
            expected_output="Improved fraud detection system with high accuracy and security compliance.",
            agent=senior_dev
        )

        return Crew(
            agents=[junior_dev, senior_dev],
            tasks=[fraud_task, security_task]
        )
