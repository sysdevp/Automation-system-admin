from aws import AWS_data

from mails import mail


if __name__ == '__main__':
    
    try:

        AWS_data()

        mail()

    except Exception as e:

        print(e)

