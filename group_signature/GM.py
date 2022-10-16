import rsa
class GM :
    def __init__(self) :
        self.gen_RSA(1024)
        

    def gen_RSA(self, bits) :
        (pubkey, privkey) = rsa.newkeys(bits)
        print("privkey = ", privkey)
        print("pubkey = ", pubkey)

    def sign(self, m) :
        k = random.randint(1, self.q - 1)
        r = pow(self.g, k, self.p) % self.q
        s = (k - self.x * r) % self.q
        return (r, s)

    def verify(self, m, r, s) :
        if r < 1 or r > self.q - 1 or s < 1 or s > self.q - 1 :
            return False
        w = inverse(s, self.q)
        u1 = (m * w) % self.q
        u2 = (r * w) % self.q
        v = ((pow(self.g, u1, self.p) * pow(self.y, u2, self.p)) % self.p) % self.q
        return v == r

    def __str__(self) :
        return "GM(p = %d, q = %d, g = %d, h = %d, x = %d, y = %d)" % (self.p, self.q, self.g, self.h, self.x, self.y)


gm = GM(23, 11, 2, 7, 3, 4)