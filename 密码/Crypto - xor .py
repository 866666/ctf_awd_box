from z3 import *

##求random，已知前5位是flag{
i = b"flag{"
so = Solver()
ans = [150, 194, 49, 195, 23, 79, 66]
flag5 = BitVec("flag5", 8)
pad = [BitVec(f"pad{i}", 8) for i in range(6)]
so.add(i[0] ^ i[1] ^ i[2] ^ pad[0] == ans[0])
so.add(i[3] ^ i[4] ^ pad[1] ^ pad[2] == ans[1])
so.add(pad[5] ^ flag5 ^ pad[1] ^ pad[3] == ans[2])
so.add(i[3] ^ pad[3] ^ pad[4] ^ pad[1] == ans[3])
so.add(flag5 ^ pad[0] ^ i[4] ^ pad[1] == ans[4])
so.add(i[2] ^ i[4] ^ pad[0] ^ pad[1] == ans[5])
so.add(i[2] ^ i[0] ^ i[4] ^ pad[4] == ans[6])
pad_ = []
if so.check() == sat:
    m = so.model()
    for k in range(6):
        # print(m.eval(pad[k]).as_long())
        pad_.append(m.eval(pad[k]).as_long())
# print(pad_)
# [253, 168, 118, 50, 62, 146]
ans = [
    [150, 194, 49, 195, 23, 79, 66],
    [194, 136, 63, 147, 3, 2, 81],
    [132, 221, 57, 144, 83, 83, 93],
    [208, 223, 37, 193, 28, 0, 70],
    [154, 203, 108, 156, 28, 78, 68],
    [159, 221, 62, 146, 86, 82, 88],
    [197, 141, 117, 192, 31, 90, 85],
]
flag_ = ""
pad = pad_
for i in ans:
    so = Solver()
    flag = [BitVec(f"flag{i}", 8) for i in range(6)]
    so.add(flag[0] ^ flag[1] ^ flag[2] ^ pad[0] == i[0])
    so.add(flag[3] ^ flag[4] ^ pad[1] ^ pad[2] == i[1])
    so.add(pad[5] ^ flag[5] ^ pad[1] ^ pad[3] == i[2])
    so.add(flag[3] ^ pad[3] ^ pad[4] ^ pad[1] == i[3])
    so.add(flag[5] ^ pad[0] ^ flag[4] ^ pad[1] == i[4])
    so.add(flag[2] ^ flag[4] ^ pad[0] ^ pad[1] == i[5])
    so.add(flag[2] ^ flag[0] ^ flag[4] ^ pad[4] == i[6])
    if so.check() == sat:
        m = so.model()
        # print(''.join(chr(m[i].as_long()) for i in flag))
        flag_ += "".join(chr(m[i].as_long()) for i in flag)
    else:
        print("Error")
print(flag_)
