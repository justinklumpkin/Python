class Triangle():
    def __init__(s=[1,1,1],a=[60,60,60]):
        sides =s.sort()
        s1=s[0]
        s2=s[1]
        s3=s[2]
        
        angles =a.sort()
        a1=a[0]
        a2=a[1]
        a3=a[2]
    def sss(t):
        if self.sides[0]/t.sides[0]==self.sides[1]/t.sides[1] and self.sides[0]/t.sides[0]==self.sides[2]/t.sides[2]:
            return True
        return False
    def aaa(t):
        if self.angles[0]==t.angles[0] and self.angles[1] ==t.angles[1]:
            return True
        return False
    def sas(t):
        if self.s1/t.s1==self.s2/t.s2 and self.a3==t.a3:
            return True
        if self.s3/t.s3==self.s2/t.s2 and self.a1==t.a1:
            return True
        if self.s3/t.s3==self.s1/t.s1 and self.a2==t.a2:
            return True
        return False


t1 = Triangle()
t2 = Triangle([1,1,1],[None,None,None])
similar = False
if len(t1.sides)==3 and len(t2.sides)==3:
    if t1.sss(t2):
        print("t1 and t2 are similar by sss")
if len(t1.angles)>=2 and len(t2.angles)>=2:
    if t1.aa(t2):
        print("t1 and t2 are similar by aa")
if len(t1.angles)>=1 and len(t2.angles)>=1 and len(t1.sides>=2)and len(t2.sides>=2):
    if t1.sas(t2):
        print("t1 and t2 are similar by sas")
if not similar:
    print("The triangles are not similar")
