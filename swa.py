# WAP to know if its a good idea to swap P into Q.
#
#   Find inter-worth of P & Q from gecko.
#   Find inter-worth of P & Q from pool size.
#   Check if iw(p,q) > cw(p,q)
#
## In:
##  Enter P
##  Enter Q
##  Enter P-pool-size
##  Enter Q-pool-size
gp = float(input("G price P   "))
gq = float(input("G price Q   "))
bp = float(input("P in pool   "))
bq = float(input("Q in pool   "))
gr = gp/gq
br = bq/bp
print("\nCGecko R: {:.8f} Q = 1 P.\nPooled R: {:.8f} Q = 1 P.\n".format(gr,br))
def s(p,q,n):
    k=p*q
    return(q-(k/(p+n)))
if(gr>br):
    print("P is undervalued in Pool. BUY!")
    nq=float(input("Amount of Q to swap:  "))
    print("\n{:.8f} Q will get {:.8f} P.\n".format(nq,s(bq,bp,nq)))
    if((nq/s(bq,bp,nq))>gr):
        print("ABORT: {:.8f} Q=1P! Unfeasible!".format(nq/s(bq,bp,nq)))
    else:
        print("GG: Go ahead!")
else:
    print("P is overvalued in Pool. SELL!")
    np=float(input("Amount of P to swap:  "))
    print("\m{:.8f} P will get {:.8f} Q.\n".format(np,s(bp,bq,np)))
    if((s(bp,bq,np)/np)<gr):
        print("ABORT: {:.8f} Q=1P! Unfeasible!".format(s(bp,bq,np)/np))
    else:
        print("GG: Go ahead!")
