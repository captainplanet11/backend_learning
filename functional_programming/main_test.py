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

# from main import *


# run_cases = [
#     (
#         [1, 2, 3, 4, 5],
#         [4, 5, 6, 7, 8],
#         True,
#         [8, 7, 6, 5, 4, 3, 2, 1],
#     ),
#     (
#         ["tent", "sleeping bag", "camp stove", "lantern", "backpack"],
#         ["flashlight", "tent", "camp chair", "sleeping bag", "water bottle"],
#         False,
#         [
#             "backpack",
#             "camp chair",
#             "camp stove",
#             "flashlight",
#             "lantern",
#             "sleeping bag",
#             "tent",
#             "water bottle",
#         ],
#     ),
#     (
#         ["milk", "bread", "eggs", "cheese", "apples"],
#         ["milk", "bananas", "bread", "oranges", "cheese"],
#         True,
#         ["oranges", "milk", "eggs", "cheese", "bread", "bananas", "apples"],
#     ),
#     (
#         ["soccer ball", "tennis racket", "basketball", "baseball glove"],
#         ["baseball bat", "soccer ball", "tennis balls", "basketball", "helmet"],
#         False,
#         [
#             "baseball bat",
#             "baseball glove",
#             "basketball",
#             "helmet",
#             "soccer ball",
#             "tennis balls",
#             "tennis racket",
#         ],
#     ),
# ]


# submit_cases = run_cases + [
#     (
#         ["notebooks", "pencils", "backpack", "textbooks", "laptop"],
#         ["highlighters", "notebooks", "erasers", "backpack", "calculator"],
#         False,
#         [
#             "backpack",
#             "calculator",
#             "erasers",
#             "highlighters",
#             "laptop",
#             "notebooks",
#             "pencils",
#             "textbooks",
#         ],
#     ),
#     (
#         ["tent", "milk", "soccer ball", "notebooks"],
#         ["bread", "tent", "swim goggles", "pencils", "milk"],
#         True,
#         [
#             "tent",
#             "swim goggles",
#             "soccer ball",
#             "pencils",
#             "notebooks",
#             "milk",
#             "bread",
#         ],
#     ),
# ]


# def test(input1, input2, input3, expected_output):
#     print("---------------------------------")
#     print(f"List 1: {input1}")
#     print(f"List 2: {input2}")
#     if input3:
#         print(f"Reversed")
#     print(f"Expected: {expected_output}")
#     result = deduplicate_lists(input1, input2, input3)
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


# def to_string(file):
#     return (
#         f"File: {file['filename']}\n"
#         f"Author: {file['author_first_name']} {file['author_last_name']}\n"
#         f"Content: {file['content']}"
#     )


# run_cases = [
#     (
#         {
#             "filename": "essay.txt",
#             "content": "Dear Mr. Vernon, we accept the fact that we had to sacrifice a whole Saturday in detention for whatever it was we did wrong...",
#             "author_first_name": "Brian",
#             "author_last_name": "Johnson",
#         },
#         "```\nFile: essay.txt\nAuthor: Brian Johnson\nContent: Dear Mr. Vernon, we accept the fact that we had to sacrifice a whole Saturday in detention for whatever it was we did wrong...\n```",
#     ),
#     (
#         {
#             "filename": "letter.txt",
#             "content": "But we think you're crazy to make us write an essay telling you who we think we are.",
#             "author_first_name": "Brian",
#             "author_last_name": "Johnson",
#         },
#         "```\nFile: letter.txt\nAuthor: Brian Johnson\nContent: But we think you're crazy to make us write an essay telling you who we think we are.\n```",
#     ),
# ]

# submit_cases = run_cases + [
#     (
#         {
#             "filename": "note.txt",
#             "content": "Does Barry Manilow know that you raid his wardrobe?",
#             "author_first_name": "John",
#             "author_last_name": "Bender",
#         },
#         "```\nFile: note.txt\nAuthor: John Bender\nContent: Does Barry Manilow know that you raid his wardrobe?\n```",
#     ),
# ]


# def test(input1, expected_output):
#     print("---------------------------------")
#     print("Inputs:")
#     print(f"  filename: {input1['filename']}")
#     print(f"  content: {input1['content'][:30]}...")  # Truncate for display
#     print(f"  author_first_name: {input1['author_first_name']}")
#     print(f"  author_last_name: {input1['author_last_name']}")
#     print(f"Expecting:\n{expected_output}")
#     result = file_to_prompt(input1, to_string)
#     print(f"Actual:\n{result}")
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

#ch2 L2

# from main import *

