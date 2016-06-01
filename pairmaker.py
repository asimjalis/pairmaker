#!/usr/bin/env python

DEBUG = False

import sys

# Usage message.
USAGE = '''
Usage: 
{program} [OPTIONS]

Example: 
{program} 0426          Pairs for 04/26
{program} today         Pairs for today
{program} help          Usage message

Notes:
- Looks for students.txt in directory where script running from
- File students.txt must contain student names one per line

'''.format(program=sys.argv[0]).strip()

STUDENTS = [
  'Dan',
  'Jayaradha',
  'Jillian',
  'Lilly',
  'Roy',
  'Shylaja',
]

STUDENTS_FILE_NAME = 'students.txt'

import os, re,sys
import datetime as dt

# Reference Monday
MONDAY1_2016 = dt.datetime(2016,1,4)

def date_to_non_weekend(date):
    date_weekday = date.weekday()
    if date_weekday <= 4:
        return date
    days_since_friday = date_weekday - 4
    return date - dt.timedelta(days_since_friday)

def date_to_workday_count(date):
    'Workdays between date and Mon 2016/1/4'
    start = MONDAY1_2016
    date = date_to_non_weekend(date)
    delta = date - start
    days = delta.days
    weeks = days / 7
    weekends = weeks * 2
    workday_count = days - weekends
    return workday_count 

def workday_count_to_shift(workday_count, student_count):
    cycle_length = student_count - 1
    return workday_count % cycle_length

def test_date_to_workday_count():
    assert 0 == date_to_workday_count(dt.datetime(2016,1,4))
    assert 1 == date_to_workday_count(dt.datetime(2016,1,5))
    assert 2 == date_to_workday_count(dt.datetime(2016,1,6))
    assert 3 == date_to_workday_count(dt.datetime(2016,1,7))
    assert 4 == date_to_workday_count(dt.datetime(2016,1,8))
    assert 4 == date_to_workday_count(dt.datetime(2016,1,9))
    assert 4 == date_to_workday_count(dt.datetime(2016,1,10))
    assert 5 == date_to_workday_count(dt.datetime(2016,1,11))
    assert 6 == date_to_workday_count(dt.datetime(2016,1,12))
    assert 7 == date_to_workday_count(dt.datetime(2016,1,13))

def right_shift(l,n):
    n = n % len(l)
    return l[-n:] + l[:-n]

def students_to_even_students(students):
    # If odd append empty string as student
    if len(students) % 2 == 1:
        return students + [""]
    return students

def students_to_count(students):
    return len(students)

def count_to_index(count):
    return range(count)

def index_to_rotated_index(index,shift):
    # First student is fixed point
    index = index[:1] + right_shift(index[1:],shift)
    return index

def index_to_index_pairs(index):
    row_length = len(index) / 2
    row1 = index[:row_length]
    row2 = index[row_length:]
    row2.reverse()
    pairs = []
    for i in xrange(row_length):
        pair = [row1[i],row2[i]]
        pairs.append(pair)
    return pairs

def index_pairs_to_student_pairs(index_pairs,students):
    student_pairs = []
    for index_pair in index_pairs:
        index0 = index_pair[0]
        index1 = index_pair[1]
        student_pair = [students[index0],students[index1]]
        student_pairs.append(student_pair)
    return student_pairs

def student_pairs_to_output_str(student_pairs):
    max_width = student_pairs_to_max_width(student_pairs)
    output_str = ''
    format_str = '%-{0}s <--> %s\n'.format(max_width)
    for student_pair in student_pairs:
        output_str += format_str % tuple(student_pair) 
    return output_str

def student_pairs_to_max_width(student_pairs):
    if len(student_pairs) == 0: return 0
    pair_to_first = lambda pair: pair[0] 
    str_to_len    = lambda s: len(s)
    first_students = map(pair_to_first, student_pairs)
    return max(map(str_to_len, first_students))

def error_handle():
    print "Error: " + str(sys.exc_info()[1])
    if DEBUG:
        print "Trace: "
        raise 
    else:
        os._exit(1)

def str_to_date(s):
    error_message = '"%s" must have format MMDD' % s
    assert re.match(r'^\d{4}$',s), error_message
    month, day = int(s[:2]),int(s[2:4])
    year = dt.datetime.now().year
    date = dt.datetime(year,month,day)
    return date

def date_to_shift(date,student_count):
    workday_count = date_to_workday_count(date)
    shift = workday_count_to_shift(workday_count, student_count)
    return shift 

def argv_to_date(argv):
    if arg_is_today(argv[1]):
        return dt.datetime.now() 
    date_string = argv[1]
    date = str_to_date(date_string)
    return date

def path_to_dir(path):
    assert 1 == 0

def argv_to_students(argv):
    script_path = argv[0]
    script_dir = os.path.dirname(script_path)
    students_file_path = os.path.join(script_dir,STUDENTS_FILE_NAME)
    students = []
    with open(students_file_path,'rb') as file:
        for line in file.readlines():
            student = line.strip()
            students.append(student)
    return students

def arg_in_list(arg,values):
    arg = arg.replace('-','').lower()
    return arg in values

def arg_is_today(arg):
    return arg_in_list(arg,['today','now'])

def arg_is_help(arg):
    return arg_in_list(arg,['help','h','?'])

def argv_to_exception(argv):
    if len(sys.argv) != 2 or arg_is_help(sys.argv[1]):
        print USAGE
        os._exit(1)

def main(argv):
    try:
        argv_to_exception(argv)
        date = argv_to_date(argv)
        students = argv_to_students(argv)
        students = students_to_even_students(students)
        student_count = students_to_count(students)
        shift = date_to_shift(date,student_count)
        print "Day %d" % (shift + 1)
        index = count_to_index(student_count)
        index = index_to_rotated_index(index,shift)
        index_pairs = index_to_index_pairs(index)
        student_pairs = index_pairs_to_student_pairs(index_pairs,students)
        output_str = student_pairs_to_output_str(student_pairs)
        print output_str,

    except: 
        error_handle()

if __name__ == '__main__':
    main(sys.argv)
 
