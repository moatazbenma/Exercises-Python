import operator

# Sample movie database
movies = [
    {"title": "Inception", "genres": ["sci-fi", "action"], "actors": ["Leonardo DiCaprio"]},
    {"title": "Titanic", "genres": ["romance", "drama"], "actors": ["Leonardo DiCaprio", "Kate Winslet"]},
    {"title": "The Matrix", "genres": ["sci-fi", "action"], "actors": ["Keanu Reeves"]},
    {"title": "The Notebook", "genres": ["romance", "drama"], "actors": ["Ryan Gosling", "Rachel McAdams"]},
    {"title": "John Wick", "genres": ["action", "thriller"], "actors": ["Keanu Reeves"]},
    {"title": "Interstellar", "genres": ["sci-fi", "drama"], "actors": ["Matthew McConaughey"]},
    {"title": "La La Land", "genres": ["romance", "musical"], "actors": ["Emma Stone", "Ryan Gosling"]},
]

# Ask user for preferences
genre_input = input("What genres do you like? (comma-separated): ").lower().split(',')
actor_input = input("Who are your favorite actors? (comma-separated): ").lower().split(',')

# Clean up whitespace
preferred_genres = [g.strip() for g in genre_input]
preferred_actors = [a.strip() for a in actor_input]

# Scoring movies
scores = {}

for movie in movies:
    score = 0
    for genre in movie["genres"]:
        if genre.lower() in preferred_genres:
            score += 1
    for actor in movie["actors"]:
        if actor.lower() in preferred_actors:
            score += 1
    scores[movie["title"]] = score

# Sort movies by score
sorted_scores = sorted(scores.items(), key=operator.itemgetter(1), reverse=True)

# Show top recommendations
print("\n🎬 Recommended for you:")
for title, score in sorted_scores:
    if score > 0:
        print(f"- {title} (Score: {score})")
