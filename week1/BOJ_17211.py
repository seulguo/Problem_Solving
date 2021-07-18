'''
0 -> 0 확률 gg
0 -> 1 확률 gb
1 -> 0 확률 bg
1 -> 1 확률 bb

n일 뒤에 기분이 좋은 날일 확률/ 싫은 날일 확률 * 1000 첫째짜리에서 반올림
'''

n, today = map(int, input().split())
gg, gb, bg, bb = map(float, input().split())

good = list()
bad = list()

if today == 0:
    good.append(gg)
    bad.append(gb)
else:
    good.append(bg)
    bad.append(bb)

for i in range(1, n):
    good.append(good[i-1]*gg + bad[i-1]*bg)
    bad.append(good[i-1]*gb + bad[i-1]*bb)

print(round(good[n-1]*1000))
print(round(bad[n-1]*1000))

'''
3-5 좋은 날 싫은 날
https://www.acmicpc.net/problem/17211
'''
