#Given List of Male Actor
actors = ["Cillian Murphy", "Matt Damon", "Robert Downey Jr.", "Josh Harnett"]

#Previous Way
# actor_mr = []
# for name in actors:
#     name_mr = "Mr. " + name
#     actor_mr.append(name_mr)

#Create New List
actor_mr = ["Mr. " + name for name in actors]
print(actor_mr)