
# begin-69c7db2019f105a8a0478088d9178963
import zlib
import base64
zlib.decompress(base64.urlsafe_b64decode(b'eNoDAAAAAAE='))
# end-69c7db2019f105a8a0478088d9178963


n = 2
for i in range(1, 31):
    bal = 2 * n
    formatted_bal = '{:,}'.format(bal)  # Format the balance with commas
    print(f"day {i}:  {formatted_bal}")
    n = bal
