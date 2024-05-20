# 01 - product.py = return product of a and b
def product (a, b):
    return a * b
print(product(2,2)) # 4
print(product(2,-2)) # -4



# 02 - weekday_name.py = return name of weekday. For days not between 1 and 7, return none
def weekday_name(day_of_week):
    week = [
        "Sunday",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday"
        "Saturday"
    ]
    
    if day_of_week < 1 or day_of_week > 7:
        return None
    
    return week[day_of_week - 1]
print(weekday_name(1)) # Sunday
print(weekday_name(9)) # None



# 03 - last_element.py = return last item in list
def last_element(lst):
    if lst:
        return lst[-1]
print(last_element([1, 2, 3])) # 3
print(last_element([])) # None




# 04 - number_compare.py = report on whether a>b, b>a, or b==a
def number_compare(a,b):
    if a > b:
        print("First is greater")
    elif a < b:
        print ('Second is greater')
    elif a == b:
        print('Numbers are equal')




#05 - reverse_string.py = reverse what is written in string
def reverse_string(phrase):
    return phrase[::-1]
print(reverse_string('animal')) # 'lamina'




#06 - single_letter_count.py = how many times does letter appear in word
def single_letter_count(word, letter):
    return word.lower().count(letter.lower())
print(single_letter_count('Hello World', 'h')) # 1



#07 - multiple_letter_count.py = return dict of {ltr: frequency}
def multiple_letter_count(phrase):
    nums = {}

    for ltr in phrase:
        nums[ltr] = nums.get(ltr, 0) + 1

    return nums
print(multiple_letter_count('yummy')) #  {'y': 2, 'u': 1, 'm': 2}

#08 - list_manipulation.py
def list_manipulation(lst, command, location, value=None):
    """Mutate lst to add/remove from beginning or end.

    - lst: list of values
    - command: command, either "remove" or "add"
    - location: location to remove/add, either "beginning" or "end"
    - value: when adding, value to add

    remove: remove item at beginning or end, and return item removed

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'remove', 'end')
        3

        >>> list_manipulation(lst, 'remove', 'beginning')
        1

        >>> lst
        [2]

    add: add item at beginning/end, and return list

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'add', 'beginning', 20)
        [20, 1, 2, 3]

        >>> list_manipulation(lst, 'add', 'end', 30)
        [20, 1, 2, 3, 30]

        >>> lst
        [20, 1, 2, 3, 30]

    Invalid commands or locations should return None:

        >>> list_manipulation(lst, 'foo', 'end') is None
        True

        >>> list_manipulation(lst, 'add', 'dunno') is None
        True
    """

    if command == "remove":
        if location == "end":
            return lst.pop()
        elif location == "beginning":
            return lst.pop(0)
        
    elif command == "add":
        if location == "beginning":
            lst.insert(0, value)
            return lst
        elif location == "end":
            lst.append(value)
            return lst
        



#09 is_palindrome.py - is phrase a palindrome (same read backwards as forward)
def is_palindrome(phrase):
    check = phrase.lower().replace(' ', '') # should ignore capitalization/spaces
    return check == check[::-1]
print(is_palindrome('taco cat')) # True



#10 frequency.py - return frequency of term in lst
def frequency(lst, search_term):
    return lst.count(search_term)
print(frequency([1, 4, 3, 4, 4], 4)) # 3

#11 - flip_case.py = in a phrase, swap lowercase/uppercase letters 
def flip_case(phrase, to_swap):
    to_swap = to_swap.lower()
    switch = ""

    for ltr in phrase:
        if ltr.lower() == to_swap:
            ltr = ltr.swapcase()
        switch += ltr
    return switch
print(flip_case('aaaaaBBBBBBBcccccc', 'b')) # aaaaabbbbbbbcccccc
print(flip_case('BoBBY', 'B')) # bobbY

#12 multiply_even_numbers - multiply the even numbers
def multiply_even_numbers(nums):
    product = 1
    for num in nums:
        if num % 2 == 0:
            product = product * num
    return product
print(multiply_even_numbers([2, 3, 4, 5, 6])) # 48



#13 - capitalize.py = capitalize for letter of first word of phrase
def capitalize(phrase):
    return phrase.capitalize()
print(capitalize('only first word')) #Only first word




#14 - compact.py - return a copy of lst with non-true elements removed
def compact(lst):
    return [val for val in lst if val]
print(compact([0, 1, 2, '', [], False, (), None, 'All done'])) # [1, 2, 'All done']



#15 - intersection.py = return intersection of 2 lst as a new lst
def intersection(l1, l2):
    between = set(l2)

    return list(set(l1) & set(l2))
print(intersection([1, 2, 3], [3, 4])) # 3



#16 partition.py
def partition(lst, fn):
    """Partition lst by predicate.

     - lst: list of items
     - fn: function that returns True or False

     Returns new list: [a, b], where `a` are items that passed fn test,
     and `b` are items that failed fn test.

        >>> def is_even(num):
        ...     return num % 2 == 0

        >>> def is_string(el):
        ...     return isinstance(el, str)

        >>> partition([1, 2, 3, 4], is_even)
        [[2, 4], [1, 3]]

        >>> partition(["hi", None, 6, "bye"], is_string)
        [['hi', 'bye'], [None, 6]]
    """

    true_list = []
    false_list = []

    for val in lst:
        if fn(val):
            true_list.append(val)
        else:
            false_list.append(val)
    return [true_list, false_list]



