# create list of words we don't care about
# articles, punctuation, etc.

# create a set from the resume
# create a set from the job description
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter

# Download NLTK resources if not already downloaded
#nltk.download("punkt")
#nltk.download("stopwords")


def extract_keywords(text):
    # Tokenize the text
    words = word_tokenize(text)
    # Remove stopwords
    stop_words = set(stopwords.words("english"))
    words = [
        word.lower()
        for word in words
        if word.isalnum() and word.lower() not in stop_words
    ]

    # Count word frequencies
    word_freq = Counter(words)

    # Return the most common words
    return word_freq.most_common()

def get_all_words(input_file):
    #take a string input file
    # Read job description from file
    with open(input_file, "r") as file:
        input_file_description = file.read()
    return input_file_description

def compare_keywords(resume, job_description):
    # get total number of words in job description 
    # get number of matches from resume 
    # return percent complete
    # return top 3 suggestions 
    word_denominator = len(job_description)


# Read job description from file
#with open("job_description.txt", "r") as file:
#    job_description = file.read()

# Extract keywords
# keywords = extract_keywords(job_description)

# Print the keywords
def print_keywords(keywords):
    print("Keywords extracted from the job description:")
    for keyword, frequency in keywords:
        print(keyword, ":", frequency)


def get_missing_keywords(job_description_keywords, resume_keywords):
    # Initialize a dictionary to store the counts
    keyword_counts = {}
    optional_additions = []

    # Iterate over keywords in job_description_keywords
    for keyword, count in job_description_keywords:
        # Count occurrences in resume_keywords
        occurrences_in_resume = sum(1 for k, _ in resume_keywords if k == keyword)
        # Store the count in the dictionary
        keyword_counts[keyword] = occurrences_in_resume

    # Print the counts
    total = sum(1 for count in keyword_counts.values() if count > 0)
    print("Matched words:", total, "of", len(job_description_keywords))

    # Get optional additions
    for keyword, count in keyword_counts.items():
        if count == 0:
            optional_additions.append(keyword)

    #print("Returning", optional_additions, "optional additions for your resume")

    return optional_additions

def compare():
    resume_keywords = get_all_words("resume.txt")
    resume_keywords_extracted = extract_keywords(resume_keywords)

    job_description_keywords = get_all_words("job_description.txt")
    job_description_keywords_extracted = extract_keywords(job_description_keywords)

    optional_additions = get_missing_keywords(job_description_keywords_extracted, resume_keywords_extracted)

    print("Optional Additons =")
    print(optional_additions)


compare()
