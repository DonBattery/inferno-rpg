# text_utility.py

# Ebben a file-ban segéd azaz utility funkciókat találunk, szövegek előállításához.
# Például egy bemeneti szövegből Discord-os code-block-ot csinálunk, help szöveget generálunk,
# vagy kimnodatunk Csontival egy mondatot.

def to_text_box(input_text:str) -> str:
    "Egy Discord-os szöveg dobozt csinál a bemeneti szövegből"
    return f"""```TEXT
{input_text}
```"""

def csonti_mondja(*args) -> str:
    input_text = ' '.join(args)
    return to_text_box(f"""{{￣)___(￣}}
   |- -| _{'_' * int(len(input_text) + 1)}
    \|/_/ {input_text} \\
    ||| \{'_' * int(len(input_text) + 2)}/""")

def justify_line(line:list, width: int) -> list:
    remaining_space = width - len(''.join(line))
    number_of_words = len(line)
    out_line = line[:]
    while remaining_space:
        word_index = 0
        for word in line:
            word_index += 1
            if remaining_space > 0 and word_index < number_of_words:
                out_line[word_index - 1] += ' '
                remaining_space -= 1
            else:
                continue
    return out_line

def justify_box(input_lines:list, box_width:int) -> list:
    output_lines = []
    line_index = 0
    for line in input_lines:
        line_index += 1
        if line_index < len(input_lines):
            output_lines.append(justify_line(line, box_width))
        else:
            output_lines.append(line)
    return output_lines

# Ez az algoritmus lebont egy szavakból álló listát, egy táblázattá (listák listája)
# minden sorban a szavak hosszának összege plusz a hozzájuk adott szóközök, nem lehetnek nagyobbak,
# mint a bemeneti box_width, az az doboz szélesség. A túl hosszú szavakat eltördeli.
def warp_words_to_box(words:list, box_width:int) -> list:
    if box_width <= 0:
        raise ValueError("shit")

    spaced_list = []
    word_counter = 0
    for word in words:
        word_counter += 1
        if len(word) % box_width and word_counter < len(words):
            spaced_list.append((word + " "))
        else:
            spaced_list.append(word)

    result = []
    subline = []
    subline_counter = 0
    while spaced_list:
        word = spaced_list.pop(0)
        if len(word) > box_width:
            w1 = word[0:box_width]
            w2 = word[box_width:len(word)]
            spaced_list.insert(0, w2)
            word = w1

        if (subline_counter + len(word)) <= box_width:
            subline.append(word)
            subline_counter += len(word)
        else:
            result.append(subline)
            subline = []
            subline.append(word)
            subline_counter = len(word)

    if len(subline):
        result.append(subline)

    return justify_box(result, box_width)

def csonti_mondja2(*args, max_width:int) -> str:
    res = warp_words_to_box(args, max_width - 12)
    width = 0
    for line in res:
        print("Line to join", line)
        line_width = len(''.join(line))
        if line_width > width:
            width = line_width
    first_line = ''.join(res[0])
    out = f"""{{￣)___(￣}}
   |- -| {'_' * int(width + 2)}
    \|/_/ { first_line + ' ' * int(width - len(first_line)) } \\
    ||| """
    remaining = len(res) - 1
    first_plus_line = True
    plus_line = 1
    while remaining > 0:
        new_line = ''.join(res[plus_line])
        out += f"{ '' if first_plus_line else '        ' }| { new_line + ' ' * int(width - len(new_line)) } |\n"
        first_plus_line = False
        remaining -= 1
        plus_line += 1
    out += f"{ '' if first_plus_line else '        ' }\{ '_'  * int(width + 2) }/"
    return to_text_box(out)
