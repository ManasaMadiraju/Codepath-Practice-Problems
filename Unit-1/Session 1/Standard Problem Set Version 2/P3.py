'''Write a function trilogy() that accepts an integer year and prints the title of the Batman trilogy movie released that year as outlined below.

Year	Movie Title
2005	"Batman Begins"
2008	"The Dark Knight"
2012	"The Dark Knight Rises"
If the given year does not match one of the years in the table above, print "Christopher Nolan did not release a Batman movie in <year>."'''

def trilogy(year):
    hashmap = {2005:"Batman Begins", 2008:"The Dark Knight", 2012:"The Dark Knight Rises"}

    if year in hashmap:
        print(hashmap[year])
    else:
        print(f"Christopher Nolan did not release a Batman movie in {year}.")


if __name__ == '__main__':
    year = 2008
    trilogy(year)

    year = 1998
    trilogy(year)