    ⚖️ 💀 🤝 ✌️ 📂 ?? invalid syntax

вот тебе код компилятора
import sys
import re
import os

G_KEYWORDS = {
    '🕳️ 👑 📂': 'def main():',
    '📂': '{', '📁': '}', '💧': '', 
    '🤝': '=', 
    '👀': '==',   
    '➕': '+', '➖': '-', '☠️': '*', '🔪': '/',
    
    '🤏': '<',    
    '🤘': '>',    
    '🍕': '%',    
    
    '⚖️': 'if', '🤷‍♂️': 'else:', '🔁': 'while', '🚶‍♂️': 'return',
    
    '✊': '0', '☝️': '1', '✌️': '2', '🤟': '3', '🖖': '4', '🖐️': '5', '👐': '10',
    '✅': 'True', '❌': 'False'
}

def emoji_to_var(match):
    text = match.group(0)
    hex_name = text.encode('utf-8').hex()
    return f"v_{hex_name}"

def compile_and_run(filename):
    if not os.path.exists(filename):
        print(f"⚠️ file {filename} not found.")
        return

    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    print(f"🛠️ [GasterGCC v6.0] compiling {filename}...")

    py_code = "import sys\n\n"
    indent_level = 0

    for line in lines:
        line = line.strip()
        if not line: continue
        
        if line.startswith('🤫'):
            continue

        if any(x in line for x in ['🔢', '🔤']) and '🤝' not in line:
            continue
        line = line.replace('🔢', '').replace('🔤', '')

        if '📁' in line: 
            indent_level = max(0, indent_level - 1)

        if '👁️🗣️' in line:
            line = re.sub(r'👁️🗣️\s*(.*?)\s*💧', r'print(\1)', line)

        if '👂📥' in line:
            line = re.sub(r'👂📥\s*(.*?)\s*💧', r'\1 = int(input("📥 > "))', line)

        for gaster, py_sym in G_KEYWORDS.items():
            line = line.replace(gaster, py_sym)

        line = re.sub(r'[^\x00-\x7F\s\+\-\*\/\(\)\=\.\,\:\<\>\%\'\"_]+', emoji_to_var, line)

        line = line.replace('{', '').replace('}', '').replace('💧', '').strip()
        if not line: continue

        if line.startswith(('def ', 'if ', 'else', 'while ')) and not line.endswith(':'):
            line += ":"

        py_code += ("    " * indent_level) + line + "\n"

        if line.endswith(':'):
            indent_level += 1

    py_code += "\ntry:\n    main()\nexcept Exception as e:\n    print(f'💀 cant run: {e}')\n"
    
    print("✅running: \n")
    print("-" * 30)
    
    try:
        exec(py_code, globals())
    except Exception as e:
        print(f"\n💀 CRASH: {e}")
    print("-" * 30)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("run: py compilator.py main.c")
    else:
        compile_and_run(sys.argv[1])
