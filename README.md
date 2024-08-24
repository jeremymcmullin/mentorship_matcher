# Mentorship Matcher

This project provides two approaches for matching mentors with mentees based on their expertise and interests in the field of Product Management. The simple approach uses a basic text similarity metric, while the advanced approach utilizes TF-IDF and cosine similarity for more accurate matching.

## Simple Approach

The simple approach, implemented in `mentor_matcher.py`, uses the following techniques:

1. Text preprocessing: Converts text to lowercase, removes punctuation, and splits into words.
2. Similarity calculation: Uses a basic set intersection over union method to calculate similarity between mentor expertise and mentee interests.
3. Matching algorithm: Iteratively finds the best matches based on similarity scores.

### Usage (Simple Approach)

1. Ensure you have Python 3.7+ installed.
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the script:
   - With sample data:
     ```
     python mentor_matcher.py
     ```
   - With external CSV file:
     ```
     python mentor_matcher.py path/to/your/data.csv
     ```

## Advanced Approach

The advanced approach, implemented in `advanced_mentor_matcher.py`, uses more sophisticated techniques:

1. TF-IDF Vectorization: Converts text into numerical vectors that capture the importance of words.
2. Cosine Similarity: Measures the similarity between TF-IDF vectors for more accurate matching.
3. Optimized Matching: Uses NumPy and scikit-learn for faster processing of larger datasets.

### Usage (Advanced Approach)

1. Ensure you have Python 3.7+ installed.
2. Create a virtual environment and install the required dependencies:
   ```
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements_advanced.txt
   ```
3. Run the script:
   - With sample data:
     ```
     python advanced_mentor_matcher.py
     ```
   - With external CSV file:
     ```
     python advanced_mentor_matcher.py path/to/your/data.csv
     ```

## Using External CSV Files

Both approaches support loading data from external CSV files. The CSV file should have the following format:

```
type,id,name,expertise_or_interests
mentor,1,John Doe,Product strategy, User experience design, Agile methodologies
mentee,2,Jane Smith,Interested in product strategy and user experience design
```

- The first row should be the header: `type,id,name,expertise_or_interests`
- Each subsequent row represents either a mentor or a mentee
- The `type` column should be either "mentor" or "mentee"
- The `id` column should be a unique integer for each entry
- The `name` column should contain the person's name
- The `expertise_or_interests` column should contain the mentor's expertise or the mentee's interests

If there are any issues with the CSV file format, the script will provide detailed error messages to help you correct the file.

## Sample Data

We provide two sample CSV files in the `sample_data` folder:

1. `small_test.csv`: Contains data for 10 mentors and 30 mentees.
2. `large_test.csv`: Contains data for 60 mentors and 160 mentees.

These files contain realistic data for a Product Management mentorship program, including various topics related to product management and development for both hardware and software products.

To use these sample files, run the scripts with the following commands:

For the simple approach:
```
python mentor_matcher.py sample_data/small_test.csv
```
or
```
python mentor_matcher.py sample_data/large_test.csv
```

For the advanced approach:
```
python advanced_mentor_matcher.py sample_data/small_test.csv
```
or
```
python advanced_mentor_matcher.py sample_data/large_test.csv
```

## Sample Output

### Simple Approach Output

```
Loading data from sample_data/small_test.csv...
Matching 10 mentors with 30 mentees...

Matched pairs:
Mentor: Robert Taylor (ID: 7)
Mentee: Ryan Garcia (ID: 17)
Similarity: 0.56
Mentor expertise: Feature prioritization, Product metrics, Wireframing and prototyping
Mentee interests: Interested in feature prioritization and product metrics
--------------------------------------------------
Mentor: Michael Chen (ID: 3)
Mentee: Matthew Davis (ID: 35)
Similarity: 0.54
Mentor expertise: Product lifecycle management, A/B testing, Data-driven decision making
Mentee interests: Interested in A/B testing and data-driven decision making
--------------------------------------------------
Mentor: David Lee (ID: 5)
Mentee: Ethan Brown (ID: 15)
Similarity: 0.54
Mentor expertise: Product launch strategies, Cross-functional team leadership, Scrum
Mentee interests: Wants to learn about product launch strategies and cross-functional team leadership
--------------------------------------------------
(Output truncated for brevity)
```

### Advanced Approach Output

```
Loading data from sample_data/small_test.csv...
Matching 10 mentors with 30 mentees...
Processed 10/10 matches...

Total matches made: 10

Top 10 matched pairs:
Mentor: David Lee (ID: 5)
Mentee: Ethan Brown (ID: 15)
Similarity: 0.57
Mentor expertise: Product launch strategies, Cross-functional team leadership, Scrum
Mentee interests: Wants to learn about product launch strategies and cross-functional team leadership
--------------------------------------------------
Mentor: Robert Taylor (ID: 7)
Mentee: Ryan Garcia (ID: 17)
Similarity: 0.56
Mentor expertise: Feature prioritization, Product metrics, Wireframing and prototyping
Mentee interests: Interested in feature prioritization and product metrics
--------------------------------------------------
Mentor: Kevin Patel (ID: 9)
Mentee: William Nguyen (ID: 19)
Similarity: 0.55
Mentor expertise: Agile product management, OKRs, Product backlog management
Mentee interests: Curious about agile product management and OKRs
--------------------------------------------------
(Output truncated for brevity)
```

## Additional Considerations

1. Data Privacy: Both approaches handle sensitive information (names and interests). Ensure proper data handling and privacy measures are in place when using real data.

2. Scalability: The advanced approach is better suited for larger datasets due to its use of optimized libraries like NumPy and scikit-learn.

3. Customization: Both scripts can now use either sample data or data from CSV files. For real-world use, prepare your data in the specified CSV format.

4. Performance: The advanced approach may require more computational resources but provides more accurate matches, especially for larger datasets or more complex text descriptions.

5. Matching Criteria: Consider expanding the matching criteria beyond text similarity. Factors like availability, time zones, or specific skills could be incorporated for more comprehensive matching.

6. User Interface: These scripts provide a command-line interface. For broader use, consider developing a web interface or API.

7. Feedback Mechanism: Implement a system for mentors and mentees to provide feedback on their matches, which could be used to improve the matching algorithm over time.

8. Data Validation: Both scripts include data validation for CSV files. If there are issues with the file format or content, clear error messages will be displayed to help users correct their data.

## Contributing

Contributions to improve the matching algorithms, add features, or enhance the user experience are welcome. Please feel free to submit issues or pull requests.

## License

This project is open-source and available under the MIT License.