# 17 - mode.py = return most common number in list
def mode(nums):
    counter = {}

    for num in nums:
        counter[num] = counter.get(num, 0) + 1

    max_value = max(counter.value())

    for (num, freq) in counter.items():
        if freq == max_value:
            return num



# 18 - calculate.py
def calculate(operation, a, b, make_int=False, message='The result is'):
    """Perform operation on a + b, ()possibly truncating) & returning w/msg.

    - operation: 'add', 'subtract', 'multiply', or 'divide'
    - a and b: values to operate on
    - make_int: (optional, defaults to False) if True, truncates to integer
    - message: (optional) message to use (if not provided, use 'The result is')

    Performs math operation (truncating if make_int), then returns as
    "[message] [result]"

        >>> calculate('add', 2.5, 4)
        'The result is 6.5'

        >>> calculate('subtract', 4, 1.5, make_int=True)
        'The result is 2'

        >>> calculate('multiply', 1.5, 2)
        'The result is 3.0'

        >>> calculate('divide', 10, 4, message='I got')
        'I got 2.5'

    If a valid operation isn't provided, return None.

        >>> calculate('foo', 2, 3)

    """
    if operation == "add":
        result = a + b
    elif operation == "subtract":
        result = a - b
    elif operation == "multiply":
        result = a * b
    elif operation == "divide":
        result = a / b
    else:
        return
    
    if make_int:
        res = int(res)

    return f"{message} {result}"

# 19 friend_date.py
def friend_date(a, b):
        """Given two friends, do they have sny hobbies in common?
        - a: friend #1, a tuple of (name, age, list-of-hobbies)
        - b: same, for friend #2

        Returns True if they have any hobbies in common, False is not.
        """
        if set(a[2]) & set(b[2]):
            return True
        else:
            return False
elmo = ('Elmo', 5, ['hugging', 'being nice'])
sauron = ('Sauron', 5000, ['killing hobbits', 'chess'])
print(friend_date(elmo, sauron)) # False



# 20 triple_and_filter.py
def triple_and_filter(nums):
    """Return new list of tripled nums for those nums divisible by 4.

    Return every number in list that is divisible by 4 in a new list,
    except multipled by 3."""
    return [num * 3 for num in nums if num % 4 == 0]
print(triple_and_filter([1, 2, 3, 4])) # [12]




# 21 - extract_full_name.py
def extract_full_names(people):
    """Return list of names, extracting from first+last keys in people dicts.

    - people: list of dictionaries, each with 'first' and 'last' keys for
              first and last names

    Returns list of space-separated first and last names."""
    return [f"{person['first']} {person['last']}" for person in people]

names = [
    {'first': 'Ada', 'last': 'Lovelace'}
]

print(extract_full_names(names)) # ['Ada Lovelace']




# 22 - sum_floats.py - return sum of floating point numbers in nums
def sum_floats(nums):
    return sum([num for num in nums if isinstance(num, float)])
print(sum_floats([1.5, 2.4, 'awesome', [], 1])) # 3.9



#23 - list_check.py - Are all items in lst a list?
def list_check(lst):
    for item in lst:
        if not isinstance(item, list):
            return False
        
    return True
print(list_check([[1], [2, 3]])) # True



#24 - remove_every_other.py
def remove_every_other(lst):
    return lst[::2]
lst = [1, 2, 3, 4, 5]
print(remove_every_other(lst)) # [1, 3, 5]

# 25 = sum_pairs.py - return tuple of first pair of nums that sum to goal
def sum_pairs(nums, goal):
    complete = set()

    for i in nums:
        difference = goal - i

        if difference in complete:
            return (difference, i)
        
        complete.add(i)
    return()

print(sum_pairs([11, 20, 4, 2, 1, 5], 100)) # ()




#26 vowel_count - return frequency map of vowels, case-insensitive
VOWELS = set("aeiou")

def vowel_count(phrase):
    phrase = phrase.lower()
    counter = {}

    for ltr in phrase:
        if ltr in VOWELS:
            counter[ltr] = counter.get(ltr, 0) + 1

    return counter
print(vowel_count('HOW ARE YOU? i am great!')) # {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}



#27 - titleize.py - return phrase in title case (each word capitalized)
def titleize(phrase):
    return phrase.title()
print(titleize('this is awesome')) #This Is Awesome


