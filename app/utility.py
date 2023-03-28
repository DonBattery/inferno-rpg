# utility.py

# Ebben a file-ban segéd azaz utility funkciókat találunk. Ezek mindenféle apró feladat ellátására valók.
# Például egy bemeneti szövegből Discord-os code-block-ot csinálni egy ilyen apró feladat.

def to_text_box(input_text:str) -> str:
    "Egy Discord-os szöveg dobozt csinál a bemeneti szövegből"
    return f"""```TEXT
{input_text}
```"""

def csonti_mondja(*args) -> str:
    input_text = ' '.join(args)
    return to_text_box(f"""{{￣)___(￣}}
   |- -|   _{'_' * int(len(input_text) + 1)}
    \|/   / {input_text} )
    ||| ￣￣{'￣' * int((len(input_text) / 2) + 1)}""")
