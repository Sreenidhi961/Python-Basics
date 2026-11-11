teamA={"Python","AI","Cloud","Cybersecurity","Data Science"}
teamB={"AI","Blockchain","Cloud","DevOps","IoT"}
print("Team A Workshops:",teamA)
print("Team B Workshops:",teamB)
common_topics=teaA.intersection(teamB)
print("(ii) Topics attended by both teams:",common_topics)
only_teamB=teamB.difference(teamA)
print("ii(Topics attended by only Team B:",only_teamB)
only_teamA=teamA.difference(teamB)
print("ii(Topics attended by only Team A:",only_teamA)
all_topics=teamA.union(teamB)
print("iv(All unique topics attended:",all_topics)
