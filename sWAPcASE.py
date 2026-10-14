def swap_case(s):
    trim_text = s.strip()
    final_answer = ""
    for letter in trim_text:
        if letter.isupper():
            final_answer += letter.lower()
         elif letter.islower():
            final_answer += letter.upper()
	 else:
            final_answer += letter
    return final_answer

if \_\_name\_\_ == '\_\_main\_\_':
    s = input()
    result = swap_case(s)
    print(result)
