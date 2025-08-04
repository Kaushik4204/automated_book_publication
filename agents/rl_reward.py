def calculate_reward(review_feedback):
    import re
    match = re.search(r"score.*?(\d+)/10", review_feedback, re.IGNORECASE)
    if match:
        return int(match.group(1))
    return 5  # Neutral default
