# minimal chess engine for make.fun tiny-chess-01 (under 4KB)
PIECES='pnbrqkPNBRQK';N=8
b=[['r','n','b','q','k','b','n','r'],['p','p','p','p','p','p','p','p'],['.','.','.','.','.','.','.','.'],['.','.','.','.','.','.','.','.'],['.','.','.','.','.','.','.','.'],['.','.','.','.','.','.','.','.'],['P','P','P','P','P','P','P','P'],['R','N','B','Q','K','B','N','R']]
c='w';t=0
while t<30:
    print('Turn',t,c)
    for r in range(8): print('|'.join(b[r]))
    moved=False
    if c=='w':
        for r in range(7,-1,-1):
            for c2 in range(8):
                if b[r][c2]=='P'and r>0and b[r-1][c2]=='.':
                    b[r-1][c2]=b[r][c2];b[r][c2]='.';moved=True;break
            if moved:break
    else:
        for r in range(8):
            for c2 in range(8):
                if b[r][c2]=='P'and r<7and b[r+1][c2]=='.':
                    b[r+1][c2]=b[r][c2];b[r][c2]='.';moved=True;break
            if moved:break
    if not moved:break
    c='b'if c=='w'else'w';t+=1
vs={'p':1,'n':3,'b':3,'r':5,'q':9,'k':0}
vs_b={k:-v for k,v in vs.items()}
eval_score=0
for r in range(8):
    for c in range(8):
        p=b[r][c]
        if p!='.':
            if p.isupper():
                eval_score+=vs[p.lower()]
            else:
                eval_score+=vs_b[p.lower()]
print('Eval',eval_score)