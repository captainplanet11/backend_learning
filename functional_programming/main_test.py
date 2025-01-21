# # ch1 L1
# from main import *

# run_cases = [
#     (
#         """The Importance of FP
# Learn how functional programming can change the way you think about code.
# Benefits include immutability, simplicity, and composability.""",
#         """          The Importance of FP          
# ****************************************
# Learn how functional programming can change the way you think about code.
# Benefits include immutability, simplicity, and composability.""",
#     ),
# ]

# submit_cases = run_cases + [
#     (
#         """Short Title
# Equally short story""",
#         """              Short Title               \n****************************************
# Equally short story""",
#     ),
#     (
#         """DocToDoc: A Guide
# Understanding the art of document conversion.
# We write cool functional code to make it happen.""",
#         """           DocToDoc: A Guide            
# ****************************************
# Understanding the art of document conversion.
# We write cool functional code to make it happen.""",
#     ),
# ]


# def test(input1, expected_output):
#     print("---------------------------------")
#     print(f"Inputs:")
#     print(f" * document: {input1}\n")
#     print(f"Expecting:\n{expected_output}\n")
#     result = stylize_title(input1)
#     print(f"Actual:\n{result}\n")
#     if result == expected_output:
#         print("Pass")
#         return True
#     print("Fail")
#     return False


# def main():
#     passed = 0
#     failed = 0
#     for test_case in test_cases:
#         correct = test(*test_case)
#         if correct:
#             passed += 1
#         else:
#             failed += 1
#     if failed == 0:
#         print("============= PASS ==============")
#     else:
#         print("============= FAIL ==============")
#     print(f"{passed} passed, {failed} failed")


# test_cases = submit_cases
# if "__RUN__" in globals():
#     test_cases = run_cases

# main()

#ch1 L3 


# from main import *

# run_cases = [
#     (
#         ("hello there", "sonny", "how ya doing"),
#         ("0. hello there", "1. sonny", "2. how ya doing"),
#     )
# ]

# submit_cases = run_cases + [
#     (
#         ("go", "python", "java", "javascript"),
#         ("0. go", "1. python", "2. java", "3. javascript"),
#     ),
#     (
#         ("boots", "everyone else"),
#         ("0. boots", "1. everyone else"),
#     ),
# ]


# def test(input1, expected_output):
#     print("---------------------------------")
#     print(f"Inputs:")
#     print(f" * documents: {input1}")
#     print(f"Expecting: {expected_output}")
#     try:
#         documents = ()
#         for doc in input1:
#             documents = add_prefix(doc, documents)
#     except Exception as e:
#         documents = f"Error: {e}"
#     print(f"Actual: {documents}")
#     if documents == expected_output:
#         print("Pass")
#         return True
#     print("Fail")
#     return False


# def main():
#     passed = 0
#     failed = 0
#     for test_case in test_cases:
#         correct = test(*test_case)
#         if correct:
#             passed += 1
#         else:
#             failed += 1
#     if failed == 0:
#         print("============= PASS ==============")
#     else:
#         print("============= FAIL ==============")
#     print(f"{passed} passed, {failed} failed")


# test_cases = submit_cases
# if "__RUN__" in globals():
#     test_cases = run_cases

# main()

#ch1 L6 

# from main import *

# run_cases = [
#     ([4, 3, 2, 1, 5], 3),
#     ([20, 14, 16], 16),
#     ([9, 11, 16, 20], 11),
# ]

# submit_cases = run_cases + [
#     ([8, 8, 8], 8),
#     ([30, 18, 14, 22], 18),
#     ([6, 24, 6, 6, 24, 24, 2, 1, 3], 6),
#     ([], None),
# ]


