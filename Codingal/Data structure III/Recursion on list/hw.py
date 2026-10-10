scores = [45, 60, 75, 88, 92]

print("\nScore List:", scores)

print("\nPART 1: Head-Tail Pattern")
print("Full List:", scores)
print("Head:", scores[0])
print("Tail:", scores[1:])

def show_shrink(score_list):
    print("Current list:", score_list)

    if len(score_list) == 1:
        print("Base case reached:", score_list)
        return

    show_shrink(score_list[1:])

print("\nPART 2: Base Case for Lists")
show_shrink(scores)

def is_sorted(score_list):
    if len(score_list) <= 1:
        return True

    if score_list[0] > score_list[1]:
        return False

    return is_sorted(score_list[1:])

print("\nPART 3: Sorted Check with Recursion")
print("Scores:", scores)
print("Is the list sorted?", is_sorted(scores))

unsorted_scores = [45, 88, 60, 75, 92]
print("Unsorted Scores:", unsorted_scores)
print("Is the list sorted?", is_sorted(unsorted_scores))

def recursive_sum(score_list):
    if len(score_list) == 0:
        return 0

    return score_list[0] + recursive_sum(score_list[1:])

print("\nPART 4: Sum of a List with Recursion")
print("Total Score:", recursive_sum(scores))

def largest_score(score_list):
    if len(score_list) == 1:
        return score_list[0]

    largest_in_tail = largest_score(score_list[1:])

    if score_list[0] > largest_in_tail:
        return score_list[0]

    return largest_in_tail

print("\nPART 5: Largest Element with Recursion")
print("Highest Score:", largest_score(scores))

