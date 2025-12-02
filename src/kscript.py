import sys
import re


# --- 1. MEMORY (Symbol Table) ---
memory = {} 
functions = {}

# --- 2. EVALUATOR (Math & Logic) ---
def evaluate(expr):
    try:
        # Replace variable names with their values
        for var, val in memory.items():
            expr = re.sub(r'\b' + var + r'\b', str(val), expr)
        
        # Auto-convert '=' to '==' for logic checks (Syntactic Sugar)
        if "=" in expr and "==" not in expr and "<=" not in expr and ">=" not in expr:
            expr = expr.replace("=", "==")
            
        return eval(expr) 
    except:
        return 0

# --- 3. CORE INTERPRETER ---
def execute(code):
    lines = code.split('\n')
    i = 0
    
    while i < len(lines):
        # STRIP COMMENTS: Remove anything after '#'
        line = lines[i].split('#', 1)[0].strip()
        
        if not line: 
            i += 1
            continue
            
        # FEATURE: FUNCTION DEFINITION (def: name do:)
        if line.startswith("def:"):
            func_name = line.replace("def:", "").replace("do:", "").strip()
            
            # Capture the block logic
            block_start = i + 1
            block_lines = []
            while block_start < len(lines):
                raw_next = lines[block_start].split('#', 1)[0]
                if not raw_next.strip():
                    block_start += 1
                    continue
                if not raw_next.startswith("    "): # Check for 4-space indent
                    break
                block_lines.append(raw_next[4:])
                block_start += 1
            
            # Save function to memory
            functions[func_name] = "\n".join(block_lines)
            i = block_start - 1

        # FEATURE: FUNCTION CALL (run: name)
        elif line.startswith("run:"):
            func_name = line.replace("run:", "").strip()
            if func_name in functions:
                execute(functions[func_name]) # Recursively execute
            else:
                print(f"Error: Function '{func_name}' not defined.")

        # FEATURE: ASSIGNMENT & INPUT (x = 10 OR x = input:'Prompt')
        elif "=" in line and "if:" not in line and "loop:" not in line:
            var, val = line.split("=", 1)
            var = var.strip()
            val = val.strip()
            
            if val.startswith("input:"):
                prompt = val.split(":", 1)[1].strip()
                if prompt.startswith("'"): prompt = prompt[1:-1]
                user_in = input(prompt + " ")
                # Auto-detect number vs string
                if user_in.isdigit(): memory[var] = int(user_in)
                else: memory[var] = user_in
            else:
                memory[var] = evaluate(val)
            
        # FEATURE: PRINTING (print:'Text' OR print:var)
        elif line.startswith("print:"):
            _, content = line.split(":", 1)
            content = content.strip()
            if content.startswith("'"): print(content[1:-1])
            else: print(memory.get(content, "Undefined"))

        # FEATURE: CONDITIONAL LOGIC (if: condition do:)
        elif line.startswith("if:"):
            condition = line.replace("if:", "").replace("do:", "").strip()
            block_start = i + 1
            block_lines = []
            while block_start < len(lines):
                raw_next = lines[block_start].split('#', 1)[0]
                if not raw_next.strip():
                    block_start += 1
                    continue
                if not raw_next.startswith("    "):
                    break
                block_lines.append(raw_next[4:])
                block_start += 1
            
            if evaluate(condition):
                execute("\n".join(block_lines))
            i = block_start - 1 

        # FEATURE: LOOPS (loop: condition do:)
        elif line.startswith("loop:"):
            condition = line.replace("loop:", "").replace("do:", "").strip()
            block_start = i + 1
            block_lines = []
            while block_start < len(lines):
                raw_next = lines[block_start].split('#', 1)[0]
                if not raw_next.strip():
                    block_start += 1
                    continue
                if not raw_next.startswith("    "):
                    break
                block_lines.append(raw_next[4:])
                block_start += 1
            
            while evaluate(condition):
                execute("\n".join(block_lines))
            i = block_start - 1 

        i += 1

# --- 4. FILE LOADER ---
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("K-Script Interpreter v1.0")
        print("Usage: python kscript.py <filename.ks>")
    else:
        try:
            with open(sys.argv[1], 'r') as f:
                execute(f.read())
        except FileNotFoundError:
            print(f"Error: File '{sys.argv[1]}' not found.")