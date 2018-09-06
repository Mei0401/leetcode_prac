def lcm(x, y):
        if x > y:
            z = x
        else:
            z = y
        while(True):
           if((z % x == 0) and (z % y == 0)):
               lcm = z
               break
           z += 1
        return lcm

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

class Solution:

    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        symbol = []
        num = []
        denum = []
        for i in range(len(expression)):
            if expression[i] == '/':
                if i < (len(expression) - 2):
                    if expression[i+1] == '1' and expression[i+2] == '0':
                        denum.append(10)
                if i > 1:
                    if expression[i-2] == '1' and expression[i-1] == '0':
                        num.append(10)
                num.append(int(expression[i-1]))
                denum.append(int(expression[i+1]))
            if expression[i] == '+' or expression[i] == '-':
                symbol.append(expression[i])
        
        temp = []
        for i in range(len(num)):
            if num[i] == 10:
                temp.append(i)
        for i in range(len(temp)):
            num.pop(temp[i]+1)
            for j in range(len(temp)):
                temp[j] = temp[j]-1
            if len(num) == i+1:
                    break
        
        temp = []
        for i in range(len(denum)):
            if denum[i] == 10:
                temp.append(i)
        for i in range(len(temp)):
            denum.pop(temp[i]+1)
            for j in range(len(temp)):
                temp[j] = temp[j]-1
            if len(denum) == i+1:
                    break

        
        divisor = denum[0]
        for i in range(1,len(denum)):
            divisor = lcm(denum[i], divisor)
        
        for i in range(len(num)):
            num[i] = num[i]*divisor//denum[i]
        
        if expression[0] == '-':
            num[0] = -1*num[0]
            symbol = symbol[1:]
        
        final_num = num[0]
        
        for i in range(len(symbol)):
            if symbol[i] == '+':
                final_num = final_num + num[i+1]
            if symbol[i] == '-':
                final_num = final_num - num[i+1]
        
        temp = gcd(final_num, divisor)
        final_num = final_num // temp
        divisor = divisor // temp
        
        return str(str(final_num)+'/'+str(divisor))

        
        

if __name__ == "__main__":
    a = Solution()
    b = a.fractionAddition("10/9-4/1+10/9-9/10+4/3")
    print(b)
