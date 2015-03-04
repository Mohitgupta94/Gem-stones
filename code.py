import string
n=input()
i=0
li=range(n)
while(i<n):
    li[i]=raw_input()
    i=i+1
li2=list(string.ascii_lowercase)
j=0
total=0
while (j<26) :
    sum1=0
    i=0
    while (i<n):
        if (li2[j] in li[i]): 
            sum1=sum1+1;
        i=i+1
    if (sum1==n):
        total=total+1
    j=j+1
print total