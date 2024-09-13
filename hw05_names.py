#Ame Shajid
#Feburary 13 2024
#In Numerology, every name has a number between 1 and 9 related to it. Given a name, we can calculate the person’s name number. Once we know the name number we can predict things about the person.


#This function named sumDigits takes a number and repeatedly sums the digits until the number is smaller than 10. You may assume the number given is always positive.

def sumDigits(number):
    if number <= 0:
        return "Invalid Input"
    while number >= 10:
        digit_sum = 0
        for digit in str(number):
            digit_sum += int(digit)
        number = digit_sum 
    return number

#This function named nameNumber takes a string containing a name as input. It returns the name number, an integer between 1 and 9. The function will return 0 on bad input, for example an empty string.

def nameNumber(name):
    if len(name) == 0:
        return 0
    letter_values = {
        'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 8, 'G': 3, 'H': 5,
        'I': 1, 'J': 1, 'K': 2, 'L': 3, 'M': 4, 'N': 5, 'O': 7, 'P': 8,
        'Q': 1, 'R': 2, 'S': 3, 'T': 4, 'U': 6, 'V': 6, 'W': 6, 'X': 5,
        'Y': 1, 'Z': 7
    }
    name_number = 0
    for char in name.upper():
        name_number += letter_values.get(char, 0)
    while name_number > 9:
        name_number = sumDigits(name_number)
    return name_number

#This funtion named prediction takes an integer between 1 and 9. It returns the meaning of the number. If a number outside the range is given return Invalid Input as the result string.


def prediction(number):
    if 1 <= number <= 9:
        predictions = {
            1: "A person who is successful in personal ambitions.",
            2: "A gentle and artistic person.",
            3: "A success in their professional career.",
            4: "An unlucky person who must put in extra work for success.",
            5: "An unlucky person who leads an unconventional life.",
            6: "Very academically blessed, high chance at successs",
            7: "A person who has a strong inner spirit.",
            8: "A person who is misunderstood by others and is not respected for their success.",
            9: "A person who is more successful in matters of the material than spiritual."
        }
        return predictions
    else:
        return "Invalid Input"

#in this main we ask for the name so we can start our numerology and then once we get the resultsnamenumber and calculate then it does the prediction

if __name__ == "__main__":
    print("Welcome to Name Number Generator")
    name = input("Enter your name: ")
    result_nameNumber = nameNumber(name)
    result_prediction = prediction(result_nameNumber)

    print(f"Your Name Number is {result_nameNumber}")
    print(f"We predict you are:\n{result_prediction[result_nameNumber]}")
# in this last part it prints all the calculations













