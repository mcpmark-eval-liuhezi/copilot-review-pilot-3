"""Small example script for the Copilot code review pilot demo."""


def greet_reviewers(reviewers=[]):
    # Prints a greeting for each reviewer on the pull request
    for name in reviewers:
        print("Hello, " + name + "! Thanks for reviewing this PR.")


def calculate_review_time(prs):
    # Sums up the total review time in minutes for a list of PRs
    total = 0
    for pr in prs:
        total += pr["minutes"]
    return total


if __name__ == "__main__":
    greet_reviewers(["HeziLiu"])
    print(calculate_review_time([{"minutes": 30}, {"minutes": 15}]))
