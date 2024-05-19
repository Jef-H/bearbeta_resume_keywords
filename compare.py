#!/usr/bin/python3
# -*- coding: utf-8 -*-

from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import argparse
import fitz
import nltk

# Download NLTK resources if not already downloaded
nltk.download("punkt", quiet=True)
nltk.download("stopwords", quiet=True)

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


def get_all_words_txt(input_file, input_pdf_path):
    # take a string input file
    # Read job description from file
    input_file_description = ""
    if input_pdf_path:
        doc = fitz.open(input_pdf_path)
        for page in doc:
            input_file_description += page.get_text()
    else:
        with open(input_file, "r") as file:
            input_file_description = file.read()
    return input_file_description


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

    # print("Returning", optional_additions, "optional additions for your resume")

    return optional_additions


def compare():

    parser = argparse.ArgumentParser()
    # Adding optional argument to input pdf resume
    parser.add_argument("-r", "--Resume", help = "Specify PDF input path for Resume input")
    parser.add_argument("-j", "--Job", help = "Specify PDF input path for Job Description input")
    args = parser.parse_args()

    resume_keywords = get_all_words_txt("resume.txt", args.Resume)
    resume_keywords_extracted = extract_keywords(resume_keywords)

    job_description_keywords = get_all_words_txt("job_description.txt", args.Job)
    job_description_keywords_extracted = extract_keywords(job_description_keywords)

    optional_additions = get_missing_keywords(
        job_description_keywords_extracted, resume_keywords_extracted
    )

    print("Consider adding some of these keywords to your resume")
    print(optional_additions)


compare()
