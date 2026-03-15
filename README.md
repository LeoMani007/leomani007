1.Multi-Threaded TCP Chat System
  A real-time, multi-client chat application built using Python, Sockets, and Threading. This project demonstrates the fundamentals of network programming and concurrent execution, allowing multiple clients to communicate simultaneously through a central server.

2.Features
    Multi-Client Support: Handles multiple simultaneous connections using Python's threading module.

    Real-Time Communication: Implements a non-blocking architecture so users can send and receive messages at the same time.

    Broadcast Logic: Messages sent by one user are automatically broadcast to all other connected participants.

    Graceful Disconnection: Handles client exits (e.g., typing 'exit' or 'quit') and unexpected socket errors without crashing the          server.
    Technology Stack:
    Language: Python 3.x

3.Libraries

    socket: For low-level network communication (TCP/IP).

    threading: To manage concurrent client sessions.

4.Project Structure
    chat.py: The server-side script that listens for connections and broadcasts messages.

    client.py: The client-side script that connects to the server and handles user input/output.

