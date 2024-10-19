import pandas as pd
def AddUser(df):
    # data = {'id':[8347820],
    #         'First Name': ['Ariel'],
    #         'Last Name': ['Spivak'],
    #         'Hebrew First Name':['אריאל'],
    #         'Hebrew Last Name':['ספיבק'],
    #         'Initials':['AS'],
    #         'rank':['קא"ב'],
    #         'title':["מהנדס מערכת ניווט"]
    #         }
    #
    # # Create DataFrame
    # df = pd.DataFrame(data)
    # df.to_csv('users/users.csv', index=False)
    #
    # print(df.keys())
    user = []
    for key in df.keys():
        user.append(input(f'{key}: '))
    userDict = dict(zip(df.keys(),user))
    df = df.append(userDict,ignore_index=True)
    df.to_csv('users/users.csv', index=False)
    return df

if __name__ == '__main__':
    df = pd.read_csv('users/users.csv')
    df = AddUser(df)
    print(df)



