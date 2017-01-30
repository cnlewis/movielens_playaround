data = pd.merge(pd.merge(ratings, users), movies)
print data[:100]
