#!/usr/bin/env python3

number_dict = {
   "zero": "0",
   "one": "1",
   "two": "2",
   "three": "3",
   "four": "4",
   "five": "5",
   "six": "6",
   "seven": "7",
   "eight": "8",
   "nine": "9",
}

def calibrate_numbers(line):
   integer_list = []
   for character in line:
       if character.isdigit():
           integer_list.append(character)
   value = str(integer_list[0]) + str(integer_list[-1])
   return int(value)

def calibrate_distilled_numbers(line, number_dict):
   distilled_numbers = []
   indexed_position = 0
   while indexed_position < len(line):
      found = False
      for word in number_dict:
         if line[indexed_position:].startswith(word):
            distilled_numbers.append(number_dict[word])
            indexed_position += len(word)
            found = True
            indexed_position -= 1
            break
      if not found:
         if line[indexed_position].isdigit():
            distilled_numbers.append(line[indexed_position])
         indexed_position += 1

   value = str(distilled_numbers[0]) + str(distilled_numbers[-1])
   return int(value)

def solution_d1p1():
    input = open('input.txt','r')
    calibrated_value_list = []
    for line in input:
        calibrated_value_list.append(calibrate_numbers(line))
    print("Solution part 1: "+str(sum(calibrated_value_list)))

def solution_d1p2():
    input = open('input.txt','r')
    calibrated_value_list = []
    for line in input:
        calibrated_value_list.append(calibrate_distilled_numbers(line, number_dict))
    print("Solution part 2: "+str(sum(calibrated_value_list)))

def main():
    solution_d1p1()
    solution_d1p2()

if __name__ == "__main__":
    main()
