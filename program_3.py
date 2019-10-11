def amt_per_genre(file_name): #function to count amount of games per genre
    file = open(file_name,'r') #opens .csv file
    file.readline()
    genre_list = []
    for line in file:
        line = line.split('')
        #splits the file based on commas
         #test to print
        genre = str(line[-31])
        if genre not in genre_list: #check to see if genre is not in list
            genre_list.append(genre) #if so then add to the list
        genre_list.sort()
    count = 0
    for genre in genre_list:
        count += 1
        print(str(count).rjust(3) + '. '+ genre)


def avg_story_genre(file_name): #function to find average story line per genre
    file = open(file_name, 'r') #opens the file
    file.readline()
    story_length = 0.0     #sets avg story to zero
    amt_genre = 0       #sets genre amt to zero
    genre = ''
    for line in file:
        line = line.split(',') #splits line on the comma

        story_length += float(line[-5])
        amt_genre += 1
        avg = story_length/amt_genre
    return avg


def highest_pub_per_year(file_name): #function to find the publisher with the most games per year
    pass


# print(amt_per_genre('video_games.csv')) #calls video_games.csv file to test
print(avg_story_genre('video_games.csv'))
print(amt_per_genre('video_games.csv'))
