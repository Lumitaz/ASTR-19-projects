#main
def introduce():
    name = "Emory Honeycutt"
    pronouns = "They/Them"
    favorite_movie = (
        "My favorite movie is The Lord of the Rings: The Return of the King, I love all bits of the movie but 100% the music has to be my favprote part.  The score of any movie is what really sets it apart for me"
    )
    favorite_food = (
        "My favorite food definitely has to be pizza, I love the variety of toppings and like the ease of access. Plus a great pizza can beat any other food no questions asked."
    )

    
    #print the introduction
    print(f"Name: {name}")
    print(f"Pronouns: {pronouns}")
    print()
    print(favorite_movie)
    print(favorite_food)

#run cmd
if __name__ == "__main__":
    introduce()