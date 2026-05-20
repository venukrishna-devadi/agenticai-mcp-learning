def filter_transaction(content: str, keyword: str) -> list:

    """
    Extract transaction matching keyword.
    Returns list of dicts with merchant and amount
    """

    results = []
    lines = content.split("\n")

    for line in lines:

        if keyword.lower() in line.lower():
            # we will extract the amount, we will look for negative numbers with $

            for word in line.split():
                if "$" in word or (word.startswith("-")) and word[1:].replace(".","").isdigit():

                    # 1. we will clean the amount
                    amount_str = word.replace("$", "").replace(",","")
                    try:
                        amount = float(amount_str)
                        results.append(
                            {
                                "merchant": line[:50].strip(),
                                "amount": amount
                            }
                        )

                        break # found amount move to next line
                    except Exception as e:
                        pass
    
    return results


def sum_amounts(transactions: list) -> float:
    total = 0

    for t in transactions:
        total += t["amount"]
    
    return total