# def test(input, expected_output):
#     print("---------------------------------")
#     print(f"Input: {input}")
#     print(f"Expected: {expected_output}")
#     input_copy = input.copy()
#     result = get_median_font_size(input)
#     print(f"Actual: {result}")
#     if result != expected_output:
#         print("Fail")
#         return False
#     if input != input_copy:
#         print(f"Expected font_sizes: {input_copy}")
#         print(f"Actual font_sizes: {input}")
#         print("font_sizes was modified")
#         print("Fail")
#         return False
#     print("Pass")
#     return True


# def main():
#     passed = 0
#     failed = 0
#     for test_case in test_cases:
#         correct = test(*test_case)
#         if correct:
#             passed += 1
#         else:
#             failed += 1
#     if failed == 0:
#         print("============= PASS ==============")
#     else:
#         print("============= FAIL ==============")
#     print(f"{passed} passed, {failed} failed")


# test_cases = submit_cases
# if "__RUN__" in globals():
#     test_cases = run_cases

# main()

# from main import *

# run_cases = [
#     (
#         "You can't spell America without Erica",
#         "YOU CAN'T SPELL AMERICA WITHOUT ERICA...",
#     ),
#     ("Friends don't lie.", "FRIENDS DON'T LIE..."),
#     (" She's our friend and she's crazy!", "SHE'S OUR FRIEND AND SHE'S CRAZY!..."),
# ]

# submit_cases = run_cases + [
#     (" You're gonna slay 'em dead, Nance. ", "YOU'RE GONNA SLAY 'EM DEAD, NANCE..."),
# ]


# def test(input, expected_output):
#     print("---------------------------------")
#     print(f"Input: {input}")
#     print(f"Expected: {expected_output}")
#     result = format_line(input)
#     print(f"Actual: {result}")
#     if result != expected_output:
#         print("Fail")
#         return False
#     print("Pass")
#     return True


# def main():
#     passed = 0
#     failed = 0
#     for test_case in test_cases:
#         correct = test(*test_case)
#         if correct:
#             passed += 1
#         else:
#             failed += 1
#     if failed == 0:
#         print("============= PASS ==============")
#     else:
#         print("============= FAIL ==============")
#     print(f"{passed} passed, {failed} failed")


# test_cases = submit_cases
# if "__RUN__" in globals():
#     test_cases = run_cases

# main()
#ch1 C1

# from main import *

# run_cases = [
#     (
#         "live long and prosper",
#         "Live Long And Prosper",
#     ),
#     (
#         "...Khan",
#         "...KHAN!!!",
#     ),
#     ("BEAM ME UP, BOOTS!", "Beam me up, boots"),
# ]

# submit_cases = run_cases + [
#     (
#         "",
#         "",
#     ),
#     (
#         "I aM a DoCtOr, nOt A fUnCtIoNaL pRoGrAmMeR!!",
#         "I aM a DoCtOr, nOt A fUnCtIoNaL pRoGrAmMeR!!",
#     ),
#     (
#         "TO BOLDLY GO WHERE NO BEAR HAS GONE BEFORE!!!!",
#         "To boldly go where no bear has gone before",
#     ),
#     (
#         "Illogical",
#         "ILLOGICAL!!!",
#     ),
# ]


# def test(input, expected_output):
#     print("---------------------------------")
#     print(f"   Input: {input}")
#     print(f"Expected: {expected_output}")
#     result = toggle_case(input)
#     print(f"  Actual: {result}")
#     if result != expected_output:
#         print("Fail")
#         return False
#     print("Pass")
#     return True


# def main():
#     passed = 0
#     failed = 0
#     for test_case in test_cases:
#         correct = test(*test_case)
#         if correct:
#             passed += 1
#         else:
#             failed += 1
#     if failed == 0:
#         print("============= PASS ==============")
#     else:
#         print("============= FAIL ==============")
#     print(f"{passed} passed, {failed} failed")


# test_cases = submit_cases
# if "__RUN__" in globals():
#     test_cases = run_cases

# main()

# from main import *


