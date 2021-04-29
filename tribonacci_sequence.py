def tribonacci(signature, n):
    # your code here
    i = 1
    signature_out = []
    if n < 4:
        while i in range(1, n + 1):
            signature_out.append(signature[i - 1])
            i += 1
        return signature_out
    while i < n - 2:
        signature.append(signature[i - 1] + signature[i] + signature[i + 1])
        i = i + 1
    return signature


a = tribonacci([1, 1, 1], 5)
print(a)
