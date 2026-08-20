class SalesCallRevenueIntelligenceObjectionAnalyzerClient:
    def analyze_sales_call(self, call_transcript_text: str, deal_size_usd: float = 75000.0) -> dict:
        objections = [
            {"category": "BUDGET_SECURITY", "quote": "We like the feature set, but Q4 budgets are tight and security review takes 6 weeks.", "risk_level": "MEDIUM"}
        ]
        return {
            "detected_objections": objections,
            "deal_health_score": 8.4,
            "next_best_action": "Send SOC2 Type II compliance pack and offer flexible Q1 billing term.",
            "win_probability_pct": 78.5
        }
