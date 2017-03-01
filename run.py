# ------------------ Credits ----------------------- #
# Idea and exploit: Boxxy                            #
# Code, performance and functionality: Bermdingetje  #
# -------------------------------------------------- #
# Requirements: python2.7 and requests.

from bin import Handler
_Handler = Handler.MainFactory()


def upvote():
    user_id = raw_input("User ID?:")
    user_id = int(user_id)
    i = 0
    while True:
        status = _Handler.upvote(user_id=user_id)
        if status:
            print 'And another upvote!'
            i += 1
            print 'We are currently at {0} successful upvotes.'.format(i)
        else:
            print 'Seems like we can\'t connect, this one is lost...'


if __name__ == '__main__':
    upvote()