# run_cases = [
#     (
#         [("document", [".doc", ".docx"]), ("image", [".jpg", ".png"])],
#         ".doc",
#         "document",
#     ),
#     (
#         [("document", [".doc", ".docx"]), ("image", [".jpg", ".png"])],
#         ".png",
#         "image",
#     ),
# ]

# submit_cases = run_cases + [
#     (
#         [("document", [".doc", ".docx"]), ("image", [".jpg", ".png"])],
#         ".txt",
#         "Unknown",
#     ),
#     (
#         [("code", [".py", ".js"]), ("markup", [".html", ".xml"])],
#         ".js",
#         "code",
#     ),
# ]


# def test(file_extension_tuples, ext, expected_output):
#     try:
#         print("---------------------------------")
#         print("Input tuples:")
#         for file_type, exts in file_extension_tuples:
#             print(f"  {file_type}: {exts}")
#         print(f"Extension: {ext}")
#         print(f"Expecting: {expected_output}")
#         getter_function = file_type_getter(file_extension_tuples)
#         result = getter_function(ext)
#         print(f"Actual: {result}")
#         if result == expected_output:
#             print("Pass")
#             return True
#         print("Fail")
#         return False
#     except Exception as e:
#         print("Fail")
#         print(e)
#         return False


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

#ch3 L5 

# from main import *

# run_cases = [
#     (
#         "* Alai\n- Dink Meeker\n",
#         "* Alai\n* Dink Meeker\n",
#     ),
#     (
#         "* Ender Wiggin\n- Petra Arkanian\n* Bean\n",
#         "* Ender Wiggin\n* Petra Arkanian\n* Bean\n",
#     ),
# ]

# submit_cases = run_cases + [
#     (
#         "- Bonzo Madrid\n- Stilson\n- The Formics\n- Peter Wiggin\n- Valentine Wiggin\n- Colonel Graff\n",
#         "* Bonzo Madrid\n* Stilson\n* The Formics\n* Peter Wiggin\n* Valentine Wiggin\n* Colonel Graff\n",
#     ),
# ]


# def test(input_document, expected_output):
#     print("---------------------------------")
#     print("Input document:")
#     print(input_document)
#     print("Expected output:")
#     print(expected_output)
#     result = change_bullet_style(input_document)
#     print("Actual output:")
#     print(result)
#     if result == expected_output:
#         print("Pass")
#         return True
#     if expected_output.endswith("\n") and not result.endswith("\n"):
#         print("Fail")
#         print("Reason: expected newline at the end of the output")
#         return False
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


# from main import *

# run_cases = [
#     (
#         "\n* We are the music makers\n- And we are the dreamers of dreams\n* Come with me and you'll be\n",
#         "\n* We are the music makers\n* Come with me and you'll be\n",
#     ),
#     (
#         "\n* In a world of pure imagination\n- There is no life I know\n* Living there - you'll be free\n",
#         "\n* In a world of pure imagination\n* Living there - you'll be free\n",
#     ),
# ]

# submit_cases = run_cases + [
#     (
#         "\n* If you want to view paradise\n- Simply look around and view it\n* Anything you want to, do it\n* There is no life I know\n- To compare with pure imagination\n* Living there, you'll be free\n",
#         "\n* If you want to view paradise\n* Anything you want to, do it\n* There is no life I know\n* Living there, you'll be free\n",
#     ),
# ]


# def test(input_document, expected_output):
#     print("---------------------------------")
#     print("Input document:")
#     print('"' + input_document + '"')
#     print("Expected output:")
#     print('"' + expected_output + '"')
#     result = remove_invalid_lines(input_document)
#     print("Actual output:")
#     print('"' + result + '"')
#     if result == expected_output:
#         print("Pass")
#         return True

#     if expected_output.endswith("\n") and not result.endswith("\n"):
#         print("Fail")
#         print("Reason: expected newline at the end of the output")
#         return False

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



# from main import *

# run_cases = [
#     (
#         ["I don't feel safe", "Are you cussing with me?"],
#         2,
#         "I don't feel safe. Are you cussing with me?.",
#     ),
#     (
#         ["You're fantastic", "He's just another rat", "Where'd the food come from?"],
#         2,
#         "You're fantastic. He's just another rat.",
#     ),
# ]

# submit_cases = run_cases + [
#     (["I'm not different"], 0, ""),
#     (
#         [
#             "You wrote a bad song",
#             "This is a good idea",
#             "Just buy the tree",
#             "It's going to flood",
#             "Tell us what to do",
#             "Here comes the train",
#             "Are you cussing with me?",
#             "This is just cider",
#             "Get me a bandit hat",
#         ],
#         3,
#         "You wrote a bad song. This is a good idea. Just buy the tree.",
#     ),
# ]


