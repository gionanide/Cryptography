
def prime_factors(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)  # supposing you want multiple factors repeated
            n //= d
        d += 2
    if n > 1:
       primfac.append(n)
    return primfac

def compute_generators(gen,prime,q):
    computed=[]
    for i in q:
        computed.append(gen**((prime-1)/i)%prime)
    return computed



def compute_prime_factors_q(prime):
    p_factors=prime_factors(prime-1)
    #print "p_factors of prime-1", p_factors
    computed=[]
    res=[]
    for g in range(2,prime):
        computed=compute_generators(g,prime,p_factors)
        #print "G=",g,"computed",computed
        if 1 not in computed:
            res.append(g)
    return res


print compute_prime_factors_q(23)
