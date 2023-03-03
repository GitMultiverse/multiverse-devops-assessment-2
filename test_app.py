from extract import get_input

def test_input_is_list():
    # Arrange
    filename = "results.csv"
    expected_output = list
   
    # act

    output = get_input(filename)

    # Assert
    assert type(output) == expected_output



def test_input_is_correct_df():
   # Arrange
    filename = "results.csv"
    expected_columns = ["user_id","first_name","last_name","answer_1","answer_2","answer_3"]
    expcted_row_count = 26 

    #act 
    output = get_input(filename)
    actual_columns = output[0]
    actual_rowcount = len(output[1:])
    
    #assert
    assert output[0] == expected_columns
    assert len(output) -1  == expcted_row_count