# Given sets of actors and actresses in the movie from Marvel 3
avengers2012 = {"Robert Downey Jr.", "Chris Evans", "Scarlett Johansson",
                "Jeremy Renner", "Samuel L. Jackson",
                "Mark Ruffalo","Tom Hiddleston","Gwyneth Paltrow",
                "Paul Bettany","Clark Gregg","Cobie Smulders","Stellan Skarsgård"}
wintersoldier = {"Chris Evans", "Scarlett Johansson", "Samuel L. Jackson",
                 "Sebastian Stan","Robert Redford",
                 "Anthony Mackie","Cobie Smulders","Frank Grillo","Maximiliano Hernández",
                 "Emily VanCamp","Hayley Atwell","Toby Jones","Stan Lee"}
thor2011 = {"Chris Hemsworth", "Natalie Portman", "Tom Hiddleston", "Anthony Hopkins",
            "Samuel L. Jackson","Stellan Skarsgård",
            "Kat Dennings","Clark Gregg","Colm Feore","Idris Elba","Ray Stevenson",
            "Tadanobu Asano","Josh Dallas","Maximiliano Hernández"}

# Who are actors from avenger 2012 and wintersoldier
print(avengers2012 & wintersoldier)

# Who are actors from all movies
print(avengers2012 & wintersoldier & thor2011)

# Given the actor name who perform at least 1 from 3
print(avengers2012 | wintersoldier | thor2011)

# How many actors
print(len(avengers2012 | wintersoldier | thor2011))

# Who perform in Avenger 2012 and not perform in Thor 2011
print(avengers2012 - thor2011)
print(len(avengers2012 - thor2011))

# Give the name and amount of actors who perform only 1 movie
print(avengers2012 ^ wintersoldier ^ thor2011)
print(len(avengers2012 ^ wintersoldier ^ thor2011))