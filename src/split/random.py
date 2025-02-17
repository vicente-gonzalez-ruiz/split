def random_split(signal):
    """
    Split the signal into two independent half-signals by dividing the data randomly.
    """
    mask = np.random.randint(0, 2, signal.shape, dtype=bool)
    s1 = np.where(mask, signal, 0)
    s2 = np.where(~mask, signal, 0)
    return s1, s2
