# Set path
file = 'C:/Users/Bkcox/Documents/PycharmProjects/venv/Rosalind_data/rosalind_iprb.txt'
# Opens file and closes after execution
with open(file) as f:
    # Assign values in text files to the proper variables
    k, m, n = [int(x) for x in next(f).split()]
    total = k + m + n
    k_to_k = (k / total) * ((k - 1) / (total - 1))
    k_to_m = (k / total) * (m / (total - 1))
    k_to_n = (k / total) * (n / (total - 1))
    m_to_m = (m / total) * ((m - 1) / (total - 1))
    m_to_k = (m / total) * (k / (total - 1))
    m_to_n = (m / total) * (n / (total - 1))
    n_to_n = (n / total) * ((n - 1) / (total - 1))
    n_to_k = (n / total) * (k / (total - 1))
    n_to_m = (n / total) * (m / (total - 1))
    dominant_allele = 1*k_to_k + 1*k_to_m + 1*k_to_n + 0.75*m_to_m + 1*m_to_k + 0.5*m_to_n + 0*n_to_n + 1*n_to_k + 0.5*n_to_m
    print(dominant_allele)