#28 - find_factors.py - find factors of num, in increasing order
def find_factors(num):
    new_list = [n for n in range (1, num // 2 + 1) if num % n == 0]

    new_list.append(num)

    return new_list
print(find_factors(10)) # [1, 2, 5, 10]


#29 includes.py
def includes(collection, sought, start=None):
    """Is sought in collection, starting at index start?

    Return True/False if sought is in the given collection:
    - lists/strings/sets/tuples: returns True/False if sought present
    - dictionaries: return True/False if *value* of sought in dictionary

    If string/list/tuple and `start` is provided, starts searching only at that
    index. This `start` is ignored for sets/dictionaries, since they aren't
    ordered."""

    if isinstance(collection, dict):
        return sought in collection.values()
    
    if start is None or isinstance(collection, set):
        return sought in collection
    
    return sought in collection[start:]
print(includes({"apple": "red", "berry": "blue"}, "blue")) # True



#30 - repeat.py = return phrase, repeated num times.
def repeat(phrase, num):
    if not isinstance(num, int) or num < 0:
        return None
    
    return phrase * num
print(repeat('*', 3)) # ***

#31 - truncate.py - return truncated-at-n-chars version of phrase
def truncate(phrase, n):
    if n < 3:
        return "Truncation must be at least 3 characters."
    
    if n > len(phrase) + 2:
        return phrase
    
    return phrase[:n - 3] + "..."
print(truncate("Woah", 4)) # W...


#32 two_list_dictionary.py - make dictionaries of keys and values
def two_list_dictionary(keys, values):
    out = {}

    for idx, val in enumerate(keys):
        out[val] = values[idx] if idx < len(values) else None

        return out


#33 sum_range.py - return sum of numbers from start...end
def sum_range(nums, start=0, end=None):
    if end is None:
        end = len(nums)
    return sum(nums[start:end + 1])
nums = [1, 2, 3, 4]
print(sum_range(nums)) # 10



#34 same_frequency.py - returns frequency counter mapping of coll
def freq_counter(coll):
    counts = {}

    for x in coll:
        counts[x] = counts.get(x, 0) + 1

    return counts

def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?"""
    return freq_counter(str(num1)) == freq_counter(str(num2))

print(same_frequency(551122, 221515)) # True


#35 two_oldest_ages.py - return two distinct oldest ages as tuple
def two_oldest_ages(ages):
    unique_ages = set(ages)
    oldest = sorted(unique_ages)[-2:]
    return tuple(oldest)
print(two_oldest_ages([1, 2, 10, 8])) # (8, 10)


#36 find_the_duplicate = find duplicate number in nums
def find_the_duplicate(nums):

    duplicate = set()

    for num in nums:
        if num in duplicate:
            return num
        duplicate.add(num)


#37 sum_up_diagnols - given a matrix, return sum of diagonals
def sum_up_diagonals(matrix):
    total = 0

    for i in range(len(matrix)):
        total += matrix[i][i]
        total += matrix[i][-1 - i]

    return total



#38 min_max_key_in_dictionary.py - return tuple (min-keys, max-keys)
def min_max_keys(d):
    keys = d.keys()
    return (min(keys), max(keys))
print(min_max_keys({"apple": "red", "cherry": "red", "berry": "blue"}))




#39 find_greater_numbers.py - return # of times a number is followed by a greater number
def find_greater_numbers(nums):
    count = 0

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[j] > nums[i]:
                count += 1

    return count
print(find_greater_numbers([6, 1, 2, 7])) # 4





# fs1 is_odd_string.py
def is_odd_string(word):
    """Is the sum of the character-positions odd?

    Word is a simple word of uppercase/lowercase letters without punctuation.

    For each character, find it's "character position" ("a"=1, "b"=2, etc).
    Return True/False, depending on whether sum of those numbers is odd."""

    DIFF = ord("a") - 1

    total = sum((ord(c) - DIFF) for c in word.lower())

    return total % 2 == 1
print(is_odd_string('aaaa')) # False



# fs2 valid_parentheses.py - Are the parentheses validly balanced
def valid_parentheses(parens):
    counter = 0

    for p in parens:
        if p == '(':
            counter += 1
        elif p == ')':
            counter -= 1

        if counter < 0:
            return False
        
    return counter == 0
print(valid_parentheses("()()")) # True



#fs3 three_odd_numbers.py - is the sum of any 3 sequential numbers odd
def three_odd_numbers(nums):
    for i in range(len(nums) - 2):
        if (nums[i] + nums[i + 1] + nums[i + 2]) % 2 != 0:
            return True
        
        return False
print(three_odd_numbers([0, -2, 4, 1, 9, 12, 4, 1, 0])) # False


#fs4 reverse_vowels.py - reverse vowels in a string
def reverse_vowels(s):
    vowels = set("aeiou")

    string = list(s)
    i = 0
    j = len(s) - 1

    while i < j:
        if string[i].lower() not in vowels:
            i += 1
        elif string[j].lower() not in vowels:
            j -= 1
        else:
            string[i], string[j] = string[j], string[i]
            i += 1
            j -= 1

    return "".join(string)
print(reverse_vowels("Reverse Vowels In A String")) # RivArsI Vewols en e Streng



#fs5 read_file_list.py - read file and print out each line separately with a "-" before it
def read_file_list(filename):
    with open(filename) as f:
        for line in f:
            line = line.strip()
            print(f"- {line}")
print(read_file_list("dogs"))
print(read_file_list("cats"))