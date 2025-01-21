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


def deduplicate_lists(lst1, lst2, reverse=False):
    combined = set(lst1 + lst2)
    return sorted(combined,reverse=reverse)
