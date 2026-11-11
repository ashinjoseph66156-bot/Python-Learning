
# STEP 1: Preloaded Feedbacks

feedback_data = {
    'S_No': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],

    'Name': ['Ravi', 'Meera', 'Sam', 'Anu', 'Raj',
             'Divya', 'Arjun', 'Kiran', 'Leela', 'Nisha'],

    'Feedback': [
        ' Very GOOD Service!!!',
        'poor support, not happy ',
        'GREAT experience! will come again.',
        'okay okay...',
        ' not BAD',
        'Excellent care, excellent staff!',
        'good food and good ambience!',
        'Poor response and poor handling of issue',
        'Satisfied. But could be better.',
        'Good support... quick service.'
    ],

    'Rating': [5, 2, 5, 3, 2, 5, 4, 1, 3, 4]
}


# STEP 2: Add More Feedbacks

n = int(input("How many more feedbacks do you want to add? "))

for i in range(n):

    name = input("Enter name: ")
    feedback = input("Enter feedback: ")
    rating = int(input("Enter rating (1-5): "))

    feedback_data['S_No'].append(11 + i)
    feedback_data['Name'].append(name)
    feedback_data['Feedback'].append(feedback)
    feedback_data['Rating'].append(rating)


# STEP 3: Text Cleaning

for i in range(len(feedback_data['Feedback'])):

    feedback = feedback_data['Feedback'][i]

    feedback = feedback.replace(".", "")
    feedback = feedback.replace(",", "")
    feedback = feedback.replace("!", "")
    feedback = feedback.replace("?", "")

    feedback = ' '.join(feedback.split())

    feedback = feedback.lower()

    feedback_data['Feedback'][i] = feedback


# STEP 4: Word Count Insights

def count_word_in_feedbacks(word):

    count = 0
    word = word.lower()

    for feedback in feedback_data['Feedback']:

        if word in feedback.split():
            count += 1

    return count


print("\nWord Count Insights")

print("Good:", count_word_in_feedbacks("good"))
print("Poor:", count_word_in_feedbacks("poor"))
print("Excellent:", count_word_in_feedbacks("excellent"))


# STEP 5: Final Summary & Insights

# 1. Display Final Cleaned Feedback Data

print("\nFinal Cleaned Feedback Data:")
print(feedback_data)


# 2. Average Rating

total_rating = sum(feedback_data['Rating'])

average_rating = total_rating / len(feedback_data['Rating'])

print("\nAverage Rating:", average_rating)


# 3. Longest Feedback

longest_feedback = max(
    feedback_data['Feedback'],
    key=lambda x: len(x.split())
)

print("\nLongest Feedback:", longest_feedback)

print("Word Count:", len(longest_feedback.split()))


# 4. Unique Words

unique_words = set()

for feedback in feedback_data['Feedback']:

    words = feedback.split()

    for word in words:
        unique_words.add(word)

print("\nUnique Words:")
print(sorted(unique_words))

print("Total Unique Words:", len(unique_words))


# OPTIONAL: Sort Feedbacks by Rating (Highest to Lowest)

sorted_feedback = sorted(
    zip(
        feedback_data['Name'],
        feedback_data['Feedback'],
        feedback_data['Rating']
    ),
    key=lambda x: x[2],
    reverse=True
)

print("\nFeedback Sorted by Rating:")

for item in sorted_feedback:
    print(item)






