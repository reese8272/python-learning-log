# llm_cost.py - helps visualize the token cost for different models and how tokens in and out affect cost

PRICING = { # these are PER MILLION, as documented by the recent pricing as of 6/22/26
    "haiku-4.5": (1, 5),
    "sonnet-4.6": (3, 15),
    "opus-4.8": (5, 25),
}

def estimate(words_in: int, words_out: int, model: str):
    tok_in = words_in * 1.33 # or roughly 0.75 words per token, this is simply an ESTIMATE, models vary.
    tok_out = words_out * 1.33 # ^^
    p_in, p_out = PRICING[model]
    total_cost = (tok_in / 1e6) * p_in + (tok_out / 1e6) * p_out # use / to normalize the number to per million (token in / one million)
    return total_cost

for m in PRICING:
    print(f"{m}: ${estimate(2000, 300, m):.5f}/turn") # testing a 2000 in, 300 out