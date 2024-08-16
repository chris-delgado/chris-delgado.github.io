---
layout: post
title: GIOS Projects
image: "/posts/GIOS.png"
tags: [Operating Systems]
---
I took the CS6200 Graduate Introduction to Operating Systems course at Georgia Tech during the Spring 2024 semester. This course taught "...basic operating system abstractions, mechanisms, and their implementations, focusing on operating system support for concurrency (threads) and synchronization, resource management (CPU, memory, I/O), and distributed services. The practical component of the course taught multithreaded programming, inter-process communication, and distributed interactions via RPC." That description from their course page was like Latin to me before I took the class but on reflection it's a pretty spot-on summary.

The bulk of the course was working on three large projects:
1. Implementing a Multithreaded Getfile Server
2. Implementing Proxy and Cache Servers using Inter-Process Communication
3. Implementing a Distributed File System using gRPC

I'll do a quick summary of each project along with "eureka moments" and design decisions that occurred while racking my brain around them.

# Project 1: Multithreading
### Warm-Up
The warm-up phase involved familiarizing oneself with socket programming concepts through practical exercises and resources such as [Beej's Guide to Network Programming](https://beej.us/guide/bgnet/html/split-wide/index.html).

**Eureka Moments**
- Going through the C Warmup Exercise posted in Piazza was a good segue into doing the project proper.
- Reading Chapter 3 [Introducing The Sockets API](https://beej.us/guide/bgnet0/html/split/introducing-the-sockets-api.html#introducing-the-sockets-api) in Beej's Guide to Network Concepts really cleared up the concepts for me.
- Tracking sent bytes and comparing it to file length in a while loop to know when a full file has been transferred.

## Part 1
![Screenshot 2024-08-16 at 5 03 15 AM](https://github.com/user-attachments/assets/94599361-f583-47b9-b8e6-003be1ba27a5)

Part 1 focused on implementing the Getfile protocol, covering the client and server components. For this part, a lot of time was spent getting more to up to speed with C programming fundamentals (thank you [Beej's Guide to C Programming](https://beej.us/guide/bgc/html/split-wide/)), most of which I mention in the eureka moments below.

**Eureka Moments**
- Understanding that a .o file is an intermediate binary that represents complied code before the final linking stage.
- Understanding that a header guard is a preprocessor directive in C that prevents a header file from being included more than once in the same compilation unit.
- Understanding that a callback function is a function that is passed as an argument to another function and are implemented in C using function pointers.
- Understanding how an opaque pointer is used to encapsulate implementation details of a data structure.
- Understanding that `void *` is a generic pointer that can be used to represent a pointer to an object of any data type.
- Realizing I need to free any malloced memory in the clean up functions.
- Setting a timeout for the client socket with the `timeval` struct and `setsockopt`
- Using `snprintf` to populate the request buffer

**Design Decisions & Tradeoffs**
- I dynamically allocated memory for hostname, path string, and some buffers using malloc to handle different lengths.
- I used a fixed buffer size (BUFSIZE) to simplify memory management at the cost of optimizing memory usage.
- I set an arbitrary timeout value of 5 seconds on the client to determine how long to keep the socket available.
- Error handling was included for various points in the code, such as socket creation, binding, accepting connections, memory allocation, sending/receiving data, etc.

## Part 2
![Screenshot 2024-08-16 at 5 03 36 AM](https://github.com/user-attachments/assets/eea1163b-f29a-4d7c-9184-99cb89ad581e)


In Part 2, we used a boss-worker pattern to parallelize multiple file requests between the client and server. This pattern involves a boss thread dividing work into smaller tasks and distributing these tasks to a number of worker threads, in this case via a queue.

**Eureka Moments**
- Realizing that the main thread only enqueues tasks and the workers pop them.
- Understanding condition variables after going through the POSIX threads programming tutorial at https://hpc-tutorials.llnl.gov/posix/
- Using print statements to see exactly when mutexes were being acquired/released and when threads were waiting/being signaled.
- Learning how the extern keyword in C works.
- Getting a file length with `fstat`.
- Using `pread` to read from a file descriptor at a given offset.

**Design Decisions & Tradeoffs**
- I used a global variable count of actioned requests to determine when workers should break from the work loop (this prevented workers from doing work when there was none to do).
- I made sure to call `pthread_cond_signal` before `pthread_mutex_unlock` as failing to unlock the mutex after calling `pthread_cond_signal()` may not allow a matching `pthread_cond_wait()` routine to complete (the tradeoff here is that spurious wake ups could potentially occur, hurting performance).

# Project 2: Inter-Process Communication
## Part 1
![Screenshot 2024-08-16 at 5 03 50 AM](https://github.com/user-attachments/assets/c806a376-c9a5-431e-a087-f0f27ad71302)

In this part of the project, we converted the implementation of the getfile server from Project 1 into a proxy server which would translate GETFILE requests into http requests for other servers. 

To do so, we relied on libcurl, an open source file transfer library. To transfer data, we have the option of using libcurl's "easy" or "multi" interface. The primary distinction between the two is that easy is synchronous (you wait for it to finish before proceeding with additional instructions) and multi is asynchronous (letting you do other things while the transfer is in progress). Part 1 used the easy interface as there was no requirement to do other work during the file transfer.

## Part 2
![Screenshot 2024-08-16 at 5 04 06 AM](https://github.com/user-attachments/assets/bfd7c30f-7bb0-4b46-bf98-292699831419)

In this part of the project, we implemented a cache server that communicates with the proxy via **POSIX shared memory** to share file content. A separate command channel was implemented using a **POSIX message queue** to transmit a request from the proxy to the cache. Synchronization between threads was accomplished using pthreads mutexes and condition variables (learned in project 1) and **POSIX semaphores**.

**Eureka Moments**
- Cache is serving as a server to the proxy's client!
- A steque will maintain a collection of shared memory segments
- Learning how to send an int over shared memory `*(int *)ptr = fd`
- File descriptors are specific to threads/processes (shouldn't send file descriptor to proxy!)
- `sem_wait` blocks if value of the semaphore is already 0
- Calling `sem_close` at the end of the handle_with_cache and simplecached worker functions helps reset them to known states when looping back around
- Using pread instead of read
- Using the proxy boss port as part of the unique ID for semaphores and shared memory segments
- Using sscanf instead of strtok (which is not thread safe). This was the final piece of the puzzle that ended up letting my code pass all Gradescope tests.

**Design Decisions & Trade-offs**
- Using POSIX instead of SysV because the overwhelming majority of students on Slack were doing the same. I would have had much less access to other's knowledge, ideas and mistakes if I had attempted a SysV implementation instead.
- Writing directly to shared memory instead of a buffer or struct placed in shared memory. I thought it was simpler to use the shared memory that way than first filling a buffer and then placing the buffer in shared memory. The trade-off may have been slightly more complicated synchronization with semaphores, but I'm not entirely sure if that's actually true.
- Used a message queue instead of shared memory for the communication channel to the cache because it's thread safe/asynchronous, making sending and receiving messages between threads quite easy. The trade-off there was that I needed to spend time learning the POSIX message queue API in addition to shared memory.
- Used semaphores instead of mutexes for synchronizing reads and writes to shared memory segments. This was arguably simpler than using mutexes, but again time was needed to learn the API. Additionally, I found myself debugging and troubleshooting my semaphore implementation much more than I had done for mutexes and condition variables in project 1.
- Using a steque to hold the shared memory segments and synchronizing access to the them with pthreads mutexes and condition variables. This was done because a very similar implementation was done in Project 1. Therefore, I just needed to apply the same concepts I'd learned previously.
- After threads completed their work, I would have them close shared memory and semaphore file descriptors. This is probably inefficient but helped ensure a stable/known state as the threads would re-open these at the beginning of their loop (e.g., after a message is received in the simplecached.c worker threads).

# Project 3: Remote Procedure Calls
## C++, Protocol Buffers, and gRPC
![Screenshot 2024-08-16 at 5 04 25 AM](https://github.com/user-attachments/assets/62e65f71-402b-4421-8c1f-087ef07b6a7e)

Some C++ standard library methods and objects which were used throughout this project:
- `duration`: Part of the `chrono` library; the `milliseconds` helper type is used to set context deadlines in this project.
- `ifstream`: Input file stream for reading data from files. The related `gcount` method is used to help keep track of the number of characters extracted in a buffered read operation.
- `lock_guard`: Manages ownership of a mutex by automatically locking when created and unlocking when the `lock_guard` instance goes out of scope.
- `map`: Container that stores elements formed by a combination of a key value and a mapped value.
- `mutex`: Synchronization primitive used to protect shared data.
- `ofstream`: Output file stream for writing data to files.
- `seekg`: Used to set the position of the file pointer within an input stream.
- `strcmp`: Compares two strings, returning 0 if equal, a negative value if the first string is less than the second, and a positive value if the first string is greater than the second (e.g., apple is "less" than banana because a comes before b in the alphabet).
- `struct dirent`: Represents a directory entry; used with the `readdir` method to interate through a directory.
- `struct stat`: Used to store information about a file's attributes (e.g., file size, modified time, creation time)
- `system_clock`: Part of the `chrono` library; represents the system clock; most systems use Unix time (time since epoch).
- `time_point`: Part of the `chrono` library; used to represent a point in time.
- `unique_ptr`: Smart pointer used to manage dynamically allocatied objects; essentially replaces the need to use something like malloc/free like we did in C in our previous projects.

Protocol Buffers are Google's language netural, platform-neutral, extensible mechanism for serializing structured data. They allow you to define how you want your data to be structured through a combination of
- A definition language (created in .proto files)
- The code the proto compiler generates to interface with data
- Language-specific runtime libraries
- The serialization format for data that is written to a file (or sent across a network connection)

*See*: [What Are Protocol Buffers](https://protobuf.dev/#what-are-protocol-buffers)

Remote Procedure Calls allow a program to trigger a subroutine to run in a separate address space, often on another computer in a network. The program code appears the same whether calling a local or remote subroutine, hiding the details of remote interaction. This interaction follows a client-server model, where the caller is the client and the executor is the server. RPC serves as a form of inter-process communication, allowing processes with distinct address spaces to communicate, whether on the same host or different hosts.

*See* [Wikipedia Article on Remote Procedure Calls](https://en.wikipedia.org/wiki/Remote_procedure_call)

gRPC is a high-performance, open-source RPC (Remote Procedure Call) framework originally developed by Google. It features a simple service definition by leveraging Protocol Buffers and works across many languages (C++ for this project) and platforms.

*See*: [Introduction to gRPC](https://grpc.io/docs/what-is-grpc/introduction/)

## Part 1
In this part of the project, we built remote procedure calls and message types that fetch, store, list, and get attributes for files on a remote server. 

**Eureka Moments**
- Learning what the layout of a .proto file should look like
- Realizing what using grpc::Status, Channel, StatusCode, etc. mean
- Using ofstream and ifstream to write/read a file in chunks
- Learning about Streaming RPCs
- Learning that service calls need placeholder arguments, even if that argument is a message type that doesn't have any fields
- Learning about dynamic memory allocation using C++ smart pointers
- Sharing protobuf message types between service calls (e.g., using a "GenericResponse" message type in multiple service calls)

**Design Decisions & Trade-offs**
- Initially, I made each RPC method have a corresponding request and response message type. This made it easy to associate methods with message types, but introduced redundancy as I could have created message types which applied to more than one method. Eventually, midway through struggling with part 2, I scrapped this, went back to part 1 and refactored the code to use more generic message types. I think this ultimately helped clear some clutter in my brain and made approaching part 2 easier.
- Used int64 to represent both modified time and creation time. I was thinking perhaps I could have used some more standard C++ time data type, but this was a simple approach that worked.
- I used `std::chrono::system_clock` to get a deadline value; I'm sure there are other ways to do it but this worked fine so I stuck with it.
- I return `StatusCode::OK` at the end of my functions and use if-else branches to return the other required codes. I believe I could just return `status.error_code()` but I wanted to be explicit to aid in debugging and code readability.

## Part 2
In this part of the project, we built a rudimentary distributed file system (DFS).

**Eureka Moments**
- Learning that inotify provides a way to monitor filesystem events.
- Learning from Slack that I can use a map to hold a filename (as a key) and client ID as a value to map which clients have a lock on which files.
- `std::lock_guard` automatically releases the lock when it goes out of scope.

**Design Decisions & Trade-offs**
- I briefly explored using the `AddMetadata` function within the grpc `ClientContext` class to pass information such as crc checksum and client ID to the server, but I decided to add fields to .proto message types instead since I already knew how to pass information back and forth using them.
- I also looked into using the `shared_mutex` synchronization primitive for the server since that header file is included there, but I couldn't figure out a use case for it that a standard mutex with a lock guard couldn't handle, which was well enough since the latter is a simple yet effective tool.
- Asynchronous file comparisons to determine whether a fetch or store needed to occur used CRC checksums instead of modified time.
- I maintained a mapping of file names and client IDs holding write locks on those files. This made it fairly simple to manage write locks. However, storing locks in-memory like this could potentially have scalability issues if there are a very large number of files or concurrent clients.

# Final Thoughts
I don't have a computer science background. My undergrad years ago was in Electrical Engineering and my work has been primarily IT support. I found the projects very interesting/rewarding/fun. They were difficult and I needed to spend at least a couple of hours each day for a few weeks to get them working in Gradescope. Reminded me of how long it takes me to learn the patterns of some bosses in Soulsborne games.
