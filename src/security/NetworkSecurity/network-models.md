# The OSI Model

**NOTES**

*(Open Systems Interconnection(OSI) Model)*

In order to send information from one computer to another & for that computer to receive and understand information, there exists a set of rules or standards for common process

This standard is called a network model

# The TCP/IP Model

## Application Layer

1. The upper three layers of the OSI model(application, presentation, session) define functions of the TCP/IP application layer
2. The application layer provides the  interface between the applications used to communicate and the underlying network over which messages are transmitted
3. some of the most widely known application layer protocols are *HTTP,FTP,TFTP,IMAP*

## Presentation Layer

**Three primary functions**-

1. Formatting, or presenting data at the source device into compatible format for receipt by the destination device
2. Comprising data in a way that can be decompressed by the destination device
3. Encrypting data for transmission and decrypting data upon receipt

## Session Layer

**session layer functions**-

1. creates, maintains dialogue between source and destination application
2. handles exchange of informatino to initiate dialogue, keep active, and restart sessions that are disrupted or idle for a very long period of time

## Transport layer
1. Tracking individual conversations
2. Segmenting data and reassembling segments
3. Adds header information
4. identifies, separates, manages multiple conversations
5. Uses segmentation and multiplexing to enable different common conversatinos to be interleaved on the same network

*TCP->connection oriented*
