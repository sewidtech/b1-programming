#grade analyzer



#data collection

student_records = []
stats = {}
unique_scores = {}






for i in range(6):
    name = input("enter your name :").lower().strip()
    score = int(input("enter your score:").strip())
    student_records.append((name , score))
    print()



scores = [score for name , score in student_records]

stats['highest'] = max(scores)
stats['lowest'] = min(scores)
stats['average'] = sum(scores) / len(scores)

unique_score =set(scores)

grade_distribution = {}
for score in scores:
    grade_distribution[score] = grade_distribution.get(score, 0) + 1


#display results

print("\n" + "="*40)
print("=== STUDENT RECORDS ===")
print("="*40)
for i, (name, score) in enumerate(student_records, 1):
    print(f"{i}. {name}: {score}")















