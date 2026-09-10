def calculate_threat_score(cpu, memory, status):

    score = 0

    # CPU contribution
    if cpu > 80:
        score += 50
    elif cpu > 50:
        score += 30

    # Memory contribution
    if memory > 50:
        score += 30
    elif memory > 20:
        score += 15

    # Suspicious status contribution
    if status == "HIGH_CPU":
        score += 20

    elif status == "SUSPICIOUS":
        score += 40

    # Limit max score
    if score > 100:
        score = 100

    return score