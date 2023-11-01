import argparse 

def local_value_numbering(f):
    f = open(f)
    s = f.read()
    f.close()

    pre = s.split("// Start optimization range")[0]
    post = s.split("// Start optimization range")[1].split("// End optimization range")[1]
    to_optimize = s.split("// Start optimization range")[1].split("// End optimization range")[0]
    
    lines = to_optimize.strip().split("\n")

    value_numbering = {}
    value_to_expr = {}
    new_lines = []
    replaced = 0

    for line in lines:
        var, expr = line.split(" = ")
        # normalize expressions (e.g., "g + k" should be the same as "k + g" since addition is commutative)
        if '+' in expr or '-' in expr:
            operands = sorted(expr.split(" + ")) if '+' in expr else expr.split(" - ")
            normalized_expr = " + ".join(operands) if '+' in expr else " - ".join(operands)
        else:
            normalized_expr = expr
            
        if normalized_expr in value_numbering:
            new_lines.append(f"{var} = {value_to_expr[value_numbering[normalized_expr]]}; // optimized")
            replaced += 1
        else:
            new_val_num = len(value_numbering) + 1
            value_numbering[normalized_expr] = new_val_num
            value_to_expr[new_val_num] = var
            new_lines.append(line)

    optimized_block = "\n".join(new_lines)

    # hint: perform the local value numbering optimization here on to_optimize
    
    print(pre)

    # hint: print out any new variable declarations you need here

    # hint: print out the optimized local block here

    # hint: store any new numbered variables back to their unumbered counterparts here
    print(optimized_block)
    
    print(post)

    # You should keep track of how many instructions you replaced
    #print("// replaced: " + str(replaced))   
    print(f"// replaced: {replaced}")    
     
    

# if you run this file, you can give it one of the python test cases
# in the test_cases/ directory.
# see solutions.py for what to expect for each test case.
if __name__ == '__main__': 
    parser = argparse.ArgumentParser()   
    parser.add_argument('cppfile', help ='The cpp file to be analyzed') 
    args = parser.parse_args()
    local_value_numbering(args.cppfile)
