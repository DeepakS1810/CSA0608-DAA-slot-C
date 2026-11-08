def find_paths(m, n, N, i, j):
    dp = [[0] * n for _ in range(m)]
    dp[i][j] = 1
    paths_out = 0

    for _ in range(N):
        next_dp = [[0] * n for _ in range(m)]

        for row in range(m):
            for col in range(n):
                paths = dp[row][col]
                if paths == 0:
                    continue

                for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    new_row = row + dr
                    new_col = col + dc

                    if 0 <= new_row < m and 0 <= new_col < n:
                        next_dp[new_row][new_col] += paths
                    else:
                        paths_out += paths

        dp = next_dp

    return paths_out


print(find_paths(2, 2, 2, 0, 0))
print(find_paths(1, 3, 3, 0, 1))