# def test(input_sentences, input_n, expected_output):
#     print("---------------------------------")
#     print("Inputs:")
#     print(f" * sentences: {input_sentences}")
#     print(f" * n: {input_n}")
#     print("Expecting:")
#     print(f" * {expected_output}")
#     result = join_first_sentences(input_sentences, input_n)
#     print("Actual:")
#     print(f" * {result}")
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


# from main import *

# run_cases = [
#     (["PDF", "DOCX", "TXT"], ["PDF", "MD", "HTML"], set(["PDF"])),
#     (
#         ["PDF", "DOCX", "TXT", "HTML"],
#         ["PDF", "MD", "HTML", "TXT"],
#         set(["PDF", "TXT", "HTML"]),
#     ),
# ]

# submit_cases = run_cases + [
#     (["TXT"], ["TXT"], set(["TXT"])),
#     (["PDF", "DOCX", "TXT"], ["JPEG", "GIF", "PNG"], set()),
#     (["PDF", "DOCX"], ["DOCX", "PDF", "TXT"], set(["PDF", "DOCX"])),
# ]


# def test(formats1, formats2, expected_output):
#     print("---------------------------------")
#     print(f"Formats for Software 1: {formats1}")
#     print(f"Formats for Software 2: {formats2}")
#     print(f"Expecting: {expected_output}")
#     result = get_common_formats(formats1, formats2)
#     print(f"Actual: {result}")
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


# from main import *

# run_cases = [
#     (
#         (["Proposal", "Invoice", "Contract"], ["docx", "pdoof", "txt"]),
#         [("Proposal", "docx"), ("Contract", "txt")],
#     ),
#     (
#         (["Presentation", "Summary"], ["pptx", "docx"]),
#         [("Presentation", "pptx"), ("Summary", "docx")],
#     ),
# ]

# submit_cases = run_cases + [
#     (([], []), []),
#     ((["Test", "Example"], ["ppt", "docx"]), [("Test", "ppt"), ("Example", "docx")]),
#     (
#         (
#             ["Python Cheatsheet", "Java Cheatsheet", "Malware", "Golang Cheatsheet"],
#             ["pdf", "docx", "trash", "docx"],
#         ),
#         [
#             ("Python Cheatsheet", "pdf"),
#             ("Java Cheatsheet", "docx"),
#             ("Golang Cheatsheet", "docx"),
#         ],
#     ),
# ]


# def test(input1, expected_output):
#     print("---------------------------------")
#     print(f"Inputs:")
#     print(f" * doc_names: {input1[0]}")
#     print(f" * doc_formats: {input1[1]}")
#     print(f"Expecting: {expected_output}")
#     try:
#         result = list(pair_document_with_format(*input1))
#     except Exception as e:
#         result = f"Error: {e}"
#     print(f"Actual: {result}")
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

#ch3 

# import main as main_

# run_cases = [
#     ("Proposal.docx", "pdf", "Proposal.pdf"),
#     ("Invoice.txt", "md", "Invoice.md"),
# ]

# submit_cases = run_cases + [
#     ("Presentation.ppt", "pptx", "Presentation.pptx"),
#     ("Intro.pptx", "jpeg", None),
#     ("Summary.md", "txt", "Summary.txt"),
#     ("Contract.pdf", "pdoof", None),
# ]


# def mutate_globals():
#     main_.valid_extensions = ["docx", "txt", "pptx", "ppt", "md"]
#     main_.valid_conversions = {
#         "docx": ["jpeg"],
#         "pdf": ["docx", "txt", "md"],
#         "txt": ["docx"],
#         "ppt": ["pptx", "jpeg"],
#         "md": ["png"],
#         "jpeg": ["png"],
#     }


# def test(input1, input2, expected_output):
#     print("---------------------------------")
#     print(f"Inputs:")
#     print(f" * filename: {input1}")
#     print(f" * target_format: {input2}")
#     print(f"Expecting: {expected_output}")
#     result = main_.convert_file_format(input1, input2)
#     print(f"Actual: {result}")
#     if result == expected_output:
#         print("Pass")
#         return True
#     print("Fail")
#     return False


# def main():
#     passed = 0
#     failed = 0
#     mutate_globals()
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
#     (12, "txt", 12),
#     (16, "md", 32),
# ]

# submit_cases = run_cases + [
#     (14, "html", "Invalid doc type"),
#     (0, "txt", 0),
#     (50, "md", 100),
# ]


# def test(input1, input2, expected_output):
#     print("---------------------------------")
#     print(f"Inputs:")
#     print(f" * font_size: {input1}")
#     print(f" * doc_type: {input2}")
#     print(f"Expecting: {expected_output}")
#     try:
#         result = converted_font_size(input1)(input2)
#     except Exception as error:
#         result = str(error)
#     print(f"Actual: {result}")
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
