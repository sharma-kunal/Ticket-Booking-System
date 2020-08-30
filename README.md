<div align="center">
<p>
  <img src="./images/api.png" width="150">
</p>
</div>

# Ticket Booking API
![Made with Python](https://img.shields.io/badge/Made%20with-Python-blueviolet?style=for-the-badge&logo=python)   ![Built with Love](https://img.shields.io/badge/Built%20With-%E2%99%A5-critical?style=for-the-badge&logo=ko-fi) ![Open Source Love](https://img.shields.io/badge/Open%20Source-%E2%99%A5-red?style=for-the-badge&logo=open-source-initiative)

A Ticket Booking System API made using `Django` (Python-based free and open-source web framework)

## Problem Statement

You have to design a REST interface for a movie theatre ticket booking system. It should support the following business cases:

- [x] An endpoint to book a ticket using a user’s name, phone number, and timings.
- [x] Maximum 20 tickets can be booked for a particular time.
- [x] An endpoint to update a ticket timing.
- [x] An endpoint to view all the tickets for a particular time.
- [x] An endpoint to delete a particular ticket.
- [x] An endpoint to view the user’s details based on the ticket id.
- [x] Mark a ticket as expired if there is a diff of 8 hours between the ticket timing and current
- [x] Delete all the tickets which are expired automatically.
- [x] Write the tests for all the endpoints.

## RESTful Structure of API

| Endpoint  |      HTTP Method      |  CRUD Method |  Result  |
|----------|-------------|------|-------|
| api/tickets |  GET | READ |   Get all tickets   |
| api/tickets/{id} |    GET   |   READ | Get a ticket using ID |
| api/tickets?date={date}&time={time} | GET |    READ |    Get all tickets with specified ID    |
| api/tickets | POST  | CREATE  | Book a Ticket |
| api/tickets/{id} | PUT | UPDATE  | Update a ticket |
| api/tickets/{id} | DELETE  | DELETE | Delete a ticket |

#### Additional Features of API:

- **Every 5 minutes** - Mark ticket as expired if there is a diff of 8 hours between the ticket time and current time
- **Every 10 minutes** - Deleting all the Expired Tickets Automatically
- **Test Cases** - Test Driven RESTful API Development


## DataBase Fields

| Name  | Phone number  | Date  | Time  | Expired |
|-------|---------------|-------|-------|---------|

## Operations Supported by API

- An endpoint to view all the Tickets.

```
GET
/api/tickets
```

![GET ALL TICKETS](https://github.com/sharma-kunal/Ticket-Booking-System/blob/master/images/Get1.png)

- An endpoint to view the user’s details based on the ticket id.

```
GET
/api/tickets/{id}
```

![GET TICKET BY ID](https://github.com/sharma-kunal/Ticket-Booking-System/blob/master/images/Get2.png)

- An endpoint to view all the tickets for a particular time.

There are 3 functionalities for getting the tickets for a specified Timing, which are:

1. To view the tickets for a specified Date and Time

```
GET
/api/tickets?date={date}&time={time}
```

![GET TICKET BY DATE AND TIME](https://github.com/sharma-kunal/Ticket-Booking-System/blob/master/images/Get3_date&time.png)

2. To view the tickets for a specified Date

```
GET
/api/tickets?date={date}
```

![GET TICKETS BY DATE](https://github.com/sharma-kunal/Ticket-Booking-System/blob/master/images/Get3_date.png)

3. To view the tickets for a specified Time

```
GET
/api/tickets?time={time}
```

![GET TICKETS BY TIME](https://github.com/sharma-kunal/Ticket-Booking-System/blob/master/images/Get3_time.png)

- An endpoint to book a ticket using a user’s name, phone number, and timings.

```
POST
/api/tickets
```

![POST TICKET](https://github.com/sharma-kunal/Ticket-Booking-System/blob/master/images/Post.png)

- An endpoint to update a ticket timing.

```
PUT
/api/tickets/{id}/
```

![UPDATE TICKET](https://github.com/sharma-kunal/Ticket-Booking-System/blob/master/images/Put.png)

- An endpoint to delete a particular ticket

```
DELETE
/api/tickets/{id}/
```

![DELETE TICKET](https://github.com/sharma-kunal/Ticket-Booking-System/blob/master/images/Delete.png)

## Additional Features

- Mark a ticket as expired if there is a diff of 8 hours between the ticket timing and current time.

    Added a Cron Job to run at the interval of 5 minutes To Mark a Ticket as Expired if the Difference is greater than or equal to 8 hours.

    ##### MARK TICKETS AS EXPIRED CRON FUNCTION

    ![Cron function to mark expired](https://github.com/sharma-kunal/Ticket-Booking-System/blob/master/images/cron_function.png)

    ##### CRON JOB (Specifying CRON FUNCTION to run every 5 minutes)

    ![Cron Job to mark expired](https://github.com/sharma-kunal/Ticket-Booking-System/blob/master/images/cron_job_time.png)


- Delete all the tickets which are expired.

  Added a Cron Job to run at the interval of 10 minutes to Delete all the Expired Tickets.

  ##### CRON FUNCTION TO DELETE EXPIRED TICKETS

  ![Cron function to delete expired tickets](https://github.com/sharma-kunal/Ticket-Booking-System/blob/master/images/delete_cron_job.png)

  ##### CRON JOB (Specifying the CRON FUNCTION to run every 10 minutes)

  ![Cron Job to delete expired ticket](https://github.com/sharma-kunal/Ticket-Booking-System/blob/master/images/delete_cron_job_time.png)


  To understand the working of the Cron Jobs

  - Making Ticket Expired
  - Deleting Expired Tickets

  Watch the below video,

  [![Image](https://github.com/sharma-kunal/Ticket-Booking-System/blob/master/images/video_thumnail.jpg)](https://www.youtube.com/watch?v=MOvikDJyzAA&t=41s)

## Testing the API (Writing Test Cases)

- To run the `test cases`, use the command

```
python manage.py test
```

To write some more test cases for the API, head over to the file `API/test.py`. It's the file containing all the test cases for the API.

![TEST RUN SUCCESSFUL](https://github.com/sharma-kunal/Ticket-Booking-System/blob/master/images/test_cases.png)


## Installation and Running

- Run the command

```
pip install -r requirements.txt
```

to install all the required dependencies.

- Now run the command

```
python manage.py runserver
```

To run the Django Server on your localhost.

**NOTE:** If the default port is busy, you can run the server on any other port using the command,

```
python manage.py runserver localhost:{port number}
```

## Django Admin

You can see the data inside the database in the Django Admin Panel.

Just go to the link

```
localhost:{port number}/admin
```

and provide the Username and Password Details. (For simplicity I have already created a SuperUser)

| Username  | Password |
|-------|--------|
| test  | test@123 |
