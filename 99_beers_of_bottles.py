def main():
    print("Printing the lyrics of the song 99 bottles of Beer")
    print("Starting with 99 bottles \n")
    for i in range(99, 0, -1):
        print("{} bottles of beer on the wall, {} bottles of beer.".format(i, i))
        print("Take one down and pass it around, {} bottles of beer on the wall.\n".format(i-1))



if __name__ == "__main__":
    main()
