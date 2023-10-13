from a01 import make_output_file

def test_make_output_file():
    test_output_filepath = 'Assignment01/my_test_airlinehub.ans' 
    make_output_file('Assignment01/airlinehub.in', test_output_filepath)
    test_file = open(test_output_filepath, 'r')
    test_file = test_file.readlines()
    print("test_file:", test_file)
    correct_output_file = open('Assignment01/airlinehub.ans')
    correct_output_file = correct_output_file.readlines()
    print("correct_output_file:",correct_output_file)
    print("test_file == correct_output_file:", test_file == correct_output_file)
    assert test_file == correct_output_file


test_make_output_file()