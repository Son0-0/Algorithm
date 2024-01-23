def simplifyPath(path: str) -> str:
    stack = []
    
    for dir in list(path.split("/")):
        if dir == "":
            continue
        elif dir == ".":
            continue
        elif dir == "..":
            if stack:
                stack.pop()
        else:
            stack.append(dir)
            
    
    return "/" + "/".join(stack)
    
    
    
print(simplifyPath("/home/"))
print(simplifyPath("/../"))
print(simplifyPath("/home//foo/"))