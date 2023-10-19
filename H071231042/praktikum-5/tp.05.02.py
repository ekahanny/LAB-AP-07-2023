kata = "muslih"
var = len(kata)
if var % 2 == 0:
    var = kata[0] + kata[var//2-1] + kata[var//2] + kata[-1]
    print(var)
else:
    kata = kata[0] + kata[var//2] + kata[-1]
    print(kata)
