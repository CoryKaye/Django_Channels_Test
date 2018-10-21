from django.conf import settings

MSG_TYPE_VOTE = 0; # For users voting
MSG_TYPE_QUES = 1; # For teacher to broadcast question
MSG_TYPE_JOIN = 2; # For when a user joins
MSG_TYPE_ANSW = 3; # For sending back the answer to the question

MESSAGE_TYPES_CHOICES = getattr(settings, 'MESSAGE_TYPES_CHOICES', (
    (MSG_TYPE_VOTE, 'VOTE'),
    (MSG_TYPE_QUES, 'QUESTION'),
    (MSG_TYPE_JOIN, 'JOIN'),
    (MSG_TYPE_ANSW, 'ANSWER')))

MESSAGE_TYPES_LIST = getattr(settings, 'MESSAGE_TYPES_LIST',
        [MSG_TYPE_VOTE,
         MSG_TYPE_QUES,
         MSG_TYPE_JOIN,
         MSG_TYPE_ANSW])

