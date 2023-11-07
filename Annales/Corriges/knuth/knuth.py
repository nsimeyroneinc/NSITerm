def knuth(f):
    p=[]
    N=len(f)
    for i in range(N):
        if p==[]:
            p.append(f.pop())
            print(f"f : {f}, p : {p}")
        else:
            e = f.pop()
            print(f"f : {f}, p : {p}")
            if e >= p[-1]:
                p.append(e)
                print(f"f : {f}, p : {p}")
            else:
                while not p==[] and e < p[-1]:
                    f.insert(0,p.pop())
                    print(f"f : {f}, p : {p}")
                p.append(e)
                print(f"f : {f}, p : {p}")
    print(f"f : {f}, p : {p}")
    while not p==[]:
        f.append(p.pop())
        print(f"f : {f}, p : {p}")

knuth([2,1,3])