## If the lyrics have to change the lyrics
lyrics = [1, 2, 3, 4, 5, 'I', 'Love', 'You']
song = lyrics
new_lyrics = lyrics.copy()
new_lyrics[6] = 'Like'
print(lyrics)
print(song)
print(new_lyrics)

## Using pop
print(new_lyrics.pop(-1))
print(new_lyrics)

## Using remove
new_lyrics.remove('Like')
print(new_lyrics)