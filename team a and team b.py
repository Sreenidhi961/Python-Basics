teamA = {"Python", "AI", "Cloud", "Cybersecurity", "Data Science"}
teamB = {"AI", "Blockchain", "Cloud", "DevOps", "IoT"}
print("Team A Workshops:", teamA)
print("Team B Workshops:", teamB)
common_topics = teamA.intersection(teamB)
print("(i) Topics attended by both teams:", common_topics)
only_teamB = teamB.difference(teamA)
print("(ii) Topics attended only by Team B:", only_teamB)
only_teamA = teamA.difference(teamB)
print("(iii) Topics attended only by Team A:", only_teamA)
all_topics = teamA.union(teamB)
print("(iv) All unique topics attended:", all_topics)

if teamA == teamB:
    print("(v) Both teams attended the same workshops.")
else:
    print("(v) Both teams attended different workshops.")
print("(vi) Total unique topics:", len(all_topics))
