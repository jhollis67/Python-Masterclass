# Tuples: ordered list that cannot be immutable

# welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
# bad = "Bad Company", "Bad Company", 1974
# budgie = "Nightflight", "Budgie", 1981
# imelda = "More Mayhem", "Emilda May", 2011, (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz")
#
# print(imelda)
#
# title, artist, year, track1, track2, track3, track4 = imelda
# print(title)
# print(artist)
# print(year)
# print(track1)
# print(track2)
# print(track3)
# print(track4)

# Challenge: Given the tuple below that represents the Imelda May album "More Mayhem", write
# code to print the album details, followed by a listing of all the tracks in the album
#
# Indent the tracks by a single tab stop when printing them (remember that you can pass
# more than one item to the print function, separating them with a comma

# imelda = "More Mayhem", "Imelda May", 2011, (
#     (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz")
# )
#
#
# title, artist, year, tracks = imelda
# print(title)
# print(artist)
# print(year)
# for song in tracks:
#     track, title = song
#     print("\tTrack number {}, Title: {}".format(track, title))
