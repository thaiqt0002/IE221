n, m = map(int, input().split())
n_count = 10**int(len(str(n)))
m_count = int(len(str(m)))
count_diff = m//n_count
mn_diff = m%n_count - n
if (mn_diff >= 0): 
    count_diff+=1
print(count_diff)