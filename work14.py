def brack(a):
    for i in a:
        if i=="[]" or i=='{}' or i=='()':
            print("balnced")
        else:
            print('not balnced')
brack("}{")