# run_cases = [
#     (
#         "00FFFF",
#         (0, 255, 255),
#     ),
#     (
#         "FFFF00",
#         (255, 255, 0),
#     ),
#     (
#         "Hello!",
#         "not a hex color string",
#     ),
#     (
#         "42",
#         "not a hex color string",
#     ),
#     (
#         1_000_000,
#         "not a hex color string",
#     ),
# ]

# submit_cases = run_cases + [
#     (
#         "",
#         "not a hex color string",
#     ),
#     (
#         "FF00FF",
#         (255, 0, 255),
#     ),
#     (
#         "000000",
#         (0, 0, 0),
#     ),
#     (
#         "FFFFFF",
#         (255, 255, 255),
#     ),
# ]


# def test(input, expected_output):
#     print("---------------------------------")
#     print(f"  Inputs: '{input}'")
#     print(f"Expected: {expected_output}")
#     try:
#         result = hex_to_rgb(input)
#     except Exception as e:
#         result = str(e)
#     print(f"  Actual: {result}")
#     if result != expected_output:
#         print("Fail")
#         return False
#     print("Pass")
#     return True


# def main():
#     passed = 0
#     failed = 0
#     for test_case in test_cases:
#         correct = test(*test_case)
#         if correct:
#             passed += 1
#         else:
#             failed += 1
#     if failed == 0:
#         print("============= PASS ==============")
#     else:
#         print("============= FAIL ==============")
#     print(f"{passed} passed, {failed} failed")


# test_cases = submit_cases
# if "__RUN__" in globals():
#     test_cases = run_cases

# main()

from main import *


run_cases = [
    (
        [1, 2, 3, 4, 5],
        [4, 5, 6, 7, 8],
        True,
        [8, 7, 6, 5, 4, 3, 2, 1],
    ),
    (
        ["tent", "sleeping bag", "camp stove", "lantern", "backpack"],
        ["flashlight", "tent", "camp chair", "sleeping bag", "water bottle"],
        False,
        [
            "backpack",
            "camp chair",
            "camp stove",
            "flashlight",
            "lantern",
            "sleeping bag",
            "tent",
            "water bottle",
        ],
    ),
    (
        ["milk", "bread", "eggs", "cheese", "apples"],
        ["milk", "bananas", "bread", "oranges", "cheese"],
        True,
        ["oranges", "milk", "eggs", "cheese", "bread", "bananas", "apples"],
    ),
    (
        ["soccer ball", "tennis racket", "basketball", "baseball glove"],
        ["baseball bat", "soccer ball", "tennis balls", "basketball", "helmet"],
        False,
        [
            "baseball bat",
            "baseball glove",
            "basketball",
            "helmet",
            "soccer ball",
            "tennis balls",
            "tennis racket",
        ],
    ),
]


submit_cases = run_cases + [
    (
        ["notebooks", "pencils", "backpack", "textbooks", "laptop"],
        ["highlighters", "notebooks", "erasers", "backpack", "calculator"],
        False,
        [
            "backpack",
            "calculator",
            "erasers",
            "highlighters",
            "laptop",
            "notebooks",
            "pencils",
            "textbooks",
        ],
    ),
    (
        ["tent", "milk", "soccer ball", "notebooks"],
        ["bread", "tent", "swim goggles", "pencils", "milk"],
        True,
        [
            "tent",
            "swim goggles",
            "soccer ball",
            "pencils",
            "notebooks",
            "milk",
            "bread",
        ],
    ),
]


def test(input1, input2, input3, expected_output):
    print("---------------------------------")
    print(f"List 1: {input1}")
    print(f"List 2: {input2}")
    if input3:
        print(f"Reversed")
    print(f"Expected: {expected_output}")
    result = deduplicate_lists(input1, input2, input3)
    print(f"  Actual: {result}")
    if result != expected_output:
        print("Fail")
        return False
    print("Pass")
    return True


def main():
    passed = 0
    failed = 0
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()