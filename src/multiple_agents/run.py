from multiple_agents.crews.dev_crew.fraud_detection_crew import FraudDetectionCrew

def main():
    crew = FraudDetectionCrew()

    print("\n🔍 Running Fraud Detection System...")

    # Detect fraud in transactions
    fraud_cases = crew.detect_fraud()
    print("\n📌 Fraud Cases Detected:\n", fraud_cases)

    # Detect phishing emails
    phishing_cases = crew.detect_phishing()
    print("\n📩 Phishing Emails Detected:\n", phishing_cases)

if __name__ == "__main__":
    main()
