# With numpy (no valid solution)
def canPair(self, nuns, k):
		if len(nuns)%2 == 1:
		    return False
        nuns_div = np.array([nun%k for nun in nuns])
        if (nuns_div == 0).sum() %2 == 1:
            return False
        for j in range(1, k//2 + 1):
            if (nuns_div == j).sum() != (nuns_div == k-j).sum()
                return False
        return True
