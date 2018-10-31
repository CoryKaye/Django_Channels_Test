### NOTE: THIS IS A TEST. EXPECT CHANGE.

##### This chat application is a test based off of the one found here - https://channels.readthedocs.io/en/latest/tutorial/

The chat application is a test to mess around with channels/websockets.

## You Will Need To Do The Following:
1. Run `python3 manage.py migrate` to make sure WS works as the DJango session framework needs the database.
2. Go to this address, represents teachers view: `http://127.0.0.1:8000/chat/squirtle/`
3. Open a seperate tab.
4. In the new tab, represents student view, go to: `http://127.0.0.1:8000/chat/join/squirtle/`

For teacher view you can:
- Send Messages: Represents questions
- Receive Votes: Receive votes from students, counter counts

For student view you can:
- Receive Messages: Represents getting a question
- Send Votes: Send votes to the teacher
