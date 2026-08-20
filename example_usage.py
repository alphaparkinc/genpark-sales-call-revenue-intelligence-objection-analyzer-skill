from client import SalesCallRevenueIntelligenceObjectionAnalyzerClient

def main():
    client = SalesCallRevenueIntelligenceObjectionAnalyzerClient()
    transcript = "Prospect: We like the platform, but need to verify SOC2 compliance before signing $120k ARR contract."
    res = client.analyze_sales_call(transcript, 120000.0)
    print(f"Deal Health Score: {res['deal_health_score']}/10")
    print(f"Win Probability: {res['win_probability_pct']}%")
    print(f"Next Best Action: {res['next_best_action']}")
    print("Detected Objections:", res["detected_objections"])

if __name__ == "__main__":
    main()
