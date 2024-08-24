import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from typing import List, Tuple
from dataclasses import dataclass
import csv
import sys

@dataclass
class Mentor:
    id: int
    name: str
    expertise: str

@dataclass
class Mentee:
    id: int
    name: str
    interests: str

def calculate_similarity(text1: str, text2: str) -> float:
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([text1, text2])
    return cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]

def find_best_matches(mentors: List[Mentor], mentees: List[Mentee]) -> List[Tuple[Mentor, Mentee, float]]:
    matches = []
    available_mentors = mentors.copy()
    available_mentees = mentees.copy()

    total_matches = min(len(available_mentors), len(available_mentees))
    for i in range(total_matches):
        best_match = None
        best_similarity = -1
        best_mentor = None
        best_mentee = None

        for mentor in available_mentors:
            for mentee in available_mentees:
                similarity = calculate_similarity(mentor.expertise, mentee.interests)
                if similarity > best_similarity:
                    best_similarity = similarity
                    best_mentor = mentor
                    best_mentee = mentee

        if best_mentor and best_mentee:
            matches.append((best_mentor, best_mentee, best_similarity))
            available_mentors.remove(best_mentor)
            available_mentees.remove(best_mentee)
        else:
            break

        if (i + 1) % 10 == 0:
            print(f"Processed {i + 1}/{total_matches} matches...")

    return matches

def generate_sample_data(num_mentors: int, num_mentees: int) -> Tuple[List[Mentor], List[Mentee]]:
    mentors = [
        Mentor(i, f"Mentor{i}", f"Expertise{i}, SharedInterest{i%5}") for i in range(1, num_mentors + 1)
    ]

    mentees = [
        Mentee(i, f"Mentee{i}", f"Interest{i}, SharedInterest{i%5}") for i in range(1, num_mentees + 1)
    ]

    return mentors, mentees

def load_data_from_csv(file_path: str) -> Tuple[List[Mentor], List[Mentee]]:
    mentors = []
    mentees = []
    
    try:
        with open(file_path, 'r') as csvfile:
            reader = csv.reader(csvfile)
            headers = next(reader)
            
            if headers != ['type', 'id', 'name', 'expertise_or_interests']:
                raise ValueError("Invalid CSV format. Expected headers: type,id,name,expertise_or_interests")
            
            for row in reader:
                if len(row) < 4:
                    raise ValueError(f"Invalid row: {row}. Expected at least 4 columns.")
                
                type_, id_, name = row[:3]
                expertise_or_interests = ','.join(row[3:])
                
                try:
                    id_ = int(id_)
                except ValueError:
                    raise ValueError(f"Invalid id: {id_}. Must be an integer.")
                
                if type_.lower() == 'mentor':
                    mentors.append(Mentor(id_, name, expertise_or_interests))
                elif type_.lower() == 'mentee':
                    mentees.append(Mentee(id_, name, expertise_or_interests))
                else:
                    raise ValueError(f"Invalid type: {type_}. Must be 'mentor' or 'mentee'.")
    
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    except ValueError as e:
        print(f"Error in CSV file: {str(e)}")
        sys.exit(1)
    
    if not mentors:
        print("Error: No mentors found in the CSV file.")
        sys.exit(1)
    if not mentees:
        print("Error: No mentees found in the CSV file.")
        sys.exit(1)
    
    return mentors, mentees

def main():
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        print(f"Loading data from {file_path}...")
        mentors, mentees = load_data_from_csv(file_path)
    else:
        print("Using sample data...")
        num_mentors, num_mentees = 20, 50  # Reduced numbers for demonstration
        mentors, mentees = generate_sample_data(num_mentors, num_mentees)

    print(f"Matching {len(mentors)} mentors with {len(mentees)} mentees...")
    matches = find_best_matches(mentors, mentees)

    print(f"\nTotal matches made: {len(matches)}")
    print("\nTop 10 matched pairs:")
    for mentor, mentee, similarity in matches[:10]:
        print(f"Mentor: {mentor.name} (ID: {mentor.id})")
        print(f"Mentee: {mentee.name} (ID: {mentee.id})")
        print(f"Similarity: {similarity:.2f}")
        print(f"Mentor expertise: {mentor.expertise}")
        print(f"Mentee interests: {mentee.interests}")
        print("-" * 50)

if __name__ == "__main__":
    main()