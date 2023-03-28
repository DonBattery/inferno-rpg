# utility.py

# Ebben a file-ban segéd azaz utility funkciókat találunk. Ezek mindenféle apró feladat ellátására valók.
# Például egy bemeneti szövegből Discord-os code-block-ot csinálni egy ilyen apró feladat.

def to_text_box(input_text:str) ->str:
    "Egy Discord-os szöveg dobozt csinál a bemeneti szövegből"
    return f"""```TEXT
{input_text}
```"""
