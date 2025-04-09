import cerberus

'''
1.
'''
def fn_one():
    schema = {'Name': {'type': 'string', 'minlength': 10, 'maxlength': 30}}

    v = cerberus.Validator(schema)

    example_tests = {'Name': 'john milder', 'Name': 'jacob howerd', 'Name': 'hi'}

    if v.validate(example_tests):
        print("Data is clean")
    else:
        print("**** ERRORS ******\n" + str(v.errors) + f"\n Please look at the **{v.document_error_tree['Name'].errors[0].schema_path[0]}** that has a value of **{v.document_error_tree['Name'].errors[0].value}** as it has a **{v.document_error_tree['Name'].errors[0].schema_path[1]}** error!")

'''
2.
'''
def fn_two():
    schema = {'Age': {'type': 'number', 'min': 18, 'max': 65}}

    v = cerberus.Validator(schema)

    example_tests = {'Age': 25, 'Age': 64}

    if v.validate(example_tests):
        print("Data is clean")
    else:
        print("**** ERRORS ******\n" + str(v.errors) + f"\n Please look at the **{v.document_error_tree['Age'].errors[0].schema_path[0]}** that has a value of **{v.document_error_tree['Age'].errors[0].value}** as it has a **{v.document_error_tree['Age'].errors[0].schema_path[1]}** error!")


'''
3.
'''
def fn_three():
    schema = {'SSN': {'type': 'string', 'minlength': 11, 'maxlength': 11, 'regex': '^(?!000|.+0{4})(?:\d{9}|\d{3}-\d{2}-\d{4})$'}}

    v = cerberus.Validator(schema)

    example_tests = {'SSN': '001-23-0000'}

    if v.validate(example_tests):
        print("Data is clean")
    else:
        print("**** ERRORS ******\n" + str(v.errors) + f"\n Please look at the **{v.document_error_tree['SSN'].errors[0].schema_path[0]}** that has a value of **{v.document_error_tree['SSN'].errors[0].value}** as it has a **{v.document_error_tree['SSN'].errors[0].schema_path[1]}** error!")

'''
4.
'''
def fn_four():
    schema = {'Phone number': {'type': 'string', 'minlength': 12, 'maxlength': 12, 'regex': '^(?!000|.+0{4})(?:\d{9}|\d{3}.\d{3}.\d{4})$'}}

    v = cerberus.Validator(schema)

    example_tests = {'Phone number': '12.122.1222'}

    if v.validate(example_tests):
        print("Data is clean")
    else:
        print("**** ERRORS ******\n" + str(v.errors) + f"\n Please look at the **{v.document_error_tree['Phone number'].errors[0].schema_path[0]}** that has a value of **{v.document_error_tree['Phone number'].errors[0].value}** as it has a **{v.document_error_tree['Phone number'].errors[0].schema_path[1]}** error!")

if __name__ == '__main__':
    print("******* ANSWER FOR NAMD AND STRING *******")
    fn_one()
    print("******* END OF ANSWER FOR NAME AND STRING ********")
    print("******* ANSWER FOR AGE AND INTEGER *******")
    fn_two()
    print("******* END OF ANSWER FOR AGE AND INTEGER ********")
    print("******* ANSWER FOR SSN *******")
    fn_three()
    print("******* END OF ANSWER FOR SSN ********")
    print("******* ANSWER FOR PHONE NUMBER *******")
    fn_four()
    print("******* END OF ANSWER FOR PHONE NUMBER ********")
