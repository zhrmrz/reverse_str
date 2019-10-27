class Sol:
    def reverse_str(self,s,k):
        l=[]
        for i in range((len(s)//k)):
            l.append(s[i*k:i*k+k])
        if len(s)%k!=0:
            l.append(s[(len(s)//k)*k:])

        for i,x in enumerate(l):
            if i%2==0:
                l[i]=l[i][::-1]
        return ''.join(l)
