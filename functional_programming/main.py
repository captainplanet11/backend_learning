# #ch1 #l1
# def stylize_title(document):
#     return add_border(center_title(document))


# # Don't touch below this line


# def center_title(document):
#     width = 40
#     title = document.split("\n")[0]
#     centered_title = title.center(width)
#     return document.replace(title, centered_title)


# def add_border(document):
#     title = document.split("\n")[0]
#     border = "*" * len(title)
#     return document.replace(title, title + "\n" + border)
#----------------------------------------------------------------------
#ch1 #L3


# def add_prefix(document, documents):
#     prefix = f"{len(documents)}. "
#     new_doc = prefix + document
#     updated_document = documents + (new_doc,)
#     return updated_document



#ch1 l6

# def get_median_font_size(font_sizes):
#     if len(font_sizes) == 0:
#         return None
#     if len(font_sizes) % 2 == 0:
#         return sorted(font_sizes)[len(font_sizes)// 2 - 1]
#     else:
#         return sorted(font_sizes)[len(font_sizes)// 2]
   

#ch1 L9 

# def format_line(line):
#     formatted = line.strip().upper()
#     if not formatted.endswith("..."):
#         formatted = formatted.rstrip('.') + "..."
#     return formatted

#ch1 C1

# def toggle_case(line):
#     if line.istitle():
#         line = line.upper() + "!!!"
#     elif line.isupper():
#         line = line.lower().capitalize().replace("!","")
        
#     elif len(line) > 0 and line[1:].islower():
#         line = line.title()
#     return line

# line = "BEAM ME UP, BOOTS!"

# print(toggle_case(line))


#c1 c2 

# def hex_to_rgb(hex_color):
#     if hex_color.startswith("#"):
#         hex_color = hex_color[1:]  
    
#     if len(hex_color) != 6 or not is_hexadecimal(hex_color):
#         raise ValueError("not a hex color string")
    
#     r = int(hex_color[:2], 16)
#     g = int(hex_color[2:4], 16)
#     b = int(hex_color[4:], 16)
    
#     return r, g, b



# def is_hexadecimal(hex_string):
#     try:
#         int(hex_string, 16)
#         return True
#     except Exception:
#         return False
    

#ch1 c3


# def deduplicate_lists(lst1, lst2, reverse=False):
#     combined = set(lst1 + lst2)
#     return sorted(combined,reverse=reverse)


# def file_to_prompt(file, to_string):

#     return "```\n" + to_string(file) + "\n" + "```"

#ch2 L2

# def file_type_getter(file_types):
#     extension_to_type = {}
#     for file_type, extensions in file_types:
#         for ext in extensions:
#             extension_to_type[ext] = file_type
#     return lambda ext: extension_to_type.get(ext, "Unknown")


#ch2  L5

# def change_bullet_style(document):
#     lines = document.split("\n")
#     convert_lines = map(convert_line, lines) # convert eacch lines
#     return "\n".join(convert_lines) # join the lines

# def convert_line(line):
#     old_bullet = "-"
#     new_bullet = "*"
#     if len(line) > 0 and line[0] == old_bullet:
#         return new_bullet + line[1:]
#     return line

# ch 2 L 6

# def is_even(x):
#     return x % 2 == 0

# numbers = [1, 2, 3, 4, 5, 6]
# evens = list(filter(is_even, numbers))
# print(evens)


# def remove_invalid_lines(document):
#     lines = document.split("\n")
#     valid_lines = filter(is_valid_line,lines)
#     return  "\n"+"\n".join(valid_lines) + "\n"

# def is_valid_line(line):
#     return len(line) > 0 and line[0] == "*"


# ch 2 L7 

# import functools


# def join(doc_so_far, sentence):
#     return f"{doc_so_far}. {sentence}"


# def join_first_sentences(sentences, n):
#     if n == 0:
#         return ""
#     selected = sentences[:n]
#     if not selected:
#         return ""
#     combined = functools.reduce(join, selected)
#     return combined + "."


# ch2 c1


# def get_common_formats(formats1, formats2):
#     return set(formats1).intersection(formats2)

#c2

# valid_formats = [
#     "docx",
#     "pdf",
#     "txt",
#     "pptx",
#     "ppt",
#     "md",
# ]



# def pair_document_with_format(doc_names, doc_formats):
#     a =  list(zip(doc_names, doc_formats))
#     filtered = filter(lambda x: x[1] in valid_formats, a)
#     return list(filtered)

#ch3 