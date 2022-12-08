# REDEMPTION!! Rank 493 on second one B)
# Part1: 00:08:55
# Part2: 00:16:42

def start(inp, lines):
    m = [list(f) for f in lines]
    sum = 0
    scenery = []
    for i in range(0, len(m)):
        for j in range(0, len(m[i])):
            if i == 0 or i == len(m):
                sum += 1
                continue
            if j == 0 or j == len(m[i]):
                sum += 1
                continue
            vis = 4
            d1 = 0
            for k in reversed(range(0, i)):
                d1 = i - k
                if m[k][j] >= m[i][j]:
                    vis -= 1
                    break
            d2 = 0
            for k in range(i+1, len(m)):
                d2 = k - i
                if m[k][j] >= m[i][j]:
                    vis -= 1
                    break
            d3 = 0
            for k in reversed(range(0, j)):
                d3 = j - k
                if m[i][k] >= m[i][j]:
                    vis -= 1
                    break
            d4 = 0
            for k in range(j+1, len(m[i])):
                d4 = k - j
                if m[i][k] >= m[i][j]:
                    vis -= 1
                    break
            if vis > 0:
                scenery.append(d1*d2*d3*d4)
                sum += 1
    print(max(scenery))
