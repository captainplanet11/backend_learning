def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read() 

    char_count = count_character(file_contents)
    for char,count in sorted(char_count.items(),key = lambda x: x[1]):
        print(f"The '{char}' character was found {count} times")
              
def count_character(text):
    text_lower = text.lower() 
    char_count = {} 
    #Iterate over each cahracter 
    for char in text_lower:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count 

main()
