from time import sleep

from bin.EmailHandler import EmailHandler
from bin.RequestHandler import RequestHandler

email_handler = EmailHandler()
request_handler = RequestHandler()


class MainFactory:
    def __init__(self):
        pass

    @staticmethod
    def upvote(user_id=123):

        email_blob = email_handler.generate_mail_id()
        md5_email = email_blob[1]
        email = email_blob[0]

        request_handler.vote(email, user_id)

        # Interval
        sleep(8)

        activation_url = request_handler.get_activation_url(md5_email)
        if activation_url:
            up_vote = request_handler.send_get_request(activation_url)

            if up_vote:
                return True
            else:
                return
        else:
            return
