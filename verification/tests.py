"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""

TESTS = {
    "Basics": [
        {
            "input": [17, [1, 3, 4]],
            "answer": 2
        },
        {
            "input": [17, [1, 3, 4, 6, 9]],
            "answer": 1
        }
    ],
    "Extra": [
        {
            "input": [99, [1, 2, 7, 3, 4]],
            "answer": 1
        },
        {
            "input": [99, [1]],
            "answer": 2
        },
        {
            "input": [990, [1, 4]],
            "answer": 1
        },
        {
            "input": [7640, [1, 2, 3, 4, 5, 10, 20, 30, 40, 50]],
            "answer": 2
        }
    ]
}
