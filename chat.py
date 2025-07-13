crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8
    }
}

while True:
    user_query = input("\nYou: ").lower()

    if "trending" in user_query:
        print("CryptoSage: These cryptos are trending up:")
        for coin, data in crypto_db.items():
            if data["price_trend"] == "rising":
                print(f"- {coin} 🚀")

    elif "sustainable" in user_query:
        recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        print(f"CryptoSage: {recommend} 🌱 is the most sustainable choice!")

    elif "most profitable" in user_query:
        for coin, data in crypto_db.items():
            if data["price_trend"] == "rising" and data["market_cap"] == "high":
                print(f"CryptoSage: {coin} 📈 looks profitable right now!")
                break

    elif "long-term" in user_query:
        for coin, data in crypto_db.items():
            if data["sustainability_score"] > 7 and data["price_trend"] == "rising":
                print(f"CryptoSage: For long-term growth, consider {coin}! 🌟")
                break

    elif "exit" in user_query:
        print("CryptoSage: Goodbye! Remember, always do your own research! ⚠️")
        break

    else:
        print("CryptoSage: Sorry, I didn’t understand that. Try asking about trending, sustainability, or profitability.")


print("👋 Hello! I'm CryptoSage — your friendly crypto guide! 🚀")
print("Ask me anything about trends, sustainability, or what to invest in!")
